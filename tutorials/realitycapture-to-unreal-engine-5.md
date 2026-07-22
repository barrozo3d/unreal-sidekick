---
title: RealityCapture to Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=kRD0rgCnOWQ
author: RealityScan
ingested: 2026-07-21
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/realitycapture-to-unreal-engine-5/
frame_count: 0
frame_status: pending-selection
---

# RealityCapture to Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=kRD0rgCnOWQ)
**Author:** RealityScan
**Duration:** 25m26s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py realitycapture-to-unreal-engine-5 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi there, my name is Jakub and I work as a Developer Relations Engineer at Epic Games.
[0:09] The Unreal Engine 5 has been officially released and I want to take this opportunity to show
[0:14] you how you can create a 3D model in Reality Capture and use it as a Nanite mesh in UE5.
[0:20] Nanite is a new virtualized geometry system that enables us to use increased geometry
[0:25] complexity, higher triangle and higher object counts.
[0:29] This was already demonstrated in the Valley of the Ancients demo with the Unreal Engine
[0:33] 5 Early Access.
[0:36] In this tutorial, I'll reconstruct the model of a wooden tower and import it to the medieval
[0:40] game environment created by my colleagues.
[0:42] Then, I'll be able to enjoy this playable experience with my custom asset from Reality
[0:47] Capture.
[0:48] In fact, all of the MegaScan assets used in this beautiful medieval village were once
[0:53] captured and processed by our very talented artists.
[0:57] I was lucky enough to stumble upon this tower during a walk near a forest and I immediately
[1:02] thought that it would nicely fit this environment.
[1:05] You might think that I used a drone or the proprietary Quixel scanning gear but I only
[1:10] used my personal 24MP full frame camera with a 24mm prime lens and a 4m long pole for attaching
[1:17] the camera.
[1:19] I used the pole to reach the upper parts and the tower's roof.
[1:23] I paired my phone with the camera to control the shutter.
[1:26] All together I captured over 900 images but not all of them were aligned.
[1:31] In the end, it wasn't a problem because all parts of the tower were successfully reconstructed.
[1:37] In Reality Capture, I'll use a standard workflow.
[1:40] I'll import the images and use the Detect Markers tool to automate the process of placing
[1:45] control points.
[1:47] Then, I'll import a distance definition from a text file to properly scale the scene.
[1:53] This is followed by the image alignment, setting up the ground plane, setting up the
[1:57] reconstruction region, model reconstruction, model cleanup, texturing, simplification and
[2:04] the texture reproduction.
[2:05] I'll export the model with 10 million polygons as an FBX with the Unreal Engine export preset
[2:11] and then I'll import it to Unreal.
[2:13] As I mentioned, I'll be using the medieval game environment that is free for download
[2:17] from the Unreal Engine marketplace.
[2:20] In Unreal Engine 5, I'll import the model with textures and build Nanite.
[2:24] I'll add some basic functionality to the generated material, create a material instance
[2:29] and apply it to the model.
[2:31] Finally, I'll place the model in the level and tweak the material instance so the model
[2:36] blends in with the environment more naturally.
[2:38] Alright, let's get started.


