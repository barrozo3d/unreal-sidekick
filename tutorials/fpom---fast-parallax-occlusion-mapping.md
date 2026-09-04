---
title: FPOM - Fast Parallax Occlusion Mapping
source: YouTube
url: https://www.youtube.com/watch?v=I7LEkredBxU
author: Tore Lervik
ingested: 2026-09-04
ue_version: "UE 5.5+ (inferred)"
tags: [materials, shaders, pbr, nanite, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/fpom---fast-parallax-occlusion-mapping/
frame_count: 7
frame_status: complete
uncertainty_frames: []
frame_selection: chapter-anchored (transcript unusable -- 381 chars, hallucinated; timestamps from the video's own chapter markers)
---

# FPOM - Fast Parallax Occlusion Mapping

**Source:** [YouTube](https://www.youtube.com/watch?v=I7LEkredBxU)
**Author:** Tore Lervik
**Duration:** 2m36s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 381 chars (min 500 for 156s). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (27 chars) in 'Overview'
- WARNING: Very short transcript (29 chars) in 'Performance'

---

Frames captured — see "Captured Frames" section below.


### Overview [0:00]
**Transcript (timestamped):**
[0:00] F-4b6a-8333-9e47495743, UVs


### FPOM, POM & Nanite Displacement [0:23]
**Transcript (timestamped):**
[0:24] FPOM, FB6a-8333-9e474957, UVs
[0:34] FPOM, FB6a-8333-9e474957, UVs
[0:44] FPOM, FB6a-8333-9e474957, UVs


### Performance [0:51]
**Transcript (timestamped):**
[0:52] FPOM, FB6a-8333-9e474957, UVs


### Material function Inputs & Outputs [1:05]
**Transcript (timestamped):**
[1:06] UVs
[1:16] FPOM, FB6a-8333-9e474957, UVs
[1:26] FPOM, FB6a-8333-9e474957, UVs
[1:36] FPOM, FB6a-8333-9e474957, UVs
[1:46] FPOM, FB6a-8333-9e474957, UVs


### Chaining UVs [1:53]
**Transcript (timestamped):**
[1:56] FPOM, FB6a-8333-9e474957, UVs
[2:06] FPOM, FB6a-8333-9e4749, UVs
[2:16] FPOM, FB6a-8333-9e4749, UVs
[2:26] FPOM, FB6a-8333-9e4749, UVs



---

## Captured Frames

- [0:12] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_000.jpg
- [0:35] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_001.jpg
- [0:55] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_002.jpg
- [1:15] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_003.jpg
- [1:35] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_004.jpg
- [2:00] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_005.jpg
- [2:20] tutorials/frames/fpom---fast-parallax-occlusion-mapping/frame_006.jpg

---

## Structured Notes

### Core Technique
Using the **`MF_FastParallaxOcclusionMapping`** material function to fake surface depth from a heightmap, driving the UV/DDX/DDY of every downstream texture sample from its outputs — and chaining it after a `TextureVariation` node so tiling break-up and parallax share one consistent set of UV derivatives.

### Summary
> **No usable narration.** The ingest's transcript floor raised a CRITICAL — 381 chars
> against a 500-char minimum for 156s — and set `needs-review`. Whisper produced only a
> repeated hallucinated fragment (`"FPOM, FB6a-8333-9e474957, UVs"`) across 11 of 14
> lines. **This entry is read from frames alone**, anchored on the video's five official
> chapter markers. No `[transcript]` citation appears below because there is nothing
> reliable to cite.

A short feature demo for FPOM, a community material function for fast parallax occlusion mapping. The setup is compact: world-space XY divided by a tile-size parameter generates UVs, a heightmap texture object feeds the function, and the function's `UV`, `DDX` and `DDY` outputs then drive *every* subsequent texture sample so colour and normal stay in lockstep with the parallaxed coordinates. Its `Pixel Depth Offset` output goes to the material's matching pin, which is what makes the illusion hold at silhouettes. The final chapter chains a `TextureVariation` node in front of it, passing that node's `Shifted UVs`/`DDX`/`DDY` into the function so tiling break-up happens *before* the parallax step rather than fighting it.

### Key Steps
1. **Generate tiling UVs from world space.** `Absolute World Position` → `XY` → `Divide`, with the divisor coming from a `Tile Size` scalar parameter (default `400.0`) `[frame_003]`. World-space UVs mean the material tiles consistently regardless of mesh UVs.
2. **Supply the heightmap** as a `Param (Tex Object)` named `Height`, with `UVs 0` and `Apply View MipBias` `[frame_003]`.
3. **Feed `MF_FastParallaxOcclusionMapping`.** Its inputs are `UV (V2)`, `Height Texture (T2d)`, `DDX (V2)`, `DDY (V2)`, `HeightRatio (S)`, `HeightCenter (S)`, `Height Texture Channel (V4)`, `AxisU (V3)`, `AxisV (V3)`, `IsDecal (SB)` and `IsTiling (SB)` `[frame_003]`.
4. **Route all four outputs, not just the UV.** The function returns `UV`, `DDX`, `DDY` and `Pixel Depth Offset` `[frame_003]`.
5. **Drive every texture sample from those outputs.** Both the `Color` and `Normal` `Param2D` samplers take `UVs` from the function's `UV`, plus `DDX(UVs)` and `DDY(UVs)` from its derivative outputs `[frame_003]`. Passing explicit derivatives is what keeps mip selection correct once UVs are being displaced per-pixel.
6. **Wire `Pixel Depth Offset`** from the function into the material's `Pixel Depth Offset` pin `[frame_003]` — this is what makes the parallaxed surface intersect correctly with other geometry rather than looking painted on.
7. **The `(SB)` inputs take static bools.** Searching `stati` in the graph offers `StaticBool` and `StaticSwitch` functions plus `StaticBoolParameter` and `StaticSwitchParameter` `[frame_004]`; `IsDecal` and `IsTiling` are compile-time switches, not runtime values.
8. **Chain `TextureVariation` in front of it** to break up tiling. That node's inputs are `Heightmap (T2d)`, `UVs (V2)`, `Variation Scale (S)`, `Variation Levels (S)`, `Heightmap Influence (S)`, `Mask Channel (V4)`, `Use Dither (SB)`, `Random Rotation and Scale (SB)` and `HQ Edge Comparison (SB)`; it outputs `Shifted UVs`, `Raw UVs`, `DDX`, `DDY` and `Random Offset` `[frame_006]`.
9. **Pass the chained triplet through.** `TextureVariation`'s `Shifted UVs` → FPOM's `UV`, and its `DDX`/`DDY` → FPOM's `DDX`/`DDY` `[frame_006]`. A `Static Bool (True)` drives `Use Dither` `[frame_006]`. This is the "Chaining UVs" chapter: the variation node must supply the derivatives too, or the parallax step will sample the wrong mips.
10. **Expect stepping at grazing angles.** The demo surface shows visible layer-stepping on distant rocks — the characteristic POM artefact where ray-march step count runs out `[frame_001]`.

### UE Systems / Blueprints / Settings
- **`MF_FastParallaxOcclusionMapping`** (material function) — in: `UV (V2)`, `Height Texture (T2d)`, `DDX (V2)`, `DDY (V2)`, `HeightRatio (S)`, `HeightCenter (S)`, `Height Texture Channel (V4)`, `AxisU (V3)`, `AxisV (V3)`, `IsDecal (SB)`, `IsTiling (SB)`; out: `UV`, `DDX`, `DDY`, `Pixel Depth Offset` `[frame_003]`
- **`TextureVariation`** (material function) — in: `Heightmap (T2d)`, `UVs (V2)`, `Variation Scale (S)`, `Variation Levels (S)`, `Heightmap Influence (S)`, `Mask Channel (V4)`, `Use Dither (SB)`, `Random Rotation and Scale (SB)`, `HQ Edge Comparison (SB)`; out: `Shifted UVs`, `Raw UVs`, `DDX`, `DDY`, `Random Offset` `[frame_006]`
- **UV generation** — `Absolute World Position` (`XY`) → `Divide` ← `Tile Size` scalar param, `Default Value 400.0` `[frame_003][frame_006]`
- **Texture inputs** — `Height` (Param Tex Object), `Color` and `Normal` as `Param2D` samplers with `UVs` / `DDX(UVs)` / `DDY(UVs)` / `Apply View MipBias` `[frame_003]`
- **Static switch types available** — `StaticBool`, `StaticSwitch`, `StaticBoolParameter`, `StaticSwitchParameter` `[frame_004]`
- **Material output** — `M_My_Material`; `Roughness` fed by a `0.9` constant; `Pixel Depth Offset` and `Displacement` pins present `[frame_003]`
- **Measured GPU cost** `[frame_002]` — frame `[TOTAL]` avg `10.60 ms` (max `10.96`, min `10.20`); `Basepass` avg **`0.06 ms`**; `Nanite BasePass` `0.64 ms`; `TemporalSuperResolution` `2.21 ms`; `LumenScreenProbeGather` `2.23 ms`; `Shadow Projection` `0.88 ms`
- **Chapters** — Overview, FPOM/POM & Nanite Displacement, Performance, Material function Inputs & Outputs, Chaining UVs

> **What the frames cannot supply.** The chapter "FPOM, POM & Nanite Displacement" is
> plainly a comparison between the three approaches, but with no narration and no on-screen
> text there is **no record of what that comparison concluded** — which is faster, which is
> recommended, or under what conditions. Likewise the numeric defaults for `HeightRatio`,
> `HeightCenter`, `Variation Scale` and `Variation Levels` are never shown expanded. Treat
> this entry as an accurate map of the function's *interface* and wiring, not as guidance
> on tuning it. The GPU counters in `[frame_002]` are the one hard performance datum
> available, and they are a scene total rather than an isolated cost for the function.
>
> **Where FPOM comes from** is not recoverable from the video itself — no on-screen URL or
> attribution appears in the sampled frames. It is a third-party material function, not
> stock Unreal content, so a reader will need to source it separately.

### Difficulty
Intermediate

### UE Version
Not stated. The material output node exposes a **`Displacement`** pin alongside Substrate-era pins (`Surface Thickness`, `Front Material`) `[frame_003]`, and the GPU counters list `Nanite BasePass`, `Nanite VisBuffer` and `Nanite Readback` `[frame_002]` — together indicating **UE 5.5 or newer**. Recorded as an inference from the UI, not a confirmed version.

### Tags
materials, shaders, pbr, nanite, rendering, intermediate

---

## Related Entries
- [Nanite: Everything You Should Know [Unreal Engine 5]](nanite-everything-you-should-know-unreal-engine-5.md) — the "FPOM, POM & Nanite Displacement" chapter weighs this function against Nanite displacement; shares nanite, rendering
- [How to Transform TEXTURE COORDINATES in Unreal Engine Materials (Tutorial)](how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial.md) — the UV-manipulation groundwork this function consumes and returns; shares materials, shaders
- [I Textured The Entire Environment Using a SINGLE Texture](i-textured-the-entire-environment-using-a-single-texture.md) — tiling break-up from one texture, the same problem the chained TextureVariation node solves here; shares materials, shaders
