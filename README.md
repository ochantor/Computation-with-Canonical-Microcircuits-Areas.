# Emergent Autonomy via Rotating Canonical Microcircuits and Distributed Space-Time Tissue

**Author:** Dr. Oscar G. Chang
**Core Architecture:** Dynamic Landscape Computation (DLC)
**Reference Implementation:** `creature_multi_CM_D.py`
**License:** GNU General Public License v3 (GPLv3)

---

## Abstract

This repository presents a minimal neuromorphic architecture in which adaptive behavior emerges without planners, symbolic rules, reinforcement learning, behavior trees, or explicit behavioral representations.

The system consists of two independent cortical fields composed of competing canonical microcircuits. Each field continuously dissipates energy through local Winner-Take-All competition while interacting with environmental and homeostatic gradients.

No microcircuit encodes food seeking, shelter seeking, predator avoidance, exploration, or resting behavior.

Instead, these behaviors emerge from the continuous rotation of competitive winners through cortical space and from the persistence of activity traces forming a distributed space-time tissue.

The central claim is simple:

> Intelligence may emerge from rotating local competitions without requiring explicit behavioral programs.

---

# Core Claim

The architecture makes a stronger claim than classical behavior-based systems:

> Behaviors are never represented.

Food seeking is not represented.

Predator avoidance is not represented.

Returning home is not represented.

Exploration is not represented.

Resting is not represented.

Only local competitions between canonical microcircuits are represented.

Behavior appears as a macroscopic consequence of distributed cortical dynamics.

---

# Architecture

The reference implementation contains two independent cortical fields:

| Field               | Function                                               |
| ------------------- | ------------------------------------------------------ |
| Motivational Cortex | Processes food, shelter, and predator gradients        |
| Navigation Cortex   | Processes geometric confinement and boundary gradients |

Both fields share the same underlying computational principle.

Each contains a population of canonical microcircuits distributed over a circular manifold.

---

# Canonical Microcircuits

A cortical field contains

```math
C=\{c_1,c_2,\ldots,c_N\}
```

canonical microcircuits.

Each microcircuit possesses:

* A preferred orientation
* Local energetic weights
* Exploratory stochasticity

For the motivational cortex, the energy of microcircuit `i` is

```math
E_i=
H\,W_i^{food}\cos(\theta_f-\phi_i)
+
S\,W_i^{home}\cos(\theta_h-\phi_i)
-
D\,W_i^{pred}\cos(\theta_p-\phi_i)
+\eta_i
```

where:

| Variable | Meaning            |
| -------- | ------------------ |
| H        | Hunger             |
| S        | Safety demand      |
| D        | Danger             |
| θf       | Food direction     |
| θh       | Shelter direction  |
| θp       | Predator direction |
| η        | Exploratory noise  |

The winning microcircuit is selected through local N-Flop competition:

```math
w(t)=\mathrm{argmax}_i\,E_i(t)
```

No behavioral interpretation is attached to the winner.

The winner only defines the direction of local energetic relaxation.

---

# Rotating Winners

Environmental geometry continuously changes.

Homeostatic variables continuously change.

Therefore:

```math
E_i(t+\Delta t)\neq E_i(t)
```

which implies

```math
w(t+\Delta t)\neq w(t)
```

The winner migrates through cortical space.

This continuous winner migration constitutes the primary computational mechanism of the architecture.

Rather than storing behaviors, the system continuously regenerates them.

---

# Distributed Space-Time Tissue

Winning states are not immediately erased.

Activity evolves according to

```math
A_i(t+1)=\lambda A_i(t)+I_i(t)
```

where

```math
0<\lambda<1
```

and

```math
I_i(t)=
\begin{cases}
1 & \text{if } i=w(t) \\
0 & \text{otherwise}
\end{cases}
```

The resulting activity traces create a distributed space-time tissue.

This tissue preserves recent competitive history without symbolic memory, stored goals, or planning structures.

---

# Cortical Coupling

The two cortical fields operate independently.

Motor output emerges from their interaction:

```math
\mathbf{M}
=
\alpha\mathbf{M}_{mot}
+
\beta\mathbf{M}_{nav}
```

where

```math
\mathbf{M}_{mot}
=
\sum_i A_i^{mot}
\begin{bmatrix}
\cos\phi_i\\
\sin\phi_i
\end{bmatrix}
```

and

```math
\mathbf{M}_{nav}
=
\sum_i A_i^{nav}
\begin{bmatrix}
\cos\phi_i\\
\sin\phi_i
\end{bmatrix}
```

Neither cortical field possesses knowledge of the other's internal state.

Behavior emerges from the interaction of independently dissipating energy landscapes.

---

# Emergent Behaviors

The reference implementation demonstrates:

* Food acquisition
* Shelter seeking
* Predator avoidance
* Boundary avoidance
* Exploration
* Rest-state dynamics

without:

* Reinforcement learning
* Behavior trees
* Symbolic reasoning
* Search algorithms
* Stored goals
* Behavioral modules
* Central controllers

The observed behaviors arise entirely from local competition and activity persistence.

---

# Why This Matters

Most artificial systems explicitly encode behaviors.

This architecture does not.

The implementation suggests that coherent adaptive behavior may emerge from:

1. Local competition
2. Energy dissipation
3. Activity persistence
4. Rotating cortical dynamics

without requiring explicit behavioral representations.

If correct, increasingly complex cognition may emerge from larger collections of interacting cortical fields operating under the same principles.

---

# Repository Purpose

This repository is intended as a minimal computational demonstration of a simple hypothesis:

> Complex adaptive behavior can emerge from rotating canonical microcircuits whose activity persists within a distributed space-time tissue.

The implementation intentionally minimizes assumptions in order to expose the underlying computational principle as clearly as possible.

---

# Citation

```bibtex
@misc{chang2026dlc,
  author = {Oscar G. Chang},
  title = {Emergent Autonomy via Rotating Canonical Microcircuits and Distributed Space-Time Tissue},
  year = {2026},
  note = {Dynamic Landscape Computation (DLC)}
}
```

