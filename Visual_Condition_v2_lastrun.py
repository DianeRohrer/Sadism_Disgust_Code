#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 18, 2025, at 14:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
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
expName = 'Visual_Condition_v2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\simla\\OneDrive\\Desktop\\Sadism_Disgust_Code\\Visual_Condition_v2_lastrun.py',
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
sync_beep_1 = sound.Sound('400', secs=0.4, stereo=True, hamming=True,
    name='sync_beep_1')
sync_beep_1.setVolume(1.0)
sync_beep_2 = sound.Sound('400', secs=0.4, stereo=True, hamming=True,
    name='sync_beep_2')
sync_beep_2.setVolume(1.0)
p_port = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Sit_Still" ---
textbox = visual.TextBox2(
     win, text='Please relax and sit still for the next 15 seconds', font='Open Sans',
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
     name='textbox',
     autoLog=True,
)
p_port_2 = parallel.ParallelPort(address='0x3FF8')
p_port_3 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Instructions" ---
instructions = visual.TextStim(win=win, name='instructions',
    text='In this portion of the experiment you will view a series of images and be asked to rate how disgusting you find each image using the scale under the image.\n\nPress space bar to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
p_port_4 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "View_Cross" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
p_port_6 = parallel.ParallelPort(address='0x3FF8')
p_port_7 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "View_Image" ---
disgust_image = visual.ImageStim(
    win=win,
    name='disgust_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
p_port_8 = parallel.ParallelPort(address='0x3FF8')
p_port_9 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Score_Image" ---
disgust_score = visual.Slider(win=win, name='disgust_score',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["Not disgusting at all", "Slightly disgusting", "Moderately disgusting,\nunpleasant to look at", "Very disgusting,\nI want to push\nthe image away", "Extremely disgusting,\nI feel nauseous"], ticks=(0, 1, 2, 3, 4), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, 1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=0, readOnly=False)
p_port_10 = parallel.ParallelPort(address='0x3FF8')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Setup_Code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from initialization_script
import json

expInfo['session'] = "Visual"

# Read in the list of opponents for this subject.
# This reads the text file where they are stored,
# and reads them in as a Python list.
subject_id = expInfo['participant']
with open(os.path.join("data", f"disgust_images_{subject_id}.txt"), "rt") as f:
    disgust_image_paths = json.loads(f.read())
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
sync_beep_1.setSound('400', secs=0.4, hamming=True)
sync_beep_1.setVolume(1.0, log=False)
sync_beep_2.setSound('400', secs=0.4, hamming=True)
sync_beep_2.setVolume(1.0, log=False)
# keep track of which components have finished
Sync_BeepsComponents = [sync_beep_1, sync_beep_2, p_port]
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
while continueRoutine and routineTimer.getTime() < 1.1:
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
        if tThisFlipGlobal > sync_beep_1.tStartRefresh + 0.4-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_1.tStop = t  # not accounting for scr refresh
            sync_beep_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_1.stopped')
            sync_beep_1.stop()
    # start/stop sync_beep_2
    if sync_beep_2.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_2.frameNStart = frameN  # exact frame index
        sync_beep_2.tStart = t  # local t and not account for scr refresh
        sync_beep_2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_2.started', tThisFlipGlobal)
        sync_beep_2.play(when=win)  # sync with win flip
    if sync_beep_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_2.tStartRefresh + 0.4-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_2.tStop = t  # not accounting for scr refresh
            sync_beep_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_2.stopped')
            sync_beep_2.stop()
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
        win.callOnFlip(p_port.setData, int(1))
    if p_port.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p_port.tStartRefresh + .1-frameTolerance:
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
if p_port.status == STARTED:
    win.callOnFlip(p_port.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.100000)

# --- Prepare to start Routine "Sit_Still" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox.reset()
# keep track of which components have finished
Sit_StillComponents = [textbox, p_port_2, p_port_3]
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
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox.started')
        textbox.setAutoDraw(True)
    if textbox.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textbox.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            textbox.tStop = t  # not accounting for scr refresh
            textbox.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.stopped')
            textbox.setAutoDraw(False)
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
        if tThisFlipGlobal > p_port_2.tStartRefresh + .1-frameTolerance:
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

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions, key_resp, p_port_4]
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
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions.started')
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 100-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions.stopped')
            instructions.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
if p_port_4.status == STARTED:
    win.callOnFlip(p_port_4.setData, int(0))
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop = data.TrialHandler(nReps=64.0, method='sequential', 
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
    
    # --- Prepare to start Routine "View_Cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    View_CrossComponents = [cross, p_port_6, p_port_7]
    for thisComponent in View_CrossComponents:
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
    
    # --- Run Routine "View_Cross" ---
    while continueRoutine and routineTimer.getTime() < 6.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        # *p_port_6* updates
        if p_port_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_6.frameNStart = frameN  # exact frame index
            p_port_6.tStart = t  # local t and not account for scr refresh
            p_port_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_6.started', t)
            p_port_6.status = STARTED
            win.callOnFlip(p_port_6.setData, int(6))
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
        # *p_port_7* updates
        if p_port_7.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_7.frameNStart = frameN  # exact frame index
            p_port_7.tStart = t  # local t and not account for scr refresh
            p_port_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_7.started', t)
            p_port_7.status = STARTED
            win.callOnFlip(p_port_7.setData, int(7))
        if p_port_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_7.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_7.tStop = t  # not accounting for scr refresh
                p_port_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_7.stopped', t)
                p_port_7.status = FINISHED
                win.callOnFlip(p_port_7.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in View_CrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "View_Cross" ---
    for thisComponent in View_CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_6.status == STARTED:
        win.callOnFlip(p_port_6.setData, int(0))
    if p_port_7.status == STARTED:
        win.callOnFlip(p_port_7.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.100000)
    
    # --- Prepare to start Routine "View_Image" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    disgust_image.setImage(disgust_image_paths.pop(0))
    # keep track of which components have finished
    View_ImageComponents = [disgust_image, p_port_8, p_port_9]
    for thisComponent in View_ImageComponents:
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
    
    # --- Run Routine "View_Image" ---
    while continueRoutine and routineTimer.getTime() < 6.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *disgust_image* updates
        if disgust_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disgust_image.frameNStart = frameN  # exact frame index
            disgust_image.tStart = t  # local t and not account for scr refresh
            disgust_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disgust_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'disgust_image.started')
            disgust_image.setAutoDraw(True)
        if disgust_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > disgust_image.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                disgust_image.tStop = t  # not accounting for scr refresh
                disgust_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disgust_image.stopped')
                disgust_image.setAutoDraw(False)
        # *p_port_8* updates
        if p_port_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_8.frameNStart = frameN  # exact frame index
            p_port_8.tStart = t  # local t and not account for scr refresh
            p_port_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_8.started', t)
            p_port_8.status = STARTED
            win.callOnFlip(p_port_8.setData, int(8))
        if p_port_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_8.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_8.tStop = t  # not accounting for scr refresh
                p_port_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_8.stopped', t)
                p_port_8.status = FINISHED
                win.callOnFlip(p_port_8.setData, int(0))
        # *p_port_9* updates
        if p_port_9.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_9.frameNStart = frameN  # exact frame index
            p_port_9.tStart = t  # local t and not account for scr refresh
            p_port_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_9.started', t)
            p_port_9.status = STARTED
            win.callOnFlip(p_port_9.setData, int(9))
        if p_port_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_9.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_9.tStop = t  # not accounting for scr refresh
                p_port_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_9.stopped', t)
                p_port_9.status = FINISHED
                win.callOnFlip(p_port_9.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in View_ImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "View_Image" ---
    for thisComponent in View_ImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_8.status == STARTED:
        win.callOnFlip(p_port_8.setData, int(0))
    if p_port_9.status == STARTED:
        win.callOnFlip(p_port_9.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.100000)
    
    # --- Prepare to start Routine "Score_Image" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    disgust_score.reset()
    # keep track of which components have finished
    Score_ImageComponents = [disgust_score, p_port_10]
    for thisComponent in Score_ImageComponents:
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
    
    # --- Run Routine "Score_Image" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *disgust_score* updates
        if disgust_score.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            disgust_score.frameNStart = frameN  # exact frame index
            disgust_score.tStart = t  # local t and not account for scr refresh
            disgust_score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disgust_score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'disgust_score.started')
            disgust_score.setAutoDraw(True)
        
        # Check disgust_score for response to end routine
        if disgust_score.getRating() is not None and disgust_score.status == STARTED:
            continueRoutine = False
        # *p_port_10* updates
        if p_port_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_10.frameNStart = frameN  # exact frame index
            p_port_10.tStart = t  # local t and not account for scr refresh
            p_port_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_10.started', t)
            p_port_10.status = STARTED
            win.callOnFlip(p_port_10.setData, int(10))
        if p_port_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_10.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_10.tStop = t  # not accounting for scr refresh
                p_port_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_10.stopped', t)
                p_port_10.status = FINISHED
                win.callOnFlip(p_port_10.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Score_ImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Score_Image" ---
    for thisComponent in Score_ImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop.addData('disgust_score.response', disgust_score.getRating())
    loop.addData('disgust_score.rt', disgust_score.getRT())
    if p_port_10.status == STARTED:
        win.callOnFlip(p_port_10.setData, int(0))
    # the Routine "Score_Image" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 64.0 repeats of 'loop'


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
