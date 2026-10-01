# Undisclosed (recruiter) — Enterprise Data Engineer, financial markets tech firm — 2026-10

## Metadata
- Date: 2026-10-01
- Status: REJECTED (2026-10-01): recruiter hard filter, immediate start required (Kris available January 2027, BNP internship runs to December 2026)
- Fit Score: Medium-Low as posted — the stack is a near-perfect match (dbt, SQL, PySpark, dimensional modeling, semantic layer and standardised KPIs, governance/quality, CI/CD testing, Finance as a domain). But "up to ~€200k" signals a senior/lead hire, and the employer is undisclosed.
- Source: LinkedIn (recruiter post)
- Contract: unknown
- Location: Amsterdam, Netherlands

## Read on the employer and level
- A €200k ceiling for a data engineer in Amsterdam "within the financial markets space" almost certainly means a proprietary trading / market-making firm (that pay scale is typical of the Amsterdam trading cluster). These firms pay very high but do hire juniors on separate, lower bands.
- "Enterprise" data (Finance, People, Business Operations) = the corporate/back-office data platform, not trading data. That's the AE side of the house, where your dimensional modeling + semantic layer + finance domain fit best.
- "Shape a modern data platform from the ground up" + "significant ownership" reads senior. Don't spend a tailored build until the level is confirmed.

## Visa
- "Visa sponsorship available" is stated. Check the actual employer against the IND register once the recruiter names it.

## CV
- `output/cv_kris_huang_eng.pdf` (Booking treasury build): grain, SCD Type 2, reconciliation over three sources, Airflow, semantic layer + LLM agent, PySpark in skills, CFA (finance domain).
- If it progresses and the level fits: a tailored variant-b build leading with "semantic layer and standardised KPIs over a dimensional model, data-quality tests, CI" and adding Databricks only after the Free Edition port is actually done.

## Recruiter message (draft)
Hi [name], thanks for posting the Enterprise Data Engineer role. The stack is very close to what I work with: dbt and SQL on a dimensional model with a semantic layer for standardised KPIs, data-quality testing, and PySpark, with a finance-data background (BNP Paribas Securities Services, CFA Charterholder). Two quick questions before I send my CV: what seniority is the hiring team targeting, and would a strong early-career profile (graduating January 2027) be considered? I'm in Paris and would relocate to Amsterdam, so it's good to see sponsorship is available. Happy to share my CV and portfolio project.

## Prep (only if it progresses)
- Data Vault 2.0: hubs/links/satellites, when to put a vault between staging and the dimensional layer, hash keys, and how it compares with your SCD Type 2 approach.
- Medallion on Databricks: bronze/silver/gold, Delta Lake, Unity Catalog lineage; dbt-databricks.
- Enterprise domains: GL/finance cube, HR headcount and attrition (SCD on employee records), standardised KPI definitions in a semantic layer.
- CI/CD for dbt: slim CI with `state:modified+`, tests as PR gates.

## Raw JD
Enterprise Data Engineer | Amsterdam | Up to €200,000. High-performing technology organisation in the financial markets space building a next-generation enterprise data platform. Hands-on; significant ownership over how data is modelled, governed and consumed across Finance, People and Business Operations.
Stack: Databricks / Lakehouse; dbt, SQL and PySpark; scalable ELT; dimensional, medallion and Data Vault modelling; semantic layers and standardised KPIs; data governance, lineage and quality; CI/CD and automated testing; BI and self-service analytics.
Interested in engineers with strong SQL and dbt who have built modern analytics/data platforms and work directly with business stakeholders; Databricks/Lakehouse highly valuable.
Amsterdam; compensation up to ~€200,000; relocation support and visa sponsorship; shape a platform from the ground up.
