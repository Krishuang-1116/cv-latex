# Aubay Data & AI — Analytics Engineer — 2026-09

## Metadata
- Date: 2026-09-03
- Fit Score: Medium — near-perfect STACK match (dbt, SQL, Snowflake/BigQuery/Databricks, data quality/governance/tests, DevOps/CI-CD) but gated by two things: (1) "au moins 4 ans" — the STEEPEST experience bar in the batch, plus a "devenir Lead / référent technique" framing aimed at mid-level+ consultants; (2) it's a consulting firm (ESN), so the work is client missions across sectors — including Banque/Assurance — not an in-house product team.
- Source: Direct paste (French JD)
- Contract: Not stated (CDI expected, consulting)
- Location: Not stated (France — Aubay is Paris-region; confirm)
- Compensation: Not stated — confirm, and check vs current Passeport Talent floor.

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
FRENCH CV: use it — this is a French-language role at a French firm. First live use of `feature/french` / `output/cv_kris_huang_fr.pdf`. Tailor the French CV, don't send the English one.
Summary line (French): "Analytics Engineer spécialisée en dbt, SQL et modélisation dimensionnelle sur data cloud (Snowflake), avec une rigueur forte sur la qualité, la documentation et le versioning des données. Double compétence data engineering / data analysis et une vraie polyvalence sectorielle (finance, luxe)."
Summary line (English): N/A for this application (French role) — keep the English canonical as backup.
Skills reorder: Variant B. Foreground dbt + data quality/governance/tests + DevOps/CI-CD (they name all of these). Note Snowflake (have), BigQuery/Databricks (familiar/learning).
CFA positioning: KEEP visible in experience/education — for a CONSULTANCY, domain range is an asset (they staff across Banque, Assurance, Luxe). Your CFA + LVMH (Luxe) experience make you placeable across their sectors; surface both. Don't lead the summary with CFA, but don't hide it here.
Optional adds: none. LVMH already on CV — lean on it as the "Luxe" sector proof for a consultancy.

## Cover Letter Angle (French)
Aubay Data & AI recrute des Analytics Engineers pour des missions variées (Banque, Assurance, Telecom, Industrie, Luxe) avec un socle technique précis : dbt, data cloud (Snowflake/BigQuery/Databricks), et une exigence forte sur la gouvernance — qualité, tests automatisés, documentation, versioning. C'est exactement la façon dont je construis la donnée : chez BNP Paribas Securities Services j'ai conçu un modèle dimensionnel de bout en bout et un framework de qualité de données garantissant l'intégrité des chiffres avant tout reporting ; mon projet pc_pipeline repose sur une suite de tests dbt couvrant six classes de défauts réels. Pour un cabinet qui place ses consultants sur des secteurs multiples, ma polyvalence est un atout concret : une expertise du capital-investissement (finance) doublée d'une expérience dans le Luxe (projet data chez LVMH / Maison Loewe), le tout sur une stack moderne dbt/Snowflake. Je serais ravie de mettre cette double compétence data engineering / data analysis au service de vos clients.

## Preparation Gaps
Fully covered by the existing one-month learning plan — nothing Aubay-specific beyond:
- **dbt certification (dbt Analytics Engineering).** Listed as a differentiator ("les plus qui vous feront sortir du lot"). Worth actually sitting — it's a concrete, quick credential that this JD explicitly rewards, and it strengthens every other dbt-heavy application too. Consider slotting it into the learning plan.
- **Multi-warehouse familiarity** (Snowflake have; BigQuery/Databricks concept-level) — same as synthesis; "familier avec" is enough here.
- **BI breadth**: Power BI (have), Tableau/Qlik (new) — concept-level awareness of how each sits on the analytical layer is enough; PL-300 or Tableau cert is a named "plus".
- **DevOps / CI-CD** — synthesis item; be fluent on dbt-in-CI, PRs, versioning.
- **Consultancy-specific soft skills**: "animation d'ateliers métiers et techniques" — be ready to talk about facilitating workshops and translating between business and technical stakeholders (your BNP business-partnering covers this).

## Stack Analysis

### Have
- dbt — core (JD: "en particulier dbt Labs", "dbt Core/Cloud" as a plus)
- SQL — strong
- Snowflake — on CV (their primary partner platform)
- Dimensional modeling / analytical data models — BNP + pc_pipeline
- Data quality / governance / tests / versioning — BNP DQ framework + pc_pipeline tests (JD stresses all of these)
- Power BI — have (one of their named BI tools)
- Git / DevOps basics — have
- Business partnering / workshop facilitation — BNP
- Domain versatility (finance + Luxe/LVMH) — a real asset for a consultancy staffing across sectors

