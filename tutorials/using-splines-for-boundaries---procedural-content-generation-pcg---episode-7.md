---
title: Using Splines For Boundaries - Procedural Content Generation (PCG) - Episode 7
source: YouTube
url: https://www.youtube.com/watch?v=AWJ7H4C6ObI
author: Ben Cloward
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/using-splines-for-boundaries---procedural-content-generation-pcg---episode-7/
frame_count: 0
frame_status: pending-selection
---

# Using Splines For Boundaries - Procedural Content Generation (PCG) - Episode 7

**Source:** [YouTube](https://www.youtube.com/watch?v=AWJ7H4C6ObI)
**Author:** Ben Cloward
**Duration:** 19m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py using-splines-for-boundaries---procedural-content-generation-pcg---episode-7 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to use splines as boundaries in PCG.
[0:06] Let's go!
[0:13] Alright, so we're in the middle of a series of videos about using Unreal's PCG.
[0:20] So far in this series, we've used PCG to build this forest.
[0:26] I'll link the playlist to the whole series down in the description
[0:30] if you'd like to go back and watch the rest of the videos in this series.
[0:34] So today, I'm going to show you how to use splines.
[0:38] And there are a lot of things that you can do with splines in PCG,
[0:42] like creating roads and rivers or placing objects in a row like fences or streetlights.
[0:50] We may cover those things in a future video, but specifically today,
[0:55] I'm going to show you how to use them for boundaries to control where PCG assets are placed.
[1:03] In our first scenario, we're going to use splines to define the areas where we're placing our forest.
[1:11] Currently, we have our forest PCG volume,
[1:18] but it's just a big cube that surrounds our entire landscape.
[1:23] So we're basically getting forest everywhere.
[1:26] And if we want to have more control over exactly where we're placing the forest,
[1:31] well, we can use splines for that.
[1:34] So let me show you how that works.
[1:36] I'll deselect my forest volume.
[1:40] And just for now, so that I can see what I'm doing, I'm going to hide the forest
[1:45] so that I can see my train without the trees.
[1:49] And I'm going to come up here to this plus button and I'm going to pick basic actor.
[1:55] And we're just going to place a couple of actors on our landscape here.
[2:00] And the actors are going to contain the splines that we're creating.
[2:04] So now that I've got an actor, I can come up here to selection mode and pick PCG.
[2:11] And then I can pick draw spline surface.
[2:15] And that's going to allow me to create a spline that is like a circle.
[2:21] That's a closed loop.
[2:23] So then I can just click and drag.
[2:25] And now I'm defining my spline with these points.
[2:28] And I'm saying, hey, I'm going to want forest trees in this area.
[2:34] And when I'm happy with this, I can just click accept.
[2:38] Okay, now here's a key part.
[2:41] I need to come over here to my search, what the actor selected and type tag
[2:47] so that I can give this actor a tag.
[2:51] And a tag is a little piece of information that allows one element in Unreal Engine
[2:58] to communicate with another element.
[3:01] So what I'm going to do is tag each of my splines.
[3:05] And then in my PCG graph, I can tell my nodes to look for that tag
[3:10] so they know which splines I want to use.
[3:16] So I need to come down here to tags and hit the plus button.
[3:21] And in this case, the tag that I'm going to give it, and I can type any word that I want,
[3:26] which is used as a keyword here.
[3:27] So I can just, mine's going to be called forest because I want to spawn forest in these specific areas.
[3:38] All right, so I'm all set with that one.
[3:39] Let's do another one.
[3:40] I'm going to come up here, click the plus button, pick basic actor.
[3:46] And then I'm going to go into PCG mode, draw spline surface.
[3:50] And I'm going to create a spline up here in this area.
[3:56] And then I'll hit accept.
[3:58] And I'll add a tag here and call it forest.
[4:02] And I'm going to do this one more time.
[4:04] So I want to create a basic actor.
[4:08] I'll hit the draw spline surface button.
[4:11] And I'm going to define this area right here to be a forest.
[4:17] And I'll hit accept.
[4:19] I'll create a new tag and I'll call it forest.
[4:23] All right, so I've defined three actors, this one, this one and this one.
[4:29] And these are the spots where I'm saying, Hey, I want my PCG forest to show up in these specific areas.
[4:37] So now I need to edit my graph to use these specific areas because otherwise, like right now,
[4:45] my forest is just spawning everywhere on my terrain, basically everywhere inside this PCG forest box.
[4:55] So let's go ahead and open our PCG graph.
[4:59] Here's our graph and we created this in a couple of weeks ago in our tutorials.
[5:06] Again, I linked the playlist down in the description so you can see how this entire thing is set up.
[5:12] So the first thing that we need to do is create a new node in our graph that's called get spline data.
[5:21] So we just defined a couple of splines and now we need to bring that spline data into our graph.
[5:28] So there's our get spline data node and we need to set a couple of settings here.
[5:33] So right now it's set to self and we want to drop this down and pick all world actors.
[5:40] So it's going to look at all of the actors to determine, Hey, do you have a spline that I want to use?
[5:46] And the way that it's going to figure out if it's if this actor is one that it wants is by the tag.
[5:52] So it's set to actor selection by tag.
[5:57] And now I can type forest here.
[6:00] So it's only going to get the splines that I created with the forest keyword in them.
[6:06] And I also want to check select multiple so that it will pick all of the splines in the actors that have that forest tag.
[6:16] All right.
[6:16] Now the next thing that I want to do is create another new node called create surface from spline.
[6:25] And I can plug my get spline data into my create surface from spline node.
[6:30] And it's going to add this other node here in between, which is translating my data.
[6:36] If I look at this data coming out of my get spline data node, the type is set to polyline.
[6:44] And what this wants is a spline.
[6:46] I'm not sure why spline data doesn't come out of here directly, but this node here in between is translated.
[6:54] And we're translating our polyline type into a spline type so I can connect it to the create surface from spline node.
[7:03] All right.
[7:04] So now what I've done is basically I've created a surface and I can plug it into my graph.
[7:10] So to understand what's going on here, we need to I need to explain this a little bit.
[7:16] Two weeks ago, I showed you how to do this.
[7:19] But let me just kind of break it down a little bit here.
[7:22] So we're bringing in our landscape and creating a surface sampler.
[7:27] And then we're creating some points that are seeds that show where we want to grow our forest.
[7:35] And then here we're creating forest in those areas and projecting it into a specific spot on our landscape.
[7:45] So what we want to do is define our projection target here.
[7:51] Right now we're defining our projection target as our landscape.
[7:57] So our get landscape data here is plugged into our check projection target.
[8:02] And what we want to do in this case is instead of projecting directly onto our landscape, we want to project into the areas that are defined by the interior of our splines.
[8:15] And so this create surface from spline node, I can just plug directly into projection.
[8:22] Now you can see here that I've gotten a warning.
[8:26] So let's zoom in on this warning here that I've gotten from my projection node and take a look at what it says.
[8:32] It says too many data items arriving on single data pin projection target.
[8:40] And so what that means is, hey, over here, I'm grabbing those three different splines that I set up on my landscape and I'm trying to pack three splines into my projection target when this node only wants one input.
[8:56] It just wants one object.
[8:59] So I do want to use my three splines.
[9:01] I want to put the forest in those three areas we defined.
[9:05] And so what I can do is take the take that those three different spline bits that I've created and I want to create a node called union.
[9:17] And what this is going to do is it's going to take those three spline objects and join them together.
[9:22] So I'm going to wire from my create surface spline into my union node.
[9:28] And now I can take the output from my union and plug that into my projection target.
[9:36] And once again, it's going to automatically create this intermediate node in between.
[9:42] That's going to convert my data from spatial to concrete.
[9:47] And now I've been able to plug that data into my projection node.
[9:52] So let's go ahead and save my PCG graph here and we'll switch over to our landscape.
[9:59] And now you can see whereas before we were growing trees everywhere.
[10:05] Now we're only growing trees in our forest in the areas that are inside those splines that I created.
[10:14] So basically I can define exactly where I want PCG to grow my forest.
[10:21] I've said, hey, I want forest in this location and I want forest in this location and I want forest in this location.
[10:31] So I can define exactly where I want my trees to go and it'd be really cool.
[10:38] I could define several different biomes.
[10:40] You know, maybe I want rocks to go over here and I want grass to go over here, that kind of thing.
[10:47] So I'm able to use splines and say, hey, I only want PCG to spawn objects in these specific areas.
[10:58] Pretty cool.
[10:58] So I can put down my splines and define exactly where I want my trees to grow.
[11:07] All right.
[11:08] Well, let's switch gears just a little bit and talk about another scenario.
[11:13] When you're building an environment, one thing that happens a lot is that there are specific areas where you want exact control over the placement of everything.
[11:23] PCG is great for building an environment really fast, but in the end, it's deciding the placement of each object.
[11:32] And if there's a spot in the environment where you want precise control, you need to be able to tell PCG to get out of the way so that you can work in that spot.
[11:44] Since I started this series on PCG, I've seen a couple of environment artists down in the comments say, hey, I don't want to give up control.
[11:52] The PCG, they want to be able to place objects exactly where they want them.
[11:58] So what I'm about to show you is a way to have it both ways.
[12:03] You can use PCG to add your forest or whatever kind of environment really quickly in the background.
[12:11] And then you can define specific areas where you don't want PCG to spawn things so that you can have exact control in those areas of where objects are being placed.
[12:22] So I'm going to show you how to use splines to set up to be exclusion zones for where not to place things.
[12:33] So here we've defined where it's going to put things and now I'm going to use these splines and tell it, hey, don't put forest in these areas.
[12:42] So let's switch back to our graph here.
[12:45] I'm going to delete these nodes that we just added to tell it, hey, only spawn our forest inside our splines and I'll reconnect up here our get landscape data to our projection node.
[12:59] If we save this once again, yeah, now we've got our forest spawning everywhere.
[13:04] So let me show you how to use these same splines that we've just set up these actors and tell it, hey, I don't want trees right here.
[13:15] Okay, so once again, we need to set up our get spline data node and instead of self, we want to set this to all world actors by tag and we've set the tag up to be forest.
[13:29] But obviously you can set up this up to whatever you want and we're going to select multiple.
[13:36] Okay, now the next node that we need is called a spline sampler.
[13:42] So there's our spline sampler node and what this node does is it starts creating points based on our spline.
[13:51] And by default, it's going to put those points on the spline and that's not what we want.
[13:57] We want the spline to be on interior or we want the points to be created inside our spline.
[14:06] And we're also going to project points onto the surface and we're going to set up our setting here for unbounded.
[14:16] So now we have two different surfaces.
[14:18] We've got the surface trend set up down here where we're adding points to our landscape and we've got this surface here where we're adding points inside our spline.
[14:30] And what we want to do is tell it, hey, I don't want points in these areas that are in spline inside our spline.
[14:38] And so what we need to do to make that happen is create this node called difference.
[14:44] And what this is going to do is it's kind of like a subtraction operation.
[14:48] It's going to take the points that we've already created and subtract these points that are inside our spline.
[14:56] So we've got our get spline data, our spline sampler, and we can plug our spline sampler into the differences input here.
[15:05] And then we can plug our source.
[15:08] And what we want to do is kind of insert this difference node here in between our transform points and the part where we actually start getting ready to spawn our meshes.
[15:19] So I'm just going to move these nodes here over just a little bit to give us some more room.
[15:24] And then I'm going to bring this difference node down here and plug our transform points into it.
[15:30] And now what this is doing is it's getting rid of any points that are inside our splines.
[15:37] And so now I can plug this into our density filter for our three nodes down here.
[15:44] And once again, it's going to create this intermediate node to translate the data into the type of information that our density filter nodes want.
[15:53] Now I'm going to delete these three connections here.
[15:59] And so what we've just done is we've inserted this difference node in between our transform points and our density filters.
[16:08] So now we should have the points inside our splines filtered out.
[16:13] So we've basically told PCG anything that's inside these spline areas, don't create points here.
[16:20] So let's go ahead and save this graph.
[16:22] We'll switch back to our landscape.
[16:24] And now if we take a look, you can see we've gotten rid of the trees that are inside our spline areas.
[16:32] Looks like it's still creating some trees here.
[16:35] So let me take a look at that really quick.
[16:39] Okay, I figured out why it's still creating some trees in this area.
[16:44] So if we take a look at our difference node here, you can see that our density function is set to minimum.
[16:52] And so what this is going to do is it's going to get rid of whichever points are the smallest.
[16:57] And that's not quite what I want.
[16:59] I want this to be set to binary.
[17:01] So it's either using these points or these points, but not both.
[17:07] And by setting it to binary, I'll be able to just get rid of everything.
[17:12] If I have this set to minimum, I have a little bit of control over exactly which trees I'm removing.
[17:20] Let's see if we take a look at our transform points here.
[17:24] I'm just going to set this, I'm going to hit D so that we can see the points on our landscape.
[17:29] And you can see these boxes that it's adding.
[17:32] And some of them are bright colors or light colors and some of them are dark.
[17:38] And so when I set that to difference, it was keeping the trees that are spawning in these points that have the lowest density value.
[17:48] And so instead, what I can do is set difference to binary.
[17:52] And when I do that, now it's going to remove all of the trees from those areas.
[17:58] All right, so we're all set.
[18:01] So now I've set up these three exclusion zones and PCG will not place any trees in these areas.
[18:10] And I'm free to create whatever I want in these areas without worrying that PCG will add things there and overlap what I'm trying to do.
[18:21] So with both of these techniques that I've showed you today, you get more control over exactly where PCG is placing objects.
[18:30] You can use splines to tell it exactly where to place the objects and you can use splines to define where not to place the objects.
[18:40] So I hope this tutorial was helpful and that you're able to use splines now to have more control over what PCG is doing.
[18:50] Where it's putting objects and where it's not putting objects.
[18:54] So thanks a lot for watching today.
[18:57] Have a great week and come back next week for more PCG tutorials.
[19:02] Thanks a lot everybody and have a good one.



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
