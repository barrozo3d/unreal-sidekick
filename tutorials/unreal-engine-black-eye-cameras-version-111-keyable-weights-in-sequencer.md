---
title: Unreal Engine Black Eye Cameras: Version 1.1.1: Keyable Weights in Sequencer
source: YouTube
url: https://www.youtube.com/watch?v=94UWBG7hKDI
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, sequencer, keyframes, weights, look-at, follow, multiple-subjects, v1-1-1]
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
**Transcript:** up. Okay, here's the scene, things are moving around. Go to place actors and  drop a black eye camera in the scene. There it is. We're gonna go follow, we're  gonna follow multiple subjects. Let's open four and click on the subjects.  You see a little red line? Cameras can average between the two. Now it's  averaging between the three and look when you mix the weight. So now we're  blending the contribution of three, four, more things towards the camera.  And there's the weight between the three to the four. So once that's in there,  we're gonna now move the camera away from that point. So I'm just gonna lift it  up, move it back and forth. And you can punch the numbers into there or you can  just grab the camera and move it and it'll maintain that offset. That's easier.  Okay, so now let's go to look at same deal. Pick the first thing. Pick the next.  We're gonna go through the list. One, two, three, four. The camera is adjusting.  Now this is a fixed lens. It can't go wide enough for that. So let's put on some  dynamic FOV. And let's adjust the screen space for those so we get a nice  framing. Okay, over there, they're driving around. The camera's way over here.  Let's fix that. So I'm gonna just change those numbers just to get a shot.  We're gonna grab the camera, throw the numbers in, either way it works. Okay, now  that that's set up, let's switch this clip to point to this new camera that we made.  And turn it on. There's new camera. Look at all that goopy nice moving. Okay, so

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_002.jpg

### Keyframing [2:27]
**Transcript:** here it is. Here's the key framing set up. We're about to do it. So go to the  camera, pick look at and then add that as a channel, right? And then go to your  subject, camera target, wait, we're gonna just speed this up because we're gonna  add one for each one. There you go. Let's drop some keyframes down and let's set  the weights all to be just the first subject. And then let's change it. So now we  go from red car to yellow truck. Those are key frames. I'm just keyframing the  weights. And sometimes if it's addressed a camera motion, you might need to  adjust the damping. So I'm gonna have a little bit more aggressive following on  the pitch. I'm just tweak the composition here. Look at that. We got a shot going  and then we are targeting the yellow truck. And we can follow more things. Go crazy.  Okay, so and look at this. Here's the keyframes. Just went to the sequence curves.  And this is how much each different thing is adding interest. So plane, just car,  just plane. And look at this. You can see the blue boxes. So when the plane is  not being considered, it stops. And when it is, it is. So you can debug the scene.  You can see what's going on. The little blue cubes show what objects are being  considered in the blending evaluation. If it's zero, the cubes go away. And you can move  the cameras around. So all this is set up. But let's just move the camera to the side.  And the weights all still work. So if you had keyframes on weights, but then you want to  move the camera around, camera's looking to do it. So here we are. Keyframes on weights.  It's real. It's a 1.1.1. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_003.jpg

### Outtro [4:22]
**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer\frame_004.jpg


---

## Structured Notes

### Core Technique
BEC v1.1.1: Look At and Follow subject weights are now **keyframeable in Sequencer**. One camera can Follow up to 4+ subjects and Look At 4+ subjects, each with independently keyframeable weight tracks. Keyframe weights 0→1 to shift camera attention between subjects over time. Debug: blue cubes appear/disappear matching weight value (0=cube gone). Enables sophisticated single-camera sequences switching between multiple targets without changing cameras.

### Summary
4m31s BEC v1.1.1 keyable weights in Sequencer announcement and tutorial. Demo: one camera following/looking at red car → yellow truck → cyan car → green car → plane. All on one camera via weight keyframes. Setup: BEC camera → Follow 4 subjects → Look At 4 subjects → Dynamic FOV → Sequencer → select camera → Look At → Add channel → "Camera Target Weight" per subject → keyframe weights. Blue debug cubes visible only when weight > 0; vanish when zero. Can still move camera after weight keyframes set up; all relationships preserved. "It's real. It's 1.1.1."

### Key Steps
**Setup (4 subjects):**
1. Place Black Eye camera → enable **Follow** → set to multiple subjects → eyedropper subjects 1–4
2. Enable **Look At** → eyedropper subjects 1–4 (same subjects as Follow or different)
3. Enable **Dynamic FOV** → adjust screen space composition for combined box
4. Place camera manually or grab and move to achieve rough shot position

**Sequencer keyframing:**
5. Drag clip to Camera Cuts track → camera active
6. Select camera → in Sequencer: expand Look At module → **Add track → Camera Target Weight** (one per subject slot)
7. Repeat for each subject: subjects 1, 2, 3, 4 each get their own weight track
8. Go to frame 0 → keyframe: Subject 1 weight = 1, Subjects 2–4 weight = 0 → camera looks at only subject 1
9. Scrub forward → keyframe: Subject 1 weight = 0, Subject 2 weight = 1 → camera transitions attention to subject 2
10. Continue for each transition (S2→S3→S4→multi, etc.)
11. Optionally adjust **damping** if weight transitions cause camera to jerk (e.g., increase pitch damping)
12. Move camera position freely at any point; weight keyframes remain valid regardless of camera world position

**Debug:**
13. Blue cubes visible when weight > 0; vanish at weight = 0 → visual confirmation of which subjects are being considered in blending evaluation

### UE Systems / Blueprints / Settings
- **Camera Target Weight tracks** (Sequencer) — per-subject keyframe track on Look At (and Follow) modules; value 0–1; camera composites weighted bounding box of all > 0 subjects
- **Multi-subject Follow** (4+ subjects) — camera follows averaged position of all subjects weighted above zero
- **Multi-subject Look At** (4+ subjects) — camera composes on weighted aggregate of all subject cubes
- **Dynamic FOV** — used here to automatically frame variable-size groups (single car = tight; group = wide)
- **Blue debug cubes** — each subject has a blue cube visible when weight > 0; disappears at weight = 0; use to debug blending evaluation in viewport
- **Weight keyframe approach** — replaces switching cameras; single camera does full sequence of attention shifts via weight animation; eliminates camera cuts for smooth transitions

### Difficulty
Beginner to intermediate. Sequencer track setup is straightforward; weight keyframe strategy requires planning for multi-subject scenes.

### UE Version
UE5 (Black Eye Cameras v1.1.1+)

### Tags
black-eye-cameras, sequencer, keyframes, weights, look-at, follow, multiple-subjects, v1-1-1

---

## Related Entries
- `unreal-engine-black-eye-cameras-version-11-new-features-multi-subject-lookat-wei.md` — v1.1 announcement; Blueprint-only weight control (predecessor)
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — keyframe weights section with space vehicle sub-component targets
- `unreal-engine-black-eye-cameras-version-111-keyable-weights-in-sequencer.md` — this file; canonical reference for weight keyframing in Sequencer
