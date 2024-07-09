#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on July 09, 2024, at 18:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'MoralCondition_v2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\simla\\OneDrive\\Desktop\\Sadism_Disgust_Code\\MoralCondition_v2_lastrun.py',
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
    size=[1728, 1117], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-0.5, -0.5, -0.5], colorSpace='rgb',
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

# --- Initialize components for Routine "Setup_Code" ---

# --- Initialize components for Routine "Sync_Beeps" ---
sync_beep_1 = sound.Sound('400', secs=0.3, stereo=True, hamming=True,
    name='sync_beep_1')
sync_beep_1.setVolume(1.0)
sync_beep_2 = sound.Sound('400', secs=0.3, stereo=True, hamming=True,
    name='sync_beep_2')
sync_beep_2.setVolume(1.0)
sync_beep_3 = sound.Sound('400', secs=0.3, stereo=True, hamming=True,
    name='sync_beep_3')
sync_beep_3.setVolume(1.0)
sync_beep_4 = sound.Sound('400', secs=0.3, stereo=True, hamming=True,
    name='sync_beep_4')
sync_beep_4.setVolume(1.0)
p_port = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Sit_Still" ---
baseline = visual.TextBox2(
     win, text='Please relax and sit still for the next 15 seconds.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='baseline',
     autoLog=True,
)
p_port_2 = parallel.ParallelPort(address='0x3FF8')
p_port_3 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Game_Start" ---
Game_Start_Text = visual.TextStim(win=win, name='Game_Start_Text',
    text='Press the spacebar to start the game. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
p_port_4 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Fixation_Cross" ---
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
p_port_5 = parallel.ParallelPort(address='0x3FF8')
p_port_6 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Opponent" ---
player_image_intro = visual.ImageStim(
    win=win,
    name='player_image_intro', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.75, .5), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
player_name_intro = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.75, .5),units='norm',     letterHeight=0.08,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='player_name_intro',
     autoLog=True,
)
p_port_7 = parallel.ParallelPort(address='0x3FF8')
p_port_8 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Offer" ---
player_image_offer = visual.ImageStim(
    win=win,
    name='player_image_offer', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.75, .5), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
