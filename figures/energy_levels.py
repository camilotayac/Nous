from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(20, 9), gridspec_kw={"width_ratios": [1.2, 1]})
fig.patch.set_facecolor("#0a0a1a")

# ─── PANEL A: Niveles de energía del Hidrógeno ──────────────────────────────
ax_a = axes[0]
ax_a.set_facecolor("#0a0a1a")
ax_a.set_xlim(0, 10)
ax_a.set_ylim(-14, 0.5)

# Niveles de energía: En = -13.6/n^2 eV
niveles = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85, 5: -0.54}
colors_niv = ["#ef5350", "#4fc3f7", "#ffd54f", "#ab47bc", "#66bb6a"]
color_map = {
    (2,1): "#4fc3f7",  # Lyman alpha (UV)
    (3,1): "#ef5350",  # Lyman beta
    (3,2): "#ffd54f",  # Balmer alpha (H-alpha, rojo)
    (4,2): "#ab47bc",  # Balmer beta
    (4,3): "#66bb6a",  # Paschen
}

for n, E in niveles.items():
    y = E
    ax_a.plot([1, 9], [y, y], color=colors_niv[n-1], lw=2.5, alpha=0.8)
    ax_a.text(0.3, y, f"n={n}", fontsize=12, color=colors_niv[n-1], va="center", fontweight="bold")
    ax_a.text(9.3, y, f"{E:.2f} eV", fontsize=11, color="#cccccc", va="center")

# Transiciones (flechas)
transiciones = [(2,1), (3,1), (3,2), (4,2), (4,3)]
for ni, nf in transiciones:
    Ei = niveles[ni]
    Ef = niveles[nf]
    delta_E = Ei - Ef
    color_t = color_map.get((ni, nf), "#ffffff")

    # Posición x aleatoria
    x_pos = 2.5 + (ni - 2) * 1.5 + (nf - 1) * 0.3

    ax_a.annotate("", xy=(x_pos, Ef + 0.3), xytext=(x_pos, Ei - 0.3),
                  arrowprops=dict(arrowstyle="->", color=color_t, lw=2.5))

    # Label de transición
    label_x = x_pos + 0.3
    label_y = (Ei + Ef) / 2
    ax_a.text(label_x, label_y, f"$\\Delta$E={delta_E:.2f}", fontsize=9, color=color_t, va="center")

# Línea de ionización
ax_a.axhline(0, color="#ffffff", lw=1, linestyle=":", alpha=0.5)
ax_a.text(5, 0.2, "Ionizacion (n=infinity)", ha="center", fontsize=11, color="#ffffff", alpha=0.7)

ax_a.set_ylabel("Energia (eV)", fontsize=14, color="white", fontfamily="monospace")
ax_a.set_title("Niveles de energia del Hidrogeno", fontsize=15, color="white", fontweight="bold", pad=12)
ax_a.tick_params(colors="#888888")
ax_a.spines[:].set_color("#333333")
ax_a.set_xticks([])

# ─── PANEL B: Serie espectrales ─────────────────────────────────────────────
ax_b = axes[1]
ax_b.set_facecolor("#0a0a1a")
ax_b.set_xlim(0, 10)
ax_b.set_ylim(-14, 0.5)

# Repetir niveles
for n, E in niveles.items():
    ax_b.plot([1, 9], [E, E], color=colors_niv[n-1], lw=2, alpha=0.5)

# Series espectrales
series_data = [
    {"name": "Lyman", "nf": 1, "color": "#ef5350", "range_n": [2,3,4,5], "region": "UV"},
    {"name": "Balmer", "nf": 2, "color": "#4fc3f7", "range_n": [3,4,5], "region": "Visible"},
    {"name": "Paschen", "nf": 3, "color": "#ffd54f", "range_n": [4,5], "region": "IR"},
]

for s_idx, series in enumerate(series_data):
    x_base = 2 + s_idx * 2.5
    for ni in series["range_n"]:
        Ei = niveles[ni]
        Ef = niveles[series["nf"]]
        x_pos = x_base + (ni - series["nf"]) * 0.4

        ax_b.annotate("", xy=(x_pos, Ef + 0.3), xytext=(x_pos, Ei - 0.3),
                      arrowprops=dict(arrowstyle="->", color=series["color"], lw=2))

    # Label de serie
    ax_b.text(x_base + 0.8, niveles[series["nf"]] - 0.8, 
              f"{series['name']}\n({series['region']})", 
              fontsize=10, color=series["color"], ha="center", fontweight="bold",
              bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a2e", edgecolor=series["color"], alpha=0.8))

ax_b.set_title("Series espectrales", fontsize=15, color="white", fontweight="bold", pad=12)
ax_b.set_xticks([])
ax_b.tick_params(colors="#888888")
ax_b.spines[:].set_color("#333333")

fig.suptitle("DIAGRAMA DE NIVELES DE ENERGIA - TRANSICIONES ATOMICAS",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
out_path = str(BASE_DIR / "energy_levels.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
