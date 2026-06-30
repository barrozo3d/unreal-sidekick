---
title: Unreal Engine Black Eye Cameras: Cam Switcher Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=ub1_ET0LLJc
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, camera-switcher, multi-camera, live-events, follow, look-at, esports, workflow, broadcast]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-cam-switcher-tutorial/
frame_count: 6
---

# Unreal Engine Black Eye Cameras: Cam Switcher Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=ub1_ET0LLJc)
**Author:** Black Eye Technologies
**Duration:** 2m59s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** New in BlackIron.1.7 is a very cool feature for the camera switcher.  Easily switch between your army of cameras which are dynamically following and framing  and composing whatever is happening.  Incredibly powerful for bulk app, live events, eSports.  Okay here's how to do it, this is our scene.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_000.jpg

### Adding the Switcher [0:15]
**Transcript:** Well these guys look like they just came back from the open pasta bar at lunch and we  got a rando singer perfect.  So drag the camera switcher actor into your project.  To your level and then you can see here under cameras we've got this array that you generate.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_001.jpg

### Configuring Switcher [0:30]
**Transcript:** So you pick a button, you pick a camera.  You can you can click that keyboard button and then actually just tap the keyboard and  you bind them.  So these are some cameras that have already gotten the scene set up but let's make another

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_002.jpg

### Creating Cameras [0:46]
**Transcript:** one.  So I'm just going to drop a blackI camera in the scene.  We'll make it look at the character.  Just the positioning a little bit.  Let's make this one look at the head.  So we hit the look at type in the headbone, turn off the actor bound so it's looking now  just at the headbone.  And you know we can put it wherever we want.  Just a composition.  Sure.  Fix that.  Just there we go.  Okay let's duplicate this and we're going to make another camera.  This is this one.  Let's make this one follow and look at the whole person.  So we're going to do a dynamic FOV.  We're going to adjust the screen size so the camera will automatically if we need to  keep the character this size on the screen.  And then we're going to follow it.  So when you click follow and you click the character we just do an offset at 300 but you  can just grab the camera and move it.  And that's going to maintain the camera's subject relationship.  A little bit of damping in there.  Let's check it out.  There we go.  Okay this camera is following the character.  I'm doing some procedural aiming composition.  Let's check this.  Head camera not too bad.  Okay great.  We got some stuff here.  Let's go.  So let's add those two cameras to the camera switcher.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_003.jpg

### Running Switcher [2:08]
**Transcript:** Save it.  It play.  Wait what's happening.  Well of course you've got the quick one your timeline that's going to override it.  Make sure you don't have a clip on your camera cuts.  Track.  Here we go.  And look at this.  You're switching.  And you can switch between cameras which are set up for character one, character three,  just head shots, framing everybody.  And if you want to have the camera print out what it is.  Do a little text ring.  You can just type it in here.  Just add that component.  This is a super fast way.  Switching cameras.  It's a camera switcher.  One at one, that's seven.  Black guy.  Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_004.jpg

### Sneak Peek [2:53]
**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_005.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.1.7 Camera Switcher actor — live keyboard-driven multi-camera switching during play. Drag the Camera Switcher into the level, add BEC cameras to its array, bind each to a keyboard key, and switch between them live during play. Use case: live events, esports broadcast, mocap sessions, rapid cinematic prototyping.

### Summary
3m Camera Switcher tutorial (Adam, Black Eye v1.1.7). Demonstrates: drag Camera Switcher actor into level → configure Cameras array → bind keyboard buttons to each camera → run in PIE and press keys to switch. Camera setup reminder: Look At with bone name + Actor Bounds off (tracks bone not actor center); Follow with dynamic FOV + screen-size setting + position offset (300) + damping. Gotcha: if Camera Cuts track has a clip, it overrides the switcher — must clear the Camera Cuts track. Optional: add Text component to Switcher actor to display current camera name on screen. Use cases: esports, live events, rapid shot prototyping, mocap monitoring.

### Key Steps
**Setup:**
1. Drag **Camera Switcher** actor from Black Eye content folder into scene
2. Details panel → **Cameras** array → click + to add entry → pick a Black Eye camera; click + again for next camera; etc.
3. For each camera entry: click the keyboard button → press desired key on keyboard → binding saved; key switches to that camera during play

**Creating cameras to add:**
4. Drag any Black Eye camera into scene → configure:
   - **Head camera**: Look At → type headbone name (e.g., "head") → disable **Actor Bounds** (looks at bone point, not bounding box)
   - **Follow camera**: Follow → pick character → offset 300 (or move camera manually); enable Dynamic FOV → set Screen Size to desired character size %; add damping
5. Duplicate cameras to quickly create variations

**Add to Switcher:**
6. Open Camera Switcher → Cameras array → add entries → pick each configured BEC camera

**Run and switch:**
7. Remove any clip from **Camera Cuts track** in Sequencer (if present — it will override the switcher)
8. Press Play → press the bound keyboard keys to switch between cameras live
9. Camera transitions are live — each camera continues its procedural tracking, compositing, and zoom during switch

**Camera name display (optional):**
10. Select Camera Switcher → Add Component → **Text Render** (or text component) → type camera name → appears on screen during play

### UE Systems / Blueprints / Settings
- **Camera Switcher** (Black Eye v1.1.7+) — actor; array of BEC cameras + keyboard bindings; keyboard press during PIE switches active camera; available from Black Eye content folder
- **Cameras array** — list of BEC cameras registered with the switcher; each entry has a keyboard button binding
- **Look At type with bone name** — targets a specific skeleton bone instead of actor center; must disable **Actor Bounds** option on the Look At module
- **Actor Bounds** — when enabled on Look At, camera tracks the actor's bounding box center; disable to track a specific bone
- **Dynamic FOV** + **Screen Size** — Follow module; automatically adjusts zoom to keep character at a consistent % of screen; works with Camera Switcher
- **Camera Cuts track conflict** — any clip on the Camera Cuts track overrides all camera switching; must be empty for Camera Switcher to function
- **Text component** — add to Camera Switcher actor; renders text (camera name) in the viewport during play for operator reference

### Difficulty
Beginner. 3-step setup (drag, configure, bind). Great for live/broadcast workflows.

### UE Version
UE5 (Black Eye v1.1.7)

### Tags
black-eye-cameras, camera-switcher, multi-camera, live-events, follow, look-at, esports, workflow, broadcast

---

## Related Entries
- `unreal-engine-black-eye-cameras-v117-switcher-pilot.md` — related v1.1.7 Switcher Pilot feature
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — full BEC plugin overview
- `unreal-engine-black-eye-cameras-rapid-shot-prototyping.md` — rapid camera prototyping workflow
