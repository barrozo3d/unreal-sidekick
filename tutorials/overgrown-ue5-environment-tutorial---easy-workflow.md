---
title: Overgrown UE5 Environment Tutorial - Easy Workflow
source: YouTube
url: https://www.youtube.com/watch?v=9926HB1PA-c
author: Polygonflow Dash
ingested: 2026-08-17
ue_version: "Not specified (UE5-era, exact point release not stated or clearly legible in captured frames)"
tags: [pcg, modelling, materials, lighting, pipeline, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Overgrown UE5 Environment Tutorial - Easy Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=9926HB1PA-c)
**Author:** Polygonflow Dash
**Duration:** 12m20s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] What if we could turn an empty environment into a forgotten, overgrown ruin in just a few minutes?
[0:06] In this tutorial, I will show you how to transform an ordinary building into a post-apocalyptic scene using Dash.
[0:13] We will scatter vegetation, create natural overgrowth with masking, and add climbing-wise in just a few simple steps.
[0:20] So let's get started.
[0:23] So, we are starting with the Quixel unfinished building scene.
[0:27] I have already cleaned it up a bit by removing a few objects, and I've added an Ultra Dynamic Sky Blueprint for the lighting.
[0:34] First, I want the focal point for the scene, so let's bring in a main object.
[0:39] I'll open the Dash Content Browser, switch to my DecoGun library, and simply drag a motorcycle model into the scene.
[0:46] After this, I tweak the lighting a bit to make the bike stand out more.


### Material Edit [0:57]
**Transcript (timestamped):**
[0:57] Assets from the Dash libraries come with fully editable materials.
[1:02] I open the Material Editing panel from the Tools panel.
[1:05] If you don't see it, just click on this icon to find it.
[1:08] Let's adjust a few settings like the color, roughness, and the dirt amount.
[1:16] Now it's time to start adding vegetation.


### Surface Scatter [1:32]
**Transcript (timestamped):**
[1:36] I have already downloaded a few Megascans plans.
[1:39] Any assets you download from Thab or Bridge will automatically appear in the Dash Content Library.
[1:45] While holding Ctrl, I simply drag them into the scene and choose Scatter here.
[1:51] From here, I can adjust the density, scale, and various masking options.
[2:04] The falloff settings are especially useful.
[2:07] I'll make just a few clicks with our de-gut and interesting layer of ground vegetation.
[2:13] We can also use objects as masks.
[2:16] For example, I will add the motorcycle to the proximity mask section.
[2:20] By adjusting it, I can keep the area and the bike cleaner.
[2:24] But I can also invert it.
[2:35] Next, let's create vegetation growing along the walls and pillars.
[2:40] I select a couple of foliage groups, hold Ctrl and drag them onto the ground, and choose Scatter on Selection.
[2:56] After a few adjustments, I select the walls and pillars where I want the plants to appear and add them to the proximity mask section.
[3:04] I can invert the mask and find between the falloff and the noise mask until I'm happy with the result.
[3:35] If I ever need to, I can convert the procedural instances into Unreal Fallage using Convert Instances to Fallage from the Dash toolbar.
[3:45] But keep in mind that after converting, the Scatter is no longer procedural and becomes a standard foliage actor.
[3:54] Let's add some vegetation to the stairs as well.
[3:57] I select the surfaces and scatter the plants just like before.
[4:17] This time, I will increase the surface line value, so some of the plants naturally hang over the edges.
[4:32] But we're not limited to the ground. We can also scatter directly onto the motorcycle.
[4:38] I will use the English Ivy Pack, but I only want a few of these assets.
[4:42] Instead of scattering immediately, I hold Ctrl, drag onto an empty area, and choose Placing Grid.
[4:51] After selecting the plants I want, I will create a new Surface Scatter from the Dash toolbar.
[5:01] Now I will assign the selected plants, set the motorcycle as the target surface, increase the density, and shape the distribution until it feels natural.
[5:24] Finally, I will use an empty actor as a mask to keep the engine visible.


