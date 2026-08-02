---
title: Adding Multiple Detail Meshes to Landscapes - Procedural Content Generation (PCG) - Episode 4
source: YouTube
url: https://www.youtube.com/watch?v=ceP88Hvopao
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, materials, landscape, hlsl, blueprint, pipeline, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Adding Multiple Detail Meshes to Landscapes - Procedural Content Generation (PCG) - Episode 4

**Source:** [YouTube](https://www.youtube.com/watch?v=ceP88Hvopao)
**Author:** Ben Cloward
**Duration:** 25m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, we're going to add multiple sets of detail meshes to our landscape.
[0:06] Let's go!
[0:14] Alright, to create a beautiful looking landscape, there are several different elements you can control.
[0:21] Two of those elements are the landscape material and the detail meshes that get added to the landscape.
[0:29] So far in this series, I've shown you how to create a PCG grass system that automatically adds grass.
[0:38] But the grass is just one type of detail mesh.
[0:42] We can add all kinds of detail meshes to the landscape.
[0:47] What I like to do is pair up the detail meshes that I'm adding with the types of materials on the landscape itself.
[0:56] The materials and meshes become partners, supporting each other in creating the look that I'm going for.
[1:04] Let me show you what I mean.
[1:06] Here are the grass textures that I'm using on my landscape.
[1:12] This one looks lush and mossy, and this other one is more dry and rocky.
[1:19] If we take a look at the landscape itself, you can see that the mossy, lush version of the grass is applied down here at the lower altitudes.
[1:32] And the dry and rocky version of the grass is applied up here at the higher altitudes.
[1:40] So what I want to do is to select some meshes that I can use as detail meshes on my terrain that match the textures that I'm using.
[1:50] If we take a look at this one, you can see that my grass is a lot more dry and this material here is filled with all kinds of little rocks and pebbles.
[2:02] But if we switch over to this one, you can see that this would support grass that's a lot more lush.
[2:09] So what I need to do is to find some meshes that I can use to put on these materials.
[2:16] So let's switch back here to our landscape and we'll take a look at the meshes that I've selected.
[2:23] And here we have three different kind of lush grass meshes that I'm using.
[2:29] These are the ones that I showed you how to use in the previous two episodes.
[2:34] And then I've also selected this collection of kind of pebbly rocks.
[2:39] And then this collection, it's called...
[2:44] So the ones back here are called grass clumps.
[2:48] And then the ones here in the front are called thatching grass.
[2:52] These are the ones that I selected for the drier area.
[2:57] So our drier area is going to have these pebbles on it and it's going to have this thatching grass.
[3:04] And then our more lush grass in the low altitudes is going to use the grass that we created in the last two episodes already.
[3:12] So the first thing that we need to do is switch over to our landscape material
[3:17] and create the grass masks that we're going to use that determine where these different assets are placed on our landscape.
[3:27] So here's our landscape material and we built this material in the last series of videos.
[3:33] And in the last couple of videos, we've been using this material to determine where our grass should be placed.
[3:40] So if we take a look over here, you can see that we've got our lush grass material and we've got our rocky dry grass material.
[3:50] And they're being blended together based on altitude.
[3:55] And then we blend between all of our grass types and our slope material based on a terrain angle mask.
[4:08] So what we need to do is change the masks that we're using.
[4:12] The one that we made last week was for all of the grass.
[4:16] And we need to divide it up so that we can create one mask for our lush grass and another mask for our dry grass.
[4:25] So that's what we've done.
[4:27] Let's take a look right here.
[4:29] So the first thing that we have here is our terrain angle mask.
[4:33] And this is masking out our terrain so that it only appears in the flat areas and not in the slopes.
[4:41] Then we multiply our terrain angle mask by one minus our snow mask so that we're not getting grass in areas where there is snow.
[4:51] And then again, we multiply it by one minus the mask that we're using for our water puddles so that we don't get grass in the puddles either.
[5:03] And this gives us a good mask for our base grass.
[5:09] But we need to differentiate between our dry grass and our lush grass.
[5:17] And so that's what we're doing here.
[5:19] Here we have a mask that's coming from our dry grass mask.
[5:28] And if we wire this mask directly into our base color, let's save this and take a look at our landscape and see what it's doing.
[5:39] So here you can see our dry grass is appearing up here in the higher altitudes.
[5:47] But our lush grass is the black area of the mask and it's only appearing down here in our lower altitudes.
[5:55] So if we want a mask that is our lush grass, we can just take the inverse of this mask using a one minus.
[6:03] And that's what we've done right here.
[6:04] So we take our base grass mask and we multiply it by one minus the dry grass mask.
[6:13] And that gives us our grass mask that we were using last week, but we've subtracted out the dry grass portion of it.
[6:22] So if I grab this and plug it into our base color.
[6:26] Now you can see here we're getting a mask that just gives us our lush grass and it's black up here in areas where our dry grass is going to appear.
[6:41] Okay, let's go ahead and create the other masks now.
[6:45] So that's our lush grass.
[6:48] For our dry grass, instead of using one minus our dry grass, we can just round our dry grass mask and then multiply by it directly.
[7:01] But then the next thing that we want to do is remove the stones.
[7:06] So there are areas in this texture here where there are rocks and we want to mask out those rocks so we don't get grass.
[7:15] Spawning on areas in the in the texture itself where there are rocks.
[7:21] And I'm doing that here in my material using a levels adjustment.
[7:28] So it's basically like taking your texture into Photoshop and applying levels adjustments there.
[7:34] But I'm actually taking the dry grass texture here and passing it into a levels adjustment so that I can make it white where there are rocks and black where there are not.
[7:53] So let's wire this into our base color and take a look at what the result of that levels adjustment is getting us.
[8:00] So here you can see I'm creating a mask that's white wherever there are rocks in the texture.
[8:10] And so I'll be able to use this mask to spawn rocks in those areas and to spawn dry grass in the other areas.
[8:19] So that is creating my rocks texture.
[8:23] And if I do one minus that and then multiply that by my dry grass, that's going to give me a dry grass mask that does not have rocks in it.
[8:35] So let's go ahead and wire this one in and take a look.
[8:37] And now you can see I've got a mask that's white where the dry grass should go, but it's black where all of the rocks in the dry grass material are.
[8:54] So I can spawn dry grass in these areas and I can spawn lush grass down here in these areas.
[9:01] And then for my stones mask, obviously I can just take the result of my three point levels adjustment and wire that directly into my landscape grass stones input.
[9:17] Okay, and then the last thing here for this landscape grass node here, I've gone ahead and added three array elements.
[9:27] The first one we had from the last two episodes and I just called it grass.
[9:33] But the next one I've called dry grass and then the third one I've had, I've called it stones.
[9:39] And you can add an array element by just hitting this plus button here.
[9:43] Now each of these array elements needs to have its own unique grass type plugged in.
[9:49] And so I went ahead and created three grass types.
[9:53] The one that we had from before was called LGT PCG grass.
[9:58] And then I just duplicated it and called it LGT PCG dry grass and LGT PCG stones.
[10:09] And then I just plugged each of these three assets into the grass type slot.
[10:14] And so what that does is it takes the mask that I've created here in my material and puts it into that asset so that then I can reference it in my PCG graph.
[10:28] All right, now that we have our grass masks set up in our landscape material, let's go ahead and use them in our PCG graph.
[10:39] So here is the PCG grass graph that we created in the last two episodes and nothing has changed here really except the mask that I'm passing in here is now using the new mask that we created that has the dry grass and the stones removed.
[11:00] So I'm only going to get the lush grass in areas where I don't get the dry grass.
[11:10] So I took this graph and I duplicated it.
[11:14] So you can see here I have my PCG grass that we already created in the last two episodes.
[11:19] I made a copy of this and I renamed it to PCG dry grass.
[11:24] So let's take a look at the differences here.
[11:27] The first thing that I did is I set the point generator here to generate 10,000 points.
[11:36] I think the other one was maybe creating like 3500 but the dry grass assets are much smaller and compact.
[11:43] And so I need more of them to fill up the space and so I'm using 10,000 points in each of my grid chunks instead of 3500.
[11:53] The next thing that I did is on this generate landscape textures node in this select grass types element you can see that I've renamed this.
[12:05] It used to just be LGT PCG grass and I've made it LGT PCG dry grass.
[12:12] So now I'm passing through the dry grass mask instead of the dry grass.
[12:18] And in our point generator here I've made a couple of changes to the HLSL code.
[12:26] The biggest, like the most important one is here under this grass mask chunk that we added last week.
[12:33] I've changed the name of the grass type to be PCG dry grass.
[12:39] So we're using that mask instead of the grass mass texture.
[12:43] And then the one other thing that I did, if you take a look here under PCG grass, there's this section here called spatial noise.
[12:54] And it creates this spatial noise parameter which we then subtract from the density.
[13:01] And that gives kind of an organic feeling to the grass where it shows up in some places and doesn't show in other places.
[13:11] Well I went ahead and removed that spatial noise from my dry grass version because the grass map that we're passing in from the landscape material is already serving that purpose.
[13:25] It already breaks up where the dry grass is being applied.
[13:29] So I can save some GPU performance by removing that spatial noise and not doing that calculation in our compute shader.
[13:38] So I altered this code just a little bit.
[13:42] Basically all I had to do was remove this spatial noise section here and then remove this one line where I say density minus equals spatial noise.
[13:55] So this line and these four lines and the comment I removed from my PCG dry grass.
[14:02] Alright and then the last thing that I did is in the static mesh spawner here, I went through all of the mesh entities and instead of the grass ones, I replaced them with my dry grass assets.
[14:17] So there's my dry grass asset.
[14:19] And then also I want to make sure to kind of scroll down this long list of parameters and check any of the ones that apply to this particular asset.
[14:31] So you can see I have nine different thatching grass assets here that I've put in or dry grass instead of my lush grass asset.
[14:45] Alright let's go ahead and take a look at our landscape and see what this does.
[14:50] Okay so we've got our mannequin character and we can just kind of run around our landscape.
[14:54] And here we're kind of at a lower altitude but we're almost at the point where we're going to start blending from our lush grass to our dry grass.
[15:04] In fact there's a dry grass patch right in front of my character there.
[15:09] So we're starting this kind of subtle slow blend and as my character runs further and further uphill, now you can see we're getting to the point where we've crossed the threshold and now we see mostly that the
[15:24] dry grass and much less of our lush grass.
[15:29] And it's those masks that we created in the landscape material that's allowing us to kind of smoothly transition between, I guess you could call them biomes.
[15:40] And this is kind of like our dry rocky highland grass area.
[15:44] And then as we come further down in altitude we can slowly blend from that to our more lush grass that we see down here in this area.
[16:00] Okay that's pretty cool.
[16:02] Well let's go ahead and take a look at the PCG graph that I created to spawn our pebbles and our rocks.
[16:10] Ah one thing that I forgot to mention we took a look at our PCG dry grass graph here.
[16:18] But in order for this to work we need to add that graph to our landscape.
[16:23] So I went ahead and grabbed our PCG dry grass graph and dragged and dropped it on the landscape.
[16:31] And there it is PCG dry grass.
[16:33] And for the location I went ahead and centered it on my landscape and I scaled it to 140, 140, 60 which is the right size to encompass my entire landscape.
[16:47] And then if we scroll down here I've also set is partitioned to true so that the grass is divided into little chunks
[17:00] and we can spawn and despawn them around the player character as we run around.
[17:06] And then it's also set, I set generation trigger to generate at runtime instead of generate on load or on demand.
[17:16] So this is what helps the PCG grass kind of slowly load in and out as we move around our landscape.
[17:27] Alright and then I also tuned the parameters here.
[17:32] I've changed the parameters so that it works well with our dry grass asset 0.7 and 0.1 or 1.2 for min and max scale.
[17:43] And then on spatial noise I removed so I just set its strength to zero and then density min and max to 0.7 and 1.5.
[17:51] So those are the parameters that are being passed into my dry grass compute shader which will then place the points.
[18:01] Okay let's go ahead and take a look at the graph that I made for the stones or the pebbles.
[18:07] So this one is pretty similar I just duplicated the grass asset.
[18:11] But on this one I changed my grid size here from 1600 to 800 and the reason that I did that is because my pebbles are smaller assets.
[18:23] And I want to deal with them in smaller chunks on the landscape.
[18:27] So I've set the grid to be 800 instead of 1600.
[18:31] And then for the point generator I changed the number of elements to 2500.
[18:38] I don't need quite as many of these as I need clumps of grass.
[18:42] And then I also on the generate landscape textures you need to make sure that you set this to match the landscape grass type asset.
[18:53] Here I've set it to PCG stones, LGT PCG stones so that it's passing in that mask that you created in your landscape material.
[19:05] So then we pass that into the point generator and just like with PCG dry grass here in point generator I also removed the spatial noise from my stones.
[19:21] Because they're already getting enough noise from the landscape grass mask.
[19:29] And I did do one additional thing in the HLSL code here and that is let me see if I can find a good example of this.
[19:38] I'm just going to kind of zoom in on some stones on my landscape here.
[19:44] Yeah here you can see these stones here.
[19:48] I wanted the stones to kind of sit down in the landscape instead of sitting on top of it.
[19:55] And so the way that I did that is I found the spot in the code here where it's setting the height of the points to match the landscape.
[20:04] And that's right here position dot Z that's the up and down axis is equal to the height of the landscape.
[20:13] And what I did is I just added a minus 1.5 here which subtracts one and a half centimeters from the height.
[20:23] So let's take a look really quick. I'm just going to remove this save it and force it to regenerate.
[20:29] If we switch back now you can see the stones are kind of sitting up on top of the landscape.
[20:35] But I wanted them to kind of sink down into the landscape instead.
[20:38] And so if I just come in here let's do minus 3 just so you can see what this is doing.
[20:51] So if we look here you can see that the stones are offset so they're sunk into the landscape just a little bit.
[20:58] And that allows them to look like they're part of the landscape rather than being placed on top of the landscape.
[21:08] But I like a value of 1.5 because it makes it so they don't sink in too much.
[21:15] So I'm just going to save that regenerate.
[21:18] Now we can see we've got our stones kind of sunk into the landscape just a little bit but not too much.
[21:25] All right so then we add our PCG Pebbles graph to the landscape.
[21:30] And just like with the dry grass version I centered at the origin and set it to a height of 1920
[21:38] and kind of encapsulate my terrain.
[21:41] I scaled it to 140, 140, 60 so that it fits around the entire terrain.
[21:47] You know you might have to make these values different depending on the size of your terrain.
[21:52] And then I came down here and checked is partitioned and generate at runtime.
[21:58] And then I set the parameter overrides so that our stones are the right size.
[22:04] I made these a little bit smaller 0.3 and 0.7.
[22:07] What I wanted to do was kind of match the size of the stones that are in the material here.
[22:17] You know obviously we could do some more tweaking but I wanted these to kind of feel like they're part of the terrain
[22:25] and that they're a partner to the textures that I've got applied to the landscape.
[22:30] All right so I've created three PCG graphs, dry grass and pebbles.
[22:37] And I'm determining where each of these three gets applied based on these masks that I've generated in my material.
[22:47] And then I feed these masks into each of the three PCG graphs.
[22:53] And then I apply those PCG graphs to my landscape and they determine at runtime dynamically generated
[23:02] where the various features of the detail meshes are going to be applied to the landscape.
[23:11] And I think this is just a really fantastic system.
[23:15] I can get all kinds of detail meshes that mask the textures that I'm applying to the landscape
[23:27] and have my detail meshes kind of support what my underlying landscape is doing.
[23:34] And it's all running really efficiently because PCG is calculating the positions of these points in a compute shader at runtime
[23:44] on the fly on the GPU and it's removing the points that are behind the player
[23:50] and also the points that are kind of off into the distance that aren't close enough for the player to see.
[23:57] So I'm only getting the landscape detail meshes that I need and it's working really nicely.
[24:05] All right so that concludes this tutorial.
[24:09] I think maybe what I'm going to do next week is we'll get away from this kind of GPU generated portion of the tutorial
[24:20] into more of the CPU PCG system where we're placing like much larger boulders and maybe add some trees to our landscape
[24:32] and we'll be doing that using PCG but the CPU version of it.
[24:36] So I hope you come back for that one. Hope you enjoyed this one and that it was useful for you.
[24:42] I look forward to seeing you in the next video and in the meantime have a great week.



---

## Captured Frames

- [1:12] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_000.jpg
- [2:23] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_001.jpg
- [4:29] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_002.jpg
- [5:39] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_003.jpg
- [6:26] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_004.jpg
- [8:00] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_005.jpg
- [8:37] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_006.jpg
- [9:17] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_007.jpg
- [11:19] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_008.jpg
- [12:26] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_009.jpg
- [14:02] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_010.jpg
- [15:04] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_011.jpg
- [18:07] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_012.jpg
- [19:44] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_013.jpg
- [21:05] tutorials/frames/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-/frame_014.jpg

---

## Structured Notes

### Core Technique
Extending the single-mask PCG grass workflow (Episode 3) to **multiple, mutually-exclusive detail-mesh types per landscape "biome"**: splitting one combined grass mask into per-type sub-masks (lush grass / dry grass / stones) in the Landscape Material, feeding each into its own duplicated PCG graph + Landscape Grass Type asset, and tuning each graph's parameters and HLSL independently so the detail meshes visually "partner" with whatever landscape texture they sit on.

### Summary
Builds directly on Episodes 2–3's single grass mask by dividing the landscape into altitude-based "biomes" — lush/mossy grass at low altitude, dry/rocky grass at high altitude — and pairing each with its own hand-picked detail meshes: 3 lush grass meshes (from earlier episodes), a set of "thatching grass" + "grass clumps" for the dry area, and a pebble/stone mesh set placed specifically where the dry-grass texture shows exposed rocks. In the Landscape Material, one base grass mask (terrain-angle × inverse-snow × inverse-puddle, from Ep.3) is intersected with a new **dry grass mask** (and its inverse for lush grass) and with a **Levels-adjustment-derived rocks mask** (crushing the dry grass texture's own albedo/roughness into a black/white "where are the visible pebbles" mask) to get a clean dry-grass-without-rocks mask and a separate stones mask. Three separate `Landscape Grass Type` assets (`LGT_PCGGrass`, `LGT_PCGDryGrass`, `LGT_PCGStones`) carry these three masks out to three duplicated PCG graphs (PCG Grass, PCG Dry Grass, PCG Pebbles), each independently tuned: different point counts (3,500 grass / 10,000 dry grass, since the meshes are smaller / 2,500 stones), different grid/tile sizes (1600 for grass and dry grass, 800 for the smaller stones), spatial noise removed from the dry-grass and stones graphs (redundant since the landscape mask itself already provides the breakup), and — for stones specifically — a small HLSL tweak subtracting a constant (author settles on **-1.5**) from each point's Z position so stones visually sink slightly into the terrain instead of floating on top of it. Ends with a teaser for next week: switching from this GPU/runtime PCG approach to CPU/static PCG for large boulders and trees.

