# Hosting, storage and deployment

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

Where does the engine run in production, what backs object storage, and how are deploys, migrations, backups and CI done?

## Context

- **Hosting**: fly.io / Render / VPS unchosen (stack_fastapi.md:32); affects Playwright, volumes, the Beat singleton, bulk-load memory (NPPES is multi-GB).
- **Object storage**: MinIO, S3, R2 or B2; durability, versioning/object lock for the evidence archive ("your legal defense", evidence_layer_plan.md:44).
- Defaultables: compose topology (api, worker groups, beat, flower, Playwright worker image, postgres, redis, minio — today's compose has 3 services, no Dockerfile); dev/test/prod with separate test DB and bucket; migrations on deploy; backups + restore drill; Redis persistence and DB separation (broker, results, rate limits, cache); CI on GitHub Actions with service containers; missing pyproject deps (anthropic, playwright, pdfplumber, camelot + Ghostscript/OpenCV, polars, selectolax, rapidfuzz, feedparser, tldextract, protego, flower).
