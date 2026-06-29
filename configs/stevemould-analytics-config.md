---
type: analytics-config
schema_version: 1.0
client: Steve Mould
maintained_by: NaaShika / Ziggurat
update_cadence: Quarterly, or when newsletter or Patreon strategy materially changes
updated: 2026-06-29
---

# Steve Mould Analytics Config

*Strategic intelligence + detection rules for the monthly analytics engine. Conforms to
client-config-TEMPLATE schema 1.0. Read in full before writing any insight.*

---

## 1. Identity

```yaml
client_name: Steve Mould
client_slug: stevemould
brand_accent_hex: #1E6FCC
output_filename: SteveMould_[MonthYear]_Performance.xlsx
platforms_active: [instagram, facebook]
```

*Note: brand_accent_hex is a working estimate (Steve uses blue heavily in thumbnails/branding). Confirm with NaaShika.*

---

## 2. Brand & audience

**Who the client is:** Steve Mould is a science communicator and YouTube creator known for rigorous,
visually-driven explanations of physics and mathematics. His authority comes from genuine scientific
understanding and a production approach that prioritises accuracy over spectacle. He has a deep
production pipeline — ideation, prototyping, testing, iteration, final production — that generates
a large volume of high-value insight that his audience rarely sees. He is protective of scientific
integrity and cautious about content that could misrepresent his explanations.

**Brand voice:** Precise, curious, and accessible — explains complex phenomena clearly without
dumbing them down. Respects the audience's intelligence. Dislikes unnecessary social media noise
and content that exists purely to game algorithms.

**The audience:** Science and mathematics enthusiasts across a broad age range. Intellectually
curious. They value accuracy and the "aha moment" that comes from a well-explained phenomenon.
They are more likely to engage deeply with a single high-quality post than to follow an account
producing high-volume social filler.

**What they sell:** Patreon (approximately 2,500 members, approximately $1,500/month) for
direct support and community access. Newsletter in development — currently approximately 90%
complete and awaiting launch activation. Potential future products (TBC).

---

## 3. Strategy & funnel

**What social is for:** Social is the attention layer for an ecosystem that mostly already exists
but is not yet fully wired together. The funnel is:

**Attention (social) → YouTube video → Newsletter subscription → Patreon membership**

Short-form social should drive to YouTube, and YouTube should drive to newsletter and Patreon.
The strategic priority during this phase is activating the newsletter and establishing a reliable
flow from social attention into the deeper ecosystem.

**The conversion mechanic:** Link in bio is the primary CTA — directing audiences to YouTube,
newsletter sign-up, or Patreon as appropriate. There is no comment-trigger / auto-DM mechanic
in use. Short-form clips are extracted verbatim from YouTube transcripts (to preserve scientific
accuracy) and should direct audiences back to the full video. Posts with no CTA are pure
awareness plays; useful for algorithm reach but do not move the funnel.

---

## 4. Platform roles

### Instagram
- **Primary function:** Awareness and curiosity-triggering. Convert short-form attention into
  YouTube views, and from there into newsletter signups and Patreon consideration.
- **What good looks like:** Saves above 150 = content sticky enough to bookmark · Shares above
  50 = content compelling enough to spread beyond current followers · Link clicks via bio = funnel
  working · Follows gained on explanation content = new audience entering the ecosystem.
- **Format expectations:** Reels drive discovery (views, reach, follows) — the primary short-form
  format · Carousels can work for step-by-step explanations or multi-panel visual sequences ·
  Static images are weaker on reach but can anchor a single striking visual or data point.
- **What to flag as underperformance:** Low saves on explanation content (hook or clarity problem)
  · No-CTA posts as a sustained pattern (missed newsletter/Patreon traffic) · High reach with low
  saves or shares (audience not finding the content bookmark-worthy — quality or hook issue).

### Facebook
- **Primary function:** Reach and brand awareness. Supplementary surface only. Do not hold to
  Instagram benchmarks.
- **What good looks like:** Views above 8,000 = strong reach · Reactions above 50 = meaningful
  engagement · Link clicks above 15 = active audience directing.
- **Format expectations:** Video/Reel outperforms photo content on all metrics consistently ·
  Photo posts have a secondary visibility role only.
- **What to flag:** Sustained low link clicks (audience not being directed into the funnel) ·
  Photo-heavy months structurally underperforming — flag as format imbalance.

---

## 5. Detection rules

### 5a. CTA detection

**Instagram:**
| Column | Logic |
|---|---|
| Trigger Word | Extract the first ALL-CAPS word (2+ letters) following "Comment"/"comment" in the description. Show the word literally. Blank if none. *Note: Steve Mould does not currently use the comment-trigger mechanic — this column will typically be blank.* |
| Link in Bio | ✓ if description contains "link in bio", "linktree", or "link in our bio" (case-insensitive). Else blank. |
| No CTA | ✓ if both Trigger Word and Link in Bio are blank. Else blank. |

**Facebook:**
| Column | Logic |
|---|---|
| Link in Comments | ✓ if the word "comment" appears anywhere in Title or Description (case-insensitive). Else blank. |

### 5b. Special content types

```yaml
special_content: []
```

