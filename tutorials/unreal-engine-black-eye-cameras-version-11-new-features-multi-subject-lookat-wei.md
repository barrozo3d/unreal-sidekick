---
title: Unreal Engine Black Eye Cameras: Version 1.1 New Features: Multi_Subject LookAt Weights
source: YouTube
url: https://www.youtube.com/watch?v=WBgBhPjzzbI
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, look-at, multiple-subjects, weights, bone-targeting, v1-1]
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
**Transcript:** There's a new version of Black Eye version 1.1 with some cool new features like this. Multi look at weights. Subject buys and okay look at these ding dogs. So let's set this up. You can now go to the place actor and drop a Black Eye camera into the scene. What we're going to do is we're going to look at both of them so we're going to add another subject. And on one we're going to pick the left person and on the right. On you can see the two blue cubes. Let's bring the clip down onto the camera cuts track. Okay, so we're tracking these two. But look at this new control. Weight. So let's make it so we're not tracking the whole body. Let's track the head. So we're now tracking both heads. Just going to adjust the screen composition a little bit and do some dynamic zooming to frame it. So look at this weight. Head one. Head two. So this is one camera. Two different weights. You can adjust the weights on different objects or different parts of the same object. And of course once that's set up it all still works with the objects moving. Now something to note. You can't keep frame this in sequence for just yet. We're working with the Epic team. There's going to be a fix soon. You can do it through Blueprints. Upcoming version very soon. You'll be able to keep frame this in sequence. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei\frame_000.jpg


---

## Structured Notes

### Core Technique
BEC v1.1 feature announcement: per-subject **Look At weights**. Each subject in the multi-subject Look At module now has an individual weight slider (0–1). Lets you mix or fade attention between different subjects or different body parts on the same subject. ⚠️ At time of recording: Sequencer keyframing of these weights was NOT yet available (planned for a near-future update with Epic team support). Blueprint-only control at v1.1. The Sequencer keyframing landed in v1.1.1 — see companion tutorial.

### Summary
1m25s BEC v1.1 multi-subject LookAt weights reveal. Short demo: two characters, Look At both heads. New weight slider per subject allows blending contribution of each head toward camera framing. Demonstrated with head 1 vs head 2 weight at various levels. Camera correctly composes on the weighted combination. Known limitation at time of recording: weight keyframing in Sequencer not yet available; use Blueprint to animate weights. Fix coming in v1.1.1.

### Key Steps
1. Place Black Eye camera → enable **Look At** → add Subject 2
2. Subject 1 → eyedropper → left character; change bone to "head"; disable Use Component Bounds → blue cube on head
3. Subject 2 → eyedropper → right character; change bone to "head" → blue cube on second head
4. New in v1.1: **Weight** slider per subject → slide between 0 and 1
5. Weight 1 full + Weight 2 zero = camera looks only at subject 1; equal weights = blended framing; adjust to taste
6. Drag camera clip to Camera Cuts track → camera tracks weighted combination in real-time
7. ⚠️ To animate weights over time at v1.1: must use Blueprint to set weight values per frame; Sequencer keyframing not yet available
8. (Upgrade to v1.1.1 for full Sequencer keyframe support — see `version-111-keyable-weights-in-sequencer.md`)

### UE Systems / Blueprints / Settings
- **Look At Subject Weight** (per-subject) — 0=ignored, 1=full weight; camera computes combined weighted bounding box and aims at result
- **Multi-subject Look At** — supports N subjects; white box = weighted aggregate of all blue subject boxes
- **Bone targeting** — works per-subject; type bone name (e.g., "head") + disable Use Component Bounds + adjust Bounding Radius
- **Blueprint weight animation** (v1.1 only) — set subject weights via BP to animate over time; Sequencer keyframing added in v1.1.1

### Difficulty
Beginner. One slider added to existing Look At multi-subject setup.

### UE Version
UE5 (Black Eye Cameras v1.1)

### Tags
black-eye-cameras, look-at, multiple-subjects, weights, bone-targeting, v1-1

---

## Related Entries
- `unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer.md` — v1.1.1 Sequencer keyframe implementation of this feature
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — multi-subject Look At + weight blending shown in detail
