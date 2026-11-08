# Category storage and recompute

Type: grilling
Status: open
Blocked by: 26, 27, 28  (Edge lifecycle: ending, retraction and staleness; Category precedence and public companies; Checked and coverage states)
Map: [engine](../map.md)

## Question

Are categories and separation degrees stored or computed on read, what does the stored row per (brand, PE owner) hold, how is a recompute fanned out after an owner kind or hop changes, and where does formerly-PE history live?

## Context

- Split from "Category precedence and storage" (now "Category precedence and public companies") on 2026-11-07 (developer ruling, to keep each ticket to one session).
- **Moved from that ticket:** ADR 0001:13 implies a stored (business, PE firm) row with separation degree; columns undefined. Is the category itself stored (with checked_at and the deciding chain) or computed on read? Recompute bookkeeping after an owner-kind change (async fan-out above N businesses). Where does formerly-PE history live? (evidence_layer_plan.md §4; build_roadmap.md Steps 7 and 9)
- **From "Funds and their investment firm"** (2026-11-07): the stored (brand, PE owner) row is keyed to the firm when the fund has a `managed_by` edge, else to the fund; a fund's inherited owner kind is computed with no evidence row.
- **From "Conflict, succession and co-investors"** (2026-11-07): edge confidence gains `sources_disagree`; a brand's category is `sources_disagree` only when its contested readings give different categories, so computing a category means evaluating each reading. Endings, restarts and the 18-month clocks come from "Edge lifecycle".
- **From "Category precedence and public companies"** (2026-11-07): what is computed (precedence, public-company rules, which entities carry a category; launch computes brands only) is settled there; this ticket decides how it is stored and kept current.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): categories gain `not_yet_checked`; the checked date (oldest completed required run) has to reach the stored category, and a withdrawn producer version can drop a brand back to its previous complete check or to "not yet checked". This ticket now waits only on "Edge lifecycle".
