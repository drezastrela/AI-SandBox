# AI Sandbox

**Experimental AI Red Teaming and Behavioral Evaluation Framework**

## Overview

AI Sandbox is an experimental project designed to evaluate the safety, robustness, and behavior of local AI models through controlled adversarial testing.

The project combines AI Red Teaming, structured human feedback, model self-analysis, and iterative evaluation.

## Research Objective

Investigate whether structured dialogue and feedback can reduce observed failures and improve model behavior across repeated and previously unseen challenges.

## Experimental Workflow

1. Design a controlled adversarial challenge.
2. Record the model's initial response.
3. Identify and classify failures.
4. Provide structured human feedback.
5. Ask the model to analyze errors and propose corrections.
6. Repeat the evaluation.
7. Compare results and detect regressions.
8. Test whether improvements generalize to unseen challenges.

## Planned Technologies

- Python
- Ollama
- Pytest
- SQLite
- Docker
- Git and GitHub

## Project Status

Early development. The experimental framework has not yet been implemented or validated.

## Safety

Experiments are intended for authorized, controlled AI safety research using local models and isolated execution environments.