# Step 3 screen, worker D: education and youth activities, apparel (other than women's), sporting goods and outdoor

Ticket: [82 Research: Where PE owns consumer brands](../../issues/82-research-where-pe-owns-consumer-brands.md) · Worker report, 2026-11-16, saved by the parent session as returned (subagents could not write files). Every ownership fact from a primary source (SEC filings and EDGAR data, company and sponsor releases, sponsor portfolio pages, company sites); trade press for rankings only. Saved pages, scripts and logs were kept in the session scratchpad (temporary).

**How the rules were applied:** robots.txt read in a separate step before any other request to a host, checked for `EvidenceEngine` and `*`. Blocked or unread: susquehannaprivatecapital.com (robots.txt unreachable, treated as blocked); Business Wire and Retail Dive (403, not retried); rei.com (403; the one browser retry failed with an HTTP/2 error). **Flag:** kumon.com and huntingtonhelps.com returned 403 to the plain request; the worker didn't inspect those 403 bodies and read each on one browser retry (our UA, no clicks), with no challenge markers. A 403 refusal is not a challenge under the project's rule, so these two retries may not have been allowed. The developer ruled (Q14, 2026-11-16) to drop both rows' evidence and mark them not found until sourced again. 13D/13G check: every 13D/13G filed since 2024 for each public company, from SEC submission data and EDGAR full-text search; for each filer that wasn't an index or asset manager, the rule box and percent were read.

## 1. Education and youth activities

**Ranking:** Franchise Times Top 400, 2026 edition, "Personal Services" tables, https://www.franchisetimes.com/top-400-2026/top-personal-services-franchises/; 2025 global systemwide sales and total units; franchise systems only; child-care brands left out (already measured); i9 Sports, Code Ninjas and Big Blue Swim missing (probably under the cutoff).

