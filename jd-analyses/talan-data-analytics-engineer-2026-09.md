# Talan — Data Analytics Engineer (senior) — 2026-09

## Metadata
- Date: 2026-09-28
- Fit Score: Medium-Low — right role TYPE (Analytics Engineer), but wrong STACK: the entire role centers on Microsoft Fabric + Azure (Power BI semantic models / Direct Lake, Fabric Lakehouse/Warehouse, Dataflows Gen2, Fabric Data Factory, dbt Fabric, DAX Studio/VertiPaq, Fabric CI/CD, RLS/OLS). Your core is dbt-core + Snowflake/DuckDB + AWS-adjacent. Also explicitly SENIOR, and a consulting firm (ESN). Bridge = Power BI/DAX + dimensional modeling + finance/luxe domain.
- Source: Direct paste (French JD, #TalanFrance)
- Contract: Not stated (CDI expected, consulting)
- Location: France (Paris-region likely) — confirm
- Compensation: Not stated — confirm, check vs Passeport Talent floor.

## Read this first — stack mismatch + consulting model
- This is a **Microsoft-ecosystem** role (Talan is a Microsoft Solutions Partner Data & AI). Fabric is Microsoft's all-in-one platform that competes with your dbt/Snowflake stack. "dbt Fabric" appears only as one adapter option; the rest (Direct Lake, Dataflows Gen2, Fabric notebooks, Fabric Data Factory, Deployment Pipelines, VertiPaq/DAX Studio, RLS/OLS) is Fabric-specific and new to you.
- **Second Azure/Microsoft role in the batch** (after Pluxee) — reinforces that Microsoft-shop roles are your weakest stack fit. Your one strong bridge is Power BI/DAX (you have it) + dimensional/star-schema modeling.
- **Consulting firm (ESN)**, like Aubay: client missions across banque/finance, énergie, transport, luxe/distribution, santé; less control over the tech; senior/ownership/mentoring framing.
- Consistent with your "stay AE-focused (dbt/Snowflake)" decision: pursuing this means investing in a whole different PLATFORM track (Fabric/Azure), the same kind of divergence you declined on the DE-infra side. Recommend NOT building a Fabric prep track unless you specifically want Microsoft-shop consulting.

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
FRENCH CV: use it — French-language role at a French firm. Tailor `cv_kris_huang_fr.pdf`.
Summary line (French): "Analytics Engineer, solide en modélisation dimensionnelle (star schema), SQL et Power BI (DAX), avec une rigueur forte sur la qualité et la documentation des données. Polyvalence sectorielle finance / luxe."
Skills reorder: Variant B, but FOREGROUND Power BI (DAX) and dimensional modeling — they are your only real overlap with a Fabric role. Keep dbt/SQL/data quality visible. Be honest that your cloud is Snowflake/AWS-adjacent, not Azure/Fabric.
CFA positioning: Out of summary; keep visible in experience — domain versatility (finance) is a consultancy asset.
Optional adds / domain: LVMH (luxe) resonates with Talan's luxe/distribution sector — mention in cover letter.

## Cover Letter Angle (French, only if pursuing)
Talan recrute pour son Pôle Cloud Data Platform des Analytics Engineers maîtrisant toute la chaîne de valeur — de la transformation à l'exposition sémantique et la visualisation — avec une exigence forte sur la qualité des modèles et la fiabilité en production. C'est exactement ma manière de travailler : chez BNP Paribas Securities Services j'ai conçu un modèle dimensionnel de bout en bout et un framework de qualité de données, et mon projet pc_pipeline repose sur une architecture en couches, des tests dbt et une couche sémantique. Je maîtrise Power BI (DAX) et la modélisation en étoile — le cœur du travail sémantique Fabric — et je monte vite en compétence sur une nouvelle plateforme (je l'ai fait sur dbt, Airflow et une couche sémantique en quelques mois). Pour un cabinet qui intervient sur des secteurs variés (finance, luxe…), ma double compétence data + domaine (capital-investissement chez BNP, projet data chez LVMH) est un atout concret. [Be transparent that Fabric/Azure would be a ramp-up.]

## Preparation Gaps
Per your AE-focus decision, DO NOT build a Fabric track unless you commit to Microsoft-shop roles. If you do pursue this specifically:
- **Microsoft Fabric** end-to-end — the whole platform: Lakehouse vs Warehouse, Direct Lake vs Import, Dataflows Gen2, Fabric Data Factory, Fabric Spark notebooks, dbt Fabric adapter. This is the dominant gap.
- **Power BI semantic models at depth** + **DAX performance tuning** (VertiPaq Analyzer, DAX Studio) — you have Power BI/DAX; the perf-tuning tooling and large-model optimization are new.
- **RLS / OLS** (row/object-level security) — access governance in Power BI/Fabric.
- **Fabric CI/CD** (Git Integration, Deployment Pipelines) — Fabric-specific.
- **Azure** — same gap as Pluxee; your cloud is AWS-familiar.
Note: none of this overlaps your dbt/Snowflake investment — it's a parallel platform, which is the core reason this ranks low for you right now.

