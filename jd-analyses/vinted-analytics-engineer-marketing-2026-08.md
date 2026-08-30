# Vinted — Analytics Engineer (Marketing) — 2026-08

## Metadata
- Date: 2026-08-30
- Fit Score: Medium-High (technical) — strong dbt + SQL + data-quality + business-partnering match, softened seniority ("typically ~3 years", "guides not checklists, apply anyway"). Gated by: marketing domain (new to you), tool swaps (BigQuery/Looker vs Snowflake/Power BI), Airflow (concept-level), and production on-call reliability (partial). The DECIDING factor is non-technical: Netherlands base + work-authorization + divergence from your France residency plan.
- Source: Direct paste (LinkedIn)
- Contract: Permanent, full-time — hybrid (2 recommended office days)
- Location: Netherlands (Amsterdam) — English working language
- Compensation: €53,900 – €72,900 gross/year + 8% holiday pay (≈ €58.2k – €78.7k effective) + share options

## STRATEGIC / VISA NOTE — read first
- This is NOT France. It cuts against your stated preference to stay in France 1–2 years for long-term residency: taking a Netherlands role restarts the residence clock in a different country (NL permanent residence / long-term EU status is a separate ~5-year track). Decide whether you're genuinely open to basing in the Netherlands before investing — the profile lists NL as "considered," so this is a real choice, not an automatic yes.
- Netherlands work authorization (non-EU): the standard route is the **Highly Skilled Migrant (kennismigrant)** permit. Requirements: (1) the employer must be an **IND-recognised sponsor** — verify Vinted's Dutch entity is (large tech employers usually are, but confirm), and (2) a gross salary at or above the IND threshold. There is a **reduced threshold** for recent graduates / under-30 / people on the post-study "orientation year" (zoekjaar) permit, and a higher standard threshold otherwise. The €53.9–72.9k band likely clears the reduced threshold and possibly the standard one — but thresholds change yearly; **confirm the current 2026 figures and which category applies to you** before assuming eligibility.
- As an ESSEC graduate you may qualify for the Dutch **orientation-year permit**, which lets you work without the employer sponsoring and lowers the salary bar — worth checking; it can de-risk this.

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
Summary line (English): "Analytics Engineer building tested, reliable dbt data models teams depend on — dimensional modeling, data-quality frameworks (tests, reconciliations, anomaly checks), and clean documented datasets from messy multi-source ingestion."
Summary line (French): N/A — English-working (Netherlands). No French CV needed.
Skills reorder: Variant B. Lead with dbt + SQL + data quality. Note BigQuery is a swap from Snowflake/Postgres (say "SQL warehouses: Snowflake, PostgreSQL, BigQuery-ready"); Looker is a swap from Power BI.
CFA positioning: Out of summary and de-emphasized — irrelevant to a marketing AE role; keep in education only.
Optional adds: none. Domain framing is "eager to learn marketing," not bolting on projects.

## Cover Letter Angle
Vinted's role is built around trust in data that comes from "diverse external sources": data-quality checks (tests, regressions, anomaly detection), owning production reliability with end-to-end root-cause analysis, and shipping fixes that prevent repeat failures. That is precisely the discipline behind your BNP data-quality framework — surfacing identity-resolution failures, duplicate detection, and cross-source inconsistencies across three source systems — and your pc_pipeline dbt test suite covering six real data-defect classes so that models are trustworthy before anyone builds on them. Tie your line to the 40+ Analytics Engineering Guild: you already build the way they work — tested, documented, reusable dbt models designed for other people to depend on — and you're eager to apply that reliability-first mindset to the marketing domain. Keep it honest: you're strong on the engineering and data-integrity half; the marketing domain is what you'd ramp on fast.

## Preparation Gaps
- **Marketing data domain — the real domain gap.** Learn the vocabulary and pipelines: channel/campaign performance, attribution models, ROAS/CAC/spend, UTM and ad-platform data (Google Ads, Meta, etc.), and marketing mix / model-driven optimisation (the JD names "Marketing Modelling Intelligence"). You speak finance metrics, not marketing — close enough to be conversant in an interview.
- **BigQuery** (swap from Snowflake/Postgres). SQL transfers directly; learn BQ specifics: partitioning/clustering, the slot/cost model, and standard-SQL quirks. Frame yourself as "warehouse-agnostic, BigQuery-ready."
- **Looker / LookML** (swap from Power BI). Understand Looker's modeling layer (LookML, explores) — conceptually close to your dbt Semantic Layer experience; lead with that bridge.
- **Airflow** — you're concept-level (DAG principles via dbt). Get hands-on-ish: authoring DAGs, operators, scheduling, retries, and how dbt runs are orchestrated in Airflow.
- **Production reliability / incident RCA.** New territory — be ready to talk root-cause analysis, pipeline monitoring/alerting, anomaly detection on metrics, and preventing repeat failures. Your testing-first habit is the foundation to build the answer on.

## Stack Analysis

