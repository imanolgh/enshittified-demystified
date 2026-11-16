# BDC Schedules of Investments: facts from real filings

Ticket: [36 BDC discovery and Schedule of Investments parsing](../issues/36-bdc-discovery-and-soi.md) · Checked 2026-11-15 by a background agent · Builds on [edgar-bdc.md](edgar-bdc.md), which it does not repeat.

Access: 422 SEC requests, 89 MB on the wire, all HTTP 200, with the UA `EvidenceEngine-research/0.1 (ownership-transparency research bot)` (accepted on www, data and efts). Scripts and raw data were kept in the session scratchpad, which is temporary. Everything is observed unless marked [estimate].

Filings parsed (latest 10-Q each, under `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/`):
- Ares Capital (ARCC): `arcc-20260930.htm` (0001628280-26-067383)
- PennantPark Floating Rate (PFLT): `pflt-20260630.htm` (0001193125-26-342352)
- Blackstone Private Credit Fund (BCRED): `bcred-20260930.htm` (0001803498-26-000063)

Main findings that change what edgar-bdc.md implied:
- The hidden identifier string never appears in the visible table as written, and in a few rows it names a different company than the visible row.
- Affiliation status (affiliate, control) is never tagged on individual holdings.
- Joint-venture schedules inside the 10-Q body are tagged as if they were the BDC's own holdings.
- The SEC's monthly BDC data set lags filings by about 5 to 35 days.

## 1. Row structure

### a. Is the borrower name on every tranche row?

- **ARCC: first row only.** For ACP Avenu Midco LLC:
  - r3 `ACP Avenu Midco LLC (13) | Provider of technology solutions… | First lien senior secured revolving loan | 8.98% | SOFR (Q) | 5.25% | 04/2025 | 10/2029 | $0.9 | $0.8 | $0.9`
  - r4 `[blank] | [blank] | First lien senior secured loan | … | 13.1 | 12.9 | 13.1`
  - r5 the same, with 3.6 / 3.5 / 3.6
  - r6 the issuer subtotal `17.2 | 17.6`
  - 1,642 of 3,813 holding rows have a blank name cell.
  - The blank carries across page breaks. Extrahop Networks' continuation sits in a new `<table>`: a header row, then `First lien senior secured loan 10.41% … 3.8`, with no name.
- **BCRED: the name is on every row** (0 blank of 4,851). Example: `West Star Aviation Acquisition, LLC (4)(10) SOFR + 4.50% … 152,878`, then the same name with 6,479, then with 24,613.
- **PFLT: the name is on every row, plus a tranche suffix.** `Wash & Wax Systems, LLC | 4/30/2025 | 4/28/2028 | Consumer Services | 9.16 % | 3M SOFR+ 550 | 6,703 | 6,790 | 6,839`, then `Wash & Wax Systems, LLC - Funded Revolver … 565`, `… - Unfunded Revolver (6) (8) … 282`, `… - Subordinate Debt … 4,741`. Only 20 of 1,398 rows are blank, and those are PIK sub-lines.

### b. Facts in the same row, scale and decimals

In all three filings, principal, cost and fair value sit in the instrument's own `<tr>`. Each row carries exactly one identifier (ARCC 3,812 of 3,813, BCRED 4,850 of 4,851, PFLT 1,398 of 1,398), so one row is one holding.

| BDC | scale | decimals | Table header says |
|---|---|---|---|
| ARCC | 6 | -5 | "(dollar amounts in millions)" |
| BCRED | 3 | -3 | "(in thousands)" |
| PFLT | 3 | -3 | "(in thousands, except per share data)" |

Interest rates use scale -2. PFLT's spread "550" uses scale -4.

### c. Does the typed identifier appear in the visible text?

It exists only in the hidden `ix:header` contexts.

| BDC | Example identifier | In visible text? | Distinct identifiers found verbatim | Borrower part (before " \| ") found verbatim |
|---|---|---|---|---|
| ARCC | `ACP Avenu Midco LLC \| First lien senior secured loan 1` | No | 499 of 2,404 (bare-name ones only) | 698 of 746 |
| BCRED | `Loar Group, Inc. 3 \| Non-Affiliated Issuer` | No | 9 of 3,095 | 1,252 of 1,288 |
| PFLT | `Inv in NCNA Prtfl Comp FLSD Wash & Wax Systems, LLC - Funded Revolver Acquisition 4/30/2025 Maturity 4/28/2028 Industry Consumer Services Current Coupon 9.23% Basis Point Spread Above Index 3M SOFR+ 550` | No | 0 of 1,288 | not checked |

