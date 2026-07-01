---
type: analytics-config
schema_version: 1.0
client: Ninjon
maintained_by: NaaShika / Ziggurat
update_cadence: Quarterly, or when Deck launch cadence or KB strategy materially changes
updated: 2026-07-01
---

# Ninjon Analytics Config

*Strategic intelligence + detection rules for the monthly analytics engine. Conforms to
client-config-TEMPLATE schema 1.0. Read in full before writing any insight.*

---

## 1. Identity

```yaml
client_name: Ninjon
client_slug: ninjon
brand_accent_hex: #C94A1A
output_filename: Ninjon_[MonthYear]_Performance.xlsx
platforms_active: [instagram, facebook]
```

*Note: brand_accent_hex is a working estimate (warm burnt-orange — consistent with Ninjon's
hobby-warm palette and the Warhammer miniature aesthetic). Confirm with NaaShika.*

---

## 2. Brand & audience

**Who the client is:** Jon Ninas — channel name Ninjon — is a recognised miniature-painting
expert with a decade-plus of YouTube IP and a trust-driven audience in the Warhammer and tabletop
hobby community. His authority comes from demonstrated skill and a community that has followed his
work closely for years. His personal integrity is the core asset: he is publicly committed to
real, licensed artists (the Deck of Many Colors artists are credited and human) and the community
is sensitive to anything that smells of AI-generated art. That sensitivity runs deep — every piece
of content, every caption, every recommendation must read as genuine expert voice, not auto-generated.

**Brand voice:** Warm, friendly, expert-but-approachable — the "Jon on your shoulder" register
(his literal greeting is "Hey again, friends"). Technique explanation is the heartland: step-by-step
guidance that gives value at every level without dumbing anything down. Hand-holding for beginners,
depth for veterans, no condescension in either direction. Avoid the tell-tale repetition patterns of
AI-content (stock greetings, generic transitions). The tone goal is "a knowledgeable friend at the
painting desk."

**The audience:** Miniature and tabletop painters across the full skill range — total beginners
arriving overwhelmed (the combat patrol just arrived, the pile of shame is real) through returning
hobbyists (the new-dad returner is the top-liked comment in the YouTube corpus) through experienced
painters who still tune in to validate and add their own tips. The community is **anti-AI-art-sensitive**
and tool-and-purchase-heavy (a "golf-money" hobby — "what's the X you're using?" is a constant
question and a meaningful revenue signal). Trust is the medium; protecting Jon's credibility is
the standing first principle.

**What they sell:** The **Deck of Many Colors** — a physical product, already live and selling,
fulfilled via an optimised landing page. Real, licensed artists. This is the proven revenue anchor
and every social post should ultimately feed back toward it. Merch is moving in-house. Longer-term:
an owned email list (via Kit), an on-site knowledge base turning Jon's YouTube videos into
guided-walkthrough articles, and eventually a Wirecutter-style trusted product-recommendation hub
for the hobby.

---

## 3. Strategy & funnel

**What social is for:** Social is the top-of-funnel attention layer for an owned-audience flywheel
that is currently being built. The funnel is:

**Attention (social + YouTube) → email capture (Kit) → guided KB journey on-site → Deck of Many
Colors → progress sharing → new attention**

Short-form social must pull the right person into the right pathway (beginner vs. expert — different
creative, different destination). Email is the capture mechanism because Jon wants off the
YouTube-treadmill long-term; social is rented attention, the inbox is owned. The KB is the
conversion architecture — not just a content library, but a structured journey with a clear next
step that eventually makes people ready for the Deck. The current strategic phase is early:
building the funnel and the KB, activating email capture, not maximising product conversion yet.

**The conversion mechanic:**

- **Comment trigger ("Confirm"):** Used during product launch and preorder campaigns (Deck of Many
  Colors). When active, "Confirm" in a post description signals a gated-DM or preorder flow. Flag
  these posts as campaign-mode content.
- **Link in bio:** Standing CTA for all non-campaign periods — directing to the KB, email sign-up,
  or Deck landing page as relevant. This is the primary ongoing mechanic.
- **No CTA:** Pure awareness / algorithm play. Flag as a missed capture opportunity during the
  current KB-build and email-activation phase.

---

## 4. Platform roles

### Instagram

- **Primary function:** Awareness and hook — pull the right persona (beginner, plateau hobbyist,
  aspiring advanced) into the matching pathway. Build the email list. Drive to the Deck during
  campaign windows.
- **What good looks like:** Saves above 150 = technique or tutorial content sticky enough to
  bookmark — the clearest quality signal for this audience · Shares above 60 = content spreading
  within the Warhammer/hobby community to new painters · Follows on technique content = new painters
  entering the ecosystem · Link clicks via bio = funnel working (KB or email capture).
