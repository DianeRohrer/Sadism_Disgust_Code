import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.patches as patches
from data import images, markers

SAMPLING_FREQUENCY = 5000.0  # Sampling frequency in Hz
EMG_SCALE = 1000

COR_OFFSET = 0.0012 * EMG_SCALE
LL_OFFSET = 0.0008 * EMG_SCALE
ZYG_OFFSET = 0.0004 * EMG_SCALE
MAS_OFFSET = 0.0000 * EMG_SCALE
EMG_MAX = 0.0005 * EMG_SCALE

Y_MIN = -ZYG_OFFSET * .6
Y_MAX = COR_OFFSET + EMG_MAX

MARKER_MAX = Y_MAX - EMG_MAX + .5
MARKER_MIN = Y_MIN / 8
MARKER_LABEL_LOW_Y = Y_MIN / 5
MARKER_LABEL_HI_Y = Y_MAX + Y_MIN * .7

LABEL_OFFSET_Y = EMG_MAX / 3
LABEL_MAIN_OFFSET_Y = Y_MIN + (Y_MAX - Y_MIN) / 2

EMG_LABEL = "Rectified and Filtered EMG (millivolts)"
COR_LABEL = "Corrugator"
LL_LABEL = "Levator"
MAS_LABEL = "Masseter"
ZYG_LABEL = "Zygomatic"

THIN_LINEWIDTH = .5
MEDIUM_LINEWIDTH = 1
THICK_LINEWIDTH = 2

COR_COLOR = "blue"
LL_COLOR = "orange"
ZYG_COLOR = "green"
MAS_COLOR = "red"


def plot_experiment(
    cor, ll, mas, zyg,
    bets,
    conditions,
    disgust_images,
    emotions,
    opponents,
    tastants,
    samples,
    labels,
    plot_name,
):
    fig_width = 11
    fig_height = 9
    fig = plt.figure(
        figsize=(fig_width, fig_height),
        label=plot_name + " experiment"
    )
    ax = fig.gca()

    ax.plot(cor * EMG_SCALE + COR_OFFSET)
    ax.plot(ll * EMG_SCALE + LL_OFFSET)
    ax.plot(zyg * EMG_SCALE + ZYG_OFFSET)
    ax.plot(mas * EMG_SCALE + MAS_OFFSET)

    for i_label, label_code in enumerate(labels):
        label = markers[label_code]
        marker_label_x = samples[i_label]

        ax.plot(
            [marker_label_x, marker_label_x],
            [MARKER_MIN, MARKER_MAX],
            color="black",
            linewidth=THIN_LINEWIDTH,
        )
        ax.text(
            marker_label_x,
            MARKER_LABEL_LOW_Y,
            label,
            fontsize=8,
            rotation=-90,
            horizontalalignment="center",
            verticalalignment="top",
        )
    ax.set_ylim(Y_MIN, Y_MAX)

    plt.show()
