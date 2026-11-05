# Claim producers and the claims door

Type: grilling
Status: resolved
Map: [engine](../map.md)

## Question

Which components produce claims (LLM extraction, the BDC parser, bulk ETLs, roster selectors), what is the "verbatim quote" for each kind, and how do claims physically enter through the one door?

## Context

- **The door**: CLAUDE.md:24 says all connector output enters via `POST /internal/claims` "or its service equivalent"; but connectors emit RawDocuments via `store_document` (connector-dev SKILL:15; architecture-study-notes.md:12) and `extract_claims` writes claim rows itself (evidence_layer_plan.md:180). HTTP or in-process service? Batched? Default: in-process `ingest_claims()`; HTTP route is a thin wrapper.
- **Roster/portfolio claims — selectors or LLM?** build_roadmap.md:95 ("structured hints", selector configs), :101 ("every match publishes an operates_location_of claim"); research_flows.md:16,18 ("a few dollars of extraction"); connector-dev SKILL:22. If code emits them, that's another non-LLM producer like bdc_soi.
- **Bulk structured claims (Form 5500, NPPES)**: what is the quote/document/offset for a CSV-row claim (RawDocument shape: one row per document, content = header + row)? Do these pass `verify_citations` and the door? (build_roadmap.md:113; research_flows.md:124–125; connector-dev SKILL:18).
- **NPPES: entity, hint, or claim?** moved out 2026-11-04 (adr 0004 split) to local-businesses "NPPES census load and census match".
- **Store-locator JSON APIs**: allowed? JSON documents? Quotes against JSON?
- **"Resolution hints" / "structured hints" / "enrichment structs"** (build_roadmap.md:95; research_flows.md:34; connector-dev SKILL:14): no contract or table exists for any.
- Record a `producer` (llm|parser|etl|selector) on claims?

## Comments

### Round 1 (2026-11-05)

- **The door** (Q1): an in-process function in `app/core` that every producer task calls. It validates against `contracts.py` and writes `pending` rows. `POST /internal/claims` is dropped until something outside the process needs it. A source-link submission sends a URL to fetch, not claims, so it doesn't need the route. "API conventions and operator surface" drops the endpoint from its list.
- **No shortcuts** (Q2): every claim, whatever produced it, quotes a stored document, enters as `pending` and passes `verify_citations` before it can count toward an edge. Confidence still comes from the source type, never from the producer.
- **Four producer kinds** (Q3):
  - `llm`, the default: any page or filing text, sponsor portfolio pages included.
  - `parser`: BDC Schedules of Investments.
  - `etl`: bulk official files. Form ADV now; Form 5500 and NPPES when their efforts unpark.
  - `selector`: long lists where every record has the same fields, such as store locators and location rosters, mapped by a per-site registry config. The config schema belongs to "Rosters, portfolio pages and the registry".
  - A selector claim from a brand's own site is `company_site` evidence, so it stays `reported` until a second source agrees.
- **Identity records** (Q4): one contract replaces "resolution hints", "structured hints" and "enrichment structs". An identity record is what one stored document states about one entity's identity: names, identifiers, addresses, phone, domain, industry code. Code producers (`etl`, `selector`, `parser`) emit them through the same door. The resolver matches or creates the entity, then writes the alias, identifier and address rows citing that document. The LLM emits only claims. "Where to look next" hints are dropped; fan-out reads identity rows and claims.
- **Store-locator JSON** (Q5): allowed when robots.txt permits the endpoint and it feeds the brand's public locator page. The usual rate limits and user agent apply. A site whose terms ban automated access is the developer's legal call, site by site.

### Round 2 (2026-11-05)

- **What each producer quotes** (Q6):
  - `llm`: an exact span of the document's text. Normalization belongs to "Citation verification rules".
  - `etl` over a bulk row (header line + data line, per "RawDocument shape"): the whole data line, exactly as in the file. The card still shows it as a labeled table.
  - `parser` (BDC): the row's text from the parsed table. Where that text is stored belongs to "Document storage, fetch log and last-confirmed". If the parser reads the SEC BDC dataset, each holding is a bulk row and the bulk rule applies.
  - `selector` on an HTML roster: the item's text, which must appear in the page's text. One document per page or per item belongs to "Rosters, portfolio pages and the registry".
  - `selector` on store-locator JSON: one document per record. Code writes the record's text in one fixed format: one `field: value` line per field, sorted, nested fields dotted (`address.city: Atlanta`). The quote is the lines the claim uses. The full response is stored as the original and each record's meta points at it. Values are verbatim, but code chose the layout.
