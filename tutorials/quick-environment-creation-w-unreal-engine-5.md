---
title: Quick Environment Creation w/ Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=YfHdlxH22cM
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-early
ue_version: "UE 5.x"
tags: [dash-early, hdri, terrain, scatter, camera, proximity-masking, environment-art, layering, lut, beginner]
extraction_status: complete
frames_dir: tutorials/frames/quick-environment-creation-w-unreal-engine-5/
frame_count: 8
---

# Quick Environment Creation w/ Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=YfHdlxH22cM)
**Author:** Polygonflow Dash
**Duration:** 8m48s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction to HDR Lighting [0:00]
**Transcript:** Hey everyone, Josh Powers with Polygon Flow. And today we're going to go through step by step on how to create a serene and peaceful environment, leveraging the power of Dash inside Unreal Engine 5. With an environment like this, I want to utilize the power of high dynamic range image-based lighting, or HDRI for short. While Unreal comes with a few images to work with, I do recommend checking out Polyhaven, which has hundreds of HDR images to download for free. Just make sure you select the HDR file type before downloading. And then from there, it's a simple drag and drop into Unreal. To add an HDRI sky in your scene, you can simply click this button up here, select the light option, and then HDRI backdrop. I'm going to change this teardrop-shaped asset to a spherical model instead. And then I'm going to change the skylight intensity, as well as the HDRI sky's blueprint intensity. Both of these will have an impact on the intensity of the lighting.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_000.jpg

### Dash Terrain Creation & Texturing [1:55]
**Transcript:** We'll start by creating a terrain by typing terrain into Dash's prompt bar, and making sure to select the create terrain action. This will drop in a procedurally created terrain mesh into our scene. For this scene, I wanted to have some larger rolling hills, so I made sure turbulence was pretty far down to give us that lower frequency of hills, as well as cranked up the height. I also bumped up the mid-turbulence value quite a bit, which gives us some chunkier layers along the hills. This will really help add some irregularities to our grass scatters that gives a more natural look later on. Once we're satisfied with these settings, we can open up the content library, select a good dirt material, drag it onto the terrain, and then open up the materials panel from Dash to make a few adjustments. We should also add a directional light to our scene to give us a strong key light, matching its direction to the sunlight in our sky box.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_001.jpg

### Key Shot Setup [3:18]
**Transcript:** There are a few types of trees in this pack, primarily field and forest. I'm using the field trees for this scene. And after a few adjustments to its position on the terrain, I'm ready to frame out the key shot. I'll go up to the prompt bar and type New Camera to create a new cinematic camera. From here, I'll play with the position, focal length, crop settings, and so on to get the look I want for this shot. Every scene will be different because every artist has their own vision. Study some photography and films to help strengthen your knowledge in this area. Now it's time to fill out this terrain with some lush vegetation.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_002.jpg

### Adding Vegetation with Dash [4:04]
**Transcript:** To do this, we'll go to our content library and search for grass. I'll grab these grass patches from Megascans because the assets cover a little more real estate than a small tuft of grass. This allows me to get more coverage across the hills with fewer instances. The scatter settings for the grass are important. Having a decent sized gap between the min scale and max scale will help break up any incidental repetition. And this can be further enhanced by using fall off along with break up to give you a nice gradient and scale variation near the edges of the scatter. As I've mentioned in previous videos, it's important for us to think in layers when it comes to building up our environment. This will help break things up and add more visual interest throughout.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_003.jpg

### Working with Proximity in Dash [5:28]
**Transcript:** For this particular scene, I plan to have a small swing hanging from the tree, and I want to remove the vegetation beneath and around the swing and tree. I decided to use Unreal's in-editor modeling tools to quickly create an oblong shape that roughly covers the area I want to clear. Then I can just select my grass scatter, and then the mesh I just created, and then I'll go ahead and click on the proximity icon up here in the dash prompt bar. This will only scatter the grass within the set threshold around the proximity mesh. So I'll bump up that threshold a bit, and then when I invert the results, we'll see that the grass has been removed from the area around my model. From here I can duplicate the masking model to extend the coverage out towards the tree. And then I'll apply the same proximity masking techniques to the other vegetation scatters.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_004.jpg

### Hero Detailing [6:34]
**Transcript:** Because the focal point of the scene is the tree and swing, this is really the only area that I need to add additional levels of detail to. I do this by adding some Megascans ground assemblies from the content library, using Dash's placement tool to quickly move, scale, and rotate them into position. I'll also add some additional scatters to those newly added meshes to add extra layers of detail. For cinematic shots, it's good to really focus our attention on the areas closer to the camera, adding detail layers there while leaving areas further away at the broadstroke passes we did earlier.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_005.jpg

