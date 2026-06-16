---
title: Unreal Engine Black Eye Cameras: That's a Cool Shot #1 Pedestal Pan
source: YouTube
url: https://www.youtube.com/watch?v=NOOpWzeC0Mg
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan/
frame_count: 5
---

# Unreal Engine Black Eye Cameras: That's a Cool Shot #1 Pedestal Pan

**Source:** [YouTube](https://www.youtube.com/watch?v=NOOpWzeC0Mg)
**Author:** Black Eye Technologies
**Duration:** 5m38s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Look at this classic pedestal pan shot.  It's such a great move and it's number one on our, that's a cool shot.  Episode one, pedestal pan.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_000.jpg

### Plugin install [0:13]
**Transcript:** Okay, install the plug in, select it, and it done.  Black eyes in your scene, now hit add object, pick a black eye camera, drop it in your  scene, then click follow and pick the thing you want to follow, we're going to follow

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_001.jpg

### Adding a camera [0:23]
**Transcript:** this car, and then you can just grab the camera and put it wherever you want, and it'll  still follow the car.  Okay, let's get a little closer to this.  Now we want to look at these two people, so click look at two subjects, multiple subjects,  person on the left, click eyedropper, person on the right.  Look how fast that is, we've got a camera that's following something and looking at something  else.  Instantly, like that was what?  20 seconds, not even.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_002.jpg

### Follow and LookAt [0:56]
**Transcript:** Okay, let's go into hybrid mode and what that means is we're going to drag the camera  onto the sequencer and we're going to keyframe, manually keyframe some things and do some procedural  things.  So let's keyframe the follow offset, and we want to do up and down the pedestal, so we're  going to put some keyframes on the Z channel.  So let's get it down low, put a keyframe, and then at the moment where we want the camera  to come up, little later, sort of doing the wipe over the car, we'll drop a keyframe.  And look at that, we're procedurally composing on the two actors and we're manually pedestaling  the camera up and down, but the camera is relative to the subject.  Okay, let's widen the camera up a little bit, let's go to 28 mil lens.  Cool.  And let's have a look through the lens.  Okay, so we're kind of long.  The camera is tracking automatically rotating, we got a little wipe.  Let's just fix that high, I'm just going to bounce the keyframe with those keyframe.  Snap to keyframe buttons, just tweak this a little bit more.  Okay, and that's looking pretty good.  You know, maybe a little bit low there.  Let's just move that out.  Let's have the camera go a little slower, snap...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_003.jpg

### Hybrid keyframing [5:14]
**Transcript:** Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_004.jpg

### End [5:35]


---

## Structured Notes

### Core Technique
Hybrid Sequencer shot: classic pedestal pan using Black Eye's follow + multi-subject LookAt with a Z-channel keyframe pedestal move — camera follows a car while looking at two walking characters and manually rises over the car.

### Summary
5.5-minute "That's a Cool Shot" episode #1. Demonstrates building a cinematic pedestal pan in under 20 seconds setup time using Black Eye. Camera follows a car but looks at two people walking beside it. Adds manual Z-axis keyframes in Sequencer (pedestal up) while keeping all rotation/tracking procedural. Uses 28mm lens for wide feel. Iterates on timing via curve editor.

### Key Steps
1. **Install plugin + add camera** — install Black Eye from Fab, drop a Black Eye Camera into the scene.
2. **Set Follow on car** — click Follow → pick car → camera jumps 300 units to side.
3. **Set Multi-subject LookAt** — click Look At → Multiple Subjects → eyedropper person left, eyedropper person right. Camera now follows the car but looks at two walking people.
4. **Add to Sequencer** — drag camera to Sequencer timeline.
5. **Add Follow Offset track** — keyframe Z channel only: start low (set key), pedestal up at the desired moment (set key). Camera rises over the car while still following it.
6. **Choose lens** — set to 28mm for wider feel. Adjust composition by reviewing through lens.
7. **Refine timing** — use Sequencer curve editor to push/pull keyframe positions for pacing. Adjust camera speed (how fast it rises) by moving keys on the Z channel.

### UE Systems / Blueprints / Settings
- **Follow** — translational tracking; camera rigidly attached to follow subject offset
- **Multiple Subjects LookAt** — camera looks at combined bounding box of multiple subjects
- **Follow Offset track** — Sequencer track; keyframe spatial relationship between camera and follow target; Z channel = pedestal
- **Hybrid mode** — procedural follow/look-at + manual Sequencer keyframes on select channels only
- **28mm lens** — wider field for the pedestal pan feel
- **Snap-to-keyframe buttons** — Sequencer navigation; bounce between keyframe positions while adjusting

### Difficulty
Beginner / Intermediate

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#beginner` `#intermediate`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — full v1 system; Follow Keyframes section covers the same hybrid technique
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — follow fly-by rig uses the same hybrid approach with more tracks
