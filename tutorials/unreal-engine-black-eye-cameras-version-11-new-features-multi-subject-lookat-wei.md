---
title: Unreal Engine Black Eye Cameras: Version 1.1 New Features: Multi_Subject LookAt Weights
source: YouTube
url: https://www.youtube.com/watch?v=WBgBhPjzzbI
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Version 1.1 New Features: Multi_Subject LookAt Weights

**Source:** [YouTube](https://www.youtube.com/watch?v=WBgBhPjzzbI)
**Author:** Black Eye Technologies
**Duration:** 1m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** There's a new version of Black Eye version 1.1 with some cool new features like this. Multi look at weights. Subject buys and okay look at these ding dogs. So let's set this up. You can now go to the place actor and drop a Black Eye camera into the scene. What we're going to do is we're going to look at both of them so we're going to add another subject. And on one we're going to pick the left person and on the right. On you can see the two blue cubes. Let's bring the clip down onto the camera cuts track. Okay, so we're tracking these two. But look at this new control. Weight. So let's make it so we're not tracking the whole body. Let's track the head. So we're now tracking both heads. Just going to adjust the screen composition a little bit and do some dynamic zooming to frame it. So look at this weight. Head one. Head two. So this is one camera. Two different weights. You can adjust the weights on different objects or different parts of the same object. And of course once that's set up it all still works with the objects moving. Now something to note. You can't keep frame this in sequence for just yet. We're working with the Epic team. There's going to be a fix soon. You can do i...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.1 Multi-Subject LookAt Weights: assign independent weight values per subject on a multi-subject LookAt to blend the camera's attention between different objects or bone targets on the same character.

### Summary
1.5-minute feature preview for Multi-Subject LookAt Weights introduced in v1.1. One camera can LookAt two subjects simultaneously with adjustable weight per subject. Demonstrates tracking head and pelvis on the same character at different weights. Blue debug cubes show active subjects. Important limitation at time of recording: weights are not yet keyframeable in Sequencer (that was fixed in v1.1.1 — see [[unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer]]).

### Key Steps
1. **Drop camera + set LookAt** — add Black Eye camera, click Look At → open subjects array.
2. **Add second subject** — click + in subjects → eyedropper for each. Both show as blue cubes.
3. **Target bones (not actor bounds)** — for intra-character targeting (head + pelvis): disable actor bounds, type bone names.
4. **Adjust weights** — each subject has a Weight value (0–1). At weight 1/weight 1, camera averages both; bias toward one by raising its weight and lowering the other.
5. **Drag to Sequencer** — add to Camera Cuts track to activate.
6. **Note: not yet keyframeable** — as of v1.1, weights cannot be keyframed in Sequencer. Upgrade to v1.1.1 for keyframeable weights.

### UE Systems / Blueprints / Settings
- **Multi-Subject LookAt** — subjects array; each entry has Weight (float 0–∞, normalized internally)
- **Blue debug cubes** — visualize each active LookAt target and its bounding volume
- **Bone targeting** — disable "actor bounds"; type bone name manually
- **Keyframing limitation** — weights not keyframeable in v1.1; fixed in v1.1.1

### Difficulty
Intermediate

### UE Version
UE 5.x (Black Eye v1.1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#intermediate`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer]] — v1.1.1 makes weights keyframeable in Sequencer
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Multiple Subjects + Keyframe Weights sections
