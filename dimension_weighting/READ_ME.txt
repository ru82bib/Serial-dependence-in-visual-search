DIMENSION WEIGHTING EXPERIMENT

HOW TO RUN

Keep all files in this folder together. Open dimension_weighting.psyexp in
PsychoPy Builder and run it, or open dimension_weighting.py in PsychoPy Coder
and run that script. The generated script was compiled with the installed
PsychoPy 2026.2.4. The Builder file was adapted from exp_1.psyexp.

Enter a numeric participant ID (for example, 001 or 002). Odd IDs receive
the gray-triangle block first; even IDs receive the red-circle block first.
If Pilot mode substitutes the word "pilot", replace it with a numeric ID.
Leave seed blank for a new random sequence, or enter an integer to replay a
sequence with the same participant ID and the same experiment settings.
Press Escape to end a session early.

DESIGN

Two blocks, 600 experimental trials each. No practice, no feedback, and no
eye tracking. Each block has exactly 300 distractor-present trials and 300
distractor-absent trials in randomized order. The diamond target is always
present. A triangle appears only in SD-present trials; a red circle appears
only in DD-present trials. Absent trials replace that distractor with an
ordinary gray circle, so there are always 12 items.

The array has 12 equally spaced fixed positions at a radius of 5.9143 degrees
(11.8286-degree diameter through the item centers). This increases the array
radius to preserve the old eight-item array's adjacent center-to-center
distance of 3.0615 degrees while retaining the original carrier sizes.
The radius is calculated as 4 * sin(pi/8) / sin(pi/12).
Target and distractor locations are randomly assigned each trial and cannot
coincide. Location sampling follows the same procedure in both contexts;
individual location/transition counts are not artificially constrained.
Every item's internal bar orientation is sampled independently in [0,180)
degrees. Carrier shapes remain fixed: upright triangles and diamonds, with
no random rotation of their outlines. Only the internal bars receive random
orientations; the central response bar is adjusted with the mouse.

Circle diameter remains 2 degrees. The diamond is defined directly by its
vertices, preserving the extent of the old 2-by-2-degree square at 45 degrees;
the carrier itself has no rotation transform. All search outlines and all
internal/response bars share an 8-pixel stroke. Bars are drawn as 0.9-degree
lines rather than filled rectangles, so visible thickness matches the outlines.
The upright triangle retains its 2-by-2-degree size, with its outline centered
around the bar's rotation point so every bar orientation fits. Its vertices
are approximately (0,1.382), (-1,-0.618), (1,-0.618) degrees.
The fixation cross retains its old
0.5-by-0.5-degree size. Ordinary-circle gaps match those in the old array.

PsychoPy RGB values: background [0,0,0], gray outlines [0.5,0.5,0.5],
red outline [1,-1,-1], and bars/fixation [1,1,1]. These are the confirmed RGB
settings, not measured luminance calibration values. The original monitor
name testMonitor, full-screen mode, and 1920-by-1200 window setting are retained.
Use the experimental computer's calibrated monitor profile for visual degrees.

TRIAL AND RESPONSE

Random 500–800 ms fixation -> 800 ms search -> 200 ms empty background ->
self-paced central orientation reproduction. Each trial independently draws
fixation duration uniformly from 500–800 ms using a separate seeded timing
stream. The requested duration is rounded to the nearest whole refresh frame
within that range (30–48 frames at 60 Hz). Search and blank remain fixed.
Requested fixation, scheduled fixation frames/seconds, actual flip times and
actual durations are saved. Search exposure is never shortened by a response.

The response bar's initial angle is independently randomized. The cursor is
not repositioned. The starting bar angle remains visible until the participant
moves the mouse; the bar then follows the cursor direction relative to center.
This avoids a macOS/Pyglet cursor-repositioning crash. The actual cursor
position at reproduction onset and whether it was moved are saved.
Left-click confirms. At the exact center the previous angle is retained.
A held left button is ignored until it is released and pressed again.
The next fixation follows confirmation without an added intertrial interval,
except when a scheduled break or the completion screen follows.

