---
title: Surface Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH
source: YouTube
url: https://www.youtube.com/watch?v=D4IPvlypNkg
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, scatter, surface-scatter, proximity-masking, vertex-color-masking, texture-masking, feature-masking, environment-art, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash/
frame_count: 7
---

# Surface Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=D4IPvlypNkg)
**Author:** Polygonflow Dash
**Duration:** 8m55s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro & Surface Scatter Basics [0:00]
**Transcript:** Greetings, I'm Jonathan, Polygon Flow's Community Director for Dash, our next Gen Unreal Engine plugin that makes creating environments like these super easy. In this video I'll be covering one of our most powerful tools, Surface Scatter, which has been significantly improved in Dash 1.4. Let's start by opening Dash, then type Scatter to bring up the Surface Scatter tool. It's a very complex tool, so expanding the tool window is a good idea to work with it. There's multiple ways of initiating a Scatter command, either by selecting existing meshes or by using the Dash content browser and holding Control as you drag the asset into the environment. From there you can adjust the number of object instances using Density, and adjust the maximum and minimum scale values too. Plus it's possible to sort scaling by a variety of factors to customize your scattered assets. I'll cover fall off soon, but it's got a dependency that will have to enable later in the video before its effects will be visible, so I'll come back to this one. Noise scale can be used to create subtle variation in the scattered assets that prevents uniformity. It's perfect for grass, so we'll go ahead and leave it enabled.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_000.jpg

### Feature Masking [1:39]
**Transcript:** Feature masking has terrain masking options. Let's start with angle mask, which constrains the scattered assets up to a specific angle on the terrain. Anything higher than this value will not render. Some height masking uses the relative Z data of the mesh to determine instance placement while maximum height does the opposite. These values are determined by the height of the mesh being used to mask. You can use max and min height masking together, too, to create different effects. Add mask infills the scattered mesh regardless of existing scatter settings, while remove mask does the exact opposite to thin out the scatter no matter what the settings are. For this next part, I'm going to use Unreal to create a simple box object which I'll use to demonstrate raycast mesh masking. This was a feature request from the community for scenes like a post-apocalyptic environment, where you'd find broken down automobiles that would have grass growing directly underneath them, or perhaps having large rocks with broken stones and pebbles collecting in the shadows underneath. It works with any mesh you can throw at it, and it's quite versatile and updates quickly.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_001.jpg

### Rotation Properties & Scale Properties [2:51]
**Transcript:** Uniform angle rotates all scatter meshes in the same direction, but you'll have to uncheck randomize angles for it to function. XY and Z rotation jitter will create randomized rotation of each asset in the scatter field giving you ultimate control over how each asset will look. Enable use custom scale to get fine precision over the scale of each asset that gets placed in the environment, not only the Z scale but the X and Y scale, too. This can allow you to create much more realistic scattering that takes into account the variation inherent to natural objects like plants. In some situations, it might make more sense to use standard minimum, maximum scaling, but I find custom scale provides a very realistic look in many use cases.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_002.jpg

### Proximity & Object Masking [3:41]
**Transcript:** Proximity is a tool that allows you to set what scatters based on physical proximity to an object in the environment. It can work with any mesh, including a basic Unreal sphere like this. Proximity distance determines how far the object's influence extends beyond it to prevent or enable scattering. Invert proximity is the opposite. Scatter will only spawn based on the proximity to the object being used. Scatter determines how closely the scattered meshes adhere to the object used as a proximity detector. You can scatter assets using a curve, too. Type draw into Dash and then select draw curve, then draw out your preferred shape. In this case, a spiral works well to demonstrate how the curve tool will play off the proximity tool. You can adjust the curve sampling to fine tune how well the curve blanks out meshes that are surrounding it. Object masking is a more precise version of proximity masking. In this case, I'll use a Megascans asset to mask out the grass. Because it's so precise, object masking only works if the mesh is physically near the mesh that scatter assets are being placed upon. Like proximity masking, you can invert this as well.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_003.jpg

### Vertex Color Masking [5:19]
**Transcript:** For vertex color masking, I've applied a basic red vertex color material to show Dash applying these colors in real time. With the vertex colors applied, I've re-selected the surface scatter and applied the original material, then enabled the red channel in vertex color masking, making the scatter meshes adhere to the existing vertex colors. Vertex coloring threshold determines how strong the vertex color masking is, which is useful for fine tuning the color mask. There are different blending modes that you can work with to further dial in the mask. You can even adjust the vertex colors using Dash and then make any adjustment in surface scatter to have it automatically update. The workflow is non-destructive and lets you iterate on any number of vertex color masks that you'd like to use in the engine.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_004.jpg

### Texture Masking & Falloff [6:19]
**Transcript:** Texture masking allows you to load any texture from the Unreal Engine content browser as a mask. You've got several options here including color threshold, which controls the intensity of the texture map, texture tiling and texture inversion too. A simple caution stripe texture can be used to create rows of grass, so imagine what else you can do using texture masking. Border distance, spread, and scale are all key factors to helping break up the edges of your scatter fields. Adjust each of these settings and you'll create natural break up along the border of the scatter mask. Now let's cover fall off. Fall off creates a transition and scale from the tip of the mask to the center of it, allowing for a more natural appearance to the scattered assets. It works even better with individual meshes instead of clumps of assets, so the scaling is applied per mesh rather than per clump.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_005.jpg

