# Double Q-Learning from Scratch (Model-Free Reinforcement Learning)

This repository contains a **from-scratch, modular implementation of Double Q-learning**,  
an **off-policy, model-free reinforcement learning** algorithm designed to address  
the **overestimation bias** present in standard Q-learning.

The algorithm is implemented on a **custom GridWorld environment**, without using Gym or any RL frameworks.

The focus is on **algorithmic correctness, update logic, and bias reduction**, not performance or abstractions.

---

## Why this project

Standard Q-learning suffers from a well-known issue:

- the `max` operator in the TD target
- uses the *same* value estimates for **action selection** and **action evaluation**
- leading to **systematic overestimation** of action values

Many implementations:
- hide this issue behind libraries
- do not make the bias explicit
- or treat Double Q-learning as a minor variation

This project does the opposite:
- explicitly maintains **two independent Q-tables**
- shows how action selection and evaluation are decoupled
- makes the bias reduction mechanism clear in code

The goal is to **understand why Double Q-learning exists and how it fixes Q-learning**, from first principles.

---


Problem:
- the same Q-values choose and evaluate the greedy action
- noise + max → overestimation

Double Q-learning fix:
- maintain **two estimators**: `Q₁` and `Q₂`
- one selects the action
- the other evaluates it

This breaks the positive feedback loop caused by the max operator.

---

## Algorithm (high level)

At each step:

1. Select action using ε-greedy policy over `Q₁ + Q₂`
2. Execute action → observe `(s, a, r, s')`
3. With 50% probability:
   - update `Q₁` using `argmax` from `Q₁` but value from `Q₂`
4. Otherwise:
   - update `Q₂` using `argmax` from `Q₂` but value from `Q₁`

Both tables converge toward unbiased value estimates.

---

### Key design choices

- **Two explicit Q-tables** (`Q1`, `Q2`)
- **Randomized update selection** (coin flip)
- **Policy independent of value updates**
- **No hidden abstractions**
- **Clear temporal flow**: `(s, a, r, s')`

---

## What this implementation emphasizes

- Why overestimation happens in Q-learning
- How Double Q-learning fixes it
- Correct separation of:
  - behavior policy
  - action selection
  - action evaluation
- Clean modular code suitable for extension

---

