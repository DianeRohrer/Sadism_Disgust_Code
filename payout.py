import json
import os
import pandas as pd

DATA_DIRECTORY = "data"


def main():
    subject_id = get_subject_id()
    total = get_total(subject_id)
    print(f"Total across all rounds is ${total}.")
    print(f"That will buy you {int(total / 10)} lottery tickets.")


def get_subject_id():
    # Get the Subject's ID number from the experimenter.
    print("Enter the subject ID")
    print("and then hit Enter")
    subject_id_input = input()

    # Make sure it's a valid value.
    try:
        subject_id = int(subject_id_input)
    except ValueError:
        print("Subject ID should be a number.")
        print("Maybe give it another go.")
        quit()
    return subject_id


def get_total(subject_id):
    """
    Go through and count up the total of all the accepted offers.
    """
    filenames = get_filenames(subject_id)

    # Open the file that has all the data collected for this subject
    # for this condition.
    success = False
    longest_df = 0
    df = None
    for filename in filenames:
        try:
            this_df = pd.read_csv(filename)
            df_length = len(this_df.index)
            if df_length >= longest_df:
                df = this_df
                longest_df = df_length
            success = True
        except Exception:
            pass

    # If it doesn't work, send a note to the experimenter.
    if not success:
        print(
            f"I had trouble reading the data file for Condition {condition}."
        )
        return None

    condition_total = 0
    # If the data file was successfully read, go through and tally up
    # accepted offers.
    # Pull out all the "offer_choice" entries from the data file.
    offer_keys = df.loc[
        df.loc[:, "offer_choice.keys"].notnull(), "offer_choice.keys"
    ]

    # Read in the file with the list of offers made to this subject
    # in this condition.
    with open(
        os.path.join("data", f"bets_{subject_id}.txt"), "rt"
    ) as f:
        offers = json.loads(f.read())

    # Check each of the accept/reject keypresses.
    for i_round, key in enumerate(offer_keys):
        # Find all the "up" keypresses.
        if key == "up":
            # Accumulate the total accepted.
            condition_total += int(offers[i_round][1])

    return condition_total


def get_filenames(subject_id):
    filenames = os.listdir(DATA_DIRECTORY)
    condition = "Moral"
    matching_filenames = []
    for filename in filenames:
        pathname = os.path.join(DATA_DIRECTORY, filename)
        if (pathname.__contains__(str(subject_id))
            and pathname.__contains__(condition)
            and pathname.__contains__(".csv")
        ):
            matching_filenames.append(pathname)
    # Put the filenames in alphabetical order.
    # Because of how they're named, this ensures that the
    # newest runs will be tested last.
    matching_filenames.sort()
    return matching_filenames


main()
