---
title: Introducing Dash for Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=NVSEN3ND6VU
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-early
ue_version: "UE 5.x"
tags: [dash-early, terrain, scatter, world-building, content-library, decals, mesh-cards, beginner]
extraction_status: complete
frames_dir: tutorials/frames/introducing-dash-for-unreal-engine-5/
frame_count: 9
---

# Introducing Dash for Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=NVSEN3ND6VU)
**Author:** Polygonflow Dash
**Duration:** 12m1s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Dash Overview [0:00]
**Transcript:** Hey everyone, Josh Powers here from Polygonflow, and today I'm thrilled to announce Dash, a novel approach to world building in the Unreal Engine. With this video, I hope to show you just how exceptional Dash is at streamlining your creative process with no loss of creative control. So sit tight and let's get into it. Okay, with the Unreal Editor open, the Dash icon should be right up here, and then if you click on it, a prompt bar will show up. Our goal for Dash is to remove literally any complex interaction you have to do with your 3D software. And as such, you'll see me throughout the tutorial working exclusively in full screen mode, with nothing but the Unreal Engine 5 viewport supercharged with Dash's incredible versatility. So let's hit F11 and go into full screen and then jump right into it. You can think of this prompt bar as a comprehensive set of solutions for world building. Typing keywords in here will show all relevant tools and actions, and the same drop down menu here can also be opened by double clicking on the logo itself. The menu on the left is where you can check for updates, open up the documentation, and much, much more.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_000.jpg

### Dash Prompting [1:21]
**Transcript:** First let's create some terrain. You can type create a terrain or just terrain into the prompt bar. You'll notice the terrain action being the first suggestion. An action will typically have its title in bold and its context sensitive, meaning it'll operate based on your prompt and sometimes you're seeing content. Tools, however, don't have their text in bold and will just open up a small panel through which the tools work. You can press the up and down arrows to cycle between suggestions, select them with your mouse, or just hit enter, which will bring up the first tool being suggested. As you can see, Dash created a terrain mesh for us and also opened a floating panel through which we can now adjust. If I close the panel, then select the terrain again, Dash will automatically show this icon, which suggests that whatever is selected in the Unreal Editor has an editable tool attached to it. Let's go ahead and click on the icon and adjust our terrain settings. Next we want to give the terrain a material and this is where the content library comes in.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_001.jpg

### Water Creation [3:27]
**Transcript:** Let's write create a plane in the Dash prompt bar, pick the primitive action and a plane should be created in the center of our view. Next let's write apply water and a water material will be applied to it. I'll go ahead and scale my plane to properly cover the terrain and now we're ready to move on. With our terrain set up let's start placing some objects in the scene. You can drag and drop them from the content library and an interactive object placement allows you to neatly drag the object around all while lining it to the underlying surface. You can hold control to scale it, shift to rotate it and even control shift to sync it below the surface which is extremely common to do when world building. The panel over here shows you all the hotkeys you can use with this context based placement tool and you can quit the context at any point by hitting escape.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_002.jpg

### Surface Scatter Intro [4:50]
**Transcript:** Before we start detailing our scene let's go ahead and type new camera to create a new camera. Then I'll pick a view I feel comfortable with and do some very brief tweaks to my field of view, sharpen and other basic effects to get a good base. I'll also pick my lighting setup either by typing cycle lighting to see all the possible lighting setups or just write a specific word to pick a preferred one. With that out of the way let's start adding more detail. Scattering is one of Dash's main strengths and its simplicity is truly unparalleled. Just drag an asset from the content library to your viewport and hold control when you drop it. This will give you a couple of scatter options. Let's just go with scatter here. Like with the terrain a floating panel shows up and with it everything we need to get a good base. As you can see I'm getting really good results within seconds. I recommend you play with all the values but fall off and break up are among my favorites as they allow you to get some truly phenomenal results in no time.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_003.jpg

### Constrain Scatter to Paths [6:18]
**Transcript:** We'll write draw curve and dash and literally just draw a curve in our viewport. Then with our grass and the curve selected an icon will show up in the toolbar allowing us to mask out the grass with the curve. As with most things a short concise panel shows up with just the right settings you need. You can use this masking workflow with any type of object. Just make sure you first select the asset you want to mask which in our case is the grass. Then select whatever you want to mask it with. It could be curves, meshes or even another set of instance objects such as large rocks scattered throughout the landscape. And by the way scattering also works on curves and instances. I can select some instances here then drag and drop some objects from the content library with control pressed and also scatter on instances.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_004.jpg

### Dash Color Grading [8:10]
**Transcript:** Dash has a plethora of color grading presets to offer. And as with the lighting we can just type cycle grading to cycle through the different options or even go with specific keywords of famous movies such as the Joker and Children of Men. Or more relevant keywords like Warm or Vintage. Back to my camera settings I'll just tweak a few things a bit and that should do it. This workflow for me is what makes Dash truly exceptional. We haven't even touched Unreal Engine's panels or nodes and everything happened through a prompt bar without ever taking over creative control.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_005.jpg

