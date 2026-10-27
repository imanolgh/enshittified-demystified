# Research: EDGAR access, BDC identification and SoI formats

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

How do we access EDGAR, identify the BDC universe, and what format are BDC Schedules of Investments in today?

## Find out

- SEC fair-access policy: declared user agent with contact, request rate cap (~10/s?), current wording.
- Submissions API (`data.sec.gov/submissions/CIK{cik}.json`), full-text search API (endpoint, params, form types, pagination, limits), filing index structure, which files of a filing to fetch; EX-99 exhibits.
- Identifying BDCs: no dedicated SIC; 814- file numbers? SEC-published BDC lists? Traded vs non-traded vs private BDCs — does "~150" hold (research_flows.md:129)?
- Primary filing format: HTML/iXBRL vs PDF (bdc-parser assumes PDF; build_roadmap.md:117 says "open each filing PDF").
- Whether BDC Schedules of Investments are now tagged in Inline XBRL (SEC rule changes), which could replace table parsing (bdc-parser SKILL:26 anticipates this).
- 10-Q vs 10-K handling; amendments.


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/edgar-bdc.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- **Access:** declared `User-Agent: <Name> <email>`, at most 10 requests/second per user across all machines, gzip. If you exceed the cap, the SEC throttles your IP until the rate has stayed under it for 10 minutes. No API keys and no CORS. Submissions API: `data.sec.gov/submissions/CIK##########.json` (10-digit CIK; `recent` holds ≥1 year or 1,000 filings, older ones are in extra files). It also has undocumented columns such as `fileNumber`, `isInlineXBRL` and `primaryDocument`.
- **Full-text search:** officially a UI only (filings since 2001, boolean/phrase/NEAR). The JSON endpoint `efts.sec.gov/LATEST/search-index?q=&forms=&startdt=&enddt=&from=` is undocumented. Observed: 100 hits per page and a hard 10,000-result window.
- **Format:** BDC 10-K/10-Q documents of record are **HTML, not PDF**. EDGAR accepts PDF only as an optional unofficial copy alongside the HTML. Ares Capital's 10-K/10-Q primary documents have been `.htm` since at least 2013, and Inline XBRL since its Q3-2022 10-Q.
- **SoI is machine-readable:** Release 33-10771 put BDC financial statements under Inline XBRL (compliance Aug 1, 2022 for short-form-eligible funds, Feb 1, 2023 for the rest). Reg S-T 405(b)(3)/(e) requires every amount in Article 12 schedules, which include the SoI, to be tagged. Filers tag each holding under the typed `us-gaap:InvestmentIdentifierAxis`.
- **The SEC publishes a flattened SoI:** DERA's monthly BDC Data Sets include `soi.tsv`, one row per holding, covering reporting periods from Aug 1, 2022. The 2025-Q4 file has about 122k holding rows from 165 BDCs. Caveats: borrower names are mostly embedded in a free-text identifier (the issuer-name field is filled on only about 2.5% of rows), columns change between updates, and the file is "as filed". JV schedules in EX-99 exhibits and filings before 2022 are untagged HTML.
- **BDC universe:** SIC is blank for BDCs. The marker is an `814-` file number. The SEC's yearly BDC Report (212 entities in 2026) is incomplete: it dropped Ares Capital. Distinct BDC CIKs filing XBRL financials total 171–179 per quarter and 187 across four recent files, so "~150" is low. Of the report entities with 2025–26 filings, 48 are exchange-listed and 119 are not. The SEC has no traded/non-traded/private field.
- **Amendments:** fairly common (13 of 183 submissions in 2025-Q4), and a `/A` may only add exhibits, e.g. Ares Capital's yearly 10-K/A adds Rule 3-09 subsidiary financials. DERA keeps both versions and flags superseded ones with `prevrpt`.

[findings](../research/edgar-bdc.md)