Filers add numeric suffixes (" 1", " 2") to keep identifiers unique.

The identifier and the visible row sometimes disagree:
- Punctuation: `TEI Intermediate, LLC` visible, `TEI Intermediate LLC 1 | …` in the identifier.
- A different entity entirely:
  - PFLT: visible `Puget Collision Holdings, LLC - Common Equity - Class A`, identifier `…HV Watterson Holdings, LLC - Common Equity…`
  - PFLT joint-venture table: visible `MDI Buyer, Inc.`, identifier `…Issuer Name MBS Holdings, Inc.…`
  - BCRED: visible `Froneri US, Inc.`, identifier `Dreyers Grand Ice Cream, Inc. | Verdelite JV LP`
  - BCRED: visible `Forgent Power, LLC`, identifier `Forgent Intermediate IV, LLC`
- Visible name found inside the identifier: ARCC 3,688 of 3,813 (most misses are page-break carry-overs), BCRED 4,839 of 4,851, PFLT 1,380 of 1,398.
- Four PFLT identifiers begin with a typesetting vendor employee's email address.

### d. Issuer name and section headings

- No `InvestmentIssuerNameExtensibleEnumeration` fact in any of the three.
  - ARCC puts `InvestmentIssuerNameAxis` extension members on its per-issuer subtotal rows, e.g. `arcc:ACPAvenuMidcoLLCMember` on 17.2 / 17.6 (452 members).
  - BCRED uses that axis only in affiliate roll-forward tables; PFLT not at all.
  - Some PFLT identifiers contain the literal text "Issuer Name".
- **Affiliation status is never a dimension on holding facts.** Holding contexts carry only `InvestmentIdentifierAxis`; `IssuerAffiliationAxis` appears only on subtotals and statement lines.
  - ARCC: headings are by industry ("Software and Services"). Status is shown by footnotes (4) "Affiliated Person" and (5) "Control", plus separate affiliate transaction tables.
  - BCRED: visible heading rows such as `First Lien Debt - non-controlled/non-affiliated`, `First Lien Debt - controlled/affiliated`, `Investments in Joint Ventures`. The identifier also ends in `| Non-Affiliated Issuer` (2,406), `| Controlled Affiliated Issuer` (44) or `| Non-Controlled Affiliated Issuer` (23).
  - PFLT: headings such as `Investments in Non-Controlled, Non-Affiliated Portfolio Companies - 208.4%` and `Investments in Controlled, Affiliated Portfolio Companies - 37.7% of Net Assets`. Identifiers carry a matching prefix (`Inv in NCNA Prtfl Comp…`).
- **Joint-venture schedules in the 10-Q body are also tagged.**
  - BCRED: Emerald JV LP (839 identifiers) and Verdelite JV LP (603) are told apart only by the identifier suffix.
  - PFLT: its joint-venture schedule in the notes uses the plain identifier axis with no legal-entity dimension. Its holdings look like PFLT's own except for the text pattern.

## 2. Where a BDC names its adviser

- ARCC 10-K FY2025, Part I Item 1 Business ("General"): "We are externally managed by Ares Capital Management LLC ("Ares Capital Management" or our "investment adviser"), a subsidiary of Ares Management Corporation…"
- BCRED 10-K FY2025, Item 1 Business: "We are externally managed by Blackstone Private Credit Strategies LLC (the "Adviser") and Blackstone Credit BDC Advisors LLC (the "Sub-Adviser"…). The Advisers are affiliates of Blackstone…"
- PFLT 10-K FY2025 has no "managed by X" sentence.
  - Item 1 says only "a closed-end, externally managed, non-diversified investment company".
  - The name is in the defined-terms paragraph that opens Part I: ""PennantPark Investment Advisers" or "Investment Adviser" refer to PennantPark Investment Advisers, LLC".
  - It also appears in the Item 1 subsection "Our Investment Adviser and Administrator" and in the Exhibit 10.3 title.
