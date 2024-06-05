import json
import os
import mne
from scipy.signal import butter, sosfilt

import numpy as np


# The variables in ALL CAPS are the settings and constants
# that might need adjusting over time.
# They're all defined right here so they're easy to find.

# Filtering settings.
HIGH_CUTOFF = 500.0  # Cutoff frequency in Hz
LOW_CUTOFF = 25.0  # Cutoff frequency in Hz
SAMPLING_FREQUENCY = 5000.0  # Sampling frequency in Hz
ORDER = 12  # Order of filter. Higher is a sharper cutoff.


def get_vhdr_filenames(subject_id, data_directory):
    filenames = os.listdir(data_directory)
    vhdr_filenames = []
    for filename in filenames:
        pathname = os.path.join(data_directory, filename)
        if pathname.__contains__("vhdr"):
            if pathname.__contains__(subject_id):
                vhdr_filenames.append(pathname)
    return vhdr_filenames


def get_condition_order(subject_id):
    condition_order_filename = "_".join(["conditions", subject_id]) + ".txt"
    condition_order_path = os.path.join("data", condition_order_filename)
    condition_order = []
    with open(condition_order_path, "rt") as f:
        parts = list(f.read())
        for part in parts:
            if part.isalpha():
                condition_order.append(part)
    return condition_order


def get_details(vhdr_name):
    vhdr_parts = vhdr_name.split("_")
    subject_id = vhdr_parts[0]

    bets_filename = "_".join(["bets", subject_id]) + ".txt"
    bets_path = os.path.join("data", bets_filename)
    with open(bets_path, "rt") as f:
        bets = list(json.loads(f.read()))

    conditions_filename = "_".join(["conditions", subject_id]) + ".txt"
    conditions_path = os.path.join("data", conditions_filename)
    with open(conditions_path, "rt") as f:
        conditions = f.read()

    disgust_images_filename = "_".join(["disgust_images", subject_id]) + ".txt"
    disgust_images_path = os.path.join("data", disgust_images_filename)
    with open(disgust_images_path, "rt") as f:
        disgust_images = list(json.loads(f.read()))

    emotions_filename = "_".join(["emotions", subject_id]) + ".txt"
    emotions_path = os.path.join("data", emotions_filename)
    with open(emotions_path, "rt") as f:
        emotions = list(json.loads(f.read()))

    opponents_filename = "_".join(["opponents", subject_id]) + ".txt"
    opponents_path = os.path.join("data", opponents_filename)
    with open(opponents_path, "rt") as f:
        opponents = list(json.loads(f.read()))

    tastants_filename = "_".join(["tastants", subject_id]) + ".txt"
    tastants_path = os.path.join("data", tastants_filename)
    with open(tastants_path, "rt") as f:
        tastants = list(json.loads(f.read()))

    return bets, conditions, disgust_images, emotions, opponents, tastants


def read_emg_data(filename, samples, labels):
    raw = mne.io.read_raw_brainvision(filename)

    # events = mne.events_from_annotations(raw)
    # event_data = events[0]
    cor_emg = raw.copy()[0, :][0].ravel()
    ll_emg = raw.copy()[1, :][0].ravel()
    zyg_emg = raw.copy()[2, :][0].ravel()
    mas_emg = raw.copy()[3, :][0].ravel()

    cor_filt = np.abs(bandpass_filter(cor_emg))
    ll_filt = np.abs(bandpass_filter(ll_emg))
    zyg_filt = np.abs(bandpass_filter(zyg_emg))
    mas_filt = np.abs(bandpass_filter(mas_emg))
    return cor_filt, ll_filt, zyg_filt, mas_filt
    '''
    # Find the final indices for each snippet.
    # ends = [s - 1 for s in starts]
    # ends = ends[1:]
    # ends.append(cor_emg.size - 1)

    emg_data = {}
    spit_beep_times = []
    i_spit = 0
    i_accept = 0
    for i in range(len(starts)):
        start = starts[i]
        end = ends[i]
        start_time = timestamps[i]
        end_time = start_time + (end - start) / SAMPLING_FREQUENCY
        label = labels[i]
        key = "label_event_ignore"

        if label == "Getting baseline":
            key = "baseline"
        if label == "Spitting":
            key = f"spit_{i_spit}"
            i_spit += 1
            spit_beep_times.append(start_time)
        if label == "Acceptance":
            key = f"accept_{i_accept:02}"
            i_accept += 1

        # Filter each muscle's EMG data to take out the very low and
        # very high frequencies.
        cor_filt = np.abs(bandpass_filter(cor_emg[start : end + 1]))
        ll_filt = np.abs(bandpass_filter(ll_emg[start : end + 1]))
        zyg_filt = np.abs(bandpass_filter(zyg_emg[start : end + 1]))
        mas_filt = np.abs(bandpass_filter(mas_emg[start : end + 1]))

        emg_data[key] = {
            "start_time": start_time,
            "end_time": end_time,
            "cor": cor_filt,
            "ll": ll_filt,
            "zyg": zyg_filt,
            "mas": mas_filt,
        }

    return emg_data, spit_beep_times
    '''


def read_snippet_info(vhdr_filename):
    vmrk_filename = vhdr_filename[:-4] + "vmrk"
    with open(vmrk_filename, "rt") as f:
        # timestamps = []
        # snippet_starts = []
        labels = []
        samples = []
        lines = f.readlines()
        for line in lines:
            if line[:2] == "Mk":
                i_eq = line.find("=")
                # if line[i_eq + 1 : i_eq + 4] == "New":
                #     elements = line[i_eq + 1 :].split(",")
                #     timestamps.append(convert_to_timestamp(elements[-1]))
                #     # There's a mysterious off-by-one error I correct for here.
                #     snippet_starts.append(int(elements[2]) - 1)
                if line[i_eq + 1 : i_eq + 4] == "Sti":
                    elements = line[i_eq + 1 :].split(",")
                    labels.append(int(elements[1].split(" ")[-1]))
                    samples.append(int(elements[2]))

        # Drop the first snippet time. It has no associated label.
        # timestamps = timestamps[1:]
        # snippet_starts = snippet_starts[1:]

    # return timestamps, snippet_starts, labels
    return samples, labels


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


def convert_to_timestamp(time_string):
    """
    BrainVision's time representations are not standard.
    They appear to be strings formatted as
        YYYYMMDDHHMMSSssssss
    This function converts BrainVision's time to a float that
    counts the seconds since midnight.
    """
    hours = float(time_string[8:10])
    minutes = float(time_string[10:12])
    seconds = float(time_string[12:14])
    milliseconds = float(time_string[14:17])
    seconds_since_midnight = (
        hours * 3600.0 + minutes * 60.0 + seconds + milliseconds / 1000.0
    )
    return seconds_since_midnight
