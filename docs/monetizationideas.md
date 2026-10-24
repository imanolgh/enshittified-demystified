# Monetization Strategy
### Pricing model for the ownership transparency platform — free/paid line, tier structure, and rejected approaches
### Companion to: marketgaps.md (business models), decisions.md (§5, §7), painpoints.md (willingness-to-pay evidence)

---

## 1. The Governing Principle

**Evidence is free; services on top of the graph are paid.**

The claim cards, sources, ownership chains, and alternatives are the trust mechanism — paywalling any of them undermines the product's reason to exist (decisions.md §7). Revenue comes from *ongoing services* composed from the graph (alerts, monitoring, analysis, certification, licensing), never from tolls on the evidence itself.

A second principle shapes every price: **event frequency.** Subscriptions survive on the feeling of receiving value regularly, and this product's raw events (acquisitions, plan changes) are rare. Every subscription below is therefore either (a) priced like insurance against a rare-but-important event, or (b) enriched with a recurring deliverable (digests, briefs, re-check confirmations) so the cadence matches the price.

---

## 2. Original Proposal vs. Revised Model

| # | Original idea | Assessment | Revision |
|---|---|---|---|
| 1 | PE acquisition alerts for followed local businesses — **$5/mo** | Right concept, wrong cadence: a follower of 3 local businesses may receive zero alerts for years → churn, and the paywall hides the product's most viral artifact (the alert itself) | **$19–29/yr** ("insurance" framing) with a **monthly digest** (re-check confirmations + metro acquisition roundup) as the recurring deliverable; **first 2–3 follows free** so alerts keep working as the growth loop |
| 2 | One-time 401(k)/pension analysis — **$120** | Two problems: consumers anchor this category to credit-report pricing ($20–40), not advisor pricing; and most analyses today honestly conclude "minimal exposure," making $120 a refund-request machine | **Headline exposure number free** (the acquisition hook for the whole retirement surface); **full cited deep-dive $29–49**; reserve $99+ for a future multi-plan "family retirement audit" |
| 3 | Retirement X-ray monitor — **$10/mo** | Underlying data changes annually (Form 5500, CAFRs) to quarterly (N-PORT); $120/yr against yearly data is a value mismatch users will notice | Either **~$3–5/mo / ~$39/yr** as pure monitoring, or **earn $10/mo** with an editorial monthly brief (filings news on the user's specific funds, gating/PIK developments, 401(k)-alternatives regulatory tracking). The enriched version is genuinely worth it and rides a guaranteed news cycle — but it is an editorial commitment, not just plumbing |
| 4 | Paid alternatives for PE-owned national brands — **$5/mo** | Rejected (see §4) | Alternatives stay free; monetize the **supply side** of the alternatives page instead |

---

## 3. Consolidated Tier Structure (canonical)

Two small overlapping subscriptions (#1 + #3) sell worse than one; subscription fatigue is real. Consolidate into a single premium tier.

### Free
- All lookups (local businesses + national brands), all claim cards with full evidence
- All alternatives (local and brand)
- Headline retirement exposure number ("check your plan in 60 seconds")
- 2–3 followed businesses with acquisition alerts (the viral loop stays free)

### Premium — ~$8/mo or ~$79/yr
- Unlimited follows + acquisition alerts (in-app always; email and/or SMS per user preference)
- Monthly digest (re-check confirmations for followed businesses + metro acquisition roundup)
- Retirement monitor with the monthly brief
- Annual cited deep-dive report included
- *(minor perk)* Priority on-demand research for businesses not yet in the graph

**Positioning (2026-10-16):** Premium is sold on monitoring — alerts, the digest, the retirement brief and the deep-dive. Priority research is a minor perk only and should not be marketed as a reason to subscribe. Most evidence-bearing businesses are pre-seeded, many on-demand results are an honest "no PE evidence found", and on-demand research stays free for everyone; Premium only moves it up the queue. A "no evidence found" result should lead the user to "follow this business so you know if that changes."

### Supply side (independent businesses pay, users never do)
- **Certified Independent** verification: $200–500/yr (marketgaps.md 5C)
- Featured placement among alternatives — scrupulously disclosed as sponsored (this audience checks)
- Affiliate revenue on alternative click-throughs / bookings

### Research/Pro — ~$20–30/mo (post-launch, ruled 2026-10-16)
- Market-wide intelligence for professionals (journalists, lawyers, investors, litigation funders): quarterly BDC loan-book diffs (new borrowers, departed loans, non-accrual and PIK trends), full rollup dossiers, cross-layer exposure maps, and eventually the insurer/NAIC exposure map as flagship.
- **Sequencing gate:** launches only after the graph has real depth (several quarters of BDC diffs, dossiers worth reading). Selling thin reports to the most demanding audience would burn trust.
- **Keep the tiers distinct:** Premium is *personal* (your businesses, your funds); Research/Pro is *market-wide*.
- Willingness-to-pay evidence: Octus and Grant's are cited approvingly in the corpus as useful but expensive. Research/Pro sits well under $1,000+/yr institutional products and above consumer pricing.
- A usage meter suits this tier (e.g. 3 free dossiers or loan-book views per month), because its audience looks things up often.

### Later
- **B2B graph & API licensing** (marketgaps.md 3C): journalists, academics, union pension committees, litigation funders — the largest long-run line ("research that would make a ton of money")
- One-time premium reports: family retirement audit ($99+), full rollup dossiers

---

## 3A. Launch Phase — ~3-Month Free Premium Beta (agreed 2026-10-17)

Before any billing, every user gets Premium free during a founding-member beta. Evidence stays free throughout and after.

- **Label it from day one:** "Founding members: Premium free until [date]." Send a reminder 2–3 weeks before it ends. No surprise paywall.
- **What's free during the beta:** unlimited follows and alerts, the monthly digest, the retirement monitor brief, and the included deep-dive.
- **Gentle downgrade after the beta:** free users keep 2–3 active follows. Extra follows are **saved and paused, not deleted**; the user picks which stay active, and subscribing reactivates the rest in one click. Deep-dives already received stay with the user; the next one comes a year later with Premium.
- **Founding-member incentive:** a locked-in lower price for beta joiners (e.g. ~$5/mo or $49/yr), so early users become defenders of the price change.
- **Trigger, not just a date:** about 3 months is the target. Turn billing on only once alerts have fired for real users and the digest has gone out reliably; otherwise extend the beta.
- **Must be ready before the beta starts:** the securities-attorney review of the retirement brief and deep-dive wording (decisions.md §5), and built and tested billing/account tiers, so the switch is a config change.
- **Make monitoring visible:** most users won't receive a real acquisition alert within 3 months, so the digest's re-check confirmations ("we checked your 6 businesses on these dates; no changes") carry the value.
- **MyRetirementX-Ray at launch:** the employer → plan lookup and the free headline exposure number launch with the PE map (they're seeded and free forever). The Premium pieces (monitor brief, deep-dive) are available from launch for free as part of the beta, and become paid when billing turns on.

## 3B. Metering Rules

- **Never meter claim cards**, sources, ownership chains or alternatives. Shared links must always land on visible evidence, since sharing is the growth loop.
- **Acceptable meters**, if wanted later: (a) depth, meaning full dossier/money-flow graph views beyond the claim card; (b) on-demand research for businesses not yet in the graph, which has real per-request cost; (c) Research/Pro usage.
- **Considered but not adopted for the consumer app:** a Simply Wall St–style "N free searches, then pay" meter. Reasons: consumers search rarely (a few businesses a few times a year), growth is driven by shared links, and the evidence-is-free principle. Simply Wall St's model fits the Research/Pro audience instead.
- **Also considered and advised against:** free-until-viral, then charging existing users to keep using the product. Taking away free access that people relied on is the bait-and-switch this audience is primed to punish; the founding-member beta above gets the same revenue without it.

---

## 4. Rejected: Paywalling Brand Alternatives

Three reasons, in increasing order of importance:

1. **Consistency.** Local alternatives free but brand alternatives paid is incoherent, and users sense incoherent trust posture quickly in exactly this market.
2. **The corpus.** Alternatives-linking was the **single most-requested feature** in the Worse on Purpose viral thread — requested by users showering a free tool with gratitude. Paywalling the community's #1 ask, in a product whose moat is community trust, reads as ransoming the boycott.
3. **Channel conflict.** Alternatives are the supply-side monetization surface. The independent brands and providers listed as alternatives are the parties with money and motive (certification, placement, affiliate). Charging users to see the page while also taking placement revenue from the businesses on it is double-dipping — and users would eventually notice which side is being served.

---

## 5. National Brand Expansion (post-MVP)

Direct competition with Worse on Purpose, on the same graph and claim-card anatomy as local services.

**Differentiation, written by their own comment thread:** their users questioned whether the content was AI-written and disputed verdicts (Carhartt, Miele) with no receipts available to settle the arguments. This platform's brand cards carry verdict + ownership *type* (PE / conglomerate / family / employee-owned / trust — resolving the Fiskars/Gerber misattribution wars) + acquisition date + primary sources. Where they have vibes-with-tiers, this has citations.

**Feature they lack that their users begged for:** acquisition dates for secondhand shopping ("the year in which these brands were bought so we know how old to look for stuff on secondhand market") — free here, powered by the same claims.

Brand alternatives: free (per §4), monetized via the supply side.

---

## 6. Pricing Rationale Reference

- **Insurance framing** for rare-event alerts: annual pricing, low absolute number, digest cadence making the service visible between events.
- **Anchor awareness**: consumer reports price against credit reports/background checks, not professional advice — and the informational-only regulatory posture (decisions.md §5) means the product *shouldn't* feel like advisor work.
- **Free headline number as funnel**: the "minimal exposure detected" outcome that undermines a $120 one-shot is a *perfect* subscription hook — "clean today; we'll watch your plan's filings and alert you the moment that changes."
- **One tier, one decision**: every paid item is a service on the graph; the free tier carries the complete trust story; upgrade is a single choice rather than a menu of small tolls.