# Qonto — Analytics Engineer (x Business Analytics) — 2026-08

## Metadata
- Date: 2026-08-28
- Fit Score: High — near 1:1 match. dbt + SQL + dimensional modeling + tests + semantic-layer migration + business partnering + end-to-end ownership is exactly your stack and your BNP/pc_pipeline story. No hard years-of-experience gate, Tier 2 target, explicitly merit-based/inclusive hiring.
- Source: Direct paste (LinkedIn)
- Contract: Full-time — CDD/CDI unstated, effectively permanent (CDI expected)
- Location: Paris, France (Qonto HQ) — hybrid; English-working, 80+ nationalities

## CV Tailoring Instructions
Variant: B (General Modern Stack)
Branch: variant-b-general
Summary line (English): "Analytics Engineer specializing in dbt and dimensional modeling — I ship tested, production-grade data models teams build dashboards on, and treat data quality as a design constraint, not an afterthought. Backed by private-capital domain depth from BNP Paribas Securities Services."
Summary line (French): French CV not required — Qonto works in English (80+ nationalities). B2 French is a plus to mention in the cover letter / interview, not a blocker. Optional placeholder: "Analytics Engineer spécialisé en dbt et modélisation dimensionnelle — je livre des modèles de données testés et fiables sur lesquels les équipes construisent leurs dashboards."
Skills reorder: Keep Variant B order (Transformation → Modeling → Warehousing → BI/Semantic → Domain). Ensure "dbt Semantic Layer" is visible under BI & Semantic — the semantic-layer migration is central to this role.
CFA positioning: Keep OUT of the summary line (Tier 2). Leave in education/experience only — lead with engineering.
Optional adds: none — the on-CV projects (pc_pipeline, Sales Analytics DW) already carry this. Do not add Guosen/UOB; finance domain is a light bonus here, not the pitch.

