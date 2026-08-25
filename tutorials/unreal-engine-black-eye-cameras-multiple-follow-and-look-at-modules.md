---
title: Unreal Engine Black Eye Cameras: Multiple follow and look at modules
source: YouTube
url: https://www.youtube.com/watch?v=lzFH7Peyyk0
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Multiple follow and look at modules

**Source:** [YouTube](https://www.youtube.com/watch?v=lzFH7Peyyk0)
**Author:** Black Eye Technologies
**Duration:** 1m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye multiple Follow and LookAt modules on a single camera rig: one camera can simultaneously follow multiple subjects and look at multiple subjects independently, with the subjects configured in separate arrays.

### Summary
1.75-minute tutorial demonstrating having multiple Follow targets and multiple LookAt targets on a single Black Eye camera rig. Frame shows: "Select a Black Eye camera rig / Select the stuff you want to follow" — the video walks through adding multiple entries to both the Follow and LookAt subject arrays. No narration recoverable from audio. Key concept: Follow and LookAt are independent systems with their own subject arrays; a camera can follow the average position of multiple objects while simultaneously looking at a different set of subjects.

### Key Steps
N/A — visual demo only (audio transcript empty). Core workflow:
1. Select Black Eye camera rig.
2. Click Follow → open subjects → add multiple entries via + → eyedropper each subject.
3. Click LookAt → open subjects → add multiple entries → eyedropper each.
4. Adjust weights and damping per-system as needed.
5. Camera position = weighted average of Follow subjects; camera rotation = composite of LookAt subjects.

### UE Systems / Blueprints / Settings
- **Follow subjects array** — multiple targets; camera position = weighted average of all Follow positions
- **LookAt subjects array** — multiple targets; camera rotation = composite look-at of all LookAt positions
- **Independent systems** — Follow and LookAt can track completely different objects simultaneously

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#beginner`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:10] tutorials/frames/unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules/frame_000.jpg
- [0:31] tutorials/frames/unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules/frame_001.jpg
- [0:57] tutorials/frames/unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules/frame_002.jpg
- [1:23] tutorials/frames/unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules/frame_003.jpg

## Related Entries
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — Multiple Subjects section (foundational)
- [[unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei]] — per-subject LookAt weights
- [[unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer]] — keyframeable weights for multi-subject
