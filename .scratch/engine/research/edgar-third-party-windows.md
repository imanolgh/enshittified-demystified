# Research: Do third-party SEC filings state a brand's owner near its name?

For engine "Cost cuts before revenue" Q2 · Measured 2026-11-21 · EDGAR full-text search, 44 filings read by hand around each mention and read twice by DeepSeek with prompt p9 · DeepSeek spend $1.13.

## Question

Q2 proposes reading a filing whole when it comes from the brand's own company or its owners, or when it is a deal-type filing (8-K with EX-99, S-4, DEFM14A, SC TO, 425), and reading every other long filing as windows around each mention of the searched name. The first measurement (`edgar-quote-distance.md`) had no third-party filings. In third-party filings, how often is the brand's owner stated at all, how far is that from the brand's name, and what does a windowed read miss compared with a whole read?

## Method

- Brands: 10 from the chains research whose owner chains are known: Aspen Dental, MB2 Dental, Natrol, Dental365, Super Star Car Wash, Dr. Scholl's, PetSmart, Jersey Mike's, Heartland Dental and Crunch Fitness.
- Search: EDGAR full-text search (`efts.sec.gov/LATEST/search-index`), one exact-phrase query per brand over ticket 70's forms (8-K, S-1, S-4, 424B1 to 424B8, 10-K, 10-Q, DEF 14A, DEFM14A, SC TO-T, SC TO-I and 425; the search also returns their amendments), from 2001-01-01 to 2026-11-20. I took the first 3 pages of 100 hits in the order the search returns them. Totals over the form list: Aspen Dental 1,031, MB2 Dental 373, Natrol 453, Dental365 45, Super Star Car Wash 20, Dr. Scholl's 261, PetSmart 10,000 (the search's cap), Jersey Mike's 148, Heartland Dental 1,430, Crunch Fitness 1,008. 2,274 hits were fetched.
- Classification in code: a BDC filer is any filer with an 814- file number on any of its hits, so a BDC's notes prospectus filed under a 333- number is also left out. A filer is the brand's company or a known owner when its name matches the owners in the audit files, plus former owners that the filings themselves name: Natrol Inc. (the brand's own company until 2007), Schering-Plough and Merck (Dr. Scholl's), and Bally Total Fitness and its subsidiaries (Crunch). Forms 8-K, S-4, DEFM14A, SC TO and 425 are deal-type. Everything else is third party. Of the 2,274 hits, 664 are the brand's company or an owner, 566 deal-type, 532 third party and 512 BDC. Credit funds without an 814- number (Silver Point, Adams Street Credit Solutions Fund, BlackRock Private Credit Fund) stay third party.
- Sample: 49 third-party files drawn across the brands and filer kinds, of which 44 were read. One 2,791,587-character mortgage-pool prospectus (Morgan Stanley Capital I, 2024, Jersey Mike's) was dropped for budget, and four were dropped as repeats of a filer and kind already in the sample. A 47 MB LendingClub prospectus was swapped for another Jersey Mike's filing before it was converted. Each hit's file was stored as its own document (ticket 70) and converted to text with the extraction tests' `html_text` (`refetch.py`).
- Way 1 (read by hand): code found every mention of the brand name, every ownership word ("owned by", "subsidiary", "portfolio company", "affiliate of", "controlled by", "acquired", "acquisition", "parent") within 3,000 characters of a brand mention or alias, and every mention of a known owner anywhere in the filing. I read those passages and decided whether the filing states who owns the brand, recording the quote and its distance in characters from the nearest brand mention.
- Way 2 (DeepSeek): prompt p9 and `schema_p9.json` from `~/.local/share/extraction-eval/scripts/`, called the way `run.py`'s `deepseek-direct` path ran the approved p9 runs (`--no-brand --no-label --max-tokens 120000`, schema appended to the system prompt, JSON mode, model `deepseek-flash`). A small runner in the session scratchpad sent the calls instead of `run.py`, because `run.py` neither tracks DeepSeek spend nor stops on a 401 or 402. (a) Whole read: the file in one request up to 200,000 tokens, and a longer file in 150,000-token windows with 2,000 tokens of overlap ("Extraction execution" Q4), estimated at 4 characters a token. Five files were split, into 18 requests. (b) Windowed read: the first 2,000 characters, then 8,000 characters on each side of every mention of the brand name, merged where they overlap and joined in order with "[...]". The windowed reads were sent first.
- Comparison: a brand fact is a claim whose subject or object contains the brand name or an alias. Facts were matched on subject, predicate and object after removing legal suffixes and punctuation. Every brand-fact quote was checked against the stored text, exactly or after collapsing whitespace (line breaks inside a quote), and all passed.
- Fetching: before the first request I read robots.txt on both hosts with the user agent `ownership-research/0.1 (public-data research)`. `efts.sec.gov/robots.txt` answered 403 with `{"message":"Forbidden"}`, the gateway's answer for a path it doesn't serve, which RFC 9309 treats as no restrictions. The first request for `www.sec.gov/robots.txt` got the SEC's 403 "Request Rate Threshold Exceeded" page. The next request, with the same user agent plus the `Accept-Encoding: gzip, deflate` header that the SEC's access guidelines ask for, got the file, which allows `/Archives/edgar/data`. All later SEC requests sent that header, at most 1 a second: 26 search requests and 50 file downloads.

## Findings

| Filer kind | Filings | Length (chars) | State the brand's owner (way 1) | Filings with any brand fact (way 2) | Brand facts, whole / windowed | Cost per read, whole / windowed |
|---|---|---|---|---|---|---|
| Landlords and REITs | 14 | 3,407 to 915,604 | 0 | 0 | 0 / 0 | $0.0139 / $0.0029 |
| Mortgage pools (prospectuses, trust reports) | 6 | 9,172 to 3,060,369 | 1 | 1 | 5 / 5 | $0.0599 / $0.0113 |
| Lenders (credit funds without an 814- number) | 3 | 288,215 to 374,594 | 0 | 0 | 0 / 0 | $0.0212 / $0.0037 |
| Licensees | 4 | 139,003 to 334,762 | 2 | 3 | 4 / 4 | $0.0185 / $0.0101 |
| Other companies (proxies, suppliers, contracts, a competitor, an affiliate) | 17 | 1,839 to 692,630 | 4 | 5 | 4 / 10 | $0.0110 / $0.0053 |
| All | 44 | 1,839 to 3,060,369 | 7 (16%) | 9 | 13 / 19 | $0.0200 / $0.0057 |

- **Owner stated at all:** 7 of 44 third-party filings (16%) state an owner of the brand. 6 (14%) name an owner other than the brand's own company: Schering-Plough as licensor or maker of Dr. Scholl's (3 filings from 2002 to 2007, when it owned the name), KKR, Ontario Teachers' and the founder in a mortgage-pool prospectus, Align's share purchase in Heartland Dental's holding company, and Sentinel as MB2 Dental's former owner. 3 (7%) name an investor in the brand's company (the last three). The seventh is a trademark notice naming Natrol Inc. None of the 14 landlord filings or the 3 lender filings states an owner, and 1 of the 6 mortgage-pool filings does.
- **Distance:** every statement sits within 391 characters of a brand mention, and 6 of the 7 contain the brand name. The farthest is a trademark footnote in Brown Shoe's 2003 annual report: "Dr. Scholl's (2)", with "2 Schering-Plough Healthcare Products, Inc." in the footnote below the list. No filing states the brand's owner far from every mention. Known owners named far from the brand were about something else: Ares as AZEK's own controlling holder, about 96,000 characters from the Aspen Dental mention, and a KKR real estate fund as a certificate holder of another loan in the Heartland Dental prospectus.
- **Whole against windowed:** 9 of 44 filings gave any brand fact. The whole reads gave 13 distinct brand facts and the windowed reads 19, and 10 were found by both. The 3 found by the whole read only are facts the windowed read stated from the same quote under a different name: "affiliates of KKR & Co. Inc." against "KKR & Co. Inc."; "Compcare" against "Compcare Health Services Insurance Corporation"; "Heartland Dental" against "Heartland Dental Plan, Inc.". So in 0 of 44 filings did the windowed read miss a brand fact that the whole read found. With 0 misses in 44 filings, the 95% upper bound on the miss rate is about 7% of filings, or about 33% of the 9 filings with any brand fact.
- **Found by the windowed read only:** 9 facts in 4 filings. In JOINT Corp's proxy the windowed read found "ADMI acquired WellNow Urgent Care (formerly Five Star Urgent Care) in 2016 and Rejuv Medical Aesthetic Clinic and ClearChoice Management Services (CCMS) in 2020" (3 facts with the brand's company as buyer), which the whole read of the same filing missed. In 12 filings the windowed text was the entire filing, so both reads saw the same input, and 2 of those 12 still differed (Cobalt's subsidiary list and Chewy's agreement with PetSmart). Two reads of one text differed about as much as the whole and windowed reads did.
- **Facts about other parties:** the whole reads gave 631 claims that don't involve the brand and the windowed reads 290. Most are the filer's own structure and brands or the parents of mortgage-loan sellers ("UBS Americas, Inc. owned_by UBS AG", "CBL Holdings I, Inc. owned_by CBL & Associates Properties, Inc.", "OXO® owned_by Helen of Troy Limited", "Prestige International Holdings, LLC owned_by GTCR Golder Rauner II, LLC"). A windowed read drops these. Whether any of them concern another tracked brand wasn't checked.
- **Statements neither read took:** Prestige Brands' 2005 prospectus ("Schering-Plough, maker of Dr Scholl's®, which competes with our Compound W brand") and Holley's 2025 proxy ("MB2 Dental, and SONNY'S Enterprises prior to Sentinel's sale of these businesses") gave no claim in either read. Both reads also gave "Dr. Scholl's owned_by Caleres, Inc." from "lower net sales of our Dr. Scholl's, Naturalizer and LifeStride brands", though Caleres sells the shoes under license, and both gave ownership facts about "Heartland Dental Plan, Inc.", a Wisconsin insurer that only shares the name.
- **Cost:** a whole read cost $0.0200 on average and a windowed read $0.0057, over 44 filings each. For the 28 filings over 100,000 characters it was $0.0301 against $0.0073. For the 16 shorter ones it was $0.0023 against $0.0029: most fit in one window, and the whole read, sent second, reused DeepSeek's prompt cache where the two texts were identical. The three mortgage-pool prospectuses cost $0.101, $0.158 and $0.099 whole against $0.014, $0.046 and $0.002 windowed. The Heartland Dental prospectus names the brand 2,678 times, because it describes a loan on the brand's offices, so its windowed text was still 26% of the filing. Windowed text was 15% of the characters (2.33 million of 15.85 million) but 28% of the cost, because reasoning tokens are a large part of every call: output was 37% of the whole-read cost and 57% of the windowed cost. The cost estimate assumed $0.019 per long filing read whole, and long third-party filings here averaged $0.030.

## Per-filing list

"Owner stated" is way 1, with the distance from the nearest brand mention. Brand facts are distinct facts from the whole read and the windowed read. Costs come from each response's usage figures.

| # | Brand | Filer | Filer kind | Form, year | Length (chars) | Owner stated, distance | Brand facts, whole / windowed | Cost, whole / windowed |
|---|---|---|---|---|---|---|---|---|
| 01 | Aspen Dental | Cole Credit Property Trust V, Inc. | non-traded REIT prospectus (landlord) | 424B3, 2016 | 12,816 | No | 0 / 0 | $0.0003 / $0.0007 |
| 02 | Aspen Dental | JOINT Corp | other company (director biography) | DEF 14A, 2022 | 129,663 | No | 0 / 3 (0 both, 0 whole only, 3 windowed only) | $0.0143 / $0.0183 |
| 03 | Aspen Dental | GS MORTGAGE SECURITIES CORP II | mortgage-pool prospectus | 424B5, 2011 | 2,354,957 | No | 0 / 0 | $0.1011 / $0.0142 |
| 04 | Aspen Dental | FrontView REIT, Inc. | landlord REIT | 10-Q, 2025 | 142,384 | No | 0 / 0 | $0.0101 / $0.0015 |
| 05 | Aspen Dental | Silver Point Private Credit Fund | lender (non-814 credit fund) | 10-Q, 2026 | 363,632 | No | 0 / 0 | $0.0210 / $0.0048 |
| 06 | Aspen Dental | LendingClub Corp | consumer-loan prospectus (borrower employer) | 424B3, 2009 | 302,929 | No | 0 / 0 | $0.0132 / $0.0008 |
| 07 | Aspen Dental | ALLIANCE DATA SYSTEMS CORP | other company (client) | 10-Q, 2013 | 152,096 | No | 0 / 0 | $0.0077 / $0.0023 |
| 08 | Aspen Dental | HENRY SCHEIN INC | supplier (contract exhibit) | 10-Q EX-10.3, 2026 | 310,732 | No | 0 / 0 | $0.0107 / $0.0008 |
| 09 | Aspen Dental | AZEK Co Inc. | other company (director biography) | 10-K/A, 2021 | 131,744 | No | 0 / 0 | $0.0163 / $0.0028 |
| 10 | Crunch Fitness | Brixmor Property Group Inc. | landlord REIT (property list) | 10-K EX-99.1, 2026 | 57,979 | No | 0 / 0 | $0.0012 / $0.0032 |
| 11 | Crunch Fitness | KIMCO REALTY CORP | landlord REIT (property list) | 10-K EX-99.1, 2025 | 61,026 | No | 0 / 0 | $0.0027 / $0.0034 |
| 13 | Crunch Fitness | Apollo Realty Income Solutions, Inc. | non-traded REIT prospectus (landlord) | 424B3, 2023 | 3,407 | No | 0 / 0 | $0.0007 / $0.0010 |
| 14 | Crunch Fitness | CBL & ASSOCIATES PROPERTIES INC | landlord REIT | 10-K, 2024 | 551,294 | No | 0 / 0 | $0.0341 / $0.0064 |
| 15 | Crunch Fitness | CTO Realty Growth, Inc. | landlord (contract exhibit) | 10-Q EX-10.1, 2020 | 245,718 | No | 0 / 0 | $0.0122 / $0.0023 |
| 16 | Dental365 | ADAMS STREET CREDIT SOLUTIONS FUND | lender (non-814 credit fund) | 10-Q, 2026 | 288,215 | No | 0 / 0 | $0.0165 / $0.0039 |
| 17 | Dr. Scholl's | CALERES INC | licensee | 10-Q, 2016 | 139,003 | No | 1 / 1 (1 both, 0 whole only, 0 windowed only) | $0.0094 / $0.0063 |
| 18 | Dr. Scholl's | BROWN SHOE CO INC/ | licensee | 10-K EX-13, 2003 | 139,156 | Yes, 391 chars | 2 / 2 (2 both, 0 whole only, 0 windowed only) | $0.0214 / $0.0194 |
| 19 | Dr. Scholl's | HELEN OF TROY LTD | licensee (appliances) | 10-K, 2007 | 334,762 | Yes, 29 chars | 1 / 1 (1 both, 0 whole only, 0 windowed only) | $0.0314 / $0.0107 |
| 20 | Dr. Scholl's | Prestige Brands Holdings, Inc. | competitor (IPO prospectus) | S-1/A, 2005 | 692,630 | Yes, 0 chars | 0 / 0 | $0.0456 / $0.0199 |
| 21 | Dr. Scholl's | Griffin Capital Essential Asset REIT II, Inc. | non-traded REIT prospectus (landlord) | 424B3, 2016 | 915,604 | No | 0 / 0 | $0.0537 / $0.0025 |
| 22 | Dr. Scholl's | WESTPOINT STEVENS INC | licensee (textiles) | 10-K, 2002 | 208,303 | No | 0 / 0 | $0.0116 / $0.0040 |
| 23 | Heartland Dental | UBS Commercial Mortgage Securitization Corp. | mortgage-pool prospectus | 424B2, 2018 | 3,060,369 | Yes, 9 chars | 5 / 5 (4 both, 1 whole only, 1 windowed only) | $0.1577 / $0.0455 |
| 24 | Heartland Dental | UBS Commercial Mortgage Trust 2019-C16 | mortgage-pool trust annual report | 10-K, 2021 | 57,923 | No | 0 / 0 | $0.0009 / $0.0027 |
| 25 | Heartland Dental | UBS Commercial Mortgage Trust 2017-C3 | mortgage-pool servicer statement | 10-K EX-35.1, 2022 | 9,172 | No | 0 / 0 | $0.0002 / $0.0014 |
| 26 | Heartland Dental | ALIGN TECHNOLOGY INC | supplier (contract exhibit) | 10-Q EX-10.3, 2023 | 15,346 | Yes, 0 chars | 1 / 1 (1 both, 0 whole only, 0 windowed only) | $0.0017 / $0.0018 |
| 27 | Heartland Dental | SPIRIT REALTY CAPITAL, INC. | landlord REIT | 10-K, 2018 | 814,882 | No | 0 / 0 | $0.0258 / $0.0017 |
| 28 | Heartland Dental | COBALT CORP | other company (subsidiary list) | 10-K EX-21, 2002 | 1,839 | No | 2 / 4 (0 both, 2 whole only, 4 windowed only) | $0.0031 / $0.0043 |
| 29 | Jersey Mike's | SAUL CENTERS, INC. | landlord REIT (supplemental) | 10-Q EX-99.A, 2021 | 13,193 | No | 0 / 0 | $0.0097 / $0.0093 |
| 30 | Jersey Mike's | WACHOVIA COMMERCIAL MORTGAGE SECURITIES INC | mortgage-pool prospectus | 424B5, 2006 | 2,065,973 | No | 0 / 0 | $0.0985 / $0.0022 |
| 32 | Jersey Mike's | RETAIL VENTURES INC | other company (contract exhibit) | 10-K EX-10.52, 2005 | 122,253 | No | 0 / 0 | $0.0068 / $0.0007 |
| 34 | Jersey Mike's | PALISADE BIO, INC. | other company (contract exhibit) | 10-Q EX-10.1, 2022 | 237,942 | No | 0 / 0 | $0.0079 / $0.0008 |
| 35 | MB2 Dental | Holley Inc. | other company (director biography) | DEF 14A, 2025 | 145,079 | Yes, 0 chars | 0 / 0 | $0.0220 / $0.0039 |
| 36 | MB2 Dental | BlackRock Private Credit Fund | lender (non-814 credit fund) | 424B3, 2026 | 374,594 | No | 0 / 0 | $0.0261 / $0.0025 |
| 37 | Natrol | FITWAYVITAMINS, INC. | other company (reseller) | 10-K/A, 2011 | 52,559 | No | 0 / 0 | $0.0060 / $0.0052 |
| 39 | Natrol | FIRST MIDWEST BANCORP INC | other company (director biography) | DEF 14A, 2003 | 67,347 | No | 0 / 0 | $0.0052 / $0.0016 |
| 40 | Natrol | MARTEK BIOSCIENCES CORP | supplier | 10-K EX-13.01, 2003 | 104,480 | Yes, 0 chars | 1 / 1 (1 both, 0 whole only, 0 windowed only) | $0.0130 / $0.0055 |
| 41 | Natrol | WOMEN FIRST HEALTHCARE INC | other company | 10-K, 2001 | 182,147 | No | 0 / 0 | $0.0134 / $0.0156 |
| 42 | PetSmart | Benchmark 2023-V2 Mortgage Trust | mortgage-pool trust annual report | 10-K, 2025 | 41,499 | No | 0 / 0 | $0.0012 / $0.0018 |
| 43 | PetSmart | Cole Credit Property Trust III, Inc. | non-traded REIT prospectus (landlord) | 424B3, 2012 | 26,728 | No | 0 / 0 | $0.0018 / $0.0038 |
| 45 | PetSmart | CORPORATE PROPERTY ASSOCIATES 15 INC | non-traded REIT prospectus (landlord) | 424B3, 2001 | 11,869 | No | 0 / 0 | $0.0006 / $0.0009 |
| 46 | PetSmart | Sonoma Pharmaceuticals, Inc. | supplier (contract exhibit) | 10-K EX-10.32, 2017 | 83,468 | No | 0 / 0 | $0.0002 / $0.0028 |
| 47 | PetSmart | Chewy, Inc. | affiliate under the same owner (contract exhibit) | S-1/A EX-10.4, 2019 | 26,448 | No | 0 / 1 (0 both, 0 whole only, 1 windowed only) | $0.0006 / $0.0030 |
| 48 | Super Star Car Wash | ESSENTIAL PROPERTIES REALTY TRUST, INC. | landlord REIT | 10-Q, 2025 | 249,244 | No | 0 / 0 | $0.0131 / $0.0014 |
| 49 | Super Star Car Wash | ESSENTIAL PROPERTIES REALTY TRUST, INC. | landlord REIT | 10-K, 2025 | 545,445 | No | 0 / 0 | $0.0279 / $0.0027 |

Way 1 notes on filings with no owner stated: most name the brand as a tenant, a loan, a borrower's employer, a counterparty or a past employer in a director's biography. AZEK's 2021 proxy says an Ares co-founder "serves on the boards of directors of City Ventures, LLC and the parent entities of Aspen Dental", which points at Ares but states no ownership. CBL's "Crunch Fitness (Owned by Others)" is about the store building. Essential Properties' tenant table pairs "Denali Midco 2 LLC" (tenant) with "Super Star Car Wash" (concept) without saying how they relate.

Brand facts by filing, from the whole read (the windowed read found the same unless noted):

- 02 JOINT Corp: none in the whole read. The windowed read gave WellNow Urgent Care, Rejuv Medical Aesthetic Clinic and ClearChoice Management Services acquired_by Aspen Dental Management, Inc.
- 17 Caleres: Dr. Scholl's owned_by Caleres, Inc. (a licensed line, as noted above).
- 18 Brown Shoe: Dr. Scholl's and Original Dr. Scholl's owned_by Schering-Plough Healthcare Products, Inc.
- 19 Helen of Troy: Dr. Scholl's® owned_by Schering-Plough HealthCare Products, Inc. ("licensed from").
- 23 UBS Commercial Mortgage Securitization Corp.: Heartland Dental, LLC owned_by Heartland Dental Holding Corporation; Heartland Dental Holding Corporation owned_by affiliates of KKR & Co. Inc. (windowed: KKR & Co. Inc.); Heartland Dental, LLC acquired_by KKR & Co. Inc.; owned_by Ontario Teachers' Pension Plan; owned_by Richard Eugene Workman (4.28%).
- 26 Align Technology: Heartland Dental Holding Corporation acquired_by Align Technology, Inc.
- 28 Cobalt: Heartland Dental Plan, Inc. owned_by Compcare, and Heartland Dental Plan of Michigan, Inc. owned_by Heartland Dental (Plan). The windowed read named the parents in full and added Cobalt as parent of both.
- 40 Martek: Natrol owned_by Natrol Inc. (trademark notice).
- 47 Chewy: none in the whole read. The windowed read, on the same text, gave Chewy, Inc. owned_by PetSmart, Inc. ("restricted subsidiary").

## DeepSeek spend

- 101 calls, all finished with `stop`, with no errors and no 401, 402 or balance error. All were sent on Saturday 2026-11-21 between 04:42 and 04:59 UTC, at off-peak prices ($0.15 per million input tokens on a cache miss, $0.003 on a cache hit, $0.60 per million output tokens).
- Whole reads: 57 calls, 4,186,856 input tokens (485,376 from cache) and 536,949 output tokens (437,962 of them reasoning), $0.8788. Windowed reads: 44 calls, 870,934 input tokens (163,584 from cache) and 239,780 output tokens (199,891 reasoning), $0.2505. Total from the usage figures: $1.1293, under the $1.25 cap.
- Balance before the first call: $3.50. Balance after the last: $2.24. The drop of $1.26 includes another agent's test that ran on the same account at the same time.

## What it means for Q2

- In this sample, third-party filings seldom state the brand's owner: 16% state any owner, 7% an investor in the brand's company, and the landlord and lender filings none. Every statement found sat within 391 characters of the brand's name, and none sat far from every mention. The self-reference pattern behind every far fact in the first measurement ("we", "our Principal Stockholder") did not occur.
- The windowed read missed no brand fact that the whole read found in 44 filings. Its differences from the whole read were the same size as the differences between two reads of identical text.
- A windowed read cost 28% of a whole read across the sample and 24% for filings over 100,000 characters. The saving comes from long filings with few mentions, such as mortgage-pool prospectuses and landlords' annual reports. A filing that names the brand thousands of times saves little, and short filings save nothing.
- A whole read also returns more than twice as many facts about other parties (631 against 290), mostly about the filer's own structure. A windowed read gives those up.
- Under the proposed rule every 8-K counts as deal-type. Here 537 of the 566 deal-type hits are 8-Ks, and 299 of the 566 come from landlords, REITs and mortgage trusts by filer name, plus 111 8-Ks from Brown Shoe, a licensee. These would be read whole. Their length wasn't measured.
- Limits: 10 brands, 44 filings from the first 300 hits per brand, only 9 filings with any brand fact, one prompt version, one run of each read, and way 1 judged by one reader.
