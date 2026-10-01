# Fitch Group (Chief Data Office) — Data Analytics Senior Associate, Conversational Analytics — London — 2026-09

## Metadata
- Date: 2026-09-30 (reposted ~1 week ago)
- Fit Score: HIGH, probably your closest content match of the whole search. The job is literally pc_pipeline's agent at enterprise scale: agentic AI over data/dashboards via natural language, AI-ready data, semantic layers ("a metric means the same thing everywhere"), knowledge-base authoring, agent routing, accuracy/permission testing, evaluation (accuracy, latency, cost). Early-career gate is explicit and inclusive: 1–3 years OR internships OR substantial end-to-end projects. Financial-information company (ratings), so the CFA is relevant. "Senior Associate" is Fitch's early-career title here, not a seniority gate.
- Tailoring effort: ZERO. Send `output/cv_kris_huang_mckinsey_data_engineer_i.pdf` (summary: dbt + semantic layer + LLM agent → validated SQL + RAG with LLM-as-judge eval + BNP data quality + CFA).
- Source: LinkedIn (direct paste)
- Contract: Not stated (permanent expected)
- Location: London (team spans London and New York)
- Compensation: Not stated
- Company: Fitch Group (Fitch Ratings, Fitch Solutions, Fitch Learning), owned by Hearst. Team: Enterprise Data & Analytics under the Chief Data Officer.

## UK work authorization (checked 2026-09-30, reference/check_sponsor.py, register 2026-09-29)
- Sponsor: "Fitch Ratings Limited", London, Worker (A rating), Skilled Worker (+ Global Business Mobility). "Fitch Solutions" and "Fitch Group" aren't listed as separate entities. Confirm the employing entity is Fitch Ratings Limited (a central CDO role likely is). Ignore B A Fitch / Carter Fitch / Franklin Fitch (unrelated).
- Salary must clear the Skilled Worker threshold (£41,700 or going rate); an early-career "Senior Associate" band may be close. Ask early.
- Right-to-work form: "I currently do not have the right to work in the UK and would require company visa sponsorship."
- Fitch Ratings requires a securities-holdings / conflict-of-interest declaration on hire; you may need to divest conflicting holdings.

## CV Tailoring Instructions
Variant: B, AI/semantic-layer-forward (CFA at the end of the summary is a plus here). ENGLISH. Reuse the McKinsey PDF; no new build.
Optional tracking copy: `cp output/cv_kris_huang_mckinsey_data_engineer_i.pdf output/cv_kris_huang_fitch_conversational_analytics.pdf`. Rename to a neutral filename when attaching.

## Cover Letter Angle
Map their bullets to what you built:
- Agentic AI over data ↔ pc_pipeline LLM agent that turns natural-language questions into validated SQL.
- Semantic layers / "a metric means the same thing everywhere" ↔ your MetricFlow semantic layer; the agent answers through defined metrics, not raw tables. That's why it's reliable.
- Testing, evaluation (accuracy, latency, cost) ↔ LVMH LLM-as-judge evaluation framework for a multi-turn RAG chatbot.
- AI-ready data + data modeling judgement ↔ BNP dimensional model (grain, SCD2) and data-quality framework; pc_pipeline tests (6 defect classes).
- Knowledge base authoring ↔ RAG corpus design at LVMH.
- MCP ↔ you build daily with MCP-connected tooling (Claude Code). Say it only at the level you've actually done it.
- Financial information domain ↔ CFA; you understand what ratings/research users actually ask.
One closing line: "The failure mode I care about most is an agent answering confidently with the wrong metric definition. Semantic models plus per-dashboard evaluation are how you prevent it."

## Preparation Gaps
- Agent routing: intent classification vs embedding similarity vs LLM router; fallbacks and "I don't know" behaviour; routing eval.
- Permissioning: row-level security, ensuring the agent respects the user's dashboard permissions (a named test item).
- Evaluation design: golden question sets per dashboard, exact-match vs LLM-judge scoring, latency/cost tracking, regression tests on onboarding.
- MCP basics: servers/tools/resources; how an MCP server could expose a dashboard's semantic model to an agent.
- BI platforms: Qlik/Tableau semantics vs Power BI datasets; what "AI-ready dashboard" means (clean measures, descriptions, synonyms).
- Fitch products: ratings, research, sector data. Know what a business user might ask a dashboard.

## Stack Analysis

### Have
- LLM agent over a semantic layer (NL → validated SQL): the core of the role
- Semantic layer / metric definitions (MetricFlow)
- LLM evaluation (LLM-as-judge), RAG/knowledge-base work (LVMH)
- Data modeling judgement, SQL, Git, Python
- BI: Power BI
- Stakeholder work with business owners (BNP, LVMH)
- Financial domain (CFA)

### Missing
- Agent routing across many data sources in production
- Enterprise permissioning/RLS testing
- Qlik/Tableau

### Partial
- MCP: user-level/tooling experience, not built servers (verify what you can claim)

### Green Flags
- Explicitly early-career; projects count
- The role is your differentiator
- Established prototype to scale: learning + ownership
- CDO-level visibility; London + NY
- Licensed sponsor (Fitch Ratings Limited, A rating)

### Red Flags
- Reposted: may have high applicant volume, or a hard-to-fill profile (the latter helps you)
- Salary vs Skilled Worker threshold unknown
- Securities conflict-of-interest declaration (a standard ratings-agency requirement)
- UK move restarts the French residency clock
- No age-discrimination wording

## Notes
- Verdict: APPLY, top priority in London. Try a referral or a note to the CDO team (Enterprise Data & Analytics).

## Raw JD (abridged)
Fitch Group CDO, Enterprise Data & Analytics, London. Senior Associate, Conversational Analytics: early-career, productive quickly, ownership in analytics + AI; scale conversational analytics across dashboards with product owners.
Work: agentic AI workflows (NL interaction with data/dashboards, existing prototype); AI-ready data with dashboard owners; semantic layers & ontologies; knowledge base authoring; agent routing; testing (accuracy, permissioning) and reusable checks; evaluation & benchmarking (accuracy, latency, cost, user impact).
Need: CS/DS/Maths degree or equivalent + delivery evidence (1–3 years, internships, or substantial end-to-end projects); curiosity about AI/LLMs; interest in data modeling; strong interpersonal skills with product owners; independence.
Stand out: data modeling/metadata/semantic layers; conversational AI/LLM/agents; MCP connections; BI (Qlik, Power BI, Tableau); Git; SQL (helpful, not essential).
Conflict-of-interest: declare securities holdings; may need to divest.
