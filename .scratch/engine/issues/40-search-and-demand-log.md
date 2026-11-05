# Search and the demand log

Type: grilling
Status: open
Blocked by: 19, 37  (Entity resolution algorithm; Retrieval fan-out, tracked entities and refresh cadence)
Map: [engine](../map.md)

## Question

How does public search work over the seeded data set, what does a search show when it finds nothing ready (a brand not in the data, or one in the data but not yet checked), what does the demand log record, and how is the log kept free of bot noise?

## Context

- **Ruled 2026-11-05 (decisions.md §15, during "Schema conventions")**: no on-demand research. The data set grows only by operator-seeded batches. A search that finds nothing ready is logged, and a demand dashboard shows the developer what people look for that is not seeded yet: brands, chains, categories and locations. Retitled from "Search and on-demand research"; the file was `40-search-and-on-demand.md`.
- **Search semantics**: parsing name + location from free text, which entity types are searched (brand, company, location; ADR 0005), the match threshold, near-match response, pagination.
- **What a miss shows**: wording for "not in the data yet" and "in the data, not checked yet" (with chains-and-brands "Card wording and the how-this-works page").
- **What the log holds**: query text and its normalized form, outcome (no match / matched an entity not yet checked), the matched entity, location (only what the searcher typed or chose, or also a coarse state from the IP address, which is then discarded?), industry if one can be inferred, time. The table and its columns are this ticket's ("Schema conventions" Q1); it follows the conventions in evidence_layer_plan.md §4.
- **What it keeps about the searcher**: proposed nothing: no IP address, no tracking id (no accounts exist). Retention period.
- **Places in the log, if at all** (facts from "Research: Google Places terms, pricing and a free geocoder"): only `place_id` may be stored (ToS §3.2.3(a)(iii) bans saving business names and addresses); a Text Search returning only ids is free and unlimited; showing a name on the dashboard costs $0.017 (Place Details Pro), must carry the Google logo and is never saved; showing Places results to searchers costs $0.032 per search after 5,000 free a month and grows with traffic. For a brand, a Places result is one store near the searcher, so place ids would scatter one brand's demand across thousands of stores; the typed text is the better brand signal, place ids matter more for local businesses.
- **Bot noise and cost**: per-IP rate limits without storing IPs, counting repeated queries once, a budget for Places calls if the log uses them.
- Required before launch (build_roadmap.md §8).
- **Dropped with on-demand research** (2026-11-05): delivery by polling `GET /api/entities/pending/{ticket}` or SSE, ticket statuses and TTL, A2 dedup, the per-search research budget, the "Unknown, research on request" coverage state.
- The demand dashboard itself is "API conventions, internal auth and operator surface".
