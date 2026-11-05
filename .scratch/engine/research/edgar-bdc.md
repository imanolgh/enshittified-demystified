# Research: EDGAR access, BDC identification and SoI formats

Ticket: [08-research-edgar-bdc](../issues/08-research-edgar-bdc.md) · Researched 2026-10-26 · Primary sources only: sec.gov pages and data files, the SEC adopting release 33-10771, 17 CFR 232.405 (eCFR), the EDGAR Filer Manual Vol. II, and the FASB taxonomy implementation guide. The FASB guide is included because FASB owns the us-gaap taxonomy. Everything sec.gov was fetched with curl using a declared `User-Agent` (`<name> <email>`). All requests succeeded (HTTP 200). Observations marked **[observed]** come from live EDGAR responses or SEC data files on 2026-10-26. They are not documented behaviour.

**Bottom line:** BDC filings are **HTML, not PDF**. Since the Inline XBRL compliance dates (Aug 1, 2022 / Feb 1, 2023), **every amount in a BDC Schedule of Investments must be XBRL-tagged**. Filers tag each holding under the typed dimension `us-gaap:InvestmentIdentifierAxis`. The SEC (DERA) already publishes a monthly **flattened `soi.tsv`**, one row per holding, covering reporting periods from Aug 1, 2022. Two things are still not machine-readable. First, the borrower name is usually not a separate field: it sits inside a free-text identifier string. Second, joint-venture SoIs filed as EX-99 exhibits are untagged HTML. "~150 BDCs" is low: about 170–187 distinct BDC CIKs file XBRL financial statements in a given recent window.

Sources used throughout:
- [S-DEV] SEC, *Developer Resources*: https://www.sec.gov/about/developer-resources
- [S-ACC] SEC, *Accessing EDGAR Data*: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data
- [S-API] SEC, *EDGAR Application Programming Interfaces*: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- [S-FAQ] SEC, *Webmaster Frequently Asked Questions* (Developers section): https://www.sec.gov/about/webmaster-frequently-asked-questions
- [S-PRIV] SEC, *Web Site Privacy and Security Policy*: https://www.sec.gov/privacy
- [S-FTS] SEC, *Full-Text Search FAQs*: https://www.sec.gov/edgar/search/efts-faq.html
- [S-BDCR] SEC, *Business Development Company Report*: https://www.sec.gov/open/datasets-bdc.html (CSV/XML per year, e.g. https://www.sec.gov/files/investment/data/other/business-development-company-report/business-development-company-2026.csv)
- [S-BDCDS] SEC/DERA, *Business Development Company (BDC) Data Sets*: https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets
- [S-README] SEC/DERA, *BDC Data Set readme* (PDF): https://www.sec.gov/files/bdc_readme.pdf
- [S-PR] SEC press release 2025-96 (June 26, 2025): https://www.sec.gov/newsroom/press-releases/2025-96-sec-publishes-data-broker-dealers-mergers-acquisitions-business-development-companies
- [S-REL] SEC Release 33-10771, *Securities Offering Reform for Closed-End Investment Companies* (Apr 8, 2020; 85 FR 33290): https://www.sec.gov/files/rules/final/2020/33-10771.pdf
- [S-IXBRL] SEC, *Inline XBRL* page: https://www.sec.gov/data-research/structured-data/inline-xbrl
- [S-405] 17 CFR 232.405 (Regulation S-T Rule 405), eCFR: https://www.ecfr.gov/current/title-17/chapter-II/part-232/subpart-232.D/section-232.405
- [S-EFM] SEC, *EDGAR Filer Manual Vol. II*, v78 (Sept 14, 2026): https://www.sec.gov/files/edgar/filermanual/edgarfm-vol2-v78.pdf
- [S-TIG] FASB, *GAAP Taxonomy Implementation Guide: Investment Companies (Including SEC S-X Schedules for BDCs)*, v2.0 (June 2024): https://xbrl.fasb.org/impguidance/BDC_TIG/financialinvestmentcompanies_1.pdf ; draft v3.0 (issued July 9, 2026): https://xbrl.fasb.org/impguidance/BDC1_TIG/financialinvestmentcompanies_1.pdf
- [E-ARCC] Example filer: Ares Capital Corp (CIK 1287750). Submissions JSON: https://data.sec.gov/submissions/CIK0001287750.json ; Q2-2026 10-Q index: https://www.sec.gov/Archives/edgar/data/1287750/000162828026050307/0001628280-26-050307-index.html

---

## 1. SEC fair-access policy

