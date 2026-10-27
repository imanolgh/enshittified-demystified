# Events and the public changelog

Type: grilling
Status: open
Blocked by: 26, 27  (Edge lifecycle: ending, retraction and staleness; Category precedence and storage)
Map: [api-spec](../map.md)

## Question

What is the `events` table (columns, event-type vocabulary, idempotency, consumers), and what does the public changelog expose?

## Context

- Named everywhere (build_roadmap.md:61,73,129,157; research_flows.md:102,162,178; ADR 0001:15; CLAUDE.md:25), defined nowhere.
- Candidate event types: published, ended, retracted, confidence_changed, category_changed, owner_kind_changed, acquisition_event (research_flows.md:102), filing_withheld. What counts as an acquisition event — only `acquired_by`, or new roster locations too?
- Payload, correlation id, idempotency key (retries must not double-emit), consumer cursors, card-cache invalidation (research_flows.md:178).
- **Changelog**: retractions only or all events? Global or per entity? Which fields are public?
- Alerts to users are out of scope (map ruling 2026-10-26); operational alerts to the developer are in — events may feed them.
