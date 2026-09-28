# Emeria (Foncia) — Analytics Engineer — 2026-08

## Metadata
- Date: 2026-08-28
- Fit Score: High — the most ATTAINABLE fit of the batch. Stack is a direct hit (Snowflake + dbt + SQL + data modeling + historization + data quality/governance) and the seniority bar is the softest yet: "1 à 2 ans." Caveats: French-language role (French CV needed; you're B2), Tableau not Power BI (minor), salary band €45-55k sits in the Passeport Talent sensitivity zone (verify), and the role leans business-partnering/dashboarding — confirm engineering depth holds.
- Source: Direct paste (French JD)
- Contract: Not stated (CDI expected) — full-time
- Location: La Défense, Paris — hybrid (2 days remote/week)
- Compensation: €45,000 – €55,000 / year

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
Summary line (English): "Analytics Engineer specializing in dbt, SQL and dimensional modeling — I build robust, tested, reusable data models and pipelines from Snowflake ingestion through to reporting, with a data-quality-first discipline from reconciliation work at BNP Paribas Securities Services."
Summary line (French): FRENCH CV NEEDED — French-language role at a French company; a French CV is expected. Draft placeholder until the French CV exists: "Analytics Engineer spécialisé en dbt, SQL et modélisation dimensionnelle — je conçois des pipelines robustes et des modèles de données fiables, testés et réutilisables, de l'ingestion Snowflake jusqu'au reporting. Rigueur qualité et réconciliation de données acquise chez BNP Paribas Securities Services."
Skills reorder: Variant B order. Put Snowflake and dbt up front (Snowflake is their platform). Ensure historization/SCD and data quality/governance are visible — the JD stresses "conserver l'historique" and "gouvernance et contrôle qualité."
CFA positioning: Out of summary (real-estate services company, general role). Education/experience only.
Optional adds: none.

## Cover Letter Angle
Emeria's Analytics team frames itself as "une start-up dans le groupe" with a hard rule: "pas d'analyses one shot — chaque dashboard, chaque extraction est pensée pour être réutilisable et scalable," plus "gouvernance et contrôle qualité pour assurer l'intégrité de la donnée." That is exactly the discipline behind your pc_pipeline project — a layered, tested dbt build (staging → intermediate → mart) whose whole purpose is reusable, trustworthy models rather than throwaway extracts — and behind your BNP work, where you built a data-quality framework to guarantee the integrity of numbers coming from inconsistent source systems. Tie your line to their "penser architecture avant tout : comment stocker la donnée de manière durable tout en conservant l'historique" — this is dimensional modeling with SCD Type 2 historization, which you designed from scratch at BNP (grain, client versioning, surrogate keys). Write it in French; keep it concrete and concise (their profile prizes "clair, concis, pédagogue").

## Preparation Gaps
- **French CV + French interview.** This is the first French-language role in the batch. You need the French CV (not yet created) — draft it from the English canonical, or use the placeholder summary above in the interim. Two of four interview rounds (and the technical SQL round) will be in French; rehearse explaining SQL, dbt, and dimensional modeling in French. B2 is workable but practice the vocabulary (modélisation, entrepôt, table de faits/dimension, historisation).
- **Live SQL technical round.** The process includes "un entretien technique d'1h ... pour tester ta logique et ton SQL" — an in-person live SQL test. Drill SQL problem-solving out loud: joins, window functions, aggregations, dedup/quality checks. This is the round most likely to decide it, and it's squarely in your strength — just be interview-fluent.
- **Tableau (minor).** They want a viz tool, "Tableau est un vrai plus." You have Power BI — say so; the concepts transfer. A few hours in Tableau to speak to marks/shelves/LODs is enough; don't overinvest.
- **Snowflake depth.** The platform is Snowflake — good, it's on your CV. Be ready to talk warehouses/roles, and physical modeling for reporting (clustering, micro-partitions) at concept level, since the JD stresses efficient, durable storage.
- **Real-estate / property domain.** Business partners span Immobilier, Finance, Marketing, Comptabilité. Skim the property-management data domain (copropriété, gestion locative, transactions) so you can ask the "bonnes questions" they prize.
- **AWS (bonus).** "Bonne connaissance de l'environnement AWS" is a bonus — your AWS-familiar level covers it; don't overclaim.

## Stack Analysis

### Have
- Snowflake — on CV; their core platform (strong, timely match)
- dbt — core ("DBT ou équivalent")
- SQL — strong; "maîtrises le SQL sur le bout des doigts" + live SQL test
- Data modeling / dimensional modeling — BNP + pc_pipeline ("excellente maîtrise de la modélisation")
- Historization / SCD Type 2 — BNP work maps to "conserver l'historique"
- Data quality / governance — pc_pipeline tests + BNP DQ framework ("gouvernance et contrôle qualité")
- Git / versioning — yes
- Python (bonus) — yes
- Business partnering / vulgarisation — BNP; JD leans hard on this
- Code industrialization / reusable, scalable pipelines — pc_pipeline design intent

### Missing
- Tableau specifically (you have Power BI) — minor, "un plus"
- Property/real-estate domain familiarity
- Multi-year production track record (but they only ask 1-2 years)

### Partial
- AWS — "familiar" covers the bonus ask
- Snowflake physical/performance tuning — conceptual
- French professional working level — B2 (workable; interviews partly in French)

### Green Flags
- Softest seniority bar in the batch (1-2 years) — genuinely attainable for your profile
- Snowflake + dbt + modeling + historization + governance = direct stack match
- "Pas d'analyses one shot" / reusable, scalable, industrialized — real AE thinking, not dashboard churn
- Data quality/governance is explicit — matches your discipline
- Agile, autonomous, start-up-in-a-group culture; strong business-partnering (your BNP strength)
- Not a bank/FI (real-estate services group) — passes your filter
- No age-discriminatory or vague buzzword language; concrete stack named
- Clear, structured hiring process with a real technical SQL round (rewards demonstrable skill)

### Red Flags
- None disqualifying. Watch-items: (1) heavy emphasis on dashboards for 10,000+ users + business partnering could tilt the role toward reporting/analytics support rather than deep infra — confirm in interview that modeling/pipeline engineering stays central (your "not interested in pure BI/reporting" filter). (2) Tableau-first tooling is a mild BI-lean, but engineering/modeling is clearly the spine, so not a true red flag.

## Country / Visa Note — IMPORTANT
- French-language role at a French company: FRENCH CV NEEDED (flagged above). Your B2 covers day-to-day and interviews with effort.
- SALARY vs PASSEPORT TALENT: the €45-55k band sits exactly in the sensitivity zone for the Passeport Talent salary floor, which matters directly for your residency plan. Do NOT assume it clears — the threshold changes yearly and differs by category (e.g. the "jeune diplômé / salarié qualifié" route vs others). Confirm the current exact annual-gross minimum for the category you'd apply under BEFORE investing in this process, and if you proceed, negotiate toward the €55k top of the band rather than the €45k floor. The lower end could jeopardize the visa route even if the role itself is a great fit.

## Raw JD (French, original)

À propos d'Emeria : leader mondial des services et technologies immobilières (particuliers et entreprises) — acquisition, location, gestion de copropriété, transactions. Opère en Europe (8 pays), stratégie multi-marques (Foncia, Constatimmo, Esset…).

Équipe Analytics (pôle Data, IA & data du groupe) : centralise et pilote l'ensemble des données du groupe (ERP, outils métiers, filiales internationales) pour produire dashboards et analyses éclairant les décisions stratégiques. Fonctionne comme une start-up dans le groupe : agile, autonomie forte, collaboration avec les métiers, culture du partage.

Missions (Analytics Engineer) : de l'ingestion dans la plateforme Data (Snowflake) jusqu'aux dashboards accessibles à 10 000+ collaborateurs. Transformer la donnée brute en insights actionnables.
- Business Partner Data : comprendre et traduire les besoins métiers (Immobilier, Finance, Marketing, Comptabilité…) ; donner du sens aux chiffres (tendances, aide à la décision) ; industrialiser les analyses (réutilisable, scalable, pas de one-shot) ; collaborer avec Data Scientists, DevOps.
- Concevoir et faire vivre les modèles de données : garant de la solidité/fiabilité de l'architecture ; construire, faire évoluer, optimiser les modèles.
- Build & Run : build = nouveaux pipelines, dashboards, outils ; run = maintenance, bugs, incidents, évolution des pipelines. Modéliser intelligemment (stockage efficace, durable, conservation de l'historique). Garantir qualité/fiabilité (gouvernance, contrôle qualité). Veille technologique.

Profil : 1 à 2 ans d'expérience en Analytics Engineer ou Data Analyst ; industrialisation de code ; modélisation + pipelines robustes (DBT ou équivalent) ; force de proposition ; autonome ; communication/vulgarisation ; curieux des enjeux business ; SQL maîtrisé + outil de visualisation (Tableau un plus) ; esprit analytique ; Git & versioning ; excellente maîtrise analyse/modélisation.
Bonus : Python pour automatiser/enrichir ; bonne connaissance de l'environnement AWS.

Process : visio RH 30min (Mathieu, Talent Acquisition) → visio 1h (Florian, Lead Data Analyst) → entretien technique 1h en présentiel avec deux membres de l'équipe data (logique + SQL) → visio 30min (Florent, Chief Data Officer).
Fourchette salariale : 45-55K€. Localisation : La Défense (2 jours de télétravail/semaine).
