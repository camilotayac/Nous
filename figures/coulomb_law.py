from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyArrowPatch

np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(22, 8), gridspec_kw={"width_ratios": [1, 1.2, 0.8]})
fig.patch.set_facecolor("#0a0a1a")

# ─── PANEL A: Dos cargas del mismo signo ────────────────────────────────────
ax_a = axes[0]
ax_a.set_xlim(-5, 5)
ax_a.set_ylim(-5, 5)
ax_a.set_aspect("equal")
ax_a.set_facecolor("#0a0a1a")
ax_a.axis("off")

# Cargas
q1_pos = np.array([-2, 0])
q2_pos = np.array([2, 0])
circle1 = plt.Circle(q1_pos, 0.6, color="#ef5350", zorder=10)
circle2 = plt.Circle(q2_pos, 0.6, color="#ef5350", zorder=10)
ax_a.add_patch(circle1)
ax_a.add_patch(circle2)
ax_a.text(-2, 0, "+q", ha="center", va="center", fontsize=16, fontweight="bold", color="white", zorder=11)
ax_a.text(2, 0, "+q", ha="center", va="center", fontsize=16, fontweight="bold", color="white", zorder=11)

# Líneas de campo (repulsión)
for angle in np.linspace(-0.8, 0.8, 7):
    dx = np.cos(angle) * 0.8
    dy = np.sin(angle) * 0.8
    # Flechas saliendo de q1
    ax_a.annotate("", xy=(-2 + dx*2.5, dy*2.5), xytext=(-2 + dx, dy),
                  arrowprops=dict(arrowstyle="->", color="#ffab91", lw=1.5, alpha=0.7))
    # Flechas saliendo de q2
    ax_a.annotate("", xy=(2 + dx*2.5, dy*2.5), xytext=(2 + dx, dy),
                  arrowprops=dict(arrowstyle="->", color="#ffab91", lw=1.5, alpha=0.7))

# Distancia
ax_a.annotate("", xy=(2, -1.5), xytext=(-2, -1.5),
              arrowprops=dict(arrowstyle="<->", color="#ffd54f", lw=2))
ax_a.text(0, -1.8, "r", ha="center", va="top", fontsize=18, color="#ffd54f", fontweight="bold")

# Fuerza
ax_a.annotate("", xy=(3.5, 0.8), xytext=(2.5, 0.4),
              arrowprops=dict(arrowstyle="->", color="#4fc3f7", lw=2.5))
ax_a.annotate("", xy=(-3.5, 0.8), xytext=(-2.5, 0.4),
              arrowprops=dict(arrowstyle="->", color="#4fc3f7", lw=2.5))
ax_a.text(3.2, 1.2, "F", fontsize=14, color="#4fc3f7", fontweight="bold")
ax_a.text(-3.5, 1.2, "F", fontsize=14, color="#4fc3f7", fontweight="bold")

ax_a.set_title("Mismo signo\n(Repulsion)", fontsize=14, color="#ef5350", fontweight="bold", pad=15)

# ─── PANEL B: Dos cargas de signo opuesto ────────────────────────────────────
ax_b = axes[1]
ax_b.set_xlim(-5, 5)
ax_b.set_ylim(-5, 5)
ax_b.set_aspect("equal")
ax_b.set_facecolor("#0a0a1a")
ax_b.axis("off")

# Cargas
circle_p = plt.Circle(q1_pos, 0.6, color="#ef5350", zorder=10)
circle_n = plt.Circle(q2_pos, 0.6, color="#4fc3f7", zorder=10)
ax_b.add_patch(circle_p)
ax_b.add_patch(circle_n)
ax_b.text(-2, 0, "+q", ha="center", va="center", fontsize=16, fontweight="bold", color="white", zorder=11)
ax_b.text(2, 0, "-q", ha="center", va="center", fontsize=16, fontweight="bold", color="white", zorder=11)

# Líneas de campo (atracción)
for angle in np.linspace(-1.0, 1.0, 9):
    dy = np.sin(angle) * 1.5
    ax_b.annotate("", xy=(1.5, dy), xytext=(-1.5, dy),
                  arrowprops=dict(arrowstyle="->", color="#ce93d8", lw=1.5, alpha=0.6,
                                  connectionstyle="arc3,rad=0"))

# Distancia
ax_b.annotate("", xy=(2, -1.5), xytext=(-2, -1.5),
              arrowprops=dict(arrowstyle="<->", color="#ffd54f", lw=2))
ax_b.text(0, -1.8, "r", ha="center", va="top", fontsize=18, color="#ffd54f", fontweight="bold")

# Fuerza (hacia adentro)
ax_b.annotate("", xy=(-0.5, 0), xytext=(-1.5, 0),
              arrowprops=dict(arrowstyle="->", color="#4fc3f7", lw=2.5))
ax_b.annotate("", xy=(0.5, 0), xytext=(1.5, 0),
              arrowprops=dict(arrowstyle="->", color="#4fc3f7", lw=2.5))
ax_b.text(-0.5, 0.3, "F", fontsize=14, color="#4fc3f7", fontweight="bold")
ax_b.text(0.5, 0.3, "F", fontsize=14, color="#4fc3f7", fontweight="bold")

# Curvas de campo con estilo
theta = np.linspace(0, 2*np.pi, 100)
for r_field in [1.5, 2.5, 3.5]:
    x_field = q1_pos[0] + r_field * np.cos(theta)
    y_field = q1_pos[1] + r_field * np.sin(theta)
    mask = x_field < q2_pos[0]
    ax_b.plot(x_field[mask], y_field[mask], color="#ce93d8", alpha=0.15, lw=0.8)

ax_b.set_title("Signo opuesto\n(Atraccion)", fontsize=14, color="#4fc3f7", fontweight="bold", pad=15)

# ─── PANEL C: Fórmula y explicación ──────────────────────────────────────────
ax_c = axes[2]
ax_c.set_xlim(0, 10)
ax_c.set_ylim(0, 12)
ax_c.set_aspect("equal")
ax_c.axis("off")
ax_c.set_facecolor("#0a0a1a")

texts_c = [
    (11.5, "LEY DE COULOMB", "#ffffff", 16, "bold"),
    (10.8, "(1785)", "#888888", 11, "normal"),
    (9.8, "F = k * |q1*q2| / r2", "#ffd54f", 20, "bold"),
    (8.8, "k = 8.99 x 109 N*m2/C2", "#cccccc", 12, "normal"),
    (7.8, "r = distancia entre cargas", "#cccccc", 12, "normal"),
    (6.8, "─────────────────", "#333333", 10, "normal"),
    (6.0, "PROPIEDADES:", "#ffffff", 14, "bold"),
    (5.2, "(1) F es conservativa", "#ef5350", 12, "normal"),
    (4.4, "(2) Principio de superposicion", "#ef5350", 12, "normal"),
    (3.6, "(3) F prop. a q1 * q2", "#ef5350", 12, "normal"),
    (2.8, "(4) F prop. a 1/r2", "#ef5350", 12, "normal"),
    (1.8, "─────────────────", "#333333", 10, "normal"),
    (1.0, "En la naturaleza:", "#4fc3f7", 12, "bold"),
    (0.3, "Enlace iónico, cristales", "#4fc3f7", 11, "normal"),
]
for y, txt, color, size, weight in texts_c:
    ax_c.text(5, y, txt, ha="center", va="top", fontsize=size, color=color, fontweight=weight, fontfamily="monospace")

fig.suptitle("LEY DE COULOMB: FUERZA ENTRE CARGAS ELECTRICAS",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.94])
out_path = str(BASE_DIR / "coulomb_law.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