After each 100 completed trials, except after the final trial, this exact
message appears:
feel free to take a break at this point. continue by pressing space bar

Pressing space continues the trials. There are eleven such breaks, including
the transition between blocks. Key presses queued before the break screen
appears are discarded. No response correctness or accuracy feedback appears.

FILES AND DATA

dimension_weighting.psyexp       Editable PsychoPy Builder experiment
dimension_weighting.py           Compiled desktop experiment
dimension_weighting_runtime.py   Shared stimulus, scheduling, and response logic

The Builder file and compiled script both require the runtime file in the
same folder. No old image or conditions CSV is required. If you change the
Builder flow, recompile the Python script. Changing runtime constants affects
both entry points; changing trial counts also requires updating Builder's
loop and the present/absent construction, so do not change only one of them.

Session files are written under data/ in this folder:
  CSV: wide trial-level data, with item arrays in Python list notation
  PSYDAT: PsychoPy's native session data
  LOG: PsychoPy session log
  *_trial_plan.json: complete planned sequence, seeds, geometry, and settings

Filter CSV rows to nonempty trial_number for the 1,200 experimental responses;
Builder may also save instruction/completion rows. No real participant data
is included in this package. The plan records planned trials, including any
not reached if the session ends early; the response CSV records completed ones.

Important columns include block, block_context, condition, distractor_present,
target_index, distractor_index, item_positions_deg, item_shapes,
item_outline_rgb, item_outline_orientations, item_orientations,
initial_response_angle, response_angle, signed_error, phase onset times,
actual phase durations, adjustment_onset_rt, mouse_movement_onset_rt,
confirmation_rt, dropped_frames, and previous-trial predictors.
New revision fields include experiment_revision, array_radius_deg,
fixation_requested_seconds, fixation_frames, and fixation_scheduled_seconds.
The current revision is 2026-11-25-fixed-outlines-matched-strokes; earlier session files retain
their original geometry and timing. Restart the experiment to load this revision;
an already-running session continues with the settings loaded at its start.
CSV array cells can be read with Python ast.literal_eval. The separate trial
plan uses JSON. This avoids the installed PsychoPy writer's handling of quotes
inside JSON strings; new exports keep item-name arrays and subsequent columns
aligned. Earlier CSV files and session data have not been overwritten.

Angles: 0 degrees is vertical, 90 is horizontal, and positive rotation is
clockwise. Bar orientations are axial, not directional. Signed error is
(response - target + 90) % 180 - 90, in [-90,90). Missing distractors have
missing index/orientation fields. lag1_valid is false at the start of each
block; use that flag to exclude transitions across block boundaries.
Previous distractor condition and block context are separate columns, so
absent trials retain their SD/DD context. Adjustment onset and confirmation
RTs are response measures, not pure visual-search RTs.

The next trial's previous_confirmation_to_fixation_seconds records the gap
between the preceding confirmation and its own fixation onset. That gap
includes any intervening break; break_before_trial identifies those cases.

VALIDATION

Successfully compiled with the installed PsychoPy 2026.2.4 Builder compiler.
Independent tests checked reproducible scheduling, odd/even counterbalancing,
exact 300/300 counts, distinct locations, continuous orientations, and angle
conversions. A simulated full 1,200-trial run checked all eleven breaks,
space continuation, held-click rejection, trial logging, block-boundary
exclusions, varying 30–48-frame fixation, and fixed 48/12-frame search/blank
phases at 60 Hz. Geometry validation confirms the new twelve-item array's
adjacent center-to-center spacing matches the original eight-item array.
Additional checks verify static carrier orientations across all trials and
identical 8-pixel strokes for the outlines, internal bars, and response bar.
With the existing monitor profile, the shortened 0.9-degree bars fit within
every carrier at every orientation, including their shared stroke width.

Live graphical validation could not run in this execution environment:
PsychoPy's graphics backend reported no available display. Before collecting
data, run a short hardware check on the experiment computer for rendering,
cursor behavior, monitor calibration, and refresh timing. Compilation and
simulation do not establish measured screen timing or photometric calibration.
