import json
import os

import numpy as np
import pandas as pd

from artifact_cleanup import process_subject
from file_tools import get_directories, get_log_filenames


def main():
    data_directory, _ = get_directories()
    local_data_directory = "data"

    print(data_directory)
    # Generate list of all subject IDs
    filenames = os.listdir(data_directory)
    subject_ids = []
    valid_subject_ids_path = os.path.join("data", "valid_subject_ids.txt")
    with open(valid_subject_ids_path, "rt") as f:
        valid_ids = list(json.loads(f.read()))
        for filename in filenames:
            if filename[-4:] == ".eeg":
                filename_parts = filename.split("_")
                # condition = filename_parts[1]
                subject_id = filename_parts[0]
                if subject_id in valid_ids:
                    subject_ids.append(subject_id)

    '''
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
    '''
    # Iterate through subject IDs and compile them into a single csv.
    filenames = os.listdir(data_directory)
    summary_filename = "all_emg_data.csv"
    all_subjects_averages = {
        "moral": {},
        "gustatory": {},
        "visual": {},
        "dsr": {},
    }
    for filename in filenames:
        if "emg_averages" in filename:
            print(f"Merging {filename}")
            pathname = os.path.join(data_directory, filename)
            df = pd.read_csv(pathname)
            subject_id = filename.split("_")[0]

            if subject_id not in valid_ids:
                continue

            condition = filename.split('_')[1]

            if condition == "visual":
                '''
                print(df)
                print(df.loc[df.loc[:, "label"].isin(["con", "cor", "ar"]), "emg_avg_norm"] )
                print(df.loc[df.loc[:, "label"].isin(["con", "cor", "ar"]), "emg_avg_norm"].mean() )
                print(df.loc[df.loc[:, "label"] == "ar", "emg_avg_norm"] )
                print(df.loc[df.loc[:, "label"] == "ar", "emg_avg_norm"].mean() )
                print(df.loc[df.loc[:, "label"] == "con", "emg_avg_norm"] )
                print(df.loc[df.loc[:, "label"] == "con", "emg_avg_norm"].mean() )
                print(df.loc[df.loc[:, "label"] == "cor", "emg_avg_norm"])
                print(df.loc[df.loc[:, "label"] == "cor", "emg_avg_norm"].mean() )
                print(condition)
                '''
                emg_avg = df.loc[
                    df.loc[:, "label"].isin(["con", "cor", "ar"]),
                    "emg_avg_norm"
                ].mean()
                all_subjects_averages["visual"][subject_id] = emg_avg

            if condition == "gustatory":
                emg_avg = df.loc[
                    df.loc[:, "label"].isin(["hq"]),
                    "emg_avg_norm"
                ].mean()
                all_subjects_averages["gustatory"][subject_id] = emg_avg

            if condition == "moral":
                emg_avg = df.loc[
                    df.loc[:, "label"].isin([91, 82]),
                    "emg_avg_norm"
                ].mean()
                all_subjects_averages["moral"][subject_id] = emg_avg

    # Add in DSR scores
    filename = "dsr_items.csv"
    pathname = os.path.join("data", filename)
    dsr_df = pd.read_csv(pathname)
    for i, row in dsr_df.iterrows():
        # print(row)
        # print(row.values)
        # print("subject id", row.values[-1])
        # print("dsr", np.sum(row.values[:-1]))
        subject_id = str(row.values[-1])
        dsr = np.sum(row.values[:-1])
        all_subjects_averages["dsr"][subject_id] = dsr

    df_all = pd.DataFrame(all_subjects_averages)
    df_all.to_csv(
        os.path.join(data_directory, summary_filename),
        columns = ["gustatory", "visual", "moral", "dsr"],
    )

    """
    # Iterate through subject IDs and compile them into a single csv.
    filenames = os.listdir(data_directory)
    summary_filename = "all_emg_data.csv"
    all_subjects_df = None
    for filename in filenames:
        if "emg_averages" in filename:
            print(f"Merging {filename}")
            pathname = os.path.join(data_directory, filename)
            df = pd.read_csv(pathname)
            subject_id = filename.split("_")[0]

            if subject_id not in valid_ids:
                continue

            new_names = {
                "spit_0": "tastant_1_emg",
                "spit_1": "tastant_2_emg",
                "spit_2": "tastant_3_emg",
                "spit_3": "tastant_4_emg",
                "spit_4": "tastant_5_emg",
                "spit_5": "tastant_6_emg",
                "accept_00": "game_01_emg",
                "accept_01": "game_02_emg",
                "accept_02": "game_03_emg",
                "accept_03": "game_04_emg",
                "accept_04": "game_05_emg",
                "accept_05": "game_06_emg",
                "accept_06": "game_07_emg",
                "accept_07": "game_08_emg",
                "accept_08": "game_09_emg",
                "accept_09": "game_10_emg",
                "accept_10": "game_11_emg",
                "accept_11": "game_12_emg",
            }
            df = df.rename(columns=new_names)
            df["subject_id"] = subject_id
            df["index"] = df[["subject_id", "condition", "muscle"]].agg(
                "_".join, axis=1
            )

            # Per tastant
            # Add tastant type
            for condition in ["A", "B", "C"]:
                tastant_codes_filename = (
                    "_".join(["tastant", "codes", condition, subject_id])
                    + ".txt"
                )
                tastant_codes_path = os.path.join(
                    "data", tastant_codes_filename
                )
                with open(tastant_codes_path, "rt") as f:
                    tastants = list(json.loads(f.read()))
                    name = {
                        "e": "quinine",
                        "p": "sucrose",
                        "w": "water",
                    }
                    for i_tastant, code in enumerate(tastants):
                        df.loc[
                            (df.loc[:, "subject_id"] == subject_id)
                            & (df.loc[:, "condition"] == condition),
                            f"tastant_{i_tastant + 1}",
                        ] = name[code]

            # Per game
            # Add bet
            for condition in ["A", "B", "C"]:
                bet_codes_filename = (
                    "_".join(["bets", condition, subject_id]) + ".txt"
                )
                bet_codes_path = os.path.join("data", bet_codes_filename)
                with open(bet_codes_path, "rt") as f:
                    bets = list(json.loads(f.read()))
                    for i_game, bet in enumerate(bets):
                        df.loc[
                            (df.loc[:, "subject_id"] == subject_id)
                            & (df.loc[:, "condition"] == condition),
                            f"game_{i_game + 1:02d}_bet",
                        ] = bet

                # Add acceptance
                # Add emotion rating
                # Add subjective rating
                log_filename = get_log_filenames(
                    subject_id, condition, local_data_directory
                )

                if log_filename is None:
                    print(
                        "No .csv log file found for "
                        + f"{subject_id}, Condition {condition}"
                    )
                    continue

                log_df = pd.read_csv(log_filename)
                moral_disgust_score = log_df.loc[
                    np.logical_not(
                        np.isnan(log_df.loc[:, "Moral_Disgust_Score.response"])
                    ),
                    "Moral_Disgust_Score.response",
                ]

                for i_game, moral_disgust in enumerate(
                    list(moral_disgust_score)
                ):
                    df.loc[
                        (df.loc[:, "subject_id"] == subject_id)
                        & (df.loc[:, "condition"] == condition),
                        f"game_{i_game + 1:02d}_moral_disgust",
                    ] = moral_disgust

                emotions_filename = (
                    "_".join(["emotions", condition, subject_id]) + ".txt"
                )
                emotions_path = os.path.join("data", emotions_filename)
                with open(emotions_path, "rt") as f:
                    emotions_long = list(json.loads(f.read()))
                    emotions = [e[0] for e in emotions_long]

                face_affinity_score = np.array(
                    log_df.loc[
                        np.logical_not(
                            np.isnan(log_df.loc[:, "AffinityScore.response"])
                        ),
                        "AffinityScore.response",
                    ]
                )

                for i_game in range(12):
                    for i_emotion in range(7):
                        i_row = i_game * 7 + i_emotion
                        if emotions[i_row] == "disgust":
                            df.loc[
                                (df.loc[:, "subject_id"] == subject_id)
                                & (df.loc[:, "condition"] == condition),
                                f"game_{i_game + 1:02d}_disgust_affinity",
                            ] = face_affinity_score[i_row]

            # Choose the order of the columns.
            try:
                df = df.loc[
                    :,
                    [
                        "index",
                        "subject_id",
                        "condition",
                        "muscle",
                        "baseline",
                        "tastant_1",
                        "tastant_2",
                        "tastant_3",
                        "tastant_4",
                        "tastant_5",
                        "tastant_6",
                        "tastant_1_emg",
                        "tastant_2_emg",
                        "tastant_3_emg",
                        "tastant_4_emg",
                        "tastant_5_emg",
                        "tastant_6_emg",
                        "game_01_bet",
                        "game_02_bet",
                        "game_03_bet",
                        "game_04_bet",
                        "game_05_bet",
                        "game_06_bet",
                        "game_07_bet",
                        "game_08_bet",
                        "game_09_bet",
                        "game_10_bet",
                        "game_11_bet",
                        "game_12_bet",
                        "game_01_emg",
                        "game_02_emg",
                        "game_03_emg",
                        "game_04_emg",
                        "game_05_emg",
                        "game_06_emg",
                        "game_07_emg",
                        "game_08_emg",
                        "game_09_emg",
                        "game_10_emg",
                        "game_11_emg",
                        "game_12_emg",
                        "game_01_moral_disgust",
                        "game_02_moral_disgust",
                        "game_03_moral_disgust",
                        "game_04_moral_disgust",
                        "game_05_moral_disgust",
                        "game_06_moral_disgust",
                        "game_07_moral_disgust",
                        "game_08_moral_disgust",
                        "game_09_moral_disgust",
                        "game_10_moral_disgust",
                        "game_11_moral_disgust",
                        "game_12_moral_disgust",
                        "game_01_disgust_affinity",
                        "game_02_disgust_affinity",
                        "game_03_disgust_affinity",
                        "game_04_disgust_affinity",
                        "game_05_disgust_affinity",
                        "game_06_disgust_affinity",
                        "game_07_disgust_affinity",
                        "game_08_disgust_affinity",
                        "game_09_disgust_affinity",
                        "game_10_disgust_affinity",
                        "game_11_disgust_affinity",
                        "game_12_disgust_affinity",
                    ],
                ]

                if all_subjects_df is None:
                    all_subjects_df = df
                else:
                    all_subjects_df = pd.concat([all_subjects_df, df])
            except KeyError:
                print(f"Subject {subject_id} seems to be missing some data.")

    all_subjects_df.to_csv(os.path.join(data_directory, summary_filename))

    n_subjects_allowed = len(valid_ids)
    included_ids = list(all_subjects_df["subject_id"].unique())
    n_subjects_included = len(included_ids)
    print(
        f"Of {n_subjects_allowed} subjects with valid ids, "
        + f"{n_subjects_included} were included in the final data file"
    )
    for valid_id in valid_ids:
        if valid_id not in included_ids:
            print(f"Subject {valid_id} was not included")
    for included_id in included_ids:
        if included_id not in valid_ids:
            print(f"Subject {included_id} should not have been included")
    """


if __name__ == "__main__":
    main()
