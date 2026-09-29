# Ledger — Analytics Engineer / Data Analyst, Consumer Sales & Marketing — 2026-09

## Metadata
- Date: 2026-09-29 (newly posted)
- Fit Score: Medium. It's an in-house Paris product company on dbt/Snowflake (your lane), and the core problem is multi-source revenue reconciliation, which is exactly your BNP story. It's pulled down by a 3–4 YoE gate, a role that leans analyst (Tableau, performance-marketing measurement, causal inference, ExCom decks), and marketing-data domain gaps (GA4, ad platforms).
- Source: LinkedIn (direct paste). Exact title not in the paste; it reads as a hybrid Senior Data Analyst / Analytics Engineer.
- Contract: Not stated (CDI expected)
- Location: Paris HQ, hybrid (up to 3 days/week remote)
- Compensation: Not stated. Confirm it clears the Passeport Talent threshold (likely fine for a 3–4 YoE Paris role).
- Company: Ledger, a crypto self-custody hardware wallet maker, ~600 people, Paris HQ. Product company with a consumer e-commerce + Amazon + wholesale/distributor go-to-market. Not a bank.

## Role shape (read this before deciding)
Roughly: 35% analytics engineering (dbt/Snowflake models across sales, sell-out, marketing and web sources; data-quality alerting; one reconciled view of revenue/units/margin), 25% BI (Tableau), 30% marketing/commercial analytics (attribution, ROAS/CAC, causal impact of pricing/promos, LTV), 10% stakeholder storytelling up to ExCom.
It's a business-facing AE who also does the analysis. That's closer to the analyst side than Alan/Tarmac, but it's not pure BI: it owns the models and data quality, and dbt comes before Tableau in the JD.

## CV Tailoring Instructions
Variant: B (General Modern Stack). ENGLISH CV (English JD, international company, "fluent in English").
Branch: variant-b-general
Summary line (English): "Analytics Engineer who builds reconciled, trusted data models on dbt and Snowflake: dimensional modeling, cross-source reconciliation and data-quality alerting, from designing a multi-source data model at BNP Paribas. Comfortable turning those models into business recommendations with Python and statistical analysis. CFA Charterholder. Seeking an Analytics Engineer role close to commercial decisions."
Summary line (French): "Analytics Engineer qui construit des modèles de données fiables et réconciliés sur dbt et Snowflake : modélisation dimensionnelle, réconciliation multi-sources et alerting qualité, issus de la conception d'un modèle de données multi-sources chez BNP Paribas. À l'aise pour transformer ces modèles en recommandations business avec Python et l'analyse statistique. CFA Charterholder." (only if needed; the English CV is primary)
Skills reorder: Variant B order, then (1) Transformation: dbt first, and mention Snowflake early; (2) BI & Semantic: keep Power BI, and add "Tableau (transferable)" only if you've actually used it — don't claim it otherwise; (3) Programming: "Python (pandas, statistics)". If your JHU coursework covered econometrics (diff-in-diff, regression discontinuity, synthetic control), add "causal inference / econometrics" somewhere visible. It's a named strong plus.
CFA positioning: Keep it in the summary, at the end. Revenue/margin reconciliation, ExCom-level recommendations and a crypto-finance product make the financial literacy relevant here, unlike a pure tech target.
Optional adds: Consider swapping TripAdvisor (PySpark, not needed here) for Stratton Group customer segmentation (PCA + K-Means, customer value). Stratton maps to "model customer value / repurchase behavior." Keep Sales Analytics: its KPI monitoring + anomaly-detection dashboards map directly to "sales anomalies alerting" and the Tableau scope.

## Cover Letter Angle
Lead with the first bullet, because it's the hardest problem in the role: "one consistent view of revenue, units and margin reconciled in Snowflake" across e-commerce, Amazon, wholesale and distributor sell-out. Sell-in and sell-out are different grains that arrive at different times and use different SKU and partner codes. Getting one number that Finance and Growth both trust is a modeling problem before it's a dashboard problem. That's the problem you solved at BNP: three manually maintained source systems, an explicit grain declaration, SCD Type 2 versioning, and a data-quality framework that surfaced identity-resolution failures, duplicates and cross-source code inconsistencies. That's the same failure mode as SKU mismatches and refund anomalies. In pc_pipeline you went further: a tested dbt layer (6 defect classes) and a semantic layer with an LLM agent on top. That fits their "leverage AI tooling (Claude, LLM-based workflows) to scale analytics delivery." Close with the business side: CFA-level financial literacy for margin work and presenting to ExCom. Be honest that marketing attribution is the part you'll ramp on. Don't pretend otherwise; show you understand why GA4, ad-platform and internal sales numbers never match.

