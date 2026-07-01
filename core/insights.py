"""
insights.py — Claude-powered insight generation for the analytics engine.

Generates the written sections (What Worked, What Didn't Work, What We Do About It,
Executive View, Recommended Focus Areas) using scored post data + the client config.

Returns None gracefully if ANTHROPIC_API_KEY is not set or the call fails — the
workbook builds without insight text in that case (shells are left for the analyst).
"""
import json
import os


_EXEC_LENSES = [
    "1. The creative formula",
    "2. CTA and conversion mechanics",
    "3. Platform differentiation",
    "4. Volume vs quality",
    "5. Strategic context",
]

_RESPONSE_SCHEMA = """{
  "What Worked": [
    {"label": "short title", "body": "1-3 sentence explanation"},
    ... (4 items total)
  ],
  "What Didn't Work": [
    {"label": "short title", "body": "1-3 sentence explanation"},
    ... (3 items total)
  ],
  "What We Do About It": [
    {"label": "short title", "body": "1-3 sentence actionable recommendation"},
    ... (4 items total)
  ],
  "Executive View": [
    {"lens": "1. The creative formula", "body": "2-4 sentence lens analysis"},
    {"lens": "2. CTA and conversion mechanics", "body": "..."},
    {"lens": "3. Platform differentiation", "body": "..."},
    {"lens": "4. Volume vs quality", "body": "..."},
    {"lens": "5. Strategic context", "body": "..."}
  ],
  "Recommended Focus Areas": [
    {"label": "short title", "body": "1-3 sentence recommendation"},
    ... (3-4 items total)
  ]
}"""


def _summarise_tables(tables: dict) -> str:
    """Build a concise text summary of scored post data for the prompt."""
    try:
        import pandas as pd
    except ImportError:
        return "(data unavailable)"

    lines = []
    platform_labels = {
        "instagram": "Instagram",
        "facebook": "Facebook",
        "stories": "Stories",
        "youtube_shorts": "YouTube Shorts",
        "youtube_longform": "YouTube Long-form",
    }

    for key, df in tables.items():
        if df is None or len(df) == 0:
            continue
        label = platform_labels.get(key, key.title())
        lines.append(f"\n## {label} ({len(df)} posts)")

        title_col = "Video title" if "Video title" in df.columns else "Description"
        score_col = "Total Score" if "Total Score" in df.columns else None

        if score_col and score_col in df.columns:
            avg = df[score_col].mean()
            lines.append(f"Average total score: {avg:.1f}")

        # Top performers
        top = df.head(min(5, len(df)))
        lines.append("Top performers (by rank):")
        for _, row in top.iterrows():
            title = str(row.get(title_col, ""))[:80].strip()
            score = int(row[score_col]) if score_col else "?"
            fmt = row.get("Post type", row.get("Format", ""))
            lines.append(f"  • [{score}pts] {title}" + (f" ({fmt})" if fmt else ""))

        # Bottom performers
        if len(df) > 5:
            bottom = df.tail(min(3, len(df) - 5))
            lines.append("Bottom performers:")
            for _, row in bottom.iterrows():
                title = str(row.get(title_col, ""))[:80].strip()
                score = int(row[score_col]) if score_col else "?"
                lines.append(f"  • [{score}pts] {title}")

        # Platform-specific aggregate stats
        for col in ("Views", "Likes", "Saves", "Follows", "Comments",
                    "Watch time (hours)", "Subscribers"):
            if col in df.columns:
                try:
                    import pandas as _pd
                    total = _pd.to_numeric(df[col], errors="coerce").sum()
                    lines.append(f"Total {col}: {total:,.0f}")
                except Exception:
                    pass

    return "\n".join(lines) if lines else "(no scored data available)"


def _build_prompt(cfg, tables: dict, month: str) -> str:
    data_summary = _summarise_tables(tables)

    return f"""You are a senior social media strategist writing the insight sections for a monthly performance report.

## Client context
{cfg.raw}

## Month
{month}

## Scored post data
{data_summary}

## Your task
Write all five insight sections for this report. Be specific — reference actual post titles, formats, scores, and metric patterns from the data above. Connect insights to the strategic goals and brand voice described in the client config.

Return ONLY a single valid JSON object matching this exact schema (no markdown fences, no commentary):

{_RESPONSE_SCHEMA}

Rules:
- Each "body" must be 1-4 sentences, specific to this client and this month's data.
- "What Worked" — 4 items: patterns and posts that over-performed.
- "What Didn't Work" — 3 items: under-performance patterns, not just low-scoring posts.
- "What We Do About It" — 4 items: concrete, actionable month-ahead recommendations.
- "Executive View" — exactly 5 items, one per lens, using the exact lens strings provided.
- "Recommended Focus Areas" — 3-4 items: highest-leverage priorities for the next month.
- Write for a marketing director audience: direct, strategic, no fluff.
"""


def generate_insights(cfg, tables: dict, month: str) -> tuple[dict | None, str]:
    """Call Claude to generate the written insight sections.

    Returns (insights_dict, note) where note describes success or failure.
    insights_dict is None if the API key is absent or the call fails — the workbook
    builds with shell tabs in that case.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None, "No Claude insights (ANTHROPIC_API_KEY not set)."

    try:
        import anthropic
    except ImportError:
        return None, "No Claude insights (anthropic SDK not installed)."

    prompt = _build_prompt(cfg, tables, month)

    try:
        client = anthropic.Anthropic(api_key=api_key)
        with client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=8000,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            msg = stream.get_final_message()

        # With adaptive thinking the response has thinking blocks followed by a text block.
        # Collect the last text block (the one that contains the JSON).
        raw_text = ""
        for block in msg.content:
            if getattr(block, "type", None) == "text" and hasattr(block, "text"):
                raw_text = block.text

        # Strip markdown fences if Claude added them despite instructions
        stripped = raw_text.strip()
        if stripped.startswith("```"):
            stripped = stripped.split("\n", 1)[1] if "\n" in stripped else stripped
            stripped = stripped.rsplit("```", 1)[0].strip()

        data = json.loads(stripped)
        return _normalise(data), "Claude insights generated."

    except Exception as exc:
        return None, f"Claude insights failed: {type(exc).__name__}: {exc}"


def _normalise(data: dict) -> dict:
    """Convert the JSON dict (label/body keys) into lists of (label, body) tuples."""
    result = {}

    for section in ("What Worked", "What Didn't Work", "What We Do About It",
                    "Recommended Focus Areas"):
        items = data.get(section, [])
        result[section] = [(item.get("label", ""), item.get("body", "")) for item in items]

    # Executive View uses "lens" instead of "label"
    ev_items = data.get("Executive View", [])
    result["Executive View"] = [(item.get("lens", ""), item.get("body", "")) for item in ev_items]

    return result
