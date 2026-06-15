---
title: How I Use Lumen in AAA Projects | Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=yspmZJ6YjpM
author: Karim Yasser
ingested: 2026-06-15
ue_version: "UE 5.0+"
tags: [lumen, global-illumination, hardware-ray-tracing, project-settings, post-process, rendering, lighting, intermediate, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-use-lumen-in-aaa-projects-unreal-engine-5/
frame_count: 4
---

# How I Use Lumen in AAA Projects | Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=yspmZJ6YjpM)
**Author:** Karim Yasser
**Duration:** 7m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** April 5, 2022. This is when Lumen was firstly introduced in Android Engine 5. And since then, a lot of videos took about the requirements to have Lumen works well. And mostly they mentioned the light values, the base color values for materials, and the indirect light intensity. But if you think that these three options are the only options that control Lumen, they are completely wrong. And that's because Lumen has different types, different approaches, and that depends on the project type, the target hardware, and the specs and quality you want to get. So in this video, I will show you how I use Lumen in the Tribal A projects I work on. First of all, we need to go in project settings, then rendering, and we can scroll down here and we can see support hardware ray tracing. This is related to the project overall to support hardware ray tracing work not. So it's not only related to Lumen, but if you want to use hardware ray tracing for Lumen, you can use it. And we have mainly two things. Like as you can see here, the hardware ray tracing, and the other one, which is the cheaper option and works on why the range of hardware specs, which is the software ray tracing. So in order to use ...

**Frame:** tutorials\frames\how-i-use-lumen-in-aaa-projects-unreal-engine-5\frame_000.jpg


---

## Structured Notes

### Core Technique
AAA-grade Lumen configuration — selecting Hardware Ray Tracing vs Software Ray Tracing based on project type and target hardware, then pushing quality beyond the three commonly cited settings via Project Settings and Post Process Volume overrides.

### Summary
Karim Yasser (an AAA industry professional) walks through how Lumen is actually configured in production projects, countering the common belief that only light values, base color values, and indirect light intensity control Lumen quality. The tutorial introduces the critical fork between Hardware Ray Tracing (HWRT) and Software Ray Tracing (SWRT), explaining when each is appropriate based on platform target and quality requirements. Across three distinct scenes — warm autumn outdoor environment, nighttime urban street, and a golden-hour canal — Karim demonstrates the settings panel and Post Process Volume knobs that deliver AAA lighting results.

### Key Steps
1. **Open `Project Settings` → `Rendering` → scroll to `Support Hardware Ray Tracing`** — this is a global project toggle that enables HWRT across all systems (not just Lumen). Must restart editor after changing.
2. **Choose your Lumen ray tracing mode** — two options:
   - `Hardware Ray Tracing` (HWRT): higher quality, requires DXR-capable GPU (RTX or RDNA 3+). Traces actual geometry, not surface cache proxies.
   - `Software Ray Tracing` (SWRT): cheaper, runs on a wider range of hardware specs. Uses distance fields. Default and recommended for most projects targeting broad audiences.
3. **For HWRT: also verify `Ray Tracing` is enabled** in `Project Settings → Rendering → Ray Tracing`. HWRT for Lumen requires this base DXR support to be on.
4. **Set the Lumen method per scene via Post Process Volume** — in `Lumen Global Illumination` section, set `Lumen GI` to `Hardware Ray Tracing` or `Software Ray Tracing` to override per-volume rather than globally.
5. **Tune `Final Gather Quality`** (in PPV → Lumen GI) — controls the number of samples Lumen uses for final gather. Higher = less noise, more cost. For AAA: 2–4. Default is 1.
6. **Tune `Scene Lighting Sensitivity`** — affects how aggressively Lumen updates GI when light changes. Lower = more stable (less flickering in lit scenes). Raise only if GI is too slow to respond to fast light changes.
7. **For HWRT: set `Ray Lighting Mode`** in PPV → Lumen GI → Advanced:
   - `Surface Cache`: fast, less accurate (uses precomputed surface cache). Good for most production scenes.
   - `Hit Lighting for Reflections`: traces secondary rays to lights directly — significantly more accurate for specular, costs more. Reserve for hero shots or cinematics.
8. **Understand what the common three settings actually do** — light values (EV100 physically correct values), base color values (keep albedo below 0.9, ideally 0.4–0.85), and indirect light intensity (PPV → Global Illumination → Indirect Lighting Intensity) are prerequisites, not the full picture.
9. **Match your setup to project type** — PC AAA: HWRT + Hit Lighting for reflections. Console or wider PC: SWRT. Mobile: Lumen is not supported (use baked lighting or DFAO).

### UE Systems / Blueprints / Settings

**Project Settings → Rendering:**
- `Support Hardware Ray Tracing` → true/false (project-wide, requires restart)
- `Ray Tracing` (DXR base toggle) → must be enabled if using HWRT Lumen

**Post Process Volume → Lumen Global Illumination:**
- `Lumen GI` method → `None` / `Lumen` (uses project default) / `Hardware Ray Tracing` / `Software Ray Tracing`
- `Final Gather Quality` → 1.0 (default) to 4.0+ (AAA)
- `Scene Lighting Sensitivity` → lower = more stable, less flickering
- `Max Trace Distance` → how far Lumen traces GI rays (increase for large outdoor scenes)
- `Ray Lighting Mode` (Advanced) → `Surface Cache` (default) / `Hit Lighting for Reflections` (HWRT only, high quality)

**Post Process Volume → Lumen Reflections:**
- `Lumen Reflections` method → `Lumen` / `Hardware Ray Tracing` / `Screen Space`
- `Reflection Quality` → 1–4 (must be 4 to run HWRT reflections simultaneously with HWRT GI)
- `Ray Lighting Mode` → `Surface Cache` / `Hit Lighting for Reflections`

**Global Illumination (General):**
- `Indirect Lighting Intensity` → scales all GI bounce; raise to compensate for dark interiors
- `Diffuse Color Boost` (PPV → Lumen Advanced) → artificially brightens material colors for GI. Use sparingly — 1.5–2.0 max for indoor scenes

### Difficulty
Intermediate

### UE Version
UE 5.0+ (Lumen first introduced April 5, 2022 with UE5 launch; HWRT / SWRT distinction and PPV overrides present from UE5.0)

### Tags
`#lumen` `#global-illumination` `#hardware-ray-tracing` `#project-settings` `#post-process` `#rendering` `#lighting` `#intermediate` `#youtube` `#ue5`

---

## Frame Analysis

**frame_000 / frame_001:** UE5 editor with a large settings panel open (Project Settings or PPV details), warm golden autumn outdoor scene in the viewport — trees, buildings, afternoon/sunset sky. Shows Lumen GI settings being configured while the scene has rich indirect light bouncing.

**frame_002:** Same settings panel open but the scene is now a dark nighttime urban environment — stone-paved street, European-style buildings, low ambient light. Demonstrates configuring Lumen settings for a drastically different lighting scenario (low EV, dark materials, artificial lighting).

**frame_003:** Final high-quality result shot — golden-hour canal scene with warm orange directional light, trees, water reflections, and European buildings. Visible in the Details/right panel are post-process or actor settings. Represents the AAA quality output achievable with properly tuned Lumen.

---

## Related Entries

- [[lumen-explained---important-tips-for-ue5]] — Surface cache internals, emissive best practices, known Lumen limitations (landscape, translucency, WPO). Shares: `#lumen` `#global-illumination` `#hardware-ray-tracing`
- [[things-to-know-about-lumen-unreal-engine-5]] — Early UE5.0 Lumen project setup (DX12, HWRT toggle, VSM), indirect controls. Shares: `#lumen` `#global-illumination` `#project-settings`
- [[lighting-in-unreal-engine-5-for-beginners]] — Light values, albedo/GI bounce theory, DX12/HWRT/VSM project setup. Shares: `#lumen` `#lighting`
- [[lighting-interiors-in-unreal-engine-5]] — Lumen + HWRT for interiors, Diffuse Color Boost, Path Tracer as ground-truth validator. Shares: `#lumen` `#hardware-ray-tracing` `#lighting`
- [[designing-visuals-rendering-and-graphics-with-unreal-engine]] — Full Epic Lumen docs reference (170 pages). Shares: `#lumen` `#rendering` `#post-process`
