# Converteo — Consultant Data Engineer (Junior) — 2026-09

## Metadata
- Date: 2026-09-30
- Status: REJECTED (2026-10-01): CV-stage rejection email ("d'autres profils correspondent davantage"). Applied with the tailored FR build `cv_kris_huang_fr_converteo_consultant_data_engineer_junior.pdf`.
- Fit Score: Medium — explicitly junior, a salaried CDI cadre, and a real engineering scope (pipelines, data quality, DataOps) with an "AI First" way of working that matches the daily use of coding agents. Gaps: GCP-first, Terraform, Cloud Composer.
- Source: LinkedIn
- Contract: CDI, statut Cadre
- Location: Paris 12e, France

## Visa / Contract
- A salaried CDI cadre is valid ground for a Passeport Talent salarié qualifié. This is not the freelance/portage trap seen with ESN missions.
- Salary is "attractive" but not stated. Confirm it is at or above the threshold (≈€39.6k per Parakar, ≈€43.8k if strictly 2× SMIC) at the fit interview. Paris junior DE consulting packages usually clear it.

## CV Tailoring Instructions
Variant: French, DE framing (base = the Nexton build)
Branch: feature/french
File: french/resume_french_base.tex
Output: output/cv_kris_huang_fr_converteo_consultant_data_engineer_junior.pdf

Summary line (French), replacing the active summary (comment out the old one per CLAUDE.md):
Data Engineer orientée fiabilité et « AI first » — pipelines ELT testés et documentés (dbt, Airflow, SQL, Python) sur Snowflake, agent LLM de restitution en langage naturel, développement quotidien avec des assistants de code (Claude Code). Framework de qualité des données sur trois sources chez BNP Paribas Securities Services.

Summary line (English, reference only): Reliability-focused, AI-first Data Engineer: tested, documented ELT pipelines (dbt, Airflow, SQL, Python) on Snowflake, an LLM agent answering in natural language, and daily development with coding assistants (Claude Code). Data-quality framework across three sources at BNP Paribas Securities Services.

Skills reorder: none (keep the Nexton skills box). Do NOT add GCP, Terraform or Composer; they are not held.
CFA positioning: not in the summary (consulting DE target); it stays in education.
Optional adds: none.
One-page check: the new summary is about the length of the Nexton one (3 lines). Recompile and confirm one page.

## Cover Letter Angle
Le Hub Tech cherche des Data Engineers qui construisent « build to run » avec l'IA dans leur workflow quotidien : c'est exactement ma façon de travailler. Chez BNP Paribas Securities Services, j'ai conçu un modèle dimensionnel (grain, SCD Type 2) et un framework de qualité des données sur trois sources maintenues à la main. Dans mon projet pc_pipeline, j'ai industrialisé la même logique : modèles dbt testés et documentés, DAG Airflow idempotent, et un agent LLM qui ne répond qu'à travers des métriques validées. Je développe au quotidien avec des assistants de code, en gardant la revue et les tests comme garde-fous. Le cadre squad + Lead + Guilds est celui où je progresserai le plus vite sur GCP et Terraform.

## Preparation Gaps
- **GCP data stack, concept level:** BigQuery (partitioning/clustering, pricing per scanned byte), Cloud Composer = managed Airflow (your Airflow DAG transfers directly), GCS, Dataform vs dbt, Cloud Run. Be ready to map pc_pipeline onto GCP: GCS → BigQuery → dbt → Composer.
- **Terraform basics:** providers, resources, state, plan/apply, modules; be able to sketch a BigQuery dataset + service account + Composer environment in HCL. A small `terraform/` folder in pc_pipeline (even for DuckDB/S3 or a GCP free tier) would turn this gap into a talking point.
- **CI/CD for data:** a GitHub Actions workflow running `dbt build` on a PR (slim CI with `state:modified+`), which is already on the pc_pipeline v2 roadmap.
- **"AI First" story:** a concrete example of directing a coding agent (task split, review, tests as guardrails) and where you don't trust it.
- **Consulting posture:** the fit and partner interviews test client communication in French. Prepare a 2-minute French pitch of the BNP model and data-quality work, framed as "besoin métier → architecture fiable".
- **Technical interview (1h on site, senior lead):** SQL window functions, data modeling (grain, SCD), pipeline design and data-quality tradeoffs; possibly a live case.

