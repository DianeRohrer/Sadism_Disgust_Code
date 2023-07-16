#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Sun Jul 16 14:48:45 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import json
import os
import time

# How many seconds to wait before deciding that the recording computer
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
BASELINE_DURATION = 30

# These are for tracking when recording starts
# so that we can measure how long it actually happened
RECORDING_STARTED = 0

# All these settings tell Python where to find the RCS program
# running on the recording computer.
WORKSPACE = "C:/Vision/Workfiles/workspaces/Sadism Disgust.rwksp"
HOST = "129.64.55.213"
PORT = 6700
AMPLIFIER = "BrainAmp Family"

# Read in the list of opponents for this subject.
# This reads the text file where they are stored,
# and reads them in as a Python list.
with open(os.path.join("data", "disgust_images.txt"), "rt") as f:
    disgust_image_paths = json.loads(f.read())

print(type(disgust_image_paths))

'''
# Do the same procedure with emotion names and filenames.
# First read in the entire list.
with open(os.path.join("data", "emotions_A.txt"), "rt") as f:
    emotions = json.loads(f.read())

# Create empty lists for the names and filenames.
emotion_names = []
emotion_filenames = []

# Break out the names and filenames into their own lists.
for emotion in emotions:
    emotion_names.append(emotion[0])
    emotion_filenames.append(emotion[1])

# Read in the list of tastant phrases.
with open(os.path.join("data", "tastant_phrases_A.txt"), "rt") as f:
    tastant_phrases = list(json.loads(f.read()))

# Read in the list of tastant codes.
with open(os.path.join("data", "tastant_codes_A.txt"), "rt") as f:
    tastant_codes = list(json.loads(f.read()))

# Read in the list of bets (offers).
with open(os.path.join("data", "bets_A.txt"), "rt") as f:
    bets = list(json.loads(f.read()))

# Read in the list of bet (offer) phrases--the long way of saying them.
with open(os.path.join("data", "bet_phrases_A.txt"), "rt") as f:
    bet_phrases = list(json.loads(f.read()))

'''

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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'Visual_Condition'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/hopswork/projects/Sadism_Disgust_Code/Visual_Condition_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Connecting" ---
connecting_message = visual.TextStim(win=win, name='connecting_message',
    text='Connecting to EMG recorder',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Setup_Code" ---

# --- Initialize components for Routine "Sit_Still" ---
textbox = visual.TextBox2(
     win, text='Please relax and sit still for the next 30 seconds', placeholder='Type here...', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textbox',
     depth=0, autoLog=True,
)

# --- Initialize components for Routine "Instructions" ---
instructions = visual.TextStim(win=win, name='instructions',
    text='In this portion of the experiment you will view a series of images and be asked to rate how disgusting you find each image using the scale under the image.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Image" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
disgust_image = visual.ImageStim(
    win=win,
    name='disgust_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Disgust_Score = visual.Slider(win=win, name='Disgust_Score',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=["Not disgusting at all", "Slightly disgusting", "Moderately disgusting, causes me to scrunch up my nose", "Very disgusting, I want to push the image away", "Extremely disgusting, I feel nauseous"], ticks=(0, 1, 2, 3, 4), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, 1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-2, readOnly=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Connecting" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ConnectingComponents = [connecting_message]
for thisComponent in ConnectingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Connecting" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 0.1:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *connecting_message* updates
    
    # if connecting_message is starting this frame...
    if connecting_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        connecting_message.frameNStart = frameN  # exact frame index
        connecting_message.tStart = t  # local t and not account for scr refresh
        connecting_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(connecting_message, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'connecting_message.started')
        # update status
        connecting_message.status = STARTED
        connecting_message.setAutoDraw(True)
    
    # if connecting_message is active this frame...
    if connecting_message.status == STARTED:
        # update params
        pass
    
    # if connecting_message is stopping this frame...
    if connecting_message.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > connecting_message.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            connecting_message.tStop = t  # not accounting for scr refresh
            connecting_message.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'connecting_message.stopped')
            # update status
            connecting_message.status = FINISHED
            connecting_message.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConnectingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Connecting" ---
for thisComponent in ConnectingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.100000)

# --- Prepare to start Routine "Setup_Code" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Setup_CodeComponents = []
for thisComponent in Setup_CodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Setup_Code" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Setup_CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Setup_Code" ---
for thisComponent in Setup_CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Setup_Code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Sit_Still" ---
continueRoutine = True
# update component parameters for each repeat
textbox.reset()
# keep track of which components have finished
Sit_StillComponents = [textbox]
for thisComponent in Sit_StillComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Sit_Still" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    
    # if textbox is starting this frame...
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox.started')
        # update status
        textbox.status = STARTED
        textbox.setAutoDraw(True)
    
    # if textbox is active this frame...
    if textbox.status == STARTED:
        # update params
        pass
    
    # if textbox is stopping this frame...
    if textbox.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textbox.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            textbox.tStop = t  # not accounting for scr refresh
            textbox.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.stopped')
            # update status
            textbox.status = FINISHED
            textbox.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Sit_StillComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Sit_Still" ---
for thisComponent in Sit_StillComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = [instructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    
    # if instructions is starting this frame...
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions.started')
        # update status
        instructions.status = STARTED
        instructions.setAutoDraw(True)
    
    # if instructions is active this frame...
    if instructions.status == STARTED:
        # update params
        pass
    
    # if instructions is stopping this frame...
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions.stopped')
            # update status
            instructions.status = FINISHED
            instructions.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
loop = data.TrialHandler(nReps=63.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop')
thisExp.addLoop(loop)  # add the loop to the experiment
thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in loop:
    currentLoop = loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Image" ---
    continueRoutine = True
    # update component parameters for each repeat
    disgust_image.setImage(disgust_image_paths.pop(0))
    Disgust_Score.reset()
    # keep track of which components have finished
    ImageComponents = [cross, disgust_image, Disgust_Score]
    for thisComponent in ImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Image" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *disgust_image* updates
        
        # if disgust_image is starting this frame...
        if disgust_image.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            disgust_image.frameNStart = frameN  # exact frame index
            disgust_image.tStart = t  # local t and not account for scr refresh
            disgust_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disgust_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'disgust_image.started')
            # update status
            disgust_image.status = STARTED
            disgust_image.setAutoDraw(True)
        
        # if disgust_image is active this frame...
        if disgust_image.status == STARTED:
            # update params
            pass
        
        # *Disgust_Score* updates
        
        # if Disgust_Score is starting this frame...
        if Disgust_Score.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            Disgust_Score.frameNStart = frameN  # exact frame index
            Disgust_Score.tStart = t  # local t and not account for scr refresh
            Disgust_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disgust_Score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Disgust_Score.started')
            # update status
            Disgust_Score.status = STARTED
            Disgust_Score.setAutoDraw(True)
        
        # if Disgust_Score is active this frame...
        if Disgust_Score.status == STARTED:
            # update params
            pass
        
        # Check Disgust_Score for response to end routine
        if Disgust_Score.getRating() is not None and Disgust_Score.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Image" ---
    for thisComponent in ImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop.addData('Disgust_Score.response', Disgust_Score.getRating())
    loop.addData('Disgust_Score.rt', Disgust_Score.getRT())
    # the Routine "Image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 63.0 repeats of 'loop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
