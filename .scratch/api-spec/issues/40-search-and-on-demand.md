# Search and on-demand research

Type: grilling
Status: open
Blocked by: 19, 37  (Entity resolution algorithm; Retrieval fan-out, tracked entities and refresh cadence)
Map: [api-spec](../map.md)

## Question

How does public search work, when does a search trigger on-demand research (scenario A2), how are results delivered, and how is the paid-API spend it triggers protected from abuse?

## Context

- **Search semantics**: parsing name + location from free text, which entity types are searched, the "found vs research" threshold, near-match response, pagination.
- **Delivery**: poll `GET /api/entities/pending/{ticket}` or SSE (research_flows.md:87–89); ticket statuses and TTL; `status: researching`.
- **Abuse / cost protection**: every A2 run costs Places + LLM money (monetizationideas.md:81): per-IP limits, global daily budget, behavior when exhausted.
- Required before launch (build_roadmap.md §8); the "Unknown — research on request" coverage state depends on it.
- A2 dedup (one in-flight research per entity / normalized query).