- **Rate cap: 10 requests/second per user, across all of that user's machines.** Wording: "Current guidelines limit each user to a total of no more than 10 requests per second, regardless of the number of machines used to submit requests." [S-DEV] The same cap appears as "Current max request rate: 10 requests/second" [S-ACC] and in [S-FAQ] ("our current maximum access rate is 10 requests per second. This is carefully monitored").
- **What happens if you exceed it:** "If a user or application submits more than 10 requests per second, further requests from the IP address(es) may be limited for a brief period. Once the rate of requests has dropped below the threshold for 10 minutes, the user may resume accessing content." The SEC "reserve[s] the right to block IP addresses that submit excessive requests", and "this policy may change". [S-PRIV]
- **Declared user agent required.** "The SEC does not allow 'unclassified' bots or automated tools to crawl the site." [S-DEV][S-PRIV] "Please declare your user agent in request headers". The sample is `User-Agent: Sample Company Name AdminContact@<sample company domain>.com`, `Accept-Encoding: gzip, deflate`, `Host: www.sec.gov`. [S-ACC][S-FAQ] An undeclared tool gets an "Undeclared Automated Tool" error. [S-FAQ]
- **Etiquette:** "use efficient scripting, downloading only what you need". The SEC offers no technical support for scripted downloading. [S-DEV][S-ACC]
- **No auth or API keys** for data.sec.gov. **No CORS**, so requests must come from a server, not a browser. [S-API]
- [observed] Requests with the declared UA `EvidenceEngine research <email>` succeeded against www.sec.gov, data.sec.gov and efts.sec.gov. The eCFR API (not SEC) requires `Accept-Encoding` compression and returns HTTP 406 without it.

## 2. Submissions API, full-text search, filing structure, which files to fetch

### Submissions API
- URL: `https://data.sec.gov/submissions/CIK##########.json`, using a **10-digit zero-padded CIK**. [S-API]
- Contents: entity metadata (current and former names, tickers, exchanges). `filings.recent` holds "at least one year's of filing or to 1,000 (whichever is more) of the most recent filings in a compact columnar data array". Older filings are in additional JSON files listed in `filings.files` with date ranges. [S-API]
- Freshness: updated in real time. Typical delay is under 1 second for submissions and under 1 minute for the XBRL APIs, and can be longer at peak times. [S-API]
- Bulk: `submissions.zip` (all filers), rebuilt nightly around 3:00 a.m. ET, at https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip. [S-API]
- [observed] Columns in `filings.recent`: `accessionNumber, filingDate, reportDate, acceptanceDateTime, act, form, fileNumber, filmNumber, items, core_type, size, isXBRL, isInlineXBRL, isXBRLNumeric, primaryDocument, primaryDocDescription`. These are not documented on [S-API]. For ARCC, `fileNumber` is `814-00663` on every 10-K, 10-Q, 10-K/A and 8-K. Prospectus filings (497) carry `333-` numbers instead. [E-ARCC]
- **XBRL APIs do not carry SoI line items.** `companyfacts`, `companyconcept` and `frames` aggregate only facts that "Use a non-custom taxonomy" **and** "Apply to the entire filing entity". [S-API] Per-holding SoI facts carry a dimension (`InvestmentIdentifierAxis`), so by this definition they are excluded. (Inference from the stated rule; I did not query companyfacts to confirm.)

### Full-text search (FTS)
- **Officially documented as a UI only** ([S-FTS]). It covers "the full text of all EDGAR filings submitted electronically since 2001", including all exhibits. Supported: boolean `OR`/`NOT`/`-`, exact phrases, trailing-`*` wildcard, `NEAR(n)` (default 10 words), filters for form type, entity/CIK, and date range. Implicit AND, case-insensitive, relevance ranking, no natural-language search. Only FTS indexes filing text; the other EDGAR searches index header metadata only. [S-FAQ]
- **The JSON endpoint behind the UI is undocumented.** I found no SEC page documenting it. [observed] `GET https://efts.sec.gov/LATEST/search-index?q=<query>&forms=<form>[,<form>]&dateRange=custom&startdt=YYYY-MM-DD&enddt=YYYY-MM-DD&from=<offset>` returns Elasticsearch-shaped JSON:
  - `hits.total` (`{"value":..., "relation":"eq"|"gte"}`) and `hits.hits[]`, with `_id` = `<accession>:<document filename>`.
  - Each `_source` has `ciks, display_names, form, root_forms, file_type, file_date, period_ending, adsh, file_num, sics, biz_states, inc_states, items, sequence, file_description`.
  - `aggregations` holds entity, SIC, state and form facets.
  - Page size 100 per request; paginate with `from`.
  - **Hard cap of 10,000 results:** `from + size` > 10000 returns a `Result window is too large` error, and totals beyond that show as `10000/gte`. Large result sets must be split by date range or form.
  - Whether the 10 req/s cap applies separately to efts.sec.gov is not stated. The policy covers "SEC.gov content". [S-PRIV]