### Detect markers and alignment [2:40]
**Transcript (timestamped):**
[2:42] Here I am in Reality Capture and as always, the first thing I need to do is to import
[2:46] the images.
[2:48] I'll bring in my Explorer window.
[2:50] Here's a folder containing all of the images but this time I won't import all of the images
[2:55] at once.
[2:56] I will open the folder and select the first six images that contain only the scale bar
[3:01] with the coded markers and I'll drag and drop them into the user interface.
[3:06] I'm importing only these six images with the scale bar to speed up the detect markers algorithm.
[3:12] With all of the images, it would take significantly more time.
[3:16] If I expand the images node in the 1DS and select one of the images, for example this
[3:21] one, a new 2D view with the image will be displayed.
[3:25] Here I can zoom in with the mouse scroll wheel and here we can see the markers.
[3:30] They serve to automate the process of placing control points.
[3:34] I manually placed control points in the tutorial about creating a winter environment using
[3:38] Reality Capture, Quixel Mixer and Twinmotion.
[3:42] The link is in the description.
[3:44] The detect markers algorithm will place control points on these markers and then I will be
[3:49] able to define a distance constraint.
[3:51] The detect markers tool is located in the alignment tab right here.
[3:56] It can be used not just for detecting the markers but it can also generate them.
[4:01] In the generator I can specify how many markers I want, how many should be per page and the
[4:07] paper size which I left at A4.
[4:10] In the end I only used two markers.
[4:12] The marker type can be selected at the top.
[4:15] I used the first default option, Circular, Single Ring, 12-bit.
[4:20] To detect the printed markers the same marker type has to be selected.
[4:25] Here I can set the required number of measurements.
[4:28] I usually increase this value a bit to prevent false positives.
[4:31] I usually use 3 but it wouldn't matter for these 6 images because I don't expect any
[4:36] false positives.
[4:38] Finally I can select the image layer that is supposed to be used for detecting the markers.
[4:43] Right now I only have a single image layer which is the geometry layer.
[4:47] To run the algorithm I'll press detect.
[4:51] The detect markers algorithm did its job.
[4:54] When I expand the control points node in D1DS we see two new control points both of which
[4:59] were detected on all 6 images.
[5:01] They are also visible directly in the images displayed in the 2D view.
[5:06] Now I want to tell RC that the distance between these two markers is 60 cm.
[5:12] I'll use the distance definitions from the workflow tab to import a text file with the
[5:15] definition.
[5:16] I will bring in my explorer window and open the distance definition.
[5:22] The file contains only one distance definition but there could be multiple.
[5:26] It has 4 columns and the first column is the name of the distance so in this case it's
[5:31] distance 1.
[5:33] The second and third columns are the names of the control points that will define the
[5:36] distance.
[5:37] They have to match the names in RC.
[5:40] And finally the actual distance in the coordinate system units.
[5:44] I'm using the default local Euclidean coordinate system with the meters as the units.
[5:49] So this distance is 60 cm.
[5:52] Now I can close it and get this window out of the way.
[5:56] I'll click on distance definitions, select a file and click open.
[6:01] In the import dialog I have to match the file format and value separator with the file
[6:05] containing the distance definition.
[6:08] These are the defaults and I created the file with these default settings in mind so it
[6:12] should be correct.
[6:14] The file format is the name of the distance, point A, point B and the distance itself.
[6:20] That is correct.
[6:22] The value separator is space which is also correct.
[6:25] There is no need to ignore the first line and the coordinate system is local Euclidean.
[6:31] In the imported data accuracy I can also edit the accuracy of the measurement but I'll
[6:35] leave it at the default value of 1 mm.
[6:38] I used a ruler with mm division to measure the distance so 1 mm is appropriate.
[6:44] Now I can click on OK.
[6:46] When I expand the constraints node in D1DS we can see the distance 1.
[6:51] In the properties we can see that the file was correctly imported.
[6:55] We don't have the calculated distance just yet because we don't have an existing alignment.
[7:00] For the alignment I'll import the rest of the images.
[7:04] Again I'll bring in my explorer window.
[7:07] This time I can select the entire folder with the images and drag and drop it to the user
[7:11] interface.
[7:12] RealityCapture will recognize that the first six images are already imported so there won't
[7:17] be any duplicates.
[7:19] And now I can just click on Align Images.


