import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc
from matplotlib.collections import PatchCollection

np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(22, 9), gridspec_kw={'width_ratios': [1, 1, 0.8]})
fig.patch.set_facecolor('#0a0a1a')

def draw_flask(ax, x_center, y_bottom, width, height, color_liquid, alpha_liquid=0.25):
    """Draw an Erlenmeyer flask shape"""
    neck_w = width * 0.15
    neck_h = height * 0.30
    body_h = height * 0.70
    
    # Flask body (trapezoid → rounded)
    body_x = [x_center - width/2, x_center + width/2,
              x_center + neck_w, x_center - neck_w]
    body_y = [y_bottom, y_bottom, y_bottom + body_h, y_bottom + body_h]
    
    from matplotlib.patches import Polygon
    flask_body = Polygon(list(zip(body_x, body_y)), closed=True,
                         facecolor=color_liquid, edgecolor='#c0c0c0',
                         linewidth=2.5, alpha=alpha_liquid, zorder=2)
    ax.add_patch(flask_body)
    
    # Flask outline
    outline = Polygon(list(zip(body_x, body_y)), closed=True,
                      facecolor='none', edgecolor='#c0c0c0',
                      linewidth=2.5, zorder=5)
    ax.add_patch(outline)
    
    # Neck
    neck_rect = plt.Rectangle((x_center - neck_w, y_bottom + body_h),
                               neck_w*2, neck_h,
                               facecolor=color_liquid, edgecolor='#c0c0c0',
                               linewidth=2.5, alpha=alpha_liquid, zorder=2)
    ax.add_patch(neck_rect)
    neck_outline = plt.Rectangle((x_center - neck_w, y_bottom + body_h),
                                  neck_w*2, neck_h,
                                  facecolor='none', edgecolor='#c0c0c0',
                                  linewidth=2.5, zorder=5)
    ax.add_patch(neck_outline)
    
    # Rim at top
    rim = plt.Rectangle((x_center - neck_w*1.4, y_bottom + height - 2),
                         neck_w*2.8, 4,
                         facecolor='#808080', edgecolor='#a0a0a0',
                         linewidth=1.5, zorder=6)
    ax.add_patch(rim)
    
    return {
        'x_center': x_center,
        'y_bottom': y_bottom,
        'body_h': body_h,
        'neck_h': neck_h,
        'width': width,
        'neck_w': neck_w,
        'body_top': y_bottom + body_h,
        'top': y_bottom + height
    }


