# In Tandem (OurFamilyWizard) — Analytics Engineer (Finance & Modeling) — 2026-08

## Metadata
- Date: 2026-08-28
- Fit Score: High — the single best domain fit of the batch. It explicitly rewards BOTH halves of your differentiator at once: "fluent in finance, unwilling to let a number you can't explain go out the door" (CFA + BNP reconciliation/data-quality) AND dbt + real dimensional modeling ("designed marts, not just queried them"). Caveats: 3+ years (softened by a take-home stage and broad "data science/advanced analytics" wording), and shipped statistical forecasting + subscription metrics are real gaps.
- Source: Direct paste (job board / OurFamilyWizard careers)
- Contract: Permanent, Full-Time
- Location: Paris, France — FULLY REMOTE. English working language (US-founded brands: OurFamilyWizard, Cozi, FamilyWall, Custody Navigator).
- Compensation: €55,000 – €70,000 / year (stated) — check against current Passeport Talent floor; likely clears it, verify.

## CV Tailoring Instructions
Variant: A (Financial Data Infrastructure) — this is the exception where finance-forward framing wins even though the company isn't a Tier-1 fin-data firm, because the ROLE requires finance fluency directly.
Branch: variant-a-finance
Summary line (English): "Analytics Engineer and CFA Charterholder who owns the number end-to-end — dimensional finance models in dbt, reconciliation and data-quality frameworks across disparate source systems, and the discipline to never ship a number I can't explain. Building modern, tested data foundations that Finance can defend."
Summary line (French): French CV not required — English-working, US-founded brands. No placeholder needed.
Skills reorder: Variant A order (Modeling → Domain/Finance → Transformation → Warehousing → BI/Semantic). Surface: dimensional modeling / SCD, dbt + tests, data quality/reconciliation, and AI-native workflow.
CFA positioning: KEEP IN SUMMARY. This is the one role where CFA is a direct requirement match ("fluent in finance") — lead with it as domain evidence, don't bury it.
Optional adds: Consider adding Stratton (PCA/K-Means) back for this one — it's your only shipped statistical-modeling evidence, and the JD wants "statistical modeling shipped into a business process." If the one-page constraint bites, mention it in the cover letter instead.

## Cover Letter Angle
This role is written in your voice: "When two systems disagree, you find out why and tell the people upstream" and "a spreadsheet nobody can reproduce reads to you as a liability" describe exactly what you built at BNP — a data-quality framework over manually maintained private-capital data that surfaced identity-resolution failures, duplicate detection, and cross-source code inconsistencies, and a dimensional model that reconciled three inconsistent source systems into one defensible view. The reconciliation task here (app stores ↔ payment processors ↔ subscription systems ↔ ledger, with automated checks that alert rather than surface at close, each discrepancy turned into a test) is the same discipline applied to subscription revenue instead of fund/deal data. Add your CFA as the reason you don't treat "defensible to Finance" as a nice-to-have, and your AI-native workflow (Claude Code and agent SDKs already part of how you build — you can speak to wiring governed metrics into an agent that answers Finance's questions directly) as evidence you already work the way their daily loop runs. Be honest that the forecasting layer is where you're growing into the role — but the foundation work they need first (governed metrics, reconciliation, tested marts) is squarely what you've already done.

