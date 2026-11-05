# Research: Form ADV and IRS exempt-org bulk data

Ticket: [07-research-form-adv-irs](../issues/07-research-form-adv-irs.md) · Researched 2026-10-26 · Primary sources only (SEC, IRS, and the files themselves).

**Question:** What do the SEC Form ADV bulk data and the IRS exempt-organization bulk data contain, and can they establish owner kinds at rank 1 ([ADR 0001](../../../docs/adr/0001-ownership-category-computed-by-code.md))?

**Short answer:** Yes for Form ADV, but **two different SEC products** are needed. One is current but adviser-level only. The other is fund-level but stops at 2024-12-31. The IRS files identify an *entity* as tax-exempt by EIN. They do not say what that entity owns, except in Form 990 Schedule R.

"Verified by download" below means I fetched the file on 2026-10-26 and read its header and rows directly.

---

## 1. Form ADV — what bulk data exists

The SEC publishes three bulk products. They differ in freshness and in how much detail they carry.

| Product | Format / cadence | Coverage | Private-fund detail |
|---|---|---|---|
| **A. FOIA "Form ADV Data" historical archive** | ZIP of CSV tables; one-time archive files, not periodic | Part 1A filings, 2000-10-19 → **2024-12-31**. Covers SEC-registered advisers *and* exempt reporting advisers (ERAs) | **Full Schedule D 7.B.(1), one row per fund per filing** |
| **B. Monthly "Information About Registered Investment Advisers and Exempt Reporting Advisers"** | ZIP holding one CSV; monthly; one file for registered advisers, one for ERAs | Latest filing per adviser, current (Oct 2026 file: latest filing dates up to 2026-10-01) | **Adviser-level counts per fund type** (e.g. `Any PE Funds`, `Total number of PE funds`); no fund names |
| **C. IAPD daily compilation feed** (`IA_FIRM_SEC_Feed_MM_DD_YYYY.xml.gz`) | gzipped XML; daily | All SEC-registered advisers + ERAs (2026-10-26: 17,259 registered, 6,795 ERA) | Only the Item 7.B yes/no flag (`<Item7B Q7B="Y"/>`); **no Schedule D** |

