---
title: Unreal Engine | Black Eye Cameras: Rapid shot prototyping
source: YouTube
url: https://www.youtube.com/watch?v=jhNjKV70uzk
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, prototyping, workflow, follow, look-at, pov, multi-subject, cinematics, technique]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-rapid-shot-prototyping/
frame_count: 4
---

# Unreal Engine | Black Eye Cameras: Rapid shot prototyping

**Source:** [YouTube](https://www.youtube.com/watch?v=jhNjKV70uzk)
**Author:** Black Eye Technologies
**Duration:** 2m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, this is Adam from Black Eye Cameras. Let's talk about rapid-shot prototyping. Okay, here's a look at and a follow camera that I'm tweaking the composition a little bit. Once it's set up, you can move the camera around and it's still going to look at and follow whatever you've got it set to. So you can see it's dynamically zooming, cameras moving and it's rotating, compensating for the players coming apart here. And then you can just grab it and you can move it around and there's no keyframes. And just try out different shot ideas. Okay, that's stacking a little bit. Let's move it and it works still because it knows how far away you want to be and it knows what the composition you want. Let's try it from the other side. Maybe the zoom's pumping a little bit and you can dampen that just a hair. Okay, let's try out another idea. We've got this cube in the world and we're gonna stick the camera onto it. Just click it. It's inside. So let's do the offset to pull the camera out. Okay, the camera's on the cube. You can dampen that too. Now we're gonna look at the two people and you just click them and now the camera's looking the two people. So you've got this track shot where the camera's following a thing with per-axis damping and then it's composing on the two and it's dynamically rotating and zooming. Here's another crazy idea. Let's put the camera inside. Let's follow the player's head. So just click on the player, type in head. Then we wanna look at the other player, click on the other player, type in their head. Boom. We're looking at their head, shots a little tight. We'll back the framing off. And now you've got this camera that's inside one player's head looking at another. Let's move it forward a little bit. We're just clipping. What I want you to see here is look at the weight of the camera that there's some, like a viscosity to it that you can adjust, but we spent so long getting that to feel right. And just for showing the speed of it, let's flip it around. Camera on the other side. Let's look at the other person's head. Just click them, adjust the offset for them. Bam. Look how fast it is. The black eye you can set stuff up so quickly. Try out crazy ideas. Do cool stuff. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-rapid-shot-prototyping\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye Cameras rapid prototyping concept demo: set up Look At + Follow, then simply drag the camera anywhere — no keyframes needed, the shot adapts instantly. Three exotic shot types shown: (1) mount camera on a tracked prop (cube following a path); (2) mount camera inside a character's head (POV-style); (3) flip instantly to the other character. Core message: BEC enables pure directorial ideation without technical overhead.

### Summary
2m17s Adam (Black Eye Technologies) rapid shot prototyping demo. Shows how quickly you can try crazy ideas with BEC by removing keyframe overhead. Scenario 1: Look At + Follow camera dragged to various positions in scene — always maintains composition because it knows desired screen size and look-at target. Scenario 2: mount camera on a moving cube → Follow the cube → Look At two characters → tracking prop shot with per-axis damping. Scenario 3: Follow player head bone → Look At other player's head bone → first-person or near-POV camera with viscous weight. Instantly flip to opposite camera. Main value: iteration speed. "Try out crazy ideas" is the entire point.

### Key Steps
1. Set up basic Look At + Follow camera (see overview tutorial)
2. **Drag camera anywhere in scene** → composition auto-adjusts; no keyframes needed → instant shot test
3. **Mount on prop**: select any moving prop in scene → set Follow target = that prop; set Look At = two characters → camera rides the prop while compositing on actors

4. **POV-style shot**: Follow → character → **subject: head bone** → camera follows character's head bone position; Look At → other character → **bone: head** → camera inside first character's head looking at other's head
5. Adjust Follow offset to position camera just ahead of head for proper POV
6. **Flip sides**: swap Follow and Look At targets → instant reverse angle shot

**Tuning:**
7. Per-axis damping on Follow → smooth out camera motion while maintaining subject tracking
8. Zoom damping on Look At → prevents pumping when subjects shift size

### UE Systems / Blueprints / Settings
- **Drag without keyframes** — BEC camera maintains desired composition regardless of physical camera position; drag = instant shot test
- **Follow target: arbitrary prop** — BEC Follow can follow any actor, not just characters; use for dollies-on-track, crane arms, moving vehicles as camera mounts
- **Follow bone targeting** — set Follow subject → actor → type bone name (e.g., "head") → camera physically follows that bone's 3D position; enables POV-style shot locked to character's eye level
- **Look At bone targeting** — same but for rotation; look at specific bone on another character
- **Per-axis damping** — tune separately for left/right (yaw) vs. up/down (pitch) on Follow module; enables different weights for different motion axes
- **Instant reverse angle** — swap Follow and Look At targets → immediate opposite camera without new keyframes

### Difficulty
Beginner. The whole point is to remove setup friction.

### UE Version
UE5 (Black Eye Cameras)

### Tags
black-eye-cameras, prototyping, workflow, follow, look-at, pov, multi-subject, cinematics, technique

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:14] tutorials/frames/unreal-engine-black-eye-cameras-rapid-shot-prototyping/frame_000.jpg
- [0:41] tutorials/frames/unreal-engine-black-eye-cameras-rapid-shot-prototyping/frame_001.jpg
- [1:15] tutorials/frames/unreal-engine-black-eye-cameras-rapid-shot-prototyping/frame_002.jpg
- [1:50] tutorials/frames/unreal-engine-black-eye-cameras-rapid-shot-prototyping/frame_003.jpg

## Related Entries
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — full BEC system overview; all modules explained
- `unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial.md` — multi-subject follow and look-at in practice
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — Follow on vehicle + cinematic composition workflow
