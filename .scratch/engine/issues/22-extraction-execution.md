# Extraction execution

Type: grilling
Status: open
Blocked by: 21  (ExtractedClaim and the extraction result envelope)
Map: [engine](../map.md)

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
- **Cost estimate for chains and brands** (added 2026-11-04; usage figures are assumptions, not measurements):
  - Anthropic prices checked 2026-11-04 against https://platform.claude.com/docs/en/about-claude/pricing (per million tokens, input / output; batch is 50% off and combines with caching): Opus 5.5 $4 / $20 (batch $2 / $10, cache read $0.20); Sonnet 5.5 $2 / $10 (batch $1 / $5, cache read $0.10); Haiku 5.5 $0.10 / $0.50 for prompts up to 100K tokens (batch $0.05 / $0.25; $0.50 / $2.50 above 100K).
  - Assumed per request: ~10k input tokens (document chunk plus prompt prefix) and ~2k output (claims, quotes and thinking). Per document: Haiku ~$0.001, Sonnet ~$0.02, Opus ~$0.04 in batch; double that without batch.
  - Assumed workload: ~1,000 brands × ~6 documents = ~6,000 requests. The brand count is the pivot proposal's unsettled figure (chains-and-brands "Product categories: vocabulary and assignment" and "Category brand lists and brand-level checked"); cost scales linearly with it. Top 30 × 10 categories would be ~300 brands, about a third of these figures.
  - One full seeding pass in batch: Haiku ~$6, Sonnet ~$120, Opus ~$240. Re-extraction after prompt changes means budgeting 2–3 passes.
  - Biggest swing: sending whole SEC filings instead of the relevant sections could multiply input several times over, so chunking (above) drives cost more than model choice.
  - Consistent with decisions.md §11's "few hundred dollars" for the parked local seeding.
- Load the `claude-api` skill when working this ticket.
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): "A2 must be synchronous" no longer applies, so nothing forces a synchronous extraction path; whether every extraction runs through the Batch API is this ticket's call. The batch-jobs and extraction-cache tables, their columns and retention are this ticket's.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): the LLM returns names as written, never ids, so a request needs no candidate list. The prompt may say which brand the documents were fetched for. Whether claims point at their extraction request (a column) is this ticket's, with the batch tables.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): the response is `claims: list[ExtractedClaim]`, possibly empty. A response that stopped at the token limit or doesn't parse is a failed request: this ticket retries it, and it gives no document `no_evidence_found`. How the schema is enforced (structured output or a tool) and how documents are labelled `D1`…`Dn` in a request are this ticket's.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): the extraction prompt also asks for `owner_descriptions` (owner's name as written, describing phrase as written, document label, quote); the model never names a kind.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): the prompt asks for an ownership claim for each owner the quote names as buyer or holder (a fund, its firm, or both: Dental365's quote gives `acquired_by` to The Jordan Company and to The Resolute Fund V), and a `managed_by` claim (fund → firm) when the quote says the fund is the firm's ("managed by", "advised by", "its affiliate, Cortec Group Fund VI, L.P."). The prompt draft words this.
- **From "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended; notes in evidence_layer_plan.md §4 `claims` and `edges`): the prompt returns a named seller, a sale release or a "Realized"/"Exited" listing as an `owned_by` claim with `holding: former` (dated like the deal); a stated 0% stake as an exit; and a deal called off as `acquired_by` with `deal_status: terminated`. When the quote that names the seller also says it keeps a stake ("Eagle Merchant Partners will retain a minority interest"), it returns only the `current` claim with that stake, because the claim hash ignores value fields. The prompt draft words this.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): each producer run writes one `document_reads` row per document it read, with outcome `cited`, `no_evidence_found`, `unreadable` (a failed response) or `claims_rejected` (every claim failed `verify_citations`), in the same door call.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): a re-fetch with unchanged extracted text costs no LLM call; a real text change is a new document version, and the LLM re-reads the whole of it (developer's choice: evidence can be anywhere), so facts still there get new claims.