### Key Steps
1. **Design the mesh-to-material pairing first** (not a PCG step, but the prerequisite decision): match detail mesh sets to the landscape textures they'll sit on — lush grass clumps for the low-altitude mossy texture, thatching grass + pebbly rocks for the high-altitude dry/rocky texture — because the visual goal is meshes and materials "supporting each other."
2. **Split the existing combined grass mask (Ep.3) into a dry-grass sub-mask:** in the Landscape Material, build a new mask from whatever drives the material's own lush/dry texture blend (e.g. an altitude-based blend factor); preview by wiring directly to Base Color.
3. **Derive the lush-grass mask** as the base grass mask (terrain-angle × inverse-snow × inverse-puddle) multiplied by **One Minus** the dry-grass mask — i.e. base mask minus wherever dry grass appears.
4. **Derive the dry-grass mask** as the base grass mask multiplied directly by the (rounded) dry-grass mask.
5. **Build a rocks/stones mask from the dry-grass texture's own detail:** feed the dry grass texture into a **Levels adjustment** node (same concept as Photoshop levels) tuned so it outputs white wherever the texture shows visible rock/pebble detail and black elsewhere.
6. **Clean the dry-grass mask of rocks:** take **One Minus** the rocks mask, multiply it by the dry-grass mask — result is white where dry grass (but not exposed rock) should spawn.
7. **Wire the stones mask directly** from the Levels-adjustment output into the Landscape Grass node's stones input (no further combination needed).
8. **Create three separate `Landscape Grass Type` assets** — one per detail-mesh category (author: `LGT_PCGGrass`, `LGT_PCGDryGrass`, `LGT_PCGStones`, made by duplicating the original asset from Ep.3) — and on the material's `Landscape Grass Output` node, add **one array element per asset**, each with its matching mask wired in and its Grass Type slot set to the corresponding asset.
9. **Duplicate the PCG graph once per detail-mesh category** (PCG Grass already existed; author adds **PCG Dry Grass** and **PCG Pebbles** as copies), then per graph:
   - Point Generator: set an appropriate point count (3,500 grass / 10,000 dry grass — smaller meshes need more points to fill the same area / 2,500 stones — fewer, larger objects).
   - `Generate Landscape Textures` node's Select Grass Types entry: point it at the matching `LGT_PCG*` asset name for that graph, so the correct mask flows in.
   - Point Generator's HLSL: update the grass-mask sampling code's asset-name reference to match this graph's Landscape Grass Type (must exactly match the Select Grass Types entry, per the naming rule established in Ep.3).
   - Remove the spatial-noise HLSL block (the density-reducing noise term and its `density -= spatialNoise` line) from the dry-grass and stones graphs specifically, since the landscape-material mask itself already provides organic breakup — this saves a compute-shader calculation per point.
   - `Change Grid Size`: smaller assets (stones) use a smaller tile size (800 vs. the default 1600) to manage them in finer-grained chunks.
   - `Static Mesh Spawner`: swap in the category-appropriate mesh set (e.g. 9 different thatching-grass mesh entries for dry grass) and re-check any per-mesh settings from Ep.2 (shadows, WPO falloff, etc.) that need to apply to the new assets.
   - Parameter Overrides: retune Point Scale Min/Max and density-noise ranges per asset type (e.g. dry grass 0.7–1.2 scale; stones smaller, 0.3–0.7 scale, spatial noise strength set to 0 since it was removed from the shader).
