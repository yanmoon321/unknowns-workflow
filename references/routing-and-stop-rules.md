# Routing and stop rules

## Select a mode from task evidence

| Evidence in the request or repository | Mode | First output |
| --- | --- | --- |
| A module, domain, requirement, or quality bar is unfamiliar | Discovery | prioritized blindspot brief |
| The user can react to examples but cannot describe the target | Exploration | 3–4 materially distinct options or a disposable prototype |
| An answer could alter architecture, data, security, UX, or scope | Interview | one-question-at-a-time decision record |
| Source code, a product, or a design is named as the target | Reference | semantic parity map before implementation |
| The work is understood but choices may still change implementation | Plan | decisions first, mechanical steps last |
| A real fact conflicts with the plan | Decision log | evidence-backed deviation entry |
| The change is ready for handoff, review, or merge | Review | explainer, verification boundary, quiz |

## Stop and ask the user

Pause instead of guessing when the unresolved answer changes any of these:

- product behavior, target user, copy, or acceptance criteria;
- credentials, privacy, authorization, money, legal obligations, or data retention;
- public interfaces, persistent data, migrations, irreversible operations, or rollback strategy;
- new paid services, dependencies, or external coordination.

Present the decision, available evidence, likely consequences, and your recommended option. Do not bury it in a long list of questions.

## Keep it lightweight

For reversible, well-specified edits with local evidence, skip artifacts and proceed. For a broad task, create only the earliest artifact that changes the next decision.
