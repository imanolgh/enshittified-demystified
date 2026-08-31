# Evidence Layer Glossary
### Every acronym, agency, API, and tool from evidence_layer_plan.md — what it is, why it's in the plan, and which pipeline stage it serves

Pipeline stages referenced below: **Stage 1** Entity Resolution · **Stage 2** Source Retrieval · **Stage 3** LLM Extraction · **Stage 4** Citation Verification · **Stage 5** Confidence Scoring · **Stage 6** Human Review · **Stage 7** Serving

---

## 1. U.S. Government Agencies & Their Data Systems

### SEC — Securities and Exchange Commission
The federal regulator of securities markets. Companies and investment funds are legally required to file disclosures with it. You never integrate with "the SEC" directly — you integrate with its database, EDGAR.

### EDGAR — Electronic Data Gathering, Analysis, and Retrieval
The SEC's free public database of every filing ever submitted. Has a free full-text search API (no key required).
**Puzzle piece:** your single richest free source of financial evidence — acquisition announcements, fund holdings, adviser registrations all live here.
**Stage:** 2 (retrieval), for both PE and PC connectors.

### Filing types you'll pull from EDGAR
- **10-K** — a company's annual report. For private credit funds, contains the full loan book.
- **10-Q** — the quarterly version of the same.
- **8-K** — "something material just happened" filing; often where acquisitions are announced.
- **Form D** — a notice companies file when raising money privately; evidence that a PE deal happened.
- **N-2** — the registration document for closed-end funds, including BDCs (below).
**Stage:** 2 (what the EDGAR connector fetches), then 3 (what the LLM/table parser reads).

### BDC — Business Development Company
A special type of publicly traded fund that lends to private companies — essentially **private credit funds that trade on the stock market**. Because they're public, they must disclose their entire loan portfolio quarterly in a table called the **Schedule of Investments** (which company they lent to, how much, at what rate, and whether it's being repaid).
**Puzzle piece:** the core dataset of the PC evidence layer — "Fund X lends to Company Y" comes straight from these tables.
**Stage:** 2 (fetch the 10-K/10-Q), Python sidecar table parsing, then 3.

### Form ADV & IAPD — Investment Adviser Public Disclosure
Every investment adviser (including PE and PC fund managers) must register with the SEC on **Form ADV**, listing their funds and assets under management. **IAPD** is the free public website/bulk-download where these live.
**Puzzle piece:** the roster of who the fund managers are and what funds they run — helps build your entity list of sponsors and funds.
**Stage:** 1 (knowing sponsors exist) and 2.

### DOL — Department of Labor
Federal agency overseeing workplace matters, including retirement plans. Two of its datasets matter to you:

### Form 5500 (+ Schedule H)
The annual filing **every private-sector retirement plan (401(k) etc.) must make** with the DOL, listing the plan's investments. Published as **free bulk CSV downloads** — no scraping required.
**Puzzle piece:** the backbone of MyRetirementX-Ray — how you show a user what's inside their employer's 401(k).
**Stage:** 2 (bulk load), your fastest PC win.

### WARN — Worker Adjustment and Retraining Notification Act
A law requiring companies to notify states before mass layoffs. States publish these notices.
**Puzzle piece:** post-acquisition layoff evidence for the worker-side features ("what happened after PE bought this employer").
**Stage:** 2.

### CAFR / ACFR — (Annual) Comprehensive Financial Report
The audited annual report every **public pension system** (teachers, state employees) publishes as a PDF. Contains the pension's asset allocation — including what percentage sits in private equity and private credit.
**Puzzle piece:** how you prove "Oregon's pension is 28% alternatives" with a page-number citation. The public-pension half of MyRetirementX-Ray.
**Stage:** 2 (PDF download), Python sidecar parsing, then 3.

### NAIC — National Association of Insurance Commissioners
The body through which insurance companies file their financial statements. Insurers are big private credit holders; their filings show that exposure.
**Puzzle piece:** the "is my annuity exposed?" question — but access is partially paywalled and messy, which is why the plan defers it to a later phase.
**Stage:** 2, Phase 5.

