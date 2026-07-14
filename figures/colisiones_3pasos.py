from pathlib import Path
BASE_DIR = Path(__file__).parent

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, Arc

np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(22, 8), facecolor="#0a0a1a")
fig.patch.set_facecolor("#0a0a1a")

# Colores
C_BLUE = "#4fc3f7"
C_RED = "#ef5350"
C_YELLOW = "#ffd54f"
C_GREEN = "#66bb6a"
C_PURPLE = "#ab47bc"
C_WHITE = "#ffffff"
C_MUTED = "#888888"
C_DARK = "#0a0a1a"

# ═════════════════════════════════════════════════════════════════════════════
# PASO 1: Moléculas acercándose (antes de la colisión)
# ═════════════════════════════════════════════════════════════════════════════
ax1 = axes[0]
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.set_aspect("equal")
ax1.axis("off")
ax1.set_facecolor(C_DARK)

# Fondo del "recipiente"
recipiente = plt.Rectangle((5, 15), 90, 70, facecolor="#111122", edgecolor=C_MUTED,
                            linewidth=2, alpha=0.5, linestyle="--", zorder=1)
ax1.add_patch(recipiente)

# Molécula A (azul) moviéndose hacia la derecha
pos_a = (20, 55)
circle_a = plt.Circle(pos_a, 6, color=C_BLUE, alpha=0.9, zorder=5,
                       edgecolor="white", linewidth=2)
ax1.add_patch(circle_a)
ax1.text(pos_a[0], pos_a[1], "A", ha="center", va="center",
         fontsize=16, fontweight="bold", color="white", zorder=6)

# Flecha de movimiento A → derecha
ax1.annotate("", xy=(pos_a[0]+22, pos_a[1]), xytext=(pos_a[0]+8, pos_a[1]),
             arrowprops=dict(arrowstyle="->", color=C_BLUE, lw=2.5, alpha=0.8),
             zorder=4)
ax1.text(pos_a[0]+15, pos_a[1]+4, "v\u2081", fontsize=12, color=C_BLUE,
         fontweight="bold")

# Molécula B (roja) moviéndose hacia la izquierda
pos_b = (75, 50)
circle_b = plt.Circle(pos_b, 6, color=C_RED, alpha=0.9, zorder=5,
                       edgecolor="white", linewidth=2)
ax1.add_patch(circle_b)
ax1.text(pos_b[0], pos_b[1], "B", ha="center", va="center",
         fontsize=16, fontweight="bold", color="white", zorder=6)

# Flecha de movimiento B ← izquierda
ax1.annotate("", xy=(pos_b[0]-22, pos_b[1]), xytext=(pos_b[0]-8, pos_b[1]),
             arrowprops=dict(arrowstyle="->", color=C_RED, lw=2.5, alpha=0.8),
             zorder=4)
ax1.text(pos_b[0]-15, pos_b[1]+4, "v\u2082", fontsize=12, color=C_RED,
         fontweight="bold")

# Trayectorias punteadas (predicción)
t = np.linspace(0, 1, 50)
tray_a_x = pos_a[0] + 8 + t * 30
tray_a_y = pos_a[1] + np.sin(t * 2) * 1.5
tray_b_x = pos_b[0] - 8 - t * 30
tray_b_y = pos_b[1] + np.cos(t * 2.5) * 1.2

ax1.plot(tray_a_x, tray_a_y, color=C_BLUE, alpha=0.3, linestyle=":", lw=1.5, zorder=2)
ax1.plot(tray_b_x, tray_b_y, color=C_RED, alpha=0.3, linestyle=":", lw=1.5, zorder=2)

# Etiquetas de trayectoria
ax1.text(48, 62, "trayectoria", fontsize=9, color=C_MUTED, alpha=0.7, style="italic")

# Label del paso
ax1.text(50, 92, "PASO 1", ha="center", fontsize=14, fontweight="bold",
         color=C_YELLOW, fontfamily="monospace")
ax1.text(50, 87, "Acercamiento", ha="center", fontsize=12,
         color=C_WHITE, fontfamily="monospace")
ax1.text(50, 10, "Las moléculas se mueven\ny sus trayectorias se interceptan",
         ha="center", fontsize=10, color=C_MUTED, fontfamily="monospace")

# ═════════════════════════════════════════════════════════════════════════════
# PASO 2: Colisión (punto de máximo acercamiento)
# ═════════════════════════════════════════════════════════════════════════════
ax2 = axes[1]
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.set_aspect("equal")
ax2.axis("off")
ax2.set_facecolor(C_DARK)

