---
title: Using Landscape Grass Masks With PCG - Procedural Content Generation (PCG) - Episode 3
source: YouTube
url: https://www.youtube.com/watch?v=PNXIGplTsgU
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, materials, landscape, hlsl, blueprint, pipeline, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Using Landscape Grass Masks With PCG - Procedural Content Generation (PCG) - Episode 3

**Source:** [YouTube](https://www.youtube.com/watch?v=PNXIGplTsgU)
**Author:** Ben Cloward
**Duration:** 28m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'll show you how to use a Landscape Grass Mask in Unreal
[0:05] to control the placement of your PCG Grass.
[0:09] Let's go!
[0:10] [♪ Music playing, in the background.
[0:16] Alright, so in last week's video, I showed you how to use Unreal's PCG
[0:22] to create an efficient Grass System.
[0:26] And this is the Grass System that we made.
[0:28] You can see that it's placing Grass on our Landscape,
[0:33] and it's kind of fading it out at a distance to save on performance.
[0:37] And as we move along the ground, you can see that it's slowly fading in additional Grass,
[0:44] kind of here on the horizon or at the boundary we've set.
[0:49] And I showed you three different ways of controlling the density of the Grass
[0:54] and how far away it draws so that you can get a good balance between visuals and performance.
[1:00] But one of the things that I pointed out is that this system is just spawning Grass everywhere on our Landscape.
[1:07] So here on this dirt hillside, we've got Grass there.
[1:12] And we've even got Grass, if we come over here to our slope,
[1:16] we've got Grass growing up this steep slope,
[1:19] and we've even got the system placing the Grass in the areas where we have snow.
[1:26] And we don't want Grass there.
[1:28] So today, I'm going to show you how to use a Grass Mask from your Landscape
[1:35] to remove Grass in areas where you don't want it.
[1:38] So basically, you're using your Landscape material to control the Grass placement.
[1:46] So let's go ahead and jump in and get started.
[1:48] The first thing that we need to do is to create a Landscape Grass type.
[1:53] So I'm going to open my content drawer here and here in my PCG folder,
[1:58] I'm just going to right click and we'll search for Grass.
[2:04] And it's going to bring up Landscape Grass type.
[2:06] So I'm going to create one of these and the name of this asset is really important.
[2:12] You can name it whatever you want, but the name that I'm using here
[2:16] is a name that I'm going to have to plug in somewhere else in just a minute
[2:19] and I'll show you that.
[2:21] So I'm going to call mine LGT for Landscape Grass type.
[2:26] Then I'm going to call it PCG Grass.
[2:31] And this is case sensitive.
[2:33] So I'm calling it LGT PCG Grass.
[2:37] And that's a name that we're going to have to reference in a minute, like I said.
[2:41] So be sure that you remember that.
[2:45] And normally with the previous Landscape System, I would have to open up this asset
[2:52] and specify right here all of the grass varieties that I wanted.
[2:57] So I would add array elements here and then I would put in all of their parameters
[3:05] and that would control the behavior of the grass.
[3:07] But with PCG, I'm not using this to spawn my Landscape Grass.
[3:13] I'm just using it to hold the mask from my Landscape Material
[3:18] that I'll pass to PCG in just a minute.
[3:22] I do need a Landscape Grass asset, but I don't actually need to populate it
[3:27] with grass varieties like you see here.
[3:30] So I'm going to go ahead and save that asset.
[3:32] And what we'll do next is switch over to our Landscape Material.
[3:38] So this is the material that we created in the previous series of videos.
[3:43] And this series is not really focused on Landscape Materials.
[3:47] So I'm not going to go into a whole lot of depth here on explaining what's happening.
[3:51] But let me just give you a quick overview.
[3:53] This portion of our graph is creating our grass.
[3:59] And we actually have two different varieties of grass.
[4:02] This grass here appears at low altitudes.
[4:06] And then this grass here is a little bit more rocky and it appears it kind of slowly blends
[4:11] from the low altitude mossy grass to the high altitude rocky grass
[4:18] based on our altitude mask that we created there.
[4:21] And then up here, we have our material that appears on slopes.
[4:25] At high altitudes, we have rocky slope material.
[4:30] And then at low altitudes, we have this dirt.
[4:33] And again, we're blending between these two materials based on our altitude mask.
[4:38] Then we blend between our flat ground assets and our slope assets
[4:45] based on our terrain angle mask node here.
[4:49] And then to kind of top it all off, we're adding snow on the top.
[4:54] And then we pass out our material attributes to our root node.
[5:00] I also forgot to mention here.
[5:02] We also are creating the puddles in our terrain that you can see.
[5:07] We just kind of zoom in here.
[5:09] You can see that we've got these nice puddles.
[5:13] But our problem is that currently we have grass growing on our slopes.
[5:17] We have grass growing on our snow and we have grass growing in our puddles.
[5:22] So what we want to do is create a mask in our material that will remove the grass from those areas.
[5:31] So the first thing that I'm going to do is right click in here and type grass.
[5:36] And I want to add a landscape grass output node.
[5:40] And this is going to be kind of like our root node over here
[5:44] where we get to output our material parameters.
[5:47] But in this case, instead of material parameters, I'm actually outputting our grass mask.
[5:53] So I'll select that node and come over here to grass type.
[5:57] And here I need to drop this down and select LGT PCG grass, that grass type that we just created.
[6:05] So I'll pop that in there and now we're ready to actually create our mask.
[6:11] So we don't want, first of all, we don't want grass growing on slopes.
[6:16] And we've already created a slope mask to blend between our slope material here
[6:25] and our grass material here.
[6:28] And that mask is right here.
[6:29] We have our terrain angle mask and that's going to be blending between our material that is on slopes
[6:39] and our material that's on flat.
[6:41] So this is the mask output right here.
[6:44] Let's go ahead and wire that mask output into our base color
[6:52] so that we can take a look at what this looks like.
[6:54] So I'm just going to connect this up to our base pin here, our base input port.
[7:00] And we'll hit save and switch over to our landscape here.
[7:04] And this is going to show us, oh, you know what?
[7:05] I'm going to switch from lit to unlit just so we can see what this mask looks like.
[7:13] All right.
[7:13] So you can see that the mask is white here on our flat ground,
[7:18] although there is a little bit of noise in here.
[7:22] And then on our slopes, this mask is black.
[7:26] But this mask is incredibly detailed.
[7:30] You can see that there's like all kinds of per pixel detail in here.
[7:36] And when we're placing grass, the grass is kind of placed in these big clumps
[7:41] and we don't need a mask that has quite this much per pixel detail between black and white.
[7:49] And the thing that's happening, the thing that's causing that detail,
[7:54] if we come back over here to our terrain angle mask is this pixel normal input.
[8:02] You can see that I'm blending between the flat areas and the slope areas,
[8:08] but we're using this normal input from the two materials for the blending.
[8:15] And so I'm getting per pixel normal details in our mask.
[8:19] Where really I just need a mask that's a little bit more simple.
[8:23] And so what I'm going to do is I'm going to take this terrain angle mask node and copy it.
[8:31] And I'm going to paste it down here where we're building our grass mask.
[8:37] And let me just add a couple of control parameters here.
[8:40] The first thing that I'm going to do is add a value of zero for my pixel normal,
[8:46] which means we're not doing per pixel details.
[8:49] We're using our vertex normals instead of our pixel normals.
[8:56] And the other parameter that I need to add is for the center of the mask.
[9:01] That's kind of the spot where on the slope our mask changes from black to white.
[9:08] And I'm going to place my center at negative 0.4 and then wire that into mask center.
[9:16] Okay, let's go ahead and wire this into our base color here and save it and take a look at our terrain.
[9:24] So that we can see what this mask looks like.
[9:27] Okay, now you can see that all of that per pixel detail is gone.
[9:33] And I've got a much more simple mask that just kind of slowly fades from here's our flat area.
[9:40] And then here is our sloped area.
[9:43] And we don't have all of that visual noise that we had before.
[9:48] That visual noise was really cool for creating the landscape's appearance.
[9:53] But for the placement of our grass, we need something that's significantly more simple.
[10:00] Okay, so let's switch back to our material.
[10:03] And the next thing that we want to do is make sure that we're not getting any grass where there's snow.
[10:10] So our snow mask, let's see if we can find yet.
[10:14] Here's our snow material and we're generating our snow mask right here.
[10:19] So what I'm going to do is take the mask that we already generated for snow.
[10:24] And this mask is white where we should apply snow and black where the snow should not go.
[10:29] But I actually want the inverse of that.
[10:32] So I'm going to add a one minus node.
[10:35] So now this mask is going to be black where the snow is.
[10:40] And so I'm going to multiply our the grass mask that we're creating here by the inverse of our snow mask.
[10:51] And that's going to remove our snow.
[10:54] And then the next thing that we want to remove is our puddles.
[10:58] And our puddles mask is the same way.
[11:00] It's white where the puddles are and black where they're not.
[11:04] And so I need to invert this one with a one minus.
[11:09] And then we need to multiply by the inverse of our puddle mask.
[11:16] So I'm going to add another multiply here and wire this out.
[11:20] Okay, so we've got our initial angle mask and then we multiply by the inverse of our snow mask
[11:27] and multiply by the inverse of our puddle mask.
[11:32] And I think that may be all we need.
[11:34] Let's take a look.
[11:35] I'm going to wire this into our base color and we'll hit save and check out what this looks like.
[11:43] Okay, so here is the white area where our grass is going to spawn.
[11:47] And you can see the black areas where our puddles are.
[11:52] And then also it's going to be black up here on our slopes where we've got our snow coming in.
[11:59] So it looks like this mask is going to work for our grass placement.
[12:04] So let's go ahead and wire this mask into our landscape grass node.
[12:09] And that's going to output this mask that we've generated here into our LCG, PCG grass asset.
[12:19] And we also need to reconnect our base color here again so that our landscape goes back to the way that it used to be.
[12:28] Okay, so that's all that we needed to do in our landscape material.
[12:32] We're just creating our mask and telling it we don't want grass on slopes.
[12:38] We don't want grass where there's snow and we don't want grass where there's puddles.
[12:44] All right, I think we're ready to switch over to work on our actual PCG graph.
[12:53] Oh, you know what?
[12:54] There's one thing that I forgot.
[12:57] When you're using a PCG or when you're using a LGT PCG grass type like this and you're generating a mask in your landscape material and passing it in,
[13:12] there is a command line parameter that we need to enter.
[13:16] So I'm going to come down here to my console and I'm just going to type grass.
[13:22] And the one that we want to use is right here.
[13:24] It says grass dot grass map dot always build runtime generation resources.
[13:31] So I'm going to pick that command line parameter and hit one.
[13:36] And what this parameter is going to do is it's going to make sure that this grass map that we're creating this mask always generates when it needs to.
[13:47] So I'm going to enter that parameter and I'll paste that parameter down in the description just in case you need to reference it.
[13:55] But that's going to ensure that our grass will always generate when we need it.
[14:00] OK, now we're going to switch over to the PCG graph that we created in last week's tutorial and add the things here that we need in order to hook up that mask that we just created in our landscape material
[14:14] so that it controls where our points are spawning.
[14:18] So here we are in our PCG graph.
[14:21] We get our landscape data.
[14:23] We alter the size of the grid on the data and then we generate points using that grid and our input parameters.
[14:32] And then finally at the end, we spawn our grass meshes on the points that we generated.
[14:39] So the first thing that we need to do is bring in some additional landscape data.
[14:45] And so what I'm going to do is create a grass maps node.
[14:51] So here's our node called generate grass maps and that's going to bring in the grass maps that we need from the landscape.
[15:00] So I'm going to connect this with our change grid size here.
[15:05] And then there are a couple of settings that we need to set over here.
[15:09] So it says select grass types and we're going to add an array element here.
[15:14] And the grass type that we want to add is our LGT PCG grass type there.
[15:22] So this is where we need to type this name in and get it correctly case sensitive LGT underscore.
[15:33] PCG grass.
[15:36] All right, so that's going to bring in the type from our PCG grass type that we just created.
[15:43] And we need to uncheck exclude selected grass types.
[15:51] OK, so this is going to bring in our grass type correctly.
[15:56] And then the next thing that we need to do is pass that data, the grass map that we just defined in our material.
[16:04] We need to pass that grass type data into our point generator.
[16:09] So I'm going to pick our point generator node here and we're going to come over here to our details panel in our input pins.
[16:16] And we need to add one additional input pin.
[16:19] Right now we have landscape and we have grass params.
[16:24] But we need to add another one here.
[16:26] And so I'm going to hit the plus here and add another array element.
[16:30] And we're going to call this array element.
[16:33] Grass mask.
[16:36] And again, this name is really important because we're going to reference it in the point generator code.
[16:42] And we need to set the type of this to not points.
[16:47] We're going to set it to base texture 2D.
[16:51] And that's because the grass map that we're passing in is a texture.
[16:56] It's a texture that we generated in our landscape material.
[17:00] OK, so now we can go here to our generate landscape textures node and connected up with our grass mask input.
[17:11] So now we've passed the the grass map into our point generator.
[17:17] And now we need to alter the code that our point generator node is using in order to reference that data.
[17:27] So I'm going to open up.
[17:28] I'm going to hit this button here called open HLSL editor.
[17:33] And what this is going to allow us to do is it's going to open this code editor here that allows us to see what's happening in the compute shader that our point generator node is using.
[17:47] So here's our point generator node and internally this node is executing all of this code on the GPU to generate the points where our grass is going to be spawned.
[18:00] So let's go over this code really quickly.
[18:03] Obviously in this short video, I don't have enough time to teach you HLSL code.
[18:09] But what I want to do is give you kind of a rough understanding of what this code is doing.
[18:16] The first thing that it does is generate our grid of points right here.
[18:21] And then it applies an initial filter to remove some of those points that we don't need based on the density parameter that we passed in.
[18:33] Next, it's going to use some randomness to generate offsets for those points.
[18:39] And then it's going to offset the point, the position of those points so that the points are no longer arranged in a regular grid.
[18:48] It kind of messes up the arrangement of the points so that they're a little bit more organic looking.
[18:55] And then the next thing that it does is apply some random rotation and random scale to the points.
[19:04] And then it applies spatial noise and does a final step where we're removing additional points based on our density.
[19:12] And then we're writing out the final point data.
[19:16] So we need to alter this code in order to take advantage of the map that we created in our material.
[19:24] And here we have our maximum number of points.
[19:30] And then here we remove some points and then do a bunch of calculations on the points.
[19:35] And then we remove some more points here at the end and then output the final data.
[19:40] So it's going to be most advantageous to insert the point, to insert the mask for our grass as far up here toward the top of the code as we can.
[19:55] Because if we were to place our grass mask down here at the bottom, we would be performing all of these calculations on those points
[20:05] and then just throwing away the ones that we wanted to get rid of.
[20:09] So the higher up here in our code that we can add this point culling information, the less work our compute shader is going to have to do.
[20:20] Because we're going to be getting rid of points before the additional work.
[20:26] So the earliest place where we can do this is right here where our points have been placed in their final locations.
[20:35] So after we randomly offset our points, but before we do random rotation and random scale,
[20:43] this is where we can actually apply our mask to get rid of the points that are in puddles on slopes and on snow.
[20:57] So how do we do this exactly?
[21:00] Well, there's a couple of places in this code already where we can see that it's removing points for us.
[21:06] The first one is right here and it says like if the density is greater than the density filter, then remove the point.
[21:14] So we're just going to grab this and copy and paste it.
[21:19] I'm going to put it right here and I'll just add a comment here called, let's see, we're just going to call this our grass mask.
[21:28] And we want to remove points.
[21:33] But we don't want to do it with the density filter.
[21:36] So I'm going to get rid of this part here and we're going to do it instead with our grass mask.
[21:43] So I'm just going to copy and paste this code that I've already written and don't worry.
[21:48] It's just a single line.
[21:52] So I'll paste this in here.
[21:54] So I'm saying if our grass mask sample position that we got from the LGT PCG grass, grass map type, and we're passing in the position of the point to get that mask.
[22:12] If the mask value is less than 0.9, then we're going to remove the point.
[22:18] And I will paste this.
[22:21] I will add this code, this entire snippet that we need to insert.
[22:27] I will put the whole code down in the description so you can just copy and paste this whole thing as it is.
[22:33] Now, the couple of really important parts to get right are this term right here, grass mask needs to match this input here.
[22:46] Grass mask that we added for input for a third input pin.
[22:52] So this grass mask word here needs to match this grass mask word here.
[22:59] And this LGT PCG grass term in the code needs to match the name of the landscape grass type asset that we created at the beginning of the tutorial.
[23:12] So those two elements need to match names, the grass mask and the LGT PCG grass.
[23:20] Now you can call those names whatever you want, as long as the term that you've written here matches your LGT grass type that you created.
[23:30] And as long as the term that you created here matches the name of your input port that you created right there.
[23:40] Alright, so let's go ahead and save this.
[23:44] And we're going to hit this force regen button to regenerate our grass.
[23:50] And now we should be able to switch over to our terrain and take a look at the grass, which is now being filtered by the grass mask in our landscape material.
[24:05] So you can see now we don't have any grass in our puddles and we don't have any grass on our slopes and we don't have any grass in areas where we've got snow.
[24:21] So we're using that mask that we created in our landscape material to control the placement of our grass.
[24:31] And I don't know about you guys, but I think this is super cool.
[24:34] There's some huge potential here for all kinds of things that we could do with PCG.
[24:40] Because basically what this means is that any kind of mask that we can create in our landscape material, whether that be like the height of our landscape or where we've painted landscape materials or based on angles or based on other things that we calculate like the puddle placement.
[25:01] Anything that we can do in our landscape material can contribute to the mask, which then determines where our PCG assets are placed.
[25:13] Let's go ahead and hit play here and we'll just kind of run around our environment and take a look at our results.
[25:21] You can see that here on our slope, there's no grass and there's no grass in our puddles and there's no grass on our cliffs.
[25:35] We're just getting the grass placed exactly where we want it based on that mask that we created in our material.
[25:43] And this is really powerful, especially for me because personally I have a lot more experience with Unreal's material editor than I do with PCG.
[25:54] I'm just learning PCG myself, but with the material editor, I'm pretty experienced.
[25:59] So I can use the material editor to create all kinds of fancy masks, but I'm not so good at creating those kinds of things in a PCG graph itself.
[26:08] And so what this means is that I can do a lot of work in the material to control where I want to place PCG items.
[26:17] And I don't have to worry about figuring out how to do those things in PCG.
[26:22] Now, don't worry later on in the series of videos, I am going to show you how to do those kinds of things in the PCG graph as I myself learn how to do them.
[26:35] But for now, what this gives us is a lot of control over where PCG is placed.
[26:44] Now, there is one thing that you might be wondering and that is, so I've placed the grass.
[26:51] What if I want to put rocks on my slope or clumps of snow on my snow cliffs?
[27:02] You know, right now I've just got one landscape mask and one type of material that I'm placing with the mask.
[27:11] I'm just placing grass.
[27:13] But what if I have a landscape with a bunch of different biomes and in some places like, let's say I have a forest and I want to put like dead sticks and leaves and rocks under the tree foresty part of the landscape.
[27:29] And I want to put grass in another part of the landscape.
[27:32] In other words, to say this in a more simple way, what if I want to use more than one grass mask to place more than one type of landscape material?
[27:44] How do I do that?
[27:46] Well, that's going to be the subject of next week's video.
[27:51] So be sure to come back next week and I'll show you how to use multiple grass masks coming out of your landscape material to control the placement of multiple types of not just grass, but other types of PCG placed meshes that you can add to your landscape.
[28:14] So be sure to come back for that one.
[28:17] That one's going to be great.
[28:18] Hope you enjoyed today's video and that you learned how to easily control the placement of PCG meshes based on the grass mask coming out of your landscape material.
[28:33] All right, that'll do it for this week.
[28:35] Have a great week, everybody, and we'll see you in the next one.



---

## Captured Frames

- [2:06] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_000.jpg
- [3:53] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_001.jpg
- [6:05] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_002.jpg
- [7:13] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_003.jpg
- [9:24] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_004.jpg
- [11:16] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_005.jpg
- [11:52] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_006.jpg
- [15:00] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_007.jpg
- [16:24] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_008.jpg
- [17:33] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_009.jpg
- [22:12] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_010.jpg
- [24:05] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_011.jpg
- [25:21] tutorials/frames/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo/frame_012.jpg

---

## Structured Notes

### Core Technique
Piping a mask generated inside a **Landscape Material** graph (via a `Landscape Grass Output` node + a `Landscape Grass Type` asset) into a runtime-GPU PCG grass graph's **HLSL point-generator compute shader**, so PCG-spawned grass is culled anywhere the landscape material says it shouldn't be (slopes, snow, puddles) — without touching the PCG graph's node layout, only its underlying shader code.

### Summary
Direct continuation of Episode 2's runtime GPU grass system, which was fixed to spawn everywhere (including steep slopes, snow-covered peaks, and puddles — clearly wrong). This episode fixes that by building a landscape-material-driven mask and threading it through into the point generator's HLSL code. Steps: create a `Landscape Grass Type` asset purely as a named "mask carrier" (not populated with actual grass varieties, since PCG — not the legacy landscape grass system — is doing the spawning); in the Landscape Material, add a `Landscape Grass Output` node bound to that asset and build a mask by combining a simplified (vertex-normal-based, not per-pixel) terrain-angle mask with the inverse of the existing snow mask and the inverse of the existing puddle mask; enable the `grass.GrassMap.AlwaysBuildRuntimeGenerationResources 1` console variable so the grass map reliably regenerates; then, in the PCG graph, add a `Generate Landscape Textures` node to pull that named grass-type's texture data in, add a new `Grass Mask` (Base Texture2D type) input pin on the Point Generator node, and hand-edit the node's HLSL source (via "Open HLSL Editor") to sample the mask texture at each point's position and discard points below a threshold (0.9) — inserted as early as possible in the shader (right after point positions are finalized, before rotation/scale randomization) to avoid wasting GPU work computing attributes for points that will be thrown away. Result: grass now respects the landscape material's own logic for slope/snow/puddle placement, and — as the author notes — *any* mask buildable in the Landscape Material (height, painted layers, angle, custom logic) can now drive PCG placement this same way.

### Key Steps
1. **Create a mask-carrier asset:** Content Drawer → right-click → search "grass" → **Landscape Grass Type**. Name it something exact and memorable (author uses `LGT_PCGGrass`) — this name must match, character-for-character (case-sensitive), a term referenced later in both the landscape material and the HLSL code. Leave its grass-variety array empty — PCG does the actual spawning, this asset just carries the mask.
2. **In the Landscape Material graph:** add a `Landscape Grass Output` node (functions like a second "root" node, alongside the main material output) → set its **Grass Type** dropdown to the `LGT_PCGGrass` asset just created.
3. **Build a simplified slope mask:** the material already has a `TerrainAngleMask` node driving the existing flat/slope material blend, but it uses **per-pixel normals**, producing far more fine-grained noise than grass placement needs. Copy that node, paste a second instance for the grass mask, and set its **Pixel Normal** input to a constant **0** (forcing vertex-normal-based blending instead of per-pixel) and its **Mask Center** to a tuned constant (author uses **-0.4**) to control where on the slope the mask transitions from white (flat) to black (steep).
4. **Remove snow and puddle areas:** take the existing snow mask (white = snow) and puddle mask (white = puddle), invert each with a **One Minus** node, then **Multiply** the simplified slope mask by the inverted snow mask and by the inverted puddle mask in sequence — final result is white where grass should spawn, black at slopes/snow/puddles.
5. **Preview the mask** by temporarily wiring it into Base Color and switching the viewport from Lit to Unlit, then wire it into the `Landscape Grass Output` node's mask input once confirmed, and **reconnect Base Color back** to its original material output.
6. **Enable the required console variable:** `grass.GrassMap.AlwaysBuildRuntimeGenerationResources 1` — ensures the grass map texture the material generates is always rebuilt when needed (without this, the mask can silently fail to regenerate).
7. **In the PCG graph** (from Episode 2): add a **Generate Landscape Textures** node (transcript sometimes calls it "Generate Grass Maps") wired from `Change Grid Size`'s output. In its settings, add an array element under **Select Grass Types** referencing the exact same `LGT_PCGGrass` type name, and **uncheck Exclude Selected Grass Types**.
8. **Add a new input pin to the Point Generator node:** Details panel → Input Pins → **+** → name it `Grass Mask` (must match the name used inside the HLSL code) → set its type to **Base Texture 2D** (not Points, since this is texture data) → wire the `Generate Landscape Textures` node's output into it.
9. **Edit the point generator's compute shader:** click **Open HLSL Editor** to view the node's underlying HLSL source. The existing code: generates a grid of points → filters by a density parameter → randomly offsets point positions off-grid → applies random rotation/scale → applies spatial noise → final density-based point removal → writes output. Insert the new mask-based point-removal **as early as possible** — specifically right after points get their randomized final positions but *before* random rotation/scale is computed — to avoid burning GPU cycles computing rotation/scale for points that will just be discarded. The inserted line samples the mask texture at the point's position via the named grass type/mask input and discards the point if the sampled value is **below 0.9**.
10. **Critical naming rule:** the `Grass Mask` term used in the HLSL snippet must exactly match the Point Generator's new input-pin name (step 8), and the `LGT_PCGGrass` term in the HLSL snippet must exactly match the Landscape Grass Type asset's name (step 1) — both are just plain identifiers so they can be renamed, but the three references (asset name, material's Grass Type dropdown, HLSL variable) must all agree.
11. Save, hit **Force Regen** on the PCG graph, and verify in the viewport/Play mode: grass no longer appears in puddles, on steep slopes, or on snow.

### UE Systems / Blueprints / Settings
- **Assets:** `Landscape Grass Type` (used purely as a mask-carrier, not populated with grass varieties).
- **Landscape Material nodes:** `Landscape Grass Output` (Grass Type dropdown), `TerrainAngleMask` (Pixel Normal, Mask Center, Mask Contrast inputs — copy an existing instance and re-tune rather than reusing the one driving visual slope blending), `One Minus`, `Multiply`.
- **Console variable:** `grass.GrassMap.AlwaysBuildRuntimeGenerationResources 1`.
- **PCG Graph nodes:** `Generate Landscape Textures` (aka Generate Grass Maps; Select Grass Types array + Exclude Selected Grass Types toggle), `Point Generator` (custom input pin added: name `Grass Mask`, type Base Texture2D).
- **HLSL editing:** Point Generator node → **Open HLSL Editor** button opens the compute-shader source directly for hand-editing; point-culling pattern is `if (sample(mask, point.position) < threshold) { remove point }`, inserted immediately after point-offset/scatter and before rotation/scale randomization for performance (cull before doing unnecessary per-point work).
- **Force Regen** button on the PCG graph to manually trigger a full regeneration after HLSL/graph edits.

### Difficulty
Advanced — requires editing raw HLSL inside a PCG compute-shader node (not just graph wiring), precise cross-referencing of identifier names across three separate systems (Landscape Grass Type asset, Landscape Material, PCG graph HLSL), and comfort with Landscape Material graphs (TerrainAngleMask, snow/puddle masks) from the author's earlier landscape-material series.

### UE Version
Not explicitly stated; direct continuation of Episode 2's UE 5.7-era runtime GPU PCG grass system.

### Tags
pcg, materials, landscape, hlsl, blueprint, pipeline, advanced, ue5-7

---

## Related Entries
- `tutorials/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2.md` — Episode 2, builds the runtime GPU grass system (Get Landscape Data → Change Grid Size → Point Generator → Static Mesh Spawner chain) that this episode extends with a landscape-material mask input; shares tags: pcg, blueprint, pipeline, advanced, ue5-7.
- `tutorials/introduction-to-procedural-content-generation-pcg---episode-1.md` — Episode 1, the series' basic PCG concepts.
- Next episode in this series (multiple grass masks / multiple PCG mesh types per biome, per the "next week" teaser) is the direct continuation of this video's end-teaser — look for a title like "Adding Multiple Detail Meshes to Landscapes."
