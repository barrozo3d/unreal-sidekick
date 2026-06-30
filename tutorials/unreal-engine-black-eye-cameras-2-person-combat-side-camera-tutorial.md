---
title: Unreal Engine | Black Eye Cameras: 2 person combat side camera tutorial
source: YouTube
url: https://www.youtube.com/watch?v=W4UZ4-vLxxw
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, camera, multi-subject, follow, look-at, automatic-zoom, cinematics, gameplay, damping, workflow]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial/
frame_count: 4
---

# Unreal Engine | Black Eye Cameras: 2 person combat side camera tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=W4UZ4-vLxxw)
**Author:** Black Eye Technologies
**Duration:** 4m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, I'm Adam from Black Eye. Let's do a quick two-character camera. That's going to attract them from the side. Ooh, looks like one guy's is on me. Alright, let's jump into it. So you're going to want to open your content browser. Make sure your engine plug-ins folders turned on so you can see everything. You can come down to the Black Eye folder. You can see we've got a bunch of cameras there. Grab the simple look at. Jump it in your scene. Now when you select that, you can see there's a few things going on. We've got a follow and a look at. We want to follow. So pick that. We're going to pick multiple subjects. I'll turn that on and let's add a subject. Here's ready for one. Now we get two. Open them up. You just get the eyedropper and you just pick them left person, right person, cameras now. In between those two, you can see the red line. That's the showing that we're tracking those two people. And you can punch in offset values or you can just grab the camera and move it to wherever you want. So we're going to do the latter. So we're just going to pick it up and move it back. Now you can see the camera is not looking at the character. So let's fix that. So open the look at. Add. So for two, same thing. You can see the camera is spinning around and grab the right guy and think obviously the lens is not great. So let's put on a automatic zoom. You can set the lens, but here we're doing an automatic zoom, which is kind of fun. And we're just going to drag the camera onto the camera cuts track. So you can see the blue cubes for each person, the white cube, which is the entire frame and the camera is going to zoom to keep the entire frame on screen. Okay. Let's pick the follow. Now we're going to be stamping on there. That's now decoupling the camera movement from the subjects. We're going to go lots too. That's a lot. But you'll see, the camera is going to be really heavy. It's very viscous. Now you can see the camera is moving with them. It's turning. It's rotating to keep them in frame. It's translating to keep them in frame. So open another viewport and it's zooming to keep them in frame. So we get the setup in what? You know, 20 seconds. And if you move the camera back, it's going to zoom to keep everything framed based on that desired subject viewport size. That's the white box. So blue box for a character left, blue box for character right, white blocks is the product of the two in the cameras now moving, zooming and rotating and tracking. You're going to have to set up and just in a couple of seconds. It's really fast. I like to put a little more FOV damping on there. It's going to slow the zoom down and make it feel a little bit more broadcast, a little less erratic. But sometimes you want it cranked up. You can see now that it feels a bit more like a camera person because the camera had to catch up for a second. OK, so what was that? Like two minutes to get a camera to dynamically move, rotate, compose, zoom on two things with no keyframes. It's really fast. Look at that. I'm just going to fix that damping a little bit to a bit too much. Just go down to one. Change the viewport size. Just get a better frame on that. Boom. Now whatever these two innocent human intervals on me do, the camera is going to be moving and framing. It's a great for like mocap or if you're just wanting to track a whole bunch of stuff, live variable performance and have your cameras figured out. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye Cameras plugin — 2-person side-camera setup using **Simple Look At** camera with **Multiple Subjects** on both Follow and Look At modules. No keyframes: camera automatically moves, rotates, and zooms to keep both subjects framed. Key controls: blue cube = per-subject frame target; white cube = combined frame; FOV Damping = zoom smoothness; Follow Damping = movement viscosity.

### Summary
4m10s Black Eye Technologies tutorial (Adam) — 2-character combat side-camera in ~30 seconds, zero keyframes. Uses the Simple Look At camera prefab from the Black Eye folder. Follow module → Multiple Subjects → eyedropper select both characters → red tracking line appears. Look At module → same two subjects. Enable Automatic Zoom → camera zooms to keep white cube (combined subject bounding box) in frame. Drag camera position backward manually. Add to Camera Cuts track. Adjust FOV Damping (1 = moderate broadcast feel; higher = more erratic/reactive). Follow Damping (viscosity) set high for heavy, "catching-up" camera feel. Final result: dynamic multi-subject camera that tracks position, rotation, and zoom simultaneously.

### Key Steps
1. Content Browser → Black Eye folder → enable **Show Plugin Content** if folder not visible → drag **Simple Look At** camera into scene
2. Select camera → Details panel: **Follow** module → enable **Multiple Subjects** → click **Add** → use eyedropper to pick Subject 1 (left character); Add again → pick Subject 2 (right character); red tracking line connects both
3. Move camera manually to desired side position (drag in viewport)
4. **Look At** module → Add → eyedropper → left character; Add → right character → camera rotates to face both
5. Enable **Automatic Zoom** → camera will auto-zoom to keep white cube (combined frame) visible at all times
6. Drag camera onto **Camera Cuts track** in Sequencer to activate it for rendering/preview
7. Adjust **FOV Damping** (zoom speed): lower = snappier; ~1 = broadcast/smooth; higher = erratic/reactive
8. Adjust **Follow Damping** (movement viscosity): "lots" = heavy, camera catches up with a lag; lower = immediate

**Reading the debug visualization:**
- **Blue cubes** (one per character) = each subject's desired frame box
- **White cube** = combined desired frame for both characters; camera zooms to fit this

### UE Systems / Blueprints / Settings
- **Black Eye Cameras plugin** (by Black Eye Technologies) — procedural camera system; no-keyframe follow/look-at/zoom cameras; plugin installs into UE5 content browser under "Black Eye" folder
- **Simple Look At** — single camera prefab with configurable Follow + Look At modules; supports single or multiple subjects
- **Follow module** — handles camera position; Multiple Subjects mode; eyedropper subject selection; Damping (viscosity = movement lag/smoothness)
- **Look At module** — handles camera rotation; separate subject list from Follow (can track different subjects); Add per subject
- **Multiple Subjects** — enables Follow or Look At to track more than one actor simultaneously; each subject gets a blue bounding cube in debug view
- **Automatic Zoom** — automatically adjusts FOV/zoom to keep white box (combined subject frame) in the camera's viewport; replaces manual focal length keyframing
- **FOV Damping** — controls speed of zoom changes; low (1) = broadcast/smooth; high = erratic/live-action feel
- **Follow Damping** — controls position/rotation momentum; high = heavy, lagging camera feel; low = immediate tracking
- **Camera Cuts track** — add camera to Sequencer Camera Cuts track to activate it as the active camera for rendering

### Difficulty
Beginner. 30-second setup with no keyframes required.

### UE Version
UE5 (Black Eye Cameras plugin)

### Tags
black-eye-cameras, camera, multi-subject, follow, look-at, automatic-zoom, cinematics, gameplay, damping, workflow

---

## Related Entries
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — full BEC plugin overview; all camera types
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — BEC beginner intro
- `unreal-engine-black-eye-cameras-multiple-targets-on-a-character.md` — related multi-target configuration
- `unreal-engine-black-eye-cameras-multiple-follow-and-look-at-modules.md` — advanced multi-module setup
