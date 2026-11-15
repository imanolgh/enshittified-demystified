# Extraction prompt rules

Type: grilling
Status: open
Blocked by: 22  (Extraction execution)
Map: [engine](../map.md)

## Question

Which rules go into the production extraction prompt: v5's narrower rules or v8's wider ones, how trademark notices and licensed brands are claimed, how a team's earlier deals ("Prior to RiverGlade") are kept from becoming the firm's holdings, and what full-run check a prompt version must pass before the developer approves it?

## Context

- Created 2026-11-14 from "Extraction execution" (Q1, developer's ruling). Claude drafts the prompt, the developer approves it, golden-fixture tests check it (CLAUDE.md role contract). Tested versions: [v5](../research/extraction-test-prompt-v5.md) and [v8](../research/extraction-test-prompt-v8.md); all results in [extraction-model-comparison](../research/extraction-model-comparison.md). Blocked by "Extraction execution" because the rules are tuned to the model it picks (v8 was tuned on DeepSeek V4.1 Flash).
- **v5 vs v8** (DeepSeek's own API, 157 clean-text documents): v5 615 claims, 615 of 615 quotes exact, blind precision 98 to 100% fully correct; v8 1,376 claims, 135 known facts against v5's 126 on the strict metric, 98.8% exact quotes, blind 95% fully correct with none wrong. v8 needs a 120,000-token output limit (Leonard Green's portfolio page needed about 36,000).
- **Trademark notices:** v4 added "X is a trademark of Y" as `owned_by` (the category audit counted these). Open cases: licensed brands on a maker's "Our Brands" page (Meyer listing KitchenAid, flagged by the judge in the 2026-11-14 precision check), and IP-holding subsidiaries such as "Applebee's IP LLC", which name an affiliate rather than the owning group.
- **"Prior to <firm>" sections:** a team page listing deals its people did at earlier firms. v8 on DeepSeek's own API gave 12 false RiverGlade holdings, stopped only because their quotes included the heading and failed the check. Through OpenRouter, Haiku and DeepSeek each gave them as former RiverGlade holdings in one of two runs, with bare-name quotes that pass the check. Both models need an explicit exception.
- **Deal stage:** Haiku's precision errors were mostly announced deals given as completed or current (5 of 6). DeepSeek through OpenRouter took Brentwood's "decision to acquire" as an exit and credited Longview with control shared by five sponsors.
- **From the first precision check:** quote the line that names the subject, never a heading; never derive a stake percentage from other numbers.
- **Portfolio pages:** the portfolio-page-first rule (v7, v8). Roark's page states no relationship in words; v8 read it correctly on one of two runs on DeepSeek's own API; through OpenRouter, DeepSeek gave 86 and 85 Roark claims (30 marked former in one run, none in the other) and Haiku none. Whether a re-read safeguard runs is "Extraction execution"'s.
- **Real recall misses** (research "Real recall"): members of a listed owner group, the sponsor named behind a buyer, brands mentioned on another subject's page, long annual reports. v6 to v8 recovered most of them.
- **No brand in the request:** every test named the brand the documents were fetched for; production names none ("Extraction execution" Q3), so the checks here run without it.
- **Check before adoption:** a full run on the 157 clean-text documents plus a blind precision check, with the existing harness at `~/.local/share/extraction-eval/` (scorer `scripts/score_clean.py`), on the model "Extraction execution" picks. Spending needs the developer's yes.
- **From "Extraction execution"** (2026-11-15, resolved): the model is DeepSeek V4.1 Flash on DeepSeek's own API, so the rules are tuned and checked on it. Under production conditions (no brand line, v8, two runs) DeepSeek found 141 and 142 known facts, read Roark's and Leonard Green's pages correctly both times, and both runs gave the 12 "Prior to RiverGlade" deals as former RiverGlade holdings. `document_label` is dropped, so the prompt's label wording goes. TSG's portfolio page makes DeepSeek rewrite "[link: Close]" as "[link: Alexia]" in about 81 quotes on some runs (on its own API too); the quote check rejects them.
- **From the 2026-11-15 blind precision check** (judge's notes): "privately owned" and "run by family" name no owner (a Qwen tuning sentence that asked for described owners produced "private" as an owner twice); "an affiliate of" is not ownership; a stake type stated for a group of sponsors ("together hold a majority") is not each sponsor's; a closed business line (Mud Bay's Mud Room) is not a current holding; Meyer's "Our Brands" list mixes owned and licensed brands (KitchenAid).
