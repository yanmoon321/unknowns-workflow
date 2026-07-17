# Artifact contracts

Use a durable artifact only when the work spans turns, people, or implementation stages. Keep it task-local and remove sensitive values.

## Discovery brief

Required sections:

1. Goal and non-goals.
2. Evidence inspected and evidence still missing.
3. Unknown unknowns, unknown knowns, and known unknowns.
4. Priority, consequence, and recommended action for every high-impact item.
5. Explicit assumptions and decisions.
6. A revised task brief or next-step plan.

## Implementation notes

Record only material deviations. For each entry include:

- timestamp or milestone;
- planned approach;
- discovered fact and evidence;
- conservative decision taken;
- affected behavior, files, tests, and follow-up.

## Merge review

Required sections:

1. Outcome and demo or observable behavior.
2. Scope and non-scope.
3. Key behavior paths and evidence.
4. Decisions, deviations, risks, rollback, and remaining unknowns.
5. Verification actually performed and not performed.
6. A 3–7 question comprehension quiz focused on causality, edge cases, and operational consequences. Give explanations after answers; never present it as a substitute for code review or tests.

## Source note

This skill operationalizes the workflow described in Thariq Shihipar's “A Field Guide to Fable: Finding Your Unknowns”: https://x.com/trq212/article/2073100352921215386. The guidance here is an original, condensed workflow and does not reproduce the article or its example artifacts.
