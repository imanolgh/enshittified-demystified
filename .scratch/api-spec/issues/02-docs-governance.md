# Docs governance and definition of done

Type: grilling
Status: resolved
Map: [api-spec](../map.md)

## Question

Under the new authorship model (decisions.md §13: Claude builds from a spec, the developer decides), which document wins when docs disagree, what happens to the old build-plan artifacts, and what does "done" mean for a piece of the build?

## Context (from the 2026-10-26 inventory)

- **Source-of-truth order is only pairwise today.** docs/README.md:15,21,25 (roadmap beats plan on build order; GLOSSARY beats evidence_layer_glossary); ADR 0001:3 and ADR 0002:3 supersede named sections; CLAUDE.md:3. No rule for GLOSSARY vs ADR, decisions.md vs ADR, or spec vs docs once the spec exists.
- **Fate of the roadmap.** build_roadmap.md now carries a "superseded" banner; decide whether it is archived, trimmed to design content, or kept as Step-N reference until the spec lands. Same for the learning ledger (§9) and evidence_layer_glossary.md vs GLOSSARY.md.
- **PROGRESS.md** (repo root) still says "developer hand-writes contracts.py" (:18–20) and claims Research/Pro tier "not in docs yet" (:29) though monetizationideas.md §3 has it. Keep, rewrite, or delete?
- **architecture-study-notes.md Part 2** (:3, :99–138) proposes a `database/` folder, `pydantic_models/` under `api/`, a requests/responses split; Claude recommended against; never ruled. CLAUDE.md structure decisions (settled 2026-08-31) may already answer it.
- **Definition of done** (CLAUDE.md:50,55; connector-dev SKILL:27–33; build_roadmap.md:85,159; conformance-tests SKILL:8; bdc-parser SKILL:8,22): does "done" still include the developer manually verifying one real lookup and being able to re-explain the module? Is the BDC acceptance loop (developer hand-checks 20 rows per fixture) still required? What is the agent-run equivalent of "verified against a real lookup"?
- **Skills' future**: connector-dev (flagged outdated), doc-digest ("so the developer can write the connector"), bdc-parser ("the ONE delegated component"), conformance-tests ("developer runs them") all encode the old contract. Rewrite, merge, or retire each?
- **Stale `stack_laravel.md` references** (README:13, decisions.md:8,93) — file deleted 2026-10-16.

## Answer

Resolved 2026-10-29 (grilling; all eight recommendations accepted).

1. **Precedence**: ADRs > `GLOSSARY.md` (terms) > `spec.md` once it exists (what/how/order of build) > `decisions.md` > `CLAUDE.md` (summary, never source) > other docs. The order only presumes a winner while a conflict is open; every conflict goes to the developer and the losing doc is fixed. The spec cannot override an ADR except via a superseding ADR. Recorded in `docs/README.md` "When documents disagree" + one line in `CLAUDE.md`.
2. **build_roadmap.md**: stays as the Step-N reference until `spec.md` exists; then the spec owns build order and the roadmap moves to `docs/archive/` with a banner pointing at the spec, cited by nothing new. No trimming in the meantime. Learning ledger (§9) and "Teaches:" lines are history.
3. **evidence_layer_glossary.md**: kept, re-roled as the **sources and tools reference**; domain-term definitions duplicating `GLOSSARY.md` are stripped to links (Mechanical docs sweep).
4. **PROGRESS.md**: deleted, after confirming each of its rulings lives elsewhere (the "parked" Research/Pro tier is already in monetizationideas.md §3). Progress is tracked by the map, then by build tickets.
5. **architecture-study-notes.md Part 2** (`database/`, `api/pydantic_models/`, requests/responses split): rejected in favour of the CLAUDE.md layout. It and `python-types-primer.md` move to `docs/archive/`.
6. **Definition of done** (recorded in `CLAUDE.md` working rules): (1) conformance tests on 2–3 real fixtures; (2) Claude runs one live lookup and records URL / response / claims in the build ticket; (3) BDC: automatic cross-check against SEC XBRL (DERA `soi.tsv`) where available — the developer's 20-row hand-check is dropped; (4) the developer's commit is the acceptance gate and where the re-explain bar is checked. Numeric bars → "Testing and acceptance bars".
7. **Skills**: `connector-dev` → rewrite as Claude's connector-building skill (house style, fixtures, live check); `doc-digest` → retire (superseded by `research`); `bdc-parser` → keep, drop "the ONE delegated component", deeper XBRL-first rewrite after "BDC discovery and Schedule of Investments parsing"; `conformance-tests` → keep, drop "developer runs them"; `registry-research` unchanged. Framing edits go to Mechanical docs sweep.
8. **Dead refs**: `stack_laravel.md` and `step1-contracts-guide.md` references removed; decisions.md §1 keeps "Laravel evaluated and rejected" without the file link.

**Done in this session**: `docs/README.md` rewritten (precedence section, roles for roadmap / sources reference / study notes, dead rows removed, renumbered); `CLAUDE.md` precedence line + definition of done.
**Handed to Mechanical docs sweep**: archive moves, PROGRESS.md deletion, glossary de-duplication, skill framing edits, decisions.md :8/:93 refs.
