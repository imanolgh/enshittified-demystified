# Docs governance and definition of done

Type: grilling
Status: open
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
