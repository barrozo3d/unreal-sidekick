---
title: How to Remove Green Screen & Composite in Unreal Engine 5 Using Media Plate (Realistic Shadows)
source: YouTube
url: https://www.youtube.com/watch?v=771myWapQ_s
author: World Of VFX
ingested: 2026-06-16
ue_version: "UE5 (version unspecified)"
tags: [vfx, compositing, rendering, lighting, materials, beginner, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/
frame_count: 4
---

# How to Remove Green Screen & Composite in Unreal Engine 5 Using Media Plate (Realistic Shadows)

**Source:** [YouTube](https://www.youtube.com/watch?v=771myWapQ_s)
**Author:** World Of VFX
**Duration:** 9m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey what's up guys welcome back to another Unreal Engine 5 video. Today we'll talk about how you can use the green screen footage instead of Unreal Engine with the shadow. And it will be a very easy technique. So let's get started. All right, so I have downloaded a project file from Epic Games Fab. And now we need to add a plugin that is named Media Plate. And you can find this called Media Plate Beta. Make sure you turn down and restart your Unreal Engine. After that, simply click here. You can find Media Plate. Click the Media Plate here. So this will create a media plate kind of a pain in front of you. Just scale it up. Now in it to browse your footage. So first of all, I just rotate it something like this. And let's make it to 90 degree. And after that, going down, you can find this file option. Click here, browse your green screen footage. Once you browse it successfully, going up, just simply click this, open the current media. And now, boom, you can see your green screen footage. Also, the light is interacting with the environment. This is the newly launched update. You can easily use it. After that, going down, you have this option called main element. Just double-click in ...

**Frame:** tutorials\frames\how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis\frame_000.jpg


---

## Structured Notes

### Core Technique
**Media Plate Beta plugin** chroma key compositing in UE5 — stream green screen video footage directly into a UE5 scene as a real-time composited actor, with the scene's lighting and shadows naturally interacting with the footage.

### Summary
This tutorial demonstrates how to use the **Media Plate Beta** plugin to composite green screen footage into a live UE5 scene in under 10 minutes. A Media Plate actor acts as a video-streaming plane that plays back green screen footage; its built-in material (**Main Element**) handles chroma key removal. The result (visible in frame_003) is an actor integrated into an interior restaurant scene with realistic shadow casting and Lumen light interaction — no external compositing software required.

### Key Steps
1. Download and open a base scene from **Epic Games Fab** (or use any UE5 project)
2. Enable the plugin: **Edit → Plugins** → search `Media Plate Beta` → enable → restart UE
3. Place a **Media Plate** actor in the scene (Mode panel → Place Actors → search "Media Plate", or drag from Content Browser)
4. Select the Media Plate; in the **Details** panel, set rotation to **90°** so the plane faces the camera
5. Scale the Media Plate up to fill the desired screen area
6. In Details → scroll to **File** → click **Browse** → navigate to and select your green screen footage file
7. At the top of the Details panel, click **Open Current Media** — the footage begins playing on the plane (frame_001 left panel shows green screen footage on the plate)
8. Scroll down to **Main Element** in the Details panel → **double-click** to open the chroma key material in the Material Editor (frame_002)
9. In the material, configure **Chroma Key Color** (pick the green), **Key Tolerance / Softness** to remove the green while preserving edge detail
10. Return to the viewport — the composited actor appears integrated in the scene with shadow casting and Lumen light bounce (frame_003 shows the final result in the restaurant interior)

### UE Systems / Blueprints / Settings
| System / Setting | Value / Notes |
|---|---|
| Plugin | **Media Plate Beta** (Edit → Plugins; requires restart) |
| Actor | **Media Plate** — video-streaming plane with built-in chroma key material |
| Rotation | 90° to face camera |
| File browse | Details panel → File → Browse → select green screen footage |
| Open media | "Open Current Media" button at top of Media Plate Details |
| Material | **Main Element** → double-click to edit chroma key material |
| Chroma key | Configured inside Main Element material (Chroma Key Color + Tolerance/Softness) |
| Lighting | Lumen GI/reflections interact automatically with the composited media (new update feature) |
| Shadow casting | Actor casts shadows into the scene (frame_003 confirms) |

**Scene context (frame_000 & 003):** Base scene is a dark restaurant/bar interior with warm point lights, wooden furniture, and shelved bottles in the background — sourced from Epic Games Fab.

### Difficulty
Beginner — plugin-based workflow, no Blueprint or custom code required. (~9 min total)

### UE Version
**UE5** — exact sub-version not stated; the "newly launched update" comment suggests UE5.2 or UE5.3+ when Media Plate Beta was introduced.

### Tags
`#vfx` `#compositing` `#rendering` `#lighting` `#materials` `#beginner` `#youtube` `#ue5`

---

## Related Entries
- [[why-you-should-be-using-stencil-render-layers---unreal-engine-426]] — Render layer compositing with DOF/motion blur support; shares `#compositing` `#rendering`; complementary for outputting actor passes to external compositors
- [[how-to-render-cryptomatte-in-unreal-new-in-426]] — Object ID matte extraction in MRQ; shares `#compositing` `#rendering`; alternative if exporting composited plates to Nuke/AE
- [[lighting-in-unreal-engine-5-for-beginners]] — All light types + Lumen setup; shares `#lighting` `#beginner` `#ue5`; useful for setting up the scene that the composited actor will be lit by