### Surface Scatter Applied [7:55]
**Transcript:** Here's one of the scenes in the beginning of the video. This took me two hours to make. Most of that was hand placing the assets that you see here — all that remains after hiding the surface scatter instances. Pretty crazy huh? One of the ways that I like to work is using cubes with a transparent material as a bounding box for scattering using object masking. This allows me to specify where exactly I want the scattered assets to appear and lets me drag the cube around to hand place them in real time. This is a technique that I used extensively with this scene, including with the trees in the background. It gave me the freedom to specify exactly where I wanted randomized scattered trees to appear without having to worry about them being placed too far forward. Thanks for watching and let us know what you think in the comments. See you guys next time.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_006.jpg


---

## Structured Notes

### Core Technique
Dash 1.4 Surface Scatter deep dive: density/scale/noise basics, five masking systems (feature/angle/height/raycast, proximity, object, vertex color, texture), rotation jitter, custom XYZ scale, fall-off, border break-up — plus the transparent bounding-box cube trick for hand-placed scatter zones.

### Summary
9-minute comprehensive Surface Scatter guide by Jonathan (Community Director), covering Dash 1.4 improvements. Full parameter walkthrough: Density, min/max scale, custom XYZ scale, rotation jitter (uniform angle + XYZ jitter), noise scale. Five masking systems: Feature Masking (angle, height min/max, add/remove, raycast mesh); Proximity (distance, invert, curve-based); Object Masking (precise, mesh must be nearby); Vertex Color Masking (channel select, threshold, blending modes, live-update); Texture Masking (load any UE texture, color threshold, tiling, inversion). Border break-up (distance/spread/scale) + Fall-off (tip-to-center scale gradient). Pro tip: transparent cube + object masking = moveable scatter bounding box for hand-placed zones.

### Key Steps
1. **Open Surface Scatter** — type `scatter` in Dash prompt bar; expand window to see all options; initiate by selecting mesh then typing scatter, or Ctrl+drag from Content Library.
2. **Density + scale** — Density = instance count; min/max scale spread breaks repetition; Custom Scale enables per-axis (X/Y/Z) scale variation per instance.
3. **Rotation jitter** — uncheck Randomize Angles for Uniform Angle (all same dir); XY/Z Rotation Jitter = per-instance randomized rotation.
4. **Noise scale** — subtle position variation to prevent uniformity; ideal for grass.
5. **Feature Masking** — Angle Mask: max slope angle cutoff; Min/Max Height Masking: Z-based range; Add Mask: force scatter regardless; Remove Mask: force clear regardless; Raycast Mesh Mask: scatter under a mesh (post-apoc cars, rocks in shadows).
6. **Proximity Masking** — assign any mesh; Proximity Distance = influence radius; Invert = scatter only within radius; Curve Sampling controls curve edge precision.
7. **Object Masking (precise)** — more precise than proximity; mesh must physically overlap scatter surface; invert available; use transparent cube as moveable bounding box.
8. **Vertex Color Masking** — paint vertex colors on terrain in Dash; enable channel (R/G/B) in scatter; Vertex Color Threshold controls strength; blending modes; live non-destructive updates.
9. **Texture Masking** — load any UE content browser texture; color threshold, tiling, inversion; stripe texture example creates rows.
10. **Border break-up** — Border Distance + Spread + Scale create natural irregular edges at scatter boundary.
11. **Fall-off** — requires a mask; creates scale gradient from boundary tip to center; works best with individual meshes (scale per mesh, not per clump).

### UE Systems / Blueprints / Settings
- **Surface Scatter (Dash 1.4)** — ISM/HISM-based scatter; fully parametric; all params live-update
- **Density** — total instance count
- **Custom XYZ Scale** — per-axis scale variation for organic variation (vs simple min/max uniform scale)
- **Rotation Jitter** — XY/Z jitter for per-instance rotation; uncheck Randomize Angles for Uniform Angle
- **Feature Masking** — Angle (slope cutoff), Min Height, Max Height (Z range), Add/Remove (force states), Raycast Mesh (scatter under meshes)
- **Proximity Masking** — distance-based include/exclude; Invert = inside-only; works with curves and meshes
- **Object Masking** — precise footprint-based mask; mesh must be coplanar/overlapping; moveable cube trick for portable zones
- **Vertex Color Masking** — channel R/G/B select; threshold strength; blending modes; live Dash vertex paint + auto-update
- **Texture Masking** — any UE texture as mask; color threshold; tiling; inversion; creative patterns possible
- **Border Break-up** — Distance/Spread/Scale triad for natural edge variation
- **Fall-off** — tip-to-center scale gradient; requires active mask; best with individual meshes

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.4)

### Tags
`#dash-1.4` `#scatter` `#surface-scatter` `#proximity-masking` `#vertex-color-masking` `#texture-masking` `#feature-masking` `#environment-art` `#intermediate`

---

## Related Entries
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Path Scatter guide (same series)
- [[beginner-content-library-tutorial-for-ue5]] — Content Library + Ctrl+drag scatter entry point
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 proximity masking with shared reference
- [[dash-110---procedural-scatter-presets-in-ue5]] — Dash 1.10 scatter presets + compound preset creation
