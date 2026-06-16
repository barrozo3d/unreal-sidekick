---
title: Unreal Engine Black Eye Cameras: Cam Switcher Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=ub1_ET0LLJc
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.1.7
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, esports, live-events, mocap, beginner]
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
**Transcript:** one.  So I'm just going to drop a blackI camera in the scene.  We'll make it look at the character.  Just the positioning a little bit.  Let's make this one look at the head.  So we hit the look at type in the headbone, turn off the actor bound so it's looking now  just at the headbone.  And you know we can put it wherever we want.  Just a composition.  Sure.  Fix that.  Just there we go.  Okay let's duplicate this and we're going to make another camera.  This is this one.  Let's make this one follow and look at the whole person.  So we're going to do a dynamic FOV.  We're going to adjust the screen size so the camera will automatically if we need to  keep the character this size on the screen.  And then we're going to follow it.  So when you click follow and you click the character we just do an offset at 300 but you  can just grab the camera and move it.  And that's going to maintain the camera's subject relationship.  A little bit of damping in there.  Let's check it out.  There we go.  Okay this camera is following the character.  I'm doing some procedural aiming composition.  Let's check this.  Head camera not too bad.  Okay great.  We got some stuff here.  Let's go.  So let's...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_003.jpg

### Running Switcher [2:08]
**Transcript:** Save it.  It play.  Wait what's happening.  Well of course you've got the quick one your timeline that's going to override it.  Make sure you don't have a clip on your camera cuts.  Track.  Here we go.  And look at this.  You're switching.  And you can switch between cameras which are set up for character one, character three,  just head shots, framing everybody.  And if you want to have the camera print out what it is.  Do a little text ring.  You can just type it in here.  Just add that component.  This is a super fast way.  Switching cameras.  It's a camera switcher.  One at one, that's seven.  Black guy.  Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_004.jpg

### Sneak Peek [2:53]
**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-cam-switcher-tutorial\frame_005.jpg


---

## Structured Notes

### Core Technique
Black Eye Camera Switcher: drag in a Camera Switcher Actor, bind cameras to keyboard keys, and live-switch between an army of dynamically-tracking Black Eye cameras during playback.

### Summary
3-minute tutorial for the Camera Switcher introduced in Black Eye v1.1.7. Drop a Camera Switcher Actor into the level, assign cameras from an array and bind each to a key. Live-switch during PIE between cameras that are all independently following and composing on different subjects. Add text label components to cameras for on-screen identification. Critical gotcha: remove any Camera Cuts clips on the Sequencer timeline — they override the switcher.

### Key Steps
1. **Drag Camera Switcher Actor into level** — available under Black Eye actors.
2. **Add cameras to the Cameras array** — click + to add entries; each entry = one camera + one key binding.
3. **Bind keys** — click the keyboard icon next to each entry, then tap the desired key to bind it.
4. **Set up cameras** — for each camera: set LookAt on desired subject/bone; optionally add Follow + Dynamic FOV. Example setups shown: head-only shot (LookAt head bone, actor bounds off) and wide follow shot (Follow + Dynamic FOV for auto-zoom).
5. **Remove Camera Cuts track clips** — if a Camera Cuts track is active on the Sequencer timeline, it overrides the switcher. Delete or disable those clips before testing.
6. **Play and switch** — enter PIE, press bound keys to cut between cameras. All cameras track their subjects dynamically while you switch.
7. **Add text label** — add a text component to a camera actor to show its name on-screen during switching (helps in complex scenes).

### UE Systems / Blueprints / Settings
- **Camera Switcher Actor** — Black Eye actor; holds Cameras array (camera + keyboard binding pairs)
- **Key binding** — click keyboard icon in array entry, tap key
- **Camera Cuts track** — UE Sequencer track; OVERRIDES the Camera Switcher if clips present — must be empty/disabled for switcher to work
- **Dynamic FOV** — auto-zoom on follow camera; screen size setting = how big the character should appear on screen
- **Follow damping** — small amount for a slight lag in following; improves feel
- **Text component** — optional label on camera actor for on-screen identification during switching

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1.1.7)

### Tags
`#blackeye-v1` `#camera` `#esports` `#live-events` `#mocap` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-v117-switcher-pilot]] — 55s feature preview of same v1.1.7 Switcher + Pilot mode
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — full v1 system; Camera Switcher section
- [[unreal-engine-black-eye-cameras-v12-preview-shot-list-module]] — auto-switching by occlusion (Shot List); complements manual switching
