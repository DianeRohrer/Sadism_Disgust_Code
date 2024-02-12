"""
Read and process EMG data.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import butter, sosfilt
import mne

# The variables in ALL CAPS are the settings and constants
# that might need adjusting over time.
# They're all defined right here so they're easy to find.

# Be specific about where to find data and where to plot copies of plots.
# LOKI_DATA_DIRECTORY = "/home/brohrer/projects/Moral_Disgust_Analysis/data"
# LOKI_PLOT_DIRECTORY = "/home/brohrer/projects/Moral_Disgust_Analysis/plots"
# THE_MORRIGAN_DATA_DIRECTORY = "/Users/themorrigan/Library/CloudStorage/Box-Box/EMG_Moral_Disgust_Data"  # noqa: E501
# THE_MORRIGAN_PLOT_DIRECTORY = "/Users/themorrigan/Desktop/Moral_Disgust_Code/plots"  # noqa: E501
# AIDAS_DATA_DIRECTORY = "/Users/hopswork/projects/Moral_Disgust_Code/data"
AIDAS_DATA_DIRECTORY = "/Users/hopswork/Library/CloudStorage/Box-Box/Sadism Disgust Study"  # noqa: E501
AIDAS_PLOT_DIRECTORY = "/Users/hopswork/projects/Sadism_Disgust_Code/plots"

# Filtering settings.
HIGH_CUTOFF = 500.0  # Cutoff frequency in Hz
LOW_CUTOFF = 25.0  # Cutoff frequency in Hz
HIGH_NOTCH_CUTOFF = 61.0  # Cutoff frequency in Hz
LOW_NOTCH_CUTOFF = 59.0  # Cutoff frequency in Hz
SAMPLING_FREQUENCY = 5000.0  # Sampling frequency in Hz
ORDER = 12  # Order of filter. Higher is a sharper cutoff.

# Set the colors for the EMG plots.
GREEN = "#10a19d"
PURPLE = "#540375"
ORANGE = "#ff7000"
YELLOW = "#ffbf00"
COLORS = {
    "cor": PURPLE,
    "ll": YELLOW,
    "zyg": GREEN,
    "mas": ORANGE,
}

# Turn plotting on and off.
PLOT_FREQUENCIES = True
PLOT_EMG = True
NOTCH_FILTER = True

# Check this is running on Loki or The Morrigan and
# set the directories accordingly.
try:
    # This will be true for Loki.
    if os.environ["DESKTOP_SESSION"] == "ubuntu":
        data_directory = LOKI_DATA_DIRECTORY
        plot_directory = LOKI_PLOT_DIRECTORY
except KeyError:
    # This will be true for The Morrigan.
    if os.environ["LOGNAME"] == "themorrigan":
        data_directory = THE_MORRIGAN_DATA_DIRECTORY
        plot_directory = THE_MORRIGAN_PLOT_DIRECTORY
    elif os.environ["LOGNAME"] == "hopswork":
        # This will be true for The Aidas under the Hopswork login.
        data_directory = AIDAS_DATA_DIRECTORY
        plot_directory = AIDAS_PLOT_DIRECTORY
    else:
        # If it can't figure it out, default to the directory from which
        # the script was run.
        data_directory = "."
        plot_directory = "."

print(data_directory)


def main():
    """
    This is the top level function responsible for displaying the EMG data.
    """
    # Get the subject ID and get the filenames of the data associated with it.
    subject_id = get_subject_id()
    vhdr_filenames = get_vhdr_filenames(subject_id)

    # If there is more than one EMG filename associated with this subject,
    # handle them each one at a time.
    for vhdr_filename in vhdr_filenames:
        # Load in the EMG for each muscle.
        (
            cor_emg,
            ll_emg,
            mas_emg,
            zyg_emg,
            time,
            i_starts,
            i_labels,
            labels,
        ) = read_emg_data(vhdr_filename)
        # Filter each muscle's EMG data to take out the very low and
        # very high frequencies.
        cor_filt = bandpass_filter(cor_emg)
        ll_filt = bandpass_filter(ll_emg)
        zyg_filt = bandpass_filter(zyg_emg)
        mas_filt = bandpass_filter(mas_emg)

        if NOTCH_FILTER:
            # Use a special filter to take out the 60 Hz noise
            # caused by electrical wiring and other devices.
            cor_filt = notch_filter(cor_filt)
            ll_filt = notch_filter(ll_filt)
            zyg_filt = notch_filter(zyg_filt)
            mas_filt = notch_filter(mas_filt)

        # Split out just the portion of the filename
        vhdr_name = vhdr_filename.split(os.path.sep)[-1].split(".")[0]

        if PLOT_FREQUENCIES:
            show_frequencies(cor_filt, COLORS["cor"], "Corrugator", vhdr_name)
            show_frequencies(ll_filt, COLORS["ll"], "Levator Labii", vhdr_name)
            show_frequencies(zyg_filt, COLORS["zyg"], "Zygomatic", vhdr_name)
            show_frequencies(mas_filt, COLORS["mas"], "Masseter", vhdr_name)

        if PLOT_EMG:
            show_emg(
                cor_filt,
                ll_filt,
                mas_filt,
                zyg_filt,
                time,
                i_starts,
                i_labels,
                labels,
                vhdr_name,
            )

    plt.show()


def get_subject_id():
    # Get the subject ID from the experimenter
    print("Enter the subject ID")
    print("and then hit Enter")
    subject_id_input = input()

    # Check to make sure that the ID is an integer
    # (or at least can be converted to an integer)
    try:
        subject_id = int(subject_id_input)
    except ValueError:
        print("Subject ID should be a number.")
        print("Maybe give it another go.")
        quit()
    return subject_id


def get_vhdr_filenames(subject_id):
    filenames = os.listdir(data_directory)
    vhdr_filenames = []
    for filename in filenames:
        pathname = os.path.join(data_directory, filename)
        if pathname.__contains__("vhdr"):
            if pathname.__contains__(str(subject_id)):
                vhdr_filenames.append(pathname)
    return vhdr_filenames


def read_emg_data(filename):
    raw = mne.io.read_raw_brainvision(filename)

    # n_time_samps = raw.n_times
    # time_secs = raw.times
    ch_names = raw.ch_names
    # n_chan = len(ch_names)  # note: there is no raw.n_channels attribute

    events = mne.events_from_annotations(raw)
    event_data = events[0]
    ii_starts = np.where(event_data[:, 2] == 99999)[0]
    i_starts = event_data[ii_starts, 0]

    ii_labels = np.where(event_data[:, 2] != 99999)[0]
    i_labels = event_data[ii_labels, 0]
    label_codes = event_data[ii_labels, 2]

    event_label_dict = events[1]
    reverse_dict = {}
    for key, value in event_label_dict.items():
        reverse_dict[value] = key

    labels = []
    for code in label_codes:
        labels.append(reverse_dict[code].split("/")[1])

    # baseline_start = t_starts[1]
    # baseline_end = t_starts[2]
    # cor_emg = raw.copy()[0, baseline_start: baseline_end][0].ravel()
    # ll_emg = raw.copy()[1, baseline_start: baseline_end][0].ravel()
    # zyg_emg = raw.copy()[2, baseline_start: baseline_end][0].ravel()
    # mas_emg = raw.copy()[3, baseline_start: baseline_end][0].ravel()
    # time = raw.copy()[0, baseline_start: baseline_end][1].ravel()
    cor_emg = raw.copy()[0, :][0].ravel()
    ll_emg = raw.copy()[1, :][0].ravel()
    zyg_emg = raw.copy()[2, :][0].ravel()
    mas_emg = raw.copy()[3, :][0].ravel()
    time = raw.copy()[0, :][1].ravel()
    return cor_emg, ll_emg, mas_emg, zyg_emg, time, i_starts, i_labels, labels


def bandpass_filter(emg):
    sos = butter(
        ORDER,
        [LOW_CUTOFF, HIGH_CUTOFF],
        "bandpass",
        fs=SAMPLING_FREQUENCY,
        output="sos",
    )
    filtered_emg = sosfilt(sos, emg)
    return filtered_emg


def notch_filter(emg):
    sos = butter(
        ORDER,
        [LOW_NOTCH_CUTOFF, HIGH_NOTCH_CUTOFF],
        "bandstop",
        fs=SAMPLING_FREQUENCY,
        output="sos",
    )
    filtered_emg = sosfilt(sos, emg)
    return filtered_emg


def show_frequencies(data, color, name, vhdr_name):
    emg_freq_full = np.abs(fft(data))
    # Remove zero offset (DC component)
    emg_freq_full[0] = 0
    nyquist = int(SAMPLING_FREQUENCY / 2)
    i_nyquist = int(emg_freq_full.size / 2)
    emg_freq = emg_freq_full[:i_nyquist]
    freq = np.linspace(0, nyquist, i_nyquist)

    filename = os.path.join(
        plot_directory, f"{vhdr_name}_{name.lower()}_emg_freq.png"
    )
    plt.figure(filename, figsize=(8, 6))

    plt.plot(freq, emg_freq, color=color)
    plt.title(f"{name} EMG, broken down by frequency")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Signal energy at each frequency")
    plt.xlim(0, 1000)
    # plt.ylim(0, .07)
    plt.savefig(filename)
    plt.show()


def show_emg(cor, ll, mas, zyg, time, i_starts, i_labels, labels, vhdr_name):
    offset = 0.0002

    filename = os.path.join(plot_directory, f"{vhdr_name}_emg.png")
    plt.figure(filename, figsize=(8, 6))
    plt.plot(time, np.abs(cor) + offset * 3, color=COLORS["cor"])
    plt.plot(time, np.abs(ll) + offset * 2, color=COLORS["ll"])
    plt.plot(time, np.abs(mas) + offset, color=COLORS["mas"])
    plt.plot(time, np.abs(zyg), color=COLORS["zyg"])
    plt.title("Rectified filtered EMG")
    plt.xlabel("Time (s)")
    plt.ylabel(
        "Electrical potential difference between elctrodes (Volts)", fontsize=9
    )
    plt.ylim(offset * -0.8, offset * 4.1)

    for i_start in i_starts:
        plt.plot(
            [time[i_start], time[i_start]],
            [offset * -0.03, offset * 4],
            color="black",
            zorder=-1,
        )
    for i, i_label in enumerate(i_labels):
        plt.text(
            time[i_label],
            offset * -0.05,
            labels[i],
            fontsize=7,
            horizontalalignment="left",
            verticalalignment="top",
            rotation=-90,
        )
    muscle_fontsize = 9
    muscle_x_offset = 6
    muscle_y_offset = offset * 0.5

    plt.text(
        muscle_x_offset,
        offset * 3 + muscle_y_offset,
        "Corrugator",
        fontsize=muscle_fontsize,
        horizontalalignment="left",
        verticalalignment="center",
    )
    plt.text(
        muscle_x_offset,
        offset * 2 + muscle_y_offset,
        "Lavator Labii",
        fontsize=muscle_fontsize,
        horizontalalignment="left",
        verticalalignment="center",
    )
    plt.text(
        muscle_x_offset,
        offset * 1 + muscle_y_offset,
        "Zygomatic",
        fontsize=muscle_fontsize,
        horizontalalignment="left",
        verticalalignment="center",
    )
    plt.text(
        muscle_x_offset,
        offset * 0 + muscle_y_offset,
        "Masseter",
        fontsize=muscle_fontsize,
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.savefig(filename)


main()
