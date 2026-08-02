---
title: Filtering Overlapping Objects - Procedural Content Generation (PCG) - Episode 11
source: YouTube
url: https://www.youtube.com/watch?v=ikhRzWHisEw
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, blueprint, pipeline, intermediate, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Filtering Overlapping Objects - Procedural Content Generation (PCG) - Episode 11

**Source:** [YouTube](https://www.youtube.com/watch?v=ikhRzWHisEw)
**Author:** Ben Cloward
**Duration:** 24m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to filter out overlapping points in Unreal Engine's PCG.
[0:08] Let's go!
[0:09] Alright, so we're in the middle of a series of tutorial videos on using Unreal Engine's PCG.
[0:22] So far in this series, we've been building this forest.
[0:27] The playlist for the whole series is down in the description, so if you haven't seen the previous videos, you can go back and watch them.
[0:37] Alright, Unreal Engine's PCG is a system that scatters random points, and one of the issues that can happen when you're scattering points is that you end up with points that are in the same location or just too close to each other.
[0:56] For example, here are a couple of trees that ended up really close to each other, and it just doesn't feel very natural.
[1:06] So let's jump out of our play mode here, and I'll show you what's going on.
[1:13] So if we come over here to our grass, and we turn on our points, I'm just going to pick our transform points node here and hit D.
[1:22] So these are all of these gray boxes are the points that we've spawned in our graph, and you can see that there's a lot of overlapping going on.
[1:34] So today I'm going to show you two ways to handle this problem.
[1:37] First, I'll show you how to solve it when you want to remove overlapping points that are in the same graph, just like in this example here.
[1:47] And then I'll also show you how to solve it when you want to make sure that points from one graph don't overlap points in another graph.
[1:57] So let's get right into it.
[2:00] So I'm just going to maximize our forest graph here, and this is the graph that we're using to spawn our trees.
[2:08] So you can see here at the end.
[2:10] And by the way, if you want to see how we made this graph, I have a very detailed video that shows exactly what all of these nodes are doing and how to put them together to create the forest that we've got here.
[2:24] So if you want to see that tutorial, be sure to check the playlist down in the description and go back to the tutorial that talks about how to create the trees in the forest.
[2:37] All right, so here's our example.
[2:38] We've got these two trees that are basically right on top of each other, and we want to fix this problem.
[2:46] So if we take a look at our graph here, we've got a whole bunch of points that we're spawning, and then we split these points up into three different groups based on their distance to the center.
[2:58] I don't know if you can see that, but the points that are black here are the points that are kind of in the middle of the forest, like the thickest, oldest growth of the forest.
[3:10] And then we've got points around those.
[3:13] So these are our thickest trees, our biggest, tallest trees that we're spawning here.
[3:18] And then we've got points that are around those, and these are kind of our medium sized trees.
[3:23] And then on the outside of the forest, we've got our smallest trees.
[3:28] And this kind of mimics the natural way that a forest can grow.
[3:33] So we've got our tallest trees here in the middle, and then our medium sized trees here outside of those, and then our smallest trees, like this one at the very edge.
[3:47] But anyway, getting back to how trees can grow too close together, that's because these points are overlapping.
[3:55] And what we want to do is use a node that's called self pruning to fix this problem.
[4:03] So I'm just going to type self, and there's our self pruning node.
[4:09] And what this node does is it looks at the bounding boxes for each of the points.
[4:16] And if there are two points that are overlapping each other, it's going to get rid of one of them.
[4:22] So if I turn on the debug mode for this part of our graph, you can see that there are two trees here and their points are overlapping.
[4:37] So when I add this node to begin with, it defaults to large to small, the pruning type.
[4:45] And that means the points, the point that has a bounding box that is larger is the one that's going to win and the smaller one is going to get pruned out.
[4:56] So let's take a look at what that looks like.
[5:00] If I connect up my node here and then bring that over, now let's turn off debug on this node here and turn on debug of this node here.
[5:14] And you can see that the tree here with the larger bounding box has one out and that other tree has been pruned.
[5:23] So now we just have one tree instead of two.
[5:26] And you can see that our trees here in our forest are a little bit more naturally spaced.
[5:32] There aren't any trees that are too close to other trees.
[5:37] And that's exactly what we want.
[5:40] Now, we also want to apply this technique to our medium sized trees and to our small trees.
[5:46] So you can see we have a whole bunch of small trees over here.
[5:50] We have medium sized trees there.
[5:52] So let's go ahead and add our self pruning node to the other three or the other two sets of trees.
[6:01] I'm just going to copy and paste this one and we'll wire it up here.
[6:06] And remove the extra wire there.
[6:10] And we'll also add it to this set of trees here.
[6:14] And now what we're going to end up with is points that don't overlap each other.
[6:22] And so we've culled out the trees that were overlapping.
[6:26] And now we have trees that are kind of a little bit more naturally spaced.
[6:30] And we end up with a forest that feels more natural.
[6:36] All right.
[6:36] So that's how you handle overlapping points within the graph itself.
[6:42] So we start out with, if we look at debugging this here, we start out with a whole bunch of
[6:51] points that are all kind of all on top of each other.
[6:54] And then when we use our self pruning node here, we start out with a whole bunch of points
[7:01] where we're able to remove the points that are on top of other points so that we end up with just
[7:10] points that are nice and correctly spaced.
[7:14] And none of them intersecting or overlapping each other.
[7:18] All right.
[7:18] Now the other example that I want to show you is what to do when you have one graph.
[7:24] So for example, here I have one graph that is my forest.
[7:30] And I have another graph that I've made where I'm spawning stumps and fallen logs and just other wood debris.
[7:40] So let's take a look at that graph.
[7:43] This is not one that I've showed you so far in the tutorial series.
[7:48] So what I'm going to do is just walk you through really quickly how this graph is working.
[7:53] The first thing that I want to show you actually let's turn off our debug here for our points just so we can see our forest.
[8:02] The first thing that I want to show you is the assets that we're using to spawn in this graph.
[8:13] So we'll come over here to our this is kind of like my construction yard where I'm showing all of the different
[8:21] elements that are coming together to make our forest.
[8:23] So here we have our trees.
[8:25] Here we have our ground scatter our grass and our little pebbles.
[8:30] And then here we have our larger rocks.
[8:33] And I've showed how to create graphs to scatter all of these elements in the previous videos in this series.
[8:39] But now what I'd like to do is add this extra wood debris here because forests have living trees, but they've also they also have trees that have died and fallen.
[8:51] And so we end up with stumps and logs and and that sort of thing.
[8:56] So these are the assets that we're going to be spawning in this graph today.
[9:01] We have a couple of fallen logs, some pieces of wood and some stumps.
[9:08] And I'll put links to the description in the description down below where you can get these assets.
[9:13] These are assets that are available from Megascans, I think most of them.
[9:18] And you can grab them on the fab or on are using Quixel Bridge.
[9:25] All right, so let's take a look at the graph here.
[9:27] This is PCG wood.
[9:30] And I started by adding the graph to to my map.
[9:35] So you can see I've got PCG wood here.
[9:38] And if we take a look.
[9:40] You can see that it's scattering all of these different logs and stumps and wood kind of all throughout our forest.
[9:48] So I've added the graph here and I set it so that its size is about the size of our whole map.
[9:57] And then let's just take a look at how I constructed this.
[10:00] So the first thing that I did is I use this create points grid node.
[10:05] And you can see that I made the extents of the grid about the size of my whole map.
[10:12] And then I made the cell size inside that grid 1000 by 1000.
[10:17] And so what this means is each of my cells inside the grid, which is where the points are generated, is about 10 meters square.
[10:28] So the idea here is that I'm going to be spawning some kind of wood debris, a stump or a fallen log on average about every 10 meters.
[10:40] If you want more wood debris, you can reduce this amount.
[10:45] And if you want less, you can increase it to make your cells larger.
[10:50] All right, so if we take a look at our debug view for this part of our project, we're going to be looking at the size of our cell.
[10:57] So we're going to take our graph here.
[11:01] Let's see, I'm going to move down here to under our terrain so you can see our points.
[11:06] So here are all the points that we are scattering with the create points grid.
[11:15] The next thing that we're going to do is we're going to transform these points because right now they're in a very orderly grid like this.
[11:21] And nothing in nature is grid in shape like this.
[11:27] And so I'm going to use this transform points to randomize them.
[11:32] So if we take a look at our transform points, you can see I'm offsetting them by four meters, minimum and four meters maximum.
[11:42] So they can move in the X and Y directions by four meters.
[11:46] Well, anywhere between negative four and positive four meters.
[11:51] And then we don't care about the Z because that's going to get snapped to the train.
[11:56] So I can just leave that at zero.
[11:58] And then for a rotation, you can see that I'm rotating them around their Z axis anywhere from zero to 360 degrees.
[12:08] And then for their scale, I'm setting their scale to from 70 to 140.
[12:14] And I set that to absolute.
[12:18] And so if we take a look at the result of that, now you can see we've we've kind of scattered our grid and randomized the rotation and the scale and the offset of the points.
[12:30] So they're a little bit more natural looking and less of a grid pattern.
[12:37] All right, the next thing that I did is added a projection node and I wanted to project.
[12:45] So right now the points are all just on this one plane, but obviously we want the points to be sitting on our landscape.
[12:52] And so I use the projection node and the gets landscape data node to project all of these points on to our landscape.
[13:03] So there are all our points and they're projected onto the landscape.
[13:08] And now the next thing that I want to do is make sure that the points are not in areas that are too steep.
[13:16] Because obviously if a log falls, it's not going to be resting on the side of a cliff.
[13:23] Gravity would drag it down to an area that's more flat.
[13:26] And so in order to achieve that, I use the normal to density node and I set the normal to 001 and the offset to zero and the strength to one.
[13:38] And what this does is it sets the black and white value or the density of the point to depend on, you know, how steep that point is.
[13:49] So if I turn this off and turn the debug on for our normal to density node here, you can see that there instead of all being white, now they're shaded according to how steep the slope is that they're on.
[14:05] So for example, this point here is kind of a grayish color because it's on a steep slope.
[14:11] And then to complete the effect, I can use the density filter node to filter out any points whose density is below a certain threshold.
[14:21] So I want to get rid of that point, for example, because it's on a slope.
[14:26] So I can take that black and white value, the density value, and I can filter it out.
[14:33] So I've set my lower bound to 0.95.
[14:38] So any point that has a density value that's less than 0.95, I'm going to get rid of.
[14:46] So now you can see when I debug this one, all of the points that are on slopes have been removed.
[14:53] So we have points that are on the flat areas now, but not any points that were on the steep slopes.
[15:02] All right. And then the next thing that I want to do right now, because I filtered by density, all of my points are going to be somewhere between 0.95 and 1 for density value.
[15:16] And so what I did in order to get the full range of 0 to 1 density attributes back, I added this attribute noise node.
[15:25] And now I've got the full range of 0 to 1. So you can see some of my points are dark black, some of them are gray, and some of them are white.
[15:35] I don't know if I actually need that node, but I went ahead and put it in anyway just so we can have the full spectrum of density values for these points.
[15:46] And then finally, I used another transform points node just to set the size of the points so that our objects are scaled correctly.
[15:56] I set absolute scale and then I set the min and maximum to 0.7 and 1.4.
[16:04] And this is just so that our objects can be spawned with a proper scale.
[16:10] Then I added my static mesh spawner node here and I added all of my meshes here as mesh entries.
[16:19] And the only thing that I changed for these mesh entries is I turned on collision.
[16:25] So I came down here to collision presets and I set the collision to block all dynamic so that when my player runs around in the world, they're going to run into the stumps, they're going to run into the fallen logs.
[16:39] And we'll have collision on those objects.
[16:42] Okay, now the problem with this, what I've set up here is that currently there's no way for the wood objects to communicate with the tree objects.
[16:58] Let me see if I can find a good example here.
[16:59] It looks like just kind of by luck, all of these objects are kind of correctly interspersed.
[17:12] I'm looking for a place where there's an object that's kind of overlapping.
[17:21] There's a good example.
[17:23] You can see this stump is sort of running into this tree and that rock.
[17:27] And what we want to be able to do is only place these objects where there aren't any trees.
[17:34] So I've got this graph here that is spawning my fallen wooden objects.
[17:43] And I've got this graph here that is spawning my trees.
[17:47] I need a way to be able to have these graphs talk to each other so that my wood objects will not be placed in the same location as the tree objects.
[17:59] So let me show you how to do that.
[18:01] Now up until now in our series of videos, we haven't really used the input and output nodes.
[18:10] Mostly, you know, when you create a new graph, you always have an input and an output node and they just kind of sit there and mostly you don't use them.
[18:19] But what you can do with these nodes is have two different graphs that will communicate with each other.
[18:26] And so what I want to do is take the points that I've spawned for my three different size of trees.
[18:34] And I want to pass them into this output node so that I can take the points that this forest graph is creating and use them in another graph.
[18:45] So all I need to do is take my output node here and yours probably looks like this.
[18:51] But if you click this little down arrow, it'll open up this this object here.
[18:56] You want to set your allowed types to point and then plug all of the points that you want to be able to use in another graph into the output, just like that.
[19:08] And then we'll save this graph with its output setup with its points.
[19:13] And then we'll come over to our wood graph here.
[19:17] And now I can come down here to my content drawer and I can grab the graph that's creating my forest and drag it into my wood graph.
[19:28] Now it's going to ask me what kind of a thing do you want to add in here?
[19:32] I don't need a loop.
[19:34] I just need to add it as a sub graph.
[19:36] So I'm going to add it there.
[19:38] And so there's the output and it allows me to bring the points from my tree graph or my forest graph into my wood graph.
[19:49] And now what I can do is I can add this node called difference.
[19:55] And this is going to do the same thing as the self pruning node.
[19:59] So I can plug my original points into the source of the difference node.
[20:06] And then I can plug my forest points into the difference of the difference node.
[20:14] And then I'm going to come up here and set my density function to binary.
[20:19] And what this is going to do is it's going to take all of the points of the forest and any points in the wood that are overlapping those forest points, it's going to remove them.
[20:32] And this is exactly what I wanted to do.
[20:34] And so now I'm checking to see, hey, is there already a forest point in this location?
[20:42] And if there is, then get rid of the point from the wood area.
[20:50] And so we're just going to check this.
[20:52] I think it's going to remove this stump right here.
[20:55] Let's see what happens.
[20:57] So we're going to delete this part of the graph.
[21:00] And yeah.
[21:01] So now our stump that was overlapping that tree is gone.
[21:06] And if we just kind of, let's see, want to move this here and just kind of organize our graph a little bit.
[21:15] And now we're going to preview our points that we're creating here.
[21:21] I'm just going to get rid of our spawner for now.
[21:25] And we'll just preview these points.
[21:28] Oh, you know what?
[21:31] They're going to be too small.
[21:33] Let me debug these and make them proper size.
[21:47] So now you can see are the points where we're going to be spawning our wood objects are in between the trees and any place where we have our tree.
[21:57] And we're going to add one of those points that used to be overlapping with the trees.
[22:02] We've removed it using that difference node so that we don't get stumps and fallen logs that are overlapping the places where our trees are growing.
[22:20] And this is great.
[22:22] This is exactly what we wanted.
[22:24] So I'm going to connect this up again.
[22:25] We're going to have our debug and.
[22:32] So yeah, now you can see that we've got a forest and we have stumps and fallen logs like this one here.
[22:40] And they're not overlapping with the trees that we already had.
[22:45] So let's go ahead just like we do customarily at the end of every video.
[22:49] Let's go ahead and take our mannequin for a spin here.
[22:55] We'll just kind of run around our level.
[22:58] Here's one of our stumps that we just added today.
[23:01] We were also able to remove our trees that were too close to each other using the self pruning node.
[23:10] And then we used the difference node and we brought in the points that were spawning our trees so that we could look at those points and not spawn our fallen logs and our stumps in the same area as where we were spawning our trees that we already had in here.
[23:32] So cool.
[23:33] Today we took a look at two different methods for removing points that are too close or overlapping each other.
[23:42] I hope this has been useful for you and that you can continue learning about PCG.
[23:49] And hopefully what I've shown today is something that you can apply in your own PCG graphs to make sure that you don't get objects that are spawning on top of each other or too close.
[24:01] Hey, thanks a lot for watching everybody.
[24:05] Hope you enjoyed this one and have a great week.



---

## Captured Frames

- [1:22] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_000.jpg
- [4:22] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_001.jpg
- [5:14] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_002.jpg
- [6:14] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_003.jpg
- [9:01] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_004.jpg
- [9:48] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_005.jpg
- [11:06] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_006.jpg
- [12:18] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_007.jpg
- [13:03] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_008.jpg
- [14:05] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_009.jpg
- [14:46] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_010.jpg
- [17:23] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_011.jpg
- [18:56] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_012.jpg
- [20:19] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_013.jpg
- [22:40] tutorials/frames/filtering-overlapping-objects---procedural-content-generation-pcg---episode-11/frame_014.jpg

---

## Structured Notes

### Core Technique
Two complementary methods for removing overlapping/too-close PCG points: **`Self Pruning`** for removing overlaps *within* a single graph's own point set (e.g. two trees spawned on top of each other), and a **cross-graph `Output`/subgraph + `Difference`** technique for making one graph's points avoid another graph's points entirely (e.g. keeping fallen-log/stump debris from spawning inside existing trees).

### Summary
Series finale addressing a common PCG artifact: randomly scattered points sometimes land at or near the same location, producing visibly overlapping objects (two trees fused together). Two scenarios are covered. **Scenario 1 (same-graph overlap):** the Episode 5 forest graph's three tree-size tiers (large/medium/small, split by distance-from-center) each independently get a `Self Pruning` node inserted before their Static Mesh Spawner. Self Pruning compares each point's bounding box against its neighbors and removes the smaller-radius point wherever two overlap, using a **Large to Small** pruning type by default (the object with the bigger bounding box wins; the smaller loses) — applied identically to all three tree tiers, it eliminates fused-together trees while preserving the natural size-gradient look. **Scenario 2 (cross-graph overlap):** a new, previously-unshown "PCG Wood" graph scatters fallen-log/stump/wood-debris meshes (Megascans assets) across the whole map via the by-now-familiar pattern (`Create Points Grid` → `Transform Points` for randomization → `Projection` onto the landscape → `Normal to Density` + `Density Filter` for slope exclusion → a final `Transform Points` for scale → `Static Mesh Spawner` with collision enabled, Block All Dynamic, so the player physically collides with logs/stumps). The problem: this graph has no way to know where the forest graph already placed trees, so wood debris sometimes spawns overlapping a tree trunk. The fix uses PCG's **Input/Output** subgraph nodes (present on every graph by default but rarely used until now): on the forest graph, the `Output` node's pin is set to Allowed Type = **Point**, with all three tree-tier point streams wired into it — this exposes the forest's spawned points as data other graphs can consume. In the wood graph, the forest graph asset is dragged in and added as a plain **subgraph node** (not a Loop node, since there's no per-item iteration needed here), exposing that same point output. A `Difference` node then takes the wood graph's own points as **Source** and the imported forest points as **Differences**, with **Density Function** set to **Binary** (matching the fix from Episode 7's exclusion-zone technique) — any wood point that spatially coincides with a forest point gets fully removed, so fallen logs/stumps never spawn on top of existing trees.

