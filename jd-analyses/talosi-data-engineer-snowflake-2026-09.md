# Talosi — Data Engineer (Snowflake / Data Apps, client mission) — 2026-09

## Metadata
- Status: NOT APPLYING (2026-09-29): ESN + off-lane scope. Kept for the record and pattern data.
- Date: 2026-09-29 (1 applicant at time of review — very low competition)
- Fit Score: Medium. The technical fit is strong: Snowflake + SQL + Python + AWS are on-CV, and the 20% Cortex/AI part maps directly to the pc_pipeline LLM agent. It stays Medium because this is a 22-person ESN (consultancy) staffing a single client mission, with no dbt, an app/API-leaning "référent" scope, and a Lille / freelance-remote setup that has to be checked against Passeport Talent.
- Source: LinkedIn (direct paste)
- Contract: CDI (Lille) OR freelance (remote). Only the CDI works for Passeport Talent; freelance is not a salaried route.
- Location: Lille, France, with one trip a month to Lyon (the client site). Lille is about 1h by TGV from Paris, but a Lille CDI in practice means being based there or doing a hybrid arrangement. Confirm on the call.
- Compensation: Not stated. Confirm it clears the current Passeport Talent salary threshold before investing time.
- Company: Talosi, a ~22-person tech "collectif" (ESN/consulting model) that offers an associate package (equity) to consultants. The end client is unnamed: a large French family-owned international industrial group working in energy transition and circular economy.

## Why only 1 applicant
- A tiny, unknown ESN brand with an emoji-heavy, ChatGPT-style post. Many strong candidates scroll past.
- Lille + monthly Lyon + a "CDI OR freelance" split makes the post read as a staffing ad for one mission (it is one).
- Low applicant count is a structural signal (brand + model + location), not a quality signal. Same pattern as eXalt Ouest. Good odds if you want it.

## CV Tailoring Instructions
Variant: B (General Modern Stack). Use the FRENCH CV (French ESN, French JD), but keep English ready because the mission is international and "bon niveau d'anglais professionnel" is required.
Branch: variant-b-general (EN) / feature/french (FR)
Summary line (English): "Data engineer building on Snowflake, SQL and Python: layered, tested data models, a semantic layer, and an LLM agent that turns natural-language questions into validated SQL. Strong data-quality discipline from designing a private-capital data model at BNP Paribas. Seeking a Data Engineer role on a modern Snowflake / AWS platform."
Summary line (French): "Data Engineer sur stack moderne (Snowflake, SQL, Python) : modèles de données en couches, testés et documentés, couche sémantique, et agent LLM qui traduit des questions en langage naturel en SQL validé. Rigueur qualité acquise en concevant un modèle de données private capital chez BNP Paribas. Recherche un poste de Data Engineer sur une plateforme Snowflake / AWS."
Skills reorder: Put Warehousing first with Snowflake first in the list (Snowflake, PostgreSQL, DuckDB). Move Python up. Keep dbt visible but not leading (the JD never mentions dbt). If a skills line can absorb it without breaking one page, add "LLM / RAG (Snowflake Cortex-type use cases)" under Programming or Big Data & Cloud. That's optional; don't break the one-page rule for it.
CFA positioning: Out of the summary; it stays in Education/experience. Industrial client, no finance angle.
Optional adds: none. Lead the pc_pipeline bullets with the LLM agent + semantic layer and the Airflow DAG (deployment/automation). They matter more here than the private-capital framing.

## Cover Letter Angle
The 20% "IA avec Snowflake Cortex" piece is your hook. Cortex Analyst is Snowflake's managed version of what you built by hand in pc_pipeline: a semantic model over the warehouse and an LLM that turns business questions into SQL, with validation before execution. Say it that way. You've built NL→SQL over a MetricFlow semantic layer yourself, so you know where it breaks (ambiguous metrics, join paths, hallucinated columns) and why the semantic model is what makes it safe. That's the conversation you'd have with the client's business users. Then connect it to the 80%. The client's "point d'entrée unique pour tous les services data" is a governed serving layer: well-grained Snowflake tables and views, tests, and a stable interface (views/API) that consumers can trust. That's what the BNP dimensional model and the pc_pipeline test suite demonstrate. Keep it concrete and in French; mention one sentence on energy transition / circular economy only if the end client is named on the call.

