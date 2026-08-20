---
title: Unreal Engine Black Eye Cameras v2: Seamless gameplay cutscene transitions
source: YouTube
url: https://www.youtube.com/watch?v=lJ_1NAYtdtg
author: Black Eye Technologies
ingested: 2026-07-23
ue_version: "UE5"
tags: [black-eye-cameras, v2, camera, gameplay, cinematics, cutscene, trigger-volume, blend-list, orbit-camera, sequencer, level-sequence, gameplay-tags]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Unreal Engine Black Eye Cameras v2: Seamless gameplay cutscene transitions

**Source:** [YouTube](https://www.youtube.com/watch?v=lJ_1NAYtdtg)
**Author:** Black Eye Technologies
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:50] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_000.jpg
- [1:02] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_001.jpg
- [1:36] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_002.jpg
- [2:55] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_003.jpg
- [3:25] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_004.jpg
- [4:24] tutorials/frames/unreal-engine-black-eye-cameras-v2-seamless-gameplay-cutscene-transitions/frame_005.jpg

---

## Structured Notes

### Core Technique
Seamless gameplay-to-cutscene camera transitions using Black Eye v2: a tag-matched Black Eye trigger volume pre-aligns the player's orbit camera to a fixed world angle before a standard UE trigger volume plays the Level Sequence, and the sequence's Camera Cut section is set to "Can Blend" so it eases in from wherever the camera already is.

### Summary
Shows how to eliminate the jarring cut when gameplay hands off to a cinematic, regardless of where the player's free-look orbit is pointing. The trick is a two-zone setup: an outer Black Eye trigger volume swings the orbit camera to a known composition via fast auto-recentering, and an inner vanilla trigger volume then starts the cutscene, whose first Camera Cut blends instead of cutting. Blend timing is centralized in a Blend List data asset with per-camera and wildcard (any-to-any) entries, and everything is tuned live during PIE with real-time viewport updates.

### Key Steps
1. Duplicate the existing gameplay orbit camera (e.g. `BlackEyeOrbit_Default` → `BlackEyeOrbit_RamenAlign`) and give it a descriptive name.
2. Create a **Black Eye trigger volume** (`BlackEyeTriggerVolume_..._CameraAlign`) placed *before* the cutscene's start area, and add a new Gameplay Tag (e.g. `RamenAlign`) via its **Camera Tag** field (Add New Tag in the Gameplay Tags picker).
3. Assign the **same tag** to the duplicated camera — the tag is what links trigger volume to camera.
4. On the new camera: turn **off Auto-Activate** (only the first/default camera should auto-activate) and turn **on auto-recentering** with a very fast recenter speed — this is what swings the orbit to the target angle.
5. Set the recenter angle in **World** space (world-relative heading), then tune **Heading Center** and pitch while PIE is running. Enable the **Realtime Viewport Updates** checkbox in the Black Eye Panel so parameter drags update continuously instead of on mouse release; adjust composition and switch to a longer lens as needed.
6. Open the **Blend List** data asset (selectable via the Black Eye Panel → Manage tab): Default Camera Blend was 0.8s; add **Wildcard Blends** — *from any camera → RamenAlign* at 1.0s in-blend, and *from RamenAlign → any camera* (~2.5s / ~0.8s out). Wildcards can also be replaced by explicit camera-A→camera-B pairs.
7. Inside the align zone, place a **standard UE trigger volume** whose `On Actor Begin Overlap` plays the Level Sequence (vanilla Blueprint, nothing Black Eye-specific).
8. In Sequencer, right-click the first Camera Cut section → enable **Can Blend**, then drag the small yellow ease handle at the section's top-left inward — the cut becomes a blend from the camera's current live position. Do the same at the sequence end to blend back to the orbit camera.
9. Result: whatever angle the player approaches from, the outer volume rotates the orbit to the composed angle first, so the cutscene blend is always smooth (demonstrated by approaching from extreme side angles).

### UE Systems / Blueprints / Settings
- **Black Eye v2 plugin**: `BlackEyeOrbit` camera actors (SceneComponent + CameraComponent), `BlackEyeTriggerVolume` (BrushComponent) with Black Eye section: Camera Tag (checkbox + Gameplay Tag), Camera Reference, On Volume Enter / On Volume Leave, plus standard Collision settings.
- **Gameplay Tags** picker (Add New Tag, e.g. `RamenAlign`) links volumes to cameras.
- Camera settings used: Auto-Activate (off for secondary cameras), auto-recentering (on, fast), World-relative Heading Center, pitch, focal length/lens.
- **Black Eye Panel** (Create / Edit / Manage / Utilities tabs): Enable Debug Overlays (Subjects, Screen Guides, Camera Names, Frustums, Show Priority Stack Info, Show Camera Manager Info, Draw Camera Manager Blend Path), Realtime Viewport Updates, Preview Selected Camera, Camera Preview Size. Manage tab lists Black Eye Assets: Camera Blend Lists (`DA_BlackEye_BlendList_Default`, `DA_BEC_Blend_List`, `DA_BlackEye_Gameplay_Example_Blend_List`), Camera Managers, Player Controllers, Game Modes.
- **Blend List data asset** (`DA_BEC_Blend_List`): Default Camera Blend (Blend Time 0.8s, Hold Time 0.1s, Blend Function `VTBlend Ease In Out`, Blend Exponent 2.0); Wildcard Blends arrays "From this camera" / "To this camera" keyed by camera tag, each with Destination Cam, Blend Time, Hold Time, Blend Function, Blend Exponent.
- **PIE debug overlay**: Black Eye Priority Stack (camera, tag, ref count) and Black Eye Camera Manager View Target readouts.
- **Sequencer**: Level Sequence (`TriggerVolume_Ramen_Start_Seq`), Camera Cuts track → right-click section → **Can Blend** + yellow ease-in handle; triggered by vanilla `On Actor Begin Overlap` → Play.

### Difficulty
Intermediate

### UE Version
Not specified (UE5-era editor; Black Eye v2 targets UE 5.3+)

### Tags
black-eye-cameras, v2, camera, gameplay, cinematics, cutscene, trigger-volume, blend-list, orbit-camera, sequencer, level-sequence, gameplay-tags

---

## Related Entries
- [Unreal Engine Black Eye Cameras v2: START HERE Tutorial](unreal-engine-black-eye-cameras-v2-start-here-tutorial.md) — full 43-min v2 walkthrough; covers the same Blend List / trigger volume / Adaptive Cutscene systems in depth
- [Unreal Engine Black Eye cameras: Behind the Lens](unreal-engine-black-eye-cameras-behind-the-lens.md) — camera philosophy behind the plugin