### NPI / NPPES — National Provider Identifier / National Plan and Provider Enumeration System
Every healthcare provider and healthcare organization in the U.S. has a federal ID number (**NPI**). **NPPES** is the free federal system where you look them up — available both as an API *and* as a **free monthly bulk file** containing the entire registry. Each record links a provider/clinic to its parent organization, an "authorized official," and other-name aliases.
**Puzzle piece:** the healthcare cheat code, twice over — the bulk file is a downloadable national census of every dental/medical organization (loaded like Form 5500, it seeds the map's denominator without per-lookup API or Places costs), while the API handles on-demand freshness checks and user-search misses. The official, free way to connect "Bright Smiles Dental in Croton" to the corporate entity that actually runs it.
**Stage:** 1 (entity resolution) and 2 (bulk census seeding), for the healthcare wedge.

### SoS — Secretary of State (state business registries)
Every U.S. state's company registry — where legal entities, their registered agents, officers, mergers, and name changes are recorded. Quality and searchability vary wildly by state; most require scraping.
**Puzzle piece:** the legal ground truth of who a business *is* (Stage 1) and paper trails of mergers/ownership changes (Stage 2).

### PACER — Public Access to Court Electronic Records
The federal court system's records database. Official but charges per page.

### RECAP / CourtListener
A free nonprofit mirror of PACER documents (run by the Free Law Project) with a free API. "RECAP" is "PACER" backwards.
**Puzzle piece:** lawsuits involving sponsors or their portfolio companies — evidence for deep-dive reports — without paying PACER fees.
**Stage:** 2, later phases.

### FTC / DOJ — Federal Trade Commission / Department of Justice
The antitrust regulators. Mentioned because the research showed citizens actively wanting to submit PE-harm evidence to their inquiry on serial acquisitions — a future outlet for your data, not an integration.

---

## 2. Industry Structures Worth Knowing

### DSO — Dental Service Organization
A management company that "supports" dental practices. In many states only a dentist can legally *own* a practice — the DSO structure is how PE effectively controls hundreds of clinics anyway (the dentist owns it on paper; the DSO runs everything). Similar structures exist for vets and physician groups (MSOs).
**Puzzle piece:** the reason healthcare ownership is obscured, and the reason your DSO-roster connector (scraping their location pages) is a key Stage 2 source.

### LP / GP — Limited Partner / General Partner
The two roles in a private fund. The **GP** is the PE/PC firm managing the money; **LPs** are the investors whose money it is — pensions, insurers, endowments, and increasingly retail. When the research says "is my pension holding the paper," it's asking whether the pension is an LP.

### PIK — Payment In Kind
A loan arrangement where the borrower doesn't pay cash interest — the interest gets added to the loan balance instead. Widely flagged in the research as how struggling loans avoid being reported as defaults.
**Puzzle piece:** one of the risk signals your PC claim cards should extract and your jargon decoder should explain.

### AUM — Assets Under Management
How much money a manager runs. Appears on Form ADV; useful entity metadata.

### LBO — Leveraged Buyout
The classic PE maneuver: buy a company mostly with borrowed money, and the *acquired company* carries the debt. Context for why "acquired by PE" and "suddenly drowning in debt" go together in the pain point data.

### Gating / Redemption gate
A fund clause letting it refuse or limit withdrawals. The single most painful PC pain point in the research ("Hotel California").
**Puzzle piece:** what the Redemption Decoder extracts from fund documents.

---

## 3. Commercial Data & Media Sources

### PitchBook / Preqin / CB Insights
The expensive institutional databases of private-market deals (PitchBook ≈ $25–30k/seat/year). **Explicitly excluded** from your architecture: their licenses forbid building products on the data, they're secondary sources (breaking your provenance premise), and your users can't verify citations to them.

### OpenCorporates
A commercial aggregator that has already normalized company-registry data from most jurisdictions into one API. Free tier is limited; paid tiers reasonable.
**Puzzle piece:** a shortcut so you don't have to build 50 individual state SoS scrapers on day one.
**Stage:** 1 and 2.

### PRNewswire / BusinessWire / GlobeNewswire
The three big commercial press-release distribution wires. Companies pay them to publish announcements — including acquisition announcements.
**Puzzle piece:** acquisition events with dates, in the sponsors' own words. Retrieved via their public sites/RSS.
**Stage:** 2.

### GDELT — Global Database of Events, Language, and Tone
A free academic project that monitors world news media and exposes it via API.
**Puzzle piece:** catching small-market local news of acquisitions that national wires miss.
**Stage:** 2.

### RSS — Really Simple Syndication
The old, reliable web-feed format. Google News and the press wires expose feeds you can poll per entity — the cheap way to run recurring "did anything new happen to this company?" checks that power Acquisition Alarm.
**Stage:** 2, scheduled re-crawls.

### Google Places API
Google's paid API for business listings (name, address, unique `place_id`).
**Puzzle piece:** the canonical identity of a *local, physical* business — the front door of Stage 1 for "who owns my dentist."

---

## 4. Your Technology Stack

### API — Application Programming Interface
The generic term for one system exposing endpoints another system can call. Used throughout: things you call (EDGAR, NPPES) and things you expose (your claim-card endpoints).

### LLM — Large Language Model
AI models like Claude. In this architecture, strictly a **reading-comprehension engine**: it extracts claims from documents your pipeline fetched, and never asserts anything it can't quote (Stage 3).

### FastAPI
A modern Python web framework for building APIs quickly. In the plan, the framework for the small **Python sidecar service** that parses PDFs and tables — because Python's document-processing libraries are far ahead of PHP's.

### pdfplumber / camelot
Python libraries for extracting text and, critically, **tables** from PDFs. What actually reads a BDC's Schedule of Investments or a pension CAFR allocation table into structured data.
**Stage:** between 2 and 3.

### AWS Textract
Amazon's managed document/table-extraction service — the "pay per page instead of running Python yourself" alternative to the sidecar.

### S3 — (Amazon) Simple Storage Service
Cloud file storage. Where every retrieved source document is stored **immutably** — your permanent evidence archive and legal defense. (Any S3-compatible storage works.)

### sha256
A cryptographic hash — a fingerprint of a file. Stored with every document so you can prove it hasn't changed and skip re-processing duplicates.

### PostgreSQL / JSONB / CTE
Your database. **JSONB** is Postgres's indexed-JSON column type (flexible metadata like deal values). A **CTE** (Common Table Expression) — specifically a *recursive* CTE — is the SQL feature that walks chains: clinic → DSO → sponsor → fund → pension, in one query. It's what makes the ownership-chain and money-flow views possible without a specialty graph database.

### Redis
In-memory data store; backs Laravel's queues and the per-domain rate limiting on your scrapers.

### Laravel Horizon
Laravel's dashboard for monitoring queued jobs — throughput, failures, retries. Your pipeline observability.

### Laravel Filament
An admin-panel builder for Laravel. The fastest route to the Stage 6 human review interface (claim + highlighted quote + approve/reject).

### Laravel Scout + Meilisearch / Typesense
**Scout** is Laravel's search abstraction; **Meilisearch** and **Typesense** are fast open-source search engines it can drive. Powers fuzzy matching of business names/aliases in Stage 1 and consumer search in Stage 7.

### CSV / JSON
Comma-Separated Values (spreadsheet-style bulk data — how Form 5500 arrives) and JavaScript Object Notation (the structured format the LLM emits claims in and your APIs speak).

### OG image — Open Graph image
The preview image shown when a link is shared on social platforms. Mentioned for the viral single-purpose checkers — each shareable result card generates one.

---

## 5. Quick Map: Which Integration Serves Which Stage

| Stage | Integrations |
|---|---|
| 1 — Entity Resolution | Google Places, NPPES/NPI, state SoS, OpenCorporates, Meilisearch |
| 2 — Retrieval (PE) | Sponsor portfolio pages, EDGAR (8-K, Form D), press wires, Google News RSS, GDELT, DSO rosters, WARN, CourtListener/RECAP |
| 2 — Retrieval (PC) | EDGAR (BDC 10-K/10-Q, N-2), Form ADV/IAPD, DOL Form 5500 bulk, pension CAFRs, NAIC (later) |
| 2→3 — Parsing | Python sidecar (FastAPI + pdfplumber/camelot) or AWS Textract |
| 3 — Extraction | Anthropic API (Claude) |
| 4 — Verification | Pure PHP string matching (no external service — by design) |
| 5 — Scoring | Pure PHP business rules |
| 6 — Review | Filament |
| 7 — Serving | Laravel API + Postgres recursive CTEs + Vue frontend |