- No structured field names the adviser. The ARCC, BCRED, PFLT and MAIN 10-Ks carry only the standard dei cover tags; their cef tags cover fees, risk and senior securities. Neither `cef-2025.xsd` (135 elements) nor `dei-2025.xsd` (209) has an adviser-name element. The closest is `cef:ManagementFeesPercent`.
- Some BDCs are internally managed:
  - Main Street's 10-K: "MSCC was formed in March 2007 to operate as an internally managed business development company… Because MSCC is internally managed, all of the executive officers and other employees are employed by MSCC." (Its subsidiary MSC Adviser I, LLC advises third parties.)
  - Full-text search over 10-Ks from Nov 2025 to Nov 2026 (matching sentences not read): "internally managed, closed-end" matched Capital Southwest, Trinity Capital and Rand Capital; "is an internally managed" matched Hercules and Capital Southwest.
  - The share of the universe that is internally managed was not checked.

## 3. How fresh the SEC BDC data sets are

- The page (https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets) says "The data sets will be updated monthly", coverage "October 2022 - October 2026", "Last Reviewed or Updated: Oct. 31, 2026". Monthly files for 2026, quarterly files for 2025 and earlier.
- Newest file `2026_10_bdc.zip`: `Last-Modified: Wed, 04 Nov 2026 15:12:38 GMT`, files inside stamped 2026-11-02. Its `sub.tsv` has 4 filings, filed 2026-10-06, 10-27 (ARCC), 10-29 and 10-30.
- Each file holds one calendar month of filings and is posted about 2 to 5 days after the month ends, so a filing reaches the data set 5 to 35 days after it is filed. BCRED's 10-Q (filed 2026-11-12) will appear only in the November file.
- `Last-Modified` on older files reflects refreshes, not first posting (the `2026_08` file, 174 filings, shows 20 Oct; the others show 8 Oct).

## 4. Size and count

Universe: 178 CIKs (union of the `2026_08` and `2026_10` `sub.tsv` files). Counts from the submissions JSON; sizes from each filing's `index.json` (the submissions JSON `size` field is the whole submission, e.g. ARCC 70.4 MB).

| BDC | Latest primary doc (MB) | Inline XBRL 10-K + 10-Q since 2022 (+ amendments) |
|---|---|---|
| Stepstone Private Credit | 63.2 | 14 |
| Antares Strategic Credit | 45.1 | 11 |
| BCRED | 32.9 | 18 |
| PFLT | 28.2 | 16 (+1) |
| ARCC | 24.8 | 17 (+4) |
| Golub BDC | 24.6 | 17 |
| Blue Owl Credit Income | 14.2 | 15 |
| Main Street | 13.7 | 18 |
| OFS | 11.5 | 18 |
| Blue Owl Capital Corp | 11.0 | 17 (+1) |
| Hercules | 8.1 | 17 |
| Saratoga | 7.2 | 17 |
| Rand | 6.7 | 15 (+1) |
| Stone Point Credit Income–Select | 0.4 | 4 |

- 2,378 Inline XBRL 10-K/10-Q filings since 2022, plus 57 amendments.
- Latest primary document per BDC: 2.17 GB uncompressed in total (median 9.6 MB).
- Every primary document since 2022: about 24 to 31 GB uncompressed [estimate].
- The SEC serves them gzip-compressed at 16 to 26 times smaller (ARCC 24.8 MB → 0.97 MB), so about 90 to 140 MB to download the latest set and about 1 to 2 GB for the full history [estimate].
- Multiply by about 1.05 to scale from 178 to 187 BDCs.

## 5. Joint-venture and senior loan fund exhibits

All 178 BDCs' latest filings were checked: 49 have non-certification exhibits; 20 of those index pages were read and every EX-99 listed was opened. 8 filings, covering 5 vehicles, carry a joint venture's or senior loan fund's own schedule of investments, all untagged (0 `ix:` tags):
1. ARCC EX-99.1: Senior Direct Lending Program, LLC
2. Ares Strategic Income Fund EX-99.1: ADLP LLC
3. Blue Owl Credit SLF LLC "Supplemental Financial Information", including its schedule; the same file is attached by OBDC, Blue Owl Capital Corp II, OTF, OCIC and OTIC
4. OCIC SLF LLC (OCIC only)
5. TCW Direct Lending Strategic Ventures LLC (TCW Direct Lending LLC, 1.5 MB)

