import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection


def add_pmts(ax=None, color='b', linewidth=1):

    x0 = 27  # 9 times the inner radius
    y0 = 6 * 3 * 2 / np.sqrt(3)  # 6 times the outer radius

    if ax is None:
        ax = plt.gca()

    per_row = [9, 10, 11, 10, 11, 10, 11, 10, 9]

    polys = []
    for row, num_pmts in enumerate(per_row):

        y = row * 3 * np.sqrt(3)
        for pmt in range(num_pmts):
            x = 6 * pmt
            if row in (0, 8):
                x += 3
            elif row % 2 == 0:
                x -= 3

            polys.append(RegularPolygon((x - x0, y - y0), 6,  radius=6 / np.sqrt(3)))

    col = PatchCollection(polys)
    col.set_facecolors('none')
    col.set_edgecolors(color)
    col.set_linewidths(linewidth)
    ax.add_artist(col)

    return col


if __name__ == '__main__':

    fig, ax = plt.subplots()

    ax.set_aspect(1)

    add_pmts(ax=ax)

    ax.set_xlim(-35, 35)
    ax.set_ylim(-26, 26)
    plt.grid()

    plt.show()
