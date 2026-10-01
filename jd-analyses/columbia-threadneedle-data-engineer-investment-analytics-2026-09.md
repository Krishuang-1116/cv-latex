# Columbia Threadneedle Investments — Data Engineer (Investment Analytics, Multi-Manager) — 2026-09

## Metadata
- Date: 2026-09-30
- Status: To apply — tailored Variant A build (instructions below)
- Fit Score: Medium-High — the domain is an unusually close match (investment data, performance and risk reporting, manager selection; CFA explicitly preferred; BNP Securities Services + Guosen product monitoring). The stack is a partial match: Python and SQL are strong, but there's no R, and quant work (attribution, factor backtesting) is off-CV.
- Source: LinkedIn
- Contract: Permanent, full time
- Location: assumed London (the team spans Boston, New York, London and India; confirm on the posting). 4 days a week in office.

## Visa / Contract
- UK Skilled Worker route. Sponsor register: **Threadneedle Management Services Limited, London, Worker (A rating), Skilled Worker**; the Senior or Specialist Worker route is also listed. Confirm it's the employing entity.
- Salary must be at least £41,700 or the going rate (the new-entrant floor may apply). A London asset-manager data engineer role should clear that; confirm the band.
- The right-to-work answer is the standard one: "do not have the right to work in the UK and would require company visa sponsorship".

## CV Tailoring Instructions
Variant: A
Branch: variant-a-finance
Output: output/cv_kris_huang_columbia_threadneedle_data_engineer_investment_analytics.pdf

1. Summary (English), replacing the active Booking summary (comment it out with a `% Columbia Threadneedle ...` label, per convention):
   Data engineer for investment teams: designed a dimensional model and data-quality framework for private capital data across three source systems at BNP Paribas Securities Services, and automated recurring reporting in Python and Power BI; previously monitored 100+ private equity products weekly with structured performance reports. \textbf{CFA Charterholder}.
2. Restore Guosen (Financial Product Analyst, Oct 2022 – Mar 2024) exactly as commented. Weekly monitoring of 100+ approved products with performance reports is the closest thing on file to multi-manager oversight and manager selection.
3. Pay for it by commenting out the TripAdvisor project (the documented Guosen ↔ TripAdvisor swap pair). Update the swap comment to note Columbia Threadneedle.
4. Skills: with TripAdvisor gone, PySpark loses its on-CV evidence. In the Programming line, replace "PySpark" with "Excel VBA" (evidenced by the ESSEC RA entry and the BNP deal-monitoring automation). Do NOT add R, Bloomberg or FactSet.
5. CFA: keep it bolded in the summary. It's in their preferred qualifications.
Optional adds: UOB stays commented (one-page budget); mention credit/risk in the cover letter instead.
One-page check: Guosen (3 lines) vs TripAdvisor (≈3 lines) should net to about zero. Recompile and confirm the clearance.

## Cover Letter Angle
Multi-manager oversight runs on the same problem I have worked on from both sides: investment data that arrives from many sources and has to be made trustworthy before anyone can compare managers on it. At Guosen Securities I monitored more than 100 approved private equity products every week and turned them into structured performance reports for investment monitoring. At BNP Paribas Securities Services I now build the data side of that work: a dimensional model and a data-quality framework that catch identity mismatches, duplicates and inconsistent codes across three source systems, plus automations that replaced manual reporting steps. As a CFA Charterholder with a master's in international economics and finance, I can talk attribution and risk with Coverage Analysts and then build the pipeline that feeds it: tested, documented and version-controlled, as your model governance standard asks.

