---
title: Unreal5 Markerless MoCap (CLEAN-UP Process)
source: YouTube
url: https://www.youtube.com/watch?v=rLPRlPlZ3Lw
author: Royal Skies
ingested: 2026-08-02
ue_version: "Not specified (UE5.x)"
tags: [mocap, animation, animation-cleanup, markerless-mocap, cascadeur, fbx-pipeline, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal5-markerless-mocap-clean-up-process/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Unreal5 Markerless MoCap (CLEAN-UP Process)

**Source:** [YouTube](https://www.youtube.com/watch?v=rLPRlPlZ3Lw)
**Author:** Royal Skies
**Duration:** 3m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:07] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_000.jpg
- [1:35] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_001.jpg
- [1:40] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_002.jpg
- [1:53] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_003.jpg
- [2:02] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_004.jpg
- [2:25] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_005.jpg
- [2:41] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_006.jpg
- [3:02] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_007.jpg
- [3:13] tutorials/frames/unreal5-markerless-mocap-clean-up-process/frame_008.jpg

---

## Structured Notes

### Core Technique
Exporting a raw Unreal 5 Markerless Mocap animation as FBX, cleaning it up in the third-party tool **Cascadeur** (keyframe reduction, foot-snap, physics-assisted in-betweening), then re-importing the fixed FBX back into Unreal.

### Summary
A short workflow video (3m50s) showing what to do with a noisy/jittery clip captured via Unreal 5's Markerless Mocap feature: export it as FBX, transfer the animation onto Cascadeur's built-in UE5 mannequin, strip it down to sparse keyframes, auto-snap footsliding, use Cascadeur's physics-assist ("Tween Machine" / auto-physics) to smooth transitions while still letting the artist override specific poses, then bake and re-export back to UE5. End result is a cleaned, more physically plausible animation ready to drop back into a game project.

### Key Steps
1. In Unreal, select the raw markerless mocap animation asset → right-click → Asset Actions → Export → save as FBX.
2. In Cascadeur, import the FBX onto its built-in UE5 mannequin: select the source skeleton root in Bone mode, select the whole timeline, Ctrl+Shift+C to copy; select the UE5 mannequin root, select its timeline, Ctrl+Shift+V to paste.
3. Bake the pasted motion onto the mannequin's controls (button, top-right toolbar) to make it editable.
4. Delete "fluff" frames by scrubbing the timeline and pressing **F** on unwanted in-between frames, leaving only sparse keyframes.
5. Select all keyframes and apply **Bezier curve** smoothing to blend the remaining sparse keys together.
6. Fix foot sliding/clipping: select the toe joints on a bad frame, press **Shift+Z** to delete that joint's keyframe data — Cascadeur auto-snaps the foot back to the ground contact point (handles ~80% of foot cases automatically; remaining awkward angles need manual repositioning).
7. Manually adjust any pose that needs stylization (e.g. extending the legs further during a flip) directly on the affected frames.
8. Enable **physics assist** (Tween Machine auto-physics toggle) — Cascadeur overlays a green "physics preview" figure showing the most physically plausible in-between motion based on gravity/velocity given the current keyframes.
9. Where the physics simulation disagrees with the desired performance, mark that frame as a **priority frame** to force ("brute force") the manually-posed keyframe into the physics calculation instead of the auto-computed one.
10. **Bake to physics**, then File → Export FBX, and re-import the fixed FBX back into Unreal 5.

### UE Systems / Blueprints / Settings
- **Unreal side:** Asset Actions → Export (FBX) on an animation sequence asset; re-import of the cleaned FBX back onto the same skeleton.
- **Cascadeur (third-party, not Unreal-native):** Bone mode selection, Ctrl+Shift+C / Ctrl+Shift+V copy-paste-onto-mannequin workflow, bake-to-controls, per-frame keyframe deletion (F), Bezier curve smoothing, auto foot-snap (Shift+Z on toe joints), Tween Machine physics-assist overlay (green ghost figure), priority-frame override, bake-to-physics.
- No in-engine Control Rig / Sequencer step is shown — cleanup happens entirely outside Unreal, in Cascadeur, then round-tripped via FBX.

### Difficulty
Beginner — no Unreal editor complexity involved; the only learning curve is Cascadeur's own UI, which the video treats as quick/intuitive. Presented as a fast fix rather than a deep dive (links to the creator's separate in-depth Cascadeur video for more detail).

### UE Version
Not specified (references "Unreal 5" generically; Markerless Mocap feature matches recent UE5.x releases, e.g. 5.6/5.8).

### Tags
mocap, animation, animation-cleanup, markerless-mocap, cascadeur, fbx-pipeline, beginner

---

## Related Entries
- `tutorials/new-unreal-engine-58-metahuman-markerless-mocap-tutorial.md` — covers the UE 5.8 Markerless Motion Capture plugin that *produces* the raw footage this video cleans up; shares tags: mocap, markerless-mocap.
- `tutorials/how-to-create-fight-scenes-with-mocap-and-ai-in-unreal-engine-58---seedance-2-me.md` — an alternative animation-cleanup approach (Butterworth low-pass filtering + additive Control Rig layers, done inside Sequencer) for the same general problem (noisy mocap curves), useful to contrast with this video's external-tool (Cascadeur) approach; shares tags: mocap, animation-cleanup.
- `tutorials/cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — another beginner mocap-cleanup pipeline using Butterworth curve filtering + manual foot-plant fixes, same problem space via a different (in-Unreal) toolset.