The other EX-99s are not schedules: Blue Owl Leasing LLC financial information; Section 13(r) disclosures (BlackRock TCP, BlackRock Direct Lending, BlackRock Private Credit Fund, HPS Corporate Lending, HPS Corporate Capital Solutions); Gladstone Capital's FINRA valuation of its preferred stock; a TPVG adviser letter; a PennantPark privacy policy; Partners Group certifications filed as EX-99.6. Rule 3-09 exhibits (10-Ks only) were not surveyed.

## 6. Consumer brands in the `2026_08` `soi.tsv`

The file has 186,668 rows (143,266 with an identifier) from 169 CIKs; the Issuer Name enumeration is filled on only 3,794 rows.

- **Express Wash** (187 rows, 25 BDCs), three different borrowers: `Express Wash Acquisition Company, LLC (Whistle)` (BlackRock TCP, BlackRock Private Credit Fund); `Express Wash Concepts, LLC 1 | Emerald JV LP` or `| Non-Affiliated Issuer` (BCRED, HPS); `Texas Express Wash, LLC` (WhiteHorse).
- **Mister Car Wash**: `Mister Car Wash Holdings, Inc.` (the listed parent), held by BCRED (`| Emerald JV LP`, `| Verdelite JV LP`), Golub Capital Private Credit Fund (`| Senior secured`), Ares Strategic Income Fund (`…, First lien senior secured loan`).
- **Mammoth** (42 rows, 6 BDCs): `Mammoth Holdings, LLC 1/2/3` (OHA, T. Rowe OHA); `Mammoth Holdings, LLC (Delayed Draw)` (First Eagle); `Mammoth Holdings, LLC | CHS BDC 2 LLC 1` (APS BDC); `MAMMOTH BORROWCO, INC.` (Capital Southwest; not confirmed to be the car wash).
- **PetVet** (147 rows, 24 BDCs): `PetVet Care Centers, LLC | First lien` (five Blue Owl BDCs, New Mountain Finance); `PetVet Care Centers LLC | One stop 1` (Golub); `Petvet Care Centers, LLC - Term Loan` (John Hancock Comvest); `PetVet Care Centers - Revolving Credit Facility` (MSD).
- **Southern Veterinary** (49 rows, 14 BDCs): `Southern Veterinary Partners, LLC | Emerald JV LP` (BCRED), `| Senior secured` (Golub). `SVP MVP Holdings, L.P.` (Diameter) may be related; not confirmed.
- **Heartland Dental** (17 rows, 6 BDCs): `Heartland Dental, LLC | Non-Affiliated Issuer` (BCRED), `Funded Investments - First lien | Heartland Dental, LLC` (New Mountain), `…Heartland Dental LLC - Term Loan` (Muzinich).
- **Smile Doctors** (36 rows, 7 BDCs): `Smile Doctors, LLC 1 | Non-Affiliated Issuer` (BCRED), `Smile Doctors LLC | First Lien 1` (New Mountain), and Crescent's common stock.
- **Dental365** (41 rows, 5 BDCs): `Dental365 LLC | Health Care Equipment & Services 1` (FS KKR and two KKR FS Income Trusts); `Premier Care Dental Management, LLC (dba Dental365)` (5C Lending); `…| Dental365` (Adams Street).
- **Aspen Dental** (12 rows, 4 BDCs): `Aspen Dental Management Inc. 1 | Non-Affiliated Issuer` (HPS), `Funded Investments - First lien | ADMI Corp. (aka Aspen Dental)` (New Mountain), `Admi Corp.` (Crescent, Franklin BSP).
- **MB2 Dental** (111 rows, 16 BDCs): `MB2 Dental Solutions LLC 1`, `MB2 Dental Solutions, LLC, First Lien Revolving`, and Audax's `Investment MB2 Dental …`.
- **Smile Brands** (38 rows, 6 BDCs): `Smile Brands, Inc. | Health Care Providers & Services 1` (AB, Franklin BSP), PFLT's `Inv in NCNA … Smile Brands, Inc. - Funded Revolver`, and `OneSmile, LLC (Smile Brands) | Preferred Units` (Nuveen Churchill).
- **Mendocino Farms**: Golub Capital BDC only, `Mendocino Farms, LLC | One stop 1 | Non-Affiliated Issuer` through `One stop 12`, plus `| Common stock`.
- **Medical Solutions**: `Medical Solutions Holdings, Inc. | … | Second Lien Term Loan` (Prospect), `Medical Solutions Parent Holdings, Inc. | Third Out Term Loan` (Barings), `Medical Solutions, LLC` (North Haven). `ARKSTONE MEDICAL SOLUTIONS` is a different company.
- **Pet Supplies Plus**: only `PSP Intermediate 4, LLC` (three Barings BDCs); the link to the brand is not confirmed.
- **No hits**: El Car Wash, Lap of Love, Zips, Orangetheory, Jersey Mike's, Planet Fitness.
- Other car washes that showed up: Go Car Wash Parent, Corp.; Quick Quack Car Wash Holdings, LLC; Club Car Wash Operating, LLC.

