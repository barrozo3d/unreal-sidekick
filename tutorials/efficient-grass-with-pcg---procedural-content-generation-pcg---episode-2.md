---
title: Efficient Grass With PCG - Procedural Content Generation (PCG) - Episode 2
source: YouTube
url: https://www.youtube.com/watch?v=jL8-C2VvpxY
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, blueprint, materials, pipeline, intermediate, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/
frame_count: 16
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Efficient Grass With PCG - Procedural Content Generation (PCG) - Episode 2

**Source:** [YouTube](https://www.youtube.com/watch?v=jL8-C2VvpxY)
**Author:** Ben Cloward
**Duration:** 42m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to make efficient grass with Unreal's PCG.
[0:06] Let's go!
[0:12] Alright, so this is the grass system that I've designed using PCG,
[0:16] and I'm going to show you how to make it today.
[0:20] But before we do that, there's something really important for you to understand
[0:25] about the way that PCG works.
[0:28] So, let's take a look.
[0:30] PCG has two different styles of spawning points.
[0:34] And last week, we talked about how the main job of PCG is to generate points
[0:41] and then add meshes to those points.
[0:44] So, these two different styles are...
[0:46] Well, the one that we looked at last week was offline static point generation
[0:52] that happens on the CPU.
[0:55] And this is for cases where you want to spawn hundreds or maybe even thousands of points.
[1:02] And these points are generated offline.
[1:05] So, you can generate them in the editor, but then once you're running the game,
[1:09] those points are always there and they're static.
[1:13] And you spawn them within boundaries.
[1:16] So, you lay down a volume or you lay down a spline as a boundary or something like that.
[1:22] And the points always stay in those boundaries.
[1:25] Now, the other type of point spawning, and this is what we're going to look at today,
[1:30] is spawning points at runtime on the GPU.
[1:35] And this style of point spawning is for when you have millions of objects that you want to place.
[1:43] The points get generated in real time during the game and they're spawned around the player.
[1:50] So, as the player moves, the points behind them are removed and the points...
[1:55] And additional points in front of them are added.
[1:59] And these points are spawned in grid tiles.
[2:02] So, the whole world is broken up into these little tiles,
[2:06] and each tile has a specific amount of points spawned in them.
[2:10] So, you can see these are two very different ways of going about the job.
[2:16] So, for things like large rocks and trees,
[2:21] you probably want to use the static spawning.
[2:25] But for things like grass, like we're going to look at today,
[2:29] you want to use the runtime point spawning.
[2:33] Alright, let's jump into the editor and take a look at how it works.
[2:37] Alright, here we are in Unreal and we're going to go ahead and create our grass spawning system.
[2:43] Now, I just want to preface this by saying,
[2:45] I've never seen an engine give you this much control over the way that your grass spawning works.
[2:53] Normally, the grass spawning system is something that's built into the engine,
[2:59] and you can't really change it without actually changing the engine source code.
[3:05] But Epic has created this system in Unreal that is super flexible.
[3:10] And I'm going to be showing you that today.
[3:12] So, let's come down here to the content drawer.
[3:16] And we're going to come to our PCG folder and I'll just right click in here
[3:20] and go to PCG and pick PCG Graph.
[3:24] And this is going to bring up the template browser.
[3:28] And the nice thing about the system that we're going to be creating today
[3:31] is that they've created a nice template for us.
[3:34] So, we're going to be using TPL showcase runtime grass GPU.
[3:39] So, I'm going to select that one and pick initialize from template.
[3:43] And what this is going to do is it's going to give us a head start
[3:47] on the graph that we're going to use.
[3:49] We're going to alter this graph a little bit as we go along.
[3:53] But this is a really nice place to start.
[3:55] So, I'm just going to type, I'm just going to name it PCG grass and hit enter.
[4:03] And let's go ahead and jump into this graph
[4:06] and we'll take a look at what's going on here.
[4:09] Let me just give us a little bit more space here in the viewport.
[4:13] So, this is our graph and we're just going to kind of take a look at these nodes
[4:18] starting over here on the left.
[4:21] The first thing that we have is a get landscape data node.
[4:25] And what this node does is it finds the landscape in our level
[4:30] and then collects information about that landscape
[4:33] that we can then use later in the graph.
[4:36] So, that's what's happening here.
[4:37] We're passing our landscape data out and we're passing it to a change grid side
[4:44] change grid size node.
[4:46] And what this node is doing is it's controlling the grid.
[4:52] I mentioned earlier that our dynamic points are going to get spawned on the grid.
[4:59] And this is the node that controls the size of that grid.
[5:03] Okay, the next thing that we do is we pass that grid size into this point generator node.
[5:10] And this node is, it's amazing.
[5:13] It's a custom node that's created from HLSL
[5:18] and it's run as a compute shader on the GPU.
[5:22] You can see there's this little tag down here that says GPU.
[5:26] And that means that whatever is happening inside this node
[5:30] is being done in a compute shader and it's happening on the GPU.
[5:35] And then we pass the points that get generated here to our static mesh spanner.
[5:41] And this is where the mesh gets spawned.
[5:43] And you can see that this node is also set to GPU.
[5:47] If we scroll our details down to the bottom,
[5:51] you can see here execute on GPU is checked,
[5:55] which means that these meshes are going to be spawned by the GPU and not the CPU.
[6:02] Now, one really important thing to know about PCG graphs
[6:06] is that if you have nodes that say GPU like this,
[6:11] you should probably stick with the GPU from that point on.
[6:16] So these nodes over here don't say GPU.
[6:19] But then once we get to here, our nodes say GPU,
[6:23] which means we probably should not insert another node here
[6:28] that's happening on the CPU and then jump back to the GPU.
[6:32] And the reason for that is that going round trip from the CPU to the GPU
[6:38] and back takes a lot of time to send data to the GPU
[6:43] and then back to the CPU.
[6:44] So once we have a node that says GPU like this,
[6:48] you want to stick with the GPU and not switch to the CPU for performance.
[6:54] OK, so this node is generating our points on the GPU.
[6:59] And then we're spawning our static meshes here.
[7:03] And we have one more node over here.
[7:04] It's called get graph parameter.
[7:07] And this node is bringing in a whole bunch of parameters
[7:10] that we need to control the behavior of the points that we're generating.
[7:15] Down here in the bottom, you can see our graph parameters.
[7:19] And here's all the parameters that were already set up for us in this template.
[7:24] And they control the behavior of the point spawning.
[7:28] And so they're getting passed into our point generator.
[7:32] OK, I think that's all we need to know about our PCG graph for now.
[7:39] Let's go ahead and save it.
[7:41] We'll switch back to our landscape.
[7:43] And I'm just going to grab our PCG graph and drop it in.
[7:47] And now you can see right away, we have a whole bunch of points that have been spawned.
[7:54] And you can see that there's this boundary and they're all getting spawned
[8:00] kind of inside that box.
[8:02] So the first thing that I'm going to do is I'm just going to take that box
[8:06] and put it at the origin so that we have it kind of centered on our terrain.
[8:14] And and there we go.
[8:16] So we're creating a whole bunch of points.
[8:19] Now, the thing to know about this this object that we've added to our terrain
[8:24] here is that it is not yet creating points at runtime.
[8:30] Right now, the method that it's using is static.
[8:35] It's using static point generation.
[8:37] And the reason that it's doing that is there is an opportunity
[8:42] for us to shoot ourselves in the foot and accidentally spawn
[8:46] too many points and run ourselves out of memory and crash the editor.
[8:52] And so what we've done is this object here is static.
[8:59] And then we need to kind of enable a bunch of settings in the right order
[9:04] so that we can make sure that we're not spawning too many points all at once
[9:10] and crashing our editor.
[9:11] So that's what we're going to do next.
[9:13] We're going to kind of turn on things just a little bit at a time
[9:17] so that we can get this system set up.
[9:19] So like I said, this system currently is statically spawning these points.
[9:26] I can move the box around and you can see like, OK, now I'm spawning points over here.
[9:31] Now I'm spawning points over here.
[9:35] And what we need to do.
[9:36] So the other thing to know is that the box that the points are being
[9:42] spawned in is relatively small.
[9:46] And you might think, well, I want the grass to be all over my level.
[9:50] So I need to just scale up that box.
[9:53] And I can do that.
[9:54] I can type in like 140 and 140.
[9:58] And what it's done is it's made the box like the size of my whole terrain
[10:03] and it's spread out these points.
[10:04] But now because I've made it huge, if I go in now and start setting things up,
[10:11] I'm going to spawn a million points all at once.
[10:15] And it's going to kind of destroy my performance.
[10:18] And so I'm going to undo my box size.
[10:20] We need to leave it kind of this small 25 by 25 for now.
[10:26] And then in just a minute after we get the setting set, we'll we'll scale it up.
[10:32] All right.
[10:33] So what we need to do is set up our mesh spawning system to instead of statically
[10:41] spawning points within this volume, we want it to we want it to divide our
[10:47] space into grid tiles and then spawn points for each tile.
[10:54] And so that's what we're going to do.
[10:57] And so we we're going to select our PCG grass here and come down here
[11:02] to our settings.
[11:05] And we're going to find our graph instance here.
[11:07] These are the parameters that we just looked at a minute ago.
[11:11] And we're going to turn on is partitioned.
[11:14] And what that's going to do is, well, first of all, it just added a whole
[11:19] ton more meshes.
[11:21] And the reason that that happened is because previously we were spawning
[11:26] these meshes in the entire box, a certain number of meshes in the entire
[11:32] box. And what we've done now by turning on is partitioned is we've split up
[11:37] our space into little tiles.
[11:40] And each one of those tiles is getting that number of meshes or that number
[11:45] of points spawned.
[11:47] Whereas before the entire box was getting those points.
[11:50] Now each individual tile is getting those points.
[11:55] Okay.
[11:56] Now the other thing that we need to do is change when our points get generated.
[12:01] So right now we have our generation trigger value set to generate on load.
[12:07] And that means when our level is loaded, all of these points get generated.
[12:12] But what we need to do is switch this from generate on load to generate at runtime.
[12:19] And that means when we play the game, our points are going to get generated then.
[12:26] Now, obviously right now we're not in the game.
[12:29] We're not playing it.
[12:30] And so our points went away because they're trigger.
[12:33] The thing that makes them spawn has changed and they only spawn when we're in the
[12:39] game. Okay.
[12:41] So if I hit play here and we entered the game, now you can see our points are
[12:46] getting generated.
[12:49] By the way, if in your level you want to be able to use a third person view and
[12:54] run around and see what's happening like that.
[12:57] The way that you can do that is come here under the content drawer, click the add button
[13:02] and then select add feature or content pack.
[13:06] And now we want to add our third person contact content pack.
[13:11] I've already done this.
[13:12] So I'm not going to click the add button, but in your level, you can add the third
[13:15] person content pack right there.
[13:19] And then you can come over here to world settings and set your game mode override
[13:24] to BP third person game mode.
[13:29] And that will allow you to jump in and run around with the third person
[13:34] character like this.
[13:37] Okay.
[13:38] So we've got our points, uh, spawning at runtime.
[13:44] Now, the next thing that we need to do is, uh, now that we have our, our points
[13:49] partitioned into tiles and we've set our trigger to, uh, spawn the points at runtime.
[13:57] Now we can take our, uh, box and we can, and we can, um, scale it up.
[14:05] So I'm going to set my scale to 140 by 140 by 60.
[14:13] I don't think that the, uh, Z matters much.
[14:17] Um, but what you can see now is we've got our box set to the size of our entire terrain.
[14:25] Okay.
[14:25] But we can't actually see our points.
[14:28] And if we want to be able to see what things look like in the editor, uh, we need to fix that.
[14:33] So I'm going to come here to my PCG world actor zero and scroll down here to treat
[14:40] editor viewport as generation source.
[14:43] So when I'm in the game, the game camera is the generation source, but when I'm in the editor,
[14:49] if I turn on this option, now wherever the editor camera is, is going to be where the points
[14:57] generate.
[14:58] And you can see as I'm moving forward, um, the tiles are, uh, slowly popping in and out.
[15:06] And you can see these chunks or tiles load in, uh, as a grid.
[15:11] Remember when we turned on, uh, is partitioned, we turned on is partitioned here and that
[15:19] breaks up our points, uh, into these little grid tiles or squares.
[15:27] And then as we move around, the points are spawning in those squares at runtime.
[15:35] All right.
[15:35] So we're making really good progress.
[15:38] By the way, what we're going to do is set this system up technically first, uh, and then a
[15:44] little bit later, we're going to make it beautiful.
[15:46] Right now it's just spawning these like temporary stand in meshes, uh, and it looks kind of ugly.
[15:53] I know we haven't got to the pretty part yet.
[15:57] But what we want to do is get this system set up and running efficiently.
[16:02] And then we're going to swap out these little temporary meshes, uh, with something that looks
[16:06] a lot nicer.
[16:09] Okay.
[16:09] The next thing that we want to do is control the distance that our points are spawning at.
[16:15] So you can see like as I move forward, new chunks spawn in in the distance.
[16:21] And there's a couple of different things that we can use to control how far away the points are
[16:27] spawning.
[16:28] Uh, first of all, we want to control where the tiles are spawning and how big the tiles are.
[16:36] And then within those tiles, we want to control the distance where individual points spawn.
[16:42] So let's go ahead and take a look.
[16:43] We have those three different things we can control.
[16:46] We can control the size of the tiles, how far away the tiles spawn in, and then within the tiles,
[16:54] how far away the points themselves are spawning.
[16:58] So first let's look at tile size.
[17:00] Uh, let's switch back to our PCG graph here and our tile size is controlled here by the
[17:08] change grid size node.
[17:11] So if I select that, you can see there's this high gen grid size and I can drop this down
[17:16] and I have a whole bunch of preset grid sizes for how big those tiles are.
[17:23] So if I change my grid size to 800, for example, I'm going to save that graph
[17:30] and switch back to our landscape.
[17:32] Now you'll see, I'm just going to kind of zoom out here so we can kind of clear everything out.
[17:41] Now you can see when my my tiles are spawning in, the grid size or the tiles are about half
[17:49] the size they used to be.
[17:51] So I can control the the size of the tiles.
[17:54] Now there is a little bit of a disadvantage to making the tiles smaller and that is the
[18:01] engine has to store more of the tiles and so it takes a little bit more memory for smaller
[18:08] tiles.
[18:09] So if I set my tile size to 800, now I'm having the engine manage more tiles and that may be a
[18:17] little bit more of a cost for the engine.
[18:20] And so what I'm going to do is just go ahead and set my tile size to 1600 as it was before.
[18:30] Okay, now the next thing that we want to look at that was the size of the tiles.
[18:35] But what we want to look at next is how far away those tiles are spawned.
[18:41] So if we switch over here to our graph settings, we can scroll down here to the bottom
[18:47] to runtime generation, generation radii.
[18:51] And if we take a look at this list, we can see for each of those different grid sizes,
[18:57] there's a distance where the tiles start spawning.
[19:01] So we're using a distance of 1600 right now and it shows that the 1600 size tiles start
[19:10] spawning in at a distance of 3200.
[19:14] And I think that distance works pretty well and so we're going to leave that as it is.
[19:19] But I wanted you to know where the controls are.
[19:21] So this, our grid here allows us to pick how big we want the tiles to be.
[19:28] And then in our graph settings, we can choose how far away we want those tiles to spawn.
[19:38] So if we want more grass further into the distance, we can turn up these values.
[19:43] You can see that there's a value here for each size of tile.
[19:49] Okay, now the third control that we have, so we can control the size of the tiles,
[19:53] the distance where the tiles spawn in, and we can also control the distance where individual
[20:01] points are spawned. And that is done in the static mesh spawner.
[20:07] So if we come into our static mesh spawner, you can see that I have two entries here,
[20:13] two array elements under mesh entries. And if I open these up and we open up mesh entries,
[20:22] index zero descriptor, I can scroll this list down and there's just like a huge number of
[20:29] parameters that we can control for how these meshes are spawned on the points.
[20:36] But what we want to find is a value called and it just keeps going, wow.
[20:43] I'm just gonna, I'm just gonna type in a call. And so here under descriptor, you can see that we
[20:50] have a start call distance and an end call distance. And this allows us to, for each individual mesh,
[20:59] we can control how far away that mesh is spawned. So right now, you can see that as we move back,
[21:08] our meshes are popping out in these chunks. But if I set the call distances to be something
[21:16] that's closer to the camera than where those chunks spawn, we can kind of smooth it out.
[21:22] Right now, we have kind of a jagged edge for those tiles. But if we come over here and type
[21:32] something smaller than 3200, we can kind of get them to, to spawn, to, to pop out in a little bit
[21:41] more elegant way. So let's set this to maybe 2900. And that's for the first one. And then for the
[21:49] second one, 2900 as well. And we'll save this and switch back. And now let's see. Ah, now you can
[21:57] see as I move around, instead of popping out in chunks, we have kind of a hard line or a circle
[22:06] around the camera where those meshes are de-spawning. Okay, I think that we've gotten ourselves to a
[22:16] point where we're ready to actually use real meshes. You know, like I said, we're, we're kind
[22:21] of using these ugly looking stand ins right now. But let's go ahead and grab some real grass meshes
[22:30] and throw them into our static mesh spawner node and see if we can improve the visual quality here.
[22:37] Before we start using real meshes, I want to pick our point generator. And instead of
[22:47] spawning the current number of points, let's see, it says it's spawning 262,144 points.
[22:57] And that is a lot. And so what I'm going to do instead is I'm going to reduce this to
[23:05] 3,500 points. And that'll make our grass more efficient. If we're spawning 200,000
[23:11] clumps of grass, that's just going to be way too many. Alright, so let's switch to our static mesh
[23:17] spawner. I'll come here under mesh entries, and I'm just going to hit this trash can icon to get
[23:23] rid of those temporary ones that we were using before. And I'm going to hit the plus button here
[23:29] so that we can add some of our own. So after hitting the plus, I'm going to open up descriptor.
[23:35] And now I can come down here to static mesh. And I'm just going to type grass. Now the the grass
[23:43] static meshes that I've found to use, I'm not particularly married to these, they're not
[23:49] amazing. And so I think I got these from fab, but you're welcome to get your grass meshes
[23:56] from wherever you want. This isn't really a tutorial about grass meshes themselves,
[24:01] but how to set up PCG as a system to spawn the grass. So yeah, you can grab whatever grass
[24:07] meshes you want, and you can probably make some that are significantly better than these.
[24:13] So I'm just going to add grass clumps, this one here. And that's going to spawn it in.
[24:21] And I'm just going to go ahead and add all three of them. So there's the first one. I'll add the
[24:26] second one. And then I'll add a third one here.
[24:44] Okay, now the crazy thing about this static mesh spawner is there are so many settings. I showed
[24:51] you a minute ago, like I was just scrolling and scrolling and strolling. Once you open up this
[24:55] descriptor, this just goes for miles and miles and miles. And the one thing that's kind of bad
[25:02] about it is that there are a bunch of settings here that are not very efficient. So we need to
[25:08] turn these things off before we're ready to use it. Because the list of settings here is so long,
[25:14] it works best if we just type in some search terms. So first of all, we can disable shadows. So we'll
[25:21] just type shadow. And now you can see we can turn off cast shadow, cast dynamic shadow, cast static
[25:29] shadow, cast contact shadow, and also for shadow cache, invalidation behavior, instead of auto,
[25:39] we want to set this to static. And what that does is if the object is rendered into virtual
[25:45] shadow maps, and it's moving around like our graph does, because it has wind animation on it,
[25:53] we can just set this to static. And that'll tell it, hey, like, don't redraw the shadow
[25:59] cache just because our grass is moving a little bit. Okay, and then we can just go ahead and turn
[26:04] all these things off for all three of our meshes. One thing that I might want to do is we have three
[26:12] meshes. And if I just enable shadows on one of them, like maybe I'll just come up here to the top and
[26:18] turn on cast dynamic shadows on that one mesh, it'll still look like it's casting shadows, even
[26:25] though only one of the three are actually doing it. Okay, the other thing that we can do is if we type
[26:35] world position offset, we do want our grass to move around a little bit. But here's a setting that
[26:41] will allow us to disable our world position offset based on a distance. So the grass in the foreground
[26:49] will be moving in the wind, but then further away in the background, where we can't see it,
[26:55] the grass will stop. So maybe we'll just type something like 2000, so that the grass further off
[27:03] is not moving. Now, here's something interesting that we can do. We have three different meshes here.
[27:09] What if we gave different values to each of these, just to kind of dither it out a little bit so they
[27:15] stopped at different times? Maybe we'll do 1900, 1700, and 2000. We'll take a look and see how that
[27:23] looks. And then finally, my last search term here is going to be lighting. And we don't want our meshes
[27:32] to affect our indirect lighting or distance field lighting. So we can turn these off as well.
[27:39] Now, there may be other settings. Like I said, this list just goes on and on and on.
[27:44] And some of these other things you may find that if you turn them off, you get better performance.
[27:50] But this is something that I'm still learning and experimenting with as well. I just know that
[27:56] those particular settings will help. Okay, well, let's go ahead and save these changes that we made
[28:03] and come back here to our landscape and take a look at our results.
[28:08] All right, so we do have some grass meshes happening here, but these grass meshes are really small.
[28:15] And I think I know why that is. So let's go ahead and select our PCG grass here and come down here
[28:23] to the parameters that we can change. Here are parameter overrides. And there are some
[28:31] values in here that work really well for those temporary stand-in meshes, but they don't work
[28:37] well for the grass that I'm using. First of all, we have a setting here for point scale min and
[28:44] point scale max. I'm going to set the min to 0.5. And I'm going to set the max to 1.5.
[28:54] And then the other setting that we have here is this controlling for scale by density min and max.
[29:04] And what that's doing is there's a noise texture that's projected onto the terrain. And the brighter
[29:11] the noise is, what this is saying is the brighter that noise is, the larger we can scale our meshes.
[29:21] And so for these values, I'm going to use a min value of 0.7 and a maximum value of 1.5.
[29:36] And now you can see our grass was really limited by those settings. But now that we've fixed them,
[29:44] we get a lot more reasonable looking grass and we can actually see it now. So we had grass that
[29:50] was the correct size, but the settings here are just kind of scaling it down quite a bit.
[29:59] All right, now we want to play with this spatial noise. So what you can see here is our grass is
[30:06] kind of spawning in clumps. And if we don't want those clumps to be quite so large, we can change
[30:15] the strength of the spatial noise. So I think what I'm going to do is turn the spatial noise strength
[30:22] down to like 0.25. And that's going to allow us to have just like a little bit more
[30:30] grass in between our clumps. All right, I might play with these settings a little bit more.
[30:38] Let me go ahead and explain what these are doing. This first setting is controlling the density of
[30:45] the grass. A value of 1 will give us the full number of points that we asked for in each of the
[30:52] tiles. But if we turn this down, this is kind of like an overall density multiplier. So if we turn
[30:59] this down, we'll get fewer and fewer points. And so you can see that we can make our grass really
[31:07] sparse if we want to. In my case, I just want one. The next noise that we have is kind of a randomness
[31:14] filter. And I think that one's working fine. The next one that we have is the scale of the spatial
[31:22] noise. And what we're seeing here is kind of clumpiness. And if I turn this up to something like
[31:30] 800, it'll change the frequency of that noise. And then this is changing the strength of the noise.
[31:45] If we turn this down to 0, now you can see we've got almost full grass. And I think the only way
[31:52] to make the grass more full and get rid of the gaps in between here would be to give ourselves
[32:03] more points. I've limited it to 3,500. So we're not getting the full density of the grass here.
[32:13] But let's go ahead and turn our spatial noise strength up to like 0.25 again.
[32:19] Okay. And then we have density min and max scaling. And what this is doing is it's making the grass
[32:26] smaller where that noise is black and making it larger where the noise is white. And then we have
[32:33] seeds here, which just allow us to kind of scramble up the grass a little bit. Okay. I kind of like
[32:39] these settings. I think they're working pretty well. But let's see what happens when we zoom out.
[32:46] Zoom out and where the grass is kind of culling away. So what you might see here
[32:55] is that as we move further back, our grass is kind of spawning in. Yeah, if you look right here kind
[33:02] of on the edge of where the grass is, it spawns in in these chunks that pop out. And what we want
[33:11] to do is instead of popping out those chunks, we want to be able to have a nice clean zone where
[33:22] the grass fades away instead of popping out. And in order to do that, in order to get rid of these
[33:29] chunks popping, we need to go back to the node in our graph that is spawning our static meshes
[33:38] and set cull distances. And so what I'm going to do here is just search for cull. And it's going to
[33:45] give me two values for each of the grass meshes. I get a start cull distance and an end cull distance.
[33:54] So we're going to start out just with the end cull distances. I'm just going to make the start
[34:00] and the end match. So we're going to cull at 2700 for this first one. Again, I'm making these values
[34:08] different for each of them so that it kind of scatters it instead of having one hard line
[34:15] where all three of them clip out. I'm making three different values to kind of spread out where that
[34:24] where that culling is happening. And putting these values in here is actually making the points
[34:33] stop spawning the meshes at this distance. So let's go ahead and save it and we'll see what kind
[34:38] of a difference that made. Okay, now you can see the meshes used to be spawning out here,
[34:44] but now they're not. Now they're spawning a little bit closer to the camera, but instead of popping
[34:51] out, we can see them kind of pop out individually. And that's really nice because it's no longer
[34:59] giving us those kind of hard jagged edges on the edges of our tiles. And it's looking pretty good,
[35:08] but there is one more thing that we can do that makes this even better. And that is we can actually
[35:15] fade out the meshes so that instead of popping out like they are now, it's kind of obvious when
[35:21] they pop off there in the horizon. Instead of doing that, we can make them slowly fade so that
[35:29] that popping isn't quite as obvious. So let's go ahead and do that. We'll switch back to our static
[35:36] mesh spawner. And what we can do is lower this start cull distance value so that there's this
[35:44] zone. And in this case, we're going to type 2100. So between 2100 and 2700, we're going to be fading
[35:52] out. And so on this next one, we're going to do 2600 to 3100. And then finally on this last one,
[36:02] we'll do, oh, we're going to do 2100 to 2900. And you know, obviously these are values that you
[36:11] can play around with so that you can get just the right kind of blend between good performance and
[36:20] making it less obvious that you're making these meshes go away. All right, I'll go ahead and save
[36:25] that. And then we'll switch back here. And now what you see is that it's a lot less obvious
[36:33] that the meshes are popping out because we have a nice zone where they start to fade.
[36:39] Now, I will say one thing about this fading, it only works if you have the material that's set up on
[36:47] your mesh set up in a very specific way. So what I want to show you now is what you need to do in
[36:53] your mesh's material so that this fading out will work. If you type a lower value for the start cull
[37:01] distance and a higher value for the end cull distance, and your meshes are still popping,
[37:08] it's likely that you don't have your material set up right. So let's switch over to the material
[37:13] that I'm using on these on these grass static meshes and take a look at what's happening here.
[37:19] So this is the shader that comes with the Megascans assets. And the node that is important to have in
[37:31] here is called per instance fade amount. This is a very special node that brings in a value
[37:39] between black and white, depending on how far away the mesh is from the camera in between that
[37:48] minimum and maximum cull distance. So at the start cull distance, the mesh is going to be white.
[37:56] And then at the end cull distance, the mesh is going to be black. And so what we can do with this
[38:02] node is multiply it by our opacity value, and then pass the result of that into the temporal,
[38:10] into the dither temporal anti aliasing node, and then pass that into our opacity mask.
[38:17] And setting up our nodes in this configuration allows them to slowly fade out over the start
[38:26] cull distance to the end cull distance. And then like I said, you can tune these values
[38:34] so that these these grasses fade out slowly. And so it's less obvious that they're going away.
[38:44] All right, well, let's switch over to our our dummy character here and we can run around.
[38:51] And you can see that our grass is kind of slowly fading in at a distance. And it looks really nice.
[39:00] We can kind of turn around here and go the other way. And our grass is slowly fading in.
[39:08] Now, depending on what kind of a game you have and what your target hardware is,
[39:13] you'll need to tune these settings. You can change the size of your tiles.
[39:19] You can change the distance where the tiles draw. And you can change for each individual point,
[39:27] the start and end distance where that point is going to be culled. So there's a ton of control
[39:33] here for controlling how much grass you you spawn and and being able to control how it fades in and
[39:43] out so that the spawning isn't like a big pop. And so that you don't get those like ugly tile
[39:50] border seams where an entire tile pops in all at once. This is an amazing system. Now, I bet you're
[39:58] asking, I can see grass kind of spawning here in this dirt. And even like up here on the mountain
[40:05] cliffs, I can see grass spawning up here. Is there a way that I can mask out the grass
[40:13] by the grass material that I have on my landscape already?
[40:18] How can I control the grass that I'm spawning based on the material that's on the landscape?
[40:26] And the answer to the question is yes, you absolutely can. But that's what we're going to talk about
[40:33] next week. So we're going to talk about controlling where the grass spawns based on a bunch of
[40:39] different factors, including the landscape mask that you create in the landscape material itself.
[40:48] So I'm going to show you how to take a value that you've generated on the landscape material
[40:54] and pass it in so that you can use it in your PCG graph to control where these different
[41:03] assets spawn on the landscape. That's going to be a great tutorial. I hope you can wait
[41:09] for just a week. Next week, we're going to go over that. And it's going to be a good one. So
[41:14] be sure to come back for that one. Hope you enjoyed today's video. I really enjoyed putting it together.
[41:21] I really like this PCG system. It's quite powerful and also really flexible. And it's
[41:29] actually more efficient than what Epic had before. So not only are you getting a tool that's more
[41:35] flexible and controllable, but it's also performing better than what Epic had before
[41:42] for applying landscape grass. All right, have a great week, everybody, and we'll see you next time.



---

## Captured Frames

- [3:39] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_000.jpg
- [7:47] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_001.jpg
- [12:19] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_002.jpg
- [14:13] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_003.jpg
- [14:40] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_004.jpg
- [17:16] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_005.jpg
- [18:47] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_006.jpg
- [20:07] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_007.jpg
- [23:05] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_008.jpg
- [24:13] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_009.jpg
- [25:14] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_010.jpg
- [28:23] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_011.jpg
- [34:08] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_012.jpg
- [36:02] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_013.jpg
- [37:13] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_014.jpg
- [38:51] tutorials/frames/efficient-grass-with-pcg---procedural-content-generation-pcg---episode-2/frame_015.jpg

---

## Structured Notes

### Core Technique
Building a **runtime, GPU-driven PCG grass system** from Epic's `TPL_Showcase_RuntimeGrassGPU` template: points are generated and mesh-spawned entirely on the GPU in real time around the player (tile-streamed, not static/offline), then tuned for density, distance culling, and smooth material-based fade-out to avoid visible pop-in/pop-out.

### Summary
Second episode in Ben Cloward's PCG series, opening with a key conceptual distinction: PCG has two spawning styles — **offline/static CPU point generation** (Episode 1's approach; good for hundreds/thousands of large static objects like rocks and trees, bounded by a volume/spline) versus **runtime GPU point generation** (this episode; for millions of small objects like grass, streamed in/out around the player in grid tiles as they move). The bulk of the video is building a production-quality runtime grass system from Epic's GPU showcase template: understanding the template's GPU-tagged node chain, safely enabling runtime generation (to avoid crashing the editor by spawning too many points at once), controlling grass density/distance via three independent levers (tile size, tile spawn distance, per-point cull distance), swapping in real grass meshes with a long list of spawner-efficiency settings (shadows, world-position-offset falloff, indirect lighting), tuning parameter-overrides (point scale, density-based scale, spatial noise) for a natural non-uniform look, and finally eliminating visible "tile popping" at the render distance by combining per-mesh start/end cull distances with a `Per Instance Fade Amount` material node so grass fades out smoothly instead of hard-clipping. Ends by teasing next week's episode: masking grass spawn locations using a landscape material mask.

