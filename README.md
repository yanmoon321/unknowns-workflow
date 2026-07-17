# Unknowns Workflow

A single agent skill for turning hidden assumptions, constraints, and risks into explicit decisions before they become expensive rework.

The skill routes itself to the smallest useful stage:

- **Before implementation:** blindspot pass, exploration, interview, reference analysis, or a change-sensitive plan.
- **During implementation:** evidence-backed decision logging when reality changes the plan.
- **Before review or merge:** an outcome-focused explainer, verification boundary, and comprehension quiz.
- **For simple work:** no workflow ceremony when the change is reversible, well specified, and supported by local evidence.

## Use

Invoke the skill with a task and let it choose the appropriate stage:

```text
Use $unknowns-workflow to identify the right next stage for this task.
```

For a safer first pass, say:

```text
Use $unknowns-workflow. Find blind spots first; do not change code yet.
```

## Included resources

- `references/routing-and-stop-rules.md` defines stage selection and when to stop for a user decision.
- `references/beginner-guardrails.md` provides plain-language request patterns and red flags.
- `references/question-prioritization.md` ranks unknowns by consequence.
- `references/artifact-contracts.md` defines durable discovery, implementation, and review artifacts.
- `scripts/create_artifact.py` creates non-overwriting Markdown shells for those artifacts.

## Attribution

This project is an original operationalization inspired by Thariq Shihipar's “A Field Guide to Fable: Finding Your Unknowns.”

Original post: https://x.com/trq212/article/2073100352921215386

The project does not reproduce the original post or its example artifacts.
