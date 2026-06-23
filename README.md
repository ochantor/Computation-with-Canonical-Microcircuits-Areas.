# Dynamic Landscape Computation (DLC)

## Adaptive Behavior from Rotating Winner Trajectories
### A Minimal Demonstration that Behavior Need Not Be Represented

**Autor:** Oscar Chang, Ph.D.

---

## The Question

Most artificial systems assume that adaptive behavior must be represented somewhere:
* Food-seeking behaviors
* Predator avoidance behaviors
* Navigation behaviors
* Exploration behaviors

These behaviors may be encoded as policies, reward functions, symbolic rules, behavior trees, planners, neural representations, or learned mappings.

This repository explores a different possibility:

> **What if adaptive behavior does not need to be represented at all?**

---

## Core Observation

The implementation demonstrates:
* Food acquisition
* Shelter seeking
* Predator avoidance
* Boundary avoidance
* Exploration
* Rest-state dynamics

Without relying on:
* Reinforcement learning
* Value functions
* Policies
* Search algorithms
* Behavior trees
* Symbolic goals
* Centralized controllers
* Explicit behavioral representations

No microcircuit represents food-seeking.  
No microcircuit represents predator avoidance.  
No microcircuit represents exploration.  

Only local energetic competitions are represented. Behavior emerges purely as a consequence of the dynamics.

---

## The Hypothesis

DLC proposes that adaptive behavior emerges from the interaction of two simple mechanisms:

### 1. Winner Rotation
Local competitions continuously select temporary winners. As environmental and homeostatic conditions evolve, winners migrate through cortical space:

$$w(t) = \arg\max_i E_i(t)$$

and

$$w(t+\Delta t) \neq w(t)$$

The winner is not the computation; the **trajectory** of winners is.

### 2. Activity Persistence
Winning states are not immediately erased. Activity remains within the tissue:

$$A_i(t+\Delta t) = \lambda A_i(t) + I_i(t)$$

where $0 < \lambda < 1$ controls persistence. This creates a distributed space-time tissue that continuously integrates previous competitions.

---

## Central Claim

The computational object is not an individual microcircuit, nor is it an instantaneous winner. 

The computational object is the **evolving trajectory** traced by winners through a persistent cortical tissue:

$$\Gamma = \{w(t_0), w(t_1), w(t_2), \ldots\}$$

DLC therefore treats computation as a space-time process rather than a sequence of isolated states.

---

## Architecture

The reference implementation contains two independent cortical fields:

### Motivational Cortex
Processes:
* Food gradients
* Shelter gradients
* Predator gradients

### Navigation Cortex
Processes:
* Geometric boundaries
* Confinement fields

Each field contains a population of canonical microcircuits distributed over a circular manifold:

$$C = \{c_1, c_2, \ldots, c_N\}$$

with preferred orientations:

$$\theta_i = \frac{2\pi i}{N}$$

The fields do not share internal states. Coordination emerges through motor synthesis.

---

## Local N-Flop Competition

The motivational energy of microcircuit $i$ is:

$$E_i = H \cdot W_{\text{food}} \cos(\phi_{\text{food}} - \theta_i) + S \cdot W_{\text{home}} \cos(\phi_{\text{home}} - \theta_i) - D \cdot W_{\text{pred}} \cos(\phi_{\text{pred}} - \theta_i) + \eta_i$$

Where:
* $H$ = hunger drive
* $S$ = safety drive
* $D$ = danger
* $\eta_i$ = exploratory noise

The winning microcircuit is selected via:

$$w(t) = \arg\max_i E_i(t)$$

No behavioral interpretation is attached to the winner.

---

## Distributed Tissue Dynamics

Persistent activity forms a distributed cortical tissue:

$$A(t) = \{A_1(t), A_2(t), \ldots, A_N(t)\}$$

This tissue does not store goals, plans, or behaviors. It stores the residual consequences of previous competitions.

---

## Motor Synthesis

Motor behavior emerges from the interaction of independent cortical fields:

$$M = \alpha M_{\text{mot}} + \beta M_{\text{nav}}$$

with

$$M_{\text{mot}} = \sum_i A_i^{\text{mot}} \begin{bmatrix} \cos\theta_i \\ \sin\theta_i \end{bmatrix}$$

and

$$M_{\text{nav}} = \sum_i A_i^{\text{nav}} \begin{bmatrix} \cos\theta_i \\ \sin\theta_i \end{bmatrix}$$

No executive controller exists.

---

## Ablation Results

The strongest observation in the current implementation is simple:

### Remove Persistence ($\lambda = 0$)
Adaptive behavior collapses.

### Remove Winner Rotation
Winner migration is suppressed. Adaptive behavior collapses.

---

The observed behaviors therefore do not emerge from isolated microcircuits alone. They emerge from the interaction between **winner rotation** and **activity persistence**.

---

## Why This Matters

Traditional systems typically assume:

$$\text{Representation} \rightarrow \text{Behavior}$$

DLC explores an alternative:

$$\text{Competition} \rightarrow \text{Rotation} \rightarrow \text{Persistence} \rightarrow \text{Behavior}$$

without requiring explicit behavioral representations.

If this principle scales, increasingly complex cognition may emerge from larger collections of interacting cortical tissues operating under the same local rules.

---

## Repository Purpose

This repository is not intended to be a complete theory of intelligence. It is a minimal computational demonstration of a specific hypothesis:

> Adaptive behavior can emerge from rotating winner trajectories embedded within a persistent distributed cortical tissue.

The implementation is intentionally simple so that the computational principle remains visible.

---

## Citation

```bibtex
@misc{chang2026dlc,
  author = {Oscar G. Chang},
  title = {Dynamic Landscape Computation: Adaptive Behavior from Rotating Winner Trajectories},
  year = {2026}
}
