"""
For all the EMG data from all the subjects,
find all the interesting bits (baseline, spitting, and acceptance),
pull out any parts that shouldn't be there (moving, talking),
show the cleaned EMG re-organized by muscle and tastant,
average the EMG during each portion, and save the result.

This script can be called from the command line like so:

python3 artifact_cleanup.py 631

where `631` is the subject ID you want to process.

Or it can be called from another script:

from artifact cleanup import process_subject
process_subject(631)

Results are saved out into a file titled like `631_emg_averages.csv`.
"""
import argparse
import copy
import os
import numpy as np
import pandas as pd

from file_tools import get_directories
from img_label_data import img_labels
# from plot_emg import plot_experiment
# from plot_emg_gustatory import plot_gustatory_condition
# from plot_emg_moral import plot_moral_condition
# from plot_emg_visual import plot_visual_condition
from processing_steps import get_vhdr_filenames
from processing_steps import get_details, read_emg_data, read_marker_info

SAMPLING_FREQUENCY = 5000.0 * 30.0 / 29.97  # Sampling frequency in Hz
# SAMPLING_FREQUENCY = 5000.0  # Sampling frequency in Hz

PLOT_ALL = False
PLOT_GUSTATORY = False
PLOT_MORAL = True
PLOT_VISUAL = False

def process_subject(subject_id=None, turn_off_plots=False):
    """
    This is the top level function that does the work of this script.
    It calls a sequence of other functions to do the hard work.
    """
    if subject_id is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("subject_id")
        args = parser.parse_args()
        subject_id = args.subject_id

    data_directory, plot_directory = get_directories()
    vhdr_filenames = get_vhdr_filenames(subject_id, data_directory)

    msg = (
        f"There are {len(vhdr_filenames)} vhdr files.\n"
        + "There should be only one."
    )
    assert len(vhdr_filenames) == 1, msg
    vhdr_filename = vhdr_filenames[0]

    # Extract the start times labels of all snippets.
    # timestamps, starts, labels = read_marker_info(vhdr_filename)
    timestamps, samples, labels = read_marker_info(vhdr_filename)

    # Load in the EMG for each muscle.
    # Pre-extract the baseline, spitting, and acceptance snippets.
    # Put them all in a dictionary.
    (
        emg_data,
        condition_start_times,
        spit_beep_times,
    ) = read_emg_data(vhdr_filename, samples, labels)

    # Remove artifacts.
    # Find the offset between the camera clock and EMG clock.
    condition_order, condition_offsets, artifacts = find_offsets(
        subject_id,
        condition_start_times,
        spit_beep_times,
        data_directory
    )

    find_emg_averages(
        subject_id,
        data_directory,
        emg_data,
        artifacts,
        condition_order,
        condition_start_times,
        condition_offsets,
    )

    '''
    if PLOT_VISUAL and not turn_off_plots:
        plot_visual_condition(
            cor, ll, mas, zyg,
            disgust_images,
            samples,
            labels,
            subject_id,
        )
    if PLOT_GUSTATORY and not turn_off_plots:
        plot_gustatory_condition(
            cor, ll, mas, zyg,
            tastants,
            samples,
            labels,
            subject_id,
        )
    if PLOT_MORAL and not turn_off_plots:
        plot_moral_condition(
            cor, ll, mas, zyg,
            bets,
            emotions,
            opponents,
            samples,
            labels,
            subject_id,
        )
    if PLOT_ALL and not turn_off_plots:
        plot_experiment(
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
        )
'''


