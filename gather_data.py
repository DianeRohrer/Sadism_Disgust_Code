import json
import os

import numpy as np
import pandas as pd

from artifact_cleanup import process_subject
from file_tools import get_directories, get_log_filenames


def main():
    data_directory, _ = get_directories()
    local_data_directory = "data"

    # Generate list of all subject IDs
    filenames = os.listdir(data_directory)
    subject_ids = []

    # When testing, use just a single subject to make it run faster
    # valid_subject_ids_path = os.path.join("data", "valid_subject_ids_test.txt")
    valid_subject_ids_path = os.path.join("data", "valid_subject_ids.txt")
    with open(valid_subject_ids_path, "rt") as f:
        valid_ids = list(json.loads(f.read()))
        print("valid ids", valid_ids)
        for filename in filenames:
            if filename[-4:] == ".eeg":
                filename_parts = filename.split("_")
                # condition = filename_parts[1]
                subject_id = filename_parts[0]
                if subject_id in valid_ids:
                    subject_ids.append(subject_id)

    for subject_id in subject_ids:
        print(f"Extracting EMG signals from subject {subject_id}")
        try:
            process_subject(subject_id=subject_id, turn_off_plots=True)
        except FileNotFoundError as e:
            print(e)
            print(
                f"It looks like video for subject {subject_id} "
                + "hasn't been reviewed for artifacts yet."
            )
            continue
        except AssertionError as e:
            print(e)
            continue

    # Iterate through all muscles, and create a separate csv for each.
    for muscle in ["cor", "mas", "ll", "zyg"]:

        baseline = "pretrial"
        # TODO: include baseline calculated during fixation cross.

        # Iterate through subject IDs and compile them
        filenames = os.listdir(data_directory)
        summary_filename = f"all_emg_{muscle}_{baseline}.csv"
        # `all_subjects_averages` is a dict of dicts where
        # top level key is the column name and snippet label.
        # They key to each sub-dict is a subjectid, and its value
        # is the average EMG. (Except in the case of the DSR.)
        all_subjects_averages = {
            "91": {},
            "82": {},
            "73": {},
            "55": {},
            "hs": {},
            "ls": {},
            "hq": {},
            "lq": {},
            "w": {},
            "n": {},
            "cor": {},
            "con": {},
            "ar": {},
            "dsr": {},
        }
        for filename in filenames:
            if f"_{muscle}_emg_averages" in filename:
                pathname = os.path.join(data_directory, filename)
                df = pd.read_csv(pathname)
                subject_id = filename.split("_")[0]

                if subject_id not in valid_ids:
                    continue

                print(f"Merging {filename}")

                condition = filename.split('_')[1]

                if condition == "visual":
                    for snippet_label in ["ar", "con", "cor", "n"]:
                        all_subjects_averages[snippet_label][subject_id] = df.loc[
                            df.loc[:, "label"] == snippet_label, "emg_avg_norm"
                        ].mean()

                if condition == "gustatory":
                    for snippet_label in ["hs", "ls", "hq", "lq", "w"]:
                        all_subjects_averages[snippet_label][subject_id] = df.loc[
                            df.loc[:, "label"] == snippet_label, "emg_avg_norm"
                        ].mean()

                if condition == "moral":
                    for snippet_label in [55, 73, 82, 91]:
                        all_subjects_averages[str(snippet_label)][subject_id] = df.loc[
                            df.loc[:, "label"] == snippet_label, "emg_avg_norm"
                        ].mean()

        # Add in DSR scores
        filename = "dsr_items.csv"
        pathname = os.path.join("data", filename)
        dsr_df = pd.read_csv(pathname)
        for i, row in dsr_df.iterrows():
            subject_id = str(row.values[-1])
            if subject_id in subject_ids:
                dsr = np.sum(row.values[:-1])
                all_subjects_averages["dsr"][subject_id] = dsr

        print(all_subjects_averages)

        df_all = pd.DataFrame(all_subjects_averages)
        df_all.to_csv(os.path.join(data_directory, summary_filename))


if __name__ == "__main__":
    main()