### Mesh reconstruction [7:21]
**Transcript (timestamped):**
[7:23] The alignment is finished.
[7:25] In the 3D view we can see the sparsing reconstruction and the camera positions.
[7:29] In D1DS we can see that RealityCapture created one large component that contains most of
[7:35] the cameras and a bunch of small components that contain from 2 to 10 cameras.
[7:40] I shot way more images than I needed for a successful reconstruction so a couple of
[7:45] unaligned images shouldn't be a problem.
[7:47] I don't see any holes in the reconstruction so the final mesh should be fine.
[7:52] If you want to know which cameras are not aligned in this large component ensure it
[7:56] is selected, switch D1DS to 2DS, go to the Scene2D View tab and click on Show Unregistered.
[8:04] There is a bunch of detailed shots and some images from the inside of the tower that were
[8:08] not aligned.
[8:09] As I said a couple of missing images should not be a problem.
[8:13] There could be a couple of reasons why they are not aligned.
[8:16] There could be blurry images, not enough common features between neighboring images or simply
[8:21] they were above the accuracy threshold and RealityCapture decided not to use them.
[8:26] You may want to try align them.
[8:28] Sometimes a simple second alignment can do the trick or you can use control points and
[8:32] realign with the control points.
[8:34] I won't bother with that this time so the next step is to set up the ground plane and
[8:38] the reconstruction region.
[8:40] I'll go to the Scene3D Tools tab and click on Set Groundplane to activate the widget.
[8:45] I'll switch the layout to 1 plus 1 to have a large 3D view.
[8:49] I like to adjust the ground plane with the help of orthographic views.
[8:53] They can be toggled in the Scene3D View tab right here.
[8:57] Or you can use the number pad.
[8:59] So I will do that.
[9:01] To enter the top view you can press number 2 on the number pad.
[9:04] First, I'll rotate the scene so the front of the hunting tower faces the right side.
[9:10] I am doing this so the exported model has the proper orientation in Unreal Engine.
[9:16] Besides rotating the scene, I'll try to place the tower in the middle of the grid.
[9:22] Something like this.
[9:23] Next, I will switch to one of the side views by pressing 5 on the number pad.
[9:29] In this view, I'll check if the tower is in the middle of the grid and I will adjust
[9:33] the bottom of the scene so it sits on this black line.
[9:40] Ok, that should be good.
[9:43] To get back to the perspective view, I will press number 0 on the number pad.
[9:48] Now I can deactivate the set ground plane tool by clicking on it again.
[9:53] To reset the reconstruction region, I'll click on the set reconstruction region command
[9:58] and again, I'll adjust it in the orthographic views.
[10:01] Number 2 on the number pad to enter the top view.
[10:04] I'll use the box widget to adjust the sides.
[10:08] If the widget is not visible, just click on the reconstruction region with the left mouse
[10:12] button.
[10:13] I'll also switch to the side view by pressing number 5 on the number pad and I will adjust
[10:18] the top and the bottom.
[10:21] I'll press number 0 on the number pad to enter the perspective view.
[10:25] And that's it.
[10:26] To launch the reconstruction, I will go to the mesh model tab and click on create model
[10:30] on normal detail.


### Mesh clean up [10:32]
**Transcript (timestamped):**
[10:33] The reconstruction is now finished.
[10:35] I'll switch the 2DS back to 1DS.
[10:38] If I expand component number 10, we can see that the model number 1 has around 139 million
[10:44] triangles.
[10:46] In the 3D view, we can see it in the form of a very dense point cloud and the reason
[10:50] for this is that it has so many polygons.
[10:53] Reality captures real-time render limit is 40 million to enter a smooth experience.
[10:59] Before I do any texturing and simplification, first I want to do some cleanup.
[11:04] Reality captures meshing algorithm creates watertight meshes.
[11:07] In this case, it fill out the bottom with large triangles.
[11:11] We call them marginal triangles.
[11:14] Right now, they are not visible because of the point cloud rendering.
[11:17] To display them, I'll use the clipping box.
[11:20] I will go to the scene 3D view tab, expand the clipping box and click on create from
[11:26] reconstruction region.
[11:28] Now I'll enable editing and bring the top of the clipping box all the way down.
[11:34] I will also make it larger so it doesn't clip the marginal triangles.
[11:39] The mesh parts should start loading if the rendering mode is set to solid.
[11:43] Now the large triangles are visible.
[11:45] I want to get rid of them.
[11:47] Now there's a couple of ways how I can do that.
[11:50] I could go to the scene 3D tools tab and use the advanced selection tool to select the
[11:54] marginal triangles and filter them out like I did in the winter environment tutorial.
[12:00] But this time, I will try something different.
[12:03] I will disable the tool, deselect the triangles and use the cut by box tool instead.
[12:09] First I'll select the reconstruction region and slightly adjust it.
[12:13] I'll enter the top view and make the reconstruction region slightly smaller.
[12:20] Like this.
[12:21] Next, I'll go to the side view by pressing the number 5 on the number pad and adjust
[12:26] the bottom.
[12:29] I want to cut everything outside of this reconstruction region so I'll use cut outer.
[12:35] Fill cut holes should be set to no because that's not what I want.
[12:39] Now I will just click on cut outer.


