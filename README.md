# Dynamic Landscape Computation: Emergent Autonomy from Coupled Cortical Fields

**Author:** Dr. Oscar G. Chang  
*Research Professor & Electronic Engineer* **ORCID:** [0000-0002-4336-7545](https://orcid.org/0000-0002-4336-7545)  
**Academic Affiliation:** Yachay Tech University  
**Degree:** PhD in Electrical Engineering (Pennsylvania State University)

---

## Technical Draft: Thermodynamics of Logical Selection in Energy-Constrained Cortical Microcircuits (Paper 1)

### 1. Introduction & The Core Hypothesis
Current mainstream artificial intelligence paradigms rely heavily on history-dependent synaptic plasticity and massive data-driven training. This framework proposes an alternative neuromorphic paradigm: **Dynamic Landscape Computation**. 

We demonstrate that complex, adaptive, and life-sustaining behaviors emerge from "Frame Zero" without any training iterations or local memory updates. The model replaces traditional synaptic weight-based arbitration with a strict **logical decision function** executed by coupled cortical fields.

### 2. Mathematical Formalization of the N-Flop / One-Winner Mechanism
The agent's brain simulates two independent cortical areas: a **Motivational Field** and a **Navigational Field**, each modeled as a closed ring of $N=25$ canonical microcircuits.

#### 2.1. Excitatory Activation & Symmetry Breaking
The competition within a group of redundant microcircuits is driven by an external excitatory K-ramp wave ($K(t)$). The internal state of a sigmoidal switching neuron $u_i$ within the $i$-th microcircuit responds to mutual inhibition according to:

$$\tau \frac{du_i}{dt} = -u_i + \sigma\left( K(t) - \gamma \sum_{j \neq i}^N w_{ji} v_j + I_i^{\text{sensory}} \right)$$

Where:
* $\sigma(x) = \frac{1}{1 + e^{-x}}$ is the sigmoidal activation function representing the logical switch.
* $\gamma$ is the negative feedback gain (mutual inhibition).
* $I_i^{\text{sensory}}$ is the immediate, non-historical sensory input vector.

The selection is history-independent. When $K(t)$ crosses a critical threshold, a rapid **symmetry breaking** occurs. The circuit that happens to have the infinitesimal energetic advantage silences all competitors, ensuring that only a single microcircuit emerges as the instantaneous winner:

$$v_i(t) = \delta_{i, \text{winner}}$$

### 3. Residual Exponential Activity Trails (The Functional Tissue)
The instantaneous winner $v_i(t)$ immediately discharges glutamate. However, the true macroscopic computational state of the cortical field is not the single active winner, but an emergent, higher-order organizational tissue ($N+1$) woven by **exponential decay trails**.

When a microcircuit wins, it leaves a persistent metabolic stencil. The activation trail $a_i$ of the $i$-th microcircuit updates at each discrete time frame according to:

$$a_i(t) = \lambda a_i(t-1) + v_i(t)$$

Where:
* $\lambda \in (0, 1)$ is the exponential decay constant.

As the creature rotates and navigates, the physical migration of winners across the circular microcircuit network weaves a continuous spatiotemporal field of activity.

### 4. Energetics: "Dark Energy Burning" & Thermodynamic Cost
The logical competition within the N-Flop architecture carries an intrinsic thermodynamic expense, modeled as **Dark Energy Burning**. The metabolic cost ($E_{\text{diss}}$) dissipated during the rapid symmetry-breaking phase is a function of the mutual inhibition conflict:

$$E_{\text{diss}} = \alpha \sum_{i=1}^N \sum_{j \neq i}^N v_i v_j + \beta \int \left( \frac{du_i}{dt} \right)^2 dt$$

#### 4.1. Cellular Roles & Reset Phase
* **Neurons (Sigmoidal):** Execute the immediate logical switching and local glutamate/GABA discharge.
* **Astrocytes:** Govern the metabolic management. They execute the "dark energy burning" process by clearing excess neurotransmitters from the synaptic cleft, resetting the system for the next computational frame.

### 5. Macroscopic Gradient Relaxation
The combined persistent activity trails of both fields mathematically deform a global potential energy landscape ($E_{\text{total}}$). The agent's final motor output vector ($m = [\dot{x}, \dot{y}]$) is not programmed; it is a direct physical relaxation along the negative gradient of this computed landscape:

$$\mathbf{m} \propto -\nabla E_{\text{total}}(x, y)$$

This ensures that the creature is continuously "falling" into the most homeostatically secure state calculated by its cortical microcircuits.

---

## Intellectual Property & Licensing
Copyright (c) 2026 Dr. Oscar G. Chang.  
Licensed under the GNU General Public License v3 (GPLv3). Mandatory academic attribution required for any derivative work or theoretical expansion.
