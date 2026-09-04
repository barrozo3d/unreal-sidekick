---
title: Introducing Mesh Terrain: Craft Large Complex Worlds | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=QJwTTmNez3k
author: Unreal Engine
ingested: 2026-07-18
ue_version: "UE 5.8 (experimental; production-ready targeted late 2027)"
tags: [landscape, nanite, pcg, world-building, open-world, performance, advanced]
extraction_status: complete
frames_dir: tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Introducing Mesh Terrain: Craft Large Complex Worlds | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=QJwTTmNez3k)
**Author:** Unreal Engine
**Duration:** 47m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Welcome to Dratri Talk about Mesh Train, which is a new feature that we just released in
[0:06] 5.8.
[0:07] And I'm genuinely excited to finally show it off after being in development for two plus
[0:12] years.
[0:13] Yeah, my name is Michael Balzer.
[0:16] I am engineering director at Epic Games and I am responsible for a number of content
[0:20] creation tools within the annual editor and also have been leading the development of
[0:24] Mesh Train over the last couple of years throughout the entire development cycle.
[0:29] And that's Etienne Carrier.
[0:31] He's a senior technical artist at Epic Games and he's basically our ex-producer about
[0:37] all things for all things Mesh Train.
[0:42] Before we go into details about Mesh Train, let's briefly go over some of the motivations
[0:47] for why we actually have been developing Mesh Train.
[0:52] Basically height maps have been a staple in games for quite a long time.
[0:56] I mean, popular was one of the only ones, Khmunchi.
[0:59] I still remember playing those games.
[1:01] So if you look at me, then you know how long ago that is.
[1:07] In 2011 Unreal actually introduced landscape, which was our or is our Height map based
[1:12] train system, but yeah, it has been quite a while.
[1:16] And I think Height maps are going to continue to be relevant for games, but they definitely
[1:21] have the limitations and I think it's now time to take the next step.
[1:27] One of those limitations for Height maps is that they have very strict topological restrictions.
[1:33] So they only provide displacement in the normal direction.
[1:39] You can't do overhangs, you can't do tunnels, you can't do floating islands.
[1:43] Anything that is not just upwards displacement is basically not possible.
[1:49] The other thing is then if you want to have these kinds of features in games, then you
[1:54] again need to use static meshes.
[1:56] You need to cut holes in the terrain, you need to add to the terrain, you need to blend
[1:59] between the terrain and those meshes.
[2:01] So there's a lot of overhead involved.
[2:05] The other important restrictions of Height maps is the resolution restrictions.
[2:10] One is that they have usually uniform resolution, meaning basically the same resolution for
[2:17] the entire terrain or for large parts of it.
[2:21] Which effectively means that the resolution that you use in practice is kind of a compromise
[2:25] between like the spatial frequency of the features you want to have in your terrain and the
[2:31] storage cost for the entire Height map.
[2:35] Another restriction is that it's a regular grid.
[2:37] It's really just next to squares, next to squares, next to squares.
[2:41] There's no variation in the apologies, always the same structure.
[2:46] And they are drawbacks because of this.
[2:48] If you have a character next to a certain Height map pixel size, you can only change the
[2:56] terrain to a certain degree without artifacts appearing.
[3:00] And then also based on the alignment of the feature, you get better results.
[3:04] If you have a diagonal alignment of a feature, you get those really nasty jagged edges and
[3:09] there's not really too much you can do about it.
[3:15] And there are also some U.E. specific restrictions admittedly.
[3:20] Landscape usually works well up to about 8K by 8K.
[3:25] Anything larger than that becomes a bit painful to say the least.
[3:30] If you want to have really large open world games, you then have to have multiple landscape
[3:34] actors to build out your world, which then has its own challenges in your transition areas
[3:38] and just managing that data.
[3:41] And the other issue is also file contention.
[3:43] Right, they have those landscape proxies and they have relatively large.
[3:47] And as soon as two artists want to work on two different features in your terrain, which
[3:52] happen to be in the same landscape proxy, well, one person is going to check it out and
[3:56] win is able to edit it and then you need to check it in and then the next person can check
[4:01] it out.
[4:03] And again, like those are landscape restrictions, arguably there are better systems maybe than
[4:08] landscape, but those restrictions are really kind of typical for what you have to deal
[4:13] with when working with HydeiteMap.
[4:15] In a way kind of terrain really used to be special.
[4:18] There's a good reason for why games are using and have been using HydeMap's, but arguably
[4:24] they're not that special anymore.
[4:27] One reason for why they were special is that they require independent continuous LEDs and
[4:32] streaming.
[4:34] Now we have nine-night four or a few years, which basically addresses exactly that issue.
[4:40] The other thing for terrain is that due to the big size, we have lots of biomes, lots
[4:45] of materials that need to be handled, lots of textures effectively that you need for that,
[4:51] creating a lot of draw calls.
[4:53] With RVT, this is also addressed where effectively the cost for dealing with many textures is shifted
[4:58] from render time to load time.
[5:01] Things get rendered into RVT and then whatever you need in a certain area is just available
[5:05] in this one RVT texture.
[5:09] Another reason is that terrains are usually big, which means that the size of the data representation
[5:15] is very important.
[5:17] Arguably, this again was more relevant in the past nowadays when we look at what games actually
[5:23] store, it's more than two-thirds just textures for materials.
[5:29] And geometry is usually what we see kind of in the range of 10 plus maybe 15% of all of
[5:34] the data.
[5:35] So taking a bit of the texture, move it over to geometry and even grow it a bit, it's
[5:40] not really going to make a big difference these days.
[5:47] So one question you have gotten a lot over the last years, why not voxels?
[5:52] Like the simple answer is that in a way it doesn't move the needle enough compared to
[5:57] height maps.
[6:00] It's basically 3D geometry stored in a similar way to height maps, it has similar restrictions.
[6:07] It's a regular grid, even if it's a multirestolution.
[6:11] It has a resolution constraint, so it's basically just a 3D height map.
[6:17] The other thing is that if we would introduce voxel based techniques to the engine, we
[6:22] would require new tools, new algorithms, new data structures.
[6:26] We would have to create that stuff and it would be again, be a bespoke solution for terrain
[6:32] that we then have to square against all of the other stuff in the engine.
[6:35] So again, it's complexity similar to how landscape adds a lot of complexity.
[6:41] If one thing changes in the engine, there's like a 40% chance that landscape is somehow
[6:46] affected and we want to avoid that.
[6:51] The other thing is also, even if we would use voxels, in reality we then need to transform
[6:57] the render data again to triangle measures because those are just still the most efficient
[7:02] thing to render.
[7:03] So it will basically just be an editor tool.
[7:07] And we thought that's not really worthwhile.
[7:09] So instead we think it's really worthwhile to double down the triangle measures.
[7:13] And we have the capabilities in the engine to do that.
[7:16] And we thought things should be fast enough nowadays to really step beyond voxels and go
[7:21] really to full triangle measures for terrain.
[7:27] Hence the name, mesh terrain.
[7:29] And also I really like kind of just simple descriptive names.
[7:32] Let's not come up with another fancy name.
[7:35] So yeah, let me give you a brief overview of what mesh terrain is all about.
[7:43] Let's get started kind of with division and goals for mesh terrain that we set out with
[7:47] and which we really managed to hold on to throughout the development cycle.
[7:51] First of all, again, doubling down on triangle measures.
[7:53] No restrictions on topology, structure, resolution and really just to build kind of the
[8:00] most high quality environments they can.
[8:04] It needs to be easy to use for small teams.
[8:07] So we really thought we need to lean into proceduralism to allow a single artist or a small
[8:12] team of artists to create large environments without hence sculpting everything individually.
[8:17] And it also needs to be collaboration friendly.
[8:20] So we need to avoid file contention.
[8:23] We need to avoid a scenario where someone needs to check out the file and two other people
[8:27] need to wait for the person to finish their work.
[8:31] The other constraint is that we want to deploy the same source data on multiple platforms.
[8:37] We want to avoid situations where you have to author one set of content for high end
[8:41] and one set of content differently for low end.
[8:44] It needs to be one set of source data which we then deploy on multiple platforms based
[8:48] on what these platforms actually can support.
[8:52] And the other thing, and it kind of was this caveat for Voxels, we want to avoid kind
[8:58] of specialized systems.
[9:01] We really want to build things generically.
[9:04] When we build things for mesh terrain, they aren't supposed to be for mesh terrain only.
[9:08] They are supposed to benefit the entire engine and we don't want to basically create more
[9:13] complexities and dependencies, especially at runtime.
[9:17] So in that respect, that kind of mesh terrain is not only for terrain, but it goes beyond
[9:22] terrain for other use cases as well that I will briefly mention later on.
[9:29] And because we want to build a generically, we're kind of trying to disambiguate the generic
[9:34] part from an engineering part.
[9:37] The generic technology stack for mesh terrain is what we internally call mesh partition.
[9:42] And this is basically just tools and systems for managing and authoring very large meshes,
[9:48] whatever those very large meshes are.
[9:51] And then on top of mesh terrain, mesh partition, sorry, you already know this, even I confuse
[9:55] this though.
[9:57] On top of mesh partition, we then want to build a tool set that is dedicated for terrain
[10:02] authoring.
[10:03] You want to have your terrain sculpting tools and your modified or create tunnels and
[10:08] all of that stuff that is terrain specific.
[10:11] And this is basically the mesh terrain layer on top of it.
[10:18] So what actually is mesh partition?
[10:22] It's basically a set of capabilities for authoring and managing meshes across streaming
[10:27] cell boundaries.
[10:29] That's basically all it is.
[10:31] Of course, there's a little more to it.
[10:34] But it basically means that you might have meshes that are so big that you can't load
[10:39] them at once in the client, and you can't even load them in the editor before running
[10:43] out of memory.
[10:45] And this is what mesh partition is supposed to enable.
[10:48] It allows you to partially load and partially stream parts of a mesh.
[10:53] Right?
[10:54] If a giant mesh, they're parts to it.
[10:56] And then in the editor, you can say, draw a little rectangle in volt partition and
[11:01] say, only load this part of the entire mesh partition.
[11:09] The other part is also that the processing of those giant meshes is still done holistically.
[11:15] So we want to make sure that the boundaries between the parts of the mesh don't join
[11:20] the artifacts and you basically can't see them.
[11:23] Or at least we give you the tools to make sure that you can't see them.
[11:27] And in that respect, it's a little bit similar to landscape, just much more generic, much
[11:33] more integrated and obviously with 3D geometry instead of height maps.
[11:40] So basically, it allows you to author and render big continuous surfaces in full 3D.
[11:47] And you don't have any restrictions on complexity or scale.
[11:51] Again, everything might not fit into all the memory in your editor.
[11:57] You can load it selectively.
[11:59] You can edit it selectively.
[12:01] You can check out parts of it and only work on this small part.
[12:05] And other people work on another small part and you try to not get into each other's
[12:09] way.
[12:10] But yeah.
[12:11] And again, mesh partition is built generically.
[12:13] But in this talk, we mainly focus on terrain.
[12:17] But it also applies to other use cases.
[12:20] And here's maybe just one example.
[12:23] It's a magic new build.
[12:24] It's like, I don't know, some sci-fi shooter.
[12:26] And you have this giant city sized spaceship that displays in, I don't know.
[12:33] So basically mesh partition would also be able to handle this case.
[12:37] Instead of having to split up this giant spaceship into hundreds or thousands of static mesh
[12:41] assets that lift someware and some file structure in your content browser, it's managed
[12:46] as one thing.
[12:48] You can selectively load and edit it.
[12:50] It gets split up, streamed automatically.
[12:54] And it's just basically much less cognitive overhead to deal with a large mesh like this
[12:59] compared to how you would build it right now.
[13:04] And again, those parts that you kind of split the mesh up into is what we call sections.
[13:12] And those sections are really a completely arbitrary subdivision of your mesh.
[13:16] There's no restrictions on like a specific structure or hierarchy.
[13:21] You can really just based on individual triangles, split things up in any way that you want.
[13:27] If you have like a little POI in your game, you can just make this little POI into a section.
[13:32] And then the stuff around it is another section.
[13:35] Again, no restrictions on shape or structure.
[13:38] And then yeah, you load each of those sections individually, process them individually.
[13:43] And yeah.
[13:45] There's these sections, so these base sections, they're also just measures, they're just
[13:50] triangle measures.
[13:51] So you can use the tools in the editor to edit them in any way that you want.
[13:55] There's again no restrictions.
[13:57] It's just the triangle soup partitioned.
[14:03] And then you take those base sections and you can add so-called modifiers.
[14:09] And the modifiers effectively just change the data and the base sections.
[14:15] In this example here on the right, you just have a so-called texture modifier.
[14:19] And it's just a height map texture once again.
[14:21] There's still a view, so no doubt about it.
[14:24] And it displaces the 3D geometry of the underlying base section.
[14:28] You can move the modifier around.
[14:30] It's non-destructive, very easy to use.
[14:33] And it's also very fast in its application.
[14:36] So like, especially texture modifiers, they are almost real time.
[14:40] So in a way, it's kind of like some of you might know landscape patches.
[14:45] It's landscape patches and steroids and much more capable, much more generic.
[14:53] Okay, so we have sections, base sections, and we have modifiers.
[15:01] And the base sections and modifiers is effectively the source data that artists offer.
[15:06] And then the mesh partition pipeline transforms the source data into intermediate data and eventually into run-term data.
[15:14] The intermediate data is taking the base sections, apply all of the modifications, and then create automatically a preview section, a preview mesh for the editor.
[15:24] So that whatever you do in the editor immediately shows up in front of you.
[15:28] The build of that is happening in the background and synchronously.
[15:31] And we use kind of dynamic measures for things that are still in flight and processing and then swap in the energy or metry.
[15:38] So here, we try to be as clever as possible to make it as seamless as an experience as possible.
[15:44] And then again, the mesh partition pipeline also takes the end result of the intermediate data and converts it into run-term data.
[15:53] And the run-time data is really optimized for random performance or whatever you want to optimize it for.
[16:00] And you can create it in a way that it's platform specific.
[16:04] You can build it so you have compile sections for high end and you have compile sections for low end.
[16:11] And they can be different data structures.
[16:14] The typical example is that on high end we use Nanite,
[16:18] a mobile or switch we don't have Nanite right now.
[16:21] So you export static mesh LEDs.
[16:27] So it's really a very, very clear separation of source data, intermediate data, and run-time data.
[16:33] And this makes your world system much less complex and gives us a lot of flexibility to also like future proof it.
[16:40] If there are new run-time data representations that let's say allow real-time deformation at some point,
[16:46] then mesh partition can generate the data.
[16:48] Right.
[16:53] Let's take a little bit of a closer look how we do the processing of that source data.
[16:57] Again, source data is base sections plus modifiers.
[17:01] There are effectively two constraints that come into play.
[17:04] One is overlap.
[17:07] So if a modifier is overlapping based on the bounding boxes,
[17:12] it's overlapping a base section.
[17:13] Then we know that when we process the base section,
[17:16] we need to take that modifier into account.
[17:20] And then in scenarios where we have multiple modifiers affecting the same base sections,
[17:26] then priorities come into play.
[17:28] So you can define priorities for all of the different modifiers.
[17:31] There's a group-aim mechanism and everything related to that as well.
[17:34] So it's not just like every single one, but groups of modifiers.
[17:39] And then the priority for the modifiers determines the order of application to a base section.
[17:46] It effectively means that we build a dependency graph,
[17:48] and then we use the dependency graph to parallelize things as much as possible.
[17:54] And the dependency graph also helps us for caching.
[17:57] So we try to do as little rebuilds as necessary.
[18:01] Let's say in this example, we have this modifier M3.
[18:05] Let's say only M3 changes.
[18:08] It means that any processing up to M0 and M1 and M2
[18:13] can just come directly from the cache.
[18:15] And then we just apply M3.
[18:18] And by parallelizing everything as much as possible,
[18:21] based on the dependency graph,
[18:23] and using good caching strategies,
[18:26] the build of mesh partition is actually surprisingly fast.
[18:32] Okay.
[18:34] So much about a bit of an introduction to what mesh terrain is based on.
[18:38] Let me hand it over to Hien, who's going to talk about toolset and workflows.
[18:44] Thank you, my y'all.
[18:47] All right, let's take a look at the mesh terrain toolset.
[18:52] So this will be a starting point.
[18:54] All the tools available to work on mesh terrain
[18:57] will be available in the mesh terrain mode.
[18:59] Shift-6 is the current shortcut.
[19:02] It's good to know that regular modeling tools
[19:05] would also work on mesh partition because it's mesh.
[19:08] However, it won't benefit from the non-destructive workflow
[19:11] that all the modifiers brings.
[19:13] So, and we'll only work on the base mesh.
[19:17] Now, this is all the modifiers that we have available
[19:20] to shape up our terrain.
[19:22] They're all non-destructive,
[19:24] so they can be modified, removed at any points while working on the terrain.
[19:28] So we'll take a closer look at some of them right now.
[19:32] So the first one, the mesh modifier will basically project the vertices
[19:37] of the mesh partition onto a selected mesh.
[19:40] We can either use a Statsk mesh from the Content Browser
[19:43] or use a dynamic mesh that we can generate in Blueprint, for instance.
[19:49] Then we have the texture modifier that create basically displacement using a texture.
[19:54] And this one also has a cool option to test the mesh automatically
[19:59] according to the deformation.
[20:01] And this can give us crisp result, no matter the resolution of the base mesh on the need.
[20:07] Then next, we have the spline modifier.
[20:10] It works with either open or closed splines.
[20:14] And of course, you can both lower or raise the terrain
[20:17] or actually move stuff sideways if you're working on a vertical surface
[20:21] or downward if you're working on ceiling, for instance.
[20:26] And then next, we have the brush modifier
[20:29] it has several different brush available.
[20:33] Also has a cool sublayer system that you can use to organize your work
[20:37] into different layers.
[20:39] And in addition to displacement,
[20:41] it can also be used to paint which channels are to an mesh.
[20:47] And then we have Boolean operation available,
[20:51] again using either Statsk or dynamic mesh.
[20:55] And it supports both union and subtract mode.
[20:58] We also have a trim mode where you can just basically punch a regular
[21:01] like terrain all without creating additional surface.
[21:08] And then to adjust the triangle density in some area,
[21:11] we have the remesh modifier.
[21:13] You can basically set the target edge line that you want for your triangles.
[21:18] It also has a smoothing option available.
[21:22] And this modifier can also do a test solution like we saw in the texture modifier.
[21:29] And in addition, it's also possible to basically use a weight channel
[21:34] to mask out the remesh operation and basically just operate the remesh
[21:39] on painted triangles, for instance.
[21:43] All right, so next one combining all these modifiers together.
[21:47] We can't need to control in which order we want to execute them.
[21:51] So if we look at the top image here,
[21:53] we have an island shape that is made with a spline modifier as a base.
[21:58] And then the road with a spline modifier again.
[22:00] And then a noise modifier on top.
[22:03] The noise is giving us the randomness that we want on our island,
[22:06] however it's breaking our road apart.
[22:09] So the order should be like at the bottom image here,
[22:12] where we first have the island shape, then the noise, and then the road on top.
[22:17] So we actually need a layering system to help us organize all that.
[22:21] So that brings us to the mesh partition definition.
[22:25] So this is basically a data asset with a mesh partition class
[22:30] that we will assign to our actor.
[22:32] And we use it to all the important information for the system.
[22:38] So here we'll be able to create and reorder the modifier layer priorities.
[22:43] So this is basically the layers that we're using to define the execution order
[22:48] of our modifiers, like in the previous example.
[22:51] And really we can see these as Photoshop layers,
[22:53] the modifiers being paint stroke on these layers,
[22:56] basically composing a final mesh or final mesh.
[23:03] Then the definition as a material section,
[23:05] that's where you're going to assign the material that you want to use
[23:08] on your mesh partition geometry.
[23:10] And then we have the weight channels that I mentioned a couple of times already.
[23:15] So here we're painting tree channels like a gravel mud and sand as a basic example.
[23:22] And that data can be painted manually,
[23:24] can be applied by a modifier or injected procedurally with PCG on the mesh.
[23:30] So here we're using a brush modifier.
[23:32] And right now these channels are used to apply a material effect,
[23:36] but they don't have to be used only for materials channels.
[23:39] It can be used by PCG to scatter some stuff
[23:43] or can be used as a mask for the tools.
[23:46] And we'll see example of that in a few minutes.
[23:49] So which channels are basically just like a flow attribute on the mesh
[23:54] and stored on vertices during iteration.
[23:57] But on the final mesh is going to be baked down into a texture
[24:01] and is going to bake basically one texture per mesh partition section.
[24:07] And then we have a channel textual size in the definition
[24:10] that we can use to basically control the resolution of that final texture.
[24:15] And then to finish the tool set to review here,
[24:20] we have the mesh partition outliner.
[24:23] It's basically one centralized place that allows you to see all the modifiers
[24:28] that are affecting a specific mesh partition.
[24:30] And so you'll see all your priority layers there,
[24:34] ordered button up like in Photoshop.
[24:36] You'll be able to see the execution time of each modifiers,
[24:40] the modifier type and the parent actor.
[24:43] And I will also bring your attention to the column with the line here,
[24:48] which is interesting.
[24:49] Basically setting the dot to a specific modifier
[24:52] will automatically disable all the modifiers that are above this one.
[24:57] It will basically build a mesh partition up to this specific point.
[25:02] And then the white line just makes it clear which ones are built
[25:05] and which ones are not.
[25:07] And then this is really convenient when working on a specific modifier
[25:11] and you only want to see your terrain up to this,
[25:15] the terrain result up to this certain point.
[25:20] All right, so that's it for the theoretical part.
[25:23] Now let's take a look concretely at how it is working with the tool set.
[25:28] First step for us would be to create our mesh partition actor.
[25:32] And we have a few options for that.
[25:33] One of them is to start from a flat rectangle,
[25:36] much like a flat idemap.
[25:39] Then we can also import a idemap directly.
[25:42] But this is still quite 2D thinking instead for demo or example.
[25:47] We'll try to build something more fun and 3D like this.
[25:51] So this concept art will be our target.
[25:54] It's 3D, it has overhangs and a lot of features that we couldn't do
[25:58] with a regular idemap.
[25:59] So that's going to make a good example.
[26:01] So all right, so to build this,
[26:04] we'll be using only four assets,
[26:07] three stats mesh and one texture.
[26:12] So what we'll do is start with one of our stats mesh that will place in the level
[26:15] and then convert it to mesh partition.
[26:18] So this step we can set on any base section,
[26:22] base mesh providers, basically,
[26:23] where that mesh will be split into.
[26:26] Actually, it could be just one,
[26:27] but here we're splitting into four by four sections.
[26:30] And this base stats mesh here is about 1 kilometer in size.
[26:34] So our section's going to be about 250 meters approximately.
[26:39] And once that's done, we would make sure to assign our mesh partition definition to it.
[26:46] So with our definition assign,
[26:48] we can now apply some base material on the mesh
[26:51] and we can make use of the brush modifier to do that,
[26:54] which can be used for sculpting, but also to simply paint that.
[26:57] So we're replacing two different modifiers,
[27:01] one that captures the old island to apply the rock material.
[27:04] And then I'll add a second one that captures just the top part to apply grass.
[27:10] And that's just to make things easier,
[27:11] like a single modifier could apply like several material, several weight channel,
[27:16] but that was just to make things more convenient.
[27:21] All right, so in this next step,
[27:23] we'll start shaping the rest of the island using Boolean modifiers.
[27:27] First, we'll set up one,
[27:28] we'll set the priority layer that we want to use,
[27:31] select the stats mesh,
[27:33] make sure the Boolean mode is the two union.
[27:36] But the thing is,
[27:37] we don't want to have to paint material on each of the Boolean portion that we're going to be adding.
[27:42] So to make things easier,
[27:43] we can actually use the stats mesh vertex color
[27:47] to automatically apply weight channels to the modifier.
[27:51] So here we have the red vertex color.
[27:53] We're going to use it to apply rock
[27:55] and we're going to use the green to apply grass.
[27:57] So that will take care of applying our material automatically for us.
[28:04] After that, we can just duplicate our modifier,
[28:07] swap the mesh and have fun shaping up our island like this.
[28:11] And again, an important note here,
[28:13] this is Boolean operation.
[28:15] So it's actually fusing the geometry together,
[28:18] not simply overlapping regular mesh and stenciling.
[28:22] So it's really creating one connected and continuous surface
[28:25] that will be able to exit further afterward.
[28:31] Then looking at our concept art again,
[28:33] it's a good start.
[28:35] Other islands in the back,
[28:38] using the same technique.
[28:39] And next step for us would be to add like that mountain peak in the back there.
[28:44] So let's do that.
[28:45] And we'll be using the texture modifier,
[28:48] using a regular itemap texture.
[28:50] We'll also reuse the grass channel,
[28:52] that is the grass material basically does already apply
[28:57] to basically use it as a mask for the eye displacement
[29:01] so that it's only like the grass part of the mesh that gets deformed.
[29:05] And we don't influence like the rock on the neat and on the side.
[29:10] And as you see, our input mesh resolution here was quite low.
[29:13] It was fine for a flat terrain,
[29:14] but we need a bit more here to shape our mountain nicely.
[29:17] So we're using a mesh, a remesh modifier.
[29:20] And we're going to make sure that this modifier is applied just before the
[29:24] mountain texture modifier.
[29:26] So we're using the same priority layer,
[29:28] but we're going to leave the sub priority to zero.
[29:31] We're going to tweak the remesh resolution a little bit.
[29:35] So now we have nice resolution.
[29:38] And then back to our mountain modifier, the texture modifier
[29:41] will just shift the sub priority to one.
[29:43] So that gets applied after the remesh.
[29:46] And as you might have guessed,
[29:47] the sub priority here is just to help us sort all the modifiers that
[29:51] might be on the same layer.
[29:54] And now we get our mountain slope.
[29:56] We'll add a second texture modifier using the same nightmare,
[29:59] but we'll slightly remap the values using a curve asset.
[30:04] And then in order to remove the grass on that peak and reveal the rock,
[30:08] that is already applied.
[30:10] Instead of writing it to the grass channel this time,
[30:13] it will basically just set up our things here to erase the grass value
[30:18] on the grasswood channel to reveal the rock on the need just like this.
[30:27] All right, so it's not identical,
[30:29] but I'm happy with that.
[30:31] I did some biomes on top of the mesh terrain.
[30:34] And next we can add more stuff just for fun and just to showcase
[30:38] other aspect of the tool.
[30:39] So using the Boolean in subtractive mode this time,
[30:44] we can punch all through that mountain peak.
[30:47] And as shown before, we can have it right into the rock weight channel
[30:51] to apply the rock material on the Boolean interior surface.
[30:55] And then to get rid of these sharp edges,
[30:59] we're going to be using the remesh again,
[31:02] but this time we're going to make use of this mooting option that it has
[31:06] to round up these corners.
[31:08] And then afterward, just as the final touch,
[31:10] we're using the noise modifier to break out their regular T here
[31:14] and have something that looks a bit more natural.
[31:17] We could also use the brush modifier to sculpt ourselves
[31:21] the specific result that we wanted.
[31:27] Next, placing asset on an even terrain can be quite annoying,
[31:31] but we can make use of our mootifiers to help us here.
[31:34] One thing to note is that all mesh terrain modifiers
[31:36] are actually components, so they can be added to any actors.
[31:40] So here, we're going to add a spline modifier to that P-O-I actor.
[31:47] We're going to set the affected mesh partition priority layer
[31:50] for all of the distance, and we all just have to adjust our spline
[31:53] around our asset.
[31:54] And once that's done, we just select the whole actor and move things around.
[31:58] We're going to be sure that the terrain will remain flat and set
[32:00] at the perfect, perfect eye for our specific P-O-I.
[32:05] So here, example, with a spline,
[32:08] but we could use a texture modifier.
[32:10] We could use a sculpt modifier if you have different eye.
[32:14] You want to set.
[32:15] And yeah.
[32:18] All right, next, let's take a look at how we can scatter modifiers
[32:21] with PCG and one requirement first would be to activate the PCG mesh partition
[32:28] interrupt plugin.
[32:30] And we'll start by using the brush modifier here to apply a new attribute
[32:35] weight channel on our mesh.
[32:36] Then within the PCG volume, the mesh partition query node that we have here
[32:42] will basically get all the geometry of the mesh terrain along with that attribute
[32:45] that we just painted.
[32:47] And then, at the output, the mesh projection instance spawner will be scattering
[32:52] modifiers using this specific static mesh with a random rotation.
[32:56] And mesh projection is basically just projecting the vertices onto that stack mesh.
[33:02] And that projection doesn't have to be perpendicular to the terrain.
[33:05] It can be in any angle.
[33:07] So we're going to give it like a 30 to 45 degree angle.
[33:12] And next, if we play Nidster here and look at what it looks from close up,
[33:20] we now have these basic but cool and gold rock formation
[33:24] with collision and everything ready to play.
[33:32] And then, weight channels that are already used for material can also be reused
[33:36] by PCG as well.
[33:38] So here, we already add that the grass material, but we can reuse that specific channel
[33:43] directly to spawn grass.
[33:45] So we're making use of the same data for two different purposes.
[33:48] So that's quite convenient.
[33:50] And then, to finish up my part, I have this small time lapse video of working with the tools.
[33:55] The modifiers are available, already opens up a lot of cool possibilities.
[34:00] And even more when combined with PCG and Blueprint.
[34:03] And as mentioned, a couple of times during the presentation,
[34:06] an important aspect of the tool set is the non-destructive workflow.
[34:10] And as proof of that, this whole sequence is actually me on building everything
[34:15] because I was a bit lazy, I didn't want to redo the whole thing.
[34:18] And playing the VDO backwards, it looks like I'm doing things up.
[34:22] So we can really go in and adjust everything at any given point.
[34:25] So it's truly non-destructive.
[34:27] And next, Michael, will give us more detail on how we can set everything up for the runtime for mesh partition.
[34:38] Thank you, Tian.
[34:39] One thing to highlight in those videos is no trickery.
[34:42] Like they are sped up a bit, but it's very clearly what's sped up.
[34:47] We're not like cutting pieces out.
[34:49] So all of the application of modifiers is actually pretty fast.
[34:53] I mean, you can get it to its knees by throwing crazy resolutions at it,
[34:57] but it's really like artists internally really like working with it.
[35:03] Okay.
[35:04] So tooling, workflows, building environments.
[35:08] Let's now kind of move over again a bit more to the runtime side of things.
[35:12] Again, bit more generically for mesh partition as well.
[35:17] I showed this diagram previously.
[35:19] And again, like very clear separation between source data and especially runtime data.
[35:26] And the important part to note again is that basically the source data and the intermediate data,
[35:30] this is where mesh partition is doing its thing.
[35:34] The runtime data, generic stuff that already exists.
[35:37] Nanat measures, normal static measures without nanite,
[35:41] or VT's, Lumen physics.
[35:44] We build no custom systems for runtime for mesh terrain.
[35:48] Everything is generic on that front.
[35:51] And this basically means that all the runtime stuff, it's hardened, it's optimized.
[35:56] We're not introducing new kind of dependencies and make things more complicated
[36:00] and effectively slower at runtime.
[36:05] Let's talk a little bit about how this is set up.
[36:09] It's broadly speaking split, I mean to three steps.
[36:12] The first one is you can define and we already shape a number of so-called transformers.
[36:17] The transformers describe how you take the result of the intermediate data
[36:22] and transform it into runtime data, any type of runtime representation.
[36:27] So a transformer generates nanat geometry, a transformer generates RVT in collision geometry,
[36:34] dedicated transformer for all of those different outputs.
[36:37] And then you aggregate those transformers into so-called transformer pipelines.
[36:42] And then those pipelines effectively get assigned to build variants.
[36:47] And build variants basically layout, okay, use this transformer pipeline
[36:51] with some additional settings and then generate runtime data.
[36:56] And then this runtime data that gets generated by the build variants,
[36:59] then gets packaged up for individual platforms.
[37:03] So you create one set of or multiple sets of build variants with runtime data
[37:08] and packaged them up depending on platforms in any way that you want.
[37:12] Let's walk through a little bit of an example to make it a bit more understandable.
[37:19] In this example, we basically have three transformer pipelines.
[37:24] One we called high end, four high end eventually, one low end and one common.
[37:29] And in the high end and the low end, they share one transformer.
[37:33] So they used us like how to integrate things well into build partition,
[37:36] aesthetic mesh transformer, how to generate the geometry for rendering.
[37:40] But even though those transformers are both used in high end and low end,
[37:44] they might have different settings individually, right?
[37:47] We configure things a bit differently for high end and for low end.
[37:50] And then high end also has RVT transformer.
[37:52] It has like additional splitting subsections to improve render performance
[37:57] and basically human data. That's what the far field transformer is.
[38:02] And then we have the common transformer pipeline.
[38:05] And this basically just generates the collision data uniformly for all platforms eventually.
[38:11] And then those transformer pipelines get assigned to build variant.
[38:15] There are some more settings in the build variant for how to generate the runtime data.
[38:20] And then eventually we take those build variants in the data generated from it
[38:24] and combine it in whatever way necessary for the runtime data that's platform specific.
[38:30] So we have one platform setting that combines high end plastic common data
[38:35] and one setting that combines the low end plastic common data.
[38:40] And then there are the existing kind of platform specific mechanisms in UE
[38:44] for how to then deploy to the different platforms.
[38:48] You might have spotted already in the last slide.
[38:50] There's also effectively a build variant for how to do preview and editor that you can modify.
[38:56] But yeah, there's obviously no platforms heading. It's just for editor.
[39:04] How to actually build runtime data?
[39:07] Important to note, we don't build runtime data at cook at least at the moment.
[39:13] You're going to trigger either the build of the mesh partition data manually via the editor
[39:19] or via a command let running on some build.
[39:24] Because effectively the mesh partition build generates artifacts that you probably want to check in.
[39:31] And that you want to version.
[39:33] And that also if other people are then want to load your giant level, they don't have to rebuild.
[39:40] They just pull it also from source control.
[39:43] And there's also some DDC support as well to make things faster overall.
[39:49] Or if you go into Pi, it gets triggered automatically to make sure that if you go into Pi like your geometry looks how it should look.
[39:57] And it is using the run-trime representation and it's performing as you expect.
[40:02] And all of this building is really done in a minimal way.
[40:06] So if things have been built before and you just made some changes in some area,
[40:11] we just recompute that area and everything else comes from a cache.
[40:16] Or yeah, from DDC or from checked in artifacts.
[40:23] You can also inspect the runtime data.
[40:26] So there is a filter, a number of filters in the outline of filter menu.
[40:31] For compiled sections, there's a space to lead the show build mesh partition sections.
[40:36] We might want to rename that.
[40:39] When you enable that, you see the compiled sections that you build for all of the build variants that you created.
[40:45] And you can then selectively load them via the right-click menu.
[40:50] And you can also, in the same outline of if those filters potentially like hide the preview sections or the base sections.
[40:58] In the end, they're just normal actors in your scene.
[41:05] So some of the details about the collision transformer that I mentioned in the previous slides.
[41:12] Landscape has really tiny collision data.
[41:15] Again, it's just a text show.
[41:18] It's fairly low resolution also in the kind of quantization.
[41:23] And if you move to chaos try mesh, your data is much, much bigger.
[41:27] Right? And this kind of example that I showed there before and after.
[41:30] If we would take a height map collision data and convert it over to chaos try mesh,
[41:36] it's like a factor of I think 59 more or less that this data inflates.
[41:43] But that's a bit of an apples to orange as comparison because when you use mesh partition, when you do what a 10 was doing,
[41:51] you don't just take the landscape data and convert it over.
[41:55] And if you then actually apply some mesh simplification based with like based on some very small arrow threshold that results like minimal hover.
[42:05] Or minimal clipping of characters feet or something, you really reduce this data by a huge amount.
[42:13] Like you usually cut about 90% of the data.
[42:17] Depending like your mileage may vary based on the environments, but like it's a huge difference.
[42:22] Just applying some fairly straightforward mesh simplification.
[42:25] And again, the collision transformer supports all of that already.
[42:30] Then we also realized that there was some inefficiencies in the chaos try mesh data.
[42:34] A lot of kind of 32 bit floating point bounding boxes. They were a bit redundant.
[42:40] We optimized that away as well, optionally.
[42:43] So if you apply those techniques, you plausibly can get into the same ballpark as landscape with your collision data.
[42:55] Another word about AVT, or VT and rate channels.
[42:59] So as H& Showed, you can paint attributes.
[43:03] You can have modifiers that apply attributes.
[43:06] They apply it per vertex in the editor.
[43:08] And then at one time they get converted over to textual or textual arrays actually.
[43:13] And what you can do with RVT is you can then instead of directly accessing those text series in your shader.
[43:20] On load, you can render to RVT.
[43:23] And then at render time use the RVT to simplify your whole material setup and make things faster overall.
[43:32] One important thing to notice that for landscape using RVT is trivial because you just have to zero to one UV space.
[43:40] And you just do top down orthographic projection for mesh terrain that's much more complicated because we have to do proper UV unwraps.
[43:47] We have to do proper 3D generalize projection of that.
[43:52] That's currently still working progress.
[43:54] Like we're very confident that it's going to land fairly soon, but it missed the 5.8 release.
[44:01] But this is an important kind of projection technique that we're going to support very soon.
[44:09] And just before wrapping up, briefly a few comments about runtime performance.
[44:15] Our extensive performance testing has shown that mesh terrain is on par with landscape or even better.
[44:23] And really on basically all the platforms.
[44:26] We used actual live Fortnite data for that.
[44:30] And we kind of did a landscape to mesh terrain comparison, which is almost a bit unfair because we don't make use of any of the capabilities that mesh terrain gives you.
[44:39] We just take the landscape data and convert it over even though like the same regular grid structure of the triangle supplies, etc.
[44:46] Which is arguably wasteful.
[44:48] But basically just having more control over streaming and LODs.
[44:55] And then just using again just high performing triangle mesh as a render time gives you better render performance.
[45:03] And again, because of better LODs and better streaming and cache management that we have with those generic systems, we end up using less memory.
[45:14] One caveat though.
[45:15] Landscape is really, really good in being predictable because you have a uniform resolution.
[45:21] With landscape artists can create whatever they want.
[45:24] And they can go crazy and you certainly still need to pay attention to what content you create.
[45:30] And you need to optimize your content still.
[45:33] That's not really going away entirely.
[45:37] Okay, let's wrap this up.
[45:41] Mesh terrain is available as experimental in 58.
[45:45] And like we know that mesh terrain is the future for Epic and for Unreal for terrain authoring.
[45:52] But right now it's experimental.
[45:54] So please don't message me in six months that maybe in a 5.9 release your 5.8 experimental mesh terrain stuff isn't working anymore.
[46:05] Right now we're working heavily on internal adoption.
[46:09] So if things go all very well, we will be shipping some actual production content fairly soon.
[46:15] Having said that it's a very gradual process with the kind of projects that we have.
[46:20] So ideally if all things go well, nobody will even notice that things ship with mesh terrain.
[46:26] And then over time we will make more and more use of the actual capabilities that it provides.
[46:31] And this internal adoption will hopefully get us to production ready, which we're currently aiming for for late 2027.
[46:39] We'll see how this is going to really align the future releases.
[46:43] But again, all development is happening on GitHub or out in the open source available on GitHub.
[46:50] Check out the documentation.
[46:52] Give it a try. Let us know what doesn't work.
[46:56] Even what you might like.
[47:00] And yeah, before ending our talk, I want to give a big thank you to the people who are actually doing all of the work.
[47:07] Who have been contributing a lot of hard work, ideas to mesh terrain over the last couple of years.
[47:14] And to really be the people who made this vision for next generation terrain system in Unreal A Reality.
[47:22] And yeah, this concludes our talk.
[47:24] Thanks, everyone.
[47:25] Thank you.



