---
type: analytics-config
schema_version: 1.0
client: ChefSteps
maintained_by: Jack Horscraft / Ziggurat
update_cadence: Quarterly, or after significant strategy inputs from ChefSteps
updated: 2026-06-22
---

# ChefSteps Analytics Config

*Strategic intelligence + detection rules for the monthly analytics engine. Conforms to
client-config-TEMPLATE schema 1.0. Read in full before writing any insight. Refactored from
`chefsteps-analytics-context.md` (v1.0) — no strategy was dropped in the split.*

---

## 1. Identity

```yaml
client_name: ChefSteps
client_slug: chefsteps
brand_accent_hex: #FC684E
output_filename: ChefSteps_[MonthYear]_Performance.xlsx
platforms_active: [instagram, facebook, stories]
```

---

## 2. Brand & audience

**Who the client is:** ChefSteps is a premium culinary education platform built around a decade of
obsessive kitchen experimentation. Every recipe, technique, and claim comes from real testing in a
real development kitchen. The brand's authority is earned, not performed.

**Brand voice:** Conversational but not lazy, grown-up but not stodgy, wry but not childish — a
curious, precise expert who happens to also be good company.

**The audience:** People who already cook and want to cook better. Not beginners, not professionals
— the curious middle. Home cooks who want to understand *why*, not just *how*. They save content to
return to, share techniques that surprise them, and follow accounts that make them feel smarter.

**What they sell:** Studio Pass membership tiers (Basic, Studio Pass, Studio Pass VIP), built around
depth of access to recipes, guides, and technique content.

---

## 3. Strategy & funnel

**What social is for:** Social is the top of ChefSteps's conversion funnel. The goal is not follower
count or engagement for its own sake. The funnel is:

**Attention → Click → Account creation → Engagement → Subscription → Retention**

Every post is evaluated against where it sits in that funnel and how effectively it moves people along it.

**The conversion mechanic:** The primary conversion tool on Instagram is the **comment trigger +
auto-DM system**:
1. Post copy includes "Comment [TRIGGER WORD] and we'll send you the recipe".
2. Viewer comments the trigger word.
3. ManyChat auto-DM fires with a link to the free recipe on ChefSteps.com.
4. Viewer lands on ChefSteps.com, experiences the product, and is shown membership options.

This is the most important mechanic in the current strategy. Comment count on trigger-word posts is
a leading indicator of DM volume → site traffic → membership conversion.

On **Facebook**, the equivalent is "link in the comments" — posting the recipe URL in the first
comment. Less interactive but still a traffic driver. Posts with no link-in-comments CTA are
broadcast posts only: they build awareness but do not drive action.

*The Linktree sits between the social CTA and ChefSteps.com as a guided journey (Start here → Learn
→ Go deeper). Linktree performance isn't in the Meta CSVs; post link-click data is a proxy for it.*

---

## 4. Platform roles

### Instagram
- **Primary function:** engagement, conversion, audience deepening. Where the most motivated audience
  lives; the algorithm rewards saves, shares, comments — all high-intent signals.
- **What good looks like:** Saves above 200 on a reel/carousel = strong · comment count 3×+ higher
  than non-trigger posts = mechanic working · shares above 100 = broadcast-worthy content · follows
  gained per post = secondary signal worth tracking over time.
- **Format expectations:** Reels drive views/reach (best for discovery) · carousels drive saves/comments
  (best for depth and recipe content) · images underperform on reach but work for technique tips or a
  single strong visual.
- **What to flag as underperformance:** a reel with views below the monthly median (hook/thumbnail
  problem) · a carousel with saves below the monthly median (save-hook/depth problem) · any No-CTA
  post (missed conversion — always note).

### Facebook
- **Primary function:** reach and brand awareness — NOT a conversion channel like Instagram. Organic
  engagement on FB brand pages is structurally suppressed; do not hold FB to IG benchmarks.
- **What good looks like:** Views above 10,000 = strong reach for a brand page · reactions above 100
  = meaningful engagement · link clicks above 20 = good traffic signal given the platform context.
- **Format expectations:** Video/Reel consistently beats Photo/Carousel on all metrics · photo posts
  still have a reach/visibility role but shouldn't be expected to match video on engagement · link-in-
  comments posts drive more measurable action than broadcast posts.