### Texturing [12:42]
**Transcript (timestamped):**
[12:43] The cut by box is finished so we have a second model.
[12:46] This time it is without the large triangles at the bottom.
[12:49] Now I can get rid of the clipping box so I will go to the scene 3D view tab and clear
[12:54] the clipping box.
[12:56] Now I have a couple of options.
[12:58] I could simplify the model and texture it later.
[13:01] But I prefer to texture the clean highest resolution model I have with the fixed textile
[13:05] size and optimal textile size to get the best possible texture quality.
[13:11] Then I'll use this high poly version to create simplified versions and bake the textures.
[13:16] To texture it I'll go to the mesh model tab and click on the texturing settings.
[13:21] In the unwrapped parameters I'll switch the maximum texture resolution from 8k to 16k.
[13:28] Next I'll set the style to fixed textile size.
[13:31] I'll keep the textile size set to optimal which is the smallest possible textile that
[13:36] provides the best detail.
[13:38] This way I will get the best possible texture that I can get from the input images.
[13:42] I'll also increase the large triangle removal threshold to 100 to ensure that even larger
[13:48] triangles are properly unwrapped and textured.
[13:51] Now I can start texturing.


### Simplification [13:54]
**Transcript (timestamped):**
[13:56] The texturing is finished so now the model has colors and we can see them in the 3D view.
[14:01] If I expand model number 2 we can see that the fixed textile size with the optimal textile
[14:06] size created 5 16k textures which is a lot.
[14:11] The next step is the simplification of this model.
[14:14] In this step I will create the final model that I will use in Unreal Engine 5.
[14:19] To do that I will use the simplify tool.
[14:21] The tool is located in the scene 3D tools tab right here.
[14:26] I want to use a model with 10 million polygons in UE5 so I'll keep the type set to absolute
[14:31] and I'll set the target triangle count to 10 million.
[14:35] In the winter environment tutorial I use the simplification tool to also bake the color
[14:40] and the normal map textures.
[14:42] This time I will keep the texture projection disabled because I want to show you another
[14:47] way that gives you more control over the unwrapping of the simplify model and also more control
[14:52] over the texture projection.
[14:54] Now everything is set so I'll click on simplify.


### Unwrap [14:58]
**Transcript (timestamped):**
[14:59] The simplification is now finished.
[15:01] We have a new model number 3 with 10 million polygons.
[15:05] Because the texture projection was disabled it doesn't have textures or UVs.
[15:10] We'll do them manually.
[15:11] The colors that we can see in the viewport are only vertex colors.
[15:16] First I'll create the UVs with the unwrap tool.
[15:19] I'll disable the simplify tool and close the texturing settings.
[15:23] The unwrap tool is in the mesh model tab right here.
[15:27] For the texturing of the high poly mesh I used the fixed textiles size that created 5 16k textures.
[15:33] I could also use the same settings but that resolution is not necessary for my purpose.
[15:38] I'll go for one 16k texture.
[15:41] I'll leave the style set to the maximal texture count and the maximal texture count set to 1.
[15:47] I'll also increase the large triangle removal threshold again to 100 and click on unwrap.