### Path Scatter [5:40]
**Transcript (timestamped):**
[5:40] Now let's create some hanging vegetation using the Path Scatter.
[5:44] First, I will draw a spline.
[5:53] Then I select the plants, hold Ctrl, and scatter them onto the spline.
[6:03] Here I just need to adjust the rotation.
[6:23] I can also duplicate splines and add them to the same scatter.
[6:38] And I can even add more Ctrl points whenever I need.


### Vine Tool [6:47]
**Transcript (timestamped):**
[6:48] Now it's time to generate some climbing wines. I will duplicate my empty actor to use it as my wine's origin.
[6:58] From the Dash toolbar I will choose the Wine tool.
[7:02] First, I will assign the origin actor, choose the Spiller as the target surface, and Dash generates a fully procedural wine.
[7:23] Naturally, I can add more surfaces if I want to.
[7:27] From here I can tweak the settings, add more branches, and even replace the default leaves with any foliage assets I want.
[7:54] But if I need more artistic control, I can also draw wines manually using the Draw Wine tool.
[8:19] I can spend forever tweaking these, but this already looks pretty good. I will quickly generate a few more around the scene.
[8:28] With this tool it's surprisingly fast to create an environment that's completely taken over by nature.
[8:35] Time to add some more details. I will place a few props, like this fuel can.


### Physics Tool [8:41]
**Transcript (timestamped):**
[8:44] Then I use Dash's physics tool to quickly create some believable brick piles. I can select this brick, choose Physics drop from the Place menu, and when it's seconds I have a nice pile.
[9:02] I will duplicate it and place it somewhere else in the scene.


### Decals [9:15]
**Transcript (timestamped):**
[9:17] Next, let's add a few decals from the Content Browser.
[9:30] This can also be scattered procedurally.
[9:56] Finally, I will add a few wall splatters to give the environment a little more history.


### Background & Details [10:10]
**Transcript (timestamped):**
[10:12] To make the scene feel larger, I will add a few ruined buildings in the background. So these assets only exist inside my project's Content folder, but Dash can index them as well.
[10:24] In the Dash Content Browser, I will switch to the Project Library, select the folder containing the assets, and click Compute.
[10:36] Dash automatically text everything, making it easy to search large asset libraries by their properties.
[10:47] I will pick this one and drag it into the scene.
[10:58] And here I can also add a few trees.
[11:05] And I can download a couple more Megascans assets and rearrange a few elements.
[11:30] I will give the motorcycle one final color adjustment so it stands out a bit more. And after a few lighting tweaks, here is the final result.


### Outro [11:35]
**Transcript (timestamped):**
[11:44] So, using just a handful of Dash tools, we have transformed the empty building into a lush, abandoned scene while keeping the entire workflow fast and fully procedural.
[11:54] If you'd like to try Dash yourself, you can download this for free using the link below. Thanks for watching and I see you in the next tutorial.



---

## Captured Frames

- [0:39] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_000.jpg
- [1:45] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_001.jpg
- [2:16] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_002.jpg
- [5:01] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_003.jpg
- [5:53] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_004.jpg
- [7:02] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_005.jpg
- [8:44] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_006.jpg
- [10:24] tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/frame_007.jpg

---

> **Third-party plugin note:** This entire workflow is built around **Dash**, a paid third-party procedural scattering/vegetation plugin for Unreal Engine (free download offered, per the outro) — not native UE tools. Its Content Browser, Scatter system, Vine tool, and Physics-drop tool are Dash's own UI, layered on top of (and alongside) Quixel/Megascans/Bridge assets and the third-party Ultra Dynamic Sky Blueprint used for lighting. Treat "Scatter," "Path Scatter," "Vine tool," and "Physics drop" as Dash-specific features, not built-in Unreal systems.

## Structured Notes

### Core Technique
Layering multiple Dash procedural-scattering tools — Surface Scatter (with proximity/noise masking), Path Scatter (spline-driven hanging vegetation), the Vine tool (procedural climbing vines with a growth simulation), and a Physics-drop tool for debris piles — onto a base Quixel "unfinished building" scene to convert it into an overgrown, post-apocalyptic environment quickly and non-destructively (scatters stay procedural/editable until explicitly converted).

