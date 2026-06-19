import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import winsound
import time

# ============================================================
# ESTADO DEL MUNDO (VALORES INICIALES)
# ============================================================

pos = np.array([0.0, 0.0])
theta = 0.0

hunger = 0.7
safety = 0.0  
danger = 0.0
border_stress = 0.0  

# ============================================================
# ENTIDADES DINÁMICAS
# ============================================================

food_pos = np.array([0.65, 0.45])
food_theta = 0.0
food_radius = 0.65

home_pos = np.array([-0.55, -0.35])
home_theta = np.pi
home_radius = 0.60

pred_pos = np.array([0.0, -0.7])
pred_theta = 0.0
pred_radius = 0.8

# ============================================================
# CONTROL
# ============================================================

decay_mode = True
time_warp = 1.0

food_lock = False
home_lock = False

# ============================================================
# BIOLOGICAL BRAIN: DOS ÁREAS CORTICALES SEPARADAS (N=25 c/u)
# ============================================================

N = 25
angles = np.linspace(0, 2*np.pi, N, endpoint=False)

# ÁREA 1: Corteza Motivacional
activity_mot = np.zeros(N)
cms_mot = []
for k in range(N):
    cms_mot.append({
        "angle": angles[k],
        "food_weight": np.random.uniform(1.2, 1.6), 
        "home_weight": np.random.uniform(1.3, 1.7), 
        "pred_weight": np.random.uniform(1.2, 1.7),
        "explore": np.random.uniform(0, 0.06)       
    })

# ÁREA 2: Corteza de Navegación Basal (Mapeo Perimetral Continuo)
activity_nav = np.zeros(N)
cms_nav = []
for k in range(N):
    cms_nav.append({
        "angle": angles[k],
        "border_weight": np.random.uniform(0.8, 1.2),  
        "explore": np.random.uniform(0, 0.05)
    })

# Configuración de la matriz visual (Brain Map) de 21x21
brain = np.zeros((21, 21))

# Dos cuadrados separados de 5x5 alineados al centro vertical
core_mot = [(r, c) for r in range(8, 13) for c in range(3, 8)]
core_nav = [(r, c) for r in range(8, 13) for c in range(13, 18)]

# ============================================================
# FIGURA
# ============================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)
ax1.set_facecolor("black")

home_zone = plt.Circle((home_pos[0], home_pos[1]), 0.25, color='blue', alpha=0.15, fill=True)
ax1.add_patch(home_zone)

boundary = plt.Rectangle((-0.95, -0.95), 1.9, 1.9, edgecolor='red', linestyle='--', fill=False, alpha=0.3)
ax1.add_patch(boundary)

dot, = ax1.plot([0], [0], 'wo', markersize=7)
food_dot, = ax1.plot(food_pos[0], food_pos[1], 'r*', markersize=14)
home_dot, = ax1.plot(home_pos[0], home_pos[1], 'bo', markersize=12)
pred_dot, = ax1.plot(pred_pos[0], pred_pos[1], 'go', markersize=14)

line, = ax1.plot([0, 0], [0, 0], 'w-', linewidth=2)
img = ax2.imshow(brain, vmin=0, vmax=1, cmap='inferno')

ax2.axvline(10, color='white', linestyle=':', alpha=0.2)

# ============================================================
# FUNCIÓN DE REINICIO
# ============================================================

def reset_system():
    global pos, theta, hunger, safety, danger, border_stress, activity_mot, activity_nav, brain
    global food_pos, food_theta, home_pos, home_theta, pred_pos, pred_theta
    global food_lock, home_lock
    
    winsound.Beep(180, 600)
    
    pos = np.array([0.0, 0.0])
    theta = 0.0
    hunger = 0.7
    safety = 0.0
    danger = 0.0
    border_stress = 0.0
    
    activity_mot = np.zeros(N)
    activity_nav = np.zeros(N)
    brain = np.zeros((21, 21))
    
    food_theta = np.random.uniform(0, 2*np.pi)
    home_theta = np.random.uniform(0, 2*np.pi)
    pred_theta = np.random.uniform(0, 2*np.pi)
    
    food_pos = np.array([food_radius * np.cos(food_theta), 0.55 * np.sin(1.7 * food_theta)])
    home_pos = np.array([home_radius * np.cos(home_theta), 0.45 * np.sin(1.3 * home_theta)])
    pred_pos = np.array([pred_radius * np.sin(pred_theta), pred_radius * np.cos(pred_theta)])
    
    food_lock = False
    home_lock = False
    
    time.sleep(0.5)

# ============================================================
# UPDATE LOOP
# ============================================================

