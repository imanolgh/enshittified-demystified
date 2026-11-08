# Graph endpoint and non-brand output shapes

Type: grilling
Status: open
Blocked by: 39  (Claim card and graph output shapes)
Map: [engine](../map.md)

## Question

What does the graph endpoint return (depth cap, directions, relation filters, history edges, node caps for hubs), and what are the output shapes for a category page, the public deal feed, and company, fund and BDC pages?

## Context

- Split from "Claim card and graph output shapes" on 2026-11-07 (developer ruling, to keep each ticket to one session). The brand card, receipt and edge shapes are settled there.
- **Moved from that ticket:** graph endpoint (build_roadmap.md Step 23; evidence_layer_plan.md): depth cap value; both directions (clinic → DSO → PE firm ← `lends_to` ← BDC); relation filters; ended and history edges; a node cap for hubs with thousands of locations. Card shapes for rollups, funds, BDCs and retirement plans (retirement parked).
- **Chains and brands** (ADR 0004): output shapes for a category page and the public deal feed; wording is in chains "Card wording and the how-this-works page", the pages in "Website pages and shareable cards".
- **From "Category storage and recompute"** (2026-11-07): category pages and shares read stored `entity_categories` rows; formerly-PE history comes from ended `entity_pe_owner_periods` rows.
- **From "Entity lifecycle"** (2026-11-06): a merged entity's card and graph redirect to the survivor's; a `closed` entity still shows its history.
- At launch every page is a brand page ("Brand and chain model"), so company, fund and BDC pages may be later; whether they exist at launch is part of the question.
