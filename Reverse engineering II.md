# The Invisible Mind - Reverse Engineering Guide

## Understanding the Creature's Cortical Architecture

---

## Introduction

This guide walks through the creature's brain, explaining how 50 simple **microcircuits** create complex behavior without memory or planning. We'll look at each component and see how they work together.

---

## The Big Picture

The creature lives in a 2D world. It has needs (hunger, safety), enemies (a predator), resources (food, home), and a brain made of two **cortical areas** that compete to control its movement.

```
SENSORS → CORTICAL AREAS → COMPETITION → MOVEMENT
```

---

## What This System Is NOT

**It is NOT two brains.** It is one brain with **two specialized cortical areas**, exactly like your brain has visual cortex, motor cortex, and prefrontal cortex—different regions handling different tasks.

| Area | Function |
|------|----------|
| **MOT** | Motivational cortex - handles needs (hunger, safety, danger) |
| **NAV** | Navigational cortex - handles space (walls, boundaries) |

These areas are **not independent brains**. They are specialized regions that **cooperate** to produce behavior, just like cortical columns in your own head.

---

## The Microcircuit

Each cortical area has **25 microcircuits** (we'll see why 25 matters later).

Each microcircuit has a **preferred direction** (angle):

```
Microcircuit 0: 0°   → Points East
Microcircuit 1: 14°  → Points slightly East
Microcircuit 2: 29°  → Points more East
...
Microcircuit 24: 346° → Points West-ish
```

**Why 25?** Because 25 directions cover the circle evenly. More microcircuits = smoother movement. Fewer = jerkier.

---

## How a Microcircuit Works

Each microcircuit calculates its **energy** by asking:

> "How well do I point toward what matters right now?"

### MOT Microcircuits Ask:

```
energy = hunger × alignment_to_food 
       + safety × alignment_to_home
       - danger × alignment_to_predator
```

### NAV Microcircuits Ask:

```
energy = -border_stress × alignment_away_from_wall
```

### Alignment

Alignment is just: `cos(angle_to_target - microcircuit_angle)`

- Points exactly at target? → alignment = 1 (perfect)
- Points 90° away? → alignment = 0 (neutral)
- Points opposite? → alignment = -1 (avoid)

**Example:** If food is East and a microcircuit points East, it gets high energy.

---

## Competition: The Winner Takes All

At each moment, all 25 microcircuits in an area calculate their energy. The one with the **highest energy** wins.

```
All microcircuits: [0.2, 0.8, 0.3, 0.1, ...]  ← energies
Winner:            [_, 0.8, _, _, ...]         ← microcircuit 1 wins!
```

The winner doesn't "decide" anything. It just happens to have the highest energy.

**The winning microcircuit gets a boost:** `activity[winner] += 1.0`

---

## Persistence: The Lingering Activity

Here's the secret to smooth behavior:

When a microcircuit wins, its activity doesn't disappear. It **lingers** through decay.

```
activity = activity × 0.92   ← Slowly fade
activity[winner] += 1.0      ← Boost the winner
```

**Why this matters:**

Without decay:
```
Frame 1: winner = microcircuit 5 → activity[5] = 1.0
Frame 2: winner = microcircuit 8 → activity[5] = 1.0, activity[8] = 1.0
Frame 3: winner = microcircuit 2 → all microcircuits active → chaos!
```

With decay:
```
Frame 1: winner = microcircuit 5 → activity[5] = 1.0
Frame 2: winner = microcircuit 8 → activity[5] = 0.92, activity[8] = 1.0
Frame 3: winner = microcircuit 2 → activity[5] = 0.84, activity[8] = 0.92, activity[2] = 1.0
```

The activity **flows** from one microcircuit to the next, creating **smooth movement**.

---

## The Motor Output

The creature moves by combining all active microcircuits:

```
motor = sum(activity[i] × direction[i] for i in range(25))
```

Each active microcircuit pulls the creature in its direction. The pull is weighted by how active the microcircuit is.

**Example:**

```
Active microcircuits:
  microcircuit 5: activity=0.92, direction=(0.8, 0.5)
  microcircuit 8: activity=1.0, direction=(0.3, 0.9)

Weighted sum = 0.92 × (0.8, 0.5) + 1.0 × (0.3, 0.9)
            = (0.736, 0.46) + (0.3, 0.9)
            = (1.036, 1.36)

Final direction = normalize → (0.61, 0.79)
```

The creature moves in a **blended** direction, smoothly transitioning between choices.

---

## Two Cortical Areas Cooperating

### MOT (Motivational Cortex)

- Handles **needs**: hunger, safety, danger
- Wants to eat, go home, avoid predators
- Active in open spaces

### NAV (Navigational Cortex)

- Handles **space**: walls, boundaries
- Wants to stay in safe areas
- Active near borders

### How They Cooperate

When near a wall:
```
final_direction = NAV_direction  ← Walls take priority
```

When in open space:
```
final_direction = MOT_direction  ← Needs take priority
```

When moderately close to wall:
```
final_direction = (1 - stress) × MOT_direction + stress × NAV_direction
```

**This is not two brains deciding.** This is one brain with two specialized regions that **cooperate** to produce balanced behavior.

---

## Dark Energy: Activity in Rest

When the creature rests at home, something interesting happens:

```
activity[winner] += 1.0          ← Normal competition
activity *= 0.70                  ← Fast decay
if random() < 0.40:               ← 40% chance
    lucky = random_microcircuit()
    activity[lucky] += 0.8        ← Spark!
```

These sparks are **spontaneous activity**—like your brain's default mode network when you're daydreaming.

**Why?**
- Without sparks: creature never leaves home (frozen)
- With sparks: random pulses occasionally suggest: *"Maybe I should explore..."*

**Dark energy keeps the brain alive even in rest.**

---

## The Complete Cycle

```
Every frame (60 times per second):

1. Update needs:
   hunger += 0.0028
   safety += 0.0042 (if outside)
   danger += 0.006

2. Calculate energy for each MOT microcircuit:
   energy = hunger × food_alignment 
          + safety × home_alignment
          - danger × pred_alignment

3. Find MOT winner

4. Update MOT activity:
   activity *= 0.92
   activity[winner] += 1.0

5. Repeat steps 2-4 for NAV (walls only)

6. Calculate motor:
   MOT_motor = sum(activity[i] × direction[i])
   NAV_motor = sum(activity[i] × direction[i])
   
   if near_wall:
       motor = (1-stress) × MOT_motor + stress × NAV_motor
   else:
       motor = MOT_motor

7. Move:
   position += speed × motor
   clip to boundaries

8. Check collisions:
   if near_food: eat (hunger = 0)
   if near_home: safe
   if near_predator and outside_home: reset!
```

---

## The Emergent Cycle

**No rule says:** *"Find food, then go home, then rest."*

**But the creature does exactly that.** How?

```
Hunger grows → MOT seeks food → Eat (hunger = 0) →
Safety grows → MOT seeks home → Enter home (safety = 0) →
Rest (dark energy sparks) → Hunger grows again → Cycle repeats
```

The cycle **emerges** from:
- Competition between microcircuits
- Changing needs
- Activity persistence
- Random exploration

**The behavior is not programmed. It emerges.**

---

## What You Can Change

| Parameter | Effect |
|-----------|--------|
| `N = 50` | Smoother movement (more microcircuits) |
| `decay = 0.98` | Slower changes, more persistent memory |
| `decay = 0.70` | Faster changes, more responsive |
| `time_warp = 2.0` | Double speed |
| `hunger_rate = 0.005` | Faster hunger growth |
| `dark_energy_prob = 0.8` | More exploration in rest |

**Try changing these. Watch how the creature's behavior transforms.**

---

## Why This Matters

### Without Memory

The creature has no memory:
- No "I remember where food is"
- No "I remember the path home"
- No stored representations

**And yet it behaves adaptively.**

### With Cortical Specialization

The creature has two cortical areas:
- **MOT** handles needs
- **NAV** handles space

**They specialize and cooperate, like cortical columns in your brain.**

### With Dark Energy

The creature has spontaneous activity:
- Sparks during rest
- Exploration without external cause

**This is exactly what Raichle discovered: your brain uses 20% of your energy even at rest.**

---

## Summary

| Principle | How It Works |
|-----------|--------------|
| **Microcircuits** | 25 per area, each with a preferred direction |
| **Competition** | Highest energy microcircuit wins each frame |
| **Persistence** | Activity decays slowly (λ=0.92) |
| **Cortical Areas** | MOT (needs) and NAV (space) cooperate |
| **Motor Output** | Weighted sum of active microcircuits |
| **Dark Energy** | Random sparks during rest |
| **Emergence** | Complex behavior from simple rules |

---

## Try It Yourself

```bash
python creature_multi_CM_D.py
```

Watch the brain display. See the microcircuits flicker. Observe the creature's behavior.

**Ask yourself:** *Where is the "mind" in this system?*

The answer: **It's everywhere and nowhere.** The mind is the **pattern** of activity flowing through the tissue—a process, not a thing.

---

## Final Thought

> A genome does not contain a creature.
> 
> A seed does not contain a forest.
> 
> A microcircuit does not contain a thought.
> 
> **Thoughts emerge when deployed structures persist long enough in space and time to generate new trajectories of interaction.**

---

*"A thought is not a thing you have. A thought is something you are."*

---

## About This Document

This guide accompanies:
- **[FOUNDATIONS.md](FOUNDATIONS.md)** — Mathematical foundations
- **[creature_multi_CM_D.py](creature_multi_CM_D.py)** — Reference implementation

The creature is real. The code runs. The behavior emerges.

**See for yourself.**
