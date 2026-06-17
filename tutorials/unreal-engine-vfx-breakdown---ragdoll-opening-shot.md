---
title: Unreal Engine VFX Breakdown - Ragdoll Opening Shot
source: YouTube
url: https://www.youtube.com/watch?v=rzMRSDxg33Q
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: ["VFX breakdown", "ragdoll", "green screen", "blue screen", "camera tracking", "media texture", "virtual production", "Composure", "DaVinci Resolve", "Fusion", "digital double", "filmmaking", "Fab assets"]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-vfx-breakdown---ragdoll-opening-shot/
frame_count: 12
---

# Unreal Engine VFX Breakdown - Ragdoll Opening Shot

**Source:** [YouTube](https://www.youtube.com/watch?v=rzMRSDxg33Q)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 2m52s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Virtual Production in Unreal Engine Overview [0:00]
**Transcript:** So in this video, in this video, I'm going to show you how I took this guy and then I  put him on a card in 3D inside of Unreal and then put him into this environment.  So first thing is I took me and I shot me against a blue screen and then I had a camera,

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_000.jpg

### Overview of VFX pipeline [0:17]
**Transcript:** it's called a second shooter and it's like a slider and if you watch my other videos,  it's one of my favourite things.  So you get this line of kind of like orbiting move, it makes it less boring than right now,

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_001.jpg

### Using Second Shooter Camera Slider [0:30]
**Transcript:** I'm just shot against a solid locked off camera so it's not too exciting.  And then I also put me on a treadmill so because I wanted to kind of push me along this  environment because my room's not very big.  And then I brought that into DaVinci Resolve to do my extraction.

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_002.jpg

### Green Screen extraction in Davinci Resolve [0:45]
**Transcript:** So an extraction is basically cutting out anything that's blue and replacing it with black  and anything that's white is something that will be solid and will actually see inside  of Unreal Engine.  And once I've got my blue screen, I then do a camera match move so basically track where

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_003.jpg

### Davinci Resolve Studio Camera Tracker [1:00]
**Transcript:** the camera is moving and then I take the plate and the camera and bring this back into  Unreal Engine and I put them on a card on a camera.  So you've got a camera with a card on the end and they're all kind of locked together.

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_004.jpg

### Ingest Footage and Matte into Unreal Engine as Media Texture [1:10]
**Transcript:** And then because he's walking we kind of pushed the whole thing forward in 3D space until

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_005.jpg

### The Illusion of Travel using a Cheap Treadmill [1:18]
**Transcript:** it felt like his feet were in sync with the distance he was travelling.  The environment I got from the fab store and this one's called legendary caves and dungeons.  And it's excellent.  And then for the swinging logs those are a pack again from fab called animated traps.

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_006.jpg

### Fab Assets for Environment [1:30]
**Transcript:** One of the things I enjoy most about compositing in real time is the fact that you can move  the environment and the lights to fit your plate as best as you can.  So here to match the lighting I can just move around the lights in the environment so I can

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_007.jpg

### Virtual Location Scouting and Real-time lighting [1:48]
**Transcript:** move this about and kind of get it to look good until the plates kind of sitting better  to the environment.  The next thing was to bring in my digital double and I've applied some ragdoll physics to  that and I'm assuming that you've watched the last video about ragdoll physics and I had

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_008.jpg

### Davinci Fusion Paint [2:05]
**Transcript:** to do it yourself.  Now once I've rendered it I brought this into DaVinci Fusion.  I added a paint node to blend together where I turn off the live action and turn on the digital  double and then I brought it into the colour page and used the film look treatment and give  it some noise and relation and all sort of like nice, singing, compy type things.

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_009.jpg

### Davinci Studio Film Look Emulation Node [2:20]
**Transcript:** So that's an overview of what I did for this video.  If you want to kind of like get more nerdy and like actually see the files and how I do  my extractions then watch these videos where I go over that whole process and then eventually

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_010.jpg

### Video to Watch for Learning my VFX Pipeline in Detail [2:30]
**Transcript:** I'm going to update it again and kind of go over, we've got some better way to do contact  shadows and things like that now.  But unreal keep changing so hopefully the next release there might be some more exciting  tools that we can use for our Visual Effects pipeline and unreal woo!  Okay, see you on the next one, thank you, bye!

**Frame:** tutorials\frames\unreal-engine-vfx-breakdown---ragdoll-opening-shot\frame_011.jpg


---

## Structured Notes

### Core Technique
A 3-minute VFX breakdown of the ragdoll opening shot from Dean Yurke's film: blue screen capture on a treadmill with a slider camera, DaVinci Resolve extraction and camera tracking, bringing the live action plate into Unreal Engine as a Media Texture on a card, matching environment/lighting, adding a ragdoll digital double, rendering, and finishing in DaVinci Fusion.

### Summary
This is a VFX breakdown / making-of video (not a step-by-step tutorial) showing Dean Yurke's full virtual production pipeline applied to a specific opening shot where he walks on a beam and falls via ragdoll physics. He filmed himself against a blue screen on a treadmill (to simulate traveling through an environment) with a camera slider ("second shooter") for an orbiting move. The footage was brought into DaVinci Resolve for extraction and 3D camera tracking (DaVinci Studio). The tracked plate and camera were imported into Unreal Engine, and the live action was placed on a media texture card locked to the tracked camera, with world-space depth adjustment for foot contact. A Fab marketplace "Legendary Caves and Dungeons" environment was used, plus "Animated Traps" (swinging logs). The digital double had ragdoll physics applied from the tutorial in the companion video. After rendering, DaVinci Fusion was used to paint out the transition between live action and digital double, and the DaVinci Resolve Color Page Film Look treatment added grain and color for the final look.

### Key Steps
1. Film subject against blue screen on a treadmill; use a camera slider for an orbiting or sliding camera move.
2. Import footage into DaVinci Resolve; perform blue screen extraction to create a matte/EXR sequence.
3. Use DaVinci Resolve Studio's 3D Camera Tracker on the plate; export FBX with tracked camera.
4. Import FBX into Unreal Engine (File > Import Into Level); put the media texture plate on a card locked to the tracked camera.
5. Translate the card/camera forward in 3D space until the subject's feet appear grounded.
6. Download and place Fab marketplace environment assets (e.g., Legendary Caves and Dungeons, Animated Traps).
7. Move environment lights to match plate lighting; virtual scout to find the best camera position.
8. Add a digital double character with ragdoll physics applied (see companion ragdoll tutorial); blend live action to digital double at the fall point.
9. Render out of Unreal Engine.
10. In DaVinci Fusion: use Paint node to blend between live action and digital double at the cut point.
11. In DaVinci Resolve Color Page: apply Film Look treatment; add grain and color correction.

### UE Systems / Blueprints / Settings
- Media Texture / Media Player on plane card (live action plate)
- Cine Camera Actor (matched to DaVinci tracked camera FBX)
- File > Import Into Level (tracked camera FBX)
- Skeletal Mesh with Ragdoll Physics Asset (digital double)
- Fab marketplace assets: Legendary Caves and Dungeons, Animated Traps (external)
- DaVinci Resolve Studio: Blue Screen extraction, 3D Camera Tracker, Film Look treatment, Color Page (external)
- DaVinci Fusion: Paint node (external)

### Difficulty
Intermediate

### UE Version
5.x (no specific sub-version)

### Tags
VFX breakdown, ragdoll, green screen, blue screen, camera tracking, media texture, virtual production, Composure, DaVinci Resolve, Fusion, digital double, filmmaking, Fab assets

---

## Related Entries
- `beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in.md` — the ragdoll physics tutorial that produced the digital double used in this shot
- `green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin.md` — more advanced version of the camera projection + green screen workflow shown here
- `green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor.md` — the detailed DaVinci camera tracking and extraction pipeline used in this breakdown