- **Identity values checked first** (Q7): the door checks every value of an identity record against the cited document's text, with the quote normalization, before the resolver sees it. It checks the value as found (`(404) 555-0123`), and code normalizes it for storage afterwards. A record with any value missing is not written. Reason: identity rows have no status, so a wrong one can't be marked rejected.
- **Producer columns** (Q8): `producer` (`llm|parser|etl|selector`) and `producer_version` on claims, and on alias, identifier, address and industry rows that cite a document. The version is declared by the producer: the prompt version for `llm`, a module constant for `parser` and `etl`, the config revision for `selector`. Golden-fixture tests fail when output changes, which prompts the bump; a git hash would change on unrelated commits. `extraction_model` stays, null except for `llm`. The task sets all three, never the model's output. Withdrawing a bad version's rows belongs to "Entity lifecycle" (identity rows) and "Edge lifecycle" (claims).
- **Code producer failures** (Q9, revised after the developer asked what continuing gains): the per-record check catches escaping, encoding and changed values, not a moved column or a redesigned site, because those values still appear in the text. So:
  - every `etl` run first compares the file header with the expected columns and reads columns by header name; every `selector` run first checks that items still come back with the expected fields and roughly the usual count. A failed shape check stops the run before it writes anything and raises an alert. A selector's shape check in detail belongs to "Rosters, portfolio pages and the registry".
  - a per-record failure (rejected claim, unwritten identity record) raises an alert naming the producer, version and document, and the run keeps going.
  - if per-record failures in one run pass a threshold set in the spec, the rest of the run stops and raises an alert. Rows already written can be found by `producer_version`.
  - Alert delivery belongs to "Operational identity and guardrails".
- **One door call per producer run** (Q10): one call per document for code producers, one per request for the LLM (a request can cover several documents).
  - It carries the document ids, producer and version, identity records, claims, and "nothing found". The shape of "nothing found" belongs to "ExtractedClaim and the extraction result envelope", and its storage to "Checked and coverage states". Owner-kind evidence rides in the same call if "Owner kind: storage, evidence and the fund–firm link" makes it its own output.
  - Each identity record has a key (`r1`) valid only inside the call, and a code producer's claim can name its subject or object by that key. Turning names into ids stays with "Claim identity".
  - Order: check identity values, resolve and write identity rows, then write claims as `pending`. Claim quotes are still checked in the `verify_citations` stage, after names are resolved, because its sanity checks need resolved entities.
  - One transaction: if the database write fails, nothing from the call is written and the task retries.
  - Idempotent: the same producer version over the same document writes nothing new. Claims dedupe on the uniqueness hash ("Claim identity"); identity rows on entity, value and document.

## Answer

Resolved 2026-11-05 in a grilling session (two rounds, recorded under Comments).

- **The door** is an in-process function in `app/core` that every producer task calls. It validates against `contracts.py`. `POST /internal/claims` is dropped until something outside the process needs it.
- **Four producers**, each declared on what it writes:
  - `llm`, the default: page and filing text, sponsor portfolio pages included.
  - `parser`: BDC Schedules of Investments.
  - `etl`: bulk official files (Form ADV now; Form 5500 and NPPES when unparked).
  - `selector`: long uniform lists such as store locators and location rosters, mapped by a per-site registry config. Store-locator JSON endpoints are allowed when robots.txt permits them and they feed the public locator page.
- **No shortcuts.** Every claim from every producer quotes a stored document, enters as `pending` and passes `verify_citations`. Confidence comes from the source type, never the producer.
- **What is quoted:**
  - LLM: an exact span of the text.
  - Bulk row: the whole data line.
  - BDC: the row's parsed-table text.
  - HTML roster item: its text, which must appear in the page text.
  - Store-locator JSON: one document per record. Code writes the record's text as sorted `field: value` lines, with nested fields dotted (`address.city`) and list items indexed (`brands.0`). The rendering format's version goes in the document's meta. The quote is the lines the claim uses, and the full response is kept as the original.
- **Identity records** replace "resolution hints", "structured hints" and "enrichment structs". An identity record is what one document states about one entity's identity: names, identifiers, addresses, phone, domain, industry code. Only code producers emit them; the LLM emits only claims. The door checks each value as found against the document's text, and a record with a missing value is not written. Then the resolver matches or creates the entity and writes the sourced alias, identifier, address and industry rows. "Where to look next" hints are dropped.
- **Provenance columns.** `producer` and `producer_version` go on claims and on the alias, identifier, address and industry rows that cite a document. The version is the prompt version, a module constant or the config revision. `extraction_model` is null except for `llm`. The task sets all three.
- **Code producer failures:**
  - A shape check runs before anything is written. An ETL checks the header and reads columns by name; a selector checks the fields and the item count. If the check fails, the run stops and raises an alert.
  - A per-record failure raises an alert and the run keeps going.
  - When failures pass a threshold set in the spec, the rest of the run stops.
- **One door call per producer run** (per document for code, per request for the LLM), in one transaction, idempotent. The call carries document ids, producer and version, identity records with call-local keys (`r1`) that claims can point at, claims, and "nothing found". The door checks identity values, writes identity rows, then writes claims as `pending`. `verify_citations` runs later, after name resolution.
- **No ADR** (each choice is cheap to reverse) and **no glossary change** (pipeline words, not product language).

Handed on:
- "Claim identity": name resolution, the uniqueness hash, local keys.
- "Entity resolution algorithm": the resolver the door calls.
- "Document storage, fetch log and last-confirmed": parsed-table text, the stored JSON originals.
- "ExtractedClaim and the extraction result envelope": the "nothing found" shape.
- "Citation verification rules": normalization, the BDC cross-check.
- "Checked and coverage states": "nothing found" storage.
- "Rosters, portfolio pages and the registry": the selector config and its shape check, one document per page or item.
- "Owner kind: storage, evidence and the fund–firm link": owner-kind evidence as door output.
- "Entity lifecycle" and "Edge lifecycle": withdrawing a bad version's rows.
- "Operational identity and guardrails": alert delivery.
- "Testing and acceptance": the version-bump test.
- "API conventions and operator surface": drops the endpoint.
