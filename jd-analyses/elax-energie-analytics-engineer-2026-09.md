# Elax Energie — Analytics Engineer — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: High — arguably your best thematic match yet. Elax's "Nao" (natural-language query tool whose reliability depends on well-documented dbt models) IS the premise of the AI agent you built. Exact stack (dbt, BigQuery, Dagster, Metabase, Claude, Airbyte), and the seniority gate is EXPLICITLY open to strong internship profiles. French-language role — your French CV is ready.
- Source: Direct paste (French JD)
- Contract: Not stated (CDI expected) — startup key hire
- Location: Paris — hybrid (2 days on-site); must reside in France
- Compensation: €45,000-60,000 — €45k floor sits in the Passeport Talent sensitivity zone (jeune-diplômé ~2×SMIC); €60k ceiling clears comfortably. Confirm current threshold; negotiate toward the upper half.

## Why this is a top-tier fit
1. **Nao = your agent, productized.** The role's second mission is literally "make the data understandable and usable by Nao": document models/fields/business synonyms/rules so the NL agent produces reliable answers, and "audit agent responses to find data or context gaps." You built exactly this — an LLM agent over your semantic layer that turns NL into validated SQL, plus trust/verify write-ups auditing where the agent could go wrong. Few candidates can claim this; you can, hands-on.
2. **Seniority gate explicitly opens to you:** "2-5 years... internship/alternance profiles considered carefully IF you've already built models and gained autonomy." That is precisely your pc_pipeline solo build. Plus "apply even without 100% of skills."
3. **Exact stack:** dbt + BigQuery + Dagster (orchestration) + Metabase + Claude + Airbyte — all things you have or can bridge fast (Dagster from your Airflow, Metabase from Power BI, BigQuery from Snowflake/DuckDB).
4. Small, high-autonomy, CTO-attached team; "data as a product, not just dashboards" — your build style. Concrete climate-impact mission.

## CV Tailoring Instructions
Variant: B (General Modern Stack) — engineering + AI-forward, PORTFOLIO-forward
Branch: variant-b-general
FRENCH CV: use it (French role, French company, France residency required). Tailor `cv_kris_huang_fr.pdf`.
Summary line (French): "Analytics Engineer spécialisée en dbt, SQL et modélisation dimensionnelle sur BigQuery, avec une rigueur forte sur la qualité, les tests et la documentation. J'ai construit une couche sémantique et un agent IA (langage naturel → SQL validé) — exactement la logique qui rend un outil comme Nao fiable."
Skills reorder: Variant B, portfolio-forward. Foreground dbt, dimensional modeling, data quality/tests, documentation, and the AI agent + semantic layer. Note BigQuery (swap from Snowflake/DuckDB) and Dagster (from Airflow).
CFA positioning: Out of summary; education only (energy startup).
Optional adds: none. The AI-agent + semantic-layer + documentation-discipline story is the pitch.

## Cover Letter Angle (French)
Chez Elax, la documentation n'est pas un livrable secondaire : elle permet à Nao de produire des réponses fiables, et une partie du poste consiste à auditer les réponses des agents pour repérer les zones d'ombre dans la donnée ou le contexte. C'est exactement ce que j'ai construit dans mon projet pc_pipeline : une couche sémantique documentée et un agent IA qui traduit une question en langage naturel en SQL validé, avec une couche de garde-fous qui vérifie les règles de qualité avant toute exécution — et un travail explicite d'audit sur les cas où l'agent pouvait se tromper. J'ai aussi appris à concevoir des modèles pensés pour durer : grain, faits, dimensions, tests dbt du staging aux marts, en gardant une exigence de qualité avant tout reporting (une discipline que j'ai aussi mise en œuvre chez BNP Paribas Securities Services via un framework de qualité de données). Rendre une donnée complexe claire, documentée et « Nao-ready », domaine par domaine, correspond précisément à ma façon de travailler — et l'impact concret d'Elax sur la transition énergétique rend le sujet d'autant plus motivant.

## Preparation Gaps
Almost fully covered — the AI-agent theme is a STRENGTH here, not a gap. Minor items:
- **Dagster** (nice-to-have) — you have hands-on Airflow; bridge to Dagster's model (assets, ops, jobs, software-defined assets). Quick given your orchestration base. Worth a short primer since it's their orchestrator.
- **BigQuery** — swap from Snowflake/DuckDB; SQL transfers. Learn partitioning/clustering, incremental on BQ.
- **Airbyte** — EL/ingestion connector tool (extract-load). New but simple concept: sources, connectors, syncs.
- **Metabase** — BI (you have Power BI); trivial concept swap.
- **Nao-readiness / semantic docs for NL agents** — you already lived this; just frame it: documenting fields, business synonyms, and rules so an agent answers reliably, and auditing agent outputs. Lead with it.
- Energy-flexibility domain — explicitly NOT required ("pas besoin d'être expert de l'énergie"). Skim demand-response/load-shifting/carbon-intensity if pursuing.
- French interview — B2; rehearse modeling vocabulary.

## Stack Analysis

