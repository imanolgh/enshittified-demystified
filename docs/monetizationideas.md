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

## 3. Consolidated Tier Structure (recommended)

Two small overlapping subscriptions (#1 + #3) sell worse than one; subscription fatigue is real. Consolidate into a single premium tier.

### Free
- All lookups (local businesses + national brands), all claim cards with full evidence
- All alternatives (local and brand)
- Headline retirement exposure number ("check your plan in 60 seconds")
- 2–3 followed businesses with acquisition alerts (the viral loop stays free)

### Premium — ~$8/mo or ~$79/yr
- Unlimited follows + acquisition alerts (in-app always; email and/or SMS per user preference)
- Retirement monitor with the monthly brief
- Annual cited deep-dive report included
- Priority on-demand research for businesses not yet in the graph

### Supply side (independent businesses pay, users never do)
- **Certified Independent** verification: $200–500/yr (marketgaps.md 5C)
- Featured placement among alternatives — scrupulously disclosed as sponsored (this audience checks)
- Affiliate revenue on alternative click-throughs / bookings

### Later
- **B2B graph & API licensing** (marketgaps.md 3C): journalists, academics, union pension committees, litigation funders — the largest long-run line ("research that would make a ton of money")
- One-time premium reports: family retirement audit ($99+), full rollup dossiers

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
