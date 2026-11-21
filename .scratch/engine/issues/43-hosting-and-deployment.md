# Hosting, storage and deployment

Type: grilling
Status: open
Blocked by: 122  (Task: Estimate build, seeding and monthly running costs)
Map: [engine](../map.md)

## Question

Where does the engine run in production, what backs object storage, and how are deploys, migrations, backups and CI done?

## Context

- **Hosting**: fly.io / Render / VPS unchosen (stack_fastapi.md:32); affects Playwright, volumes, the Beat singleton, bulk-load memory (NPPES is multi-GB).
- **Object storage**: MinIO, S3, R2 or B2; durability, versioning/object lock for the evidence archive ("your legal defense", evidence_layer_plan.md:44).
- Defaultables: compose topology (api, worker groups, beat, flower, Playwright worker image, postgres, redis, minio — today's compose has 3 services, no Dockerfile); dev/test/prod with separate test DB and bucket; migrations on deploy; backups + restore drill; Redis persistence and DB separation (broker, results, rate limits, cache); CI on GitHub Actions with service containers; missing pyproject deps (anthropic, playwright, pdfplumber, camelot + Ghostscript/OpenCV, polars, selectolax, rapidfuzz, feedparser, tldextract, protego, flower).
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): document bytes live at `documents/{sha256}`, written once and never deleted; the production bucket needs versioning plus object lock (MinIO supports both locally); operational files go under a separate prefix. Whether the chosen host supports object lock is this ticket's.
- **Fact checked 2026-11-08** (Celery docs via Context7, "Backends and Brokers"): Postgres can't be Celery's broker (SQLAlchemy as a broker was removed in Celery 4.0), so production needs Redis, RabbitMQ or Amazon SQS beside Postgres and S3; SQS has no Celery monitoring or remote control. Redis also holds the per-domain rate-limit token buckets. Which managed service and its cost is this ticket's.
- **From "Rosters, portfolio pages and the registry"** (2026-11-12; results in research/portfolio-wall-survey.md): before launch, re-run the wall survey from the production IPs; from the developer's home IP, 90 of 93 PE firm sites were readable under the honest rules, and bot services trust hosting IPs less. The script is kept on the developer's machine at `~/.local/share/playwright-tools/challenge-test/run.py`. The server image needs the Playwright browser and its system libraries (on the developer's WSL machine libnss3, libnspr4 and libasound2t64 were missing).
- **From chains "Website stack and hosting"** (2026-11-18): the website is static, served by Cloudflare Pages (domain and TLS there). The engine host serves the public read API the build reads and the browser calls (search, the report form). The engine calls a Cloudflare Pages deploy hook to rebuild.
- **From "Task: Estimate build, seeding and monthly running costs"** (2026-11-20; `.scratch/engine/research/cost-estimate.md` §1 and §5): priced options for API, workers with Playwright, Beat, Postgres 16 and Redis: Hetzner one CPX42 in Helsinki about $65 a month (two US boxes about $202; plans showed "currently unavailable" when read); DigitalOcean managed $124 to $248; Fly.io with managed high-availability Postgres about $450. Backblaze B2 for object storage with Object Lock at no extra cost, $6.95 per TB. Not priced: Hetzner backups, DigitalOcean standby nodes and Spaces Object Lock, Fly's Redis and storage.
- **From "Cost cuts before revenue"** (2026-11-21): before revenue the engine runs on the developer's machine (the `docker compose` stack); the site is built there and uploaded to Cloudflare Pages (free); the "Report a mistake" form posts to a small free Cloudflare function. This ticket now also settles that setup: which function, its free limits, where reports land, backups of the home database and documents (Backblaze B2 with Object Lock, $6.95 per TB), and the move to a paid host once the site earns money (the three priced hosts in `research/cost-estimate.md`).
