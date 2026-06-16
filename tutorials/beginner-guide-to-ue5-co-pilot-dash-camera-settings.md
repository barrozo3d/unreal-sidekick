---
title: Beginner Guide to UE5 Co-Pilot DASH Camera Settings
source: YouTube
url: https://www.youtube.com/watch?v=00kSXM3b788
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.3
ue_version: "UE 5.x"
tags: [dash-1.3, camera, dof, color-grading, post-process, cinematics, beginner]
extraction_status: complete
frames_dir: tutorials/frames/beginner-guide-to-ue5-co-pilot-dash-camera-settings/
frame_count: 15
---

# Beginner Guide to UE5 Co-Pilot DASH Camera Settings

**Source:** [YouTube](https://www.youtube.com/watch?v=00kSXM3b788)
**Author:** Polygonflow Dash
**Duration:** 3m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Greetings I'm Jonathan polygon flow's Community director for dash our next gen plug-in for Unreal Engine that makes creating environments a total Breeze in this video I'm going to go over the camera tool one of many new tools that we've updated and upgraded for dash 1.3 the latest release as of this video Let's dive into it and see what it can do I'll use a pre-made environment that I've already created for the scene with a lot of Dash placed foliage that will make it easier to Showcase how the camera system works in unreal so let's start by opening dash and then type camera into the prompt bar this will create a camera and automatically pops up the options menu to adjust settings within it now let's start with the camera tool itself focal length determines the zoom of the lens which is how close the subject of the camera will appear in the viewport the larger the focal length the more the camera Zooms in aperture controls the size of the camera lens low aperture values decrease the depth of field which is the range at which the image can be in focus a larger aperture is a smaller number a smaller aperture is a large larger number aperture combined with ...

**Frame:** tutorials\frames\beginner-guide-to-ue5-co-pilot-dash-camera-settings\frame_000.jpg


---

## Structured Notes

### Core Technique
Dash 1.3 Camera Tool: type `camera` → CineCameraActor spawns with Dash settings panel; set focal length (zoom), aperture (DOF size), focus distance (DOF target), post-process FX (color grading, bloom, vignette, film grain, chromatic aberration), and LUT presets for final look.

### Summary
4-minute camera settings beginner guide (Dash 1.3) by Jonathan. Covers the Dash camera creation flow: type `camera` → settings panel auto-opens. Explains all key params: Focal Length (zoom), Aperture (DOF range — lower number = larger aperture = shallower DOF), Focus Distance (target Z), Post-Process FX block (color grading, bloom, vignette, film grain, chromatic aberration), and LUT preset cycling for color grade. Part of the Dash 1.3 update highlight series. Frame count 15 indicates extensive visual coverage of all parameters.

### Key Steps
1. **Create camera** — open Dash → type `camera` → CineCameraActor spawns + Dash camera settings panel opens automatically.
2. **Focal Length** — zoom of lens; higher = more zoom/telephoto compression.
3. **Aperture** — controls DOF breadth; lower number = larger aperture = shallower DOF (more blur); higher number = smaller aperture = more in focus.
4. **Focus Distance** — distance from camera to focus plane; objects at this distance are sharp.
5. **Post-Process FX** — color grading sliders, bloom intensity, vignette amount, film grain, chromatic aberration.
6. **LUT presets** — cycle through pre-made color grading LUT presets for cinematic looks.
7. **Position camera** — move/rotate in viewport to frame shot; settings update live.

### UE Systems / Blueprints / Settings
- **Dash Camera Tool (1.3 update)** — spawns CineCameraActor; inline settings panel in Dash UI; all params live-update
- **Focal Length** — mm-equivalent zoom; larger = telephoto compression
- **Aperture (f-stop)** — lower number = larger aperture = shallower DOF; counterintuitive: f/1.4 = very blurry background, f/16 = all in focus
- **Focus Distance** — Z distance for focus plane; set to hero subject distance
- **Post-Process** — color grading, bloom, vignette, film grain, chromatic aberration — all in Dash panel
- **LUT presets** — built-in cinematic color grading looks; cycleable from Dash panel

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.3)

### Tags
`#dash-1.3` `#camera` `#dof` `#color-grading` `#post-process` `#cinematics` `#beginner`

---

## Related Entries
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 camera with image-based color grade extraction
- [[how-to-create-a-cinematic-archviz-render-with-ue5-dash]] — cinematic rendering with camera settings
- [[quick-environment-creation-w-unreal-engine-5]] — camera-first workflow principle + LUT grading
- [[new-ue5-plugin---easy-environment-creation]] — camera aperture/focal distance for DOF on hero subjects
