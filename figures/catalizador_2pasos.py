from pathlib import Path
BASE_DIR = Path(__file__).parent

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

np.random.seed(42)

fig = plt.figure(figsize=(22, 9), facecolor="#0a0a1a")
fig.patch.set_facecolor("#0a0a1a")

C_BLUE = "#4fc3f7"
C_RED = "#ef5350"
C_YELLOW = "#ffd54f"
C_GREEN = "#66bb6a"
C_PURPLE = "#ab47bc"
C_WHITE = "#ffffff"
C_MUTED = "#888888"
C_DARK = "#0a0a1a"

# ═════════════════════════════════════════════════════════════════════════════
# PASO 1: SIN CATALIZADOR (ruta de alta energía)
# ═════════════════════════════════════════════════════════════════════════════
ax1 = fig.add_subplot(121, facecolor=C_DARK)

# Perfil de energía sinusoidal simulando ruta directa
x = np.linspace(0, 10, 500)

# Ruta SIN catalizador: barrera alta
E_reactivos = 0
E_productos = -3
Ea_sin = 8  # barrera alta

y_sin = np.where(x < 5,
                 E_reactivos + Ea_sin * np.sin(np.pi * x / 10) ** 2 * (1 + 0.5*np.sin(x*2)),
                 E_productos + (E_reactivos - E_productos) * (1 - (x-5)/5) ** 2)

# Simplificación: curva suave con barrera
x_curve = np.linspace(0, 10, 300)
y_curve = np.zeros_like(x_curve)
for i, xi in enumerate(x_curve):
    if xi < 5:
        # Subida hasta la barrera
        t = xi / 5
        y_curve[i] = E_reactivos + Ea_sin * np.sin(t * np.pi / 2) ** 1.5
    else:
        # Bajada hasta productos
        t = (xi - 5) / 5
        y_curve[i] = Ea_sin * (1 - t) ** 2 + E_productos * t

# Rellenar área bajo la curva
ax1.fill_between(x_curve, y_curve, alpha=0.1, color=C_RED)

# Curva principal
ax1.plot(x_curve, y_curve, color=C_RED, lw=3, label="Ruta SIN catalizador")

# Línea de reactivos
ax1.axhline(E_reactivos, xmin=0, xmax=0.35, color=C_BLUE, lw=2, linestyle="--", alpha=0.7)
ax1.text(0.5, E_reactivos + 0.3, "Reactivos (A + B)", fontsize=11,
         color=C_BLUE, fontweight="bold")

# Línea de productos
ax1.axhline(E_productos, xmin=0.65, xmax=1, color=C_GREEN, lw=2, linestyle="--", alpha=0.7)
ax1.text(7.5, E_productos + 0.3, "Productos (AB)", fontsize=11,
         color=C_GREEN, fontweight="bold")

# Flecha de barrera de energía (Ea)
peak_x = 5
peak_y = Ea_sin
ax1.annotate("", xy=(peak_x, peak_y + 0.5), xytext=(peak_x, E_reactivos - 0.5),
             arrowprops=dict(arrowstyle="<->", color=C_RED, lw=2.5))
ax1.text(peak_x + 0.3, (peak_y + E_reactivos) / 2, "Ea = ALTA",
         fontsize=13, color=C_RED, fontweight="bold", fontfamily="monospace")

# Delta G
ax1.annotate("", xy=(8, E_productos), xytext=(8, E_reactivos),
             arrowprops=dict(arrowstyle="<->", color=C_YELLOW, lw=1.5, alpha=0.6))
ax1.text(8.3, (E_reactivos + E_productos)/2, "\u0394G",
         fontsize=11, color=C_YELLOW, fontfamily="monospace")

# Label del paso
ax1.set_title("PASO 1: SIN CATALIZADOR", fontsize=16, color=C_RED,
              fontweight="bold", pad=15, fontfamily="monospace")
ax1.set_xlabel("Progreso de la reacción", fontsize=12, color=C_WHITE, fontfamily="monospace")
ax1.set_ylabel("Energía (kJ/mol)", fontsize=12, color=C_WHITE, fontfamily="monospace")
ax1.set_ylim(-5, 11)
ax1.set_xlim(-0.5, 10.5)
ax1.grid(True, alpha=0.1)
ax1.tick_params(colors=C_MUTED)
ax1.spines[:].set_color("#333333")

