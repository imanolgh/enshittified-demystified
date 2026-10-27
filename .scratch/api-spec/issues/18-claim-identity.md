# Claim identity and resolving extracted names

Type: grilling
Status: open
Blocked by: 13, 17  (Entity lifecycle: status, merges and renames; Claim producers and the claims door)
Map: [api-spec](../map.md)

## Question

How do names in extracted claims become entity ids, where in the pipeline that happens, what happens to a claim whose subject/object is unresolved or ambiguous, and what exactly is hashed for claim uniqueness?

## Context

- Extraction-time claims carry names (step1 guide@HEAD:57,61–63); the DB stores entity ids (evidence_layer_plan.md:100,105); research_flows.md:56–59 shows the LLM emitting `ent_…`/`d_…` ids. What does the LLM receive (target entity + related-entity handles?) and return?
- **Pipeline shape**: evidence_layer_plan.md:16,144–195 describe only an entity-first pipeline; most flows are document-first: build_roadmap.md:77 (`retrieve → extract → verify → publish`, no resolve), research_flows.md:16–17 (A0), :101 (A3), :132–134 (B1b: claims first, borrowers resolved after). No stage resolves claim names before scoring.
- **Unresolved/ambiguous object** ("Sponsor X" comes back ambiguous under the ADR 0002 rule): stored with null object, held, or dropped?
- **Uniqueness hash** (CLAUDE.md:29): over names or resolved ids? `doc_sha` or `document_id`? Serialization? Hash stability across merges (ids change on merge; names collide across aliases).
- **Field-name drift**: quote / verbatim_quote, doc / doc_sha / document_id, predicate / relation (CLAUDE.md:29; evidence_layer_plan.md:106,115; build_roadmap.md:69; research_flows.md:57; bdc-parser SKILL:13). Pick canonical names.
- Missing claim columns: raw subject/object names, `prompt_version`, extraction run id, what `quote_offset` points into (original vs normalized text), page number.
