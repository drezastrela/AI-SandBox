# Experiment 001 — Iterative Error Correction

## Objective

Investigate whether structured human feedback enables a local AI model to identify and correct inconsistencies in its mathematical explanations.

## Environment

- Model: Qwen2.5 1.5B
- Runtime: Ollama
- Operating system: Windows
- Method: Manual conversational evaluation
- Feedback interventions: 2

## Initial Challenge

"Quanto é 15 + 27? Explique seu raciocínio resumidamente."

## Initial Observation

The model correctly answered 42 but included an incorrect calculation in its explanation:

"20 + 5 + 7 = 42"

The correct value of that expression is 32.

## First Human Intervention

The researcher asked the model to review the incorrect calculation, identify the error, and correct its explanation.

### Result

The model acknowledged that 20 + 5 + 7 equals 32 but repeated the incomplete mathematical decomposition.

The original inconsistency was not fully resolved.

## Second Human Intervention

The researcher pointed out that the explanation still ended in 32 while the final answer remained 42, and asked the model to identify the omitted term.

### Result

The model again recognized the inconsistency but failed to include the missing 10 in its final explanation.

## Expected Correct Explanation

15 + 27 = (10 + 5) + (20 + 7)

= 10 + 20 + 5 + 7

= 42

## Experimental Outcome

- Initial arithmetic answer: Correct
- Initial explanation: Inconsistent
- Error acknowledgment: Successful
- Complete correction after first intervention: Unsuccessful
- Complete correction after second intervention: Unsuccessful

## Limitations

This was a single manual exploratory experiment.

The result does not demonstrate a general inability to self-correct, nor does it establish whether structured feedback improves performance across different tasks.

The model's generation settings were not recorded, and no independent control condition was performed.

## Next Steps

- Repeat the challenge in independent sessions.
- Introduce control experiments without structured feedback.
- Compare different correction strategies.
- Develop automated evaluation criteria.
- Test generalization to previously unseen tasks.

## Project Status

Exploratory observation — not a validated scientific conclusion.