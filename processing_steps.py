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
# Sampling rate (~5005 Hz) differs from the nominal (5000 Hz)
# because the actual video frame rate (29.97 frames per second)
# is different from nominal (30 frames per second) that Adobe Premiere uses
# when displaying frames and calculating times.
SAMPLING_FREQUENCY = 5000.0 * 30.0 / 29.97  # Sampling frequency in Hz
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


'''
def get_condition_order(subject_id):
    condition_order_filename = "_".join(["conditions", subject_id]) + ".txt"
    condition_order_path = os.path.join("data", condition_order_filename)
    condition_order = []
    with open(condition_order_path, "rt") as f:
        parts = f.read().split("'")
        condition_order = [parts[1], parts[3], parts[5]]
    return condition_order
'''

def get_details(subject_id):
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
    # cor_emg = raw.copy()[0, :][0].ravel()
    ll_emg = raw.copy()[1, :][0].ravel()
    # zyg_emg = raw.copy()[2, :][0].ravel()
    # mas_emg = raw.copy()[3, :][0].ravel()

    # Filter each muscle's EMG data to take out the very low and
    # very high frequencies.
    # cor_filt = np.abs(bandpass_filter(cor_emg))
    ll_filt = np.abs(bandpass_filter(ll_emg))
    # zyg_filt = np.abs(bandpass_filter(zyg_emg))
    # mas_filt = np.abs(bandpass_filter(mas_emg))

    emg_data = {}
    condition_start_times = {}
    spit_beep_times = []
    i_baseline = 0
    i_cross = 0
    i_palatability = 0
    i_offer = 0
    i_spit = 0
    i_view = 0

    for i_label, label in enumerate(labels):
        assertion_message = "Marker numbers are misaligned in read_emg_data()"
        if label == 2:
            # Pull out baseline snippets.
            # The next marker should always be 3.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 1] == 3, assertion_message
            key = f"baseline_{i_baseline}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 1]
            i_baseline += 1
        elif label == 6:
            # Pull out fixation cross snippets.
            # The next marker should always be 7.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 1] == 7, assertion_message
            key = f"cross_{i_cross}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 1]
            i_cross += 1
        elif label == 22:
            # Pull out spitting snippets from the gustatory condition.
            # The next marker should always be 32.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 1] == 32, assertion_message
            key = f"spit_{i_spit}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 1]
            # Record when the spit beep occurs for synchronizing with
            # the video.
            # spit_beep_times.append(samples[i_label] / SAMPLING_FREQUENCY)
            i_spit += 1
        elif label == 21:
            # Record when the spit beep occurs for synchronizing with
            # the video.
            spit_beep_times.append(samples[i_label] / SAMPLING_FREQUENCY)
            continue
        elif label == 26:
            # Pull out palatability scoring snippets from the gustatory condition.
            # The next marker should always be 23.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 1] == 23, assertion_message
            key = f"palatability_{i_palatability}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 1]
            i_palatability += 1
        elif label == 14:
            # Pull out offer consideration snippets from the moral condition.
            # The marker after next should always be 15.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 2] == 15, assertion_message
            key = f"offer_{i_offer}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 2]
            i_offer += 1
        elif label == 8:
            # Pull out image viewing snippets from the visual condition.
            # The next marker should always be 9.
            # Just double check and throw an error if it's not.
            assert labels[i_label + 1] == 9
            key = f"view_{i_view}"
            start_sample = samples[i_label]
            end_sample = samples[i_label + 1]
            i_view += 1
        elif label == 1:
            condition_start_times["visual"] = (
                samples[i_label] / SAMPLING_FREQUENCY)
            continue
        elif label == 5:
            condition_start_times["gustatory"] = (
                samples[i_label] / SAMPLING_FREQUENCY)
            continue
        elif label == 11:
            condition_start_times["moral"] = (
                samples[i_label] / SAMPLING_FREQUENCY)
            continue
        else:
            continue

        start_time = start_sample / SAMPLING_FREQUENCY
        end_time = end_sample / SAMPLING_FREQUENCY

        # cor_snippet = cor_filt[start_sample : end_sample]
        ll_snippet = ll_filt[start_sample : end_sample]
        # zyg_snippet = zyg_filt[start_sample : end_sample]
        # mas_snippet = mas_filt[start_sample : end_sample]

        emg_data[key] = {
            "start_time": start_time,
            "end_time": end_time,
            "start_sample": start_sample,
            "end_sample": end_sample,
            # Only the "ll" lavator labii muscle is being extracted for now.
            # "cor": cor_snippet,
            "ll": ll_snippet,
            # "zyg": zyg_snippet,
            # "mas": mas_snippet,
        }

    return emg_data, condition_start_times, spit_beep_times


def read_marker_info(vhdr_filename):
    vmrk_filename = vhdr_filename[:-4] + "vmrk"
    with open(vmrk_filename, "rt") as f:
        timestamps = []
        labels = []
        samples = []
        lines = f.readlines()
        for line in lines:
            if line[:2] == "Mk":
                i_eq = line.find("=")
                if line[i_eq + 1 : i_eq + 4] == "Sti":
                    elements = line[i_eq + 1 :].split(",")
                    # This finds the number of seconds since the experiment
                    # was started.
                    label = int(elements[1].split(" ")[-1])
                    labels.append(label)
                    sample = int(elements[2])
                    samples.append(sample)
                    timestamp = int(sample) / SAMPLING_FREQUENCY
                    timestamps.append(timestamp)

    return timestamps, samples, labels


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
