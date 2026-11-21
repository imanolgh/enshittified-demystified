# Research: Do 10-Ks name the deals that earlier 10-Qs report?

For engine "Cost cuts before revenue" Q7 · Measured 2026-11-21 · code over EDGAR filings, then every flagged deal read by hand · no AI calls, no spend.

## Question

The revised Q7 has EDGAR full-text search read every 10-Q that a brand's company or its owners filed after their latest 10-K, and skip older 10-Qs, because the next 10-K normally restates the year's deals. The risk is a deal that an old 10-Q reports and the next 10-K leaves out, such as a brand bought and sold within one year, or a small acquisition the 10-K never names. Does that happen, and how often?

## Method

- Companies: 22 US-listed consumer companies that buy or sell brands often: Central Garden & Pet, B&G Foods, Hain Celestial, Post Holdings, Driven Brands, J.M. Smucker, Conagra, Campbell's, Hershey, McCormick, Church & Dwight, Clorox, Spectrum Brands, Newell Brands, Tractor Supply, Chewy, Petco, Planet Fitness, Restaurant Brands International, General Mills, Edgewell and Energizer. Mister Car Wash and Kenvue from the candidate list are no longer in the SEC's ticker file, so Edgewell and Energizer took their places. Spectrum Brands' filer number (CIK 109177) belonged to HRG Group until their 2018 merger, so its 2015 to 2018 10-Qs also cover HRG's other holdings.
- Filings: each company's 10-Qs filed from 2015-01-01 to 2026-11-20 and its 10-Ks from 2014 on, listed from `data.sec.gov/submissions`. That is 734 10-Qs (filed 2015-01-30 to 2026-11-19) and 261 10-Ks. Amendments were left out. Only the primary document of each filing was downloaded and kept as plain text. Smucker's 10-Ks for fiscal 2014 to 2018, Edgewell's fiscal 2014 10-K (filed as Energizer Holdings) and all of Clorox's 10-Ks keep the MD&A and financial statements in Exhibit 13 or Exhibit 99.1, so that exhibit was added to those 10-Ks (19 filings).
- Deals in each 10-Q, collected by code in two ways:
  - Inline XBRL (485 of the 734 10-Qs have it): any `us-gaap:BusinessAcquisitionAcquireeEntityName` value, and every company-defined member on `BusinessAcquisitionAxis`, `AssetAcquisitionAxis`, `DisposalGroupNameAxis` and the disposal-group axis, with the member's name split into words (`drvn:ClearwaterCarWashMember` becomes "Clearwater Car Wash"). No filing in the set used the acquiree-name tag, so the members carry the deals.
  - Text: sentences containing deal language ("completed the acquisition of", "acquisition of", "acquired", "purchase of", "sale of", "sold", "divestiture of", "divested", "disposition of", "merger with", "exit of"), taking the proper name after the phrase, any "X business" or "X brand" name in the sentence, and a quoted defined term when no other name came out. Names made only of generic words, and the company's own name, were dropped.
  - A second, wider pass took every capitalised name in any sentence with "completed", "acquired", "sold" or "divested", to check what the first pass missed.