def update(frame):
    global pos, theta
    global hunger, safety, danger, border_stress
    global activity_mot, activity_nav, brain
    global food_pos, home_pos, pred_pos
    global food_theta, home_theta, pred_theta
    global food_lock, home_lock

    # ========================================================
    # DISTANCIAS CRÍTICAS
    # ========================================================
    dist_food = np.linalg.norm(pos - food_pos)
    dist_home = np.linalg.norm(pos - home_pos)
    dist_pred = np.linalg.norm(pos - pred_pos)

    # ========================================================
    # HOMEOSTASIS Y FILTRO DE HISTÉRESIS
    # ========================================================
    hunger += 0.0028 * time_warp  

    if dist_home < 0.25:
        safety = 0.0  
    else:
        safety += 0.0042 * time_warp  

    hunger = np.clip(hunger, 0, 1)
    safety = np.clip(safety, 0, 1)
    danger += 0.006 * time_warp
    danger = np.clip(danger, 0, 1)

    # Determinar si está formalmente en reposo dentro de la cueva
    in_cave_repose = False
    if dist_home < 0.25:
        if hunger < 0.75:
            effective_hunger = 0.0  
            current_safety_need = 1.0  
            in_cave_repose = True  
        else:
            effective_hunger = hunger  
            current_safety_need = 0.0
    else:
        if safety > 0.80:
            attenuation = (1.0 - safety) / 0.20
            effective_hunger = hunger * np.clip(attenuation, 0, 1)
            current_safety_need = safety * 1.8   
        elif hunger > 0.50 and safety < 0.40:
            effective_hunger = hunger * 1.5   
            current_safety_need = safety * 0.3  
        else:
            effective_hunger = hunger
            current_safety_need = safety

    # Variable de confinamiento de bordes
    dist_to_wall_x = 1.0 - abs(pos[0])
    dist_to_wall_y = 1.0 - abs(pos[1])
    closest_wall_dist = min(dist_to_wall_x, dist_to_wall_y)
    
    if closest_wall_dist < 0.25:
        border_stress = np.clip((0.25 - closest_wall_dist) / 0.25, 0, 1) ** 2
    else:
        border_stress = 0.0

    # ========================================================
    # MOTION ENTIDADES
    # ========================================================
    food_theta += 0.015 * time_warp
    food_pos = np.array([food_radius * np.cos(food_theta), 0.55 * np.sin(1.7 * food_theta)])

    home_theta -= 0.010 * time_warp
    home_pos = np.array([home_radius * np.cos(home_theta), 0.45 * np.sin(1.3 * home_theta)])
    home_zone.set_center((home_pos[0], home_pos[1])) 

    # MOTION DEPREDADOR
    pred_speed = 0.023 * time_warp
    if dist_home < 0.25:
        pred_theta += np.random.uniform(-0.6, 0.6)
    else:
        to_prey = pos - pred_pos
        pred_theta = np.arctan2(to_prey[1], to_prey[0])

    pred_pos += pred_speed * np.array([np.cos(pred_theta), np.sin(pred_theta)])
    pred_pos = np.clip(pred_pos, -1.2, 1.2)

    # COLISIONES / RECOMPENSAS
    if dist_food < 0.10 and not food_lock:
        hunger = 0.0
        winsound.Beep(1200, 120)
        food_lock = True

    if dist_home < 0.10 and not home_lock:
        winsound.Beep(500, 180)
        home_lock = True

    if dist_pred < 0.12:
        if dist_home < 0.25:
            danger = 0.0  
        else:
            reset_system()
            return dot, line, img, food_dot, home_dot, pred_dot

    if dist_food > 0.18: food_lock = False
    if dist_home > 0.18: home_lock = False

    # ========================================================
    # DIRECCIONES SENSORIALES
    # ========================================================
    vec_food = food_pos - pos
    vec_home = home_pos - pos
    vec_pred = pred_pos - pos

    angle_food = np.arctan2(vec_food[1], vec_food[0])
    angle_home = np.arctan2(vec_home[1], vec_home[0])
    angle_pred = np.arctan2(vec_pred[1], vec_pred[0])

    # Gradiente de campo continuo para el límite geométrico
    fuerza_oeste = 1.0 / (1.0 + (pos[0] - (-0.95)))
    fuerza_este  = 1.0 / (1.0 + (0.95 - pos[0]))
    fuerza_sur   = 1.0 / (1.0 + (pos[1] - (-0.95)))
    fuerza_norte = 1.0 / (1.0 + (0.95 - pos[1]))

    vec_border_continuo = np.array([
        (fuerza_este - fuerza_oeste),
        (fuerza_norte - fuerza_sur)
    ])
    angle_border = np.arctan2(vec_border_continuo[1], vec_border_continuo[0])

    # ========================================================
    # COMPETENCIA LOCAL N-FLOP POR ÁREA
    # ========================================================
    energies_mot = np.zeros(N)
    for i, cm in enumerate(cms_mot):
        food_align = np.cos(angle_food - cm["angle"])
        home_align = np.cos(angle_home - cm["angle"])
        pred_align = np.cos(angle_pred - cm["angle"])
        
        current_danger_factor = 0.0 if dist_home < 0.25 else danger

        E_mot = (
            effective_hunger * cm["food_weight"] * food_align +
            current_safety_need * cm["home_weight"] * home_align -
            current_danger_factor * cm["pred_weight"] * pred_align +
            cm["explore"] * np.random.uniform(-1, 1)
        )
        energies_mot[i] = E_mot + 0.06 * np.random.randn() 
    winner_mot = np.argmax(energies_mot)

    energies_nav = np.zeros(N)
    for i, cm in enumerate(cms_nav):
        border_align = np.cos(angle_border - cm["angle"])
        E_nav = -border_stress * cm["border_weight"] * border_align + cm["explore"] * np.random.uniform(-1, 1)
        energies_nav[i] = E_nav + 0.05 * np.random.randn()
    winner_nav = np.argmax(energies_nav)

    # ========================================================
    # INTEGRACIÓN DE DECAY (ESPACIALMENTE DISPERSO EN REPOSO)
    # ========================================================
    if decay_mode:
        activity_mot *= (0.92 ** time_warp)
        activity_mot[winner_mot] += 1.0
        
        if in_cave_repose:
            # 🔥 CORRECCIÓN VISUAL: El decaimiento es fuerte (para vaciar el fondo)
            activity_nav *= (0.70 ** time_warp)  
            
            # Solo permitimos que se enciendan 1 o 2 CM elegidos al azar en cada ciclo (Sparse Noise)
            # Esto simula fluctuaciones locales ganando la competencia temporalmente mientras el resto queda oscuro
            if np.random.uniform(0, 1) < 0.40:  # Probabilidad de disparo espontáneo por ciclo
                num_destellos = np.random.choice([1, 2])
                indices_suertudos = np.random.choice(N, size=num_destellos, replace=False)
                # Inyectamos un brillo intenso y nítido que contrastará fuertemente
                brillo_destello = 0.65 + 0.25 * np.sin(frame * 0.2)
                activity_nav[indices_suertudos] += brillo_destello
        else:
            activity_nav *= (0.90 ** time_warp)  
            activity_nav[winner_nav] += 1.0
    else:
        activity_mot[:] = 0.0; activity_mot[winner_mot] = 1.0
        if in_cave_repose:
            activity_nav[:] = 0.0
            activity_nav[np.random.choice(N)] = 0.8
        else:
            activity_nav[:] = 0.0; activity_nav[winner_nav] = 1.0

    activity_mot = np.clip(activity_mot, 0, 1)
    activity_nav = np.clip(activity_nav, 0, 1)

    # ========================================================
    # SÍNTESIS MOTORA E INTEGRACIÓN CORTICAL
    # ========================================================
    motor_mot = np.zeros(2)
    motor_nav = np.zeros(2)

    for i in range(N):
        vec = np.array([np.cos(angles[i]), np.sin(angles[i])])
        motor_mot += activity_mot[i] * vec
        motor_nav += activity_nav[i] * vec

    if np.linalg.norm(motor_mot) > 0: motor_mot /= np.linalg.norm(motor_mot)
    if np.linalg.norm(motor_nav) > 0: motor_nav /= np.linalg.norm(motor_nav)

    if border_stress > 0.15:
        motor = (1.0 - border_stress) * motor_mot + border_stress * motor_nav
    else:
        motor = motor_mot

    mag = np.linalg.norm(motor)
    if mag > 0:
        motor /= mag
        theta = np.arctan2(motor[1], motor[0])
        
        speed = (0.03 + 0.03 * np.clip(mag, 0, 1)) * time_warp
        
        if in_cave_repose:
            pos = 0.90 * pos + 0.10 * home_pos  
            speed = 0.0
            
        pos += speed * motor

    pos = np.clip(pos, -0.95, 0.95)

    # ========================================================
    # MAPA VISUAL CORTICAL (TEJIDO ESPACIO-TIEMPO)
    # ========================================================
    brain *= 0.82  
    
    for i, a in enumerate(activity_mot):
        ii, jj = core_mot[i]
        brain[ii, jj] = a
        
    for i, a in enumerate(activity_nav):
        ii, jj = core_nav[i]
        brain[ii, jj] = a

    brain = np.clip(brain, 0, 1)

    # ========================================================
    # INTERFAZ GRÁFICA
    # ========================================================
    dot.set_data([pos[0]], [pos[1]])
    head = pos + 0.12 * np.array([np.cos(theta), np.sin(theta)])
    line.set_data([pos[0], head[0]], [pos[1], head[1]])

    food_dot.set_data([food_pos[0]], [food_pos[1]])
    home_dot.set_data([home_pos[0]], [home_pos[1]])
    pred_dot.set_data([pred_pos[0]], [pred_pos[1]])

    img.set_data(brain)

    ax2.set_title(
        f"Izq: Córtex MOT (H={hunger:.2f} S={safety:.2f})\n"
        f"Der: Córtex NAV (Destellos Dispersos)"
    )

    return dot, line, img, food_dot, home_dot, pred_dot

# ============================================================
# RUN
# ============================================================
ani = FuncAnimation(fig, update, interval=60, cache_frame_data=False)
plt.show()