def find_offsets(
    subject_id,
    condition_start_times,
    spit_beep_times,
    data_directory,
):
    """
    This function calculates the difference between video time and
    EMG time. Knowing this difference lets us use the behaviors we find
    in the video (like talking or touching) to remove the
    relevant portions of the EMG.
    """
    filename = f"artifacts_{subject_id}.csv"
    filepath = os.path.join(data_directory, filename)
    artifacts = pd.read_csv(filepath)

    # Convert video artifact start and stop times to be
    # the number of seconds since the beginning of the video.
    # This representation is easier to do math on.
    # There are 30 frames per second, so each frame is 1/30 second.
    artifacts["start_time"] = (
        artifacts["start_hour"] * 3600
        + artifacts["start_minute"] * 60
        + artifacts["start_second"]
        + artifacts["start_frame"] / 30.0
    )
    artifacts["end_time"] = (
        artifacts["end_hour"] * 3600
        + artifacts["end_minute"] * 60
        + artifacts["end_second"]
        + artifacts["end_frame"] / 30.0
    )
    artifacts["duration"] = artifacts["end_time"] - artifacts["start_time"]

    # For manually scanning artifact durations
    # for duration in artifacts["duration"]:
    #     print(duration)
    # bins = [-1e100, 0, 1, 2, 4, 8, 15, 30, 60, 1e100]
    # durations = artifacts["duration"].array
    # print(np.histogram(durations, bins))

    # Pull out the artifacts that are specifically tied to the start of
    # a condition. These moments are marked by syncrhronous PsychoPy beeps
    # and Markers sent to the EMG recording computer.
    # This lets us synchronize PsychoPy's representation
    # of time with the camera's.
    condition_start_times_camera = np.array(
        artifacts.loc[artifacts.loc[:, "start_condition"] == 1, "start_time"]
    )
    spit_beep_times_camera = np.array(
        artifacts.loc[artifacts.loc[:, "spitting (from beep)"] == 1, "start_time"]
    )
    # rinse_beep_times_camera = np.array(
    #     artifacts.loc[artifacts.loc[:, "rinsing (from beep)"] == 1, "start_time"]
    # )

    spit_beep_times_markers = np.array(spit_beep_times)

    # There should be exactly 25 spit beeps annotated on the video.
    # If there aren't,
    # then something isn't right with the data and the script
    # will exit so that we can figure out what went wrong.
    msg = (
        f"There are {spit_beep_times_camera.size}"
        + " spit beeps annotated."
        + "There should be 25."
    )
    assert spit_beep_times_camera.size == 25, msg

    # There should be exactly three `start_condition` beeps annotated
    # on the video.
    # If there aren't,
    # then something isn't right with the data and the script
    # will exit so that we can figure out what went wrong.
    msg = (
        f"There are {condition_start_times_camera.size} condition"
        + " start beeps annotated."
        + "There should be 3 (1 per condition)."
    )
    assert condition_start_times_camera.size == 3, msg

    # There should be exactly 25 spit beep markers.
    # If there aren't,
    # then something isn't right with the data and the script
    # will exit so that we can figure out what went wrong.
    msg = (
        f"There are {spit_beep_times_markers.size}"
        + " spit beep markers."
        + "There should be 25."
    )
    assert spit_beep_times_markers.size == 25, msg

    condition_start_times_markers = np.fromiter(
        condition_start_times.values(), dtype=float)

    # Just double check that there are exactly 3 condition start
    # markers. If there aren't, that's a real problem.
    msg = (
        f"There are {condition_start_times_markers.size} condition start markers."
        + "There should be 3."
    )
    assert condition_start_times_markers.size == 3, msg

    # camera_syncs = np.concatenate((
    #     spit_beep_times_camera,
    #     condition_start_times_camera
    # ))
    camera_syncs = condition_start_times_camera
    camera_syncs.sort()

    # marker_syncs = np.concatenate((
    #     spit_beep_times_markers,
    #     condition_start_times_markers
    # ))
    marker_syncs = condition_start_times_markers
    marker_syncs.sort()

    # This is the heart: Find the difference between the PsychoPy time
    # and the video time at each condition start.
    # They should all be approximately
    # the same. Average them together to get an even more accurate
    # estimate.
    # offset = np.median(marker_syncs - camera_syncs)
    # offsets = marker_syncs - camera_syncs

    # print("offsets")
    # for off in offsets:
    #     print(f"    {off}")
    # print("offset", offset)

    # Create offsets for each condition.
    # Add offsets to artifact times to make them line up with emg times.
    offsets = marker_syncs - camera_syncs

    # Pull the conditions in the order in which they occurred
    condition_order = sorted(
        condition_start_times,
        key=lambda k: condition_start_times[k]
    )

    offset = dict(zip(condition_order, offsets))

    return condition_order, offset, artifacts


