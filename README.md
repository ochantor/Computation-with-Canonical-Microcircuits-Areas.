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

The reference implementation contains two independent cortical fields deployed in parallel:

| Field | Function |
| :--- | :--- |
| **Motivational Cortex** (`cms_mot`) | Processes food, shelter, and predator dynamic gradients |
| **Navigation Cortex** (`cms_nav`) | Processes geometric confinement and perimeter boundary continuous fields |

Both fields share the same underlying computational principle. Each contains a population of $N=25$ canonical microcircuits distributed over an isomorphic circular manifold, structurally rotated in space during deployment to map independent features of the global landscape without a centralized executive referee.

---

# Canonical Microcircuits & Non-Linear Hysteresis

A cortical field contains a population of canonical microcircuits:

$$C=\{c_1,c_2,\ldots,c_N\}$$

Each microcircuit possesses a preferred structural orientation $\theta_i = \frac{2\pi i}{N}$, local energetic weights initialized from uniform distributions ($W_i \sim \mathcal{U}$), and exploratory stochasticity.

### The Hysteresis Filter
To prevent behavioral paralysis at critical ecological boundaries, the raw homeostatic vector $\vec{H}(t) = [\text{hunger}, \text{safety}, \text{danger}]^T$ passes through an instantaneous non-linear threshold filter to yield the effective metabolic drives ($\mathbf{S}_{\text{hunger}}, \mathbf{S}_{\text{safety}}$):

$$\text{If } \|\vec{p} - \vec{h}\| < 0.25 \implies \begin{cases} \mathbf{S}_{\text{hunger}} = 0.0, \quad \mathbf{S}_{\text{safety}} = 1.0 & \text{if hunger} < 0.75 \\ \mathbf{S}_{\text{hunger}} = \text{hunger}, \quad \mathbf{S}_{\text{safety}} = 0.0 & \text{if hunger} \geq 0.75 \end{cases}$$

$$\text{If } \|\vec{p} - \vec{h}\| \geq 0.25 \implies \begin{cases} \mathbf{S}_{\text{hunger}} = \text{hunger} \cdot \text{clip}\left(\frac{1.0 - \text{safety}}{0.20}, 0, 1\right), \quad \mathbf{S}_{\text{safety}} = \text{safety} \cdot 1.8 & \text{if safety} > 0.80 \\ \mathbf{S}_{\text{hunger}} = \text{hunger} \cdot 1.5, \quad \mathbf{S}_{\text{safety}} = \text{safety} \cdot 0.3 & \text{if hunger} > 0.50 \text{ and safety} < 0.40 \\ \mathbf{S}_{\text{hunger}} = \text{hunger}, \quad \mathbf{S}_{\text{safety}} = \text{safety} & \text{otherwise} \end{cases}$$

### Local N-Flop Competition
For the motivational cortex, the internal scalar energy drive of microcircuit $i$ at time $t$ is governed by:

$$E_i(t) = \mathbf{S}_{\text{hunger}} W_{i,\text{food}} \cos(\phi_{\text{food}} - \theta_i) + \mathbf{S}_{\text{safety}} W_{i,\text{home}} \cos(\phi_{\text{home}} - \theta_i) - \text{danger} \cdot W_{i,\text{pred}} \cos(\phi_{\text{pred}} - \theta_i) + \eta_i(t)$$

The winning microcircuit is selected through an instantaneous Winner-Take-All N-Flop logistic operator that breaks local symmetry under a Gaussian perturbation $\eta_i(t) \sim \mathcal{N}(0, \sigma^2)$:

$$w(t)=\arg\max_{i \in \{1, \dots, N\}}\,E_i(t)$$

No behavioral interpretation is attached to the winner. The standard basis vector activation $\vec{A}(t) = \mathbf{E}_{w(t)}$ only defines the direction of immediate local energetic relaxation.

---

# Rotating Winners

Environmental geometry continuously changes. Homeostatic variables continuously change. Therefore:

$$E_i(t+\Delta t)\neq E_i(t) \implies w(t+\Delta t)\neq w(t)$$

The winning node migrates through cortical space. This continuous winner migration constitutes the primary computational mechanism of the architecture. Rather than storing behaviors, the system continuously regenerates them on the fly.

---

# Distributed Space-Time Tissue & Latent Repose

Winning states are not immediately erased; they leave fading structural trails. The temporal evolution of the activation state for any microcircuit $i$ within the space-time fabric is bound to a finite difference equation coupled to the homeostatic repose state:

$$A_i(t + \Delta t) = \text{clip} \left( \lambda \cdot A_i(t) + I_i(t) + \xi_i(t) \cdot \mathbb{I}_{(\text{repose})}, \, 0, \, 1 \right)$$

Where $I_i(t) = 1$ if $i=w(t)$ (and $0$ otherwise).

### The Sparse Noise Phase Transition
When the agent enters the safe boundary of the cave and fulfills the rest criteria ($\mathbb{I}_{(\text{repose})} = 1$), a crucial phase transition occurs:
1. The navigation field accelerates its metabolic decay rate to $\lambda = 0.70$, effectively purging historical spatial footprints.
2. The network uncouples from deterministic inputs and enters a **Sparse Noise** regime. Spontaneous, slow-wave fluctuations fire with an intrinsic probability $P=0.40$ over a randomly sampled subset of microcircuits $\mathcal{S}_{\text{lucky}}$:

$$\xi_i(t) = \begin{cases} 0.65 + 0.25 \sin(0.2 \cdot t) & \text{if } i \in \mathcal{S}_{\text{lucky}} \\ 0 & \text{if } i \notin \mathcal{S}_{\text{lucky}} \end{cases}$$

This low-frequency background burning ensures the cortical fabric preserves a latent energy baseline—keeping the tissue responsive—without storing historical data during repose.

---

# Cortical Coupling & Motor Synthesis

The two cortical fields operate independently without knowing each other's internal states. Motor output stabilizes as an emergent relaxation along the negative gradient of the combined potential energy landscape:

$$\mathbf{M} = \alpha\mathbf{M}_{\text{mot}} + \beta\mathbf{M}_{\text{nav}}$$

$$\mathbf{M}_{\text{mot}} = \sum_{i=1}^N A_i^{\text{mot}}(t) \begin{bmatrix} \cos\theta_i \\ \sin\theta_i \end{bmatrix}, \quad \mathbf{M}_{\text{nav}} = \sum_{i=1}^N A_i^{\text{nav}}(t) \begin{bmatrix} \cos\theta_i \\ \sin\theta_i \end{bmatrix}$$

The displacement updates the physical coordinates via:

$$\vec{p}(t + \Delta t) = \vec{p}(t) + \left[ (0.03 + 0.03 \cdot \|\mathbf{M}\|) \cdot \frac{\mathbf{M}}{\|\mathbf{M}\|} \right] \cdot \mathbb{I}_{(\text{active})}$$

---

# Emergent Behaviors

The reference implementation demonstrates:
* Food acquisition
* Shelter seeking
* Predator avoidance
* Boundary avoidance
* Exploration
* Rest-state dynamics

Without reinforcement learning, behavior trees, symbolic reasoning, search algorithms, stored goals, behavioral modules, or central controllers. The observed behaviors arise entirely from local competition, geometry rotation, and activity persistence.

---

# Why This Matters

Most artificial systems explicitly encode behaviors. This architecture does not. The implementation suggests that coherent adaptive behavior may emerge from:

1. Local competition (N-Flop operators)
2. Energy dissipation (Metabolic cost)
3. Activity persistence (Space-time tissue)
4. Rotating cortical dynamics

Without requiring explicit behavioral representations. If correct, increasingly complex cognition may emerge from larger collections of interacting cortical fields operating under the same modular geometric principles.

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
