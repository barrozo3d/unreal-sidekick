---
title: Architecture Scenes Made Easy in Unreal Engine 5 - Dash Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=N7XLl348vG4
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.6
ue_version: "UE 5.x"
tags: [dash-1.6, architecture, archviz, scatter, radial-scatter, cable-tool, physics, ai-tagging, terrain, lighting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial/
frame_count: 17
---

# Architecture Scenes Made Easy in Unreal Engine 5 - Dash Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=N7XLl348vG4)
**Author:** Polygonflow Dash
**Duration:** 17m48s | 17 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Hello and welcome! In the previous video I showed you how useful dash can be in exterior space design.  Now it's time to demonstrate how quickly any other spaces can be brought to life using the real time power of dash,  lumen and the mega scan assets and how helpful this can be in ARCFIS project.  I show you how to utilize handy dash tools such as scattering tools,  the pipe and cable tools, physics tools, post processing and the helpful AI-taking system.  You can try dash for free and you can find all the assets I used down below.  I'm Tomash Norge, let's go!

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_000.jpg

### Adding and Adjusting Materials [0:33]
**Transcript:** I modeled the simple interior space in Blender, which I imported to Unreal Engine.  The models don't have materials yet, but I quickly changed it using dash.  I click on the dash icon, which brings up the toolbar.  I downloaded some materials and models from the mega scan library.  I simply drag and drop a concrete material onto the selected mesh, which I can easily modify.  As the next step, I will use the AI-taking system of dash.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_001.jpg

### AI Tagging Assets [1:00]
**Transcript:** Dash creates text for the assets, so I can search also for properties, not just names.  I click on the AI-taking button, which brings up the content browser.  I click on the compute button to start the process.  Now all my assets are available and ready to use.  I type the word book is in and dash fill list all the assets, tag with this tag for me.  If I want, I can edit my text individually.  I furnished the room with some furniture, all of which I downloaded for free.  You can find the links to these in the description.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_002.jpg

### Procedural Staircase with Radial Scatter [1:50]
**Transcript:** Next, I'd like to demonstrate the wide range of capabilities of the dash scattering tools.  First, I will create the spiral staircase using the radial scattering tool.  You also find the model for the staircase in the description, so you can try it out right away.  Before starting the scattering, I make sure that the mesh pivot point is in the correct position  and that the mesh location is set to zero.  Next, I type in radial and select the radial scatter tool.  I choose my mesh and click on the plus sign.  I want around 18 steps, so I set the count to that.  I set the radius to zero.  After this, I adjust the height and I already have the base of my staircase.  I quickly align the cylinder to the center.  I repeat the same process with the metal wires.  Creating a staircase was as simple as that.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_003.jpg

### Creating and Adjusting Cameras [2:55]
**Transcript:** I simply create the camera using dash and I can adjust the settings easily.  It's important to set up our camera angles early in the process  so that we don't waste time working on areas that won't be visible anyway.  Then I create another angle.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_004.jpg

### Foliage Wall [3:11]
**Transcript:** I want to scatter some plants on the wall.  I create the plane and align it to the wall.  This is where the plants will go.  I set the plant I like and while holding down the control,  I drop it onto the selected plane.  I choose scatter on selection and adjust the density, scale and other settings to my liking.  Feel free to play around with the settings a bit.  I will add another type of plant and use different settings.  And one more.  I don't want the leaves to hang over the wall across the window frame.  I simply duplicate my plane and scale it down.  In the surface scatter settings of my original plane,  under the proximity mask one section, I add the scale down plane by clicking on the plus sign.  In the distance section, I set the parameters and click on invert.  Now by moving the plane, I can adjust how far my plants extend.  I repeat the process on the other side as well.  I want to scatter some planters under the window.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_005.jpg

### Scattering Plants and Pots [5:02]
**Transcript:** I create the plane just like before.  I select a few planters and holding control,  I drop them onto the selected plane.  Here, I play around with the parameters until I achieve the look I like.  Once I find the composition I am happy with, I use the same option to hide the plane.  Next, I will place some vegetation into the planters.  I use this plate mesh to assist me.  I place the plate inside the planter.  I select the mesh and drop some plants from the desk library onto the selected mesh by holding down control.  I play around a bit and voila!  There's the last vegetation in the planter.  I can repeat this method several times with different plants and I also position some larger plants into the planters as well.  I type the word vegetation into the asset library and drag in any asset I like.  Since I have AI tag my assets, I simply type in the word firewood into the search bar and dash list all the assets tag with this tag for me.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_006.jpg

### Placing Assets with Physics Simulation [6:16]
**Transcript:** I select a few and simply drag them into the scene.  I adjust the scale and rotation of some models.  I select the physics tool from the toolbar.  A new bar popped up.  After selecting the objects, I make sure that they are set to dynamic.  Then I press the star button to begin the simulation.  I duplicate the locks.  I play around with the tool until I achieve the composition I like.  I can use the physics tool in multiple places.  I use the dash tool to create a curve.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_007.jpg

### Procedural Cables [7:41]
**Transcript:** My new favorite dash feature is the quick pipe tool.  I can quickly create cables for it for example.  Using the dash curve tool I create a curve.  I paste the base into 70 and then draw a curve freehand for the cable.  I can freely adjust the points individually.  Now I select the quick pipe tool.  After selecting my desired curve, I click on the plus sign in the curve section.  This creates a pipe around the curve for me.  I can adjust the radius as desired.  Then I refine the pipe in the smoothness section.  I apply a material and now I have a great cable.  I add another curve to the easy pipe.  If I want, I can always come back and adjust both the curve and the cable.  Nothing is baked in.  If I want, I can always come back and adjust both the curve and the cable.  Nothing is baked in.  I can scale it not only on meshes, but also on curves.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_008.jpg

### Scattering Hanging Foliage [9:16]
**Transcript:** I can scale it not only on the curve, but also on the smoothness section.  I will scale some hanging plants as well.  I type in the keyword plant into my asset library and select any plant I like.  Now let's add some details to the scene.  I draw some decals under the fireplace using dash.  I can scale my decals by holding down Ctrl and the left mouse button.  I can rotate it with shift and the left mouse button.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_009.jpg

### Placing Decals [10:03]
**Transcript:** I can scale horizontally and vertically by holding down Ctrl and the right mouse button.  I also play some decals under the fireplace.  I select them all and uncheck the received decals option in the details panel.  So the decals will only appear on the concrete beneath them.  I've also added some spots and cracks to other concrete surfaces.  Now I will scatter a few pieces of wood to add more details to the scene.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_010.jpg

### Physics Painting Details [11:18]
**Transcript:** I select some random pieces and click on the paint function of the physics tool.  By holding down shift and the middle mouse button, I can adjust the brush size and scale the pieces around.  Next I create the terrain, unto which I will later scatter some trees.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_011.jpg

### Procedural Terrain [11:54]
**Transcript:** I type in terrain and dash creates one in the viewport.  I can adjust it as needed.  In dash you can reach all the assets from Polyhaven and I will choose a free texture for the terrain material.  I can select the resolution and I drop it under the mesh.  Then I will adjust the UV scale.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_012.jpg

### Scattering Trees from Another UE Project [12:28]
**Transcript:** Next I want to scatter some trees.  In dash 1.6 you can easily access assets from other projects without needing the copy them separately.  Another project of mine contains Pegascan trees, which I can access in this project as well.  I select the project folder in the top bar.  As you can see, I can easily access the trees.  I select the view and drag them into the scene.  Let's create a dance forest.  I mask out my main building using the proximity mask.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_013.jpg

### Adding Lights [13:46]
**Transcript:** It looks quite dark, so I will add some lights.  At the start I will eliminate the armchair with a rectangle light.  I use the light source in other areas as well.  The back area isn't getting enough light, so I will place a larger light source near the windows.  I've put more effort to highlight some areas in the scene.  This corner here still feels a bit empty.  So I will use the cable tool of dash to create a string of lights here.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_014.jpg

### Procedural Light Strings [14:54]
**Transcript:** I drop in a simple cube, scale it down and duplicate it twice.  In the dash toolbar I can find the cable tool.  In the dash toolbar I can find the cable tool.  I select my cubes and now I press the plus sign in the object section.  Dash connects the three cubes with a cable.  I adjust the radius to my liking and then duplicate the cables a few times.  I can also adjust the gravity.  I model the simple light bulb, which I will scale along the cables I created.  I select it from the dash asset library.  I choose scatter on selection.  I set the scale, the surface alignment and the edge breakup.  And once again I can always come back and adjust my settings.  I will add some more place to perfect my composition.  As a final step, let's do some post processing.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_015.jpg

### Post Processing [16:28]
**Transcript:** I choose my camera and click on the adjust camera settings.  Here I can find you in my image.  I will add some more place to the image.  I will add some more place to the image.  I will add some more place to the image.  If you want to edit your footage even further,  you can make some adjustments into your result as well.  So here's the final scene.  I hope this video was helpful and if you'd like to learn more about Dash,  you can find plenty of tutorials on this channel.  Please feel free to leave a comment if you have any questions.  And if you like this video, consider subscribing to the channel.  And you can also join our Discord server,  where you can even share your creations with us.  Thank you for watching. Bye bye.

**Frame:** tutorials\frames\architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial\frame_016.jpg


---

## Structured Notes

### Core Technique
Full Dash archviz workflow by Tomáš — Blender-modeled interior brought to life with Materials, AI Tagging, Radial Scatter (staircase), foliage wall scatter with proximity mask exclusion, Quick Pipe Tool, Physics Paint, terrain, cross-project trees (Dash 1.6), IES/rect lights, Cable Tool string lights, and post-process camera polish.

### Summary
18-minute interior archviz tutorial demonstrating nearly the full Dash toolset in one project. Tomáš builds a Blender-imported interior space by layering: drag-drop concrete material, AI-tagged asset search, Radial Scatter for a spiral staircase (count=18, radius=0, adjust height), foliage wall with Proximity Mask invert for window exclusion, Physics simulation for debris and firewood, Quick Pipe/Cable Tool for cables and string lights, cross-project tree access (Dash 1.6 feature), rect/IES lights, decals with Received Decals disabled for concrete-only placement, and camera post-processing.

### Key Steps
1. **Apply Megascans material** — drag concrete/material from Dash Content Browser onto mesh; edit inline
2. **AI Tag assets** — click AI Tagging button → Content Browser → select folder → Compute; search by property (type `books`, `firewood`, `vegetation`)
3. **Radial Scatter (staircase)** — type `radial` → Radial Scatter Tool → add mesh → Count=18 → Radius=0 → adjust Height; repeat for balustrade wires
4. **Camera setup early** — type `camera` → CineCameraActor; set all angles before detailing invisible areas
5. **Foliage wall** — create plane aligned to wall → Ctrl+drag plant → Scatter on Selection → density/scale; duplicate plane scaled down → add to Proximity Mask → set Distance + Invert → moveable mask plane controls foliage boundary
6. **Planter vegetation** — place small plate inside planter → Ctrl+drag plants onto plate mesh → Scatter Here
7. **Physics simulation** — select logs/firewood → Physics Tool → Start → duplicate → adjust positions
8. **Quick Pipe/Cable Tool** — type `pipe` → draw curve (freehand) → Quick Pipe Tool → + curve → set Radius + Smoothness → apply material; add second curve for variation
9. **Physics Paint** — select wood pieces → Physics Tool → Paint function; Shift+MMB = adjust brush size
10. **Terrain** — type `terrain` → Dash creates terrain mesh; drop Poly Haven texture for material → adjust UV Scale
11. **Cross-project trees (Dash 1.6)** — select project folder in Content Browser top bar → access trees from another UE project → drag into scene → Proximity Mask to exclude building
12. **String lights** — place 3 cubes as anchors → Cable Tool → + objects → adjust Radius + Gravity → Scatter scatter light bulb mesh along cable → set Surface Alignment + Edge Breakup
13. **Post-processing** — Camera → Adjust Camera Settings → color grade, exposure, bloom, vignette

### UE Systems / Blueprints / Settings
- **Radial Scatter** — type `radial`; parameters: Count, Radius (0 = no offset), Height (Z stacking), Rotation step
- **Quick Pipe / Cable Tool (Curves)** — draw curve → add to pipe; parameters: Radius (thickness), Smoothness; non-destructive — edit curve = live pipe update
- **Physics Tool → Paint** — paint objects onto surfaces; Shift+MMB = brush size; random placement + physics settle
- **Scatter on Selection** — Ctrl+drag any asset onto plane → Scatter Here; scatter respects plane bounds; plane can be hidden after
- **Proximity Mask (invert)** — add a scale-down mesh as proximity actor; Distance + Invert = exclusion zone around it; moveable for real-time adjustment
- **Cross-project access (Dash 1.6)** — Content Browser → project folder picker in top bar; access assets computed in external UE project directly
- **Received Decals (UE Detail Panel)** — uncheck on selected mesh so decals only render on adjacent surface, not the selected one
- **Cable Tool → Objects mode** — add cube anchors to Objects array; Dash auto-connects cables between them with Gravity + Radius

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.6)

### Tags
`#dash-1.6` `#architecture` `#archviz` `#scatter` `#radial-scatter` `#cable-tool` `#physics` `#ai-tagging` `#terrain` `#lighting` `#intermediate`

---

## Related Entries
- [[how-to-create-procedural-cables-in-ue5---world-building-plugin]] — Cable Tool full reference (Objects/Curve/Mixed modes)
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Proximity Mask invert pattern
- [[new-physics-tool-for-unreal-engine-5]] — Physics Tool basics + Paint mode
- [[centralized-content-browser-for-ue5---free-plugin]] — Cross-project asset access (Dash 1.6) explained in depth
- [[beginner-guide-to-ue5-co-pilot-dash-camera-settings]] — Camera Tool + post-process settings
