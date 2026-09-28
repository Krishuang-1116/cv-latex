# Dashlane — Analytics Engineer — 2026-08

## Metadata
- Date: 2026-08-28
- Fit Score: Medium (stretch) — tooling/stack fit is among the best you've seen (dbt, Omni, AWS, Airflow, GitLab, Claude Code / AI-native), but it is explicitly a SENIOR role: "3+ years", "senior technical contributor", "mentor more junior engineers", plus B2B-SaaS-metrics fluency (ARR/NRR/churn/PLG) you don't yet have. Apply only with a deliberate punch-up narrative; expect the 3+ years line to be the filter.
- Source: Direct paste (LinkedIn)
- Contract: Full-time — CDD/CDI unstated (CDI expected)
- Location: Paris, France — hybrid (office Mon/Tue/Thu), English working language. Founded Paris; offices NY + Lisbon.

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
Summary line (English): "Analytics Engineer building tested, production-grade dbt models and treating data as a product — turning messy source data into clean single-source-of-truth models, with a data-quality-first discipline and an AI-native workflow (dbt tests, docs, and modeling accelerated with Claude Code)."
Summary line (French): French CV not required — Dashlane works in English. No placeholder needed.
Skills reorder: Variant B order. Push "AI-native workflow / Claude Code" high — this JD makes "AI Champion" a hard requirement, and it's one of your few genuinely senior-grade signals. Keep dbt + data quality + Omni/semantic visible.
CFA positioning: Out of summary (Tier 2 / general SaaS). Education/experience only.
Optional adds: none on the base CV. If you want to signal SaaS-metric awareness, address it in the cover letter, not by bolting projects on.

## Cover Letter Angle
Dashlane's first bullet is "untangle historically messy datasets (like Salesforce) and refactor them into clean, intuitive models that serve as a single source of truth," and its governance bullet is about data-quality tests that make the org trust the data. That is the literal purpose of your BNP work: you built a data-quality framework over manually maintained private-capital data — surfacing identity-resolution failures, duplicate detection, and cross-source code inconsistencies — and a dimensional model (grain, SCD Type 2, surrogate keys) that turned three inconsistent source systems into one coherent model. Pair that with the "AI Champion" requirement, where you have an unusually authentic story: you don't just use AI as a chat assistant, you run an AI-native analytics workflow — using Claude Code to accelerate dbt test generation, model documentation, and even to systematize your own decision pipelines — and you know where to distrust the output and verify it. Be honest about level: frame yourself as an AE who already works the way their senior contributors are supposed to (data-as-a-product, quality-first, AI-accelerated), punching toward the role rather than claiming 3 years you don't have.

## Preparation Gaps
- **B2B SaaS metrics — this is the real domain gap.** You speak ARR of private-capital/finance, not SaaS. Learn cold: ARR/MRR, NRR vs GRR, logo vs revenue churn, expansion/contraction, CAC/LTV, and product-led-growth funnel metrics — and specifically how these get modeled in dbt (subscription/event grain, snapshotting MRR, cohort retention). Without this you'll stall in the business-acumen screen.
- **Salesforce data modeling.** Understand why Salesforce data is notoriously messy (Account/Contact/Opportunity/Lead object model, custom fields, history tables) and the standard AE pattern for refactoring it into clean staging + marts. This is called out by name.
- **AWS data platform (Redshift-centric).** You're "AWS familiar"; go deeper on Redshift physical modeling — distribution keys, sort keys, and how that pairs with dimensional design (this is exactly the "table distribution/indexing" theme from other JDs). Know at a concept level what S3/Lambda/Kinesis/Glue each do in an ELT pipeline.
- **Airflow + GitLab CI/CD.** You're concept-level on orchestration; be able to explain DAG scheduling, dependencies, and how dbt runs are orchestrated in Airflow, plus a dbt-on-GitLab CI flow (MR pipelines, slim CI, test-on-PR).
- **Omni + semantic layer** (same as Qonto). Governed metrics, self-service, why migrate to it — you can speak to this from your dbt Semantic Layer work.
- **"AI data agents" for reporting/alerting.** They want you to implement AI agents that automate metric reporting/alerting. Have a concrete POV: an LLM agent over the semantic layer that watches metrics, detects anomalies, and drafts alerts — and the guardrails (grounding on governed metrics, human-in-the-loop). This is where your AI-native edge can actually differentiate you against more senior but less AI-fluent candidates.
- **Seniority framing.** Prepare a direct, non-defensive answer for "you have less than 3 years" — lead with scope and quality of what you've built, and the AI-multiplier argument (you deliver senior-level output velocity with AI).

## Stack Analysis