---

## Captured Frames

- [1:33] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_000.jpg
- [9:42] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_001.jpg
- [19:20] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_002.jpg
- [22:12] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_003.jpg
- [24:23] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_004.jpg
- [27:04] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_005.jpg
- [30:44] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_006.jpg
- [36:42] tutorials/frames/introducing-mesh-terrain-craft-large-complex-worlds-unreal-fest-chicago-2026/frame_007.jpg

---

## Structured Notes

### Core Technique
Official Epic deep-dive into **Mesh Terrain** (experimental in UE 5.8): a true triangle-mesh terrain system built on the generic **Mesh Partition** stack — non-destructive modifiers over streamed base sections, compiled per-platform via transformer pipelines into standard runtime systems (Nanite, RVT, Chaos, Lumen).

### Summary
Michael Balzer (engineering director) and Etienne Carrier (senior TA) present the motivation (heightmap limits: normal-only displacement, no overhangs/tunnels, uniform grid resolution, jagged diagonals, ~8K landscape limit, proxy file contention), why not voxels ("3D heightmap" with the same grid limits; would still need triangle conversion), and the architecture: **Mesh Partition** = authoring/managing meshes across streaming cell boundaries (arbitrary "sections", partial load/edit, holistic processing without seams; also works for e.g. a city-sized spaceship). **Mesh Terrain** = the terrain toolset on top (Shift+6 mode). Modifiers (all non-destructive components attachable to any actor): Mesh (project verts onto static/dynamic mesh), Texture (displacement + auto-tessellation), Spline (open/closed, any direction), Brush (sublayers; paints weight channels too), Boolean (union/subtract/trim, true geometry fusion), Remesh (target edge length, smoothing, weight-channel masked), Noise. Ordering via priority layers + sub-priorities in the **Mesh Partition Definition** data asset (Photoshop-layer mental model), inspected in the **Mesh Terrain Outliner** (execution times, build-up-to-here dot). Weight channels (gravel/mud/sand…) live per-vertex during editing, bake to one texture per section, and drive materials, PCG scattering, and tool masks. Runtime: source → intermediate (background async preview builds) → runtime data via **Transformer Pipelines → Build Variants → Platform Settings** (e.g. Nanite for high-end, static-mesh LODs for mobile/Switch, shared collision pipeline). Collision via simplified Chaos tri-mesh (~90% reduction, near-landscape sizes). Perf testing on live Fortnite data: on par with or better than landscape, less memory. Builds are manual/commandlet (artifacts checked into source control, DDC-supported), auto-triggered on PIE. RVT projection for mesh terrain (3D UV unwrap) missed 5.8, landing soon. Development in the open on GitHub.