### Filing index structure and which files to fetch
- Paths: the complete submission is at `/Archives/edgar/data/{cik}/{accession}.txt`. The per-filing directory is `/Archives/edgar/data/{cik}/{accession-no-dashes}/`, and `{accession}-index.html` lists the documents with their type. Each CIK and accession directory also serves hidden `index.json` and `index.xml` files for automated crawling. [S-ACC]
- Accession number format: `0001193125-15-118890`. The first 10 digits are the CIK of the **submitter**, which may be a filing agent rather than the company. The middle 2 digits are the year, then a sequence number. [S-ACC][S-FAQ]
- Post-acceptance corrections: filings can be removed or corrected after acceptance. Full and quarterly indexes are rebuilt weekly (Saturday) to reflect this. [S-ACC]
- [observed] ARCC Q2-2026 10-Q (`0001628280-26-050307`), from `index.json` and `-index.html`:
  - `arcc-20260630.htm`, the **primary document, type 10-Q, flagged "iXBRL"** (24.8 MB). The SoI is inside this document.
  - Taxonomy extension files: `.xsd`, `_cal.xml`, `_def.xml`, `_lab.xml`, `_pre.xml`.
  - `arcc-20260630_htm.xml` (14.6 MB), the XBRL instance in plain XML.
  - `FilingSummary.xml`, `MetaLinks.json`, and rendered `R1.htm`…`R87.htm` pages. Several are multi-MB; R9/R49/R52 are 5–12 MB.
  - `…-xbrl.zip`.
  - Exhibits EX-31.1/31.2/32.1, and **EX-99.1 `arccq2-2026ex991xsdlpconde.htm`**.
- **EX-99 exhibits:** the ARCC 10-Q EX-99.1 is the *Senior Direct Lending Program, LLC Consolidated Condensed Schedule of Investments*, a joint venture's own loan list with borrower names, par, rate and spread. [observed] It contains **zero `ix:` tags**, so it is plain HTML that needs table parsing. ARCC's 10-K/A filings attach the audited financials of an unconsolidated portfolio company (Ivy Hill Asset Management) as **EX-99.3** under Reg S-X Rule 3-09. The 10-K/A explanatory note says so: https://www.sec.gov/Archives/edgar/data/1287750/000162828026020560/arcc-20251231.htm. How common JV/3-09 exhibits are across BDCs was not surveyed.

## 3. Identifying BDCs; how many; traded vs non-traded vs private

- **814- file numbers are the official marker.** The SEC's BDC Report covers "all entities with an 'active' filing status that have been issued an 814- reporting number": either N-6F filers (notice of intent) or N-54A filers (election to be regulated as a BDC). It includes N-6F filers that have not started selling shares, and entities that have ceased operations but not filed N-54C (withdrawal). Fields: File Number, CIK, Name, address, Date/Type of Last Filing. Published yearly as CSV and XML; the latest is "Updated 6/1/2026". [S-BDCR]
- **No dedicated SIC.** [observed] Submissions JSON for ARCC, CSWC, GBDC, PNNT, Blackstone Private Credit Fund and Blue Owl Credit Income Corp all have `sic: ""` and `entityType: "operating"`. An SIC- or entity-type-based discovery step (as in research_flows.md:129) would therefore not find them.
- **The BDC Report is not a complete list.** [observed]
  - The 2026 CSV has 212 entities, 167 of them with a last filing in 2025–26. The 2025 CSV has 196 entities. The union of the two years is 227.
  - **Ares Capital (814-00663, the largest BDC) is in the 2025 file but missing from the 2026 file**, even though it filed 10-Qs under that number in April and July 2026.
  - 18 of the 171 CIKs in DERA's 2025-Q4 BDC data set are missing from the 2026 report, including Sixth Street Specialty Lending, Gladstone Capital, Trinity Capital, Monroe Capital and Goldman Sachs Private Credit Corp.