## Preparation Gaps
- **Performance attribution:** Brinson-Fachler (allocation, selection, interaction), arithmetic vs geometric linking across periods, and returns-based vs holdings-based attribution for external managers (a multi-manager team often only has returns). Be able to say what data grain each one needs.
- **Manager selection data:** eVestment/Morningstar peer universes, survivorship bias, tracking error, information ratio, up/down capture, style drift via returns-based style analysis. Link it to your Guosen weekly monitoring.
- **Factor research and backtesting, concept level:** factor exposures via regression, look-ahead bias, point-in-time data (why the SCD Type 2 "as-of" history you built is exactly what a backtest needs, a strong bridge from your AE work).
- **R:** they list it as advanced-required. Don't claim it. Be honest in the interview that you're Python-first, and learn enough tidyverse to read colleagues' scripts.
- **Model governance:** documentation, version control, validation protocols; map these to dbt tests/docs + Git in pc_pipeline.
- **Data platforms:** what Aladdin, FactSet and Bloomberg feeds look like (security master, holdings, prices, benchmarks) and how you'd reconcile them. This is the BNP reconciliation story again.

## Stack Analysis

### Have
- Python, SQL (advanced), database platforms (PostgreSQL, Snowflake, DuckDB)
- Data quality and validation across multiple sources (BNP framework)
- Reporting automation and dashboards (Power BI/DAX, Python pandas/openpyxl, Excel VBA)
- Version control and documentation (Git, dbt tests/docs)
- Investment domain: CFA, JHU MA International Economics & Finance, private capital data (BNP), PE product monitoring (Guosen), credit analysis (UOB)
- AI/ML exposure (LLM agent, RAG, LLM-as-judge at LVMH)

### Missing
- R (listed as advanced-required)
- Performance attribution systems, factor models, backtesting in practice
- Bloomberg / FactSet / Morningstar / eVestment / Aladdin hands-on
- FRM (CFA covers the certification preference)

### Partial
- AWS (familiar); no Azure
- Investment consulting / multi-manager background: adjacent via Guosen product monitoring and BNP Securities Services
- Quant modeling: statistics and ML from the DS master's, not investment-quant production

### Green Flags
- CFA explicitly preferred, so the domain differentiator counts at screening
- Hands-on ownership: data quality, automation, governance, AI/ML evaluation
- A specific domain (multi-manager solutions, manager selection, investment oversight)
- A sponsor-licensed A-rated UK entity

### Red Flags
- An asset manager inside Ameriprise: a traditional financial institution, which was an original "not interested" filter (softened since the search broadened)
- Title says Data Engineering, but duties lean quant analytics + reporting + dashboards (risk of a BI-heavy role); no transformation layer or modern stack named
- R required at an advanced level
- 4 days a week in office

## Raw JD
About Columbia Threadneedle Investments — global team of 2,300, 550+ investment professionals; part of Ameriprise Financial (with RiverSource).

Job Description — Join the Data Engineering team shaping data, analytics and reporting for investment oversight, research, portfolio construction and manager selection. Partner with Coverage Analysts, Investment Strategy & Research and Multi-Manager Solutions. Hands-on role with ownership, cross-functional influence, data quality, workflow automation and new analytical capabilities.

Responsibilities
- Partner with Coverage Analysts, IS&R and MMS professionals; translate analytical needs into data solutions, models and reporting
- Participate in research discussions and project planning
- Source, validate and maintain investment data across platforms and databases; reliable data feeds
- Build, maintain and enhance quantitative models, analytical tools and performance attribution systems (backtesting, scenario analysis, factor-based research)
- Automate recurring analytical and reporting workflows (performance reports, risk metrics, strategy dashboards)
- Design and maintain dashboards and data visualisations
- Apply model governance: documentation, version control, validation protocols
- Evaluate new technologies incl. AI and ML; support product development and market research
- Collaborate with Enterprise Technology, IT and Investment Risk Management; teams across Boston, New York, London and India

Required
- Prior experience in data analytics, quantitative development or reporting within investment management or financial services; strong knowledge of investment data, portfolio analytics, performance attribution and risk
- Bachelor's or Master's in mathematics, statistics, CS, data science or related
- Advanced Python, R and SQL; database platforms
- Strong communication; manage multiple priorities; initiative and problem solving

Preferred
- CFA or FRM
- AWS or Azure, big data or BI tools
- Bloomberg, FactSet, Morningstar, eVestment or Aladdin
- Investment consulting, multi-manager investing or investment operations

In-office at least 4 days/week. Full time, Permanent. Job Family Group: Investment Management.
