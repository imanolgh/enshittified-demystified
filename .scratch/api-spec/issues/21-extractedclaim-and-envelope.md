# ExtractedClaim and the extraction result envelope

Type: grilling
Status: open
Blocked by: 18  (Claim identity and resolving extracted names)
Map: [api-spec](../map.md)

## Question

What exactly does the LLM return — the `ExtractedClaim` model and the result envelope — and where does `no_evidence_found` live and at what granularity?

## Context

- **Envelope** (step1 guide@HEAD:74–81): (1) `ExtractionResult` with `claims` + `no_evidence_found: bool` + a model_validator (empty ⟺ flag), or (2) empty list = no evidence. research_flows.md:61 adds a per-predicate `{"no_evidence_for": ["lends_to"]}`; bdc-parser adds per-section/per-filing. Pick one shape and one granularity (per document set, per predicate, per section) and how each maps to a category / "checked".
- **ExtractedClaim leftovers** (guide@HEAD:70–72): `ConfigDict(frozen=True)`? Do `extraction_model`/`extracted_at` ride on the model or get attached by the task (argument for the task: the LLM shouldn't self-report its model)?
- **Document reference**: per-request labels (D1…Dn) mapped by code to document_id/sha (default).
- Field inventory from the guide: subject, predicate, object (names, min_length 1), verbatim_quote (required, meaningful min_length), event_date (optional), value (typed per "Claim value schemas…"), doc_sha. `ownership_type` removed (ADR 0001).
- `no_evidence` / `no_evidence_found` / `no_evidence_for` naming drift (build_roadmap.md:117; research_flows.md:61).
- Pydantic conventions: StrEnum, frozen, `extra="forbid"`, tz-aware datetimes.