- **The DERA BDC Data Sets give a better "files financials" universe.** Their scope is any XBRL submission "with file number beginning with '814-' OR a filer who previously filed an N-54A and is yet to file an N-54C", with financial statements (10-K, 10-Q), for reporting periods on or after Aug 1, 2022. [S-README] [observed] Distinct CIKs in `sub.tsv`:

  | File | Distinct CIKs | Forms |
  |---|---|---|
  | 2025 Q4 | 171 | 158 10-Q, 12 10-K, 10 10-Q/A, 3 10-K/A |
  | 2026-03 | 121 | 10-K season |
  | 2026-05 | 179 | |
  | 2026-08 | 174 | |
  | Union of the four files | **187** | |

  So **"~150" understates the current universe**. About 175–180 BDCs file a 10-Q each quarter, and the 814- population including dormant entities is above 200.
- **Traded vs non-traded vs private:** the SEC publishes **no official classification** in either dataset. The SEC's investor bulletin covers only *publicly traded* BDCs: https://www.sec.gov/oiea/investor-alerts-and-bulletins/investor-bulletin-publicly-traded-business-development-companies (cited for existence only; not used for counts). [observed] Proxy check using the `exchanges` field in the submissions JSON, over the 167 report entities with 2025–26 filings: **48 exchange-listed, 119 with no exchange.** The no-exchange group mixes non-traded public BDCs (registered offerings, e.g. 497/424B3 filers) and privately offered BDCs. Telling them apart would need a further signal, such as whether the BDC files prospectuses under a `333-` registration. That signal is not confirmed.

## 4. Primary filing format: HTML/iXBRL vs PDF

- **EDGAR official documents are ASCII or HTML. PDF is normally only an unofficial companion copy.** "The EDGAR system accepts ASCII, HTML, XML and, in some cases, XBRL or PDF primary documents … Two other document formats can be used as unofficial copies: PDF and, in some cases, XBRL." [S-EFM §2] "Unofficial PDF documents may not be submitted to EDGAR without their official ASCII/HTML versions". An official document may have **one** supplemental unofficial PDF. [S-EFM §5.2.3.5]
- [observed] Every ARCC 10-K/10-Q primary document from 2013 to 2026 is `.htm`. From the Q3-2022 10-Q (filed 2022-10-25) onward, `isInlineXBRL=1`; through the Q2-2022 10-Q (filed 2022-07-26), `isInlineXBRL=0`. [E-ARCC] The 2026 10-Q directory contains no PDF.
- The DERA SOI file links each row to the inline viewer (`inlineurl`, e.g. `https://www.sec.gov/ix?doc=/Archives/edgar/data/…/orcic-20250930.htm`). [S-README][observed]
- So the premise in bdc-parser SKILL.md (pdfplumber over PDFs) and build_roadmap.md:117 ("open each filing PDF") does not match EDGAR. The document of record is an HTML/iXBRL file. A PDF exists only if a filer chose to attach an unofficial copy.

## 5. Are BDC Schedules of Investments tagged in Inline XBRL?

**Yes, since the 2022–2023 compliance dates.**
- **Rule:** Release 33-10771 (adopted Apr 8, 2020; effective Aug 1, 2020) amended Reg S-K Item 601(b)(101) and Reg S-T Rule 405(b)(3)(i) to require "BDCs, like operating companies, to submit financial statement information using Inline XBRL format", removing the earlier BDC exclusion. [S-REL pp. 77–78] The SEC's Inline XBRL page: "BDCs must tag the financial statements and other disclosures in their Exchange Act reports to the same extent as required for operating companies." [S-IXBRL]
- **Compliance dates:** funds eligible for short-form registration had to comply by **August 1, 2022**; "All other affected funds … February 1, 2023". [S-REL pp. 112–113]
- **What must be tagged:** for a BDC, the Interactive Data File must cover the complete financial statements, including footnotes, **and "All schedules set forth in §§ 210.12-01 through 210.12-29 (Article 12 of Regulation S-X)"**. [S-405 (b)(3)(i)] The schedule of investments is Article 12 (Rule 12-12, *Investments in securities of unaffiliated issuers*, is referenced in [S-REL]). For Article 12 schedules: "Each complete financial statement schedule must be block-text tagged" **and** "Each amount (i.e., monetary value, percentage and number) must be tagged separately". Narrative may be tagged at the filer's option. [S-405 (e)]
- **How filers tag it (FASB taxonomy):** the typed dimension **`Investment, Identifier [Axis]` (`InvestmentIdentifierAxis`)** "is intended to be used to tag each issue of investment and its related information. The members … are unique for each issue and are part of the instance document and not in the extension taxonomy". Explicit axes (issuer affiliation, type, industry) are for disaggregated totals. Per-holding attributes use extensible enumerations, including `Investment, Issuer Name [Extensible Enumeration]` (XL76), `Investment, Type`, `Industry Sector`, and `Variable Interest Rate, Type`. [S-TIG v2.0 §1, Ex. notes] The FASB guide is "not authoritative". [S-TIG] Draft v3.0 (July 2026; 2026qx taxonomy, pending SEC acceptance) adds a "virtual fact option" that packs non-numeric per-investment data into the typed member as key-value pairs. [S-TIG v3.0]
- [observed, ARCC Q2-2026 instance]
  - 3,881 contexts use `us-gaap:InvestmentIdentifierAxis` as a typed member with free text. Example: `UKG Inc. and H&F Unite Partners, L.P., Limited partnership interests`, with `InvestmentOwnedBalanceShares`, `InvestmentOwnedAtCost` and similar facts attached.
  - 7,658 `InvestmentOwnedAtFairValue` occurrences.
  - 774 contexts use `InvestmentIssuerNameAxis`.
