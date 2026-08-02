---
title: Spawn Objects Along Splines - Procedural Content Generation (PCG) - Episode 8
source: YouTube
url: https://www.youtube.com/watch?v=WQc0imxsGdI
author: Ben Cloward
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/spawn-objects-along-splines---procedural-content-generation-pcg---episode-8/
frame_count: 0
frame_status: pending-selection
---

# Spawn Objects Along Splines - Procedural Content Generation (PCG) - Episode 8

**Source:** [YouTube](https://www.youtube.com/watch?v=WQc0imxsGdI)
**Author:** Ben Cloward
**Duration:** 25m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py spawn-objects-along-splines---procedural-content-generation-pcg---episode-8 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to spawn objects along a spline using Unreal's PCG.
[0:07] Let's go!
[0:14] Alright, so we're in the middle of a series of videos about using Unreal's PCG.
[0:20] So far in the series, we've created this forest.
[0:25] And in last week's video, I showed you how to use splines to define specific areas where the forest can grow.
[0:33] If you'd like to watch the previous episodes in this series, I'll link the playlist down in the description so you can catch up.
[0:40] Today, I'm going to show you two examples of spawning objects along a spline.
[0:47] First, I'll show you how to create a simple row of traffic cones along our spline.
[0:54] And then I'll show you how to make this fence, which is a little bit more advanced.
[1:00] So I'm going to be showing examples using traffic cones and a fence today, but you can use these techniques for anything that needs to be placed in a line or along a path like street lights or railroad tracks, cement barriers, power poles, that sort of thing.
[1:20] So all of these are examples of how you might use a spline in PCG to quickly place objects in a row like this.
[1:30] Alright, so let's dive in and get started.
[1:32] So the first thing that I want to do is give myself a spline to work with.
[1:37] So I'm going to create a spline in my level here.
[1:40] I'll just come up here to the Add Object button and I'm going to go to Basic and select Actor.
[1:49] So this is going to give me an actor over here in my list of objects in my scene.
[1:55] And now I can create a spline inside that actor.
[1:58] In order to do that, I'm going to come up here to where it says Selection Mode and drop this down and pick PCG.
[2:06] And now that I'm in PCG mode, I'm going to click Draw Spline.
[2:11] Now there are two different kinds of splines I can draw.
[2:13] Draw Spline Surface will give me a spline that's going to be a closed loop circle.
[2:19] And Draw Spline is going to be an open-ended spline.
[2:22] And in my case, that's what I want to use today.
[2:25] So I'm just going to click Draw Spline.
[2:28] And then I can click and drag on my landscape to create a spline.
[2:33] And I'm just going to kind of meander my spline around here just a little bit to give myself something to work with.
[2:40] Alright, so I'm going to hit Accept.
[2:42] And so now I have an actor with a spline.
[2:46] And you can see that I've got these little debug arrows here indicating where the points of the spline are.
[2:56] Okay, so the next thing that I need to do is create a PCG graph.
[3:01] So I'm going to open my content drawer.
[3:04] And I'm going to come here to the PCG folder that I created previously.
[3:08] And I can just right click in here and pick PCG PCG graph.
[3:14] And that's going to open up this template browser here.
[3:17] And the nice thing about creating a spline PCG graph is there's a template that's all set up to get started from.
[3:26] So I'm going to pick TPL Sampler Spline and pick Initialize from Template.
[3:33] And I'm just going to name this new graph PCG Blime Tutorial.
[3:43] And we'll grab it and drag it and drop it into our level.
[3:50] Now you can see that the boundaries by default, the boundaries are going to be 25 by 25 scale.
[3:59] And I just want to make this a little bit bigger just to make sure that it will fit everything we're working on.
[4:06] So I'm just going to change it to 40 by 40.
[4:09] Obviously, you can make your graph whatever size you want in your level.
[4:15] But mainly the important thing is that I want it to encompass my spline.
[4:20] Oh, and there's one thing that I forgot.
[4:22] When I created this actor, I also need to add a tag on the actor.
[4:29] So I'm going to select the actor here and in the search, I'm going to type tag.
[4:35] And I need to give this actor a tag so that I can easily identify it in my PCG graph.
[4:41] So in my case, I'm just going to call this spline.
[4:46] Now for yours, if you're making a fence, you might want to name it fence.
[4:50] If you're adding a row of traffic cones, you might want to name it cones.
[4:55] But I'm going to use the same spline for both of our examples today.
[4:59] So in this case, I'm just going to call it spline.
[5:03] All right.
[5:03] So that's good.
[5:05] Now let's go ahead and open up our PCG graph, our PCG spline tutorial.
[5:16] And you can see here right out of the gate, it's created three nodes for us.
[5:23] We have a get spline data node.
[5:26] We have a spline sampler node and we have a debug node.
[5:30] So our get spline data is going to be retrieving the spline from the scene and bringing the data in
[5:37] so that we can use it in the graph.
[5:39] And in order to get the spline that we just created, we need to come up here to actor filter
[5:45] and drop this down and pick all world actors.
[5:49] So it's going to be looking at all the actors in our world.
[5:52] And we want to select which actor to use by tag.
[5:57] And the tag that I gave it was spline.
[5:59] So I'm just going to type spline here so that the tags match.
[6:04] And if I switch back here, now you can see that it's found the spline data.
[6:09] And we can tell that because it's adding these little debug indicators here.
[6:16] Let me show you how that's working.
[6:19] So our get spline data is finding the spline from our scene and then it's creating points along that spline.
[6:27] So our spline sampler node is creating points on our spline.
[6:32] We have the dimension set to on spline.
[6:34] That's where we want to create the points.
[6:37] We have the mode set to distance.
[6:40] And what that does is it creates a point every X amount of distance along the line.
[6:46] And in our case, we have our distance increments set to 100.
[6:50] So it's going to be creating points every meter along our line.
[6:54] Let's spread these out just a little bit.
[6:56] I'm going to make it 250 instead.
[7:00] And then our last note here in our graph is debug.
[7:04] And what that's going to do is it's going to add a debug mesh to every one of our points.
[7:10] And in this case, you can see that our point mesh is set to be this nice little access tripod.
[7:17] So if we switch back to our landscape here, you can see that everywhere where we've created a point along our spline,
[7:25] we get this nice little access tripod.
[7:28] And this is a good debug mesh because it indicates the orientation.
[7:33] As well as just the position of our points, we can actually see which direction our points are pointing.
[7:41] And that's really useful.
[7:43] Now, what we actually want to do our main goal here is to create some objects along this spline.
[7:51] And so what I'm going to do next is I'm going to create a new static mesh spawner node.
[7:58] And this is going to take the points that are created by our spline sampler node here.
[8:03] And spawn static meshes on them so I can connect up our spline sampler node to our static mesh spawner.
[8:10] And now I need to come over here to the settings of my static mesh spawner and add some mesh entries.
[8:17] So I'm going to hit the plus to add a mesh entry.
[8:19] Then I'm going to open up my descriptor and for the static mesh, I want to add some traffic cones just because obviously all forests need to have traffic cones in a line going
[8:32] through the middle of them.
[8:34] No, I'm just using this for an example.
[8:36] So I'll add my first traffic cone mesh here.
[8:41] And then I want to add a second index here because I have two different traffic cones.
[8:48] So what I'm doing here is just adding a little bit of variety.
[8:53] We have two different cone objects.
[8:57] All right.
[8:57] So I'll save that switch back to our landscape.
[9:00] And now you can see we have a nice little row of traffic cones here all lined up perfectly 250 centimeters apart all along our curve.
[9:14] So pretty cool.
[9:15] We've created a nice line of traffic cones.
[9:20] There's a couple of things that we can do to make this a little bit more interesting.
[9:24] So let's switch back to our graph.
[9:28] Let's just de-unconnect our debug for now and save it and that'll get rid of those little axis tripods.
[9:38] And if we hit the G key, we can hide our spline as well.
[9:42] Now you can see we just have our cones kind of weaving their way through the middle of the forest.
[9:50] Okay, like I said, there are a couple of things that we can do to make this a little bit more realistic.
[9:55] So what I'm going to do is insert transform points node here.
[10:04] And the problem with our traffic cones right now is they're a little bit too exact like nobody who's laying down traffic cones is going to make every single one of them exactly 250 centimeters apart and aligned perfectly like this.
[10:23] And so we want to apply or we want to introduce a little bit of variability here.
[10:28] And so what I'm going to do is add some random rotation along the Z axis.
[10:34] So along the axis that's pointing up from the traffic cone, I'm going to say, Hey, you can make these cones any rotation that's between negative 180 and 180 degrees.
[10:48] And then we'll plug this into our static mesh spawner here.
[10:52] And now what we'll see is that every single one of our traffic cones as a slightly different rotation.
[11:00] So we've given them some random rotation.
[11:02] And the last thing that we want to do is give them a little bit of random offset because nobody places traffic cones exactly 250 centimeters apart.
[11:14] And so I'm going to say, Hey, offset these traffic cones in the X and the Y somewhere between negative 40 and 40 centimeters.
[11:24] So we'll save this.
[11:25] And what this is going to do is just going to mess up the traffic cones a little bit so they feel a little bit more natural and organic.
[11:33] So we've got our traffic cones in a row.
[11:35] We've randomly rotated them and we've applied a little bit of random offset.
[11:40] Now, you'll notice I didn't add any random offset to the Z component because we want the traffic cones to be resting on the landscape on the ground.
[11:52] We don't want to push them into the terrain or make them float above the terrain.
[11:57] But we did want to give them a little bit of offset on the X and the Y and then rotate them randomly around the Z.
[12:06] All right.
[12:06] So that's a good tutorial for how to put objects in a line.
[12:10] If the objects don't have to be associated with each other at all, traffic cones don't touch each other.
[12:18] They don't care like what the rotation of their neighbors are or anything like that.
[12:25] But a lot of times when we spawn objects along a spline like this, we want to do something like a cement barrier or a fence or something like that.
[12:36] That has components that need to connect with each other.
[12:41] So let's switch back to our graph here.
[12:47] And we've got our get spline data, our spline sampler that's creating points.
[12:52] And then this portion of our points is spawning our traffic cones.
[12:56] So let's just disconnect that for now.
[12:59] And what I want to do instead is create a variation of this graph that will allow us to lay down a fence.
[13:07] So I'm going to copy our static mesh spawner here and instead of our traffic cones, let's get rid of these mesh entries.
[13:18] And I want to add a different mesh entry here for a fence.
[13:24] So we'll just add our modular wooden fence here and connect this up to our static mesh spawner.
[13:32] And let's take a look at what we get.
[13:36] So you can see our fence objects are spawning here and there are a couple of different problems.
[13:45] The first problem that I see is that they're a little bit too far away from each other.
[13:51] And so we need to set the distance between each of the points to be something that's a little bit, a little bit more realistic.
[14:00] So let's switch back here and just fix this problem.
[14:03] We can go to our spline sampler here and set our distance to match the length of these fence objects.
[14:13] And I happen to know that we need to set our distance increment to a value of 156 centimeters.
[14:20] And now when we save this and switch back, now you can see that our fence posts are doing a much better job of connecting with each other.
[14:30] But there are still some problems and you can see it right here.
[14:35] This fence post as we come around this corner, the point that we're spawning this fence post on is right here and its orientation is going this direction.
[14:46] But then our next point is right there.
[14:49] And let's just turn on our debug so that it makes this a little bit more obvious.
[14:55] I'm going to hook up our debug and we'll disconnect our fence posts for now.
[15:00] And let's take a look here.
[15:01] So you can see that this point here is pointing here and this point here is pointing here.
[15:07] But what we actually need is for these points to point at the next point in the line.
[15:15] So we need to do kind of a look at thing in order to make our points be more connected with each other so that our fence posts will attach kind of at the pivot point.
[15:29] And there's some really complicated ways of like rotating our points so they're doing a look at and that sort of thing.
[15:35] But we're going to skip the complicated method today and do just a really easy method.
[15:41] And the way that I'm going to do the easy method is I'm just going to use the points that we've created here and I'm going to drag out and I'm going to create a new spline.
[15:55] And you might be saying now we already have a spline here.
[15:58] Why are you creating a new one?
[16:00] Well, this one we're going to set it to linear and it's basically creating a small spline for each of these points.
[16:07] That's pointed at the next point along the line.
[16:13] And so this is how we can very easily do a look at.
[16:18] And so for each of these splines, now I'm going to create a new spline sampler.
[16:26] And this is going to create points that are on this new spline that's looking at the next point in the row.
[16:32] And for this new spline sampler, I'm going to set it to subdivision and I'm going to set the subdivisions to zero.
[16:38] So we've got the lines that are linear and then spline a spline sampler with zero subdivision.
[16:46] So it's just basically a straight line that goes from point A to point B from one point to the next in the line.
[16:56] So let's go ahead and plug our debug into this and see what we're getting now.
[17:01] So I'm going to connect up our spline sampler to debug and we'll switch back.
[17:07] And now what you'll see is that these red arrows are all of them pointing at the very next point in the line.
[17:16] Because we created a spline from that point to the next one and then spawn points basically in the line.
[17:24] So we're going to create a spline sampler that's going to spawn points based on that.
[17:29] And so now we can connect up our static mesh spawner here and what it's going to do is make us a fence that is significantly more attached to itself.
[17:38] Even when we're going around kind of these sharp turns, our fence posts are all going to be attached.
[17:46] All right, so that's pretty cool.
[17:50] A not so complicated solution to kind of a complex problem.
[17:56] And it's not perfect, but it works pretty well.
[18:00] All right, one last thing that we want to look at today, what do we do here at the end of our fence?
[18:08] So we've got this piece here that's just kind of hanging and there's no support here at the end.
[18:14] So what we want to do in order to fix this, the first thing that we need to do is to find the point that's at the very end of our spline.
[18:26] And we can do that by adding a node that's called filter elements by index.
[18:33] So basically we want to tell it a point and say, hey, filter out all the points that we're using so far except for just this one.
[18:42] So on the filter elements by index node, I don't want to select indices by input.
[18:48] So I'm going to uncheck that.
[18:50] I want to select specific indices.
[18:52] So if I were to say point zero, that would be the first point on my spline and point one is the second point on my spline point two is the third point.
[19:02] But what I want is the last one.
[19:04] And I have no idea how many points there are.
[19:08] So if I look at this tool tip here, I can see that I can type in point or I can I can type in negative one.
[19:16] And so what I'm going to do is type negative one and that is the last point on my spline.
[19:22] I don't know how many points there are, but if I just say negative one, it'll give me the last point.
[19:29] And now if I hook this up to my debug.
[19:36] You can see that the last point of my spline is right there.
[19:39] I only have one point that I'm connecting to the debug.
[19:44] There aren't any more of those nice access tripods except right here, which is the very last point on my spline and it's spawning this very last fence piece here at the end of the spline.
[20:00] Now I actually don't want this last fence post to be here because it's creating these horizontal beams that are just hanging.
[20:09] And so the next thing that I want to do is use the fact that I've found this last post or this last point and subtract this last point from my set before I spawn my meshes.
[20:24] And so what I can do with that and we've used this node a little bit in the past.
[20:29] We can create a difference node.
[20:32] So what this will do is I'll plug my points into the difference node and then I'll plug that one point that I've found that's at the end of the spline in there.
[20:42] And that is going to find the very last point that I need.
[20:47] And then now that I've found that difference, this is basically I'm saying, hey, take this set of points, subtract the last point and give me a new set.
[20:56] So now I can plug this into my static mesh spawner.
[21:00] And you can see sometimes nodes create this node here in between.
[21:05] And what this is doing is just converting from subtype spatial data to subtype point data so that I can plug it correctly into my static mesh spawner.
[21:18] So now if I say switch back to my landscape, you can see that last fence post has been removed.
[21:25] And now I can add a different static mesh to this final point that I've singled out here.
[21:34] So I'm going to copy and paste my static mesh spawner and connect up that point to it.
[21:41] And now we need to come over here and instead of using our wooden fence here, I need to add this last piece that's just the post.
[21:58] So instead of adding a fence with two horizontal beams, I just want to add a single beam there.
[22:03] That's the post.
[22:05] All right.
[22:06] And there we go.
[22:07] Now I have my post added on the final point and I've cleaned up my fence so that it has a nice termination there.
[22:15] So I had to do kind of this little complicated thing at the end of the graph here where I found the last point, subtracted that point from the set and then spawned all of the meshes with horizontal beams in that set, except for the very last point.
[22:34] And that one I can just spawn a post in.
[22:38] All right.
[22:39] So that got a little bit complicated, but nothing too bad.
[22:43] But we were able to create a really nice fence where all of the pieces connect with each other.
[22:50] They flow along the landscape and then we're able to terminate them with a nice little single post at the end for a clean ending.
[23:00] All right.
[23:01] Like I said earlier, you can use this same technique to spawn all kinds of different objects.
[23:07] We could spawn light posts, cement barriers, railroad tracks, you know, all kinds of things, anything that you need to spawn along a line or along a curve.
[23:18] This is a great way to do it.
[23:20] PCG is just really neat because it allows you to do all kinds of things really quickly.
[23:26] And the nice thing about this technique that I showed you today is now like I can just come in here.
[23:34] And if I need to change this path, I can just move any of these points and PCG will just instantly adapt the objects that I've added to my spline to flow along my new curve.
[23:49] And so it's really easy to edit these things after the fact.
[23:53] If I were doing this manually and I placed all these fence posts down by hand and rotated them to align them.
[24:00] And then my art director said, yeah, but I need to change this and move it over there.
[24:05] I would just be like, ah, now I got to do all that manual work.
[24:09] But this system automatically will adapt to changes you want to make and make it really quick to realign these things.
[24:19] It just does that for you instantly.
[24:21] All right, I hope this tutorial was useful and that you're seeing kind of the magic of PCG and you can integrate it into your workflow to really speed up your editing process.
[24:35] Thanks for watching everybody.
[24:37] Be sure to come back next week for more tutorials on PCG.
[24:41] And in the meantime, have a great week, everybody.



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