How the borrower name relates to the brand:
- Same name plus an entity suffix (PetVet, Heartland, Smile Doctors, MB2, Mendocino).
- A holding company or acquisition vehicle (`Express Wash Acquisition Company`, `Mammoth Holdings`, `Medical Solutions Parent Holdings`).
- A differently named parent with the brand as an aka, dba or parenthetical (`ADMI Corp. (aka Aspen Dental)`, `Premier Care Dental Management (dba Dental365)`, `OneSmile, LLC (Smile Brands)`).
- Spelling and punctuation vary between BDCs for the same borrower.

## 7. When BDCs started Inline XBRL

- Blue Owl Credit Income Corp (CIK 1812554) complied in 2023: its FY2022 10-K (`a01orcic-20221231x10k.htm`, filed 2023-03-10) has no XBRL at all; its first Inline XBRL filing is the Q1-2023 10-Q `orcic-20230331.htm` (0001812554-23-000014, filed 2023-05-11).
- For contrast: Morgan Stanley Direct Lending Fund's first is its FY2022 10-K (filed 2023-03-09); Goldman Sachs BDC (August 2022 group) starts with its Q3-2022 10-Q (filed 2022-11-03), plus one stray Inline XBRL 10-Q from 2017-08.
- Before a BDC's compliance date its 10-K/10-Qs have no XBRL at all.
- Month of each BDC's first Inline XBRL filing (178 BDCs): 2022-08: 19; 2022-10/11: 28; 2023-02/03: 40; 2023-05: 17; the rest were formed later. 44 BDCs filed an untagged 10-Q for Q3 2022 or later before switching in 2023.

## 8. What skipping joint-venture schedules would miss (measured 2026-11-16)

Measured on the SEC's `2026_08_bdc.zip` data set (`soi.tsv`: 174 filings, mostly Q2 2026 10-Qs), re-downloaded with the same UA.

- Three venture schedules in that file are tagged inside a BDC's 10-Q with a venture suffix on the identifier: Blackstone Private Credit Fund's Emerald JV LP (799 rows) and Verdelite JV LP (597 rows), and TPG Twin Brook Capital Income Fund's TCAP JV (181 rows). Every other venture match in the file is the BDC's own stake in a venture (one equity row, e.g. `BCRED Emerald JV LP - LP Interest`, `Blue Owl Credit SLF LLC | LLC Interest`), not the venture's loans. PennantPark's venture rows carry no suffix and were not counted.
- Borrowers in those schedules, after rough name matching (part before " | ", trailing numbers, parentheticals and common suffixes such as LLC, Inc., Holdings and Acquisition removed): Emerald JV 407, Verdelite JV 317, TCAP JV 181; 670 distinct together.
- Of those 670, **97 (about 14%) appear in no BDC's own Schedule** that month: Emerald JV 65 (16%), Verdelite JV 68 (21%), TCAP JV 0. Examples: American Greetings, CWGS Group (Camping World's borrowing entity), Marriott Ownership Resorts, NRG Energy, International SOS, OpenLane. The other 573 also borrow directly from at least one BDC (sometimes Blackstone Private Credit Fund itself).
- For scale: the BDCs' own Schedules name roughly 37,600 distinct borrower strings that month (inflated by spelling variants), so the venture-only borrowers are well under 1% of all borrowers.
- The rough matching can both merge different companies and miss variants (`Canadian Hospital Specialties 1 | Emerald JV` slipped through), so treat 97 as approximate.
- The five untagged EX-99 venture schedules (section 5) were not measured; a tagged-only reader misses them either way.
