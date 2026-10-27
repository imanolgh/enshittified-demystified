# RawDocument shape

Type: grilling
Status: resolved
Map: [api-spec](../map.md)

## Question

What exactly does every connector hand to storage — the `RawDocument` contract — and how do provenance, hashing and the raw bytes travel with it?

## Answer

Resolved 2026-10-26 in the developer's "grill me" session (before this map existed; recorded here because the guide that held it, `docs/step1-contracts-guide.md`, was deleted the same day).

- **One RawDocument = the smallest unit a claim can cite.** Connectors split bulk files into one document per row/record; the original file's identity goes in `meta` (`bulk_file`, `row_key`). Quotes verify against small texts, cards point at the exact row, and a refreshed bulk file only re-extracts rows whose sha changed.
- **`source_type`**: the SourceType enum (ADR 0003).
- **`url: HttpUrl`, required** — where the bytes came from. Every source is fetched over HTTP. Bulk rows carry the file's download URL; API pulls the request URL; form POSTs the endpoint URL with params in `meta["form_params"]`.
- **`retrieved_at`**: timezone-aware datetime (validator enforces tz). Bulk rows carry the file's download time.
- **No `sha256` field.** `store_document` computes sha256 from `content` — one place, hash can never disagree with bytes. `ExtractedClaim.doc_sha` is filled from the stored document.
- **`mime_type`**: plain string.
- **`content: bytes`**, `Field(repr=False)` — payload rides on the model.
- **Bulk row content** = the original header line + that row's line, as bytes from the file; `raw_text` = that decoded. Verbatim stays literally true; the card may display it as a labeled table.
- **`raw_text`**: nullable. PDFs: `None` at hand-off; a parse stage after storage fills it **once and never overwrites it** (verified quotes/offsets stay valid).
- **`meta`**: `dict[str, Any]`, JSON-serializable; conventional keys `fetch_method` (bulk/api/scrape, ADR 0003), `bulk_file`, `row_key`, `form_params`, parsed tables. Typed per-connector models later only if it gets messy.
- **RawDocument never crosses a Celery boundary.** The connector calls `store_document(doc)` in the same task; only the stored document's id/sha travels onward.
- `model_config = ConfigDict(frozen=True)`.

Open follow-ons live in other tickets: document uniqueness/fetch log ("Document storage, fetch log and last-confirmed"), what is quoted for structured rows ("Claim producers and the claims door").
