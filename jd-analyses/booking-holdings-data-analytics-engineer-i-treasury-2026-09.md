# Booking Holdings — Data Analytics Engineer I (Treasury Data Science & Analytics) — 2026-09

## Metadata
- Date: 2026-09-29 (just posted)
- Fit Score: HIGH. Probably the best-aligned JD of the whole search. Junior level (I, 1–3 years); dbt + PySpark + Snowflake; explicit grain/historical coverage; automated DQ incl. reconciliation; workflow management with retries/backfills; Snowflake semantic views for AI-assisted analytics (= your LLM agent over a semantic layer); Streamlit; and the domain is Group Treasury (cash-flow forecasting, liquidity, risk), where the CFA is real domain evidence. Gaps: Docker/Kubernetes, Tableau/Grafana, production on-call/monitoring, "local candidates prioritised".
- Tailoring effort: LOW (Variant A summary swap; skills same as the Marktlink build).
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: Not stated in the paste. Booking Holdings/Booking.com treasury teams sit in Amsterdam; confirm. Hybrid, 2 days in office. "Local candidates will be prioritised."
- Compensation: Not stated. Big-tech NL pay should clear the HSM threshold easily.
- Company: Booking Holdings (Booking.com, Priceline, Agoda, KAYAK, OpenTable). Team: Treasury Data Science & Analytics, analysts + data scientists; you'd be the first and only Analytics Engineer.

## Before applying
- IND sponsor: check the register for the employing entity (Booking.com B.V. / Booking Holdings entity in NL). Almost certainly recognised; verify as you did for Marktlink.
- "Local candidates prioritised": in the application/note, state it plainly: based in Paris, relocating to Amsterdam, available from Jan 2027 (after BNP ends Dec 2026), eligible via the NL orientation-year route / HSM with a recognised sponsor. Removes the uncertainty that gets non-local CVs filtered.

## CV Tailoring Instructions (for Claude Code)
Variant: A (Financial Data Infrastructure). ENGLISH CV.
Branch: `variant-a-finance` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
Start from the branch state after the Marktlink edits (skills reorder etc.). If those aren't applied yet, apply the Marktlink skills steps (2–3 in that file) first.
1. Summary: comment out the current active summary, add a `% Booking Holdings Treasury (AE I) —` label comment, then set as the active text:
   "Analytics Engineer with finance domain depth: dbt models on Snowflake with explicit grain and SCD Type 2 history, automated data-quality and reconciliation checks over three source systems (BNP Paribas Securities Services), Airflow orchestration with retries and idempotent reruns, and an LLM agent over a semantic layer. \textbf{CFA Charterholder}."
   Must not exceed the current summary's line count. If it wraps, drop "over three source systems", then "with retries and idempotent reruns".
