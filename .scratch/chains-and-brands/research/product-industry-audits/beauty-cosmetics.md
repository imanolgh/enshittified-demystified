# Product industry audit: Beauty and cosmetics

Ticket: [91-research-product-industry-audits](../../issues/91-research-product-industry-audits.md) · Researched 2026-11-17 (fetches logged 22:58–23:25 UTC) · Scope: makeup, skin care and hair care products, the same scope as the earlier screen's section 2 ([s3-a](../pe-consumer-scan/s3-a-beauty-personal-care.md)). Ownership facts come from primary sources only. YouGov supplies the ranking only.

**Short answer**

| | Beauty and cosmetics (N = 30 brand rows, all ranked) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **6 / 30 (20.0%)**. All six count as PE-owned and none as minority: Suave and St. Ives (Evermark, a Yellow Wood Partners portfolio company), Revlon (former lenders, among them Angelo, Gordon & Co.), CoverGirl and Sally Hansen (Coty, where the JAB group holds about 54% of the votes) and Clairol (Wella Company, held by KKR). |
| Sensitivity (numbers only, see Open questions) | **5 / 30 (16.7%)** if Revlon's lender ownership, last confirmed 2023-05-02, is treated as stale under the 18-month rule. **4 / 30 (13.3%)** if JAB's stake in Coty doesn't count as PE. **4 / 30 (13.3%)** if body lotion and sun care brands are put in beauty instead of personal care. **3 / 30 (10.0%)** with both the Revlon and JAB caveats. **7 / 30 (23.3%)** if Regent, Avon's new owner, counted as PE. |
| Owner not found | **1 / 30 (3.3%)**: Mary Kay. Its site served "Mary Kay Inc. \| Site Unavailable" to the bot. |
| Brand-direct affiliate programs | **0 confirmed.** **Probable: 1, non-PE** (Avon): search shows an avon.com "Affiliates" page for a program run through CJ, but avon.com returned 403. **Network listings only: 6, all non-PE** (e.l.f., Clinique, Estée Lauder, Lancôme, Neutrogena, Olay). These are directory listings that weren't opened. **PE rows: 0 brand-direct.** Revlon has only an India network listing, which one directory says is paused. |
| BDC overlap | **1 row: Suave.** "Suave Silk Holdings III Corp." (industry "Personal Care Products") holds first-lien term loans and revolvers at four Apollo-managed BDCs. The largest is a $210.0M term-loan principal at Apollo Debt Solutions BDC on 2026-06-30. MidCap Financial Investment Corp also lists "Suave Silk Holdings I Corp. Common Equity - Common Stock". BDC-held equity doesn't count toward PE. |

- **Biggest finding:** the PE in mass beauty sits on brands that the big conglomerates sold or spun off: Suave and St. Ives (Unilever to Yellow Wood), Clairol (Coty to KKR), Revlon (lenders after Chapter 11) and Coty's mass color brands (JAB). The 24 other rows belong to public conglomerates or family-controlled companies: P&G, L'Oréal, Kimberly-Clark through Kenvue, Beiersdorf, Estée Lauder, Unilever, Clorox, Reckitt, Galderma, e.l.f. Beauty and Paul Mitchell. Avon is the exception: Regent, a holding company, bought it.
- **The earlier screen's top 10 found 0 PE.** That screen used a different YouGov measure: consideration in a mixed beauty and personal care top 25. Its first 10 rows (Dove hair care, Neutrogena, CeraVe, Olay, Head & Shoulders, Nivea, Pantene, Burt's Bees, Aveeno, Maybelline) are still non-PE here. The PE rows rank 5th (Suave), 11th (Revlon), 14th (CoverGirl), 19th (St. Ives), 26th (Clairol) and 28th (Sally Hansen).
- **The industry clears the 10% bar** on the headline count, on every single sensitivity and on any two caveats combined (3 / 30 at worst). It falls below only when the wider scope, the JAB caveat and the Revlon caveat all apply together: 2 / 30 (6.7%). See "Category share".
- **Pending:** Coty's strategic review of its consumer beauty business has been running since September 2025, and a sale of CoverGirl or Sally Hansen would change their owner. Coty's filings of 2026-11-04 and 2026-11-05 announced no deal.

## How this was sourced (read first)

- **Ranking:** three YouGov Ratings lists ("skincare & cosmetics brands", "hair care brands", "household & personal care brands"), all with the data collection period "Third quarter of 2026", merged by popularity. The section "Ranking" gives the rules. YouGov supplied the ranking only.
- **Ownership facts** come from:
  - SEC filings: 10-K, DEF 14A, 20-F, 8-K exhibit, 424B5, Schedule 13D/A and 13G/A, and EDGAR submissions JSON;
  - sponsor releases on the sponsor's own site (Yellow Wood, EQT);
  - company releases on PR Newswire (LG H&H with The Avon Company; Natura);
  - Revlon's own release, read as Business Wire wire copy on StreetInsider;
  - company pages: L'Oréal, L'Oréal Finance, Beiersdorf, Galderma, Reckitt and Paul Mitchell;
  - brand-site footers: Suave, St. Ives, Clairol, CoverGirl, Sally Hansen and Revlon.
- **Reused from the earlier screen:** the P&G, Clorox, Kimberly-Clark/Kenvue, Unilever, L'Oréal and Beiersdorf sources. Every one was re-fetched and its quote re-checked. The screen's 13G check (22 Schedule 13Gs at P&G, Unilever, Kimberly-Clark and Clorox, dated 2025-11 to 2026-11, all filed under Rule 13d-1(b)) is relied on, not repeated. The four EDGAR filing lists were re-read today: they show no Schedule 13D since Unilever's 2018 13D/A, and no new 13G filer.
- **SEC access:** 24 requests (www.sec.gov 16, data.sec.gov 7, efts.sec.gov 1), all HTTP 200. All used the user agent `EvidenceEngine ownership-research bot (product industry audit)`, spaced at least 1.1 s apart.
- **Robots:**
  - robots.txt was read before the first request to every host (40 reads).
  - Hosts whose robots.txt returned 4xx (not 429) were treated as unrestricted, per the rule: data.sec.gov 404, yellowwoodpartners.com 404, efts.sec.gov 403, businesswire.com 403, sheamoisture.com 403, avon.com 403, unilever.com 403, esteelauder.com 403, neutrogena.com 403, download.marykay.com 403.
  - www.marykay.com answered its robots.txt with the same HTML splash page, so no rules applied.
  - **regentco.com disallows ClaudeBot** (a Cloudflare-managed block). It was never fetched.
  - www.regentlp.com's robots.txt redirected to regentco.com and was not followed further.
  - No crawl-delay applied to any host used.
- **Blocked or failed:**
  - 403 Access Denied (Akamai or CloudFront, not challenge pages): businesswire.com, sheamoisture.com, avon.com, unilever.com, esteelauder.com, neutrogena.com.
  - 404: paulmitchell.com/pages/about-us. Its /pages/our-story page worked.
  - Bot-challenge pages ("Just a moment"):
    - streetinsider.com: one retry in the bot's own Playwright browser, no clicks. It cleared by itself (page 024).
    - lancome-usa.com (homepage only): not retried, because no ownership fact depended on it.
  - marykay.com served "Site Unavailable" to the bot.
