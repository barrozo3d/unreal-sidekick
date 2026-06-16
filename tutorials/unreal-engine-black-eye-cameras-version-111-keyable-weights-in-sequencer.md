---
title: Unreal Engine Black Eye Cameras: Version 1.1.1: Keyable Weights in Sequencer
source: YouTube
url: https://www.youtube.com/watch?v=94UWBG7hKDI
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.1.1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer/
frame_count: 5
---

# Unreal Engine Black Eye Cameras: Version 1.1.1: Keyable Weights in Sequencer

**Source:** [YouTube](https://www.youtube.com/watch?v=94UWBG7hKDI)
**Author:** Black Eye Technologies
**Duration:** 4m31s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** This is kind of a big deal. It's a small number upgrade, but it's a big, powerful  big feature. That is keyframeable weights. Here we go. I'm looking at the red

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_000.jpg

### Overview [0:10]
**Transcript:** car, looking at the yellow car, I'm looking at the yellow and the blue cyan  car, adding the green car. Now I'm looking at the plane. Now we're following the  green car, we're looking at the car and the plane, then we're gonna go and  follow the red car, we're gonna look at both of them and then you see we're  getting with this. You can look at anything, you could follow anything and look  at all those keyframes. So here's the weights. You can see them going up and down,  you can see all the keyframes on the left. You can see mixing and matching. This is  one camera and here are the keyframes. And if you have two things that will  compose on two, or just one, or four, or 15, to get the idea. Here's how to set it

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_001.jpg

### Setup [0:56]
**Transcript:** up. Okay, here's the scene, things are moving around. Go to place actors and  drop a black eye camera in the scene. There it is. We're gonna go follow, we're  gonna follow multiple subjects. Let's open four and click on the subjects.  You see a little red line? Cameras can average between the two. Now it's  averaging between the three and look when you mix the weight. So now we're  blending the contribution of three, four, more things towards the camera.  And there's the weight between the three to the four. So once that's in there,  we're gonna now move the camera away from that point. So I'm just gonna lift it  up, move it back and forth. And you can punch the numbers into there or you can  just grab the camera and move it and it'll maintain that offset. That's easier.  Okay, so now let's go to look at same deal. Pick the first thing. Pick the next.  We're gonna go through the list. One, two, three, four. The camera is adjusting.  Now this is a fixed lens. It can't go wide enough for that. So let's put on some  dynamic FOV. And let's adjust the screen space for those so we get a nice  framing. Okay, over there, they're driving around. The camera's way over here.  Let's fix that. ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_002.jpg

### Keyframing [2:27]
**Transcript:** here it is. Here's the key framing set up. We're about to do it. So go to the  camera, pick look at and then add that as a channel, right? And then go to your  subject, camera target, wait, we're gonna just speed this up because we're gonna  add one for each one. There you go. Let's drop some keyframes down and let's set  the weights all to be just the first subject. And then let's change it. So now we  go from red car to yellow truck. Those are key frames. I'm just keyframing the  weights. And sometimes if it's addressed a camera motion, you might need to  adjust the damping. So I'm gonna have a little bit more aggressive following on  the pitch. I'm just tweak the composition here. Look at that. We got a shot going  and then we are targeting the yellow truck. And we can follow more things. Go crazy.  Okay, so and look at this. Here's the keyframes. Just went to the sequence curves.  And this is how much each different thing is adding interest. So plane, just car,  just plane. And look at this. You can see the blue boxes. So when the plane is  not being considered, it stops. And when it is, it is. So you can debug the scene.  You can see what's going on. The little blue cubes show...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_003.jpg

### Outtro [4:22]
**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_004.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.1.1 Keyable Weights in Sequencer: keyframe the weight/contribution of each individual subject in multi-subject Follow and LookAt, enabling smooth transitions between subjects within a single camera setup.

### Summary
4.5-minute feature tutorial for keyable weights, introduced in v1.1.1. A single camera can Follow and LookAt multiple subjects simultaneously; each subject has an individual weight (0–1). By keyframing these weights in Sequencer you can smoothly ramp from "looking at red car" to "looking at yellow truck" to "averaging between plane and car" — all on one camera without cuts. Blue debug boxes visualize which subjects are being considered and their relative weights. Dynamic FOV adjusts automatically as the camera frames different combinations of subjects.

### Key Steps
1. **Set up multi-subject Follow** — drop Black Eye camera, click Follow → Multiple Subjects. Open subjects array, click + for each subject. Camera averages the positions (contribution per subject weight).
2. **Add LookAt multi-subjects** — same process for Look At: add all subjects you want to track. Camera composes on the weighted average.
3. **Add Dynamic FOV** — required when subjects vary greatly in position/distance. Adjust screen size so framing looks good.
4. **Add Sequencer channels for weights** — in Sequencer, find the camera, expand LookAt or Follow → Subjects → Camera Target Weight for each subject.
5. **Keyframe transitions** — set all weights to 0 except one (= looking at subject 1). Move playhead forward → change weight to transition to subject 2. Can blend multiple subjects simultaneously by setting multiple non-zero weights.
6. **Debug visualization** — blue boxes appear around each subject based on its current weight. Useful to verify the blending behavior.
7. **Adjust composition + damping** — after weight keyframing, tweak Follow and LookAt damping for smooth transitions. Pitch damping may need to be more aggressive during subject swaps.

### UE Systems / Blueprints / Settings
- **Keyable Weight** — per-subject float value (0–1) on Follow and LookAt multi-subject arrays; keyframeable in Sequencer
- **Multi-subject Follow** — camera position = weighted average of all subject positions
- **Multi-subject LookAt** — camera rotation = weighted average of all subject look-at targets
- **Dynamic FOV** — required for variable subject groupings; set screen size to control how large subjects appear
- **Blue debug boxes** — visualize active subjects and their weight contribution
- **Camera Target Weight channel** — Sequencer sub-channel under LookAt / Follow → each subject

### Difficulty
Intermediate

### UE Version
UE 5.x (Black Eye v1.1.1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#intermediate`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Keyframe Weights section (overview); Multiple Subjects section
- [[unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei]] — v1.1 Multi-Subject LookAt Weights (precursor to v1.1.1 keyable weights)
- [[plugin-blackeye-versions]] — v1.1.1 changelog
