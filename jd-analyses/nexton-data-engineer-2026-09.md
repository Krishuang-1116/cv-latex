# NEXTON — Data Engineer (CDI, client mission: usage & subscription data) — 2026-09

## Metadata
- Date: 2026-09-29
- Fit Score: Medium. The mission is pipelines + data reliability + making data available to analytics/BI teams + tracking usage/subscription KPIs, which is squarely your BNP + pc_pipeline story. Held back by: an ESN (off-lane category), no stack named at all (the real tools depend on the client), API development listed as a mastered skill (your gap), and "expérience réussie" wording (soft, no number).
- Tailoring effort: LOW (summary swap only, French CV).
- Source: LinkedIn (direct paste, French JD)
- Contract: CDI
- Location: Paris (client site)
- Compensation: Not stated. Confirm it clears the Passeport Talent threshold.
- Company: NEXTON, ~450 people, ESN/consulting/"Factory" hybrid founded 2011. Clients: SNCF, Orange, BNP Paribas, pure players. The "usages et abonnements" focus suggests a telecom/transport/subscription client (Orange or SNCF plausible; unconfirmed).

## CV Tailoring Instructions (for Claude Code)
Variant: B (General Modern Stack), FRENCH CV.
Branch: `feature/french` (edit `french/resume_french_base.tex`). Follow `french/CLAUDE.md`: feminine agreement, nominal style, one page, don't touch geometry/fonts, don't commit.
1. Summary: comment out the current active summary line (keep it as a `%` line, with a one-line `% NEXTON (Data Engineer) —` label comment above the new text, like the existing variant history), then add as the new active text:
   "Data Engineer orientée fiabilité — conception de pipelines ELT (dbt, Airflow, SQL, Python) et de modèles de données testés et documentés, mis à disposition des équipes analytics et BI (Snowflake, Power BI). Mise en place d'un framework de qualité des données sur des sources hétérogènes chez BNP Paribas Securities Services."
   (It must stay within the current summary's line count; if it wraps to an extra line, drop "(Snowflake, Power BI)".)
2. Skills: no change.
3. CFA: stays out of the summary (it remains under Formation).
4. Rebuild with tectonic, confirm one page, then export: `cp` the build PDF to `output/cv_kris_huang_fr_nexton_data_engineer.pdf`.
Summary line (English, for reference / if ever sent in English): "Reliability-focused Data Engineer: ELT pipelines (dbt, Airflow, SQL, Python) and tested, documented data models served to analytics and BI teams (Snowflake, Power BI). Built a data-quality framework over heterogeneous sources at BNP Paribas Securities Services."
Optional adds: none.

## Cover Letter Angle
Short, in French. Their key phrase is "fiabilisation": collecting, reconciling and serving usage/subscription data that analysts and reporting can trust. At BNP you integrated three heterogeneous, manually maintained sources into one dimensional model, and built a data-quality framework that catches identity-resolution failures, duplicates and cross-source code inconsistencies. That's the same failure mode as duplicate subscribers or mismatched usage events. pc_pipeline shows the modern-stack version end to end: dbt layers with tests for 6 defect classes, an Airflow DAG, a semantic layer defining metrics once, so KPIs like active subscribers or churn mean the same thing in every report.

## Preparation Gaps
- Subscription/usage metrics modeling: active subscribers (grain, snapshot vs event tables), churn, MRR/ARPU, cohorts, and SCD2 on subscription plans (you know SCD2 — map it to plan changes, upgrades, cancellations).
- Event/usage data: late-arriving events, deduplication, incremental models (dbt incremental + unique_key), idempotent reloads.
- API development: the stated gap. Minimum: a small FastAPI endpoint serving one pc_pipeline mart (pagination, auth basics). Also know how to *consume* REST APIs as sources (pagination, rate limits, retries) — likely what "développement d'API" means for ingestion.
- Stack-agnostic readiness: be ready to discuss the same design on a GCP/BigQuery or Azure client stack, since the JD names none.

## Stack Analysis

### Have
- ETL/ELT pipelines: dbt + Airflow (pc_pipeline); PySpark (TripAdvisor)
- Integration of heterogeneous sources: BNP three-source model
- Data serving for analytics/BI: marts + semantic layer; Power BI; Sales Analytics warehouse
- KPI tracking: Sales Analytics KPI monitoring; semantic-layer metric definitions
- Data quality/reliability ("fiabilisation"): BNP DQ framework, dbt test suite
- Databases: PostgreSQL, DuckDB, Snowflake

### Missing
- API development (production)
- Professional Data Engineer title / "expérience réussie" in DE
- Subscription/usage-data domain

### Partial
- API: light FastAPI exposure (off-CV)
- Cloud: AWS familiar; client cloud unknown

### Green Flags
- CDI, Paris
- Reliability + analytics serving is the core, not an afterthought
- Specific domain (usage & subscriptions)
- Training/community support

### Red Flags
- ESN: client-mission model (off-lane)
- No stack named: generic JD, the real tools depend on the client
- "Maîtrise" of API development as a requirement
- No age-discrimination wording

## Notes
- Verdict: apply, with only the summary swap. A cheap application with a decent functional match; ranks with Devoteam/Sia/Valtech as a consultancy fallback, below in-house product targets.
- If interviewed, ask which client and which stack first; that decides whether it's a modern-stack mission (worth it) or legacy ETL.

## Raw JD (abridged)
NEXTON (fondée 2011, 450+ experts; conseil + Factory + ESN; clients SNCF, Orange, BNP Paribas, pure players). Data Engineer H/F, CDI, Paris, pour un grand compte client: mise en œuvre et évolution des pipelines de données, focus collecte, fiabilisation et exploitation des données liées aux usages et aux abonnements.
Missions: développer/maintenir les pipelines (flux automatisés); intégrer des sources hétérogènes; préparer et structurer les données pour les équipes analytics et les outils de reporting; suivre les métriques d'usages, d'abonnements et les KPI globaux.
Profil: Bac+5; expérience réussie en Data Engineering et pipelines; maîtrise ETL/ELT, développement d'API, gestion des bases de données; expérience avérée dans la mise à disposition de données pour l'Analytics/BI; qualité, rigueur, sensibilité à la fiabilisation.
Avantages: communautés, meetups, formations, événements, forfait mobilité durable, téléphone.
