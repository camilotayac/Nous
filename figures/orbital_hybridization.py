from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(20, 7), facecolor="#0a0a1a")

# ─── PANEL A: Orbitales atómicos p ──────────────────────────────────────────
ax_a = fig.add_subplot(131, projection="3d", facecolor="#0a0a1a")

def orbital_p(ax, axis, color, alpha=0.35):
    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 40)
    r = 1.2
    if axis == "z":
        x = r * np.outer(np.sin(v), np.cos(u))
        y = r * np.outer(np.sin(v), np.sin(u))
        z = r * 2 * np.outer(np.cos(v), np.ones_like(u))
    elif axis == "x":
        y = r * np.outer(np.sin(v), np.cos(u))
        z = r * np.outer(np.sin(v), np.sin(u))
        x = r * 2 * np.outer(np.cos(v), np.ones_like(u))
    else:
        x = r * np.outer(np.sin(v), np.cos(u))
        z = r * np.outer(np.sin(v), np.sin(u))
        y = r * 2 * np.outer(np.cos(v), np.ones_like(u))
    ax.plot_surface(x, y, z, color=color, alpha=alpha)

orbital_p(ax_a, "x", "#ef5350")
orbital_p(ax_a, "y", "#4fc3f7")
orbital_p(ax_a, "z", "#ffd54f")
ax_a.set_title("Orbitales p\n(3 direcciones)", fontsize=14, color="white", fontweight="bold", pad=10)
ax_a.set_xlim(-3, 3); ax_a.set_ylim(-3, 3); ax_a.set_zlim(-3, 3)
ax_a.axis("off")
ax_a.view_init(elev=20, azim=45)

# ─── PANEL B: Hibridación sp3 ───────────────────────────────────────────────
ax_b = fig.add_subplot(132, projection="3d", facecolor="#0a0a1a")

# Tetraedro: 4 orbitales sp3
angles_sp3 = [
    (1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)
]
colors_sp3 = ["#ab47bc", "#ab47bc", "#ab47bc", "#ab47bc"]

for (dx, dy, dz), col in zip(angles_sp3, colors_sp3):
    norm = np.sqrt(dx**2 + dy**2 + dz**2)
    dx, dy, dz = dx/norm, dy/norm, dz/norm
    # Lóbulo principal
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi/2, 20)
    r = 1.5
    x = r * np.outer(np.sin(v), np.cos(u)) * abs(dx)
    y = r * np.outer(np.sin(v), np.sin(u)) * abs(dy)
    z = r * np.outer(np.cos(v), np.ones_like(u)) * abs(dz)
    x += dx * 0.5
    y += dy * 0.5
    z += dz * 0.5
    ax_b.plot_surface(x, y, z, color=col, alpha=0.45)

# Centro (núcleo)
ax_b.scatter([0], [0], [0], color="#ffd54f", s=200, zorder=100, edgecolors="white", linewidth=2)
ax_b.text(0, 0, 0.3, "C", ha="center", fontsize=14, color="white", fontweight="bold")

# Enlaces
for dx, dy, dz in angles_sp3:
    norm = np.sqrt(dx**2 + dy**2 + dz**2)
    ax_b.plot([0, dx/norm*2], [0, dy/norm*2], [0, dz/norm*2], 
              color="white", lw=1.5, alpha=0.6, linestyle="--")

ax_b.set_title("Hibridacion sp3\n(Geometria tetraedrica)", fontsize=14, color="white", fontweight="bold", pad=10)
ax_b.set_xlim(-3, 3); ax_b.set_ylim(-3, 3); ax_b.set_zlim(-3, 3)
ax_b.axis("off")
ax_b.view_init(elev=20, azim=60)

# ─── PANEL C: Explicación ───────────────────────────────────────────────────
ax_c = fig.add_subplot(133, facecolor="#0a0a1a")
ax_c.set_xlim(0, 10)
ax_c.set_ylim(0, 12)
ax_c.axis("off")

texts_c = [
    (11.5, "HIBRIDACION sp3", "#ffffff", 16, "bold"),
    (10.5, "Mezcla de orbitales", "#888888", 12, "normal"),
    (9.5, "─────────────────", "#333333", 10, "normal"),
    (8.7, "1 orbital s + 3 orbitales p", "#ab47bc", 14, "bold"),
    (7.8, "= 4 orbitales hibridos sp3", "#ab47bc", 14, "bold"),
    (6.8, "─────────────────", "#333333", 10, "normal"),
    (6.0, "Geometria:", "#ffffff", 13, "bold"),
    (5.2, "Tetraedrica (109.5 grados)", "#ffd54f", 12, "normal"),
    (4.4, "Angulo entre enlaces:", "#cccccc", 12, "normal"),
    (3.6, "  cos(theta) = -1/3", "#4fc3f7", 13, "bold"),
    (2.6, "─────────────────", "#333333", 10, "normal"),
    (1.8, "Ejemplos:", "#ffffff", 13, "bold"),
    (1.0, "CH4, NH3, H2O, C2H6", "#ef5350", 13, "bold"),
    (0.2, "Carbono, nitrogeno, oxigeno", "#888888", 11, "normal"),
]
for y, txt, color, size, weight in texts_c:
    ax_c.text(5, y, txt, ha="center", va="top", fontsize=size, color=color, fontweight=weight, fontfamily="monospace")

fig.suptitle("HIBRIDACION sp3: ORBITALES Y GEOMETRIA MOLECULAR",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
out_path = str(BASE_DIR / "orbital_hybridization.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
