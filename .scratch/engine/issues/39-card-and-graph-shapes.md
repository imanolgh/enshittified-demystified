# Claim card and graph output shapes

Type: grilling
Status: open
Blocked by: 26, 27, 68  (Edge lifecycle: ending, retraction and staleness; Category precedence and public companies; Category storage and recompute)
Map: [engine](../map.md)

## Question

What do the public output models contain — the business card, the per-claim receipt, edges, and the graph response — and what may be shown from stored documents?

## Context

- **"Claim card" means two things**: step1 guide@HEAD:92 (one claim + quote + provenance) vs evidence_layer_plan.md:203 (business-level card: category, separation degree, sponsor, date, N sources) vs decisions.md:58 (verdict, ownership type…). Name both.
- EdgeOut lost `ownership_type` (ADR 0001); nothing replaces it (category, separation degree, last confirmed, end date?).
- Card contents needed: chains, formerly-PE history, last-confirmed, owner-type-not-confirmed, sources-disagree links, checked date, coverage state, PC jargon hooks; card shapes for rollups, funds, BDCs, retirement plans.
- **Graph endpoint** (build_roadmap.md:121; evidence_layer_plan.md:204): depth cap value; both directions (clinic→DSO→PE firm←lends_to←BDC); relation filters; ended/history edges; node cap for hubs with thousands of locations.
- **Document receipts**: re-serve archived copies (copyright risk for news) or only URL + quote + retrieved_at + sha? pre-launch-seeding.md:119 requires cards to resolve to stored documents.
- `ConfigDict(from_attributes=True)` for ORM-built outputs.
- **Chains and brands** (added 2026-11-04, ADR 0004): output shapes for a brand, a chain, a category page and the public deal feed. Their wording is in chains-and-brands "Card wording and the how-this-works page", the pages in "Website pages and shareable cards".
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): the graph has two hop kinds (`owned_by`, `operated_by`) plus non-hop money edges; a store shows both the brand verdict and the store verdict, and code can say whether the store is company-run or franchised (glossary "Operator").
- **From chains-and-brands "Brand and chain model"** (2026-11-06): one verdict per card at launch, the brand's. The store map (follow-up) shows the brand's verdict on each pin, labeled as the brand's; a second, operator verdict waits for operators.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): a merged entity's card and graph redirect to the survivor's; a `closed` entity (store-map follow-up) still shows its history.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): the card names the firm that manages a PE fund through its `managed_by` edge without adding a hop, and one (brand, PE owner) row covers a fund and its firm (Jersey Mike's two Blackstone funds give one Blackstone row). Whether and how the card shows a firm's listed parent ("part of Blackstone Inc. (NYSE: BX)") is this ticket's.
- **From "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended; notes in evidence_layer_plan.md §4 `claims` and `edges`): a card may list several co-owners (THL and Linden at Smile Doctors), an owner line marked sources disagree with each side's links (edge confidence `sources_disagree`) while the category stands, and pending deals (announced, not completed; ended by `terminated` or 18 months). The shapes for these are this ticket's.
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): a card may show every co-owner with its own chain label, the ticker beside a PE-owned public company (Jersey Mike's, Chewy), PE holders of a public company with their stake ("3G Capital, a PE firm, holds 22% of voting power"), and an unconfirmed controlling owner beside a PE minority stake. The shapes are this ticket's.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): a card can be in the state "not yet checked" (no completed check and no PE found), showing any owner found so far; every other non-PE result carries its checked date.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): a claim's receipt links to its child document (a Schedule row, a locator record, a bulk row), which shows its parent filing or file.
