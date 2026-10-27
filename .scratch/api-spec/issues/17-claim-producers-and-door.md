# Claim producers and the claims door

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

Which components produce claims (LLM extraction, the BDC parser, bulk ETLs, roster selectors), what is the "verbatim quote" for each kind, and how do claims physically enter through the one door?

## Context

- **The door**: CLAUDE.md:24 says all connector output enters via `POST /internal/claims` "or its service equivalent"; but connectors emit RawDocuments via `store_document` (connector-dev SKILL:15; architecture-study-notes.md:12) and `extract_claims` writes claim rows itself (evidence_layer_plan.md:180). HTTP or in-process service? Batched? Default: in-process `ingest_claims()`; HTTP route is a thin wrapper.
- **Roster/portfolio claims — selectors or LLM?** build_roadmap.md:95 ("structured hints", selector configs), :101 ("every match publishes an operates_location_of claim"); research_flows.md:16,18 ("a few dollars of extraction"); connector-dev SKILL:22. If code emits them, that's another non-LLM producer like bdc_soi.
- **Bulk structured claims (Form 5500, NPPES)**: what is the quote/document/offset for a CSV-row claim (RawDocument shape: one row per document, content = header + row)? Do these pass `verify_citations` and the door? (build_roadmap.md:113; research_flows.md:124–125; connector-dev SKILL:18).
- **NPPES: entity, hint, or claim?** build_roadmap.md:88 (census → entities + aliases); research_flows.md:34 ("a hint for retrieval, not a claim") vs :72 (NPPES other-name counted as a verifying source); connector-dev SKILL:18 (ETL → claims). Because NPPES self-verifies, an alias field alone would publish a verified link.
- **Store-locator JSON APIs**: allowed? JSON documents? Quotes against JSON?
- **"Resolution hints" / "structured hints" / "enrichment structs"** (build_roadmap.md:95; research_flows.md:34; connector-dev SKILL:14): no contract or table exists for any.
- Record a `producer` (llm|parser|etl|selector) on claims?
