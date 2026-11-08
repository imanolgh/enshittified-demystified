# Category storage and recompute

Type: grilling
Status: resolved
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
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): moved here: recomputing only the affected edges (incremental re-derivation), writing events only when something visible changes, and re-deriving edges after an entity type change, a claim re-resolution or a merge. Edges are one row per ownership period, changed in place, with phases `pending|active|unconfirmed|ended`; only `active` rows count toward categories. This ticket is now takeable.

## Comments

### Round 1 (2026-11-07)

Scale noted: launch has about 374 brands (audit rows); local businesses, if unparked, could add millions of locations.

- **Stored, not computed on read** (Q1): an `entity_categories` table, one current row per brand (`category`, `confidence`, `checked_on`, `deciding_owner_id`, `computed_at`), changed in place. An events row only when the category or its confidence changes; `checked_on` advances quietly on each re-check. Companies and locations get rows only when a product needs them; a brand's walk passes through companies without storing theirs (Dunkin': `pe_owned`, verified, decided by Roark through Inspire Brands).
- **PE owner rows and formerly-PE history** (Q2; name chosen after the developer suggested `entity_pe_owners_history`): `entity_pe_owner_periods`, one row per brand, PE owner and period (`pe_owner_id`: the firm, or the fund when it has no `managed_by` edge; `separation_degree`, the shortest path; `stake_role` control or minority; `confidence`; `phase` active, unconfirmed or ended; `started_on`, the latest of the chain's hop starts; `ended_on`; `end_reason`). Ended rows are the "formerly PE-owned {years}" history; an unconfirmed row shows "last confirmed". `_history` was turned down because most reads are current (Jersey Mike's current owner) and the other tables keep current and past rows together without a suffix. Chains aren't stored; the card walks the edges on read.
- **Triggers and spread** (Q3): an edge's visible change (including phase), an owner kind change, a check completing or withdrawn, and a merge, unmerge, type change or re-resolution (after its edges are re-derived). Code walks edges downward from the changed entity to every brand it owns, directly or through companies, and recomputes each in its own Celery task, queued in chunks (size: "Operational identity, budgets and guardrail values"). Edge re-derivation is incremental: only the touched pairs and relations; events only on visible change.
- **Nightly drift check** (Q4): a nightly task recomputes every stored brand from scratch and compares; a difference is fixed with events rows and raises an operational alert, because it means a missed trigger (a bug). Seconds at launch scale; sampled or chunked later.
- **Checked date and fallback** (Q5): `checked_on` = the oldest completed required run, recomputed when a run completes or a withdrawal retracts the reads a run relied on; no complete check gives `not_yet_checked` unless PE was found; a withdrawal falls back through the same recompute.

## Answer

Resolved 2026-11-07 in a grilling session (one round, recorded under Comments).

- **Stored:** `entity_categories`, one current row per brand (`category`, `confidence`, `checked_on`, `deciding_owner_id`, `computed_at`), changed in place; events only when the category or its confidence changes, while `checked_on` advances quietly. Companies and locations get rows only when a product needs them.
- **PE owners:** `entity_pe_owner_periods`, one row per brand, PE owner (firm, or fund without a manager) and period, with `separation_degree` (shortest path), `stake_role`, `confidence`, `phase` (`active|unconfirmed|ended`), `started_on`, `ended_on`, `end_reason`. Ended rows are the "formerly PE-owned {years}" history. Chains aren't stored; the card walks the edges on read.
- **Recompute:** owner kinds (including inherited fund kinds), then edges (re-derived only for touched pairs and relations), then categories and PE owner periods for every brand reached by walking edges downward from the changed entity, each in its own Celery task, queued in chunks. Triggers: a visible edge change, an owner kind change, a check completing or withdrawn, and merges, unmerges, type changes and re-resolutions.
- **Drift check:** a nightly full recompute compares with what's stored; any difference is fixed with events rows and raises an operational alert (a missed trigger is a bug).
- **Checked date:** `checked_on` is the oldest completed required run; with none, `not_yet_checked` unless PE was found; withdrawals fall back through the same recompute.
- Docs: evidence_layer_plan.md §4; ADR 0001 separation-degree note; build_roadmap.md Step 8; conformance-tests skill. No new ADR, no glossary change.

Handed on:
- "Claim card and graph output shapes": reads the two tables, walks chains on read.
- "Events and the public changelog": category and confidence events; quiet `checked_on`; drift fixes.
- "Celery topology": recompute tasks, chunking, the nightly drift task.
- "Operational identity, budgets and guardrail values": chunk size, drift alert.
- "API conventions, internal auth and operator surface": drift alerts.
- chains "Website pages and shareable cards": category pages and shares read the stored rows.
