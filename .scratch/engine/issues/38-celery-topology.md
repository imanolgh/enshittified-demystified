# Celery topology

Type: grilling
Status: open
Blocked by: 22, 37  (Extraction execution; Retrieval fan-out, tracked entities and refresh cadence)
Map: [engine](../map.md)

## Question

How are Celery queues, priorities, chains/chords, retries, dead-lettering and deduplication arranged?

## Context

- **Queue topology**: per-stage queues (CLAUDE.md:63; evidence_layer_plan.md:280 — no parse stage) vs priority classes `on_demand > refresh > seed` (research_flows.md:88,174), never reconciled. Redis priority only works via emulated sub-queues (`queue_order_strategy`, `priority_steps`). Options: stage × priority queues, or dedicated on_demand workers.
- **Chain shape for the Batch API** (from "Extraction execution").
- Defaultables: sync SQLAlchemy + `def` routes; Redis result backend (chords need one); tenacity for HTTP + Celery autoretry for transient errors; DLQ = `on_failure` → `failed_tasks` table + replay command (Redis has no native DLQ); one in-flight research per entity; A2 dedup by normalized query; `acks_late` + prefetch 1; empty rate-limit bucket → `retry(countdown)`; Playwright on its own queue/image; time limits; single Beat instance, timezone, scheduler persistence.
- Context7 for Celery API specifics (CLAUDE.md documentation rules).
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): the A2 priority queue and A2 dedup are gone. The `failed_tasks` table, its columns and retention are this ticket's. An ingest item's `failed` result now covers resolution errors only; later failures belong to the entity's research.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): ambiguous claim names are retried automatically when identity data changes, and all claims are re-resolved after a resolution rules change; when and on which queue these run is this ticket's.
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): moved here: concurrency of publishing (a lock per brand or a single publish queue). Also needed in Beat: a daily sweep that marks edges `unconfirmed` after 18 months without confirmation, and a daily sweep that expires pending deals after 18 months without completion.
- **Fact checked 2026-11-08** (Celery docs via Context7, "Backends and Brokers", docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/; raised when the developer asked whether Redis is needed): Celery lists three stable brokers, RabbitMQ, Redis and Amazon SQS; Zookeeper, Kafka and Google Cloud Pub/Sub are experimental. Using SQLAlchemy (a database such as Postgres) as the broker was removed in Celery 4.0; SQLAlchemy remains supported only as a result backend. Monitoring and remote control (Flower, `celery inspect`) work on RabbitMQ and Redis, not SQS. No decision was taken; the stack still lists Celery + Redis (CLAUDE.md).