player_name_offer = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.75, .5),units='norm',     letterHeight=0.08,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='player_name_offer',
     autoLog=True,
)
proposed_split = visual.TextStim(win=win, name='proposed_split',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
accept_reject = visual.TextStim(win=win, name='accept_reject',
    text='Do you accept or reject this offer?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
p_port_9 = parallel.ParallelPort(address='0x3FF8')
p_port_10 = parallel.ParallelPort(address='0x3FF8')
p_port_15 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Arrows" ---
arrow_instructions = visual.TextStim(win=win, name='arrow_instructions',
    text='Press the "up" arrow to accept\n\nPress the "down" arrow to reject',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
offer_choice = keyboard.Keyboard()
p_port_11 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Non_Verbal_Instructions" ---
Instructions_Affinity_Score = visual.TextStim(win=win, name='Instructions_Affinity_Score',
    text='Please rate on the following scale how well each face captures your feelings about the offer you received. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
p_port_12 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neutral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, 1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)
p_port_13 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Verbal" ---
Instruction = visual.TextStim(win=win, name='Instruction',
    text='Please rate on the following scale how morally wrong you felt the offer you received was. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Moral_Disgust_Score = visual.Slider(win=win, name='Moral_Disgust_Score',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=("Extremely Immoral", "Immoral", "Somewhat Immoral", "Neutral", "Somewhat Moral", "Moral", "Extremely Moral"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, 1.0000], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)
p_port_14 = parallel.ParallelPort(address='0x3FF8')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Setup_Code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
import json

expInfo['session'] = "Moral"

# Read in the list of opponents for this subject.
# This reads the text file where they are stored,
# and reads them in as a Python list.
subject_id = expInfo['participant']
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
with open(os.path.join("data", f"bets_{subject_id}.txt"), "rt") as f:
    bets = list(json.loads(f.read()))

# Read in the list of bet (offer) phrases--the long way of saying them.
with open(os.path.join("data", f"bet_phrases_{subject_id}.txt"), "rt") as f:
    bet_phrases = list(json.loads(f.read()))
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

# --- Prepare to start Routine "Sync_Beeps" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sync_beep_1.setSound('400', secs=0.3, hamming=True)
sync_beep_1.setVolume(1.0, log=False)
sync_beep_2.setSound('400', secs=0.3, hamming=True)
sync_beep_2.setVolume(1.0, log=False)
sync_beep_3.setSound('400', secs=0.3, hamming=True)
sync_beep_3.setVolume(1.0, log=False)
sync_beep_4.setSound('400', secs=0.3, hamming=True)
sync_beep_4.setVolume(1.0, log=False)
# keep track of which components have finished
Sync_BeepsComponents = [sync_beep_1, sync_beep_2, sync_beep_3, sync_beep_4, p_port]
for thisComponent in Sync_BeepsComponents:
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

# --- Run Routine "Sync_Beeps" ---
while continueRoutine and routineTimer.getTime() < 2.1:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sync_beep_1
    if sync_beep_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_1.frameNStart = frameN  # exact frame index
        sync_beep_1.tStart = t  # local t and not account for scr refresh
        sync_beep_1.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_1.started', tThisFlipGlobal)
        sync_beep_1.play(when=win)  # sync with win flip
    if sync_beep_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_1.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_1.tStop = t  # not accounting for scr refresh
            sync_beep_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_1.stopped')
            sync_beep_1.stop()
    # start/stop sync_beep_2
    if sync_beep_2.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_2.frameNStart = frameN  # exact frame index
        sync_beep_2.tStart = t  # local t and not account for scr refresh
        sync_beep_2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_2.started', tThisFlipGlobal)
        sync_beep_2.play(when=win)  # sync with win flip
    if sync_beep_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_2.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_2.tStop = t  # not accounting for scr refresh
            sync_beep_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_2.stopped')
            sync_beep_2.stop()
    # start/stop sync_beep_3
    if sync_beep_3.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_3.frameNStart = frameN  # exact frame index
        sync_beep_3.tStart = t  # local t and not account for scr refresh
        sync_beep_3.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_3.started', tThisFlipGlobal)
        sync_beep_3.play(when=win)  # sync with win flip
    if sync_beep_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_3.tStop = t  # not accounting for scr refresh
            sync_beep_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_3.stopped')
            sync_beep_3.stop()
    # start/stop sync_beep_4
    if sync_beep_4.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_4.frameNStart = frameN  # exact frame index
        sync_beep_4.tStart = t  # local t and not account for scr refresh
        sync_beep_4.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_4.started', tThisFlipGlobal)
        sync_beep_4.play(when=win)  # sync with win flip
    if sync_beep_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_4.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_4.tStop = t  # not accounting for scr refresh
            sync_beep_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_4.stopped')
            sync_beep_4.stop()
    # *p_port* updates
    if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p_port.frameNStart = frameN  # exact frame index
        p_port.tStart = t  # local t and not account for scr refresh
        p_port.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('p_port.started', t)
        p_port.status = STARTED
        win.callOnFlip(p_port.setData, int(11))
    if p_port.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            p_port.tStop = t  # not accounting for scr refresh
            p_port.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('p_port.stopped', t)
            p_port.status = FINISHED
            win.callOnFlip(p_port.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Sync_BeepsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Sync_Beeps" ---
for thisComponent in Sync_BeepsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sync_beep_1.stop()  # ensure sound has stopped at end of routine
sync_beep_2.stop()  # ensure sound has stopped at end of routine
sync_beep_3.stop()  # ensure sound has stopped at end of routine
sync_beep_4.stop()  # ensure sound has stopped at end of routine
if p_port.status == STARTED:
    win.callOnFlip(p_port.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.100000)

# --- Prepare to start Routine "Sit_Still" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
baseline.reset()
# keep track of which components have finished
Sit_StillComponents = [baseline, p_port_2, p_port_3]
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
while continueRoutine and routineTimer.getTime() < 15.1:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baseline* updates
    if baseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        baseline.frameNStart = frameN  # exact frame index
        baseline.tStart = t  # local t and not account for scr refresh
        baseline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(baseline, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'baseline.started')
        baseline.setAutoDraw(True)
    if baseline.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > baseline.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            baseline.tStop = t  # not accounting for scr refresh
            baseline.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline.stopped')
            baseline.setAutoDraw(False)
    # *p_port_2* updates
    if p_port_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p_port_2.frameNStart = frameN  # exact frame index
        p_port_2.tStart = t  # local t and not account for scr refresh
        p_port_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p_port_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('p_port_2.started', t)
        p_port_2.status = STARTED
        win.callOnFlip(p_port_2.setData, int(2))
    if p_port_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port_2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            p_port_2.tStop = t  # not accounting for scr refresh
            p_port_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('p_port_2.stopped', t)
            p_port_2.status = FINISHED
            win.callOnFlip(p_port_2.setData, int(0))
    # *p_port_3* updates
    if p_port_3.status == NOT_STARTED and t >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        p_port_3.frameNStart = frameN  # exact frame index
        p_port_3.tStart = t  # local t and not account for scr refresh
        p_port_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p_port_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('p_port_3.started', t)
        p_port_3.status = STARTED
        win.callOnFlip(p_port_3.setData, int(3))
    if p_port_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port_3.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            p_port_3.tStop = t  # not accounting for scr refresh
            p_port_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('p_port_3.stopped', t)
            p_port_3.status = FINISHED
            win.callOnFlip(p_port_3.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
if p_port_2.status == STARTED:
    win.callOnFlip(p_port_2.setData, int(0))
if p_port_3.status == STARTED:
    win.callOnFlip(p_port_3.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.100000)

# --- Prepare to start Routine "Game_Start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Game_StartComponents = [Game_Start_Text, key_resp, p_port_4]
for thisComponent in Game_StartComponents:
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

# --- Run Routine "Game_Start" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Game_Start_Text* updates
    if Game_Start_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Game_Start_Text.frameNStart = frameN  # exact frame index
        Game_Start_Text.tStart = t  # local t and not account for scr refresh
        Game_Start_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Game_Start_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Game_Start_Text.started')
        Game_Start_Text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *p_port_4* updates
    if p_port_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p_port_4.frameNStart = frameN  # exact frame index
        p_port_4.tStart = t  # local t and not account for scr refresh
        p_port_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p_port_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('p_port_4.started', t)
        p_port_4.status = STARTED
        win.callOnFlip(p_port_4.setData, int(4))
    if p_port_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port_4.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            p_port_4.tStop = t  # not accounting for scr refresh
            p_port_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('p_port_4.stopped', t)
            p_port_4.status = FINISHED
            win.callOnFlip(p_port_4.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Game_StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Game_Start" ---
for thisComponent in Game_StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
if p_port_4.status == STARTED:
    win.callOnFlip(p_port_4.setData, int(0))
# the Routine "Game_Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop = data.TrialHandler(nReps=20.0, method='sequential', 
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
    
    # --- Prepare to start Routine "Fixation_Cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Fixation_CrossComponents = [fixation_cross, p_port_5, p_port_6]
    for thisComponent in Fixation_CrossComponents:
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
    
    # --- Run Routine "Fixation_Cross" ---
    while continueRoutine and routineTimer.getTime() < 6.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross.started')
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                fixation_cross.setAutoDraw(False)
        # *p_port_5* updates
        if p_port_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_5.frameNStart = frameN  # exact frame index
            p_port_5.tStart = t  # local t and not account for scr refresh
            p_port_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_5.started', t)
            p_port_5.status = STARTED
            win.callOnFlip(p_port_5.setData, int(6))
        if p_port_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_5.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_5.tStop = t  # not accounting for scr refresh
                p_port_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_5.stopped', t)
                p_port_5.status = FINISHED
                win.callOnFlip(p_port_5.setData, int(0))
        # *p_port_6* updates
        if p_port_6.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_6.frameNStart = frameN  # exact frame index
            p_port_6.tStart = t  # local t and not account for scr refresh
            p_port_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_6.started', t)
            p_port_6.status = STARTED
            win.callOnFlip(p_port_6.setData, int(7))
        if p_port_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_6.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_6.tStop = t  # not accounting for scr refresh
                p_port_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_6.stopped', t)
                p_port_6.status = FINISHED
                win.callOnFlip(p_port_6.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_CrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_Cross" ---
    for thisComponent in Fixation_CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_5.status == STARTED:
        win.callOnFlip(p_port_5.setData, int(0))
    if p_port_6.status == STARTED:
        win.callOnFlip(p_port_6.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.100000)
    
    # --- Prepare to start Routine "Opponent" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    player_image_intro.setImage(opponent_filenames[0])
    player_name_intro.reset()
    player_name_intro.setText(opponent_names[0])
    # keep track of which components have finished
    OpponentComponents = [player_image_intro, player_name_intro, p_port_7, p_port_8]
    for thisComponent in OpponentComponents:
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
    
    # --- Run Routine "Opponent" ---
    while continueRoutine and routineTimer.getTime() < 6.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *player_image_intro* updates
        if player_image_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_image_intro.frameNStart = frameN  # exact frame index
            player_image_intro.tStart = t  # local t and not account for scr refresh
            player_image_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_image_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_image_intro.started')
            player_image_intro.setAutoDraw(True)
        if player_image_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_image_intro.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                player_image_intro.tStop = t  # not accounting for scr refresh
                player_image_intro.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_image_intro.stopped')
                player_image_intro.setAutoDraw(False)
        
        # *player_name_intro* updates
        if player_name_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_name_intro.frameNStart = frameN  # exact frame index
            player_name_intro.tStart = t  # local t and not account for scr refresh
            player_name_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_name_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_name_intro.started')
            player_name_intro.setAutoDraw(True)
        if player_name_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_name_intro.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                player_name_intro.tStop = t  # not accounting for scr refresh
                player_name_intro.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_name_intro.stopped')
                player_name_intro.setAutoDraw(False)
        # *p_port_7* updates
        if p_port_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_7.frameNStart = frameN  # exact frame index
            p_port_7.tStart = t  # local t and not account for scr refresh
            p_port_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_7.started', t)
            p_port_7.status = STARTED
            win.callOnFlip(p_port_7.setData, int(12))
        if p_port_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_7.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_7.tStop = t  # not accounting for scr refresh
                p_port_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_7.stopped', t)
                p_port_7.status = FINISHED
                win.callOnFlip(p_port_7.setData, int(0))
        # *p_port_8* updates
        if p_port_8.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_8.frameNStart = frameN  # exact frame index
            p_port_8.tStart = t  # local t and not account for scr refresh
            p_port_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_8.started', t)
            p_port_8.status = STARTED
            win.callOnFlip(p_port_8.setData, int(13))
        if p_port_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_8.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_8.tStop = t  # not accounting for scr refresh
                p_port_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_8.stopped', t)
                p_port_8.status = FINISHED
                win.callOnFlip(p_port_8.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OpponentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Opponent" ---
    for thisComponent in OpponentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_7.status == STARTED:
        win.callOnFlip(p_port_7.setData, int(0))
    if p_port_8.status == STARTED:
        win.callOnFlip(p_port_8.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.100000)
    
    # --- Prepare to start Routine "Offer" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    player_image_offer.setImage(opponent_filenames.pop(0))
    player_name_offer.reset()
    player_name_offer.setText(opponent_names.pop(0))
    proposed_split.setText(bet_phrases.pop(0))
    # keep track of which components have finished
    OfferComponents = [player_image_offer, player_name_offer, proposed_split, accept_reject, p_port_9, p_port_10, p_port_15]
    for thisComponent in OfferComponents:
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
    
    # --- Run Routine "Offer" ---
    while continueRoutine and routineTimer.getTime() < 12.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *player_image_offer* updates
        if player_image_offer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_image_offer.frameNStart = frameN  # exact frame index
            player_image_offer.tStart = t  # local t and not account for scr refresh
            player_image_offer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_image_offer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_image_offer.started')
            player_image_offer.setAutoDraw(True)
        if player_image_offer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_image_offer.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                player_image_offer.tStop = t  # not accounting for scr refresh
                player_image_offer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_image_offer.stopped')
                player_image_offer.setAutoDraw(False)
        
        # *player_name_offer* updates
        if player_name_offer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_name_offer.frameNStart = frameN  # exact frame index
            player_name_offer.tStart = t  # local t and not account for scr refresh
            player_name_offer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_name_offer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_name_offer.started')
            player_name_offer.setAutoDraw(True)
        if player_name_offer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_name_offer.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                player_name_offer.tStop = t  # not accounting for scr refresh
                player_name_offer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_name_offer.stopped')
                player_name_offer.setAutoDraw(False)
        
        # *proposed_split* updates
        if proposed_split.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proposed_split.frameNStart = frameN  # exact frame index
            proposed_split.tStart = t  # local t and not account for scr refresh
            proposed_split.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proposed_split, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proposed_split.started')
            proposed_split.setAutoDraw(True)
        if proposed_split.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > proposed_split.tStartRefresh + 5.7-frameTolerance:
                # keep track of stop time/frame for later
                proposed_split.tStop = t  # not accounting for scr refresh
                proposed_split.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'proposed_split.stopped')
                proposed_split.setAutoDraw(False)
        
        # *accept_reject* updates
        if accept_reject.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            accept_reject.frameNStart = frameN  # exact frame index
            accept_reject.tStart = t  # local t and not account for scr refresh
            accept_reject.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(accept_reject, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'accept_reject.started')
            accept_reject.setAutoDraw(True)
        if accept_reject.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > accept_reject.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                accept_reject.tStop = t  # not accounting for scr refresh
                accept_reject.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'accept_reject.stopped')
                accept_reject.setAutoDraw(False)
        # *p_port_9* updates
        if p_port_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_9.frameNStart = frameN  # exact frame index
            p_port_9.tStart = t  # local t and not account for scr refresh
            p_port_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_9.started', t)
            p_port_9.status = STARTED
            win.callOnFlip(p_port_9.setData, int(14))
        if p_port_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_9.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_9.tStop = t  # not accounting for scr refresh
                p_port_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_9.stopped', t)
                p_port_9.status = FINISHED
                win.callOnFlip(p_port_9.setData, int(0))
        # *p_port_10* updates
        if p_port_10.status == NOT_STARTED and t >= 12.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_10.frameNStart = frameN  # exact frame index
            p_port_10.tStart = t  # local t and not account for scr refresh
            p_port_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_10.started', t)
            p_port_10.status = STARTED
            win.callOnFlip(p_port_10.setData, int(15))
        if p_port_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_10.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_10.tStop = t  # not accounting for scr refresh
                p_port_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_10.stopped', t)
                p_port_10.status = FINISHED
                win.callOnFlip(p_port_10.setData, int(0))
        # *p_port_15* updates
        if p_port_15.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_15.frameNStart = frameN  # exact frame index
            p_port_15.tStart = t  # local t and not account for scr refresh
            p_port_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_15.started', t)
            p_port_15.status = STARTED
            win.callOnFlip(p_port_15.setData, int(31))
        if p_port_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_15.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_15.tStop = t  # not accounting for scr refresh
                p_port_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_15.stopped', t)
                p_port_15.status = FINISHED
                win.callOnFlip(p_port_15.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OfferComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Offer" ---
    for thisComponent in OfferComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_9.status == STARTED:
        win.callOnFlip(p_port_9.setData, int(0))
    if p_port_10.status == STARTED:
        win.callOnFlip(p_port_10.setData, int(0))
    if p_port_15.status == STARTED:
        win.callOnFlip(p_port_15.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.100000)
    
    # --- Prepare to start Routine "Arrows" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    offer_choice.keys = []
    offer_choice.rt = []
    _offer_choice_allKeys = []
    # keep track of which components have finished
    ArrowsComponents = [arrow_instructions, offer_choice, p_port_11]
    for thisComponent in ArrowsComponents:
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
    
    # --- Run Routine "Arrows" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *arrow_instructions* updates
        if arrow_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow_instructions.frameNStart = frameN  # exact frame index
            arrow_instructions.tStart = t  # local t and not account for scr refresh
            arrow_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arrow_instructions.started')
            arrow_instructions.setAutoDraw(True)
        
        # *offer_choice* updates
        waitOnFlip = False
        if offer_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            offer_choice.frameNStart = frameN  # exact frame index
            offer_choice.tStart = t  # local t and not account for scr refresh
            offer_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(offer_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'offer_choice.started')
            offer_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(offer_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(offer_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if offer_choice.status == STARTED and not waitOnFlip:
            theseKeys = offer_choice.getKeys(keyList=['up','down'], waitRelease=False)
            _offer_choice_allKeys.extend(theseKeys)
            if len(_offer_choice_allKeys):
                offer_choice.keys = _offer_choice_allKeys[-1].name  # just the last key pressed
                offer_choice.rt = _offer_choice_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *p_port_11* updates
        if p_port_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_11.frameNStart = frameN  # exact frame index
            p_port_11.tStart = t  # local t and not account for scr refresh
            p_port_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_11.started', t)
            p_port_11.status = STARTED
            win.callOnFlip(p_port_11.setData, int(16))
        if p_port_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_11.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_11.tStop = t  # not accounting for scr refresh
                p_port_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_11.stopped', t)
                p_port_11.status = FINISHED
                win.callOnFlip(p_port_11.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ArrowsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Arrows" ---
    for thisComponent in ArrowsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if offer_choice.keys in ['', [], None]:  # No response was made
        offer_choice.keys = None
    loop.addData('offer_choice.keys',offer_choice.keys)
    if offer_choice.keys != None:  # we had a response
        loop.addData('offer_choice.rt', offer_choice.rt)
    if p_port_11.status == STARTED:
        win.callOnFlip(p_port_11.setData, int(0))
    # the Routine "Arrows" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal_Instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Non_Verbal_InstructionsComponents = [Instructions_Affinity_Score, p_port_12]
    for thisComponent in Non_Verbal_InstructionsComponents:
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
    
    # --- Run Routine "Non_Verbal_Instructions" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Affinity_Score* updates
        if Instructions_Affinity_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Affinity_Score.frameNStart = frameN  # exact frame index
            Instructions_Affinity_Score.tStart = t  # local t and not account for scr refresh
            Instructions_Affinity_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Affinity_Score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Affinity_Score.started')
            Instructions_Affinity_Score.setAutoDraw(True)
        if Instructions_Affinity_Score.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Instructions_Affinity_Score.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_Affinity_Score.tStop = t  # not accounting for scr refresh
                Instructions_Affinity_Score.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Instructions_Affinity_Score.stopped')
                Instructions_Affinity_Score.setAutoDraw(False)
        # *p_port_12* updates
        if p_port_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_12.frameNStart = frameN  # exact frame index
            p_port_12.tStart = t  # local t and not account for scr refresh
            p_port_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_12.started', t)
            p_port_12.status = STARTED
            win.callOnFlip(p_port_12.setData, int(17))
        if p_port_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_12.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_12.tStop = t  # not accounting for scr refresh
                p_port_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_12.stopped', t)
                p_port_12.status = FINISHED
                win.callOnFlip(p_port_12.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Non_Verbal_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Non_Verbal_Instructions" ---
    for thisComponent in Non_Verbal_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_12.status == STARTED:
        win.callOnFlip(p_port_12.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # set up handler to look after randomisation of conditions etc
    evaluate_all_emotions = data.TrialHandler(nReps=7.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='evaluate_all_emotions')
    thisExp.addLoop(evaluate_all_emotions)  # add the loop to the experiment
    thisEvaluate_all_emotion = evaluate_all_emotions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEvaluate_all_emotion.rgb)
    if thisEvaluate_all_emotion != None:
        for paramName in thisEvaluate_all_emotion:
            exec('{} = thisEvaluate_all_emotion[paramName]'.format(paramName))
    
    for thisEvaluate_all_emotion in evaluate_all_emotions:
        currentLoop = evaluate_all_emotions
        # abbreviate parameter names if possible (e.g. rgb = thisEvaluate_all_emotion.rgb)
        if thisEvaluate_all_emotion != None:
            for paramName in thisEvaluate_all_emotion:
                exec('{} = thisEvaluate_all_emotion[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Non_Verbal" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Emotion_Image.setImage(emotion_filenames.pop(0))
        AffinityScore.reset()
        # keep track of which components have finished
        Non_VerbalComponents = [Emotion_Image, AffinityScore, p_port_13]
        for thisComponent in Non_VerbalComponents:
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
        
        # --- Run Routine "Non_Verbal" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Emotion_Image* updates
            if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Emotion_Image.frameNStart = frameN  # exact frame index
                Emotion_Image.tStart = t  # local t and not account for scr refresh
                Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Emotion_Image.started')
                Emotion_Image.setAutoDraw(True)
            
            # *AffinityScore* updates
            if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                AffinityScore.frameNStart = frameN  # exact frame index
                AffinityScore.tStart = t  # local t and not account for scr refresh
                AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'AffinityScore.started')
                AffinityScore.setAutoDraw(True)
            
            # Check AffinityScore for response to end routine
            if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
                continueRoutine = False
            # *p_port_13* updates
            if p_port_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_13.frameNStart = frameN  # exact frame index
                p_port_13.tStart = t  # local t and not account for scr refresh
                p_port_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_13.started', t)
                p_port_13.status = STARTED
                win.callOnFlip(p_port_13.setData, int(18))
            if p_port_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_13.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_13.tStop = t  # not accounting for scr refresh
                    p_port_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_13.stopped', t)
                    p_port_13.status = FINISHED
                    win.callOnFlip(p_port_13.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Non_VerbalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Non_Verbal" ---
        for thisComponent in Non_VerbalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        evaluate_all_emotions.addData('AffinityScore.response', AffinityScore.getRating())
        evaluate_all_emotions.addData('AffinityScore.rt', AffinityScore.getRT())
        if p_port_13.status == STARTED:
            win.callOnFlip(p_port_13.setData, int(0))
        # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 7.0 repeats of 'evaluate_all_emotions'
    
    
    # --- Prepare to start Routine "Verbal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Moral_Disgust_Score.reset()
    # keep track of which components have finished
    VerbalComponents = [Instruction, Moral_Disgust_Score, p_port_14]
    for thisComponent in VerbalComponents:
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
    
    # --- Run Routine "Verbal" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction* updates
        if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.tStart = t  # local t and not account for scr refresh
            Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction.started')
            Instruction.setAutoDraw(True)
        
        # *Moral_Disgust_Score* updates
        if Moral_Disgust_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Moral_Disgust_Score.frameNStart = frameN  # exact frame index
            Moral_Disgust_Score.tStart = t  # local t and not account for scr refresh
            Moral_Disgust_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Moral_Disgust_Score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Moral_Disgust_Score.started')
            Moral_Disgust_Score.setAutoDraw(True)
        
        # Check Moral_Disgust_Score for response to end routine
        if Moral_Disgust_Score.getRating() is not None and Moral_Disgust_Score.status == STARTED:
            continueRoutine = False
        # *p_port_14* updates
        if p_port_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_14.frameNStart = frameN  # exact frame index
            p_port_14.tStart = t  # local t and not account for scr refresh
            p_port_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_14.started', t)
            p_port_14.status = STARTED
            win.callOnFlip(p_port_14.setData, int(19))
        if p_port_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_14.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_14.tStop = t  # not accounting for scr refresh
                p_port_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_14.stopped', t)
                p_port_14.status = FINISHED
                win.callOnFlip(p_port_14.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VerbalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Verbal" ---
    for thisComponent in VerbalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop.addData('Moral_Disgust_Score.response', Moral_Disgust_Score.getRating())
    loop.addData('Moral_Disgust_Score.rt', Moral_Disgust_Score.getRT())
    if p_port_14.status == STARTED:
        win.callOnFlip(p_port_14.setData, int(0))
    # the Routine "Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'loop'


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
