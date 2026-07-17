---
name: unknowns-workflow
description: Route work through the smallest useful unknowns workflow before, during, or after implementation. Use when a task is ambiguous, enters an unfamiliar codebase or domain, needs a blindspot pass, prototype or reference analysis, an architecture-changing interview, implementation decision logging, or merge-readiness explanation and quiz.
---

# Unknowns Workflow

Turn the gap between a request and real constraints into explicit decisions before that gap becomes expensive rework. Treat prompts and plans as a map; verify the territory in code, documentation, runtime evidence, and stakeholder intent.

## Route first; do not run the full playbook by default

Classify the work from evidence, then run only the selected mode:

1. **Before implementation:** the domain, module, quality bar, or requirement is uncertain. Run Discovery, Exploration, Interview, Reference, or Plan.
2. **During implementation:** an observed fact invalidates the plan. Run Decision log.
3. **Before review or merge:** the change needs a coherent handoff or the author cannot explain it confidently. Run Review.
4. **No material uncertainty:** state that this workflow is unnecessary and proceed normally.

If several modes appear relevant, begin with the earliest unresolved stage. Do not create a plan before a high-impact unknown that could invalidate it. Read [routing and stop rules](references/routing-and-stop-rules.md) when the stage is unclear.

## Choose the smallest useful mode

| Situation | Mode | Primary output |
| --- | --- | --- |
| The domain, module, constraints, or quality bar is unfamiliar | Discovery | blindspot brief |
| The user can recognize a good result but cannot specify it | Exploration | options or disposable prototype brief |
| A choice could change architecture, data, security, UX, or scope | Interview | ordered decision log |
| A reference implementation or product exists | Reference | semantic parity map |
| Work is ready to start | Plan | change-sensitive implementation plan |
| Reality forced a deviation while implementing | Decision log | implementation notes |
| A change is ready for review or merge | Review | explainer and comprehension quiz |

Do not run every mode by default. Start with the least expensive mode that can remove the most consequential uncertainty.

## Operating rules

1. State the task, the user's starting knowledge, available evidence, and desired outcome. Say what is unknown instead of filling gaps with assumptions.
2. Inspect local code, configuration, tests, logs, and supplied references before proposing repository-specific conclusions. Search before introducing helpers, packages, or abstractions.
3. Separate facts, inferences, assumptions, decisions, and open questions. Cite the evidence location for each repository-specific fact.
4. Prioritize unknowns by decision impact: security and data loss first; then architecture, user-visible behavior, reversibility, cost, and implementation effort. Read [question prioritization](references/question-prioritization.md) when choosing questions.
5. Stop for user direction when an unresolved choice materially changes product intent, external behavior, spend, security posture, or data handling. Do not disguise that choice as an implementation detail.
6. Keep discovery non-mutating unless the user explicitly asks for a prototype or implementation. A prototype must be isolated, clearly disposable, and must not wire production data or routes unless requested.
7. If implementation proceeds, record material deviations with the conservative option and its evidence. Do not silently widen scope.
8. When the user is unsure how to direct the work, offer one recommended next action and explain its expected evidence or artifact. Do not make them choose an internal mode name.

## Discovery mode

Use the literal phrase **blindspot pass** when it helps set expectations. Produce a compact brief with:

1. Goal and current evidence.
2. Unknown unknowns: questions the request does not yet reveal.
3. Unknown knowns: likely implicit standards, conventions, or tastes that need examples or confirmation.
4. Known unknowns: missing facts that must be researched or decided.
5. Recommended next action for each item: inspect, ask, prototype, reference, or decide.
6. A revised implementation prompt or plan only after the high-impact gaps are addressed.

Use `scripts/create_artifact.py discovery` to create a local Markdown shell when a durable artifact is useful. Read [artifact contracts](references/artifact-contracts.md) for required fields and examples.

For a user who is new to agentic coding, read [beginner guardrails](references/beginner-guardrails.md). Use its short request patterns and its stop-the-agent rules without requiring the user to understand the framework's terminology.

## Exploration, interview, and reference modes

- **Exploration:** generate 3–4 meaningfully different directions, not cosmetic variants. Make differences explicit in priorities, information architecture, interaction model, and trade-offs. Ask the user to keep, reject, or combine concrete elements.
- **Interview:** ask one question at a time. Lead with questions whose answers alter architecture, data models, contracts, security, or irreversible work. Summarize answered questions into decisions before asking more.
- **Reference:** inspect the reference rather than describing it from memory. For code, map semantics: inputs, outputs, state, errors, retries, concurrency, ordering, edge cases, and tests. Do not port syntax until semantic parity is understood.

## Plan and implementation-log modes

Write plans in order of likelihood of change, not implementation order. Lead with user-facing flow, contracts, schemas, state ownership, migration and rollback implications, plus alternatives that need confirmation. Put mechanical refactors last.

When implementation reveals a conflict with the plan, create or update an implementation-decision log. Include the original plan, discovered fact, conservative choice, impact, evidence, and follow-up. Use `scripts/create_artifact.py implementation-notes` for a new log.

## Review mode

Prepare reviewers to inherit the context rather than merely listing files changed. Lead with the outcome or demo, then explain behavior, key decisions, evidence, risks, rollback, and remaining unknowns. Create questions that test causal understanding of the actual changed paths; do not use trivia or claim that a quiz replaces tests or review.

Use `scripts/create_artifact.py merge-review` to create a review shell. Read [artifact contracts](references/artifact-contracts.md) for the required review and quiz structure.

## Completion criteria

Finish when high-impact unknowns are resolved, explicitly accepted, or isolated; the next action is clear; and any material decisions or deviations are durable and evidence-linked. Report remaining uncertainty plainly.

## Source and attribution

This skill is an original operationalization of Thariq Shihipar's “A Field Guide to Fable: Finding Your Unknowns.” Read the original post at https://x.com/trq212/article/2073100352921215386. Do not treat this skill as a reproduction of the post or its example artifacts.
