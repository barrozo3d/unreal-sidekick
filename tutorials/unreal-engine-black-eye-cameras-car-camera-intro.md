---
title: Unreal Engine Black Eye Cameras: Car camera INTRO
source: YouTube
url: https://www.youtube.com/watch?v=Wh-QAH49C70
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, teaser, pointer, not-a-tutorial]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Car camera INTRO

**Source:** [YouTube](https://www.youtube.com/watch?v=Wh-QAH49C70)
**Author:** Black Eye Technologies
**Duration:** 1m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, this is Adam. We just released a new Black Eye tutorial video for driving cameras. So for gameplay, look at this. You can feel the weight of the car. It's not stuck to the middle of the screen. It's moving. Like, it's not 1996 anymore. Having a car stuck to the middle of the screen, you can't feel the physics. But with Black Eye, you can feel the acceleration, the deceleration, the braking, the how the tires are sticking to the road. And I'll show you how fast it is to set up. Controls for rotational damping, lots. Here's hardly any. So you can fine-tune your camera. We show you the effects of like variable pivot points. See how it's far in front. And as you slow down, it comes further back. You can create crazy drone cameras. And for cinematics shooting cars, I'll break down how you can do sweeping flybys, how you can lean into Black Eye's procedural composition, and easy off-sets, follow modes. So you can, in a handful of keyframes, create these beautiful sweeping buttery smooth sequences. Look at this. As the car speeds up, we're looking at the front of the car. As it slows down, we're looking at the whole thing. Magic. Come check it out. It's on YouTube. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-camera-intro\frame_000.jpg


---

## Structured Notes

### Core Technique
**Promo/intro video for the Black Eye car camera tutorial.** No technical steps — previews features covered in the full tutorial: rotational damping, positional damping, velocity look ahead (pivot point moves forward with speed), variable pivot position, drone cameras, cinematic flyby shots, and procedural composition key framing. See `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` for full details.

### Summary
1m17s teaser by Adam (Black Eye Technologies) promoting the full car cameras tutorial. Demonstrates the difference between rigid 1996-style car cameras vs. Black Eye's physics-responsive driving cameras. Highlights: rotational damping control, velocity look ahead (pivot shifts forward when speeding, back when slowing), drone-style elevated cameras, cinematic sweeping flyby shots. No technical steps.

### Key Steps
*Promo video — see `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` for full workflow.*

### UE Systems / Blueprints / Settings
*Not detailed in this video — see companion tutorial.*

Key capabilities teased:
- **Rotational damping** — controls how quickly camera rotates to track subject
- **Velocity Look Ahead** — pivot point moves forward with speed; centers at rest
- **Variable pivot position** — offset look-at point from car center to front/rear
- **Dynamic FOV** — auto-zoom for drone/replay cameras
- **Cinematic composition key framing** — just key frame desired composition; BEC handles rotation

### Difficulty
N/A (promo)

### UE Version
UE5

### Tags
black-eye-cameras, car-camera, driving, cinematics, follow, damping, velocity-lookahead, gameplay

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:08] tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/frame_000.jpg
- [0:23] tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/frame_001.jpg
- [0:42] tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/frame_002.jpg
- [1:02] tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/frame_003.jpg

## Related Entries
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — full 24-minute car camera tutorial; all settings explained
