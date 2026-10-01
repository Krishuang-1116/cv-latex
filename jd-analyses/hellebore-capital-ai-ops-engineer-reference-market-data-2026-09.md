# Hellebore Capital — AI Ops Engineer, Reference & Market Data — 2026-09

## Metadata
- Status: TO APPLY (short note required, draft below)
- Date: 2026-09-30
- Fit Score: HIGH on odds, MEDIUM on career direction. Recent grads are welcome, a Bac+5 is required, and finance is "taught in-house". As a CFA with credit experience (UOB) and an identity-resolution/data-quality track record (BNP), you'd be far above their stated bar. Agents + prompt/rule tuning + coding agents match how you already work. Caveat: this is AI-pipeline supervision / data ops, not analytics engineering. There's no dbt, warehouse or modelling, and the platform (OtcStreaming) is proprietary.
- Tailoring effort: LOW. A summary swap. The short note matters more than the CV.
- Source: LinkedIn (direct paste)
- Contract: Full-time (CDI presumed; confirm)
- Location: Paris, up to 20% remote
- Compensation: €48k gross. Clears the Passeport Talent salarié qualifié / jeune diplômé threshold (≈€39.6k for 2026 per Parakar, which lists it as 2x SMIC; if the true rule is 2x SMIC at 35h, that gives ≈€43.8k. €48k clears either way; confirm with the prefecture guidance/employer). Consistent with the Paris junior-DE benchmark (€45–60k).
- Company: Hellebore Capital, Paris credit investment firm (bonds, CDS). Small, AI-first operations. Role reports to the Director General.

## Work authorization
- France = primary country; the role keeps the French residency clock running.
- Salary clears the Passeport Talent threshold (see above). Ask whether they've hired on a titre de séjour before (small firm; they may need guidance on the procedure).

## CV Tailoring Instructions (for Claude Code)
Variant: A (Financial Data Infrastructure), AI-agents + data-quality + credit-forward. ENGLISH CV (the JD is in English).
Branch: `variant-b-general` (edit `resume_base.tex`). Follow `CLAUDE.md`: comment-don't-delete, one page, no geometry/font changes, don't commit.
1. Summary: comment out the active summary, add a `% Hellebore Capital AI Ops Engineer (Paris) -- agents + data quality + credit; CFA kept:` label, then set as the active text:
   "Data engineer who automates data-quality work and supervises what it produces: an LLM agent that answers questions only through validated metrics, a data-quality framework resolving identity mismatches, duplicates and code inconsistencies across three private-capital sources at BNP Paribas, and daily work directing coding agents (Claude Code). \textbf{CFA Charterholder} with credit-analysis experience (UOB)."
   Must not exceed the current summary's line count. If it wraps, drop "(Claude Code)", then "duplicates and".
2. Optional add: UOB (credit analysis, ~SGD 500m corporate portfolio) if it fits on one page. It directly supports "curiosity for bonds, CDS and credit".
3. Programming line: "Python, Git, coding agents (Claude Code), LLM APIs (Anthropic, Gemini)" if it fits.
4. Rebuild with tectonic, confirm one page, export: `cp build/resume_base.pdf output/cv_kris_huang_hellebore_ai_ops_engineer.pdf`. Attach under a neutral filename.
Fallback (no build): the Booking Holdings treasury PDF (finance-forward, English).

## Application note (draft)
See chat. Grounded in BNP data-quality framework + French deals monitoring automation.

## Cover Letter Angle
Their operating model is "agents propose, a human decides, and the human's job is to shrink their own review queue". That is exactly the loop you built at BNP. The hard part of manually maintained private-capital data was identity: the same client or fund under different names and codes across three sources. You built checks that surfaced those failures, then fixed the rules upstream instead of patching rows. In pc_pipeline the LLM agent is never trusted blindly: every query passes a validation gate. As a CFA with credit-analysis experience, you can read a dealer quote and tell when a price/yield pair doesn't make sense, which means fewer escalations from day one.

## Preparation Gaps
- Bond/CDS quote conventions: clean vs dirty price, yield-to-maturity/worst, spread quoting, CDS running spread vs upfront, recovery assumptions. Why a price/yield mismatch flags a wrong security or a wrong settlement date.
- Reference data: FIGI (OpenFIGI API), ISIN, FIRDS (ESMA MiFID II reference data), SEC EDGAR filings, prospectus fields (coupon, maturity, call schedule, seniority).
- Email quote extraction: typical dealer run formats, LLM structured-output extraction, confidence thresholds, human-in-the-loop routing.
- Review-rate KPI: precision/recall of auto-approval, thresholds vs data quality, versioning prompts/rules (Git, eval sets, regression tests on past exceptions).
- Quant path: backtesting data pitfalls (survivorship, look-ahead, point-in-time reference data).

## Stack Analysis

### Have
- Python; directing coding agents and reading/fixing their output
- LLM agent with a validation gate (pc_pipeline); LLM-as-judge evaluation (LVMH)
- Data-quality framework, identity resolution across sources (BNP)
- Credit/finance domain: CFA, UOB credit analysis, Guosen product monitoring
- Master's (ESSEC–CentraleSupélec) + engineering undergrad (UCLA EE)

### Missing
- Production monitoring of daily pipelines
- Hands-on bond/CDS quote handling; FIGI/FIRDS/EDGAR tooling

### Partial
- Prompt/rule versioning and evaluation (LVMH eval framework, Git discipline)

### Green Flags
- Explicitly open to recent graduates; finance taught in-house (you're overqualified on domain)
- Clear operating model and a measurable KPI
- Reports to the DG: visibility; path into quant workflows
- Paris + salary above the Passeport Talent threshold

### Red Flags
- Not an AE/DE role: supervision/ops, no dbt/warehouse/modelling. Risk of widening the modern-stack gap.
- Proprietary platform (OtcStreaming): lower skill portability
- Small investment firm: stability, and little engineering mentorship on the data-stack side
- Investment firm (skill says avoid traditional FIs; this is a small AI-native boutique, so acceptable)

## Notes
- Verdict: APPLY. High odds and a strong France/visa backstop. Weigh it against AE offers if one comes; the quant extension and the €48k in Paris make it a respectable landing spot.

## Raw JD
AI Ops Engineer, Reference & Market Data. Paris (up to 20% remote). Full-time. €48k. Reports to the Director General.
Hellebore Capital is a Paris-based credit investment firm. Data operations are AI-managed: agents extract bond and CDS quotes from dealer emails, identify securities, create reference data (FIGI, FIRDS, EDGAR, prospectuses) and run quality checks. Investment decisions stay with PMs.
Do: run/monitor daily AI pipelines on private OtcStreaming instance; review agent proposals (they propose, you decide); investigate exceptions (unresolved securities, suspect quotes, price/yield mismatches); fix the cause by adjusting prompts, rules, thresholds, settings (versioned); KPI: fewer human reviews over time at equal or better quality. Later: quant trading (backtesting datasets, live model inputs, automating quant workflows).
Bring: Bac+5 from engineering school or quantitative programme, recent grads welcome; Python and AI tools (prompts, coding agents, read and fix output); curiosity for bonds/CDS/credit, finance taught in-house; fast and sound.
Apply: short note on an automation or data-quality process you have owned end-to-end.
