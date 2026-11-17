# Research: Industry screen (twelve candidate industries)

Ticket: [80 Research: Industry screen](../issues/80-research-industry-screen.md) · Researched 2026-11-16 by four background workers, assembled by the parent session. Worker reports, with every table, quote and Form ADV lookup: [a: bowling, golf, ski](industry-screen/a-bowling-golf-ski.md), [b: child care, salons, funeral homes](industry-screen/b-child-care-salons-funeral.md), [c: collision, auto service, home services](industry-screen/c-collision-auto-home-services.md), [d: urgent care, physical therapy, landlords](industry-screen/d-urgent-care-pt-landlords.md).

Method: the top ~10 national US brands per industry (a scaled-down version of the category audits), ownership from primary sources only, rankings from trade press, Form ADV `Any PE Funds` from the SEC's November 2026 adviser files, and the strict rule for public companies (a PE minority stake only from a 13D or a 13G not filed under Rule 13d-1(b)). Rollups whose locations keep local names are listed separately, not counted as rows. Quote checks: 285 of 285 quotes matched their saved page text across the four workers; every negative control failed.

## Short answer

| Industry | PE share by brand row | Worker's verdict | Main owners and notes |
|---|---|---|---|
| Collision repair | 9 of 10 (90%) | full audit | Caliber (H&F), Driven's CARSTAR, ABRA, Fix Auto and Maaco (Roark ~62% of a public company), Crash Champions (Clearlake), Classic (TPG); Gerber (public Boyd) the only non-PE row |
| Urgent care | 8 of 10 (80%; 7 without CityMD, provisional) | full audit | AFC (Lorient), GoHealth (TPG Growth), Fast Pace (Revelstoke), WellNow (Aspen Group, LGP); the two non-PE rows are HCA and a nonprofit system |
| Physical therapy | 8 of 10 (80%) | full audit, with the rollup list | Select (WCAS, private since 2026-07-01), Athletico (BDT), ATI (creditor and sponsor group), Ivy Rehab (Waud); 31% of clinics sit in consolidators, many with local names |
| Home services franchises | 9 of 13 (69%) | full audit, but define the size measure first | SERVPRO (Blackstone), TruGreen (CD&R), Neighborly brands (KKR), ServiceMaster brands (Roark), Authority brands (Apax); the list is a composite, not a ranking |
| Child care centers | 6 of 10 (60%; 11 of 15 with Learning Care Group's brands as rows) | full audit | KinderCare (public, Partners Group controls), Learning Care Group (American Securities, 11 brands), Primrose (Roark), Goddard (Sycamore), The Learning Experience (Harvest, 2025) |
| Oil change and auto service | 6 of 12 (50%) | full audit | Jiffy Lube (Monomoy, 2026-07-01), Mavis with Midas and Pep Boys (BayPine), Take 5 and Meineke (Driven, Roark) |
| Bowling and family entertainment | 5 of 11 (45%; 64% if Atairos counted) | full audit | Sky Zone (Palladium), Urban Air (Seidler), Altitude (NRD); Dave & Buster's and Main Event (Hill Path 13D); Chuck E. Cheese's owners unnamed since 2020 |
| Hair salons | 3 of 10 (30%) | no | the PE sits only in salon-suite brands (Sola, MY SALON Suite, Phenix); Great Clips, Sport Clips and Regis have none |
| Golf | 2 of 7 (29%) | audit as operators, not brands | Topgolf (Leonard Green 60% since 2026-01-01), Five Iron; course and club operators keep local names (Troon, Invited, Arcis, all PE-backed) |
| Landlord brands | 2 of 8 strict (25%); 4 of 8 owned by investment funds of any kind | no | Progress (Pretium), FirstKey (Cerberus), Tricon (Blackstone Real Estate); Invitation Homes and AMH public with no PE holder |
| Ski resorts | 1 of 8 (12.5%) | no | Alterra/Ikon (KSL and Henry Crown); resorts keep local names |
| Funeral homes | 0 of 6 | no brand audit | every national brand is SCI's (Dignity Memorial); the PE sits in rollups with local names (Everstory/Axar, Park Lawn/Birch Hill) |

Seven industries pass the about-20% bar by brand row and were judged worth a full audit: collision repair, urgent care, physical therapy, home services franchises, child care, oil change and auto service, bowling and family entertainment. Golf passes only through operators whose courses keep local names.

## Questions for the developer (from the workers; nothing decided)

1. **Owners whose Form ADV says no PE funds.** Atairos holds 80.9% of Lucky Strike's Class A shares by 13D (and a "substantial ownership position" in Arcis Golf); Meritage Group owns Les Schwab; both report `Any PE Funds = N`, which proves nothing under ADR 0001. Counting Atairos moves bowling from 45% to 64%.
2. **A public holding company.** Icahn Enterprises holds about 17% of Monro by 13D (plus swaps) and files no Form ADV. Does such a holder count as PE?
3. **Real estate funds as landlords.** Blackstone's real estate adviser reports 53 real estate funds and no PE funds; Pretium's single-family rental manager reports its funds as hedge funds; Cerberus reports mostly hedge funds. The engine already has the `real_estate` owner kind; how its rules read these owners decides the landlord numbers.
4. **Industries where PE hides in local-name rollups** (funeral homes, golf courses and clubs, ski resorts, part of physical therapy): the brand-only model doesn't show them.
5. **Home services' size measure**: Franchise Times sales (its robots.txt blocks ClaudeBot) or FDD Item 20 unit counts.

## Cost

About 1.10M agent tokens in all (harness counts: 272k, 245k, 312k and 269k), about 25 to 35 minutes per worker, roughly 550 HTTP requests and 110 web searches. Approved estimate: about 1.2M.