- **Format expectations:** Reels drive discovery (views, reach, follows) — primary format for new
  audience · Carousels for step-by-step technique walkthroughs or product comparisons (the hobby
  community responds well to multi-panel visual sequences) · Static images weaker on reach but can
  anchor a single striking finished-model shot or product reveal.
- **What to flag as underperformance:** Low saves on tutorial/technique content (hook or depth
  problem — the content isn't delivering enough value to bookmark) · No-CTA posts as a sustained
  pattern during the email-activation phase (missed capture) · High views with low saves or shares
  (reach working, content not landing — quality or positioning issue) · Confirm-trigger posts with
  low engagement (campaign creative not converting).

### Facebook

- **Primary function:** Supplementary reach and brand presence. Secondary surface only — do not
  hold to Instagram benchmarks.
- **What good looks like:** Views above 6,000 = solid reach for the platform · Reactions above 40 =
  meaningful engagement signal · Link clicks above 10 = active audience directing toward the funnel.
- **Format expectations:** Video/Reel consistently outperforms photo content · Photo posts have
  a secondary awareness role only.
- **What to flag:** Sustained low link clicks (audience not being moved into the KB or Deck) ·
  Photo-heavy months structurally underperforming — flag as format imbalance.

---

## 5. Detection rules

### 5a. CTA detection

**Instagram:**
| Column | Logic |
|---|---|
| Trigger Word | Extract the first ALL-CAPS word (2+ letters) following "Comment"/"comment" in the description. Show the word literally. Blank if none. *Ninjon uses "Confirm" during product-launch and preorder campaigns; flag months where this appears as campaign-mode periods.* |
| Link in Bio | ✓ if description contains "link in bio", "linktree", "link in our bio", or "in bio" (case-insensitive). Else blank. |
| No CTA | ✓ if both Trigger Word and Link in Bio are blank. Else blank. |

**Facebook:**
| Column | Logic |
|---|---|
| Link in Comments | ✓ if the word "comment" appears anywhere in Title or Description (case-insensitive). Else blank. |

### 5b. Special content types

```yaml
special_content:
  - name: Deck Post
    detection: description or title contains "Deck of Many Colors" or "Deck" (case-insensitive)
    flag_column: Deck Post
    note: >
      Product content — the revenue anchor. Flag these separately; track whether they outperform
      or underperform pure technique content, and whether they carry a Confirm trigger or
      link-in-bio CTA. Campaign posts without a CTA are a flag.

  - name: Beginner Content
    detection: description or title contains "beginner", "start here", "first time", "first mini",
               "getting started", or "for beginners" (case-insensitive)
    flag_column: Beginner Content
    note: >
      The beginner pathway is the primary top-of-funnel entry point. Track these separately to
      see whether beginner-targeted content drives higher follows and saves (new audience entering)
      vs. technique-depth content that retains existing followers.
```

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
  content worth returning to; tutorial and technique content that explains well gets bookmarked;
  saves above 150 on a beginner or technique post are a strong quality signal) · Shares (both —
  organic spread within the Warhammer/hobby community to new painters is the primary new-audience
  acquisition route) · Link clicks (FB — best proxy for KB or Deck traffic; the standing measure
  of whether the funnel is working).
- **Tier 2 — important context:** Follows (IG — new painters entering the ecosystem; the primary
  growth signal during this phase) · Views (reach/top-of-funnel; the reach layer that feeds the
  funnel) · Reach (unique accounts) · Reactions/Likes (passive positive signal — warmer signal for
  Ninjon than for science creators because the community actively appreciates and endorses).
- **Tier 3 — supporting:** Comments (IG — engagement depth; the Ninjon comment section historically
  mixes genuine technique questions with community pro-tips — note this pattern) · Total clicks (FB) ·
  Profile visits (IG — curiosity signal; high profile visits with low follows = bio or grid isn't
  converting).

---

## 9. Insight patterns

**What Worked — always look for:**
- Did beginner/tutorial content outperform general content on Saves and Shares? This is the core
  content thesis: the beginner pathway is the top of the funnel.
- Did technique-depth posts (step-by-step walkthroughs, paint recipes, tool recommendations) drive
  higher Saves than awareness-only posts? Saves = bookmark intent = the audience found it worth
  returning to.
- Did Deck of Many Colors posts drive higher link clicks (Bio/FB) than non-Deck posts? This is the
  product health signal.
- Did posts with a Confirm trigger (campaign mode) produce a measurable engagement spike vs. the
  standing average? Campaign-window performance matters for planning the next launch.
- Did Reels dominate discovery metrics (Views, Reach, Follows) vs. other formats? Expected — flag
  any month where this breaks.
- Did content featuring finished models / results outperform process/WIP content? The hobby community
  responds to aspiration as well as instruction.