### Summary
Starting scene: Quixel Bridge's "Unfinished Building" megascan environment, lightly cleaned up, lit via the third-party Ultra Dynamic Sky Blueprint. A focal-point hero prop (a motorcycle from the "DecoGun" asset library inside Dash's own Content Browser) is dragged in first; Dash-library assets ship with fully editable materials accessible via a Material Editing panel in the Tools panel (color, roughness, dirt-amount sliders demoed). **Ground vegetation:** Megascans plant assets (auto-indexed into the Dash Content Library once downloaded via Quixel/Bridge) are Ctrl+dragged into the viewport and dropped with the **Scatter** option, exposing density, scale, and multiple masking modes; **Falloff** settings shape scatter density gradients, and objects in the scene (e.g. the motorcycle) can be added to a **Proximity Mask** slot (invertible) to keep specific areas clear of — or exclusively covered by — vegetation. **Wall/pillar growth:** multiple foliage groups are multi-selected, Ctrl-dragged onto the ground, and dropped with **Scatter on Selection**; target walls/pillars are then added to the Proximity Mask (often inverted) and blended against Falloff/Noise Mask settings until the growth pattern reads as natural climbing coverage rather than a uniform layer. Procedural scatters can be permanently baked via **Convert Instances to Foliage** from the Dash toolbar — but this is one-way: the result becomes a standard Unreal Foliage actor and is no longer procedurally editable through Dash. **Edge-hanging plants:** raising a scatter's "Surface Line" value lets some instances naturally droop/hang over geometry edges (demoed on stairs). **Scattering onto a hero prop:** rather than scattering directly, individual plant instances (English Ivy pack) are first hand-picked via Ctrl+drag → **Placing Grid** (a picker layout), then the selected subset is fed into a **new Surface Scatter** targeting the motorcycle mesh itself as the scatter surface — density and distribution shaped until it reads naturally, with an Empty Actor used as an additional mask to keep the engine area clear of foliage. **Path Scatter (hanging vines along a curve):** draw a Spline in the level, multi-select plant assets, Ctrl+drag onto the spline, and choose the Path Scatter option — per-instance rotation is adjusted afterward; multiple duplicated splines can feed the same scatter setup, and control points can be added to a spline at any time to extend/reshape the path. **Vine tool (procedural climbing vines):** duplicate an Empty Actor to serve as the vine's origin point; from the Dash toolbar choose the **Vine tool**, assign the origin actor and a target surface (e.g. a pillar) — Dash then procedurally grows a full vine simulation across that surface, with exposed parameters including Growth Iterations, Growth Size, Gravity Weight, and a Seed value for variation; additional target surfaces can be added to the same vine, branch count can be increased, and the tool's default leaf asset can be swapped for any other foliage asset. For hand-authored placement instead of procedural growth, a separate **Draw Vine** tool allows manually drawing a vine's path directly. **Debris/props:** small hero props (e.g. a fuel can) are hand-placed; for believable rubble piles, Dash's **Physics tool** (Physics Drop, from the Place menu) is applied to a brick asset, letting physics settle a natural-looking pile in seconds — duplicated and repositioned around the scene as needed. **Decals:** wall splatters and grime decals are added from the Content Browser and can also be scattered procedurally (via the same Scatter system) rather than placed one at a time, for environmental storytelling/history. **Background depth:** additional ruined-building assets that live only inside the project's own Content folder (not a Dash/Megascans library) can still be indexed and searched by Dash — switch the Dash Content Browser to the **Project Library** tab, select the folder containing those local assets, and click **Compute** to have Dash auto-tag them for search, after which they behave like any other library asset (drag-and-drop into the scene). The scene is finished with additional background trees, a few more downloaded Megascans assets, general element rearrangement, a final color tweak on the motorcycle material, and final lighting adjustments.

