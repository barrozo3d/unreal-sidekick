---
title: Unreal Engine | Black Eye Cameras: Rapid shot prototyping
source: YouTube
url: https://www.youtube.com/watch?v=jhNjKV70uzk
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, beginner]
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
**Transcript:** Hey, this is Adam from Black Eye Cameras. Let's talk about rapid-shot prototyping. Okay, here's a look at and a follow camera that I'm tweaking the composition a little bit. Once it's set up, you can move the camera around and it's still going to look at and follow whatever you've got it set to. So you can see it's dynamically zooming, cameras moving and it's rotating, compensating for the players coming apart here. And then you can just grab it and you can move it around and there's no keyframes. And just try out different shot ideas. Okay, that's stacking a little bit. Let's move it and it works still because it knows how far away you want to be and it knows what the composition you want. Let's try it from the other side. Maybe the zoom's pumping a little bit and you can dampen that just a hair. Okay, let's try out another idea. We've got this cube in the world and we're gonna stick the camera onto it. Just click it. It's inside. So let's do the offset to pull the camera out. Okay, the camera's on the cube. You can dampen that too. Now we're gonna look at the two people and you just click them and now the camera's looking the two people. So you've got this track shot where the ca...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-rapid-shot-prototyping\frame_000.jpg


---

## Structured Notes

### Core Technique
Rapid shot prototyping with Black Eye: move a camera freely in the scene without keyframes to explore angles and follow setups; the camera always tracks its subject regardless of where you drag it, enabling fast idea exploration.

### Summary
2.5-minute workflow tip video. Black Eye cameras track their subjects regardless of camera position — you can grab and move the camera anywhere in the scene and it will re-compose in real time. No keyframes needed to prototype shots. Also demonstrates attaching a camera to a world object (cube) as the Follow target, then pointing LookAt at two characters for a creative dolly rig. Demonstrates: live repositioning, damping adjustment on the fly, attaching to world objects as non-standard follow subjects.

### Key Steps
1. **Set up LookAt + Follow** — configure camera as normal (bone tracking, follow on subject).
2. **Prototype by moving camera** — grab the camera and drag it anywhere. It re-composes and follows automatically. No keyframes needed.
3. **Tune damping live** — if zoom is pumping, dampen it slightly while repositioning.
4. **Attach to world object** — click Follow → pick any object in scene (cube, prop). Camera snaps to 300-unit offset from that object. Use Follow Offset to pull camera out if it clips inside.
5. **LookAt two characters** — while following the world object, add multi-subject LookAt on two characters. Camera is now a moving platform that always looks at the characters.
6. **Try ideas without keyframes** — test camera angles quickly; when satisfied, add Sequencer for polished version.

### UE Systems / Blueprints / Settings
- **LookAt** — tracks subject during live repositioning; always recomposes
- **Follow** — can follow any actor (characters, props, world objects); 300-unit default offset
- **Follow Offset** — pull camera out if Follow target is inside an object
- **Zoom damping** — reduces pumping if Dynamic FOV is reacting too aggressively during live repositioning
- **No-keyframe prototyping** — core workflow: drag camera → inspect shot → no commit needed until satisfied

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — LookAt + Follow setup in detail
- [[unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators]] — director workflow using multiple cameras similarly
