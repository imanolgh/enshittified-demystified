# Celery topology

Type: grilling
Status: open
Blocked by: 22, 37  (Extraction execution; Retrieval fan-out, tracked entities and refresh cadence)
Map: [api-spec](../map.md)

## Question

How are Celery queues, priorities, chains/chords, retries, dead-lettering and deduplication arranged?

## Context

- **Queue topology**: per-stage queues (CLAUDE.md:63; evidence_layer_plan.md:280 — no parse stage) vs priority classes `on_demand > refresh > seed` (research_flows.md:88,174), never reconciled. Redis priority only works via emulated sub-queues (`queue_order_strategy`, `priority_steps`). Options: stage × priority queues, or dedicated on_demand workers.
- **Chain shape for the Batch API** (from "Extraction execution").
- Defaultables: sync SQLAlchemy + `def` routes; Redis result backend (chords need one); tenacity for HTTP + Celery autoretry for transient errors; DLQ = `on_failure` → `failed_tasks` table + replay command (Redis has no native DLQ); one in-flight research per entity; A2 dedup by normalized query; `acks_late` + prefetch 1; empty rate-limit bucket → `retry(countdown)`; Playwright on its own queue/image; time limits; single Beat instance, timezone, scheduler persistence.
- Context7 for Celery API specifics (CLAUDE.md documentation rules).