2. Skills: same as the Marktlink build (Modeling → Transformation → Warehousing; Snowflake first; Streamlit/Claude Code only if no wrap). If "dbt Semantic Layer" can become "dbt Semantic Layer (MetricFlow)" without wrapping, do it (maps to their semantic views).
3. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_booking_holdings_data_analytics_engineer_i_treasury.pdf`.
CFA positioning: summary (Treasury = finance domain).
Optional adds: none.

## Cover Letter Angle
Their bullets read like a description of your last year. Curated datasets with "clearly defined granularity, historical coverage and schedules": at BNP you declared the grain of a private-capital deal model, versioned clients with SCD Type 2, and reconciled three manually maintained source systems. "Recency, completeness, uniqueness, reconciliation" checks: your BNP data-quality framework and pc_pipeline's dbt test suite (6 defect classes). "Scheduling, dependencies, retries, backfills": pc_pipeline's Airflow DAG (task groups in dependency order, retries, idempotent reruns). "Snowflake semantic views … for AI-assisted analytics": you built exactly that pattern with MetricFlow + an LLM agent that turns natural-language questions into validated SQL, and you know why agreed metric definitions are what make AI analytics trustworthy. For Treasury specifically: as a CFA charterholder you understand cash-flow forecasting, liquidity and FX risk from the business side, so you can talk to finance stakeholders without translation. That matters for the first and only AE on a team of analysts and data scientists.

## Preparation Gaps
- Snowflake semantic views: `CREATE SEMANTIC VIEW` (tables, relationships, dimensions, facts, metrics), how Cortex Analyst uses them, and the mapping from your MetricFlow semantic models/metrics. Rebuild 2–3 pc_pipeline metrics as a semantic view in a Snowflake trial. It's the best possible talking point.
- Treasury data: cash positions by entity/bank/currency, bank statement feeds (MT940 / camt.053), intercompany flows, FX exposure, cash-flow forecasting (actuals vs forecast grain), liquidity buffers. Model "daily cash position" as a periodic snapshot fact.
- Workflow ops: backfills (partitioned/idempotent, `--full-refresh` vs incremental in dbt), alerting, SLAs, incident triage from logs.
- DQ extras: schema-change detection (dbt contracts, source schema tests), reconciliation tests against source totals.
- Docker/Kubernetes basics: build/run an image, read pod logs, restart jobs. The bar is "troubleshoot within existing environments", not administer.
- PySpark performance (execution time, resource efficiency): partitioning, broadcast joins, caching, spill.
- Workflow migration: how you'd migrate legacy scripts/notebooks to dbt + an orchestrator safely (parallel run, reconciliation of outputs, cut-over).

## Stack Analysis

### Have
- SQL, Python, dbt (core)
- Analytical/dimensional modeling with grain + history (BNP SCD2, pc_pipeline star schema)
- Automated DQ + reconciliation (BNP framework, dbt tests)
- Orchestration with dependencies/retries/idempotency (Airflow DAG)
- Snowflake; PySpark (TripAdvisor); Git
- Semantic layer for AI-assisted analytics (MetricFlow + LLM agent)
- Streamlit; Power BI (dashboards)
- Finance domain: CFA, BNP Securities Services
- Stakeholder communication with finance users (BNP)
- Basic stats/ML concepts (MSc DSBA)

### Missing
- Docker/Kubernetes hands-on troubleshooting
- Tableau, Grafana
- Production on-call/incident resolution
- Snowflake semantic views specifically (the concept is held)

### Partial
- CI/CD: Git discipline, no owned pipeline
- API integration: light
- Data governance/access controls: concept + BNP exposure

### Green Flags
- Junior level explicitly (I, 1–3 years)
- dbt + Snowflake + PySpark + semantic layer + Streamlit: your exact stack
- Finance/Treasury domain inside a tech company: the best of both
- Clear, specific, engineering-literate JD (grain, backfills, reconciliation, schema-change detection)
- "With guidance on complex design decisions": support for a junior
- AI-assisted analytics is explicitly in scope

### Red Flags
- "Local candidates will be prioritised": relocation hurdle (address it up front)
- First and only AE on the team: little AE peer mentoring (engineering standards exist, though)
- Docker/Kubernetes in requirements
- Outside France: residency-clock trade-off
- No age-discrimination wording

## Notes
- Verdict: APPLY, top priority. Tailor carefully and apply fast (just posted). Look for a referral: ESSEC/CentraleSupélec alumni at Booking.com Amsterdam, ideally in finance/treasury data.
- If both this and Marktlink progress, this is the stronger long-term base: big-tech engineering standards + finance domain + junior-appropriate support.

## Raw JD (abridged)
Booking Holdings — Treasury Data Science & Analytics team (cash-flow forecasting, liquidity optimization, risk modelling, reporting, self-service analytics for Group Treasury). Data Analytics Engineer I: design/develop/maintain analytical data models, pipelines, reusable assets; own migration/modernisation deliverables; establish practices for developing, deploying, scheduling, monitoring pipelines; first and only AE; partner with finance stakeholders; guidance on complex design. Hybrid, 2 days in office; local candidates prioritised.
Duties: own workflow migration; dbt + PySpark assets/pipelines (efficiency); multi-source integration into curated datasets with consistent definitions, granularity, history, schedules; workflow management (scheduling, dependencies, retries, backfills, monitoring, alerting, incidents); automated DQ (recency, completeness, uniqueness, reconciliation, schema-change detection, critical metrics); processing/integration components for analytical apps and automation; Snowflake semantic views + metric definitions for self-service and AI-assisted analytics; governance, access control, lineage, documentation.
Requirements: 1–3 years AE/DE/DWH or related; CS or related degree or equivalent; strong SQL; Python; analytical modelling (granularity, relationships, aggregation, history); dbt or similar; RDBMS/cloud DW (Snowflake beneficial); scheduled workflows + logs/monitoring/alerts; automated DQ + validation against source; Git, code review, testing, CI/CD; cloud services + troubleshooting containers in Docker/Kubernetes; exploration/visualization + stakeholder explanation; governance/security fundamentals; communication.
Desirable: Snowflake; PySpark/Spark SQL; Tableau/Grafana/Streamlit; Snowflake semantic views or similar; data for forecasting/predictive models.
Stack: SQL, Python; Snowflake; dbt, Spark; Docker, Kubernetes; Tableau, Streamlit, Grafana; Snowflake semantic views; Git; code review, testing, CI/CD.