## Preparation Gaps
- **Subscription finance metrics — build fluency and be ready to defend them.** ARR/MRR, renewal rate, gross vs net churn, LTV/CAC, cohort revenue — how each is DEFINED, why finance stakeholders argue about them, and how you'd version them in dbt with tests. This recurs in every AE JD now; for this one it's front-and-center ("built and defended to a finance stakeholder").
- **Statistical modeling shipped into a process — your biggest gap here.** The JD wants forecasting, survival/cohort analysis, and propensity/uplift shipped as scored dbt tables (not notebooks). Study: cohort retention curves (and why one is "the wrong shape"), survival analysis for renewal/retention forecasting, churn-propensity and uplift modeling, and LTV projection by acquisition source. You have PCA/K-Means (Stratton) as shipped ML but not forecasting/survival — close this at concept + one worked example level before the take-home.
- **Statistical rigor / reading results honestly.** "What a model is leaking, when a result is noise" → refresh overfitting, data leakage, significance vs noise, and how to read an A/B or price-change lift honestly (you don't need to design the test, but must interpret it). Your stats coursework + CFA quant background is the base; sharpen it.
- **Reconciliation to a financial system of record.** Understand the mechanics of subscription/app-store reconciliation: revenue recognition timing, processor fees, refunds/chargebacks, proration, and how you tie transactions to the ledger. Frame your BNP reconciliation as the transferable skill.
- **Databricks + Unity Catalog + lakehouse** (nice-to-have, not dealbreaker). You're on dbt/DuckDB — read up on running dbt on Databricks, Unity Catalog for governance/lineage/documentation, and the lakehouse model. Concept-level is enough to be credible.
- **marimo** (named specifically — a whole bullet is "move the finance pack into marimo, retire Tableau"). Learn what marimo is (reactive, git-friendly Python notebooks) and why code-first scheduled reporting beats hand-built Tableau packs. Same idea as Hex/Streamlit/Quarto.
- **The take-home (Stage 2).** This is GOOD for you — it lets you prove skill despite fewer years. Expect a modeling + reconciliation or a metric-definition/forecasting exercise. Prepare to show tested, reproducible, documented work (your pc_pipeline habits) rather than a clever one-off.

## Stack Analysis

### Have
- dbt + tests — core (JD nice-to-have, but central to the work)
- Real dimensional modeling / designed marts — BNP + pc_pipeline (JD: "designed marts, not just queried them" — strong match)
- Strong SQL — yes
- Python + Git as daily habits — yes
- Finance fluency / CFA — direct match to "fluent in finance" (rare candidate strength here)
- Reconciliation + data-quality discipline — BNP framework maps directly to their reconciliation-and-tests bullet
- AI-native (Claude Code, agent SDKs) — authentic; part of their daily loop
- Semantic-layer + AI-agent concept — dbt Semantic Layer experience; JD runs an agent off the semantic layer

### Missing
- 3+ years experience (softened: "data science / BI / advanced analytics" counts, and there's a skill-tested take-home)
- Statistical modeling SHIPPED into a business process (forecasting, survival, cohort, propensity) — you have ML (PCA/K-Means) but not shipped forecasting
- Subscription metrics built & defended to finance (ARR/MRR/renewal/churn/LTV/CAC) — finance-fluent but not subscription-domain specifically
- Reconciling transactional data to a financial system of record (app store/payment/ledger) — analogous BNP work, but not this exact domain

### Partial
- Databricks / Unity Catalog / lakehouse — nice-to-have; you have dbt, not Databricks (concept transfer)
- Code-first notebook reporting (marimo/Hex/Streamlit/Quarto) — not yet; learnable quickly
- Experiment/lift reading — CFA + stats coursework base; needs sharpening
- Cohort/survival analysis — conceptual; not shipped

### Green Flags
- Rewards finance domain depth AND modern data stack simultaneously — your exact differentiator, uniquely so in this batch
- dbt on Databricks with a star-schema finance mart already in production — you build the layer on top, not from scratch
- Data quality / reconciliation / "defensible numbers" is the spine — matches your BNP work precisely
- AI-native is real (internal Slack agent off the semantic layer; Claude Code + agent SDKs in the daily loop)
- Fully remote, Paris-based, permanent, salary stated (€55-70k) and transparent
- Not a bank/FI — family-tech company; finance is the internal function you'd serve
- Take-home stage lets skill outweigh years
- Not a pure BI/reporting role and not tool-heavy-without-depth — passes your "not interested in" filter

### Red Flags
- None on JD quality — unusually well-written and specific. Watch-items are fit gaps, not warnings: the statistical-forecasting and subscription-metrics requirements are genuine, and "willing to wear several hats" on a small team supporting four brands means real scope sprawl (fine if you want breadth, worth confirming the modeling center holds).

## Notes
- Ranking: this and Qonto are your two strongest live fits, for different reasons — Qonto is the cleaner AE match with no seniority gate; In Tandem is the best DOMAIN match (finance + CFA + reconciliation) with a take-home that rewards proven skill. Both worth prioritizing over Pluxee/Dashlane.
- This role validates keeping CFA prominent — file it as evidence that finance-forward roles exist in the modern-stack space, not just Tier-1 fin-data-infra firms.

## Raw JD

Company: In Tandem — builds family-coordination technology across four brands (OurFamilyWizard, Cozi, FamilyWall, Custody Navigator). Mission: technology that strengthens relationships and reduces the mental load of family coordination.

Role: Analytics Engineer (Finance & Modeling). Own the metrics, reporting and reconciliation financial decisions rest on — turning subscription and transaction data across the four brands into numbers the business can defend. As that foundation becomes automatic, the work shifts toward forecasting and modeling. dbt project is live on Databricks with a star-schema finance mart in production, documented in Unity Catalog; you build the layer on top. An internal AI agent answers business questions in Slack off the semantic layer, so every metric you define/test becomes a question Finance can ask directly.
Department: Engineering. Permanent, Full-Time. Fully remote, Paris. €55,000–€70,000/year.

What you'll accomplish:
- Governed metrics: add missing definitions (ARR, renewal rate, churn, CAC), versioned in dbt, documented in Unity Catalog, with tests that make each defensible, wired into the agent
- Reporting Finance can run without you: move the recurring finance pack into marimo, retire the Tableau views behind it, turn a monthly hand-build into a scheduled run
- Numbers that reconcile: reconcile transactions across app stores, payment processors, subscription systems and the ledger, with automated checks that alert rather than surface at close; route discrepancies upstream with evidence, turn each into a test. You build checks and escalate; Accounting owns treatment
- Forecasting for Finance: cohort subscriber & revenue projection; aggregate renewal & retention forecasting feeding CFO forecast and board reporting; LTV by acquisition source feeding paid-spend allocation with Growth; pricing & promo impact modeled before shipping; individual churn propensity & uplift once a retention motion exists
- Models ship as scored tables in dbt and Unity Catalog with tests, lineage and a definition the agent can answer from — not as notebooks

Who you are:
- Statistically rigorous (why a cohort curve is the wrong shape, what a model is leaking, when a result is noise)
- Fluent in finance, unwilling to let a number you can't explain go out; when two systems disagree, find out why and tell upstream
- An engineer who owns the number end to end — from a CFO's question through model, test, report and the conversation after; a spreadsheet nobody can reproduce reads as a liability
- AI-proficient in practice (Claude Code, coding agents, agent SDKs part of the daily loop; a week of modeling is now an afternoon)
- Willing to wear several hats (small team, four brands; some weeks a retention model, some weeks an app-store discrepancy or unblocking a dashboard)
- Motivated by work that matters

What you bring:
- 3+ years in analytics engineering, data science, BI engineering or advanced analytics
- Statistical modeling shipped into a business process: forecasting, survival or cohort analysis, or propensity
- Measuring lift from a price change or growth experiment (read the result honestly)
- Subscription metrics built & defended to a finance stakeholder: ARR/MRR, renewal, churn, LTV/CAC, cohort revenue
- Strong SQL and real dimensional modeling (designed marts, not just queried them)
- Python and Git as daily habits

Nice to have (not a dealbreaker):
- dbt, Databricks and Unity Catalog, or a comparable lakehouse
- Reconciling transactional data to a financial system of record
- Code-first notebook reporting (marimo, Hex, Streamlit, Quarto)

Hiring process: Recruiter Interview → Take-Home Assignment → Hiring Manager Zoom → Team Interview → Hired.
