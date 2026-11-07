# Claim card and graph output shapes

Type: grilling
Status: open
Blocked by: 26, 27  (Edge lifecycle: ending, retraction and staleness; Category precedence and storage)
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
