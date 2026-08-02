---
title: Introduction to Procedural Content Generation (PCG) - Episode 1
source: YouTube
url: https://www.youtube.com/watch?v=NZLtrWLNTes
author: Ben Cloward
ingested: 2026-08-02
ue_version: "PCG added 5.2 (experimental); production-ready as of 5.7"
tags: [pcg, blueprint, pipeline, beginner, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Introduction to Procedural Content Generation (PCG) - Episode 1

**Source:** [YouTube](https://www.youtube.com/watch?v=NZLtrWLNTes)
**Author:** Ben Cloward
**Duration:** 20m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, we're starting a brand new series of videos about creating environments procedurally
[0:07] using PCG in Unreal.
[0:10] Let's go!
[0:17] PCG is a powerful tool, and this new series is going to be amazing.
[0:23] But before we jump in and start learning it, it's important for us to cover the basics,
[0:29] so you know what it is and why you should learn it.
[0:34] PCG is a system built into Unreal that allows you to create large, complex environments
[0:43] that are fast and easy to edit and run efficiently in your game project.
[0:50] It was first added to the Unreal Engine as an experimental feature in version 5.2 in early
[0:56] 2023.
[0:59] In version 5.7, it's now considered to be production ready, which is why we're going
[1:06] to jump in and learn it.
[1:09] Okay, but I hear you saying Unreal already has tools for placing objects in large environments.
[1:19] Why should I go to the trouble of learning this new system?
[1:25] So let's talk about that.
[1:27] Here's a basic environment that I created in Unreal 4 several years ago.
[1:33] I built it manually by placing down the rocks and the trees one at a time.
[1:39] For the smaller rocks and ferns, I used the foliage tool that allows you to paint objects
[1:45] onto the landscape using a brush, which speeds up the workflow quite a bit.
[1:52] As I worked, I made up rules for myself for where things should be placed.
[1:57] So for example, this grass here went right along the edge of the water, and then I placed
[2:03] ferns going up the banks of the brook here.
[2:09] I also added these little mounds around the trees so wherever a tree met the landscape,
[2:16] there's a little mound that allows it to blend into the landscape better.
[2:22] So as you can see, as I was working, I made up these little rules for myself where the
[2:29] objects should be placed.
[2:32] But the engine doesn't know these rules, they're just in my head.
[2:38] So this environment looks pretty nice, but now that it's done, what can I do with it?
[2:44] What if I decide that I want to change my rules?
[2:47] What if I want to put the grass further up the bank and the ferns close to the water?
[2:55] Or what if the level designers decide that they want to move the river kind of over here
[3:01] 20 meters to the left of where it is now?
[3:05] I would have to go back in and kind of erase everything that I have and basically start
[3:11] from scratch.
[3:13] Or what if I just need to take what I have here and build something similar in another
[3:19] level?
[3:20] I would have to build it manually all over again.
[3:25] So when building an environment using this method, the engine has no understanding of
[3:30] what you're doing.
[3:32] And once you're done, you have a very static thing that's hard to adjust.
[3:39] There's lots of manual labor to make it and lots of manual labor to change it.
[3:46] So what about PCG?
[3:48] How is it different?
[3:51] Well, when you build an environment using PCG, you're basically teaching the engine
[3:59] what all of the rules are.
[4:02] Instead of manually placing every tree and every rock, you explain to the engine how
[4:08] placement of these objects should work and then the engine does the object placement.
[4:15] You're basically building an object placement machine and then letting it do the work.
[4:23] The real power of PCG is that your result is dynamic and can instantly rebuild itself.
[4:33] This means that you can change the rules after the environment is built and it will
[4:39] adapt to any change you make.
[4:42] You want to move the river 20 meters to the left?
[4:46] Sure, you can do that and all of the rocks in the foliage go right along with it.
[4:52] You want the ferns growing near the water?
[4:55] Just change a few nodes and all the ferns instantly update.
[5:00] If you want to create a similar environment in another level, you just add your PCG object
[5:05] to that level and all your assets get added just like you have them here.
[5:13] Now I'm not going to sugarcoat this and pretend that setting all of this up is easy.
[5:20] It's actually quite complex and requires a lot of effort to learn and build.
[5:26] But once the work is done, you have a very powerful world building machine that can do
[5:33] amazing things.
[5:35] So with PCG, the paradigm is shifting from lots of manual labor and static results that
[5:43] are hard to edit to lots of work defining the system up front.
[5:50] But once you have the system set up, it's flexible and easy to make changes fast.
[5:56] You're turning over the slow parts of the process, the manual placement of objects,
[6:01] to the engine which allows you to focus on the creative work.
[6:10] I mentioned a minute ago that setting up PCG is complex.
[6:15] There's a lot to learn and that's exactly why I'm making this series of videos.
[6:21] I see a lot of power in this system and I want to enable you to use it.
[6:27] Over the coming weeks, we're going to deep dive into this system and I'm going to show
[6:32] you how to achieve some amazing things.
[6:35] But today, we're going to start off with just some very basic things.
[6:40] So first of all, to get started with PCG, you need to enable the PCG plugin.
[6:47] So you come up here under edit and choose plugins and then in the search bar, you can
[6:52] just type PCG and the one you want to enable is called procedural content generation framework,
[7:00] PCG.
[7:01] This is the base plugin.
[7:03] There are a whole bunch of extras and add-ons and additional things that you can enable
[7:09] to allow for more power and content.
[7:13] But we're not going to deal with any of those for now.
[7:16] We're just going to start at the very beginning.
[7:18] So just enable procedural content generation framework, PCG.
[7:23] All right.
[7:24] And then once you have that plugin enabled, you can start creating PCG content.
[7:30] At its core, PCG is just a system that places a set of points in the world.
[7:38] And then spawn object and then spawns objects on those points.
[7:43] You set up the rules and the parameters for how those points are placed.
[7:48] And then the engine does the work of placing the points and adding the objects to them.
[7:55] So let's create our very first PCG asset.
[8:00] I'm going to click on the content drawer and come in here to the PCG graphs folder.
[8:07] And I'm just going to right-click and pick PCG, PCG Graph to create a new one.
[8:14] Now it's going to open up this template browser.
[8:19] And there are a bunch of templates here that can help me get a jumpstart on achieving specific
[8:24] tasks in PCG.
[8:26] But the graph that we're going to create is so simple that I don't even want to start
[8:32] with one of these templates.
[8:33] So I'm just going to pick Create Empty Graph.
[8:37] And that's going to give us a graph with nothing in it.
[8:38] I won't even bother to give it a name this time.
[8:41] I'm just going to let it be called New PCG Graph.
[8:46] And we're going to take that graph and drag it into our map and drop it right there.
[8:52] I'm going to put it at the origin here.
[8:55] So I'm just going to type 0000 so that it's right at the origin.
[9:02] And it'll just kind of come over here and center it up.
[9:05] So the next thing that I want to do is open the graph.
[9:09] And this graph is the tool that we use for creating points, for scattering them around,
[9:17] and then for spawning objects on those points.
[9:19] And so that's exactly what we're going to do.
[9:22] And so the very first node that we're going to add to the graph, by the way, this is very
[9:26] similar to the Material Editor Graph if you've used that.
[9:31] So a lot of the same kinds of things that you do in the Material Editor can also be
[9:37] done in a PCG Graph.
[9:40] So we're going to right click here.
[9:42] And I'm just going to type create.
[9:44] And the node that we want is called create points grid.
[9:49] So this is a node that generates points.
[9:52] And it has one output port.
[9:54] And you can see that the little icon by this output port is like a pile of three points.
[10:02] And that means this node contains point data.
[10:06] Now if we want to visualize the data that this node contains, there are two ways of
[10:12] doing that.
[10:13] The first way is to press the A key.
[10:16] So I'm going to press A. And you can see here now down in my attributes window, there's
[10:23] a big list.
[10:25] And this is my array of all of my points.
[10:28] And you can see that each point has an x, y, and z position.
[10:33] And then it has a whole bunch of other attributes.
[10:35] It has bounds.
[10:38] And if we scroll over here, the attributes just keep going.
[10:41] It has color, density, steepness, and also a random seed value.
[10:46] So each of my points has a bunch of attributes.
[10:50] And I can look at each of the points in the list just by scrolling down here and seeing
[10:55] all of them.
[10:56] You can see that my list currently goes from zero all the way down to 99.
[11:02] So I have 100 points just by default.
[11:06] So I told you there were two methods.
[11:08] So that's the A pressing A. I'm able to see all the points in the list.
[11:13] The other method that I can use for visualizing my points is by pressing D. Now D stands for
[11:20] A stands for attributes, by the way.
[11:24] So if I'm in debug mode, let me just rip off my graph here and make my window a size where
[11:34] we can see what's going on out here in the world.
[11:38] So here you can see that I've got kind of like a white plane.
[11:42] And these are all of the points that I'm visualizing in the world.
[11:46] Now in order to make them show up just a little bit better, what I can do is come over here
[11:52] with my create points grid node selected.
[11:56] I can come to this debug section and right now it's scaling to the extents.
[12:03] And what I can do is set this to absolute and then just scale these points down to like
[12:08] 0.3 for example.
[12:11] And now you can see that my points have been placed in the world.
[12:17] So I'm able to visualize the attributes with A looking in the attribute window here, like
[12:26] that.
[12:28] And with D, I'm able to actually display the points in the world by putting a little box
[12:34] on each of the points.
[12:36] I can also come over here and change the mesh that I'm using to represent the points.
[12:42] Right now it's just using the default cube.
[12:44] But what that does is it allows me to see what the points look like in the environment
[12:50] before I actually add anything to them.
[12:53] Now speaking of adding things to the points, kind of the whole purpose of this is to create
[13:00] points and then spawn something on them.
[13:04] So in order to spawn something, I can just grab left click here and drag out and drop.
[13:12] And now I can type spawn and what I want to do is spawn static meshes.
[13:18] So I'm going to add this node called static mesh spawner.
[13:22] And this is going to allow me to select what I want to put on each of those points.
[13:29] All right, so we can come over here and in the mesh selector section, we have mesh entries.
[13:35] I'm going to hit the plus button to add an element to my array.
[13:39] And then I'm going to open up the descriptor.
[13:42] And here now you can see this dropdown for a static mesh.
[13:47] Now I think we should add some ferns here because we had some ferns in that other scene
[13:53] we were working on.
[13:55] So let's just type sm underscore fern.
[13:59] And yep, sure enough, there are some static mesh ferns.
[14:02] And I can just pick that static mesh and stick it into the slot.
[14:07] And we'll save that.
[14:09] And now we've got ferns spawned in a really nice uniform grid.
[14:18] Look at that. All my ferns nicely lined up.
[14:21] Okay, so now obviously meshes in reality don't grow this way.
[14:29] And so we need to find a way of altering the positions of my points so they're not lined
[14:35] up in a nice uniform grid.
[14:39] And so what I'm going to do is add a transform node so I can grab this and drag it out.
[14:46] And we're going to use the transform points node.
[14:52] And what this is going to do is it's going to add random transforms to each of my points.
[14:59] So with that transform points node selected, if I come up here you can see I have an offset
[15:05] min and an offset max.
[15:09] And just so that we can see our ferns, they're kind of mixed in with everything else right
[15:13] now.
[15:14] So I think what we should do first is just kind of raise them up.
[15:18] And so maybe we'll give them a vertical offset of like 50.
[15:26] Let's see if that's enough.
[15:28] Then we can plug this in.
[15:30] Yeah, okay.
[15:32] Now you can see I've got my ferns kind of raised up a little bit.
[15:37] And let's offset them maybe 90.
[15:42] There we go.
[15:43] Now I've got some floating ferns, but at least they're not mixed in with all the rest of
[15:48] the foliage in the environment.
[15:50] Okay, now instead of being in a nice uniform grid like this, we want them to be offset
[15:59] on the X and the Y.
[16:00] So what I'm going to do is create a range.
[16:03] I'm going to go anywhere from negative 300 to 300 on both the X and the Y.
[16:09] And we'll make this negative 300.
[16:11] And now what you can see is each of those points, instead of being a nice uniform grid,
[16:18] we've offset each of our points somewhere between negative 300 and 300.
[16:25] So we've kind of scattered them out.
[16:28] And the other thing that we can do is give them a random scale and a random rotation.
[16:36] Now for the rotation, we want them to rotate around their Z axis, which is the axis that's
[16:44] pointing up.
[16:45] And we want that to be like anywhere in the full circle.
[16:48] So I'm going to go negative 180 to 180.
[16:52] And that's going to give all of my ferns, you know, license to rotate anywhere between
[16:59] negative 180 and 180.
[17:01] And then for the X and the Y, we're going to do like negative 10 to positive 10 and
[17:10] negative 10 to positive 10.
[17:13] And that gives them each just a little bit of tilt.
[17:17] And then for scale, let's go with something like 0.7 to 1.4.
[17:25] And because we have this uniform box checked here and these locks on, I just have to type
[17:30] them into one and it applies it to all of them.
[17:33] So now you can see that we have ferns that are randomly scaled and rotated and translated.
[17:43] So we've got them kind of a little bit more organically scattered.
[17:49] And that is a very basic illustration of what PCG does.
[17:53] So if we switch back here to our graph again, just the basics.
[17:59] We have a node that generates points.
[18:03] We have a node that takes the points positions and kind of randomizes them.
[18:08] And then we've got our last node that takes those points and puts meshes on them.
[18:13] And so now we're able to very quickly and easily add 100 ferns to our environment and
[18:22] randomly rotate and scale them.
[18:24] Now, this rabbit hole goes a lot deeper than this.
[18:28] This is just like the very tip of the surface of what can be done with this tool.
[18:34] But I hope you can see I'm creating these objects procedurally and defining rules for
[18:42] how they're scaled and how they're positioned.
[18:45] And it's really easy to just change the rules and instantly have the results reflect the
[18:51] changes that I made.
[18:52] And I can scale that up to a huge extent to create the environments that you see here
[19:02] in this level.
[19:03] They've created this entire forest using PCG to add all of these objects with logic and
[19:13] rules.
[19:15] And it makes it really easy to adjust the rules and change how the objects are added.
[19:22] So if you're excited to learn about PCG, let me know down in the comments.
[19:28] If you're not subscribed yet, get subscribed because this is going to be a really cool,
[19:34] really useful series of videos.
[19:36] By the way, this is something that I'm learning at the same time as you guys.
[19:41] And so in order to make these videos, I'm learning new things kind of just a couple
[19:46] of days before you do.
[19:48] So if there are things that you know of that will be useful that I maybe skipped over or
[19:53] didn't point out in a video during this series, I'd love to have your participation.
[19:59] If there are things that you know how to make the system go faster or just mistakes that
[20:04] I'm making because I'm learning as we're going here, please let me know.
[20:09] And also, if there are specific things that you'd like to know how to make PCG do, let
[20:15] me know about those as well.
[20:17] I'm excited to go on this learning adventure with you, figure all of this stuff out.
[20:22] So be sure to come back next week for the next video in the series.
[20:29] It's going to be great.
[20:30] And in the meantime, have a great week.



---

## Captured Frames

- [7:00] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_000.jpg
- [8:14] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_001.jpg
- [9:50] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_002.jpg
- [12:10] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_003.jpg
- [13:22] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_004.jpg
- [14:09] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_005.jpg
- [15:05] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_006.jpg
- [16:16] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_007.jpg
- [17:25] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_008.jpg
- [19:55] tutorials/frames/introduction-to-procedural-content-generation-pcg---episode-1/frame_009.jpg

---

## Structured Notes

### Core Technique
Introduction to Unreal's **PCG (Procedural Content Generation) Framework**: enabling the plugin, creating a PCG Graph asset, and building the simplest possible point-generation-to-mesh-spawning chain (Create Points Grid → Transform Points → Static Mesh Spawner) to scatter randomized foliage instead of hand-placing it.

### Summary
Series-opener explaining *why* PCG matters before touching any nodes: manually-built environments (shown via the author's own hand-placed Unreal 4 rock/tree/foliage scene) encode placement "rules" only in the artist's head — the engine has no understanding of them, so any change (move the river, adjust where ferns grow, reuse the layout in another level) means manually redoing the work. PCG inverts this: you teach the engine the *rules* for placement via a node graph, and the engine performs the placement — meaning changes to the rules instantly propagate everywhere. Added experimental in UE 5.2 (early 2023), production-ready as of UE 5.7. The hands-on portion builds the minimal PCG graph: a point generator, a randomizing transform, and a mesh spawner, ending with ~100 randomly scaled/rotated/offset ferns instead of a rigid grid — explicitly framed as "the tip of the iceberg" versus the full forest-scale PCG environment shown at the end.

### Key Steps
1. Enable the plugin: Edit → Plugins → search "PCG" → enable **Procedural Content Generation Framework (PCG)** (the base plugin; related experimental add-ons like Biome Core/Biome Sample and FastGeo/Geometry Script Interop exist but aren't needed yet).
2. Create the graph asset: Content Drawer → right-click in a folder → PCG → **PCG Graph** → in the template browser, pick **Create Empty Graph** (skip the presets for this basic example).
3. Drag the new PCG Graph asset into the level (snap to origin, e.g. type `0 0 0` in the location field) and open it for editing — the graph editor closely resembles the Material Editor's node-graph UX.
4. Add a **Create Points Grid** node (right-click → type "create") — generates a grid of 100 points by default, each carrying attributes: X/Y/Z position, bounds, color, density, steepness, and a random seed.
5. Inspect the point data two ways: press **A** (Attributes) to list every point and its attribute values in the Attributes panel; press **D** (Debug) to visualize the points in the viewport as small boxes/cubes. In the node's Debug section, switch Point Scale from "Scale to Extents" to **Absolute** and set it small (e.g. 0.3) to see individual points clearly; the debug mesh (default cube) can also be swapped for a custom preview mesh.
6. Add a **Static Mesh Spawner** node downstream of Create Points Grid — in its Mesh Selector → Mesh Entries, click **+** to add an entry, open the descriptor, and pick a static mesh (e.g. searching `SM_Fern`) to spawn one instance per point. At this stage the meshes spawn in a perfectly uniform grid.
7. Add a **Transform Points** node between the two (Create Points Grid → Transform Points → Static Mesh Spawner) to randomize the grid: set a vertical **Offset** (e.g. Z ≈ 50–90) to lift meshes clear of other foliage for visibility while tuning; set **Offset Min/Max** on X and Y (e.g. −300 to 300) to scatter points off-grid; set **Rotation Min/Max** on Z (−180 to 180) for full free rotation around the up axis, and small X/Y ranges (e.g. −10 to 10) for a slight organic tilt; set **Scale Min/Max** (e.g. 0.7 to 1.4) for size variation — with the uniform/lock toggle enabled, one typed value applies to all axes at once.
8. Result: a graph of exactly three nodes (generate points → randomize transform → spawn mesh) turns a rigid 100-point grid into organically scattered, randomly rotated/scaled/offset ferns — and changing any node's parameters (or swapping the target mesh) instantly re-generates the whole result.

### UE Systems / Blueprints / Settings
- **Plugin:** Procedural Content Generation Framework (PCG) — base/required; Biome Core, Biome Sample, FastGeo Interop, Geometry Script Interop mentioned as optional experimental add-ons, not covered yet.
- **PCG Graph nodes used:** `Create Points Grid` (point generator; Debug section has Point Scale = Scale to Extents/Absolute + scale value + preview mesh override), `Transform Points` (Offset Min/Max, Rotation Min/Max, Scale Min/Max per-axis, with a uniform-box lock to apply one value to all axes), `Static Mesh Spawner` (Mesh Selector → Mesh Entries array, `+` to add, per-entry static mesh descriptor).
- **Point data attributes** (visible via the Attributes panel, key `A`): Position (X/Y/Z), Bounds, Color, Density, Steepness, Seed.
- **Viewport visualization key:** `A` = show attribute list, `D` = toggle debug point visualization in the 3D viewport.

### Difficulty
Beginner — explicitly the "very basics" first episode of a longer series; assumes no prior PCG knowledge, though familiarity with Unreal's Material Editor node-graph conventions helps since PCG Graph reuses similar UX patterns.

### UE Version
PCG added experimental in UE 5.2 (early 2023); marked production-ready as of UE 5.7 (the version this series treats as the baseline for adoption).

### Tags
pcg, blueprint, pipeline, beginner, ue5-7

---

## Related Entries
- Ben Cloward's "Shader Graph Basics" episodes (`tutorials/input-vectors---shader-graph-basics---episode-9.md`, `tutorials/random-noise---shader-graph-basics---episode-35.md`) — same author/channel and same node-graph-editor teaching style (explicitly compared to the Material Editor in this video), useful for consistent terminology across his series.
- This is Episode 1 of an ongoing PCG series in this library — see later episodes (Efficient Grass, Landscape Grass Masks, Growing a Forest, Automatic Tree Blending, Splines for Boundaries, Spawning Along Splines, Rocks via Hierarchical Generation, Magic Moss, Filtering Overlapping Objects) for the deeper techniques this episode explicitly defers ("the rabbit hole goes a lot deeper than this").
