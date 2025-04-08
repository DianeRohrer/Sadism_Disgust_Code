# Pipeline Instructions
----------------------------

## Update the local repository

- On Asher open up the GutHub app
- Click on the `Sadism_disgust_code` repository if it isn't already open
- Click "Pull origin"
- Click "Push origin" if it's offered

## Update the list of subjects to be processed

- Open file `Sadism_Disgust_Code/data/valid_subject_ids.txt`
    - Right click
    - Open with "TextEdit"
- Add any subject IDs that need to be added to the list
    - Between quotes
    - Followed by a comma
- Save the file

## Run the subjects through the pipeline

- Open a Terminal window
- Type and run `cd ~/Desktop/Sadism_Disgust_Code`
- Type and run `python3 gather_data.py`

This will loop through all the subjects for which EMG data and artifacts
files exist and
1. read in their experiment logs,
2. isolate the EMG segments from each muscle for each condition and portion
of the experiment,
3. filter the EMG signal, remove any artifacts, and calculate its average,
4. record the average EMG together with information about the type
of offer made, the emotion affinity scores, and the participant's moral
judgment score,
5. save the result as `all_emg_data.csv` in the Box directory.

## Use the results

- On Asher Box directory `Sadism Disgust Study`, download `all_emg_data.csv`
- Move `all_emg_data.csv` to `Desktop/Diss_Data`.
- In RStudio pull up `MoralDisgust.R` and run it.
