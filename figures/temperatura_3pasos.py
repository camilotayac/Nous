from pathlib import Path
BASE_DIR = Path(__file__).parent

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(22, 8), facecolor="#0a0a1a")
fig.patch.set_facecolor("#0a0a1a")

C_BLUE = "#4fc3f7"
C_RED = "#ef5350"
C_YELLOW = "#ffd54f"
C_GREEN = "#66bb6a"
C_WHITE = "#ffffff"
C_MUTED = "#888888"
C_DARK = "#0a0a1a"

def draw_particles_with_speed(ax, n, speed_range, color, temp_label, y_label, temp_color):
    """Dibuja partículas con flechas de velocidad proporcionales a T"""
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor(C_DARK)

    # Recipiente
    recip = plt.Rectangle((5, 15), 90, 70, facecolor="#111122", edgecolor=C_MUTED,
                           linewidth=2, alpha=0.5, linestyle="--", zorder=1)
    ax.add_patch(recip)

    # Termómetro visual
    term_x = 88
    term_y = 80
    ax.plot([term_x, term_x], [term_y-12, term_y+5], color=C_MUTED, lw=4, solid_capstyle="round")
    ax.plot([term_x, term_x], [term_y-12, term_y - 12 + 17 * (speed_range[1]/30)],
            color=temp_color, lw=4, solid_capstyle="round", zorder=5)
    term_circle = plt.Circle((term_x, term_y-14), 3, color=temp_color, zorder=5)
    ax.add_patch(term_circle)
    ax.text(term_x-6, term_y+8, temp_label, fontsize=10, color=temp_color,
            fontweight="bold", fontfamily="monospace")

    # Posiciones de partículas
    xs = np.random.uniform(15, 80, n)
    ys = np.random.uniform(25, 75, n)

    # Velocidades (longitud de flecha proporcional a T)
    speeds = np.random.uniform(speed_range[0], speed_range[1], n)
    angles = np.random.uniform(0, 2*np.pi, n)

    for i in range(n):
        # Partícula
        particle = plt.Circle((xs[i], ys[i]), 3.5, color=color, alpha=0.85,
                               zorder=5, edgecolor="white", linewidth=1)
        ax.add_patch(particle)

        # Flecha de velocidad (longitud = speed)
        dx = speeds[i] * np.cos(angles[i])
        dy = speeds[i] * np.sin(angles[i])
        ax.annotate("", xy=(xs[i]+dx, ys[i]+dy), xytext=(xs[i], ys[i]),
                     arrowprops=dict(arrowstyle="->", color="white",
                                     lw=1.5, alpha=0.5), zorder=4)

    # Conteo de colisiones simulado
    collision_count = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = np.sqrt((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)
            if dist < speeds[i] + speeds[j] + 10:
                collision_count += 1

    # Mostrar colisiones detectadas
    drawn = 0
    for i in range(n):
        if drawn >= 3:
            break
        for j in range(i+1, n):
            if drawn >= 3:
                break
            dist = np.sqrt((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)
            if dist < 20:
                mid_x = (xs[i]+xs[j])/2
                mid_y = (xs[i]+ys[j])/2
                flash = plt.Circle((mid_x, mid_y), 5, color=C_YELLOW, alpha=0.3, zorder=8)
                ax.add_patch(flash)
                ax.plot([xs[i], xs[j]], [ys[i], ys[j]], color=C_YELLOW,
                        lw=1.5, alpha=0.6, linestyle="--", zorder=8)
                drawn += 1

    ax.text(50, 92, y_label, ha="center", fontsize=14, fontweight="bold",
            color=temp_color, fontfamily="monospace")
    ax.text(50, 10, f"Colisiones detectadas: ~{collision_count}",
            ha="center", fontsize=10, color=C_MUTED, fontfamily="monospace")

# ═════════════════════════════════════════════════════════════════════════════
# PASO 1: Temperatura BAJA
# ═════════════════════════════════════════════════════════════════════════════
draw_particles_with_speed(axes[0], n=8, speed_range=(3, 8), color=C_BLUE,
                          temp_label="T = 200K", y_label="T BAJA",
                          temp_color=C_BLUE)

# ═════════════════════════════════════════════════════════════════════════════
# PASO 2: Temperatura MEDIA
# ═════════════════════════════════════════════════════════════════════════════
draw_particles_with_speed(axes[1], n=8, speed_range=(8, 18), color=C_YELLOW,
                          temp_label="T = 400K", y_label="T MEDIA",
                          temp_color=C_YELLOW)

# ═════════════════════════════════════════════════════════════════════════════
# PASO 3: Temperatura ALTA
# ═════════════════════════════════════════════════════════════════════════════
draw_particles_with_speed(axes[2], n=8, speed_range=(18, 28), color=C_RED,
                          temp_label="T = 600K", y_label="T ALTA",
                          temp_color=C_RED)

# Título general
fig.suptitle("EFECTO DE LA TEMPERATURA: MOVIMIENTO Y ENERGÍA DE COLISIÓN",
             fontsize=20, fontweight="bold", color=C_WHITE, fontfamily="monospace", y=0.98)

# Pie de página con concepto clave
fig.text(0.5, 0.01,
         "E_kin = (3/2)RT    |    v_prom = \u221a(3RT/M)    |    Mayor T → Mayor v → Más colisiones + Mayor energía",
         ha="center", fontsize=11, color=C_YELLOW, fontfamily="monospace")

plt.tight_layout(rect=[0, 0.04, 1, 0.93])

out = BASE_DIR / "temperatura_3pasos.png"
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.savefig(BASE_DIR / "temperatura_3pasos.pdf", bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.close()
print(f"[OK] {out}")
