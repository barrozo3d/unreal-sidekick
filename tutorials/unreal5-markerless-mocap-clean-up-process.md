---
title: Unreal5 Markerless MoCap (CLEAN-UP Process)
source: YouTube
url: https://www.youtube.com/watch?v=rLPRlPlZ3Lw
author: Royal Skies
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal5-markerless-mocap-clean-up-process/
frame_count: 0
frame_status: pending-selection
---

# Unreal5 Markerless MoCap (CLEAN-UP Process)

**Source:** [YouTube](https://www.youtube.com/watch?v=rLPRlPlZ3Lw)
**Author:** Royal Skies
**Duration:** 3m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal5-markerless-mocap-clean-up-process <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So you got some video mocap animation from Unreal 5's Marketless Mocap, but the feed
[0:04] are a little bit weird and you need to clean it up.
[0:06] Not a problem.
[0:07] First thing we do is export the animation as an FBX.
[0:10] So click your mocap animation, right click, asset actions, export, and from this point
[0:15] you can clean it up wherever you want.
[0:17] You can do it in Unreal, Blender, 3D Max, Maya, wherever, but personally I always believe in
[0:22] using the best tool for the job and by far the best mocap animation cleanup software
[0:28] is Cascader.
[0:29] It's $8 a month but I am telling you it will pay for itself within the first 3 days of
[0:33] using it.
[0:34] I have a whole in-depth video explaining why Cascader is better than any other animation
[0:38] software, but long story short it applies real world math and physics to your poses
[0:43] and keyframes and it will even generate the movements between your keyframes if you ask
[0:47] it to.
[0:48] For example, if you have a keyframe here and another one here and you say make the character
[0:52] walk between this frame and that one, it will calculate the most likely way to generate
[0:57] a walk that starts on this frame and ends on this one.
[1:00] It's absolutely crazy technology and the best part is once it generates something for you
[1:05] you can easily adjust it to change the parts you want to be more stylized to your liking.
[1:10] That being said, Cascader also has a built-in Unreal 5 mannequin by default so if you open
[1:15] a new tab and import the FBX from Unreal, go to bone mode, double click the route to
[1:19] select everything, click on the timeline, control shift C to copy everything, then go
[1:24] to the Unreal mannequin and in bone mode, double click the route to select everything
[1:27] again, select the whole timeline and control shift V to paste, you will now see the animation
[1:32] show up on the default mannequin.
[1:35] From this point we just go to the top right and hit this button to bake the movements
[1:38] to our controls and now we are ready to clean up.
[1:40] We will want to start by deleting all of the fluff so that we only have keyframes, I do
[1:45] this by going through the timeline and selecting the frames I don't like and just pressing
[1:48] all F to remove them.
[1:50] Once I've done that, we should just be left with keyframes and if we select everything
[1:53] and go up here and hit bzia curve, it will start to smoothen everything together.
[1:57] But more importantly, we can start looking on how to fix the feet now.
[2:01] Cascader makes this super easy.
[2:02] When you see a frame where the feet look a little bit weird, like if the toes are going
[2:05] through the ground, just select all the toes, press shift Z to delete the data and it will
[2:10] automatically snap what's left to the ground.
[2:12] Sometimes we'll have some awkward angles like this and we just have to manually decide
[2:15] to move it wherever we think makes most sense, but overall the auto delete snap will do 80%
[2:20] of the work for you.
[2:21] Once the feet look right, we can go through the rest of the animation to see if anything
[2:24] else needs to be changed.
[2:25] For me, I think the legs during the flip should be a bit more straightened out and extended,
[2:29] so I'm just going to grab the feet and extend them out on these frames right here.
[2:33] Okay, looking much better.
[2:35] And remember how I said we have physics assist in Cascader to make the animations more accurate
[2:40] to real life gravity and velocity?
[2:41] Well, we can turn that on by clicking this button up here and now you will see a green
[2:45] figure which will show us what the animation would most likely look like given our keyframes
[2:50] and physics.
[2:51] Now sometimes you as an artist might want to say screw the physics.
[2:54] I think this pose is really important and should be more exaggerated.
[2:57] For example, in cases like right here, I sort of disagree with the physics simulation and
[3:02] in this case, I can just go up here and set this as a priority frame.
[3:05] And now you can see I have brute force the pose into the physics calculation.
[3:09] And now we have a really nice smooth butterfly kick with the feet and legs corrected.
[3:13] From this point, we just go up here and hit bake to physics and then file, export fbx and
[3:18] then Unreal import the new fixed fbx.
[3:21] And now we have the fixed animation in Unreal 5 and we can go back to making our game.
[3:25] Now I know this was a super short and easy tutorial, but if you want a more in depth
[3:28] video explaining the ins and outs of Cascader controls, you can find that video in the pinned
[3:33] comment.
[3:34] And if you want to try Cascader out for yourself, then be sure to use my promo code.
[3:37] They made it just for you guys.
[3:38] Regardless, hope that helps and as always, let me have a fantastic day.
[3:43] Now see you around.



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
