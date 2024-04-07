"""
==============
HorizontalBarchart with shadows
==============

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Normal

# Fixing random state for reproducibility
np.random.seed(19680)

# Example data
n = 5
x_pos = np.arange(n)
performance = 5 * np.random.rand(n)
colors = [f"C{i}" for i in range(n)]

# %%

fig, ax = plt.subplots(num=1, clear=True)
bars = ax.barh(x_pos, performance, align='center', alpha=0.7, color=colors)
ax.set_xlim(0, 2.8)


from matplotlib.path import Path
import mpl_visual_context.patheffects as pe
from mpl_visual_context.patheffects_shadow import ShadowPath
from mpl_pe_fancy_bar import BarTransformBase, BarToRoundBar
from mpl_pe_fancy_bar.bar_with_icon import Icon, BarWithIcon

circle = Path.unit_circle().copy()
icon_circle = Icon((-1, -1, 2, 2), circle)
bar_with_circle = BarWithIcon(icon_circle, scale=0.6, dh=0, orientation="horizontal")

round_bar = BarToRoundBar(orientation="horizontal", dh=0)

pe1 = [
    round_bar| pe.AlphaGradient("0.4 > 0.8"),
    round_bar | pe.ClipPathSelf() | ShadowPath(135, 7) | pe.FillColor("k") | pe.GCModify(alpha=0.2),
    bar_with_circle | ShadowPath(135, 5) | pe.FillColor("k") | pe.GCModify(alpha=0.3),
    bar_with_circle | pe.GCModify(alpha=1) | pe.HLSModify(l=0.95),
]

for p in bars:
    p.set_path_effects(pe1)

for x, p in zip(x_pos, performance):
    ax.annotate(f"{p:.2f}", (p-0.1, x),
                va="center_baseline", ha="right", size=20, color="w")

pe2 = [
    ShadowPath(135, 5) | pe.HLSModify(l="20%") | pe.GCModify(alpha=0.5),
    pe.FillOnly()
]

for t in ax.texts:
    t.set_path_effects(pe2)

plt.show()
