# Research: Category audit pilot (restaurants, gyms, eyewear)

Type: research
Status: open
Map: [chains-and-brands](../map.md)

## Question

In three pilot categories (restaurants, gyms, eyewear), what share of each category's top ~30 US brands is owned or backed by private equity today, which of those brands or their parents borrow from public BDCs, and do the method and cost hold up for a full audit of ~15 categories?

## Context

- The audit was proposed in `.scratch/pivot-handoff-2026-11-02.md` §5 ("Choosing categories"). The developer ruled on 2026-11-04 to run a 3-category pilot first, then decide whether to run the rest. ADR 0004 says a chains-and-brands seeding plan follows the category audit.
- The full candidate list (not part of the pilot): restaurants, pharmacy and dollar stores, gyms, car washes, pet stores, eyewear, women's apparel, mattresses, cookware, supplements, healthcare chains (Aspen Dental, VCA and similar), and others.
- Proposed selection test, **not decided**: keep categories around 20% PE or higher, with at least three that can earn affiliate income. This research reports numbers only. The developer picks.
- Known leads, to verify against primary sources, never to cite: Roark behind Subway, Dunkin', Sonic, Arby's, Buffalo Wild Wings and Jimmy John's (the Inspire Brands link for Dunkin' and Jimmy John's is from memory); Jersey Mike's is Blackstone (closed January 2025); Pizza Hut to LongRange and Denny's to TriArtisan, reported in 2026, closing unconfirmed; the Ravenous list (98 restaurant brands, contains at least one error).
- BDC data: [engine/research/edgar-bdc.md](../../engine/research/edgar-bdc.md). The SEC DERA BDC dataset (`soi.tsv`) lists ~122k holdings, with borrower names mostly in free-text identifiers.

## Find out

Per category:
- **The brand list**: the top ~30 US brands, the public source the ranking comes from (systemwide sales, units or revenue), and its date.
- **Per brand**: current owner as a primary source states it; whether that owner is a PE firm or a PE-held company (where checkable, a Form ADV adviser with `Any PE Funds`); acquisition date; public company (ticker) if so; franchised or company-operated; the source URL and a verbatim quote for each fact. Mark "not found" rather than guess.
- **BDC overlap**: does the brand, its operating company or its parent appear as a borrower in the DERA BDC dataset? Name the BDC and filing period.
- **Affiliate income**: do brand-direct affiliate programs exist in this category (yes/no per brand where findable, program URL)?
- **Category share**: count and percentage PE-owned or PE-backed, public, other (family, founder, co-op, strategic). Note any brand where sources disagree.

For the method:
- Time and fetch counts per category, and what made brands slow to settle, so the developer can judge the cost of ~12 more categories.
- Gaps: which kinds of brands had no primary source for the owner.

## Rules

- Public primary sources only (CLAUDE.md): SEC filings, company and sponsor press releases, sponsor portfolio pages, Form ADV, official registries. Public trade press may supply the brand ranking. No PitchBook, Preqin, CB Insights or any paywalled secondary source.
- Competitor sites (Buy'r, Worse on Purpose, Grass, ShopFair, Ethos) are never sources. Never fetch WhoIsMyDentist or Private Equity Vet (their terms bar automated access). Never fetch Reddit.
- Owner kinds here are research notes for a human decision, not engine classifications (ADR 0001 governs the product).
- Respect robots.txt and rate limits. SEC requests need an identified user agent and stay under 10 req/s.

## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/chains-and-brands/research/category-audit-pilot.md`, with one table per category and a method-and-cost section. No branches, commits or pushes. Then append `
