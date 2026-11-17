# Research: Brand licensors and where licensees are stated

Type: research
Status: open
Blocked by: none
Map: [non-pe-owners](../map.md)

## Question

Which companies own US consumer brand names in order to license them out, who owns those licensors, and which free public primary sources name the licensee that makes or sells a licensed brand's products?

## Context

- Charted 2026-11-16. **Not run until the developer unparks this map.**
- v1 rule: a brand's owner is whoever owns the name, never a licensee (GLOSSARY "Brand"); the prompt claims the licensor on "licensed from" or "used under license" and gives the licensee nothing (engine "Extraction prompt rules", Q2). Licensing is not a predicate in v1 (engine "Predicate semantics", Q6).
- Known cases from the audits:
  - Cookware: five of 30 rows are licensed names (Farberware, KitchenAid, Martha Stewart, Rachael Ray, Pioneer Woman) ([category-audit-full](../../chains-and-brands/research/category-audit-full.md) §7 item 10). Marquee Brands owns Martha Stewart, Emeril Lagasse and Sur La Table, with Neuberger Berman as lead investor ([cookware](../../chains-and-brands/research/category-audit/cookware.md) CK22). Meyer's "Our Brands" page lists KitchenAid without saying it is licensed, which gives the licensee as owner (chains "Product categories", Q7).
  - Apparel: Authentic Brands Group sits on the portfolio pages of GA, LGP and CVC (Reebok, Brooks Brothers, Forever 21) ([pe-consumer-scan](../../chains-and-brands/research/pe-consumer-scan.md); [1-large-diversified](../../chains-and-brands/research/pe-consumer-scan/1-large-diversified.md)).
  - USPTO: sponsor-owned brands sit in "IP Holder" or "IP Holdings" subsidiaries, and the register records licenses rarely ([uspto-trademarks](../../chains-and-brands/research/uspto-trademarks.md)).
- Publicly filing licensors and licensees on EDGAR's ticker list (2026-11-16): Xcel Brands (XELB), Newell Brands (NWL). Iconix and Sequential Brands no longer trade.

## Find out

1. **Licensors:** the companies whose business is owning consumer brand names and licensing them (Authentic Brands Group, WHP Global, Marquee Brands, Xcel Brands, Bluestar Alliance, Iconix and similar), each with its US consumer brands and its owners as primary sources state them, including Form ADV `Any PE Funds` for any investment-firm owner.
2. **Where licensees are named:** for 10 to 15 licensed brands, which sources name the licensee and in what words: a licensee's 10-K or 10-Q (material license agreements, often in exhibits), a licensor's 10-K, licensor and licensee press releases, licensor "partners" pages, product packaging text on brand sites, USPTO assignment records. Whether each source dates the license.
3. **Shapes of licensing:** product licenses (KitchenAid cookware by Meyer), store-operating licenses (Forever 21 stores run by an operating partner), and the "licensed in some categories only" case (Farberware cookware by Meyer, kitchen tools by Lifetime Brands). Whether a brand can have several licensees by product line or region.
4. **How common:** across the brands in the thirteen audited industries and the screens, how many are licensed names, by industry.

## Rules

- Same rules as chains "Research: Where PE owns consumer brands": public primary sources only, no PitchBook, Preqin, CB Insights or paywalled sources, competitor sites never sources, never fetch WhoIsMyDentist, Private Equity Vet or Reddit; robots.txt followed; SEC user agent with the project's name and no email, at or under 2 requests per second.
- Findings go to `.scratch/non-pe-owners/research/brand-licensors.md`.

## Hands on

- "Brand licensors and licensees on the brand page".
