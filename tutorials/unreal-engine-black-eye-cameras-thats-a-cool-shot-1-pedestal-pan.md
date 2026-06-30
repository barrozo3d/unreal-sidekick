---
title: Unreal Engine Black Eye Cameras: That's a Cool Shot #1 Pedestal Pan
source: YouTube
url: https://www.youtube.com/watch?v=NOOpWzeC0Mg
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, pedestal, pan, hybrid-workflow, follow, look-at, composition, sequencer, keyframes, cinematics]
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
**Transcript:** Okay, let's go into hybrid mode and what that means is we're going to drag the camera  onto the sequencer and we're going to keyframe, manually keyframe some things and do some procedural  things.  So let's keyframe the follow offset, and we want to do up and down the pedestal, so we're  going to put some keyframes on the Z channel.  So let's get it down low, put a keyframe, and then at the moment where we want the camera  to come up, little later, sort of doing the wipe over the car, we'll drop a keyframe.  And look at that, we're procedurally composing on the two actors and we're manually pedestaling  the camera up and down, but the camera is relative to the subject.  Okay, let's widen the camera up a little bit, let's go to 28 mil lens.  Cool.  And let's have a look through the lens.  Okay, so we're kind of long.  The camera is tracking automatically rotating, we got a little wipe.  Let's just fix that high, I'm just going to bounce the keyframe with those keyframe.  Snap to keyframe buttons, just tweak this a little bit more.  Okay, and that's looking pretty good.  You know, maybe a little bit low there.  Let's just move that out.  Let's have the camera go a little slower, snap to that keyframe, and just the height.  Of course, check the curves.  It's really great to do a lot of fine tuning of the anything animation.  So we'll just tweak that so it's looking good at each position.  Still like using less keyframes than more.  Very smooth.  So let's make sure we get this.  What we're doing is we're procedurally moving the camera with the car.  We're procedurally targeting the two dancers, but we're keyframing the height.  The only keyframes here are on the heights so far.  So we're getting some really sophisticated movement just with those two keyframes.  But the composition is still in the center.  So let's add a look at animation track.  Close a follow, we'll open the look at and let's put some keyframes on our subject screen position.  This is very powerful.  So what we're doing here is we're keyframing where we want things composed right here.  It's in the center, but just by changing the X and Y, we're changing where we want the subject  composed in screen space.  And what's so powerful about this is you just think like a director.  Like, where do I want the composition at the start?  And here at the end, we want the composition a little bit over to the right.  Let me just lift it up a little bit.  And the magic here is we start with the composition on the left.  And we're blending the composition from the start to the end.  So we've got now what, one, two, three, four, five, six keyframes to do this complex shot.  It's so fast.  So let's watch it again.  Procedural movement, procedural rotation, keyframe composition, keyframe height.  Let's do a little bit more tweaking now that we got it all working.  So few keyframes so fast to work.  And these shots will still work even if things change.  That's the magic of them because you're giving the camera intent.  This is the composition I want at this moment in time.  This is the height.  These are things that I'm relative to.  The cameras are smart.  They'll follow your direction.  You tell them what you want.  And they can handle variability.  Let's go even a little bit wider.  I want to see a bit more of the car.  Just to just see the camera position relative to the car.  This is probably going to crash through though.  Yeah, it's crashing.  That's fine.  Just find that crash bit.  Just move the camera over.  Again, that's the offset between the camera and the car.  Let's try that one more time.  When we lift and go over the car, we get a nice white boom.  Pretty cool shot.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_003.jpg

### Hybrid keyframing [5:14]
**Transcript:** Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan\frame_004.jpg

### End [5:35]


---

## Structured Notes

### Core Technique
Classic **pedestal pan** shot using BEC hybrid mode: Follow camera locks to a moving car (positional); Look At tracks two separate walking characters (rotational). Only 6 keyframes total — 2 on Follow Offset Z (camera height for pedestal move) + 2–4 on Subject Screen Position (composition shift left→right). BEC handles all the rotation math automatically.

### Summary
5m38s Black Eye Technologies "That's a Cool Shot #1" episode. Adam demonstrates how to build a cinematic pedestal pan using BEC hybrid mode. Setup: Follow car → Look At two people (multiple subjects) → 28mm lens → drag to Sequencer. Hybrid mode: keyframe Follow Offset Z channel for pedestal up (camera rises over car) + keyframe Subject Screen Position for composition change (starts left, ends right). Fine-tune keyframe curves for timing. Minimum keyframes, maximum procedural behavior. Shot still works if characters move/change.

### Key Steps
1. Install BEC plugin (Fab → Edit→Plugins → Black Eye → enable → restart)
2. Drop Black Eye camera into scene
3. Enable **Follow** → eyedropper → pick car → camera jumps 300 units off side; drag to desired starting position (low, close to car)
4. Enable **Look At → Multiple Subjects** → eyedropper subject 1: left character, subject 2: right character → white box tracks both
5. Set lens: 28mm (wide gives dynamic feel for pedestal)
6. **Drag camera onto Sequencer** (Camera Cuts track)

**Hybrid mode:**
7. In Sequencer: open Follow module → **Follow Offset Z channel** → scrub to shot start → keyframe Z at low position
8. Scrub to moment camera should rise → keyframe Z at high position (pedestal up, camera wipes over car)
9. Open Look At module → **Subject Screen Position track** → look through lens
10. Keyframe composition at start (subject slightly left of center)
11. Scrub to end → adjust X/Y to move composition right → keyframe
12. Refine with Sequencer curve editor: check tangents on Z height + screen position to control timing of rise and composition shift
13. Widen lens further if too cramped (e.g., 24mm) → grab camera and adjust offset to avoid clipping through car geometry

### UE Systems / Blueprints / Settings
- **Follow Offset channel** (Sequencer) — keyframe specific axes (Z only) while BEC handles lateral follow procedurally; Z channel = pedestal/crane move
- **Subject Screen Position** (Sequencer track, under Look At) — X/Y position of subject on screen; keyframe composition shifts across shot duration
- **Multiple Subjects** (Look At) — 2 subjects in white framing box; camera rotation tracks combined bounding box
- **Hybrid mode** — mix of: procedural Follow (lateral + rotation) + manual Z keyframes + manual screen position keyframes; non-destructive blend
- Total keyframes needed: 2 (height) + 2–4 (composition) = 4–6 keyframes for a fully polished complex moving shot

### Difficulty
Beginner. Demonstrates BEC hybrid mode principles efficiently. Use as a template for any pedestal/crane move.

### UE Version
UE5 (Black Eye Cameras)

### Tags
black-eye-cameras, pedestal, pan, hybrid-workflow, follow, look-at, composition, sequencer, keyframes, cinematics

---

## Related Entries
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — full BEC system overview; hybrid mode explained in detail
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — BEC overview; hybrid workflow section
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — car Follow + Subject Screen Position composition keyframing workflow
