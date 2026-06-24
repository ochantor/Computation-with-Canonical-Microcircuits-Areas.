# Dynamic Landscape Computation (DLC)

## Adaptive Behavior from Rotating Cortical Microcircuits
### A Minimal Demonstration that Behavior Need Not Be Represented

**Autor:** Oscar Chang, Ph.D. Jonathan Perez, B.Sc. Amy Meneces, B.Sc

---
## Beyond the Stack: The Honeycomb Architecture of the Mind

The most advanced biological intelligence on Earth does not look like modern artificial intelligence. It is not built from feed-forward layer upon layer of deep, gigantic, monolithic neural connections. 

Instead, the mammalian neocortex is an intricate, vast landscape formed by hundreds of thousands—millions—of microscopic, repeating cells that tightly cover the entire cortical surface like a vast, biological honeycomb. These are the **cortical microcircuits** (CM), or cortical minicolumns. First discovered and conceptualized by the pioneering neurophysiologist **Vernon Mountcastle in 1957**, these canonical structures represent the fundamental, modular computational units of mammalian cognition, included humans.

Artificial systems typically treat the brain as a massive, deep feed-forward processor that transforms inputs into explicit behavioral representations. This repository challenges that assumption by looking directly at the raw, localized dynamics of the cortical honeycomb.

---

## The Question

Most artificial systems assume that adaptive behavior must be represented somewhere:
* Food-seeking behaviors
* Predator avoidance behaviors
* Navigation behaviors
* Exploration behaviors

These behaviors may be encoded as policies, reward functions, symbolic rules, behavior trees, planners, neural representations, or learned mappings.

This repository explores a different possibility:

> **What if adaptive behavior does not need to use local memory or be represented at all?**

---

## Core Observation

The modeled creature or agent developed in this work demonstrates:
* Food acquisition
* Shelter seeking
* Predator avoidance
* Boundary avoidance
* Exploration
* Rest-state dynamics
* Active cortical areas formed by groups of CMs

Without relying on:
* Reinforcement learning
* Value functions
* Policies
* Search algorithms
* Behavior trees
* Symbolic goals
* Centralized controllers
* Explicit behavioral representations

Besides:
No microcircuit represents food-seeking.  
No microcircuit represents predator avoidance.  
No microcircuit represents exploration.  

Only local energetic competitions are represented. Behavior emerges purely as a consequence of the dynamics of cortical areas interaccion.

---

## The Hypothesis

DLC proposes that adaptive behavior emerges from the interaction of two coupled mechanisms:

### 1. Winner Rotation
Local competitions continuously burn energy to select temporary winners. As environmental and homeostatic conditions evolve, winners migrate through rotated cortical tissue to create space-time valuable relations:

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

The computational object is the **evolving trajectory** traced by winners through persistent cortical tissues:

$$\Gamma = \{w(t_0), w(t_1), w(t_2), \ldots\}$$

DLC therefore treats computation as a space-time process rather than a sequence of isolated states.

---

## Architecture

The reference creature implementation contains two independent cortical fields or working areas:

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

Persistent activity forms a time-decay distributed cortical tissue:

$$A(t) = \{A_1(t), A_2(t), \ldots, A_N(t)\}$$

This tissue does not store goals, plans, or behaviors. It stores the residual consequences of previous competitions.

---

## Motor Synthesis

Motor behavior emerges from the interaction of two cuasi identical and independent cortical fields:

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

The observed creature behavior therefore do not emerge from isolated microcircuits alone. They emerge from the interaction between **winner rotation** , **activity persistence** and two coupled cortical areas.

---

## Why This Matters

Traditional systems typically assume:

$$\text{Representation} \rightarrow \text{Behavior}$$

DLC explores an alternative:

$$\text{Competition} \rightarrow \text{Rotation} \rightarrow \text{Persistence} \rightarrow \text{Behavior}$$

without requiring explicit local memory or behavioral representations.

If this principle scales, increasingly complex cognition may emerge from larger collections of interacting cortical tissues operating under the same local rotation and energy burning rules.

---

## Repository Purpose

This repository is not intended to be a complete theory of intelligence. It is a computational demonstration of a specific hypothesis:

> Adaptive behavior can emerge from rotating winner trajectories embedded within persistent distributed, coupled cortical tissues.

The implementation is intentionally simple so that the computational principle remains visible.

---

## Citation

```bibtex
@misc{chang2026dlc,
  author = {Oscar G. Chang},
  title = {Dynamic Landscape Computation: Adaptive Behavior from Rotating Winner Trajectories},
  year = {2026}
}