- **The SEC already publishes a flattened SoI.** DERA's **BDC Data Sets** (first press-released June 26, 2025 [S-PR]) cover Oct 2022–Sept 2026 [S-BDCDS] and are monthly zips (quarterly for older years) containing `sub, tag, num, txt, pre, cal, non` tables plus **`soi.tsv`**, "one row for each holding reported on the schedule of investments". [S-README]
  - **Preset `soi.tsv` columns:** `adsh, cik, name, ddate, form, filed, period, inlineurl, cstm`; Industry Sector Axis, Investment Identifier Axis, Issuer Affiliation Axis, Investment Type Axis; Interest Rate, Basis Spread, Maturity Date, Principal Amount, Cost, Fair Value, % Net Assets. A `qtrs` column was added Sept 2026. [S-README][S-BDCDS]
  - **Dynamic columns:** other columns are created dynamically, so column positions and sets "may change for each update". The file "excludes any custom tags and custom axis reported; custom members are included". It is "as filed" and has no key. [S-README]
  - **Revision history:** the files have been refreshed repeatedly (June/July/Sept/Oct 2026: typed dimensions, untruncated footnotes, a parsing fix, previously excluded SOI records restored). [S-BDCDS]
  - [observed, 2025-Q4 zip, 33 MB; `soi.tsv` 96 MB] 160,886 rows from 167 CIKs. **122,242 rows** (165 CIKs) have an Investment Identifier; the rest are subtotal and disaggregation rows. 256 columns.
  - Column names did not all match the readme. In this file the fair-value and cost values sat under filer-label-like columns ("Initial fair value of Investment", "Adjusted cost basis"), while the preset "Investment Owned, Fair Value" column was empty in the rows sampled. The `cstm` values are `0`/`1`; the readme says `1`/`2`.
  - **Issuer Name enumeration** was populated on only 3,056 of 122,242 holding rows. Usually the borrower name has to be parsed out of the identifier text. Example (PennantPark): `Investments in Non-Controlled, Non-Affiliated Portfolio Companies First Lien Secured Debt Issuer Name Ad.net Acquisition, LLC - Funded Revolver Maturity 05/07/2026 Industry Media Current Coupon 10.93% …`.

## 6. 10-Q vs 10-K; amendments

- Both forms carry a full Schedule of Investments and are in scope of the tagging rule and the DERA data sets ("e.g., 10-K, 10-Q"). [S-405][S-README] The XBRL data APIs list "10-Q, 10-K … and their variants" as covered forms. [S-API]
- **Amendments are common and vary in content.** [observed] 2025-Q4 DERA `sub.tsv`: 10 × 10-Q/A and 3 × 10-K/A against 170 originals. ARCC files a 10-K/A every year, and the ones checked (2025, 2026) only add Rule 3-09 subsidiary financials (EX-99.3) and new certifications. "Except as described above, no other changes have been made". In other words, a `/A` is not necessarily a restated SoI.
- DERA's `sub.tsv` field `prevrpt` = TRUE "indicates that the submission information was subsequently amended prior to the end cutoff date of the table". The data sets keep both original and amended submissions "as filed", so they "may contain redundancies". [S-README]
- `fp` (FY/Q1–Q4) and `fy` come from the XBRL DEI and are in `sub.tsv`. [S-README]

---

## Implications for the design (facts and consequences only)