### Have
- dbt — core; staging→marts, tests, quality (their central need)
- Dimensional modeling — grain/facts/dims/relations (explicitly the mission)
- Data quality / dbt tests / documentation — pc_pipeline + BNP DQ framework; documentation is first-class here and is your habit
- SQL — strong
- Semantic layer + AI agent (NL→validated SQL) — near-exact match for Nao; your rarest differentiator
- AI fluency beyond chat — authentic (agent build, MCP, Claude in daily workflow)
- Business partnering / challenge-the-request / "savoir dire non" — BNP + recurring strength
- Git discipline, conventions/standards mindset

### Missing
- Production models other teams depend on (yours is solo portfolio + internal BNP) — SOFTENED by their explicit "internship profiles considered if you've built models + autonomy"
- BigQuery hands-on (Snowflake/DuckDB instead)
- Dagster hands-on (Airflow instead — close)
- Airbyte, Metabase (learnable, concept-level)
- Energy-flexibility domain (explicitly not required)

### Partial
- Orchestration — Airflow hands-on; Dagster is the swap
- Semantic layer — MetricFlow; Nao is a different NL tool but same underlying premise (documented models power the agent)
- ~2-5 years — you're below, but the internship clause explicitly brings you into scope

### Green Flags
- Nao / NL-agent-on-documented-models = your exact built experience; near-perfect thematic fit
- Seniority gate EXPLICITLY open to strong internship profiles + "apply without 100%"
- Exact stack (dbt/BigQuery/Dagster/Metabase/Claude/Airbyte)
- Documentation + data quality + dimensional modeling as core — your strengths
- "Data as a product, not dashboards" + high autonomy + CTO-attached small team — your build style
- AI fluency beyond chat explicitly wanted — your differentiator
- French CV ready; concrete climate mission; inclusive language

### Red Flags
- None on JD quality — this is a well-defined, well-matched role. Watch-items: BigQuery/Dagster/Airbyte are (easy) tool swaps; French-language interviews at B2; and the €45k salary floor vs the Passeport Talent threshold — negotiate toward €60k, verify current figure.

## Notes
- Ranking: TOP TIER — put it alongside (or above) Alan/Emeria/Tarmac. The Nao match is the single most precise thematic fit in your whole search, and the internship clause removes your usual seniority barrier. Strong candidate for a priority application.
- Lead every artifact (CV, cover letter, interview) with the AI-agent + semantic-layer + documentation story — it's what this role is built around.
- Mildly amusing: Elax's own health insurance is Alan (another of your targets) — irrelevant to the role, just noting.

## Raw JD (French, abridged)

Elax Energie (depuis 2020) — boîtier fabriqué en France pilotant à distance des chauffe-eaux pour réduire la conso des logements sociaux et consommer quand l'électricité est moins carbonée. 80k+ boîtiers, 100+ bailleurs sociaux, 20% d'économies moyennes, 50+ employés.

Équipe Data Platform (rattachée au CTO, 3 personnes : Head of Data & IA, Analytics Engineer, IA Engineer). Rôle : transformer les données brutes en data model clair/documenté/fiable, base des décisions de toute l'entreprise, y compris via Nao (outil de requête en langage naturel). Contexte de montée en compétences IA. Environnement très autonome, feedback régulier, place pour challenger.
Stack : dbt, BigQuery, Metabase, Nao, Claude, Dagster, Airbyte.

Missions:
1. Fiabiliser le data model par domaine : définir grain/faits/dimensions/relations ; construire les modèles dbt staging→marts sur BigQuery ; écrire les tests dbt, garantir qualité/cohérence/robustesse.
2. Rendre la donnée exploitable par Nao : documenter systématiquement modèles/champs/synonymes métier/règles de gestion ; auditer les réponses des agents pour identifier zones d'ombre/incohérences ; aucun domaine exposé dans Nao sans modèle documenté ; prendre la responsabilité d'un domaine de bout en bout.
3. Partenaire des équipes métier : traduire des besoins flous en périmètres data clairs ; challenger une demande sans dégrader la relation ; savoir dire non quand un correctif rapide nuit à la fiabilité ; contribuer aux conventions (SQL/dbt, nommage, doc, Nao-readiness).
4. Décupler les workflows via l'IA : accélérer doc/tests/modélisation avec l'IA, en gardant l'esprit critique.

Objectifs 1 an: Phase 1 (0-3m) onboarding + premiers modèles documentés + zones prioritaires ; Phase 2 (3-6m) autonomie sur domaines + KPI + cadrage métier ; Phase 3 (6-12m) pleinement responsable d'un périmètre, standards qualité, partenaire reconnu, domaine entièrement modélisé/documenté.

Profil: ~2-5 ans en data ; alternance/stages significatifs étudiés si modèles déjà construits + autonomie. Maîtrise dbt + SQL + modélisation dimensionnelle ; modèles déployés en prod dont d'autres équipes dépendent ; aisance relationnelle + challenge de la demande ; modèles pensés pour durer ; pratique fluide de l'IA au-delà du chat ; goût de la propriété des sujets. Nice-to-have : Dagster, Metabase, semantic layer ; pas besoin d'être expert énergie/Nao.

Salaire : 45-60K€. Paris hybride (2j présentiel), résidence en France requise. Mutuelle Alan, tickets restau Swile. Inclusif ("autorisez-vous à candidater").