- **What to flag:** any month where Photo/Carousel consistently underperforms Video/Reel across all
  metrics (recommend shifting volume to video) · very low overall link clicks (audience not given
  enough reason to click).

### Stories
- **Primary function:** relationship maintenance with existing followers, traffic to feed content,
  direct conversion via link taps. Not a discovery format — primarily reaches existing followers.
- **What good looks like:** avg views/story above 2,500 = healthy reach · link clicks/story above 15
  = active traffic driving · profile visits above 10 = audience exploring the account · replies above
  5 = meaningful two-way interaction.
- **What to flag:** high story volume with low avg views (posting too much, diluting attention) ·
  stories not connected to feed content (missed amplification) · long runs with no description or CTA
  (passive publishing, not strategic).

---

## 5. Detection rules

### 5a. CTA detection

**Instagram:**
| Column | Logic |
|---|---|
| Trigger Word | Extract the first ALL-CAPS word (2+ letters) following "Comment"/"comment" in the description. Show the word literally (e.g. POMME, CRUSHING). Blank if none. |
| Link in Bio | ✓ if description contains "link in bio", "linktree", or "link in our bio" (case-insensitive). Else blank. |
| No CTA | ✓ if both Trigger Word and Link in Bio are blank. Else blank. |

*If a post has both a Trigger Word and Link in Bio, mark both ✓.*

**Facebook:**
| Column | Logic |
|---|---|
| Link in Comments | ✓ if the word "comment" appears anywhere in `Title` or `Description` (case-insensitive). Else blank. |

### 5b. Special content types

```yaml
special_content:
  - name: Trial Reels
    platform: instagram
    detect_when_copy_contains: ["we are always AD FREE", "and we never have ads"]
    handling: separate_tab
    min_count_note: If fewer than 2 Trial Reels detected, build the tab anyway with the data present and a note explaining the low count.
```

*Footnote count required: "X Trial Reels excluded from main IG scoring."*

---

## 6. Metrics to score

**Instagram (score these):** Views, Reach, Likes, Comments, Shares, Saves, Follows.

**Facebook (score these):** Views, Reach, Reactions, Comments, Shares, Total clicks, Link clicks.
- *Exclude:* `Reactions, comments and shares` — a lump sum of metrics already scored above.

**Stories (score these):** Views, Reach, Likes, Replies, Link clicks, Profile visits.
- *Exclude:* `Navigation` — records exits/forwards, not positive signal.
- *Sparsity rule:* drop `Follows` / `Sticker taps` (or any metric) where fewer than 15% of stories
  have a non-zero value — too sparse to rank meaningfully.

---

## 7. Benchmarks

*Used in written insights only, never in scoring. Update after each monthly crunch.*

### Instagram feed (as of April 2026)
| Metric | Monthly average | Strong | Exceptional |
|---|---|---|---|
| Views per post | ~18,000 | >30,000 | >60,000 |
| Saves per post | ~280 | >500 | >1,500 |
| Comments per post (trigger) | ~50 | >80 | >100 |
| Comments per post (no trigger) | ~5–10 | — | — |
| Shares per post | ~120 | >200 | >1,000 |
| Likes per post | ~230 | >400 | >700 |

### Facebook feed (as of April 2026)
| Metric | Monthly average | Strong | Exceptional |
|---|---|---|---|
| Views per post (video) | ~13,700 | >20,000 | >30,000 |
| Views per post (photo) | ~6,200 | >10,000 | — |
| Reactions per post | ~59 | >150 | >350 |
| Link clicks per post | ~1 | >10 | >30 |

### Instagram Stories (as of April 2026)
| Metric | Monthly average | Strong | Exceptional |
|---|---|---|---|
| Views per story | ~1,900 | >2,500 | >5,000 |
| Link clicks per story | ~13 | >20 | >50 |
| Profile visits per story | ~4 | >10 | >50 |
| Replies per story | ~0.4 | >5 | >30 |

*December 2025 is the Stories ceiling — avg 3,384 views/story, 21.3 link clicks/story. Target this
level consistently.*

---

## 8. Metric strategic tiers

- **Tier 1 — highest strategic value:** Saves (IG — strongest intent signal) · Comments on trigger
  posts (IG — proxy for auto-DM volume → site traffic) · Link clicks (FB, Stories — closest thing to
  conversion data in Meta exports) · Shares (both — organic reach amplification).