Sources:
- A: [SEC FOIA — Form ADV Data](https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data). The page says data "from January 1, 2025 onward" is on [IAPD](https://adviserinfo.sec.gov/adv) and the archive files cover data through 2024-12-31. Files: [`adv-filing-data-20111105-20241231-part1.zip`](https://www.sec.gov/files/adv-filing-data-20111105-20241231-part1.zip) (705 MB, last-modified 2026-10-13) and [`…-part2.zip`](https://www.sec.gov/files/adv-filing-data-20111105-20241231-part2.zip) (429 MB). Contents verified by download (zip directory read with HTTP range requests). The page says the "data sets consist of multiple tables that may need to be combined or linked". No data dictionary is linked.
- B: [SEC — Information About Registered Investment Advisers and Exempt Reporting Advisers](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers). Monthly since July 2006 (ERA files since Feb 2012). Oct and Nov 2025 are "no-data" PDFs, and Jan 2019 is missing (government shutdown). Columns verified by download: [`ia100226.zip`](https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia100226.zip) (448 columns, 17,210 advisers; the CSV inside is named `ia09012026.csv`) and [`ia100226-exempt.zip`](https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia100226-exempt.zip) (171 columns, 6,778 ERAs). The page says: "Please refer to the Form ADV for a full description of the data fields". In other words, no data dictionary; column headings name Form ADV items.
- C: e.g. [`IA_FIRM_SEC_Feed_10_26_2026.xml.gz`](https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_FIRM_SEC_Feed_10_26_2026.xml.gz). A new file was posted every day 10-23 through 10-26 (~7 MB gz, ~83 MB XML). Element inventory verified by download. I found this URL pattern by probing. I did not find a written SEC description of it (IAPD pages are JavaScript and did not render for fetching).

**Gap:** In no SEC bulk product I found does fund-level 7.B.(1) data run past 2024-12-31. For 2025 onward, fund-level data appears only on IAPD, one adviser at a time, as a Form ADV PDF. Example: [`reports.adviserinfo.sec.gov/reports/ADV/342972/PDF/342972.pdf`](https://reports.adviserinfo.sec.gov/reports/ADV/342972/PDF/342972.pdf), which contains Section 7.B.(1) with fund name and `805-` ID (verified by download). Caveat: in that PDF the Q10 fund-type checkboxes are graphics. Plain text extraction (pypdf) prints all seven options and does not show which one is checked.

## 2. Schedule D Section 7.B.(1) — the fund-type field

- **Who must file it:** any adviser answering "yes" to Item 7.B ("Are you an adviser to any private fund?") "must complete a Section 7.B.(1) of Schedule D" for **each** private fund. There is one exception: if another SEC-registered adviser or ERA already reports that fund (e.g. you are a subadviser), you file Section 7.B.(2) instead. Advisers may identify a fund by a code instead of its name under rule 204-2(d) ("to preserve the anonymity of a private fund client"). [Form ADV Part 1A, Item 7.B, p.18–19](https://www.sec.gov/files/formadv-part1a_1.pdf)
- **The field:** Question 10, "What type of fund is the private fund?" Exactly one of: hedge fund · liquidity fund · private equity fund · real estate fund · securitized asset fund · venture capital fund · Other private fund (free text). [Form ADV Part 1A, Schedule D §7.B.(1) Q10](https://www.sec.gov/files/formadv-part1a_1.pdf)
- **Definitions** ([Form ADV General Instructions / Part 1A Instruction 6.e.(2), SEC 1707 (07-24), p.24–25](https://www.sec.gov/files/formadv-instructions.pdf)):
  - "**Private equity fund** means any private fund that is not a hedge fund, liquidity fund, real estate fund, securitized asset fund, or venture capital fund and does not provide investors with redemption rights in the ordinary course." In other words, PE is defined *by exclusion*.
  - "Venture capital fund" = meets rule 203(l)-1. "Real estate fund" = not a hedge fund, no ordinary-course redemption rights, invests primarily in real estate. "Hedge fund" = performance fee on unrealized gains, borrowing > ½ NAV / gross notional > 2× NAV, or short selling. "Other private fund" = none of the above.
- **Values in the bulk CSV** (column `Fund Type`, verified by download). Exact strings: `Private Equity Fund`, `Venture Capital Fund`, `Hedge Fund`, `Real Estate Fund`, `Securitized Asset Fund`, `Liquidity Fund`, `Other Private Fund`, plus a `Fund Type Other` free-text column. Counts in `ERA_Schedule_D_7B1` (all filings 2011–2024, not distinct funds): VC 207,103 · PE 86,857 · Hedge 37,751 · Other 16,530 · Real estate 11,689 · Securitized 1,936 · Liquidity 532.
- **Other 7.B.(1) columns** (`IA_/ERA_Schedule_D_7B1_*.csv`, verified): `FilingID, Fund Name, Fund ID, ReferenceID, State, Country, 3(c)(1)/3(c)(7) Exclusion, Master Fund, Feeder Fund, Master Fund Name, Master Fund ID, Fund of Funds, …, Fund Type, Fund Type Other, Gross Asset Value, Minimum Investment, Owners, %Owned You or Related, …, Prime Brokers, Custodians, Administrator, … Marketing`.
- **Child tables keyed by `FilingID` + `ReferenceID`** (verified headers):
  - `7B1A3a` — "Name of Partner, etc." (Q3a: general partner / manager / trustee / directors)
  - `7B1A3b` — "Filing/Relying Adviser" (Q3b: which adviser in an umbrella registration sponsors the fund)
  - `7B1A6b` / `7B1A7` — feeder/master fund names + `Fund ID`
  - `7B1A17b` / `7B1A18b` — other advisers/subadvisers: `Name of Adviser, SEC File Number, CRD Number`
  - `7B1A22` — `Form D File Number`
  - `7B1A28` — marketers
  - `7B2` — subadvised funds: `Fund Name, Fund ID, Adviser Name, Adviser SEC Number`

## 3. Identifiers

| Identifier | Where | Notes |
|---|---|---|
| **CRD number** (adviser) | Bulk A base tables, column `1E1`; B `Organization CRD#`; C `FirmCrdNb` | Item 1.E |
| **SEC file number** | A `1D`; B `SEC#`; C `SECNb` | `801-` = SEC-registered adviser, `802-` = ERA (observed in data, e.g. `801-688`, `802-136595`) |
| **CIK** | A `IA_1D3_CIK` / `ERA_1D3_CIK` tables; B `CIK#` | Item 1.N, if the adviser has one |
| **Private fund ID** | 7.B.(1) `Fund ID`, format `805-##########` | The adviser "must acquire an identification number for the fund … using the private fund identification number generator" on IARD, "must continue to use the same identification number whenever you amend". If another adviser already acquired a number for that fund, "you must not acquire a new identification number, but must instead utilize the existing number." [Instructions 6.b, p.23](https://www.sec.gov/files/formadv-instructions.pdf) |
| **Form D file number** | `7B1A22` (`021-…`) | Links a fund to its EDGAR Form D |
| **FilingID** | Key across all bulk A tables | One per filing (initial/annual/other-than-annual amendment; see `ADV_Filing_Types`). Base table `FilingID` → `1E1` CRD gives fund → adviser |

**Fund → adviser link:** yes, for 2011-11 to 2024-12. The route is `Schedule_D_7B1.FilingID` → `ADV_Base.FilingID` → CRD / SEC#. The fund carries a **name** (`Fund Name`), a stable cross-adviser **ID** (`805-`), and its GP/manager entity names (`7B1A3a`). Caveats: names may be codes under rule 204-2(d), and series/classes managed separately count as separate funds ([Instructions 6.c](https://www.sec.gov/files/formadv-instructions.pdf)).

**Cadence of underlying filings:** an annual updating amendment is due "within 90 days after the end of your fiscal year". Some items also need other-than-annual amendments "promptly" ([Instructions, General Instruction 4](https://www.sec.gov/files/formadv-instructions.pdf)). So fund lists can be up to ~15 months stale. Observed: most `Latest ADV Filing Date` values fall in late March (December fiscal-year filers).

## 4. Exempt reporting advisers (ERAs)

- ERAs file only Items 1, 2, 3, 6, 7, 10 and 11 of Part 1A plus the matching schedules. That includes Item 7 and therefore Schedule D 7.B.(1). [Instructions, "How is Form ADV organized?"](https://www.sec.gov/files/formadv-instructions.pdf); [SEC monthly-data page](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers)
- ERA bases (Item 2.B): solely VC funds (rule 203(l)-1), or solely private funds with < $150 M US AUM (rule 203(m)-1). [Form ADV Part 1A, Item 2.B](https://www.sec.gov/files/formadv-part1a_1.pdf)
- All three bulk products include ERAs: A has separate `ERA_*` tables; B has the `-exempt` file; C has `FirmType="ERA"`.
- Oct 2026 snapshot (bulk B): `Any PE Funds = Y` for **2,578 of 17,210** registered advisers and **1,994 of 6,778** ERAs.
- Not covered: state-registered advisers ("SEC does not have state-registered adviser data", [FOIA page](https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data)), and advisers exempt from both registration and reporting (e.g. family offices, foreign private advisers). Those categories come from the Advisers Act exemptions. I did not research their sizes.

## 5. IRS — Exempt Organizations Business Master File (EO BMF)

- **Format:** CSV, split by state (+DC, PR, international `eo_xx.csv`) and into 4 regional files. Sorted by EIN. State is the filing (headquarters) address. 1,975,975 records as posted 2026-10-13. [IRS EO BMF page](https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf)
- **Cadence:** "Exempt organization information is extracted monthly" and the file is "cumulative … the most recent information the IRS has". [EO BMF information sheet, Jan 2026](https://www.irs.gov/pub/foia/ig/tege/eo-info.pdf)
- **Fields** (verified against [`eo_ri.csv`](https://www.irs.gov/pub/irs-soi/eo_ri.csv) header): `EIN, NAME, ICO, STREET, CITY, STATE, ZIP, GROUP, SUBSECTION, AFFILIATION, CLASSIFICATION, RULING, DEDUCTIBILITY, FOUNDATION, ACTIVITY, ORGANIZATION, STATUS, TAX_PERIOD, ASSET_CD, INCOME_CD, FILING_REQ_CD, PF_FILING_REQ_CD, ACCT_PD, ASSET_AMT, INCOME_AMT, REVENUE_AMT, NTEE_CD, SORT_NAME`.
  - `SUBSECTION` = the 501(c) paragraph (e.g. `03`); `CLASSIFICATION` refines it (1–4 codes)
  - `FOUNDATION` = private foundation / public charity type
  - `ORGANIZATION` = 1 corporation, 2 trust, 3 co-op, 4 partnership, 5 association
  - `STATUS` = 01 unconditional, 02 conditional, 12 4947(a)(2) trust, 25 terminating PF status
  - [info sheet](https://www.irs.gov/pub/foia/ig/tege/eo-info.pdf)
- **What it excludes:** "Self-declared organizations; Churches and other organizations that are not required under the Code to file an application and that have not filed an application …; Split interest trusts". Revoked organizations' names are "removed from publicly accessible venues, including this file". [info sheet](https://www.irs.gov/pub/foia/ig/tege/eo-info.pdf)
- **Version note:** an older copy at [`/pub/irs-soi/eo-info.pdf`](https://www.irs.gov/pub/irs-soi/eo-info.pdf) is dated November 2023. The BMF page links the January 2026 copy.

### Related IRS bulk sets ([TEOS bulk downloads](https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads), "updated monthly")
- **Pub 78** ([zip](https://apps.irs.gov/pub/epostcard/data-download-pub78.zip), pipe-delimited, updated 2026-09-10). Lists organizations eligible for deductible contributions. Rows as downloaded are `EIN|Name|City|State|Country|deductibility code` (e.g. `…|PC`), ~1.43 M lines. Registered names only, no DBAs. This six-field layout comes from the file itself; the IRS describes columns in [Pub 5891](https://www.irs.gov/pub/irs-pdf/p5891.pdf), which I did not read.
- **Auto-revocation list** ([zip](https://apps.irs.gov/pub/epostcard/data-download-revocation.zip)) and **990-N e-Postcard** ([zip](https://apps.irs.gov/pub/epostcard/data-download-epostcard.zip)), pipe-delimited.
- **Form 990-series e-file XML** ([downloads page](https://www.irs.gov/charities-non-profits/form-990-series-downloads)). Years 2019–2026 as monthly `YYYY_TEOS_XML_NN[A-D].zip` files, plus one `index_YYYY.csv` per year. Verified index header: `RETURN_ID, FILING_TYPE, EIN, TAX_PERIOD, SUB_DATE, TAXPAYER_NAME, RETURN_TYPE (990/990EZ/990PF), DLN, OBJECT_ID, XML_BATCH_ID`. Schemas are on the TEOS schemas page.
- **Form 990 Schedule R** is the only IRS source that names what a nonprofit *owns*. It is filed when Form 990 Part IV line 34 is "yes" (related organizations). [Instructions for Schedule R (12/2024)](https://www.irs.gov/instructions/i990sr)
  - Part III: related partnerships. Columns include the filer's percentage ownership and whether it is general/managing partner.
  - Part IV: related C/S corporations and trusts. Columns include name, EIN, direct controlling entity, percentage ownership, and whether it is a §512(b)(13) controlled entity.
  - Control of a stock corporation = owning "more than 50% of the stock" (by vote or value).

### How the IRS data identifies a nonprofit owner
The BMF (and Pub 78) answers one question: *is this EIN a recognized tax-exempt organization, under which subsection*. They carry no ownership or subsidiary data. To mark an owner `nonprofit` from them, you need the owner's EIN, or a name+address match against `NAME`/`SORT_NAME`/`STREET`/`CITY`/`STATE`/`ZIP`. The other direction (nonprofit → businesses it controls) exists only in Form 990 Schedule R XML, by name and EIN, for e-filed 990s.

## 6. Licensing / terms

- **SEC:** "Information presented on sec.gov is considered public information and may be copied or further distributed by users of the web site without the SEC's permission"; citation to the SEC is requested. Automated access is capped at "no more than 10 requests per second, regardless of the number of machines", and "unclassified" bots are not allowed. [SEC Privacy & Security / website policies](https://www.sec.gov/about/privacy-information). SEC caveat on Form ADV data: "Neither the SEC nor the state securities authorities have approved the information filed on Form ADV, and we can not guarantee its accuracy." [monthly-data page](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers)
- **IRS:** neither the bulk pages nor the IRS privacy policy states terms of use. As works of the U.S. Government they are not copyrightable: "Copyright protection under this title is not available for any work of the United States Government" ([17 U.S.C. §105(a)](https://www.law.cornell.edu/uscode/text/17/105), statute text via Cornell LII).
- **IAPD (adviserinfo.sec.gov):** I could not find terms of use (JavaScript site). See Unconfirmed.

---

## Implications for the design

These are facts and consequences only. The developer decides.

1. **The ADR 0001 `pe_firm` test can be answered from official bulk data at the adviser level, for current data.** Monthly bulk B gives `Any PE Funds` (Y/N) and `Total number of PE funds` per CRD/SEC#, for registered advisers and ERAs. These values are SEC aggregates of Q10 answers.
2. **Fund-level data (fund name → adviser, fund type per fund) is in bulk only through 2024-12-31.** A business owned by "XYZ Capital Partners IV, L.P." can be linked to its adviser through `Fund Name` / `805-` ID / GP names (`7B1A3a`) only from the historical archive. Funds formed in 2025+ appear only in per-adviser IAPD PDFs, and their fund-type checkbox does not come out as plain text.
3. **"Private equity fund" is a residual category.** The adviser self-classifies it under the SEC's exclusion-based definition. VC funds under rule 203(l)-1 are always a separate type, so ADR 0001's PE/VC split matches the form exactly. Advisers advising "Other private fund" or mixed types will exist, and their ADR treatment is not specified by the form.
4. **Coverage holes are structural.** Advisers that neither register with the SEC nor report as ERAs are absent: state-registered advisers, family offices, foreign private advisers. A PE firm missing from Form ADV is not evidence it is not PE.
5. **Each fact has a filing date.** Bulk A rows key to `FilingID` with `DateSubmitted`. Bulk B gives `Latest ADV Filing Date`. Fund lists refresh at least annually, within 90 days of fiscal year-end.
6. **The `nonprofit` owner kind from IRS data depends on an EIN or name/address match.** The BMF says an entity is exempt; it says nothing about holdings. Churches that never applied, and revoked organizations, are absent. Nonprofit → subsidiary links exist only in Schedule R of e-filed 990 XML.
7. **The bulk files are large but few.** Bulk A is ~1.1 GB zipped, and its biggest single CSV is ~770 MB. Bulk B is ~6 MB/month. Bulk C is ~7 MB/day. Per-firm IAPD PDF fetches fall under the 10 req/s sec.gov cap.

## Unconfirmed / open

- **Whether any SEC bulk product carries fund-level 7.B.(1) for 2025+.** The FOIA page says 2025+ data "is on" IAPD, and I found only per-firm PDFs there. IAPD's "compilation reports" menu did not render for fetching. The daily XML feed I found has no Schedule D. If the archive gets extended (part1 was re-posted 2026-10-13 but still ends 2024-12-31), this gap closes.
- **How to read the Q10 checkbox from IAPD per-firm PDFs.** It may be recoverable from PDF drawing objects. Not tested.
- **Written documentation for the IAPD daily XML feed.** A "Compilation Report XML Guide" (IARD, release 2021.10) is referenced in search results; I did not locate or read it.
- **IAPD terms of use**: not found.
- **Exact methodology behind bulk B's `Any PE Funds`** (latest filing only? includes 7.B.(2) subadvised funds?). The page gives no data dictionary.
- **Data dictionary for the FOIA archive tables:** none linked. Column meanings are inferred from Form ADV item numbers in the headers.
- **Distinct-fund counts** (vs. filing-row counts) in the archive were not computed.
- **Pub 78 column definitions** are in [Pub 5891](https://www.irs.gov/pub/irs-pdf/p5891.pdf), not read. The layout above is from the file itself.
- **Mismatched filename in bulk B:** the registered October 2026 zip (`ia100226.zip`) contains `ia09012026.csv`. Its latest filing dates run to 2026-10-01, so the content looks current, but the name mismatch is unexplained.
