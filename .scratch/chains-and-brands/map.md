# Map: Chains and brands

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-04

**Active product** (ADR 0004): national chains and brands; version 1 is a website.

## Destination

`.scratch/chains-and-brands/spec.md`: a build spec for version 1 of the chains-and-brands product, on top of the [engine](../engine/map.md) spec. It covers the brand and chain model, launch categories and their brand lists, franchises and licensing, alternatives and affiliate rules, card wording, seeding, and the public website (stack, brand, chain and category pages, the deal feed). It must be complete enough that Claude can build it without asking a design question, with `docs/`, `GLOSSARY.md` and the ADRs consistent with it (scope ruled 2026-11-04).

## Notes

- The [engine map](../engine/map.md) Notes apply here too: authorship, skills, how to resolve, no application code.
- Shared questions live in engine tickets. A blocker there is written `engine/NN`. Work engine frontier tickets alongside this map's.
- **Background**: `.scratch/pivot-handoff-2026-11-02.md` holds the pivot proposal and its evidence (competitors, the USDA barcode test, chain examples, the money estimate, the Worse on Purpose review). Its recommendations are proposals until a ticket rules on them (decisions.md §14).
- **Competitor sites** (Buy'r, Worse on Purpose, Grass, ShopFair, Ethos) are leads a person reads, never sources. WhoIsMyDentist and Private Equity Vet are never fetched automatically (their terms). Reddit is never fetched; the developer pastes threads. The pipeline rule itself is engine "Competitor and third-party data rule".
- **Research tickets**: findings go to `.scratch/chains-and-brands/research/<slug>.md`, every claim cited to a primary source.

## Decisions so far

- Pivot, website first, money model, retirement deferred, ticket layout: [ADR 0004](../../docs/adr/0004-chains-and-brands-first.md) and decisions.md §14 (ruled 2026-11-04, before this map existed).
- No on-demand research: the data set grows only by operator-seeded batches, and searches that find nothing ready feed a demand dashboard ([decisions.md §15](../../docs/decisions.md), ruled 2026-11-05 during engine "Schema conventions").
- Category audit: pilot three categories (restaurants, gyms, eyewear) first, then the developer decides on the rest (ruled 2026-11-04).
- [Research: Category audit pilot (restaurants, gyms, eyewear)](issues/52-research-category-audit-pilot.md): of each top 30, PE-owned or PE minority stake: restaurants 30% (40% if public companies with a PE-fund 5%+ holder count), gyms 30% (33%), eyewear 13% by brands or 21% by sales; owner not found for 2, 7 and 12 brands. 21 of 90 brands borrow from BDCs (Q2 2026). Brand-direct affiliate programs exist only in eyewear, and none is on a PE-owned brand. Leads corrected: Jersey Mike's IPO'd (JMKE, still Blackstone-controlled), Pizza Hut to LongRange closed. Cost ≈ 25–32 min and ~260–280k tokens per category; ~3.1–3.4M tokens for 12 more. Five counting questions for the developer in findings §9.
- [Research: USPTO trademark data as an official source](issues/56-research-uspto-trademark-data.md): USPTO holds one "last recorded owner" per mark, updated only by six recorded document types and without validity checks; changes sit in a separate Assignment database (one record per document; security interests recorded but owner unchanged). In 8 spot checks the registered owner never named the PE sponsor: sponsor-owned brands sat in "IP Holder" or franchisor subsidiaries, and stock acquisitions left no record; Jersey Mike's owner field disagrees with a 2019 assignment. Bulk files and APIs need a USPTO.gov sign-in or keys (ID.me for the bulk API). Adoption, self-verification and source-type count are open for the developer.
- [Brand and chain model](issues/53-brand-and-chain-model.md): every page is a brand page (a chain is a brand with locations); each consumer-facing name is its own brand and a group of brands is a company; a brand page reports the owner of the brand's US business; launch has no locations or operators, every brand page carries the same franchise note, and licensed-run brands read like any brand; a **store map** without operators is the first follow-up after launch; rollups whose practices keep local names are companies.

## Not yet specified

- **Store map** (first follow-up after launch, ruled 2026-11-06 in "Brand and chain model"): stores from brand store locators (selector producers), each with its address and brand, the brand's verdict labeled as the brand's, and a line saying the store's operator isn't checked; open map tiles; a geographic index; monthly re-crawl. No operators.

- **Full category audit**: the remaining ~12 candidate categories. The pilot is done; the developer decides whether to run the rest, and how shares are counted (findings §9).
- **Seeding plan** for chains and brands: sources, order and runbook. ADR 0004 says it follows the category audit; it replaces nothing in `pre-launch-seeding.md`, which stays as the parked local plan.
- **BDC lenders on brand pages**: how a PE-owned chain's page shows which public funds lend to it, once engine "BDC discovery and Schedule of Investments parsing" closes (first follow-up, ADR 0004).

## Out of scope

- **Accounts, follows, paid alerts and billing**: a later map. The alert price is open until `monetizationideas.md` is updated (decisions.md §14).
- **Barcode scanning and a native app**: later (ADR 0004).
- **Local businesses and retirement**: parked in the [local-businesses](../local-businesses/map.md) and [retirement](../retirement/map.md) maps.
- **Outreach and partnerships** (Worse on Purpose, creators): the developer's call, not a spec question.
