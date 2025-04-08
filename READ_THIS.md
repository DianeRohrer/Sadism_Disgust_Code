# Sadism Disgust Code
====================

Pyschopy files, Python scripts, and data for the Moral Disgust study.
Talk with Diane Rohrer (drohrer@brandeis.edu) to learn more.


## Useful files
---------------

* `run_first.py` Run this before running a subject to prepare the
randomization order for them. Run with
```
python3 run_first.py
```
and you'll be prompted to add the subject ID.

* `payout.py` Run this after the subject has completed their run
in order to calculate the payout to them in lottery tickets. Run with
```
python3 payout.py
```
and you'll be prompted to add the subject ID.

* `angelatron_2.py` Visualize the time series and frequency distribution
of EMG data with events and sections added in. Run with
```
python3 angelatron_2.py
```
and you'll be prompted to add the subject ID.

* `artifact_cleanup.py` Using EMG data and annotations from video,
isolate EMG segments, remove any artifacts present, and average the
portion of interest. For example with fictitous subject 999,
run at the command line with
```
python3 artifact_cleanup.py 999
```
This generates plots of the EMG measured for each portion of
each condition and trial, with the artifact sections shaded.
The resulting EMG averages are stored back in the Box directory
in the format `999_emg_averages.csv`.

* `gather_data.py` Collect the extracted and processed EMG data
for all subjects and compile it into a single file called `all_emg_data.csv`.

* `Gustatory_Condition_v2.psyexp`
* `MoralCondition_v2.psyexp`
* `Visual_Condition_v2.psyexp`
The files that define the Psychopy experiments.
There are also some scripts with copies of the code that is included in
the Psychopy experiments.

  * and `*_lastrun.py` records the actual script
  generated on the most recent run.
  
* There are also some helper code that gets called by the other scripts.

  * `file_tools.py`
  * `plot_emg.py`
  * `processing_steps.py`

## Preparing video annotation data

This example is for subject with ID 9978.

1. In the Sadism Disgust Data Cleaning
[spreadsheet](https://docs.google.com/spreadsheets/d/100dUkdengbKxAaEwLbpFWtlfuiY3I9IZlghmAsHYuSE/edit?gid=0#gid=0)
find the tab labeled `Subject 9978`.

2. Export this this tab with the menu selections `File` -> `Download` ->
`Comma-Separated Values (.csv)`

3. This will save a csv version of this subject 9978's annotations to the
default Downloads directory with a name like
`Sadism Disgust Data Cleaning - Subject 9978.csv`

4. Change the name to `artifacts_9978.csv`

5. Move the file to where the Box files are stored on your computer.
For example on The Morrigan this would have been
`/Users/themorrigan/Library/CloudStorage/Box-Box/Sadism Disgust Study`


## Collecting experiment logs

The log files contain the results of the PsychoPy experiment, including
moral disgust ratings and affinity scores for the emotion faces.

1. On the participant computer, in the GitHub app
commit all the newly created data
files by adding a short summary message and clicking the
"Commit to main" button.

2. On the participant computer in the GitHub app
"Fetch origin" and "Pull origin"
to bring all the participant computer's files up to date.

3. On the participant computer in the Github app "Push to origin"
to upload new data files.

4. On Aidas or Asher in the GitHub app "Fetch origin" and "Pull origin"
to download the new data files.


## Update the list of Subject IDs to be included in this pass.

1. Open `data/valid_subject_ids.txt`

2. Add and remove IDs to until it is only the list of subjects you want to 
include in this analysis

TODO walk through `gather_data.py`
## Gathering annotated data

To collect all of the `artifacts_####.csv` files from all the subjects,
run at the command line

```
python3 gather_data.py
```

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


## Analyzing the collected data

1. On The Morrigan copy `all_emg_data.csv` from the Box directory
to `Desktop/Moral_Disgust_data`.

2. In RStudio pull up `MoralDisgust.R` and run it.

