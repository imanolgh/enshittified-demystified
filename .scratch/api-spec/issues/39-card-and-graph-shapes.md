# Claim card and graph output shapes

Type: grilling
Status: open
Blocked by: 26, 27  (Edge lifecycle: ending, retraction and staleness; Category precedence and storage)
Map: [api-spec](../map.md)

## Question

What do the public output models contain — the business card, the per-claim receipt, edges, and the graph response — and what may be shown from stored documents?

## Context

- **"Claim card" means two things**: step1 guide@HEAD:92 (one claim + quote + provenance) vs evidence_layer_plan.md:203 (business-level card: category, separation degree, sponsor, date, N sources) vs decisions.md:58 (verdict, ownership type…). Name both.
- EdgeOut lost `ownership_type` (ADR 0001); nothing replaces it (category, separation degree, last confirmed, end date?).
- Card contents needed: chains, formerly-PE history, last-confirmed, owner-type-not-confirmed, sources-disagree links, checked date, coverage state, PC jargon hooks; card shapes for rollups, funds, BDCs, retirement plans.
- **Graph endpoint** (build_roadmap.md:121; evidence_layer_plan.md:204): depth cap value; both directions (clinic→DSO→PE firm←lends_to←BDC); relation filters; ended/history edges; node cap for hubs with thousands of locations.
- **Document receipts**: re-serve archived copies (copyright risk for news) or only URL + quote + retrieved_at + sha? pre-launch-seeding.md:119 requires cards to resolve to stored documents.
- `ConfigDict(from_attributes=True)` for ORM-built outputs.
