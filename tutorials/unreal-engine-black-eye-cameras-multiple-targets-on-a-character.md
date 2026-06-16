---
title: Unreal Engine Black Eye Cameras: Multiple targets on a character
source: YouTube
url: https://www.youtube.com/watch?v=x18zbUJoI9U
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-multiple-targets-on-a-character/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Multiple targets on a character

**Source:** [YouTube](https://www.youtube.com/watch?v=x18zbUJoI9U)
**Author:** Black Eye Technologies
**Duration:** 0m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Nothing leafles, but itええ!

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-multiple-targets-on-a-character\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye multi-bone targeting on a single character: LookAt targeting both Head and Torso_5 (spine) bones simultaneously to frame a specific body region regardless of animation.

### Summary
32-second short demonstrating Black Eye targeting two bones on the same character (a cat/animal). Frame shows subtitle: "The Black Eye Unreal Camera system is targeting the Head and Torso_5 bones." No narration recoverable from transcript. Shows the multi-subject LookAt applied to intra-character bone pairs for precise body-region framing (e.g., upper body / mid-body) rather than actors.

### Key Steps
N/A — visual demo only. For implementation see [[unreal-engine-black-eye-cameras-start-here-tutorial]] Multiple Subjects + Keyframe Weights sections.

Concept: add multiple subjects to LookAt, each targeting a different bone on the same character (disable actor bounds for each, type bone names). Camera frames the combined bounding region of those bones.

### UE Systems / Blueprints / Settings
- **Multi-subject LookAt (intra-character)** — multiple entries in LookAt subjects array, each targeting a different bone on the same character
- **Bone targeting** — disable actor bounds; type bone name (Head, Torso_5, spine_01, etc.)

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei]] — Multi-subject LookAt weights (weight per bone)
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Multiple Subjects + Keyframe Weights sections
