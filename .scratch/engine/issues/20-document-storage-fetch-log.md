# Document storage, fetch log and last-confirmed

Type: grilling
Status: resolved
Blocked by: 17  (Claim producers and the claims door)
Map: [engine](../map.md)

## Question

How are documents keyed and stored, how is each fetch recorded (so "last confirmed" can advance when a page is unchanged), and where do raw text and parsed tables live?

## Context

- **Document uniqueness**: unique-on-sha256 collapses identical content fetched from two URLs. Needs a document-vs-fetch split, a `domain` column (registrable domain via the public suffix list), a per-URL version chain for the diff loop.
- **Last confirmed vs sha dedup**: an unchanged re-fetch stops at the sha compare (research_flows.md:99; evidence_layer_plan.md:164), so nothing records that the source still shows the fact, and last-confirmed (GLOSSARY:83–85) / the 18-month rule (ADR 0001:15) never advance. Needs a `fetches` table or `last_seen_at`.
- **Where text lives**: Postgres column vs S3 object for `raw_text`; BDC quotes match "parsed table text stored on the document row" (research_flows.md:133) — which column, and does `verify_citations` search both?
- **S3 layout**: only `docs/{sha256}.html` given (research_flows.md:49); bulk archives, batch files, versioning/object lock for the "legal defense" archive (evidence_layer_plan.md:44,225).
- **Text-extraction rules must be versioned** (quotes and offsets match exact text): HTML→text (boilerplate, block separators), PDF (layout mode, page separators for page citations, ligatures, hyphenation), Playwright capture (post-render DOM, wait conditions).
- Builds on "RawDocument shape" (raw_text written once).
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): the fetch log table, its columns and retention are this ticket's; it follows the shared conventions.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): the BDC parser quotes a row's parsed-table text, so where that text is stored and whether `verify_citations` searches it is this ticket's. A store-locator JSON record is one document whose text code renders (sorted `field: value` lines); `meta` records the rendering version and points at the full response, kept as the original. Where that original lives, and whether it gets a documents row, is this ticket's.
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): an `owned_by` claim without a stated as-of date is confirmed on the document's date; whether that is the publication date or the retrieval date is this ticket's.
- **From "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended; notes in evidence_layer_plan.md §4 `claims` and `edges`): an undated claim takes its document's own date (a release's dateline, a filing date), else the fetch date, for ordering claims and for last-confirmed. Which document field holds that date, and how a connector fills it, is this ticket's.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): a fetch that fails after retries, or is blocked by robots.txt or site terms, makes that entity's source run `failed` or `blocked` in `source_runs`; the fetch log is where that shows first.

## Comments

### Round 1 (2026-11-07)

