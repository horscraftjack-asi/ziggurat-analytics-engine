---
type: analytics-config
schema_version: 1.0
client: Xyla
maintained_by: Jack Horscraft / Ziggurat
update_cadence: Monthly, or after significant changes to content strategy
updated: 2026-06-29
---

# Xyla Analytics Config

*Xyla Foxlin — STEM creator, maker, pilot, aerospace content. Config covers Facebook and
Instagram. No auto-DM mechanic currently in use on Instagram.*

---

## 1. Identity

```yaml
client_name: Xyla
client_slug: xyla
brand_accent_hex: #5B3A7A
output_filename: Xyla_[MonthYear]_Performance.xlsx
platforms_active: [instagram, facebook]
```

---

## 2. Brand & audience

**Who the client is:** Xyla Foxlin is a STEM/maker creator — aerospace engineer, licensed
pilot, and builder — whose content spans hands-on making, physics explainers, aviation, and
personal projects. Her authority comes from genuine expertise: she actually builds the
things she talks about and holds the credentials to back up the science. Her Miss America
background adds an unusual dimension of personality-led accessibility to technical content.

**Brand voice:** Enthusiastic, technically credible, personally warm. She explains hard
things by doing them, not just describing them. The personality is the hook; the expertise
is the retention.

**The audience:** STEM-interested generalist viewers — people who liked science at school,
watch engineering content casually, and respond to the combination of competence and
charisma. Skews toward science/aviation/maker enthusiasts. The Facebook audience in
particular is large and monetisation-eligible, suggesting a broad reach beyond a niche core.

**What they sell:** No current owned product in active promotion. Facebook content
monetisation (in-stream ads) is the primary revenue signal tracked here. Instagram is a
secondary engagement and audience-building platform.

---

## 3. Strategy & funnel

**What social is for:** At present, Facebook is primarily a **monetisation platform** —
Xyla earns via Facebook's in-stream ad monetisation on video content. The strategic goal is
maximising monetisation-eligible views (views that reach the in-stream ad threshold) rather
than conversions to an owned product. Instagram serves audience engagement and reach, with
lower direct monetisation relevance currently.

**The conversion mechanic:** No comment-trigger or auto-DM mechanic in use. The primary
metric of commercial value on Facebook is `Approximate content monetisation earnings` and
the views that drive it. On Instagram, saves and shares are the strongest signals of content
health in the absence of a conversion mechanic.

---

## 4. Platform roles

### Instagram
- **Primary function:** audience engagement and content reach. No active conversion mechanic.
- **What good looks like:** Saves above 200 = strong intent signal · shares above 100 =
  broadcast-worthy content · reels driving views into the tens of thousands for discovery.
- **Format expectations:** Reels for reach and discovery · carousels for depth and saves.
  Xyla's account currently splits roughly 50/50 between the two.
- **What to flag as underperformance:** reels with views well below the monthly median ·
  carousels with low saves relative to reach · any post with zero engagement signals.

### Facebook
- **Primary function:** monetisation via in-stream ads on video content. The primary
  commercial channel. Photos do not earn meaningful monetisation revenue — video is
  everything here.
- **What good looks like:** Video RPM (earnings per 1,000 views) above $0.15 = healthy ·
  monthly video views above 3M = strong monetisation base · individual video earnings above
  $50 = standout post.
- **Format expectations:** Videos drive all monetisation. Photos contribute reach and
  engagement but earn nothing meaningful via in-stream ads. Volume of video posts matters —
  more qualifying videos = more monetisation surface.
- **What to flag:** RPM collapse (earnings drop without a corresponding views drop — signals
  a monetisation eligibility or content-type issue, not a reach issue) · views collapse
  (reach problem, not monetisation rate) · months where video volume drops below 15 posts ·
  any month where photo posts outnumber video posts.

---

## 5. Detection rules

### 5a. CTA detection

**Instagram:**
| Column | Logic |
|---|---|
| Link in Bio | ✓ if description contains "link in bio", "linktree", or "link in our bio" (case-insensitive). Else blank. |
| No CTA | ✓ if Link in Bio is blank. Else blank. |

*No trigger-word mechanic in use. Trigger Word column omitted.*

**Facebook:**
| Column | Logic |
|---|---|
| Link in Comments | ✓ if the word "comment" appears anywhere in Title or Description (case-insensitive). Else blank. |

### 5b. Special content types

```yaml
special_content: []
```

*No special content types currently. If Facebook monetisation-ineligible posts (e.g. shares,
crossposted content) appear regularly, consider splitting them out in a future config update.*

---

## 6. Metrics to score

**Instagram (score these):** Views, Reach, Likes, Comments, Shares, Saves, Follows.

