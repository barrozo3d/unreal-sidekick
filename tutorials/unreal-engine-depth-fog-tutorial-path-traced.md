---
title: Unreal Engine Depth Fog TUTORIAL [Path Traced]
source: YouTube
url: https://www.youtube.com/watch?v=0ltfUCHwevY
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [fog, rendering, path-tracing, materials, post-process, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/
frame_count: 6
---

# Unreal Engine Depth Fog TUTORIAL [Path Traced]

**Source:** [YouTube](https://www.youtube.com/watch?v=0ltfUCHwevY)
**Author:** Boundless Entertainment
**Duration:** 9m6s | 6 section(s)

---

## Structured Notes

### Core Technique
Path Tracer-compatible depth fog using a Post Process Volume + custom Post Process material. Exponential Height Fog is incompatible with Path Tracing; this PPV material workaround produces distance-based fog that works in both Lit and Path Tracing render modes.

### Summary
9-minute tutorial solving the Path Tracer's incompatibility with Exponential Height Fog. The workaround: create a custom material with Material Domain = Post Process + Blendable Location = Before Tone Mapping, using the Scene Depth node to compute per-pixel fog density based on distance from camera, then assign this material to a Post Process Volume (Infinite Extent = true). Parameters: Density/Opacity scalar controls fog thickness; Distance scalar controls start depth (how far from camera fog begins); Color vector for fog tint. The result works identically in Lit mode and Path Tracing mode.

### Key Steps
1. **Add Post Process Volume** — Place Actors > Post Process Volume; Details > Infinite Extent (Unbound) = true (extends PPV to whole scene)
2. **Assign material slot** — PPV Details > Blendables > search "Material"; click + > add array element; set to Asset Reference > drag your fog material into the slot
3. **Create fog material** — Content Browser > right-click > Material > name "Fog"; double-click to open Material Editor
4. **Set Material Domain** — Material Details (right panel) > Material Domain = Post Process (not Surface); this restricts outputs to Emissive Color only and targets the post process pipeline
5. **Set Blendable Location** — Material Details > Blendable Location = Before Tone Mapping (not After); "Before" = correct fog density response in both Lit and PT modes; "After" causes wrong behavior in Lit mode
6. **Build fog graph** — nodes: Scene Depth → manipulate (scale by Distance parameter, raise to power, multiply by Opacity/Density) → Lerp (A=original color via Scene Texture, B=fog color vector) → Emissive Color
7. **Expose parameters** — create Scalar Parameters: "Distance" (controls fog start depth in world units; 5000 = distant fog, 1000 = thick near fog); "Density/Opacity" (fog strength 0–1); Vector Parameter: "Fog Color" (default = white/grey)
8. **Apply and test** — save; toggle Path Tracing on/off to verify fog appears in both modes; adjust Distance + Density to taste

### UE Systems / Settings
- **Post Process Volume (PPV)** — scene-wide post-processing; Infinite Extent = unbound (applies everywhere); Blendables array: add Post Process materials for custom screen-space effects
- **Material Domain: Post Process** — makes material apply as a full-screen pass after rendering; only Emissive Color output; runs per-pixel in screen space
- **Blendable Location: Before Tone Mapping** — applies material before the tone mapping pass; required for correct color response in PT and Lit modes; "After Tone Mapping" can cause unintended contrast changes
- **Scene Depth node** — Material node that outputs the depth (distance from camera) of each pixel; used to compute distance-based effects (fog, depth of field, atmosphere)
- **Exponential Height Fog limitation** — UE5 native fog system; does NOT work in Path Tracing mode; this PPV material method is the standard workaround

### Difficulty
Intermediate

### UE Version
UE 5.x (Path Tracer era)

### Tags
`#fog` `#rendering` `#path-tracing` `#materials` `#post-process` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_000.jpg
- [0:50] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_001.jpg
- [1:21] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_002.jpg
- [2:55] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_003.jpg
- [6:50] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_004.jpg
- [8:34] tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/frame_005.jpg

## Related Entries
- [[unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came]] — Exp Height Fog for Lit mode (when PT not needed)
- [[best-settings-for-unreal-engine-56---perfect-renders-every-time]] — LightForge automates path tracer setup
- [[how-to-make-your-unreal-engine-renders-look-real]] — other PPV-based cinematic effects
- [[easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing]] — Path Tracing setup companion