def find_emg_averages(
    subject_id,
    data_directory,
    emg_data,
    artifacts,
    condition_order,
    condition_start_times,
    offsets,
):
    # Process the muscles one at a time.
    for muscle in ["cor", "mas", "ll", "zyg"]:
        # For each muscle, process the conditions one at a time.
        for i_condition, condition in enumerate(condition_order):
            # Initialize this so that the last condition ends up with an
            # end time that is far in the future.
            end_time = 1e10
            # For the first two conditions, the start of the next condition
            # is their end time.
            if i_condition < 2:
                next_condition = condition_order[i_condition + 1]
                end_time = condition_start_times[next_condition]
            start_time = condition_start_times[condition]
            offset = offsets[condition]

            # Collect just the emg snippets that belong to this condition.
            emg_cond = {}
            for emg_key in emg_data.keys():
                if (
                    (emg_data[emg_key]["start_time"] >= start_time) and
                    (emg_data[emg_key]["start_time"] < end_time)
                ):
                    emg_cond[emg_key] = emg_data[emg_key]

            # Collect just the artifacts that belong to this condition.
            artifacts_cond = artifacts.loc[np.logical_and(
                artifacts.loc[:, "end_time"] + offset >= start_time,
                artifacts.loc[:, "start_time"] + offset < end_time
            ), :]
            artifact_start_times = artifacts_cond.loc[:, "start_time"].values + offset
            artifact_end_times = artifacts_cond.loc[:, "end_time"].values + offset

            # Processess the EMG snippets one at a time
            for snippet_name, data in emg_cond.items():

                emg_snippet = copy.deepcopy(data[muscle])
                n_points = emg_snippet.size
                snippet_start_time = data["start_time"]
                snippet_end_time = data["end_time"]

                # Find the artifacts that overlap with this particular snippet.
                i_snippet_artifacts = np.where(
                    np.logical_and(
                        artifact_start_times <= snippet_end_time,
                        snippet_start_time <= artifact_end_times,
                    )
                )[0]
                remove_starts = None
                remove_ends = None

                # If any artifacts are found, remove those segments from the snippet.
                if i_snippet_artifacts.size > 0:
                    remove_starts = np.maximum(
                        snippet_start_time, artifact_start_times[i_snippet_artifacts]
                    )
                    remove_ends = np.minimum(
                        snippet_end_time, artifact_end_times[i_snippet_artifacts]
                    )
                    for i_snip in range(remove_starts.size):
                        start_index = int(
                            (remove_starts[i_snip] - snippet_start_time)
                            * SAMPLING_FREQUENCY
                        )
                        last_index = int(
                            (remove_ends[i_snip] - snippet_start_time)
                            * SAMPLING_FREQUENCY
                        )

                        index_err_msg = "Index error in removing artifacts"

                        assert start_index >= 0, index_err_msg
                        assert last_index <= n_points, index_err_msg

                        # Handle what appears to be an unfortunate rounding error
                        # to keep all indices within bounds.
                        if last_index == n_points:
                            last_index = n_points - 1

                        emg_snippet[start_index : last_index + 1] = np.nan

                data[f"emg_avg_{muscle}"] = np.nanmean(emg_snippet) * 1e6

            write_emg_averages(emg_cond, condition, muscle, data_directory, subject_id)


def write_emg_averages(emg_data, condition, muscle, data_directory, subject_id):
    # Create filename dict
    emg_averages_filename = f'{subject_id}_{condition}_{muscle}_emg_averages.csv'
    emg_averages_pathname = os.path.join(data_directory, emg_averages_filename)

    (
        bets,
        conditions,
        disgust_images,
        emotions,
        opponents,
        tastants_nested,
    )= get_details(subject_id)

    # Flatten the tastants list of lists into a single list
    tastants = []
    for top_level_list in tastants_nested:
        for t in top_level_list:
            tastants.append(t)

    tastant_abbreviations = {
        "high_quinine": "hq",
        "low_quinine": "lq",
        "high_sucrose": "hs",
        "low_sucrose": "ls",
        "water": "w",
    }

    # print(emg_averages_pathname)
    emg_dict_list = []
    for snippet_name, data in emg_data.items():
        emg_dict = {}
        emg_dict["snippet_name"] = snippet_name
        emg_dict["emg_avg"] = data[f"emg_avg_{muscle}"]
        snippet_type = snippet_name.split('_')[0]
        snippet_num = int(snippet_name.split('_')[1])
        emg_dict["snippet_type"] = snippet_type
        emg_dict_list.append(emg_dict)

        if snippet_type == "baseline":
            baseline_emg_avg = data[f"emg_avg_{muscle}"]

        if condition == "moral" and snippet_type == "offer":
            emg_dict["label"] = bets[snippet_num]

        if condition == "gustatory" and snippet_type == "spit":
            emg_dict["label"] = tastant_abbreviations[tastants[snippet_num]]

        if condition == "visual" and snippet_type == "view":
            img_id = disgust_images[snippet_num][22: 26]
            emg_dict["label"] = img_labels[img_id]

    # Find the baseline-adjusted emg averages for every snippet in
    # this condition.
    for emg_dict in emg_dict_list:
        emg_dict["emg_avg_norm"] = emg_dict["emg_avg"] - baseline_emg_avg

    df = pd.DataFrame(emg_dict_list)
    df.to_csv(emg_averages_pathname)

    # TODO: Also calculate the baseline using the average EMG during
    # the fixation cross


'''
def generate_plots(
    all_emg_data,
    all_plot_names,
    all_tastants,
    all_bets,
    artifacts,
    video_offsets,
):
    for condition in ["A", "B", "C"]:
        emg_data = all_emg_data[condition]
        plot_name = all_plot_names[condition]
        tastants = all_tastants[condition]
        bets = all_bets[condition]
        offset = video_offsets[condition]

        generate_plot(emg_data, plot_name, tastants, bets, artifacts, offset)
'''


if __name__ == '__main__':
    process_subject()
