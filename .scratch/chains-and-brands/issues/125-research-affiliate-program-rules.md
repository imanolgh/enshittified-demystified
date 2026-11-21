# Research: Affiliate program approval and sales rules

Type: research
Status: open
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

For the affiliate programs the alternatives block plans to use, what does each program require before it approves a site, what keeps an account open after approval, how are links built, and which of its terms touch the plan in "Alternatives and affiliate links"?

## Context

- Opened 2026-11-21 when the developer reviewed the monetization tickets (developer: "yes" to adding it). No ticket covers joining the programs, and affiliate links are the only revenue in v1 (v1 has no accounts; ADR 0004 "Launch backend parked").
- Claude raised two points from memory, not checked: Amazon Associates closes an account that makes fewer than 3 qualifying sales in its first 180 days, and Amazon's Product Advertising API is open only to accounts with recent sales. "Alternatives and affiliate links" Q5 also wrote the API point down as "from memory, for the build to confirm". This ticket checks both against Amazon's own pages.
- The plan to check against ("Alternatives and affiliate links", 2026-11-17):
  - a brand's own program (direct or through a network such as Impact, CJ or Rakuten) linking to the brand's own store;
  - retailer programs (Amazon, Walmart, Target) linking only to the qualifying brand's own store or product pages there, never to search or category pages;
  - never a link for a PE-owned or PE minority stake brand;
  - a label at every link ("We earn a commission if you buy through this link"), `rel="sponsored"`, a how-this-works section, and Amazon's required line on pages with Amazon links;
  - links stored as operator batches in `affiliate_links`; links can't come from crawling Amazon (its robots.txt shuts out automated fetchers).
- The site is a static Astro site on Cloudflare Pages with share images made at build time ("Website stack and hosting"), run by one self-funded US person, with no accounts. Engine "Cost cuts before revenue" put it on the developer's machine until the site earns money.
- Brand-direct program counts from the audits: cookware 9, mattresses 5 to 6, clothing and shoes 6, women's clothing 4, eyewear 4, personal care 3, vitamins and supplements 2, sporting goods 2, pharmacies 2, pet stores 1, pet food 1 ("Launch industries", "Research: Audits of five product industries", "Category brand lists and checked").

## What to find, per program

Programs: Amazon Associates (US), Walmart's affiliate program, Target's affiliate program, and the networks Impact, CJ, Rakuten Advertising and Awin (ShareASale). For brand-direct programs, sample about five from the audit files above and report what they share rather than covering every brand.

1. **Approval:** what a site must show before the program approves it (a live site, a number of pages or posts, traffic, a privacy policy, a site age), and whether a site still being built can apply.
2. **Staying open:** minimum sales or activity rules, the window, and what happens when the window passes (closure, reapplication).
3. **Link building:** how links are made (dashboard, link builder, API), which tools are gated and on what condition, and whether stored links may be used in a static site, in share images or in an app later.
4. **Terms that touch the plan:** where links may point, required disclosure text and placement, rules on link cloaking or redirects, rules on using the retailer's prices, images or product data, and any ban on sites that rate or criticize brands.
5. **Who can join:** individual versus business accounts, tax forms (W-9), payment thresholds and methods.
6. **Timing:** from the above, when in the build the developer should apply to each program so links exist on launch day without an account closing before the site has traffic.

## Rules

- Findings go to `.scratch/chains-and-brands/research/affiliate-program-rules.md`, every claim cited to the program's own pages (operating agreement, program policies, help pages, API docs) with the date read. Trade press only where a program publishes nothing, marked as such.
- The map's research rules apply: robots.txt read before the first request to every host, including redirect targets; stop and report on any permission refusal, never reaching the same host another way.
- No sign-ups, no applications, no paid calls. Public pages only; a page behind a login is reported as unread.
- Budget about 400k tokens, stop at 500k against the harness count.