## Preparation Gaps
- **Sell-in vs sell-out modeling.** Sell-in = Ledger → distributor/retailer (Ledger's invoiced revenue). Sell-out = retailer → end customer (reported by partners, late, messy, different SKU codes). Be able to sketch the dbt design: a conformed product/SKU dimension with a mapping table, a partner dimension, separate fact tables at their native grain, and a reconciled mart that exposes gaps (channel inventory = sell-in − sell-out). Also refunds/returns handling and FX. This is the whiteboard question they'll most likely ask.
- **Marketing attribution + why sources disagree.** GA4 vs Google Ads vs Amazon Ads vs internal orders: attribution models (last-click vs data-driven), attribution windows, view-through vs click-through, consent/cookie loss, time zones, currency, and gross vs net of refunds. Know the definitions of ROAS, CAC, blended vs channel-level metrics, and incrementality. You don't need hands-on GA4, but you need to be fluent in why the numbers never match and how you'd model the reconciliation.
- **Causal inference for campaigns.** CausalImpact (Bayesian structural time series: build a counterfactual from control series, measure the post-period gap), synthetic control, difference-in-differences, and the pitfalls of naive pre-post (seasonality, Black Friday, crypto price cycles driving demand — very relevant for Ledger, since sales spike with BTC price). A small notebook applying CausalImpact to a public time series would be a strong, fast talking point.
- **LTV / repurchase.** Cohort retention, repurchase rates, simple BG/NBD-style or cohort-based LTV, and "services attach" (subscriptions/services on top of devices). Concept-level + one worked example.
- **Tableau.** Get basic fluency on Tableau Public (calculated fields, LODs, dashboard actions) — 1–2 evenings. It's the most visible "strong" requirement you lack, and it transfers quickly from Power BI/DAX.
- **Ledger context.** Product lines (Nano, Flex, Stax), channels (ledger.com, Amazon, retail), and the fact that demand is tightly linked to crypto market cycles. Mention that forecasting/causal work has to control for it.

## Stack Analysis

### Have
- SQL (strong), dbt, Snowflake: named core requirements
- Multi-source data modeling + reconciliation: BNP three-source dimensional model
- Data-quality alerting (SKU, anomaly, duplicates): BNP DQ framework, pc_pipeline test suite, Sales Analytics anomaly dashboards
- Python for analysis/statistics
- AI tooling for analytics: pc_pipeline LLM NL→SQL agent; LVMH RAG + LLM-as-judge. Matches "Claude, LLM-based workflows."
- Business orientation + financial literacy: CFA; margin/revenue concepts
- English fluency (TOEFL 120); presentation experience (LVMH client deliverables)

### Missing
- 3–4 years of data analytics / AE experience (you have an internship + projects)
- Tableau (hands-on)
- Marketing/web analytics data: GA4, Google Ads, Amazon Ads, affiliation networks
- Causal inference in production (CausalImpact, synthetic control)
- E-commerce / retail sell-in/sell-out domain

### Partial
- BI dashboards: Power BI strong → Tableau transferable
- Causal inference: econometrics background possible via the JHU MA (verify what you can honestly claim)
- Customer value modeling: Stratton segmentation (off-CV); LTV concept-level
- Salesforce data model: not held, but it's a "contribute to" item

### Green Flags
- dbt + Snowflake as the named source of truth: your core lane
- In-house product company, Paris HQ, hybrid 3 days remote
- Clear, specific problem (sell-in/sell-out/margin reconciliation), not generic
- Owns data quality alerting and model development, supported by a DE team (good for a junior-ish AE)
- Explicit AI/LLM tooling mention (Claude): matches your differentiator
- Well-written, concrete JD; the company knows what it wants
- Equity/shareholder option

### Red Flags
- 3–4 YoE stated: the most real barrier. It doesn't read soft (no "first experience" contradiction).
- Analyst-leaning scope: Tableau + marketing attribution + causal + ExCom decks are ~65% of the role. It drifts from engineering-first AE, though not into pure BI.
- Marketing-analytics domain (GA4/ads) is a genuine ramp.
- Crypto-cycle exposure: the business is sensitive to crypto markets (a company-risk consideration, not a JD-quality issue).
- No age-discrimination wording.

## Notes
- Ranking: worth applying. It's in-lane on stack, company type and location, and the reconciliation angle is one of your best-matched "hardest problems" so far. Odds are tempered by the 3–4 YoE gate and marketing-analytics scope. It's a better long-shot than any ESN fallback.
- Apply early (newly posted), and try a referral or direct note to the Data Team lead on LinkedIn. It sidesteps the YoE screen better than a cold application.
- If you get an interview, spend prep on sell-in/sell-out modeling + attribution discrepancies first, then a CausalImpact notebook, then Tableau basics.

## Raw JD
About the job
We're a team of experts pushing the limits of what's possible, united by our common goal to unlock true freedom through digital ownership, making technology accessible for all. We believe in a world where users, creators and enterprises manage their value with ownership and freedom. Our curiosity drives us to innovate, empowering individuals on a global scale. We believe change is constant and our team moves forward as one, with a culture of problem-solving where every employee is empowered and supported to challenge tradition and create solutions. Our mission is simple: to make self-custody accessible and give people the keys to their own financial futures. If you want to make a true impact, we want you to join us at Ledger.

At Ledger, we're proud to be the global platform for digital assets and Web3, with over 20% of the world's crypto assets secured through our Ledger devices. With our headquarters in Paris, and offices in Vierzon, Grenoble, Montpellier, London, Portland, Geneva, Zurich and Central Singapore, we have a team of around 600 professionals developing a variety of products and services to enable individuals and companies to securely buy, store, swap, grow and manage crypto assets – including the Ledger hardware wallets line with more than 7.5 millions units already sold in 200 countries.

The team:
You'll join the Data Team, responsible for turning data into actionable insights and recommendations for our consumer sales and marketing operations across all channels.

What you'll be doing:
* Own analytics across the full consumer sales scope: Ledger.com e-commerce, Amazon marketplaces, wholesale and resellers/distributors - covering both sell-in and sell-out- with one consistent view of revenue, units and margin reconciled in Snowflake, our source of truth
* Develop and improve data models (dbt/Snowflake) across varied data sources (sales, sell-out, marketing, web analytics) with the support of the data engineering team; co-own data quality alerting (SKU, refunds, sales anomalies)
* Build and maintain Tableau dashboards for business stakeholders: e-commerce performance, wholesale, resellers sell-out, affiliation, editorial content, shipping costs
* Own the measurement of performance marketing channels - SEM / Google Ads, affiliation & retargeting, Amazon Ads: spend, revenue attribution, ROAS/CAC across GA4, ad platforms and internal sales data, reconciling discrepancies between sources
* Measure the true impact of pricing, promotional and marketing campaigns using causal inference methods (CausalImpact, pre-post, control/synthetic groups) and recommend budget arbitrations to the Growth team
* Model customer value (LTV, repurchase behavior, services attach) and feed it back into marketing ROI decisions
* Contribute to cross-functional data projects (Salesforce data model, new data source integrations) and leverage AI tooling (Claude, LLM-based workflows) to scale analytics delivery
* Create and deliver presentations that turn complex analyses into clear recommendations for stakeholders up to ExCom level

What we're looking for:
* Strong SQL and dbt skills (Snowflake)
* Python for analysis and statistics; experience with causal inference methods is a strong plus
* Strong Tableau skills
* Familiarity with marketing/web analytics data: GA4, ad platforms (Google Ads, Amazon Ads), affiliation networks
* 3-4 years of experience in data analytics/analytics engineering
* Data driven and business oriented; able to challenge stakeholders' methodology
* Excellent organizational skills, fluent in English

Benefits: hybrid (up to 3 days WFH/week), health & life insurance, shareholder opportunity, commuter allowance, L&D.
