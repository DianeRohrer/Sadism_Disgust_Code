#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 13, 2025, at 12:24
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
expName = 'Gustatory_Condition_v2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\simla\\OneDrive\\Desktop\\Sadism_Disgust_Code\\Gustatory_Condition_v2_lastrun.py',
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
sync_beep_1 = sound.Sound('400', secs=0.25, stereo=True, hamming=True,
    name='sync_beep_1')
sync_beep_1.setVolume(1.0)
sync_beep_2 = sound.Sound('400', secs=0.25, stereo=True, hamming=True,
    name='sync_beep_2')
sync_beep_2.setVolume(1.0)
sync_beep_3 = sound.Sound('400', secs=0.25, stereo=True, hamming=True,
    name='sync_beep_3')
sync_beep_3.setVolume(1.0)
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

# --- Initialize components for Routine "Cross" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
p_port_4 = parallel.ParallelPort(address='0x3FF8')
p_port_5 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Instructions" ---
instructions = visual.TextStim(win=win, name='instructions',
    text="During this experiment you will be tasting different liquids. You will be told when to grab a cup, when to roll the liquid around your mouth, and when to spit the liquid into the cup. After this you will get to rinse your mouth with water.\n\nHit the spacebar when you're ready to start.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
spacebar_hit = keyboard.Keyboard()
p_port_6 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Cup" ---
grab_cup = visual.TextStim(win=win, name='grab_cup',
    text='Participant please grab a cup.\n\n\n\nExperimenter hit "9" when ready.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
p_port_7 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "taste_beeps" ---
taste_sound_1 = sound.Sound('600', secs=.3, stereo=True, hamming=True,
    name='taste_sound_1')
taste_sound_1.setVolume(1.0)
taste_sound_2 = sound.Sound('600', secs=.3, stereo=True, hamming=True,
    name='taste_sound_2')
taste_sound_2.setVolume(1.0)
taste_sound_3 = sound.Sound('600', secs=.3, stereo=True, hamming=True,
    name='taste_sound_3')
taste_sound_3.setVolume(1.0)
Roll_liquid_taste = visual.TextStim(win=win, name='Roll_liquid_taste',
    text='Roll liquid gently across your tongue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
p_port_8 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "spit_beep" ---
spit_text = visual.TextStim(win=win, name='spit_text',
    text='Spit',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
spit_sound = sound.Sound('450', secs=1.0, stereo=True, hamming=True,
    name='spit_sound')
spit_sound.setVolume(1.0)
screen_clear = visual.TextStim(win=win, name='screen_clear',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
p_port_9 = parallel.ParallelPort(address='0x3FF8')
p_port_18 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Palatability" ---
Palatability_Score = visual.Slider(win=win, name='Palatability_Score',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=("Worst thing I have ever tasted", "", "Not horrible but would not try again", "", "Pleasant tasting, would try again", "", "Best thing I have ever tasted"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0, -1.0, 1.0], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=0, readOnly=False)
p_port_17 = parallel.ParallelPort(address='0x3FF8')
Instruction = visual.TextStim(win=win, name='Instruction',
    text='Please rate how good or bad liquid you received was.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Rinse" ---
Rinse_text = visual.TextStim(win=win, name='Rinse_text',
    text='When you hear the tone start rinsing. Please grab a cup. You will hear a second tone to tell you to stop and spit. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Begin_Rinse = sound.Sound('300', secs=1.0, stereo=True, hamming=True,
    name='Begin_Rinse')
Begin_Rinse.setVolume(1.0)
Finish_rinse = sound.Sound('600', secs=1.0, stereo=True, hamming=True,
    name='Finish_rinse')
Finish_rinse.setVolume(1.0)
Rinse_Spit = visual.TextStim(win=win, name='Rinse_Spit',
    text='Spit',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
p_port_10 = parallel.ParallelPort(address='0x3FF8')
p_port_11 = parallel.ParallelPort(address='0x3FF8')
p_port_12 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Rest" ---
rest_text = visual.TextBox2(
     win, text='Relax for the next 30 seconds', font='Open Sans',
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
     name='rest_text',
     autoLog=True,
)
p_port_13 = parallel.ParallelPort(address='0x3FF8')
p_port_14 = parallel.ParallelPort(address='0x3FF8')

# --- Initialize components for Routine "Break" ---
break_text = visual.TextStim(win=win, name='break_text',
    text='Please take a 30 second break',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
p_port_15 = parallel.ParallelPort(address='0x3FF8')
p_port_16 = parallel.ParallelPort(address='0x3FF8')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Setup_Code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from initialization_script
expInfo['session'] = "Gustatory"
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
sync_beep_1.setSound('400', secs=0.25, hamming=True)
sync_beep_1.setVolume(1.0, log=False)
sync_beep_2.setSound('400', secs=0.25, hamming=True)
sync_beep_2.setVolume(1.0, log=False)
sync_beep_3.setSound('400', secs=0.25, hamming=True)
sync_beep_3.setVolume(1.0, log=False)
# keep track of which components have finished
Sync_BeepsComponents = [sync_beep_1, sync_beep_2, sync_beep_3, p_port]
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
while continueRoutine and routineTimer.getTime() < 1.25:
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
        if tThisFlipGlobal > sync_beep_1.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_1.tStop = t  # not accounting for scr refresh
            sync_beep_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_1.stopped')
            sync_beep_1.stop()
    # start/stop sync_beep_2
    if sync_beep_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_2.frameNStart = frameN  # exact frame index
        sync_beep_2.tStart = t  # local t and not account for scr refresh
        sync_beep_2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_2.started', tThisFlipGlobal)
        sync_beep_2.play(when=win)  # sync with win flip
    if sync_beep_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_2.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_2.tStop = t  # not accounting for scr refresh
            sync_beep_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_2.stopped')
            sync_beep_2.stop()
    # start/stop sync_beep_3
    if sync_beep_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        sync_beep_3.frameNStart = frameN  # exact frame index
        sync_beep_3.tStart = t  # local t and not account for scr refresh
        sync_beep_3.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('sync_beep_3.started', tThisFlipGlobal)
        sync_beep_3.play(when=win)  # sync with win flip
    if sync_beep_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sync_beep_3.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            sync_beep_3.tStop = t  # not accounting for scr refresh
            sync_beep_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sync_beep_3.stopped')
            sync_beep_3.stop()
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
        win.callOnFlip(p_port.setData, int(5))
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
sync_beep_3.stop()  # ensure sound has stopped at end of routine
if p_port.status == STARTED:
    win.callOnFlip(p_port.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.250000)

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
        if tThisFlipGlobal > p_port_3.tStartRefresh + 0.1-frameTolerance:
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

# set up handler to look after randomisation of conditions etc
Blocks_of_Tastants = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks_of_Tastants')
thisExp.addLoop(Blocks_of_Tastants)  # add the loop to the experiment
thisBlocks_of_Tastant = Blocks_of_Tastants.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_of_Tastant.rgb)
if thisBlocks_of_Tastant != None:
    for paramName in thisBlocks_of_Tastant:
        exec('{} = thisBlocks_of_Tastant[paramName]'.format(paramName))

for thisBlocks_of_Tastant in Blocks_of_Tastants:
    currentLoop = Blocks_of_Tastants
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_of_Tastant.rgb)
    if thisBlocks_of_Tastant != None:
        for paramName in thisBlocks_of_Tastant:
            exec('{} = thisBlocks_of_Tastant[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Each_Tastant_Once = data.TrialHandler(nReps=5.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Each_Tastant_Once')
    thisExp.addLoop(Each_Tastant_Once)  # add the loop to the experiment
    thisEach_Tastant_Once = Each_Tastant_Once.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEach_Tastant_Once.rgb)
    if thisEach_Tastant_Once != None:
        for paramName in thisEach_Tastant_Once:
            exec('{} = thisEach_Tastant_Once[paramName]'.format(paramName))
    
    for thisEach_Tastant_Once in Each_Tastant_Once:
        currentLoop = Each_Tastant_Once
        # abbreviate parameter names if possible (e.g. rgb = thisEach_Tastant_Once.rgb)
        if thisEach_Tastant_Once != None:
            for paramName in thisEach_Tastant_Once:
                exec('{} = thisEach_Tastant_Once[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Cross" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        CrossComponents = [cross, p_port_4, p_port_5]
        for thisComponent in CrossComponents:
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
        
        # --- Run Routine "Cross" ---
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
                win.callOnFlip(p_port_4.setData, int(6))
            if p_port_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_4.tStop = t  # not accounting for scr refresh
                    p_port_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_4.stopped', t)
                    p_port_4.status = FINISHED
                    win.callOnFlip(p_port_4.setData, int(0))
            # *p_port_5* updates
            if p_port_5.status == NOT_STARTED and t >= 6.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_5.frameNStart = frameN  # exact frame index
                p_port_5.tStart = t  # local t and not account for scr refresh
                p_port_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_5.started', t)
                p_port_5.status = STARTED
                win.callOnFlip(p_port_5.setData, int(7))
            if p_port_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_5.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_5.tStop = t  # not accounting for scr refresh
                    p_port_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_5.stopped', t)
                    p_port_5.status = FINISHED
                    win.callOnFlip(p_port_5.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Cross" ---
        for thisComponent in CrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port_4.status == STARTED:
            win.callOnFlip(p_port_4.setData, int(0))
        if p_port_5.status == STARTED:
            win.callOnFlip(p_port_5.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.100000)
        
        # --- Prepare to start Routine "Instructions" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        spacebar_hit.keys = []
        spacebar_hit.rt = []
        _spacebar_hit_allKeys = []
        # keep track of which components have finished
        InstructionsComponents = [instructions, spacebar_hit, p_port_6]
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
                if tThisFlipGlobal > instructions.tStartRefresh + 100.0-frameTolerance:
                    # keep track of stop time/frame for later
                    instructions.tStop = t  # not accounting for scr refresh
                    instructions.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instructions.stopped')
                    instructions.setAutoDraw(False)
            
            # *spacebar_hit* updates
            waitOnFlip = False
            if spacebar_hit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                spacebar_hit.frameNStart = frameN  # exact frame index
                spacebar_hit.tStart = t  # local t and not account for scr refresh
                spacebar_hit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(spacebar_hit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'spacebar_hit.started')
                spacebar_hit.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(spacebar_hit.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(spacebar_hit.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if spacebar_hit.status == STARTED and not waitOnFlip:
                theseKeys = spacebar_hit.getKeys(keyList=['space'], waitRelease=False)
                _spacebar_hit_allKeys.extend(theseKeys)
                if len(_spacebar_hit_allKeys):
                    spacebar_hit.keys = _spacebar_hit_allKeys[-1].name  # just the last key pressed
                    spacebar_hit.rt = _spacebar_hit_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
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
                win.callOnFlip(p_port_6.setData, int(4))
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
        if spacebar_hit.keys in ['', [], None]:  # No response was made
            spacebar_hit.keys = None
        Each_Tastant_Once.addData('spacebar_hit.keys',spacebar_hit.keys)
        if spacebar_hit.keys != None:  # we had a response
            Each_Tastant_Once.addData('spacebar_hit.rt', spacebar_hit.rt)
        if p_port_6.status == STARTED:
            win.callOnFlip(p_port_6.setData, int(0))
        # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Cup" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        CupComponents = [grab_cup, key_resp, p_port_7]
        for thisComponent in CupComponents:
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
        
        # --- Run Routine "Cup" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grab_cup* updates
            if grab_cup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grab_cup.frameNStart = frameN  # exact frame index
                grab_cup.tStart = t  # local t and not account for scr refresh
                grab_cup.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grab_cup, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grab_cup.started')
                grab_cup.setAutoDraw(True)
            if grab_cup.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grab_cup.tStartRefresh + 100-frameTolerance:
                    # keep track of stop time/frame for later
                    grab_cup.tStop = t  # not accounting for scr refresh
                    grab_cup.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grab_cup.stopped')
                    grab_cup.setAutoDraw(False)
            
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
                theseKeys = key_resp.getKeys(keyList=['num_9'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
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
                win.callOnFlip(p_port_7.setData, int(20))
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CupComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Cup" ---
        for thisComponent in CupComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        Each_Tastant_Once.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            Each_Tastant_Once.addData('key_resp.rt', key_resp.rt)
        if p_port_7.status == STARTED:
            win.callOnFlip(p_port_7.setData, int(0))
        # the Routine "Cup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "taste_beeps" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        taste_sound_1.setSound('600', secs=.3, hamming=True)
        taste_sound_1.setVolume(1.0, log=False)
        taste_sound_2.setSound('600', secs=.3, hamming=True)
        taste_sound_2.setVolume(1.0, log=False)
        taste_sound_3.setSound('600', secs=.3, hamming=True)
        taste_sound_3.setVolume(1.0, log=False)
        # keep track of which components have finished
        taste_beepsComponents = [taste_sound_1, taste_sound_2, taste_sound_3, Roll_liquid_taste, p_port_8]
        for thisComponent in taste_beepsComponents:
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
        
        # --- Run Routine "taste_beeps" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop taste_sound_1
            if taste_sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taste_sound_1.frameNStart = frameN  # exact frame index
                taste_sound_1.tStart = t  # local t and not account for scr refresh
                taste_sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('taste_sound_1.started', tThisFlipGlobal)
                taste_sound_1.play(when=win)  # sync with win flip
            if taste_sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taste_sound_1.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    taste_sound_1.tStop = t  # not accounting for scr refresh
                    taste_sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taste_sound_1.stopped')
                    taste_sound_1.stop()
            # start/stop taste_sound_2
            if taste_sound_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                taste_sound_2.frameNStart = frameN  # exact frame index
                taste_sound_2.tStart = t  # local t and not account for scr refresh
                taste_sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('taste_sound_2.started', tThisFlipGlobal)
                taste_sound_2.play(when=win)  # sync with win flip
            if taste_sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taste_sound_2.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    taste_sound_2.tStop = t  # not accounting for scr refresh
                    taste_sound_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taste_sound_2.stopped')
                    taste_sound_2.stop()
            # start/stop taste_sound_3
            if taste_sound_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                taste_sound_3.frameNStart = frameN  # exact frame index
                taste_sound_3.tStart = t  # local t and not account for scr refresh
                taste_sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('taste_sound_3.started', tThisFlipGlobal)
                taste_sound_3.play(when=win)  # sync with win flip
            if taste_sound_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taste_sound_3.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    taste_sound_3.tStop = t  # not accounting for scr refresh
                    taste_sound_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taste_sound_3.stopped')
                    taste_sound_3.stop()
            
            # *Roll_liquid_taste* updates
            if Roll_liquid_taste.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Roll_liquid_taste.frameNStart = frameN  # exact frame index
                Roll_liquid_taste.tStart = t  # local t and not account for scr refresh
                Roll_liquid_taste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Roll_liquid_taste, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Roll_liquid_taste.started')
                Roll_liquid_taste.setAutoDraw(True)
            if Roll_liquid_taste.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Roll_liquid_taste.tStartRefresh + 8.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Roll_liquid_taste.tStop = t  # not accounting for scr refresh
                    Roll_liquid_taste.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Roll_liquid_taste.stopped')
                    Roll_liquid_taste.setAutoDraw(False)
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
                win.callOnFlip(p_port_8.setData, int(21))
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in taste_beepsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "taste_beeps" ---
        for thisComponent in taste_beepsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        taste_sound_1.stop()  # ensure sound has stopped at end of routine
        taste_sound_2.stop()  # ensure sound has stopped at end of routine
        taste_sound_3.stop()  # ensure sound has stopped at end of routine
        if p_port_8.status == STARTED:
            win.callOnFlip(p_port_8.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "spit_beep" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        spit_sound.setSound('450', secs=1.0, hamming=True)
        spit_sound.setVolume(1.0, log=False)
        # keep track of which components have finished
        spit_beepComponents = [spit_text, spit_sound, screen_clear, p_port_9, p_port_18]
        for thisComponent in spit_beepComponents:
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
        
        # --- Run Routine "spit_beep" ---
        while continueRoutine and routineTimer.getTime() < 10.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *spit_text* updates
            if spit_text.status == NOT_STARTED and tThisFlip >= 0.-frameTolerance:
                # keep track of start time/frame for later
                spit_text.frameNStart = frameN  # exact frame index
                spit_text.tStart = t  # local t and not account for scr refresh
                spit_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(spit_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'spit_text.started')
                spit_text.setAutoDraw(True)
            if spit_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spit_text.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    spit_text.tStop = t  # not accounting for scr refresh
                    spit_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'spit_text.stopped')
                    spit_text.setAutoDraw(False)
            # start/stop spit_sound
            if spit_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                spit_sound.frameNStart = frameN  # exact frame index
                spit_sound.tStart = t  # local t and not account for scr refresh
                spit_sound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('spit_sound.started', tThisFlipGlobal)
                spit_sound.play(when=win)  # sync with win flip
            if spit_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spit_sound.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    spit_sound.tStop = t  # not accounting for scr refresh
                    spit_sound.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'spit_sound.stopped')
                    spit_sound.stop()
            
            # *screen_clear* updates
            if screen_clear.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                screen_clear.frameNStart = frameN  # exact frame index
                screen_clear.tStart = t  # local t and not account for scr refresh
                screen_clear.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screen_clear, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'screen_clear.started')
                screen_clear.setAutoDraw(True)
            if screen_clear.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > screen_clear.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    screen_clear.tStop = t  # not accounting for scr refresh
                    screen_clear.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'screen_clear.stopped')
                    screen_clear.setAutoDraw(False)
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
                win.callOnFlip(p_port_9.setData, int(22))
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
            # *p_port_18* updates
            if p_port_18.status == NOT_STARTED and t >= 10.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_18.frameNStart = frameN  # exact frame index
                p_port_18.tStart = t  # local t and not account for scr refresh
                p_port_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_18.started', t)
                p_port_18.status = STARTED
                win.callOnFlip(p_port_18.setData, int(32))
            if p_port_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_18.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_18.tStop = t  # not accounting for scr refresh
                    p_port_18.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_18.stopped', t)
                    p_port_18.status = FINISHED
                    win.callOnFlip(p_port_18.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in spit_beepComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "spit_beep" ---
        for thisComponent in spit_beepComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        spit_sound.stop()  # ensure sound has stopped at end of routine
        if p_port_9.status == STARTED:
            win.callOnFlip(p_port_9.setData, int(0))
        if p_port_18.status == STARTED:
            win.callOnFlip(p_port_18.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.100000)
        
        # --- Prepare to start Routine "Palatability" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Palatability_Score.reset()
        # keep track of which components have finished
        PalatabilityComponents = [Palatability_Score, p_port_17, Instruction]
        for thisComponent in PalatabilityComponents:
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
        
        # --- Run Routine "Palatability" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Palatability_Score* updates
            if Palatability_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Palatability_Score.frameNStart = frameN  # exact frame index
                Palatability_Score.tStart = t  # local t and not account for scr refresh
                Palatability_Score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Palatability_Score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Palatability_Score.started')
                Palatability_Score.setAutoDraw(True)
            
            # Check Palatability_Score for response to end routine
            if Palatability_Score.getRating() is not None and Palatability_Score.status == STARTED:
                continueRoutine = False
            # *p_port_17* updates
            if p_port_17.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_17.frameNStart = frameN  # exact frame index
                p_port_17.tStart = t  # local t and not account for scr refresh
                p_port_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_17.started', t)
                p_port_17.status = STARTED
                win.callOnFlip(p_port_17.setData, int(26))
            if p_port_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_17.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_17.tStop = t  # not accounting for scr refresh
                    p_port_17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_17.stopped', t)
                    p_port_17.status = FINISHED
                    win.callOnFlip(p_port_17.setData, int(0))
            
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PalatabilityComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Palatability" ---
        for thisComponent in PalatabilityComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Each_Tastant_Once.addData('Palatability_Score.response', Palatability_Score.getRating())
        Each_Tastant_Once.addData('Palatability_Score.rt', Palatability_Score.getRT())
        if p_port_17.status == STARTED:
            win.callOnFlip(p_port_17.setData, int(0))
        # the Routine "Palatability" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Rinse" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Begin_Rinse.setSound('300', secs=1.0, hamming=True)
        Begin_Rinse.setVolume(1.0, log=False)
        Finish_rinse.setSound('600', secs=1.0, hamming=True)
        Finish_rinse.setVolume(1.0, log=False)
        # keep track of which components have finished
        RinseComponents = [Rinse_text, Begin_Rinse, Finish_rinse, Rinse_Spit, p_port_10, p_port_11, p_port_12]
        for thisComponent in RinseComponents:
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
        
        # --- Run Routine "Rinse" ---
        while continueRoutine and routineTimer.getTime() < 29.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Rinse_text* updates
            if Rinse_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Rinse_text.frameNStart = frameN  # exact frame index
                Rinse_text.tStart = t  # local t and not account for scr refresh
                Rinse_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rinse_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Rinse_text.started')
                Rinse_text.setAutoDraw(True)
            if Rinse_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rinse_text.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Rinse_text.tStop = t  # not accounting for scr refresh
                    Rinse_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Rinse_text.stopped')
                    Rinse_text.setAutoDraw(False)
            # start/stop Begin_Rinse
            if Begin_Rinse.status == NOT_STARTED and tThisFlip >= 6.2-frameTolerance:
                # keep track of start time/frame for later
                Begin_Rinse.frameNStart = frameN  # exact frame index
                Begin_Rinse.tStart = t  # local t and not account for scr refresh
                Begin_Rinse.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('Begin_Rinse.started', tThisFlipGlobal)
                Begin_Rinse.play(when=win)  # sync with win flip
            if Begin_Rinse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Begin_Rinse.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Begin_Rinse.tStop = t  # not accounting for scr refresh
                    Begin_Rinse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Begin_Rinse.stopped')
                    Begin_Rinse.stop()
            # start/stop Finish_rinse
            if Finish_rinse.status == NOT_STARTED and tThisFlip >= 26.2-frameTolerance:
                # keep track of start time/frame for later
                Finish_rinse.frameNStart = frameN  # exact frame index
                Finish_rinse.tStart = t  # local t and not account for scr refresh
                Finish_rinse.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('Finish_rinse.started', tThisFlipGlobal)
                Finish_rinse.play(when=win)  # sync with win flip
            if Finish_rinse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Finish_rinse.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Finish_rinse.tStop = t  # not accounting for scr refresh
                    Finish_rinse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Finish_rinse.stopped')
                    Finish_rinse.stop()
            
            # *Rinse_Spit* updates
            if Rinse_Spit.status == NOT_STARTED and tThisFlip >= 26.2-frameTolerance:
                # keep track of start time/frame for later
                Rinse_Spit.frameNStart = frameN  # exact frame index
                Rinse_Spit.tStart = t  # local t and not account for scr refresh
                Rinse_Spit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rinse_Spit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Rinse_Spit.started')
                Rinse_Spit.setAutoDraw(True)
            if Rinse_Spit.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Rinse_Spit.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Rinse_Spit.tStop = t  # not accounting for scr refresh
                    Rinse_Spit.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Rinse_Spit.stopped')
                    Rinse_Spit.setAutoDraw(False)
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
                win.callOnFlip(p_port_10.setData, int(23))
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
            # *p_port_11* updates
            if p_port_11.status == NOT_STARTED and t >= 6.2-frameTolerance:
                # keep track of start time/frame for later
                p_port_11.frameNStart = frameN  # exact frame index
                p_port_11.tStart = t  # local t and not account for scr refresh
                p_port_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_11.started', t)
                p_port_11.status = STARTED
                win.callOnFlip(p_port_11.setData, int(24))
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
            # *p_port_12* updates
            if p_port_12.status == NOT_STARTED and t >= 26.2-frameTolerance:
                # keep track of start time/frame for later
                p_port_12.frameNStart = frameN  # exact frame index
                p_port_12.tStart = t  # local t and not account for scr refresh
                p_port_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_12.started', t)
                p_port_12.status = STARTED
                win.callOnFlip(p_port_12.setData, int(25))
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
            for thisComponent in RinseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Rinse" ---
        for thisComponent in RinseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Begin_Rinse.stop()  # ensure sound has stopped at end of routine
        Finish_rinse.stop()  # ensure sound has stopped at end of routine
        if p_port_10.status == STARTED:
            win.callOnFlip(p_port_10.setData, int(0))
        if p_port_11.status == STARTED:
            win.callOnFlip(p_port_11.setData, int(0))
        if p_port_12.status == STARTED:
            win.callOnFlip(p_port_12.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-29.200000)
        
        # --- Prepare to start Routine "Rest" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        rest_text.reset()
        # keep track of which components have finished
        RestComponents = [rest_text, p_port_13, p_port_14]
        for thisComponent in RestComponents:
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
        
        # --- Run Routine "Rest" ---
        while continueRoutine and routineTimer.getTime() < 30.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rest_text* updates
            if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_text.frameNStart = frameN  # exact frame index
                rest_text.tStart = t  # local t and not account for scr refresh
                rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_text.started')
                rest_text.setAutoDraw(True)
            if rest_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rest_text.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rest_text.tStop = t  # not accounting for scr refresh
                    rest_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_text.stopped')
                    rest_text.setAutoDraw(False)
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
                win.callOnFlip(p_port_13.setData, int(27))
            if p_port_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_13.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_13.tStop = t  # not accounting for scr refresh
                    p_port_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_13.stopped', t)
                    p_port_13.status = FINISHED
                    win.callOnFlip(p_port_13.setData, int(0))
            # *p_port_14* updates
            if p_port_14.status == NOT_STARTED and t >= 30.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_14.frameNStart = frameN  # exact frame index
                p_port_14.tStart = t  # local t and not account for scr refresh
                p_port_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_14.started', t)
                p_port_14.status = STARTED
                win.callOnFlip(p_port_14.setData, int(28))
            if p_port_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_14.tStartRefresh + .1-frameTolerance:
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
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Rest" ---
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port_13.status == STARTED:
            win.callOnFlip(p_port_13.setData, int(0))
        if p_port_14.status == STARTED:
            win.callOnFlip(p_port_14.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.100000)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'Each_Tastant_Once'
    
    
    # --- Prepare to start Routine "Break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    BreakComponents = [break_text, p_port_15, p_port_16]
    for thisComponent in BreakComponents:
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
    
    # --- Run Routine "Break" ---
    while continueRoutine and routineTimer.getTime() < 30.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if break_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_text.started')
            break_text.setAutoDraw(True)
        if break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                break_text.tStop = t  # not accounting for scr refresh
                break_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_text.stopped')
                break_text.setAutoDraw(False)
        # *p_port_15* updates
        if p_port_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_15.frameNStart = frameN  # exact frame index
            p_port_15.tStart = t  # local t and not account for scr refresh
            p_port_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_15.started', t)
            p_port_15.status = STARTED
            win.callOnFlip(p_port_15.setData, int(29))
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
        # *p_port_16* updates
        if p_port_16.status == NOT_STARTED and t >= 30.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_16.frameNStart = frameN  # exact frame index
            p_port_16.tStart = t  # local t and not account for scr refresh
            p_port_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_16.started', t)
            p_port_16.status = STARTED
            win.callOnFlip(p_port_16.setData, int(30))
        if p_port_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_16.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_16.tStop = t  # not accounting for scr refresh
                p_port_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_16.stopped', t)
                p_port_16.status = FINISHED
                win.callOnFlip(p_port_16.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Break" ---
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_15.status == STARTED:
        win.callOnFlip(p_port_15.setData, int(0))
    if p_port_16.status == STARTED:
        win.callOnFlip(p_port_16.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.100000)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'Blocks_of_Tastants'


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