def draw_particles_and_arrows(ax, flask_info, n_particles, particle_color,
                               speed_label, collision_zone=False):
    """Place particles with velocity arrows and optional collision highlight"""
    xc = flask_info['x_center']
    yb = flask_info['y_bottom']
    bh = flask_info['body_h']
    w = flask_info['width']
    
    # Place particles randomly inside the flask body
    xs = np.random.uniform(xc - w*0.38, xc + w*0.38, n_particles)
    ys = np.random.uniform(yb + 5, yb + bh - 8, n_particles)
    
    # Draw particles
    for i in range(n_particles):
        # Glow effect
        glow = plt.Circle((xs[i], ys[i]), 4.5, color=particle_color, alpha=0.15, zorder=3)
        ax.add_patch(glow)
        # Main particle
        particle = plt.Circle((xs[i], ys[i]), 3, color=particle_color,
                               alpha=0.9, zorder=7, edgecolor='white', linewidth=0.5)
        ax.add_patch(particle)
    
    # Draw velocity arrows
    angles = np.random.uniform(0, 2*np.pi, n_particles)
    arrow_lengths = np.random.uniform(12, 25, n_particles)
    
    for i in range(n_particles):
        dx = arrow_lengths[i] * np.cos(angles[i])
        dy = arrow_lengths[i] * np.sin(angles[i])
        ax.annotate('', xy=(xs[i] + dx, ys[i] + dy), xytext=(xs[i], ys[i]),
                     arrowprops=dict(arrowstyle='->', color='#ffffff',
                                     lw=1.2, alpha=0.5), zorder=6)
    
    # Collision zones (draw X marks on nearby particles)
    if collision_zone and n_particles > 3:
        drawn = 0
        for i in range(n_particles):
            if drawn >= 4:
                break
            for j in range(i+1, n_particles):
                dist = np.sqrt((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)
                if dist < 20:
                    # Draw collision flash
                    mid_x = (xs[i] + xs[j]) / 2
                    mid_y = (ys[i] + ys[j]) / 2
                    flash = plt.Circle((mid_x, mid_y), 7, color='#ffff00', alpha=0.35, zorder=8)
                    ax.add_patch(flash)
                    ax.plot([xs[i], xs[j]], [ys[i], ys[j]], 
                            color='#ffff00', lw=2, alpha=0.7, zorder=8,
                            linestyle='--')
                    drawn += 1
                    break
    
    return xs, ys


# ========== PANEL A: BAJA CONCENTRACIÓN ==========
ax_a = axes[0]
ax_a.set_xlim(0, 100)
ax_a.set_ylim(0, 130)
ax_a.set_aspect('equal')
ax_a.axis('off')
ax_a.set_facecolor('#0a0a1a')

flask_a = draw_flask(ax_a, 50, 8, 80, 100, '#1a3a5c', 0.30)
n_a = 6
xs_a, ys_a = draw_particles_and_arrows(ax_a, flask_a, n_a, '#4fc3f7', 'lento',
                                         collision_zone=False)

# Label
ax_a.text(50, 126, 'A. BAJA CONCENTRACIÓN', ha='center', va='top',
          fontsize=15, fontweight='bold', color='#4fc3f7',
          fontfamily='monospace')
ax_a.text(50, 5, f'n = {n_a} particulas en 1 L', ha='center', va='bottom',
          fontsize=11, color='#aaaaaa', fontfamily='monospace')
ax_a.text(50, -1, 'Volumen = 1 L', ha='center', va='bottom',
          fontsize=10, color='#888888', fontfamily='monospace')


# ========== PANEL B: ALTA CONCENTRACIÓN ==========
ax_b = axes[1]
ax_b.set_xlim(0, 100)
ax_b.set_ylim(0, 130)
ax_b.set_aspect('equal')
ax_b.axis('off')
ax_b.set_facecolor('#0a0a1a')

flask_b = draw_flask(ax_b, 50, 8, 80, 100, '#5c1a1a', 0.30)
n_b = 20
xs_b, ys_b = draw_particles_and_arrows(ax_b, flask_b, n_b, '#ef5350', 'rápido',
                                         collision_zone=True)

# Label
ax_b.text(50, 126, 'B. ALTA CONCENTRACIÓN', ha='center', va='top',
          fontsize=15, fontweight='bold', color='#ef5350',
          fontfamily='monospace')
ax_b.text(50, 5, f'n = {n_b} particulas en 1 L', ha='center', va='bottom',
          fontsize=11, color='#aaaaaa', fontfamily='monospace')
ax_b.text(50, -1, 'Volumen = 1 L', ha='center', va='bottom',
          fontsize=10, color='#888888', fontfamily='monospace')


# ========== PANEL C: EXPLICACION ==========
ax_c = axes[2]
ax_c.set_xlim(0, 100)
ax_c.set_ylim(0, 130)
ax_c.set_aspect('equal')
ax_c.axis('off')
ax_c.set_facecolor('#0a0a1a')

texts = [
    (126, 'CONCENTRACION', '#ffffff', 16, 'bold'),
    (120, '(mol/L)', '#888888', 11, 'normal'),
    (110, '─────────────────', '#333333', 10, 'normal'),
    (103, 'C = n / V', '#ffd54f', 18, 'bold'),
    (95, 'n = moles de soluto', '#cccccc', 12, 'normal'),
    (89, 'V = volumen (L)', '#cccccc', 12, 'normal'),
    (80, '─────────────────', '#333333', 10, 'normal'),
    (73, 'POR QUE MAS', '#ffffff', 14, 'bold'),
    (67, 'COLISIONES?', '#ffffff', 14, 'bold'),
    (58, '(1) Mas particulas en', '#ef5350', 12, 'normal'),
    (53, '    mismo volumen', '#ef5350', 12, 'normal'),
    (46, '(2) Menor distancia', '#ef5350', 12, 'normal'),
    (41, '    entre particulas', '#ef5350', 12, 'normal'),
    (34, '(3) Mayor frecuencia', '#ef5350', 12, 'normal'),
    (29, '    de encuentro', '#ef5350', 12, 'normal'),
    (20, '─────────────────', '#333333', 10, 'normal'),
    (13, 'Prob. colisión ∝ C²', '#4fc3f7', 12, 'bold'),
    (7, 'Velocidad ∝ √T', '#4fc3f7', 11, 'normal'),
]

for y, txt, color, size, weight in texts:
    ax_c.text(50, y, txt, ha='center', va='top',
              fontsize=size, color=color, fontweight=weight,
              fontfamily='monospace')

# Title
fig.suptitle('CONCENTRACION Y PROBABILIDAD DE COLISIONES MOLECULARES',
             fontsize=20, fontweight='bold', color='white',
             fontfamily='monospace', y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.94])
plt.savefig('/Users/tayac/Documents/GitHub/Nous/figures/concentration_diagram.png',
            dpi=200, bbox_inches='tight', facecolor='#0a0a1a', edgecolor='none')
plt.savefig('/Users/tayac/Documents/GitHub/Nous/figures/concentration_diagram.pdf',
            bbox_inches='tight', facecolor='#0a0a1a', edgecolor='none')
print("✓ Figura guardada en figures/concentration_diagram.png y .pdf")
print("OK")