## Cover Letter Angle
Qonto's ask is unusually specific: an Analytics Engineer who will "push back on requests that would trade reliability for speed" and "reduce technical debt at scale," while the team migrates to Omni and a real semantic layer. That is the exact posture behind your pc_pipeline project — a layered dbt pipeline whose reason for existing is a test suite covering six real data-defect classes, so that downstream marts are trustworthy before anyone builds on them — and behind your BNP work, where you built a data-quality framework surfacing identity-resolution failures, duplicate detection, and cross-source inconsistencies in manually maintained private-capital data. Tie your line directly to Jules's framing (he's rebuilding how AEs and BAs work together): you don't treat data quality as a QA step after modeling, you treat it as the modeling constraint — which is precisely what lets an AE say no to a fast-but-fragile request without damaging the relationship, because the pushback is grounded in a standard, not a preference. You're also already living the semantic-layer transition yourself (building a dbt Semantic Layer / MetricFlow layer on pc_pipeline), so Qonto's move to Omni's semantic layer is a shift you understand from the inside, not a buzzword.

## Preparation Gaps
- **Omni — learn it specifically.** This is the one concrete tool gap. Understand what Omni is (a BI + semantic-layer platform), how its modeling/semantic layer compares to the dbt Semantic Layer / MetricFlow you've been building, and *why a company migrates to it* (governed metrics, self-serve, killing dashboard sprawl / metric drift). Be ready to talk about what makes a semantic-layer migration hard (metric parity, trust, deprecating old dashboards) — you don't need hands-on Omni, you need a credible point of view on the migration.
- **"Production-grade models other teams build dashboards on."** Extend your pc_pipeline story from "it has tests" to "how I'd make a model reliable for downstream consumers": model contracts, incremental models, CI on PRs, exposures, documentation, and clear layering conventions (staging/intermediate/mart discipline). Have a crisp answer to "how do you keep a model trustworthy six months later."
- **A concrete stakeholder-pushback story (STAR).** They test this twice in the JD. Prepare one real example — the BNP data-quality framework is the material: a case where surfacing a data issue changed what got shipped, told so the *relationship* stays intact. Rehearse the "challenge without shutting down the relationship" framing explicitly.
- **AI-native workflow — bring a real example.** This is weighted heavily and repeatedly. Have a genuine, specific instance of using AI beyond chat: e.g. generating dbt tests or model YAML/docs from a schema, or using an LLM to draft/refactor SQL and then validating it. Be ready to say where you *distrust* the output and check it — they explicitly want "know when to trust it and when to question it."
- **dbt at scale / tech debt.** Skim patterns for reducing dbt tech debt: DRY macros, removing redundant models, incremental strategies, model naming/ownership standards. The role is partly a standards-setting role ("building the standards that will define how Analytics Engineering works at Qonto").

## Stack Analysis

### Have
- dbt — core, on CV and in pc_pipeline (staging → intermediate → mart, star schema)
- SQL — strong (CTEs, window functions, subqueries)
- Dimensional modeling — explicitly the JD's emphasis; your BNP model (grain, SCD Type 2, surrogate keys) and pc_pipeline both demonstrate it
- dbt tests / data quality — pc_pipeline test suite (6 defect classes) + BNP data-quality framework; this is the JD's central theme
- Semantic layer — dbt Semantic Layer / MetricFlow experience; conceptually transfers to Qonto's Omni move
- Business partnering — BNP work embedded with business, translating needs into models
- End-to-end ownership — pc_pipeline is discovery-to-delivery, self-built
- Python, Git — for AI-assisted workflows and version control

### Missing
- Omni (their target BI/semantic platform) — genuine tool gap, but they're mid-migration and will onboard you into it
- Large-scale, multi-team production track record — your production work is one internship + portfolio, not years of "other teams depend on my models." Not disqualifying (no years gate), but the seniority ceiling ("if senior") won't apply to you yet — pitch as the mid-level, high-ownership hire.

### Partial
- "Production-grade models other teams build dashboards on top of" — BNP + Sales Analytics DW are real but not yet at multi-team scale; frame honestly with the reliability discipline you bring
- AI-native workflow — you use AI tools; needs one sharp, concrete modeling/testing example to land as "AI-native" rather than "AI-curious"
- dbt-at-scale / tech-debt reduction — you know good structure; less experience with large legacy refactors specifically

### Green Flags
- dbt-first, transformation-and-modeling-centric role — no BI-first framing
- Semantic layer explicitly central (Omni migration)
- Data quality / reliability is the spine of the role — matches your testing-first approach exactly
- Real engineering ownership + standards-setting, not ticket execution
- Specific, concrete context (named manager, named team scopes, real migration) — the company knows what it wants
- Clear AE-vs-BA distinction — you're the engineer the analysts build on
- Strongly inclusive, merit-based hiring language ("apply regardless of the boxes you tick", discrimination-free process) — the opposite of the age/"young dynamic team" red flags; a real plus
- English-working environment — no French-CV blocker
- Not a traditional bank — profitable fintech/SME finance workspace with a real product

### Red Flags
- None identified. The heavy "AI-native" emphasis is substantive here (Qonto has a published AI vision), not filler — treat it as a genuine requirement to prepare for, not a warning sign.

## Notes
- Seniority: the JD accommodates both mid and senior ("if senior, ... raise the team's standards"). Apply as the mid-level, ownership-ready hire; don't overclaim the standards-ownership/mentoring track yet.
- French: B2 is a nice-to-have signal (manager Jules is French; culture content is bilingual) but not required — mention it, don't lead with it.
- Salary: if this advances, confirm the current Passeport Talent minimum annual gross before negotiating (changes yearly) — a permanent AE role at Qonto should clear it.

## Raw JD

Mission: Join us as Analytics Engineer x Business Analytics — become the person the Business Analytics teams can build on without a second thought. Own end-to-end the data models feeding Product, Growth, and Ops Finance analytics — designing scalable dbt models, pushing back on requests that would trade reliability for speed, and helping the team migrate to Omni and a real semantic layer. Work closely with Jules Jeanroy (Analytics Engineering Manager) and partner daily with Business Analysts across Product, Growth, and Ops Finance. Team is at a pivotal moment — investing in scalability, cutting technical debt, building standards.

As an Analytics Engineer you will:
- Build data models Business Analytics teams trust — design and ship dbt models and tests that hold up under real everyday use across Product, Growth, and Ops Finance
- Partner with Business Analysts, not just execute for them — understand what they actually need, and push back when a request would trade long-term reliability for a quick fix
- Reduce technical debt at scale — help migrate parts of the data stack to a more scalable setup, including the ongoing move to Omni
- Own your projects end-to-end — from discovery through delivery, following up on real impact
- Scale your own workflow with AI — use AI tools to speed up documentation, testing, and modeling, keeping judgment calls in your hands

What you can expect:
- Join at a pivotal moment — team is scaling and migrating to Omni
- Room to move — grow horizontally across Business Analytics, Compliance, and Foundation scopes, or toward mentoring/standards ownership as a senior profile
- Business partnering is core, not incidental — daily work with Product, Growth, Ops Finance; challenging a request without damaging the relationship matters as much as technical chops
- AI is the multiplier — used daily; expected to use it for modeling, documentation, testing, not just as a coding assistant

Manager: Jules Jeanroy, Analytics Engineering Manager. Joined Qonto March 2026 to lead the AE team partnering with Business Analysts. Focus on strengthening AE/BA collaboration, reliable high-quality data foundations, scaling data practices. Previously Lead Analytics Engineer at Spendesk and BI Engineer at Brevo. Direct and collaborative style.

About You:
- Analytics Engineering fundamentals — strong in dbt and SQL, especially dimensional modeling; shipped production-grade models other teams build dashboards on top of
- Comfortable pushing back — challenge a stakeholder request that would hurt data quality without shutting down the relationship
- Built for scale, not just speed — design models that hold up months later; know when "good enough now" beats "perfect later"
- AI-native work style — use AI tools beyond chatting, to speed up modeling, documentation, or test generation
- Appetite for ownership — take projects end-to-end, and if senior, help raise the team's standards

Company: Qonto — Europe's leading finance workspace for SMEs, banking at its core plus financial tools. Trustpilot 4.8 (55,000+ reviews), NPS 75. Founded 2017 by Alexandre Prot and Steve Anavi. 1,600+ employees, 600,000+ customers, 8 European countries, profitable since 2023. 80+ nationalities, 45% women (56% of women in leadership). Discrimination-free, merit-based hiring. AI deeply embedded; unlimited access to AI tools.
