---
title: Unreal Engine Black Eye Cameras for Gameplay: Top Down
source: YouTube
url: https://www.youtube.com/watch?v=MFrmcgQHGJk
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/
frame_count: 4
---

# Unreal Engine Black Eye Cameras for Gameplay: Top Down

**Source:** [YouTube](https://www.youtube.com/watch?v=MFrmcgQHGJk)
**Author:** Black Eye Technologies
**Duration:** 3m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey everybody, this is Adam. Let's get into some gameplay cameras. In this video, we're gonna get into the top down gameplay cameras. It's so cool how Epic has created all these test scenes for us to deconstruct. Let's get into the top down one. Have you ever noticed? Top down, first person, third person. Video game genres. Our camera descriptions. The Delta between a good project and a great one is often the camera. Okay, let's get into it. So here's the camera that's in there and it's great. Stampin, it's following, but you can see without much look ahead, the character can get pretty close to the edge of the screen. So what we're gonna do is we're gonna show you how quickly you can do some velocity look ahead stuff on the black eye. So let's get some black eye mode out into the scene. So look at this. This is where we're gonna get to. You're running, but the camera is giving you some leading composition. You can see the center of the screen is in front of the character. But as you go slower, it comes back and as you go faster, it goes forward. When you've got powerful camera controls like this, you can experiment, you can iterate, you can try out ideas like look at this. We got a camera up high. Nope, let's put it in closer. Let's have the orientation damping low. One number change. It's a completely different feel. You can iterate, you can tune, you can move fast. Okay, let's install this. We go to edit plugins, go to black eye, turn it on. You might have to reboot. Once you get it in, let's go to black eye, drop a camera in the scene and we're gonna set it to target player zero and look at and follow it. Click the look at and set it to world space center. And then click save and play so all your changes are saved and let's run it. The default camera position is not ideal. So let's punch in some offsets. We're gonna mimic the camera that was in there slightly just so you can see the differences with the look ahead, change the lens. Okay, and let's turn on the debug so you can see what's going on. Okay, so now we got a camera. Similar. Let's put a little follow damping on there. One is quite a bit. And we turned off the look damping so the camera's get the car, the caratress can be pinned to this end of the screen and the camera is going to follow dampened. You can still see we get kind of close to each the frame. You know, smooth and buttery in one regard, but it's not really a sophisticated camera yet. And it kind of packs up a little bit when you're on towards the camera. So let's fix that. So the look at, there's an offset. And if it's in local space, you can change where you're looking on the character. So we just pushed it forward a little bit. And that's cool sometimes, but look, it's a little C-Sick E-in. For some things that's amazing, but for this, we wanted to look at the character, but not always. So let's move it back. We're gonna use velocity look ahead. So I'm gonna just punch some numbers in there. Too much. Now when we start to move the velocity, we're looking ahead based on the character's velocity. Let's make these numbers a little less crazy. So you can see that dot, it moves forward. And the camera is now composing on the that velocity position that's ahead. But as you slow down, it comes back. You can see that look ahead. Now just to compare with the original camera with no look ahead, look at this, you're packing in. So just a couple of seconds under a minute, you've got velocity look ahead on a top-down camera. Good cameras make great projects. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-for-gameplay-top-down\frame_000.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
