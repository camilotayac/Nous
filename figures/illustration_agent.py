#!/usr/bin/env python3
"""
AGENTE ITERATIVO DE ILUSTRACIÓN CIENTÍFICA
============================================
Bucle infinito que crea ilustraciones, evalúa calidad, y guarda estilo
hasta que 5 iteraciones consecutivas no encuentren mejoras.

Filosofía:
- Tufte: maximizar data-ink ratio
- Feynman: explicar lo complejo de forma simple
- Gestalt: proximidad, similitud, continuidad
- Cognitive Load: dual coding, segmentación
- Accessibility: contraste WCAG AA

Herramientas: matplotlib, tikz, manim, plotly, d3 (vía subagente)
"""

import json
import os
import sys
import time
import subprocess
import textwrap
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import importlib

import numpy as np

# ─── CONFIGURACIÓN ───────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
STYLE_MEMORY_PATH = BASE_DIR / "style_memory.json"
OUTPUT_DIR = BASE_DIR / "iterations"
OUTPUT_DIR.mkdir(exist_ok=True)

# Catálogo de ilustraciones por crear
ILLUSTRATION_CATALOG = [
    {
        "id": "conc_colisiones",
        "title": "Concentración y colisiones moleculares",
        "subject": "quimica",
        "concept": "Relación entre concentración y frecuencia de choques",
        "tool_preference": ["matplotlib", "manim"],
        "target_audience": "universitario",
        "status": "completed",
        "path": "concentration_diagram.py"
    },
    {
        "id": "Ley_coulomb",
        "title": "Ley de Coulomb - Fuerza entre cargas",
        "subject": "fisica",
        "concept": "Fuerza electrostática proporcional al producto de cargas e inversamente al cuadrado de la distancia",
        "tool_preference": ["matplotlib", "tikz"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "orbital_hibridacion",
        "title": "Hibridación de orbitales sp3",
        "subject": "quimica",
        "concept": "Forma de orbitales híbridos y geometría tetraédrica",
        "tool_preference": ["matplotlib", "manim"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "onda_estacionaria",
        "title": "Ondas estacionarias en cuerdas",
        "subject": "fisica",
        "concept": "Armónicos, nodos y antinodos",
        "tool_preference": ["matplotlib", "manim"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "energia_niveles",
        "title": "Diagrama de niveles de energía",
        "subject": "quimica",
        "concept": "Transiciones electrónicas y emisión/absorción de fotones",
        "tool_preference": ["matplotlib"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "circuito_rc",
        "title": "Circuito RC - Carga y descarga",
        "subject": "fisica",
        "concept": "Curva exponencial de carga/descarga del capacitor",
        "tool_preference": ["matplotlib", "tikz"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "cinetica_enzimatica",
        "title": "Cinética enzimática Michaelis-Menten",
        "subject": "bioquimica",
        "concept": "Velocidad vs concentración de sustrato",
        "tool_preference": ["matplotlib"],
        "target_audience": "universitario",
        "status": "pending"
    },
    {
        "id": "estructura_atomo",
        "title": "Modelo atómico cuántico",
        "subject": "quimica",
        "concept": "Nubes de probabilidad y números cuánticos",
        "tool_preference": ["matplotlib", "manim"],
        "target_audience": "divulgacion",
        "status": "pending"
    },
]

# ─── UTILIDADES ──────────────────────────────────────────────────────────────

def load_style_memory() -> dict:
    with open(STYLE_MEMORY_PATH, "r") as f:
        return json.load(f)

def save_style_memory(memory: dict):
    with open(STYLE_MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)
    print(f"  [memory] Guardado style_memory.json (v{memory['version']})")

def log_iteration(memory: dict, iteration: int, result: dict):
    entry = {
        "iteration": iteration,
        "timestamp": datetime.now().isoformat(),
        "tool_used": result["tool"],
        "illustration_id": result["illustration_id"],
        "score": result["score"],
        "improvements": result.get("improvements", []),
        "new_learning": result.get("new_learning", ""),
        "file_path": result.get("file_path", ""),
    }
    memory["iterations_log"].append(entry)
    memory["convergence"]["total_iterations"] = iteration

    if result["score"] > memory["convergence"]["best_score_ever"]:
        memory["convergence"]["best_score_ever"] = result["score"]
        memory["convergence"]["consecutive_no_improvement"] = 0
    else:
        memory["convergence"]["consecutive_no_improvement"] += 1

def select_tool(illustration: dict, memory: dict) -> str:
    """Selecciona la mejor herramienta según el catálogo y aprendizaje previo.
    Si el tool seleccionado no tiene generador, cae en matplotlib."""
    candidates = illustration["tool_preference"]
    tool_scores = {}
    for tool in candidates:
        if tool in memory["tool_catalog"]:
            base_score = memory["tool_catalog"][tool]["score"]
            subj = illustration["subject"]
            if subj in memory["learning"]["preferred_tools_per_subject"]:
                prefs = memory["learning"]["preferred_tools_per_subject"][subj]
                if tool in prefs:
                    base_score += prefs[tool] * 0.5
            tool_scores[tool] = base_score
    best = max(tool_scores, key=tool_scores.get)
    
    # Verificar que existe generador; si no, fallback a matplotlib
    gen_key = (best, illustration["id"])
    if gen_key not in GENERATORS and best != "matplotlib":
        fallback_key = ("matplotlib", illustration["id"])
        if fallback_key in GENERATORS:
            print(f"  [tool] {best} sin generador para '{illustration['id']}', fallback a matplotlib")
            best = "matplotlib"
    
    print(f"  [tool] Seleccionado: {best} (score: {tool_scores.get(best, 0):.1f})")
    return best

# ─── GENERADORES POR HERRAMIENTA ────────────────────────────────────────────

def _script_header():
    """Retorna el header común para todos los scripts generados."""
    return "from pathlib import Path\nBASE_DIR = Path(__file__).parent\n\n"

def generate_matplotlib_coulomb(memory: dict) -> str:
    """Genera diagrama de Ley de Coulomb con matplotlib."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "coulomb_law.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "coulomb_law.png")


def generate_matplotlib_orbitals(memory: dict) -> str:
    """Genera diagrama de hibridación sp3 con matplotlib."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "orbital_hybridization.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "orbital_hybridization.png")


def generate_matplotlib_ondas(memory: dict) -> str:
    """Genera diagrama de ondas estacionarias."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "standing_waves.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "standing_waves.png")


def generate_matplotlib_niveles(memory: dict) -> str:
    """Genera diagrama de niveles de energía atómicos."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "energy_levels.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "energy_levels.png")


def generate_matplotlib_circuito_rc(memory: dict) -> str:
    """Genera diagrama de circuito RC con curvas de carga/descarga."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "circuito_rc.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "circuito_rc.png")


def generate_matplotlib_michaelis_menten(memory: dict) -> str:
    """Genera cinética enzimática Michaelis-Menten."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "michaelis_menten.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "michaelis_menten.png")


def generate_matplotlib_cuantico(memory: dict) -> str:
    """Genera modelo atómico cuántico (nubes de probabilidad)."""
    code = _script_header() + textwrap.dedent(r'''
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
''')
    code_path = BASE_DIR / "quantum_atom.py"
    with open(code_path, "w") as f:
        f.write(code)
    subprocess.run(["python3", str(code_path)], check=True)
    return str(BASE_DIR / "quantum_atom.png")


# Mapa de generadores por tool + illustration_id
GENERATORS = {
    ("matplotlib", "Ley_coulomb"): generate_matplotlib_coulomb,
    ("matplotlib", "orbital_hibridacion"): generate_matplotlib_orbitals,
    ("matplotlib", "onda_estacionaria"): generate_matplotlib_ondas,
    ("matplotlib", "energia_niveles"): generate_matplotlib_niveles,
    ("matplotlib", "circuito_rc"): generate_matplotlib_circuito_rc,
    ("matplotlib", "cinetica_enzimatica"): generate_matplotlib_michaelis_menten,
    ("matplotlib", "estructura_atomo"): generate_matplotlib_cuantico,
}

# ─── EVALUACIÓN ──────────────────────────────────────────────────────────────

def evaluate_illustration(file_path: str, illustration: dict, iteration: int, memory: dict) -> dict:
    """Evalúa la ilustración generada con métricas heurísticas."""
    score = 0
    improvements = []
    new_learning = ""
    
    # 1. Existe el archivo
    if os.path.exists(file_path):
        score += 2
        size_kb = os.path.getsize(file_path) / 1024
        if size_kb > 50:
            score += 1  # Contenido sustancial
            improvements.append(f"Archivo sustancial ({size_kb:.0f} KB)")
    
    # 2. PDF también generado
    pdf_path = file_path.replace(".png", ".pdf")
    if os.path.exists(pdf_path):
        score += 1
        improvements.append("Exportado en PNG y PDF (vectorial)")
    
    # 3. Código Python generado
    py_path = file_path.replace(".png", ".py")
    if os.path.exists(py_path):
        with open(py_path) as f:
            code = f.read()
        lines = len(code.split("\n"))
        score += min(lines // 50, 3)  # Hasta 3 puntos por complejidad
        improvements.append(f"Código: {lines} líneas")
    
    # 4. Filosofía Tufte: data-ink ratio
    if "ax.axis" in code or "ax.set_xticks([])" in code:
        score += 1
        improvements.append("Tufte: ejes minimizados")
    
    # 5. Dual coding: texto + visual
    if "ax.text" in code and ("plt.Circle" in code or "ax.plot" in code or "ax.scatter" in code):
        score += 1
        improvements.append("Dual coding: texto + elementos visuales")
    
    # 6. Paleta limitada
    color_count = code.count("#") // 2  # simplificado
    if color_count <= 15:
        score += 1
        improvements.append("Paleta de colores coherente")
    
    # 7. Fondo oscuro consistente
    if '#0a0a1a' in code:
        score += 1
        improvements.append("Fondo oscuro consistente")
    
    # 8. Múltiples paneles
    if "subplots" in code:
        score += 1
        improvements.append("Múltiples paneles para comparación")
    
    # 9. Tipografía monospace
    if "fontfamily" in code and "monospace" in code:
        score += 1
        improvements.append("Tipografía monospace para labels científicos")
    
    # 10. Anotaciones y labels detallados
    annotation_count = code.count("ax.text") + code.count("ax_a.text") + code.count("ax_b.text")
    if annotation_count >= 10:
        score += 1
        improvements.append(f"Rico en anotaciones ({annotation_count} textos)")
    
    # Bonus por iteración (exploración)
    if iteration <= 3:
        score += 1
        improvements.append("Iteración temprana: exploración de estilo")
    
    # Bonus por herramienta nueva
    tool = illustration["tool_preference"][0]
    if tool not in memory["learning"]["preferred_tools_per_subject"].get(illustration["subject"], {}):
        score += 1
        new_learning = f"Herramienta {tool} probada por primera vez para {illustration['subject']}"
        improvements.append(new_learning)
    
    # Aprendizaje
    if illustration["subject"] not in memory["learning"]["preferred_tools_per_subject"]:
        memory["learning"]["preferred_tools_per_subject"][illustration["subject"]] = {}
    tool_prefs = memory["learning"]["preferred_tools_per_subject"][illustration["subject"]]
    if tool not in tool_prefs:
        tool_prefs[tool] = 0
    tool_prefs[tool] += 1
    
    return {
        "score": score,
        "max_score": 12,
        "improvements": improvements,
        "new_learning": new_learning,
    }


# ─── BUCLE PRINCIPAL ────────────────────────────────────────────────────────

def run_agent_loop():
    print("=" * 70)
    print("  AGENTE ITERATIVO DE ILUSTRACION CIENTIFICA")
    print("  Filosofia: Tufte + Feynman + Gestalt + Cognitive Load")
    print("=" * 70)
    
    memory = load_style_memory()
    max_iter = memory["convergence"]["max_iterations"]
    convergence_threshold = memory["convergence"]["convergence_threshold"]
    
    # Filtrar ilustraciones pendientes
    pending = [ill for ill in ILLUSTRATION_CATALOG if ill["status"] == "pending"]
    
    if not pending:
        print("\n  [!] No hay ilustraciones pendientes en el catálogo.")
        print("  Agregando ilustraciones de ejemplo...")
        pending = ILLUSTRATION_CATALOG[:3]  # Usar las primeras 3
    
    iteration = memory["convergence"]["total_iterations"]
    illustrated_ids = set()
    
    while iteration < max_iter:
        iteration += 1
        print(f"\n{'─' * 60}")
        print(f"  ITERACION {iteration}/{max_iter}")
        print(f"  Consecutivas sin mejora: {memory['convergence']['consecutive_no_improvement']}/{convergence_threshold}")
        print(f"{'─' * 60}")
        
        # Seleccionar siguiente ilustración (round-robin)
        remaining = [ill for ill in pending if ill["id"] not in illustrated_ids]
        if not remaining:
            # Si ya iluminamos todas, permitir repetir con mejoras
            remaining = pending
        
        illustration = remaining[iteration % len(remaining)]
        print(f"\n  [topic] {illustration['title']}")
        print(f"  [subject] {illustration['subject']} | [audience] {illustration['target_audience']}")
        
        # Seleccionar herramienta
        tool = select_tool(illustration, memory)
        
        # Generar
        gen_key = (tool, illustration["id"])
        if gen_key not in GENERATORS:
            print(f"  [!] No hay generador para {tool} + {illustration['id']}. Saltando...")
            illustrated_ids.add(illustration["id"])
            continue
        
        print(f"  [generando] Usando {tool}...")
        try:
            file_path = GENERATORS[gen_key](memory)
            print(f"  [ok] Ilustración generada: {file_path}")
        except Exception as e:
            print(f"  [ERROR] Falló la generación: {e}")
            memory["convergence"]["consecutive_no_improvement"] += 1
            memory["learning"]["failed_approaches"].append({
                "tool": tool,
                "illustration_id": illustration["id"],
                "error": str(e),
                "iteration": iteration,
            })
            illustrated_ids.add(illustration["id"])
            continue
        
        # Evaluar
        result = evaluate_illustration(file_path, illustration, iteration, memory)
        result["tool"] = tool
        result["illustration_id"] = illustration["id"]
        result["file_path"] = file_path
        
        print(f"\n  [score] {result['score']}/{result['max_score']}")
        for imp in result["improvements"]:
            print(f"    + {imp}")
        
        # Guardar en memoria
        log_iteration(memory, iteration, result)
        illustrated_ids.add(illustration["id"])
        
        # Guardar improved learning
        if result["new_learning"]:
            memory["learning"]["common_improvements"].append(result["new_learning"])
        
        # Actualizar score del tool en catálogo
        if tool in memory["tool_catalog"]:
            memory["tool_catalog"][tool]["score"] = min(10, memory["tool_catalog"][tool]["score"] + 0.1)
        
        save_style_memory(memory)
        
        # Check convergencia
        no_improve = memory["convergence"]["consecutive_no_improvement"]
        print(f"\n  [convergencia] {no_improve}/{convergence_threshold} iteraciones sin mejora")
        
        if no_improve >= convergence_threshold:
            print(f"\n{'=' * 70}")
            print(f"  CONVERGENCIA ALCANZADA en {iteration} iteraciones")
            print(f"  Mejor score: {memory['convergence']['best_score_ever']}/{result['max_score']}")
            print(f"{'=' * 70}")
            break
    
    # Resumen final
    print(f"\n{'=' * 70}")
    print(f"  RESUMEN FINAL")
    print(f"{'=' * 70}")
    print(f"  Iteraciones totales: {iteration}")
    print(f"  Mejor score: {memory['convergence']['best_score_ever']}")
    print(f"  Herramientas probadas: {len(memory['learning']['preferred_tools_per_subject'])}")
    print(f"  Fallos registrados: {len(memory['learning']['failed_approaches'])}")
    print(f"  Archivos generados:")
    for entry in memory["iterations_log"]:
        if entry.get("file_path"):
            print(f"    [{entry['iteration']}] {entry['file_path']}")
    print(f"\n  Style memory guardado en: {STYLE_MEMORY_PATH}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    run_agent_loop()
