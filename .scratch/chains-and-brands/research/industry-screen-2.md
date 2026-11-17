# Research: Screen of five more industries

Ticket: [92 Research: Screen of five more industries](../issues/92-research-screen-five-more-industries.md) · Researched 2026-11-17 by two background workers, assembled by the parent session. Worker reports: [a: grocery, thrift stores, arts and crafts](industry-screen-2/a-grocery-thrift-crafts.md), [b: home furnishings, casinos](industry-screen-2/b-home-furnishings-casinos.md).

Method: the top ~10 national US brands per industry by a trade-press ranking blind to ownership, owners from primary sources only, Form ADV `Any PE Funds` from the SEC's November 2026 adviser files, the engine's counting rules ("Launch industries" Round 1, Q2). The bar: 20% or more at about 10 brands qualifies; 10% to 20% earns a 30-brand audit; under 10% doesn't launch.

## Short answer

| Industry | PE share by brand row | Verdict as screened | PE rows | National brands available | Owner not found |
|---|---|---|---|---|---|
| Arts and crafts retail | 2 of 7 (28.6%); 1 of 5 on the core five | qualifies (every national brand counted) | Michaels (Apollo, 2021 completion 8-K), Paper Source (Elliott, which reports PE funds; sale completed 2021-05-27) | 7 in all | 2 (Blick, Artist & Craftsman Supply) |
| Thrift stores | 2 of 13 (15.4%); 1 of 10 on the strict top 10; 2 of 6 for donation-based thrift only | audit candidate | Savers Value Village (Ares 61.5%, 13G/A as of 2026-09-30), America's Thrift Stores (TZP, "Current" on TZP's page) | about 13 to 15 multi-state brands | 2 (St. Vincent de Paul, Clothes Mentor) |
| Grocery | 1 of 11 (9.1%) at one banner per company; 2 of 14 (14.3%) at two per multi-banner grocer | below the bar, or audit candidate | Albertsons (PE minority stake: Cerberus 31.0% on a 13G filed under Rule 13d-1(d), not (b); Cerberus reports PE funds) | more than 30 multi-state banners | 2 (Trader Joe's, H-E-B) |
| Home furnishings | 1 of 10 (10%) | audit candidate | Bob's Discount Furniture (Bain Capital about 73% after its February 2026 NYSE listing) | about 35 national names | 1 (Rooms To Go) |
| Casinos | 1 of 10 (10%) | audit candidate | Bally's (Standard General 66.8%; reports PE funds) | about 15 to 20 multi-state operators | 0 |

- **Arts and crafts:** JOANN closed its stores in 2025; joann.com now redirects to a Michaels "welcome JOANN" page.
- **Grocery's banner rule decides its share.** Albertsons alone names 22 banners; the worker didn't compute an every-banner share. Leads checked but not rows: The Fresh Market (Apollo, 2016 release), Cardenas and Tony's (Apollo, 2022 agreement, closing not confirmed); Save Mart (Kingswood) and Erewhon (a Stripes minority) from trade press only.
- **Home furnishings:** the ranking (Home News Now's HNN 125, 2025 furniture and bedding sales) barely reaches decor chains and direct-to-consumer brands. Outside the top 10: Leonard Green lists The Shade Store and Visual Comfort as current; World Market (#49) is under Kingswood; At Home is owned by its lenders (all Form ADV `N`, so not PE).
- **Casinos:** rows are operators' brands (Caesars, MGM, PENN), ranked by 2025 revenue from SEC XBRL data, so non-SEC operators (Hard Rock, The Venetian, Mohegan) couldn't be placed. The Venetian doesn't count as PE: Las Vegas Sands' 10-K says Sands has "licensed the “Venetian” and “Palazzo” brands" to the Apollo-run operator. Variants: 1 of 7 (14.3%) if Boyd, Churchill Downs and Golden are treated as local-name rollups; 1 or 2 of 12 with Hard Rock and The Venetian placed.

## Open questions from the workers (numbers only; nothing decided)

1. Grocery row rule: one banner per company, two per multi-banner grocer, or every banner.
2. Whether Whole Foods is a grocery row (1 of 12, 8.3%); Amazon's 10-K text doesn't name it.
3. Thrift scope: donation-based only, or buy-sell resale franchises too.
4. Whether Paper Source and HobbyTown count as arts and crafts.
5. Casino row rule (operator brands or property names) and the unplaced operators.
6. Michaels, Paper Source and The Fresh Market rest on deal documents older than 18 months; no exit was found for any.

## Process issues

- **Robots slip (worker a):** following svdpusa.org's robots.txt redirect, the fetcher requested the ssvpusa.org homepage once before reading that site's robots.txt, which disallows ClaudeBot. The response was deleted unread and the fetcher patched.
- Worker b reported no slips. One weak source: At Home's ownership release was read as a reprint on a host that looks like a Cision demo site (flagged in its report).
- SEC: 70 requests across both workers, at least 1.1 seconds apart.

## Quote check

Workers' own checks: 65 of 65 and 50 of 50, with every altered control failing. The parent session's re-check of every quoted string against the saved pages and SEC data matched every evidence quote; 0 of 95 altered copies matched. The one unmatched string is a ranking's title.

## Cost

Harness counts: worker a 305,288 tokens, worker b 266,065; **571,353 in all** (approved about 0.55M, stop at 0.7M). About 147 page fetches, 63 robots.txt reads and 44 web searches.
