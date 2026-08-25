---
title: Unreal Engine Black Eye Cameras: Crazy Millennium Falcon shot with only 7 keyframes
source: YouTube
url: https://www.youtube.com/watch?v=7jNy5snGOJM
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, cinematics, spaceship, follow, composition, keyframes, camera-shake, bake, workflow]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Crazy Millennium Falcon shot with only 7 keyframes

**Source:** [YouTube](https://www.youtube.com/watch?v=7jNy5snGOJM)
**Author:** Black Eye Technologies
**Duration:** 2m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** This amazing shot from the Force Awakens. Let's do it in Black Eye with only 7 Q frames in a couple of minutes. Let's go. You might have seen this video from Merit on YouTube. It breaks it down. It showed the stabilization. This was the inspiration. Okay, so I got a Millennium Falcon in a desert from Fab. There are links to that below. Did a real quick animation. Drop the Black Eye camera in the scene. Set it to follow. Put the distance. How to kind of close because we want this bringingness of the camera damping to give it some mojo. Let's get the angle. Yeah, so a little bit more wide damping. That's the distance damping on the camera. Then just set the look at the Millennium Falcon. Very simple. There's the screen space composition. We're going to keyframe that. I'll show you that in a sec. Then a bit of damping on the composer. Okay, then this is the follow. We've got the follow mode to be subject locked. That means we're listening to all of the follow transforms. Then here's the keyframes. Very few. Some on the roll. This is the screen space composition keyframes. Right now we're in the center. I drag the playhead over. Now we're saying, be on the left of the screen. This is so powerful. You keyframe where you want something to be on screen. So it goes from the center to left to then to the right. Okay, let's do it. Here it is. We're going to put a little camera shake on. This is a default one that comes with Black Eye. It's noise-based. We're actually working on a way cooler system. But this is good to get you started. A bit of noise. All right. Here we go. Let's press press play and see what happens. So is this exactly the same? No, it's not. But it's pretty good for two minutes and seven keyframes. Wow. Oh, here's still here. Look at this. No roll. I just turned the roll off on the camera. Look at that pillow-y damping. We spent so long getting that damping stuff right to feel really buttery and smooth. You might also want to bake this camera down. Procedural cameras are great and fast to work with. But sometimes once you're close and you like it, you want to lock it down. So it's consistent every time. So drop a camera in the scene. You link it to the Black Eye camera. Bring it in a sequencer. Hit bake. Boom. There's your keyframes. Thanks for watching. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram\frame_000.jpg


---

## Structured Notes

### Core Technique
Recreate the Force Awakens Millennium Falcon flyby shot in ~2 minutes with only 7 keyframes. BEC workflow: Follow (Subject Locked) + Look At for procedural tracking; key frame only Screen Space Composition (where ship appears on screen) and a few Roll keys; add noise-based camera shake; optionally bake to static CineCameraActor for pipeline consistency.

### Summary
2m24s Black Eye Technologies tutorial recreating a famous Force Awakens Millennium Falcon shot with minimal keyframes. Assets from Fab. Process: quick animation on the Millennium Falcon → drop BEC camera → Follow mode: Subject Locked (camera follows subject's all transforms) → Look At → fine tune distance and damping → small amount of width/distance damping. Key frame only: Screen Space Composition (ship on screen at center → left → right = 3 composition keys) + Roll (minimal) = 7 total keyframes. Camera shake: attach noise profile from Black Eye content → Duration=0 (infinite). Compare with/without roll. Bake: drop static CineCameraActor → link to BEC camera → Sequencer → Bake → all procedural motion becomes standard keyframes for pipeline export.

### Key Steps
1. Get Millennium Falcon (or any vehicle) from Fab; create quick animation in Sequencer
2. Drop BEC **Simple Look At** camera → set Follow mode: **Subject Locked** (camera follows subject's position, rotation, and all transforms)
3. Enable **Look At** → pick Falcon → camera tracks it
4. Set follow distance (close = more damping mojo); add **distance damping** for buttery movement
5. Enable **debug** to see the look-at point and composition markers
6. In Sequencer: add **Subject Screen Space Position track** → keyframe where the Falcon should appear on screen:
   - Frame 0: center screen
   - Mid-flight: left screen
   - End: right screen
   → Only 3-4 composition keyframes; BEC handles all rotation math
7. Add a few **Roll keyframes** (minimal) for ship banking feel
8. Add **Camera Shake track** → drag BEC noise profile (from Black Eye content) → set Duration = 0 (infinite); tune amplitude
9. Toggle Roll off in BEC settings to test "pillow-y damping" effect without roll
10. **Optional bake**: drop standard CineCameraActor → link to BEC camera → add to Sequencer → hit Bake → all motion baked to dense keyframes for consistent/pipeline-safe playback

### UE Systems / Blueprints / Settings
- **Subject Locked** (Follow mode) — camera follows all transforms of subject (position + rotation + roll); tightest follow mode
- **Screen Space Composition track** — Sequencer track; X/Y position of subject on screen; key frame desired framing per moment; BEC handles camera rotation to achieve it
- **Distance Damping / Width Damping** — separate positional damping axes; affects how the camera's offset distance feels ("soft" vs "rigid")
- **Camera Shake track** (BEC) — add noise profile from Black Eye content (show plugin content to find); Duration=0 = infinite; tune amplitude and frequency; noise-based (acknowledged as limited; better system coming)
- **Camera Bake** — link BEC camera to a destination CineCameraActor → Sequencer → Bake → produces dense standard keyframes; good for: (a) locking down a good take, (b) DCC export, (c) render layers

### Difficulty
Beginner. Demonstrates just how few keyframes are needed with BEC's procedural system.

### UE Version
UE5 (Black Eye Cameras)

### Tags
black-eye-cameras, cinematics, spaceship, follow, composition, keyframes, camera-shake, bake, workflow

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:14] tutorials/frames/unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram/frame_000.jpg
- [0:43] tutorials/frames/unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram/frame_001.jpg
- [1:19] tutorials/frames/unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram/frame_002.jpg
- [1:55] tutorials/frames/unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram/frame_003.jpg

## Related Entries
- `unreal-engine-black-eye-cameras-bake-down-cam-anims.md` — full camera bake tutorial; DCC round-trip
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — similar Screen Space Composition keyframing for vehicle shots
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — BEC full system overview
