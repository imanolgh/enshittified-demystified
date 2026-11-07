# Claim identity and resolving extracted names

Type: grilling
Status: resolved
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

## Comments

### Round 1 (2026-11-06)

Boundaries: how the resolver matches (lookup order, scoring, thresholds, normalization, fuzzy engine) is "Entity resolution algorithm"; the rest of what the LLM returns is "ExtractedClaim and the extraction result envelope"; what goes in a request is "Extraction execution".

- **Names as written** (Q1, reworded after the developer asked what "name" meant): for each side of a claim the LLM copies the words the document uses ("Subway", "Roark Capital"), never a database id or handle; code decides which entity row they mean. A vague phrase ("the company", "its sponsor") isn't a name; the LLM returns the name the document gives elsewhere. The name as written must appear word for word in the document; whether it must also be inside the quote is "Citation verification rules".
- **Stored names, resolved in the door** (Q2, option a): claims gain `subject_name` and `object_name` (only `renamed_from`'s object is empty; a keyed code-producer claim takes its identity record's main name). The door resolves them in the same call and writes `subject_entity_id`/`object_entity_id`, null when a name doesn't resolve. Claim content (names, quote, value, document) never changes. The ids are the resolver's current answer: code fills nulls when identity data arrives and may change an id when the resolver's rules improve, each change with an events row and an edge recompute. Merges never touch them (pointer).
- **Field names** (Q3): the §4 names stay (`predicate`, `verbatim_quote`, `document_id`, plus `subject_name`, `object_name`; edges keep `relation`). `ExtractedClaim` uses the same names except the request's document label (`D1`), mapped by code. `quote_offset` becomes `quote_start` and `quote_end`, character offsets into the stored `raw_text` (mapping from normalized text: "Citation verification rules"). No page column (page markers in stored text: "Document storage…"); whether a claim points at its extraction request is "Extraction execution". The mechanical docs sweep fixes the drift elsewhere.
- **Type checks** (Q4): the resolver only considers the types the predicate's role table allows on that side; `verify_citations` re-checks both types after resolution and rejects a misfit with `sanity_check_failed`.

### Round 2 (2026-11-06)

- **Unresolved names** (Q5, option a): one clear match → that id. No candidate → create an entity (type per Q6). Several candidates with no deterministic winner → ADR 0002's ambiguous rule applied to claims: id null, never create, never take the top candidate, retried automatically when identity data changes (timing: "Celery topology"). A null id (except `renamed_from`'s object) never counts toward an edge. Catching a vague phrase passed off as a name: "Citation verification rules".
- **Type of a created entity** (Q6, option a): a claim creates only a `company` or a `family`, never a brand, location, investment firm, fund, insurer or retirement plan. The LLM marks each side whose name as written is a person or family ("the Cathy family", "founder Jerry Pugh"); a marked side creates a `family`, everything else a `company`. The mark answers only "person or family, or not"; the field is "ExtractedClaim…"'s.
- **Hash** (Q7): `claim_hash` = sha256 of `[subject_name, predicate, object_name or "", document_id, verbatim_quote]`, whitespace collapsed. No entity ids (re-resolution and merges never change it), no producer (a fixed version replaces an old one only by withdrawing it and re-running), no `value`. The unique index skips retracted claims. Claims from one document count as one source; from different documents, separate sources ("Source independence and syndication"). CLAUDE.md's idempotency line updated.

## Answer

Resolved 2026-11-06 in a grilling session (two rounds, recorded under Comments).

- **Names as written.** For each side of a claim the LLM copies the words the document uses, never an id; the name must appear in the document. Claims store `subject_name` and `object_name`.
- **Resolution in the door.** The door resolves names to `subject_entity_id`/`object_entity_id` in the same call, filtering candidates by the role table; `verify_citations` re-checks the types (misfit → `sanity_check_failed`). Claim content never changes; the ids are the resolver's current answer, filled or improved by code with an events row and an edge recompute. Merges never touch them.
- **Unresolved names.** No candidate → create a `company`, or a `family` when the LLM marks the side as a person or family. Ambiguous → null id, never counts, retried automatically (ADR 0002 rule now covers claims). Claims never create brands, locations, investment firms, funds, insurers or plans.
- **Hash:** sha256 of `[subject_name, predicate, object_name or "", document_id, verbatim_quote]`, unique among non-retracted claims.
- **Field names:** the §4 names stay; `quote_offset` becomes `quote_start`/`quote_end` (offsets into `raw_text`); no page or request column.
- No new ADR, no glossary change.

Handed on:
- "Entity resolution algorithm": matching inputs, re-resolution after a rules change.
- "ExtractedClaim and the extraction result envelope": field names and the person-or-family mark.
- "Extraction execution": target-brand context in the prompt, a request link.
- "Citation verification rules": name-in-document check, vague phrases, offset mapping, type re-check.
- "Source independence and syndication": one document is one source.
- "Edge lifecycle": null ids, recomputes after re-resolution.
- "Events and the public changelog": the claim re-resolved event.
- "Celery topology": retry timing.
- "Owner kind": family entities from the LLM mark.
- "Mechanical docs sweep": field-name drift.