### Key Steps
1. **Create from template:** Content Drawer → PCG folder → right-click → PCG → PCG Graph → in the template browser pick **TPL_Showcase_RuntimeGrassGPU** → Initialize from Template (instead of Create Empty Graph as in Ep.1) → name it (e.g. "PCGGrass").
2. **Understand the template graph:** `Get Landscape Data` (finds the level's landscape, passes landscape data downstream) → `Change Grid Size` (controls the runtime streaming tile size, via a Grid Cell Volume-type parameter) → `Point Generator` (a custom **HLSL compute-shader node, tagged GPU** — generates points entirely on the GPU) → `Static Mesh Spawner` (also tagged **GPU**, with "Execute on GPU" checked in its Details panel — spawns meshes without CPU round-trip) → separately, a `Get Graph Parameter` node feeds a big set of exposed graph parameters into the Point Generator. **Rule of thumb: once a node chain says GPU, keep everything downstream on GPU** — bouncing back to a CPU node and back costs a lot of round-trip data-transfer time.
3. **Drop the graph into the level** and re-center its spawn-boundary box at the origin. At this point it's still using **static** point generation (deliberately, to prevent accidentally spawning too many points at once and crashing the editor) — box size stays small (e.g. 25×25) until the runtime settings are properly staged.
4. **Enable `Is Partitioned`** on the PCG component's graph-instance settings — splits the spawn volume into grid tiles, each independently getting the configured point count (instead of the whole box sharing one global point budget).
5. **Switch `Generation Trigger`** from **Generate on Load** to **Generate at Runtime** — points now only spawn during Play, not when the level loads in the editor.
6. (Optional, for testing) Add the **Third Person content pack** (Content Drawer → Add → Add Feature or Content Pack) and set World Settings → Game Mode Override to **BP Third Person Game Mode** to run around and see streaming live.
7. **Scale the spawn box up** to cover the whole terrain (e.g. 140×140×60 — Z doesn't matter much) now that Is Partitioned + runtime generation are both safely enabled.
8. To preview streaming in the **editor** (not just Play mode): on the PCG World Actor, enable **Treat Editor Viewport as Generation Source** — tiles then stream in/out around the editor camera instead of only the game camera.
9. **Control distance/density with three independent levers:** (a) **Tile size** — the `Change Grid Size` node's grid-size dropdown (e.g. 800 vs. 1600; smaller tiles = more granular streaming but more memory overhead for the engine to track); (b) **Tile spawn distance** — Graph Settings → Runtime Generation → Generation Radii, a per-grid-size list of distances at which tiles start generating (e.g. 1600-size tiles at a 3200 radius); (c) **Per-point cull distance** — in the `Static Mesh Spawner`'s Mesh Entries → each descriptor has **Start Cull Distance / End Cull Distance**, searchable via the settings search box (type "cull") since the descriptor has an enormous parameter list. Setting per-mesh cull distances slightly inside the tile-spawn radius (and varying them slightly per mesh) turns hard jagged tile-edge pop-in into a softer, staggered circular cull boundary around the camera.
10. **Reduce point count for real grass:** the template defaults to a huge number (262,144 points) meant for the stand-in preview cubes — drop this via the `Point Generator` node to something practical (e.g. 3,500) before swapping in real meshes.
11. **Add real grass meshes:** in `Static Mesh Spawner` → Mesh Entries, delete the temporary stand-ins (trash icon) and add real static meshes (e.g. 3 different grass-clump variants) via **+** → Descriptor → Static Mesh.
12. **Tune spawner efficiency settings** (the descriptor's parameter list is huge — use the search box): disable **Cast Shadow / Cast Dynamic Shadow / Cast Static Shadow / Cast Contact Shadow**, set **Shadow Cache Invalidation Behavior** to **Static** (prevents constant shadow-cache redraws from wind-animated foliage); set a **World Position Offset** distance-disable threshold (e.g. ~1900–2000, varied slightly per mesh) so wind sway stops once grass is far enough to not matter; disable contribution to **indirect/distance-field lighting**.
13. **Fix undersized grass** via the PCG component's **Parameter Overrides**: `Point Scale Min/Max` (e.g. 0.5–1.5) and a density-driven scale range, `Scale By Density Min/Max` (e.g. 0.7–1.5) — density here comes from a noise texture projected onto the terrain (brighter = larger scale).
14. **Tune clumping via spatial noise parameters:** an overall density multiplier (1 = full requested point count per tile, lower = sparser), a randomness filter, a **spatial noise scale** (frequency/size of clumps — higher = smaller, more frequent clumps), and a **spatial noise strength** (0 = uniform full coverage, higher = more pronounced clumping/gaps) — plus min/max density-scaling and per-point random seeds.
15. **Eliminate tile-edge popping (final polish):** set matching Start/End Cull Distance pairs per mesh close together at first (e.g. 2700/2700) to confirm hard culling works, then widen the gap between Start and End (e.g. 2100→2700, 2600→3100, 2100→2900, staggered per mesh) to create a fade zone instead of a hard cutoff.
16. **Wire the material for fading to actually work:** the mesh's material graph needs a **Per Instance Fade Amount** node (white at Start Cull Distance, black at End Cull Distance) multiplied into the opacity value, run through a **Dither Temporal AA** node, then into **Opacity Mask** — without this exact material setup, cull-distance fading has no visible effect and meshes will still hard-pop even with a wide Start/End gap.

### UE Systems / Blueprints / Settings
- **PCG Graph template:** `TPL_Showcase_RuntimeGrassGPU`.
- **Nodes:** `Get Landscape Data`, `Change Grid Size` (Grid Cell Volume / grid-size dropdown), `Point Generator` (custom HLSL/compute-shader node, GPU-tagged), `Static Mesh Spawner` (GPU-tagged, "Execute on GPU" toggle, Mesh Entries array with per-entry Start/End Cull Distance plus a very large descriptor parameter list searchable by keyword — shadow-*, world position offset, lighting, cull), `Get Graph Parameter`.
- **PCG Component / graph-instance settings:** `Is Partitioned` (splits volume into grid tiles), `Generation Trigger` (Generate on Load vs. Generate at Runtime), Parameter Overrides (Point Scale Min/Max, Scale By Density Min/Max, spatial noise density multiplier / randomness / scale / strength, seeds).
- **Graph Settings → Runtime Generation → Generation Radii:** per-grid-size list controlling spawn-in distance for tiles.
- **PCG World Actor setting:** `Treat Editor Viewport as Generation Source` (lets the editor camera drive streaming for in-editor preview).
- **Material graph node:** `Per Instance Fade Amount` → multiply into opacity → `Dither Temporal AA` → Opacity Mask (required for cull-distance fading to visually work; used on the Megascans grass material shown).
- **Project setup (optional, for live testing):** Third Person content pack, Game Mode Override = BP Third Person Game Mode.

### Difficulty
Intermediate/Advanced — assumes Episode 1's basic PCG concepts; introduces GPU compute-shader nodes, runtime streaming/partitioning safety concerns (editor-crash risk from over-spawning), and material-graph integration (Per Instance Fade Amount) alongside the PCG graph itself.

### UE Version
Not explicitly stated; continues directly from Episode 1's UE 5.7 "production ready" PCG baseline — GPU-based runtime point generation via `TPL_Showcase_RuntimeGrassGPU` is a 5.7-era template.

### Tags
pcg, blueprint, materials, pipeline, intermediate, advanced, ue5-7

---

## Related Entries
- `tutorials/introduction-to-procedural-content-generation-pcg---episode-1.md` — Episode 1 of this same series (Ben Cloward), establishes the static/CPU point-generation basics that this episode explicitly contrasts against runtime/GPU generation; shares tags: pcg, blueprint, pipeline.
- Next episode in this series (landscape grass masks, using a landscape-material-generated mask to control PCG spawn locations) is the direct continuation of the "next week" teaser at the end of this video — check for it under a title like "Using Landscape Grass Masks With PCG."
