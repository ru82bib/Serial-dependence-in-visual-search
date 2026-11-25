"""Shared desktop PsychoPy implementation for dimension_weighting.psyexp.

Pure scheduling/angle helpers can be imported without installing PsychoPy.
Angles are axial: 0 = vertical, 90 = horizontal, clockwise positive.
"""
import json
import math
import random
import re
import secrets
from pathlib import Path

TRIALS_PER_BLOCK = 600
N_ITEMS = 12
EXPERIMENT_REVISION = '2026-11-25-fixed-outlines-matched-strokes'
FIXATION_MIN_SECONDS = 0.5
FIXATION_MAX_SECONDS = 0.8
SEARCH_SECONDS = 0.8
BLANK_SECONDS = 0.2
# Preserve the old eight-item array's adjacent center-to-center distance,
# while retaining the old individual item dimensions in a twelve-item array.
RADIUS_DEG = 4.0 * math.sin(math.pi / 8.0) / math.sin(math.pi / N_ITEMS)
OUTLINE_SIZE_DEG = 2.0
STROKE_WIDTH_PX = 8.0
BAR_LENGTH_DEG = 0.9
DIAMOND_VERTICES_DEG = ((0.0, math.sqrt(2.0)), (math.sqrt(2.0), 0.0),
                        (0.0, -math.sqrt(2.0)), (-math.sqrt(2.0), 0.0))
# Same 2-by-2-degree triangle, translated so its inscribed-circle center is
# the shared item/bar center. This leaves clearance for every bar orientation.
TRIANGLE_INRADIUS_DEG = 2.0 / (1.0 + math.sqrt(5.0))
TRIANGLE_VERTICES_DEG = ((0.0, 2.0 - TRIANGLE_INRADIUS_DEG),
                         (-1.0, -TRIANGLE_INRADIUS_DEG),
                         (1.0, -TRIANGLE_INRADIUS_DEG))
BACKGROUND_RGB = (0.0, 0.0, 0.0)
GRAY_RGB = (0.5, 0.5, 0.5)
RED_RGB = (1.0, -1.0, -1.0)
BAR_RGB = (1.0, 1.0, 1.0)
BREAK_TEXT = (
    'feel free to take a break at this point. '
    'continue by pressing space bar'
)
INSTRUCTIONS = (
    'Find the light-gray diamond on every trial.\n'
    'Remember the orientation of the bar inside the diamond.\n\n'
    'When a single bar appears in the center, move the mouse to rotate it '
    'until it matches the remembered orientation.\n'
    'Confirm your answer with the left mouse button.\n\n'
    'Respond as accurately as possible.\n'
    'You can take a break after every 100 trials.\n\n'
    'Press the space bar to begin.'
)


def wrap180(angle):
    """Map an axial difference to [-90, 90)."""
    return (angle + 90.0) % 180.0 - 90.0


def cursor_angle(x, y, previous):
    """Convert cursor vector into the orientation of a vertical bar."""
    if math.hypot(x, y) < 1e-8:
        return previous
    return math.degrees(math.atan2(x, y)) % 180.0


def cursor_position(angle, radius=1.5):
    radians = math.radians(angle)
    return (radius * math.sin(radians), radius * math.cos(radians))


def fixation_frame_count(requested_seconds, frame_period):
    """Round to the nearest refresh while staying within the fixation range."""
    minimum = math.ceil(FIXATION_MIN_SECONDS / frame_period - 1e-9)
    maximum = math.floor(FIXATION_MAX_SECONDS / frame_period + 1e-9)
    if minimum < 1 or maximum < minimum:
        raise ValueError('Display refresh period cannot represent a 500–800 ms fixation.')
    return max(minimum, min(maximum, int(round(requested_seconds / frame_period))))


def trial_data_cell(value):
    """Use PsychoPy's conventional list notation in its wide-text CSV.

    Its writer wraps comma-containing values but does not escape internal JSON
    quotes. Python list notation uses single-quoted carrier names and keeps
    exported columns aligned; the separate trial plan remains proper JSON.
    """
    return repr(value) if isinstance(value, (list, tuple, dict)) else value


def participant_number(value):
    value = str(value).strip()
    if not re.fullmatch(r'[0-9]+', value):
        raise ValueError('Participant must be a nonnegative integer for odd/even counterbalancing.')
    return int(value)