### Have
- dbt — core (JD: "expert in SQL and dbt")
- SQL — strong
- Dimensional modeling — BNP + pc_pipeline (JD wants complex production models, single source of truth)
- Data quality tests / governance — pc_pipeline test suite + BNP DQ framework (JD: "implement and maintain data quality tests and governance")
- Python — yes (stack lists SQL + Python)
- Semantic layer / self-service concept — dbt Semantic Layer; transfers to Omni
- AI-native workflow / Claude Code — genuine, authentic (their exact stack + "AI Champion" requirement); one of your strongest, rarest signals here
- Data-as-a-product mindset — matches pc_pipeline's design intent

### Missing
- 3+ years AE experience / "senior technical contributor" / mentoring juniors — you are a graduating intern; this is the primary barrier
- B2B SaaS metric fluency (ARR/NRR/churn/PLG) — your domain is finance/private capital
- Salesforce data experience — named explicitly; you haven't worked it
- Production experience at multi-team scale over years

### Partial
- AWS platform — "familiar"; Redshift/S3/Lambda/Kinesis/Glue depth not yet there
- Airflow orchestration — concept-level (DAG principles via dbt)
- GitLab CI/CD — Git yes, GitLab dbt CI flow specifically not yet
- Omni — no hands-on, concept transfers from dbt Semantic Layer
- "AI data agents" — you use AI in-workflow, but building agentic reporting/alerting is a build you'd need to reason about, not something you've shipped

### Green Flags
- dbt-first, data-as-a-product, single-source-of-truth framing — engineering-and-modeling centric
- Data quality + governance is a first-class responsibility — matches your discipline
- Omni self-service + semantic layer (same modern direction as Qonto)
- AI-native is central and their stack literally includes Claude Code — authentic fit for you
- Clear ownership + consultative partnering (not ticket execution)
- Strongly inclusive DEI language (age listed as a diversity dimension positively) — no age red flags
- Not a bank; real B2B/B2C SaaS product; English-working (no French-CV blocker)

### Red Flags
- None on JD *quality* — the role is well-defined. The concern is purely fit level: the "3+ years / senior / mentor juniors" framing makes this a reach for a new-grad profile. Treat as a targeted stretch application, not a core-tier match.

## Notes
- Rank below Qonto for now: Qonto has the same dbt/Omni modern-stack appeal with NO hard seniority gate. If prioritizing effort, Qonto first; Dashlane as a stretch/"why not" application where the AI-native angle carries you.
- Salary: confirm current Passeport Talent minimum annual gross before negotiating (yearly change); a senior AE role clears it comfortably if you land it.

## Raw JD

About the role: Dashlane (credential security; 25,000+ brands incl. Michelin, Air France, Forrester; patented zero-knowledge security; founded Paris, offices NY + Lisbon, 300+ employees). Seeking an Analytics Engineer for the Data & Analytics team — a strategic partner to the business bridging technical modeling and business strategy, transforming the team from reactive support into a proactive strategic function; building AI-ready data foundations, tackling complex data architecture, empowering self-service, and mentoring peers. Paris-based, English working language, hybrid (office Mon/Tue/Thu).

At Dashlane you will:
- Build & own complex data models end-to-end within a dbt-powered "Unified Data Model"; untangle messy datasets (like Salesforce) into clean single-source-of-truth models
- Drive proactive business impact — consultative partner to Product + Go-to-Market teams; move beyond reactive support to uncover business problems and deliver proactive insights ("what happened" → "what's next")
- Champion self-service & upskill stakeholders — drive self-service analytics culture, guide stakeholders to scalable self-serve solutions in Omni, push back on ad-hoc dashboard requests
- Pioneer AI data agents & automation — implement AI data agents and underlying foundations to automate reporting/alerting for key business metrics, AI-first mindset
- Elevate data governance & the team — implement/maintain data quality tests and governance; as a senior technical contributor, mentor junior engineers, improve team processes, raise the technical bar

Requirements:
- 3+ years in an Analytics Engineering position or equivalent
- Expert in SQL and dbt, deep hands-on experience designing/deploying/maintaining complex data models in production
- Strong strategic business acumen and deep understanding of the B2B SaaS engine; fluent in ARR, NRR, churn, product-led growth
- Highly consultative stakeholder management; uncover the true business need, drive alignment, take proactive end-to-end ownership
- "AI Champion" — fluent with AI coding platforms such as Claude Code; demonstrated experience integrating GenAI tooling into day-to-day analytics workflow; eager to mentor the org on these tools
- Thrive in autonomous, high-exposure environment; relentless curiosity
- Fluent in English (verbal and written)

Tech stack:
- Data Modeling & Transformation: dbt
- Programming: SQL, Python
- Data Platform: AWS (Redshift, S3, Lambda, Kinesis, Glue)
- BI & Visualisation: Omni
- Orchestration: Airflow
- CI/CD & Version Control: GitLab
- AI: Claude Code

DEI: international company (France, US, Portugal); values gender identity, sexual orientation, ability, ethnic origin, social background, age, lifestyle; committed to diverse hiring and belonging.
