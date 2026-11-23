# Target and distractor history in visual search

### Background

Maljkovic and Nakayama (1994, Experiment 8) found that repeating either the target color or the distractor color facilitated search, with a larger benefit for target-color repetition. We ask whether selection history also carries over to a different feature of those same objects: their orientation.

### Question and hypotheses

Does selecting or ignoring an object on one trial influence how its orientation biases the target-orientation report on the next trial?

| Hypothesis | Prediction |
|---|---|
| **H1. Target-history facilitation** | Target-color repetition speeds search. Reports are attracted toward the previous target orientation. |
| **H2. Distractor-history suppression** | Distractor-color repetition speeds search. If suppression leaves a repulsive trace, reports shift away from previous distractor orientations. |
| **H3. Attentional gating** | The magnitude or direction of distractor-induced bias depends on how effectively distractors were ignored during the preceding trial. |

### Dependent variables

Target localization RT and accuracy, and signed orientation error (reported minus actual target orientation on the current trial, wrapped to ±90°).

### Experimental design

Each trial contains one array of three independently oriented Gabors in colored rings at randomly assigned locations. One ring has a unique color and defines the target. Participants locate the target and then reproduce its orientation from memory.

**Fixation → Search and localize the target → Reproduce the target orientation**

The within-participant design crosses **target-color repetition** (repeated/changed) with **distractor-color repetition** (repeated/changed) across consecutive trials. Changed colors are absent from the previous trial to prevent role reversals. Target positions and color identities are balanced across conditions.

### Analysis

For **H1 and H2**, estimate both color-repetition effects on correct-trial log RT and check accuracy for speed–accuracy trade-offs. Model signed orientation error on trial \(n\) jointly as a function of the angular differences between the current target and each of the three items on trial \(n-1\). H1 predicts target-induced attraction. H2 predicts distractor-induced repulsion. Test whether target-color repetition changes target-induced bias and whether distractor-color repetition changes distractor-induced bias.

**H3 requires a separate measure or manipulation of attention on trial \(n-1\).** In a follow-up, present either a valid distractor-color cue or a neutral cue before the search array on trial \(n-1\). Test whether cueing changes distractor-induced bias on trial \(n\), and use occasional probe-letter trials to verify that cueing reduced processing at distractor locations.