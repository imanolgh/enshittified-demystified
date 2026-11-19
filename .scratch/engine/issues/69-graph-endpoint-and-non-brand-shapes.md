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
- **Chains and brands** (ADR 0004): output shapes for a category page and the public deal feed; wording is in chains "Card wording" (split 2026-11-18; the page itself is "The how-this-works page"), the pages in "Website pages and shareable cards".
- **From "Category storage and recompute"** (2026-11-07): category pages and shares read stored `entity_categories` rows; formerly-PE history comes from ended `entity_pe_owner_periods` rows.
- **From "Entity lifecycle"** (2026-11-06): a merged entity's card and graph redirect to the survivor's; a `closed` entity still shows its history.
- At launch every page is a brand page ("Brand and chain model"), so company, fund and BDC pages may be later; whether they exist at launch is part of the question.
- **From "BDC discovery and Schedule of Investments parsing"** (2026-11-16; section "BDC connector and Schedule parser" in evidence_layer_plan.md §5): BDC and joint-venture pages (if any) can show: the BDC's adviser (`managed_by`), its lending and position edges with every tranche from the newest Schedule (`value_document_id`), ventures it holds, and lenders that are ventures of a BDC.
- **From chains "Product categories: vocabulary and assignment"** (2026-11-16): industry pages list brands only, so a search for a rollup's own name ("Heartland Dental", whose practices keep local names) has no brand to show; what it shows, a company page or nothing yet, is this ticket's.
- **From chains "Alternatives and affiliate links"** (2026-11-17): the brand card of a PE-owned or PE minority stake brand gains an alternatives block: brands on the same industry list with a completed check, a non-PE verdict and no pending deal to a PE buyer, grouped by industry in list order, each with its verdict line and any live `affiliate_links` rows. Industry pages need a "no PE found" filter. Both are computed from `entity_categories` and list order.

