---
title: Realistic and Physical Lighting in UE5: The PBL Workflow
source: YouTube
url: https://www.youtube.com/watch?v=GsE0mDtxtiQ
author: arthur tasquin
ingested: 2026-06-18
ue_version: "UE5"
tags: ["lighting", "rendering", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/realistic-and-physical-lighting-in-ue5-the-pbl-workflow/
frame_count: 10
---

# Realistic and Physical Lighting in UE5: The PBL Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=GsE0mDtxtiQ)
**Author:** arthur tasquin
**Duration:** 28m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en [music] &gt;&gt; Hey there. My name is Arthur and I'm a real-time artist working in the VFX industry. This is the second video of a two-part tutorial series in which [music] we'll be talking about lighting and most specifically the science behind it. If you haven't seen the first one, I highly recommend you watch it first as we'll rely on it extensively. [music] In this video, we'll dive into the process of using physically based lighting in Unreal Engine. We'll see how the theory applies in practice, where PBL works and most importantly, [music] where it falls short. I'll explain how I personally used [music] PBL through a couple of lighting studies and try to be as transparent as possible where I deviated from it. My approach here is first and foremost cinematic. [music] I want the best-looking image straight from the engine. While I will try to be [music] as exhaustive as possible, so many things can affect your render. I will not cover color grading, materials, or local exposure, but I recommend you take some time to [music] study those as they also play a key role. At the end of this video, you'll be able to make your own PBL studies. You will know ...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-the-pbl-workflow\frame_000.jpg


---

## Structured Notes

### Core Technique
Applying Physically-Based Lighting in UE5 practice — using PBL Database plugin values in real lighting scenarios, cinematic exposure workflow, and where PBL succeeds vs. falls short.

### Summary
Part 2 of Arthur Tasquin's PBL series. Translates theory into a working UE5 lighting workflow: pulling real-world values from the PBL Database plugin, applying them to different scenario types (interior, exterior, artificial, natural), setting camera exposure via EV values, and identifying where strict PBL values must be overridden for cinematic goals.

### Key Steps
1. Open the **PBL Database** plugin panel; select matching scenario tags (interior, natural, evening, etc.)
2. Read the recommended Lux/Lumen/Candela values for the scenario and enter them into the corresponding UE light
3. Set `Directional Light` intensity using Lux values (real overcast ≈ 10,000 lx; golden hour ≈ 30,000 lx)
4. Set camera `Exposure → Manual` mode, target EV matching real-world scenario (indoor ≈ EV 8–10)
5. Iterate: compare render to reference photograph; adjust only exposure compensation, not light values, first
6. Where PBL falls short (e.g. deep interiors with no bounce), intentionally deviate — document the deviation
7. Use Sub-Level workflow from Part 1 to switch between scenario presets for lighting studies

### UE Systems / Blueprints / Settings
`PBL Database Plugin` (FAB) → real-world light value reference organized by scenario
`Directional Light → Intensity (Lux)` → solar illuminance values
`Post Process Volume → Exposure → Manual EV100` → match real-world exposure
`Rect Light / Area Light → Intensity (Lumen)` → practical light sources
`Auto Exposure` → disable during PBL workflow; use Manual EV100

### Difficulty
Intermediate

### UE Version
UE5

### Tags
lighting, rendering, intermediate

---

## Related Entries
- `tutorials/realistic-and-physical-lighting-in-ue5-what-is-pbl.md` — Part 1: theory and units
- `references/rendering-pipeline.md` — exposure, post-process, Lumen
- `references/color-pipeline.md` — color grading after PBL render