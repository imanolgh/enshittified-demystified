# API conventions, internal auth and operator surface

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

What are the cross-cutting HTTP conventions, how are `/internal` and `/admin` protected, and how does the operator (the developer) trigger loads, matches and replays now that the review panel is gone?

## Context

- Implied endpoints: `GET /health`, `GET /api/entities/{id}/card`, `GET /api/entities/{id}/graph`, `GET /api/search`, `GET /api/entities/pending/{ticket}`, `POST /internal/claims`, `POST /internal/edges/{id}/retract`, `POST /admin/ingest-batches`; implied without a path: public changelog, batch report, employer→plan lookup, document receipts.
- **Auth**: user accounts are out of scope (map ruling); `fastapi-users` vs JWT (evidence_layer_plan.md:42; stack_fastapi.md:28) only matters later. For /internal and /admin: static API key from settings, not publicly exposed (default).
- **Admin surface** (build_roadmap.md:133,181; research_flows.md:22,77 "batch dashboard"; evidence_layer_plan.md:41): any UI, or endpoints + CLI + Flower only?
- Defaultables: `/api/v1`, error format, cursor pagination, CORS, ETag + Redis card cache invalidated by events, OpenAPI in production; batch report format (counts per build_roadmap.md:103, updated vocabulary).
