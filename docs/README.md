# Project Documents Index

The fifteen project documents in this folder, in reading order, with the role of each (for both the developer and Claude Code). The whole application is **FastAPI / Python**; nothing is being built in Laravel.

| # | File | Role |
|---|---|---|
| 1 | `painpoints.md` | The why — PE + PC pain research with quotes; source of user constituencies and demand validation |
| 2 | `marketgaps.md` | The what — product/opportunity analysis, five frameworks, top-3 ranking |
| 3 | `evidence_layer_glossary.md` | Vocabulary — every acronym/source/tool, with pipeline-stage mapping |
| 4 | `evidence_layer_plan.md` | The architecture — pipeline stages, schema, FastAPI stack (Laravel equivalents noted for learning only), guardrails; §1 is the anti-hallucination principle, §4 the schema |
| 5 | `research_flows.md` | The system in motion — scenarios A0–A3 (PE) and B1–B3 (PC), cross-cutting mechanics |
| 6 | `stack_fastapi.md` | Chosen stack blueprint |
| 7 | `stack_laravel.md` | Rejected-path contrast (reference only — not being built) |
| 8 | `decisions.md` | Decision log — §11 seeding strategy, §5 regulatory line, §7 evidence-is-free, etc. |
| 9 | `build_roadmap.md` | THE working plan — 29 steps, 5 phases, assistant contract, learning ledger. "Step N" references resolve here; where it differs from `evidence_layer_plan.md` on build order, the roadmap wins |
| 10 | `monetizationideas.md` | Pricing model and free/paid line — canonical for pricing |
| 11 | `pre-launch-seeding.md` | Launch data plan — coverage states, category tiers, workstreams W1–W8, readiness checklist. Launch = roadmap engine **plus** these workstreams |
| 12 | `architecture-study-notes.md` | Study notes — layering/folder-structure Q&A between developer and Claude Code |
| 13 | `python-types-primer.md` | Python data structures and type annotations, angled at a PHP/Laravel background |
| 14 | `step1-contracts-guide.md` | Guide for roadmap Step 1 (`app/core/contracts.py`), incl. the 7-predicate ruling |
| — | `../GLOSSARY.md` | Canonical domain vocabulary (ownership, owners, evidence) — built by `/grill-with-docs`; wins over `evidence_layer_glossary.md` where they differ |
| — | `adr/` | Architecture decision records, `NNNN-slug.md`. 0001 ownership categories computed by code; 0002 no manual review; 0003 one source type per publisher |
| 15 | (this file) | Index |

Claude Code: consult these on demand and treat them as authoritative context. Since 2026-09-04 they are editable when the developer asks (requirements pivot, docs follow). If code and docs conflict, flag it to the developer rather than silently following either.
