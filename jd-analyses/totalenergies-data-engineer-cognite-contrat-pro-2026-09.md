# TotalEnergies — Data Engineer for Cognite Platform (CDF), débutant — Contrat de professionnalisation — 2026-09

## Metadata
- Status: NOT VIABLE as posted (2026-09-29). A RECE-bridge scenario was considered: the 12-month RECE fails their 13-month permit requirement, and the Dec 2026 start falls while still on student status. See Blocker.
- Date: 2026-09-29 (promoted ~3 days ago, so likely still open)
- Fit Score: Low. The technical fit is reasonable for a junior (data prep, data quality, Python, Power BI, Databricks, documentation), but the contract structurally doesn't work for a Passeport Talent path, and the scope and location are off-lane.
- Source: LinkedIn search "data cdd" (direct paste)
- Contract: Contrat de professionnalisation, 12 months, full-time (100% in company) with training modules. Legally a contrat pro is a CDD or CDI with a mandatory training component; this one is a 12-month CDD. Start: DECEMBER 2026 (not September).
- Location: Pau (CSTJF, TotalEnergies' technical/scientific center), southwest France
- Compensation: Not stated. Contrat pro pay is set by law as a % of the SMIC / the collective-agreement minimum, so it's structurally far below a Passeport Talent salary threshold.
- Company: TotalEnergies (major energy group, not a bank). Team: DEP, deploying the Cognite Data Fusion industrial data platform across 36 assets + an Enterprise Data Model.

## Blocker (read first)
1. The JD states: "la conclusion de ce contrat de professionnalisation ne permet pas la délivrance d'un titre de séjour (art. R.5221-6 Code du travail)". The contract can't be the basis for any residence permit, including Passeport Talent or a salarié change of status.
2. You must already hold a titre de séjour valid for the whole period (13 months minimum from the hire date). A permit tied to studies or a post-study job search usually won't cover December 2026 → January 2028, and even if one did, it would end with no route to renew from this contract.
3. Even ignoring (1), contrat pro pay is SMIC-based, so it couldn't meet the Passeport Talent salary threshold.
4. Timing overlap: start December 2026 overlaps with the BNP internship (to Dec 2026) and the master's end (Jan 2027). The JD also excludes people in a degree program ("ne s'adresse pas aux personnes recherchant une alternance avec une école ou formation diplômante").
Net: even if you got the offer, taking it would cost you a year off the residency path. Don't apply.

## CV Tailoring Instructions
N/A (not applying). If it were ever relevant: French CV, Variant B, lead with the BNP data-quality framework (completeness/availability checks = "éligibilité technique et données").

## Cover Letter Angle
N/A.

## Preparation Gaps
N/A. For reference only: Cognite Data Fusion (industrial DataOps platform: asset hierarchies, time series, contextualization), Databricks, industrial data models (ISO 15926 / CFIHOS-style EDMs).

## Stack Analysis

### Have
- Data collection/prep, data quality controls (formatting, correction, completeness): BNP DQ framework, pc_pipeline tests
- Python, Power BI
- Documentation discipline; professional English; French B2
- Data pipelines (dbt/Airflow in pc_pipeline); PySpark (TripAdvisor → Databricks transferable)

### Missing
- Cognite Data Fusion; industrial/asset data (time series, sensors, oil & gas asset hierarchies)
- Databricks hands-on (PySpark transfers)
- API development (partial: light FastAPI exposure)

### Partial
- Enterprise Data Model design: dimensional modeling ≠ industrial EDM, but the modeling discipline transfers

### Green Flags
- Explicitly junior ("débutant", recent Bac+5): no YoE gate
- Emphasis on documentation, data quality, scaling
- Large international team, energy-transition context

### Red Flags
- Contract type can't support a residence permit (legal blocker, stated explicitly)
- Contrat pro = training contract with SMIC-based pay, fixed 12 months
- Pau (southwest), not Paris
- Off-lane stack/domain: Cognite + Databricks + Power BI + Office suite; industrial OT data, not dbt/Snowflake product analytics
- No age-discrimination wording ("récemment diplômé(e)" is a legal contract-pro eligibility condition here, not a bias signal)

## Notes
- Search lesson: "data cdd" surfaces a lot of contrats pro / alternances. For LinkedIn searches, exclude them ("-alternance -apprentissage -professionnalisation") and prefer CDI filters; CDD only where it could lead to a CDI on a salarié contract that can support Passeport Talent.
- The "promoted 3 days ago" read is right (promotion = still actively hiring), but it doesn't matter given the blocker.

## Raw JD (abridged)
TotalEnergies, CSTJF Pau. Équipe DEP: déploiement de la Data Platform CDF (Cognite) sur 36 assets; développement d'un EDM aligné sur les standards de l'industrie; data collection, data préparation, mise en qualité (formatage, correction, contrôle qualité).
Missions (Data Engineer for Cognite Platform – débutant): valider l'éligibilité technique et données des sites (disponibilité, qualité, complétude); développer des outils d'analyse (Databricks, Power BI, Cognite) et analyses ad hoc (Data Discovery, DataPrep); accent sur documentation et scaling.
Profil: Bac+5 récent (information/data); expérience data engineering (pipelines, exploration, API); Office, notions Power BI, Python, Databricks; curiosité, esprit d'équipe; bonne capacité rédactionnelle; anglais professionnel indispensable.
Contrat: Contrat de Professionnalisation temps plein qualifiant, 12 mois (100% en entreprise), à partir de décembre 2026, avec formations internes.
Infos: titre de séjour valide pour la période (min. 13 mois) obligatoire à l'embauche; "la conclusion de ce contrat de professionnalisation ne permet pas la délivrance d'un titre de séjour (article R.5221-6 du Code du travail)". Ne s'adresse pas aux personnes cherchant une alternance avec formation diplômante.