# Recipiente
recipiente2 = plt.Rectangle((5, 15), 90, 70, facecolor="#111122", edgecolor=C_MUTED,
                              linewidth=2, alpha=0.5, linestyle="--", zorder=1)
ax2.add_patch(recipiente2)

# Moléculas en contacto (colisión)
pos_col = (50, 50)
# Molécula A (izquierda de la colisión)
circle_a2 = plt.Circle((pos_col[0]-5, pos_col[1]), 6, color=C_BLUE, alpha=0.9,
                         zorder=5, edgecolor="white", linewidth=2)
ax2.add_patch(circle_a2)
ax2.text(pos_col[0]-5, pos_col[1], "A", ha="center", va="center",
         fontsize=16, fontweight="bold", color="white", zorder=6)

# Molécula B (derecha de la colisión)
circle_b2 = plt.Circle((pos_col[0]+5, pos_col[1]), 6, color=C_RED, alpha=0.9,
                         zorder=5, edgecolor="white", linewidth=2)
ax2.add_patch(circle_b2)
ax2.text(pos_col[0]+5, pos_col[1], "B", ha="center", va="center",
         fontsize=16, fontweight="bold", color="white", zorder=6)

# Flash de colisión (múltiples anillos concéntricos)
for r, a in [(15, 0.15), (20, 0.1), (25, 0.05)]:
    flash = plt.Circle(pos_col, r, color=C_YELLOW, alpha=a, zorder=3)
    ax2.add_patch(flash)

# Líneas de fuerza (ondas de choque)
for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
    dx = np.cos(angle) * 14
    dy = np.sin(angle) * 14
    dx2 = np.cos(angle) * 18
    dy2 = np.sin(angle) * 18
    ax2.plot([pos_col[0]+dx, pos_col[0]+dx2], [pos_col[1]+dy, pos_col[1]+dy2],
             color=C_YELLOW, lw=1.5, alpha=0.5, zorder=4)

# Etiqueta de energía
ax2.text(pos_col[0], pos_col[1]+30, "E = \u00bdmv\u00b2", ha="center",
         fontsize=14, color=C_YELLOW, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e", edgecolor=C_YELLOW, alpha=0.9),
         zorder=7)

# Flechas de energía cinética (entrando)
ax2.annotate("", xy=(pos_col[0]-10, pos_col[1]), xytext=(pos_col[0]-25, pos_col[1]),
             arrowprops=dict(arrowstyle="->", color=C_BLUE, lw=2, alpha=0.6))
ax2.annotate("", xy=(pos_col[0]+10, pos_col[1]), xytext=(pos_col[0]+25, pos_col[1]),
             arrowprops=dict(arrowstyle="->", color=C_RED, lw=2, alpha=0.6))

# Ángulo de orientación
arc = Arc(pos_col, 10, 10, angle=0, theta1=30, theta2=150,
          color=C_GREEN, lw=2, linestyle="--", zorder=6)
ax2.add_patch(arc)
ax2.text(pos_col[0]-15, pos_col[1]+12, "\u03b8", fontsize=12, color=C_GREEN,
         fontweight="bold")

# Labels
ax2.text(50, 92, "PASO 2", ha="center", fontsize=14, fontweight="bold",
         color=C_YELLOW, fontfamily="monospace")
ax2.text(50, 87, "Colisión", ha="center", fontsize=12,
         color=C_WHITE, fontfamily="monospace")
ax2.text(50, 10, "Energía cinética se convierte en energía potencial\nOrientación correcta (\u03b8) necesaria para reaccionar",
         ha="center", fontsize=10, color=C_MUTED, fontfamily="monospace")

# ═════════════════════════════════════════════════════════════════════════════
# PASO 3: Resultado (reacción exitosa vs fallida)
# ═════════════════════════════════════════════════════════════════════════════
ax3 = axes[2]
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 100)
ax3.set_aspect("equal")
ax3.axis("off")
ax3.set_facecolor(C_DARK)

# Recipiente
recipiente3 = plt.Rectangle((5, 15), 90, 70, facecolor="#111122", edgecolor=C_MUTED,
                              linewidth=2, alpha=0.5, linestyle="--", zorder=1)
ax3.add_patch(recipiente3)

# ─── CASO A (arriba): COLISIÓN EXITOSA → REACCIÓN ──────────────────────────
# Producto AB (verde, nuevo enlace)
pos_prod = (35, 65)
circle_prod = plt.Circle(pos_prod, 7, color=C_GREEN, alpha=0.9, zorder=5,
                          edgecolor="white", linewidth=2)
