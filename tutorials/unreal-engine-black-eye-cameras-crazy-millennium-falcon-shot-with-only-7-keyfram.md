---
title: Unreal Engine Black Eye Cameras: Crazy Millennium Falcon shot with only 7 keyframes
source: YouTube
url: https://www.youtube.com/watch?v=7jNy5snGOJM
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, vehicles, beginner]
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
**Transcript:** This amazing shot from the Force Awakens. Let's do it in Black Eye with only 7 Q frames in a couple of minutes. Let's go. You might have seen this video from Merit on YouTube. It breaks it down. It showed the stabilization. This was the inspiration. Okay, so I got a Millennium Falcon in a desert from Fab. There are links to that below. Did a real quick animation. Drop the Black Eye camera in the scene. Set it to follow. Put the distance. How to kind of close because we want this bringingness of the camera damping to give it some mojo. Let's get the angle. Yeah, so a little bit more wide damping. That's the distance damping on the camera. Then just set the look at the Millennium Falcon. Very simple. There's the screen space composition. We're going to keyframe that. I'll show you that in a sec. Then a bit of damping on the composer. Okay, then this is the follow. We've got the follow mode to be subject locked. That means we're listening to all of the follow transforms. Then here's the keyframes. Very few. Some on the roll. This is the screen space composition keyframes. Right now we're in the center. I drag the playhead over. Now we're saying, be on the left of the screen. This is s...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-crazy-millennium-falcon-shot-with-only-7-keyfram\frame_000.jpg


---

## Structured Notes

### Core Technique
Recreating the Force Awakens Millennium Falcon shot with 7 keyframes in Black Eye: Follow in subject-locked mode + LookAt + 3-4 Screen Space Position keyframes + roll keyframes for cinematic banking feel.

### Summary
2.5-minute tutorial recreating a famous Star Wars: The Force Awakens Millennium Falcon tracking shot using only 7 keyframes in Black Eye. The technique: Follow the ship in "subject locked" mode (camera transforms tied to all subject transforms), LookAt the ship with damping, then keyframe screen-space composition (ship center → left of screen → right) and camera roll. The camera feels heavy and cinematic because the damping on the Follow gives it mass, and the composition keyframes handle all the reframing.

### Key Steps
1. **Animate the Millennium Falcon** — quick animation pass on the subject (simple keyframes). Acquire Falcon asset from Fab.
2. **Drop Black Eye camera + set Follow** — set Follow mode to "subject locked" (camera subscribes to all subject transforms including roll/pitch). Set follow distance appropriately close for the "bringingness" of the damping.
3. **Set distance damping** — adds camera mass; you feel the ship's weight because the camera lags slightly behind the ship's motion.
4. **Set LookAt on the Falcon** — adds rotational tracking; camera always points at ship.
5. **Tune composition damping** — adds slight lag on the screen-space position target.
6. **Add Screen Space Position keyframes** — only 3-4 keyframes: ship starts at center, moves left of screen, then right. Black Eye interpolates smoothly between compositions.
7. **Add roll keyframes** — camera banks slightly with the ship's movement for cinematic feel.
8. **Total: 7 keyframes** — roll keys + screen space position keys = roughly 7 total, yet the result looks like a dense hand-animated camera move.

### UE Systems / Blueprints / Settings
- **Follow (subject locked mode)** — camera position locked to all subject transforms (translation + rotation); camera moves with the ship including when it banks
- **Distance damping** — controls lag between camera and subject position; gives mass/weight to the camera
- **LookAt** — rotational tracking; camera always points at ship
- **Composition damping** — lag on screen-space target for cinematic smoothness
- **Screen Space Position** — Sequencer keyframes; target position on screen (center → left → right)
- **Roll keyframes** — camera rotation channel in Sequencer; bank with ship motion

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1; Fab used for asset acquisition)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#vehicles` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Follow Vehicles + Keyframe Composition sections
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — detailed vehicle cinematic rigs with same technique