def build_schedule(participant, seed):
    """Exactly 300 present / 300 absent per context, shuffled independently.

    All locations are sampled with the same independent uniform procedure in
    both contexts; the target and distractor never share a location.
    """
    number = participant_number(participant)
    order = ('SD', 'DD') if number % 2 else ('DD', 'SD')
    master = random.Random(seed)
    # A separate timing stream keeps fixation independent of stimulus draws
    # and leaves existing stimulus sequences reproducible for the same seed.
    fixation_rng = random.Random(str(seed) + ':fixation-jitter-v1')
    trials = []
    for block_index, context in enumerate(order):
        block_seed = master.getrandbits(64)
        rng = random.Random(block_seed)
        present_flags = [True] * 300 + [False] * 300
        rng.shuffle(present_flags)
        for trial_index, present in enumerate(present_flags):
            locations = list(range(N_ITEMS))
            rng.shuffle(locations)
            target_index = locations[0]
            distractor_index = locations[1] if present else None
            orientations = [rng.uniform(0.0, 180.0) for _ in range(N_ITEMS)]
            shapes = ['circle'] * N_ITEMS
            colors = [list(GRAY_RGB) for _ in range(N_ITEMS)]
            shapes[target_index] = 'diamond'
            if present:
                if context == 'SD':
                    shapes[distractor_index] = 'triangle'
                else:
                    colors[distractor_index] = list(RED_RGB)
            positions = [
                [RADIUS_DEG * math.cos(2 * math.pi * i / N_ITEMS),
                 RADIUS_DEG * math.sin(2 * math.pi * i / N_ITEMS)]
                for i in range(N_ITEMS)
            ]
            trials.append({
                'trial_number': len(trials) + 1,
                'experiment_revision': EXPERIMENT_REVISION,
                'block': block_index + 1,
                'trial_in_block': trial_index + 1,
                'block_context': context,
                'distractor_present': present,
                'condition': context if present else 'absent',
                'seed': seed,
                'block_seed': block_seed,
                'block_order': '-'.join(order),
                'target_index': target_index,
                'distractor_index': distractor_index,
                'target_orientation': orientations[target_index],
                'distractor_orientation': orientations[distractor_index] if present else None,
                'initial_response_angle': rng.uniform(0.0, 180.0),
                'fixation_requested_seconds': fixation_rng.uniform(FIXATION_MIN_SECONDS, FIXATION_MAX_SECONDS),
                'array_radius_deg': RADIUS_DEG,
                'item_positions_deg': positions,
                'item_orientations': orientations,
                'item_shapes': shapes,
                'item_outline_rgb': colors,
                'item_outline_orientations': [0.0] * N_ITEMS,
            })
    return trials


class ArrayScene:
    """Keep carrier outlines fixed; independently orient only their inner bars."""
    def __init__(self, win, visual):
        self.circles = [visual.ShapeStim(
            win, vertices='circle', size=(OUTLINE_SIZE_DEG,) * 2,
            ori=0, lineWidth=STROKE_WIDTH_PX, lineColor=GRAY_RGB,
            colorSpace='rgb', fillColor=None, units='deg', autoLog=False,
        ) for _ in range(N_ITEMS)]
        # Draw the diamond directly as vertices, rather than rotating a square.
        # These vertices preserve the original 2-by-2-degree square's extent.
        self.diamond = visual.ShapeStim(
            win, vertices=DIAMOND_VERTICES_DEG, size=(1, 1),
            ori=0, lineWidth=STROKE_WIDTH_PX, lineColor=GRAY_RGB,
            colorSpace='rgb', fillColor=None, units='deg', autoLog=False,
        )
        self.triangle = visual.ShapeStim(
            win, vertices=TRIANGLE_VERTICES_DEG, size=(1, 1),
            ori=0, lineWidth=STROKE_WIDTH_PX, lineColor=GRAY_RGB,
            colorSpace='rgb', fillColor=None, units='deg', autoLog=False,
        )
        self.bars = [visual.Line(
            win, start=(0, -BAR_LENGTH_DEG / 2), end=(0, BAR_LENGTH_DEG / 2),
            ori=0, lineWidth=STROKE_WIDTH_PX, lineColor=BAR_RGB,
            colorSpace='rgb', units='deg', autoLog=False,
        ) for _ in range(N_ITEMS)]
        self.outlines = []
        self.prepared_index = None

    def prepare(self, trial, index):
        self.outlines = []
        for i in range(N_ITEMS):
            shape = trial['item_shapes'][i]
            outline = (self.diamond if shape == 'diamond' else
                       self.triangle if shape == 'triangle' else self.circles[i])
            outline.setPos(trial['item_positions_deg'][i], log=False)
            outline.setLineColor(trial['item_outline_rgb'][i], colorSpace='rgb', log=False)
            self.outlines.append(outline)
            self.bars[i].setPos(trial['item_positions_deg'][i], log=False)
            self.bars[i].setOri(trial['item_orientations'][i], log=False)
        self.prepared_index = index

    def draw(self):
        for outline in self.outlines:
            outline.draw()
        for bar in self.bars:
            bar.draw()


