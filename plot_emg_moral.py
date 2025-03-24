import numpy as np
import matplotlib.pyplot as plt
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
ZYG_LABEL = "Zygomatic"
MAS_LABEL = "Masseter"

THIN_LINEWIDTH = .5
MEDIUM_LINEWIDTH = 1
THICK_LINEWIDTH = 2

COR_COLOR = "blue"
LL_COLOR = "orange"
ZYG_COLOR = "green"
MAS_COLOR = "red"


def plot_moral_condition(
    cor, ll, mas, zyg,
    bets,
    emotions,
    opponents,
    samples,
    labels,
    subject_id,
):
    # Pull out the starts and stops of all the image EMG snippets
    # From data.py, "Offer Start" is 14 and "Offer Stop" is 15.
    starts = []
    stops = []
    for i_label, label in enumerate(labels):
        if label == 14:
            starts.append(samples[i_label])
        if label == 15:
            stops.append(samples[i_label])

    types = []
    for bet in bets:
        types.append(bet)

    # If there are excess bets, trim them off.
    types = types[:len(starts)]

    msg = "Must have same number of offer start and stop markers."
    assert len(starts) == len(stops), msg
    msg = "Must have same number of offer start markers and bets."
    assert len(starts) == len(types), msg

    plot_name = f"{subject_id}_gustatory_condition"
    fig_width = 11
    fig_height = 9
    fig = plt.figure(
        figsize=(fig_width, fig_height),
        label=plot_name
    )
    ax = fig.gca()

    last_t = 0
    for i_img in range(len(starts)):
        start = starts[i_img]
        stop = stops[i_img]
        img_type = types[i_img]
        t = np.arange(0, stop - start) / SAMPLING_FREQUENCY + last_t

        channels = [
            cor[start: stop] * EMG_SCALE + COR_OFFSET,
            ll[start: stop] * EMG_SCALE + LL_OFFSET,
            zyg[start: stop] * EMG_SCALE + ZYG_OFFSET,
            mas[start: stop] * EMG_SCALE + MAS_OFFSET,
        ]
        colors = [
            COR_COLOR,
            LL_COLOR,
            ZYG_COLOR,
            MAS_COLOR,
        ]

        for channel, color in zip(channels, colors):
            ax.plot(t, channel, color=color, clip_on=False)

        ax.plot(
            [last_t, last_t],
            [MARKER_MIN, MARKER_MAX],
            color="black",
            linewidth=THIN_LINEWIDTH,
        )
        ax.text(
            last_t,
            MARKER_LABEL_LOW_Y,
            img_type,
            fontsize=8,
            rotation=-90,
            horizontalalignment="left",
            verticalalignment="top",
        )
        ax.text(
            last_t,
            MARKER_LABEL_HI_Y,
            img_type,
            fontsize=8,
            rotation=-90,
            # zorder=3,
            horizontalalignment="left",
            verticalalignment="bottom",
        )
        last_t += (stop - start) / SAMPLING_FREQUENCY

    ax.plot(
        [last_t, last_t],
        [MARKER_MIN, MARKER_MAX],
        color="black",
        linewidth=THIN_LINEWIDTH,
    )
    x_max = last_t
    x_min = 0
    label_offset_x = -x_max / 18
    label_main_offset_x = -x_max / 12

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(Y_MIN, Y_MAX)

    label_offsets_y = [
        COR_OFFSET + LABEL_OFFSET_Y,
        LL_OFFSET + LABEL_OFFSET_Y,
        ZYG_OFFSET + LABEL_OFFSET_Y,
        MAS_OFFSET + LABEL_OFFSET_Y,
    ]
    muscle_labels = [
        COR_LABEL,
        LL_LABEL,
        ZYG_LABEL,
        MAS_LABEL,
    ]
    for offset_y, muscle_label in zip(label_offsets_y, muscle_labels):
        ax.text(
            label_offset_x,
            offset_y,
            muscle_label,
            fontsize=10,
            rotation=90,
            horizontalalignment="right",
            verticalalignment="center",
        )

    ax.text(
        label_main_offset_x,
        LABEL_MAIN_OFFSET_Y,
        EMG_LABEL,
        fontsize=12,
        rotation=90,
        horizontalalignment="right",
        verticalalignment="center",
    )
    ax.set_xlabel("time (seconds)")
    plt.show()