## Preparation Gaps
- **Snowflake stored procedures + Snowflake Scripting.** The role explicitly says "procédures." Learn SQL Scripting procedures (DECLARE/BEGIN/EXCEPTION, loops, RETURN TABLE), Python stored procedures via Snowpark, and when to use a procedure vs a view vs a task. Write 1–2 on your pc_pipeline data in a Snowflake trial account.
- **Exposing data via an API.** This is the biggest gap and a large part of the 80% scope. Know the two patterns: (a) a FastAPI service reading from Snowflake with a connection pool, auth, pagination and a secure-view layer; (b) Snowflake-native options (SQL API, Snowpark Container Services, Streamlit in Snowflake for internal apps). A small FastAPI endpoint over one pc_pipeline mart would close this fast and it's portfolio-worthy.
- **Snowflake Cortex.** Know the families: Cortex LLM functions (COMPLETE, SUMMARIZE, CLASSIFY_TEXT, EXTRACT_ANSWER), Cortex Search (RAG over unstructured data), and Cortex Analyst (NL→SQL over a semantic model YAML). Map each to your LVMH RAG chatbot and pc_pipeline agent. This is where you can sound like the most qualified person in the room.
- **CI/CD for Snowflake objects.** "Automatisation des déploiements" + "tests automatisés": understand schemachange or Terraform (Snowflake provider) for versioned DDL, GitHub Actions/GitLab CI running tests on PR, and environment promotion (DEV → PROD with zero-copy clone). This overlaps with the deferred Terraform/IaC item in the learning plan.
- **Lakehouse on Snowflake.** Concept-level: Iceberg tables in Snowflake, external stages on S3, ELT via Snowpipe / COPY INTO. Enough to join an architecture discussion.
- **Snowflake RBAC + secure views.** Needed as soon as you expose data to many consumers through a single entry point.

## Stack Analysis

### Have
- Snowflake (on-CV), SQL (strong), Python
- Modern ELT architecture: layered staging → intermediate → marts, test suite (pc_pipeline)
- Automated tests / data quality: dbt generic + singular tests covering 6 defect classes; BNP DQ framework
- AI use cases on data: pc_pipeline NL→validated-SQL agent over a semantic layer; LVMH RAG chatbot + LLM-as-judge evaluation. This maps directly to Cortex user support.
- Orchestration evidence: real Airflow DAG in pc_pipeline
- AWS (familiar), English (TOEFL 120), French B2 (workable for a French ESN)
- Autonomy / proposing ideas: solo end-to-end portfolio build