### Texture reprojection [15:54]
**Transcript (timestamped):**
[15:55] The unwrap is finished.
[15:57] Okay now I'll use the texture projection tool to bake the texture.
[16:01] I'll disable the unwrap tool and enable texture projection.
[16:05] The tool is located next to the simplification tool in the scene 3d tools tab.
[16:10] You might ask why am I using this tool?
[16:13] Well it takes significantly less time to bake the texture from the high resolution source model
[16:18] than to texture the simplified model from scratch.
[16:21] I need to specify the source model so that's my high resolution model number 2.
[16:26] My result model is this model number 3.
[16:29] Color reproduction is already enabled by default and I can also enable the normal map texture
[16:35] projection. I went from 139 million polygons to 10 million polygons.
[16:41] So many lost details can be stored in the normal map texture.
[16:45] Now I'll press project to start the process.


### Export [16:48]
**Transcript (timestamped):**
[16:49] The texture projection is now finished.
[16:51] Model number 3 has 116k color texture and 116k normal map texture.
[16:57] This is my final model and texture and now I will export the model as an FBX.
[17:03] I'll click on the RC icon and click on export.
[17:07] I already have FBX in my recently used formats.
[17:11] I'll pick where I want to save it that will be my export folder and I will simply call it tower
[17:17] and click on save.
[17:19] In the export dialog I'll enable export normals and disable export vertex colors because I will
[17:25] need them. The texture will be saved as a PNG which is fine with me.
[17:31] The coordinated system will be the grid plane and then in the export transformation settings
[17:37] I'll pick the Unreal Engine preset.
[17:39] This preset scales the mesh 100 times and then I don't have to modify the scale during import
[17:45] to Unreal. This preset also flips the wide channel of the normal map so it properly works in Unreal.
[17:52] Now I will click on OK.
[17:55] And that's it. I'm finished in reality capture and now I will jump into Unreal Engine to import
[18:00] this model. If you don't have Unreal Engine 5 already installed go ahead and install it through


### Medieval Game Environment [18:02]
**Transcript (timestamped):**
[18:07] the Epic Games launcher. In the marketplace search for the medieval game environment and
[18:12] create a new project with it. Once it's downloaded open the project with UE5.
[18:19] Here I am in the Unreal Engine 5 editor with the medieval game environment already loaded.
[18:24] I have the main startup level loaded and everything works straight out of the box.
[18:29] I'll just import the mesh from RC, make a basic setup and place it in the level.
[18:34] Now first I recommend you to go and explore this environment.
[18:38] It is also a fully playable experience so definitely try it out.


### Importing the mesh to UE5 [18:42]
**Transcript (timestamped):**
[18:42] There's a lot of things going on in the 3D viewport so I will press G on the keyboard to enter
[18:47] the game view mode. That will get rid of everything. The first thing I need to do is to import my mesh
[18:55] from reality capture. I will open the content drawer and I will click on dock and layout.
[19:03] In the content drawer I want to make these icons smaller so I will press control and use the mouse
[19:09] scroll wheel. In the content folder I'll add a new folder and call it reality capture.
[19:20] I'll press enter to confirm the name and I'll double click it to open the folder.
[19:27] Now I'll click on import. In the explorer I will select my mesh from reality capture
[19:34] and click on open. In the import options I am using the default settings.
[19:40] Just make sure that build.nite is checked. Unreal will also import my textures and it will also
[19:46] create a material for the model. Now I can just click on import and now based on the size of your
[19:52] mesh it may take a couple of minutes to import the asset into unreal. The assets are loaded so we
[19:59] can see the mesh, here is the material and here are the textures. You can rename the assets if you
[20:05] want but I'll keep the original names. This star icon on the asset means that they were not saved
[20:11] yet so I will click on save all and wait. The assets are saved. Virtual texture support is
[20:20] enabled for this project and because of the 16k resolution of the textures virtual texture streaming
[20:26] was automatically enabled for them. It can be disabled in the texture details. The auto virtual
[20:33] texturing setting size can be changed in the project settings. Now I will open the material


