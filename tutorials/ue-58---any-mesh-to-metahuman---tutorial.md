---
title: UE 5.8 - Any Mesh To MetaHuman - Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=ZmiTuYglaRI
author: Unreal - X - Tutorials
ingested: 2026-07-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ue-58---any-mesh-to-metahuman---tutorial/
frame_count: 0
frame_status: pending-selection
---

# UE 5.8 - Any Mesh To MetaHuman - Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=ZmiTuYglaRI)
**Author:** Unreal - X - Tutorials
**Duration:** 13m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ue-58---any-mesh-to-metahuman---tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, and welcome back to the channel. In this tutorial, we're taking static
[0:08] meshes, and turning them into fully animated meta-humans.
[0:15] Textures we transfer, but alignment and proportions, importance they are. Blender we use?
[0:26] Yes, but the body, the whole body must match, or it breaks.
[0:35] We'll also attach custom meshes, like my horns, directly to the meta-human skeleton.
[0:44] Don't correctly, everything follows.
[0:48] And then, it moves, it talks, it lives. Let's get started.
[0:57] Yes, I found a couple of interesting meshes on Sketchfab. You'll find the link in the description.
[1:06] Let's start with Darth Maul. I downloaded the GLB file.
[1:12] Then go to import and use the default settings, but make sure to enable Combine all
[1:19] under static meshes. Since the model doesn't include a body mesh without clothing, we'll
[1:26] only use the hat, and create the body from scratch in meta-human creator.
[1:31] So let's separate the hat. Switch to modeling mode, select mesh, and choose try select.
[1:41] Instead of brush, switch to buy material all. Click on the hat and the eyes. Then click invert
[1:50] and delete. Finally, hit accept.
[1:55] Now let's check the scale compared to a meta-human. The meta-human creator always uses this default
[2:03] meta-human for custom mesh wrapping. So go to export, geometry export, and choose full scale
[2:12] until mesh. Now we have a reference to scale and align our custom mesh. Bring it into the level.
[2:21] Zero out both meshes. Scale looks good.
[2:27] Now align the hat mesh close to the meta-human head.
[2:34] Open the modeling mode again, X form, and edit pivot. Set X, Y and Z to zero, and hit accept.
[2:47] Now open or create a new meta-human character. Go to import, choose from custom mesh,
[2:55] and select head and body. Drag our hat mesh into the slot. Position our model like this in the
[3:03] viewport, frontal, and centered to the camera. Open the manual solve actions. Now click on trace facial
[3:13] features. Sometimes you may run into this error message, failed to trace facial features.
[3:21] In most cases you can fix this by removing the material from the static mesh.
[3:26] Hit trace facial features again. You can also adjust the camera angle and try again.
[3:34] Then click auto-solve.
[3:40] If the result looks like this, perfect. Before doing anything else, we need to use save
[3:49] pose. This creates a DNA file with the original solved pose. We need this later for texture transfer,
[3:58] and for adding the horns correctly. As you can see, the horns are not solved together with a
[4:04] hat mesh. Everything that extends too far beyond a human head is ignored by the solva,
[4:12] such as horns or large ears. But we will add them later. Now I slightly adjust the body
[4:20] parameters. A little less fat and a little more muscle. I also think Darth Maul has very worn out
[4:29] teeth, so I'll try to recreate that. I also adjust the eyes to match the original look with these
[4:38] black yellow and red rings. Okay, next let's transfer the texture. Find the hat mesh we've used
[4:49] and export it. Using asset action, export. Disable level of detail and collision. Next,
[4:58] right click on the DNA file we saved from the creator plugin and select generate skeletal mesh.
[5:06] Then right click on the generated skeletal mesh and export it as well. Again, disable level of
[5:13] details and collision. Also export the original face texture. To transfer the texture to our
[5:21] metayuman mesh, we'll use blender. First import the DNA skeletal mesh. We only need the hat mesh,
[5:30] so we have to separate it. Select no mesh and switch to UV editing. Enable UV sync selection.
[5:40] On the left side, select the hat UVs. In the right window press P and choose separate by selection.
[5:48] Now import the original hat mesh. It should line up perfectly. But first we need to assign the texture
[6:01] we want to transfer. Select the hat mesh and switch to shading. Go to the materials tab,
[6:09] delete all existing materials and create a new one. Name it base color. Now drag out the base color
[6:18] and add an image texture color note. Click open and assign the exported face texture.
[6:27] Now select the DNA hat mesh. Again, delete the existing materials and create a new one.
[6:34] Add an image texture note, click new, name it something like Darth Maul base color,
[6:41] and set the resolution to 4096 by 4096 for a high quality texture.
[6:49] Now switch to the render settings. Set the render engine to cycles. Open the bake settings.
[6:56] Set the bake type to diffuse and disable direct and indirect lighting.
[7:02] Enable selected to active and set the extrusion value to 0.2.
[7:09] If your result is too far away, you can play around with this value to get different results.
[7:15] Something between 0.1 and 0.5 may give better results in your case.
[7:21] Now select the hat mesh first. Hold control and select the DNA hat mesh.
[7:28] Click bake. This can take a couple of seconds and gives us a very accurate transfer of the original texture.
[7:37] Let's see how it looks on our meta human.
[7:41] Click on the three lines, choose image and select save as.
[7:49] Import the image into Unreal. In the create plugin, go to materials, texture and material
[7:56] overrides, enable texture overrides and add an element for face.
[8:02] Choose base color and drag the imported texture into the slot.
[8:08] There might be a few minor issues, like these red dots on the back of the hat,
[8:13] nothing you can't fix in any image editing software.
[8:18] For the body skin, I simply use this black texture that comes with a Darth Maul asset.
[8:24] Finally, giving him the default cloth for now, but make it black.
[8:30] Okay, create a full rig. Download the texture source and assemble our Darth Maul meta human.
[8:39] I choose the UE optimized high version.
[8:44] The next step is to reattach the horns to the hat.
[8:48] So first we need to separate them.
[8:51] Double-kid the head mesh and drag the copy into the level.
[8:56] Switch to modeling mode, select mesh, choose try select and then select by material connected.
[9:04] Select the face into the eyes and hit delete.
[9:09] Now, select the remaining fragments from the eyes and the head and delete them again until only the horns are left.
[9:17] Then click accept.
[9:21] Oh, and we can reassign the original material to the horn mesh.
[9:27] If we now bring in our meta human and the horn mesh, you can see that they do not fit.
[9:35] But if we use our DNA skeletal mesh, the horns fit perfectly.
[9:41] So we need to bring our meta human skeleton into the same pose as the DNA skeleton.
[9:48] We temporarily modify the meta human reference pose for this process.
[9:52] However, we don't want to lose the original meta human reference pose because this could affect animations.
[10:00] That's why we first create a backup to save the original values.
[10:06] Go to the meta human's folder. Common, female, medium, normal weight, body.
[10:13] Here we find the meta human basis skeleton.
[10:17] Duplicate it and name it backup.
[10:21] Then go to meta human's dothmall, body and duplicate the body skeletal mesh as well.
[10:28] Name this one backup to.
[10:31] Right click on the copied skeletal mesh, go to skeleton and select assign skeleton.
[10:39] Choose the newly created backup base skeleton.
[10:43] Now we have an asset with the original reference pose safely stored inside.
[10:49] Open the original meta human body mesh and also open the DNA skeletal mesh.
[10:56] Place the windows side by side and enable edit skeleton on both sides.
[11:02] Now we copy and paste the bone transform values from the DNA skeleton to the meta human skeleton,
[11:10] starting from the root and going up to the head.
[11:14] Select the pelvis bone on both sides.
[11:17] Hover over transform.
[11:20] Shift and right click copies the values and shift and left click paste stem.
[11:26] Select the next bone and repeat the copy and paste process until you reach the head bone.
[11:40] Finally click apply to asset.
[11:46] If we now bring in our meta human and the horn mesh they line up perfectly.
[11:53] It's a little bit deformed because we only copied the bone chain from root to head,
[11:58] but that's enough to align the horns correctly.
[12:02] Find the horn mesh, right click it and convert it to a skeletal mesh.
[12:08] Choose use existing skeletal mesh and assign the Darth Maul body mesh.
[12:14] For the binding bone name choose root and hit convert.
[12:19] Now open the skeletal horn mesh, search for the head bone and select edit skin weights.
[12:26] Select mesh, then faces, select everything and click flood to make sure every triangle is selected.
[12:35] Now set the weight to 1.
[12:38] This means the head bone has a weight of 1 and all other bones have a weight of 0.
[12:44] Click apply to asset.
[12:48] Now we just need to drag the skeletal horn mesh into the meta human blueprint.
[12:53] Make it a shot of the body component.
[12:56] The horns will fit perfectly and stay attached to the head during animations.
[13:02] The last step is to restore the original meta human reference pose on the base skeleton.
[13:08] Open the original body mesh and the back up body mesh, side by side.
[13:14] Copy and paste the bone chain transform values from root to head back to the original skeleton
[13:20] just like we did before.
[13:22] And there we go.
[13:24] Darth Maul has been converted from a static mesh into a meta human.
[13:30] Okay, in part two of this tutorial, I'll show you how to work with a full character mesh,
[13:37] including body and head.
[13:39] We'll also improve the solving by adding additional tracking points.
[13:44] And I'll show you how to attach a meta human head to a completely different skeletal body.
[13:51] So stay tuned for Golan and Yoda.
[13:56] Cheers!



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
