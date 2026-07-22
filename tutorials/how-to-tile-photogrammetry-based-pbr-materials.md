---
title: How to tile photogrammetry based PBR materials
source: YouTube
url: https://www.youtube.com/watch?v=q0TaRbtE4xU
author: Grzegorz Baran
ingested: 2026-07-21
ue_version: "N/A (DCC-side: ZBrush / Substance Painter / Substance Designer / Marmoset)"
tags: [materials, pbr, pipeline, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to tile photogrammetry based PBR materials

**Source:** [YouTube](https://www.youtube.com/watch?v=q0TaRbtE4xU)
**Author:** Grzegorz Baran
**Duration:** 26m51s | 53 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'To capture the first surface I took 65 images'
- **CRITICAL:** Empty transcript in chapter 'I used the monopod to stabilise the camera. Entire capture process took me about 5 minutes'
- **CRITICAL:** Empty transcript in chapter 'The next step is to position it over the highpoly surface to cover the space I want to be baked into the texture later'
- **CRITICAL:** Empty transcript in chapter 'This part is very important from tiling and seam removal point of view'
- **CRITICAL:** Empty transcript in chapter 'The better and more accurate it is done, the less work has to be done in actual seam removal pass'
- **CRITICAL:** Empty transcript in chapter 'to be even more accurate 1 modify the lowpoly mesh with the Move brush'
- **CRITICAL:** Empty transcript in chapter 'As baking part is irrelevant for this tutorial I will speed this up.'
- **CRITICAL:** Empty transcript in chapter 'Just to mention for baking I usually use Substance Designer baker'
- **CRITICAL:** Empty transcript in chapter 'And this is the proper part of this tutorialthe one where tiling and seam removal happens :'
- **CRITICAL:** Empty transcript in chapter 'To remove seams and tweak/rearrange the texture I use Substance Painter and it's Clone tool'
- **CRITICAL:** Empty transcript in chapter 'The first step is to load all baked textures with the tiling plane. The tiling plane is the one I use to preview how tiling goes and help to tile the edges'
- **CRITICAL:** Empty transcript in chapter 'I usually use the plane which covers additional 20% of space on each side'
- **CRITICAL:** Empty transcript in chapter 'With all textures loaded (they appear in the Project shelf) I define material channels I want to tile'
- **CRITICAL:** Empty transcript in chapter 'Next I fill the channels with proper maps'
- **CRITICAL:** Empty transcript in chapter 'To get seams in the middle of UV space I offset the texture to 0.5 in both directions'
- **CRITICAL:** Empty transcript in chapter 'I usually use the 2D view to remove main seams and do tweaks in 3D view later'
- **CRITICAL:** Empty transcript in chapter 'Before I start'l create Paint Layer and apply Passthrough' mode for each channel I want to be affected by the Clone tool'
- **CRITICAL:** Empty transcript in chapter 'Next with the 'Paint' layer selected I activate the Clone tool'
- **CRITICAL:** Empty transcript in chapter 'I mark 'good' areas I want to copy from by selecting them with 'V button pressed'
- **CRITICAL:** Empty transcript in chapter 'It is good practice to preview how material reacts by previewing light direction changes...'
- **CRITICAL:** Empty transcript in chapter 'It is important to keep the surface's the flow and logic'
- **CRITICAL:** Empty transcript in chapter 'Light behavior preview is very important when dealing with textures like this one'
- **CRITICAL:** Empty transcript in chapter 'And the main tiling is done!'
- **CRITICAL:** Empty transcript in chapter 'Height map sucks but no worries, I am going to use it only as visual reference later while generating the proper one from bent normal.'
- **CRITICAL:** Empty transcript in chapter 'The next step involves Substance Designer'
- **CRITICAL:** Empty transcript in chapter 'To do that just simply paste the file into the directory with exported maps and open it.'
- **CRITICAL:** Empty transcript in chapter 'On this stage I usually preview how material tiles itself in 2D window by pressing 'SPACE BAR'
- **CRITICAL:** Empty transcript in chapter 'if tiling is too obvious. I tweak Equalizer values until it is not.'
- **CRITICAL:** Empty transcript in chapter 'Looks like turning the height map off solves the issue'
- **CRITICAL:** Empty transcript in chapter 'A few more checks to make sure everything else looks fine'
- **CRITICAL:** Empty transcript in chapter 'Now it is the time to do the final test of the rule of 3' by using '3D View' preview window'
- **CRITICAL:** Empty transcript in chapter 'Next I did a fast check is there anything else which attracts my attention and since it was not I re-exported the textures'
- **CRITICAL:** Empty transcript in chapter 'The last thing left for tweaking is the generated height map, since it feels a bit noisy while previewed'
- **CRITICAL:** Empty transcript in chapter 'Final color luminosity tweaks to to make sure RGB range is filled properly. This is where 'Histogram' preview window is very helpful'
- **CRITICAL:** Empty transcript in chapter 'And this is where the tiling process is done and entire material is finished and ready to export'
- **CRITICAL:** Empty transcript in chapter 'I usually do one more test in Marmoset Toolbag. This is also where I do my renders to present and compare material in my library later. If material looks fine there it should be ok everywhere else'
- **CRITICAL:** Empty transcript in chapter 'This is also the moment to do the last check how material reacts to any light changes and how it tiles'
- **CRITICAL:** Empty transcript in chapter 'It was enough to use the monopod to stabilise the camera and still get image quality useful for high quality photogrammetry reconstruction'
- **CRITICAL:** Empty transcript in chapter 'same as before I trimmed the highpoly model below 67min as FBX struggles to hold vertex color information for everything above. I did it by trimming useless edges.'
- **CRITICAL:** Empty transcript in chapter 'To get a bit more accuracy I changed the lowpoly mesh density to be a bit denser as with the previous material'
- **CRITICAL:** Empty transcript in chapter 'Next T adjusted the scale and direction of lowpoly to match the pattern flow'
- **CRITICAL:** Empty transcript in chapter 'Same as before, time spent on this stage can save a lot of time and effort later.'
- **CRITICAL:** Empty transcript in chapter 'Brick pattern under the each edge has to match to the one on the opposite side as close as possible'
- **CRITICAL:** Empty transcript in chapter 'Now when the plane is set time for micro adjustments with the Move brush'
- **CRITICAL:** Empty transcript in chapter 'On this stage lowpoly plane matches the pattern good enough to be used for baking.'
- **CRITICAL:** Empty transcript in chapter 'I set offset to 0.5 to get seam in the middle of texture's space since it is easier to find and deal with'
- **CRITICAL:** Empty transcript in chapter 'Pattern is slightly shifted but it is nothing that cannot be fixed in Substance Designer with the Clone tool.'
- **CRITICAL:** Empty transcript in chapter 'Same as before exported textures were loaded into the Substance Designer and tweaked using the same graph as before this time without height map on input'
- **CRITICAL:** Empty transcript in chapter 'Color distribution check-on histogram'
- **CRITICAL:** Empty transcript in chapter 'and that's it! Material is ready to export and the final check in Marmoset Toolbag'
- **CRITICAL:** Empty transcript in chapter 'Environment PBR Texture Creation Using Photogrammetry'
- **CRITICAL:** Total transcript only 40 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (14 chars) in '<Untitled Chapter 1>'
- WARNING: Very short transcript (26 chars) in 'The process is exactly the same as before. I simply copy material from a 'good' spot and apply it into the broken one by seam'

---

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] 邁The Pantheon,


### To capture the first surface I took 65 images [0:41]

### I used the monopod to stabilise the camera. Entire capture process took me about 5 minutes [0:50]

### The next step is to position it over the highpoly surface to cover the space I want to be baked into the texture later [3:06]

### This part is very important from tiling and seam removal point of view [3:29]

### The better and more accurate it is done, the less work has to be done in actual seam removal pass [3:53]

### to be even more accurate 1 modify the lowpoly mesh with the Move brush [4:05]

### As baking part is irrelevant for this tutorial I will speed this up. [4:46]

### Just to mention for baking I usually use Substance Designer baker [4:57]

### And this is the proper part of this tutorialthe one where tiling and seam removal happens : [5:13]

### To remove seams and tweak/rearrange the texture I use Substance Painter and it's Clone tool [5:20]

### The first step is to load all baked textures with the tiling plane. The tiling plane is the one I use to preview how tiling goes and help to tile the edges [5:28]

### I usually use the plane which covers additional 20% of space on each side [5:37]

### With all textures loaded (they appear in the Project shelf) I define material channels I want to tile [5:47]

### Next I fill the channels with proper maps [5:57]

### To get seams in the middle of UV space I offset the texture to 0.5 in both directions [6:40]

### I usually use the 2D view to remove main seams and do tweaks in 3D view later [7:08]

### Before I start'l create Paint Layer and apply Passthrough' mode for each channel I want to be affected by the Clone tool [7:17]

### Next with the 'Paint' layer selected I activate the Clone tool [7:26]

### I mark 'good' areas I want to copy from by selecting them with 'V button pressed [7:55]

### It is good practice to preview how material reacts by previewing light direction changes... [8:31]

### It is important to keep the surface's the flow and logic [9:22]

### Light behavior preview is very important when dealing with textures like this one [10:01]

### And the main tiling is done! [12:07]

### Height map sucks but no worries, I am going to use it only as visual reference later while generating the proper one from bent normal. [12:16]

### The next step involves Substance Designer [12:59]

### To do that just simply paste the file into the directory with exported maps and open it. [13:10]

### On this stage I usually preview how material tiles itself in 2D window by pressing 'SPACE BAR [13:27]

### if tiling is too obvious. I tweak Equalizer values until it is not. [13:37]

### Looks like turning the height map off solves the issue [15:26]

### A few more checks to make sure everything else looks fine [15:51]

### Now it is the time to do the final test of the rule of 3' by using '3D View' preview window [16:32]

### Next I did a fast check is there anything else which attracts my attention and since it was not I re-exported the textures [17:05]

### The last thing left for tweaking is the generated height map, since it feels a bit noisy while previewed [17:30]

### Final color luminosity tweaks to to make sure RGB range is filled properly. This is where 'Histogram' preview window is very helpful [18:22]

### And this is where the tiling process is done and entire material is finished and ready to export [18:40]

### I usually do one more test in Marmoset Toolbag. This is also where I do my renders to present and compare material in my library later. If material looks fine there it should be ok everywhere else [18:52]

### This is also the moment to do the last check how material reacts to any light changes and how it tiles [19:08]

### It was enough to use the monopod to stabilise the camera and still get image quality useful for high quality photogrammetry reconstruction [19:55]

### same as before I trimmed the highpoly model below 67min as FBX struggles to hold vertex color information for everything above. I did it by trimming useless edges. [20:12]

### To get a bit more accuracy I changed the lowpoly mesh density to be a bit denser as with the previous material [20:41]

### Next T adjusted the scale and direction of lowpoly to match the pattern flow [20:56]

### Same as before, time spent on this stage can save a lot of time and effort later. [21:10]

### Brick pattern under the each edge has to match to the one on the opposite side as close as possible [21:29]

### Now when the plane is set time for micro adjustments with the Move brush [21:49]

### On this stage lowpoly plane matches the pattern good enough to be used for baking. [22:24]

### I set offset to 0.5 to get seam in the middle of texture's space since it is easier to find and deal with [23:05]

### Pattern is slightly shifted but it is nothing that cannot be fixed in Substance Designer with the Clone tool. [23:16]

### The process is exactly the same as before. I simply copy material from a 'good' spot and apply it into the broken one by seam [23:29]
**Transcript (timestamped):**
[24:27] Don't miss it.
[24:53] Kpectенной.


### Same as before exported textures were loaded into the Substance Designer and tweaked using the same graph as before this time without height map on input [25:04]

### Color distribution check-on histogram [25:56]

### and that's it! Material is ready to export and the final check in Marmoset Toolbag [26:05]

### Environment PBR Texture Creation Using Photogrammetry [26:28]


---

## Captured Frames

- [0:45] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_000.jpg
- [3:29] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_001.jpg
- [6:45] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_002.jpg
- [8:00] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_003.jpg
- [13:40] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_004.jpg
- [16:40] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_005.jpg
- [19:15] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_006.jpg
- [21:35] tutorials/frames/how-to-tile-photogrammetry-based-pbr-materials/frame_007.jpg

---

## Structured Notes

> **Note on source format:** this is a silent, caption-driven tutorial — there is no narration, hence transcript not captured (nothing to transcribe) (the safeguard CRITICALs above are expected, not a failed ingest). The 53 YouTube chapter titles ARE the tutorial text; extraction below is built from those chapters plus 8 captured frames. Do not re-transcribe.

### Core Technique
Turning a raw photogrammetry surface scan into a production-ready seamless/tileable PBR material: align a lowpoly tiling plane over the scan in ZBrush, bake, remove seams with Substance Painter's Clone tool (texture offset 0.5), then equalize/finish in Substance Designer and verify with the "rule of 3" tiling test and a Marmoset Toolbag light sweep.

### Summary
Grzegorz Baran demonstrates his complete scan-to-tileable-material pipeline twice on two different pavement surfaces (a stone-slab floor and a herringbone brick), showing that capture can be as light as 65 handheld images on a monopod in ~5 minutes. The heart of the method is doing tiling work *before* baking (accurately placing/warping the lowpoly plane so pattern edges already nearly match) so the Painter clone-stamp seam pass stays small, then using Designer's Equalizer and histogram to kill lighting gradients that make tiling obvious.

### Key Steps
1. **Capture:** 65 images of the surface patch, handheld camera on a monopod, ~5 minutes total — monopod stabilization is enough for high-quality reconstruction. Reconstruct to a highpoly scan mesh (vertex-colored).
2. **Highpoly prep:** trim the highpoly below ~67M vertices by deleting useless edges — FBX struggles to hold vertex color above that.
3. **ZBrush plane alignment (the critical step):** position a lowpoly plane over the highpoly scan covering the bake region; scale/rotate it so the surface pattern flows with the plane's axes, and make the pattern under each edge match the opposite edge as closely as possible. Refine with the **Move brush** (and densify the plane for pattern-heavy surfaces like herringbone brick). Time spent here directly reduces seam-removal work later.
4. **Bake** highpoly → plane (Baran uses the Substance Designer baker; baking specifics skipped as out of scope).
5. **Seam removal in Substance Painter:** load baked maps onto a *tiling-preview plane* that shows ~20% extra space on each side; fill the material channels to tile; **offset the texture 0.5 in both U and V** so seams land in the middle of UV space where they're easy to see and fix.
6. Create a **Paint layer set to Passthrough** per channel to be affected, activate the **Clone tool**, pick "good" source areas with **V held**, and stamp out the seams — mostly in the 2D view, tweaks in 3D view after. Keep the surface's flow/logic (don't break pattern continuity), and repeatedly **preview under changing light direction** — height/normal seams only reveal themselves under raking light.
7. **Substance Designer finishing:** drop Baran's reusable finishing graph into the exported-maps folder; preview tiling in the 2D view (SPACE), and if tiling repetition is obvious, tweak **Equalizer** values until it isn't (large-scale luminance gradients are the usual culprit — in the demo, disabling the bad scanned height map input fixed it). Regenerate a clean height map from **bent normal** rather than using the noisy scanned one.
8. **Rule-of-3 test:** in Designer's 3D View set **Tiling = 3** and inspect the 3×3 repeat for visible repetition patterns; final color/luminosity tweaks against the **Histogram** window so the RGB range is properly filled.
9. **Final check in Marmoset Toolbag:** apply to a sphere/plane, sweep the light and check tiling + light response; this doubles as the library presentation render. "If material looks fine there it should be OK everywhere else."
10. Repeat of the whole pipeline on the herringbone brick shows the only surface-specific differences: denser lowpoly plane, more careful pattern-flow alignment, and running the same Designer graph without the height input.

