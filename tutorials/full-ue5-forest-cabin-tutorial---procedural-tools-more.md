---
title: Full UE5 Forest Cabin Tutorial - Procedural Tools & More!
source: YouTube
url: https://www.youtube.com/watch?v=VQMHQR4sQCo
author: Polygonflow Dash
ingested: 2026-09-07
plugin_version: "Not specified"
ue_version: "UE5 (version not stated)"
tags: [dash, polygonflow, procedural, terrain, curve-deformation, road-tool, surface-scatter, path-scatter, proximity-mask, object-mask, vertex-painting, vines, rvt, runtime-virtual-texture, fog-cards, environment-art, foliage, lighting, cine-camera, composition, world-building, intermediate, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/
frame_count: 10
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Full UE5 Forest Cabin Tutorial - Procedural Tools & More!

**Source:** [YouTube](https://www.youtube.com/watch?v=VQMHQR4sQCo)
**Author:** Polygonflow Dash
**Duration:** 29m41s | 12 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, today we will see how we can make this scene in Unreal Engine using Dash.
[0:07] We will start by doing some vertex painting on our terrain, then scatter grass and trees,
[0:19] followed by vines,
[0:24] and IVs.
[0:27] We will finish with the lighting paths to embellish our scene.


### Terrain [0:37]
**Transcript (timestamped):**
[0:37] Let's start by typing terrain in the Dash toolbar. Select Create Terrain, your newly created terrain will appear in the viewport, alongside the Tools panel.
[0:48] I would like to hide the horizon line from eye level, curved value allows you to achieve that.
[0:56] UV scale will increase the tiling of the texture.
[1:01] Let's now apply a material on our terrain. I open the content browser and select the materials I would like to use.
[1:08] While holding down Ctrl, drag and drop them on your terrain and select Apply Blend Material.
[1:14] Now that we have a material applied, let's increase the tiling to make it look more natural.
[1:19] While your terrain is selected, go to the Tools panel, click on the Edit menu and select Edit Blend Material.
[1:27] I will scroll down to Global Tiling and change its value to 2.8.
[1:36] Now, if you zoom out, you will see how the tiling is repetitive. To solve that, I'll scroll down to Tiling Control and check Enable Breakup Tiling.
[1:45] We now get a nicer result.


### Curves & Road [1:52]
**Transcript (timestamped):**
[1:53] Let's move to the next step and create some deformation for the road on our terrain.
[1:58] In the Dash toolbar, type Draw and select Draw Curve, then draw a path on the terrain.
[2:05] You can adjust the distance value in order to reduce the points on the curve.
[2:15] In the Terrain Tools, under Curve deformation, I will add the curve and adjust some values like Width and Falloff to get a good result.
[2:27] Next, I'm going to place one curve that forms the path toward the cabin and another to level the terrain under the cabin.
[2:38] I would like to show you how you can manage the curves used to deform our terrain.
[2:46] In the Terrain Tool, under Curve deformation, click on Edit Table.
[2:52] A pop-up menu will open. You can click on the plus icon to add a new item.
[2:57] Make sure your curve is selected. Then click on the plus icon under Curve in order to add the curve to your item.
[3:05] You can adjust the Width to your liking and the position as well as the rotation of the curve.
[3:18] Let's add a second curve. While selected, click on the plus icon to add another item to the table.
[3:26] Then click on the plus icon under Curve to add an object.
[3:29] Adjust the Width to your liking. I found 11 was a value that matched what I was going for.
[3:42] While your curve is selected, you can also click on each point in order to manually adjust its position.
[3:59] Let's create a road on the road path. In the Dashbar, type Road and select Road tool.
[4:06] Make sure the curve is selected. In the Tools panel, click on the plus button under the Curves properties.
[4:15] The road will appear on the curve. Adjust some values like Width and Inside height to your liking.
[4:20] You can also apply any material you like. I decided to go for this nice Pine American Road material from the Megascans library. It gives it a really nice look.
[4:33] After I'm done with the road, I import the cabin from the Fisherman cabin asset pack that I downloaded from Fab.
[4:41] This cabin would be our main focal point.
[4:43] The set dressing is really nice. You can see all the details they put in.


### Vertex Painting [4:48]
**Transcript (timestamped):**
[4:51] To get rid of the shadow artifact, you can use the console command r.raytracing.normalbias with a value of 5.
[5:00] Because the path cannot be this uniform, let's vertex paint a different material on it.
[5:05] Switch to Modeling mode. Select your terrain and press the big icon.
[5:11] Then go to Attribute, Paint Vertex Colors and change a couple of values like Brush Size and Strength.
[5:18] And select only the R channel. Change the paint color to black.
[5:26] Then you can paint on the terrain and refine all the small areas.
[5:35] Let's now scatter some grass on the terrain. Select the grass from the Content Browser while holding CTRL, drop it in the scene and choose Scatter here.


### Scattering [5:45]
**Transcript (timestamped):**
[5:58] Adjust the density and other values to your liking.
[6:00] I also decided to change my lighting to make it match the mood I'm going for.
[6:10] Our grass is now scattered on the entire terrain. However, I would like it to be excluded from some areas like the road, cabin and main path.
[6:21] We can achieve that by selecting our curve and adding it to the proximity mask of the scattered grass.
[6:27] Click on the plus button of the Object property and adjust the width and falloff.
[6:40] We can apply the same process to the road and cabin.
[6:50] I would like to remove the grass from this area. It will be a secondary focal point.
[6:55] Let's draw a circle using our draw curve and add it to the object mask and play with the parameters to get a good result.
[7:12] Next, let's scatter some trees in the scene. In the Content Browser, I select the trees I would like to use. It's always good to have some variety.
[7:21] It will make your forest feel nice and natural.
[7:32] Once scattered, I reduce the density to a value of 0.2.
[7:36] Afterward, I have to clear the trees from all the paths using the same proximity mask method as before.
[7:54] Let's hide the forest to have a better view of the scene. I would like to also have some trees behind the cabin.
[8:01] For that, let's draw a curve and use path scatter on it to scatter some trees.
[8:07] I select my curve, hold CTRL and drag and drop them from the Content Browser and then choose scatter on selection.
[8:17] You can see that right now they look quite uniform. By adding some jitter, it will make them look more interesting.
[8:31] You will notice some trees are overlapping with the cabin. Let's clear them by adding them to the proximity table.
[9:02] I also cleared the tree from the secondary focal point. I would like to add a little bit of vertex painting to this area.
[9:13] We will have a fire pit right there, so grass cannot grow in that place.
[9:19] Let's also create a path leading from the house to the fire pit.
[9:24] Because this area will be a focal point, let's place a tree over there. I decided to do it manually.
[9:36] That way, I can rotate and scale it the way I want without it affecting the scattered trees.
[9:43] I noticed the grass was quite sparse. I decided to increase the density. Now it looks more lush and nice looking.
[9:53] Let's add a new asset. Select the Decogon library and type track in the search bar. Select the rusty old one.
[10:02] I would like it to feel like it's been sitting there for a long time and some plants grew on it.
[10:07] I decided to use the version that doesn't have doors anymore. It gives it the feeling that some scrappers stole them alongside some other parts.
[10:19] Let's also clear the grass around it.
[10:38] For the main path, you can see that right now it looks too artificial. Let's add some grass and weeds along that path.
[10:54] Now it looks better.
[11:07] You will notice that there are no trees on the left and the right. We can still see the sky.
[11:14] Thanks to this system being procedural, you can select the point of the curve just to move them or extrude them.
[11:23] The trees will grow where you moved the points.
[11:27] When we bring back the forest, now we have a nice looking scene.
[11:31] You will notice that right now we have trees and grass. We don't have plants that are in between the size.
[11:43] So I decided to add some bushes in order to break that. Have some large, medium and small.
[11:51] You can add the bushes to the grass scatter by selecting the grass and going into the edit table of the scatter and adding a new element.
[12:01] Then you select your grass or your bushes and add them.
[12:08] Of course you have to play with the density. I decided to reduce the density to 0.1.
[12:14] Now it looks much nicer with a nice variety.
[12:21] One more thing that I would like to have is a path, a clear path from the cabin to the fireplace or the fire pit area.
[12:31] Now we can go to the fountain browser, go to Polyhaven and find a nice fireplace or fire pit.
[12:38] Place it where we would like it to be.
[12:41] Now we can go to the fountain browser, go to Polyhaven and find a nice fireplace or fire pit.


### Fireplace [12:44]
**Transcript (timestamped):**
[12:47] In our case, we would like it to be right in the middle of this soil area.
[12:55] I would like to also have some wood inside the fire pit. Later on we will also add a fire.
[13:02] I decided to add a fire pit.
[13:05] I decided to add a fire pit.
[13:08] I would like to also have some wood inside the fire pit. Later on we will also add a fire.
[13:16] I decided to use physics paint in order to place the wood inside the fire pit.
[13:21] Now let's now add the fire.
[13:25] I have a couple of assets or blueprints here that use fire.
[13:30] The blueprint are mostly comprised of Niagara particles and some textures.
[13:52] When working on a scene like this, composition is really important.
[13:57] That's why you will sometimes see me move around trees, rotate them or the truck for instance.
[14:04] I had to play a lot around with it in order to get a nice composition.
[14:10] Let's scatter some grass and weeds on the roof.
[14:21] In an overgrown environment, we can find some vines and plants hanging from the roofs.


### Vines [14:28]
**Transcript (timestamped):**
[14:35] Let's add that to our cabin.
[14:38] Open the content browser, then go to the Quixel library and select the broom creeper.
[14:45] Drag and drop it on your curve, select scatter on selection.
[14:50] You will see that they are scattered however their position is not correct.
[14:55] By disabling the use asset rotation scale, they will be in the correct rotation.
[15:00] Let's now create some vines on our truck.
[15:08] Open the content browser, select your atlases, drag and drop them on your truck and choose create vines on selection.
[15:17] The vines will be created.
[15:19] You can tweak some values like growth instance, growth size and seed in order to get the result you're after.
[15:49] Let's add some additional assets next to our fire pit.
[16:03] You will notice that these assets don't blend well with our terrain.


### RVT Blending [16:04]
**Transcript (timestamped):**
[16:10] Select the terrain and run the RVT command.
[16:18] Enable virtual texture on your scattered assets.
[16:24] Select the assets, go to the tools panel, click on the edit menu, then select edit material.
[16:30] Scroll down to enable virtual texture and check the box.
[16:35] Now our assets blend really well.
[16:40] Let's add some more vines.
[16:47] Now we're taking full advantage of the content browser in order to place the assets that we would like them.
[17:17] And our direct our scene.
[17:34] Now that area looks more natural.
[17:37] We can also have some assets next to the tree or right under the tree.
[17:43] At first I wanted to use this one.
[17:46] Then I realized that it doesn't match well.
[17:49] However, it can be placed right next to the tree and we can use another asset instead.
[18:01] We also enable RVT on this one just to make it blend with the scene.
[18:14] One more thing that I would like to do is have some vines growing along the tree.
[18:20] Right now the tree looks nice, however it can be a little bit more interesting.
[18:27] One of the important values here is mainly the seed.
[18:32] By playing with the seed I can get a lot of different variations.
[18:49] Now the result looks quite nice.
[18:58] I bring back the forest and we can see the composition.


### Lighting [19:01]
**Transcript (timestamped):**
[19:03] Now one of the important parts of any scene is lighting.
[19:09] I start by adding that small fire torch and then I call the lighting.
[19:14] I add first these spotlights.
[19:20] They are round a lot with the intensity and the unit as well as the attenuation radius and the volumetric scatter.
[19:45] Let's also put the light on the window up there.
[19:52] That way it will be visible from the outside.
[20:15] Next is the fire pit.
[20:19] I would like it to be quite bright, that way it will influence the vegetation surrounding it.
[20:27] Now I can adjust the volumetric on that window.
[20:58] We can also add some rocks on our main path in order to make it more interesting.
[21:05] By enabling RVT on the rocks it will give them the feeling of having moss.
[21:27] Next let's go to the dash bar and click on create.


### Fog [21:42]
**Transcript (timestamped):**
[21:48] Then select create fog card.
[21:51] A fog card will appear in the scene.
[21:53] You can move it around and scale it to your liking.
[22:03] By playing around with the cloud density and cloud brightness and color tint you will be able to change the color and its density to your liking.
[22:23] Let's place a couple of them in our scene in order to push back some of the trees and create some nice fogging behind the cabin.
[22:53] Depending on the value of your exponential height fog it is important to play with the cloud brightness in order for your color to be visible in your scene.
[23:04] The higher the brightness the more visible your colors will be.


### Camera Setup [24:22]
**Transcript (timestamped):**
[24:23] Next we can create a camera and add it in our scene.
[24:28] In the dash bar type camera and select create camera.
[24:35] Go to the tools panel, click on the edit menu and select edit camera.
[24:41] Now you will be able to edit your camera and see the result directly in the viewport.
[24:46] I like to play around with the focal length.
[24:48] Usually 24 gives a nice result and a good squeeze factor to make it feel cinematic as that's what we are going for.
[25:01] We can also add some post processing effects like grading presets.
[25:07] I like to go for bright sunny day.
[25:09] It looks really nice and some effects like film grain, vignette and sharpen.
[25:18] I notice that the cabin is facing too much towards the path.


### Final Tweaks [25:28]
**Transcript (timestamped):**
[25:36] It could look slightly more towards the left and we will see the side of the cabin and the light coming out of the window.
[25:44] I decided to rotate the cabin and this is the new composition that we get.
[25:52] Of course with the rotation we also need to adjust the roof.
[25:57] You will see that the grass is now a little bit offset to adjust that.
[26:02] Now we can place a rectangular light on the main path.
[26:15] It will bring in a little bit more warmth to the scene overall.
[26:25] It will also highlight the path.
[27:02] I also decided to reduce the start and distance of my exponential height bog.
[27:10] I also decided to reduce the start and distance of my exponential height bog.
[27:20] I noticed that the highlight on the tree is not strong enough which is why I decided to add another yellow light and place it right next to the trunk.
[27:35] It created a stronger highlight on that tree.
[27:43] There can be another fog separating the fire and the trees.
[27:51] This area right here was quite dark.
[27:57] I decided to add a rectangular light in order to make it more visible, especially at a distance.
[28:04] I decided to add a rectangular light to the tree.
[28:10] I decided to add a rectangular light in order to make it more visible, especially at a distance.
[28:21] Now it looks more natural.
[28:31] Last but not least, let's place some falling leaves in our scene.
[28:38] In the dash bar go to create then create falling leaves.
[28:43] You will see it appear in the scene. Select it and move it around to where you would like the leaves to be falling.
[28:52] I decided to place it next to the fire pit, of course above ground, that way it will feel like the leaves are falling down.
[29:00] I also increased the radius, the spawn radius to a value of 500 and put maximum leaf spawn rate.
[29:12] I hope you guys liked this video and I hope you will be able to implement some of the things you learned throughout this video in your own project.
[29:28] Leave a like and subscribe if you would like to see more.
[29:32] Thanks for watching.



---

## Captured Frames

- [1:27] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_000.jpg
- [2:46] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_001.jpg
- [4:15] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_002.jpg
- [5:11] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_003.jpg
- [6:27] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_004.jpg
- [11:51] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_005.jpg
- [15:08] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_006.jpg
- [16:30] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_007.jpg
- [22:03] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_008.jpg
- [24:48] tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/frame_009.jpg

---

## Structured Notes

### Core Technique
End-to-end procedural environment build in UE5 driven almost entirely from the Dash toolbar — Create Terrain with curve deformation, Road tool on a spline, vertex-painted material breakup, Surface/Path Scatter governed by proximity and object masks, vines, Runtime Virtual Texture blending, fog cards, and a Dash cine camera — so that moving one curve point re-propagates through terrain, road and scatter.

### Summary
A 29-minute full-scene tutorial building a forest cabin environment, structured in 12 chapters from bare terrain to final graded camera. The spine of the workflow is that nearly every element stays linked to a Dash curve or a mask rather than being hand-placed: curves deform the terrain and drive the road, then the same curves act as proximity masks that carve grass and trees away from the path and cabin, so composition changes stay non-destructive. The back half shifts from construction to look — RVT blending to seat scattered assets into the terrain [frame_007], fog cards for atmospheric depth [frame_008], practical lights around the fire pit and window, and a Dash cine camera with grading presets [frame_009]. The author repeatedly re-blocks composition (rotating the cabin, moving curve points) and lets the procedural setup absorb it.

### Key Steps
1. **Terrain** — type `terrain` in the Dash toolbar → **Create Terrain**; the terrain and the **Tools Panel** appear together. `Curved` hides the horizon line at eye level; `UV Scale` drives texture tiling [frame_001 shows `Uv Scale 3.0`, `Seed 954`]. Ctrl+drag materials from the Content Browser onto the terrain → **Apply Blend Material**, then **Edit → Edit Blend Material** → `Global Tiling` **2.8**, and enable **Tiling Control → Enable Breakup Tiling** to kill the visible repeat [frame_000 shows the Blend Material panel: R/G/B/S/T Weight, Global Tiling, Height Contrast, Height Intensity; transcript 1:19–1:45].
2. **Curves + terrain deformation** — type `draw` → **Draw Curve**, draw the path; `distance` thins the point count. In **Terrain Tool → Curve Deformation** add the curve and set `Width` / `Falloff` [frame_001: `Sampling 180.0`, `Width 13.33`, `Falloff 0.33`, `Project Curves` on]. Multiple curves are managed via **Edit Table** — `+` adds an item, then `+` under `Curve` assigns the curve; each item carries its own Width/position/rotation. One curve forms the path, a second levels the ground under the cabin (Width **11**) [transcript 2:46–3:41].
3. **Road** — type `road` → **Road tool**; with the curve selected, `+` under `Curves` in the Tools panel snaps the road onto it [frame_002: `Width 25.0`, `Inside Height 5.0`, `Border Height -6.0`, plus `Projection Mask` and `Full Mesh Projection`]. Any material can be applied — he uses a Megascans pine/American road material. The cabin (Fisherman's Cabin pack from Fab) is imported as the focal point.
4. **Shadow artifact fix** — console command `r.raytracing.normalbias 5` clears the shadow artifact on the terrain [transcript 4:51]. *(Transcript-only — not visible in a captured frame.)*
5. **Vertex painting** — switch to **Modeling Mode → Attribs → Paint Vertex Colors** [frame_003 confirms the mode and category]. Set `Brush Size` / `Strength`, enable **only the R channel**, set paint colour to black, and paint the path so the material stops reading as uniform.
6. **Scatter grass** — Ctrl+drag grass from the Content Browser into the scene → **Scatter here**. Base properties are `Density`, `Uniform Scale`, `Min/Max Scale`, `Pivot Mode`, `Scale Mode`, `Falloff`, `Sink` [frame_006]. Lighting is swapped here to set mood — the project carries Dash lighting blueprints (`Dash_Night_/Noon_/Overcast_/Sunrise_/Sunset_Lighting`) [frame_004].
7. **Mask the scatter back off** — select the grass scatter → **Proximity Mask** → `+` on `Objects`, add the curve, then tune the mask; repeat for road and cabin. The Proximity Mask section actually exposes `Objects`, `Distance` (10.0), `Width` (0.0), `Sampling` (256) and a `Proximity Table` with its own **Edit Table** [frame_005] — **there is no `Falloff` here**, despite the narration saying "width and falloff" [transcript 6:27]; `Falloff` lives in the scatter's Base Properties [frame_006] and in Terrain Tool curve deformation [frame_001]. A drawn circle added to the **Object Mask** clears the secondary focal point. The full mask set available on a scatter is `Feature Masking`, `Proximity Mask`, `Noise Mask`, `Object Masking`, `Border Masking`, `Edge Breakup`, `Directional Masking`, `Rotation Properties` [frame_004].
8. **Trees** — scatter mixed tree species for variety, drop `Density` to **0.2**, then clear them from paths with the same proximity-mask method. Behind the cabin, draw a curve and use **Path Scatter** (`scatter on selection`); add **jitter** to break the uniform spacing, and add the cabin to the proximity table where trees intersect it [transcript 7:12–8:40].
9. **Mid-layer bushes** — the scene reads as grass-then-trees with nothing between, so bushes (large/medium/small) are added *into the existing grass scatter* via the scatter's **Edit Table** → new element → assign meshes, `Density` **0.1** [frame_006 shows `Edit Table` beside the `Scatter` row; transcript 11:31–12:14].
10. **Fire pit** — a Polyhaven fire pit is placed as the secondary focal point, **physics paint** drops wood inside it, and fire comes from existing blueprints built on Niagara particles + textures [transcript 12:44–13:30].
11. **Vines** — roof vines: drag Quixel broom creeper onto a curve → `scatter on selection`, then **disable `use asset rotation scale`** to correct their orientation. Truck/tree vines: drag atlases onto the mesh → **create vines on selection**, then tune `growth instance`, `growth size` and especially `seed` for variation [transcript 14:35–18:32].
12. **RVT blending** — select the terrain and run the **RVT** command, then per asset: **Tools panel → Edit → Edit Material → Virtual Texture → Enable Virtual Texture**. The blend is controlled by `Slope`, `Edge Blend`, `Blend Falloff` and `Noise` [frame_007: `Slope 3.42`, `Edge Blend 1.58`, `Blend Falloff 1.17`, `Noise 1.0`]. Also applied to path rocks to fake moss [transcript 21:05].
13. **Lighting** — spotlights for the torch and fire pit tuned on `intensity`, unit, `attenuation radius` and **volumetric scatter**; a light in the cabin window so it reads from outside; the fire pit deliberately over-bright so it spills onto surrounding vegetation. Later a rectangular light warms the main path and a yellow light strengthens the tree highlight [transcript 19:03–20:27, 26:02–27:35].
14. **Fog cards** — Dash bar → **Create → Create Fog Card**, then scale/place. Controlled by `Base Color Tint`, `Cloud Density`, `Cloud Brightness`, `Cloud Contrast`, `Edge Fading Distance`, `Camera Fading Distance`, `Wind Speed`, `Wind Direction`, `Cloud Wind Tilling` [frame_008: tint `FFFFFF`, density `1.0`, brightness `2.0`, contrast `-2.3`, edge fade `300.0`, camera fade `1000.0`, wind speed `0.1`]. **Cloud Brightness must be balanced against the Exponential Height Fog** — the higher the brightness, the more the card's colour survives the height fog [transcript 22:53–23:04].
15. **Camera** — Dash bar → `camera` → **Create Camera** (a `DashCineCameraV2`), then **Edit → Edit Camera** for live viewport feedback [frame_009: `Focal Length ~24`, `Aperture 2.8`, `Focus Distance 2.0`, `Squeeze Factor 1.0`, `Sensor Width 36.0`, `Sensor Height 24.0`, `Aspect Ratio 16:9`, plus a `Control Camera from UE Details Panel` toggle]. Post FX via grading presets — he picks **bright sunny day** — with film grain, vignette and sharpen.
16. **Final tweaks** — the cabin is rotated for a better read of its side and window light; roof and grass offsets are re-fixed afterwards; Exponential Height Fog start distance reduced; and **Create → Create Falling Leaves** is placed above ground near the fire pit to finish [transcript 25:28–28:52].

### UE Systems / Blueprints / Settings
**Dash toolbar** — `Content · Place · Scatter · Create · Edit · Marketplace · Search` [frame_000]. Tools open into a dockable **Tools Panel**; `Edit` re-opens the panel for whatever is selected.

| Tool / Panel | Key properties (frame-confirmed) |
|---|---|
| **Terrain Tool** | `Uv Scale`, `Seed`, `Noise Deformation`, `Curve Deformation` → `Curves`, `Sampling`, `Width`, `Falloff`, `Project Curves` [frame_001] |
| **Blend Material** | `R/G/B/S/T Weight`, `Global Tiling`, `Height Contrast`, `Height Intensity`; `Tiling Control → Enable Breakup Tiling` [frame_000] |
| **Road Tool** | `Curves`, `Projection Mask`, `Full Mesh Projection`, `Width`, `Inside Height`, `Border Height`, `Shape Refining`, `Profile Settings` [frame_002] |
| **Surface Scatter** | `Surface`, `Scatter` (+ **Edit Table**), `Density`, `Uniform Scale`, `Min Scale`, `Max Scale`, `Pivot Mode`, `Scale Mode`, `Falloff`, `Sink`, `Randomize Sink` [frame_006] |
| **Scatter masks** | `Feature Masking`, `Proximity Mask`, `Noise Mask`, `Object Masking`, `Border Masking`, `Edge Breakup`, `Directional Masking`, `Rotation Properties` [frame_004] |
| **Proximity Mask** (expanded) | `Objects`, `Distance`, `Width`, `Sampling`, `Proximity Table` → **Edit Table** [frame_005] |
| **Edit Material (RVT)** | `Tiling`, `Displacement`, `Virtual Texture → Enable Virtual Texture`, `Slope`, `Edge Blend`, `Blend Falloff`, `Noise`, `Uvs` [frame_007] |
| **Fog Card** | `Base Color Tint`, `Cloud Density`, `Cloud Brightness`, `Cloud Contrast`, `Edge Fading Distance`, `Camera Fading Distance`, `Wind Speed`, `Wind Direction`, `Cloud Wind Tilling` [frame_008] |
| **Edit Camera** | `Control Camera from UE Details Panel`, `Focal Length`, `Aperture`, `Focus Distance`, `Squeeze Factor`, `Sensor Width/Height`, `Aspect Ratio` [frame_009] |

**Concrete values called out:** Global Tiling `2.8`; second deformation curve Width `11`; tree scatter Density `0.2`; bush element Density `0.1`; camera Focal Length `24`; `r.raytracing.normalbias 5`.

**Content Browser sources** seen in use across the build: `Quixel (old)` [frame_000, frame_002], `Fab` [frame_004], and `Project Library` [frame_005] — the Dash content browser switches source per asset family.

**Scene organisation:** Dash writes its output into a `DashToolsOutput` folder in the Outliner (`Terrain Tool_Terrain`, `Road Tool_Dash_Road`, `dash_curve` ×3, `Scatter Wild Grass`, `Scatter Mossy Rocks`, `Ivy` group, etc.), with a `DashSceneData` actor alongside [frame_004, frame_009]. Level is `H_Cabin_LVL`; the scene reaches ~1,020 actors by the camera stage.

> **Naming note:** `Cloud Wind Tilling` is spelled that way in the Dash UI [frame_008] — recorded as shown rather than corrected to "Tiling", so a grep against the panel matches.

> **Transcript note:** a few lines are duplicated by the transcriber around 12:38–13:08 and 27:02–28:10 (the same sentence emitted twice); these are artifacts, not repeated steps. "Fountain browser" at 12:31 is a mishearing of *content browser*, and "exponential height bog" at 27:02 is *Exponential Height Fog*. At 6:27 the narration says the Proximity Mask is tuned with "width and falloff", but the panel has no `Falloff` property [frame_005] — read that line as loose phrasing for `Distance`/`Width`.

### Difficulty
Intermediate

### UE Version
UE5, exact version not stated. The Dash bar carries both `Marketplace` and a `Fab` Content Browser source, and the Content Browser also still shows a `Quixel (old)` source [frame_000, frame_002], consistent with a UE 5.5+ editor during the Fab transition. Treat as UE5.x — no on-screen version string was shown.

### Tags
dash, polygonflow, procedural, terrain, curve-deformation, road-tool, surface-scatter, path-scatter, proximity-mask, object-mask, vertex-painting, vines, rvt, runtime-virtual-texture, fog-cards, environment-art, foliage, lighting, cine-camera, composition, world-building, intermediate, youtube, ue5

---

## Related Entries
- [Working Fully Procedurally in Unreal Engine 5 - Custom Asset Tutorial](working-fully-procedurally-in-unreal-engine-5---custom-asset-tutorial.md) — same author; the single-curve version of this idea (Path Scatter + proximity mask + Quick Pipe/Cable on one spline). Strongest overlap on proximity masking and curve-driven scatter.
- [DASH 1.12 - IMPROVED UE5 WORLD BUILDING TOOLS](dash-112---improved-ue5-world-building-tools.md) — nearest release-notes entry for the toolset used here; useful for dating individual tools.
- [DASH 1.10 - Procedural Scatter Presets in UE5](dash-110---procedural-scatter-presets-in-ue5.md) — path scatter, physics paint and preset workflow, all of which appear in this build.
- [DASH 1.11 - Unreal Engine World Building Just Got Easier](dash-111---unreal-engine-world-building-just-got-easier.md) — Content Browser / preset side of the same toolset.

> **Dash version not recorded.** The video (uploaded 2026-09-07) never states a Dash version on screen or in its description, and no version string appears in the captured frames. `plugin_version` is deliberately left `Not specified` rather than assumed to be the newest known entry (`dash-1.12`) — several tools shown here (Fog Card, Falling Leaves, Create Camera, RVT command) postdate the earlier entries and may belong to a later release.