### Rope Swing Creation [7:20]
**Transcript:** As for the swing, it's a very simple setup. I created two cylinders in a subdivided plank, both of which were UV mapped to Megascans surfaces. I then rigged the asset in Blender using two bones, and animated it to look as if it's gently swaying in a breeze before bringing it into Unreal. Alright, with the swing in place, we're just about wrapped up. From here, it's just a matter of tweaking and polishing — adjusting the lighting, scatter settings, and various materials in the scene to match both our reference images and what I envision the final result looking like.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_006.jpg

### Camera Setup [8:02]
**Transcript:** Then lastly, we can go into our camera settings to adjust a few post-process settings, as well as tell our camera to keep its focus on the swing, no matter where the camera's located. Now we'll just cycle through a few pre-made look-up textures for our color grading, and voila, we have our peaceful retreat finished and ready to render out. I hope this tutorial was helpful for you, and I would love to see your own interpretation on this scene. Thank you so much for watching, and I'll see you next time.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_007.jpg


---

## Structured Notes

### Core Technique
HDRI-lit rolling hills environment: terrain with mid-turbulence for natural foliage irregularity, layered foliage scatter (fall-off + break-up + min/max scale spread), proximity-mask exclusion zone for hero area, camera-first framing discipline, detail pass concentrated near camera, Blender-rigged swing prop, LUT color grading.

### Summary
8-minute beginner environment walkthrough (early Dash) by Josh Powers. Polyhaven HDRI → rolling terrain with mid-turbulence for natural scatter irregularity → directional light matched to HDRI sun → camera established first before any scattering → layered grass/foliage scatter (large patches, min/max scale gap, fall-off + break-up) → proximity mask exclusion around swing/tree using oblong modeling mesh → hero detail pass with Megascans ground assemblies + micro-scatters → Blender-rigged 2-bone swing prop → LUT-based color grading. Key principle taught: establish camera shot first, then scatter; concentrate detail only where camera sees it closely.

### Key Steps
1. **HDRI** — Polyhaven (free .hdr download) → drag into UE → Content button → Light → HDRI Backdrop; switch to sphere model; adjust Skylight intensity + HDRI blueprint intensity independently.
2. **Terrain** — type `terrain` → Create Terrain → low turbulence (large hills) + high mid-turbulence (chunky sub-layer irregularity) + height.
3. **Ground material** — Dash Content Library → drag Megascans dirt material → Materials panel tweaks.
4. **Directional light** — match direction to HDRI sun position.
5. **Camera first** — type `new camera` → set position, focal length, crop before scattering; establishes composition intent.
6. **Layered foliage scatter** — Content Library → large Megascans grass patches → Ctrl+drag → Scatter Here; wide min/max scale gap to break repetition; fall-off (edge gradient) + break-up (pattern variation); repeat multiple foliage types for natural layering.
7. **Proximity mask exclusion** — UE Modeling Tools → create oblong mesh over swing/tree area → select grass scatter + mesh → proximity icon → increase threshold → Invert (removes grass inside mesh zone); duplicate mesh to expand zone; apply to all foliage scatters.
8. **Hero detail pass** — Placement Tool → add Megascans ground assemblies near focal point; additional micro-scatters on new meshes for close-up detail.
9. **Swing prop** — modeled in Blender (2 cylinders + subdivided plank, Megascans UV), 2-bone rig, swaying loop animation → import to UE.
10. **LUT color grading** — Camera → post-process → cycle LUT presets to choose final look; set focus target to swing.

### UE Systems / Blueprints / Settings
- **HDRI Backdrop** — sphere model; Skylight intensity + blueprint intensity are separate controls
- **Terrain mid-turbulence** — adds chunky sub-frequency detail that creates natural scatter irregularity when foliage is scattered on top
- **Scatter min/max scale gap** — wide spread breaks incidental repetition patterns in ISM foliage
- **Fall-off** — density gradient near scatter boundary (fades out at edges)
- **Break-up** — pattern variation within scatter body (prevents tiling look)
- **Proximity Mask (invert)** — use any UE modeling mesh as exclusion zone; invert = remove scatter inside mesh bounds; duplicate mesh to extend zone
- **Placement Tool** — rapid hero-prop positioning without breaking viewport flow
- **Post-process LUT** — cycle pre-made look-up textures in camera post-process settings
- **Focus target** — camera post-process focus set to swing location for consistent DOF

### Difficulty
Beginner

### UE Version
UE 5.x (Dash early release, pre-1.7)

### Tags
`#dash-early` `#hdri` `#terrain` `#scatter` `#camera` `#proximity-masking` `#environment-art` `#layering` `#lut` `#beginner`

---

## Related Entries
- [[introducing-dash-for-unreal-engine-5]] — original Dash intro with same scatter + terrain workflow
- [[new-ue5-plugin---easy-environment-creation]] — similar approach with displacement + foreground/mid/background composition
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — dedicated scatter guide
- [[tutorial-create-subtle-realistic-environments-in-ue5]] — subtle realistic environment layering
