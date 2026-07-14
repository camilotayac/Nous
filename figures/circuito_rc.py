from pathlib import Path
BASE_DIR = Path(__file__).parent


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20, 8), facecolor="#0a0a1a")

# ─── PANEL A: Circuito esquemático ──────────────────────────────────────────
ax_a = fig.add_subplot(131, facecolor="#0a0a1a")
ax_a.set_xlim(0, 10)
ax_a.set_ylim(0, 8)
ax_a.axis("off")

# Batería
ax_a.plot([1, 1], [2, 6], color="#4fc3f7", lw=3)
ax_a.plot([1.5, 1.5], [2.5, 5.5], color="#4fc3f7", lw=3)
ax_a.text(0.5, 4, "V", fontsize=14, color="#4fc3f7", fontweight="bold")

# Cable superior
ax_a.plot([1, 9], [6, 6], color="#888888", lw=2)

# Resistencia (zigzag simplificado)
r_x = np.array([3, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
r_y = np.array([6, 7, 5, 7, 5, 7, 5, 7, 5, 7, 6])
ax_a.plot(r_x, r_y, color="#ffd54f", lw=2.5)
ax_a.text(4, 7.5, "R", fontsize=14, color="#ffd54f", fontweight="bold", ha="center")

# Capacitor
ax_a.plot([7, 7], [6, 5.2], color="#888888", lw=2)
ax_a.plot([6.5, 7.5], [5.2, 5.2], color="#ef5350", lw=4)
ax_a.plot([6.5, 7.5], [4.5, 4.5], color="#ef5350", lw=4)
ax_a.plot([7, 7], [4.5, 3.8], color="#888888", lw=2)
ax_a.text(8, 4.85, "C", fontsize=14, color="#ef5350", fontweight="bold")

# Cable inferior
ax_a.plot([1, 7], [2, 2], color="#888888", lw=2)
ax_a.plot([7, 7], [3.8, 2], color="#888888", lw=2)

# Corriente
ax_a.annotate("", xy=(8, 6.3), xytext=(6, 6.3),
              arrowprops=dict(arrowstyle="->", color="#ab47bc", lw=2))
ax_a.text(7, 6.5, "i(t)", fontsize=12, color="#ab47bc", fontweight="bold")

# Voltaje en C
ax_a.annotate("", xy=(7.8, 4.85), xytext=(7.8, 3.5),
              arrowprops=dict(arrowstyle="<->", color="#ef5350", lw=2))
ax_a.text(8.5, 4.2, "Vc(t)", fontsize=12, color="#ef5350", fontweight="bold")

ax_a.set_title("Circuito RC", fontsize=15, color="white", fontweight="bold", pad=12)

# ─── PANEL B: Curvas de carga y descarga ─────────────────────────────────────
ax_b = fig.add_subplot(122, facecolor="#0a0a1a")

tau = 1.0  # constante de tiempo RC
V0 = 1.0   # voltaje de la batería

t_charge = np.linspace(0, 5*tau, 500)
t_discharge = np.linspace(0, 5*tau, 500)

V_charge = V0 * (1 - np.exp(-t_charge / tau))
V_discharge = V0 * np.exp(-t_discharge / tau)

i_charge = (V0 / tau) * np.exp(-t_charge / tau) * tau  # simplificado
i_discharge = -(V0 / tau) * np.exp(-t_discharge / tau) * tau

# Carga
ax_b.plot(t_charge/tau, V_charge, color="#4fc3f7", lw=3, label="Carga: Vc(t) = V0(1 - e^(-t/RC))")
ax_b.plot(t_charge/tau, i_charge, color="#ab47bc", lw=2, linestyle="--", alpha=0.7, label="Corriente i(t) carga")

# Descarga
ax_b.plot(t_discharge/tau, V_discharge, color="#ef5350", lw=3, label="Descarga: Vc(t) = V0 * e^(-t/RC)")
ax_b.plot(t_discharge/tau, -i_discharge, color="#ff7043", lw=2, linestyle="--", alpha=0.7, label="Corriente i(t) descarga")

# tau marker
ax_b.axvline(1.0, color="#ffd54f", lw=1.5, linestyle=":", alpha=0.8)
ax_b.text(1.05, 0.55, "$\\tau$ = RC\n(63.2%)", fontsize=12, color="#ffd54f", fontweight="bold")

# 5tau marker
ax_b.axvline(5.0, color="#66bb6a", lw=1.5, linestyle=":", alpha=0.6)
ax_b.text(5.05, 0.35, "5$\\tau$\n(99.3%)", fontsize=11, color="#66bb6a")

ax_b.set_xlabel("Tiempo (unidades de $\\tau$ = RC)", fontsize=13, color="white", fontfamily="monospace")
ax_b.set_ylabel("Voltaje / Corriente (normalizado)", fontsize=13, color="white", fontfamily="monospace")
ax_b.set_title("Respuesta temporal del circuito RC", fontsize=15, color="white", fontweight="bold", pad=12)
ax_b.legend(fontsize=10, loc="center right", facecolor="#1a1a2e", edgecolor="#333333", labelcolor="white")
ax_b.set_ylim(-0.2, 1.15)
ax_b.grid(True, alpha=0.15)
ax_b.tick_params(colors="#888888")
ax_b.spines[:].set_color("#333333")

fig.suptitle("CIRCUITO RC: CARGA Y DESCARGA DEL CAPACITOR",
             fontsize=20, fontweight="bold", color="white", fontfamily="monospace", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
out_path = str(BASE_DIR / "circuito_rc.png")
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.savefig(out_path.replace(".png", ".pdf"), bbox_inches="tight", facecolor="#0a0a1a", edgecolor="none")
plt.close()
print(f"[matplotlib] Guardado: {out_path}")
