from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(20, 8), facecolor="#0a0a1a")

# ─── PANEL A: Nube de probabilidad 1s ───────────────────────────────────────
ax_a = fig.add_subplot(131, projection="3d", facecolor="#0a0a1a")

# Simular distribución de probabilidad 1s (exponencial)
n_particles = 3000
r = np.random.exponential(1.0, n_particles)
theta = np.random.uniform(0, 2*np.pi, n_particles)
phi = np.arccos(np.random.uniform(-1, 1, n_particles))

x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Colorear por densidad de probabilidad
prob = np.exp(-2*r)

ax_a.scatter(x, y, z, c=prob, cmap="hot", s=2, alpha=0.4, edgecolors="none")
ax_a.set_title("Orbital 1s\n(n=1, l=0, m=0)", fontsize=13, color="white", fontweight="bold", pad=5)
ax_a.set_xlim(-4, 4); ax_a.set_ylim(-4, 4); ax_a.set_zlim(-4, 4)
ax_a.axis("off")
ax_a.view_init(elev=25, azim=45)

# ─── PANEL B: Nube 2p ───────────────────────────────────────────────────────
ax_b = fig.add_subplot(132, projection="3d", facecolor="#0a0a1a")

# Orbital 2p_z: distribución r * cos(theta) * exp(-r/2)
n_p = 4000
r_p = np.random.exponential(2.0, n_p)
theta_p = np.random.uniform(0, 2*np.pi, n_p)
phi_p = np.arccos(np.random.uniform(-1, 1, n_p))

x_p = r_p * np.sin(phi_p) * np.cos(theta_p)
y_p = r_p * np.sin(phi_p) * np.sin(theta_p)
z_p = r_p * np.cos(phi_p)

# Probabilidad 2p ∝ r² * cos²(theta) * exp(-r)
prob_2p = np.abs(np.cos(phi_p)) * np.exp(-r_p/2)
mask = prob_2p > np.percentile(prob_2p, 30)

ax_b.scatter(x_p[mask], y_p[mask], z_p[mask], c=prob_2p[mask], cmap="cool", s=2, alpha=0.4, edgecolors="none")
ax_b.set_title("Orbital 2p\n(n=2, l=1, m=0)", fontsize=13, color="white", fontweight="bold", pad=5)
ax_b.set_xlim(-6, 6); ax_b.set_ylim(-6, 6); ax_b.set_zlim(-6, 6)
ax_b.axis("off")
ax_b.view_init(elev=25, azim=45)

# ─── PANEL C: Explicación ───────────────────────────────────────────────────
ax_c = fig.add_subplot(133, facecolor="#0a0a1a")
ax_c.set_xlim(0, 10)
ax_c.set_ylim(0, 12)
ax_c.axis("off")

texts_c = [
    (11.5, "MODELO ATOMICO CUANTICO", "#ffffff", 15, "bold"),
    (10.5, "Schrodinger (1926)", "#888888", 11, "normal"),
    (9.5, "─────────────────", "#333333", 10, "normal"),
    (8.7, "Numeros cuanticos:", "#ffffff", 13, "bold"),
    (7.9, "n  = principal (capa)", "#4fc3f7", 12, "normal"),
    (7.1, "l  = azimutal (forma)", "#ef5350", 12, "normal"),
    (6.3, "ml = magnetico (ori.)", "#ffd54f", 12, "normal"),
    (5.5, "ms = espín (+1/2, -1/2)", "#ab47bc", 12, "normal"),
    (4.5, "─────────────────", "#333333", 10, "normal"),
    (3.7, "Orbitales:", "#ffffff", 13, "bold"),
    (2.9, "s = esfera (l=0)", "#4fc3f7", 12, "normal"),
    (2.1, "p = dumbbell (l=1)", "#ef5350", 12, "normal"),
    (1.3, "d = trebol (l=2)", "#ffd54f", 12, "normal"),
    (0.5, "f = complejo (l=3)", "#ab47bc", 12, "normal"),
]
for y, txt, color, size, weight in texts_c:
    ax_c.text(5, y, txt, ha="center", va="top", fontsize=size, color=color, fontweight=weight, fontfamily="monospace")

fig.suptitle("NUBES DE PROBABILIDAD - ORBITALES ATOMICOS",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
out_path = str(BASE_DIR / "quantum_atom.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