# Texto explicativo
ax1.text(5, -4, "La mayoría de moléculas\nNO tienen suficiente energía\npara superar la barrera",
         ha="center", fontsize=10, color=C_RED, alpha=0.8, fontfamily="monospace",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e", edgecolor=C_RED, alpha=0.7))

# ═════════════════════════════════════════════════════════════════════════════
# PASO 2: CON CATALIZADOR (ruta de menor energía)
# ═════════════════════════════════════════════════════════════════════════════
ax2 = fig.add_subplot(122, facecolor=C_DARK)

# Ruta CON catalizador: barrera reducida
Ea_con = 4  # barrera reducida a la mitad

y_con = np.zeros_like(x_curve)
for i, xi in enumerate(x_curve):
    if xi < 5:
        t = xi / 5
        y_con[i] = E_reactivos + Ea_con * np.sin(t * np.pi / 2) ** 1.5
    else:
        t = (xi - 5) / 5
        y_con[i] = Ea_con * (1 - t) ** 2 + E_productos * t

# Rellenar área bajo la curva del catalizador
ax2.fill_between(x_curve, y_con, alpha=0.1, color=C_GREEN)

# Mostrar ambas curvas para comparación
ax2.plot(x_curve, y_curve, color=C_RED, lw=2, linestyle=":", alpha=0.4,
         label="Sin catalizador (referencia)")
ax2.plot(x_curve, y_con, color=C_GREEN, lw=3, label="Con catalizador")

# Línea de reactivos
ax2.axhline(E_reactivos, xmin=0, xmax=0.35, color=C_BLUE, lw=2, linestyle="--", alpha=0.7)
ax2.text(0.5, E_reactivos + 0.3, "Reactivos (A + B)", fontsize=11,
         color=C_BLUE, fontweight="bold")

# Línea de productos (mismo nivel)
ax2.axhline(E_productos, xmin=0.65, xmax=1, color=C_GREEN, lw=2, linestyle="--", alpha=0.7)
ax2.text(7.5, E_productos + 0.3, "Productos (AB)", fontsize=11,
         color=C_GREEN, fontweight="bold")

# Flecha de barrera REDUCIDA
peak_x2 = 5
peak_y2 = Ea_con
ax2.annotate("", xy=(peak_x2, peak_y2 + 0.5), xytext=(peak_x2, E_reactivos - 0.5),
             arrowprops=dict(arrowstyle="<->", color=C_GREEN, lw=2.5))
ax2.text(peak_x2 + 0.3, (peak_y2 + E_reactivos) / 2, "Ea = BAJA",
         fontsize=13, color=C_GREEN, fontweight="bold", fontfamily="monospace")

# Flecha comparativa entre barreras
ax2.annotate("", xy=(3.5, peak_y2), xytext=(3.5, peak_y),
             arrowprops=dict(arrowstyle="<->", color=C_YELLOW, lw=2, alpha=0.7))
ax2.text(2.5, (peak_y + peak_y2)/2, "\u0394Ea\n(reducción)",
         fontsize=10, color=C_YELLOW, fontweight="bold", ha="center", fontfamily="monospace")

# Etiqueta del catalizador
ax2.text(5, 7, "\u26A1 CATALIZADOR \u26A1", ha="center", fontsize=12,
         color=C_PURPLE, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e", edgecolor=C_PURPLE, alpha=0.9))

# Label del paso
ax2.set_title("PASO 2: CON CATALIZADOR", fontsize=16, color=C_GREEN,
              fontweight="bold", pad=15, fontfamily="monospace")
ax2.set_xlabel("Progreso de la reacción", fontsize=12, color=C_WHITE, fontfamily="monospace")
ax2.set_ylabel("Energía (kJ/mol)", fontsize=12, color=C_WHITE, fontfamily="monospace")
ax2.set_ylim(-5, 11)
ax2.set_xlim(-0.5, 10.5)
ax2.grid(True, alpha=0.1)
ax2.tick_params(colors=C_MUTED)
ax2.spines[:].set_color("#333333")

# Texto explicativo
ax2.text(5, -4, "El catalizador ofrece una\nRUTA ALTERNATIVA con menor\nbarrera de energía (Ea menor)",
         ha="center", fontsize=10, color=C_GREEN, alpha=0.8, fontfamily="monospace",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1a2e", edgecolor=C_GREEN, alpha=0.7))

# Leyenda
ax2.legend(fontsize=10, loc="upper right", facecolor="#1a1a2e", edgecolor="#333333",
           labelcolor=C_WHITE)

# Título general
fig.suptitle("CATALIZADOR: CAMBIA LA RUTA, NO EL DESTINO",
             fontsize=20, fontweight="bold", color=C_WHITE, fontfamily="monospace", y=0.98)

fig.text(0.5, 0.01,
         "El catalizador reduce Ea pero NO cambia \u0394G (misma termodinámica)  |  Se regenera al final",
         ha="center", fontsize=11, color=C_PURPLE, fontfamily="monospace")

plt.tight_layout(rect=[0, 0.04, 1, 0.93])

out = BASE_DIR / "catalizador_2pasos.png"
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.savefig(BASE_DIR / "catalizador_2pasos.pdf", bbox_inches="tight", facecolor=C_DARK, edgecolor="none")
plt.close()
print(f"[OK] {out}")
