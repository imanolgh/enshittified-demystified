# ExtractedClaim and the extraction result envelope

Type: grilling
Status: resolved
Blocked by: 18  (Claim identity and resolving extracted names)
Map: [engine](../map.md)

## Question

What exactly does the LLM return — the `ExtractedClaim` model and the result envelope — and where does `no_evidence_found` live and at what granularity?

## Context

- **Envelope** (step1 guide@HEAD:74–81): (1) `ExtractionResult` with `claims` + `no_evidence_found: bool` + a model_validator (empty ⟺ flag), or (2) empty list = no evidence. research_flows.md:61 adds a per-predicate `{"no_evidence_for": ["lends_to"]}`; bdc-parser adds per-section/per-filing. Pick one shape and one granularity (per document set, per predicate, per section) and how each maps to a category / "checked".
- **ExtractedClaim leftovers** (guide@HEAD:70–72): `ConfigDict(frozen=True)`? Do `extraction_model`/`extracted_at` ride on the model or get attached by the task (argument for the task: the LLM shouldn't self-report its model)?
- **Document reference**: per-request labels (D1…Dn) mapped by code to document_id/sha (default).
- Field inventory from the guide: subject, predicate, object (names, min_length 1), verbatim_quote (required, meaningful min_length), event_date (optional), value (typed per "Claim value schemas…"), doc_sha. `ownership_type` removed (ADR 0001).
- `no_evidence` / `no_evidence_found` / `no_evidence_for` naming drift (build_roadmap.md:117; research_flows.md:61).
- Pydantic conventions: StrEnum, frozen, `extra="forbid"`, tz-aware datetimes.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): the task sets `producer`, `producer_version` and `extraction_model`; the model's output never does (settles that leftover). The LLM emits only claims, never identity records. "Nothing found" rides in the door call, one per LLM request (a request can cover several documents); its shape is this ticket's.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): `ExtractedClaim` uses the §4 names: `subject_name`, `predicate`, `object_name`, `verbatim_quote`, `event_date`, `value`, plus the request's document label (`D1`) that code maps to `document_id`. Each name is the name as written in the document, never an id or handle. New field for this ticket to shape: a per-side mark saying the name is a person or a family (it only answers that); a marked unmatched name creates a `family` entity.

## Comments

### Round 1 (2026-11-06)

Boundaries: `value` is "Claim value schemas"; quote length and date plausibility are "Citation verification rules"; where "no evidence found" is stored and how it becomes "checked" is "Checked and coverage states"; request mechanics and schema enforcement are "Extraction execution"; whether quoted owner self-descriptions become a second output list is "Owner kind".

- **Envelope** (Q1): the response is `claims: list[ExtractedClaim]`, possibly empty, with no flag. Code knows which documents went into the request and gives every document no claim cites the outcome `no_evidence_found`. "No lending evidence" is just no `lends_to` claim citing the document, so `no_evidence_for` goes; `no_evidence` and `no_evidence_for` are dropped as names. Storage, "checked", and documents whose claims were all rejected: "Checked and coverage states".
- **Unreadable is a failure** (Q2): an unparseable BDC section or filing is a parse failure with the alert from "Claim producers and the claims door", never `no_evidence_found` and never read. A Schedule that parses cleanly with no row for a borrower is read: no lending evidence in that filing. ADR 0002's BDC bullet and the bdc-parser skill corrected.
- **Fields** (Q3): `subject_name`, `subject_is_family` (default false), `predicate` (StrEnum), `object_name` (None only for `renamed_from`), `object_is_family`, `document_label` (`D1`…, mapped by code), `verbatim_quote`, `event_date` (Q4), `value` (validated against the predicate's schema). `frozen=True`, `extra="forbid"`. No producer, model, timestamp, entity id, document id, `ownership_type` or free-text note.
- **Date precision** (Q4, option a): the LLM returns `"2019"`, `"2024-04"` or `"2024-04-30"`; the claim stores `event_date` as the first day of that period plus `event_date_precision` (`year|month|day`). Plausibility and datelines: "Citation verification rules".
- **Failures** (Q5): a bad item (unknown label, name not in the document, bad date, `value` failing its schema) is dropped and logged; the rest stands. A response that didn't finish (token limit) or doesn't parse fails as a request, retried by "Extraction execution", and gives no document `no_evidence_found`. A document cited only by dropped items gets no outcome. The alert threshold for dropped items is "Operational identity and guardrails" (the docs' 5% is a starting figure).
- **Resolution plan detail** (confirmed): a family mark on a side where the role table allows no family (the subject of `owned_by`) drops the item.

## Answer

Resolved 2026-11-06 in a grilling session (one round plus the resolution plan, recorded under Comments).

- **Envelope:** `claims: list[ExtractedClaim]`, possibly empty, no flag. Code gives each document in the request that no claim cites `no_evidence_found` (the only spelling), and only from a response that finished and parsed.
- **Unreadable documents fail.** An unparseable BDC section or filing, or a failed LLM response, is a failure (alert or retry) and never `no_evidence_found`.
- **`ExtractedClaim`:** `subject_name`, `subject_is_family`, `predicate`, `object_name` (None only for `renamed_from`), `object_is_family`, `document_label`, `verbatim_quote`, `event_date`, `value`; frozen, `extra="forbid"`; the task and door add everything else.
- **Dates** keep the document's precision: `event_date` (first day of the period) plus `event_date_precision` (`year|month|day`).
- **Bad items** are dropped and logged (including a family mark where the role table allows no family); a document cited only by dropped items gets no outcome.
- No new ADR, no glossary change.

Handed on:
- "Owner kind": a possible self-description list in the envelope.
- "Claim value schemas": per-predicate `value` schemas.
- "Extraction execution": failed responses, retries, schema enforcement.
- "Citation verification rules": quote length, date plausibility, datelines.
- "Conflict, succession and co-investors": date precision.
- "Checked and coverage states": storing the per-document outcome, documents whose claims were all rejected.
- "BDC discovery and Schedule of Investments parsing": parse failures.
- "Operational identity and guardrails": the dropped-item alert.
- "Mechanical docs sweep": `no_evidence` naming drift.
