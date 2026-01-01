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