### Key Steps
1. Start from a base environment (e.g. Quixel Bridge's Unfinished Building megascan), clean up unwanted objects, and set up lighting (demoed with the third-party Ultra Dynamic Sky Blueprint).
2. Establish a focal-point hero prop by dragging an asset from Dash's own Content Browser (organized into libraries, e.g. "DecoGun") into the scene; edit its material via the Tools panel's Material Editing panel (color, roughness, dirt amount, etc. — Dash-library assets ship fully editable).
3. Add ground vegetation: Ctrl+drag downloaded Megascans plant assets (auto-indexed into the Dash Content Library) into the viewport, choose **Scatter**, and tune Density, Scale, Falloff, and masking.
4. Use a **Proximity Mask** (assign a scene object, e.g. the hero prop, and optionally invert it) to keep an area clear of or exclusively covered by scattered vegetation.
5. For wall/pillar climbing growth: multi-select several foliage groups, Ctrl+drag onto the ground, choose **Scatter on Selection**, then add the target walls/pillars to the Proximity Mask (often inverted) and balance against Falloff/Noise Mask settings for a natural coverage pattern.
6. (Optional, one-way) Use **Convert Instances to Foliage** from the Dash toolbar to bake a procedural scatter into a standard Unreal Foliage actor — understand this permanently drops procedural editability.
7. Raise a scatter's Surface Line value to let some plant instances naturally hang over geometry edges (e.g. stair nosings).
8. To scatter directly onto a hero prop: Ctrl+drag the desired plant pack onto an empty area and choose **Placing Grid** to hand-pick specific instances, then start a new Surface Scatter with the prop itself set as the target surface; use an Empty Actor as an extra mask to protect specific sub-areas (e.g. an engine) from coverage.
9. For hanging vegetation along a path: draw a Spline in the level, multi-select plant assets, Ctrl+drag onto the spline, and choose **Path Scatter**; adjust per-instance rotation afterward, and freely duplicate splines or add spline control points to extend the effect.
10. For procedural climbing vines: duplicate an Empty Actor as a vine origin point, select the **Vine tool** from the Dash toolbar, assign the origin actor and a target surface, and let Dash grow the vine simulation; tune Growth Iterations, Growth Size, Gravity Weight, and Seed, add more target surfaces or branches, and optionally swap the default leaf asset for a different foliage asset.
11. For hand-drawn vine placement instead of procedural growth, use the separate **Draw Vine** tool.
12. Add small hero debris props by hand, and use Dash's **Physics tool** (Physics Drop, Place menu) on a base asset (e.g. a brick) to quickly generate a naturalistic settled pile via physics simulation; duplicate/reposition as needed.
13. Add wall-splatter/grime decals from the Content Browser, either placed individually or scattered procedurally via the same Scatter system, for environmental storytelling.
14. To use assets that live only in the project's own Content folder (not a Dash/Megascans library) with Dash's search/scatter tooling: switch the Dash Content Browser to the **Project Library** tab, select the folder, and click **Compute** to auto-index/tag them.
15. Finish with background elements (additional ruined buildings, trees, more downloaded Megascans assets), general rearrangement, and final material/lighting polish passes.

### UE Systems / Blueprints / Settings
- Third-party: **Dash** plugin (Content Browser w/ libraries + Project Library tab, Material Editing panel, Scatter / Scatter on Selection, Path Scatter, Vine tool, Draw Vine tool, Physics tool/Physics Drop, Convert Instances to Foliage)
- Dash Scatter parameters: Density, Scale, Falloff, Proximity Mask (invertible), Noise Mask, Surface Line (edge-hang amount)
- Dash Vine tool parameters: Origin actor, target Surface(s), Growth Iterations, Growth Size, Gravity Weight, Seed, branch count, swappable leaf asset
- Third-party: Quixel Bridge/Megascans assets (auto-indexed into Dash), Ultra Dynamic Sky Blueprint (lighting)
- Native UE elements used alongside Dash: Spline tool (for Path Scatter), Empty Actor (used as scatter origin/mask), standard material editing

### Difficulty
Intermediate (plugin-driven workflow with a shallow learning curve per the video's own "Easy Workflow" framing, but effective use of masking/falloff combinations to get natural-looking results takes some iteration)

### UE Version
Not specified verbally; UE5-era based on the Quixel/Megascans/Bridge integration and general editor UI shown, but exact point release is not stated or clearly legible in the captured frames.

### Tags
pcg, modelling, materials, lighting, pipeline, intermediate

---

## Related Entries
No directly related tutorials yet in the library covering the Dash plugin or procedural vegetation/scatter workflows — flag for cross-linking if another Dash, PCG, or environment-scattering tutorial is ingested later.