### Manmade Environments with Dash [9:06]
**Transcript:** Here we have a new scene I built using the various tools in Dash. But to really make it shine I can just search for some decals in the content library, drag and drop them onto the viewport, and then the interactive decal placement will give us the best decal workflow out there. And even more you can select multiple decals and scatter them as you would scatter regular meshes. This makes detailing man-made environments such a fun and inspiring process.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_006.jpg

### Forest Creation [9:41]
**Transcript:** I'll drag and drop the trees somewhere in the scene, find and open the tool surface scatter, add the trees to scatter, then a surface to scatter onto. Just like with drag and drop scatter, if we select the trees we just manually scattered we can select the icon up here and now have the floating bar to adjust our trees. This method of scattering is now identical to the other, which means we can also mask them out based on curves or other objects.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_007.jpg

### Create Leaf Scatter [10:30]
**Transcript:** Megascans comes with thousands of Atlas textures through their website, but they're unfortunately not available in the bridge plugin. To remedy this, we can download them locally through the Megascans website or bridge software. And then back in dash, you can write, create scatter mesh cards or just scatter cards, then select the action mesh cards. And it'll open a dialog for you to select the opacity map of your Atlas asset. And just from that, dash will import all your textures, create mesh cards and materials with them, then scatter them on whatever object you had selected in your viewport. Again, there's zero loss of control. All our scatter parameters are right there to tweak.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_008.jpg


---

## Structured Notes

### Core Technique
Dash prompt-bar world building: terrain, Megascans content library, surface/path scatter, proximity masking, camera creation, color grading, decal placement/scatter, and mesh-card scatter from Megascans atlas textures — all without touching UE5 panels.

### Summary
First official Dash introduction video (early release, pre-1.7). Josh Powers demonstrates the complete initial feature set: prompt-bar Actions (bold, context-sensitive) vs Tools (floating panel), terrain generation, water planes, drag-and-drop placement, surface scatter with fall-off/break-up, curve-constrained scatter masks, lighting and color grading presets by keyword, decal placement and scatter, and Megascans atlas mesh-card creation from opacity map.

### Key Steps
1. **Open prompt bar** — click Dash icon or double-click logo; type keywords → Actions (bold) or Tools (panel).
2. **Create terrain** — type `terrain` → Create Terrain action → adjust scale, turbulence, height in panel.
3. **Apply material** — open Dash Content Library → drag Megascans material onto terrain.
4. **Add water plane** — type `create a plane` → primitive → scale/position → type `apply water` → water material applied.
5. **Place objects** — drag from Content Library → interactive placement; Ctrl = scale, Shift = rotate, Ctrl+Shift = sync below surface.
6. **New camera** — type `new camera`; adjust FOV, sharpen, post effects from prompt bar.
7. **Surface scatter** — drag asset + Ctrl → Scatter Here → adjust density, fall-off, break-up.
8. **Constrain scatter to curve** — type `draw curve` → draw curve in viewport → select scatter + curve → click mask icon → proximity masking panel.
9. **Color grading** — type `cycle grading` or movie/mood keywords (Joker, Children of Men, Warm, Vintage).
10. **Mesh card scatter** — type `scatter cards` → select atlas opacity map → Dash imports textures, creates mesh card materials, scatters on selected object.

### UE Systems / Blueprints / Settings
- **Dash prompt bar** — Actions (bold, context-sensitive) vs Tools (floating panel); Ctrl on sliders = faster rate; context icon on selected object re-opens its tool
- **Content Library** — Megascans integration; drag+drop scatter with Ctrl held
- **Surface Scatter** — density, fall-off (edge gradient), break-up (pattern variation); works on meshes, curves, instances
- **Proximity Mask (curve)** — select scatter → select curve/mesh/instances → mask icon; constrains or excludes scatter
- **Cycle Lighting** — keyword-based HDRI/lighting preset switcher
- **Cycle Grading** — keyword-based color grade presets; supports movie names and mood words
- **Decal Placement** — interactive decal tool from prompt bar; multiple decals scatterable
- **Mesh Cards** — `scatter cards` action → opacity map dialog → auto-creates mesh card materials from Megascans atlas textures

### Difficulty
Beginner

### UE Version
UE 5.x (Dash early release, pre-1.7)

### Tags
`#dash-early` `#terrain` `#scatter` `#world-building` `#content-library` `#decals` `#mesh-cards` `#beginner`

---

## Related Entries
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 with road tool, AI assistant, blend material
- [[new-ue5-plugin---easy-environment-creation]] — follow-up environment creation with same early feature set
- [[quick-environment-creation-w-unreal-engine-5]] — HDRI + layered scatter with proximity masking
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — dedicated surface scatter beginner guide
