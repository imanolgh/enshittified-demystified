# Document storage, fetch log and last-confirmed

Type: grilling
Status: open
Blocked by: 17  (Claim producers and the claims door)
Map: [api-spec](../map.md)

## Question

How are documents keyed and stored, how is each fetch recorded (so "last confirmed" can advance when a page is unchanged), and where do raw text and parsed tables live?

## Context

- **Document uniqueness**: unique-on-sha256 collapses identical content fetched from two URLs. Needs a document-vs-fetch split, a `domain` column (registrable domain via the public suffix list), a per-URL version chain for the diff loop.
- **Last confirmed vs sha dedup**: an unchanged re-fetch stops at the sha compare (research_flows.md:99; evidence_layer_plan.md:164), so nothing records that the source still shows the fact, and last-confirmed (GLOSSARY:83–85) / the 18-month rule (ADR 0001:15) never advance. Needs a `fetches` table or `last_seen_at`.
- **Where text lives**: Postgres column vs S3 object for `raw_text`; BDC quotes match "parsed table text stored on the document row" (research_flows.md:133) — which column, and does `verify_citations` search both?
- **S3 layout**: only `docs/{sha256}.html` given (research_flows.md:49); bulk archives, batch files, versioning/object lock for the "legal defense" archive (evidence_layer_plan.md:44,225).
- **Text-extraction rules must be versioned** (quotes and offsets match exact text): HTML→text (boilerplate, block separators), PDF (layout mode, page separators for page citations, ligatures, hyphenation), Playwright capture (post-render DOM, wait conditions).
- Builds on "RawDocument shape" (raw_text written once).
