"""
====================
Demo of SVG bar chart
====================
"""

# Let's try to read gift-pack-svgrepo-com2.svg
# https://www.svgrepo.com/svg/368437/gift-pack


xmlstring = b"""
<svg width="800px" height="800px" viewBox="0 0 90 90" xmlns="http://www.w3.org/2000/svg">

<defs>

<style>.cls-1{fill:#ffffff;}.cls-2{fill:#ff8898;}.cls-3{fill:#e6d488;}.cls-4{fill:#ffeb97;}.cls-5{fill:#576065;}</style>

</defs>

<title>gift-pack</title>

<g id="gift-pack">

<g id="gift-pack-2" data-name="gift-pack">

<g id="fill">

<path class="cls-1" d="M79.77,46.59V85a3.18,3.18,0,0,1-3.16,3.2H13.39A3.18,3.18,0,0,1,10.22,85V46.59Z"/>

<path class="cls-2" d="M82.57,43.21a3.17,3.17,0,0,1-3.13,3.2H10.56a3.17,3.17,0,0,1-3.13-3.2V28.81a3.17,3.17,0,0,1,3.13-3.2H79.43a3.17,3.17,0,0,1,3.13,3.2Z"/>

<rect class="cls-3" x="38.43" y="46.59" width="13.15" height="41.61"/>

<rect class="cls-4" x="38.43" y="25.61" width="13.15" height="20.98"/>

</g>

<g id="outline">

<path class="cls-5" d="M76.61,90H13.39a5,5,0,0,1-5-5V46.59a1.8,1.8,0,0,1,1.8-1.8H79.77a1.8,1.8,0,0,1,1.8,1.8V85A5,5,0,0,1,76.61,90ZM12,48.39V85a1.38,1.38,0,0,0,1.36,1.4H76.61A1.38,1.38,0,0,0,78,85V48.39Z"/>

<path class="cls-5" d="M79.43,48.22H10.56a5,5,0,0,1-4.93-5V28.81a5,5,0,0,1,4.93-5H79.43a5,5,0,0,1,4.93,5v14.4A5,5,0,0,1,79.43,48.22ZM10.56,27.41a1.37,1.37,0,0,0-1.33,1.4v14.4a1.37,1.37,0,0,0,1.33,1.4H79.43a1.37,1.37,0,0,0,1.33-1.4V28.81a1.37,1.37,0,0,0-1.33-1.4Z"/>

<path class="cls-5" d="M47.4,26.77a4.33,4.33,0,0,1-3.23-1.2C39.49,20.78,51,4.75,52.88,2.84A9.35,9.35,0,0,1,59.61,0h0a9.52,9.52,0,0,1,6.84,2.9,9.91,9.91,0,0,1,.06,13.78h0C64.14,19.11,53.27,26.77,47.4,26.77ZM59.61,3.6h0a5.78,5.78,0,0,0-4.16,1.76c-3.84,3.93-10.17,16.08-8.7,17.7,1.6,1.43,13.4-5,17.19-8.9a6.29,6.29,0,0,0-.06-8.74A5.94,5.94,0,0,0,59.61,3.6Zm5.62,11.82h0Z"/>

<path class="cls-5" d="M42.55,26.86h0c-5.83,0-16.76-7.74-19.16-10.2h0a9.87,9.87,0,0,1,0-13.73A9.37,9.37,0,0,1,30.1.07h0A9.44,9.44,0,0,1,36.89,3a52.71,52.71,0,0,1,7,10.55c3.19,6.19,3.79,10.18,1.83,12.18A4.26,4.26,0,0,1,42.55,26.86ZM30.1,3.67a5.8,5.8,0,0,0-4.17,1.77,6.25,6.25,0,0,0,0,8.7h0c3.84,3.93,15.47,10.34,17.2,9,1.36-1.74-4.93-13.7-8.83-17.69a5.87,5.87,0,0,0-4.22-1.8Z"/>

<path class="cls-5" d="M39.36,89.73a1.8,1.8,0,0,1-1.8-1.8V27.11a1.8,1.8,0,0,1,3.6,0V87.93A1.8,1.8,0,0,1,39.36,89.73Z"/>

<path class="cls-5" d="M50.64,89.73a1.8,1.8,0,0,1-1.8-1.8V27.11a1.8,1.8,0,0,1,3.6,0V87.93A1.8,1.8,0,0,1,50.64,89.73Z"/>

<path class="cls-5" d="M28.8,39.29a1.8,1.8,0,0,1-1.52-2.76c.28-.45,7.07-11,17.48-13.84a1.8,1.8,0,0,1,.95,3.47c-9.08,2.48-15.33,12.19-15.39,12.29A1.8,1.8,0,0,1,28.8,39.29Z"/>

<path class="cls-5" d="M61.2,39.29a1.8,1.8,0,0,1-1.57-.92c-2.49-4.47-11.88-10.53-15.29-12.49a1.8,1.8,0,0,1,1.79-3.12c.54.31,13.15,7.6,16.64,13.86a1.8,1.8,0,0,1-1.57,2.68Z"/>

</g>

</g>

</g>

</svg>
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_visual_context.patheffects as pe

from mpl_simple_svg_parser import SVGMplPathIterator, get_paths_extents
from mpl_pe_fancy_bar import PathsStretcher

from mpl_pe_fancy_bar.paths_stretcher import (
    get_normalizing_transform,
)

import matplotlib.pyplot as plt

def get_ribbonbox_drawer():

    svg = SVGMplPathIterator(xmlstring)
    paths = list(svg.iter_mpl_path_patch_prop())
    bb = get_paths_extents([p for p, _ in paths])
    tr, height = get_normalizing_transform(bb)
    paths = [(tr.transform_path(p), _) for (p, _) in paths]

    def get_color(i, p, fc, ec, fc_new, ec_new):
        if i == 0:
            return fc_new, ec

        return fc, ec

    # we use height of the box without the ribbon part at the top.
    ribbonbox_drawer = PathsStretcher(paths, height-0.3, y_thresh=0.4, height_lim=0.4,
                                      fn_get_color=get_color)


    return ribbonbox_drawer


np.random.seed(19680)

# Example data
n = 7
x_pos = np.arange(n)
performance = 5 * np.random.rand(n)
colors = [f"C{i}" for i in range(n)]

fig, ax = plt.subplots(1, 1, num=6, clear=True)

bars = ax.bar(x_pos, performance, align='center', alpha=0.7, color=colors)

drawer = get_ribbonbox_drawer()

# from mpl_visual_context.patheffects_path import BarTransformFromFunc
from mpl_pe_fancy_bar import BarToMultiplePaths #BarTransformFromFunc
pe1 = BarToMultiplePaths(drawer)

for p in bars:
    # for p, perf in zip(bars, performance):
    p.set_path_effects([pe1.path_only() | pe.AlphaGradient("0.2 ^ 1.0"),
                        pe.FillColor(None) | pe1,
                        ])

# ax.set_ylim(0, 2.8)
plt.show()
