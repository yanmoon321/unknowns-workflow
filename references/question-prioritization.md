# Question prioritization

Use this reference when deciding what to investigate or ask first.

## Rank unknowns

Score each unknown qualitatively on impact and cost of being wrong.

1. **Critical:** credential exposure, authorization, privacy, data deletion or corruption, financial charge, legal or regulatory effect.
2. **High:** public contract, persistent schema, architecture boundary, irreversible migration, core user journey, production reliability.
3. **Medium:** performance budget, analytics semantics, design direction, maintainability, reversible behavior.
4. **Low:** wording, naming, formatting, optional polish.

Within the same tier, ask the question that most changes the next decision. Prefer evidence already present in code, tests, logs, config, contracts, or a supplied reference over speculative questions.

## Good question properties

- Answerable from the user or a named evidence source.
- Changes a concrete decision, not just general understanding.
- Narrow enough for one response.
- States the consequence of each likely answer when that helps the user decide.

## Anti-patterns

- Asking a long questionnaire before inspecting available evidence.
- Asking preference questions that do not affect the current decision.
- Treating an industry default as a project fact.
- Continuing after an unanswered question that controls security, persistence, public behavior, or cost.