- **Document rows** (Q1): one `documents` row per URL, content and text-extractor version; the S3 object is keyed by sha256, so identical bytes are stored once. A `domain` column holds the registrable domain (public suffix list) for "Source independence and syndication". A URL's versions are its rows in order of first fetch; the sponsor-page diff compares the newest with the one before (El Car Wash: Warburg's release on PR Newswire and on elcarwash.com are two rows, two domains).
- **Fetches and last-confirmed** (Q2): `retrieved_at` stays the first fetch of that content; new `last_seen_at` advances on every later successful fetch of the same URL returning the same bytes. A hop's last-confirmed date is the newest `last_seen_at` among the documents its accepted claims cite; if the fact is gone from a changed page, confirmation stops and the hop ages out after 18 months unless a `former` claim ends it sooner. A `fetches` log row per attempt (URL, time, outcome `ok|not_modified|failed|blocked|not_found`, HTTP status, error, matched document) feeds the operator report and `failed`/`blocked` source runs; operational, kept 90 days.
- **A document's own date** (Q3): new `published_on`, filled by the connector from structured fields only (SEC filing date, feed publication date, a page's `datePublished` or `article:published_time`, a bulk file's release date), never by the LLM or HTTP `Last-Modified`; null when none exists. An undated claim's as-of date is `published_on`, else `retrieved_at`; last-confirmed always uses `last_seen_at`.
- **Parent and child documents** (Q4): a filing, full locator response or bulk file is a parent document holding the original bytes; each citable part (a Schedule row's parsed-table text, a rendered locator record, a header plus data line) is a child document with its own `raw_text` and a `parent_document_id`. `verify_citations` searches only `raw_text`. The card links to the child, which shows its parent.
- **Bytes to text** (Q5): keep all visible text (only scripts, styles and hidden elements dropped; no boilerplate removal, since a release's "About" paragraph often carries the ownership fact); PDFs get a page marker at each page break; JavaScript-rendered pages store the rendered DOM with capture settings in `meta`. Each document records its text-extractor version; a fixed extractor applies to new fetches only, and re-extracting old documents is a deliberate re-run that creates new rows. Detailed rules go in the spec with golden tests.
- **S3 layout** (Q6): document bytes at `documents/{sha256}`, written once and never deleted, MIME type in the row; operational files (Anthropic batch files, crawl caches) under a separate prefix with retention set by their tickets; the production documents bucket uses versioning plus object lock (whether the host supports it: "Hosting, storage and deployment"; MinIO does locally).

### Round 2 (2026-11-07)

- **Bytes change, text doesn't** (Q7): each row stores a `text_sha256` of its extracted text; a re-fetch whose text matches the URL's current version counts as unchanged (no new row, `last_seen_at` advances, new bytes not stored; the first version's bytes stay the archived original), so an unchanged page costs no LLM spend.
- **Re-reading a changed page** (Q8, option a, the developer's choice): the LLM re-reads the whole new version, because evidence can be anywhere in it; every fact still there gets a new claim from the new version, which keeps it confirmed (Q2 stands as answered). Turned down: reading only the changed blocks and confirming old claims by string match. Cost stays bounded by Q7: only a real text change triggers a re-read.
- **Conditional requests** (Q9): connectors send back the server's `ETag` or `Last-Modified` value; a `304 Not Modified` counts as the same bytes (`last_seen_at` advances, nothing downloaded); a `404` or `410` is `not_found` and confirms nothing. Whether repeated misses end a fact: "Edge lifecycle".
- **Recurring children** (Q10): a child's identity is its parent's stable address plus its row key (a locator endpoint plus store id; for a monthly bulk file, a stable dataset address the connector supplies, such as the SEC's monthly-adviser page, plus the CRD). An unchanged record in the next response or file is the same child (`last_seen_at` advances, no new claims); a changed record is a new version of that child. Children inherit their parent's `domain` and `published_on`.

## Answer

Resolved 2026-11-07 in a grilling session (two rounds, recorded under Comments).

- **Documents:** one row per URL, extracted text (`text_sha256`) and `text_extractor_version`, unique on those three; text that returns after a change reuses its old row, and a URL's current version is its row with the newest `last_seen_at`. Bytes live once at `documents/{sha256}`. New columns: `domain` (registrable domain), `published_on`, `last_seen_at`, `text_sha256`, `text_extractor_version`, `parent_document_id`.
- **Fetches:** a `fetches` log row per attempt (`ok|not_modified|failed|blocked|not_found`), kept 90 days. An unchanged re-fetch (same text, or `304 Not Modified` from a conditional request) creates no row and advances `last_seen_at`. A hop's last-confirmed date is the newest `last_seen_at` among the documents its accepted claims cite.
- **Changed pages:** only a real text change makes a new version, and the LLM then re-reads the whole new version (developer's choice: evidence can be anywhere); facts still there get new claims, which keep them confirmed.
- **Dates:** `published_on` comes from structured fields only (filing date, feed date, `datePublished`/`article:published_time`, bulk release date), never the LLM or `Last-Modified`. An undated claim's as-of date is `published_on`, else `retrieved_at`.
- **Parents and children:** a filing, full locator response or bulk file is a parent holding the original bytes; each citable part is a child with its own `raw_text` and `parent_document_id`, and `verify_citations` searches only `raw_text`. A child's identity is its parent's stable address plus its row key (`#row=<key>` in its `url`); an unchanged recurring record is the same child. Children inherit `domain` and `published_on`.
- **Text:** keep all visible text (no boilerplate removal); PDF page markers; JavaScript pages stored as the rendered DOM; a versioned extractor whose fixes apply to new fetches, with re-extraction as a deliberate re-run.
- **S3:** documents written once, never deleted; operational files under a separate prefix; production bucket with versioning and object lock.
- Docs: evidence_layer_plan.md §4 (documents, fetches, RawDocument notes), research_flows.md, build_roadmap.md Step 4. No ADR, no glossary change.

Handed on:
- "Source independence and syndication": `domain`; syndicated copies are separate rows.
- "Edge lifecycle": `last_seen_at`, `not_found` and disappearances, the 90-day log.
- "Extraction execution": re-reads only on a text change, always of the whole document.
- "Citation verification rules": `raw_text` only, page markers, extractor versions, children.
- "BDC discovery and Schedule of Investments parsing", "Form ADV and IRS exempt-org ingestion", "Rosters, portfolio pages and the registry": child documents and recurring children.
- "Press and EDGAR full-text connectors": `published_on` from feed and filing dates.
- "Hosting, storage and deployment": object lock, versioning, bucket layout.
- "Retrieval fan-out, tracked entities and refresh cadence": conditional requests.
- "API conventions, internal auth and operator surface": failed and blocked fetches.
- "Operational identity, budgets and guardrail values": LLM spend on re-reads.
- "Claim card and graph output shapes": a card links to the child, which shows its parent.