ax3.add_patch(circle_prod)
ax3.text(pos_prod[0]-2, pos_prod[1], "A", ha="center", va="center",
         fontsize=11, fontweight="bold", color="white", zorder=6)
ax3.text(pos_prod[0]+3, pos_prod[1], "B", ha="center", va="center",
         fontsize=11, fontweight="bold", color="white", zorder=6)

# Enlace A-B
ax3.plot([pos_prod[0]-1, pos_prod[0]+1], [pos_prod[1], pos_prod[1]],
         color="white", lw=3, zorder=6)

# Flash de éxito
flash_ok = plt.Circle(pos_prod, 12, color=C_GREEN, alpha=0.15, zorder=3)
ax3.add_patch(flash_ok)

# Check mark
ax3.text(pos_prod[0]+12, pos_prod[1]+8, "\u2713", fontsize=20, color=C_GREEN,
         fontweight="bold", zorder=7)

# Label
ax3.text(20, 78, "COLISIÓN EXITOSA", ha="center", fontsize=11,
         color=C_GREEN, fontweight="bold", fontfamily="monospace")
ax3.text(20, 74, "E \u2265 Ea  +  \u03b8 correcto", ha="center", fontsize=9,
         color=C_GREEN, fontfamily="monospace")
ax3.text(20, 70, "→ Producto AB formado", ha="center", fontsize=9,
         color=C_GREEN, fontfamily="monospace")

# ─── CASO B (abajo): COLISIÓN FALLIDA → REBOTE ─────────────────────────────
# Moléculas rebotando (separándose)
pos_a3 = (30, 40)
pos_b3 = (40, 38)

circle_a3 = plt.Circle(pos_a3, 5, color=C_BLUE, alpha=0.7, zorder=5,
                         edgecolor="white", linewidth=1.5)
ax3.add_patch(circle_a3)
ax3.text(pos_a3[0], pos_a3[1], "A", ha="center", va="center",
         fontsize=12, fontweight="bold", color="white", zorder=6)

circle_b3 = plt.Circle(pos_b3, 5, color=C_RED, alpha=0.7, zorder=5,
                         edgecolor="white", linewidth=1.5)
ax3.add_patch(circle_b3)
ax3.text(pos_b3[0], pos_b3[1], "B", ha="center", va="center",
         fontsize=12, fontweight="bold", color="white", zorder=6)

# Flechas de rebote (opuestas)
ax3.annotate("", xy=(pos_a3[0]-15, pos_a3[1]-3), xytext=(pos_a3[0]-7, pos_a3[1]),
             arrowprops=dict(arrowstyle="->", color=C_BLUE, lw=2, alpha=0.6))
ax3.annotate("", xy=(pos_b3[0]+15, pos_b3[1]+3), xytext=(pos_b3[0]+7, pos_b3[1]),
             arrowprops=dict(arrowstyle="->", color=C_RED, lw=2, alpha=0.6))

# X mark de fallo
ax3.text(55, 39, "\u2717", fontsize=20, color=C_RED, fontweight="bold", zorder=7)

# Label
ax3.text(20, 52, "COLISIÓN FALLIDA", ha="center", fontsize=11,
         color=C_RED, fontweight="bold", fontfamily="monospace")
ax3.text(20, 48, "E < Ea  o  \u03b8 incorrecto", ha="center", fontsize=9,
         color=C_RED, fontfamily="monospace")
ax3.text(20, 44, "→ Las moléculas rebotan", ha="center", fontsize=9,
         color=C_RED, fontfamily="monospace")

# Labels generales
ax3.text(50, 92, "PASO 3", ha="center", fontsize=14, fontweight="bold",
         color=C_YELLOW, fontfamily="monospace")
ax3.text(50, 87, "Resultado", ha="center", fontsize=12,
         color=C_WHITE, fontfamily="monospace")

# Separador
ax3.plot([10, 90], [60, 60], color=C_MUTED, lw=1, linestyle=":", alpha=0.4)

fig.suptitle("TEORÍA DE COLISIONES: 3 PASOS PARA UNA REACCIÓN",
             fontsize=20, fontweight="bold", color=C_WHITE, fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])

out = BASE_DIR / "colisiones_3pasos.png"
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.savefig(BASE_DIR / "colisiones_3pasos.pdf", bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.close()
print(f"[OK] {out}")
