---
title: Unreal Engine Black Eye Cameras: V1.2 Preview Shot List module
source: YouTube
url: https://www.youtube.com/watch?v=w2CBsFWMUys
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.2
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, esports, live-events, mocap, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-v12-preview-shot-list-module/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: V1.2 Preview Shot List module

**Source:** [YouTube](https://www.youtube.com/watch?v=w2CBsFWMUys)
**Author:** Black Eye Technologies
**Duration:** 1m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** This is a cool side-hinging shot, but you know it goes bad. And this shot, and it goes bad too. And this one? And this is a neat shot, but it starts out bad. What if your cameras knew when they had the shot? So let's add that functionality of this camera here. It knows. As soon as the character walks under something, it cuts to a safer shot, and then it cuts back. And you can put cameras in your world, and this system will evaluate them and cut between them based on an order that you best apply. And this is a new feature, the black eye shot list. And here's how it works. It's one camera where you set multiple sub-cameras. They're priority-stacked. It'll try to do the first shot. But if that's occluded, it'll do the next. And so on down the list. There's a minimum shot time, so your cut don't happen too quickly. And it does a ray cast from the camera to the subject. And you can build these simple but very powerful rigs where you're getting a dynamic cutting. This is a game changer for esports, replays anywhere where you want cameras to figure out the best shots themselves. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v12-preview-shot-list-module\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.2 Shot List module: a single camera actor containing an ordered list of sub-cameras; uses raycasting to auto-evaluate which sub-camera has an unoccluded shot and cuts to it, with a minimum shot time to prevent rapid-fire cuts.

### Summary
1-minute feature preview for the Black Eye Shot List introduced in v1.2. Solves the problem of cameras getting occluded (character passes under an obstacle, blocking the shot). One Shot List camera holds multiple sub-cameras in a priority stack; the system raycasts from camera to subject and automatically cuts to the next available unoccluded shot. A minimum shot time prevents jitter. Extremely powerful for eSports, replay cameras, and any live scenario where you can't manually control cuts.

### Key Steps
1. **Create a Shot List camera** — Add a Black Eye Shot List camera to the scene (new camera type in v1.2).
2. **Add sub-cameras to priority stack** — Each sub-camera is a separate Black Eye camera (with its own Follow/LookAt config). Add them in order of preference (best shot first).
3. **Set minimum shot time** — Prevents the system from cutting too rapidly when the shot quality fluctuates at the threshold.
4. **Place cameras to cover your scene** — Ensure your sub-camera positions cover all angles so there's always at least one unoccluded option.
5. **Raycast evaluation** — The system automatically raycasts from each sub-camera to the subject. The first un-occluded camera in the priority list wins. When the character walks under something, the system cuts to a safer shot and cuts back when clear.

### UE Systems / Blueprints / Settings
- **Shot List** — Black Eye v1.2+ camera actor; contains ordered array of sub-cameras
- **Priority stack** — ordered list; system tries camera 0 first, falls back down the list when occluded
- **Raycast evaluation** — each tick, raycast from camera position to subject; occlusion triggers priority fallback
- **Minimum shot time** — cooldown before the system is allowed to cut again; prevents rapid-fire switching

### Difficulty
Intermediate

### UE Version
UE 5.x (Black Eye v1.2)

### Tags
`#blackeye-v1` `#camera` `#esports` `#live-events` `#mocap` `#intermediate`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:07] tutorials/frames/unreal-engine-black-eye-cameras-v12-preview-shot-list-module/frame_000.jpg
- [0:22] tutorials/frames/unreal-engine-black-eye-cameras-v12-preview-shot-list-module/frame_001.jpg
- [0:40] tutorials/frames/unreal-engine-black-eye-cameras-v12-preview-shot-list-module/frame_002.jpg
- [0:58] tutorials/frames/unreal-engine-black-eye-cameras-v12-preview-shot-list-module/frame_003.jpg

## Related Entries
- [[unreal-engine-black-eye-cameras-cam-switcher-tutorial]] — manual camera switcher (keyboard-driven); complementary to the auto Shot List
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — full v1 system overview including Camera Switcher
- [[plugin-blackeye-versions]] — v1.2 feature release notes
