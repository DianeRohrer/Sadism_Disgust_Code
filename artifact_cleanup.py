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
from plot_emg import plot_experiment
from plot_emg_gustatory import plot_gustatory_condition
from plot_emg_moral import plot_moral_condition
from plot_emg_visual import plot_visual_condition
from processing_steps import get_vhdr_filenames, get_condition_order
from processing_steps import get_details, read_emg_data, read_snippet_info

SAMPLING_FREQUENCY = 5000.0  # Sampling frequency in Hz

PLOT_ALL = False
PLOT_GUSTATORY = False
PLOT_MORAL = True
PLOT_VISUAL = False

def process_subject(subject_id=None):
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

    condition_order = get_condition_order(subject_id)

    # Create some dictionaries. These will be used to gather up the
    # results into one place.
    # all_spit_beep_times = {"A": None, "B": None, "C": None}
    # all_emg_data = {}
    # all_tastants = {}
    # all_bets = {}
    # all_plot_names = {}

    # Split out just the portion of the filename
    vhdr_name = vhdr_filename.split(os.path.sep)[-1].split(".")[0]
    plot_name = vhdr_filename.split(os.path.sep)[-1][:-5]
    bets, conditions, disgust_images, emotions, opponents, tastants = get_details(vhdr_name)

    # Extract the start times labels of all snippets.
    # timestamps, starts, labels = read_snippet_info(vhdr_filename)
    samples, labels = read_snippet_info(vhdr_filename)

    # Load in the EMG for each muscle.
    # Pre-extract the baseline, spitting, and acceptance snippets.
    # Put them all in a dictionary.
    # emg_data, spit_beep_times = read_emg_data(
    #     vhdr_filename, timestamps, starts, labels
    # )
    # emg_data, spit_beep_times = read_emg_data(vhdr_filename, samples, labels)
    cor, ll, zyg, mas = read_emg_data(vhdr_filename, samples, labels)
    # all_emg_data[condition] = emg_data
    # all_spit_beep_times[condition] = spit_beep_times
    # all_tastants[condition] = tastants
    # all_bets[condition] = bets
    # all_plot_names[condition] = plot_name

    # Remove artifacts.
    # Find the offset between the camera clock and EMG clock.
    # video_offsets, artifacts = find_offsets(
    #     subject_id, condition_order, all_spit_beep_times, data_directory
    # )

    # find_all_emg_averages(all_emg_data, artifacts, video_offsets)

    # write_emg_averages(all_emg_data, data_directory, subject_id)

    if PLOT_VISUAL:
        plot_visual_condition(
            cor, ll, mas, zyg,
            disgust_images,
            samples,
            labels,
            subject_id,
        )
    if PLOT_GUSTATORY:
        plot_gustatory_condition(
            cor, ll, mas, zyg,
            tastants,
            samples,
            labels,
            subject_id,
        )
    if PLOT_MORAL:
        plot_moral_condition(
            cor, ll, mas, zyg,
            bets,
            emotions,
            opponents,
            samples,
            labels,
            subject_id,
        )
    if PLOT_ALL:
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


def find_offsets(subject_id, condition_order, spit_beep_times, data_directory):
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

    # Pull out the artifacts that are specifically tied to spitting
    # out the tastants. Because spitting is prompted by PsychoPy beeps,
    # this particular artifact lets us synchronize PsychoPy's representation
    # of time with the camera's.
    spit_artifact_starts = np.array(
        artifacts.loc[artifacts.loc[:, "spitting"] == 1, "start_time"]
    )
    spit_artifact_starts.sort()

    # There should be exactly 18 tastant spits. If there aren't,
    # then something isn't right with the data and the script
    # will exit so that we can figure out what went wrong.
    msg = (
        f"There are {spit_artifact_starts.size} spitting artifacts. "
        + "There should be 18 (6 per condition)."
    )
    assert spit_artifact_starts.size == 18, msg

    offsets = {}
    for i, condition in enumerate(condition_order):
        spit_times = np.array(spit_beep_times[condition])
        spit_times.sort()

        # Just double check that there are exactly 6 tastant spits
        # for each condition. If there aren't, that's a real problem.
        msg = (
            f"There are {spit_times.size} spitting events "
            + f"for condition {condition}. "
            + "There should be 6."
        )
        assert spit_times.size == 6, msg

        condition_spit_artifact_starts = spit_artifact_starts[
            i * 6 : (i + 1) * 6
        ]

        # This is the heart: Find the difference between the PsychoPy time
        # and the video time at each spit. They should all be approximately
        # the same. Average them together to get an even more accurate
        # estimate.
        offsets[condition] = np.mean(
            spit_times - condition_spit_artifact_starts
        )

    # Pad spitting start times backward in time by 1 second
    # to make sure they cover the start of the spit EMG window.
    # This eliminates the big spike at the beginning of most
    # spit windows.
    artifacts.loc[artifacts.loc[:, 'spitting'] == 1, 'start_time'] -= 1

    return offsets, artifacts


def find_all_emg_averages(all_emg_data, artifacts, video_offsets):
    for condition in ["A", "B", "C"]:
        emg_data = all_emg_data[condition]
        offset = video_offsets[condition]
        find_emg_averages(emg_data, artifacts, offset)


def find_emg_averages(emg_data, artifacts, offset):
    artifact_start_times = artifacts["start_time"].values + offset
    artifact_end_times = artifacts["end_time"].values + offset
    muscles = ["cor", "mas", "ll", "zyg"]

    for snippet_name, data in emg_data.items():
        tmp_data = copy.deepcopy(data)
        n_points = data["cor"].size
        time = (np.arange(n_points) / SAMPLING_FREQUENCY) + data["start_time"]
        snippet_start_time = time[0]
        snippet_end_time = time[-1]

        i_snippet_artifacts = np.where(
            np.logical_and(
                artifact_start_times <= snippet_end_time,
                snippet_start_time <= artifact_end_times,
            )
        )[0]
        remove_starts = None
        remove_ends = None
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
                assert last_index < n_points, index_err_msg

                for muscle in muscles:
                    tmp_data[muscle][start_index : last_index + 1] = np.NaN

        for muscle in muscles:
            avg_name = f"emg_avg_{muscle}"
            data[avg_name] = np.nanmean(tmp_data[muscle]) * 1e6


def write_emg_averages(all_emg_data, data_directory, subject_id):
    emg_averages_filename = f'{subject_id}_emg_averages.csv'
    emg_averages_pathname = os.path.join(data_directory, emg_averages_filename)

    emg_dict_list = []
    for condition in ["A", "B", "C"]:
        emg_data = all_emg_data[condition]
        muscles = ["cor", "mas", "ll", "zyg"]
        for muscle in muscles:
            emg_dict = {'condition' : condition, 'muscle' : muscle}
            for snippet_name, data in emg_data.items():
                avg_name = f'emg_avg_{muscle}'
                emg_dict[snippet_name] = data[avg_name]
            emg_dict_list.append(emg_dict)

    df = pd.DataFrame(emg_dict_list)
    df.to_csv(emg_averages_pathname)


if __name__ == '__main__':
    process_subject()
