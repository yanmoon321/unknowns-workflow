# Beginner guardrails

Use this reference when the user has limited confidence directing an agent or asks the agent to decide what happens next.

## What the agent must do

1. Inspect evidence before offering a solution.
2. Name one recommended next action in plain language.
3. Separate verified facts, assumptions, and decisions needing approval.
4. Keep the first artifact short enough to review in one pass.
5. Stop before an irreversible or externally visible decision.

## Useful user requests

- "Find blind spots first; do not change code yet."
- "Inspect the existing implementation and tell me the single most important thing to confirm."
- "Give me three meaningfully different options and explain their costs."
- "Write a plan first. Stop and ask before changing data, permissions, or public behavior."
- "Log why implementation deviates from the plan and tell me what remains unverified."
- "Explain the change in plain language before merge, then quiz me on three key points."

## Red flags

Ask the user to slow down when the agent claims success without showing evidence, silently introduces a package or service, modifies many unrelated files, reports a guess as a repository fact, or says a test passed without stating the command and result.