### Editing the material [20:36]
**Transcript (timestamped):**
[20:38] that was created for me because I want to edit it. I want to have more control over some settings.
[20:44] Mainly I want to control the brightness of the color texture and I also want to have control
[20:49] over the roughness of the material. I'll use multiply and a scalar parameter to control the
[20:55] brightness of the texture. I will press M on the keyboard and left click in the node graph to create
[21:00] the multiply node. Now I also need a scalar parameter to control the brightness so I will
[21:06] press S on the keyboard and again click in the node graph. Right away I will rename this parameter
[21:12] to brightness. I will connect brightness to the A input and I will connect the texture to the B input.
[21:19] The order doesn't matter because it's multiplication. I will connect the output of the
[21:24] multiply node to the base color of the material. Right now the brightness is set to zero and when
[21:30] you multiply anything with zero the result is zero. So in my case that returns a black color of the
[21:37] material. That's not exactly what I want so I will set the default value to be one. That means the
[21:43] brightness won't change. To control the roughness I will again create another scalar parameter
[21:49] so I will press S on the keyboard and click in the node graph. This time I'll rename it to roughness
[21:56] and I'll connect it to the roughness of the material. I will set the default value to 0.5.
[22:02] That's a good starting point but I will tweak it later in the material instance.
[22:07] So now I can save it and close it. Out of this material I will create a material instance.


### Creating a material instance [22:10]
**Transcript (timestamped):**
[22:15] The reason why I'm doing this is to have control over the brightness and over the roughness of the
[22:19] material in real time. Now when I open it I can enable the options for editing the brightness
[22:26] and roughness. I won't make any changes just yet. First I'll apply the material instance to the mesh.
[22:33] Let's minimize this for now. I'll open the mesh. Currently the mesh is using the original material
[22:42] so to apply the material instance I will just drag and drop the material instance to the material
[22:47] slot. Now I can save the mesh. The mesh is saved so now I can close it. For now I will only minimize
[22:58] the material instance. Now I will place the tower into the level and I think that somewhere around


### Placing the mesh in the level [23:00]
**Transcript (timestamped):**
[23:05] here will be a good place for the tower so I will move in closer. I will drag and drop the tower
[23:11] into the level like this. I will switch to rotation and I will rotate the tower so it faces the field.
[23:21] Now I will switch back to translate objects and I will move it back like this.
[23:28] I also want to hide the original scan ground so I will move it down.
[23:35] I think that's good enough.
[23:39] Now right away we can see that the tower is too bright so I am going to edit the material instance.
[23:45] I will switch from lit mode to unlit and now we can see that the brightness is even more obvious.
[23:52] I will open the material instance and set the brightness to around 0.4.
[23:59] And now I think that the color of the tower blends in the environment more naturally.
[24:04] Now I am going to switch the unlit mode to a buffer visualization.
[24:10] Roughness. We can see that right now it also stands out. White means 100% roughness and black
[24:17] means no roughness. I will increase the roughness to let's say 0.9. I think that this is more
[24:28] appropriate for the tower. Now I will switch back to the lit mode and I think that the tower
[24:36] blends in the environment more naturally. You definitely can spend way more time on this
[24:42] making a more complex material and tweaking everything. But I think it's time for me to
[24:47] play the experience so I will save the material instance and close it. Now I can press play.
[24:55] I hope you enjoyed watching this tutorial as I did making it. We covered every single step of
[25:02] making and bringing the asset from Reality Capture to Unreal Engine 5. You should be able to turn
[25:08] your own scans into UE5 assets with ease. If you have any thoughts or questions feel free to drop
[25:15] them to the comments of this video. See you in the next one!



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