## Stack Analysis

### Have
- Power BI (DAX) — genuine bridge; Fabric semantic models ARE Power BI semantic models
- Dimensional / star-schema modeling — BNP + pc_pipeline (JD wants Gold Layer star schema)
- SQL — strong
- dbt — core (dbt Fabric is an adapter; concept transfers)
- Data quality / documentation / reliability discipline — your strength
- Git / CI-CD concept — transferable
- Domain versatility (finance + luxe/LVMH) — consultancy asset

### Missing
- Microsoft Fabric platform (Lakehouse/Warehouse, Direct Lake, Dataflows Gen2, Fabric Data Factory, Fabric notebooks) — the core of the role
- Azure ecosystem — AWS-familiar, not Azure
- DAX/SQL perf tuning tooling (VertiPaq Analyzer, DAX Studio)
- RLS / OLS
- Fabric CI/CD (Git Integration, Deployment Pipelines)
- Senior-level / production-ownership / mentoring track record

### Partial
- Semantic layer — dbt Semantic Layer/MetricFlow, not Power BI/Fabric semantic models (concept transfers, tooling differs)
- Spark — PySpark (TripAdvisor) transfers to Fabric notebooks conceptually
- CI/CD — Git strong, Fabric deployment pipelines new

### Green Flags
- Analytics Engineer role type (on-track with your AE focus)
- Dimensional modeling + semantic exposure + data quality centric — matches your strengths conceptually
- Power BI/DAX is genuinely central here — your best single bridge
- Domain versatility rewarded (consultancy across finance/luxe) — your differentiator
- Strong learning/practice-capitalization culture (could train you on Fabric)
- No age-discriminatory language; diversity-committed

### Red Flags
- None on JD quality. Fit concerns: (1) Microsoft Fabric/Azure platform is off your core stack and is the whole role; (2) explicitly senior; (3) consulting/ESN model (client-placement, sector-variable incl. banks). A stretch on both stack and seniority.

## Notes
- Ranking: below your dbt/Snowflake AE targets (Emeria etc.) and below the product-team roles. Off-stack + senior + consulting. Apply only if you're open to a Microsoft-shop consulting path and willing to pitch Fabric as a fast ramp on top of your Power BI/DAX + modeling base.
- Pattern (for the next synthesis): Microsoft Fabric/Azure roles (Pluxee, Talan) are a distinct platform track from your dbt/Snowflake investment — the same "different platform" divergence as DE-infra. Your Power BI/DAX is the bridge, but the platform gap is large; consistent to deprioritize unless targeting Microsoft shops.

## Raw JD (French, original — abridged)

Talan (groupe international, conseil + tech, transformation Data & IA ; 6000+ collaborateurs ; secteurs : banque/finance, énergie, transport, luxe/distribution, santé ; entreprise responsable, diversité). #TalanFrance.

Rôle : Data Analytics Engineer senior au Pôle Cloud Data Platform ; piloter des plateformes Microsoft Fabric et Azure sur projets clients. Maîtriser toute la chaîne de valeur (transformation → exposition sémantique → visualisation) ; concevoir des solutions Fabric robustes/performantes, fiables jusqu'en production ; exigence qualité, arbitrage en contextes complexes, communication transverse, amélioration continue.

Modélisation & Analytics :
- Concevoir/maintenir des modèles sémantiques Fabric (Power BI semantic model) en Direct Lake ou Import selon perf
- Implémenter la Gold Layer dans Fabric (Lakehouse ou Warehouse) et les modèles dimensionnels (star schema)
- Concevoir/opérer des pipelines de transformation dans Fabric : dbt Fabric, Dataflows Gen2, notebooks Spark, Fabric Data Factory
- Détecter/résoudre les problèmes de performance DAX et SQL (VertiPaq Analyzer, DAX Studio)
- Appliquer CI/CD Fabric (Git Integration, Deployment Pipelines) ; gérer les accès (RLS/OLS)

Delivery & Engagement Client :
- Ownership des périmètres analytiques en production ; superviser/diagnostiquer/corriger les incidents durablement
- Accompagner les équipes (partage de connaissances, revues de code, revues de modèles DAX)
- Capitalisation et amélioration continue de la practice

Rôle chez Talan : benchmark de solutions + conseil client ; réalisation de POC ; projets internes + partage de connaissances ; formations internes.
