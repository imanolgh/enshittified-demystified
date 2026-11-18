# Alternatives and affiliate links

Type: grilling
Status: resolved
Blocked by: 54, 81  (Product categories: vocabulary and assignment; Launch industries)
Map: [chains-and-brands](../map.md)

## Question

When does a page show alternatives, by what published rule are they chosen and ranked, how are affiliate links disclosed, and which programs are allowed?

## Context

- ADR 0004 money model: product categories may carry affiliate links with a visible disclosure, ranked by a published rule and never by commission.
- Pivot proposal, **not decided**: alternatives must not imply quality ("No PE evidence found, not a quality rating", or link independent reviews); prefer brand-direct programs (Amazon reportedly cut rates in May 2026). Illustrative economics: 10,000 visits at 8% clicks, 4% purchases, $120 order, 6% commission ≈ $230.
- Every alternative shown is itself a claim about ownership: does a brand need to be checked before it can be listed as an alternative?
- In-store chains (restaurants, gyms) earn no affiliate income; affiliate applies to product categories.
- **From "Product categories: vocabulary and assignment"** (2026-11-16): no country filter in version 1, but the request behind it ("Some US brands look awesome but I sadly can't buy from them... If I can find an alternative in my region") is about where an alternative is sold, which is this ticket's.
- **From "Launch industries"** (2026-11-16): six launch industries have brand-direct affiliate programs on brands that aren't PE-owned: cookware 9, mattresses 5 to 6, women's clothing 4, eyewear 4, vitamins and supplements 2, pet stores 1. At least three affiliate industries launch, guaranteed ahead of the PE-share order if seeding can't check every industry. "Research: Audits of five product industries" counts programs in five more.
- **From "Research: Audits of five product industries"** (2026-11-17): brand-direct affiliate programs in the new launch industries: clothing and shoes 6 (1 on a PE brand, Reebok), personal care 3 (1 on a PE brand, Supergoop!'s college-ambassador program), sporting goods 2, pet food 1, beauty products 0 confirmed (1 probable, Avon).
- **From "Category brand lists and checked"** (2026-11-17): eyewear covers retailers, online sellers (Warby Parker, Zenni, GlassesUSA) and frame brands (Ray-Ban, Oakley), where its affiliate programs sit. Pharmacies launch too (named exception; 2 brand-direct programs in the audit, 1 on a PE brand).


## Comments

### Round 1 (2026-11-17)

- **Where alternatives appear** (Q1): an alternatives block on every brand page whose verdict is PE-owned or PE minority stake, in every industry (restaurants and gyms too, where nothing earns); industry pages get a "Show only brands with no PE found" filter; pages for brands without PE get no block. Alternatives stay free (`monetizationideas.md` §4).
- **Who qualifies** (Q2): same industry list, a completed check, and a verdict other than PE-owned, PE minority stake, owner type not confirmed, sources disagree or not yet checked; a brand with a pending deal to a PE buyer is left out. Each alternative shows its own verdict line and any "formerly PE-owned" history. No regional filter (v1 has no locations; where-to-buy waits for the store map).
- **Order** (Q3): the industry list's own order (its method's ranking), ties alphabetical, all qualifying brands collapsed after 10; brands with and without affiliate programs ranked together; commission never changes order or inclusion. No paid or featured placement in v1 (`monetizationideas.md` marked).
- **Quality** (Q4): the block states that brands are chosen by ownership alone and that this isn't a quality rating; no reviews, ratings or written praise.
- **Programs** (Q5, revised after the developer said marketplace links for non-PE products that sell on Amazon are fine): a brand's own program (direct or through a network such as Impact, CJ or Rakuten) linking to the brand's own store, and retailer programs (Amazon, Walmart, Target) linking only to the qualifying brand's own store or product pages there, never to search or category pages that put PE brands beside it. Never an affiliate link for a PE-owned or PE minority stake brand on any retailer. When both exist, both links show, labeled "Shop at {brand}" and "On Amazon". Links can't be built by crawling Amazon (its robots.txt shuts out automated fetchers); they come from Amazon's own tools, and its Product Advertising API has been gated on prior sales (from memory, for the build to confirm).
- **Disclosure** (Q6, revised): a label next to every affiliate link ("We earn a commission if you buy through this link"), `rel="sponsored"`, a how-this-works section, and Amazon's required line ("As an Amazon Associate I earn from qualifying purchases") on pages with Amazon links. Disclosure wording and retailer terms go to "Legal review before launch".

### Round 2 (2026-11-17)

- **Storage** (Q7): an `affiliate_links` table of operator data (brand, store, URL, program, batch, dates), uploaded in batches, never through the claims door and never evidence; code hides a link whenever its brand stops qualifying; dead links go to the operator report. Schema note in `evidence_layer_plan.md` §4.
- **Several industries** (Q8): a PE brand on several lists shows its alternatives grouped by industry, under each label and in each list's order.
- **Glossary** (Q9): "Alternative" added as proposed.

## Answer

Resolved 2026-11-17 in a grilling session (two rounds, recorded under Comments).

- **Alternatives** appear on every PE-owned and PE minority stake brand page, grouped by industry, in each list's own order, collapsed after 10; industry pages get a "no PE found" filter. An alternative is checked, on the same list, with no PE in its ownership and no pending deal to a PE buyer, and shows its own verdict line. The block says alternatives aren't a quality rating.
- **No paid placement** in v1; commission never changes order or inclusion.
- **Affiliate links:** a brand's own program or a retailer program (Amazon, Walmart, Target) landing only on the qualifying brand's own pages; never for PE brands; both links shown when both exist.
- **Disclosure:** a label at every link, `rel="sponsored"`, a how-this-works section, and Amazon's required line.
- **Storage:** `affiliate_links`, operator batches, never evidence; hidden automatically when a brand stops qualifying.
- Docs: GLOSSARY "Alternative"; `evidence_layer_plan.md` §4 `affiliate_links`; `monetizationideas.md` (featured placement not in v1; affiliate rule). No ADR: ADR 0004's money model already says ranked by a published rule, never by commission.

Handed on:
- "Card wording and the how-this-works page": the quality line, the per-link label, Amazon's line, and the how-this-works section on programs and order.
- "Website pages and shareable cards": the alternatives block (grouped by industry, collapsed after 10, "Shop at {brand}" and "On Amazon"), the industry page filter.
- "Legal review before launch": FTC disclosure wording and placement; retailer program terms (Amazon Associates' required line, linking rules, its Product Advertising API).
- engine "Graph endpoint and non-brand output shapes": the alternatives block and the industry filter as output shapes, computed from categories and list order.
- engine "API conventions, internal auth and operator surface": affiliate link batches and the dead-link report.