### Missing
- Building APIs to expose data (production-grade)
- Snowflake stored procedures / Snowpark in practice
- CI/CD deployment automation for Snowflake (schemachange/Terraform)
- Professional DE experience in a "référent" (lead) capacity
- Snowflake Cortex hands-on (the concepts are held; the product isn't)

### Partial
- FastAPI/REST: light, off-CV exposure only
- Data Lakehouse: concept-level
- CI/CD: strong Git discipline, but no pipeline-deploy ownership
- Architecture choices: you've made them solo in pc_pipeline, not on a team

### Green Flags
- Snowflake-centric modern stack, not Microsoft/Fabric
- An AI/LLM component that matches your strongest differentiator (NL→SQL agent)
- The role owns design: Snowflake objects, architecture input, data-serving layer
- The problem is specific (a single data entry point for a large industrial group), not generic
- "Experts ou jeunes talents en devenir": open to juniors, no stated YoE gate
- 1 applicant: very low competition
- A coach, training, and an equity/associate package (unusual for an ESN)

### Red Flags
- ESN / régie model staffing one client mission. This is the off-lane category from your patterns. Your job depends on that mission; ask what happens at the end of the mission (inter-contrat).
- No dbt, no transformation-modeling language. The 80% is closer to data-application / backend engineering on Snowflake (objects, procedures, APIs) than to analytics engineering.
- "Référent Applications Data" implies a lead role; it may be sized for a senior despite the junior-friendly wording.
- The JD is emoji-heavy and generic (likely AI-written): company boilerplate dominates, the role is summarized in 4 lines, and no YoE, salary or seniority is given.
- CDI vs freelance split. Only the CDI route works for your residency; confirm the CDI isn't just nominal.
- Location: Lille + monthly Lyon, not Paris.
- No age-discrimination wording ("jeunes talents en devenir" is inclusive, not exclusionary).

## Notes
- Ranking: below the in-house dbt/Snowflake product-company lane (Alan, Alma, Tarmac, Vallourec). It sits with eXalt Ouest / Valtech as an ESN fallback, but it has the best AI angle of any ESN role so far.
- Worth a quick WhatsApp/email to ask 4 things before tailoring: (1) CDI salary range vs the Passeport Talent threshold; (2) whether Lille is on-site or hybrid from Paris; (3) is a junior profile acceptable for the référent role; (4) what happens at the end of the mission. The contact route (WhatsApp/email to Kevin) is informal, so a short direct message fits the culture better than a formal application.
- Skill-building value even if you don't land it: Snowflake procedures + a FastAPI endpoint + Cortex basics close gaps that recur across Snowflake JDs.

## Raw JD
🤗 Rejoins notre collectif d'experts et deviens Associé Talosi ! Chez Talosi, bienvenue chez toi, bienvenue chez nous 🤗

Nous recherchons notre futur Data Engineer pour une super mission !

📍 Modalités : CDI à Lille ou Freelance en remote (prévoir 1 déplacement par mois à Lyon 🚄)

Qui êtes vous ❓
🚀 Créée par des passionnées de techs 🤓 qui œuvrent sur l'eco-système depuis des années, Talosi en finnois signifie « ta maison »🏡 .
Dans ce collectif et projet commun, tout sera fait pour que tu te sentes chez toi 🙋‍♀️
Par-delà les valeurs que nous partageons tous et qui sont le socle de notre collectif 🫂, nous te proposons une vision, un accompagnement, de l'expertise et un vrai projet entrepreneurial commun 🔥

Quelle est votre promesse ❓
😎 Déjà t'éclater humainement et techniquement sur un projet que tu auras choisi
👩‍🏫 Ensuite développer tes compétences avec un cocktail de coaching et de formations
💫 Enfin, nous t'offrirons si tu le souhaites, un package d'associé qui comprend des parts dans la société.

Quelle sera mon aire de jeux ❓
Tu interviendras pour un grand groupe industriel international et familial français, reconnu aujourd'hui comme un acteur de la transition énergétique et de l'économie circulaire.
👩‍💻 Le projet : Des applications autour de la Data, dont une solution clé qui sert de point d'entrée unique pour tous les services data.
🦹‍♀️ Ton rôle :
* 80% Référent Applications Data : Conception et développement des objets Snowflake (tables, vues, procédures), création d'API pour exposer les données, et participation aux choix d'architecture.
* 20% Data Engineering & IA : Accompagnement des utilisateurs sur des cas d'usage IA avec Snowflake Cortex, intégration de données et automatisation des déploiements.

🧱 Data & DevOps : SQL, Python, architectures Data modernes (Data Lakehouse, ELT), CI/CD et tests automatisés. 🌥️ Cloud & Outils : Snowflake, environnement AWS.

Qui seront mes coéquipiers ❓
💃 Les Talosien.nes sont une communauté d'experts ou de jeunes talents en devenir 👨‍🎨.
Au quotidien, tu collaboreras étroitement avec les équipes de développement autour de la Data dans un environnement Agile et international (un bon niveau d'anglais professionnel est demandé !).

Comment je serai intégré ❓
👨‍🚀 Pour accompagner ta carrière, un coach t'animera dans ton parcours ainsi qu'une famille d'experts à tes cotés 🥷.
Sur le terrain, tu pourras t'appuyer sur ta forte autonomie, ta rigueur et ta capacité à être force de proposition.

On peut en parler ❓
Tu as des questions, le projet t'intéresse ou tu connais quelqu'un susceptible de l'être ?
📲 What's app nous au 📞 06 08 15 37 35 ou via le mail kevin@talosi.com
