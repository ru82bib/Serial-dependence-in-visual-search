#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed Nov 18 11:20:27 2026
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
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {
    'ID': '',
    'Name': '',
    'Gender': '',
    'Age': '',
    'Session': '0',
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
    filename = u'data/%s_Order_%s_%s' % (expInfo['ID'], expInfo['Session'], expInfo['Name'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/siyichen/Downloads/Direction_Wed_tutorial finalcode/Direction1_2024_beha_lastrun.py',
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
    logging.console.setLevel(logging.DEBUG)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
    
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
            units='height'
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
        win.units = 'height'
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
    
    # --- Initialize components for Routine "Instruction" ---
    # Run 'Begin Experiment' code from code_SubID
    time=core.Clock()
    win.mouseVisible = False
    from psychopy.hardware import keyboard
    kb = keyboard.Keyboard()
    
    import random
    Sub_ID = expInfo['ID']
    
    Sub_Order = expInfo['Session']
    SubList = "TimeDirect_Conditions_2024_beha/sub"+str(Sub_ID)+".csv"
    
    Ins_image = visual.ImageStim(
        win=win,
        name='Ins_image', units='norm', 
        image='Instruction.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-1.0)
    Ins_Key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "block" ---
    # Run 'Begin Experiment' code from Block_code_2
    Block_text=''
    Block_id = 0
    Block_num = 8
    Block_trial = 68
    Practice_num = 10 # start from 0
    Block_t_2 = visual.TextStim(win=win, name='Block_t_2',
        text='',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    Block_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    Blank_text = visual.TextStim(win=win, name='Blank_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fixation" ---
    Fixation_1 = visual.Polygon(
        win=win, name='Fixation_1',units='deg', 
        edges=360, size=(0.5, 0.5),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Grating" ---
    Fixation_2 = visual.Polygon(
        win=win, name='Fixation_2',units='deg', 
        edges=360, size=(0.5, 0.5),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    grating = visual.GratingStim(
        win=win, name='grating',units='deg', 
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(-6.5, 0), size=(9, 9), sf=1.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=1.0, contrast=0.25, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-1.0)
    grating_2 = visual.GratingStim(
        win=win, name='grating_2',units='deg', 
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(6.5, 0), size=(9, 9), sf=1.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=1.0, contrast=0.25, blendmode='add',
        texRes=512.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "noise" ---
    # Run 'Begin Experiment' code from noisecode
    import numpy as np
    from scipy.ndimage import gaussian_filter
    
    # Screen and visual parameters
    viewing_distance_cm = 57  # Viewing distance in cm
    screen_height_cm = 30     # Physical screen height in cm
    resolution_px = 256       # Texture resolution (power of 2, e.g., 256x256)
    degrees_per_pixel = 2 * np.arctan((screen_height_cm / 2) / viewing_distance_cm) * (180 / np.pi) / win.size[1]
    
    # Noise and Gaussian parameters
    gaussian_kernel_sd_deg = 0.91  # Gaussian kernel s.d. in degrees
    gaussian_window_sd_deg = 1.5  # Gaussian window s.d. in degrees
    
    # Convert degrees to pixels
    gaussian_kernel_sd_px = gaussian_kernel_sd_deg / degrees_per_pixel
    gaussian_window_sd_px = gaussian_window_sd_deg / degrees_per_pixel
    
    noisePatch1 = visual.ImageStim(
        win=win,
        name='noisePatch1', units='deg', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(-6.5, 0), size=(9, 9),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    noisePatch2 = visual.ImageStim(
        win=win,
        name='noisePatch2', units='deg', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(6.5, 0), size=(9, 9),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    fixation2 = visual.Polygon(
        win=win, name='fixation2',units='deg', 
        edges=360, size=(0.5, 0.5),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "fixation2_2" ---
    fixation_2 = visual.Polygon(
        win=win, name='fixation_2',units='deg', 
        edges=360, size=(0.5, 0.5),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "cue_2" ---
    tricue = visual.ShapeStim(
        win=win, name='tricue',units='deg', 
        size=(0.5, 0.5), vertices='triangle',
        ori=1.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Response_D_new" ---
    # Run 'Begin Experiment' code from Resp_D_code_2
    from psychopy.hardware import keyboard
    import math
    
    #if Sub_Order == '1':
    #    PointerMove = - 0.5
        
    #if Sub_Order == '2':
    #    PointerMove = 0.5
    BKG_7 = visual.Polygon(
        win=win, name='BKG_7',
        edges=360, size=(0.35, 0.35),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=5,     colorSpace='rgb',  lineColor=[0.0035,0.0035,0.0035], fillColor=[0.0035,0.0035,0.0035],
        opacity=1, depth=-1.0, interpolate=True)
    Circle = visual.Polygon(
        win=win, name='Circle',
        edges=360, size=(0.03, 0.03),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-2.0, interpolate=True)
    Line_2 = visual.Line(
        win=win, name='Line_2',
        start=(-(0,0)[0]/2.0, 0), end=(+(0,0)[0]/2.0, 0),
        ori=30, pos=[0,0], anchor='center',
        lineWidth=8,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "Feedback_for_Direction" ---
    # Run 'Begin Experiment' code from Feedback_code_3
    PresentDur = 0.5
    
    
    
    color_1 = [1,1,1];
    color_2 = [1,1,1];
    color_3 = [1,1,1];
    color_4 = [1,1,1];
    color_5 = [1,1,1];
    
    x_D_FD_1 = 0.2 * cos(150*math.pi/180)
    y_D_FD_1 = 0.2 * sin(150*math.pi/180)
    x_D_FD_2 = 0.2 * cos(120*math.pi/180)
    y_D_FD_2 = 0.2 * sin(120*math.pi/180)
    x_D_FD_3 = 0.2 * cos(90*math.pi/180)
    y_D_FD_3 = 0.2 * sin(90*math.pi/180)
    x_D_FD_4 = 0.2 * cos(60*math.pi/180)
    y_D_FD_4 = 0.2 * sin(60*math.pi/180)
    x_D_FD_5 = 0.2 * cos(30*math.pi/180)
    y_D_FD_5 = 0.2 * sin(30*math.pi/180)
    feedback_1_D = visual.Polygon(
        win=win, name='feedback_1_D',
        edges=3600, size=(0.035, 0.035),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-2.0, interpolate=True)
    feedback_2_D = visual.Polygon(
        win=win, name='feedback_2_D',
        edges=3600, size=(0.035, 0.035),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-3.0, interpolate=True)
    feedback_3_D = visual.Polygon(
        win=win, name='feedback_3_D',
        edges=3600, size=(0.035, 0.035),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-4.0, interpolate=True)
    feedback_4_D = visual.Polygon(
        win=win, name='feedback_4_D',
        edges=3600, size=(0.035, 0.035),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-5.0, interpolate=True)
    feedback_5_D = visual.Polygon(
        win=win, name='feedback_5_D',
        edges=3600, size=(0.035, 0.035),
        ori=0, pos=[0,0], anchor='center',
        lineWidth=0.5,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "Bye" ---
    Bye_text = visual.TextStim(win=win, name='Bye_text',
        text='The Experiment is done! Thanks for your participation!\n',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    Bye_resp = keyboard.Keyboard()
    
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
    
    # --- Prepare to start Routine "Instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_SubID
    win.mouseVisible = False
    Ins_Key.keys = []
    Ins_Key.rt = []
    _Ins_Key_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [Ins_image, Ins_Key]
    for thisComponent in InstructionComponents:
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
    
    # --- Run Routine "Instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_SubID
        win.mouseVisible = False
        
        # *Ins_image* updates
        
        # if Ins_image is starting this frame...
        if Ins_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ins_image.frameNStart = frameN  # exact frame index
            Ins_image.tStart = t  # local t and not account for scr refresh
            Ins_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ins_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ins_image.status = STARTED
            Ins_image.setAutoDraw(True)
        
        # if Ins_image is active this frame...
        if Ins_image.status == STARTED:
            # update params
            pass
        
        # *Ins_Key* updates
        
        # if Ins_Key is starting this frame...
        if Ins_Key.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ins_Key.frameNStart = frameN  # exact frame index
            Ins_Key.tStart = t  # local t and not account for scr refresh
            Ins_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ins_Key, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ins_Key.status = STARTED
            # keyboard checking is just starting
            Ins_Key.clock.reset()  # now t=0
            Ins_Key.clearEvents(eventType='keyboard')
        if Ins_Key.status == STARTED:
            theseKeys = Ins_Key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Ins_Key_allKeys.extend(theseKeys)
            if len(_Ins_Key_allKeys):
                Ins_Key.keys = _Ins_Key_allKeys[-1].name  # just the last key pressed
                Ins_Key.rt = _Ins_Key_allKeys[-1].rt
                Ins_Key.duration = _Ins_Key_allKeys[-1].duration
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
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction.stopped', globalClock.getTime())
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp.csv'),
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
        
        # --- Prepare to start Routine "block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block.started', globalClock.getTime())
        # Run 'Begin Routine' code from Block_code_2
        # practice start
        win.mouseVisible = False
        if trials.thisTrialN ==0:
            Block_text='Practice will start. '+' Please press s key to continue.'
            thisExp.addData('Block_exp', Block_id)
        # not practice or block start, then don't show the info of block
        elif trials.thisTrialN != Practice_num and trials.thisTrialN != Block_trial*Block_id+Practice_num:
            thisExp.addData('Block_exp', Block_id)
            continueRoutine = False
            
        else:
            # all blocks finished.
            if Block_id == Block_num: 
                thisExp.addData('Block_exp', Block_id)
                continueRoutine = False
            # each block start.
            else:
                thisExp.addData('Block_exp', Block_id)
                Block_id = Block_id+1
                Block_text='Block ('+ str(Block_id) +' / ' +str(Block_num) +  ') '+ ' will start. '+' Please press s key to continue.'
                
        Block_t_2.setText(Block_text)
        Block_resp_2.keys = []
        Block_resp_2.rt = []
        _Block_resp_2_allKeys = []
        # keep track of which components have finished
        blockComponents = [Block_t_2, Block_resp_2]
        for thisComponent in blockComponents:
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
        
        # --- Run Routine "block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Block_t_2* updates
            
            # if Block_t_2 is starting this frame...
            if Block_t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Block_t_2.frameNStart = frameN  # exact frame index
                Block_t_2.tStart = t  # local t and not account for scr refresh
                Block_t_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Block_t_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Block_t_2.started')
                # update status
                Block_t_2.status = STARTED
                Block_t_2.setAutoDraw(True)
            
            # if Block_t_2 is active this frame...
            if Block_t_2.status == STARTED:
                # update params
                pass
            
            # *Block_resp_2* updates
            waitOnFlip = False
            
            # if Block_resp_2 is starting this frame...
            if Block_resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Block_resp_2.frameNStart = frameN  # exact frame index
                Block_resp_2.tStart = t  # local t and not account for scr refresh
                Block_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Block_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Block_resp_2.started')
                # update status
                Block_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Block_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Block_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Block_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = Block_resp_2.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                _Block_resp_2_allKeys.extend(theseKeys)
                if len(_Block_resp_2_allKeys):
                    Block_resp_2.keys = _Block_resp_2_allKeys[-1].name  # just the last key pressed
                    Block_resp_2.rt = _Block_resp_2_allKeys[-1].rt
                    Block_resp_2.duration = _Block_resp_2_allKeys[-1].duration
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
            for thisComponent in blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block.stopped', globalClock.getTime())
        # check responses
        if Block_resp_2.keys in ['', [], None]:  # No response was made
            Block_resp_2.keys = None
        trials.addData('Block_resp_2.keys',Block_resp_2.keys)
        if Block_resp_2.keys != None:  # we had a response
            trials.addData('Block_resp_2.rt', Block_resp_2.rt)
            trials.addData('Block_resp_2.duration', Block_resp_2.duration)
        # the Routine "block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # keep track of which components have finished
        ITIComponents = [Blank_text]
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
            
            # *Blank_text* updates
            
            # if Blank_text is starting this frame...
            if Blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank_text.frameNStart = frameN  # exact frame index
                Blank_text.tStart = t  # local t and not account for scr refresh
                Blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                Blank_text.status = STARTED
                Blank_text.setAutoDraw(True)
            
            # if Blank_text is active this frame...
            if Blank_text.status == STARTED:
                # update params
                pass
            
            # if Blank_text is stopping this frame...
            if Blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank_text.tStartRefresh + round(2+random.random(),2)-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank_text.tStop = t  # not accounting for scr refresh
                    Blank_text.frameNStop = frameN  # exact frame index
                    # update status
                    Blank_text.status = FINISHED
                    Blank_text.setAutoDraw(False)
            
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
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # keep track of which components have finished
        fixationComponents = [Fixation_1]
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
        while continueRoutine and routineTimer.getTime() < 0.35:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_1* updates
            
            # if Fixation_1 is starting this frame...
            if Fixation_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_1.frameNStart = frameN  # exact frame index
                Fixation_1.tStart = t  # local t and not account for scr refresh
                Fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Fixation_1.status = STARTED
                Fixation_1.setAutoDraw(True)
            
            # if Fixation_1 is active this frame...
            if Fixation_1.status == STARTED:
                # update params
                pass
            
            # if Fixation_1 is stopping this frame...
            if Fixation_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_1.tStartRefresh + 0.35-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_1.tStop = t  # not accounting for scr refresh
                    Fixation_1.frameNStop = frameN  # exact frame index
                    # update status
                    Fixation_1.status = FINISHED
                    Fixation_1.setAutoDraw(False)
            
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
            routineTimer.addTime(-0.350000)
        
        # --- Prepare to start Routine "Grating" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Grating.started', globalClock.getTime())
        grating.setOri(90-LeftDirection)
        grating.setSF(cpdleft)
        grating_2.setOri(90-RightDirection)
        grating_2.setSF(cpdright)
        # keep track of which components have finished
        GratingComponents = [Fixation_2, grating, grating_2]
        for thisComponent in GratingComponents:
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
        
        # --- Run Routine "Grating" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_2* updates
            
            # if Fixation_2 is starting this frame...
            if Fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_2.frameNStart = frameN  # exact frame index
                Fixation_2.tStart = t  # local t and not account for scr refresh
                Fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Fixation_2.status = STARTED
                Fixation_2.setAutoDraw(True)
            
            # if Fixation_2 is active this frame...
            if Fixation_2.status == STARTED:
                # update params
                pass
            
            # if Fixation_2 is stopping this frame...
            if Fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_2.tStop = t  # not accounting for scr refresh
                    Fixation_2.frameNStop = frameN  # exact frame index
                    # update status
                    Fixation_2.status = FINISHED
                    Fixation_2.setAutoDraw(False)
            
            # *grating* updates
            
            # if grating is starting this frame...
            if grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grating.frameNStart = frameN  # exact frame index
                grating.tStart = t  # local t and not account for scr refresh
                grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating.started')
                # update status
                grating.status = STARTED
                grating.setAutoDraw(True)
            
            # if grating is active this frame...
            if grating.status == STARTED:
                # update params
                pass
            
            # if grating is stopping this frame...
            if grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grating.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    grating.tStop = t  # not accounting for scr refresh
                    grating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grating.stopped')
                    # update status
                    grating.status = FINISHED
                    grating.setAutoDraw(False)
            
            # *grating_2* updates
            
            # if grating_2 is starting this frame...
            if grating_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grating_2.frameNStart = frameN  # exact frame index
                grating_2.tStart = t  # local t and not account for scr refresh
                grating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grating_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_2.started')
                # update status
                grating_2.status = STARTED
                grating_2.setAutoDraw(True)
            
            # if grating_2 is active this frame...
            if grating_2.status == STARTED:
                # update params
                pass
            
            # if grating_2 is stopping this frame...
            if grating_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grating_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    grating_2.tStop = t  # not accounting for scr refresh
                    grating_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grating_2.stopped')
                    # update status
                    grating_2.status = FINISHED
                    grating_2.setAutoDraw(False)
            
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
            for thisComponent in GratingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Grating" ---
        for thisComponent in GratingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Grating.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "noise" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('noise.started', globalClock.getTime())
        # Run 'Begin Routine' code from noisecode
        # Create White Noise
        noise = np.random.uniform(-1, 1, (resolution_px, resolution_px))
        
        # Apply Gaussian Smoothing
        smoothed_noise = gaussian_filter(noise, gaussian_kernel_sd_px)
        
        # Create Gaussian Envelope (Window)
        x, y = np.meshgrid(np.linspace(-resolution_px / 2, resolution_px / 2, resolution_px),
                           np.linspace(-resolution_px / 2, resolution_px / 2, resolution_px))
        gaussian_envelope = np.exp(-0.5 * ((x**2 + y**2) / gaussian_window_sd_px**2))
        
        # Apply Gaussian Window to Noise
        windowed_noise = smoothed_noise * gaussian_envelope
        
        noisePatch1.image = windowed_noise
        noisePatch2.image = windowed_noise
        
        
        # keep track of which components have finished
        noiseComponents = [noisePatch1, noisePatch2, fixation2]
        for thisComponent in noiseComponents:
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
        
        # --- Run Routine "noise" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *noisePatch1* updates
            
            # if noisePatch1 is starting this frame...
            if noisePatch1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noisePatch1.frameNStart = frameN  # exact frame index
                noisePatch1.tStart = t  # local t and not account for scr refresh
                noisePatch1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noisePatch1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noisePatch1.started')
                # update status
                noisePatch1.status = STARTED
                noisePatch1.setAutoDraw(True)
            
            # if noisePatch1 is active this frame...
            if noisePatch1.status == STARTED:
                # update params
                pass
            
            # if noisePatch1 is stopping this frame...
            if noisePatch1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noisePatch1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    noisePatch1.tStop = t  # not accounting for scr refresh
                    noisePatch1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noisePatch1.stopped')
                    # update status
                    noisePatch1.status = FINISHED
                    noisePatch1.setAutoDraw(False)
            
            # *noisePatch2* updates
            
            # if noisePatch2 is starting this frame...
            if noisePatch2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noisePatch2.frameNStart = frameN  # exact frame index
                noisePatch2.tStart = t  # local t and not account for scr refresh
                noisePatch2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noisePatch2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noisePatch2.started')
                # update status
                noisePatch2.status = STARTED
                noisePatch2.setAutoDraw(True)
            
            # if noisePatch2 is active this frame...
            if noisePatch2.status == STARTED:
                # update params
                pass
            
            # if noisePatch2 is stopping this frame...
            if noisePatch2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noisePatch2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    noisePatch2.tStop = t  # not accounting for scr refresh
                    noisePatch2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noisePatch2.stopped')
                    # update status
                    noisePatch2.status = FINISHED
                    noisePatch2.setAutoDraw(False)
            
            # *fixation2* updates
            
            # if fixation2 is starting this frame...
            if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation2.frameNStart = frameN  # exact frame index
                fixation2.tStart = t  # local t and not account for scr refresh
                fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation2.status = STARTED
                fixation2.setAutoDraw(True)
            
            # if fixation2 is active this frame...
            if fixation2.status == STARTED:
                # update params
                pass
            
            # if fixation2 is stopping this frame...
            if fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation2.tStop = t  # not accounting for scr refresh
                    fixation2.frameNStop = frameN  # exact frame index
                    # update status
                    fixation2.status = FINISHED
                    fixation2.setAutoDraw(False)
            
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
            for thisComponent in noiseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "noise" ---
        for thisComponent in noiseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('noise.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "fixation2_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation2_2.started', globalClock.getTime())
        # keep track of which components have finished
        fixation2_2Components = [fixation_2]
        for thisComponent in fixation2_2Components:
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
        
        # --- Run Routine "fixation2_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_2* updates
            
            # if fixation_2 is starting this frame...
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation_2.status = STARTED
                fixation_2.setAutoDraw(True)
            
            # if fixation_2 is active this frame...
            if fixation_2.status == STARTED:
                # update params
                pass
            
            # if fixation_2 is stopping this frame...
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # update status
                    fixation_2.status = FINISHED
                    fixation_2.setAutoDraw(False)
            
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
            for thisComponent in fixation2_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation2_2" ---
        for thisComponent in fixation2_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation2_2.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "cue_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('cue_2.started', globalClock.getTime())
        tricue.setOri(Target*(-90))
        # keep track of which components have finished
        cue_2Components = [tricue]
        for thisComponent in cue_2Components:
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
        
        # --- Run Routine "cue_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.35:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tricue* updates
            
            # if tricue is starting this frame...
            if tricue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tricue.frameNStart = frameN  # exact frame index
                tricue.tStart = t  # local t and not account for scr refresh
                tricue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tricue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tricue.started')
                # update status
                tricue.status = STARTED
                tricue.setAutoDraw(True)
            
            # if tricue is active this frame...
            if tricue.status == STARTED:
                # update params
                pass
            
            # if tricue is stopping this frame...
            if tricue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tricue.tStartRefresh + 0.35-frameTolerance:
                    # keep track of stop time/frame for later
                    tricue.tStop = t  # not accounting for scr refresh
                    tricue.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tricue.stopped')
                    # update status
                    tricue.status = FINISHED
                    tricue.setAutoDraw(False)
            
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
            for thisComponent in cue_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cue_2" ---
        for thisComponent in cue_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cue_2.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.350000)
        
        # --- Prepare to start Routine "Response_D_new" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Response_D_new.started', globalClock.getTime())
        # Run 'Begin Routine' code from Resp_D_code_2
        win.mouseVisible = False
        Ini_angle = DirectionRes
        FD_middle = DirectionAngle
        
        
        Diff_A = float(DirectionRes - DirectionAngle)
        
        Pointer = 0.7 
        
        x = 0.3 * cos(Ini_angle * math.pi / 180)
        y = 0.3 * sin(Ini_angle *math.pi /180)
        
        angle_temp = 0
        
        kb = keyboard.Keyboard()
        kb.clock.reset()  # now t=0
        time.reset()
        
        RT_Direction = 9999
        keyDuration_D = 9999
        Key_pressed_D = False # need an initial value
        Key_release_D = 0
        
        kb.clearEvents(eventType='keyboard')
        event.clearEvents(eventType='keyboard')
        
        
        BKG_7.setPos([0,0])
        # keep track of which components have finished
        Response_D_newComponents = [BKG_7, Circle, Line_2]
        for thisComponent in Response_D_newComponents:
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
        
        # --- Run Routine "Response_D_new" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from Resp_D_code_2
            keys = kb.getKeys(keyList=['left', 'right'], waitRelease=False, clear=False)
            
            timeEnd = time.getTime()
            
            if (event.getKeys(keyList=['left', 'right'])):
                Key_pressed_D = True
                RT_Direction = time.getTime()
                
            
            # keep in mind the direction in Psychopy is counterclockwise
            # and the 0 in psychopy is the 45.
            for key in keys:
                if key.name == 'left': 
                      angle_temp = angle_temp + Pointer
                elif key.name == 'right':
                      angle_temp = angle_temp - Pointer
                    
                Ini_angle = DirectionRes + angle_temp
            
                x = 0.3 * cos(Ini_angle *math.pi /180)
                y = 0.3 * sin(Ini_angle *math.pi /180)
                    
                if key.duration != None:
                    Key_pressed_D = False
                    Key_release_D = 1
                    
            keyDuration_D = timeEnd - RT_Direction
            textRT = round(keyDuration_D,2)
            
            Final_angle = Ini_angle%360
            
            #if Final_angle > 180:
            #     Final_angle = Final_angle - 180  # Reflect angle back to [0, 180]
            
            if Key_release_D == 1 or (timeEnd>=6):
                continueRoutine = False
                
                
            
            
            
            # *BKG_7* updates
            
            # if BKG_7 is starting this frame...
            if BKG_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BKG_7.frameNStart = frameN  # exact frame index
                BKG_7.tStart = t  # local t and not account for scr refresh
                BKG_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BKG_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                BKG_7.status = STARTED
                BKG_7.setAutoDraw(True)
            
            # if BKG_7 is active this frame...
            if BKG_7.status == STARTED:
                # update params
                pass
            
            # if BKG_7 is stopping this frame...
            if BKG_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BKG_7.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    BKG_7.tStop = t  # not accounting for scr refresh
                    BKG_7.frameNStop = frameN  # exact frame index
                    # update status
                    BKG_7.status = FINISHED
                    BKG_7.setAutoDraw(False)
            
            # *Circle* updates
            
            # if Circle is starting this frame...
            if Circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle.frameNStart = frameN  # exact frame index
                Circle.tStart = t  # local t and not account for scr refresh
                Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
                # update status
                Circle.status = STARTED
                Circle.setAutoDraw(True)
            
            # if Circle is active this frame...
            if Circle.status == STARTED:
                # update params
                Circle.setPos([x, y], log=False)
            
            # if Circle is stopping this frame...
            if Circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle.tStop = t  # not accounting for scr refresh
                    Circle.frameNStop = frameN  # exact frame index
                    # update status
                    Circle.status = FINISHED
                    Circle.setAutoDraw(False)
            
            # *Line_2* updates
            
            # if Line_2 is starting this frame...
            if Line_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Line_2.frameNStart = frameN  # exact frame index
                Line_2.tStart = t  # local t and not account for scr refresh
                Line_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Line_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Line_2.status = STARTED
                Line_2.setAutoDraw(True)
            
            # if Line_2 is active this frame...
            if Line_2.status == STARTED:
                # update params
                Line_2.setPos([(0,0),(x,y)], log=False)
            
            # if Line_2 is stopping this frame...
            if Line_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Line_2.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Line_2.tStop = t  # not accounting for scr refresh
                    Line_2.frameNStop = frameN  # exact frame index
                    # update status
                    Line_2.status = FINISHED
                    Line_2.setAutoDraw(False)
            
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
            for thisComponent in Response_D_newComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Response_D_new" ---
        for thisComponent in Response_D_newComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Response_D_new.stopped', globalClock.getTime())
        # Run 'End Routine' code from Resp_D_code_2
        Key_pressed = False
        if TrialType == 'Direction':
            DirectionResDur = keyDuration_D
            FiDirection = Final_angle
            DirError = abs(Final_angle - DirectionAngle)
            if Key_release_D == 1:
                thisExp.addData('FinalDirection', FiDirection)
                thisExp.addData('DirectionError', DirError)
                thisExp.addData('RT_D', RT_Direction)
                thisExp.addData('DirectionRepDuration', DirectionResDur)
            elif Key_release_D == 0:
                thisExp.addData('FinalDirection', 9999)
                thisExp.addData('DirectionError', 9999)
                thisExp.addData('RT_D', 9999)
                thisExp.addData('DirectionRepDuration', 9999)
        kb.clearEvents(eventType='keyboard')
        event.clearEvents(eventType='keyboard')
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "Feedback_for_Direction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Feedback_for_Direction.started', globalClock.getTime())
        # Run 'Begin Routine' code from initial
        if not DirError > 30:
            continueRoutine = False
        
        # Run 'Begin Routine' code from Feedback_code_3
        PresentDur = 0.5
        
        win.mouseVisible = False
        
        Middle_Pos = float(FD_middle)+random.uniform(-1, 1)
        
        
        x_D_FD_1 = 0.2 * cos((Middle_Pos+40)*math.pi/180)
        y_D_FD_1 = 0.2 * sin((Middle_Pos+40)*math.pi/180)
        x_D_FD_2 = 0.2 * cos((Middle_Pos+20)*math.pi/180)
        y_D_FD_2 = 0.2 * sin((Middle_Pos+20)*math.pi/180)
        x_D_FD_3 = 0.2 * cos(Middle_Pos*math.pi/180)
        y_D_FD_3 = 0.2 * sin(Middle_Pos*math.pi/180)
        x_D_FD_4 = 0.2 * cos((Middle_Pos-20)*math.pi/180)
        y_D_FD_4 = 0.2 * sin((Middle_Pos-20)*math.pi/180)
        x_D_FD_5 = 0.2 * cos((Middle_Pos-40)*math.pi/180)
        y_D_FD_5 = 0.2 * sin((Middle_Pos-40)*math.pi/180)
        
        # keep in mind the direction in Psychopy is counterclockwise
        # and the 0 in psychopy is the 45.
        if TrialType == 'Direction':
            if Key_release_D == 1:
                if abs(float(Final_angle) - float(DirectionAngle))<= 3:
                   color_3 = [0,0.9,0.3]; 
                   thisExp.addData('FeedbackID_D', 3)
                   
                elif (float(Final_angle) - float(DirectionAngle))>10:
                    color_1 = [1,0,0];
                    thisExp.addData('FeedbackID_D', 1)
        
                elif (float(DirectionAngle)-float(Final_angle))>10:
                    color_5 = [1,0,0];
                    thisExp.addData('FeedbackID_D', 5)
        
                elif ((float(DirectionAngle)-float(Final_angle))>3) and ((float(DirectionAngle)-float(Final_angle))<=10) :
                    color_4 = [1,0.3,0.4];
                    thisExp.addData('FeedbackID_D', 4)
        
                elif ((float(Final_angle)-float(DirectionAngle))>3) and ((float(Final_angle)-float(DirectionAngle))<=10) :
                    color_2 = [1,0.3,0.4];
                    thisExp.addData('FeedbackID_D', 2)
            else:
                thisExp.addData('FeedbackID_D', 0)
        
        feedback_1_D.setFillColor(color_1)
        feedback_1_D.setPos([x_D_FD_1, y_D_FD_1])
        feedback_1_D.setLineColor(color_1)
        feedback_2_D.setFillColor(color_2)
        feedback_2_D.setPos([x_D_FD_2, y_D_FD_2])
        feedback_2_D.setLineColor(color_2)
        feedback_3_D.setFillColor(color_3)
        feedback_3_D.setPos([x_D_FD_3, y_D_FD_3])
        feedback_3_D.setLineColor(color_3)
        feedback_4_D.setFillColor(color_4)
        feedback_4_D.setPos([x_D_FD_4, y_D_FD_4])
        feedback_4_D.setLineColor(color_4)
        feedback_5_D.setFillColor(color_5)
        feedback_5_D.setPos([x_D_FD_5, y_D_FD_5])
        feedback_5_D.setLineColor(color_5)
        # keep track of which components have finished
        Feedback_for_DirectionComponents = [feedback_1_D, feedback_2_D, feedback_3_D, feedback_4_D, feedback_5_D]
        for thisComponent in Feedback_for_DirectionComponents:
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
        
        # --- Run Routine "Feedback_for_Direction" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_1_D* updates
            
            # if feedback_1_D is starting this frame...
            if feedback_1_D.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                feedback_1_D.frameNStart = frameN  # exact frame index
                feedback_1_D.tStart = t  # local t and not account for scr refresh
                feedback_1_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_1_D, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_1_D.status = STARTED
                feedback_1_D.setAutoDraw(True)
            
            # if feedback_1_D is active this frame...
            if feedback_1_D.status == STARTED:
                # update params
                pass
            
            # if feedback_1_D is stopping this frame...
            if feedback_1_D.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_1_D.tStartRefresh + PresentDur-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_1_D.tStop = t  # not accounting for scr refresh
                    feedback_1_D.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_1_D.status = FINISHED
                    feedback_1_D.setAutoDraw(False)
            
            # *feedback_2_D* updates
            
            # if feedback_2_D is starting this frame...
            if feedback_2_D.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                feedback_2_D.frameNStart = frameN  # exact frame index
                feedback_2_D.tStart = t  # local t and not account for scr refresh
                feedback_2_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_2_D, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_2_D.status = STARTED
                feedback_2_D.setAutoDraw(True)
            
            # if feedback_2_D is active this frame...
            if feedback_2_D.status == STARTED:
                # update params
                pass
            
            # if feedback_2_D is stopping this frame...
            if feedback_2_D.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_2_D.tStartRefresh + PresentDur-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_2_D.tStop = t  # not accounting for scr refresh
                    feedback_2_D.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_2_D.status = FINISHED
                    feedback_2_D.setAutoDraw(False)
            
            # *feedback_3_D* updates
            
            # if feedback_3_D is starting this frame...
            if feedback_3_D.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                feedback_3_D.frameNStart = frameN  # exact frame index
                feedback_3_D.tStart = t  # local t and not account for scr refresh
                feedback_3_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_3_D, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_3_D.status = STARTED
                feedback_3_D.setAutoDraw(True)
            
            # if feedback_3_D is active this frame...
            if feedback_3_D.status == STARTED:
                # update params
                pass
            
            # if feedback_3_D is stopping this frame...
            if feedback_3_D.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_3_D.tStartRefresh + PresentDur-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_3_D.tStop = t  # not accounting for scr refresh
                    feedback_3_D.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_3_D.status = FINISHED
                    feedback_3_D.setAutoDraw(False)
            
            # *feedback_4_D* updates
            
            # if feedback_4_D is starting this frame...
            if feedback_4_D.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                feedback_4_D.frameNStart = frameN  # exact frame index
                feedback_4_D.tStart = t  # local t and not account for scr refresh
                feedback_4_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_4_D, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_4_D.status = STARTED
                feedback_4_D.setAutoDraw(True)
            
            # if feedback_4_D is active this frame...
            if feedback_4_D.status == STARTED:
                # update params
                pass
            
            # if feedback_4_D is stopping this frame...
            if feedback_4_D.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_4_D.tStartRefresh + PresentDur-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_4_D.tStop = t  # not accounting for scr refresh
                    feedback_4_D.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_4_D.status = FINISHED
                    feedback_4_D.setAutoDraw(False)
            
            # *feedback_5_D* updates
            
            # if feedback_5_D is starting this frame...
            if feedback_5_D.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                feedback_5_D.frameNStart = frameN  # exact frame index
                feedback_5_D.tStart = t  # local t and not account for scr refresh
                feedback_5_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_5_D, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_5_D.status = STARTED
                feedback_5_D.setAutoDraw(True)
            
            # if feedback_5_D is active this frame...
            if feedback_5_D.status == STARTED:
                # update params
                pass
            
            # if feedback_5_D is stopping this frame...
            if feedback_5_D.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_5_D.tStartRefresh + PresentDur-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_5_D.tStop = t  # not accounting for scr refresh
                    feedback_5_D.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_5_D.status = FINISHED
                    feedback_5_D.setAutoDraw(False)
            
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
            for thisComponent in Feedback_for_DirectionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback_for_Direction" ---
        for thisComponent in Feedback_for_DirectionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Feedback_for_Direction.stopped', globalClock.getTime())
        # Run 'End Routine' code from Feedback_code_3
        keyDuration_D = 10
        Key_pressed_D = False # need an initial value
        Key_release_D == 0
        
        color_1 = [1,1,1];
        color_2 = [1,1,1];
        color_3 = [1,1,1];
        color_4 = [1,1,1];
        color_5 = [1,1,1];
        kb.clock.reset()  # now t=0
        
        kb.clearEvents(eventType='keyboard')
        event.clearEvents(eventType='keyboard')
        # the Routine "Feedback_for_Direction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Bye" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Bye.started', globalClock.getTime())
    Bye_resp.keys = []
    Bye_resp.rt = []
    _Bye_resp_allKeys = []
    # keep track of which components have finished
    ByeComponents = [Bye_text, Bye_resp]
    for thisComponent in ByeComponents:
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
    
    # --- Run Routine "Bye" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bye_text* updates
        
        # if Bye_text is starting this frame...
        if Bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bye_text.frameNStart = frameN  # exact frame index
            Bye_text.tStart = t  # local t and not account for scr refresh
            Bye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bye_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Bye_text.status = STARTED
            Bye_text.setAutoDraw(True)
        
        # if Bye_text is active this frame...
        if Bye_text.status == STARTED:
            # update params
            pass
        
        # if Bye_text is stopping this frame...
        if Bye_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bye_text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Bye_text.tStop = t  # not accounting for scr refresh
                Bye_text.frameNStop = frameN  # exact frame index
                # update status
                Bye_text.status = FINISHED
                Bye_text.setAutoDraw(False)
        
        # *Bye_resp* updates
        waitOnFlip = False
        
        # if Bye_resp is starting this frame...
        if Bye_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bye_resp.frameNStart = frameN  # exact frame index
            Bye_resp.tStart = t  # local t and not account for scr refresh
            Bye_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bye_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Bye_resp.started')
            # update status
            Bye_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Bye_resp.clock.reset)  # t=0 on next screen flip
        
        # if Bye_resp is stopping this frame...
        if Bye_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bye_resp.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Bye_resp.tStop = t  # not accounting for scr refresh
                Bye_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Bye_resp.stopped')
                # update status
                Bye_resp.status = FINISHED
                Bye_resp.status = FINISHED
        if Bye_resp.status == STARTED and not waitOnFlip:
            theseKeys = Bye_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _Bye_resp_allKeys.extend(theseKeys)
            if len(_Bye_resp_allKeys):
                Bye_resp.keys = _Bye_resp_allKeys[-1].name  # just the last key pressed
                Bye_resp.rt = _Bye_resp_allKeys[-1].rt
                Bye_resp.duration = _Bye_resp_allKeys[-1].duration
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
        for thisComponent in ByeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Bye" ---
    for thisComponent in ByeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Bye.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
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