- Matching: each name was counted once per company, at the first 10-Q that mentions it. Code checked whether it appears anywhere in the next 10-K, after lower-casing, dropping punctuation, apostrophes and legal suffixes (Inc., LLC, Holdings), and treating "&" as "and". A name joined by "and" also counted as present when every part appears. An XBRL member also counted as present when the 10-K's XBRL uses the same member. The 10-K for the fiscal year containing the 10-Q's quarter was the next 10-K in every case, so the two checks are one. Code also checked the previous 10-K and every later one.
- Grouping: name forms of one deal ("Bell Nursery Holdings LLC", "Bell", "Bell Nurseries") were grouped when they share an uncommon word and first appear within 400 days. Grouping can also merge separate deals that share a word (Driven's 2021 and 2022 car wash purchases all share "wash"), so every name form missing from its next 10-K was read on its own, whatever its group.
- Reading: I read every name form that code flagged as missing from the next 10-K, from both passes, and searched the 10-K for other spellings. I sorted each into (a) a real brand or business the company bought or sold that the 10-K doesn't name, (b) present in the 10-K under another form, or (c) not an ownership deal. For the one case (a), I read every 8-K the company filed from 2022-04-01 to 2023-03-31 (the main document and every EX-99 exhibit) and the company's investor newsroom.
- Denominator: most name forms are not deals (segments, agreements, defined terms). To estimate how many of the groups that code found in the next 10-K are real ownership deals, I read a random sample of 40 of them, each with the 10-Q sentence and the 10-K text around the match.

## Findings

### Counts

| Measure | Count |
|---|---|
| 10-Qs scanned | 734 (22 companies) |
| Name forms found in 10-Qs (first pass) | 991, of which 953 have a later 10-K |
| Groups of those 953 forms | 627 |
| Forms code found in the next 10-K | 885 of 953 |
| Forms missing from the next 10-K, all read | 68 (in 30 groups with no form in the 10-K, and 38 forms whose group is named) |
| Extra name forms from the wide pass | 1,152; 71 missing from the next 10-K, all read |
| Real ownership deals among the found groups (sample) | 28 of 40 sampled groups (70%), so about 420 of the 604 found groups |
| Deals missing from the next 10-K after reading | 1 |
| Share | about 1 in 420 deals, 0.2% (0.2% to 0.3% over the sample's 95% range of 330 to 495 deals) |

- How the 139 forms read by hand sorted out: first pass 68 forms, 1 (a), 44 (b) and 23 (c); wide pass 71 forms, the same case (a) again, 16 (b) and 54 (c).
- The sample also tested the matching. In all 28 real deals, the 10-K text around the match names the same deal. One match was weak: "WoodWick Candle" matched only "Yankee Candle" in a brand list, though the 10-K does name the deal (Smith Mountain, WoodWick).
- 38 name forms come from 10-Qs filed after the company's latest 10-K, so they have no next 10-K. Q7 reads those 10-Qs, and they were not tested.
- The one case comes from Driven Brands, the only roll-up in the set. It names small purchases one by one in its 10-Qs and puts some of them under "All Other" in the 10-K.

### The confirmed case

- **Driven Brands, Clearwater Car Wash.** The 10-Q for the quarter ended 2022-06-25 (filed 2022-08-05) says in Note 13, Subsequent Events: "From June 26, 2022 through August 4, 2022, the Company acquired Jack Morris Auto Glass and K & K Glass for approximately $54 million and $40 million, respectively. The acquisition of these 18 glass sites further expand the Company's U.S. auto glass offering. The Company also acquired 4 car wash sites including Speedy Shine Express Car Wash and Clearwater Car Wash for approximately $34 million and $24 million, respectively." The filing's XBRL also has `drvn:ClearwaterCarWashMember`. Source: https://www.sec.gov/Archives/edgar/data/1804745/000162828022021169/drvn-20220625.htm
  - Next 10-K: fiscal 2022, filed 2023-03-01, https://www.sec.gov/Archives/edgar/data/1804745/000180474523000007/drvn-20221231.htm. It names Jimmy Clean Car Wash, Speedy Shine Express Car Wash and Quick & Clean Car Wash, with sites and prices, and puts everything else under "All Other Car Wash". It never names Clearwater. The next 10-Q (quarter ended 2022-09-24) had already dropped the name. No later Driven 10-K or 10-Q names it either.
  - 8-Ks: none of Driven's 12 8-Ks filed from 2022-04-01 to 2023-03-31 names Clearwater or Speedy Shine. That includes the earnings releases in their EX-99.1 exhibits (filing list: https://data.sec.gov/submissions/CIK0001804745.json).
  - Press releases: Driven's investor newsroom lists 20 releases for 2022, and none is about either car wash (feed: https://investors.drivenbrands.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=3&pressReleaseDateFilter=3&categoryId=00000000-0000-0000-0000-000000000000&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=2022&excludeSelection=1). The 2022 auto glass deals got releases (2022-01-04, 2022-09-08), and the car washes did not. The corporate newsroom at drivenbrands.com has only recent feature stories.
  - So the one 10-Q that names this purchase is the only public filing or release found that does. The deal is small: about $24 million, inside a group of 4 sites that also included Speedy Shine's 2. The sites joined Driven's US car wash business, whose sale Driven's 10-Q filed 2025-05-08 reports.

### False alarms, (b)

All 60 were the same deal under another spelling, under a defined term, or with a parsing artefact. Examples:

- Hershey, Tyrrell's: the 10-Q filed 2018-10-26 writes "the sale of the Tyrrell's business" (https://www.sec.gov/Archives/edgar/data/47111/000004711118000049/a2018_formx10-qq3.htm). The fiscal 2018 10-K writes "On July 5, 2018, we sold the Tyrrells business", without the apostrophe (https://www.sec.gov/Archives/edgar/data/47111/000004711119000010/a2018form10-kq4.htm). This brand was bought (inside Amplify, January 2018) and sold within one year, and the 10-K names both.
- Church & Dwight, "LDS Acquisition": the 10-Q filed 2015-05-07 uses the defined term (https://www.sec.gov/Archives/edgar/data/313927/000156459015003545/chd-10q_20150331.htm). The 10-K filed 2016-02-19 says "the acquisition of the Lil' Drug Store products" (https://www.sec.gov/Archives/edgar/data/313927/000156459016012917/chd-10k_20151231.htm).
- Restaurant Brands, "CRG": the 2024 Q1 10-Q's XBRL member `qsr:CRGMember` (https://www.sec.gov/Archives/edgar/data/1618756/000161875624000082/qsr-20240331.htm). The 10-K filed 2025-02-21 says "Carrols Restaurant Group Inc." 109 times and "CRG" never (https://www.sec.gov/Archives/edgar/data/1618756/000161875625000087/qsr-20241231.htm).
- Hershey "barkTHINS" (code read "THINS"), B&G "Green Giant and La Sueur" (a misspelling of Le Sueur in the 10-Q), Driven "Frank's Car Wash Express" (the 10-K says "Frank's Car Wash"), Spectrum "GBL Purchase Price", Planet Fitness "Fitmex Transaction" and Newell "CH&S" are the same kind.
- Without Exhibit 13 and 99.1, five more real deals would have looked missing. Smucker's fiscal 2015 10-K main document never names Sahale Snacks, bought in September 2014 (https://www.sec.gov/Archives/edgar/data/91419/000119312515235197/d918672d10k.htm). Its Exhibit 13 does (https://www.sec.gov/Archives/edgar/data/91419/000119312515235197/d918672dex13.htm). The same holds for Smucker's Enray and Silocaf purchases and Clorox's Aplicare sale (fiscal 2018 Exhibit 99.1) and Saudi joint-venture purchase.

### Non-deals, (c)

All 77 were names near deal words that are not a purchase or sale of a brand or business. Examples:

- Plants and assets: Post's `ClintonMassachusettsPlantMember` disposal group (https://www.sec.gov/Archives/edgar/data/1530950/000153095022000154/post-20220331.htm), Post's David City, Nebraska egg plant, Energizer's Tianjin plant, Edgewell's Household Products Asia packaging facility, HRG's Compass oil and gas assets.
- Securities: Petco's sale of its Rover Group shares (https://www.sec.gov/Archives/edgar/data/1826470/000095017023026849/woof-20230429.htm), Hershey's purchase of its own shares from the Milton Hershey School Trust, 10b5-1 plan text.
- Agreements, programs and labels: "Merger Sub 1", "Rule 10b5-1 Plan", "Adjusted EBITDA", "Condensed Consolidated Balance Sheets", segment names, brand lists ("sold under the brands ...").
- Driven's XBRL members for groups of unnamed sites ("A2022 Car Wash Acquisitions").

### Deals that no filing names

Some deals have no name in the 10-Q either, so Q7's rule doesn't change whether full-text search can find them. Conagra's 10-Q filed 2024-10-02 reports that "In July 2024, we acquired the manufacturing operations of an existing co-manufacturer of our cooking spray products" (https://www.sec.gov/Archives/edgar/data/23217/000155837024013126/tmb-20240825x10q.htm), and the 10-K repeats it without a name. Hain's 10-Q filed 2024-11-07 says that "the Company completed the sale of three non-core brands during the fourth quarter of fiscal 2024 and first quarter of fiscal 2025" and names only ParmCrisps in that filing (https://www.sec.gov/Archives/edgar/data/910406/000095017024123246/hain-20240930.htm). Driven and Planet Fitness also report site and franchisee-store purchases by count ("acquired 7 car wash sites", "Eight California Stores").

## What this means for Q7

- In 22 brand-buying companies over 2015 to 2026, the next 10-K named every deal an earlier 10-Q named, except one: a roughly $24 million car wash purchase by Driven Brands that only one 10-Q names. No 8-K or company press release names it either. That is about 1 deal in 420 (0.2%).
- No brand bought and sold within one year was missing. The one such case in the set, Hershey's Tyrrells, is in the 10-K.
- The 10-K often names a deal in a different form from the 10-Q (Tyrrell's and Tyrrells, a defined term against the full name, a member code against a company name). Code found 68 names missing at first, and 67 of them turned out to be in the 10-K or not deals.
- For Smucker (fiscal 2014 to 2018) and Clorox (every year), the restated deals sit in the 10-K's Exhibit 13 or 99.1, not its main document. Five deals in this set are named only there.
- The test covers deals that a 10-Q names. Deals reported only by count or description, like Conagra's co-manufacturer or Driven's unnamed sites, can't be found by searching a name in either filing.

## Limits

- Recall depends on the patterns. The first pass missed the Clearwater sentence ("acquired 4 car wash sites including ...") and found the deal only through its XBRL member. The wide pass found it in the text. 249 of the 734 10-Qs (mostly before 2019) have no inline XBRL, so deals there depend on the text patterns alone.
- The share's denominator is an estimate from a sample of 40 groups. Grouping by shared words merges some separate deals, so the true number of deals is, if anything, higher, which would make the share smaller.
- Only the 10-K's primary document (plus Exhibit 13 or 99.1 where the financial statements sit) was checked. Other exhibits, such as Exhibit 21's subsidiary list, were not.
- The companies are large consumer companies that buy and sell brands. Smaller roll-ups that report many named small purchases, the pattern behind the one case, are represented only by Driven Brands.

## Fetching

Before the first request I read `www.sec.gov/robots.txt`, which allows `/Archives/edgar/data`, and `data.sec.gov/robots.txt`, which answered 404, meaning no restrictions. Every SEC request sent `User-Agent: ownership-research/0.1 (public-data research)` and `Accept-Encoding: gzip, deflate`, one at a time, at least 1.05 seconds apart: 1,105 to `www.sec.gov` and 38 to `data.sec.gov`. All answered 200, except the 404 for `data.sec.gov/robots.txt`, with no 403 and no rate-limit page. EDGAR full-text search (`efts.sec.gov`) was not used. For Driven Brands I read `investors.drivenbrands.com/robots.txt` (allows everything, crawl delay 10 seconds) and made three more requests there: a press-release page that returned 404, then the overview page and the 2022 release feed, each after a 10-second wait. The gap between the robots.txt read and the first page was not timed. I also read `www.drivenbrands.com/robots.txt` (allows everything) and its sitemap. Scripts and downloads are in the session scratchpad and are not part of the repo.
