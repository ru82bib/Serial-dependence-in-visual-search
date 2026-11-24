#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Tue Nov 24 10:06:20 2026
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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'search_chen'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'block': '2',
    'age': '',
    'gender': '',
    'handness': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/siyichen/Downloads/search_experiments/experiment_1/exp_1_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1200], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='deg'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'deg'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
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
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "ins" ---
    ins3 = visual.ImageStim(
        win=win,
        name='ins3', 
        image='Slide4.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(35, 25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixation" ---
    cross = visual.ShapeStim(
        win=win, name='cross', vertices='cross',
        size=(0.5, 0.5),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from trial_code
    # All RTs from correct trials
    rt_list = []
    correct_responses = []
    
    # Counters for each probe type
    probe_counts = {'fast': 0, 'avg': 0, 'slow': 0, 'ran': 0}
    max_probes = 14
    total_probe_limit = 42
    
    # Control when a probe was last shown
    trials_since_last_probe = 99  # just large to begin
    
    # For identifying if current trial is a probe
    next_is_probe = False
    next_probe_type = None
    previous_was_probe = False
    response_error = False
    no_response = False
    correct_response = None
    feedback_reps = 0
    instruction_text = visual.TextStim(win=win, name='instruction_text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color=[1.0000, 0.2941, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard()
    fix_cross = visual.ShapeStim(
        win=win, name='fix_cross', vertices='cross',
        size=(0.5, 0.5),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ITI" ---
    # Run 'Begin Experiment' code from iti_code
    import numpy as np
    iti_dur = 0
    iti_blank = visual.TextStim(win=win, name='iti_blank',
        text=None,
        font='Arial',
        pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end" ---
    key_resp_3 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "ins" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ins.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    insComponents = [ins3, key_resp_2]
    for thisComponent in insComponents:
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
    
    # --- Run Routine "ins" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ins3* updates
        
        # if ins3 is starting this frame...
        if ins3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins3.frameNStart = frameN  # exact frame index
            ins3.tStart = t  # local t and not account for scr refresh
            ins3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins3.started')
            # update status
            ins3.status = STARTED
            ins3.setAutoDraw(True)
        
        # if ins3 is active this frame...
        if ins3.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in insComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins" ---
    for thisComponent in insComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ins.stopped', globalClock.getTime())
    # the Routine "ins" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fixation.started', globalClock.getTime())
    # keep track of which components have finished
    fixationComponents = [cross]
    for thisComponent in fixationComponents:
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
    
    # --- Run Routine "fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
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
            if tThisFlipGlobal > cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fixation.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=15.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conds_10pctRed.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from trial_code
        import numpy as np 
        import random
        
        if 'carry_shape' not in globals():
            carry_shape = None
            
        # for before trial fixation
        pre_fix_clock = core.Clock() 
        pre_fix_phase = True 
        pre_fix_dur = 0.5
        
        response_error = False
        no_response = False
        correct_response = None
        feedback = False
        # Set timing
        stim_clock = core.Clock()
        instruction_timer = core.Clock()
        fix_clock = core.Clock()
        
        show_instructions = next_is_probe
        #show_stimuli = not next_is_probe
        pre_fix_phase = not show_instructions
        show_fix = not show_instructions
        stim_duration = 0.8  # shapes shown for 800ms
        total_duration = 1.3  # shapes + response window (800ms + 1s)
        
        if show_instructions:
            carry_shape = Shape  # remember what we just instructed
        
        ShapeForStim = carry_shape if previous_was_probe else Shape
        
        is_probe = next_is_probe
        probe_type = next_probe_type
        is_instruction_trial = next_is_probe  # trial n
        is_stimulus_trial = previous_was_probe  # trial n+1
        show_stimuli = True
        show_instruction = False
        #correct_resp = None
        
        # code from search_ex
        theta = [0, 45, 90, 135, 180, 225, 270, 315]
        thetarad = [t*pi/180 for t in theta]
        posx = [4*cos(t) for t in thetarad]
        posy = [4*sin(t) for t in thetarad]
        
        
        CircleDist = [visual.ShapeStim(
                win=win, name='',
                size=(2, 2), vertices='circle',
                ori=45.0, pos=[posx[i],posy[i]], 
                anchor='center',
                lineWidth=8.0, colorSpace='rgb',  
                lineColor='white', fillColor=None,
                opacity=1.0, depth=-1.0, interpolate=True)
                for i in range(8)]
                
        DiamondDist = [visual.Rect(
            win=win, name='',
            width=(2, 2)[0], height=(2, 2)[1],
            ori=45.0, pos=[posx[i],posy[i]],
            anchor='center',
            lineWidth=8.0, colorSpace='rgb', 
            lineColor='white', fillColor=None,
            opacity=1.0, depth=-2.0, interpolate=True)
            for i in range(8)]
            
        DistLines = [visual.Rect(
                win=win, name='TargetLine',
                width=(0.3, 1.5)[0], height=(0.3, 1.5)[1],
                ori=1.0, pos=[posx[i],posy[i]], anchor='center',
                lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
                opacity=None, depth=-3.0, interpolate=True)
                for i in range(8)]
        
        # adding target stimuli
        CircleTarget = visual.ShapeStim(
                win=win, name='CircleTarget',
                size=(2, 2), vertices='circle',
                ori=45.0, pos=[0,0], anchor='center',
                lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
                opacity=1.0, depth=-1.0, interpolate=True)
        DiamondTarget = visual.Rect(
                win=win, name='DiamondTarget',
                width=(2, 2)[0], height=(2, 2)[1],
                ori=45.0, pos=[0,0], anchor='center',
                lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
                opacity=1.0, depth=-2.0, interpolate=True)
        TargetLine = visual.Rect(
                win=win, name='TargetLine',
                width=(0.3, 1.5)[0], height=(0.3, 1.5)[1],
                ori=1.0, pos=[0,0], anchor='center',
                lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
                opacity=None, depth=-3.0, interpolate=True)
        
        CircleTarget.setPos((posx[TarPos], posy[TarPos]))
        CircleTarget.setLineColor(Color)
        CircleTarget.setLineWidth((8 if ShapeForStim=="Circle" else 0))
        DiamondTarget.setPos((posx[TarPos], posy[TarPos]))
        DiamondTarget.setLineColor(Color)
        DiamondTarget.setLineWidth((0 if ShapeForStim=="Circle" else 8) )
        TargetLine.setPos((posx[TarPos], posy[TarPos]))
        TargetLine.setOri(LineOri)
        
        DistOri = [np.random.randint(2)*90 for i in range(8)]
        shapes = []
        if ShapeForStim == "Circle":
            for i in range(8):
                if i == TarPos:
                    shapes.append(CircleTarget)
                    shapes.append(TargetLine)
                    continue
                if i != TarPos:
                    DiamondDist[i].lineColor = Color
                    DistLines[i].ori = DistOri[i]
                    shapes.append(DiamondDist[i])
                    shapes.append(DistLines[i])
                    
        else:
           for i in range(8):
                if i == TarPos:
                    shapes.append(DiamondTarget)
                    shapes.append(TargetLine)
                    continue
                if i != TarPos:
                    CircleDist[i].lineColor = Color
                    DistLines[i].ori = DistOri[i]
                    shapes.append(CircleDist[i])
                    shapes.append(DistLines[i])
        
        '''for i in range(8):
            if i != TarPos:
                DistLines[i].setOri(DistOri[i])
                DistLines[i].setAutoDraw(True)'''
        
        stim_started = False
        
        # instruction text toggle
        if show_instructions:  
            pre_fix_phase = False
            instruction_timer.reset()
            instruction_text.text = "Search for " + Shape
            instruction_text.setAutoDraw(True)
            fix_cross.setAutoDraw(False)
            correct_response = 'up' if LineOri == 0 else 'left'
        else:
            pre_fix_phase = True
            pre_fix_clock.reset()
            instruction_text.setAutoDraw(False)
            fix_cross.setAutoDraw(True)
            correct_response = 'q' if Color == 'Lawngreen' else 'w'
        
        thisExp.addData('DistOri', DistOri)
                    
        # Save data
        thisExp.addData('show_instruction', show_instruction)
        thisExp.addData('show_stimuli', show_stimuli)
        
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [instruction_text, key_resp, fix_cross]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from trial_code
            # Instruction timing
            if show_instructions:
                # ensure nothing else is on while instruction shows
                if stim_started:
                    for s in shapes: 
                        s.setAutoDraw(False)
                    stim_started = False
            
                instruction_text.setAutoDraw(True)
                fix_cross.setAutoDraw(False)
            
                #if instruction_timer.getTime() >= 1.0:
                if instruction_timer.getTime() >= 0.5:
                    # transition to stimulus phase without ending the trial
                    show_instructions = False
                
                    # clean up instruction visuals
                    instruction_text.setAutoDraw(False)
                    #show_stimuli = True
                    #show_fix = True
                    #fix_clock.reset()
                    pre_fix_phase = True
                    pre_fix_clock.reset()
                    fix_cross.setAutoDraw(True)
            
                #    (re)start stimulus timing
                    #stim_started = False
                    #stim_clock.reset()
                    #key_resp.clock.reset()
            
            # new fixation before trial block
            # Pre-fixation: 500 ms of fixation-only before stimuli
            if pre_fix_phase:
                fix_cross.setAutoDraw(True)
                # make sure stimuli are off
                if stim_started:
                    for s in shapes:
                        s.setAutoDraw(False)
                    stim_started = False
            
                if pre_fix_clock.getTime() >= pre_fix_dur:
                    pre_fix_phase = False
                    show_stimuli = True
                    stim_clock.reset()
                    key_resp.clock.reset()
            
            
            # Stimulus timing
            if show_stimuli and not show_instructions and not pre_fix_phase:
                if not stim_started:
                    stim_clock.reset()
                    key_resp.clock.reset()
                    for s in shapes: 
                        s.setAutoDraw(True)
                    stim_started = True
            
                if stim_clock.getTime() >= stim_duration or key_resp.keys:
                    for s in shapes: 
                        s.setAutoDraw(False)
                    continueRoutine = False  # or leave True if you want a post-stim window
            
            # Safety: if we’re about to leave, make sure nothing remains
            if not continueRoutine:
                for s in shapes: s.setAutoDraw(False)
                instruction_text.setAutoDraw(False)
            
            
            
            # *instruction_text* updates
            
            # if instruction_text is starting this frame...
            if instruction_text.status == NOT_STARTED and is_probe:
                # keep track of start time/frame for later
                instruction_text.frameNStart = frameN  # exact frame index
                instruction_text.tStart = t  # local t and not account for scr refresh
                instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_text.started')
                # update status
                instruction_text.status = STARTED
                instruction_text.setAutoDraw(True)
            
            # if instruction_text is active this frame...
            if instruction_text.status == STARTED:
                # update params
                pass
            
            # if instruction_text is stopping this frame...
            if instruction_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > instruction_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    instruction_text.tStop = t  # not accounting for scr refresh
                    instruction_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_text.stopped')
                    # update status
                    instruction_text.status = FINISHED
                    instruction_text.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','up','q','w'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
            
            # *fix_cross* updates
            
            # if fix_cross is starting this frame...
            if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross.frameNStart = frameN  # exact frame index
                fix_cross.tStart = t  # local t and not account for scr refresh
                fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross.started')
                # update status
                fix_cross.status = STARTED
                fix_cross.setAutoDraw(True)
            
            # if fix_cross is active this frame...
            if fix_cross.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # Run 'End Routine' code from trial_code
        response = key_resp.keys if key_resp.keys else None
        rt = key_resp.rt if key_resp.keys else None
        correct = 0
        response_error = False
        feedback_reps = 0
        no_response = False
        response_error = False
        correct = 0
        
        response = key_resp.keys if key_resp.keys else None
        rt = key_resp.rt if key_resp.keys else None
        
        if response is None:
            no_response = True
            feedback_reps = 1          # show "Too slow" feedback
        
        elif response == correct_response:
            correct = 1                # correct; no feedback
        
        else:  # response != correct_response
            response_error = True
            if is_probe:               # only probes get error feedback
                feedback_reps = 1
        
        '''if response is not None:    
            print("correct response: " + correct_response)
            print("response: " + response)'''
            
        correct_responses.append(correct)
        # code from search_ex
        for d in DiamondDist:
            d.setAutoDraw(False)
        for d in CircleDist:
            d.setAutoDraw(False)
        for i in range(8):
            DistLines[i].setAutoDraw(False)
        # end code from search_ex
        
        # After trials
        total_trials = len(correct_responses)
        total_correct = sum(correct_responses)
        accuracy = total_correct / total_trials if total_trials > 0 else 0
        accuracy_percent = round(accuracy * 100, 2)
        
        thisExp.addData('response', response)
        thisExp.addData('rt', rt)
        thisExp.addData('correct_response', correct_response)
        thisExp.addData('correct', correct)
        thisExp.addData('correct_sum', accuracy_percent)
        thisExp.addData('is_probe', is_probe)
        thisExp.addData('probe_type', probe_type)
        thisExp.addData('rt_mu', mu if 'mu' in locals() else '')
        thisExp.addData('rt_sigma', sigma if 'sigma' in locals() else '')
        thisExp.addData('rt_recent', recent_rt if 'recent_rt' in locals() else '')
        
        
        instruction_text.setAutoDraw(False)
        
        if rt is not None:
            rt_list.append(rt)
            
        # Update trial gap counter
        if next_is_probe:
            trials_since_last_probe = 0
        else:
            trials_since_last_probe += 1
        
        # Compute μ and σ after 80 trials
        next_is_probe = False  # default
        next_probe_type = None
        
        if len(rt_list) >= 60:
            mu = np.mean(rt_list)
            sigma = np.std(rt_list)
            recent_rts = rt_list[-3:]
            if len(recent_rts) == 3:
                recent_rt = np.mean(recent_rts)
        
                if trials_since_last_probe > 3 and random.random() < 0.4 and sum(probe_counts.values()) < total_probe_limit:
                    if recent_rt < (mu - sigma) and probe_counts['fast'] < max_probes:
                        next_is_probe = True
                        next_probe_type = 'fast'
                        probe_counts['fast'] += 1
                    elif recent_rt > (mu + sigma) and probe_counts['slow'] < max_probes:
                        next_is_probe = True
                        next_probe_type = 'slow'
                        probe_counts['slow'] += 1
                    elif trials_since_last_probe > 50 and (mu - sigma) <= recent_rt <= (mu + sigma) and probe_counts['avg'] < max_probes:
                        next_is_probe = True
                        next_probe_type = 'avg'
                        probe_counts['avg'] += 1
        elif len(rt_list) < 60:
            if trials_since_last_probe > 10 and random.random() < 0.4 and probe_counts['ran'] < 4:
                next_is_probe = True
                next_probe_type = 'ran'
                probe_counts['ran'] += 1
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        feedback_loop = data.TrialHandler(nReps=feedback_reps, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='feedback_loop')
        thisExp.addLoop(feedback_loop)  # add the loop to the experiment
        thisFeedback_loop = feedback_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_loop.rgb)
        if thisFeedback_loop != None:
            for paramName in thisFeedback_loop:
                globals()[paramName] = thisFeedback_loop[paramName]
        
        for thisFeedback_loop in feedback_loop:
            currentLoop = feedback_loop
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisFeedback_loop.rgb)
            if thisFeedback_loop != None:
                for paramName in thisFeedback_loop:
                    globals()[paramName] = thisFeedback_loop[paramName]
            
            # --- Prepare to start Routine "feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('feedback.started', globalClock.getTime())
            feedback_text.setText('')
            # Run 'Begin Routine' code from feedback_code
            feedback_text.text = ''
            
            if is_probe:
                if no_response:
                    feedback_text.text = 'Too slow'
                elif response_error:
                    feedback_text.text = 'Error'
                
            if no_response and not is_probe:
                feedback_text.text = 'Too slow'
            # keep track of which components have finished
            feedbackComponents = [feedback_text]
            for thisComponent in feedbackComponents:
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
            
            # --- Run Routine "feedback" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text* updates
                
                # if feedback_text is starting this frame...
                if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text.frameNStart = frameN  # exact frame index
                    feedback_text.tStart = t  # local t and not account for scr refresh
                    feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.started')
                    # update status
                    feedback_text.status = STARTED
                    feedback_text.setAutoDraw(True)
                
                # if feedback_text is active this frame...
                if feedback_text.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text is stopping this frame...
                if feedback_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text.tStop = t  # not accounting for scr refresh
                        feedback_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                        # update status
                        feedback_text.status = FINISHED
                        feedback_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('feedback.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed feedback_reps repeats of 'feedback_loop'
        
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from iti_code
        iti_dur = float(np.random.uniform(0.5, 0.75))
        thisExp.addData('iti_dur', iti_dur)
        # keep track of which components have finished
        ITIComponents = [iti_blank]
        for thisComponent in ITIComponents:
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
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti_blank* updates
            
            # if iti_blank is starting this frame...
            if iti_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti_blank.frameNStart = frameN  # exact frame index
                iti_blank.tStart = t  # local t and not account for scr refresh
                iti_blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti_blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'iti_blank.started')
                # update status
                iti_blank.status = STARTED
                iti_blank.setAutoDraw(True)
            
            # if iti_blank is active this frame...
            if iti_blank.status == STARTED:
                # update params
                pass
            
            # if iti_blank is stopping this frame...
            if iti_blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iti_blank.tStartRefresh + iti_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    iti_blank.tStop = t  # not accounting for scr refresh
                    iti_blank.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti_blank.stopped')
                    # update status
                    iti_blank.status = FINISHED
                    iti_blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 15.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    endComponents = [key_resp_3]
    for thisComponent in endComponents:
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
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from code
    # Display result
    
    final_message = f"Block1 {accuracy_percent}%."
    
    text1 = visual.TextStim(win, text=final_message, height=1.5, pos=(-3, 0), wrapWidth=1.5)
    
    # Draw both texts
    text1.draw()
    
    # Show on screen
    win.flip()
    core.wait(3)  # Small delay to prevent CPU overload
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
