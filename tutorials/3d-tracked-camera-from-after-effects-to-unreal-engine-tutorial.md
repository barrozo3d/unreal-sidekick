---
title: 3D TRACKED CAMERA FROM AFTER EFFECTS TO UNREAL ENGINE | TUTORIAL
source: YouTube
url: https://www.youtube.com/watch?v=v38O-9KTqx4
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 4"
tags: [compositing, camera, vfx, after-effects, sequencer, beginner]
extraction_status: complete
frames_dir: tutorials/frames/3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial/
frame_count: 9
---

# 3D TRACKED CAMERA FROM AFTER EFFECTS TO UNREAL ENGINE | TUTORIAL

**Source:** [YouTube](https://www.youtube.com/watch?v=v38O-9KTqx4)
**Author:** Boundless Entertainment
**Duration:** 14m28s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** What's going on guys, it's Sam here and I have a tutorial for you guys today and what  we're going to be doing is taking a 3D tracked camera from After Effects and bringing it  into Unreal Engine.  So there's not a super direct way of doing this so we're going to have to go from After Effects  into Blender and then from Blender into Unreal Engine.  So you might be wondering why would I want to bring a camera from After Effects into Unreal  Engine, why not just put it into Blender and the answer is Quixel Megascans.  So like Blender, Unreal Engine is free to use and what's great about Unreal Engine is  that it has a direct connection with Quixel Megascans and what that is, it's a huge asset  library of photoscan 3D elements and these elements look incredibly realistic because  they're real objects that have been photoscaned into 3D space.  So you have access to thousands of these 3D assets.  So if you're using CGI in your film and you're trying to build a realistic world, this is  a great tool to help you to accomplish that.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_000.jpg

### Blender to Unreal Exporter [3:15]
**Transcript:** Download and install the add-on and you can then export your camera from Blender into Unreal Engine. Back in After Effects, we have our camera 3D tracked and you can now see all of the points here. Find a surface that looks like it tracked pretty well — on our foreground, find a pretty good surface. Click on these three points and then right-click and hit Create Solid and Camera. That's going to create a solid in 3D space as well as a 3D camera. Check it, render our scene and we can see it's following very nicely to that point in 3D space. Select our 3D camera again and find some points a little further away — create another solid. The point of this is we're going to have a solid in the foreground and a solid a little further away.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_001.jpg

### Blender [5:23]
**Transcript:** Jump over into Blender — go Edit > Preferences > Add-ons > Install > navigate to AE to Blend plugin folder > click AE_to_Blend.py > Install Add-on. Search "AE to blend" and check the box. The widget pops up in the bottom. We've copied our position and orientation keyframes from After Effects. Now hit Create Camera. The camera appears — hit Numpad Period to frame it. Jump back to After Effects.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_002.jpg

### Camera Properties [7:59]
**Transcript:** Focal length is 50 millimeters. Shot at 35mm but in AE camera settings it shows 37mm. Go back into Blender and set focal length to 37.1 to match AE camera. Add background image to verify alignment.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_003.jpg

### Background Image [8:34]
**Transcript:** Check Background Images > Movie Clip > Open > navigate to image sequence > Open Clip. Set End Frame to last frame with data. Repeat for the other two solids. Grid is way out of whack — we need to fix orientation. Parent everything (camera transform, foreground plane, background plane) to ground plane: select camera + planes, select ground plane last, Ctrl+P > Object. Now move all objects so the ground plane sits on the floor — the camera will follow correctly.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_004.jpg

### Exporting this Camera into Unreal Engine [10:41]
**Transcript:** Install the Blender to Unreal Engine add-on. Go to Blender for Unreal Engine menu. Get out of active camera view (hit 0). In the hierarchy, select the camera. It shows up in the export box. Set it to Export Recursive. Camera 1 is ready to be exported.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_005.jpg

### Export for Unreal Engine 4 [11:17]
**Transcript:** Export for Unreal Engine 4 > Import Sequence. Head over to Unreal Engine. In the UE scene, hit tilde (~) to bring up the console command, hit Ctrl+V and Enter. It asks to save the asset — name it (e.g. "tutorial camera") > Save. Camera now moves within the scene matching the AE track.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_006.jpg

### Compositing [12:25]
**Transcript:** Back in After Effects, import UE footage. Put footage on the bottom layer. Set quick mask on the area, set mask to Add. Copy mask from other comp, tighten + feather. Add Extract effect. Add atmosphere effects from Video Copilot. Turn off tracking solids. Shot in log format — grade in post.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_007.jpg

### Final Shot [13:23]
**Transcript:** Final shot showing the composite. Camera from After Effects through Blender into Unreal, UE rendered city into AE composite. Tutorial wraps, mentions Gemini short film in production.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_008.jpg


---

## Structured Notes

### Core Technique
Pre-Genesis AE-to-UE4 camera-tracking pipeline: 3D track in After Effects → AE-to-Blend addon bridges camera to Blender → Blender-to-UE4 addon exports the Sequencer-ready camera animation into Unreal Engine 4 → composite UE render back in AE.

### Summary
14-minute tutorial showing the full AE → Blender → UE4 camera-tracking pipeline, motivated by Quixel Megascans access (free only through UE). The workflow uses two community Blender addons as bridges: "AE to Blend" to paste AE camera keyframes into Blender, and "Blender for Unreal Engine" to export the camera as a UE Sequencer track. The final composite is assembled back in AE using log-format UE renders + masking + Video Copilot atmosphere effects.

### Key Steps
1. **After Effects — 3D Camera Track**: Track > 3D Camera Tracker; place track points on a foreground surface and a distant surface; right-click 3+ points > Create Solid and Camera; verify tracking by previewing render.
2. **Copy AE camera**: Select the 3D camera layer; copy position + orientation keyframes to clipboard (AE to Blend format).
3. **Blender — AE to Blend addon**: Edit > Preferences > Add-ons > Install > `AE_to_Blend.py` > enable. In the bottom widget, hit **Create Camera** — camera + solids import at clipboard keyframes.
4. **Match focal length**: In AE camera settings, read the focal length (e.g. 37.1mm). In Blender, set camera Focal Length to match.
5. **Background image**: Camera Properties > Background Images > Movie Clip > open image sequence; set End Frame.
6. **Fix orientation**: Select camera + all solids + ground plane; Ctrl+P > Object (parent to ground plane); move ground plane to floor — all objects follow.
7. **Blender for UE addon**: Select camera > set Export Recursive > **Export for Unreal Engine 4**.
8. **UE4 import**: Tilde (`~`) > console > Ctrl+V > Enter; name and save sequence. Camera animation now plays in UE4 Sequencer.
9. **AE composite**: Import UE render; mask + Add blend mode; Extract effect for edge keying; Video Copilot atmosphere; grade log footage in post.

### UE Systems / Blueprints / Settings
- **Sequencer camera import** — via console command (`~` + Ctrl+V); pastes FBX camera as a Sequencer track
- **Quixel Megascans** — primary motivation; free 3D scanned assets accessible through UE's Quixel Bridge
- **UE4** — tutorial targets UE4 (workflow predates UE5 and Genesis plugin)
- **Blender addons used**: AE-to-Blend (AE keyframe bridge); Blender for Unreal Engine (export recursive)
- **AE effects**: Extract (edge key), Video Copilot Atmosphere (haze/depth)
- **Log format** — shoot/render in log for grade headroom

### Difficulty
Beginner

### UE Version
UE 4

### Tags
`#compositing` `#camera` `#vfx` `#after-effects` `#sequencer` `#beginner`

---

## Related Entries
- [[unreal-engine-5-compositing-tutorial---composite-any-scene-fully-inside-of-ue5]] — updated AE track → FBX → UE5 → Image Plate workflow (supersedes this)
- [[unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in]] — fog card compositing technique in UE5
- [[unreal-engine-for-filmmakers---create-cinematic-3d-worlds-for-free-course-in-des]] — earliest Boundless video; also mentions Quixel Megascans as primary motivation
