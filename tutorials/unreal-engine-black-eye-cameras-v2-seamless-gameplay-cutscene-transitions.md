---
title: Unreal Engine Black Eye Cameras v2: Seamless gameplay cutscene transitions
source: YouTube
url: https://www.youtube.com/watch?v=lJ_1NAYtdtg
author: Black Eye Technologies
ingested: 2026-07-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/
frame_count: 0
frame_status: pending-selection
---

# Unreal Engine Black Eye Cameras v2: Seamless gameplay cutscene transitions

**Source:** [YouTube](https://www.youtube.com/watch?v=lJ_1NAYtdtg)
**Author:** Black Eye Technologies
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] The seamless gameplay to cutscene transitions.
[0:02] These can be really tricky. There's a lot of edge cases.
[0:05] BlackEye helps make it a snap.
[0:06] Okay, look at this. See that camera swing around?
[0:09] Change the composition and smoothly go in.
[0:12] Look at this. I'm going to go really low here.
[0:15] I'm not adjusting the free look.
[0:17] That's the camera blending straight in to the cutscene.
[0:21] Look at this. We're over top.
[0:22] The camera gets into position before the cutscene starts.
[0:27] Let me show you how to do this.
[0:28] This is the BlackEye camera plugin for Unreal Engine.
[0:33] Okay, so you've got your gameplay camera.
[0:36] Duplicate it. Give it a name.
[0:38] Now let's make a BlackEye trigger volume.
[0:40] We're going to put it here before where the cutscene starts.
[0:45] And we're going to add a tag.
[0:46] And we're going to say,
[0:48] Rhymon Align.
[0:51] Make this tag right here.
[0:53] Okay, now we go to the camera and say the same tag.
[0:55] So now the trigger volume and the camera have the same tag.
[0:58] Turn off auto-activate because you just want that for the first camera.
[1:01] And we're going to turn on the auto-rescentering and have it be really quick.
[1:03] This is what's going to swing the camera into position
[1:05] because we're re-centering the camera to a specific angle.
[1:08] And let's play.
[1:09] We're going to tune the camera while it's running.
[1:11] This is part of the magic of BlackEye.
[1:12] So here we go.
[1:13] We walk up to the trigger volume and we can see we blend to it.
[1:17] It's not the right angle.
[1:18] Not what we want yet.
[1:19] But that's cool. We're going to tune it.
[1:21] So let's adjust this angle.
[1:24] We're going to make sure you're on world, by the way.
[1:25] So this is like world relative angle.
[1:28] So we're going to tune the heading center.
[1:30] We're going to make sure that let's get that angle right.
[1:33] We want to be something over here.
[1:35] Now we get this little checkbox real-time viewport updates.
[1:38] You know when you move and it goes blip,
[1:39] blip, blip and it only updates when you release.
[1:41] Well, turn that on.
[1:42] Now it updates in real time.
[1:44] Let's adjust the composition with a little look through the new panel.
[1:48] And then let's get the pitch up.
[1:52] Let's get the heading right.
[1:54] Okay, you know what?
[1:55] And let's go to the longer lens.
[1:56] Let's just do a slightly longer lens.
[1:58] So we're doing all this while it's running.
[2:01] Adjust the composition a little bit.
[2:03] Out we come.
[2:04] We blend seamlessly to your orbit camera.
[2:09] And then let's go and see how that feels.
[2:11] Let's walk back in.
[2:15] And we blend to this shot.
[2:16] Bam.
[2:23] That's a nice transition.
[2:24] So let's try to break it.
[2:25] Look at this.
[2:25] We come far to the side.
[2:27] The camera will swing around.
[2:30] So no matter what angle the orbit's at,
[2:32] when you hit that trigger volume,
[2:34] we're rotating to that specific angle
[2:37] to make the transition from your orbit gameplay seamless.
[2:42] So the blend.
[2:42] Okay, and what's this blend?
[2:43] How are we doing this?
[2:44] Well, look at this.
[2:45] Looks like a couple of seconds.
[2:48] We've made this a really handy way through the panel.
[2:52] You can select your blend list and that's this.
[2:54] So we get a default blend.
[2:55] So we just made it three seconds, much slower.
[3:02] And this is a blend list file that dictates
[3:05] all of how the cameras blend together.
[3:07] Now here's .8 seconds.
[3:11] Really quick.
[3:13] Okay, that's fine.
[3:13] That's a default, but we've got wild cards
[3:15] or any camera to any camera.
[3:17] So here we're going to say from any camera,
[3:19] we want to be one second,
[3:21] and to the ram in the line.
[3:26] We're going to be two and a half seconds.
[3:27] So these are wild cards.
[3:28] So from any camera,
[3:30] and then from the ram and to any other camera.
[3:33] And there's two and a half seconds in,
[3:37] about a point a second up.
[3:39] You can make this wild cards per camera,
[3:42] or you can do camera A to camera B,
[3:44] camera B to camera A, any combination.
[3:48] Okay, so here's how the sequencer is set up.
[3:49] So inside that, we've got a standard trigger volume,
[3:52] standard UE trigger volume,
[3:54] and it's playing a cutscene.
[3:55] This is just vanilla normal on actor begin overlap,
[4:01] play the cutscene.
[4:02] But because it's inside a little bit,
[4:04] and we've got our black eye trigger volume
[4:06] on the outside of that,
[4:08] we create these zones where we grab the orbit control
[4:11] from the user, put it into the right spot,
[4:13] and then seamlessly transition into the cutscene.
[4:17] So here's the cutscene here.
[4:18] Right click, can blend,
[4:21] and then see in the top,
[4:22] it's really small, this little yellow.
[4:26] Okay, that lets you go.
[4:27] So cut, cut, so that's a cut,
[4:29] and you move that in,
[4:30] and that will blend from wherever the camera is.
[4:32] You can see it's just blending from where the camera is
[4:34] right now, and then do this at the end.
[4:36] But because black eye is gonna position that camera
[4:39] in the right spot, that transition goes perfectly smooth.
[4:44] So you can now create cutscenes
[4:47] that will take wherever the camera is,
[4:50] where the user's orbit is perfectly aligned to camera,
[4:54] and then perfectly transition into the cutscene.
[4:58] And this is gonna help you in all those weird edge cases
[5:00] where you don't know what the person's doing.
[5:02] Look at this, we're composing at the bottom right of the screen,
[5:04] but as we transition,
[5:06] move into the middle, back to orbit camera.
[5:09] So fast and easy.
[5:10] It's black eye.
[5:12] Great cameras make great projects.
[5:14] Do cool stuff.
[5:18] Thank you for watching.



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
