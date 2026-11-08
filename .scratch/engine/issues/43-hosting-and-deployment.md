# Hosting, storage and deployment

Type: grilling
Status: open
Map: [engine](../map.md)

## Question

Where does the engine run in production, what backs object storage, and how are deploys, migrations, backups and CI done?

## Context

- **Hosting**: fly.io / Render / VPS unchosen (stack_fastapi.md:32); affects Playwright, volumes, the Beat singleton, bulk-load memory (NPPES is multi-GB).
- **Object storage**: MinIO, S3, R2 or B2; durability, versioning/object lock for the evidence archive ("your legal defense", evidence_layer_plan.md:44).
- Defaultables: compose topology (api, worker groups, beat, flower, Playwright worker image, postgres, redis, minio — today's compose has 3 services, no Dockerfile); dev/test/prod with separate test DB and bucket; migrations on deploy; backups + restore drill; Redis persistence and DB separation (broker, results, rate limits, cache); CI on GitHub Actions with service containers; missing pyproject deps (anthropic, playwright, pdfplumber, camelot + Ghostscript/OpenCV, polars, selectolax, rapidfuzz, feedparser, tldextract, protego, flower).
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): document bytes live at `documents/{sha256}`, written once and never deleted; the production bucket needs versioning plus object lock (MinIO supports both locally); operational files go under a separate prefix. Whether the chosen host supports object lock is this ticket's.
- **Fact checked 2026-11-08** (Celery docs via Context7, "Backends and Brokers"): Postgres can't be Celery's broker (SQLAlchemy as a broker was removed in Celery 4.0), so production needs Redis, RabbitMQ or Amazon SQS beside Postgres and S3; SQS has no Celery monitoring or remote control. Redis also holds the per-domain rate-limit token buckets. Which managed service and its cost is this ticket's.
