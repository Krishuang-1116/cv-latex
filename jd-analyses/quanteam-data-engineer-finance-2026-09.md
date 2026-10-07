# Quanteam — Data Engineer (finance-sector consulting) — 2026-09

## Metadata
- Date: 2026-09-29
- Status: Recruiter phone screen 2026-10-06 (probable match: Kris recalled the firm as "Kantine"; confirm). Kris asked to switch to English; recruiter asked preferred industry/positions and will pass the profile to a business manager.
- Fit Score: Medium. You clear the gate better than most juniors (a "première expérience" DE in banking/finance: BNP Paribas Securities Services is literally one of the client types they list, "dépositaires de titres", plus CFA), and SQL/Python/Spark/Airflow/dbt/PostgreSQL/AWS are all held. Desirability is low: an ESN placing you at banks is both off-lane categories at once (consultancy + traditional financial institution), and the stack list is a generic catch-all (Hadoop/Kafka/Scala/Oracle/Talend).
- Tailoring effort: ZERO. The canonical French CV (`output/cv_kris_huang_fr.pdf`) already leads with private capital + BNP + CFA — exactly Variant A for this JD.
- Source: LinkedIn (direct paste, French JD)
- Contract: Not stated (CDI expected, consultant)
- Location: Not stated; Paris most likely (also Lyon, London, etc.)
- Compensation: Not stated. Confirm it clears the Passeport Talent threshold.
- Company: Quanteam (Rainbow Partners group), ~740 consultants, consulting specialized in banking/finance (CIB, asset managers, private/retail banks, custodians), front-to-back, business + IT.

## CV Tailoring Instructions
Variant: A (Financial Data Infrastructure), FRENCH CV.
Branch: none. Send `output/cv_kris_huang_fr.pdf` as-is.
Summary line (French): as on the canonical French CV: "Profil d'Analytics Engineer alliant une expertise du capital-investissement (BNP Paribas Securities Services) et la maîtrise d'une stack data moderne — modélisation dimensionnelle, pipelines dbt et qualité des données. Titulaire du CFA. À la recherche d'un poste d'Analytics Engineer ou de Data Engineer."
Summary line (English): canonical master line (Variant A).
Skills reorder: none.
CFA positioning: summary (domain evidence; it's their core sector).
Optional adds: none. Guosen/UOB would strengthen the finance angle but cost a one-page rebuild; not worth it for a fallback.

## Cover Letter Angle
Short. You've already done their job from the client side: at BNP Paribas Securities Services (a custodian, one of their client types) you designed a dimensional model across three manually maintained source systems and built a data-quality framework for identity-resolution failures, duplicates and cross-source code inconsistencies — "contraintes fortes liées au contexte réglementaire et à la qualité des données". The CFA means you speak the business side of front-to-back (the "double compétence métier et IT" they sell). Mention pc_pipeline (dbt + Airflow + tests) as the modern-stack side.

## Preparation Gaps
- Batch vs streaming at concept level (Kafka topics/partitions/consumer groups; why intraday risk or trade feeds need streaming while NAV/reporting stays batch).
- Spark tuning basics (partitioning, shuffles, broadcast joins) — PySpark held, depth likely asked.
- Bank data context: BCBS 239 (risk data aggregation principles), lineage, reconciliations. Your BNP work maps directly.
- Oracle/SQL Server dialect differences: light.

## Stack Analysis

### Have
- SQL, Python (impératif), Spark (PySpark — TripAdvisor), Airflow, dbt, PostgreSQL, AWS (familiar)
- First experience in a financial environment (BNP Paribas Securities Services) + CFA
- Data quality/reliability in a regulated context
- Data Warehouse modeling; English (TOEFL 120); French B2

### Missing
- Kafka / real-time; Hadoop; Scala; Oracle / SQL Server / NoSQL in practice; Talend
- Formal "Data Engineer" title (yours is Data Analyst intern, though the work is AE/DE)

### Partial
- Cloud: AWS familiar; GCP/Azure not held
- Agile/Scrum: some via BNP

### Green Flags
- Explicitly junior ("première expérience")
- Your finance background is the gate, not a nice-to-have
- Clear pipeline/quality scope; dbt + Airflow in the list
- Training/certification support

### Red Flags
- ESN (consultancy) + bank/finance clients: both on your "not interested" list — you'd likely be placed at a bank
- Generic catch-all stack list (the mission defines the real stack; could land on Oracle/Talend legacy work)
- No age-discrimination wording

## Notes
- Verdict: apply as a zero-effort fallback IF you're OK with bank-client missions. Attainability is among the best so far (the finance gate filters out most dbt-native juniors and favors you). It's a hedge, not a target: it pulls you back toward banking rather than into product-company AE.
- The career risk to be aware of: 2 years at bank clients via an ESN reinforces the "finance" label on your profile rather than the product AE one.

## Raw JD (abridged)
Quanteam (Groupe Rainbow Partners), cabinet de conseil Banque/Finance/Services financiers, 740 consultants (Paris, Lyon, Londres, NY, Montréal, Genève, Lisbonne, Porto, Bruxelles, Casablanca, Singapour). Clients: BFI, sociétés de gestion, banques privées et de détail, dépositaires de titres; Front-to-Back.
Missions (chez clients grands comptes): pipelines robustes et scalables; collecte, transformation, mise à disposition (batch/temps réel); modernisation data (Data Lake, DWH, cloud); optimisation performance/qualité/fiabilité; collaboration Data Science/BI/IT/métiers finance; contraintes réglementaires et qualité des données.
Stack: Python, SQL (impératif), Scala apprécié; Spark, Hadoop, Kafka; PostgreSQL, Oracle, SQL Server, NoSQL; AWS/GCP/Azure; Airflow, DBT, Talend; Agile/Scrum.
Profil: Bac+5; première expérience Data Engineer en environnement bancaire/financier; SQL et Python solides; autonomie, rigueur, esprit d'analyse, relationnel; anglais obligatoire.
