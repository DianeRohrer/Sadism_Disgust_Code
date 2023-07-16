#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Sun Jul 16 12:28:48 2023
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'MoralCondition'  # from the Builder filename that created this script
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
    originPath='/Users/hopswork/projects/Sadism_Disgust_Code/MoralCondition_lastrun.py',
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

# --- Initialize components for Routine "Game_Start" ---
Game_Start_Text = visual.TextStim(win=win, name='Game_Start_Text',
    text='Press the spacebar to start the game. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Fixation_Cross" ---
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Opponent" ---
player_image_intro = visual.ImageStim(
    win=win,
    name='player_image_intro', units='norm', 
    image='brandon is hot stuff', mask=None, anchor='center',
    ori=0.0, pos=(-.75, .5), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
player_name_intro = visual.TextBox2(
     win, text=opponent_names[0], placeholder='Type here...', font='Open Sans',
     pos=(.75, .5),     letterHeight=0.08,
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
     name='player_name_intro',
     depth=-1, autoLog=True,
)

# --- Initialize components for Routine "Offer" ---
player_image_offer = visual.ImageStim(
    win=win,
    name='player_image_offer', 
    image=opponent_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(-.75, .5), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
player_name_offer = visual.TextBox2(
     win, text=opponent_names.pop(0), placeholder='Type here...', font='Open Sans',
     pos=(.75, .5),     letterHeight=0.08,
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
     name='player_name_offer',
     depth=-1, autoLog=True,
)
proposed_split = visual.TextStim(win=win, name='proposed_split',
    text=bet_phrases.pop(0),
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

# --- Initialize components for Routine "Arrows" ---
arrow_instructions = visual.TextStim(win=win, name='arrow_instructions',
    text='Press the "up" arrow to accept\n\nPress the "down"arrow to reject',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
offer_choice = keyboard.Keyboard()

# --- Initialize components for Routine "Non_Verbal_Instructions" ---
Instructions_Affinity_Score = visual.TextStim(win=win, name='Instructions_Affinity_Score',
    text='Please rate on the following scale how well each face captures your feelings about the offer you received. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Non_Verbal" ---
Emotion_Image = visual.ImageStim(
    win=win,
    name='Emotion_Image', 
    image=emotion_filenames.pop(0), mask=None, anchor='center',
    ori=0.0, pos=(0, .25), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AffinityScore = visual.Slider(win=win, name='AffinityScore',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Very untrue of me", "Untrue of me", "Somewhat untrue of me", "Neurtral", "Somewhat true of me", "True of me", "Very true of me"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor=[1.0000, -1.0000, -1.0000], lineColor=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Verbal" ---
Instruction = visual.TextStim(win=win, name='Instruction',
    text='Please rate on the following scale how morally wrong you felt the offer you received was. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Moral_Disgust_Score = visual.Slider(win=win, name='Moral_Disgust_Score',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=("Extremely Immoral", "Immoral", "Somewhat Immoral", "Neutral", "Somewhat Moral", "Moral", "Extremely Moral"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.8, 0.8, 0.8], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Game_Start" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Game_StartComponents = [Game_Start_Text, key_resp]
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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Game_Start_Text* updates
    
    # if Game_Start_Text is starting this frame...
    if Game_Start_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Game_Start_Text.frameNStart = frameN  # exact frame index
        Game_Start_Text.tStart = t  # local t and not account for scr refresh
        Game_Start_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Game_Start_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Game_Start_Text.started')
        # update status
        Game_Start_Text.status = STARTED
        Game_Start_Text.setAutoDraw(True)
    
    # if Game_Start_Text is active this frame...
    if Game_Start_Text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
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
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
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
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
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
    # update component parameters for each repeat
    # keep track of which components have finished
    Fixation_CrossComponents = [fixation_cross]
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
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        
        # if fixation_cross is starting this frame...
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross.started')
            # update status
            fixation_cross.status = STARTED
            fixation_cross.setAutoDraw(True)
        
        # if fixation_cross is active this frame...
        if fixation_cross.status == STARTED:
            # update params
            pass
        
        # if fixation_cross is stopping this frame...
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                # update status
                fixation_cross.status = FINISHED
                fixation_cross.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "Opponent" ---
    continueRoutine = True
    # update component parameters for each repeat
    player_name_intro.reset()
    # keep track of which components have finished
    OpponentComponents = [player_image_intro, player_name_intro]
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
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *player_image_intro* updates
        
        # if player_image_intro is starting this frame...
        if player_image_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_image_intro.frameNStart = frameN  # exact frame index
            player_image_intro.tStart = t  # local t and not account for scr refresh
            player_image_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_image_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_image_intro.started')
            # update status
            player_image_intro.status = STARTED
            player_image_intro.setAutoDraw(True)
        
        # if player_image_intro is active this frame...
        if player_image_intro.status == STARTED:
            # update params
            pass
        
        # if player_image_intro is stopping this frame...
        if player_image_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_image_intro.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                player_image_intro.tStop = t  # not accounting for scr refresh
                player_image_intro.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_image_intro.stopped')
                # update status
                player_image_intro.status = FINISHED
                player_image_intro.setAutoDraw(False)
        
        # *player_name_intro* updates
        
        # if player_name_intro is starting this frame...
        if player_name_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_name_intro.frameNStart = frameN  # exact frame index
            player_name_intro.tStart = t  # local t and not account for scr refresh
            player_name_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_name_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_name_intro.started')
            # update status
            player_name_intro.status = STARTED
            player_name_intro.setAutoDraw(True)
        
        # if player_name_intro is active this frame...
        if player_name_intro.status == STARTED:
            # update params
            pass
        
        # if player_name_intro is stopping this frame...
        if player_name_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_name_intro.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                player_name_intro.tStop = t  # not accounting for scr refresh
                player_name_intro.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_name_intro.stopped')
                # update status
                player_name_intro.status = FINISHED
                player_name_intro.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "Offer" ---
    continueRoutine = True
    # update component parameters for each repeat
    player_name_offer.reset()
    # keep track of which components have finished
    OfferComponents = [player_image_offer, player_name_offer, proposed_split, accept_reject]
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
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *player_image_offer* updates
        
        # if player_image_offer is starting this frame...
        if player_image_offer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_image_offer.frameNStart = frameN  # exact frame index
            player_image_offer.tStart = t  # local t and not account for scr refresh
            player_image_offer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_image_offer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_image_offer.started')
            # update status
            player_image_offer.status = STARTED
            player_image_offer.setAutoDraw(True)
        
        # if player_image_offer is active this frame...
        if player_image_offer.status == STARTED:
            # update params
            pass
        
        # if player_image_offer is stopping this frame...
        if player_image_offer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_image_offer.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                player_image_offer.tStop = t  # not accounting for scr refresh
                player_image_offer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_image_offer.stopped')
                # update status
                player_image_offer.status = FINISHED
                player_image_offer.setAutoDraw(False)
        
        # *player_name_offer* updates
        
        # if player_name_offer is starting this frame...
        if player_name_offer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player_name_offer.frameNStart = frameN  # exact frame index
            player_name_offer.tStart = t  # local t and not account for scr refresh
            player_name_offer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player_name_offer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'player_name_offer.started')
            # update status
            player_name_offer.status = STARTED
            player_name_offer.setAutoDraw(True)
        
        # if player_name_offer is active this frame...
        if player_name_offer.status == STARTED:
            # update params
            pass
        
        # if player_name_offer is stopping this frame...
        if player_name_offer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > player_name_offer.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                player_name_offer.tStop = t  # not accounting for scr refresh
                player_name_offer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'player_name_offer.stopped')
                # update status
                player_name_offer.status = FINISHED
                player_name_offer.setAutoDraw(False)
        
        # *proposed_split* updates
        
        # if proposed_split is starting this frame...
        if proposed_split.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proposed_split.frameNStart = frameN  # exact frame index
            proposed_split.tStart = t  # local t and not account for scr refresh
            proposed_split.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proposed_split, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proposed_split.started')
            # update status
            proposed_split.status = STARTED
            proposed_split.setAutoDraw(True)
        
        # if proposed_split is active this frame...
        if proposed_split.status == STARTED:
            # update params
            pass
        
        # if proposed_split is stopping this frame...
        if proposed_split.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > proposed_split.tStartRefresh + 5.7-frameTolerance:
                # keep track of stop time/frame for later
                proposed_split.tStop = t  # not accounting for scr refresh
                proposed_split.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'proposed_split.stopped')
                # update status
                proposed_split.status = FINISHED
                proposed_split.setAutoDraw(False)
        
        # *accept_reject* updates
        
        # if accept_reject is starting this frame...
        if accept_reject.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            accept_reject.frameNStart = frameN  # exact frame index
            accept_reject.tStart = t  # local t and not account for scr refresh
            accept_reject.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(accept_reject, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'accept_reject.started')
            # update status
            accept_reject.status = STARTED
            accept_reject.setAutoDraw(True)
        
        # if accept_reject is active this frame...
        if accept_reject.status == STARTED:
            # update params
            pass
        
        # if accept_reject is stopping this frame...
        if accept_reject.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > accept_reject.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                accept_reject.tStop = t  # not accounting for scr refresh
                accept_reject.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'accept_reject.stopped')
                # update status
                accept_reject.status = FINISHED
                accept_reject.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    
    # --- Prepare to start Routine "Arrows" ---
    continueRoutine = True
    # update component parameters for each repeat
    offer_choice.keys = []
    offer_choice.rt = []
    _offer_choice_allKeys = []
    # keep track of which components have finished
    ArrowsComponents = [arrow_instructions, offer_choice]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *arrow_instructions* updates
        
        # if arrow_instructions is starting this frame...
        if arrow_instructions.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            arrow_instructions.frameNStart = frameN  # exact frame index
            arrow_instructions.tStart = t  # local t and not account for scr refresh
            arrow_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arrow_instructions.started')
            # update status
            arrow_instructions.status = STARTED
            arrow_instructions.setAutoDraw(True)
        
        # if arrow_instructions is active this frame...
        if arrow_instructions.status == STARTED:
            # update params
            pass
        
        # *offer_choice* updates
        waitOnFlip = False
        
        # if offer_choice is starting this frame...
        if offer_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            offer_choice.frameNStart = frameN  # exact frame index
            offer_choice.tStart = t  # local t and not account for scr refresh
            offer_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(offer_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'offer_choice.started')
            # update status
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
                offer_choice.duration = _offer_choice_allKeys[-1].duration
                # a response ends the routine
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
        loop.addData('offer_choice.duration', offer_choice.duration)
    # the Routine "Arrows" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal_Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Non_Verbal_InstructionsComponents = [Instructions_Affinity_Score]
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
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Affinity_Score* updates
        
        # if Instructions_Affinity_Score is starting this frame...
        if Instructions_Affinity_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Affinity_Score.frameNStart = frameN  # exact frame index
            Instructions_Affinity_Score.tStart = t  # local t and not account for scr refresh
            Instructions_Affinity_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Affinity_Score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Affinity_Score.started')
            # update status
            Instructions_Affinity_Score.status = STARTED
            Instructions_Affinity_Score.setAutoDraw(True)
        
        # if Instructions_Affinity_Score is active this frame...
        if Instructions_Affinity_Score.status == STARTED:
            # update params
            pass
        
        # if Instructions_Affinity_Score is stopping this frame...
        if Instructions_Affinity_Score.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Instructions_Affinity_Score.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_Affinity_Score.tStop = t  # not accounting for scr refresh
                Instructions_Affinity_Score.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Instructions_Affinity_Score.stopped')
                # update status
                Instructions_Affinity_Score.status = FINISHED
                Instructions_Affinity_Score.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Non_Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    AffinityScore.reset()
    # keep track of which components have finished
    Non_VerbalComponents = [Emotion_Image, AffinityScore]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emotion_Image* updates
        
        # if Emotion_Image is starting this frame...
        if Emotion_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emotion_Image.frameNStart = frameN  # exact frame index
            Emotion_Image.tStart = t  # local t and not account for scr refresh
            Emotion_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emotion_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Emotion_Image.started')
            # update status
            Emotion_Image.status = STARTED
            Emotion_Image.setAutoDraw(True)
        
        # if Emotion_Image is active this frame...
        if Emotion_Image.status == STARTED:
            # update params
            pass
        
        # *AffinityScore* updates
        
        # if AffinityScore is starting this frame...
        if AffinityScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AffinityScore.frameNStart = frameN  # exact frame index
            AffinityScore.tStart = t  # local t and not account for scr refresh
            AffinityScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AffinityScore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AffinityScore.started')
            # update status
            AffinityScore.status = STARTED
            AffinityScore.setAutoDraw(True)
        
        # if AffinityScore is active this frame...
        if AffinityScore.status == STARTED:
            # update params
            pass
        
        # Check AffinityScore for response to end routine
        if AffinityScore.getRating() is not None and AffinityScore.status == STARTED:
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
    loop.addData('AffinityScore.response', AffinityScore.getRating())
    loop.addData('AffinityScore.rt', AffinityScore.getRT())
    # the Routine "Non_Verbal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Verbal" ---
    continueRoutine = True
    # update component parameters for each repeat
    Moral_Disgust_Score.reset()
    # keep track of which components have finished
    VerbalComponents = [Instruction, Moral_Disgust_Score]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction* updates
        
        # if Instruction is starting this frame...
        if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.tStart = t  # local t and not account for scr refresh
            Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction.started')
            # update status
            Instruction.status = STARTED
            Instruction.setAutoDraw(True)
        
        # if Instruction is active this frame...
        if Instruction.status == STARTED:
            # update params
            pass
        
        # *Moral_Disgust_Score* updates
        
        # if Moral_Disgust_Score is starting this frame...
        if Moral_Disgust_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Moral_Disgust_Score.frameNStart = frameN  # exact frame index
            Moral_Disgust_Score.tStart = t  # local t and not account for scr refresh
            Moral_Disgust_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Moral_Disgust_Score, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Moral_Disgust_Score.started')
            # update status
            Moral_Disgust_Score.status = STARTED
            Moral_Disgust_Score.setAutoDraw(True)
        
        # if Moral_Disgust_Score is active this frame...
        if Moral_Disgust_Score.status == STARTED:
            # update params
            pass
        
        # Check Moral_Disgust_Score for response to end routine
        if Moral_Disgust_Score.getRating() is not None and Moral_Disgust_Score.status == STARTED:
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