## Stack Analysis

### Have
- Python, SQL (advanced), dbt, Git
- Airflow (transfers to Cloud Composer)
- Snowflake (one of the accepted platforms)
- Data-quality processes (BNP framework, dbt tests)
- AI-assisted development (Claude Code daily); an LLM agent over a semantic layer
- A master's in Data Science (fits the "Master … mathématiques appliquées ou connexe" line)

### Missing
- GCP (BigQuery, Composer), stated as "GCP First"
- Terraform / Infrastructure as Code
- Dataiku
- Consulting experience (listed as an "atout" only)

### Partial
- AWS (familiar)
- CI/CD for data pipelines (planned in pc_pipeline v2, not yet shipped)
- French: B2, with an all-French interview process

### Green Flags
- Explicitly junior, with a Lead owning delivery quality: a structured ramp-up
- Real engineering scope: pipeline design, data quality, IaC, CI
- An "AI First" coding culture matches your daily workflow
- CDI cadre (valid for the titre de séjour), internal School and certifications, Guilds
- Snowflake/AWS/Azure accepted alongside GCP

### Red Flags
- GCP-first consultancy: the earlier skip filter was the BigQuery mastery gate, but here it's softened by junior level and the explicit acceptance of other clouds
- The experience line ("spécialisation prouvée dans le déploiement de plateformes data scalables") is template text that overstates a junior requirement; don't self-screen on it
- Consulting: mission staffing risk and client-dependent stack

## Raw JD
Converteo — conseil et services technologiques (Data, IA, Agentique), 500+ consultants, 200+ clients, fondé en 2007, siège à Paris (bureaux New York, Toronto, Madrid, Milan).

Hub Tech — activité Platform Engineering : plateformes data Cloud-Native, Data et Analytics Engineering, développement full stack, gouvernance des données ; squads agiles.

Poste — Consultant Data Engineer, sous le pilotage d'un Lead.
- Ingénierie & Architecture Cloud-Native (« Build to Run ») : conception, architecture et développement de pipelines de données performants et des processus de Data Quality ; architectures Cloud-Native robustes.
- DataOps & Industrialisation : infrastructure as code (Terraform) et pipelines d'intégration pour une mise en production fluide et industrielle.
- Culture « AI First » : assistants de code et LLMs dans le workflow quotidien ; préparation des socles de données pour les systèmes d'IA.
- Collaboration Agile : avec des PO/PM pour traduire les exigences métiers en architectures de données fiables.
- Hard skills, R&D et Guilds : bonnes pratiques, veille, assets réutilisables.

Profil — Diplôme d'ingénieur ou Master (informatique, développement logiciel, mathématiques appliquées ou connexe). Expérience en ingénierie de données avec spécialisation prouvée dans le déploiement de plateformes data scalables ; conseil = atout.
- Python et SQL (bon niveau)
- Cloud : GCP en priorité (GCP First), ou Snowflake, AWS, Azure
- Terraform ; orchestration via Cloud Composer ou Dataiku
- Forte culture IA pour coder
- Rigueur, culture Software Engineering ; proactivité (dette technique, amélioration continue)

Process : fit avec un lead + recruteur (45 min visio) ; technique avec senior lead + lead (1h sur site) ; final avec un partner (45 min visio).
Conditions : Paris 12e (40 avenue des Terroirs de France), CDI cadre, dès que possible, rémunération attractive, télétravail flexible, School interne, WellPass, forfait mobilité durable.
