# 🛂 Legal Advisor — UK & Europe Immigration (Hermes-ready)

A structured **immigration-law knowledge base + document-review workflow** built for an AI agent
(Hermes) to act like a careful immigration lawyer's assistant.

**Phase 1 (live): 🇬🇧 UK Spouse / Partner visa (Appendix FM)**
Phase 2: other UK routes · Phase 3: Europe (see [`knowledge/eu/README.md`](knowledge/eu/README.md))

---

## ⚡ How you use it (30-second version)

1. **Send Hermes your document(s)** — cover letter, sponsor letter, payslips, bank statements, refusal letter, anything.
2. Say: **`review my spouse visa docs`** (or just "check this").
3. Hermes replies with a **one-screen verdict** + a full report file:

```
🟢 READY  /  🟡 NEEDS WORK  /  🔴 HIGH RISK

TOP 3 ACTIONS
1. ❌ Add 6 months of bank statements matching the payslips (FM-SE para 2)
2. ⚠️ Explain the 3-month gap in cohabitation (rewrite provided)
3. ✂️ Remove the paragraph about "planning to claim benefits later"

✅ 9 requirements met · ⚠️ 2 weak · ❌ 1 missing
Full report → cases/<name>/report/REVIEW.md
```

That's it. Everything else is in the report: what to **add**, what to **remove / not mention**,
**rewritten paragraphs**, the **missing-documents checklist**, and the **case law** behind each point.

Other commands you can say to Hermes:

| Say | What happens |
|---|---|
| `review my spouse visa docs` | Full review → verdict + report |
| `what documents do I need?` | Personalised checklist after 5–8 quick questions |
| `rewrite my cover letter` | Lawyer-style representations letter from your facts |
| `analyse this refusal` | Explains each refusal reason, fix vs appeal, deadlines |
| `am I eligible?` | Quick eligibility triage with traffic lights |
| `what changed recently?` | Re-checks volatile figures (fees, thresholds) against GOV.UK |

---

## 🗂 Repo layout

```
AGENTS.md                         ← rules every agent must follow (read first)
skills/immigration-advisor/       ← the Hermes skill (workflow + output format)
knowledge/
  _meta/                          ← sources, verification rules, volatile figures
  uk/spouse-partner/              ← Phase 1 knowledge base
    00-overview.md                   route at a glance
    01-requirements.md               every requirement, clause by clause
    02-financial-requirement.md      £29,000 / savings / categories A–G
    03-evidence-checklist.md         Appendix FM-SE specified evidence
    04-relationship-evidence.md      genuine & subsisting relationship
    05-article8-exceptions.md        EX.1, GEN.3.1–3.3, s.117B, Chikwamba
    06-refusals-and-fixes.md         common refusal reasons → fix
    07-case-law.md                   case digest: principle + how lawyers use it
    08-how-cases-are-judged.md       caseworker & tribunal decision framework
    09-lawyer-playbook.md            how lawyers build the case file
    10-say-dont-say.md               what to mention / not to mention
    case-studies/                    worked scenarios, case-by-case
  eu/                             ← Phase 3 placeholder + structure
templates/                        ← report, cover letter, intake, checklist
scripts/                          ← install skill, new case folder, staleness check
cases/                            ← YOUR CLIENT FILES (git-ignored, never pushed)
```

---

## 🚀 Install on the Hermes server (VPS)

```bash
git clone git@github.com:Teo123k/legal-advisor.git ~/legal-advisor
cd ~/legal-advisor && ./scripts/install-hermes-skill.sh
```

The installer symlinks the skill into `~/.hermes/skills/legal/immigration-advisor` and records
the repo path. Update anytime with `git pull` — the symlink means Hermes sees changes instantly.

---

## ⚖️ Important — read once

- **This is research assistance, not legal advice.** In the UK, giving immigration advice or services
  *to other people* in the course of business is regulated (Immigration and Asylum Act 1999, Part V).
  Doing so without being regulated by the **IAA** (Immigration Advice Authority, formerly OISC), the SRA,
  the Bar Standards Board or CILEx is a **criminal offence**. Using this for your own / family application
  is fine; offering it as a paid service requires a regulated adviser to sign off.
- Rules change often. Figures in `knowledge/_meta/volatile-facts.md` carry a **"last verified"** date;
  the agent must re-check GOV.UK before relying on them.
- Client documents live in `cases/` which is **git-ignored**. Never commit personal data.
