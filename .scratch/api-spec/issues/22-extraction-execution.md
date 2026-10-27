# Extraction execution

Type: grilling
Status: open
Blocked by: 21  (ExtractedClaim and the extraction result envelope)
Map: [api-spec](../map.md)

## Question

How does extraction run: per document or per entity, Batch API vs synchronous, which models and when to escalate, what goes in a request, chunking and caching, failure handling, re-extraction, and what it costs?

## Context

- **Unit of extraction**: research_flows.md:52 says one multi-document call per entity; extractions are cached "by document sha256" (evidence_layer_plan.md:229). A 500-location roster relevant to 500 entities: extract once entity-agnostic, or per (document, entity)?
- **Batch vs sync**: A2 must be synchronous; Batch API results are async (most within 1h, max 24h), arrive in any order and can expire — seeding needs submit → poll → resume; a blocking `retrieve → extract → verify → publish` chain can't wait on it.
- **Models and escalation**: CLAUDE.md:7 "Opus-class for conflicts"; evidence_layer_plan.md:179 "…or classification is ambiguous". Classification is gone (ADR 0001) and conflicts publish as "sources disagree" (ADR 0002) — what triggers escalation now, if anything? Exact model ids, effort level.
- **Structured output mechanics** (from the gap analysis; verify with the claude-api skill): `output_config.format` structured outputs; forced `tool_choice` may 400 on current models incl. Batches; native citations can't combine with `output_config.format`; sampling params may 400 on recent API versions → cache key (sha, prompt_version, model).
- **Request contents**: target entity + aliases, related-entity handles, document labels, predicate role definitions, self-description instruction (ties to "Claim identity…").
- **Chunking & prompt-cache layout**: chunk size/overlap, quotes crossing chunk boundaries, stable cached prefix.
- **Failure handling**: ">5% malformed → batch flagged" (research_flows.md:65) — under ADR 0002 "flagged" must mean an operational alert / halt / retry; also `refusal` and `max_tokens` stop reasons.
- **Re-extraction policy** when prompt or model changes.
- **Cost figures disagree**: evidence_layer_plan.md:229 (cents to tens of cents per entity; "real money at 100k") vs decisions.md:89 / pre-launch-seeding.md:102 (low hundreds total; the latter still counts BDC parsing as LLM cost) vs research_flows.md:18 ("a few dollars" for national roster seeding).
- Load the `claude-api` skill when working this ticket.