*No special content types currently defined. If the verbatim-transcript short-form system
produces a distinct post type (e.g. "From the archive" clips), add a detection rule here.*

---

## 6. Metrics to score

**Instagram (score these):** Views, Reach, Likes, Comments, Shares, Saves, Follows.

**Facebook (score these):** Views, Reach, Reactions, Comments, Shares, Total clicks, Link clicks.
- *Exclude:* `Reactions, comments and shares` — a lump sum of metrics already scored above.

---

## 7. Benchmarks

None yet — this month establishes the baseline.

*Update this section after the first monthly crunch with actual averages from the data.*

---

## 8. Metric strategic tiers

- **Tier 1 — highest strategic value:** Saves (IG — the clearest signal that this audience found
  the content worth returning to; science content that explains well gets bookmarked) · Link clicks
  (FB — best proxy for YouTube/newsletter/Patreon traffic) · Shares (both — organic spread to
  new scientifically curious audiences).
- **Tier 2 — important context:** Views (reach/top-of-funnel) · Reach (unique accounts) ·
  Follows (IG — new audience entering the ecosystem, the primary growth metric this phase) ·
  Likes/Reactions (passive positive signal).
- **Tier 3 — supporting:** Comments (IG — engagement depth when content sparks a question) ·
  Total clicks (FB) · Profile visits (IG — curiosity signal).

---

## 9. Insight patterns

**What Worked — always look for:**
- Did short-form clips that deliver a single clear "aha moment" outperform broader or vaguer
  content? Track this — it is the core of Steve's content strength.
- Did verbatim-transcript clips (exact words from YouTube) outperform paraphrased or
  summary-style content? This validates the transcript-extraction system.
- Did posts with explicit newsletter or Patreon CTAs drive higher link clicks than generic
  link-in-bio posts?
- Did Reels dominate discovery metrics (views, reach, follows) vs. other formats?

**What Didn't Work — always look for:**
- Content that feels like social media filler (generic science trivia, trend-chasing) — flag as
  off-brand and likely underperforming.
- No-CTA posts as a sustained pattern — flag as missed newsletter/Patreon traffic.
- High reach with low saves or shares — suggests the hook is working but content depth is not
  delivering enough value to bookmark or spread.
- Duplicate posts or publishing errors — flag immediately.

**What We Do About It — standing recommendations to reassess each month:**
1. Is the newsletter now live? If yes — is the link-in-bio directing to sign-up? If no —
   flag the activation gap every month until it resolves.
2. Is the verbatim-transcript short-form system producing regular content? If output is
   inconsistent, flag as a pipeline issue.
3. Is the link-in-bio pointing to the right destination for the current strategic priority
   (newsletter sign-up, Patreon, or latest YouTube video)?
4. Are Follows trending upward month on month? This is the primary ecosystem growth signal.

---

## 10. Strategic phase

**Current phase — Ecosystem activation (through late 2026):** The core strategic challenge for
Steve Mould is not content creation — it is activation and connection. The newsletter is ~90%
built but not yet live. The Patreon has ~2,500 members but is underutilised. Social content
exists but there is no reliable system connecting attention → newsletter → Patreon. The current
phase is about wiring these pieces together, not building new ones.

**What this means for monthly insights:**
- Every month, flag whether the newsletter is live and whether social is driving to it.
- Track Follows as the primary leading indicator of ecosystem growth.
- Flag any month where No-CTA posts dominate — these represent wasted funnel opportunity during
  a phase when activating the ecosystem is the priority.
- Note whether short-form volume is consistent — irregular posting is a structural problem for
  funnel building.

**Upcoming phases (for context):**
- **Newsletter launch (timing TBC):** When live, social should pivot to explicit newsletter CTAs.
  The primary link-in-bio destination should become the newsletter sign-up page.
- **Patreon activation:** If the "Steve's Notepad" concept (behind-the-scenes production content)
  is activated, Patreon becomes a more explicit conversion target and insight patterns should
  track Patreon-directed CTAs specifically.

---

## 11. Glossary

- **Steve's Notepad:** A proposed Patreon content concept — behind-the-scenes access to Steve's
  production pipeline (experiments, thought processes, failures). Not yet live as of June 2026.
- **Verbatim-transcript clips:** Short-form social content extracted directly from Steve's YouTube
  transcripts (his exact words, no paraphrasing). Designed to preserve scientific accuracy and
  reduce the sign-off bottleneck.
- **Patreon:** Steve's direct-support platform. Approximately 2,500 members, approximately
  $1,500/month. Currently underutilised — key strategic growth target.
- **Newsletter:** Steve Mould's newsletter product, built on Kit. Approximately 90% complete as
  of June 2026. Not yet live.
- **No CTA post:** An Instagram post with neither a trigger word nor a link-in-bio prompt.
  Awareness only — does not move traffic to newsletter or Patreon. A significant flag during
  ecosystem activation phase.
- **NaaShika:** Ziggurat SMA lead for Steve Mould.

---

## Related Files
- [[analytics-engine-SKILL]]
- [[client-config-TEMPLATE]]
- [[clients]]
- [[Steve Mould Creative Context]]

---
*Config schema 1.0 — runs against analytics-engine-SKILL v2.0.*