- **Tier 2 — important context:** Views (reach/top-of-funnel) · Reach (unique accounts) · Likes /
  Reactions (passive positive signal) · Follows (IG — new audience, meaningful spikes worth noting).
- **Tier 3 — supporting:** Profile visits (Stories — curiosity) · Replies (Stories — two-way) ·
  Total clicks (FB — broader than link clicks).

---

## 9. Insight patterns

**What Worked — always look for:**
- Did technique-first content with a visual transformation arc outperform recipe-list content? (Expected yes.)
- Did comment-trigger posts significantly outperform non-trigger posts? (Track the ratio.)
- Did any format (Reel vs Carousel vs Image) dominate in a specific metric?
- Any standout saves or share numbers signalling exceptional content?
- Did creator-tagged or collab content drive unusual profile visits or follows?

**What Didn't Work — always look for:**
- Compilation/aggregation posts (no singular hook) consistently underperform — flag every time.
- Non-culinary content (job posts, announcements) typically underperforms — note engagement ratio vs reach.
- Posts with No CTA — always note as a missed conversion opportunity.
- Duplicate posts or publishing errors — flag immediately, recommend deletion.
- Photo/Carousel FB posts that significantly underperform video — ongoing format strategy signal.

**What We Do About It — standing recommendations to reassess each month:**
1. Is comment-trigger usage consistent across all IG posts? If not, flag it.
2. Is Facebook content being differentiated by format (more video)? If not, flag it.
3. Are Stories amplifying feed content, or running in parallel? Flag the gap if present.
4. Is there evidence the DM-to-site conversion loop is tracked? If not, keep flagging until it is.

---

## 10. Strategic phase

**Current phase — ChefSteps 3.0 Pre-Launch (through September 2026):** ChefSteps is preparing to
relaunch as ChefSteps 3.0 in September 2026, a significant product upgrade. Social during this phase
should **reintroduce and establish** (remind audiences what ChefSteps is and why it matters — demonstrate
product depth, don't announce the relaunch), **show the value** (every post is a proof point; the
comment trigger + DM + free recipe is the clearest demonstration — volume of this mechanic matters now),
and **build anticipation** (as September nears, signal something bigger is coming through quality
escalation, not explicit announcement).

**What this means for monthly insights:**
- Flag whether social is actively functioning as a pre-launch proof-of-value engine.
- Note whether the ChefSteps.com landing experience (post-DM) is being optimised.
- Flag any content that feels off-brand or inconsistent with the 3.0 positioning.
- Track whether follow rates trend upward month on month — audience growth before launch is strategic.

**Upcoming phases (for context):**
- **Launch (September 2026):** direct conversion push; content pivots to explicit membership offers and launch CTAs.
- **Post-launch education (October 2026+):** onboarding new members, demonstrating platform depth, retention content.

---

## 11. Glossary

- **Studio Pass:** ChefSteps paid membership. Tiers: Basic, Studio Pass, Studio Pass VIP.
- **Trial Reel:** an IG Reel running as a paid Meta trial for the Reels format. Identified by copy
  containing "we are always AD FREE" or "and we never have ads". Excluded from main IG scoring,
  analysed separately.
- **Trigger word:** the all-caps word in IG copy after "Comment" that activates the ManyChat auto-DM
  flow (e.g. "Comment POMME and we'll send you the recipe").
- **Auto-DM:** the automated DM sent via ManyChat when a viewer comments the trigger word.
- **Linktree:** the link hub between social CTAs and ChefSteps.com. URL in the IG bio.
- **Parametric:** ChefSteps's signature format — a large printable PDF summarising deep-dive culinary
  testing on a single topic.
- **Nick and Sasha:** ChefSteps on-camera hosts. Their personalities inform caption voice and on-screen reasoning.
- **Grant and Jane:** ChefSteps-side contacts involved in platform strategy and briefing.

---

## Related Files
- [[analytics-engine-SKILL]]
- [[client-config-TEMPLATE]]
- [[README]]

---
*Config schema 1.0 — runs against analytics-engine-SKILL v2.0. Supersedes chefsteps-analytics-context.md (v1.0).*
