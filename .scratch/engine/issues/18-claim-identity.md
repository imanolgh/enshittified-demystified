# Claim identity and resolving extracted names

Type: grilling
Status: open
Blocked by: 13, 17  (Entity lifecycle: status, merges and renames; Claim producers and the claims door)
Map: [engine](../map.md)

## Question

How do names in extracted claims become entity ids, where in the pipeline that happens, what happens to a claim whose subject/object is unresolved or ambiguous, and what exactly is hashed for claim uniqueness?

## Context

- Extraction-time claims carry names (step1 guide@HEAD:57,61–63); the DB stores entity ids (evidence_layer_plan.md:100,105); research_flows.md:56–59 shows the LLM emitting `ent_…`/`d_…` ids. What does the LLM receive (target entity + related-entity handles?) and return?
- **Pipeline shape**: evidence_layer_plan.md:16,144–195 describe only an entity-first pipeline; most flows are document-first: build_roadmap.md:77 (`retrieve → extract → verify → publish`, no resolve), research_flows.md:16–17 (A0), :101 (A3), :132–134 (B1b: claims first, borrowers resolved after). No stage resolves claim names before scoring.
- **Unresolved/ambiguous object** ("Sponsor X" comes back ambiguous under the ADR 0002 rule): stored with null object, held, or dropped?
- **Uniqueness hash** (CLAUDE.md:29): over names or resolved ids? `doc_sha` or `document_id`? Serialization? Hash stability across merges (ids change on merge; names collide across aliases).
- **Field-name drift**: quote / verbatim_quote, doc / doc_sha / document_id, predicate / relation (CLAUDE.md:29; evidence_layer_plan.md:106,115; build_roadmap.md:69; research_flows.md:57; bdc-parser SKILL:13). Pick canonical names.
- Missing claim columns: raw subject/object names, `prompt_version`, extraction run id, what `quote_offset` points into (original vs normalized text), page number.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): a door call carries identity records with keys (`r1`) valid only inside the call, and a code producer's claim can name its subject or object by key. Name resolution is then needed for LLM claims and for code claims that name an entity outside the call. Claims now carry `producer` and `producer_version`, which covers the missing `prompt_version`. Open for this ticket: whether the uniqueness hash includes the producer (a fixed version that reproduces the same claim currently dedupes to the old row, which keeps the old version).
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): the resolver only considers the entity types a predicate allows (role table), and a resolved claim whose types don't fit is rejected with `sanity_check_failed`. Where that check runs relative to resolution is this ticket's.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): merges add a pointer (`merged_into_id`) and rewrite nothing, so claims keep the entity ids they were written with; whether the uniqueness hash is over ids that may later be merged, and how two identical claims on a duplicate and its survivor count, is this ticket's. `renamed_from` has no object (`object_entity_id` nullable for it only; `value.former_name`). The type a claim-created entity starts with is this ticket's; the only later change is `company` → `investment_firm` or `fund` on a Form ADV match.