### Key Steps
**Scenario 1 — Self Pruning (same-graph overlap):**
1. Identify the overlap: temporarily enable Debug on a pre-spawn points node to see gray/white bounding-box cubes clearly overlapping at the same location.
2. Add a `Self Pruning` node (type "self" to find it) inserted just before the affected `Static Mesh Spawner`.
3. Leave (or confirm) **Pruning Type** = **Large to Small** — for each pair of overlapping point bounding boxes, the point with the larger bounding box is kept and the smaller one is discarded.
4. Repeat/duplicate this node for every parallel track that can independently produce overlaps — in the Episode 5 forest graph, this means adding one `Self Pruning` node to each of the three tree-size tiers (large/medium/small) right before their respective Static Mesh Spawners.
5. Verify: debug the points after Self Pruning — previously overlapping pairs now show only one surviving point, and the resulting forest has no visibly fused-together trees.

**Scenario 2 — cross-graph exclusion (Output/subgraph + Difference):**
6. Build the second graph independently first (author's "PCG Wood" graph, not previously shown in the series): `Create Points Grid` (Grid Extents ≈ whole map, Cell Size 1000×1000 = ~1 wood-debris object every 10m) → `Transform Points` (Offset ±4m X/Y, Z=0 since height comes from projection; Rotation Z 0–360°; Scale 70–140% absolute) → `Projection` (Projection Target = `Get Landscape Data`) → `Normal to Density` (Normal = (0,0,1), Offset 0, Strength 1) → `Density Filter` (lower bound 0.95, removes points on slopes too steep for fallen debris to rest on) → `Attribute Noise` (restores full 0–1 density range after the filter step skewed it, matching the pattern from Episode 5) → a second `Transform Points` (Absolute Scale 0.7–1.4, purely for final object sizing) → `Static Mesh Spawner` (fallen logs/stumps/wood pieces, with **Collision Presets** set to **Block All Dynamic** so the player physically collides with them).
7. On the **forest graph** (Episode 5), open its default `Output` node, click its expand arrow, set **Allowed Types** to **Point**, and wire all three tree-tier point streams (large/medium/small, post-Self-Pruning) into it.
8. In the **wood graph**, drag the forest graph asset from the Content Drawer directly into the graph editor; when prompted, choose to add it as a plain **subgraph node** (not a Loop node — no per-point iteration is needed, just a one-time data pull).
9. Add a `Difference` node: wire the wood graph's own (pre-spawn) points into **Source**, and the forest subgraph node's point output into **Differences**.
10. Set the Difference node's **Density Function** to **Binary** (not the default Minimum, per the same fix established in Episode 7) — this fully removes any wood point that spatially overlaps a forest point, rather than only partially thinning based on density comparison.
11. Wire the Difference node's output into the wood graph's Static Mesh Spawner (replacing the direct connection used before).
12. Verify: a stump previously overlapping a tree trunk (and a nearby rock) is now gone from that location — the wood graph no longer spawns anything on top of existing forest trees, while both graphs' Debug views confirm complementary, non-overlapping point sets.

### UE Systems / Blueprints / Settings
- **Nodes:** `Self Pruning` (Pruning Type: Large to Small; also has a Radius Similarity Factor and Component Source setting visible in the graph parameters), `Output`/`Input` graph pins (Allowed Types = Point; present by default on every PCG graph, rarely used until cross-graph communication is needed), subgraph node (vs. Loop node — chosen when a one-time data pull is needed rather than per-point iteration), `Difference` (Source/Differences inputs; Density Function = Binary, reused from Episode 7's exclusion-zone fix).
- **Wood-graph-specific nodes** (all reused patterns from earlier episodes): `Create Points Grid`, `Transform Points` (×2 — one for position/rotation scatter, one purely for final scale), `Projection` + `Get Landscape Data`, `Normal to Density`, `Density Filter`, `Attribute Noise`, `Static Mesh Spawner` with **Collision Presets: Block All Dynamic**.

### Difficulty
Intermediate/Advanced — Self Pruning (Scenario 1) is a simple one-node fix; the cross-graph Output/subgraph/Difference technique (Scenario 2) requires understanding PCG's Input/Output pin system and the subgraph-vs-loop distinction, concepts not otherwise used elsewhere in the series until this point.

### UE Version
Not explicitly stated; concludes the UE 5.7-era PCG series, reusing the Episode 5 forest graph and Episode 7's Difference/Binary density-function fix.

### Tags
pcg, blueprint, pipeline, intermediate, advanced, ue5-7

---

## Related Entries
- `tutorials/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep.md` — Episode 5, the forest graph that gains Self Pruning nodes here and whose Output node is exposed for cross-graph use; shares tags: pcg, blueprint, pipeline, ue5-7.
- `tutorials/using-splines-for-boundaries---procedural-content-generation-pcg---episode-7.md` — Episode 7, source of the `Difference` node and the Binary-vs-Minimum Density Function fix reused verbatim in this episode's cross-graph exclusion technique; shares tags: pcg, blueprint, pipeline, intermediate, ue5-7.
- `tutorials/adding-rocks-with-hierarchical-generation---procedural-content-generation-pcg---.md` — Episode 9, the rocks referenced as one of the other "construction yard" elements (trees, grass, rocks, and now wood debris) making up the full forest environment built across this series.