### Key Steps
1. Enable Mesh Terrain mode (**Shift+6**). Regular modeling tools work on the base mesh but bypass the non-destructive modifier stack.
2. Create the actor: from a flat rectangle, an imported heightmap, or **convert a static mesh to Mesh Partition** (demo: 1 km mesh split 4×4 → ~250 m sections); assign a **Mesh Partition Definition** (priority layers, material sections, weight channels + channel texture size).
3. Paint base materials with Brush modifiers writing weight channels (rock all-over; grass on top).
4. Shape with **Boolean union** modifiers; use the source static mesh's **vertex colors** to auto-apply weight channels (red→rock, green→grass); duplicate modifier + swap mesh to iterate. Booleans fuse into one continuous surface.
5. Mountain: **Texture modifier** (heightmap) masked by the grass weight channel so only grass deforms; put a **Remesh modifier** on the same layer at sub-priority 0 and the texture at sub-priority 1 (remesh first); second texture modifier remapped by a curve asset *erases* the grass channel on the peak to reveal rock.
6. Tunnel: **Boolean subtract** writing the rock channel onto interior faces → Remesh with smoothing to round edges → Noise modifier to naturalize.
7. Flatten terrain under POIs: modifiers are components — add a **Spline modifier** to the POI actor (falloff distance set), then move the whole actor and the terrain follows.
8. PCG: enable the **PCG Mesh Partition Interop** plugin; paint an attribute channel; `Mesh Partition Query` node reads geometry+attributes; **Mesh Projection Instance Spawner** scatters projection modifiers (any projection angle, e.g. 30–45°) — rock formations with collision; reuse material weight channels (grass) to spawn grass.
9. Runtime setup: define **Transformers** (Nanite geometry, RVT, collision, far-field) → group into **Transformer Pipelines** (high-end / low-end / common) → assign to **Build Variants** → combine per **Platform Settings**. Editor preview is its own build variant.
10. Build manually in-editor or via commandlet; check artifacts into source control; DDC accelerates; PIE triggers a minimal incremental build. Inspect compiled sections via outliner filters ("Show Built Mesh Partition Sections"), selectively load via right-click.

