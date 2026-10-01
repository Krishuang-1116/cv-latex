# Dojo — Analytics Engineer (Partnerships & Sales Compensation) — 2026-09

## Metadata
- Status: TO APPLY TODAY (posted minutes ago; early applicants get read)
- Date: 2026-09-30
- Fit Score: HIGH. dbt + Airflow + Python data-quality automation + reusable metrics + AI-assisted modelling/testing/docs = pc_pipeline plus your workflow. The domain (incentive/commission data paying out tens of millions of pounds a month) rewards financial-grade accuracy and reconciliation, which is your CFA + BNP data-quality angle. Gaps: BigQuery (you have Snowflake), Looker (Power BI), Airbyte/Fivetran (concept only). "Independently own" implies mid-level, but there's no year gate.
- Tailoring effort: LOW, and worth it. The Lendable build leads with Snowflake; this is a BigQuery shop, so use a warehouse-neutral, accuracy/metrics-forward summary.
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: Not stated; Dojo HQ is London. Office-first, 4+ days/week.
- Compensation: Not stated
- Company: Dojo (legal entity Paymentsense Limited), UK card acquirer for in-person commerce, 150k+ customers, 4 countries. Team builds sales/partner incentive & compensation data products.

## UK work authorization (checked 2026-09-30, grep on reference/uk-licensed-sponsors.csv, register 2026-09-29)
- Sponsor: CONFIRMED. "Paymentsense Limited", London, Worker (A rating), Skilled Worker. Dojo is the trading name of Paymentsense. Confirm the employing entity and the office city (Dojo also has other European offices).
- Salary must clear £41,700 or the going rate; ask early.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), accuracy + reusable-metrics-forward. ENGLISH CV.
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the active summary, add a `% Dojo AE (Partnerships & Sales Compensation) -- dbt + DQ + reusable metrics, warehouse-neutral; CFA kept (payout accuracy):` label, then set as the active text:
   "Analytics Engineer who builds data products where the numbers must be right: tested dbt models (6 defect classes) with Airflow orchestration and Python data-quality automation, reusable metrics defined once in a semantic layer, and a data-quality framework reconciling three private-capital source systems at BNP Paribas. AI-assisted modelling and docs (Claude Code). \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps, drop "(Claude Code)", then "(6 defect classes)".
2. Skills: Warehousing → "Snowflake, PostgreSQL, DuckDB" (keep; do NOT claim BigQuery). BI & Semantic → "Power BI (DAX), dbt Semantic Layer". Programming → "Python, Git, coding agents (Claude Code)" if it fits.
3. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_dojo_analytics_engineer.pdf`. Attach under a neutral filename.
Fallback if the build can't happen today: `output/cv_kris_huang_lendable_analytics_data_engineer_python_infrastructure.pdf` (don't wait; speed matters here).

## Cover Letter Angle
Your team's data products decide what partners and salespeople get paid, so a wrong join is a wrong payout. That's the standard I work to. At BNP Paribas I reconciled private-capital deal data across three manually maintained systems, and I built checks that catch identity mismatches, duplicates and code inconsistencies before they reach a report. In pc_pipeline, dbt tests cover six defect classes, metrics are defined once in a semantic layer so every consumer gets the same number, and Airflow runs the pipeline. As a CFA Charterholder I read commission and incentive logic as financial contracts: tiers, clawbacks, effective dates. That's where compensation data usually breaks.

## Preparation Gaps
- Sales compensation data modelling: plan/tier/rate tables as SCD2 with effective dates, accelerators, clawbacks, splits, and payout reconciliation vs finance; auditability (reproduce last month's payout exactly).
- Acquiring basics: merchant acquiring economics (MSC, interchange++, scheme fees), TPV, merchant churn, partner/ISO channels. Commissions are typically based on these.
- BigQuery: partitioning/clustering, slot vs on-demand pricing, cost-conscious dbt (incremental + partition pruning, `require_partition_filter`), dbt-bigquery specifics.
- Looker/LookML: views, explores, derived tables; how LookML relates to dbt metrics.
- Airbyte/Fivetran: connector sync modes (incremental vs full), CDC, schema drift handling.
- Tech-debt paydown stories: refactoring a model, deprecating duplicate metrics.

## Stack Analysis

### Have
- SQL; dbt models + tests + docs; Airflow; Python for DQ/automation
- Reusable metrics (dbt Semantic Layer); data quality judgment
- AI-assisted development (Claude Code)
- Financial accuracy/reconciliation mindset (CFA, BNP)

### Missing
- BigQuery hands-on
- Looker
- Airbyte/Fivetran in practice

### Partial
- Cloud DW (Snowflake instead of BigQuery: transferable)
- BI (Power BI instead of Looker)
- Independent ownership in production (BNP workstreams, but internship)

### Green Flags
- In-house fintech; high-stakes, clearly scoped domain
- Modern stack; standards, reusable metrics, tech-debt culture
- Responsible AI-assisted development explicitly valued
- Licensed A-rated sponsor

### Red Flags
- Office 4+ days/week
- "Independently own workstreams": likely wants some production AE experience
- BigQuery + Looker preferred (your stack is Snowflake + Power BI)
- Values copy leans on hustle ("relentless")

## Notes
- Verdict: APPLY today. Tailored build if Claude Code is free within the hour; otherwise send the Lendable PDF now.

## Raw JD (abridged)
Dojo, Analytics Engineer. UK's largest acquirer for in-person commerce; 150k+ customers, 4 countries. Own AE workstreams end to end, deliver data products, contribute reusable standards; dbt, Airflow, BigQuery, BI. Team: data solutions to incentivise and compensate Partnerships and Sales channels, paying out tens of millions of pounds monthly.
Do: own workstream end to end; cost-conscious BigQuery pipelines with dbt + data viz; orchestration with Airflow, dbt, Airbyte, Fivetran; Python automation and DQ validation; shared standards, reusable metrics, tech-debt paydown; AI tools for modelling/testing/docs with ownership.
Bring: technical quality + business impact; AE/DE background; strong SQL + dbt; cloud DW (pref BigQuery), BI (ideally Looker); Airflow, Airbyte/Fivetran; practical Python; judgment on DQ/maintainability; independent technical decisions.
Office-first, 4+ days/week. Values: curious, relentless, customer-obsessed.