### Missing
- 4+ years experience — the hard gate; you're a graduating intern. Steepest bar in the batch.
- Lead / référent-technique readiness — they want mid-level+ who can lead at client sites
- Tableau / Qlik Sense — hands-on (have Power BI)
- Databricks — hands-on (have dbt/DuckDB/Snowflake)
- Named certifications (dbt AE, PL-300, Tableau) — none yet

### Partial
- BigQuery — SQL transfers, platform not yet
- CI/CD / DevOps philosophy — Git yes, full CI/CD pipeline practice partial
- Consulting/client-facing delivery — BNP internal stakeholder work is adjacent, not client-billed

### Green Flags
- dbt-first, modeling + governance-centric — matches your strengths precisely
- Data quality / tests / documentation / versioning as core responsibilities
- Modern data cloud focus (Snowflake partner) — your platform
- Strong learning/certification culture (they pay for + expect certs) — good for leveling up
- Domain versatility rewarded — your finance + Luxe range is a genuine differentiator here
- Clear, non-vague technical spec; no age-discriminatory language

### Red Flags
- **4-year experience requirement** — a real filter for an entry-level profile. This specific posting targets experienced AEs on a lead track, not juniors. (Aubay likely has junior openings too — but not this one.)
- **Consulting / ESN model** — you'd be placed on client missions, sector- and tech-variable, with less control over the work than an in-house team; missions may route through Banque/Assurance clients you'd otherwise avoid. Not a JD-quality flag, a fit/preference flag: weigh whether the ESN model suits you. Some love the variety and fast skill-building; others find staffing generic.

## Notes
- Ranking: strong on stack, but the 4-year gate + ESN model put it below Emeria (1-2 yr, in-house) and the product-team roles for your current profile. Worth a targeted application IF you're open to consulting and can frame the internship + portfolio as punching up — the domain-versatility angle is your best lever with an ESN.
- This is the first role that actually uses the new FRENCH CV — good live test of `feature/french`.
- If you pursue consulting generally, sitting the dbt Analytics Engineering cert would materially help (named here, cheap, reusable).

## Raw JD (French, original)

Aubay Data & AI (cabinet Data de Aubay Solutec) recherche des Analytics Engineers pour concevoir et optimiser des solutions analytiques modernes. Double compétence Data Engineering + Data Analysis.

Quotidien :
- Collaboration avec Data Analysts et équipes métiers pour comprendre les besoins reporting et proposer des solutions
- Conception/maintenance de modèles de données analytiques (modélisation, documentation, optimisation des performances) pour fournir des jeux de données prêts à l'emploi
- Implémentation de transformations via outils modernes (SQL, dbt…) pour standardiser/enrichir/structurer les données pour la BI et les métiers
- Optimisation des workflows analytiques (robustesse, scalabilité, maintenabilité)
- Bonnes pratiques de gouvernance des données : qualité, versioning, documentation, tests automatisés
- Contribution à l'adoption de solutions Cloud modernes (Snowflake, BigQuery, Databricks…) et modernisation des environnements analytiques
- Animation d'ateliers métiers et techniques

Profil :
- BAC+5 (Master 2 ou école d'ingénieur) spécialisé en informatique
- Au moins 4 ans d'expérience en ingénierie analytique et environnements BI modernes
- Maîtrise des technologies de transformation analytique (en particulier dbt Labs) ; familier avec plateformes Data Cloud (Snowflake, BigQuery, Databricks…)
- À l'aise avec BI (Power BI, Tableau, Qlik Sense) et leurs interactions avec les couches analytiques
- Approche rigoureuse qualité/documentation/contrôle des versions
- Maîtrise DevOps + CI/CD
- Environnement collaboratif/agile ; communication technique et métier
- Curieux, force de proposition

Les plus :
- Expérience dbt Core/Cloud + Snowflake ou BigQuery
- Certification(s) : dbt Analytics Engineering, Power BI PL-300, Tableau Certified Data Analyst…

Contexte : missions variées (Banque, Assurance, Telecom, Industrie, Luxe) ; apprentissage continu + certifications ; communautés Data ; partenaire Snowflake/Databricks SELECT, Microsoft Fabric, GCP. Évolution vers Lead / référent technique.

Process : 1) RH 30mn ; 2) expert technique min 1h ; 3) direction BU Data & AI 45mn–1h.