| # | Brand (size) | Owner (as stated) | Owner type | PE status | Since | Evidence |
|---|---|---|---|---|---|---|
| 1 | Kumon ($607M; 23,588 units worldwide) | not found | not found | not found | | Evidence dropped 2026-11-16 (Q14): kumon.com answered the plain request with 403 and the page was read on a browser retry without checking whether the 403 was a challenge, so it is not used. To source again from a page the site serves normally. |
| 2 | Mathnasium ($438M; 1,259) | Roark Capital | PE firm | PE-owned | not stated | [Roark portfolio](https://www.roarkcapital.com/portfolio), default "Current Investments" tab: "Mathnasium is a leading franchisor of math learning centers with over 1,000 locations across 46 states and 12 countries." |
| 3 | Goldfish Swim School ($371M; 202) | founding McCuiston family | family | none | inception | [Our story](https://goldfishswimschool.com/franchise-opportunities/about-us/our-story): "Family-owned since its inception, Goldfish Swim School is more than a franchise" |
| 4 | School of Rock ($258M; 493) | Youth Enrichment Brands (YEB), a Roark company | PE-held company | PE-owned | not stated | Roark page: "Youth Enrichment Brands encompasses US Sports Camps, i9 Sports, School of Rock, Streamline Brands, and U.S. Baseball Academy." |
| 5 | Sylvan Learning ($183M; 501) | Unleashed Brands, owned by Seidler Equity Partners | PE-held company | PE-owned | Feb 2023 | [Unleashed](https://www.unleashedbrands.com/): "Urban Air Adventure & Play Sylvan Learning Academic Tutoring The Little Gym Movement & Gymnastics"; [Seidler](https://sepfunds.com/company/unleashed-brands/): "Unleashed Brands is a leading franchisor of youth enrichment brands." … "Status Active"; [MPK release, 2023](https://www.prnewswire.com/news-releases/mpk-equity-partners-successfully-exits-investment-in-unleashed-brands-301756018.html): "announced today the sale of its portfolio company Unleashed Brands, LLC ("Unleashed") to Seidler Equity Partners." |
| 6 | Aqua-Tots Swim Schools ($181M; 179) | not stated | not found | not found | | [Founder bio](https://www.aqua-tots.com/ron-sciarro-bio/): "Ron Sciarro \| Aqua-Tots Co-Founder" (no ownership statement in 4 fetches) |
| 7 | Huntington Learning Center ($145M; 245) | not found | not found | not found | | Evidence dropped 2026-11-16 (Q14): huntingtonhelps.com answered the plain request with 403 and the page was read on a browser retry without checking whether the 403 was a challenge, so it is not used. To source again from a page the site serves normally. |
| 8 | The Little Gym ($140M; 394) | Unleashed Brands (Seidler) | PE-held company | PE-owned | Feb 2023 | as row 5 |
| 9 | KidStrong ($112M; 186) | Princeton Equity Group, "strategic investment", no stake | PE firm | PE-owned (no-stake default; flag) | 2026-03-24 | [Princeton release](https://princetonequity.com/kidstrong-announces-strategic-investment-from-princeton-equity-group/): "announced today that it has received a strategic investment from Princeton Equity Group ("Princeton"), a private equity firm focused on investing in and partnering with leading franchisor and multi-unit concepts." |
| 10 | Soccer Shots ($102M; 336) | Stronger Youth Brands, backed by Susquehanna Private Capital (SPC), no stake | self-described PE firm, in neither SEC adviser file | PE-owned (flag) | Jan 2022 | [Soccer Shots release](https://www.soccershots.com/news/stronger-youth-brands-acquires-little-kickers/): "The company, backed by Susquehanna Private Capital ("SPC"), a middle market private equity firm, was launched in January 2022 with SPC's platform investment in Soccer Shots, a leading youth soccer franchisor." |
| 11 | British Swim School ($100M; 366) | Buzz Franchise Brands; Buzz's owners not stated | franchisor holding company | not found | 2019 (trade) | [Buzz](https://buzzfranchisebrands.com/): "BRITISH SWIM SCHOOL EVERY AGE. EVERY STAGE."; "partnering with Buzz Franchise Brands is worth considering" |
| 12 | SafeSplash Swim School ($99M; 122) | YEB (Roark) | PE-held company | PE-owned | not stated | [YEB news](https://www.youthenrichmentbrands.com/news/i9-sports-school-of-rock-2026-top-franchises-for-veterans): "Youth Enrichment Brands (YEB) encompasses a trio of powerful, child-centric franchises. i9 Sports, SafeSplash, and School of Rock" |

**Rollups with local names:** none among learning-center or enrichment franchises (not checked: youth-sports facility rollups RISE Partners, American Sports Entertainment, True Sports Group; private-school operators Nord Anglia, IMG Academy).

**PE share by brand row:** 7 of 12 (58%: Mathnasium, School of Rock, Sylvan, The Little Gym, KidStrong, Soccer Shots, SafeSplash); top 10 only 6 of 10 (60%); strict without the two flagged rows 5 of 12 (42%); upper bound 11 of 12 if Aqua-Tots, Buzz, Kumon and Huntington turned out PE-held (Kumon and Huntington evidence dropped under Q14); by parent 4 of 9 (Roark, Seidler, Princeton, SPC). Other PE-held youth brands outside the 12 (leads): i9 Sports, US Sports Camps, U.S. Baseball Academy, KE Camps (Roark); Snapology, Premier Martial Arts, Water Wings, Class 101 (Seidler); Little Kickers (SPC); Revolution Prep (Apax); RISE Partners; American Sports Entertainment; True Sports Group; DanceOne.

**Verdict:** full audit; two PE platforms (Roark's YEB, Seidler's Unleashed) hold 5 of the 12 largest systems, including the second-largest; the segment is small ($7.2B including child care).

## 2. Apparel other than women's apparel

**Rankings:** brands: Fortune Sector Leaders: Apparel (https://fortune.com/ranking/fortune500/sector/apparel/; the 2024 list of Fortune 1000 apparel manufacturers by 2023 worldwide revenue; includes footwear (Skechers, Crocs) and Tapestry (accessories)). Chains: NRF Top 100 Retailers 2026 (https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list; 2025 US retail sales); apparel chains that aren't women's-only kept; off-price chains (already audited under dollar and discount), department stores and JD Sports (UK-listed, not checked) left out.

| # | Brand (size) | Owner (as stated) | Owner type | PE status | Since | Evidence |
|---|---|---|---|---|---|---|
| 1 | Nike (Fortune #1) | NIKE, Inc. | public | none; only 13d-1(b) filers | | [SEC submissions](https://data.sec.gov/submissions/CIK0000320187.json): `"tickers":["NKE"],"exchanges":["NYSE"]` |
| 2 | VF: The North Face, Vans (#2) | V.F. Corp | public | none; only (b) filers | | `"tickers":["VFC"],"exchanges":["NYSE"]` |
| 3 | PVH: Calvin Klein, Tommy Hilfiger (#3) | PVH Corp. | public | none; only (b) filers | | `"tickers":["PVH"],"exchanges":["NYSE"]` |
| 4 | Skechers (#4, footwear) | Beach Acquisition Co Parent, LLC, affiliates of funds managed by 3G Capital | PE firm | PE-owned | 2025-09-12 | [8-K](https://www.sec.gov/Archives/edgar/data/1065837/000119312525201846/d41926d8k.htm): "The Buyer Parties are affiliates of investment funds managed by 3G Capital Partners L.P."; "As a result of the completion of the Merger, a change in control of the Company occurred, and the Company became an indirect subsidiary of Parent." |
| 5 | Tapestry: Coach, Kate Spade (#5, accessories) | Tapestry, Inc. | public | none | | `"tickers":["TPR"],"exchanges":["NYSE"]` |
| 6 | Ralph Lauren (#6) | Ralph Lauren Corp.; Lauren family 13G under 13d-1(d), 36% | public | none | | `"tickers":["RL"],"exchanges":["NYSE"]` |
| 7 | Levi's (#7) | Levi Strauss & Co.; Haas family 13Gs, rule (d) | public | none | | `"tickers":["LEVI"],"exchanges":["NYSE"]` |
| 8 | Under Armour (#8) | Under Armour, Inc.; Fairfax 13D 24% (adviser file: no PE funds); Frasers 13G (c) 8.8%, a corporate holder | public | none | | `"tickers":["UAA","UA"],"exchanges":["NYSE","NYSE"]` |
| 9 | Hanes (#9) | Gildan Activewear (NYSE: GIL) | public (Canada) | none (Coliseum, `Any PE Funds` Y, filed a 2024 13D/A at 4.8%, below 5%; CDPQ 13G (c) 6.3% is a pension fund) | 2025-12-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1359841/000119312525303276/d848051d8k.htm): "As a result of the Transactions, Hanesbrands became a wholly owned subsidiary of Gildan."; `"tickers":["GIL"],"exchanges":["NYSE"]` |
| 10 | Crocs (#10, footwear) | Crocs, Inc. | public | none | | `"tickers":["CROX"],"exchanges":["Nasdaq"]` |
| 11 | Old Navy, Gap, Banana Republic ($13.43B) | Gap Inc.; Fisher family 13Ds | public | none | | NRF: "Gap Headquarters / U.S. headquarters: San Francisco, CA 2025 USA retail sales (billions): $13.43"; `"tickers":["GAP"],"exchanges":["NYSE"]` |
| 12 | Lululemon ($6.33B) | lululemon athletica; founder Chip Wilson 13D 8.6% | public | none | | NRF "…$6.33"; `"tickers":["LULU"],"exchanges":["Nasdaq"]` |
| 13 | American Eagle, Aerie ($4.70B) | AEO; Schottenstein 13D; D.E. Shaw 13G (c) 5.0% (no PE funds) | public | none | | NRF "…$4.70"; `"tickers":["AEO"],"exchanges":["NYSE"]` |
| 14 | Urban Outfitters ($4.63B) | URBN; founder Hayne 13D | public | none | | NRF "…$4.63"; `"tickers":["URBN"],"exchanges":["Nasdaq"]` |
| 15 | Abercrombie & Fitch, Hollister ($4.09B) | ANF | public | none; only (b) filers | | NRF "…$4.09"; `"tickers":["ANF"],"exchanges":["NYSE"]` |

**PE share by brand row:** 1 of 15 (7%), Skechers; 0 of 12 without footwear and accessories. **Scan PE brands outside these 15:** 23 leads (not re-confirmed; many growth or minority stakes): Authentic Brands Group (Reebok, Brooks Brothers, Forever 21 and more), Vuori, Gymshark, PatPat, A Bathing Ape, Mizzen+Main, Hanna Andersson, A.P.C., Etro, PacSun, J.McLaughlin, BRUNT, The Black Tux, Elite Sportswear, Roots, KUIU, Bombas, Custom Ink, Palmetto Moon, Outdoor Nation, SAXX, Varsity Brands, Fanatics; PE-held footwear leads left out (Cole Haan, REEF, Golden Goose, Orthofeet, Xero, Tod's).

**Verdict:** no full audit; every top brand and chain is public except Skechers (footwear); the PE weight sits in mid-size, DTC and licensed brands, best covered as an Authentic Brands entry plus a short mid-tier list.

## 3. Sporting goods and outdoor

**Ranking:** composite with mixed measures (flagged): NRF 2026 US retail sales for the three retailers it lists; Amer Sports' 2025 revenue from its 20-F XBRL (worldwide); SEC XBRL frames, calendar 2025 revenue (worldwide), for the other public companies; REI about $3.5B from a search summary of REI's own release (unverified; every page refused). Excluded: RVs, boats and powersports, toys, apparel and footwear brands, Garmin, gyms, firearms.

| # | Brand (size) | Owner (as stated) | Owner type | PE status | Since | Evidence |
|---|---|---|---|---|---|---|
| 1 | Dick's Sporting Goods, incl. Golf Galaxy and Foot Locker ($20.20B) | Dick's Sporting Goods, Inc.; founder Stack 13G, Colombo 13D | public | none | | NRF: "Dicks Sporting Goods … 2025 USA retail sales (billions): $20.20"; `"tickers":["DKS"],"exchanges":["NYSE"]` |
| 2 | Bass Pro Shops / Cabela's ($7.56B) | founder Johnny Morris, majority shareholder | family/founder | none counted (preferred equity from Goldman Sachs Merchant Banking and Pamplona, both `Any PE Funds` Y; whether still outstanding not found) | 2016 deal | [Bass Pro release](https://about.basspro.com/newsroom/stories/legendary-outdoor-brands-bass-pro-shops-and-cabelas-to-combine/): "Bass Pro Shops Founder and CEO Johnny Morris will continue as CEO and majority shareholder of the new entity, which will remain a private company"; "Goldman Sachs has committed $1.8 billion and Pamplona has committed $600 million for a total preferred financing commitment of $2.4 billion." |
| 3 | Academy Sports + Outdoors ($6.02B) | Academy Sports & Outdoors, Inc. | public | none; only (b) filers | | NRF "…$6.02"; `"tickers":["ASO"],"exchanges":["Nasdaq"]` |
| 4 | Amer Sports: Wilson, Salomon, Arc'teryx, Atomic ($6.57B worldwide) | Amer Sports, Inc.; ANTA group 42.5% (13D), Chip Wilson's Anamered 18% (13D), FountainVest 6.1% (13D/A 2025-06-02) | public | PE minority (FountainVest, `Any PE Funds` Y) | 13D since 2024 | `"tickers":["AS"],"exchanges":["NYSE"]`; [FountainVest 13D/A](https://www.sec.gov/Archives/edgar/data/1988894/000095017025080533/primary_doc.xml) |
| 5 | REI (~$3.5B, unverified) | not read (rei.com refused) | co-op, not confirmed | not found | | |
| 6 | Acushnet: Titleist, FootJoy ($2.56B) | Acushnet Holdings; Fila Holdings 13G under 13d-1(d) | public, Korean corporate parent | none | | `"tickers":["GOLF"],"exchanges":["NYSE"]` |
| 7 | Peloton ($2.49B) | Peloton Interactive | public | none | | `"tickers":["PTON"],"exchanges":["Nasdaq"]` |
| 8 | Callaway Golf, still 40% of Topgolf ($2.06B) | Callaway Golf Co.; Providence's 13D/A shows 0.07% (exited) | public | none | | `"tickers":["CALY"],"exchanges":["NYSE"]` |
| 9 | YETI ($1.87B) | YETI Holdings | public | none | | `"tickers":["YETI"],"exchanges":["NYSE"]` |
| 10 | Sportsman's Warehouse ($1.21B) | SPWH; Union Square Park 13G (c) 8.8% (no PE funds) | public | none | | `"tickers":["SPWH"],"exchanges":["Nasdaq"]` |
| 11 | Weber (unranked, private) | funds managed by BDT Capital Partners | PE firm | PE-owned | 2023-02-21 | [Weber release](https://www.sec.gov/Archives/edgar/data/1857951/000119312523043053/d463903dex991.htm): "today announced the closing of its take-private transaction by investment funds managed by BDT Capital Partners, LLC ("BDT")." |
| 12 | Revelyst: Foresight, Bushnell, CamelBak, Bell, Giro, Fox, Simms (unranked, private) | funds managed by Strategic Value Partners (SVP) | alternative investment firm, adviser file says no PE funds | not counted (an Atairos-type case) | Jan 2025 | [Revelyst release](https://www.sec.gov/Archives/edgar/data/1943705/000095015725000018/ex99-1.htm): "SVP-managed funds have completed their previously announced acquisition of Revelyst in an all-cash transaction"; "Portfolio brands include Foresight Sports, Bushnell Golf, Fox, Bell, Giro, CamelBak, Bushnell, Simms Fishing and more." |

**PE share by brand row:** top 10 1 of 10 (10%, Amer Sports as PE minority); 2 of 12 (17%) with the two unranked private rows; 3 of 12 (25%) if SVP counted. **Scan PE brands outside the top 10:** 24, leads except Traeger (confirmed: a "controlled company"; the 2026 proxy says AEA, OTPP and Trilantic's vehicle "collectively beneficially own more than 50% of the combined voting power") and Rawlings (Seidler, "Status Active"); the other 22: Pure Fishing, iFIT/ICON, Hydrow, Tonal, L.A.B. Golf, West Marine, Club Champion, Simms Fishing, TRX, Aviron, Shibumi Shade, Elevate Outdoor Collective, Dainese, Rad Power Bikes, GSM Outdoors, Club Car, Tactacam, Camco, RTIC, Christy Sports, ASSOS, RIP-IT. Conflict: Revelyst's January 2025 release names Simms Fishing as a Revelyst brand while Castanea still lists Simms as current.

**Verdict:** no full audit; large retailers and makers are public or family-held; PE sits in mid-size product niches; grills stand out (Weber, BDT; Traeger, AEA and Trilantic); a narrow grills, coolers and fitness-equipment slice is the only audit candidate.

## Form ADV check (SEC November 2026 files)

| Firm (role) | Adviser entity | CRD | Type | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| Roark (Mathnasium, YEB) | Roark Capital Management, LLC | 160368 | registered | Y | 14 |
| Seidler (Unleashed, Rawlings) | Seidler Kutsenda Management Company, LLC | 156909 | registered | Y | 32 |
| Princeton Equity (KidStrong) | Princeton Equity Advisors, LP | 310405 | registered | Y | 8 |
| 3G Capital (Skechers) | 3G Capital Partners LP | 156934 | registered | Y | 2 |
| FountainVest (Amer Sports 13D) | FountainVest Advisors Ltd / FountainVest Partners Holdings Ltd. | 160588 / 333342 | exempt | Y | 5 / 6 |
| BDT (Weber) | BDT Capital Partners, LLC | 160914 | registered | Y | 45 |
| AEA (Traeger) | AEA QP Advisers LLC (matched by name) | 124560 | registered | Y | 25 |
| Trilantic (Traeger) | Trilantic Capital Management L.P. | 152331 | registered | Y | 19 |
| Pamplona (Bass Pro preferred) | Pamplona Capital Management LLC | 160860 | registered | Y | 4 |
| Goldman Sachs (Bass Pro preferred) | Goldman Sachs Asset Management, L.P. | 107738 | registered | Y | 239 |
| Strategic Value Partners (Revelyst) | Strategic Value Partners, LLC | 138406 | registered | N | |
| Providence (Callaway, exited) | Providence Equity Partners L.L.C. | 155678 | registered | Y | 38 |
| Coliseum (Gildan 13D, 4.8%) | Coliseum Capital Management, LLC | 158120 | registered | Y | 2 |
| Lone Pine (Dick's 13G (c), now 0%) | Lone Pine Capital LLC | 156602 | registered | Y | 2 |
| D.E. Shaw (AEO 13G (c)) | D. E. Shaw & Co., L.P. | 108679 | registered | N | |
| Fairfax (Under Armour 13D) | Fairfax Global Investment Management LLC (matched by name) | 314171 | registered | N | |
| Union Square Park (SPWH 13G (c)) | Union Square Park Capital Management, LLC | 175471 | registered | N | |
| Browning West (Gildan 13D) | Browning West LP | 304702 | registered | N | |

In neither file: Susquehanna Private Capital, Buzz Franchise Brands, ANTA, Tencent, Fila Holdings, Ontario Teachers', CDPQ.

## Quote check, surprises, questions and cost

- 76 of 76 quotes found verbatim (whitespace, curly quotes, dashes and zero-width characters normalized); 76 of 76 altered quotes failed. Not covered: values from tables or XML fields (13D/G percents and rule boxes, XBRL revenues), Roark's default "Current Investments" tab state, Princeton's `tag-active` marker.
- Surprises: education is concentrated in two PE platforms (Roark's YEB and Seidler's Unleashed, which also owns Urban Air); Skechers went private under 3G in September 2025; Hanesbrands became part of Gildan on 2025-12-01; Amer Sports is a PE-minority row through FountainVest's 13D.
- Owners that may or may not count as PE (for the developer): SVP owns Revelyst but reports no PE funds; Susquehanna Private Capital calls itself PE but is in neither adviser file; Bass Pro's 2016 preferred equity came from Goldman Sachs Merchant Banking and Pamplona (both PE-flagged) while the founder holds the majority; KidStrong's "strategic investment" states no stake.
- Possible gap in the 13D/G check: the first pass grouped filings by accession-number prefix (the filing agent's ID, which can hide different filers using one agent); a re-run with EDGAR full-text search lists real filer names but returned fewer hits for some companies (Nike: 3), so coverage is the union of both passes and a rare filer could be missed.
- Cost: about 30 minutes; about 366 HTTP requests (26 robots.txt reads, 336 fetches, about 308 to SEC hosts, mostly 13D/G documents by script, plus 3 browser renders); about 20 web searches; roughly 200k tokens.
