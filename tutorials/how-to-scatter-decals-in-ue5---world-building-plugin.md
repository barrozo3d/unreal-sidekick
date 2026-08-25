---
title: How to Scatter Decals in UE5 - World Building Plugin
source: YouTube
url: https://www.youtube.com/watch?v=IU8VFAXOa7w
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, decals, scatter, placement-tool, environment-art, detail, beginner]
extraction_status: complete
frames_dir: tutorials/frames/how-to-scatter-decals-in-ue5---world-building-plugin/
frame_count: 4
---

# How to Scatter Decals in UE5 - World Building Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=IU8VFAXOa7w)
**Author:** Polygonflow Dash
**Duration:** 5m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Greetings, I'm Jonathan, Polygonflow's Community Director. Today I'm covering Decal Scattering, one of the many incredible tools available in Polygonflow's Dash, our next Gen Unreal Engine plugin. If you want to create environments featuring heavy use of Decals to break up repetition, this video is for you. I'll start by opening Dash, then move it out of the Unreal Viewport. Select the Content Library and find a Decal that you'd like to work with. Decals can be selected and dragged directly into the world. Dash will automatically align the Decal to the surface of any object. You can also adjust how the Decal is rotated, scaled, and placed at any point prior to hitting Enter. The little Quick Tip menu covers all aspects of the placement tool. The Decal placement in Dash is super robust, making it very easy to place Decals precisely. But what if you want to scatter those Decals instead? That is where Dash really shines. Using the Content Browser, hold Shift and select multiple Decals, then hold Ctrl and drag those Decals into the world. Then select scatter here, and watch the magic unfold. There's a wide array of options available for the decal scatter.

**Frame:** tutorials\frames\how-to-scatter-decals-in-ue5---world-building-plugin\frame_000.jpg


---

## Structured Notes

### Core Technique
Dash decal workflow: single decal drag-and-drop with auto surface alignment + modifier keys for precise placement, OR multi-select decals + Ctrl+drag → Scatter Here for area decal scatter with density/scale/rotation controls.

### Summary
5-minute decal scattering tutorial (Dash 1.4 era) by Jonathan. Two workflows: (1) Single decal placement — drag from Content Library → auto-aligns to surface; rotate/scale/position with modifier keys before confirming with Enter; (2) Multi-decal scatter — Shift-select multiple decals in Content Library → Ctrl+drag → Scatter Here → full surface scatter panel with density, scale, rotation, masking options. Ideal for breaking up surface repetition with stains, cracks, grunge, footprints etc.

### Key Steps
1. **Single decal placement** — Content Library → find decal → drag into viewport → Dash auto-aligns to surface; use placement modifier keys (Shift=rotate, Ctrl=scale, etc.) → Enter to confirm.
2. **Multi-decal scatter** — Content Library → hold Shift + click multiple decals → hold Ctrl + drag into viewport → select Scatter Here.
3. **Scatter settings** — density, min/max scale, rotation jitter, masking — same surface scatter options apply to decals.
4. **Use case** — stains, cracks, grunge, wet patches, footprints, road markings; scatter across floors, roads, walls for surface variation.

### UE Systems / Blueprints / Settings
- **Dash Decal Placement** — drag from Content Library; auto surface-alignment; modifier keys for rotation/scale (same as mesh placement); Enter = confirm
- **Multi-decal Scatter** — Shift-select multiple decals + Ctrl+drag → Scatter Here; same scatter panel as mesh scatter
- **Scatter settings for decals** — density, min/max scale, rotation jitter, proximity/object masking — all applicable to decals

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.4 era)

### Tags
`#dash-1.4` `#decals` `#scatter` `#placement-tool` `#environment-art` `#detail` `#beginner`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:30] tutorials/frames/how-to-scatter-decals-in-ue5---world-building-plugin/frame_000.jpg
- [1:30] tutorials/frames/how-to-scatter-decals-in-ue5---world-building-plugin/frame_001.jpg
- [2:46] tutorials/frames/how-to-scatter-decals-in-ue5---world-building-plugin/frame_002.jpg
- [4:01] tutorials/frames/how-to-scatter-decals-in-ue5---world-building-plugin/frame_003.jpg

## Related Entries
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — full surface scatter system (masking, rotation, etc.)
- [[beginner-content-library-tutorial-for-ue5]] — content library placement modifier keys
- [[introducing-dash-for-unreal-engine-5]] — decal placement in original Dash intro
- [[create-run-down-environments-in-minutes---dash-ue5]] — decal scatter for run-down environment detailing
