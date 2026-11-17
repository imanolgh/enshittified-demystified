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
- [Research: Full category audit (ten remaining candidates)](issues/66-research-full-category-audit.md): by brand row after the Form ADV pass, PE-owned or PE minority stake is dental 50%, vet 52% (21 rows), car washes 53%, women's apparel 38% (32 rows), mattresses 27%, pet stores 19%, cookware and supplements 10–13%, dollar and discount 8%, pharmacies 3%; 66 of 284 brands overlap BDC holdings; mattresses and cookware have 10 brand-direct affiliate programs each; 1 of 1,022 quotes failed re-check (no owner fact depends on it); about 4.1M tokens in all. Open counting questions in the findings §7.
- [Research: Industry screen](issues/80-research-industry-screen.md): in twelve industries the audits never covered, PE share by brand row is collision repair 90%, urgent care 80%, physical therapy 80%, home services franchises 69%, child care 60%, oil change and auto service 50%, bowling and family entertainment 45% (64% if Atairos counted), hair salons 30%, golf 29%, landlord brands 25%, ski resorts 12.5%, funeral homes 0% (PE in local-name rollups); seven judged worth a full audit; five counting questions handed to "Launch industries"; about 1.10M tokens.
- [Product categories: vocabulary and assignment](issues/54-product-categories.md): the word is **industry** everywhere (industry pages; "category" never on the site); a brand gets its industries only from the industry brand lists and can sit in several; search matches names, owners and industry words and may add a meaning-based part (embedding model or an LLM such as DeepSeek, chosen in engine "Search and the demand log") that only ranks; no country filter (US businesses); licensed product lines are never brands; rollups are never industry page entries; the launch list split off to "Launch industries", which waits on the industry screen and a new bottom-up scan.

## Not yet specified

- **Store map** (first follow-up after launch, ruled 2026-11-06 in "Brand and chain model"): stores from brand store locators (selector producers), each with its address and brand, the brand's verdict labeled as the brand's, and a line saying the store's operator isn't checked; open map tiles; a geographic index; monthly re-crawl. No operators.

- **Seeding plan** for chains and brands: sources, order and runbook. ADR 0004 says it follows the category audit; it replaces nothing in `pre-launch-seeding.md`, which stays as the parked local plan.
- **BDC lenders on brand pages**: how a PE-owned chain's page shows which public funds lend to it, once engine "BDC discovery and Schedule of Investments parsing" closes (first follow-up, ADR 0004). Engine resolved it 2026-11-16: lenders are BDCs and their joint ventures, one edge per BDC and borrower with every tranche; borrowers are often holding companies, and a trailing dba or aka in the borrower name is stored as `other_name` ("dba Dental365"), which this follow-up can use to link a loan to a brand. Also open here: whether a brand counts as "checked" only after the BDC Schedules' latest complete pass.

## Out of scope

- **Property managers** (Greystar and similar): ruled out 2026-11-16 in "Product categories" (Q6), because a manager's page would report the manager's owner, not the building's.
- **Accounts, follows, paid alerts and billing**: a later map. The alert price is open until `monetizationideas.md` is updated (decisions.md §14).
- **Barcode scanning and a native app**: later (ADR 0004).
- **Local businesses and retirement**: parked in the [local-businesses](../local-businesses/map.md) and [retirement](../retirement/map.md) maps.
- **Housing search** (buildings and houses by address, and who owns or runs them): its own parked [housing map](../housing/map.md), ruled 2026-11-07 in engine "Funds and their investment firm". Landlords that rent under their own name were screened in "Research: Industry screen" (25% PE by brand row); whether they launch is "Launch industries".
- **Outreach and partnerships** (Worse on Purpose, creators): the developer's call, not a spec question.
