# Reverse Engineering Analysis of creature_multi_CM_D.py

[cite_start]This document provides a formal mathematical and architectural breakdown of the simulation implemented in `creature_multi_CM_D.py`[cite: 1, 2]. [cite_start]The system models an autonomous agent whose behavioral complexity emerges from the decoupling of macroscopic environmental states and microscopic cortical selection loops[cite: 3].

---

## Level 1: The Outer Loop (Macroscopic Environment & Homeostatic Dynamics)

[cite_start]At the macroscopic scale, the simulation is governed by the `update(frame)` loop within `FuncAnimation`[cite: 5]. [cite_start]The system behaves as a **classical field physics environment**, where the creature is a point mass parameterized by its position $\vec{p}(t) = (x, y)$ within a bounded Euclidean space $[-0.95, 0.95]^2$[cite: 6].

[cite_start]The environment projects three dynamic vector fields representing external entities: Food ($\vec{f}$), Home/Cave ($\vec{h}$), and Predator ($\vec{d}$)[cite: 7]. [cite_start]The Euclidean distances to these coordinates modulate the inner homeostatic variables of the creature[cite: 8]:

* [cite_start]**Hunger:** Accumulates linearly over time ($+0.0028 \cdot \Delta t$) and resets to $0$ upon a collision event with food[cite: 9].
* [cite_start]**Safety Need:** Accumulates linearly ($+0.0042 \cdot \Delta t$) while outside the cave radius ($d \geq 0.25$) and collapses to $0$ when inside[cite: 10].
* [cite_start]**Border Stress:** A localized quadratic penalty triggered exclusively by proximity to the rectangular geometric boundaries[cite: 11].

### Equation 1: Operational Homeostatic Dynamics
[cite_start]For a homeostatic state vector $\vec{H}(t) = [\text{hunger}(t), \text{safety}(t), \text{border\_stress}(t)]^T$, the macroscopic transition is formalized as[cite: 13]:

$$\vec{H}(t + \Delta t) = \text{clip} \left( \vec{H}(t) + \Delta t \cdot \begin{bmatrix} \alpha_h \\ \alpha_s \cdot \mathbb{I}_{(\|\vec{p} - \vec{h}\|| \geq 0.25)} \\ 0 \end{bmatrix} - \begin{bmatrix} \text{Reward}_{\text{food}} \\ \text{Reward}_{\text{home}} \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ \left( \frac{\max(0, \, 0.25 - d_{\text{wall}})}{0.25} \right)^2 \end{bmatrix}, \, 0, \, 1 \right)$$

[cite_start]*Where $\mathbb{I}$ is the indicator function of the creature's spatial position, and $d_{\text{wall}}$ is the minimum distance to the outer boundaries[cite: 15].*

---

## Level 2: Intermediate Selection Loops (Local N-Flop Competition)

[cite_start]Descending into the cortical layer, the architecture instantiates two discrete operational areas: the **Motivational Cortex** (`cms_mot`) and the **Basal Navigation Cortex** (`cms_nav`)[cite: 17]. [cite_start]Each area contains $N = 25$ Cortical Microcircuits (CMs) oriented geometrically along preferred angular vectors $\theta_i$[cite: 18].

[cite_start]Sensory transduction maps continuous environmental vectors into the localized microcircuit space via cosine alignments ($\cos(\phi_{\text{stimulus}} - \theta_i)$)[cite: 19]. [cite_start]Each CM independently computes a scalar activation energy biased by heterogeneous synaptic weights initialized at runtime (`food_weight`, `home_weight`, etc.) and intrinsic stochastic noise[cite: 20].

[cite_start]The network resolves local action selection through a **pure logical switching mechanism (Winner-Take-All)** executed by `np.argmax`[cite: 21]. [cite_start]Rather than averaging vectors (which would lead to behavioral paralysis), the system forces a symmetry-breaking event, collapsing the directional uncertainty into a single winning microcircuit[cite: 22].

### Equation 2: The Active N-Flop Logistic Operator
[cite_start]For a competitive network of $N$ modules with continuous activation drives under a Gaussian stochastic perturbation $\varepsilon_i(t) \sim \mathcal{N}(0, \sigma^2)$, the selection of the unique executing circuit $k$ is defined by[cite: 24]:

