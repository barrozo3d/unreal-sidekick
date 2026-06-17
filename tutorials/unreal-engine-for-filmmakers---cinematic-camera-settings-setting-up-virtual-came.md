---
title: Unreal Engine for Filmmakers - Cinematic Camera Settings & Setting up Virtual Camera
source: YouTube
url: https://www.youtube.com/watch?v=gFO0qhdLKec
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [camera, cinematography, lighting, fog, rendering, composition, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came/
frame_count: 9
---

# Unreal Engine for Filmmakers - Cinematic Camera Settings & Setting up Virtual Camera

**Source:** [YouTube](https://www.youtube.com/watch?v=gFO0qhdLKec)
**Author:** Boundless Entertainment
**Duration:** 14m44s | 9 section(s)

---

## Structured Notes

### Core Technique
Cinematic camera configuration in UE5: Focal Length, Filmback sensor size, Bloom, Chromatic Aberration, Exponential Height Fog, frame rate (23.976 + 180-degree shutter) and composition principles for depth layering.

### Summary
15-minute guide on making UE5 renders look cinematic. Covers: longer focal length (47mm vs 24mm) compresses depth making distant objects read closer — classic film look; Filmback presets (16x9 SLR = larger virtual sensor = wider natural FOV at same focal length); Bloom (3) for filmic highlight glow; Chromatic Aberration (0.4–0.5) for organic lens imperfection; Exponential Height Fog for atmospheric depth (near = dark/clear, far = hazy); frame rate = 23.976 FPS mandatory for cinematic motion blur (60+ FPS = video game look); composition rules: foreground + midground + background layering, leading lines, shooting along walls/objects that recede into the scene.

### Key Settings
1. **Focal Length** — 47mm collapses depth (objects behind read closer, more compressed); 24mm = wide, more depth visible; longer lens = fewer perspective distortion artifacts on architecture; Cine Camera Actor > Filmback > Focal Length
2. **Filmback sensor** — Cine Camera Actor > Filmback > Sensor preset; "16x9 Digital Film" = smaller virtual sensor (narrower FOV); "16x9 SLR" = larger sensor (wider FOV at same focal length, simulates full-frame); the larger the sensor, the shallower DOF at same f-stop
3. **Bloom** — Post Process > Lens > Bloom > Intensity = ~3; adds filmic highlight glow/roll-off around bright light sources; too high = over-blown (keep subtle)
4. **Chromatic Aberration** — Post Process > Lens > Chromatic Aberration > Intensity = 0.4–0.5; adds subtle color channel fringing at image edges; organic lens imperfection; avoid going above 1.0
5. **Exponential Height Fog** — adds depth cues: near objects = darker/clearer, distant objects = hazy; use Fog Density 0.05–0.1; Height Falloff = 2 keeps fog near ground; always add for cinematic depth
6. **Frame rate** — Sequencer > settings = 23.976 FPS; 180-degree shutter angle for correct motion blur (Shutter Speed = 2x frame rate = ~1/48 sec); avoid 60+ FPS for cinematics (looks like a video game cutscene)
7. **Composition** — place foreground elements close to camera; mid-ground elements to fill space; far background (city, mountains); leading lines (walls, railings, roads) that recede into the image; without foreground the scene appears flat

### UE Systems / Settings
- **Cine Camera Actor** — Place Actors > Camera > Cine Camera Actor; has Filmback, Current Focal Length, Current Aperture, Focus Distance, Post Process Settings
- **Filmback Presets** — Cine Camera > Filmback > Sensor preset dropdown; controls virtual sensor size; affects FOV and DOF at given focal length
- **Post Process Settings (per-camera)** — applies bloom, chromatic aberration, vignette, DOF directly to specific camera without needing a PPV
- **Exponential Height Fog** — Place Actors > Lights > Exp Height Fog; Fog Density, Fog Height Falloff, Fog Inscattering Color; does NOT work with Path Tracer (see depth-fog-path-traced tutorial for PT workaround)
- **Level Sequence frame rate** — Sequencer settings: Playback > Frame Rate = 23.976; lock this before animating camera moves

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
`#camera` `#cinematography` `#lighting` `#fog` `#rendering` `#composition` `#beginner`

---

## Related Entries
- [[unreal-engine-depth-fog-tutorial-path-traced]] — depth fog workaround for Path Tracer
- [[how-to-make-your-unreal-engine-renders-look-real]] — film emulation (bloom, grain, halation)
- [[the-simplest-rendering-trick-90-of-unreal-artists-miss]] — chromatic aberration + physical camera imperfections
- [[unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic]] — lighting companion (night scene, god rays)