class ExperimentController:
    """Frame-driven controller, called by Builder routines (one row per trial)."""
    def __init__(self, win, exp_info, experiment, output_dir, keyboard_device=None):
        from psychopy import core, event, logging, visual
        from psychopy.hardware import keyboard
        self.core, self.event, self.logging = core, event, logging
        self.win, self.experiment = win, experiment
        self.keyboard = keyboard_device if keyboard_device is not None else keyboard.Keyboard()
        self.mouse = event.Mouse(win=win, visible=False)
        self.index = -1
        participant_number(exp_info['participant'])
        entered_seed = str(exp_info.get('seed', '')).strip()
        self.seed = int(entered_seed) if entered_seed else secrets.randbits(63)
        exp_info['seed'] = str(self.seed)
        self.schedule = build_schedule(exp_info['participant'], self.seed)
        exp_info['block_order'] = self.schedule[0]['block_order']
        exp_info['experiment_revision'] = EXPERIMENT_REVISION
        self.period = float(win.monitorFramePeriod)
        self.phase_frames = {
            'search': max(1, int(round(SEARCH_SECONDS / self.period))),
            'blank': max(1, int(round(BLANK_SECONDS / self.period))),
        }
        for trial in self.schedule:
            trial['fixation_frames'] = fixation_frame_count(trial['fixation_requested_seconds'], self.period)
            trial['fixation_scheduled_seconds'] = trial['fixation_frames'] * self.period
        self.scenes = [ArrayScene(win, visual), ArrayScene(win, visual)]
        self.scenes[0].prepare(self.schedule[0], 0)
        self.fixation = visual.ShapeStim(
            win, vertices='cross', size=(.5, .5),
            lineWidth=1, lineColor='white', fillColor='white',
            units='deg', autoLog=False,
        )
        self.response_bar = visual.Line(
            win, start=(0, -BAR_LENGTH_DEG / 2), end=(0, BAR_LENGTH_DEG / 2),
            ori=0, lineWidth=STROKE_WIDTH_PX, lineColor=BAR_RGB,
            colorSpace='rgb', pos=(0, 0), units='deg', autoLog=False,
        )
        self.message = visual.TextStim(
            win, text='', color='white', units='height', height=.032,
            wrapWidth=1.35, autoLog=False,
        )
        self.previous = None
        self.stage = None
        self.times = {}
        self.closed = False
        self.plan_path = Path(str(experiment.dataFileName) + '_trial_plan.json')
        self.plan_path.parent.mkdir(parents=True, exist_ok=True)
        metadata = {
            'experiment': 'dimension_weighting',
            'experiment_revision': EXPERIMENT_REVISION,
            'participant': str(exp_info['participant']), 'seed': self.seed,
            'angle_convention': '0 vertical; 90 horizontal; clockwise positive; axial [0,180)',
            'signed_error_convention': 'wrap180(report - target) in [-90,90)',
            'background_rgb': BACKGROUND_RGB, 'bar_rgb': BAR_RGB,
            'array_radius_deg': RADIUS_DEG, 'array_diameter_deg': 2 * RADIUS_DEG,
            'adjacent_center_distance_deg': 2 * RADIUS_DEG * math.sin(math.pi / N_ITEMS),
            'outline_size_deg': OUTLINE_SIZE_DEG, 'outline_width_px': STROKE_WIDTH_PX,
            'bar_stroke_width_px': STROKE_WIDTH_PX, 'bar_length_deg': BAR_LENGTH_DEG,
            'diamond_vertices_deg': DIAMOND_VERTICES_DEG,
            'outline_rotation_policy': 'all carrier orientations fixed at zero; only inner bars have randomized orientation',
            'triangle_vertices_deg': TRIANGLE_VERTICES_DEG,
            'triangle_inradius_deg': TRIANGLE_INRADIUS_DEG,
            'nominal_seconds': {'fixation_range': [FIXATION_MIN_SECONDS, FIXATION_MAX_SECONDS], 'search': SEARCH_SECONDS, 'blank': BLANK_SECONDS},
            'fixation_sampling': 'independent uniform seconds, rounded to the nearest refresh within the range',
            'response_pointer_policy': 'no cursor repositioning; hold randomized bar angle until first pointer movement, then follow cursor direction',
            'frame_period_seconds': self.period, 'fixed_phase_frames': dict(self.phase_frames),
            'eyetracking': False, 'feedback': False, 'practice_trials': 0,
            'trials': self.schedule,
        }
        self.plan_path.write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        self.win.recordFrameIntervals = True

    def _message_start(self, text):
        self.message.text = text
        self.mouse.setVisible(False)
        self.message_first_frame = True

    def _message_frame(self):
        if self.message_first_frame:
            # Clear on the first visible refresh, so earlier presses cannot skip it.
            self.win.callOnFlip(self.keyboard.clearEvents)
            self.message_first_frame = False
            self.message.draw()
            return True
        if self.keyboard.getKeys(keyList=['space'], waitRelease=False):
            return False
        self.message.draw()
        return True

    def start_instructions(self):
        self._message_start(INSTRUCTIONS)

    def instructions_frame(self):
        return self._message_frame()

    def start_end(self):
        self._message_start('The experiment is complete. Thank you.\n\nPress the space bar to finish.')

    def end_frame(self):
        return self._message_frame()

    def begin_trial(self):
        self.index += 1
        self.trial = self.schedule[self.index]
        self.phase_frames['fixation'] = self.trial['fixation_frames']
        self.scene = self.scenes[self.index % 2]
        if self.scene.prepared_index != self.index:
            raise RuntimeError('Upcoming array was not prepared before the preceding response.')
        self.times = {}
        self.row = {}
        self.first_movement_rt = None
        self.first_adjustment_rt = None
        self.confirmation_time = None
        self.break_started = None
        self.break_ended = None
        self.prepared_next = False
        self.dropped_start = self.win.nDroppedFrames
        if self.index and self.index % 100 == 0:
            self.stage = 'break'
            self._message_start(BREAK_TEXT)
        else:
            self._start_phase('fixation')

    def _start_phase(self, phase):
        self.stage = phase
        self.phase_onset_pending = True
        if phase == 'response':
            self.response_angle = self.trial['initial_response_angle']
            self.response_bar.setOri(self.response_angle, log=False)
            self.initial_cursor = None
            self.last_cursor = None
            self.pointer_has_moved = False
            self.previous_left = True  # require release before accepting a new click
            self.click_armed = False
            self.mouse.setVisible(True)

    def _stamp_phase(self):
        self.win.timeOnFlip(self.times, self.stage + '_onset')
        if self.stage == 'response':
            self.win.callOnFlip(self._capture_response_pointer)
        self.phase_onset_pending = False

    def _capture_response_pointer(self):
        # Pyglet's macOS cursor-warp path can fail with an NSEvent/objectForKey_
        # error. Read the real pointer instead of moving it. Until the participant
        # moves, its previous position must not overwrite the randomized bar.
        self.initial_cursor = tuple(float(value) for value in self.mouse.getPos())
        self.last_cursor = self.initial_cursor

    def _prepare_next(self):
        if not self.prepared_next:
            upcoming = self.index + 1
            if upcoming < len(self.schedule):
                self.scenes[upcoming % 2].prepare(self.schedule[upcoming], upcoming)
            self.prepared_next = True

    def trial_frame(self):
        if self.stage == 'break':
            if self.break_started is None:
                # The first break flip is also the offset of the preceding response.
                self.win.timeOnFlip(self.times, 'break_onset')
                self.break_started = True
            if self._message_frame():
                return True
            self.break_ended = self.logging.defaultClock.getTime()
            self._start_phase('fixation')

        future_flip = self.win.getFutureFlipTime(clock=None)
        if self.stage in self.phase_frames and not self.phase_onset_pending:
            onset = self.times[self.stage + '_onset']
            duration = self.phase_frames[self.stage] * self.period
            if future_flip >= onset + duration - .001:
                self._start_phase({'fixation': 'search', 'search': 'blank', 'blank': 'response'}[self.stage])

        first_frame = self.phase_onset_pending
        if first_frame:
            self._stamp_phase()
        elif self.stage == 'fixation':
            # Prepare the following array after fixation is already on screen.
            # This avoids stimulus creation or setup between click and fixation.
            self._prepare_next()

        if self.stage == 'fixation':
            self.fixation.draw()
        elif self.stage == 'search':
            self.scene.draw()
        elif self.stage == 'response':
            if not first_frame:
                xy = tuple(float(v) for v in self.mouse.getPos())
                now = self.logging.defaultClock.getTime()
                rt = now - self.times['response_onset']
                if math.hypot(xy[0] - self.last_cursor[0], xy[1] - self.last_cursor[1]) > 1e-6:
                    self.pointer_has_moved = True
                    if self.first_movement_rt is None:
                        self.first_movement_rt = rt
                new_angle = cursor_angle(*xy, self.response_angle) if self.pointer_has_moved else self.response_angle
                if abs(wrap180(new_angle - self.response_angle)) > 1e-6:
                    if self.first_adjustment_rt is None:
                        self.first_adjustment_rt = rt
                self.response_angle = new_angle
                self.last_cursor = xy
                self.response_bar.setOri(self.response_angle, log=False)
                left = bool(self.mouse.getPressed()[0])
                if not left:
                    self.click_armed = True
                if self.click_armed and left and not self.previous_left:
                    self.confirmation_time = now
                    self.confirmation_rt = rt
                    self.confirmation_cursor = xy
                    self.mouse.setVisible(False)
                    return False  # next Builder routine draws fixation on the next flip
                self.previous_left = left
            self.response_bar.draw()
        # blank phase deliberately draws nothing
        return True

    def end_trial(self):
        trial = dict(self.trial)
        trial.update(self.times)
        trial.update({
            'response_angle': self.response_angle,
            'signed_error': wrap180(self.response_angle - self.trial['target_orientation']),
            'confirmation_time': self.confirmation_time,
            'confirmation_rt': self.confirmation_rt,
            'adjustment_onset_rt': self.first_adjustment_rt,
            'mouse_movement_onset_rt': self.first_movement_rt,
            'confirmation_cursor_deg': self.confirmation_cursor,
            'response_pointer_start_deg': self.initial_cursor,
            'response_pointer_moved': self.pointer_has_moved,
            'fixation_duration_actual': self.times['search_onset'] - self.times['fixation_onset'],
            'search_duration_actual': self.times['blank_onset'] - self.times['search_onset'],
            'blank_duration_actual': self.times['response_onset'] - self.times['blank_onset'],
            'frame_period_seconds': self.period,
            'dropped_frames': self.win.nDroppedFrames - self.dropped_start,
            'search_requested_seconds': SEARCH_SECONDS,
            'blank_requested_seconds': BLANK_SECONDS,
            'break_before_trial': bool(self.index and self.index % 100 == 0),
            'break_continue_time': self.break_ended,
            'bar_rgb': BAR_RGB, 'bar_stroke_width_px': STROKE_WIDTH_PX,
            'bar_length_deg': BAR_LENGTH_DEG, 'outline_size_deg': OUTLINE_SIZE_DEG,
            'outline_width_px': STROKE_WIDTH_PX,
            'previous_trial_number': self.previous['trial_number'] if self.previous else None,
            'previous_condition': self.previous['condition'] if self.previous else None,
            'previous_block_context': self.previous['block_context'] if self.previous else None,
            'previous_target_orientation': self.previous['target_orientation'] if self.previous else None,
            'previous_distractor_orientation': self.previous['distractor_orientation'] if self.previous else None,
            'previous_response_angle': self.previous['response_angle'] if self.previous else None,
            'previous_target_index': self.previous['target_index'] if self.previous else None,
            'previous_distractor_index': self.previous['distractor_index'] if self.previous else None,
            'previous_confirmation_time': self.previous['confirmation_time'] if self.previous else None,
            'previous_confirmation_to_fixation_seconds': self.times['fixation_onset'] - self.previous['confirmation_time'] if self.previous else None,
            'lag1_valid': bool(self.previous and self.previous['block'] == self.trial['block']),
        })
        valid = trial['lag1_valid']
        trial['lag1_target_difference'] = wrap180(trial['previous_target_orientation'] - trial['target_orientation']) if valid else None
        trial['lag1_distractor_difference'] = wrap180(trial['previous_distractor_orientation'] - trial['target_orientation']) if valid and trial['previous_distractor_orientation'] is not None else None
        for key, value in trial.items():
            self.experiment.addData(key, trial_data_cell(value))
        self.previous = dict(self.trial, response_angle=self.response_angle,
                             confirmation_time=self.confirmation_time)

    def close(self):
        if self.closed:
            return
        self.closed = True
        self.mouse.setVisible(True)
        self.win.recordFrameIntervals = False
