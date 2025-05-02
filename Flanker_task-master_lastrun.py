#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on เมษายน 18, 2025, at 03:48
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
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
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Flanker_task-master'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
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
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
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
        originPath='C:\\Users\\Dell\\Downloads\\Flanker_task-master\\Flanker_task-master_lastrun.py',
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
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
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
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
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
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
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
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
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
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
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
    
    # --- Initialize components for Routine "Instructions" ---
    text_Instructions = visual.TextStim(win=win, name='text_Instructions',
        text='\nในเกมนี้จะมี ลูกศร โผล่มาให้ดูบนหน้าจอ\n\nโดยที่ ให้ดูลูกศรตรง “กลาง” ว่าชี้ไปทางไหน\nแล้วให้กดปุ่มตาม เช่น\n\nถ้าลูกศรตรงกลางชี้ ขวา  กดปุ่ม ขวา\nถ้าลูกศรตรงกลางชี้ ซ้าย  กดปุ่ม ซ้าย\n\nแตะหน้าจอเพื่อไปฝึกเล่น',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse_Instructions = event.Mouse(win=win)
    x, y = [None, None]
    mouse_Instructions.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "countdown" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Fixation" ---
    text_Fixation = visual.TextStim(win=win, name='text_Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Tutorial" ---
    Image_t = visual.ImageStim(
        win=win,
        name='Image_t', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.5, 1.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    R_t = visual.ImageStim(
        win=win,
        name='R_t', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.15, -0.2), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    L_t = visual.ImageStim(
        win=win,
        name='L_t', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.15, -0.2), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_resp_t = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp_t.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Feedback" ---
    text_feedback_Tutorial = visual.TextStim(win=win, name='text_feedback_Tutorial',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Instructions_2" ---
    text_Instructions_2 = visual.TextStim(win=win, name='text_Instructions_2',
        text='\nเมื่อเล่นจริงจะไม่มีการบอกว่าถูกหรือผิด\n\nแตะหน้าจอเพื่อไปเล่นจริง',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse_Instructions_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_Instructions_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "countdown" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Fixation" ---
    text_Fixation = visual.TextStim(win=win, name='text_Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "FlankerTask" ---
    Image = visual.ImageStim(
        win=win,
        name='Image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.5, 1.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    R = visual.ImageStim(
        win=win,
        name='R', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.15, -0.2), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    L = visual.ImageStim(
        win=win,
        name='L', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.15, -0.2), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "End" ---
    text_end = visual.TextStim(win=win, name='text_end',
        text='ขอบคุณสำหรับการเข้าร่วม',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[text_Instructions, mouse_Instructions],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_Instructions
    gotValidClick = False  # until a click is received
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
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
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Instructions* updates
        
        # if text_Instructions is starting this frame...
        if text_Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Instructions.frameNStart = frameN  # exact frame index
            text_Instructions.tStart = t  # local t and not account for scr refresh
            text_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Instructions.status = STARTED
            text_Instructions.setAutoDraw(True)
        
        # if text_Instructions is active this frame...
        if text_Instructions.status == STARTED:
            # update params
            pass
        # *mouse_Instructions* updates
        
        # if mouse_Instructions is starting this frame...
        if mouse_Instructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_Instructions.frameNStart = frameN  # exact frame index
            mouse_Instructions.tStart = t  # local t and not account for scr refresh
            mouse_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_Instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_Instructions.status = STARTED
            mouse_Instructions.mouseClock.reset()
            prevButtonState = mouse_Instructions.getPressed()  # if button is down already this ISN'T a new click
        if mouse_Instructions.status == STARTED:  # only update if started and not finished!
            buttons = mouse_Instructions.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[text_3, text_2, text_1],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
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
    
    # --- Run Routine "countdown" ---
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_1* updates
        
        # if text_1 is starting this frame...
        if text_1.status == NOT_STARTED and t >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_1.status = STARTED
            text_1.setAutoDraw(True)
        
        # if text_1 is active this frame...
        if text_1.status == STARTED:
            # update params
            pass
        
        # if text_1 is stopping this frame...
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.tStopRefresh = tThisFlipGlobal  # on global time
                text_1.frameNStop = frameN  # exact frame index
                # update status
                text_1.status = FINISHED
                text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            countdown.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if countdown.maxDurationReached:
        routineTimer.addTime(-countdown.maxDuration)
    elif countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    Play_t = data.TrialHandler2(
        name='Play_t',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions_arrows.csv'), 
        seed=None, 
    )
    thisExp.addLoop(Play_t)  # add the loop to the experiment
    thisPlay_t = Play_t.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPlay_t.rgb)
    if thisPlay_t != None:
        for paramName in thisPlay_t:
            globals()[paramName] = thisPlay_t[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPlay_t in Play_t:
        currentLoop = Play_t
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPlay_t.rgb)
        if thisPlay_t != None:
            for paramName in thisPlay_t:
                globals()[paramName] = thisPlay_t[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[text_Fixation],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
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
        
        # --- Run Routine "Fixation" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Fixation* updates
            
            # if text_Fixation is starting this frame...
            if text_Fixation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Fixation.frameNStart = frameN  # exact frame index
                text_Fixation.tStart = t  # local t and not account for scr refresh
                text_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_Fixation.status = STARTED
                text_Fixation.setAutoDraw(True)
            
            # if text_Fixation is active this frame...
            if text_Fixation.status == STARTED:
                # update params
                pass
            
            # if text_Fixation is stopping this frame...
            if text_Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Fixation.tStop = t  # not accounting for scr refresh
                    text_Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_Fixation.frameNStop = frameN  # exact frame index
                    # update status
                    text_Fixation.status = FINISHED
                    text_Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Tutorial" ---
        # create an object to store info about Routine Tutorial
        Tutorial = data.Routine(
            name='Tutorial',
            components=[Image_t, R_t, L_t, mouse_resp_t],
        )
        Tutorial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_t
        if(condition == 'go'):
            space_key = 'space'
        else:
            space_key = 'None'
        
        # ใน Begin Routine
        import random
        
        # สุ่มเวลาในช่วง 1 ถึง 3 วินาที (1000 ถึง 3000ms)
        min_time = 1.0  # นาทีต่ำสุด (วินาที)
        max_time = 3.0  # นาทีสูงสุด (วินาที)
        
        # สุ่มระยะเวลา
        random_time = random.uniform(min_time, max_time)
        
        # กำหนดเวลาที่สุ่มได้ให้เป็นตัวแปร
        thisExp.addData('random_time', random_time)
        
        # กำหนดให้ตัวแปรนี้จะใช้เป็นเวลาหยุดแสดงภาพ
        continueRoutine = True
        
        Image_t.setImage(photo)
        R_t.setImage('Images/R.png')
        L_t.setImage('Images/L.png')
        # setup some python lists for storing info about the mouse_resp_t
        mouse_resp_t.x = []
        mouse_resp_t.y = []
        mouse_resp_t.leftButton = []
        mouse_resp_t.midButton = []
        mouse_resp_t.rightButton = []
        mouse_resp_t.time = []
        mouse_resp_t.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for Tutorial
        Tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Tutorial.tStart = globalClock.getTime(format='float')
        Tutorial.status = STARTED
        thisExp.addData('Tutorial.started', Tutorial.tStart)
        Tutorial.maxDuration = None
        # keep track of which components have finished
        TutorialComponents = Tutorial.components
        for thisComponent in Tutorial.components:
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
        
        # --- Run Routine "Tutorial" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Tutorial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image_t* updates
            
            # if Image_t is starting this frame...
            if Image_t.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image_t.frameNStart = frameN  # exact frame index
                Image_t.tStart = t  # local t and not account for scr refresh
                Image_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image_t, 'tStartRefresh')  # time at next scr refresh
                # update status
                Image_t.status = STARTED
                Image_t.setAutoDraw(True)
            
            # if Image_t is active this frame...
            if Image_t.status == STARTED:
                # update params
                pass
            
            # if Image_t is stopping this frame...
            if Image_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image_t.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    Image_t.tStop = t  # not accounting for scr refresh
                    Image_t.tStopRefresh = tThisFlipGlobal  # on global time
                    Image_t.frameNStop = frameN  # exact frame index
                    # update status
                    Image_t.status = FINISHED
                    Image_t.setAutoDraw(False)
            
            # *R_t* updates
            
            # if R_t is starting this frame...
            if R_t.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_t.frameNStart = frameN  # exact frame index
                R_t.tStart = t  # local t and not account for scr refresh
                R_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_t, 'tStartRefresh')  # time at next scr refresh
                # update status
                R_t.status = STARTED
                R_t.setAutoDraw(True)
            
            # if R_t is active this frame...
            if R_t.status == STARTED:
                # update params
                pass
            
            # *L_t* updates
            
            # if L_t is starting this frame...
            if L_t.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_t.frameNStart = frameN  # exact frame index
                L_t.tStart = t  # local t and not account for scr refresh
                L_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_t, 'tStartRefresh')  # time at next scr refresh
                # update status
                L_t.status = STARTED
                L_t.setAutoDraw(True)
            
            # if L_t is active this frame...
            if L_t.status == STARTED:
                # update params
                pass
            # *mouse_resp_t* updates
            
            # if mouse_resp_t is starting this frame...
            if mouse_resp_t.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp_t.frameNStart = frameN  # exact frame index
                mouse_resp_t.tStart = t  # local t and not account for scr refresh
                mouse_resp_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp_t, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_resp_t.started', t)
                # update status
                mouse_resp_t.status = STARTED
                mouse_resp_t.mouseClock.reset()
                prevButtonState = mouse_resp_t.getPressed()  # if button is down already this ISN'T a new click
            if mouse_resp_t.status == STARTED:  # only update if started and not finished!
                buttons = mouse_resp_t.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([L_t,R_t], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_resp_t):
                                gotValidClick = True
                                mouse_resp_t.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_resp_t.clicked_name.append(None)
                        x, y = mouse_resp_t.getPos()
                        mouse_resp_t.x.append(x)
                        mouse_resp_t.y.append(y)
                        buttons = mouse_resp_t.getPressed()
                        mouse_resp_t.leftButton.append(buttons[0])
                        mouse_resp_t.midButton.append(buttons[1])
                        mouse_resp_t.rightButton.append(buttons[2])
                        mouse_resp_t.time.append(mouse_resp_t.mouseClock.getTime())
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Tutorial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Tutorial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Tutorial" ---
        for thisComponent in Tutorial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Tutorial
        Tutorial.tStop = globalClock.getTime(format='float')
        Tutorial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Tutorial.stopped', Tutorial.tStop)
        # store data for Play_t (TrialHandler)
        Play_t.addData('mouse_resp_t.x', mouse_resp_t.x)
        Play_t.addData('mouse_resp_t.y', mouse_resp_t.y)
        Play_t.addData('mouse_resp_t.leftButton', mouse_resp_t.leftButton)
        Play_t.addData('mouse_resp_t.midButton', mouse_resp_t.midButton)
        Play_t.addData('mouse_resp_t.rightButton', mouse_resp_t.rightButton)
        Play_t.addData('mouse_resp_t.time', mouse_resp_t.time)
        Play_t.addData('mouse_resp_t.clicked_name', mouse_resp_t.clicked_name)
        # the Routine "Tutorial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        # create an object to store info about Routine Feedback
        Feedback = data.Routine(
            name='Feedback',
            components=[text_feedback_Tutorial],
        )
        Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_Feedback_Tutorial
        
        
        if(key_resp.corr == 1):
            feedback_text = "Correct"
        elif(key_resp.corr == 0):
            feedback_text = "Incorrect"
        
        #if(condition == 'go'):
        #    if(Play.key_resp.corr == 'space'):
        #        feedback_text = "Correct"
        #    else:
        #        feedback_text = "Incorrect"
        #if(condition == 'nogo'):
        #    if(Play.key_resp.corr == 'None'):
        #        feedback_text = "Correct"
        #    else:
        #        feedback_text = "Incorrect"
        
        text_feedback_Tutorial.setText(feedback_text)
        # store start times for Feedback
        Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback.tStart = globalClock.getTime(format='float')
        Feedback.status = STARTED
        Feedback.maxDuration = None
        # keep track of which components have finished
        FeedbackComponents = Feedback.components
        for thisComponent in Feedback.components:
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
        
        # --- Run Routine "Feedback" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_feedback_Tutorial* updates
            
            # if text_feedback_Tutorial is starting this frame...
            if text_feedback_Tutorial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_Tutorial.frameNStart = frameN  # exact frame index
                text_feedback_Tutorial.tStart = t  # local t and not account for scr refresh
                text_feedback_Tutorial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_Tutorial, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_feedback_Tutorial.status = STARTED
                text_feedback_Tutorial.setAutoDraw(True)
            
            # if text_feedback_Tutorial is active this frame...
            if text_feedback_Tutorial.status == STARTED:
                # update params
                pass
            
            # if text_feedback_Tutorial is stopping this frame...
            if text_feedback_Tutorial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_feedback_Tutorial.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_feedback_Tutorial.tStop = t  # not accounting for scr refresh
                    text_feedback_Tutorial.tStopRefresh = tThisFlipGlobal  # on global time
                    text_feedback_Tutorial.frameNStop = frameN  # exact frame index
                    # update status
                    text_feedback_Tutorial.status = FINISHED
                    text_feedback_Tutorial.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback
        Feedback.tStop = globalClock.getTime(format='float')
        Feedback.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback.maxDurationReached:
            routineTimer.addTime(-Feedback.maxDuration)
        elif Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Play_t'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Instructions_2" ---
    # create an object to store info about Routine Instructions_2
    Instructions_2 = data.Routine(
        name='Instructions_2',
        components=[text_Instructions_2, mouse_Instructions_2],
    )
    Instructions_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_Instructions_2
    gotValidClick = False  # until a click is received
    # store start times for Instructions_2
    Instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_2.tStart = globalClock.getTime(format='float')
    Instructions_2.status = STARTED
    thisExp.addData('Instructions_2.started', Instructions_2.tStart)
    Instructions_2.maxDuration = None
    # keep track of which components have finished
    Instructions_2Components = Instructions_2.components
    for thisComponent in Instructions_2.components:
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
    
    # --- Run Routine "Instructions_2" ---
    Instructions_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Instructions_2* updates
        
        # if text_Instructions_2 is starting this frame...
        if text_Instructions_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Instructions_2.frameNStart = frameN  # exact frame index
            text_Instructions_2.tStart = t  # local t and not account for scr refresh
            text_Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instructions_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Instructions_2.status = STARTED
            text_Instructions_2.setAutoDraw(True)
        
        # if text_Instructions_2 is active this frame...
        if text_Instructions_2.status == STARTED:
            # update params
            pass
        # *mouse_Instructions_2* updates
        
        # if mouse_Instructions_2 is starting this frame...
        if mouse_Instructions_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_Instructions_2.frameNStart = frameN  # exact frame index
            mouse_Instructions_2.tStart = t  # local t and not account for scr refresh
            mouse_Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_Instructions_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_Instructions_2.status = STARTED
            mouse_Instructions_2.mouseClock.reset()
            prevButtonState = mouse_Instructions_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_Instructions_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_Instructions_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_2" ---
    for thisComponent in Instructions_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_2
    Instructions_2.tStop = globalClock.getTime(format='float')
    Instructions_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_2.stopped', Instructions_2.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[text_3, text_2, text_1],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
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
    
    # --- Run Routine "countdown" ---
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_1* updates
        
        # if text_1 is starting this frame...
        if text_1.status == NOT_STARTED and t >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_1.status = STARTED
            text_1.setAutoDraw(True)
        
        # if text_1 is active this frame...
        if text_1.status == STARTED:
            # update params
            pass
        
        # if text_1 is stopping this frame...
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.tStopRefresh = tThisFlipGlobal  # on global time
                text_1.frameNStop = frameN  # exact frame index
                # update status
                text_1.status = FINISHED
                text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            countdown.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if countdown.maxDurationReached:
        routineTimer.addTime(-countdown.maxDuration)
    elif countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    Play = data.TrialHandler2(
        name='Play',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions_arrows.csv'), 
        seed=None, 
    )
    thisExp.addLoop(Play)  # add the loop to the experiment
    thisPlay = Play.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPlay.rgb)
    if thisPlay != None:
        for paramName in thisPlay:
            globals()[paramName] = thisPlay[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPlay in Play:
        currentLoop = Play
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPlay.rgb)
        if thisPlay != None:
            for paramName in thisPlay:
                globals()[paramName] = thisPlay[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[text_Fixation],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
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
        
        # --- Run Routine "Fixation" ---
        # if trial has changed, end Routine now
        if isinstance(Play, data.TrialHandler2) and thisPlay.thisN != Play.thisTrial.thisN:
            continueRoutine = False
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Fixation* updates
            
            # if text_Fixation is starting this frame...
            if text_Fixation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Fixation.frameNStart = frameN  # exact frame index
                text_Fixation.tStart = t  # local t and not account for scr refresh
                text_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_Fixation.status = STARTED
                text_Fixation.setAutoDraw(True)
            
            # if text_Fixation is active this frame...
            if text_Fixation.status == STARTED:
                # update params
                pass
            
            # if text_Fixation is stopping this frame...
            if text_Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Fixation.tStop = t  # not accounting for scr refresh
                    text_Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_Fixation.frameNStop = frameN  # exact frame index
                    # update status
                    text_Fixation.status = FINISHED
                    text_Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "FlankerTask" ---
        # create an object to store info about Routine FlankerTask
        FlankerTask = data.Routine(
            name='FlankerTask',
            components=[Image, R, L, mouse_resp],
        )
        FlankerTask.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if(condition == 'go'):
            space_key = 'space'
        else:
            space_key = 'None'
        
        #condition = go -> space_key = 'space'
        #condition = nogo -> space_key = 'None'
        Image.setImage(photo)
        R.setImage('Images/R.png')
        L.setImage('Images/L.png')
        # setup some python lists for storing info about the mouse_resp
        mouse_resp.x = []
        mouse_resp.y = []
        mouse_resp.leftButton = []
        mouse_resp.midButton = []
        mouse_resp.rightButton = []
        mouse_resp.time = []
        mouse_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for FlankerTask
        FlankerTask.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        FlankerTask.tStart = globalClock.getTime(format='float')
        FlankerTask.status = STARTED
        thisExp.addData('FlankerTask.started', FlankerTask.tStart)
        FlankerTask.maxDuration = None
        # keep track of which components have finished
        FlankerTaskComponents = FlankerTask.components
        for thisComponent in FlankerTask.components:
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
        
        # --- Run Routine "FlankerTask" ---
        # if trial has changed, end Routine now
        if isinstance(Play, data.TrialHandler2) and thisPlay.thisN != Play.thisTrial.thisN:
            continueRoutine = False
        FlankerTask.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image* updates
            
            # if Image is starting this frame...
            if Image.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                # update status
                Image.status = STARTED
                Image.setAutoDraw(True)
            
            # if Image is active this frame...
            if Image.status == STARTED:
                # update params
                pass
            
            # if Image is stopping this frame...
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.tStopRefresh = tThisFlipGlobal  # on global time
                    Image.frameNStop = frameN  # exact frame index
                    # update status
                    Image.status = FINISHED
                    Image.setAutoDraw(False)
            
            # *R* updates
            
            # if R is starting this frame...
            if R.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R.frameNStart = frameN  # exact frame index
                R.tStart = t  # local t and not account for scr refresh
                R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
                # update status
                R.status = STARTED
                R.setAutoDraw(True)
            
            # if R is active this frame...
            if R.status == STARTED:
                # update params
                pass
            
            # *L* updates
            
            # if L is starting this frame...
            if L.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L.frameNStart = frameN  # exact frame index
                L.tStart = t  # local t and not account for scr refresh
                L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
                # update status
                L.status = STARTED
                L.setAutoDraw(True)
            
            # if L is active this frame...
            if L.status == STARTED:
                # update params
                pass
            # *mouse_resp* updates
            
            # if mouse_resp is starting this frame...
            if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp.frameNStart = frameN  # exact frame index
                mouse_resp.tStart = t  # local t and not account for scr refresh
                mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_resp.started', t)
                # update status
                mouse_resp.status = STARTED
                mouse_resp.mouseClock.reset()
                prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
            if mouse_resp.status == STARTED:  # only update if started and not finished!
                buttons = mouse_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([R,L], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_resp):
                                gotValidClick = True
                                mouse_resp.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_resp.clicked_name.append(None)
                        x, y = mouse_resp.getPos()
                        mouse_resp.x.append(x)
                        mouse_resp.y.append(y)
                        buttons = mouse_resp.getPressed()
                        mouse_resp.leftButton.append(buttons[0])
                        mouse_resp.midButton.append(buttons[1])
                        mouse_resp.rightButton.append(buttons[2])
                        mouse_resp.time.append(mouse_resp.mouseClock.getTime())
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                FlankerTask.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FlankerTask.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FlankerTask" ---
        for thisComponent in FlankerTask.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for FlankerTask
        FlankerTask.tStop = globalClock.getTime(format='float')
        FlankerTask.tStopRefresh = tThisFlipGlobal
        thisExp.addData('FlankerTask.stopped', FlankerTask.tStop)
        # store data for Play (TrialHandler)
        Play.addData('mouse_resp.x', mouse_resp.x)
        Play.addData('mouse_resp.y', mouse_resp.y)
        Play.addData('mouse_resp.leftButton', mouse_resp.leftButton)
        Play.addData('mouse_resp.midButton', mouse_resp.midButton)
        Play.addData('mouse_resp.rightButton', mouse_resp.rightButton)
        Play.addData('mouse_resp.time', mouse_resp.time)
        Play.addData('mouse_resp.clicked_name', mouse_resp.clicked_name)
        # the Routine "FlankerTask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'Play'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[text_end],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
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
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end* updates
        
        # if text_end is starting this frame...
        if text_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end.frameNStart = frameN  # exact frame index
            text_end.tStart = t  # local t and not account for scr refresh
            text_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_end.status = STARTED
            text_end.setAutoDraw(True)
        
        # if text_end is active this frame...
        if text_end.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


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


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
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
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