**Facebook (score these):** Views, Reach, Reactions, Comments, Shares, Total clicks, Link clicks.
- *Exclude:* `Reactions, comments and shares` — a lump sum of metrics already scored above.
- *Note:* `Approximate content monetisation earnings` is NOT scored in the rank-order system
  (it's too skewed by a small number of viral posts to be a fair ranking signal) but MUST be
  included as a raw column and called out explicitly in the insight sections.
- **Extra columns (facebook):** Earnings: Approximate content monetisation earnings

**Stories:** Not currently active for this client.

---

## 7. Benchmarks

*Based on April–June 2026 data. April was an outlier high month; May–June are more representative
of the current baseline. Update after each monthly crunch.*

### Facebook feed (as of Q2 2026)
| Metric | Monthly baseline | Strong | Exceptional |
|---|---|---|---|
| Video views/month (total) | ~3–6M | >6M | >10M |
| RPM (earnings per 1,000 views) | ~$0.05–0.21 | >$0.15 | >$0.20 |
| Monthly earnings total | ~$260–440 | >$600 | >$1,000 |
| Individual video earnings | ~$5–15 | >$50 | >$200 |
| Video posts/month | ~21–22 | — | — |

### Instagram feed (as of Q2 2026)
| Metric | Monthly baseline | Strong | Exceptional |
|---|---|---|---|
| Posts/month | ~15 | — | — |
| Saves per post | TBC — establish from first monthly crunch | — | — |
| Views per reel | TBC | — | — |

*Instagram benchmarks not yet established from monthly data — this crunch establishes the
baseline.*

---

## 8. Metric strategic tiers

- **Tier 1 — highest strategic value:** Approximate content monetisation earnings (FB — the
  commercial output) · Video views (FB — the monetisation driver) · RPM trend (derived —
  calculated in insight writing, not scored).
- **Tier 2 — important context:** Reach (both) · Saves (IG — best engagement signal without
  a conversion mechanic) · Shares (both — organic amplification).
- **Tier 3 — supporting:** Likes/Reactions · Comments · Follows · Total clicks.

---

## 9. Insight patterns

**What Worked — always look for:**
- Which video topics drove the highest individual earnings? (Aviation, maker builds, physics
  explainers — which category is currently monetising best?)
- Did any video significantly outperform on RPM as well as raw views? (This is the ideal —
  reach AND monetisation rate both strong.)
- Did Instagram saves or shares signal content worth repurposing or amplifying on Facebook?

**What Didn't Work — always look for:**
- RPM collapse: a month where views held but earnings dropped sharply. This is the key
  failure mode to flag — it signals monetisation-ineligible content, content-type changes,
  or a platform policy shift rather than a reach problem.
- Views collapse: a month where both views and earnings dropped. This is a reach/content
  problem — different diagnosis, different fix.
- High photo-to-video ratio on Facebook. Photos earn nothing via in-stream; a month with
  heavy photo volume is a missed monetisation opportunity.
- Very low per-video earnings spread — if no individual video earns above $20, the content
  may not be generating enough watch time to trigger monetisation at scale.

**What We Do About It — standing checks each month:**
1. Calculate RPM (total earnings ÷ total video views × 1,000). Is it above $0.15? If not,
   flag whether the issue is views or rate.
2. Is video volume consistent (20+ posts/month)? If it drops, flag it.
3. Are there any zero-earnings videos with significant views? These may be ineligible for
   monetisation — flag the content type.
4. Instagram: are saves tracking upward month on month? In the absence of a conversion
   mechanic, saves are the clearest signal of content quality.

---

## 10. Strategic phase

**Current phase — Facebook monetisation baseline (ongoing):** The immediate priority is
understanding and stabilising Facebook earnings, which showed significant volatility in
Q2 2026: April $1,086 → May $439 → June $259 (partial). The May drop was driven by RPM
collapse (views were actually higher than April); the June drop appears to be a views
collapse with RPM recovering to April levels. These are two different problems requiring
separate diagnosis.

**What this means for monthly insights:**
- Always lead with the earnings number and decompose it: was this a views problem or an RPM
  problem? These have different causes and different fixes.
- Flag any content-type changes that might explain an RPM shift (e.g. a sudden increase in
  short-form clips, reaction content, or shares of others' videos — these often earn less).
- Track whether the recovery in RPM in June sustains into July, or whether May's collapse
  was the new normal.
- Instagram analysis is secondary for now but worth watching for signs of audience growth
  that could support a future conversion mechanic.

---

## 11. Glossary

- **RPM:** Revenue per mille — earnings per 1,000 video views. Calculated as
  (total monetisation earnings ÷ total video views) × 1,000. The key diagnostic metric for
  separating a reach problem from a monetisation-rate problem.
- **Approximate content monetisation earnings:** The Facebook in-stream ad earnings column.
  This is the primary commercial metric for this client.
- **In-stream ads:** Facebook's video monetisation programme — ads served during qualifying
  video content. Requires videos to be above a minimum length and meet eligibility criteria.
- **Views collapse:** A month where both views and earnings drop proportionally. Cause:
  content reach or algorithm change.
- **RPM collapse:** A month where views hold or grow but earnings drop sharply. Cause:
  monetisation eligibility, content type, or platform rate change — not a reach problem.

---

## Related Files
- [[analytics-engine-SKILL]]
- [[client-config-TEMPLATE]]
- [[clients]]

---
*Config schema 1.0 — initial version based on Q2 2026 (April–June) data.*