- **The "PDF" premise is wrong for EDGAR.** BDC 10-K/10-Q documents of record are HTML (iXBRL since 2022–23). A pdfplumber/camelot pipeline would have to run on a filer's optional unofficial PDF, or on a rendering of the HTML. The bdc-parser skill, build_roadmap Step 21 ("open each filing PDF") and research_flows B1b step 3 all assume PDF.
- **Since Aug 2022 / Feb 2023, structured SoI data exists two ways:** (a) parse the filing's own XBRL instance (`*_htm.xml`, or the ix-tags in the primary `.htm`) and group facts by `InvestmentIdentifierAxis` member; (b) download DERA's monthly `soi.tsv`. Both are the filer's tagged data. (b) is an SEC-derived flattening with a disclaimer, a column layout that shifts over time, and a history of refreshes. The skill's line 26 already anticipates this kind of strategy change ("propose it with trade-offs — the developer decides").
- **For citation quoting:** the typed-member identifier string is filer text inside the filing, and the HTML table row is also in the stored document. Which of the two counts as "the quote" for `verify_citations`, and whether a numeric cross-check of the quoted principal against the structured value can use XBRL facts, are open design questions. The data supports either.
- **Borrower name is not a clean field in most filings.** Only ~2.5% of holding rows carry the `Issuer Name` enumeration. Elsewhere it is embedded in free text whose format differs by filer, so name extraction per filer convention remains a parsing task even with XBRL.
- **Gaps that need HTML table parsing even with XBRL:** pre-iXBRL history (filings before Aug 2022 / Feb 2023), JV/SLF schedules of investments in EX-99 exhibits (untagged), and Rule 3-09 exhibits.
- **BDC discovery:** SIC-based discovery will not work (SIC is blank). Possible universe sources are the yearly BDC Report (814- numbers, but it has demonstrably dropped live BDCs such as ARCC), DERA `sub.tsv` (BDCs that actually filed XBRL financials), and per-CIK `fileNumber` starting `814-` in the submissions JSON. Their counts differ (212 / 187 / not enumerated). The "~150" figure in build_roadmap Step 20 and research_flows:129 is below the observed ~175–187.
- **Rate and politeness constraints for the connector:** ≤10 req/s total, declared `Name email` UA, gzip, and a 10-minute cooldown if throttled. Primary documents and R-pages run to tens of MB, so download cost is size-driven more than request-count-driven. FTS has a hard 10,000-result window per query.
- **Amendments:** a `/A` may only add exhibits, so it cannot be treated as a full SoI replacement without checking. DERA's `prevrpt` flag only covers amendments within each file's cutoff.

## Unconfirmed / open

- **FTS JSON API** (`efts.sec.gov/LATEST/search-index`): parameters and the 10k cap are observed, not documented. The SEC could change it without notice. Whether its rate limit is separate from www.sec.gov's is unknown.
- Whether the Inline XBRL compliance dates key off **filing date or fiscal period end**. The release says "comply … August 1, 2022" without saying which. DERA's scope uses reporting period ≥ Aug 1, 2022. ARCC's first iXBRL 10-Q was for the period ended Sept 30, 2022, filed Oct 25, 2022.
- Which BDCs qualified for the Aug 2022 date (short-form eligible) versus Feb 2023, and whether any BDC voluntarily filed iXBRL earlier: not enumerated.
- Why the 2026 BDC Report omits ARCC and other live BDCs. Possibly an "active filing status" artefact; the SEC does not explain it.
- Whether `*_htm.xml` is generated by EDGAR or supplied by the filer. It is present in the filing directory, but no Filer Manual passage confirming its provenance was found in Vol. II.
- The mismatch between `soi.tsv` preset column names and the columns actually populated in the 2025-Q4 file (fair value under "Initial fair value of Investment"), and `cstm` values 0/1 versus the readme's 1/2. Only one quarterly file was inspected. The Sept 2026 refresh ("resolve a parsing issue") may have changed this.
- How consistently BDCs tag every SoI amount, i.e. the share of filings where the `soi.tsv` row count matches the HTML table row count. DERA's `detail` flag was 1 for all 183 submissions in 2025-Q4, but that flag is not a row-level completeness check.
- Splitting non-traded public from private BDCs: no official SEC field found. The `333-` prospectus heuristic is untested.
- Prevalence of JV/SLF EX-99 SoIs and Rule 3-09 exhibits across the universe: only ARCC inspected.
- XBRL `companyfacts` exclusion of dimensional SoI facts is inferred from [S-API]'s definition, not tested.
