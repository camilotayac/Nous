from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20, 8), facecolor="#0a0a1a")

# ─── PANEL A: Curva Michaelis-Menten ────────────────────────────────────────
ax_a = fig.add_subplot(121, facecolor="#0a0a1a")

Vmax = 1.0
Km = 1.0

S = np.linspace(0, 10, 500)
v = (Vmax * S) / (Km + S)

ax_a.plot(S, v, color="#4fc3f7", lw=3, label="v = Vmax * [S] / (Km + [S])")

# Vmax line
ax_a.axhline(Vmax, color="#ef5350", lw=2, linestyle="--", alpha=0.8)
ax_a.text(10.2, Vmax, "Vmax", fontsize=13, color="#ef5350", va="center", fontweight="bold")

# Vmax/2 line
ax_a.axhline(Vmax/2, color="#ffd54f", lw=1.5, linestyle=":", alpha=0.7)
ax_a.text(10.2, Vmax/2, "Vmax/2", fontsize=12, color="#ffd54f", va="center")

# Km marker
ax_a.axvline(Km, color="#ffd54f", lw=1.5, linestyle=":", alpha=0.7)
ax_a.text(Km, -0.08, "Km", fontsize=13, color="#ffd54f", ha="center", fontweight="bold")

# Punto Km, Vmax/2
ax_a.scatter([Km], [Vmax/2], color="#ffd54f", s=120, zorder=10, edgecolors="white", linewidth=2)

# Regiones
ax_a.axvspan(0, Km, alpha=0.08, color="#4fc3f7")
ax_a.axvspan(Km, 10, alpha=0.08, color="#ef5350")
ax_a.text(0.5, 0.15, "Region\nprimer orden", fontsize=11, color="#4fc3f7", ha="center", alpha=0.8)
ax_a.text(6, 0.15, "Region\norden cero", fontsize=11, color="#ef5350", ha="center", alpha=0.8)

ax_a.set_xlabel("Concentracion de sustrato [S]", fontsize=14, color="white", fontfamily="monospace")
ax_a.set_ylabel("Velocidad de reaccion v", fontsize=14, color="white", fontfamily="monospace")
ax_a.set_title("Cinetica de Michaelis-Menten", fontsize=15, color="white", fontweight="bold", pad=12)
ax_a.legend(fontsize=11, loc="lower right", facecolor="#1a1a2e", edgecolor="#333333", labelcolor="white")
ax_a.set_xlim(0, 11)
ax_a.set_ylim(-0.05, 1.15)
ax_a.grid(True, alpha=0.15)
ax_a.tick_params(colors="#888888")
ax_a.spines[:].set_color("#333333")

# ─── PANEL B: Lineweaver-Burk ───────────────────────────────────────────────
ax_b = fig.add_subplot(122, facecolor="#0a0a1a")

# Lineweaver-Burk: 1/v = (Km/Vmax)(1/[S]) + 1/Vmax
S_lb = np.linspace(0.2, 5, 200)
v_lb = (Vmax * S_lb) / (Km + S_lb)
inv_S = 1 / S_lb
inv_v = 1 / v_lb

ax_b.plot(inv_S, inv_v, color="#ab47bc", lw=3, label="Lineweaver-Burk")

# Intercepto en y: 1/Vmax
ax_b.axhline(1/Vmax, color="#ef5350", lw=1, linestyle=":", alpha=0.5)
ax_b.text(-0.8, 1/Vmax, "1/Vmax", fontsize=12, color="#ef5350", va="center")

# Intercepto en x: -1/Km
ax_b.axvline(-1/Km, color="#4fc3f7", lw=1, linestyle=":", alpha=0.5)
ax_b.text(-1/Km, -0.3, "-1/Km", fontsize=12, color="#4fc3f7", ha="center")

# Puntos
ax_b.scatter(inv_S[::30], inv_v[::30], color="#ab47bc", s=40, zorder=10, alpha=0.8)

ax_b.set_xlabel("1/[S]", fontsize=14, color="white", fontfamily="monospace")
ax_b.set_ylabel("1/v", fontsize=14, color="white", fontfamily="monospace")
ax_b.set_title("Grafica Lineweaver-Burk (doble reciproco)", fontsize=15, color="white", fontweight="bold", pad=12)
ax_b.legend(fontsize=11, loc="upper left", facecolor="#1a1a2e", edgecolor="#333333", labelcolor="white")
ax_b.grid(True, alpha=0.15)
ax_b.tick_params(colors="#888888")
ax_b.spines[:].set_color("#333333")
ax_b.set_xlim(-2, 6)
ax_b.set_ylim(-0.5, 6)

fig.suptitle("CINETICA ENZIMATICA: MICHAELIS-MENTEN",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
out_path = str(BASE_DIR / "michaelis_menten.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
