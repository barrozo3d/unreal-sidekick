---
title: Creating Magic Moss With PCG - Procedural Content Generation (PCG) - Episode 10
source: YouTube
url: https://www.youtube.com/watch?v=QyCzfsuakuY
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, materials, pipeline, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating Magic Moss With PCG - Procedural Content Generation (PCG) - Episode 10

**Source:** [YouTube](https://www.youtube.com/watch?v=QyCzfsuakuY)
**Author:** Ben Cloward
**Duration:** 23m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to automatically add 3D moss to the rocks in your environment using PCG.
[0:09] Let's go!
[0:16] Alright, so we're in the middle of a series of videos showing how to use Unreal PCG.
[0:23] So far in this series, we've used PCG to build this forest environment.
[0:29] I'll link the playlist to the whole series down in the description so you can watch the rest of the videos.
[0:36] Last time, we added these rocks to our environment using PCG's hierarchical generation.
[0:45] And today, I'm going to show you how to cover them with moss like this.
[0:52] Before PCG, I could create an effect like this by opening my rock meshes in Blender one at a time and using a mesh scatter tool to cover them with moss cards.
[1:05] But this was a time-consuming process because I had to do it uniquely for every individual mesh that I wanted to add the moss to.
[1:14] And the resulting mesh is used a lot of memory.
[1:18] With the technique that I'm going to show you today in PCG, you can add moss like this to any mesh almost instantly without needing to make any alterations to the rocks outside of Unreal.
[1:33] So, let's jump in and I'll show you how I did this.
[1:37] The first thing that I want to do is just give you a really quick rundown of how I made the moss mesh cards.
[1:48] So, first thing that I did is I took a look at the Quixel Megascans library and there are a bunch of textures on there for moss atlases.
[2:00] This is one example of one.
[2:02] And I've actually made this one by compositing two of them together.
[2:06] I just downloaded a couple of different moss textures and I took the ones that I liked and put them all on the same sheet.
[2:15] So, I made a texture like this and you can see it has an alpha channel that cuts out the moss nicely.
[2:23] Then I brought this texture into a program like Maya or 3ds Max or Blender for example.
[2:30] And I applied this texture to a large plane.
[2:35] And then for each individual moss element here, I created a single polygon and then I mapped this texture to that set of polygons.
[2:49] So, first I took the texture and applied it to a plane so that I could see it in the viewport.
[2:56] Then I created a single polygon that encapsulated each of the individual moss elements and then I split those elements out into their own cards and imported them into Unreal.
[3:11] So, in Unreal, my moss actually ends up looking like this.
[3:16] So, I have a bunch of static meshes one for each moss element.
[3:22] Now, I kind of went overboard and created like 38 different elements and you probably don't need something quite that complex when you're doing this.
[3:32] You can probably get away with maybe three or four mesh variations.
[3:38] But the point is each of these is its own little card.
[3:42] So, if I open this up here, you can see that I just have a flat card with that single moss element mapped to it.
[3:51] And this is what we're going to scatter all over our meshes using PCG.
[3:57] So, let's go ahead and jump in and make our PCG graph that will generate these moss cards.
[4:05] Now, one interesting thing about the way that I've made these rocks is that the rocks are created using the hierarchical generation system.
[4:15] And they don't exist way off in the distance.
[4:21] And so, I need to set up PCG so that it's mapping my moss cards just to the rocks that currently exist and not to the entire set of rocks.
[4:38] It's not a static problem we're trying to solve.
[4:41] I'm dynamically generating these rocks.
[4:44] And so, I also have to dynamically generate the moss cards to add to them.
[4:50] So, here's the graph that we created in the video last time to create our rocks.
[4:56] Here at the end, we have our static mesh spawner.
[4:59] And this is what's creating our rocks.
[5:01] But what we want to do is take each rock at this point and loop through each of the rocks.
[5:08] And for each rock, we want to add a bunch of points to it so that we can spawn our moss cards onto it.
[5:17] And so, since we're using this data and passing it out, we need to come over here to our out attribute name and give it the name of mesh.
[5:27] If we don't have that there and we have none, then we won't be able to identify our mesh attributes, our rocks that we've spawned in the rest of the graph.
[5:41] And so, I need to set my out attribute name to mesh.
[5:46] And then I'm going to key off of that word in just a minute in order to identify my meshes to spawn my moss cards onto them.
[5:57] Alright, so the next thing that I need to do is come to my content drawer, go to my PCG folder, and I'm going to create a new graph that will enable me to loop through each of the rocks and add moss card points to them.
[6:15] So, I'm going to right click here, I'm going to come down and pick PCG, I'm going to create an empty graph, and I'm going to call this PCG Moss Point Generator.
[6:32] And then we'll open this graph up, and this is going to be a sub-graph.
[6:38] And so, I need to use my input and my output points here.
[6:42] So, what I'm going to be inputting are points, and they're the points that represent the rocks.
[6:49] So, I'm going to call this, I'm going to give it the label of points in.
[6:54] And I'm going to set the usage to loop because I want to loop over each rock and do what I'm about to create in this graph for each of them.
[7:04] My allowed types are going to be points, and then I want to set my pin status to normal.
[7:12] So, I'm going to be bringing points in, and for each of the points, I'm going to loop over this graph.
[7:17] Alright, the next thing that I want to do is create a node called yet attribute from point index.
[7:25] And so, I'm going to grab my points here, bring them in, and then this is where I want to use my mesh name that I added to my static mesh spawner.
[7:37] So, I'm going to say my input source is called mesh.
[7:42] So, my static mesh spawner is outputting the mesh data, and then I'm going to get that mesh data here with this get attribute from point index node.
[7:54] And then I'm going to use that mesh data to spawn points.
[7:59] And so, in order to do that, I need to create a mesh sampler node.
[8:04] And typically, when you create a mesh sampler node, you just tell it what mesh you want it to sample on.
[8:10] But in my case, I'm dynamically spawning these meshes, and I don't know exactly which one I'm going to be using.
[8:18] So, I want to be able to pass that data in.
[8:21] So, I'm going to click this little down arrow here and open this up.
[8:25] And here, I have an input for static meshes, and I'm going to connect up the attribute output from my get attribute from point index node into my static mesh attribute.
[8:36] And that way, as I'm looping through these rocks, I get a rock in here, I isolate the mesh attribute, and then I pass the mesh attribute into my mesh sampler node.
[8:50] And then this node is what I'm going to use to spawn all of the points onto my rock.
[8:58] So, on my mesh sampler node, I want to set my sampling method to Poisson sampling.
[9:06] And this is the type of sampling method I want to use.
[9:10] The other methods available are per triangle and per vertex.
[9:15] And my rocks don't have enough triangles or vertices to be able to spawn enough points for my moss.
[9:23] And so, I want to use Poisson sampling so that I can scatter more points onto them than I have available normally.
[9:31] So, now that I've set Poisson sampling, I can come down here and set the values for that.
[9:38] For my sampling radius, I'm going to set that to 0.2.
[9:43] For my maximum number of points, I'm going to set this to 40,000.
[9:48] And for subsample density, I'm going to set this to 0.5.
[9:53] This is a value that if you set it lower, it defaults to 10, but if you set it lower, you'll get better performance in your point sampling.
[10:02] Because it uses kind of a lower quality version of the point scattering.
[10:09] It still does a fine job. It just does it quicker.
[10:14] Okay, so now that we are sampling those points, we want to copy the points to the mesh.
[10:20] And so, I'm going to add a copy points node here.
[10:24] And for the target, I'm going to grab the mesh that's coming in.
[10:28] And for the source, I'm going to take the points that I just created.
[10:32] So we're copying these sample points onto the source mesh that we just created.
[10:41] Alright, and then the last thing that we need to do is pass out our points.
[10:45] So we're going to take the points that we just generated and pass them out here.
[10:51] And here, I can just call the output points out.
[10:57] And I can set the allowed type to points.
[11:04] Alright, so I've created a subgraph.
[11:06] And what this does is it brings in the meshes, the rock meshes, and then it loops through them one at a time.
[11:14] And for each one, it isolates the attribute called mesh.
[11:18] And it uses a point sampler to use Poisson sampling to spawn a whole bunch of points, as many as 40,000 onto the rock.
[11:30] It copies those points to the rock, and then it outputs the point data.
[11:38] So let's save this.
[11:40] And now what we want to do is come back to our rock spawner.
[11:46] And we want to go ahead and use that subgraph that we just created.
[11:53] So I'll come down here and I'll grab my PCGMOS point generator subgraph and drag it in.
[12:00] And it's going to ask me, do you want to create it as a subgraph node or a loop node?
[12:05] And I want it to be a loop node because I need it to perform this loop for each of the rocks that are coming out of my static mesh spawner.
[12:14] Now, in order to pass in the correct data here, I need to create another node that's called attribute partition.
[12:23] So I'm going to create an attribute partition node.
[12:29] And the attribute that I want to grab out of my static mesh spawner is the mesh attribute.
[12:37] So I'm going to type mesh right there.
[12:39] So I'm grabbing the mesh attribute out of my static mesh spawner and then I can pass that into my PCGMOS point generator.
[12:51] All right, well, let's go ahead and debug this and see what I've created so far.
[12:56] So I'm just going to create a debug node here.
[13:00] And we'll save our graph and take a look at what it looks like in our level.
[13:05] All right, here's one of our rocks and you can see that it's just solid white.
[13:10] And that's because the points are a little bit too big.
[13:12] So I'm going to take my debug node here.
[13:15] We're going to set the scale method to absolute.
[13:20] And I'm going to set the size to like 0.003.
[13:26] And now you can see I've got these points randomly scattered all over my rock.
[13:35] And that's exactly what we're looking for.
[13:37] And what's better is I can come over here and I've got points randomly scattered over this rock and this rock and that rock.
[13:48] In fact, anything that I plug into the attribute partition here that has an attribute of mesh, it will scatter these points all over it.
[13:59] And so I could pass trees into it.
[14:02] I could pass, you know, my little rocks into it.
[14:06] Anything that I want to spawn moss onto, I can use or I can do that using this method.
[14:13] So pretty cool.
[14:15] We're most of the way there.
[14:17] We just want to add a few more things.
[14:20] If we take a look at our rock, we're getting moss kind of everywhere on it.
[14:25] And so I think the next thing that we want to do is get rid of points that are facing down.
[14:33] And so in order to do that, I can just come in here and create a normal density node.
[14:41] And this is going to take the density attribute and give that density attribute of value according to the normal.
[14:53] So right now the normal is set to 001, which is up facing.
[14:58] And then I can give it strength value.
[15:01] I'm just going to leave that strength value of one.
[15:03] And let's go ahead and plug our debug node into here.
[15:07] And before our density node was white, so all of our points were white.
[15:12] But now if we take a look at our rock, you can see that the points that are not facing up.
[15:19] Let me just make these points a little bit bigger so that we can see them.
[15:25] I'm going to make these 0.07.
[15:28] Yeah, so now you can see the points that are pointing up have a density value of one or they're white.
[15:36] And the points that are pointing down have a density value of black.
[15:40] And I can use that density attribute now to throw out the points that I don't want.
[15:47] So I can create a density filter node here and just filter out the points that are above a specific value.
[15:59] So this defaults for the lower bound to 0.5.
[16:03] But I'm going to set it to 0.65.
[16:06] And you can tune this if your effect is a little bit too expensive.
[16:10] You have maybe too much moss.
[16:12] You can raise this lower bound.
[16:14] So if I set this to 0.9, for example, let's go ahead and debug the result coming out of here.
[16:21] It's only going to leave the points that are just pointing exactly straight up.
[16:28] But if I set this to, I'm going to set it to a value of like 0.65.
[16:33] And that way I get just a little bit more points on the top of my rock.
[16:39] So now I can use these points to scatter my moss cards.
[16:46] But there is one more thing right now.
[16:48] The points are just kind of a uniform rotation and scale.
[16:52] And I want to kind of randomize them a little bit.
[16:57] And so I'm going to add a transform points node.
[17:08] And we'll connect this up.
[17:10] And we want to randomly rotate our points.
[17:13] So we're going to come over here to rotation.
[17:16] And I'm going to say our points can be anywhere from negative 40 to 40 on the X and the Y.
[17:25] And then on the Z axis, they can be anywhere from 0 to 360.
[17:32] And that will allow the points to just be randomly rotated along their Z,
[17:38] but then have like a negative 40 to 40 along their X and their Y.
[17:43] So now if we debug this, you can see our points have some really nice random rotation on them.
[17:51] And so now at this point, now that we've got these points scattered on our rocks,
[17:54] I think we're ready to add our static mesh spawner.
[17:58] Like I said, I created 38 of these moss cards.
[18:06] And it's going to take me a really long time to add all of these to a static mesh spawner.
[18:11] So I'm not going to do that.
[18:12] I'm just going to copy and paste the static mesh spawner that I've already created
[18:17] just so you guys don't have to sit here and watch me do all this stuff 38 times.
[18:23] So here's my static mesh spawner.
[18:26] And here you can see I have 0, I can scroll all the way down here, 0 to 37.
[18:34] These are all the moss cards that I've added.
[18:38] I'll just open up one of these and you can see there's my moss card.
[18:43] And basically on all these attributes, I just went through and unchecked every single one of these boxes.
[18:50] I want to turn everything off to make the cards as fast as possible to render,
[18:55] except for you definitely want it to render in the main pass and be visible.
[19:00] But everything else I turned off.
[19:03] And then for culling, I set my start cull distance to 400 and my end cull distance to 1200.
[19:12] So I can get the moss cards to fade out over a distance.
[19:17] So at four meters, they start fading out and then at 12 meters, they're completely faded.
[19:23] Just to save on a little bit of performance.
[19:26] Alright, so now I can take my transform points node here and pass that into my static mesh spawner.
[19:35] So you can see I'm first I'm spawning my rocks and then I'm taking the rock
[19:43] and for each of the rocks, I'm spawning my moss cards onto them.
[19:50] So I'll save this and we'll jump out and now you can see I've got beautiful moss spawned on all my rocks.
[20:02] And you know what? It's a little bit too big.
[20:04] I forgot in the transform points here to set my scale.
[20:09] I want to set my scale to absolute scale and I want to set them anywhere from 0.1 to 0.3.
[20:21] And that'll just size them a little bit nicer.
[20:23] You know, obviously you're welcome to set these to whatever works good for the moss cards that you created.
[20:30] But I think the size of 0.1 to 0.3 works really nicely.
[20:36] Alright, let's come over here and take a look at this rock that I've got on the clip here.
[20:44] And you can see that I've got this really beautiful moss spawning on my rock.
[20:52] And my rocks are also dynamically spawning.
[20:56] So I'm able to manage the performance of this pretty well.
[20:59] But the system allows me to put this moss on anything that I want.
[21:04] And I don't have to jump out to Blender or whatever other software and kind of painstakingly and manually add these cards outside and then bring it in and have like an FBX file that's really big because I've added these there.
[21:22] I'm able to dynamically add them right inside of Unreal.
[21:27] And this is just super cool to me.
[21:30] Alright, so that brings us to the end of the video.
[21:32] Let's go ahead and take our mannequin and run around a little bit.
[21:39] So here's our moss spawning on our rocks.
[21:43] You can see the moss there.
[21:45] And then as I kind of move away from the rocks, the moss fades out.
[21:52] And it just adds a lot of depth and additional complexity to these rock meshes.
[22:00] Just makes them look, you know, that much more interesting to look at.
[22:07] And it makes that rock feel really realistic in my opinion.
[22:13] I just absolutely love this, you guys.
[22:16] Alright, thanks a lot for watching.
[22:18] That's my tutorial video for today.
[22:22] Come back next week for another PCG tutorial.
[22:27] If you have any suggestions for me on how I can take this technique and make it even more efficient or make it visually more appealing,
[22:38] I'd love to hear from you.
[22:39] Leave those comments down below.
[22:41] We can get a great conversation going.
[22:44] If you have another method that you use for creating moss like this, please let me know.
[22:51] Anyway, that's it for today.
[22:53] Have a great week, everybody.



---

## Captured Frames

- [3:42] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_000.jpg
- [5:27] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_001.jpg
- [8:36] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_002.jpg
- [10:20] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_003.jpg
- [12:00] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_004.jpg
- [12:29] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_005.jpg
- [13:20] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_006.jpg
- [14:41] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_007.jpg
- [16:06] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_008.jpg
- [17:43] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_009.jpg
- [19:50] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_010.jpg
- [20:21] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_011.jpg
- [21:39] tutorials/frames/creating-magic-moss-with-pcg---procedural-content-generation-pcg---episode-10/frame_012.jpg

---

## Structured Notes

### Core Technique
A PCG **loop subgraph** that dynamically scatters flat "moss card" meshes onto whatever mesh a PCG node just spawned — using `Mesh Sampler` (Poisson sampling) driven by a per-point mesh attribute rather than a hardcoded static mesh reference — so moss can be added to dynamically-spawned, hierarchically-generated rocks (Episode 9) entirely inside Unreal, without pre-authoring moss onto each rock mesh in a DCC tool.

### Summary
Replaces a previously manual, per-mesh workflow (opening each rock in Blender/Maya/3ds Max, using a mesh-scatter tool to hand-place moss cards, one time per unique mesh, bloating file size) with a fully procedural in-Unreal system that works on any mesh at runtime — critical because Episode 9's rocks are dynamically spawned via hierarchical generation, so there's no fixed set of "rock instances" to pre-author moss onto. The moss itself is a set of ~38 flat single-polygon "cards," each mapped to one moss cluster cut from a composited Megascans moss-atlas texture (with alpha) — authored once in a DCC tool, then imported as ordinary Unreal static meshes (a handful of variations would suffice for most projects; the video's 38 is described as overkill). The PCG technique: on the existing rock-spawning graph's final `Static Mesh Spawner`, set its **Out Attribute Name** to `mesh` so downstream nodes can identify which mesh got spawned at each point. A new **loop subgraph** ("PCG Moss Point Generator") is built separately: its input pin is set to **Usage: Loop** (so the parent graph invokes it once per incoming point/rock) and typed as Points; inside, a `Get Attribute From Point Index` node pulls out the `mesh` attribute for the current rock, which feeds a `Mesh Sampler` node's **Static Mesh** input dynamically (rather than the node's normal static, pre-selected mesh) — sampling method set to **Poisson** (not Per-Triangle or Per-Vertex, since the rocks don't have enough geometry density for those to yield enough points) with a small Sampling Radius (0.2), a high Max Point Count (40,000), and a reduced Subsample Density (0.5, trading a little quality for speed) to scatter thousands of points across the rock's actual surface. `Copy Points` then stamps those sampled points onto the rock mesh, and the subgraph outputs the result. Back in the main graph, the subgraph is dragged in and instantiated as a **Loop node** (not a plain subgraph node), fed via an `Attribute Partition` node keyed on the same `mesh` attribute name — this is what makes the loop iterate per-rock. Post-processing on the resulting per-rock point cloud: a `Normal to Density` node (reference up-vector, strength 1) tags each point's density by how upward-facing its surface normal is; a `Density Filter` (author settles on lower bound 0.65, tunable for a performance/coverage tradeoff) discards points on downward/sideways-facing surfaces so moss only grows on top-facing areas; and a `Transform Points` node adds randomized rotation (X/Y tilt ±40°, full 0–360° Z spin) and scale (0.1–0.3 absolute) for natural variation. A final `Static Mesh Spawner` (all 38 moss-card meshes, every rendering-cost toggle disabled except main-pass visibility, with a 400–1200cm start/end cull-distance fade) spawns the actual moss cards on the filtered/transformed points. Because the technique keys purely off a generic `mesh` attribute name, it's explicitly reusable for adding detail meshes (moss or otherwise) onto any PCG-spawned object, not just these specific rocks — trees, other props, etc.

### Key Steps
1. **Moss asset preparation (outside this PCG technique, done once in a DCC tool):** composite several Quixel Megascans moss-atlas textures (with alpha) onto one sheet; apply to a plane in Maya/3ds Max/Blender; build one single-polygon card per distinct moss cluster, mapped to that region of the atlas; export each as its own small static mesh (author made 38; 3–4 is usually enough).
2. **Tag the source Static Mesh Spawner's output:** on the existing rock-spawning graph (Episode 9)'s final `Static Mesh Spawner`, set **Out Attribute Name** to `mesh` — without this, downstream nodes can't identify which mesh was spawned at each point.
3. **Build the loop subgraph:** Content Drawer → PCG folder → new empty PCG Graph, named e.g. "PCG Moss Point Generator." Set its **Input** pin: Label = "Points In," **Usage = Loop**, Allowed Types = Points, Pin Status = Normal (this Usage setting is what makes the parent graph invoke the subgraph once per incoming point instead of once overall).
4. Inside the subgraph, add `Get Attribute From Point Index`, wired from the loop's input points, with **Input Source** set to `mesh` — extracts the current rock's mesh reference for this loop iteration.
5. Add a `Mesh Sampler` node; expand its collapsed "Static Mesh" section and wire the `Get Attribute From Point Index` output into its **Static Mesh** input (instead of picking a fixed mesh from a dropdown) — this is what lets the same subgraph work for whichever mesh happens to be at each point. Set **Sampling Method** to **Poisson Sampling** (Per-Triangle/Per-Vertex don't have enough source geometry on low-poly rocks to yield useful point counts). Configure Poisson settings: **Sampling Radius** 0.2, **Max Number of Points** 40,000, **Subsample Density** 0.5 (lower = faster/lower-quality sampling; default is 10).
6. Add a `Copy Points` node: **Target** = the mesh data flowing through, **Source** = the Mesh Sampler's generated points — stamps the sampled points onto the actual rock surface.
7. Add an **Output** pin (label e.g. "Points Out," Allowed Type = Points) and wire the Copy Points result into it. Save the subgraph.
8. **Instantiate the loop in the main rock graph:** drag the "PCG Moss Point Generator" asset into the main graph — when prompted, choose **Loop node** (not "subgraph node") so it iterates per-point.
9. Add an `Attribute Partition` node between the rock Static Mesh Spawner and the loop node, with its target attribute set to `mesh` (matching the Out Attribute Name from step 2) — this correctly groups/passes the per-rock mesh data into the loop.
10. **Debug-verify:** temporarily wire a `Debug` node to the loop's output; if points render as one solid white blob, reduce the Debug node's point **Scale Method** to Absolute and a small size (e.g. 0.003) to actually see the individually-scattered points across the rock surface. Confirm the same setup scatters points correctly on multiple different rocks (or any other mesh with a `mesh` attribute) simultaneously.
11. **Filter to upward-facing surfaces:** add `Normal to Density` (reference Normal = (0,0,1), Strength = 1) after the loop — writes each point's Density based on how closely its surface normal matches "up," then add a `Density Filter` keeping only points above a tuned lower bound (author settles on 0.65 — higher values = less moss coverage but cheaper; 0.9 keeps only near-perfectly-flat-up points).
12. **Randomize orientation/scale:** add a `Transform Points` node — Rotation Min/Max: X/Y = ±40°, Z = 0–360° (full random spin around up-axis, slight tilt otherwise); Scale Min/Max (Absolute Scale mode): 0.1–0.3 (tuned to the specific moss card size — author initially forgot this step and got oversized moss).
13. **Spawn the moss cards:** final `Static Mesh Spawner` with all moss-card mesh variants added as entries (copy-pasted from a previously-built one to avoid manually re-adding dozens of entries); for each entry, disable every rendering-affecting checkbox except main-pass visibility (for performance, since these are simple flat cards), and set **Start/End Cull Distance** (author: 400/1200cm — moss starts fading at 4m, fully gone by 12m) for a soft distance fade.
14. Wire the (loop → Normal to Density → Density Filter → Transform Points) chain into this final Static Mesh Spawner — the parent graph now spawns rocks, then for each rock spawns a scattered field of moss cards on its upward-facing surfaces.

### UE Systems / Blueprints / Settings
- **Subgraph/loop system:** custom PCG subgraph with an Input pin set to **Usage: Loop** and an Output pin, instantiated in a parent graph as a **Loop node** (vs. a plain subgraph node) to iterate once per incoming point.
- **Nodes:** `Get Attribute From Point Index` (Input Source = a named point attribute, e.g. `mesh`), `Mesh Sampler` (Static Mesh input driven dynamically by an attribute rather than a fixed picker; Sampling Method = Poisson vs. Per-Triangle/Per-Vertex; Sampling Radius, Max Number of Points, Subsample Density), `Copy Points` (Target/Source), `Attribute Partition` (keyed on a named attribute, e.g. `mesh`, to route data into a Loop node correctly), `Normal to Density` (reference Normal vector, Strength), `Density Filter`, `Transform Points` (Rotation/Scale Min-Max, Absolute Scale mode), `Static Mesh Spawner` (Out Attribute Name property; per-mesh-entry render-cost toggles; Start/End Cull Distance).
- **Debug tip:** Debug node's Point Scale Method (Absolute) and Size — needed to see individually-scattered points instead of one overlapping white mass when point density is very high.

### Difficulty
Advanced — the loop-subgraph pattern (Usage: Loop input pin, Loop node instantiation, Attribute Partition routing) and dynamic mesh-attribute-driven Mesh Sampler are among the more advanced PCG constructs in the series; the post-processing (Normal to Density, Density Filter, Transform Points) reuses patterns familiar from earlier episodes.

### UE Version
Not explicitly stated; continues the UE 5.7-era PCG series baseline, directly building on Episode 9's hierarchical-generation rock system.

### Tags
pcg, materials, pipeline, advanced, ue5-7

---

## Related Entries
- `tutorials/adding-rocks-with-hierarchical-generation---procedural-content-generation-pcg---.md` — Episode 9, the rock-spawning graph this episode's moss subgraph is attached downstream of; the `mesh` attribute naming and cull-distance-fade pattern are directly reused; shares tags: pcg, materials, pipeline, advanced, ue5-7.
- `tutorials/using-landscape-grass-masks-with-pcg---procedural-content-generation-pcg---episo.md` and `tutorials/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-.md` — Episodes 3–4, source of the `Normal to Density`-adjacent slope/surface-based filtering concept (there via HLSL/landscape masks, here via a dedicated node) applied to a different placement context (mesh surfaces instead of landscape).