### Have
- dbt — core (JD: "hands-on dbt, obvious well-tested performant models")
- SQL — strong (JD: readable, maintainable, performance at scale)
- Data quality / tests / reconciliations / anomaly checks — BNP DQ framework + pc_pipeline test suite (this is the JD's spine)
- Dimensional modeling — decision-ready datasets from raw ingestion
- Python — yes (part of their stack)
- Git / PRs / code review — yes
- Business partnering / translating needs — BNP; JD wants requirements-gathering + documentation
- Reusable, documented, dependable models — pc_pipeline design intent; fits the 40+ AE Guild culture

### Missing
- Marketing domain knowledge (attribution, channels, MMM, ad-platform data)
- BigQuery (hands-on) — SQL transfers, but not the platform yet
- Looker / LookML — you have Power BI
- Production on-call reliability / incident RCA track record
- ~3 years experience (soft: "typically", and "apply anyway")

### Partial
- Airflow — concept-level via dbt DAGs
- GCP ecosystem — AWS-familiar, not GCP
- Ingestion from diverse external sources — TripAdvisor/pc_pipeline touch this; not at marketing-pipeline scale

### Green Flags
- dbt-first, end-to-end (raw ingestion → trusted documented datasets), data-quality-centric — matches your strengths
- Reliability + tests + anomaly detection is a first-class responsibility
- 40+ AE Guild with code reviews, reusable components, knowledge sharing — great for a strong early-career AE to level up fast
- Soft seniority framing ("typically ~3 years", explicit "apply anyway, guides not checklists")
- Strong inclusive/equal-opportunity language — no age red flags
- English-working; not a bank; real product; strong comp + benefits + learning budget

### Red Flags
- None on JD quality. Non-fit considerations only: marketing-domain unfamiliarity, tool swaps, and — most importantly — the Netherlands relocation / visa / France-residency tradeoff above.

## Notes
- Ranking: technically comparable to Qonto/Emeria on the AE+DQ axis, but the country decision dominates. If you're open to the Netherlands, this is a strong application with a supportive Guild structure ideal for early-career growth. If your France-residency plan is firm, deprioritize despite the good fit.
- Comp is healthy (€53.9–72.9k + 8% holiday pay + share options) and well above typical French mid-level bands — a genuine upside of the NL market if you consider relocating.

## Raw JD

Company: Vinted — second-hand fashion marketplace. Three units: Vinted Marketplace (20+ markets), Vinted Go (shipping/logistics, 500k+ pick-up/drop-off points, 60+ carriers), Vinted Pay (payments). Founded 2008 Lithuania, HQ Vilnius, 2,000+ people, offices across Europe.

Role: Analytics Engineer in Marketing. Design, build, operate business-critical marketing data pipelines teams rely on to optimize marketing performance and decision-making. Build robust future-proof pipelines that ingest, process, and monitor data from diverse external sources for high-integrity data. Build deep marketing-domain understanding; proactively identify data process-optimisation opportunities. End-to-end across BigQuery, dbt, Airflow: raw ingestion → transformations → trusted, well-documented datasets → domain-ready reporting.

Partners: Marketing Operations Intelligence + Marketing Modelling Intelligence teams; other Marketing AEs (shared domain ownership); a 40+ person Analytics Engineering Guild (established patterns, code reviews, reusable dbt/python components, knowledge sharing). Reports to Manager of Data Science & Analytics, Marketing Analytics Engineering.

You'll:
- Design/build scalable reliable marketing data models in dbt/BigQuery/Looker → decision-ready datasets for reporting, analysis, optimization
- Implement data quality checks/controls (tests, regressions, anomaly detection) for reliability/consistency
- Own production reliability: investigate incidents end-to-end, root-cause analysis, ship fixes preventing repeat failures
- Translate marketing needs into technical delivery: gather requirements in plain language, align definitions, document models/metrics
- Drive adoption/correct usage via practical documentation, enabling self-serve analysis

About you:
- Hands-on Analytics/Data Engineering (typically ~3 years) or related role with ownership of production pipelines
- Strong SQL (readable, maintainable, performance at scale)
- Hands-on dbt (obvious, well-tested, performant models); rest of stack a plus (GCP, Airflow, Python, Looker)
- Working knowledge of Git + collaboration (PRs, code reviews, version control)
- Strong attention to detail (tests/reconciliations, edge cases, consistent documented metric definitions)
- Problem-solving/optimization mindset
- Strong communication/collaboration; translate business needs to technical solutions
- Excellent English

Salary: €53,900–€72,900 gross/year excluding 8% holiday pay. Benefits: share options, 25 days leave, learning budget €3,000+, workation policy, hybrid (2 office days), pension, NS Business Card, etc. Netherlands-based. Equal opportunity ("guides not checklists, apply anyway").

## Visa — RESOLVED (researched 2026-08-30)
Netherlands work authorization is NOT a barrier for this profile.
- **Orientation-year (zoekjaar) permit:** non-Dutch grads qualify if the
  Master's is from a top-200 university (THE/QS/ARWU). Kris's ESSEC &
  CentraleSupélec degree qualifies via CentraleSupélec / Université Paris-Saclay
  (QS top 80, ARWU global top ~15–20, 2026). Apply within 3 years of graduation.
  Permit allows job-search + work with NO employer sponsorship. (Confirm IND
  accepts the joint ESSEC-CentraleSupélec diploma under the Paris-Saclay listing
  — very likely yes; ESSEC alone doesn't appear in those general rankings.)
- **HSM salary thresholds 2026 (gross/month, excl. 8% holiday allowance):**
  30+ €5,942 · under-30 €4,357 · **reduced criterion €3,122**.
- **Reduced criterion is AGE-INDEPENDENT** — applies to orientation-year holders
  / grads within 3 years of graduation, regardless of being over 30. So at ~33,
  converting to HSM after a ~1-year orientation-year search still uses €3,122/mo,
  valid for 3 years from graduation (grad ~Jan 2027 → window to ~Jan 2030).
- **Vinted's band (€53.9–72.9k ≈ €4,491–6,075/mo) clears the reduced threshold
  by a wide margin** — and clears the under-30 bar across the entire band.
- Only risk: converting AFTER the 3-year reduced window (~Jan 2030) reverts to
  the standard 30+ bar (€5,942/mo ≈ €71.3k), which the lower salary band misses.
  Convert within the window and age is a non-factor.
- Figures are 2026 and checked at application time — reconfirm when applying.
- Bottom line: the Netherlands decision is purely the France-vs-NL residency
  strategy, not eligibility.
