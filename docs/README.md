# Project Documents Index

The project documents in this folder, in reading order, with the role of each (for both the developer and Claude Code). The whole application is **FastAPI / Python**; nothing is being built in Laravel.

| # | File | Role |
|---|---|---|
| 1 | `painpoints.md` | The why — PE + PC pain research with quotes; source of user constituencies and demand validation |
| 2 | `marketgaps.md` | The what — product/opportunity analysis, five frameworks, top-3 ranking |
| 3 | `evidence_layer_glossary.md` | Sources and tools reference — every acronym, data source and tool, with pipeline-stage mapping. Domain vocabulary lives in `../GLOSSARY.md`, not here |
| 4 | `evidence_layer_plan.md` | The architecture — pipeline stages, schema, FastAPI stack (Laravel equivalents noted for learning only), guardrails; §1 is the anti-hallucination principle, §4 the schema |
| 5 | `research_flows.md` | The system in motion — scenarios A0–A3 (PE) and B1–B3 (PC), cross-cutting mechanics |
| 6 | `stack_fastapi.md` | Chosen stack blueprint |
| 7 | `decisions.md` | Decision log — §11 seeding strategy, §5 regulatory line, §7 evidence-is-free, §13 authorship, etc. |
| 8 | `build_roadmap.md` | Build-order reference until `.scratch/api-spec/spec.md` exists: "Step N" references resolve here, and where it differs from `evidence_layer_plan.md` on build order, the roadmap wins. When the spec lands, the spec owns build order and this file moves to `docs/archive/` |
| 9 | `monetizationideas.md` | Pricing model and free/paid line — canonical for pricing |
| 10 | `pre-launch-seeding.md` | Launch data plan — coverage states, category tiers, workstreams W1–W8, readiness checklist. Launch = roadmap engine **plus** these workstreams |
| 11 | `architecture-study-notes.md` | Study notes (learning material, to be archived). Part 2's folder proposals are rejected in favour of the CLAUDE.md layout |
| 12 | `python-types-primer.md` | Python types primer (learning material, to be archived) |
| — | `../GLOSSARY.md` | Canonical domain vocabulary (ownership, owners, evidence) |
| — | `adr/` | Architecture decision records, `NNNN-slug.md`. 0001 ownership categories computed by code; 0002 no manual review; 0003 one source type per publisher |
| — | `agents/` | How agent skills use this repo (issue tracker, domain docs) |
| 13 | (this file) | Index |

## When documents disagree

Precedence, highest first:

1. **ADRs** (`adr/`)
2. **`GLOSSARY.md`** — on what a term means
3. **`.scratch/api-spec/spec.md`**, once it exists — on what is built, how, and in what order
4. **`decisions.md`**
5. **`CLAUDE.md`** — a summary of the invariants, never their source
6. Every other document in `docs/`

Two rules go with the order:

- **The order only says which document is presumed right while a conflict is open.** Every conflict found is put to the developer, and the losing document is fixed. A known conflict is never left standing.
- **The spec cannot quietly override an ADR.** Changing an ADR's decision takes a new ADR that supersedes it.

Claude Code: consult these on demand and treat them as authoritative context. They are editable when the developer asks (requirements pivot, docs follow). If code and docs conflict, flag it to the developer rather than silently following either.