### UE Systems / Blueprints / Settings
- Mesh Partition: sections (arbitrary triangle subdivisions), partial load/edit, dependency-graph build with caching/parallelization
- Modifiers: Mesh / Texture (auto-tessellation) / Spline / Brush (sublayers) / Noise / Boolean (union-subtract-trim) / Remesh (edge length, smoothing, masked) — all components, all non-destructive
- Mesh Partition Definition data asset: priority layers + sub-priorities, material sections, weight channels (per-vertex → baked texture per section)
- Mesh Terrain Outliner: layer stack, per-modifier execution time, build-up-to-here dot
- Transformer Pipelines → Build Variants → Platform Settings; Nanite / static-mesh LOD / RVT / Chaos tri-mesh (simplified ~90%) / Lumen — all generic runtime systems, nothing bespoke
- PCG Mesh Partition Interop plugin: Mesh Partition Query, Mesh Projection Instance Spawner
- Status: experimental 5.8, no back-compat promises, production target late 2027, source on GitHub

### Difficulty
Advanced

### UE Version
UE 5.8 (experimental)

### Tags
#landscape #nanite #pcg #worldbuilding #open-world #performance #advanced

---

## Related Entries
- [Unreal Engine 5.8 Mesh Terrain — Full Deep Dive](unreal-engine-58-mesh-terrain-full-deep-dive.md) — hands-on coaching-call walkthrough of the same system; this talk is the official architecture view
- Unreal Engine 5.8 Release Notes (Epic Documentation) — see INDEX.md for the 5.8 feature context
