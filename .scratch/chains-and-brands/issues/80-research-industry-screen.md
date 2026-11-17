# Research: Industry screen

Type: research
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

In twelve candidate industries the two category audits never covered, what share of the top ~10 US consumer-facing brands is owned or backed by private equity today? The screen finds which industries deserve a full audit before "Launch industries" picks the launch list.

## Context

- Split off "Product categories: vocabulary and assignment" on 2026-11-16 (round 1 Q2 revised). The developer asked where the thirteen audited industries came from (the 2026-11-02 pivot proposal's candidate list; nobody screened outside it) and raised bowling alleys from an article.
- Candidates, approved by the developer with Q2 and Q6 revised:
  1. bowling and family entertainment centers
  2. golf (courses, clubs and golf entertainment)
  3. ski resorts
  4. child care centers
  5. hair salons and barbershops
  6. funeral homes
  7. collision repair
  8. oil change and auto service
  9. home services franchises (HVAC, plumbing, pest control and similar)
  10. urgent care
  11. physical therapy
  12. landlord brands: companies that rent out homes they own under their own name (single-family rental). Property managers such as Greystar are ruled out.
- Model to copy, scaled down to the top 10: [research/category-audit-pilot.md](../research/category-audit-pilot.md) and [research/category-audit-full.md](../research/category-audit-full.md). Counting rules since then: Form ADV `Any PE Funds = Y` marks a PE firm and `N` proves nothing; above a public company a PE minority stake counts only from a 13D or a 13G not filed under Rule 13d-1(b), and passive 13Gs (index and asset managers) never count (engine "Category precedence and public companies"); a brand is a name a consumer sees on a storefront or sign, and a rollup whose locations keep local names is a company, listed separately (chains "Brand and chain model").
- Estimated cost approved: about 1.2M tokens in all.

## Find out

Per industry:
- The top ~10 national US brands by locations, sales or revenue, with the ranking's public source and date. Rollups with locally named locations in a separate short list, with a one-line note on how much of the industry they make up.
- Per brand: current owner as a primary source states it, owner type (PE firm or PE-held company, public, family, franchisor and so on), acquisition date, ticker if public, a source URL and verbatim quote for each fact, "not found" rather than a guess.
- PE share by brand row (PE-owned plus PE minority stake), and a one-line verdict: full audit or not.

## Rules

- Public primary sources only (CLAUDE.md). Trade press supplies rankings only. No PitchBook, Preqin, CB Insights or paywalled sources. Competitor sites are never sources; never fetch WhoIsMyDentist, Private Equity Vet or Reddit.
- Respect robots.txt. SEC requests use the user agent `EvidenceEngine ownership-research bot (industry screen)` with no email or contact detail, at or under 2 per second.
- About 5 fetches per brand, then "not found".
- Owner types here are research notes for a human decision, not engine classifications (ADR 0001 governs the product).
- Findings go to `.scratch/chains-and-brands/research/industry-screen.md`.

## Answer

Resolved 2026-11-16 by four background workers (about 1.10M tokens). Findings: [industry-screen](../research/industry-screen.md), with the four worker reports in [research/industry-screen/](../research/industry-screen/).

- PE share by brand row: collision repair 90%, urgent care 80%, physical therapy 80%, home services franchises 69% (composite list), child care 60%, oil change and auto service 50%, bowling and family entertainment 45% (64% if Atairos counted), hair salons 30% (salon suites only), golf 29% (operators PE-backed), landlord brands 25% strict, ski resorts 12.5%, funeral homes 0% (PE in local-name rollups).
- Worth a full audit: collision repair, urgent care, physical therapy, home services franchises (size measure first), child care, oil change and auto service, bowling and family entertainment; golf only as an operator audit.
- Five questions for the developer, handed to "Launch industries": owners whose Form ADV says no PE funds (Atairos, Meritage); a public holding company as a holder (Icahn Enterprises); real estate funds as landlords; industries where PE sits in local-name rollups; home services' size measure.
- 285 of 285 quotes matched; every negative control failed.
