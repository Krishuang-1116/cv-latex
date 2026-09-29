# Devoteam (Snowflake Partner entity) — Modern Data Stack Engineer (Snowflake & dbt) — 2026-09

## Metadata
- Date: 2026-09-29 (reposted 6 days ago, 200+ applicants)
- Fit Score: Medium. The stack is a near-exact match (Snowflake + dbt indispensable, SQL/Python, and Streamlit/GenAI as "atout sérieux" — pc_pipeline has all of these). Held back by "expérience significative" + "expertise avérée" wording, 200+ applicants, and the ESN/consulting model (off-lane category, but a modern-stack one).
- Tailoring effort: LOW. Reuse an existing CV; at most one word added (see below).
- Source: LinkedIn (direct paste, French JD)
- Contract: Not stated (CDI expected)
- Location: Not stated. Devoteam HQ is in the Paris region; confirm. Client-facing missions.
- Compensation: Not stated. Confirm it clears the Passeport Talent threshold.
- Company: Devoteam, a large tech consultancy (ESN). A brand-new internal entity dedicated to Snowflake integration for clients ("pionniers").

## Why reposted + 200 applicants
- Reposting usually means the first round didn't produce a hire: likely few candidates with real Snowflake + dbt production experience. That helps a candidate whose CV shows both clearly.
- 200+ applicants is the Devoteam brand + generic "Data Engineer" title + LinkedIn Easy Apply volume. Much of that pool won't have dbt at all.
- A new entity staffing up = more openness to strong juniors who can be certified fast.

## CV Tailoring Instructions
Variant: B. The JD is in French → FRENCH CV preferred; English is acceptable (Devoteam is international).
Branch: reuse, don't rebuild.
- French: `output/cv_kris_huang_fr_sia_partners.pdf` (modern-stack consultancy framing) — usable as-is.
- English: `output/cv_kris_huang_valtech_data_engineer_snowflake.pdf` (Snowflake DE framing) — usable as-is.
Only optional change (one word, via Claude Code): add "Streamlit" to the pc_pipeline tech line (`dbt | Airflow | Snowflake | SQL` → `dbt | Airflow | Snowflake | Streamlit | SQL`), because Streamlit is named as an "atout sérieux" and isn't currently visible on the CV. Only if the Streamlit app is real and in the repo.
Summary line (French): reuse the Sia line: "Analytics Engineer sur stack moderne (dbt, Snowflake, Airflow, SQL avancé) avec une vraie rigueur qualité/documentation et le sens du dialogue métier — je transforme des données brutes en produits data fiables et exploitables, de la modélisation à la restitution."
Summary line (English): reuse the Valtech line.
Skills reorder: none.
CFA positioning: as in the reused variant (out of the summary).
Optional adds: none.

## Cover Letter Angle
Short, and in French. Their "atout sérieux" list (Streamlit + GenAI) is exactly what pc_pipeline adds on top of dbt: a layered dbt project with tests covering 6 defect classes, a MetricFlow semantic layer, an Airflow DAG, and an LLM agent that turns business questions into validated SQL, served through Streamlit. That's the kind of accelerator a new Snowflake practice can show clients (Snowflake Cortex Analyst + Streamlit in Snowflake follow the same pattern). Add one line on BNP: designing a multi-source dimensional model and a data-quality framework on messy manual data = the migration/modernization work their clients need. Say you'd go for the SnowPro Core + dbt certifications quickly.

## Preparation Gaps
- Snowflake migration patterns (they list "accompagner nos clients dans la migration"): lift-and-shift vs re-architecture, COPY INTO / Snowpipe, stages, zero-copy clone for testing, validating row counts/checksums between source and target.
- Snowflake cost/performance basics: warehouse sizing, auto-suspend, clustering, query profile. Already on your learning-plan backlog.
- SnowPro Core certification: a strong interview talking point for a Snowflake-partner entity; plan it regardless.
- Streamlit in Snowflake + Cortex: know how your pc_pipeline agent would be rebuilt natively.

## Stack Analysis

### Have
- Snowflake, dbt (indispensable): both on-CV and in pc_pipeline
- SQL, Python
- Modern Data Stack concepts: layered modeling, tests, semantic layer, orchestration (Airflow)
- Data modeling: BNP dimensional model, SCD2
- Streamlit + GenAI (atout sérieux): pc_pipeline LLM agent + Streamlit; LVMH RAG chatbot
- "Prompts qui cartonnent": daily heavy LLM/agent workflow

### Missing
- "Expérience significative" as a Data Engineer (internship + projects)
- Client-facing consulting delivery
- Snowflake/dbt certifications ("bienvenue")

### Partial
- Snowflake migrations, cost/perf tuning: concept-level

### Green Flags
- Snowflake + dbt as the core: your exact lane
- GenAI/Streamlit explicitly valued: your differentiator
- New entity: build it, certification training included
- Reposted: the first round didn't fill it

### Red Flags
- ESN/consulting model (off-lane category)
- "Expertise avérée" + "expérience significative": seniority wording, no number (likely soft-ish)
- 200+ applicants
- Hype-heavy JD, no location/contract/salary
- No age-discrimination wording

## Notes
- Verdict: apply. Near-zero tailoring cost for a strong stack match. Fits the "modern-stack consultancy fallback" tier with Valtech/Sia, and ranks above them on stack precision.
- If there's a way to reach the entity lead or a Devoteam Snowflake practice manager on LinkedIn, a short note cuts through the 200-applicant pile better than the Easy Apply.

## Raw JD (abridged)
Devoteam lance une nouvelle entité dédiée à l'intégration de Snowflake chez ses clients. Poste: Modern Data Stack Engineer spécialisé(e) Snowflake et dbt.
Missions: concevoir/développer/déployer des architectures data modernes sur Snowflake; pipelines robustes avec dbt; accompagner la migration des clients vers Snowflake; modèles de données et solutions d'intégration; conseil bonnes pratiques MDS; veille/innovation.
Profil: expérience significative Data Engineer (certification bienvenue); expertise avérée Snowflake et dbt indispensable; compréhension MDS; SQL et Python; Streamlit et/ou Generative AI = atout sérieux; travail en équipe, communication, adaptation aux environnements clients; "vous utilisez des prompts qui cartonnent".
Avantages: formations certifiantes Snowflake et dbt, accompagnement personnalisé, entité pionnière.
