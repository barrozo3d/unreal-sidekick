---
title: Unreal Engine Black Eye cameras: Dynamic Dialog intro
source: YouTube
url: https://www.youtube.com/watch?v=vKG_qFXKcyY
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v2
ue_version: "UE 5.3+"
tags: [blackeye-v2, camera, dialogue, cinematics, gameplay, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-dynamic-dialog-intro/
frame_count: 4
---

# Unreal Engine Black Eye cameras: Dynamic Dialog intro

**Source:** [YouTube](https://www.youtube.com/watch?v=vKG_qFXKcyY)
**Author:** Black Eye Technologies
**Duration:** 1m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Dialogue camera systems, especially when things are variable, can be tricky. Black eye to the rescue. Look at this. You set these shots up, and characters move. The camera's figured it out. You can grab a camera, and you can say, this is the angle that I want. Black eye will get that shot for you, just like a camera operator, even when things change. So we're not taking anything away from you. We're allowing you to work so fast, you're working on the shot, you're working on the framing that you want, and then for a game with a variable dialogue scene, you don't know what people are seeing, maybe you don't know how many lines you're going back and forth, different size characters, and we'll still figure it out. So here's what works. This camera, we're looking at the girl's head, that's that blue cube, and the chest, and then we're looking at the guy on the left's frame. In this white box here, that's the frame, that's the camera figuring out, that shot, no matter what happens. But then you can just grab a camera and be like, no, let's, how does it look like from here? And then things can change. Camera's figured it out. Good cameras make great projects. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-dynamic-dialog-intro\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye Cameras Dynamic Dialog system: cameras track two characters' head and chest bones and auto-frame dialogue shots even when character counts, line counts, or sizes vary.

### Summary
1-minute intro to Black Eye's Dynamic Dialog camera mode. You set a desired shot/angle for a dialogue scene; Black Eye tracks the target bones (head, chest) of each participant and recalculates framing automatically regardless of how many lines are spoken, how many characters are present, or how their sizes differ. The white bounding box visible in the frame represents the camera's computed frame target.

### Key Steps
1. **Place a dialogue camera** — position it at the angle you want for the scene.
2. **Assign bone targets** — set "look at" bones for each character (e.g., head + chest of character A; frame of character B shown as white bounding box).
3. **Camera Manager handles framing** — Black Eye computes the correct framing automatically from the bone data, even if characters move, script changes, or characters are different sizes.
4. **Grab and redirect** — you can re-grab the camera mid-scene and change the angle; Black Eye recalculates framing from the new position.
5. **Variable dialogue support** — works with unknown dialogue lengths, variable participant counts, and multi-size characters without per-shot tweaking.

### UE Systems / Blueprints / Settings
- **Dynamic Dialog camera mode** — Black Eye camera sub-mode; assigns per-character bone targets (head, chest)
- **White bounding box** — on-screen frame preview showing the computed shot boundary
- **Camera Manager** — routes framing math; no manual keyframing needed for bone tracking

### Difficulty
Beginner

### UE Version
UE 5.3+ (Black Eye v2)

### Tags
`#blackeye-v2` `#camera` `#dialogue` `#cinematics` `#gameplay` `#beginner`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:07] tutorials/frames/unreal-engine-black-eye-cameras-dynamic-dialog-intro/frame_000.jpg
- [0:20] tutorials/frames/unreal-engine-black-eye-cameras-dynamic-dialog-intro/frame_001.jpg
- [0:36] tutorials/frames/unreal-engine-black-eye-cameras-dynamic-dialog-intro/frame_002.jpg
- [0:53] tutorials/frames/unreal-engine-black-eye-cameras-dynamic-dialog-intro/frame_003.jpg

## Related Entries
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — Cross Camera section covers two-subject tracking (same underlying system)
- [[unreal-engine-black-eye-cameras-version-11-new-features-cross-camera]] — Cross Camera v1.1 feature that precedes Dynamic Dialog
