import json
import os
import time

# BEFORE RUNNING THIS, start up RCS manually on the recording computer.
# And make sure that the BrainVision Recorder is open and running too.

# If we're testing at home, we want to be able to run through the
# experiments with just pretend EMG recording.
# But if we're in the lab, we absolutely want to stop everything
# if there's a problem with the EMG recording and figure out what's wrong.
TESTING_AT_HOME = True

# How many seconds to wait before deciding that the recording computer
# can't be reached.
TIMEOUT = 4

# How many seconds to spend collecting a baseline EMG measurement.
# During the actual experiment this will be 60 seconds.
# While we're still testing things, it's convenient to have this
# be shorter so we don't have to wait so long each time the experiment runs.
BASELINE_DURATION = 20

# These are for tracking when recording starts
# so that we can measure how long it actually happened
RECORDING_STARTED = 0

# All these settings tell Python where to find the RCS program
# running on the recording computer.
WORKSPACE = "C:/Vision/Workfiles/Sadism Disgust.rwksp"
HOST = "172.20.71.7"
PORT = 6700
AMPLIFIER = "BrainAmp Family"

expInfo['session'] = "Moral"

# Read in the list of opponents for this subject.
# This reads the text file where they are stored,
# and reads them in as a Python list.
subject_id = expInfo['participant']
# with open(os.path.join("data", "opponents.txt"), "rt") as f:
with open(os.path.join("data", f"opponents_{subject_id}.txt"), "rt") as f:
    opponents = json.loads(f.read())

# Create empty lists for both the opponents' names
# and the filenames where their images are stored.
opponent_names = []
opponent_filenames = []

# Go through the list of opponent information.
for opponent in opponents:
    # Each item in the opponent list is a tuple with two parts:
    # the opponent's name and their image filename.
    # Break out the name and add it to the list of names.
    opponent_names.append(opponent[0])
    # Break out the filename and add it to the list of filenames.
    opponent_filenames.append(opponent[1])

# Do the same procedure with emotion names and filenames.
# First read in the entire list.
# with open(os.path.join("data", "emotions.txt"), "rt") as f:
with open(os.path.join("data", f"emotions_{subject_id}.txt"), "rt") as f:
    emotions = json.loads(f.read())

# Create empty lists for the names and filenames.
emotion_names = []
emotion_filenames = []

# Break out the names and filenames into their own lists.
for emotion in emotions:
    emotion_names.append(emotion[0])
    emotion_filenames.append(emotion[1])

# Read in the list of bets (offers).
# with open(os.path.join("data", "bets.txt"), "rt") as f:
with open(os.path.join("data", f"bets_{subject_id}.txt"), "rt") as f:
    bets = list(json.loads(f.read()))

# Read in the list of bet (offer) phrases--the long way of saying them.
# with open(os.path.join("data", "bet_phrases.txt"), "rt") as f:
with open(os.path.join("data", f"bet_phrases_{subject_id}.txt"), "rt") as f:
    bet_phrases = list(json.loads(f.read()))


# Connect to the Brain Products Remote Control Server
# API documentation at
# https://www.psychopy.org/api/hardware/brainproducts.html

# Try to connect to the computer running BrainProducts Recorder.
try:
    from psychopy.hardware import brainproducts
    RCS = brainproducts.RemoteControlServer(
        host=HOST,
        port=PORT,
        timeout=TIMEOUT,
    )

    # If connection is successful, print a little notification.
    print("INFO:")
    print("RCS connection SUCCESSFUL, EMG will be recorded.")
    print()

    # If you ever wanted to the Recorder remotely, you can do it with
    # these lines. We're not doing this, because we want to give the
    # experimenter a little more control.
    # RCS.openRecorder()
    # time.sleep(2)

except Exception:
    # If we're at home and
    # if connection isn't successful, assume the experiment is going to run
    # in test mode with dummy commands and responses.
    if TESTING_AT_HOME:
        print("INFO:")
        print("RCS connection wasn't successful.")
        print("Running in MOCK recording mode.")
        print()
        RCS = None
    else:
        # If we're in the lab, make sure to loudly fail with
        # an error message so we can try to figure out what's wrong.
        raise Exception

# If the connection is successful, get the EMG recording set up.
if RCS is not None:
    # Provide the type of amplifier (with serial number when using LiveAmp).
    RCS.amplifier = AMPLIFIER

    # Turn overwrite protection on.
    RCS.overwriteProtection = True

    # Start monitoring (this will wait for a positive confirmation or timeout)
    # RCS automatically starts up in "default" mode, but we'll set it
    # here just to play it safe.
    RCS.mode = "default"
    # Just sit and wait for one second.
    # These seem to be necessary in order to give the recorder time
    # to process the commands.
    time.sleep(1)

    # Perform a DC reset.
    # This is only necessary if you're NOT going to do a high-pass filter
    # step on the data later.
    # We are going to high-pass filter, so we don't need to do this part
    # RCS.dcReset()
    # time.sleep(1)

    # Tell RCS where to set up the workspace.
    RCS.workspace = WORKSPACE
    # `expName` (the name of the experiment) and
    # `expInfo` (a variable with the experiment information)
    # will already be defined in the psychopy code.
    RCS.expName = expName  # NoQA: F821
    # Pull out the participant name from `expInfo`.
    RCS.participant = f"{expInfo['participant']}"  # NoQA: F821
    time.sleep(1)

    # Switch the recorder over to monitoring mode.
    # This means it's ready to start recording.
    RCS.mode = "monitor"
    time.sleep(1)

    # Start up the recording, give it a couple seconds to
    # settle in, then pause it so that it's ready to go
    # for the rest of the experiment.
    RCS.startRecording()
    time.sleep(2)
    RCS.pauseRecording()
    time.sleep(1)


def start_EMG_recording(annotation=None):
    # Keep track of when this snippet of EMG started recording.
    recording_start_time = time.time()
    # Set up the annotation.
    if annotation is None:
        # If the annotataion wasn't provided, note
        # the recording start time.
        annotation = f"recording started at {int(recording_start_time)}"
    annotation_type = "start"

    # If there is no recording going on, do mock recording,
    # showing some pretend messages in the psychopy run window.
    if RCS is None:
        print()
        print("MOCK:  Pretend EMG recording started")
        print(f"MOCK:  Annotated '{annotation}, {annotation_type}'")

    else:
        # Restart the recording and annotate it.
        RCS.resumeRecording()
        RCS.sendAnnotation(annotation, annotation_type)

    return recording_start_time


def stop_EMG_recording(recording_stop_time):
    # Note when the snippet stopped recording and
    # calculate how long it has been recording.
    recording_stop_time = time.time()
    duration = recording_stop_time - RECORDING_STARTED

    # If there is no recording going on, do mock recording,
    # showing some pretend messages on the console.
    if RCS is None:
        print()
        print("MOCK:  Pretend EMG recording stopped")
        print(f"MOCK:  {duration} seconds of fake EMG recorded")

    else:
        # Pause the recording.
        RCS.pauseRecording()