**What Didn't Work — always look for:**
- No-CTA posts as a sustained pattern — flag as missed email capture / KB traffic during the current
  activation phase.
- High reach with low saves or shares — hook working but depth not landing (quality or positioning
  problem, not a reach problem).
- Deck posts without a CTA — product content that doesn't direct anywhere is a structural miss.
- Generic lifestyle content that doesn't connect to technique, product, or the community — off-brand
  and likely underperforming.
- Photo-heavy months on Facebook — structural format underperformance, flag directly.

**What We Do About It — standing recommendations to reassess each month:**
1. Is the Kit email list growing? Are social posts directing to email sign-up in non-campaign months?
   If no, flag the activation gap.
2. Is the beginner-pathway creative (the persona-targeted Reels for total beginners, plateau
   hobbyists, and aspiring advanced) being produced consistently? Irregular output is a structural
   pipeline problem.
3. Is the link-in-bio pointing to the right destination — KB, email capture, or Deck — for the
   current strategic moment?
4. Are Follows trending upward month on month? This is the primary top-of-funnel growth signal for
   the owned-audience build.
5. Is there a Deck launch window coming? Flag the month ahead so campaign creative (Confirm trigger)
   is planned in advance, not retrofitted.

---

## 10. Strategic phase

**Current phase — Owned-audience build + KB activation (2026):** Ninjon has a large YouTube
audience and a proven physical product (the Deck), but the conversion architecture between social
attention and owned audience is nascent. The website is migrating Squarespace → Shopify, the KB
is being built from YouTube transcripts, and Kit is live but underutilised beyond preorder updates.
The current phase is about wiring the funnel: social → email capture → KB journey → Deck readiness.
Social content should be persona-targeted and directed; the metric that matters most is whether
saves and follows are growing (audience finding the content bookmark-worthy and entering the
ecosystem).

**What this means for monthly insights:**
- Flag any month where email CTAs are absent from non-campaign posts — missed capture is the
  standing risk.
- Track the beginner-content performance cluster separately every month — this is the strategic
  top-of-funnel investment.
- Note whether Deck posts appear and whether they carry a proper CTA — product content without
  direction is a structural miss.
- Flag any engagement patterns that suggest the community is reacting poorly to tone or content
  quality — the trust asset is everything, and a drift toward generic or AI-feeling content is a
  serious brand risk.

**Upcoming phases (for context):**
- **Full KB live:** When the on-site knowledge base is complete and the beginner pathway is live,
  social should shift to active KB-driving CTAs (specific article links, not just "link in bio").
  Track KB-directed link clicks as a distinct signal once live.
- **Deck 3 & 4 launch:** The next Deck launch will trigger a Confirm-mechanic campaign window.
  Build in the month before: ensure campaign creative is planned, the trigger is in the descriptions,
  and the DM/landing flow is tested before launch.
- **Wirecutter-style review hub:** A longer-term content layer (tool and product recommendations
  built from YouTube-comment sentiment — "what's the X you're using?" is the dominant question
  cluster). Don't centre this yet; note when the KB foundation is stable enough to support it.

---

## 11. Glossary

- **Deck of Many Colors:** Ninjon's physical product — an artist-designed deck featuring real,
  licensed miniature painters. The proven revenue anchor. Everything feeds back toward it.
- **Kit:** Email platform (ConvertKit). Live for preorder status updates. Extending to the nurture
  funnel is the next step.
- **Confirm:** The comment-trigger keyword used during product-launch and preorder campaigns.
  Comments the word → automated DM → preorder link or landing page. Campaign-mode only.
- **KB (Knowledge Base):** The on-site library being built from Jon's YouTube video transcripts —
  guided-walkthrough articles organised by skill level and pathway. The site architecture that
  turns social attention into a structured journey.
- **Beginner pathway:** The "Start Here" entry lane — designed for total beginners and returning
  hobbyists ("pile of shame" / new-parent returner segment). The flagship article anchors the front
  door of the KB.
- **Deck 3 & 4:** Upcoming Deck of Many Colors editions (artist shortlisting and palettes in
  progress as of July 2026 — AdMagic finalisation end Sept / start Oct).
- **Adam:** Ninjon's volunteer technical lead (Shopify build, merch in-house, AI article back-end).
  Remit is physical/infrastructure — distinct from Ziggurat's digital/journey scope.
- **NaaShika:** Ziggurat SMA lead for Ninjon.

---

## Related Files
- [[analytics-engine-SKILL]]
- [[client-config-TEMPLATE]]
- [[clients]]
- [[ninjon-build-context]]
- [[ninjon-vision-journey-board-revised]]
- [[sentiment-engine-ninjon]]

---
*Config schema 1.0 — runs against analytics-engine-SKILL v2.0.*