$$k = \arg\max_{i \in \{1, \dots, N\}} \left( \sum_{s \in \text{Stimuli}} W_{i,s} \cdot \mathbf{S}_s \cdot \cos(\phi_s - \theta_i) + \varepsilon_i(t) \right)$$

$$\vec{A}_{\text{net}}(t) = \mathbf{E}_k = [0, \dots, 1_k, \dots, 0]^T$$

[cite_start]*Where $\mathbf{S}_s$ represents the effective homeostatic modulators derived from the hysteresis filter (e.g., `effective_hunger` or `current_safety_need`), and $\mathbf{E}_k$ is a standard basis vector indicating a discrete state activation[cite: 27].*

---

## Level 3: The Deepest Loop (Cortical Space-Time Fabric & Sparse Noise)

[cite_start]At the deepest computational layer, the simulation updates the brain matrix ($21 \times 21$), which represents the visual cortical map[cite: 29]. [cite_start]This structure tracks the agent's historical state space, mapping time into a spatial dimension[cite: 30].

* [cite_start]**Active Locomotion:** Cortical sheets undergo a multiplicative decay process (`activity * 0.92`)[cite: 31]. [cite_start]The winning microcircuit injects a unitary impulse ($+1.0$), leaving a *residual activity trail* from previous execution cycles[cite: 32].
* [cite_start]**Homeostatic Rest State:** Inside the cave (`in_cave_repose = True`), the code activates a **Sparse Noise** regime[cite: 33, 34]. [cite_start]The navigation cortex accelerates its decay rate multiplicatively ($0.70$), effectively purging historical spatial representations, while allowing $1$ or $2$ randomly sampled microcircuits to spontaneously fire[cite: 34]. [cite_start]These bursts are modulated by a slow-wave temporal sine function: $0.65 + 0.25 \sin(\text{frame} \cdot 0.2)$[cite: 35].

### Equation 3: Evolution Law of the Cortical Fabric with Latent Spontaneous Fluctuations
[cite_start]The temporal evolution of the activation state for any given microcircuit $i$ within the space-time matrix is determined by a finite difference equation coupled to the homeostatic repose flag[cite: 37]:

$$A_i(t + \Delta t) = \text{clip} \left( \gamma(H) \cdot A_i(t) + \delta_{i, k}(t) + \xi_i(t) \cdot \mathbb{I}_{(\text{repose})}, \, 0, \, 1 \right)$$

*Where:*
* [cite_start]*$\gamma(H)$ is the adaptive decay coefficient: $\gamma = 0.92$ during active navigation, contracting to $\gamma = 0.70$ for the navigational array during rest[cite: 40].*
* [cite_start]*$\delta_{i, k}(t)$ is the Kronecker delta function injecting full structural energy into the winning CM $k$ selected by the N-Flop operator[cite: 41].*
* [cite_start]*$\xi_i(t)$ represents the stochastic quantum-like burst driving spontaneous activation in isolation, occurring with an intrinsic probability $P = 0.40$ exclusively if the microcircuit belongs to the randomly selected subset $\mathcal{S}_{\text{lucky}}$[cite: 42]:*

$$\xi_i(t) = \begin{cases} 0.65 + 0.25 \sin(0.2 \cdot t) & \text{if } i \in \mathcal{S}_{\text{lucky}} \\ 0 & \text{if } i \notin \mathcal{S}_{\text{lucky}} \end{cases}$$

---

## Architectural Conclusion

[cite_start]The architecture of `creature_multi_CM_D.py` successfully demonstrates how complex, adaptive behavior emerges from simple, localized mathematical rules[cite: 45]. 

[cite_start]The **outer loop** interfaces with the continuous physical environment [cite: 46][cite_start]; the **intermediate loop** uses a Winner-Take-All N-Flop mechanism to collapse environmental uncertainty into distinct logical decisions [cite: 46][cite_start]; and the **inner loop** projects these decisions onto a spatial matrix with temporary memory (the structural trails of the brain grid)[cite: 47]. 

[cite_start]When resting, the creature accelerates its metabolic decay to clear out past navigational data, while maintaining a low-frequency, stochastic baseline fluctuation—representing a latent energy state ready to respond when it re-enters the active space-time continuum[cite: 48].