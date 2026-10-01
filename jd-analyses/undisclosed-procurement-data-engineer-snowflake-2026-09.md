# Undisclosed (likely ESN/mission) — Data Engineer Snowflake, Data & AI Procurement — 2026-09

## Metadata
- Status: TO APPLY (recently posted, so apply quickly; qualify contract type first)
- Date: 2026-09-30
- Fit Score: HIGH on stack. Every must-have is your stack: SQL, Python, Snowflake, dbt modelling/transformations, Airflow. Nice-to-haves (tests, docs, CI/CD) are covered by pc_pipeline; GitLab ≈ GitHub. Gaps: "maîtrise avancée" of Python, and production (not portfolio) Snowflake/Airflow.
- Tailoring effort: NONE. Reuse the Devoteam FR build (Snowflake & dbt MDS engineer), which is the closest existing match. Alternative if they want an English CV (team works in English): `cv_kris_huang_valtech_data_engineer_snowflake.pdf`.
- Source: LinkedIn (direct paste)
- Contract: NOT STATED. The format ("Must Haves / Nice to Have / Détails contextuels") reads like an ESN staffing or freelance mission for a large corporate client's Procurement data team.
- Location: Not stated ("International", work in English); presumably Paris/France.
- Compensation: Not stated

## Work authorization
- Only a salaried CDI/CDD (or CDI with an ESN) works for Passeport Talent. Freelance/portage salarial/mission-only = NOT viable. First question: "Is this a CDI with your company, or a freelance mission?"
- Salary must clear the Passeport Talent threshold (≈€39.6k–43.8k, 2026; confirm).

## CV Tailoring Instructions
No new build. Send `output/cv_kris_huang_fr_devoteam.pdf` (French, Snowflake + dbt-forward) under a neutral filename. If the process runs in English, send `output/cv_kris_huang_valtech_data_engineer_snowflake.pdf`.
Summary line (English, for reference only): unchanged from the Valtech build.
CFA positioning: as in the reused builds.
Optional adds: none.

## Cover Letter Angle
Your Data Foundation team ingests varied sources into Snowflake, models them with dbt, and orchestrates with Airflow for business analysts. pc_pipeline is that pipeline end to end: raw sources → staging → intermediate → marts on Snowflake, dbt tests covering six defect classes, docs, and an Airflow DAG. At BNP Paribas you work with business users on messy, manually maintained data across three systems (identity resolution, duplicates, code inconsistencies). That's the kind of work procurement data involves: supplier master data, spend categories and purchase orders from several ERPs. Working in English is a plus for you (TOEFL 120).

## Preparation Gaps
- Procurement data domain: spend analysis, supplier master data dedup/matching, category taxonomies (UNSPSC), PO → invoice → payment (P2P) flow, savings tracking.
- Snowflake ingestion: stages, COPY INTO, Snowpipe, file formats; streams & tasks; cost/warehouse sizing.
- dbt at team scale: incremental models (merge), snapshots (SCD2), packages, slim CI in GitLab CI.
- Airflow: DAG design, sensors, retries, idempotency, triggering dbt (Cosmos / BashOperator).
- Python "advanced": typing, testing (pytest), packaging, API ingestion with pagination/retries.

## Stack Analysis

### Have
- SQL (CTEs, window functions); Python
- Snowflake; dbt modelling + tests + docs; Airflow DAG (pc_pipeline)
- Git; clean code/testing/documentation practice
- Business-facing requirement gathering (BNP)

### Missing
- Production Snowflake/Airflow experience
- GitLab CI specifically

### Partial
- "Advanced" Python (solid scripting/pandas/openpyxl; not software-engineering depth)
- CI/CD (slim CI planned in pc_pipeline v2)

### Green Flags
- Exact modern stack; engineering scope (ingestion + transformation, end-to-end)
- Works in English, inside a Data Foundation team with other DEs

### Red Flags
- Contract type unknown: freelance/mission = not viable for the titre de séjour
- Likely ESN placement for a corporate client (procurement); the end client is unknown
- Vague on seniority (could expect 3+ years in practice)

## Notes
- Verdict: APPLY now with the Devoteam FR CV; confirm salaried CDI on first contact.

## Raw JD
Résumé: Le poste de Data Engineer sur Snowflake a pour objectif principal d'intégrer l'équipe Data & AI Procurement, en se concentrant sur l'ingestion et la transformation des données, afin de répondre aux besoins des métiers.
Responsabilités: ingestion et transformation des données à partir de sources variées; pipelines de bout en bout; collaborer avec les Data Analysts; travailler avec d'autres Data Engineers sur les bonnes pratiques.
Must Haves: SQL avancé; Python avancé; Snowflake; dbt (modélisation, transformations); Airflow.
Nice to Have: Gitlab; bonnes pratiques (clean code, tests, documentation, CI/CD).
Détails: International, échanges en anglais; équipe Data Foundation; projet Data Foundation.
