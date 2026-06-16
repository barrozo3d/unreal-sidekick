---
title: Unreal Engine Black Eye Cameras: Unleash Your Army of Camera Operators
source: YouTube
url: https://www.youtube.com/watch?v=rw5OmVtBri8
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators/
frame_count: 7
---

# Unreal Engine Black Eye Cameras: Unleash Your Army of Camera Operators

**Source:** [YouTube](https://www.youtube.com/watch?v=rw5OmVtBri8)
**Author:** Black Eye Technologies
**Duration:** 3m10s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey, this is Adam. In this video, we're going to show a simple camera move, but one that

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_000.jpg

### Overview [0:11]
**Transcript:** could be tricky to keyframe. In black eye, it's really easy. So we come from the side,  we're following, we push up, and then we tip out to look and see the world. So this

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_001.jpg

### LookAt [0:26]
**Transcript:** is using the look at, and we say, we're on screen. We're targeting the head, just pushing  it to the rule of thirds on the right. But look at this, we can put it to the left and  hit play. It'll compose it that way. Obviously, that's not what we want, just to show you.  You're controlling the shot with keyframes to the composition. So let's put the head where  we want it on that. Let's grab forward a little bit and say right here, we want the composition  to be just so. And it's a great way of working. What you're doing is you're saying, where  in time you want the composition to be. And in between, it does all this buttery math to  make it very smoothly going between those different compositions. So there's a shot. Now,  we want to tip up. So look at this. Just pull the keyframe down. The camera looks up.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_002.jpg

### Follow [1:12]
**Transcript:** Straight forward. Now, this is a follow. This is keyframes saying that camera's position  relative to what we're following. And in this, it's the character. So there's damping  down here. So we're decoupling slightly from the character's movement. And we're saying  here at time, at this point, we want to be exactly behind. And we can keyframe the position  of the camera relative to the subject. So halfway through, you know, we could be inside  by side or we can be at a sort of a 45 degree angle there. So this is keyframes camera  position relative to the subject with damping. Okay, so here's a front shot just doing a real

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_003.jpg

### Front shot [1:51]
**Transcript:** quick camera relative to subject. It moves with them. Let's, you know, we close her further away.  We need to move the composition up down. Let's get that shot. Okay, how does this feel? Cool.  Got a nice shot at the front. And the magic of this means that if the character walks slower,  faster, it all still works. So now in the edit, because these cameras are all following the subject

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_004.jpg

### Editing [2:13]
**Transcript:** around, you can change your mind on the edit. Let's start with a close-up shot. Let's go to the side  shot. You can feel it out. And what you've got is this camera operator. You're now working as a  director. You've got all these camera operators, these camera robots that are filming your scene.  Look at them. They're describing like crazy, but look at this. All of these cameras are following.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_005.jpg

### Camera Operators [2:40]
**Transcript:** And the magic of black eye is now you're making edit decisions. You're getting closer to the story.  You're moving cameras around, but they're still smart. They're still framing. They're still  doing their mojo and you're just directing them. And this, you can work so quickly. This is a power  black eye. Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-unleash-your-army-of-camera-operators\frame_006.jpg

### Easter Egg [3:07]


---

## Structured Notes

### Core Technique
Director workflow: deploy multiple Black Eye cameras (Follow + LookAt + Screen Space Position keyframes) to cover a scene from all angles, then edit between them freely — each camera operator tracks independently while you make edit decisions.

### Summary
3-minute workflow concept video. Demonstrates building multiple Black Eye cameras around a moving subject (each with Follow + LookAt + screen-space composition keyframes), then cutting between them freely in the edit. The paradigm: you're the director with an army of robot camera operators. Cameras track and compose automatically; you decide the edit. Shows a side-follow shot (push up + tip-out using Follow offset Z + LookAt screen composition keyframes), a front-follow shot, and a close-up — all following the same character with different compositions. If the character walks faster/slower, all cameras still work correctly.

### Key Steps
1. **Set up multiple cameras** — each camera gets Follow on the character + LookAt on the head. Position each for a different angle (side, front, close-up, high push).
2. **Side shot with pedestal-tip** — Follow offset keyframes on Z (camera rises); LookAt Screen Space Position keyframe (tip camera up to reveal world).
3. **Screen Space Position keyframes** — add LookAt channel in Sequencer → Screen Space Position. Keyframe the target's position on screen at key moments (rule of thirds, left, right, center). Black Eye smoothly interpolates between positions.
4. **Follow offset keyframes** — keyframe camera position relative to subject (behind → side → 45 degrees). Damping on Follow decouples slightly for natural motion.
5. **Front shot** — camera locked to front of character; compose up/down via screen space. Works regardless of character speed.
6. **Cut between cameras** — all cameras track the subject throughout. Make edit decisions based on story, not tracking setup. Change mind on the cut freely.

### UE Systems / Blueprints / Settings
- **Follow** — translational follow; keyframe Follow Offset (position of camera relative to subject)
- **LookAt** — rotational tracking on head bone
- **Screen Space Position** — Sequencer channel under LookAt; keyframe subject placement on screen
- **Follow damping** — small amount decouples camera from character micro-motion
- **Multiple cameras** — each camera is independent; they all track simultaneously and can be cut between freely

### Difficulty
Beginner / Intermediate

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#beginner` `#intermediate`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — full v1 system; Follow, LookAt, Keyframe Composition sections
- [[unreal-engine-black-eye-cameras-thats-a-cool-shot-1-pedestal-pan]] — similar hybrid keyframing technique
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — same workflow applied to vehicles
