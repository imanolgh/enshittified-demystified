# Mechanical docs sweep

Type: task
Status: open
Blocked by: 02  (Docs governance and definition of done)
Map: [api-spec](../map.md)

## Question

Apply the ~80 pure wording fixes the 2026-10-26 inventory found (no decision needed), so later tickets aren't wading through noise. Whatever "Docs governance and definition of done" rules about archiving files decides which of these are worth doing.

## Checklist (from the inventory; line numbers as of 2026-10-26)

- **docs/README.md**: :3 "fifteen" documents; :13 `stack_laravel.md` (deleted 2026-10-16; also decisions.md:8,93); :20 `step1-contracts-guide.md` (deleted 2026-10-26); :15 roadmap as "THE working plan… assistant contract, learning ledger".
- **build_roadmap.md**: hand-writing/learning wording at :2, :11, :13, §1 (:17–31), :51, :57, :79, :85, :107, :145, :159, :161, :173, every "Teaches:", §9 :181; :37 "uv (or poetry)"; :42 and :77 `connectors/…` → `app/source_connectors/`; :46 "ten .md"; :59 `str, Enum` and Step 1 list lacks OwnerKind/BusinessCategory/Confidence/envelope; :71 "You write the prompt"; :73 "Group verified claims" → accepted; :11/:117 "delegated exception"; :127 "Review" in Phase 4 title; :133 Step 26 body; :142 "claim status `unsupported`" → rejection_reason; :149 "Ownership-type agreement rate".
- **decisions.md**: :10 learning investment; :12 review-UI gap; :34 Tier 1 "(all get NPPES)" includes vets (contradicts :85); :58 card "verdict, ownership type, sponsor"; :87 "review-queue follow-ups"; :89 "review throughput"; :93 §12 reading order.
- **evidence_layer_plan.md**: :31 "(or arq)"; :40 "hand-written"; :41, :287 admin/review UI rows; :56, :151 OpenCorporates in Stage 1 (deferred); :65–67 WARN/CourtListener/GDELT not marked deferred; :179 "classification is ambiguous"; :187 "status `unsupported`"; :190 "verified claims"; :200 Stage 6 `source_type = submission`; :214 "Stage 3 classification", "LLM interprets parsed tables"; :216 "Ownership-type taxonomy"; :239 "minimal review view", ramp-up; :261 "`unknown` state".
- **stack_fastapi.md**: :2, :8, :27, :45, :51, :64 review UI/queue; :39 "ambiguity → review" + OpenCorporates; :50 learning; :18 "(or arq)".
- **evidence_layer_glossary.md**: :4 "Stage 6 Human Review"; :145 review; :169–170 "Review panel"; :174–175, :196–197 Jev ownership-type/review routing; :29 BDC "then 3"; :57 NAIC "Phase 5"; :192–193 deferred sources unmarked.
- **research_flows.md**: :25 "(status `queued`)", :34 "Item status → resolved", :36 "item status ambiguous" → stage/result; :34 "DSO entity" → rollup; :78 percentages >100% and omit sources_disagree; :110 GDELT; :131 `parse_soi` vs :132 `bdc_soi`.
- **pre-launch-seeding.md**: :14 "single authoritative source" (roster isn't official); :88 W5 review queue; :94 W8 body; :106 review-queue time; :115 "review queue drained"; :102 "BDC parse" as LLM cost.
- **architecture-study-notes.md**: :12, :113 `app/core/` "developer-only".
- **python-types-primer.md**: :55, :107 two-source rule omits domain.
- **monetizationideas.md**: :101 "ownership type (PE / conglomerate / …)".
- **marketgaps.md**: :24 "Verified independent"; :82 "unknown" verdict (wording only; substance in "Product-doc contradictions").
- **GLOSSARY.md**: :50 "or its sources disagree" → same-rank contradictions only (ADR 0001:9, ADR 0002:12).
- **ADR 0002**: :15 "claim status `unsupported`" vs its own :21 (`rejection_reason`).
- **Skills**: bdc-parser :3, :6, :25; conformance-tests :8; connector-dev :3, :10, :20–26, :32–33; doc-digest :3, :8, :24 — unless "Docs governance…" rewrites/retires them.
- **PROGRESS.md**: :18–20, :29.
- **Across docs**: GLOSSARY-avoided terms in active use — "sponsor" as an entity/card label (evidence_layer_plan.md:203; decisions.md:58), "DSO" for non-dental rollups, "consolidator", "platform", "Unknown" (pre-launch-seeding.md:16), "ownership type"; `no_evidence` / `no_evidence_found` / `no_evidence_for` (resolve per "ExtractedClaim and the extraction result envelope").

## Added by "Docs governance and definition of done" (2026-10-29)

- **docs/README.md**: already fixed (dead rows, count, roadmap role) — skip its checklist line.
- **Archive**: create `docs/archive/`; move `architecture-study-notes.md` and `python-types-primer.md` there (skip their wording fixes above); update README rows 11–12. `build_roadmap.md` is **not** moved yet — that happens when the spec lands; still do its wording fixes only if cheap, since it becomes history.
- **PROGRESS.md**: delete, after confirming each "Rulings" bullet is recorded elsewhere (predicates → CLAUDE.md; FastAPI-only → decisions.md §1; launch scope, pricing, first connector → check); record any that isn't in the right doc first. Skip its checklist line.
- **evidence_layer_glossary.md**: retitle as the sources and tools reference; replace domain-term definitions that duplicate `GLOSSARY.md` with links.
- **Skills**: `doc-digest` → retire (delete `.claude/skills/doc-digest/`, remove mentions); `connector-dev` → rewrite framing as Claude's connector-building skill (house style, fixtures, live check per CLAUDE.md definition of done); `bdc-parser` → drop "the ONE delegated component"/hand-check loop (deeper XBRL rewrite waits for "BDC discovery and Schedule of Investments parsing"); `conformance-tests` → drop "developer runs them".
- **decisions.md** :8, :93 — drop `stack_laravel.md` refs; §1 keeps "Laravel was evaluated and rejected".

## How to resolve

AFK. Make the edits, then append `## Answer` listing what changed and anything skipped (with why). No commits.