10. **Sink stones into the terrain (stones graph only):** in the HLSL, find where a point's `position.z` is set to the landscape height, and subtract a small constant offset (author tests -1.5 and -3.0, settles on **-1.5 cm**) so stone meshes partially embed in the ground instead of floating on the surface — save and **Force Regen** to preview.
11. **Add each PCG graph to the landscape as a separate actor:** drag-drop each graph onto the level, center at the origin, scale to cover the whole terrain (author uses 140×140×60 for all three), and set **Is Partitioned** = true and **Generation Trigger** = **Generate at Runtime** on each (same runtime-streaming setup as Ep.2/3, repeated per graph instance).
12. **Verify in Play mode:** running across the terrain shows a smooth altitude-based blend from lush grass → dry grass/pebbles, driven entirely by the landscape-material masks feeding three independently-tuned runtime-GPU PCG graphs.

### UE Systems / Blueprints / Settings
- **Assets:** three `Landscape Grass Type` assets (`LGT_PCGGrass`, `LGT_PCGDryGrass`, `LGT_PCGStones`), three PCG graphs (PCG Grass, PCG Dry Grass, PCG Pebbles) as duplicates of the Ep.2/3 graph.
- **Landscape Material nodes:** existing `TerrainAngleMask`/snow/puddle mask chain (Ep.3) as the base grass mask; new **Levels** adjustment node (rocks-from-texture mask); `One Minus` and `Multiply` chains to derive lush/dry/stones sub-masks; `Landscape Grass Output` node extended to 3 array elements, each bound to its own Grass Type asset and mask.
- **Per-graph PCG settings varied:** Point Generator point count (3,500 / 10,000 / 2,500), `Change Grid Size` tile size (1600 / 1600 / 800), `Generate Landscape Textures` → Select Grass Types entry (must match each graph's Landscape Grass Type name), Point Generator HLSL (grass-mask asset-name reference per graph; spatial-noise block removed for dry grass and stones; stones-only Z-position offset of -1.5 for ground-sinking), Static Mesh Spawner mesh entries (category-specific meshes), Parameter Overrides (Point Scale Min/Max, spatial noise strength/density min-max, tuned per asset type).
- **Per-graph-instance level settings** (repeated for each of the 3 graph actors placed on the landscape): Scale (140×140×60), `Is Partitioned` = true, `Generation Trigger` = Generate at Runtime.

### Difficulty
Advanced — builds directly on the HLSL-editing and landscape-material-masking techniques from Episodes 2–3, adding the complexity of managing three parallel, independently-tuned graph/mask/asset triads that must stay name-consistent with each other.

### UE Version
Not explicitly stated; direct continuation of the UE 5.7-era runtime GPU PCG grass system from Episodes 2–3.

### Tags
pcg, materials, landscape, hlsl, blueprint, pipeline, advanced, ue5-7

---

## Related Entries
- `tutorials/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo.md` — Episode 3, establishes the single-mask HLSL-editing technique (Landscape Grass Type asset, Generate Landscape Textures node, Grass Mask input pin, HLSL point-culling) that this episode extends to three parallel masks; shares tags: pcg, materials, landscape, hlsl, advanced, ue5-7.
- `tutorials/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2.md` — Episode 2, the base runtime-GPU grass graph (Is Partitioned, Generate at Runtime, tile/cull-distance tuning) that all three graphs in this episode are duplicated from.
- Next episode in this series moves from GPU/runtime PCG to CPU/static PCG for large boulders and trees, per this video's own end-teaser — look for a title matching that CPU-focused follow-up (likely "How To Grow A Forest in Unreal With PCG").
