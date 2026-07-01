---
type: analytics-config
schema_version: 1.0
client: Chris Young + Combustion Inc.
maintained_by: Jack Horscraft / Ziggurat
update_cadence: Quarterly, or after significant strategy or product updates from Combustion
updated: 2026-06-29
---

# Chris Young Analytics Config

*Strategic intelligence + detection rules for the monthly analytics engine. Conforms to
client-config-TEMPLATE schema 1.0. Read in full before writing any insight.*

---

## 1. Identity

```yaml
client_name: Chris Young
client_slug: chrisyoung
brand_accent_hex: #D9291C
output_filename: ChrisYoung_[MonthYear]_Performance.xlsx
platforms_active: [instagram, facebook, youtube]
```

*Note: brand_accent_hex is a working estimate (Combustion red). Confirm with Jack.*

---

## 2. Brand & audience

**Who the client is:** Chris Young is a scientist-turned-chef with one of the most credible
technical cooking voices in the world. He spent five years running the experimental kitchen at
Heston Blumenthal's Fat Duck, co-authored Modernist Cuisine, co-founded ChefSteps, and now runs
Combustion Inc. — the company behind the Predictive Thermometer. His authority is built on
measurement, comparison, and demonstrated expertise, not on personality or aesthetic.

**Brand voice:** Direct, rigor-first, and precise — confident conclusions earned through visible
testing. Dry understatement when humour appears. Never generic food enthusiasm.

**The audience:** Technically curious cooks who want to understand *why* things work, not just
how to follow a recipe. They are builders, sceptics, and experimenters. They skew toward home
cooks serious enough to invest in equipment, with crossover into food professionals. They trust
Chris because he has done the work — in professional kitchens, physics labs, and product
engineering — and shares it without condescension.

**What they sell:** Combustion Inc. Predictive Thermometer — a precision cooking instrument. The
product ecosystem also includes educational content (YouTube, newsletter) that drives product
consideration and repeat engagement. Social content sits at the top of the funnel leading to
YouTube → newsletter → Combustion.com.

---

## 3. Strategy & funnel

**What social is for:** Social is the attention layer for the Chris Young ecosystem. It drives
audiences into the YouTube and newsletter funnel, which then converts to Combustion product
consideration. The funnel is:

**Attention (social) → YouTube video → Newsletter signup → Combustion product**

Content on social should demonstrate Chris's unique analytical lens — not product-push content.
The social job is to make the audience curious enough to follow the chain to YouTube and newsletter.

**The conversion mechanic:** The primary conversion path is link in bio — a single destination
(Linktree or direct link) directing to YouTube channel and newsletter signup. There is no
comment-trigger / auto-DM mechanic in use. Posts with no CTA (no link-in-bio prompt) are pure
awareness plays; they build trust and authority but do not drive action.

---

## 4. Platform roles

### Instagram
- **Primary function:** Audience building and awareness. Demonstrate the analytical, rigorous side
  of Chris's content to attract and retain technically curious followers.
- **What good looks like:** Saves above 150 on a reel = strong content depth signal · Shares above
  50 = broadcast-worthy content reaching new audiences · Comments above 20 = genuine engagement with
  a technical audience · Link-in-bio posts with Follows gained = funnel working.
- **Format expectations:** Reels drive views and discovery · Carousels work for multi-step
  explanations or technique breakdowns · Static images underperform on reach but can anchor a
  specific data point or visual.
- **What to flag as underperformance:** Low saves on educational content (content not sticky
  enough to bookmark) · No CTA posts as a pattern (missed newsletter/YouTube traffic) · Posts
  without a clear analytical hook underperforming across all metrics.

### Facebook
- **Primary function:** Reach and brand awareness. Not a primary conversion channel. Organic
  engagement is structurally suppressed on Facebook brand pages; hold to Facebook norms only.
- **What good looks like:** Views above 8,000 = strong reach for this audience size · Reactions
  above 50 = meaningful engagement · Link clicks above 15 = active traffic driving.
- **Format expectations:** Video/Reel consistently outperforms photo on all metrics · Photo posts
  have a secondary visibility role but should not be benchmarked against video.
- **What to flag:** Consistently low link clicks (audience not being directed effectively) ·
  Photo/Carousel dramatically underperforming video across all metrics (format rebalance signal).

---

### YouTube

- **Primary function:** The primary content surface. YouTube is where Chris's analytical reputation
  lives — long-form demonstrations, tests, and breakdowns that social and newsletter funnel toward.
  Short-form (Shorts ≤60s) serve as entry hooks and curiosity drivers; long-form (>60s) are the
  main content product.
- **Shorts — what good looks like:** Views above 300,000 = strong discovery · Impressions CTR
  above 7% = title/thumbnail compelling within the feed · Subscribers gained on a Short = new
  audience entering the long-form ecosystem.
- **Long-form — what good looks like:** Views above 100,000 = solid discovery for the niche ·
  Watch time (hours) high relative to Views = audience completing the video (depth signal) ·
  Impressions CTR above 6% = strong title/thumbnail pairing · Subscribers gained = new ecosystem
  entrants drawn by the analytical content.
- **What to flag:** Shorts with high Views but low Impressions CTR (distributing well but
  thumbnail/title underperforming in the feed) · Long-form with low Watch time relative to Views
  (audience dropping off — hook or pacing issue) · Low Subscribers gained across both formats
  (reach not converting to retained audience).

---

## 5. Detection rules

### 5a. CTA detection