### UE Systems / Blueprints / Settings
Not a UE tutorial — this is the DCC side of the scan-based environment pipeline (the materials feed UE master materials):
- Capture: 65 images, monopod, ~5 min per surface
- ZBrush: lowpoly plane over highpoly, Move brush micro-alignment; highpoly < 67M verts for FBX vertex color
- Substance Painter: tiling plane with +20% border preview, texture offset 0.5/0.5, Paint layer in Passthrough per channel, Clone tool (V = pick source), light-direction preview
- Substance Designer: reusable finishing graph, Equalizer for tiling-gradient removal, height regenerated from bent normal, 2D tiling preview (SPACE), 3D View Tiling=3 ("rule of 3"), Histogram for RGB range
- Marmoset Toolbag: final tiling + light-sweep check, library presentation renders

### Difficulty
Intermediate

### UE Version
N/A (ZBrush / Substance Painter / Substance Designer / Marmoset Toolbag pipeline)

### Tags
materials, pbr, pipeline, modelling, intermediate

---

## Related Entries
- [How I Made This Shot in Unreal Engine 5](how-i-made-this-shot-in-unreal-engine-5.md) — the capture side (RealityCapture, cross-polarized flash) and UE/Path Tracer finishing of the same scan pipeline
- [RealityCapture to Unreal Engine 5](realitycapture-to-unreal-engine-5.md) — the prop-scan half of scan-based environment work (this entry covers the surface/material half)
- [Unlock Thousands of Free Assets in Unreal Engine](unlock-thousands-of-free-assets-in-unreal-engine.md) — pre-made Megascans scan materials when you can't capture your own
