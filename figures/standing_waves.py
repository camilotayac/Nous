from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 3, figsize=(20, 10), facecolor="#0a0a1a")
fig.patch.set_facecolor("#0a0a1a")

L = 10  # longitud de la cuerda
x = np.linspace(0, L, 500)
n_modes = [1, 2, 3, 4, 5, 6]
colors = ["#4fc3f7", "#ef5350", "#ffd54f", "#ab47bc", "#66bb6a", "#ff7043"]

for idx, (ax, n, col) in enumerate(zip(axes.flat, n_modes, colors)):
    ax.set_facecolor("#0a0a1a")

    # Onda estacionaria: y(x,t) = A * sin(n*pi*x/L) * cos(wt)
    # Mostramos superposición de viaje y regreso
    y_envelope = np.sin(n * np.pi * x / L)

    # "Cuerda" con fill entre + y -
    ax.fill_between(x, y_envelope, -y_envelope, alpha=0.15, color=col)
    ax.plot(x, y_envelope, color=col, lw=2.5, label=f"n={n}")
    ax.plot(x, -y_envelope, color=col, lw=1.5, alpha=0.5, linestyle="--")

    # Nodos (puntos donde y=0 siempre)
    nodos_x = [i * L / n for i in range(n + 1)]
    ax.scatter(nodos_x, [0]*len(nodos_x), color="white", s=60, zorder=10, edgecolors=col, linewidth=2)

    # Antinodos (máximos)
    antinodos_x = [(2*i+1) * L / (2*n) for i in range(n)]
    antinodos_y = [1.0 if i % 2 == 0 else 1.0 for i in range(n)]
    ax.scatter(antinodos_x, antinodos_y, color=col, s=80, zorder=10, marker="D", edgecolors="white", linewidth=1.5)

    # Labels de nodos y antinodos
    for nx in nodos_x[1:-1]:
        ax.text(nx, -0.35, "N", ha="center", fontsize=9, color="white", alpha=0.7)

    ax.set_title(f"Arm. {n}  |  f{n} = {n}f1", fontsize=13, color=col, fontweight="bold", pad=8)
    ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color="#333333", lw=0.8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_color("#333333")

    # Longitud de onda
    if n <= 3:
        lambda_val = 2 * L / n
        ax.annotate("", xy=(lambda_val, 1.3), xytext=(0, 1.3),
                     arrowprops=dict(arrowstyle="<->", color=col, lw=1.5))
        ax.text(lambda_val/2, 1.4, f"$\\lambda_{{{n}}}$", ha="center", fontsize=12, color=col)

fig.suptitle("ONDAS ESTACIONARIAS EN CUERDA FIJA",
             fontsize=22, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

# Leyenda general
fig.text(0.5, 0.01, "N = Nodo (amplitud cero)    |    Diamante = Antinodo (amplitud max)    |    f_n = n * f_1",
         ha="center", fontsize=12, color="#888888", fontfamily="monospace")

plt.tight_layout(rect=[0, 0.04, 1, 0.94])
out_path = str(BASE_DIR / "standing_waves.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