**Instagram:**
| Column | Logic |
|---|---|
| Trigger Word | Extract the first ALL-CAPS word (2+ letters) following "Comment"/"comment" in the description. Show the word literally. Blank if none. *Note: Chris Young does not currently use the comment-trigger mechanic — this column will typically be blank.* |
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

*No special content types in use. Standard feed scoring applies to all posts.*

---

## 6. Metrics to score

**Instagram (score these):** Views, Reach, Likes, Comments, Shares, Saves, Follows.

**Facebook (score these):** Views, Reach, Reactions, Comments, Shares, Total clicks, Link clicks.
- *Exclude:* `Reactions, comments and shares` — a lump sum of metrics already scored above.

**YouTube Shorts (score these):** Views, Impressions, Impressions CTR, Subscribers.
- *Note: Watch time is excluded for Shorts — duration ≤60s makes cumulative watch time a Views proxy rather than a depth signal. Revenue (Estimated revenue (USD)) is displayed as a passthrough column but not scored.*

**YouTube Long-form (score these):** Views, Watch time (hours), Impressions, Impressions CTR, Subscribers.
- *Note: Watch time is the primary depth signal for long-form content — Chris's audience watches in full when the analytical hook is strong. Revenue (Estimated revenue (USD)) is displayed as a passthrough column but not scored.*

---

## 7. Benchmarks

None yet — this month establishes the baseline.

*Update this section after the first monthly crunch with actual averages from the data.*

---

## 8. Metric strategic tiers

- **Tier 1 — highest strategic value:** Saves (IG — intent signal; this audience bookmarks to
  return to dense technical content) · Link clicks (FB — best proxy for newsletter/YouTube
  traffic) · Shares (both — organic amplification to new technically curious audiences).
- **Tier 2 — important context:** Views (reach/top-of-funnel) · Reach (unique accounts) ·
  Likes/Reactions (passive positive signal) · Follows (IG — new audience entering the funnel).
- **Tier 3 — supporting:** Comments (IG — engagement depth signal, but a technical audience
  comments less than a general one) · Total clicks (FB — broader than link clicks) · Profile
  visits (IG — curiosity signal).

---

## 9. Insight patterns

**What Worked — always look for:**
- Did content with a visible analytical hook (test result, measurement, data reveal) outperform
  content without one? Track the ratio — this is the core of Chris's value proposition.
- Did any post drive unusually high saves? That signals the audience found it bookmark-worthy
  (the highest intent signal for this client).
- Did Reels outperform other formats on discovery metrics (views, reach, follows)?
- Did link-in-bio posts drive measurably more link clicks / follows than No-CTA posts?

**What Didn't Work — always look for:**
- Posts without a clear analytical or technical hook — if they underperform, flag as off-brand.
- No-CTA posts — always note as a missed newsletter/YouTube traffic opportunity.
- Product-push posts without underlying educational content — this audience distrusts overt
  sales content; flag if engagement is weak.
- Duplicate posts or publishing errors — flag immediately.

**What We Do About It — standing recommendations to reassess each month:**
1. Is the link-in-bio CTA appearing consistently across IG posts? If not, flag it.
2. Is the content mix maintaining the analytical/rigor-first voice, or drifting toward generic
   food content? If it drifts, flag it.
3. Are Facebook posts being optimised for video (the dominant format)? If not, flag it.
4. Is there evidence of newsletter subscriber growth being tracked month on month? If not, flag.

---

## 10. Strategic phase

**Current phase — Ecosystem activation (ongoing through 2026):** Chris Young's social presence
is building the top-of-funnel for a connected content ecosystem: YouTube (primary content) →
newsletter (knowledge bites extracted from production material) → Combustion product. The newsletter
system is being rebuilt to extract directly from YouTube pre-production material — authentic to
the production process, not standalone content. Social posts drive to newsletter sign-up.

**What this means for monthly insights:**
- Flag whether social content is doing the analytical, trust-building work that makes the YouTube
  and newsletter funnel credible.
- Track whether Follows trend upward month on month — audience growth is the primary pre-product
  signal.
- Note any content that reads as generic food content rather than Chris Young specifically — the
  differentiated voice is the strategic asset.
- Flag whether link-in-bio is being used consistently to capture newsletter and YouTube traffic.

**Upcoming phases (for context):**
- Newsletter relaunch (timing TBC): when the rebuilt newsletter system is live, social should
  pivot to more explicit newsletter CTAs. The social/newsletter connection should tighten.
- Combustion product campaigns: when a product moment arrives (launch, update, seasonal push),
  content pivots from pure education toward product-grounded education with direct CTAs.

---

## 11. Glossary

- **Combustion Inc.:** Chris's company. Makes the Predictive Thermometer and related precision
  cooking instruments.
- **Predictive Thermometer:** Combustion Inc.'s flagship product — a precision cooking instrument
  that predicts when food will reach target temperature.
- **Modernist Cuisine:** The definitive multi-volume work on the science of cooking, co-authored
  by Chris Young. Referenced as a credential anchor.
- **The Fat Duck:** Heston Blumenthal's three-Michelin-star restaurant, where Chris ran the
  experimental kitchen. Referenced as a credential anchor.
- **No CTA post:** An Instagram post with neither a trigger word nor a link-in-bio prompt.
  Awareness only — does not move the funnel.
- **Danielle:** Combustion Inc. contact. Key liaison for paid ads and campaign direction.

---

## Related Files
- [[analytics-engine-SKILL]]
- [[client-config-TEMPLATE]]
- [[clients]]
- [[ChrisYoung_ToV_Guide_v1]]

---
*Config schema 1.0 — runs against analytics-engine-SKILL v2.0.*