- **YouGov list paging:** each Ratings list shows 20 brands and loads the rest with its own "Load More" button and then infinite scroll. The rendering script (Playwright, bot user agent) triggered that button by script and scrolled to the list's own loading marker until the list was complete: 113, 54 and 117 brands. This is pagination on a robots-allowed page, not a challenge page. It is flagged under Open questions in case the developer reads the no-clicks rule more broadly.
- **Never fetched:**
  - competitor sites, WhoIsMyDentist, Private Equity Vet and Reddit;
  - PitchBook, CB Insights and Preqin;
  - Wikipedia and trade press (Retail Dive, BeautyMatter, Premium Beauty News, Glossy, AlphaMaven, Miller Thomson's deal note), which came up in searches;
  - affiliate directories (FlexOffers, LinkClicky, UpPromote, INRDeals, Cuelinks, GRIN).
- **Leads only, never cited:** the trade-press items above. Two examples: a law firm's note that Regent's purchase of Avon North America closed on 2026-09-01, and Ralph Lauren's 2021 Business Wire headline calling Regent a "Leading Private Equity Firm".
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control, or a PE owner with no stated stake.
- **Quotes:** copied from saved page text. A check script found all 76 quotes in their saved text after normalizing whitespace, curly quotes and dashes. Pages and scripts are in the session scratchpad (temporary) under `pages/beauty/` and `scripts/beauty/`.

## Ranking

**No free brand-level US sales ranking exists for beauty.** The earlier screen recorded that Circana's brand data appears only in paywalled or registration-walled trade press, and that Brand Finance's Cosmetics 50 measures global brand value with only 10 rows free. That wasn't re-searched here. YouGov's 2026 consideration ranking (the earlier screen's source) has only 25 rows, and they mix beauty with oral care, deodorant and soap. So this audit uses YouGov Ratings, which ranks every brand it tracks.

**Sources** (all for US adults, popularity = "the % of people who have a positive opinion of" a brand; "Data collection period: Third quarter of 2026"):
- (A) "The most popular skincare & cosmetics brands": https://yougov.com/en-us/ratings/skincare-cosmetics-brands. 113 brands (pages 003, 008).
- (B) "hair care brands": https://yougov.com/en-us/ratings/hair-care-brands. 54 brands (pages 004, 009).
- (C) "household & personal care brands": https://yougov.com/en-us/ratings/household-personal-care-brands. 117 brands (pages 010, 011). It is used only for the beauty brands YouGov files there: Burt's Bees, Suave, Clairol and the direct sellers.

**Composite rules (applied by `scripts/beauty/rank.py`):**
1. **Merge** all entries of A and B, plus the beauty entries of C, and sort by popularity, highest first. Ties are broken by fame (higher first), then by name.
2. **Scope:** makeup, skin care, hair care, nails and fragrance. The following were excluded and left to the personal care audit (the earlier screen split them the same way):
   - body lotion and ointment: Vaseline, Aquaphor, Jergens, Gold Bond, Lubriderm;
   - sun care: Coppertone, Banana Boat, Hawaiian Tropic;
   - soap and body wash: Softsoap, Dial, Dove (the household list's whole Dove brand, 75%), Le Petit Marseillais, Dr. Bronner;
   - deodorant, shaving, oral care and feminine care;
   - baby care: Johnson's Baby, Dove Baby, Aveeno Baby, Baby Magic, Babyganics.

   Also excluded:
   - retailers and salons: Bath & Body Works, Ulta Beauty, Sephora, Sally Beauty, Great Clips, Supercuts, Sport Clips, Fantastic Sams, European Wax Center;
   - company names: Unilever, Coty Inc., LVMH, Beiersdorf AG, Procter & Gamble, Kimberly-Clark;
   - OTC drugs: Rogaine, Differin, Desitin.
3. **Product lines fold into the master brand printed on the pack.** The row keeps the master brand's own score where it is listed, otherwise its best line's score:
   - Fructis and Nutrisse → Garnier;
   - Nice 'n Easy and Natural Instincts → Clairol;
   - Revlon Colorsilk → Revlon;
   - 18 L'Oréal Paris lines (True Match, Voluminous, Feria, Excellence, Elvive lines and others) → L'Oréal Paris.
4. **Two YouGov entities for one brand merge:** Mary Kay and Mary Kay Cosmetics, MAC Cosmetics and M.A.C., BeneFit's two entries, and La Mer's two entries.
5. **Cutoff:** the top 30 after rules 1–4. Row 30, Mary Kay (41%, fame 87), and row 31, Clean & Clear (41%, fame 66), tie on popularity, and fame puts Mary Kay in. Rows 31–35 would be Clean & Clear (41%), MAC (40%), Proactiv (39%), Redken (39%) and Fenty (39%).

**Limits:**
- Popularity is not sales. It favours old mass brands and penalises young brands that fewer people have heard of, which is where the earlier scan found most of beauty's PE (L Catterton, VMG and others).
- The scope line for body lotion and sun care changes the count (see "Category share").
- The scan's PE brands that are absent from these lists are not rows. Olaplex (B #23, 27%) and Anastasia Beverly Hills (A #91, 25%) are in the lists but fall below the cutoff.

| # | Brand (YouGov list, rank, fame / popularity) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Burt's Bees (C #30, 86/65) | The Clorox Company | public company | none (13Gs all 13d-1(b)) | not checked | CLX | brand of a consumer-products company | none found | BE1 |
| 2 | Neutrogena (A #3, 95/64) | Kimberly-Clark (Kenvue purchase closed 2026-11-02) | public company | none (13Gs all 13d-1(b)) | 2026-11-02 | KMB | brand of a consumer-products company | network listing only (CJ/FlexOffers per directories); neutrogena.com 403 | BE2 |
| 3 | Olay (A #5, 94/62) | Procter & Gamble | public company | none | not checked | PG | brand of a consumer-products company | network listing only (FlexOffers; one directory says closed); olay.com runs a customer referral program, not an affiliate program | BE3 |
| 4 | Head & Shoulders (B #1, 97/61) | Procter & Gamble | public company | none | not checked | PG | as row 3 | none found | BE4 |
| 5 | **Suave** (C #41, 92/61) | Evermark, LLC (merger of Suave Brands Company and Elida Beauty), a Yellow Wood Partners portfolio company; North America only, Unilever elsewhere | **PE-owned** (no stated stake) | Yellow Wood Partners | 2023-05-09 (Suave Brands Company); Evermark 2026-01-20 | — | brand of a PE-owned consumer-products company | none found | BE5 |
| 6 | CeraVe (A #6, 85/61) | L'Oréal (Dermatological Beauty Division) | public company (foreign-listed: Euronext Paris); Bettencourt Meyers family 34.79%, Nestlé 20.16% | none | not checked | OR (Euronext Paris) | brand of a consumer-products company | none found (GRIN: no open enrollment) | BE6 |
| 7 | Aveeno (A #8, 84/59) | Kimberly-Clark (via Kenvue) | public company | none | 2026-11-02 | KMB | as row 2 | none found | BE7 |
| 8 | Nivea (A #9, 86/58) | Beiersdorf AG; maxingvest group 54.4% | public company (foreign-listed: Frankfurt), majority holder a holding company | none | not checked | BEI (Frankfurt; not read from a filing) | brand of a consumer-products company | none found | BE8 |
| 9 | L'Oréal Paris (A #14, 88/57) | L'Oréal (Consumer Products Division) | public company (foreign-listed) | none | not checked | OR | as row 6 | none found (lorealparisusa.com's own terms mention Amazon Associates, which is the brand acting as an affiliate, not running a program) | BE9 |
| 10 | Cetaphil (A #16, 84/55) | Galderma Group AG; EQT fully exited 2026-03-13 | public company (foreign-listed: SIX) | none now (EQT, 2019 to 2026-03-13) | not checked | GALD (SIX) | brand of a dermatology company | none found | BE10 |
| 11 | **Revlon** (A #17, 89/54) | Revlon Group Holdings LLC; majority owned by former lenders, among them affiliates of Angelo, Gordon & Co. | **PE-owned** (no stated stake per named lender; together a majority) | Angelo, Gordon & Co. (TPG Angelo Gordon) | 2023-05-02 | — | brand of a lender-owned consumer-products company | none found (India-only network listing, reported paused) | BE11 |
| 12 | Pantene (B #2, 88/54) | Procter & Gamble | public company | none | not checked | PG | as row 3 | none found | BE12 |
| 13 | Maybelline (A #19, 90/53) | L'Oréal (Consumer Products Division) | public company (foreign-listed) | none | not checked | OR | as row 6 | none found | BE13 |
| 14 | **CoverGirl** (A #25, 90/50) | Coty Inc. (owned brand); JAB Beauty B.V. majority stockholder, JAB group about 54% of votes | **PE-owned** (public company with a PE holder over 50% of votes) | JAB (JAB Consumer Fund Management SARL reports PE funds) | JAB tender 2019-04-30 | COTY | brand of a public consumer-products company | none found (GRIN: no open enrollment) | BE14 |
| 15 | Clearasil (A #26, 86/50) | Reckitt (listed on Reckitt's US brand page) | public company (foreign-listed: London; ticker not read from a filing) | none found | not checked | — (LSE) | brand of a consumer-health company | none found | BE15 |
| 16 | Estée Lauder (A #28, 81/50) | The Estée Lauder Companies Inc.; LAL Family Corporation 49.8% of votes, plus other Lauder holdings | public company, family-controlled votes | none (5%+ holders BlackRock, Managed Account Advisors, Vanguard) | not checked | EL | brand of a public prestige-beauty company | network listing only (Rakuten per directories); esteelauder.com 403 | BE16 |
| 17 | Eucerin (A #27, 73/50) | Beiersdorf AG | as row 8 | none | not checked | BEI | as row 8 | none found | BE17 |
| 18 | Herbal Essences (B #3, 86/49) | Procter & Gamble | public company | none | not checked | PG | as row 3 | none found | BE18 |
| 19 | **St. Ives** (A #29, 78/49) | Evermark, LLC (Yellow Wood) for North America and Europe; Unilever elsewhere | **PE-owned** (US owner; no stated stake) | Yellow Wood Partners | 2024-06-06 (Elida Beauty); Evermark 2026-01-20 | — | as row 5 | none found | BE19 |
| 20 | Clinique (A #31, 82/48) | The Estée Lauder Companies Inc. | as row 16 | none | not checked | EL | as row 16 | network listing only (Rakuten/FlexOffers per directories) | BE20 |
| 21 | Avon (A #32, 82/47) | The Avon Company (Avon North America); LG H&H agreed 2026-08-24 to sell to Regent, closing "expected" 2026-09-01 (closing not confirmed from a primary source) | not PE under the rules: Regent has no Form ADV and calls itself "a privately held global investment firm" and "a global holding company"; LG H&H is public (KRX) | none under the rules | 2026-09-01 (expected) | — (seller LG H&H: KRX 051900) | direct seller (Ambassadors) plus online | **probable, brand-direct**: avon.com "Affiliates" page found in search (program through CJ, up to 10%); avon.com returned 403 | BE21 |
| 22 | Garnier (B #6, 76/44; Fructis 74/45) | L'Oréal (Consumer Products Division) | public company (foreign-listed) | none | not checked | OR | as row 6 | none found | BE22 |
| 23 | Paul Mitchell (B #7, 75/44) | John Paul Mitchell Systems: "the largest family-owned pro hair care brand" | family | none found | not applicable (founded 1980) | — | pro hair care sold through salons | none found | BE23 |
| 24 | Lancôme (A #34, 73/44) | L'Oréal (Luxe Division) | public company (foreign-listed) | none | not checked | OR | as row 6 | network listing only (Awin per directories); lancome-usa.com challenge page, not retried | BE24 |
| 25 | TRESemmé (B #8, 82/43) | Unilever PLC (a Beauty & Wellbeing "Power Brand") | public company | none (no 13D since 2018; 13Gs 13d-1(b)) | not checked | UL (NYSE ADS) | brand of a consumer-products company | none found | BE25 |
| 26 | **Clairol** (C #74, 74/43; Nice 'n Easy 61/34) | Wella Company (Rainbow JVCo Limited); KKR affiliates bought the majority, then Coty's last 25.8% on 2025-12-18 | **PE-owned** | KKR | majority 2020 (date not read); remaining stake 2025-12-18 | — | brand of a PE-owned hair company | none found (a Wella professional store runs a stylist program; not opened, not brand-direct) | BE26 |
| 27 | e.l.f. Cosmetics (A #35, 71/43) | e.l.f. Beauty, Inc. | public company | none (Baillie Gifford 11.86% on a 13G filed under Rule 13d-1(b)) | not checked | ELF | brand of a public beauty company | network listing only (Rakuten/FlexOffers per directories) | BE27 |
| 28 | **Sally Hansen** (A #36, 68/42) | Coty Inc. (owned brand) | **PE-owned** (as row 14) | JAB | 2019-04-30 (JAB tender) | COTY | as row 14 | none found | BE28 |
| 29 | SheaMoisture (A #37, 61/42) | Unilever (major brand, 2024 prospectus); Sundial Brands, LLC a Unilever group company (2025 20-F) | public company | none | not checked | UL | as row 25 | none found (sheamoisture.com 403) | BE29 |
| 30 | Mary Kay (A #38–39, 87/41) | not found (site unavailable to the bot) | not found (trade press: privately held, founder's family; not cited) | none found | not found | — | direct seller (independent beauty consultants) | none found (direct-selling model) | BE30 |

### Evidence
Page numbers are the saved files in `pages/beauty/` (`NNN.txt`). All pages were accessed 2026-11-17.

- **BE1 Burt's Bees**
  - Owner: "and Burt’s Bees® natural personal care products." and "Common Stock – $1.00 par value CLX New York Stock Exchange" — [Clorox 10-K FY2026](https://www.sec.gov/Archives/edgar/data/21076/000002107626000034/clx-20260630.htm) (031)
  - Holders: EDGAR filing list re-read (042): no 13D. Four 13G filers since 2025-11, all covered by the earlier screen's 13d-1(b) check.
  - BDC names: "The Clorox Company", "Burt's Bees, Inc."
- **BE2 Neutrogena**
  - Owner: "(NASDAQ: KMB), a core S&P 500 component, today announced that it has completed its acquisition of Kenvue." and "includes 10 billion-dollar brands: Huggies, Listerine, Cottonelle, Neutrogena, Depend, Tylenol, Kleenex, Johnson’s Baby, Kotex and Scott." — [Kimberly-Clark 8-K ex. 99.1, 2026-11-02](https://www.sec.gov/Archives/edgar/data/55785/000110465926120990/tm2628636d1_ex99-1.htm) (032)
  - Brand: "Major brands in the segment include Aveeno®, Dr.Ci:Labo®, Le Petit Marseillais®, Lubriderm®, Neutrogena®, OGX®, and Rogaine®." — [Kenvue 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1944048/000194404826000030/kvue-20251228.htm) (033)
  - Holders: K-C filing list (044): no 13D. Its 13G filers (Vanguard, BlackRock, FMR, State Street) are 13d-1(b) per the earlier screen.
  - Affiliate: directories list CJ and FlexOffers programs (not opened). neutrogena.com returned 403.
- **BE3 Olay / BE4 Head & Shoulders / BE12 Pantene / BE18 Herbal Essences**
  - Owner: "Skin Care (Facial Moisturizers, Cleaners and Treatments) Olay, SK-II"; "Hair Care (Conditioners, Shampoos, Styling Aids, Treatments) Head & Shoulders, Herbal Essences, Pantene, Rejoice"; "P&G trades on the New York Stock Exchange under the stock symbol PG." — [P&G 10-K FY2026](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm) (030)
  - Holders: P&G filing list (041): no 13D. Two 13G filers since 2025-11.
  - Affiliate: olay.com's homepage (080) has no affiliate link. Domain search found only "Referral Program" and "Give $10, Get $10 with Refer a Friend", which are customer referral programs.
- **BE5 Suave (PE)**
  - Acquisition: "has completed the previously announced acquisition of the beauty and personal care brand, Suave, in North America from Unilever (NYSE: UL)." — [Yellow Wood release, 2023-05-09](https://yellowwoodpartners.com/news-article/yellow-wood-partners-completes-acquisition-of-suave-north-american-beauty-and-personal-care-brands-from-unilever) (019)
  - Current: "today announced that they have completed a merger to create Evermark, LLC ("Evermark" or the "Company"), a leading global platform of iconic personal care brands. Both businesses are portfolio companies of Yellow Wood Partners ("Yellow Wood")" and "including Suave, the top U.S. wash and care brand by volume" — [Yellow Wood release, 2026-01-20](https://yellowwoodpartners.com/news-article/yellow-wood-partners-portfolio-companies-suave-brands-and-elida-beauty-complete-merger-to-create-evermark-a-leading-global-platform-of-personal-care-brands) (018)
  - Footer: "© 2026 Evermark, LLC. All rights reserved." — [suave.com](https://www.suave.com/) (071)
  - Seller: "2023 includes a gain of €497 million related to the disposal of Suave." — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm) (034)
  - Owner kind: "a Boston-based private equity firm focused on investing in consumer brands and companies" (012). Form ADV: Yellow Wood Partners LLC, `Any PE Funds = Y`, 10 PE funds.
  - BDC names: "Suave Silk Holdings III Corp." and "Suave Silk Holdings I Corp." (both found; see "BDC names"), "Evermark, LLC", "Suave Brands Company".
  - Notes: no stake is stated, so the hop counts as control. Yellow Wood's Brands page (016) lists Suave and St. Ives, but its "Current/Past" filter couldn't be read from the HTML.
- **BE6 CeraVe / BE9 L'Oréal Paris / BE13 Maybelline / BE22 Garnier / BE24 Lancôme**
  - Brands:
    - "Dermatological Beauty Division La Roche-Posay Skinbetter Science Vichy CeraVe SkinCeuticals" — [L'Oréal, Dermatological Beauty Division](https://www.loreal.com/en/dermatological-beauty-division/) (046)
    - "Consumer Products Division Dr.G L'Oréal Paris Thayers Vogue Garnier Maybelline New York NYX Professional Makeup" — [L'Oréal, Consumer Products Division](https://www.loreal.com/en/consumer-products-division/) (045)
    - "Luxe Division Lancôme Yves Saint Laurent Armani Valentino" — [L'Oréal, Luxe Division](https://www.loreal.com/en/luxe-division/) (047)
  - Owners: "Françoise Bettencourt Meyers and her family(1) 185,715,079 34.79 34.79(2)" and "Nestlé(3) 107,621,021 20.16 20.16" — [L'Oréal 2025 URD, 7.3 Ownership structure](https://www.loreal-finance.com/eng/2025-universal-registration-document/en/article/396/) (048)
  - Notes: L'Oréal isn't an SEC filer, so 13D rules don't apply and no PE holder appears in the table. The earlier screen's quote "L'Oréal Paris, the No.1 beauty brand in the world" is no longer on the division page, so the menu text is cited instead.
- **BE7 Aveeno:** the Kenvue 10-K quote under BE2 plus the K-C closing release.
- **BE8 Nivea / BE17 Eucerin**
  - Brand: "NIVEA is part of Beiersdorf AG, a skin care company based in Hamb" (the page text cuts the word) — [Beiersdorf, NIVEA](https://www.beiersdorf.com/brands/nivea) (049). "Eucerin is part of Beiersdorf AG, a global skin care company based in Hamburg, Germany" — [Beiersdorf, Eucerin](https://www.beiersdorf.com/brands/eucerin) (050)
  - Owner: "Maxingvest Group: 54.4% Free Float: 36.4% Beiersdorf AG: 9.2%" — [Beiersdorf, Shareholder structure](https://www.beiersdorf.com/investor-relations/shares/shareholder-structure) (051)
  - Notes: maxingvest isn't in either Form ADV file. Its owners weren't read; trade press says the Herz family (not cited).
- **BE10 Cetaphil**
  - Brand: "CETAPHIL is a gentle skincare brand that has been recommended by dermatologists1 for over 70 years" — [Galderma, Cetaphil](https://www.galderma.com/cetaphil) (053)
  - Former PE: "EQT completes final sell-down in Galderma"; "in Galderma Group AG (SIX: GALD) (“Galderma”)"; "EQT Private Equity, together with a consortium of co-investors, carved out Galderma from Nestlé in October 2019" — [EQT release, 2026-03-13](https://eqtgroup.com/news/eqt-exits-galderma-group-ag-in-full-via-largest-sponsor-backed-block-trade-ever-2026-03-13) (052)
  - Notes:
    - Formerly PE-owned (2019 to 2026-03-13). Galderma is public on SIX with no PE holder found.
    - Trade press says L'Oréal now holds 20%, after buying 10% from the EQT group in December 2025 (not cited).
    - EQT's Form ADV: EQT Fund Management S.à r.l. `Y` (58 PE funds).
- **BE11 Revlon (PE)**
  - Owner: "The newly reorganized company is named "Revlon Group Holdings LLC.”" and "The majority of the Company’s reorganized equity is now owned by its former lenders, including affiliates of Glendon Capital Management LP, King Street Capital Management, L.P., Angelo, Gordon & Co., L.P., Antara Capital LP, Nut Tree Capital Management, LP, Oak Hill Advisors, L.P., and Cyrus Capital Partners, LP, among others." — [Revlon release "Revlon Emerges from Chapter 11 Reorganization", 2023-05-02, Business Wire copy on StreetInsider](https://www.streetinsider.com/Business+Wire/Revlon+Emerges+from+Chapter+11+Reorganization/21596627.html) (024; Business Wire itself returned 403)
  - Footer: "© 2026 Revlon US." — [revlon.com](https://www.revlon.com/) (066)
  - Form ADV:
    - Angelo, Gordon & Co., L.P. (TPG Angelo Gordon) `Y` (32 PE funds).
    - `N`: Glendon, King Street, Oak Hill Advisors, Nut Tree, Cyrus.
    - Not found: Antara Capital LP.
  - Notes:
    - Each named lender's stake is unstated, and together they hold a majority. Under the "no stated stake" rule the Angelo Gordon hop counts as control, as the Gabe's and Cano lender groups were counted.
    - The release is dated 2023-05-02. No newer primary document naming the owners was found, so under the 18-month rule the hop would read "last confirmed 2023-05-02" (Open questions).
    - Trade press also names Ares and Oak Hill among the 2022 lender group. Ares isn't in the release, so it isn't counted.
  - BDC names: "Revlon Group Holdings LLC", "Revlon Consumer Products Corporation", "Revlon Intermediate Holdings". None was found in the data sets.
- **BE14 CoverGirl / BE28 Sally Hansen (PE)**
  - Brands: "CoverGirl* Etro Jovan* Gucci" … "Sally Hansen* Tiffany & Co. Vera Wang * Indicates an owned beauty brand." — [Coty 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm) (026)
  - Majority holder: "our relationship with JAB Beauty B.V., as our majority stockholder" (026). "JAB Beauty B.V. 451,853,684 (2)(4)(5) 51.3 (2)(4)(5)" and "as of September 10, 2026, JAB Group owns approximately 54% (inclusive, pursuant to a proxy agreement, of all voting interests of Mr. Harf" — [Coty DEF 14A, 2026-09-24](https://www.sec.gov/Archives/edgar/data/1024305/000102430526000060/coty-20260924.htm) (027)
  - Footers: "© Copyright 2026 Coty Inc. All right reserved" — [covergirl.com](https://www.covergirl.com/) (067). "© Sally Hansen 2026" — [sallyhansen.com](https://www.sallyhansen.com/en-us) (070)
  - Form ADV: JAB Consumer Fund Management SARL `Y` (10 PE funds). JAB Capital Management, LLC `N`. ADR 0001 names JAB among firms that report PE funds.
  - Voting arithmetic: "Holders of the Series B Preferred Stock are entitled to vote with the holders of the Class A Common Stock on an “as converted” basis" and "On the Record Date, there were 880,686,464 shares of Class A Common Stock issued and outstanding and 146,057 shares of Series B Preferred Stock issued and outstanding." (027) The proxy puts the Series B at about 23,818,730 Class A equivalents. So JAB Beauty's own 451,853,684 shares are 51.3% of Class A but 49.96% of all votes, and about 54% with Mr. Harf's proxy (Open questions).
  - Pending: the strategic review of the consumer beauty business (mass color brands) has run since September 2025. The 8-Ks of 2026-11-04 (results) and 2026-11-05 (annual meeting) announced no deal (028, 029).
  - BDC names: "Coty Inc.", "Coty B.V.". Not found.
- **BE15 Clearasil**
  - Brand: "Our Brands Airborne Clearasil Durex K-Y Move Free Nutramigen" — [Reckitt US](https://www.reckitt.com/us/) (054)
  - Notes: Reckitt is listed in London and isn't an SEC 13D subject. Its holders weren't read. Trade press reported a 2020 plan to sell Clearasil, but no sale was found, and the 2026 page still lists the brand.
- **BE16 Estée Lauder / BE20 Clinique**
  - Brands: "Since the initial launch of the Estée Lauder brand in the United States" and "Introduced in 1968, Clinique skin care and makeup products are all allergy tested and 100% fragrance free"; "Class A Common Stock, $.01 par value EL New York Stock Exchange" — [Estée Lauder 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1001250/000100125026000041/el-20260630.htm) (059)
  - Holders:
    - The beneficial-ownership table lists "LAL Family Corporation(3)(4)" at 49.8% of voting power. Lauder family members (William, Aerin, Jane) hold more Class B. The other 5%+ holders are BlackRock (7.5%), Managed Account Advisors LLC (7.5%; ADV `N`) and Vanguard Portfolio Management (5.0%) — [Estée Lauder DEF 14A, 2026-09-30](https://www.sec.gov/Archives/edgar/data/1001250/000110465926112176/tm2623505-1_def14a.htm) (037)
    - The latest 13D/A (2026-09-18) was filed by "Trust Under Article 2 of The Zinterhofer 2008 Descendants Trust Agreement", a family trust (039).
  - Notes: Eric Zinterhofer, a director, is a PE founder (Searchlight). His Class B shares are shared with Aerin Lauder, so they are family holdings, not a PE fund's.
- **BE19 St. Ives (PE)**
  - Owner: "today announced that it has completed the acquisition of Elida Beauty brands from Unilever (NYSE: UL). The Elida Beauty portfolio of storied consumer brands includes Q-tips®, Caress, Ponds and St. Ives (for North America and Europe only), Impulse, Noxzema, Monsavon, and Timotei, among others." — [Yellow Wood release, 2024-06-06](https://yellowwoodpartners.com/news-article/yellow-wood-partners-completes-acquisition-of-elida-beauty-from-unilever) (012)
  - Territory: "The transaction perimeter excludes the Pond's and St. Ives brands sold beyond North America and Europe which will remain in Unilever's Beauty & Wellbeing brand portfolio." — [Yellow Wood release, 2023-12-18](https://yellowwoodpartners.com/news-article/yellow-wood-partners-announces-acquisition-of-elida-beauty-from-unilever) (013)
  - Current: "as well as Pond's, Caress, St. Ives, Noxzema and TIGI" (018, Evermark release). "© 2026 Evermark, LLC. All rights reserved. This website is directed only to U.S. consumers for products and services of Evermark, LLC." — [stives.com](https://www.stives.com/) (072)
  - Seller: "2024 net loss related to the disposals of our Russian business, Elida Beauty, Pureit and Qinyuan." (034)
  - Notes: Unilever's 2025 20-F still lists "St. Ives Laboratories, Inc." as a group company, consistent with Unilever keeping St. Ives outside North America and Europe.
- **BE21 Avon**
  - Deal: "today announced that it has entered into a definitive agreement with Regent, the global investment firm founded by investor Michael A. Reinstein, as part of its ongoing global portfolio optimization to sell its interest in The Avon Company ("Avon North America")." and "The transaction is expected to close on September 1st." — [LG H&H / The Avon Company release, 2026-08-24](https://www.prnewswire.com/news-releases/regent-to-acquire-avon-north-america-reuniting-major-avon-businesses-after-more-than-a-decade-apart-302857829.html) (020)
  - Owner kind: "Regent is a privately held global investment firm headquartered in Beverly Hills, California" (020). "Regent is a global holding company with investments across the consumer, technology, media, automotive and industrial sectors." — [Natura release, 2025-09-18](https://www.prnewswire.com/news-releases/natura-announces-agreement-to-sell-avon-international-and-reinforces-focus-on-latin-america-302560532.html) (021)
  - Brand rights: "The intellectual property rights and the management of the Avon brand in Latin America remain under Natura's control." (021)
  - Form ADV: no Regent adviser. The only matches are unrelated firms named Regent (Regent Peak Wealth, Regent Properties and others).
  - Notes:
    - Regent's own site (regentco.com) disallows ClaudeBot and wasn't fetched. avon.com returned 403.
    - The closing date comes only from a law firm's deal note (not cited). Avon isn't PE under either owner: LG H&H is public, and Regent has no ADV and doesn't call itself PE in the two documents read.
    - Who owns the Avon trademark in the US wasn't found.
  - Affiliate: the search result shows an avon.com page titled "Affiliates" ("earn a commission up to 10% while supporting Avon Ambassadors when you join Avon's Affiliate Program through CJ's Network"). That is a search snippet, not cited text, and the page returned 403. Probable.
- **BE23 Paul Mitchell**
  - Owner: "As the largest family-owned pro hair care brand, 45 years and counting" and "It was 1980 when hairstylist Paul Mitchell and businessman John Paul DeJoria teamed up to start a beauty company" — [Paul Mitchell, Our Story](https://www.paulmitchell.com/pages/our-story) (057). The site footer names "John Paul Mitchell Systems" (055).
- **BE25 TRESemmé**
  - Owner: "Our Power Brands: Clear Dermalogica Dove Hourglass K18 Liquid I.V. Nexxus Nutrafol OLLY Paula’s Choice Pond’s Sunsilk TRESemmé Vaseline"; "Unilever’s shares are also traded on the New York Stock Exchange (UL) in the form of American Depositary Shares" — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm) (034)
  - Holders: Unilever filing list (043): the last 13D is a 2018 13D/A (the Leverhulme Trust, per the earlier screen). One 13G since 2025-11.
- **BE26 Clairol (PE)**
  - Owner: "following the sale of a majority stake in our Professional and Retail Hair business, including the Wella, Clairol, OPI and ghd brands" and "On December 18, 2025, the Company completed the sale of its remaining 25.8% equity interest in Wella to an entity affiliated with Kohlberg Kravis Roberts & Co. L.P. ("KKR")." — [Coty 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm) (026)
  - Footer: "© 2026 Wella Operations US LLC, all trademarks registered." — [clairol.com](https://www.clairol.com/en-US) (074)
  - Form ADV: Kohlberg Kravis Roberts & Co. L.P. `Y` (553 PE funds).
  - Notes:
    - The 2020 date of the majority sale wasn't read from a primary source.
    - The 10-K names the buyer vehicle as "Tides Holdco Limited" (exhibit list). Whether investors other than KKR hold part of Wella isn't stated.
- **BE27 e.l.f. Cosmetics**
  - Owner: "Our family of brands consists of e.l.f. Cosmetics, e.l.f. SKIN, rhode, Naturium and Well People." and "Common Stock, $0.01 par value ELF New York Stock Exchange" — [e.l.f. Beauty 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1600033/000160003326000020/elf-20260331.htm) (060)
  - Holders: "Baillie Gifford & Co.(2) 7,349,678 12.5 %" (BlackRock 8.6%, Vanguard Capital Management 5.1%) — [e.l.f. DEF 14A, 2026-07-08](https://www.sec.gov/Archives/edgar/data/1600033/000160003326000030/elf-20260706.htm) (038)
  - Baillie Gifford's latest 13G/A shows "11 Percent of class represented by amount in row (9) 11.9 %". Its raw HTML marks "Rule 13d-1(b)" with the image alt text "Checkbox checked" — [13G/A, 2026-08-04](https://www.sec.gov/Archives/edgar/data/1600033/000108887526000053/xslSCHEDULE_13G_X02/primary_doc.xml) (040)
  - Form ADV: Baillie Gifford International LLC `Y` (7 PE funds), so the firm counts as PE, but its stake is passive under 13d-1(b).
- **BE29 SheaMoisture**
  - Owner: "Major brands include Dove, Living Proof, Nexxus, TRESemmé, SheaMoisture, Vaseline" — [Unilever 424B5, 2024-08-08](https://www.sec.gov/Archives/edgar/data/217410/000110465924087130/tm2420521-2_424b5.htm) (065, found through EDGAR full-text search, 064). "Sundial Brands, LLC" is listed among Unilever group companies in the 2025 20-F (034).
  - Notes: sheamoisture.com and unilever.com returned 403. The 2025 20-F doesn't name SheaMoisture.
- **BE30 Mary Kay**
  - Owner: not found. www.marykay.com served a splash frame whose page reads "Mary Kay Inc. | Site Unavailable" (056, 058).
  - Notes: trade press and Wikipedia describe a privately held company led by the founder's family (Rogers). Not cited.

### Groups that are not brands
Not counted in the 30.
- **Procter & Gamble** (PG): Olay, Head & Shoulders, Pantene, Herbal Essences.
- **L'Oréal** (Euronext Paris, family 34.79%, Nestlé 20.16%): CeraVe, L'Oréal Paris, Maybelline, Garnier, Lancôme.
- **Kimberly-Clark** (KMB; Kenvue closed 2026-11-02): Neutrogena, Aveeno, and Clean & Clear (row 31).
- **Beiersdorf** (maxingvest 54.4%): Nivea, Eucerin.
- **The Estée Lauder Companies** (EL; Lauder family votes): Estée Lauder, Clinique.
- **Coty Inc.** (COTY; JAB group about 54% of votes): CoverGirl, Sally Hansen. Kylie Cosmetics (C #102) is below the cutoff.
- **Unilever** (UL): TRESemmé, SheaMoisture, and St. Ives outside North America and Europe.
- **Evermark, LLC** (Yellow Wood Partners): Suave, St. Ives (North America and Europe).
- **Wella Company / Rainbow JVCo Limited** (KKR): Clairol, plus Nice 'n Easy and Natural Instincts as Clairol lines. OPI (A #54) is below the cutoff.
- **Revlon Group Holdings LLC** (former lenders): Revlon. Elizabeth Arden (A #48) and Almay (A #68) are below the cutoff.
- **Galderma** (SIX: GALD): Cetaphil. **Reckitt**: Clearasil. **Clorox** (CLX): Burt's Bees. **e.l.f. Beauty** (ELF): e.l.f.
- **The Avon Company** (Regent, per the agreement): Avon. **John Paul Mitchell Systems** (family): Paul Mitchell.

### Category share
**All rows (N = 30, all ranked).**
- **PE-owned: 6 / 30 = 20.0%.**
  - Suave: Yellow Wood via Evermark, no stated stake.
  - St. Ives: Yellow Wood via Evermark, for North America and Europe.
  - Revlon: lender group including Angelo Gordon, no stated stake.
  - CoverGirl and Sally Hansen: Coty, with the JAB group at about 54% of votes.
  - Clairol: Wella, held by KKR.
- **PE minority stake: 0.** PE-owned plus minority = **6 / 30 = 20.0%.**
- **Public company: 21 / 30 = 70.0%.**
  - P&G 4; L'Oréal 5; Kimberly-Clark 2; Beiersdorf 2; Estée Lauder 2 (votes family-controlled); Unilever 2; Clorox, Galderma, Reckitt and e.l.f. Beauty 1 each.
- **Family: 1 / 30**: Paul Mitchell.
- **Owner kind not confirmed: 1 / 30**: Avon. The Avon Company was sold by LG H&H, which is public, to Regent, which has no ADV and calls itself an investment firm or holding company. Avon isn't PE under either owner.
- **Not found: 1 / 30 = 3.3%**: Mary Kay.
- **Total:** 6 + 21 + 1 + 1 + 1 = 30.
- **Sensitivities (PE-owned plus minority):**
  - Revlon stale under the 18-month rule: 5 / 30 (16.7%).
  - JAB not counted as PE: 4 / 30 (13.3%).
  - Both of the above: 3 / 30 (10.0%).
  - Body lotion and sun care in beauty: Vaseline, Aquaphor, Coppertone, Jergens, Banana Boat, Gold Bond, Lubriderm and Hawaiian Tropic enter (each above 51%). Paul Mitchell, Lancôme, TRESemmé, Clairol, e.l.f., Sally Hansen, SheaMoisture and Mary Kay leave. Result: 4 / 30 (13.3%), assuming all eight entering brands are non-PE. Vaseline (Unilever), Gold Bond (Sanofi) and Jergens (Kao) were sourced in the earlier screen, and Lubriderm is in the Kenvue 10-K quote under BE2. Aquaphor, Coppertone, Banana Boat and Hawaiian Tropic weren't checked.
  - Wider scope plus JAB not counted: 3 / 30 (10.0%). Wider scope plus Revlon stale: 3 / 30 (10.0%). All three caveats: 2 / 30 (6.7%).
  - Suave moved to personal care: Clean & Clear enters, giving 5 / 30 (16.7%).
  - Product lines unfolded: Fructis (45%) enters and Mary Kay leaves. No change.
  - Regent counted as PE: 7 / 30 (23.3%).
- **By parent company:** 16 parents (P&G, L'Oréal, Kimberly-Clark, Beiersdorf, Estée Lauder, Unilever, Coty, Evermark, Wella, Revlon, Galderma, Reckitt, Clorox, e.l.f. Beauty, Avon, John Paul Mitchell Systems), plus Mary Kay counted as its own parent, for 17. PE-held parents: 4 / 17 = 23.5% (Coty, Evermark, Wella, Revlon).
- **By popularity:** the six PE rows average 49.8% popularity, against 51.4% for all 30, and sit at ranks 5, 11, 14, 19, 26 and 28.
- **Sources disagree:** none on owners. Framing notes:
  - Suave and St. Ives are split by territory (Unilever outside North America, and outside North America and Europe).
  - Avon's closing is unconfirmed in primary sources.
  - Coty's 54% voting figure includes a proxy over Mr. Harf's votes.

**Affiliate income (brand-direct):**
- **Confirmed:** 0.
- **Probable:** 1 (Avon, non-PE).
- **Network listings only:** 6, all non-PE (e.l.f., Clinique, Estée Lauder, Lancôme, Neutrogena, Olay).
- **PE rows:** 0 brand-direct. Revlon has an India-only network listing that one directory says is paused.
- Brand sites checked for an affiliate link: 20. Five failed (Estée Lauder, Lancôme, Neutrogena, SheaMoisture and Avon, all 403). None of the 15 that loaded had one: Revlon, CoverGirl, Sally Hansen, Suave, St. Ives, Clairol, e.l.f., Clinique, Burt's Bees, Olay, CeraVe, Maybelline, L'Oréal Paris, Garnier and Paul Mitchell. Some footers may be script-rendered.
- Domain-restricted searches across all 30 brand domains found only avon.com's page, plus customer referral and loyalty programs (Olay, e.l.f. Beauty Squad, Clinique+).
- So, unlike cookware (10 brand-direct programs), the big beauty brands in this list run affiliate programs, if at all, through networks or retailers.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it:
- **Yellow Wood Partners**: "Yellow Wood Partners LLC" (Suave, St. Ives; Evermark, LLC)
- **KKR**: "Kohlberg Kravis Roberts & Co. L.P." ("KKR"); vehicles "Rainbow JVCO LTD", "Tides Holdco Limited", "KKR Bidco" (Clairol / Wella)
- **JAB**: "JAB Beauty B.V." (formerly "Cottage Holdco B.V."), "JAB Holdings B.V.", "JAB Group"; above them "Agnaten SE" and "Lucresca SE" (Coty)
- **Revlon's former lenders**: "Glendon Capital Management LP", "King Street Capital Management, L.P.", "Angelo, Gordon & Co., L.P.", "Antara Capital LP", "Nut Tree Capital Management, LP", "Oak Hill Advisors, L.P.", "Cyrus Capital Partners, LP"
- **Regent** (Avon): "Regent, the global investment firm founded by investor Michael A. Reinstein"
- **EQT** (former Galderma owner): "Sunshine SwissCo GmbH, an affiliate of the EQT VIII fund", "EQT Private Equity"
- 5%+ holders of public rows:
  - **Coty**: JAB Beauty B.V.; BlackRock, Inc. (6.40%); HFS Holdings S.à r.l. (Series B preferred, Mr. Harf).
  - **Estée Lauder**: LAL Family Corporation and Lauder family members; BlackRock, Inc.; Managed Account Advisors LLC; Vanguard Portfolio Management.
  - **e.l.f. Beauty**: Baillie Gifford & Co.; BlackRock, Inc.; Vanguard Capital Management LLC.
- Leads only, from trade press (not cited, not counted): Ares Management and Oak Hill (2022 Revlon lender group); L'Oréal's 20% of Galderma; the Herz family behind maxingvest; the Rogers family behind Mary Kay; TPG at Anastasia Beverly Hills (below the cutoff).

## Form ADV results
From the November 2026 monthly files (registered and exempt):

| Firm (as matched) | CRD | File | Any PE Funds | PE funds | Counts as PE? |
|---|---|---|---|---|---|
| Yellow Wood Partners LLC | 161062 | registered | Y | 10 | yes |
| Kohlberg Kravis Roberts & Co. L.P. | 144533 | registered | Y | 553 | yes |
| JAB Consumer Fund Management SARL | 299567 | exempt | Y | 10 | yes (firm: JAB) |
| JAB Capital Management, LLC | 320809 | exempt | N | — | (same firm; Y elsewhere) |
| Angelo, Gordon & Co., L.P. (TPG Angelo Gordon) | 131940 | registered | Y | 32 | yes |
| Glendon Capital Management L.P. | 166119 | registered | N | — | no |
| King Street Capital Management, L.P. | 156785 | registered | N | — | no |
| Oak Hill Advisors, L.P. | 125352 | registered | N | — | no |
| Cyrus Capital Partners, L.P. | 136713 | registered | N | — | no |
| Nut Tree Capital Management, LP | 282219 | registered | N | — | no |
| Antara Capital LP | not found | — | — | — | no evidence |
| Regent (regentco.com) | not found | — | — | — | no (no PE self-description found) |
| EQT Fund Management S.à r.l. | 288390 | exempt | Y | 58 | yes (exited Galderma) |
| Baillie Gifford International LLC | 305849 | registered | Y | 7 | yes as a firm; its e.l.f. stake is 13d-1(b) passive |
| Baillie Gifford Overseas Ltd; Baillie Gifford & Co Limited | 110296; 304197 | registered; exempt | N | — | (same firm) |
| Managed Account Advisors LLC | 142558 | registered | N | — | no |
| maxingvest | not found | — | — | — | no |

## BDC names
SEC BDC data sets for 2026-07 to 2026-10 were scanned for each row's brand, owner and vehicle names (`scripts/beauty/bdc.py`).
- **Found: Suave**, through the borrower name "Suave Silk Holdings III Corp." (industry label "Personal Care Products"):
  - Apollo Debt Solutions BDC: first-lien term loan with $210.0M principal on 2026-06-30 ($213.9M on 2025-12-31), plus a revolver; S+450, maturity 2032-12-03.
  - Apollo Origination II (UL) Capital Trust and Apollo Origination II (Levered) Capital Trust: term loans and revolvers.
  - MidCap Apollo Institutional Private Lending: term loan of $9.2M.
  - MidCap Financial Investment Corp: term loan of $25.0M, plus "Suave Silk Holdings I Corp. Common Equity - Common Stock". This is BDC-held equity, which doesn't count.
  - The tie to the brand is the brand name in the borrower name. No filer text names Evermark.
- **Not found:** Revlon, Coty, Wella/Rainbow JVCo/Tides Holdco, Clairol, CoverGirl, Sally Hansen, Evermark, Elida, St. Ives, Avon, Paul Mitchell, Mary Kay, e.l.f., and every public owner. Regent matches are unrelated (Regent Education, Regent Craft, Regent Surgical Health).

## Licensed rows
- **None of the 30 is a licensed name.** Every row's source names a brand owner, and Coty's 10-K marks CoverGirl and Sally Hansen with "* Indicates an owned beauty brand."
- **Territory splits** (one name, different owners by region):
  - St. Ives: Evermark in North America and Europe, Unilever elsewhere.
  - Suave: Evermark in North America, Unilever elsewhere.
  - Avon: The Avon Company in North America; "intellectual property rights and the management of the Avon brand in Latin America remain under Natura's control"; Regent's Avon International in Europe, Asia, Africa and the Middle East.
  - The US owner is used for each row. Who holds the US Avon trademark wasn't found.

## Surprises
- **Suave and St. Ives are no longer Unilever's in the US.** Both sit in Evermark, LLC, a Yellow Wood portfolio company formed 2026-01-20.
- **Clairol is entirely outside Coty.** Coty sold its last 25.8% of Wella to a KKR affiliate on 2025-12-18.
- **Cetaphil left PE in March 2026.** EQT's "final sell-down" closed 2026-03-13.
- **Avon is reunited under Regent,** which has no Form ADV and calls itself an investment firm and a holding company. Its site blocks ClaudeBot.
- **e.l.f.'s largest holder, Baillie Gifford, has an adviser that reports PE funds** (`Y`), but it files its 13G under Rule 13d-1(b).
- **Coty's majority is thin:** JAB's own shares are 49.96% of all votes counting the Series B preferred, 51.3% of Class A, and about 54% with Mr. Harf's proxy.
- **BDC overlap:** an Apollo-led loan of more than $210M to "Suave Silk Holdings III Corp.", plus BDC-held common equity in its parent.
- **No brand-direct affiliate program was confirmed** among 30 mass and prestige beauty brands. Cookware had 10.

## Open questions for the developer (numbers only, nothing decided)
1. **JAB (CoverGirl, Sally Hansen):** the stake sits in JAB Beauty B.V., a subsidiary of JAB Holdings B.V., which is held by Agnaten SE and Lucresca SE. The ADV `Y` is on JAB Consumer Fund Management SARL. Counted as PE: 6 / 30. Not counted: 4 / 30.
2. **Coty's "over 50% of the votes":** JAB Beauty's own shares are 51.3% of Class A and 49.96% of all votes (Series B as converted). The proxy states about 54% for the JAB group including a proxy over Mr. Harf's votes. Which figure decides control? If 49.96%, the Coty rows need a 13D-based minority instead. JAB's latest 13D/A (2025-09-03) wasn't opened.
3. **Revlon and the 18-month rule:** the only primary source naming the owners is dated 2023-05-02. Current: 6 / 30. Stale: 5 / 30.
4. **Scope line:** body lotion, sun care and the whole Dove brand were put in personal care. In beauty, the count is 4 / 30.
5. **Suave's category:** it was placed in beauty because it is hair-care led ("the top U.S. wash and care brand by volume"). In personal care, the count is 5 / 30.
6. **Product lines:** folding them into master brands changes no count. Unfolded, Fructis enters and Mary Kay leaves.
7. **Territory-split brands** (St. Ives, Suave, Avon) were counted by their US owner.
8. **Regent (Avon):** no ADV, and its own words are "privately held global investment firm" and "global holding company". A seller's 2021 headline (Ralph Lauren) calls it a PE firm. If counted: 7 / 30.
9. **YouGov paging:** the Ratings lists were completed by triggering the page's own "Load More" button by script and scrolling. Allowed under the no-clicks rule, or should future lists stop at the 20 rows served without interaction? With 20 rows per list, the composite would have reached only about 22 beauty rows.
10. **BDC tie:** "Suave Silk Holdings III Corp." counts under the brand-name-in-borrower rule. Its link to Evermark isn't stated by any filer.

## Cost
- **Time:** start 2026-11-17T22:56Z; fetches 22:58–23:25Z; report written by about 23:40Z.
- **Requests:**
  - 85 logged page fetches: 78 curl and 7 Playwright renders. Six renders were YouGov list paging, three of them partial attempts while the paging script was fixed. One was the StreetInsider challenge retry.
  - 40 robots.txt reads.
  - 24 of the page fetches went to SEC hosts: 16 documents (10-K ×6, DEF 14A ×3, 20-F, 8-K ×2, 8-K exhibit, 424B5, 13D/A, 13G/A) and 8 JSON (7 submissions lists, 1 full-text search).
  - Status mix: 72 × 200, 4 redirects (followed after robots checks), 8 × 403 (6 Akamai or CloudFront access-denied pages, 1 Cloudflare challenge on lancome-usa.com, and the StreetInsider challenge, which cleared on retry), 1 × 404.
  - 29 WebSearch calls (5 for the ranking and scope, 15 for owners, 9 for affiliates). 0 WebFetch.
- **Tokens:** about 240k (estimate; not metered).
