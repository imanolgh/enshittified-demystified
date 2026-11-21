# Form ADV fund-type mix: asset managers vs PE firms

Date: 2026-11-20. Facts only, no recommendation. Every number below comes from the two SEC monthly files named here, computed by script. Ownership of affiliates that trade under other names, and the exclusion of name collisions, come from general knowledge and are flagged where used.

## Source files

- Page: [SEC, Information About Registered Investment Advisers and Exempt Reporting Advisers](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers). It lists "Registered Investment Advisers, November 2026" and "Exempt Investment Advisers, November 2026" as the newest files.
- Registered: [`ia110226-registered.zip`](https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia110226-registered.zip) (5,351,876 bytes). It holds `IA_SEC_-_FIRM_ROSTER_FOIA_DOWNLOAD_-_34688412.CSV`, dated 2026-11-02 inside the zip: 448 columns, 17,263 advisers, Latin-1 encoded.
- Exempt reporting advisers (ERAs): [`ia11022026-exempt.zip`](https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia11022026-exempt.zip) (876,412 bytes). It holds `IA_SEC_-_FIRM_ROSTER_FOIA_DOWNLOAD_-_34688411.CSV`, dated 2026-11-02: 171 columns, 6,848 advisers.
- Item meanings were checked against [Form ADV Part 1A](https://www.sec.gov/files/formadv-part1a_1.pdf) (Item 5.D, Item 5.F, Item 7.B and Schedule D 7.B).
- robots.txt was read first; `/files/` and `/data-research/` are not disallowed. Requests used the agreed bot user agent, one at a time, at least 1 s apart.

## Columns the monthly file has

Fund-type columns, the same names in both files:
`7B`, `Count of Private Funds - 7B(1)`, `Any PFs a Master`, `Any Hedge Funds`, `Total number of Hedge funds`, `Any Liquidity Funds`, `Total number of Liquidity funds`, `Any PE Funds`, `Total number of PE funds`, `Any Real Estate Funds`, `Total number of Real Estate funds`, `Any Securitized Funds`, `Total number of Securitized funds`, `Any VC Funds`, `Total number of VC funds`, `Any Other Funds`, `Total number of Other funds`, `Total Gross Assets of Private Funds`, `Count of Private Funds - 7B(2)`.

- There are seven type counts, and in every one of the 24,111 rows they add up exactly to `Count of Private Funds - 7B(1)`. A blank count means zero.
- `Total Gross Assets of Private Funds` is one total per adviser. Assets by fund type are not in the file, so every share below is by **fund count**.
- 7B(1) against 7B(2): Part 1A says a private fund another SEC adviser already reports in its own Schedule D 7.B.(1) goes in 7.B.(2) instead, for example when you are a subadviser. So related registrations should not count the same fund twice in 7B(1). The 7B(2) counts are in the registration table.

Client-type columns (Item 5.D), **registered file only**:
- `5D(a)(1)` … `5D(n)(3)`. (1) is the number of clients, (2) the "fewer than 5 clients" box, (3) the regulatory AUM. Rows (d), (e) and (f) have no (2) column: `5D(d)(1)`, `5D(d)(3)`, `5D(e)(1)`, `5D(e)(3)`, `5D(f)(1)`, `5D(f)(3)`.
- Per Part 1A: (d) is "Investment companies", (e) "Business development companies", (f) "Pooled investment vehicles (other than investment companies and business development companies)".
- The form says to answer (d) only if you advise an investment company registered under the Investment Company Act of 1940. It also says the 5.D.(3) amounts should add up to 5.F.(2)(c).
- Total regulatory AUM is `5F(2)(c)`. In the file, the 5D(x)(3) amounts are within 1% of `5F(2)(c)` for all but 2 of 17,263 rows, and neither of those 2 is in this study.
- `5D(1)(a)`–`5D(1)(m)` and `5D(2)(a)`–`5D(2)(m)` (the older form's percentage fields) have a value in 1 row only.
- Also present: `5.G.(3) - Total number of RICs or BDCs` and `5.G.(3) - Total amount of Parallel Assets`. They were not used.

**The ERA file has no Item 5 columns**, so it has no client types and no regulatory AUM. ERA rows add fund counts only.

## How registrations were assigned

- **Core**: the firm's brand appears in the primary or legal business name. Name collisions with unrelated firms were dropped (listed below). FIAM (Fidelity) and SSGA (State Street) count as brand abbreviations.
- For J.P. Morgan and Goldman Sachs, **core is the asset-management entities only**. The brokerage and wealth entities with the same brand are a separate set, "brand, not AM".
- **Affiliate**: a known subsidiary with a different name, for example HPS (BlackRock), Oaktree (Brookfield) or AlpInvest (Carlyle). Ownership comes from general knowledge, not from the file. These are left out of core and tested separately.
- **Unsure**: a brand-named row that may be a joint venture or an unrelated firm. Left out of core and tested in "all".
- The shares are firm-level sums over these registrations: PE share = sum of PE funds ÷ sum of 7B(1) funds. IC share = sum of `5D(d)(3)` ÷ sum of `5F(2)(c)`, over registered rows. "(IC+BDC)" adds `5D(e)(3)` to the top of the fraction.
- RAUM can be counted twice across affiliated registrations through subadvice. For example, The Vanguard Group, Inc. reports $11,092.7bn and Vanguard Capital Management, LLC $8,436.2bn, both 100% investment companies. So the RAUM totals overstate firm AUM. The shares are ratios over the same rows.

## Per-firm results (core registrations)

| Firm | Regs | Any PE Funds | Private funds 7B(1) | PE | Hedge | Real estate | VC | Securitized | Liquidity | Other | PE share | Largest type | PE strictly largest | IC clients 5D(d)(1) | IC RAUM 5D(d)(3) $bn | Total RAUM 5F(2)(c) $bn | IC share of RAUM | (IC+BDC) share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BlackRock | 13 | Y | 697 | 294 | 246 | 18 | 0 | 71 | 10 | 58 | 42.2% | PE | yes | 913 | 5,630.2 | 8,152.6 | 69.1% | 69.1% |
| Vanguard | 7 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0% | - | no | 457 | 22,185.3 | 22,791.0 | 97.3% | 97.3% |
| State Street | 1 | Y | 21 | 1 | 17 | 0 | 0 | 0 | 3 | 0 | 4.8% | Hedge | no | 264 | 1,368.2 | 1,420.7 | 96.3% | 96.3% |
| Fidelity (FMR) | 7 | Y | 38 | 6 | 7 | 4 | 0 | 4 | 0 | 17 | 15.8% | Other | no | 787 | 5,699.4 | 6,121.8 | 93.1% | 93.2% |
| T. Rowe Price | 9 | Y | 7 | 3 | 0 | 0 | 1 | 0 | 0 | 3 | 42.9% | PE and Other tied | no | 468 | 1,504.9 | 2,775.7 | 54.2% | 54.2% |
| J.P. Morgan AM | 8 | Y | 348 | 85 | 46 | 44 | 0 | 0 | 1 | 172 | 24.4% | Other | no | 386 | 1,954.2 | 4,752.3 | 41.1% | 41.1% |
| Goldman Sachs AM | 5 | Y | 1,317 | 239 | 72 | 52 | 0 | 9 | 6 | 939 | 18.1% | Other | no | 205 | 778.3 | 3,376.7 | 23.0% | 23.9% |
| Invesco | 11 | Y | 111 | 20 | 18 | 4 | 0 | 43 | 5 | 21 | 18.0% | Securitized | no | 1,581 | 1,295.8 | 2,112.7 | 61.3% | 61.3% |
| Capital Group | 5 | Y | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 66.7% | PE | yes | 158 | 3,950.5 | 4,690.4 | 84.2% | 84.2% |
| Franklin Templeton | 15 | Y | 89 | 52 | 17 | 7 | 0 | 6 | 2 | 5 | 58.4% | PE | yes | 485 | 589.7 | 1,015.1 | 58.1% | 58.5% |
| Wellington | 5 | Y | 218 | 48 | 107 | 0 | 0 | 5 | 0 | 58 | 22.0% | Hedge | no | 209 | 636.4 | 1,557.5 | 40.9% | 40.9% |
| Northern Trust | 3 | N | 9 | 0 | 1 | 0 | 0 | 0 | 0 | 8 | 0.0% | Other | no | 109 | 295.9 | 1,455.3 | 20.3% | 20.3% |
| Blackstone | 30 | Y | 896 | 350 | 156 | 135 | 0 | 176 | 0 | 79 | 39.1% | PE | yes | 12 | 16.0 | 1,352.7 | 1.2% | 8.7% |
| KKR | 5 | Y | 752 | 599 | 83 | 34 | 0 | 18 | 0 | 18 | 79.7% | PE | yes | 6 | 3.3 | 677.1 | 0.5% | 0.5% |
| Apollo | 8 | Y | 714 | 214 | 151 | 108 | 0 | 19 | 0 | 222 | 30.0% | Other | no | 8 | 17.8 | 762.4 | 2.3% | 6.6% |
| Carlyle | 4 | Y | 404 | 251 | 2 | 38 | 0 | 112 | 0 | 1 | 62.1% | PE | yes | 2 | 7.1 | 363.7 | 2.0% | 3.5% |
| Ares | 5 | Y | 722 | 158 | 289 | 116 | 5 | 99 | 0 | 55 | 21.9% | Hedge | no | 12 | 8.8 | 618.5 | 1.4% | 10.7% |
| TPG | 6 | Y | 423 | 184 | 177 | 34 | 0 | 21 | 0 | 7 | 43.5% | PE | yes | 0 | 0.0 | 463.1 | 0.0% | 0.0% |
| Bain Capital | 12 | Y | 293 | 77 | 100 | 26 | 19 | 70 | 0 | 1 | 26.3% | Hedge | no | 1 | 0.0 | 216.1 | 0.0% | 0.0% |
| Leonard Green | 1 | Y | 107 | 107 | 0 | 0 | 0 | 0 | 0 | 0 | 100.0% | PE | yes | 0 | 0.0 | 85.6 | 0.0% | 0.0% |
| Warburg Pincus | 1 | Y | 213 | 213 | 0 | 0 | 0 | 0 | 0 | 0 | 100.0% | PE | yes | 0 | 0.0 | 108.7 | 0.0% | 0.0% |
| Roark | 1 | Y | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 100.0% | PE | yes | 0 | 0.0 | 34.2 | 0.0% | 0.0% |
| New Mountain | 3 | Y | 29 | 20 | 0 | 1 | 0 | 8 | 0 | 0 | 69.0% | PE | yes | 0 | 0.0 | 61.0 | 0.0% | 15.0% |
| Brookfield | 6 | Y | 497 | 376 | 7 | 109 | 0 | 0 | 1 | 4 | 75.7% | PE | yes | 10 | 7.7 | 497.7 | 1.6% | 1.6% |

"PE strictly largest" means the PE count is above every other type's count. T. Rowe Price's core registrations have PE = Other = 3, so PE is not strictly largest there. If a tie counted as largest, T. Rowe Price would also land on the PE side.

## Threshold results (core)

A line "works" only if all 12 asset managers fall on one side and all 12 PE firms on the other. **None of the lines below works.** The observed ranges after the table show where the two groups overlap and where they do not.

| Line (classed as PE / asset manager) | Asset managers on the PE side | PE firms on the non-PE side |
|---|---|---|
| PE strictly the largest type | BlackRock (294 PE of 697), Capital Group (2 of 3), Franklin Templeton (52 of 89) | Apollo (Other 222 > PE 214), Ares (Hedge 289 > PE 158), Bain Capital (Hedge 100 > PE 77) |
| PE ≥ 50% of private funds | Capital Group 66.7%, Franklin Templeton 58.4% | Blackstone 39.1%, Apollo 30.0%, Ares 21.9%, TPG 43.5%, Bain Capital 26.3% |
| PE ≥ 25% | BlackRock 42.2%, T. Rowe Price 42.9%, Capital Group 66.7%, Franklin Templeton 58.4% | Ares 21.9% |
| PE ≥ 10% | BlackRock, Fidelity 15.8%, T. Rowe Price, J.P. Morgan AM 24.4%, Goldman Sachs AM 18.1%, Invesco 18.0%, Capital Group, Franklin Templeton, Wellington 22.0% (9 of 12) | none |
| Any PE Funds = Y (current rule) | 10 of 12: all except Vanguard and Northern Trust | none |
| IC share of RAUM ≥ 50% → asset manager | Below 50%, so not caught: J.P. Morgan AM 41.1%, Goldman Sachs AM 23.0%, Wellington 40.9%, Northern Trust 20.3% | none (highest: Apollo 2.3%) |
| (IC+BDC) share ≥ 50% → asset manager | Same four as the line above | none (highest: New Mountain 15.0%) |

Observed ranges (facts, not a proposal):
- PE share by count: asset managers 0%–66.7%, PE firms 21.9%–100%. The ranges overlap.
- IC share of RAUM: asset managers 20.3%–97.3%, PE firms 0%–2.3%. They do not overlap in core. Across the variants below, the lowest asset manager is 20.1% (Northern Trust with 50 South) and the highest PE firm is 2.7% (Ares with unsure rows).
- (IC+BDC) share: the highest PE firm is New Mountain at 15.0% in core and 15.0% in every variant.

## Sensitivity: other registration sets

Core plus differently named affiliates (only the firms that change):

| Firm | Regs | Any PE Funds | Private funds 7B(1) | PE | Hedge | Real estate | VC | Securitized | Liquidity | Other | PE share | Largest type | PE strictly largest | IC clients 5D(d)(1) | IC RAUM 5D(d)(3) $bn | Total RAUM 5F(2)(c) $bn | IC share of RAUM | (IC+BDC) share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BlackRock | 16 | Y | 1,087 | 558 | 317 | 18 | 0 | 123 | 10 | 61 | 51.3% | PE | yes | 913 | 5,630.2 | 8,473.6 | 66.4% | 66.5% |
| Fidelity (FMR) | 8 | Y | 38 | 6 | 7 | 4 | 0 | 4 | 0 | 17 | 15.8% | Other | no | 802 | 6,288.9 | 7,491.9 | 83.9% | 84.0% |
| T. Rowe Price | 12 | Y | 101 | 3 | 49 | 0 | 1 | 45 | 0 | 3 | 3.0% | Hedge | no | 469 | 1,505.2 | 2,880.8 | 52.2% | 52.4% |
| J.P. Morgan AM | 9 | Y | 364 | 85 | 62 | 44 | 0 | 0 | 1 | 172 | 23.4% | Other | no | 386 | 1,954.2 | 4,759.8 | 41.1% | 41.1% |
| Franklin Templeton | 32 | Y | 392 | 168 | 106 | 30 | 0 | 55 | 3 | 30 | 42.9% | PE | yes | 707 | 884.4 | 1,859.7 | 47.6% | 47.8% |
| Northern Trust | 4 | Y | 135 | 114 | 13 | 0 | 0 | 0 | 0 | 8 | 84.4% | PE | yes | 110 | 296.2 | 1,471.4 | 20.1% | 20.1% |
| Blackstone | 32 | Y | 947 | 384 | 157 | 144 | 2 | 176 | 0 | 84 | 40.5% | PE | yes | 13 | 16.2 | 1,441.2 | 1.1% | 8.2% |
| KKR | 6 | Y | 752 | 599 | 83 | 34 | 0 | 18 | 0 | 18 | 79.7% | PE | yes | 22 | 6.0 | 679.8 | 0.9% | 0.9% |
| Apollo | 11 | Y | 979 | 214 | 153 | 234 | 0 | 126 | 0 | 252 | 21.9% | Other | no | 8 | 17.8 | 858.2 | 2.1% | 5.9% |
| Carlyle | 7 | Y | 514 | 359 | 2 | 38 | 0 | 114 | 0 | 1 | 69.8% | PE | yes | 4 | 11.6 | 465.7 | 2.5% | 3.7% |
| Brookfield | 8 | Y | 781 | 383 | 228 | 109 | 0 | 41 | 1 | 19 | 49.0% | PE | yes | 20 | 9.3 | 695.1 | 1.3% | 3.1% |

Changes against core:
- **BlackRock** with HPS, GIP and Tennenbaum: PE share 51.3%.
- **Northern Trust** with 50 South Capital: PE 114 of 135 (84.4%), and Any PE Funds becomes Y.
- **T. Rowe Price** with OHA: PE share 3.0%.
- **Franklin Templeton** with its 17 other-named advisers: IC share 47.6%, below 50%.
- **Brookfield** with Oaktree: PE share 49.0%.
- **Apollo** with Bridge and Redding Ridge: PE share 21.9%.
- **Carlyle** with AlpInvest: PE share 69.8%.

Results with affiliates:
- PE strictly largest: wrong side are BlackRock, Capital Group, Franklin Templeton and Northern Trust, against Apollo, Ares and Bain Capital.
- ≥ 50%: BlackRock, Capital Group and Northern Trust, against Blackstone, Apollo, Ares, TPG, Bain Capital and Brookfield.
- ≥ 25%: BlackRock, Capital Group, Franklin Templeton and Northern Trust, against Apollo and Ares.
- ≥ 10%: 9 asset managers (all except Vanguard, State Street and T. Rowe Price), against no PE firms.
- IC ≥ 50%: J.P. Morgan AM, Goldman Sachs AM, Franklin Templeton, Wellington and Northern Trust fall below, against no PE firms.

Core plus the same-brand brokerage and wealth entities (no private funds; only the IC share moves):

| Firm | Regs | Any PE Funds | Private funds 7B(1) | PE | Hedge | Real estate | VC | Securitized | Liquidity | Other | PE share | Largest type | PE strictly largest | IC clients 5D(d)(1) | IC RAUM 5D(d)(3) $bn | Total RAUM 5F(2)(c) $bn | IC share of RAUM | (IC+BDC) share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J.P. Morgan AM | 10 | Y | 348 | 85 | 46 | 44 | 0 | 0 | 1 | 172 | 24.4% | Other | no | 386 | 1,954.2 | 5,182.0 | 37.7% | 37.7% |
| Goldman Sachs AM | 7 | Y | 1,317 | 239 | 72 | 52 | 0 | 9 | 6 | 939 | 18.1% | Other | no | 205 | 778.3 | 3,542.1 | 22.0% | 22.8% |

The threshold results are the same as core.

"All" (core + brand, not AM + affiliates + unsure; only the firms that differ from core+affiliates):

| Firm | Regs | Any PE Funds | Private funds 7B(1) | PE | Hedge | Real estate | VC | Securitized | Liquidity | Other | PE share | Largest type | PE strictly largest | IC clients 5D(d)(1) | IC RAUM 5D(d)(3) $bn | Total RAUM 5F(2)(c) $bn | IC share of RAUM | (IC+BDC) share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| State Street | 3 | Y | 23 | 3 | 17 | 0 | 0 | 0 | 3 | 0 | 13.0% | Hedge | no | 264 | 1,368.2 | 1,420.7 | 96.3% | 96.3% |
| J.P. Morgan AM | 11 | Y | 364 | 85 | 62 | 44 | 0 | 0 | 1 | 172 | 23.4% | Other | no | 386 | 1,954.2 | 5,189.5 | 37.7% | 37.7% |
| Goldman Sachs AM | 7 | Y | 1,317 | 239 | 72 | 52 | 0 | 9 | 6 | 939 | 18.1% | Other | no | 205 | 778.3 | 3,542.1 | 22.0% | 22.8% |
| Capital Group | 6 | Y | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 66.7% | PE | yes | 158 | 3,950.5 | 4,690.6 | 84.2% | 84.2% |
| Franklin Templeton | 33 | Y | 392 | 168 | 106 | 30 | 0 | 55 | 3 | 30 | 42.9% | PE | yes | 707 | 884.4 | 1,860.2 | 47.5% | 47.8% |
| KKR | 7 | Y | 752 | 599 | 83 | 34 | 0 | 18 | 0 | 18 | 79.7% | PE | yes | 22 | 6.0 | 695.9 | 0.9% | 3.2% |
| Apollo | 12 | Y | 979 | 214 | 153 | 234 | 0 | 126 | 0 | 252 | 21.9% | Other | no | 8 | 17.8 | 858.3 | 2.1% | 5.9% |
| Ares | 7 | Y | 722 | 158 | 289 | 116 | 5 | 99 | 0 | 55 | 21.9% | Hedge | no | 13 | 16.8 | 626.7 | 2.7% | 11.8% |
| TPG | 7 | Y | 423 | 184 | 177 | 34 | 0 | 21 | 0 | 7 | 43.5% | PE | yes | 0 | 0.0 | 465.3 | 0.0% | 0.0% |

In this set, State Street's two unsure ERA rows raise it to 3 PE of 23 (13.0%), which puts it over the 10% line. Every other result is the same as with affiliates.

## Per-registration data

Amounts are in $bn, rounded from the file's dollar values. ERA rows have no Item 5 data.

| Firm | Set | CRD | File | Primary business name (legal name if different) | Latest ADV filing | Any PE | 7B(1) | PE | Hedge | RE | VC | Sec | Liq | Other | 7B(2) | IC RAUM $bn | BDC RAUM $bn | RAUM $bn | Umbrella (relying) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BlackRock | core | 105247 | REG | BLACKROCK FUND ADVISORS | 10/02/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4,277.6 | 0.0 | 4,282.2 | N |
| BlackRock | core | 106614 | REG | BLACKROCK ADVISORS, LLC | 05/15/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1,070.5 | 0.0 | 1,096.1 | N |
| BlackRock | core | 106843 | REG | BLACKROCK INTERNATIONAL LIMITED | 05/15/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 21.6 | 0.0 | 30.8 | N |
| BlackRock | core | 107105 | REG | BLACKROCK FINANCIAL MANAGEMENT, INC | 08/27/2026 | Y | 352 | 73 | 180 | 3 | 0 | 49 | 2 | 45 | 30 | 17.4 | 0.0 | 1,595.1 | Y (1) |
| BlackRock | core | 108069 | REG | BLACKROCK CAPITAL MANAGEMENT, INC. | 07/09/2026 | N | 8 | 0 | 6 | 0 | 0 | 0 | 2 | 0 | 0 | 0.0 | 0.0 | 172.6 | N |
| BlackRock | core | 108928 | REG | BLACKROCK INVESTMENT MANAGEMENT, LLC | 07/24/2026 | Y | 49 | 43 | 3 | 0 | 0 | 1 | 0 | 2 | 2 | 238.5 | 0.0 | 676.7 | N |
| BlackRock | core | 109457 | REG | BLACKROCK REALTY ADVISORS INC | 07/24/2026 | N | 3 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0.0 | 0.0 | 1.1 | N |
| BlackRock | core | 161987 | REG | BLACKROCK ASSET MANAGEMENT SCHWEIZ AG | 05/15/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.0 | 0.0 | 2.4 | N |
| BlackRock | core | 164594 | REG | BLACKROCK (SINGAPORE) LIMITED | 06/17/2026 | N | 6 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 5 | 2.3 | 0.0 | 70.3 | N |
| BlackRock | core | 165482 | REG | BLACKROCK ASSET MANAGEMENT NORTH ASIA LIMITED | 09/25/2026 | N | 11 | 0 | 1 | 9 | 0 | 0 | 0 | 1 | 2 | 2.0 | 0.0 | 140.3 | N |
| BlackRock | core | 288041 | REG | BLACKROCK ALTERNATIVES MANAGEMENT, LLC | 07/24/2026 | Y | 82 | 53 | 24 | 0 | 0 | 0 | 0 | 5 | 0 | 0.0 | 0.0 | 18.0 | Y (2) |
| BlackRock | core | 290336 | REG | BLACKROCK CAPITAL INVESTMENT ADVISORS, LLC | 08/12/2026 | Y | 162 | 125 | 12 | 0 | 0 | 21 | 0 | 4 | 3 | 0.3 | 2.8 | 66.9 | N |
| BlackRock | core | 162379 | ERA | BLACKROCK INVESTMENT MANAGEMENT (UK) LIMITED | 08/03/2026 | N | 24 | 0 | 12 | 5 | 0 | 0 | 6 | 1 | 15 |  |  |  |  |
| BlackRock | affiliate | 282125 | REG | HPS INVESTMENT PARTNERS, LLC | 05/20/2026 | Y | 253 | 142 | 58 | 0 | 0 | 50 | 0 | 3 | 0 | 0.0 | 0.0 | 175.7 | Y (21) |
| BlackRock | affiliate | 157434 | REG | GLOBAL INFRASTRUCTURE MANAGEMENT, LLC | 10/05/2026 | Y | 101 | 93 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 142.2 | Y (2) |
| BlackRock | affiliate | 113203 | REG | TENNENBAUM CAPITAL PARTNERS, LLC | 06/17/2026 | Y | 36 | 29 | 5 | 0 | 0 | 2 | 0 | 0 | 0 | 0.0 | 1.5 | 3.2 | N |
| Vanguard | core | 106715 | REG | VANGUARD ADVISERS, INC. | 10/22/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 344.6 | N |
| Vanguard | core | 285366 | REG | VANGUARD PERSONALIZED INDEXING MANAGEMENT | 10/23/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 11.4 | N |
| Vanguard | core | 105958 | REG | VANGUARD GROUP INC (THE VANGUARD GROUP, INC.) | 10/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11,092.7 | 0.0 | 11,092.7 | N |
| Vanguard | core | 341357 | REG | VANGUARD ALTERNATIVE ASSETS ADVISER, LLC | 09/18/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| Vanguard | core | 338003 | REG | VANGUARD PORTFOLIO MANAGEMENT, LLC | 09/21/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2,656.5 | 0.0 | 2,656.5 | N |
| Vanguard | core | 164593 | REG | VANGUARD GLOBAL ADVISERS, LLC | 09/18/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 249.7 | N |
| Vanguard | core | 338002 | REG | VANGUARD CAPITAL MANAGEMENT, LLC | 09/21/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8,436.2 | 0.0 | 8,436.2 | N |
| State Street | core | 111242 | REG | SSGA FUNDS MANAGEMENT, INC. | 08/28/2026 | Y | 21 | 1 | 17 | 0 | 0 | 0 | 3 | 0 | 0 | 1,368.2 | 0.0 | 1,420.7 | N |
| State Street | unsure | 340778 | ERA | STATE STREET DIGITAL LTD (FINORYAQ CAPITAL) | 02/23/2026 | Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |
| State Street | unsure | 340663 | ERA | SPIRIT EYE INVESTMENT LTD (STATE STREET DIGITAL LTD) | 02/03/2026 | Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |
| Fidelity (FMR) | core | 108281 | REG | FIDELITY MANAGEMENT & RESEARCH COMPANY LLC | 07/30/2026 | Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 5,416.1 | 0.0 | 5,685.0 | N |
| Fidelity (FMR) | core | 133196 | REG | FIAM LLC | 07/30/2026 | Y | 21 | 2 | 1 | 3 | 0 | 0 | 0 | 15 | 1 | 235.1 | 0.0 | 347.7 | N |
| Fidelity (FMR) | core | 301896 | REG | FIDELITY INSTITUTIONAL WEALTH ADVISER LLC | 03/30/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 9.4 | N |
| Fidelity (FMR) | core | 315088 | REG | FIDELITY DIVERSIFYING SOLUTIONS LLC | 08/20/2026 | Y | 12 | 3 | 6 | 1 | 0 | 0 | 0 | 2 | 1 | 10.0 | 3.1 | 18.9 | N |
| Fidelity (FMR) | core | 148045 | REG | FIDELITY MANAGEMENT & RESEARCH (HONG KONG) LIMITED | 06/29/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25.2 | 0.0 | 32.5 | N |
| Fidelity (FMR) | core | 108273 | REG | FMR INVESTMENT MANAGEMENT (UK) LIMITED | 06/29/2026 | N | 4 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 5 | 10.7 | 0.0 | 25.8 | N |
| Fidelity (FMR) | core | 148239 | REG | FIDELITY MANAGEMENT & RESEARCH (JAPAN) LIMITED | 06/29/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.4 | 0.0 | 2.4 | N |
| Fidelity (FMR) | affiliate | 104555 | REG | STRATEGIC ADVISERS LLC | 03/30/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 589.4 | 0.0 | 1,370.1 | N |
| T. Rowe Price | core | 105496 | REG | T. ROWE PRICE ASSOCIATES, INC. | 07/06/2026 | Y | 7 | 3 | 0 | 0 | 1 | 0 | 0 | 3 | 446 | 1,182.6 | 0.0 | 2,196.5 | N |
| T. Rowe Price | core | 107290 | REG | T. ROWE PRICE (CANADA), INC. (T. ROWE PRICE (CANADA) INC.) | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 6.6 | N |
| T. Rowe Price | core | 108958 | REG | T. ROWE PRICE ADVISORY SERVICES, INC. | 10/02/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 5.9 | N |
| T. Rowe Price | core | 126032 | REG | T. ROWE PRICE INTERNATIONAL LTD | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 130.5 | 0.0 | 277.2 | N |
| T. Rowe Price | core | 155827 | REG | T.ROWE PRICE HONG KONG LIMITED | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15.9 | 0.0 | 42.3 | N |
| T. Rowe Price | core | 155831 | REG | T. ROWE PRICE SINGAPORE PRIVATE LTD | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 | 0.0 | 2.3 | N |
| T. Rowe Price | core | 290585 | REG | T. ROWE PRICE JAPAN, INC. | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.7 | 0.0 | 24.1 | N |
| T. Rowe Price | core | 290594 | REG | T. ROWE PRICE AUSTRALIA LIMITED | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.6 | 0.0 | 16.7 | N |
| T. Rowe Price | core | 314590 | REG | T.ROWE PRICE INVESTMENT MANAGEMENT, INC. | 07/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 172.5 | 0.0 | 204.2 | N |
| T. Rowe Price | affiliate | 125352 | REG | OAK HILL ADVISORS, L.P. | 06/01/2026 | N | 94 | 0 | 49 | 0 | 0 | 45 | 0 | 0 | 0 | 0.0 | 0.0 | 100.7 | Y (2) |
| T. Rowe Price | affiliate | 319664 | REG | OHA PRIVATE CREDIT ADVISORS LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 3.6 | 3.6 | N |
| T. Rowe Price | affiliate | 322289 | REG | OHA PRIVATE CREDIT ADVISORS II, L.P. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 | 0.5 | 0.8 | N |
| J.P. Morgan AM | core | 107038 | REG | J.P. MORGAN INVESTMENT MANAGEMENT INC. | 08/26/2026 | Y | 239 | 27 | 16 | 26 | 0 | 0 | 1 | 169 | 12 | 1,823.2 | 0.0 | 3,519.4 | N |
| J.P. Morgan AM | core | 110186 | REG | J.P. MORGAN PRIVATE INVESTMENTS INC. | 10/08/2026 | Y | 75 | 57 | 10 | 8 | 0 | 0 | 0 | 0 | 1 | 130.7 | 0.0 | 470.0 | N |
| J.P. Morgan AM | core | 111944 | REG | J.P. MORGAN NATURAL CAPITAL (JPMORGAN ASSET MANAGEMENT NATURAL CAPITAL, LLC) | 09/29/2026 | N | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 7.0 | N |
| J.P. Morgan AM | core | 20989 | REG | JPMORGAN ALTERNATIVE ASSET MANAGEMENT (J.P. MORGAN ALTERNATIVE ASSET MANAGEMENT, INC.) | 07/16/2026 | Y | 15 | 1 | 14 | 0 | 0 | 0 | 0 | 0 | 2 | 0.0 | 0.0 | 29.7 | N |
| J.P. Morgan AM | core | 300114 | REG | JPMORGAN ASSET MANAGEMENT (ASIA PACIFIC) LIMITED | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.2 | 0.0 | 169.6 | N |
| J.P. Morgan AM | core | 135960 | REG | JPMORGAN ASSET MANAGEMENT (UK) LIMITED | 04/14/2026 | N | 14 | 0 | 1 | 10 | 0 | 0 | 0 | 3 | 17 | 0.0 | 0.0 | 484.1 | N |
| J.P. Morgan AM | core | 172045 | REG | JPMORGAN FUNDS LIMITED | 05/08/2026 | N | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 6 | 0.0 | 0.0 | 72.4 | N |
| J.P. Morgan AM | core | 304190 | ERA | JPMORGAN ASSET MANAGEMENT (EUROPE) S.A.R.L. (JPMORGAN ASSET MANAGEMENT (EUROPE) S.A R.L.) | 10/06/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 |  |  |  |  |
| J.P. Morgan AM | brand, not AM | 79 | REG | J.P. MORGAN SECURITIES LLC | 10/29/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 429.7 | N |
| J.P. Morgan AM | brand, not AM | 335439 | REG | J.P.MORGAN WEALTH MANAGEMENT SOLUTIONS INC. | 10/08/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| J.P. Morgan AM | affiliate | 134776 | REG | HIGHBRIDGE CAPITAL MANAGEMENT, LLC | 03/31/2026 | N | 16 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 7.6 | N |
| Goldman Sachs AM | core | 107738 | REG | GOLDMAN SACHS ASSET MANAGEMENT, L.P. | 09/25/2026 | Y | 1,286 | 239 | 62 | 52 | 0 | 9 | 0 | 924 | 7 | 777.3 | 29.1 | 2,648.9 | N |
| Goldman Sachs AM | core | 286066 | REG | GOLDMAN SACHS ASSET MANAGEMENT (HONG KONG) LIMITED | 05/22/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 21.2 | N |
| Goldman Sachs AM | core | 107715 | REG | GOLDMAN SACHS ASSET MANAGEMENT INTERNATIONAL | 08/21/2026 | N | 31 | 0 | 10 | 0 | 0 | 0 | 6 | 15 | 66 | 1.0 | 0.0 | 621.0 | N |
| Goldman Sachs AM | core | 286067 | REG | GOLDMAN SACHS ASSET MANAGEMENT (SINGAPORE) PTE. LTD. | 05/22/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0.0 | 0.0 | 13.8 | N |
| Goldman Sachs AM | core | 283221 | REG | GOLDMAN SACHS ASSET MANAGEMENT CO., LTD. | 05/22/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 71.8 | N |
| Goldman Sachs AM | brand, not AM | 361 | REG | GOLDMAN SACHS & CO. LLC | 07/27/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 133.6 | N |
| Goldman Sachs AM | brand, not AM | 106693 | REG | GOLDMAN SACHS WEALTH SERVICES, L.P. | 10/30/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 31.7 | N |
| Invesco | core | 104885 | REG | INVESCO INVESTMENT ADVISERS LLC | 03/24/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4.4 | 0.0 | 4.4 | N |
| Invesco | core | 105360 | REG | INVESCO ADVISERS, INC. | 06/11/2026 | N | 30 | 0 | 12 | 3 | 0 | 0 | 5 | 10 | 2 | 459.3 | 0.0 | 749.5 | N |
| Invesco | core | 107584 | REG | INVESCO PRIVATE CAPITAL, INC. | 03/26/2026 | Y | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.9 | N |
| Invesco | core | 107590 | REG | INVESCO SENIOR SECURED MANAGEMENT, INC. | 03/25/2026 | Y | 27 | 14 | 1 | 0 | 0 | 3 | 0 | 9 | 0 | 14.9 | 0.0 | 29.4 | N |
| Invesco | core | 125601 | REG | INVESCO CAPITAL MANAGEMENT LLC | 08/12/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 804.4 | 0.0 | 941.0 | N |
| Invesco | core | 154461 | REG | INVESCO MANAGED ACCOUNTS, LLC | 06/29/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 31.3 | N |
| Invesco | core | 306746 | REG | INVESCO LOAN MANAGER, LLC | 03/25/2026 | Y | 44 | 2 | 0 | 0 | 0 | 40 | 0 | 2 | 0 | 0.0 | 0.0 | 17.7 | Y (7) |
| Invesco | core | 109923 | REG | INVESCO HONG KONG LIMITED | 09/10/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.5 | 0.0 | 26.2 | N |
| Invesco | core | 109985 | REG | INVESCO ASSET MANAGEMENT LTD. | 03/31/2026 | N | 5 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 1 | 5.2 | 0.0 | 187.6 | N |
| Invesco | core | 143238 | REG | INVESCO MANAGEMENT S.A. | 03/31/2026 | N | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5.1 | 0.0 | 48.7 | N |
| Invesco | core | 107155 | REG | INVESCO ASSET MANAGEMENT (JAPAN) LIMITED | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 76.1 | N |
| Capital Group | core | 110885 | REG | CAPITAL RESEARCH AND MANAGEMENT COMPANY | 09/25/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3,939.6 | 0.0 | 4,320.8 | N |
| Capital Group | core | 110682 | REG | CAPITAL INTERNATIONAL, INC. | 10/07/2026 | Y | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10.9 | 0.0 | 64.3 | N |
| Capital Group | core | 170017 | REG | CAPITAL BANK AND TRUST COMPANY | 10/07/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 257.0 | N |
| Capital Group | core | 312837 | REG | CAPITAL GROUP PRIVATE CLIENT SERVICES, INC. | 09/25/2026 | N | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0.0 | 0.0 | 48.4 | N |
| Capital Group | core | 110684 | REG | CAPITAL RESEARCH COMPANY | 09/25/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| Capital Group | unsure | 295193 | REG | THE CAPITAL GROUP FIDUCIARY ADVISORS, LLC | 03/19/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.2 | N |
| Franklin Templeton | core | 104517 | REG | FRANKLIN ADVISERS, INC. | 09/16/2026 | Y | 73 | 51 | 13 | 0 | 0 | 6 | 2 | 1 | 0 | 368.1 | 0.0 | 509.5 | N |
| Franklin Templeton | core | 111361 | REG | FRANKLIN ADVISORY SERVICES, LLC | 09/16/2026 | N | 6 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 9.2 | 0.0 | 14.1 | N |
| Franklin Templeton | core | 111370 | REG | TEMPLETON INVESTMENT COUNSEL, LLC | 09/16/2026 | N | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2.4 | 0.0 | 4.6 | N |
| Franklin Templeton | core | 140432 | REG | FRANKLIN TEMPLETON FUND ADVISER, LLC | 09/03/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 143.5 | 0.0 | 167.4 | N |
| Franklin Templeton | core | 142219 | REG | FRANKLIN TEMPLETON PRIVATE PORTFOLIO GROUP, LLC | 08/28/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 139.9 | N |
| Franklin Templeton | core | 339083 | REG | FRANKLIN TEMPLETON PRIVATE MARKETS ADVISER, LLC | 01/07/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| Franklin Templeton | core | 111364 | REG | FRANKLIN TEMPLETON INVESTMENTS CORP. | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.9 | 0.0 | 12.8 | N |
| Franklin Templeton | core | 111383 | REG | TEMPLETON GLOBAL ADVISORS LIMITED | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15.1 | 0.0 | 25.8 | N |
| Franklin Templeton | core | 117384 | REG | FRANKLIN TEMPLETON INSTITUTIONAL, LLC | 09/16/2026 | N | 7 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 11.5 | 0.0 | 29.6 | N |
| Franklin Templeton | core | 111376 | REG | FRANKLIN MUTUAL ADVISERS, LLC | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 33.0 | 0.0 | 42.6 | N |
| Franklin Templeton | core | 111360 | REG | FRANKLIN TEMPLETON INVESTMENT MANAGEMENT LIMITED | 09/16/2026 | N | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 4.0 | 0.0 | 40.5 | N |
| Franklin Templeton | core | 111382 | REG | TEMPLETON ASSET MANAGEMENT LTD. | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1.9 | 0.0 | 24.0 | N |
| Franklin Templeton | core | 307684 | REG | FRANKLIN BSP CAPITAL ADVISER LLC | 03/27/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 4.2 | 4.2 | N |
| Franklin Templeton | core | 172140 | ERA | FRANKLIN TEMPLETON INTERNATIONAL SERVICES S.A R.L. | 09/03/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |
| Franklin Templeton | core | 288668 | ERA | FRANKLIN TEMPLETON ALTS BRASIL ADMIN. DE INVESTIMENTOS LTDA. | 09/03/2026 | Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |
| Franklin Templeton | affiliate | 106629 | REG | PUTNAM INVESTMENT MANAGEMENT, LLC | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 104.3 | 0.0 | 117.2 | N |
| Franklin Templeton | affiliate | 106631 | REG | THE PUTNAM ADVISORY COMPANY, LLC | 09/16/2026 | N | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 2.5 | 0.0 | 33.2 | N |
| Franklin Templeton | affiliate | 107689 | REG | ROYCE INVESTMENT PARTNERS (ROYCE & ASSOCIATES, LP) | 02/02/2026 | N | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 10.5 | 0.0 | 12.4 | N |
| Franklin Templeton | affiliate | 108803 | REG | CLARION PARTNERS (CLARION PARTNERS, LLC) | 10/20/2026 | N | 22 | 0 | 3 | 19 | 0 | 0 | 0 | 0 | 0 | 1.1 | 0.0 | 73.7 | N |
| Franklin Templeton | affiliate | 322449 | ERA | CLARION PARTNERS EUROPE LIMITED | 12/18/2025 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |  |  |  |  |
| Franklin Templeton | affiliate | 322463 | ERA | CLARION PARTNERS EUROPE (U.K.) LIMITED | 12/18/2025 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |  |  |  |  |
| Franklin Templeton | affiliate | 110441 | REG | WESTERN ASSET MANAGEMENT COMPANY (WESTERN ASSET MANAGEMENT COMPANY, LLC) | 09/16/2026 | N | 33 | 0 | 18 | 0 | 0 | 12 | 1 | 2 | 1 | 82.1 | 0.0 | 185.0 | N |
| Franklin Templeton | affiliate | 142188 | REG | WESTERN ASSET MANAGEMENT COMPANY PTE LTD | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 2.8 | N |
| Franklin Templeton | affiliate | 110427 | REG | WESTERN ASSET MANAGEMENT COMPANY LIMITED | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 20.1 | N |
| Franklin Templeton | affiliate | 110783 | REG | BRANDYWINE GLOBAL INVESTMENT MANAGEMENT, LLC | 09/29/2026 | N | 15 | 0 | 1 | 0 | 0 | 0 | 0 | 14 | 0 | 17.6 | 0.0 | 65.4 | N |
| Franklin Templeton | affiliate | 124062 | REG | FIDUCIARY TRUST INTERNATIONAL, LLC | 12/22/2025 | N | 7 | 0 | 1 | 0 | 0 | 0 | 0 | 6 | 0 | 0.0 | 0.0 | 7.7 | Y (2) |
| Franklin Templeton | affiliate | 137028 | REG | CLEARBRIDGE INVESTMENTS, LLC | 08/28/2026 | N | 4 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 74.6 | 0.0 | 184.8 | N |
| Franklin Templeton | affiliate | 139012 | REG | CLEARBRIDGE INVESTMENT MANAGEMENT LIMITED | 09/16/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 | 0.0 | 9.9 | N |
| Franklin Templeton | affiliate | 151223 | REG | CLEARBRIDGE INVESTMENTS (NORTH AMERICA) PTY LIMITED | 08/28/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 | 0.0 | 2.2 | N |
| Franklin Templeton | affiliate | 147281 | REG | LEXINGTON PARTNERS L.P. | 06/16/2026 | Y | 113 | 113 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0.0 | 0.0 | 79.3 | Y (6) |
| Franklin Templeton | affiliate | 158672 | REG | BENEFIT STREET PARTNERS L.L.C. | 07/30/2026 | Y | 71 | 1 | 47 | 4 | 0 | 19 | 0 | 0 | 1 | 1.0 | 0.0 | 28.3 | N |
| Franklin Templeton | affiliate | 160617 | REG | BENEFIT STREET PARTNERS LIMITED | 05/07/2026 | Y | 34 | 2 | 13 | 0 | 0 | 18 | 0 | 1 | 9 | 0.5 | 0.0 | 22.6 | N |
| Franklin Templeton | unsure | 128240 | REG | TEMPLETON FINANCIAL SERVICES INC. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.4 | N |
| Wellington | core | 106595 | REG | WELLINGTON MANAGEMENT COMPANY LLP | 07/09/2026 | N | 77 | 0 | 34 | 0 | 0 | 0 | 0 | 43 | 163 | 636.4 | 0.0 | 1,428.0 | N |
| Wellington | core | 226715 | REG | WELLINGTON ALTERNATIVE INVESTMENTS (WELLINGTON ALTERNATIVE INVESTMENTS LLC) | 09/29/2026 | Y | 128 | 48 | 68 | 0 | 0 | 5 | 0 | 7 | 0 | 0.0 | 0.0 | 92.2 | Y (1) |
| Wellington | core | 288313 | REG | WELLINGTON FUNDS (US) LLC | 07/09/2026 | N | 13 | 0 | 5 | 0 | 0 | 0 | 0 | 8 | 0 | 0.0 | 0.0 | 5.4 | N |
| Wellington | core | 165192 | REG | WELLINGTON MANAGEMENT JAPAN PTE LTD (WELLINGTON MANAGEMENT JAPAN PTE. LTD.) | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0.0 | 0.0 | 17.7 | N |
| Wellington | core | 165208 | REG | WELLINGTON MANAGEMENT HONG KONG LIMITED | 07/09/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0.0 | 0.0 | 14.2 | N |
| Northern Trust | core | 7927 | REG | NORTHERN TRUST SECURITIES, INC (NORTHERN TRUST SECURITIES, INC.) | 07/17/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 1.7 | N |
| Northern Trust | core | 105780 | REG | NORTHERN TRUST INVESTMENTS, INCORPORATED | 06/15/2026 | N | 9 | 0 | 1 | 0 | 0 | 0 | 0 | 8 | 0 | 294.5 | 0.0 | 1,245.2 | N |
| Northern Trust | core | 111900 | REG | NORTHERN TRUST GLOBAL INVESTMENTS LTD | 03/27/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.4 | 0.0 | 208.4 | N |
| Northern Trust | affiliate | 174762 | REG | 50 SOUTH CAPITAL ADVISORS, LLC | 10/27/2026 | Y | 126 | 114 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 | 0.0 | 16.1 | N |
| Blackstone | core | 120934 | REG | BLACKSTONE ASSET BASED FINANCE ADVISORS LP | 10/20/2026 | Y | 37 | 3 | 2 | 1 | 0 | 31 | 0 | 0 | 0 | 0.0 | 0.0 | 70.4 | N |
| Blackstone | core | 134018 | REG | BLACKSTONE CREDIT SYSTEMATIC STRATEGIES LLC | 10/20/2026 | Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1.1 | 0.0 | 35.7 | N |
| Blackstone | core | 135952 | REG | BLACKSTONE REAL ESTATE ADVISORS EUROPE L.P. | 10/19/2026 | N | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 2.8 | N |
| Blackstone | core | 136979 | REG | BLACKSTONE MANAGEMENT PARTNERS L.L.C. | 03/30/2026 | Y | 36 | 36 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 145.7 | Y (3) |
| Blackstone | core | 137519 | REG | BLACKSTONE ALTERNATIVE CREDIT ADVISORS LP | 10/20/2026 | Y | 87 | 85 | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 0.0 | 0.0 | 44.1 | N |
| Blackstone | core | 142979 | REG | BLACKSTONE REAL ESTATE ADVISORS L.P. | 10/19/2026 | N | 53 | 0 | 0 | 53 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 130.7 | N |
| Blackstone | core | 146043 | REG | BLACKSTONE REAL ESTATE SPECIAL SITUATIONS ADVISORS L.L.C. | 10/19/2026 | N | 20 | 0 | 4 | 16 | 0 | 0 | 0 | 0 | 10 | 0.2 | 1.6 | 70.0 | N |
| Blackstone | core | 152294 | REG | BLACKSTONE LIQUID CREDIT ADVISORS I LLC | 10/20/2026 | Y | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.0 | 0.0 | 51.6 | N |
| Blackstone | core | 226598 | REG | BLACKSTONE PROPERTY ADVISORS L.P. | 10/19/2026 | N | 78 | 0 | 21 | 57 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 77.4 | N |
| Blackstone | core | 289751 | REG | BLACKSTONE INFRASTRUCTURE ADVISORS L.L.C. | 05/26/2026 | N | 41 | 0 | 41 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 80.2 | N |
| Blackstone | core | 296294 | REG | BLACKSTONE CREDIT BDC ADVISORS LLC | 10/20/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 100.6 | 100.6 | N |
| Blackstone | core | 304477 | REG | BLACKSTONE LIFE SCIENCES ADVISORS L.L.C. | 03/30/2026 | Y | 9 | 6 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0.0 | 0.0 | 13.2 | N |
| Blackstone | core | 305708 | REG | BLACKSTONE GROWTH ADVISORS L.L.C. | 05/05/2026 | Y | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 10.5 | N |
| Blackstone | core | 317860 | REG | BLACKSTONE PRIVATE INVESTMENTS ADVISORS L.L.C. | 03/30/2026 | N | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 17.9 | N |
| Blackstone | core | 327208 | REG | BLACKSTONE PRIVATE CREDIT STRATEGIES LLC | 10/20/2026 | Y | 54 | 54 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.7 | 0.0 | 57.9 | N |
| Blackstone | core | 158784 | REG | BLACKSTONE ALTERNATIVE SOLUTIONS L.L.C. | 10/15/2026 | N | 40 | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 20.1 | N |
| Blackstone | core | 292144 | REG | BLACKSTONE IRELAND FUND MANAGEMENT LIMITED | 10/20/2026 | Y | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 2.5 | N |
| Blackstone | core | 165796 | REG | BLACKSTONE STRATEGIC CAPITAL ADVISORS, L.L.C. | 03/30/2026 | Y | 18 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 15.6 | Y (1) |
| Blackstone | core | 107580 | REG | BLACKSTONE ALTERNATIVE ASSET MANAGEMENT L.P. | 10/15/2026 | N | 113 | 0 | 46 | 0 | 0 | 0 | 0 | 67 | 0 | 0.0 | 0.0 | 92.0 | N |
| Blackstone | core | 160157 | REG | BLACKSTONE TACTICAL OPPORTUNITIES ADVISORS L.L.C. | 07/21/2026 | Y | 103 | 103 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 40.4 | N |
| Blackstone | core | 289550 | REG | BLACKSTONE ISG-II ADVISORS L.L.C. | 03/30/2026 | Y | 6 | 4 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0.0 | 0.0 | 8.0 | N |
| Blackstone | core | 171640 | REG | BLACKSTONE MULTI-ASSET ADVISORS L.L.C. | 07/31/2026 | Y | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 8.5 | N |
| Blackstone | core | 165782 | REG | BLACKSTONE ALTERNATIVE INVESTMENT ADVISORS LLC | 08/04/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5.4 | 0.0 | 5.4 | N |
| Blackstone | core | 289202 | REG | BLACKSTONE ISG-I ADVISORS L.L.C. | 03/30/2026 | Y | 6 | 4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0.0 | 0.0 | 183.5 | N |
| Blackstone | core | 142922 | REG | BLACKSTONE STRATEGIC ALLIANCE ADVISORS L.L.C. | 03/30/2026 | N | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0.0 | 0.0 | 3.0 | N |
| Blackstone | core | 138208 | REG | BLACKSTONE REAL ESTATE ADVISORS V L.P. | 10/19/2026 | N | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.1 | N |
| Blackstone | core | 292121 | REG | BLACKSTONE IRELAND LIMITED | 10/20/2026 | Y | 50 | 1 | 0 | 0 | 0 | 49 | 0 | 0 | 0 | 0.0 | 0.0 | 15.2 | N |
| Blackstone | core | 304307 | REG | BLACKSTONE CLO MANAGEMENT LLC (BLACKSTONE CLO MANAGEMENT LLC (MANAGEMENT SERIES)) | 10/20/2026 | Y | 78 | 1 | 0 | 0 | 0 | 77 | 0 | 0 | 0 | 0.0 | 0.0 | 30.7 | N |
| Blackstone | core | 144537 | REG | BLACKSTONE LIQUID CREDIT STRATEGIES LLC | 10/20/2026 | Y | 24 | 8 | 0 | 0 | 0 | 16 | 0 | 0 | 2 | 8.7 | 0.0 | 18.8 | N |
| Blackstone | core | 290012 | ERA | BLACKSTONE EUROPE FUND MANAGEMENT S.A.R.L. | 03/30/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 46 |  |  |  |  |
| Blackstone | affiliate | 134009 | REG | STRATEGIC PARTNERS FUND SOLUTIONS ADVISORS L.P. | 06/11/2026 | Y | 45 | 34 | 0 | 9 | 2 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 80.4 | N |
| Blackstone | affiliate | 154425 | REG | HARVEST FUND ADVISORS LLC | 03/30/2026 | N | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 0.1 | 0.0 | 8.1 | N |
| KKR | core | 144533 | REG | KOHLBERG KRAVIS ROBERTS & CO. L.P. | 09/25/2026 | Y | 630 | 553 | 18 | 34 | 0 | 16 | 0 | 9 | 1 | 0.0 | 0.0 | 399.9 | Y (32) |
| KKR | core | 146629 | REG | KKR CREDIT ADVISORS (US) LLC | 09/25/2026 | Y | 108 | 38 | 60 | 0 | 0 | 2 | 0 | 8 | 1 | 1.9 | 0.0 | 270.9 | Y (1) |
| KKR | core | 309284 | REG | KKR REGISTERED ADVISOR LLC | 04/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.5 | 0.0 | 1.5 | N |
| KKR | core | 309194 | REG | KKR CREDIT ADVISORS (SINGAPORE) PTE. LTD. | 09/25/2026 | Y | 14 | 8 | 5 | 0 | 0 | 0 | 0 | 1 | 0 | 0.0 | 0.0 | 4.9 | N |
| KKR | core | 226531 | ERA | KKR ALTERNATIVE INVESTMENT MANAGEMENT (KKR ALTERNATIVE INVESTMENT MANAGEMENT UNLIMITED COMPANY) | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 178 |  |  |  |  |
| KKR | affiliate | 167429 | REG | GLOBAL ATLANTIC INVESTMENT ADVISORS, LLC (GLOBAL ATLANTIC INVESTMENT ADVISORS,  LLC) | 04/30/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.7 | 0.0 | 2.7 | N |
| KKR | unsure | 292803 | REG | FS/KKR ADVISOR, LLC | 06/01/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 16.1 | 16.1 | N |
| Apollo | core | 130610 | REG | APOLLO INVESTMENT MANAGEMENT, L.P. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 3.3 | 3.3 | N |
| Apollo | core | 143161 | REG | APOLLO CAPITAL MANAGEMENT, L.P. | 10/28/2026 | Y | 714 | 214 | 151 | 108 | 0 | 19 | 0 | 222 | 0 | 9.9 | 0.0 | 718.5 | Y (141) |
| Apollo | core | 156115 | REG | APOLLO CREDIT MANAGEMENT, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.8 | 29.2 | 30.0 | N |
| Apollo | core | 169120 | REG | APOLLO REAL ESTATE FUND ADVISER, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4.3 | 0.0 | 4.3 | N |
| Apollo | core | 286485 | REG | APOLLO CAPITAL CREDIT ADVISER, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.4 | 0.0 | 2.4 | N |
| Apollo | core | 327828 | REG | APOLLO MANAGER, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 3.6 | N |
| Apollo | core | 330339 | REG | APOLLO S3 RIC MANAGEMENT, L.P. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.4 | 0.0 | 0.4 | N |
| Apollo | core | 338148 | REG | APOLLO MPS MANAGEMENT, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| Apollo | affiliate | 159127 | REG | BRIDGE INVESTMENT GROUP (BRIDGE MULTIFAMILY FUND MANAGER LLC) | 07/01/2026 | N | 153 | 0 | 2 | 126 | 0 | 1 | 0 | 24 | 0 | 0.0 | 0.0 | 49.3 | Y (9) |
| Apollo | affiliate | 283058 | REG | REDDING RIDGE ASSET MANAGEMENT LLC | 09/24/2026 | N | 83 | 0 | 0 | 0 | 0 | 77 | 0 | 6 | 0 | 0.0 | 0.0 | 33.3 | Y (2) |
| Apollo | affiliate | 284256 | REG | REDDING RIDGE ASSET MANAGEMENT (UK) LLP | 03/31/2026 | N | 29 | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 0.0 | 0.0 | 13.2 | N |
| Apollo | unsure | 144673 | REG | APOLLO WEALTH MANAGEMENT, LLC | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 | N |
| Carlyle | core | 111128 | REG | THE CARLYLE GROUP (CARLYLE INVESTMENT MANAGEMENT L.L.C.) | 07/07/2026 | Y | 314 | 167 | 1 | 37 | 0 | 109 | 0 | 0 | 6 | 0.0 | 0.0 | 283.8 | Y (10) |
| Carlyle | core | 162053 | REG | CARLYLE GLOBAL CREDIT INVESTMENT MANAGEMENT L.L.C. | 07/15/2026 | Y | 67 | 62 | 0 | 1 | 0 | 3 | 0 | 1 | 1 | 7.1 | 5.6 | 68.4 | N |
| Carlyle | core | 168456 | REG | CARLYLE AVIATION SECURITIES PARTNERS LLC | 03/31/2026 | N | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 1.1 | N |
| Carlyle | core | 305746 | REG | CARLYLE AVIATION PDP MANAGEMENT LLC | 03/31/2026 | Y | 22 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 10.4 | Y (3) |
| Carlyle | affiliate | 322058 | REG | ALPINVEST PRIVATE EQUITY INVESTMENT MANAGEMENT, LLC | 02/10/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4.5 | 0.0 | 4.5 | N |
| Carlyle | affiliate | 159215 | REG | ALPINVEST PARTNERS B.V. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 39.9 | N |
| Carlyle | affiliate | 328458 | REG | ALPINVEST US HOLDINGS, LLC | 07/16/2026 | Y | 110 | 108 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0.0 | 0.0 | 57.7 | N |
| Ares | core | 130074 | REG | ARES MANAGEMENT LLC | 08/26/2026 | Y | 682 | 157 | 255 | 113 | 5 | 98 | 0 | 54 | 2 | 0.0 | 0.0 | 458.8 | Y (71) |
| Ares | core | 131619 | REG | ARES CAPITAL MANAGEMENT LLC | 08/26/2026 | Y | 34 | 1 | 31 | 0 | 0 | 1 | 0 | 1 | 0 | 0.0 | 53.9 | 97.6 | N |
| Ares | core | 157292 | REG | ARES CAPITAL MANAGEMENT II LLC | 08/26/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8.5 | 3.5 | 19.6 | N |
| Ares | core | 159050 | REG | ARES COMMERCIAL REAL ESTATE MANAGEMENT LLC | 08/26/2026 | N | 5 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 32.5 | N |
| Ares | core | 307090 | REG | ARES SYSTEMATIC CREDIT LIMITED | 08/26/2026 | N | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.2 | 0.0 | 9.9 | N |
| Ares | unsure | 284930 | REG | CION ARES MANAGEMENT, LLC | 08/26/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8.0 | 0.0 | 8.0 | N |
| Ares | unsure | 282852 | REG | ARES FINANCIAL CONSULTING LLC | 08/17/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 0.2 | N |
| TPG | core | 131940 | REG | TPG ANGELO GORDON (ANGELO, GORDON & CO., L.P.) | 08/24/2026 | Y | 237 | 32 | 176 | 1 | 0 | 21 | 0 | 7 | 0 | 0.0 | 0.0 | 115.9 | Y (2) |
| TPG | core | 159732 | REG | TPG GLOBAL ADVISORS, LLC | 03/27/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 196 | 0.0 | 0.0 | 173.6 | Y (6) |
| TPG | core | 159738 | REG | TPG CAPITAL ADVISORS, LLC | 07/24/2026 | Y | 127 | 127 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 140.6 | Y (50) |
| TPG | core | 170731 | REG | TPG REAL ESTATE ADVISORS, LLC | 06/04/2026 | N | 33 | 0 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 17.0 | Y (6) |
| TPG | core | 288851 | REG | TPG RE FINANCE TRUST MANAGEMENT, L.P. | 03/27/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 4.4 | N |
| TPG | core | 313020 | REG | TPG SOLUTIONS ADVISORS (TPG SOLUTIONS ADVISORS, LLC) | 06/02/2026 | Y | 26 | 25 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 11.6 | Y (5) |
| TPG | unsure | 141153 | REG | TPG FINANCIAL ADVISORS, LLC | 03/26/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 2.2 | N |
| Bain Capital | core | 134852 | REG | BAIN CAPITAL CREDIT, LP | 08/17/2026 | Y | 158 | 3 | 85 | 0 | 0 | 70 | 0 | 0 | 0 | 0.0 | 0.0 | 76.3 | Y (7) |
| Bain Capital | core | 145650 | REG | BAIN CAPITAL PUBLIC EQUITY, LP | 03/31/2026 | N | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0.0 | 0.0 | 0.2 | N |
| Bain Capital | core | 145652 | REG | BAIN CAPITAL VENTURES, LP | 03/31/2026 | Y | 20 | 4 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 9.8 | Y (1) |
| Bain Capital | core | 145653 | REG | BAIN CAPITAL PRIVATE EQUITY, LP | 03/31/2026 | Y | 36 | 36 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 96.4 | Y (3) |
| Bain Capital | core | 183517 | REG | BAIN CAPITAL ASSET MANAGEMENT, LP | 03/31/2026 | Y | 43 | 30 | 7 | 3 | 3 | 0 | 0 | 0 | 2 | 0.0 | 0.0 | 16.3 | N |
| Bain Capital | core | 291809 | REG | BAIN CAPITAL REAL ESTATE, LP | 06/09/2026 | N | 23 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 10.0 | Y (1) |
| Bain Capital | core | 297457 | REG | BAIN CAPITAL PARTNERSHIP STRATEGIES, LP | 03/31/2026 | N | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 1.7 | N |
| Bain Capital | core | 305575 | REG | BAIN CAPITAL INSURANCE SOLUTIONS, LP | 03/31/2026 | Y | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0.0 | 0.0 | 5.4 | N |
| Bain Capital | core | 321903 | ERA | BAIN CAPITAL INVESTMENTS (IRELAND) LIMITED | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |  |  |  |  |
| Bain Capital | core | 309371 | ERA | BAIN CAPITAL INVESTMENTS (LUXEMBOURG) S.A.R.L. | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |  |  |  |  |
| Bain Capital | core | 298511 | ERA | BAIN CAPITAL INVESTMENTS (EUROPE) LIMITED | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |  |  |  |  |
| Bain Capital | core | 167487 | ERA | BAIN CAPITAL PRIVATE EQUITY (EUROPE), LLP | 03/31/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |
| Leonard Green | core | 158164 | REG | LEONARD GREEN & PARTNERS, L.P. | 03/31/2026 | Y | 107 | 107 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 85.6 | N |
| Warburg Pincus | core | 156945 | REG | WARBURG PINCUS LLC | 03/31/2026 | Y | 213 | 213 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 108.7 | Y (20) |
| Roark | core | 160368 | REG | ROARK CAPITAL MANAGEMENT, LLC | 03/31/2026 | Y | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 34.2 | N |
| New Mountain | core | 155493 | REG | NEW MOUNTAIN FINANCE ADVISERS, L.L.C. | 06/01/2026 | Y | 7 | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.0 | 9.2 | 11.2 | N |
| New Mountain | core | 307111 | REG | NEW MOUNTAIN CREDIT CLO ADVISERS, L.L.C. | 10/15/2026 | N | 8 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0.0 | 0.0 | 3.4 | N |
| New Mountain | core | 161394 | REG | NEW MOUNTAIN CAPITAL, LLC (NEW MOUNTAIN CAPITAL, L.L.C.) | 03/30/2026 | Y | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 46.4 | N |
| Brookfield | core | 110497 | REG | BROOKFIELD PUBLIC SECURITIES GROUP LLC | 09/02/2026 | N | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 3.1 | 0.0 | 66.5 | N |
| Brookfield | core | 151599 | REG | BROOKFIELD ASSET MANAGEMENT PIC US, LLC | 08/06/2026 | N | 116 | 0 | 7 | 109 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 105.3 | Y (15) |
| Brookfield | core | 171207 | REG | BROOKFIELD ASSET MANAGEMENT PIC ADVISER (PRIVATE EQUITY), L.P. | 07/10/2026 | Y | 123 | 123 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | 73.8 | N |
| Brookfield | core | 312797 | REG | BROOKFIELD ASSET MANAGEMENT PIC BMG, LLC (BROOKFIELD ASSET MANAGEMENT PIC (ISG), LLC) | 07/10/2026 | N | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0.0 | 0.0 | 0.9 | N |
| Brookfield | core | 151605 | REG | BROOKFIELD ASSET MANAGEMENT PIC CANADA, LP | 08/05/2026 | Y | 135 | 135 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.7 | 0.0 | 152.1 | N |
| Brookfield | core | 316590 | REG | BROOKFIELD RENEWABLE ENERGY GROUP LLC | 08/05/2026 | Y | 119 | 118 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1.9 | 0.0 | 99.1 | N |
| Brookfield | affiliate | 106793 | REG | OAKTREE CAPITAL MANAGEMENT, L.P. | 08/17/2026 | Y | 284 | 7 | 221 | 0 | 0 | 41 | 0 | 15 | 2 | 0.0 | 0.0 | 183.3 | Y (9) |
| Brookfield | affiliate | 290193 | REG | OAKTREE FUND ADVISORS, LLC | 08/17/2026 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.6 | 12.4 | 14.1 | N |

## Name hits not counted (name collisions)

- Vanguard: 285052 Vanguard Capital (Vanguard Capital Wealth Advisors, LLC, Denver).
- Fidelity: 115504 Geode Capital Management, LLC (Boston). Its name does not carry Fidelity, and general knowledge says it has been separate from Fidelity since 2001.
- Goldman: 136134 Goldman Lancaster, Inc.; 157465 J. Goldman & Co., L.P.; 290153 Goldman Wealth Management & Associates, LLC.
- Capital Group: 140 unrelated names containing "Capital Group", "Capital Research" or "Capital International", among them 109868 Capital Research & Consulting LLC (Pasadena).
- Franklin Templeton: 106223 F L Putnam Investment Management; 106275 Franklin Street Advisors; 114465 Franklin, Parlapiano, Turner & Welch; 126508 Franklin Park Associates; 149101 Templeton & Phillips Capital Management; 311908 Franklin Parker Financial; 331699 AGP Franklin; 343891 East Franklin Capital.
- Wellington: 105837 Wellington Consulting Services; 149021 and 150529 Wellington Shields; 283853 Wellington Investment Advisors (Bullock Wealth Management Group); 297314 Wellington-Altus USA; 332803 The Wellington Grp; ERA 337658 Wellington Harbor Cap; ERA 333839 Wellington Partners (Munich VC).
- KKR: 156498 Accel-KKR (AKKR Fund II Management Company, LP).
- Apollo: 291902 Apollon Wealth Management; 321217 Apollon Financial.
- Ares: 161344 Black Creek Investment Management Inc. (Toronto).
- TPG: 298496 The Planning Group (TPG Advisors LLC, Northfield).
- Brookfield: 168271 Oaktree Advisors LLC (Coopersburg, PA).

## Could not match or verify

- **Affiliate ownership is not in the monthly file.** It has `Count of IA Affiliates` but no names. Every "affiliate" assignment and every collision exclusion rests on general knowledge, including Geode's independence and Tennenbaum and Highbridge still belonging to BlackRock and J.P. Morgan.
- **Unsure rows, left out of core:**
  - State Street: ERA 340778 (primary "STATE STREET DIGITAL LTD", legal "FINORYAQ CAPITAL", Boston) and ERA 340663 (primary "SPIRIT EYE INVESTMENT LTD", legal "STATE STREET DIGITAL LTD", Denver), 1 PE fund each.
  - Capital Group: 295193 The Capital Group Fiduciary Advisors, LLC (no city, $0.19bn).
  - Franklin Templeton: 128240 Templeton Financial Services Inc. (Chandler, AZ).
  - KKR: 292803 FS/KKR Advisor, LLC (a joint venture).
  - Apollo: 144673 Apollo Wealth Management, LLC (no address, $0.04bn).
  - Ares: 284930 CION Ares Management, LLC (a joint venture) and 282852 Ares Financial Consulting LLC (Calabasas).
  - TPG: 141153 TPG Financial Advisors, LLC (Portland).
- **Not included anywhere:** 285820 MidCap Financial Services Capital Management, LLC, a possible Apollo affiliate (5 private funds, 0 PE).
- **Not found in the file:**
  - No Capital Group non-US adviser entities.
  - No Ares "Landmark" adviser.
  - No Apollo "Athene" adviser.
  - No State Street-named registered adviser other than SSGA Funds Management.
  - No Northern Trust-named row with private equity funds.
- **Filing dates differ.** Counts reflect each adviser's latest filing in the file. Core rows run from 01/07/2026 to 10/28/2026, and all rows from 12/18/2025 to 10/30/2026. Leonard Green, Warburg Pincus, Roark and Bain Capital Private Equity are all dated 03/31/2026.
- **Fund type is self-reported** under Schedule D 7.B.(1) Q10. The monthly file gives no fund names, so no type assignment could be checked fund by fund here.
- **J.P. Morgan Private Investments Inc. (110186)** is counted as asset management because of its name. Whether it sits in J.P. Morgan's asset-management or wealth division was not verified.
