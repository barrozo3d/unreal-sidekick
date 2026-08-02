---
title: How To Grow A Forest in Unreal With PCG - Procedural Content Generation (PCG) - Episode 5
source: YouTube
url: https://www.youtube.com/watch?v=DoZRYtvb8OU
author: Ben Cloward
ingested: 2026-08-02
ue_version: "Not specified (UE5.7-era)"
tags: [pcg, blueprint, pipeline, intermediate, advanced, ue5-7]
extraction_status: complete
frames_dir: tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/
frame_count: 20
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How To Grow A Forest in Unreal With PCG - Procedural Content Generation (PCG) - Episode 5

**Source:** [YouTube](https://www.youtube.com/watch?v=DoZRYtvb8OU)
**Author:** Ben Cloward
**Duration:** 50m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to grow a forest using Unreal's PCG. Let's go!
[0:14] Alright, so we're in the middle of a series of videos about Unreal's procedural content generation system.
[0:21] In the first video in the series, I explained that PCG is a framework that allows you to define rules about how objects should be placed, and then the engine would place them for you.
[0:35] Today, we're going to do just that. We're going to define a set of rules for how our trees should be placed, and then Unreal will follow those rules to instantly build a forest for us.
[0:47] First, I'll show you a very simple method for placing the trees, and then I'll show you a more advanced method that gives much more natural-looking results.
[0:58] So, let's start building!
[1:01] Okay, the first thing that we're going to do is come down here to our Content drawer and select our PCG folder, where we've been creating all of the parts of our landscape so far.
[1:12] And I'm just going to right-click in here and pick PCG, PCG Graph, and we're just going to start from scratch on this one.
[1:21] So, I'm going to just create an empty graph, and we're going to call this PCG Forest, and I'm going to drag PCG Forest into my landscape, and it creates this little box here, you can see.
[1:41] And I actually want to make it a little bit bigger, so let's come over here and make our scale like 120 by 120.
[1:53] And then if we just zoom out, we'll be able to see how it fits around our landscape, so we kind of need to center it around the landscape.
[2:07] And I'm going to set the Z scale to 60, so 120 by 120 by 60, and that should do us pretty well.
[2:19] Okay, the next thing that we need to do is open up our graph, so I'm just going to double-click here, and we'll bring our graph window over so that we can see what's going on.
[2:32] And basically what we're going to do, the way this process works is we create a set of points, and then we control the attributes of the points, like position, rotation, and scale, and then we spawn our meshes on those points.
[2:52] And this graph here is where we're going to create those rules and edit the attributes of our points.
[3:03] So the most basic PCG graph for adding objects to our landscape consists of three nodes.
[3:12] The first one that we need to add is called Get Landscape Data, and this is going to bring in the information from our landscape so that we're able to spawn points on the surface.
[3:28] And the next node that we need to do is going to actually create those points, and it's called Surface Sampler.
[3:37] And so what we're going to do just really basically is pass the data from our Get Landscape node into our Surface Sampler, and then this node is going to create our points.
[3:50] And if we want to see just a debug visualization of what our points look like on the surface, we can select our Surface Sampler node there and hit the D key.
[4:02] And now you can see our landscape is totally covered with all of these random points.
[4:10] And if we zoom in here, you can see that each point has its own random black and white value somewhere between zero and one, and that is an attribute that's called density.
[4:22] So down here at the bottom of our PCG window, we have the Attributes panel, and if I select this object here and hit the A key, now I can see a big list of all of the points that it's created for me, and it's kind of a spreadsheet of all of the attributes.
[4:42] And if we scroll over here to the right, one of the attributes that we'll find is called density.
[4:48] So all of our points have a density value there, and the density value is just a random number between zero and one.
[4:56] So when we preview our points on our landscape here, it shows us that density value.
[5:01] So we can see this black one has a very low density value, and there's probably a white one here with kind of a high density value.
[5:10] Now they're called density, but that doesn't necessarily mean you have to use the term for that.
[5:15] You can use the density value for any kind of randomness that you want to apply to the points.
[5:22] Alright, so we've got two of the three nodes that we need to create our forest.
[5:28] The last node that we want to create is called Static Mesh Spawner.
[5:37] Okay, so we can take our points and plug them into our Static Mesh Spawner,
[5:44] and now we need to tell that object what points or what meshes to spawn.
[5:50] So let's take a look at the tree meshes that I've found to use in this project today.
[5:58] So over here, I just brought our tree meshes into our world and just placed them manually
[6:06] so that we can take a look at the trees that we're going to be using.
[6:09] Now if you want to use these trees, I downloaded this tree pack from FAB.
[6:15] It's called Temperate Vegetation Spruce Forest, and I'll put the FAB link down in the description below.
[6:23] This is a free set of assets, so you're welcome to grab these and use them in your own projects,
[6:28] or you might be able to find something that you like better.
[6:32] So this is what our trees look like.
[6:35] We have four really tall trees here, and then we have three sort of medium-sized trees,
[6:42] and then we have a bunch of different variations of trees that are getting younger and younger
[6:49] as we kind of go down the line here.
[6:51] So these are the assets that we're going to be using.
[6:54] And so if I bring up my PCG window again, let's go ahead and add these assets to our static mesh spawner.
[7:03] I need to come over here to our mesh selector, and under Mesh Entries, I need to add elements to this array.
[7:13] So I'm just going to hit this plus button here, and then open the descriptor,
[7:18] and now this is where I add the meshes.
[7:20] So I can drop this box down and type spruce, and I'm going to add spruce full one low,
[7:28] and then I'll add another one, and I'm going to add spruce full two low,
[7:38] and I'm just going to go ahead and go down this list and add all of the trees in our pack.
[7:44] Okay, so here's our static mesh spawner, and I've added all of our spruce trees here.
[7:49] Looks like we have 14 mesh entries, and each of them has a descriptor with a static mesh in it.
[7:59] And now if we take a look at our graph, I'll just save our graph here, and we can switch back to our level.
[8:09] Holy cow, we have a crazy looking forest. This is great.
[8:16] So we've got trees coming out our ears, and right now I think there's a problem here.
[8:23] Our forest is like really, really dense, and this is not going to run at any kind of frame rate that we want.
[8:31] So what we need to do is after we get landscape data and then create our points,
[8:38] in between creating our points and our static mesh spawner here,
[8:43] what we want to do is actually remove some of these points that we don't need.
[8:48] So right now you can see that our points, there are a whole lot of them.
[8:55] And so what I'm going to do is add a new node that's called a density filter.
[9:00] So I'll just type density, and we'll add the density filter node.
[9:06] And what this node is going to do is it's going to remove some of these points based on the input values that I define.
[9:13] So let's connect up our surface sampler here, and then take a look.
[9:18] In our density filter, we have a lower bound and an upper bound.
[9:23] So I talked about that density value that each of the points has.
[9:27] And what we can do is throw out the points.
[9:30] And in our case, we want to get rid of points that have a density value less than 0.3 and greater than 0.6.
[9:40] So I'll just set the values like that.
[9:43] So right now we're previewing the points at the surface sampler stage of our graph.
[9:49] But if I turn those off and preview the points after the density filter has been applied,
[9:55] now you can see that we have kind of a much more reasonable set of points here.
[10:02] And if I plug this value now into our static spawner,
[10:06] now we don't have the crazy amount of trees that we have before.
[10:11] Our number of trees is a lot more in the realistic range.
[10:18] All right, now the next thing that we can see that's kind of crazy is we've got trees that are all aligned with the slope of the terrain.
[10:27] And that can look okay in some cases, but we have some kind of large steep hills here in our terrain.
[10:34] And it's making the trees kind of grow all wacky.
[10:38] You know, in nature, trees grow straight up for the most part.
[10:43] So let's go ahead and fix that.
[10:45] In order to fix that, we're going to add a new points, a new node in here that is called transform points.
[10:57] There's our transform points node.
[10:59] So we'll go ahead and wire from our density filter to our transform points.
[11:04] And then what this node does is it changes the position, rotation, and scale attributes of our points.
[11:13] So if we come over here, you can see that we can offset the points, but in this case, we're not going to use, we're not going to change the points position.
[11:21] We're going to change their rotation and scale.
[11:25] So for rotation, we can set the minimum and maximum for x, y, and z.
[11:33] So for x and y, we're going to set negative five as the minimum and negative 180 or the z, because we want to be able to randomly rotate the tree any direction around its up facing axis.
[11:50] But then around the other two axes, we just want to give a little bit of variation.
[11:55] So there's a range here of anywhere between negative five and five degrees.
[12:01] So they're not pointing perfectly straight up, but we're able to make them kind of have a little bit of variety.
[12:10] And then this box is the one that actually fixes the problem that we have, absolute rotation.
[12:16] So instead of our points being aligned to the landscape, we're telling them these are the rotation values that we want to absolutely apply.
[12:26] If you don't check this absolute rotation box, these will be added to their already present rotation values.
[12:36] So they're just going to be offsets of the rotation they already have.
[12:40] But checking absolute rotation means the points are going to use these values as absolute.
[12:46] And I can also give them some scale, minimum and maximum values.
[12:50] And so in my case, I'm going to say their minimum values are 0.7 and then their maximum values are going to be 1.5.
[13:00] And what that does is it just gives them some some height variety.
[13:05] So not every tree is going to be the same.
[13:08] And so let's just take our transform points node that we just created, wire it into our static mesh spawner and hit save.
[13:18] And let's take a look now.
[13:20] And we can turn off our points debug view there.
[13:25] And now you can see that we've got a pretty cool looking forest.
[13:30] Our trees are no longer growing out of the side of the cliffs, but they're all for the most part growing straight up and down.
[13:42] And that's pretty cool.
[13:44] All right, now there is one more thing that we can apply to this simple forest that we've created so far.
[13:51] And that is right now we've got trees growing on the sides of cliffs here.
[13:57] And that may be a little bit unrealistic.
[13:59] If we have a cliff that's made of rock, we're probably not going to have a big tree like this growing right out of the middle of it.
[14:06] And so we need to filter our points based on their angle.
[14:12] And so that's the next thing that we can do.
[14:14] I hope you can see how we started out with just a crazy random set of points and we're slowly applying rules to these points to make the results more natural and more realistic.
[14:30] All right, so the next rule that we're going to apply is to not grow trees on steep slopes.
[14:37] And we're going to do that right here in between our density filter and our transform points node.
[14:46] Some of you might know a better way of doing this, but this is the way that I've found to not get the trees to grow on steep slopes.
[14:55] We're going to use a node in PCG called filter elements by range.
[15:01] And what this does is it allows us to remove points if their attributes are within or outside of a specific range.
[15:12] So I'm going to wire my density filter in here.
[15:15] And then I'm going to come over here to my target attribute and I'm going to click this plus here and I'm going to pick point rotation.
[15:26] So if the rotation of my point and I don't want just any part of the rotation, I actually want the pitch.
[15:34] So I'm going to say rotation dot pitch.
[15:38] And now I need to set the minimum and maximum values.
[15:43] So I'm going to create a constant.
[15:47] So there's a constant value.
[15:49] And I'm going to say if the pitch of my point is greater or if it's less than negative 35.
[16:00] So that's going to be my minimum.
[16:03] And then I'll make a new constant just by copying and pasting.
[16:07] And the maximum is going to be 35.
[16:10] So wire that into my maximum.
[16:14] So now I've filtered out points whose pitch attribute is less than negative 35 or greater than 35.
[16:24] So that's the pitch, but I also need to filter by the role attribute.
[16:29] So I'm going to copy this filter attribute by range.
[16:33] And instead of pitch, I'm going to change this version to rotation dot role.
[16:40] And now I can set the points that are inside the filter and I'll wire that in.
[16:48] And then I want to keep the points that are inside the filter.
[16:51] I could also keep the points that are outside the filter if I wanted to.
[16:56] But in this case, I want the points that are inside.
[17:00] All right, so I'm also going to pass my negative 35 and 35 into my filter min and filter max where I'm filtering the role.
[17:11] So if we preview this set of points here, let's see, let's stop spawning our trees just for a minute so we can see what this is doing.
[17:25] So right now we're previewing the result of our density filter.
[17:30] And you can see that I have these points spawned on this really steep slope.
[17:36] But then if we plug in our filter attributes by element range here, I'll stop previewing that node and I'll come over here and hit D on my transform points.
[17:48] Now you can see that these filter attribute elements by range nodes have removed the points that have a pitch attribute or a role attribute that's too steep.
[18:01] So now I can plug my transform points into my static mesh spawner.
[18:06] And now I've got trees that are growing where it's relatively flat and not on steep slopes.
[18:16] Now my steepness value is still kind of steep.
[18:20] So if it's up to negative 35, between negative 35 and 35 and pitch or roll, it's still going to create that tree.
[18:28] But at least it's not going to be spawning where it's really steep like right here.
[18:35] All right, so we've used PCG to define our set of rules where we want our trees to go.
[18:41] And we've got a pretty cool looking forest.
[18:44] Let's go ahead and run around this forest and see if there's anything interesting we can find.
[18:49] So we've got our mannequin character there and we're free to run around and explore our forest.
[18:59] So this is great. PCG has just instantly created a forest for us based on the rules that we created for ourselves.
[19:09] Now one thing that you might notice is that these trees...
[19:14] Oh, let me jump out here really quickly and I want to show you something else that's neat.
[19:18] So it just created this forest for us.
[19:21] But let's say that we're not really happy with the way that this forest turned out.
[19:25] And we wanted to try again, maybe say like give us another variation of this forest.
[19:32] Well, that is really easy to do.
[19:35] So we can just come over here to our surface sampler node and change the seed.
[19:42] So right now we have this seed value that's a random seed and every time this value changes,
[19:50] it's going to update the forest and give us a different variation of it.
[19:54] So I can just change the seed value and every time I change it,
[19:59] it's going to give us a different variation and put those trees in a slightly different place with slightly different tree meshes.
[20:07] So it's really easy to instantly try different varieties and there are like an infinite number of variations that are available.
[20:18] All right, now the thing that I was saying before is right now, so this is a pretty basic forest,
[20:25] but there's no real logic to how the trees grow.
[20:29] We haven't defined any rules about, you know, larger trees or smaller trees.
[20:36] And if we think carefully, let's come over here to the trees that we have available to us.
[20:43] If we think carefully about these trees, we've got a couple of trees here that are the oldest and we know they're older because they've grown taller.
[20:52] And then the next oldest trees are these here, these kind of medium sized ones.
[20:57] And then our youngest trees are here in this line in the front.
[21:02] So if we think about the growth pattern, these trees here probably grew first and then they're going to drop pine cones around them.
[21:13] And so we're going to get medium trees grouped around the tall trees.
[21:20] And then finally, the medium trees are also going to drop pine cones.
[21:23] So they're going to have the smaller trees grouped around them.
[21:28] And so we're going to get this growth pattern where we have clumps of large trees surrounded by medium trees.
[21:37] And then outside of the medium trees, we're going to have small trees growing.
[21:42] And believe it or not, you can use PCG to define this type of system.
[21:48] And that's what we're going to do next.
[21:50] So the first part of this video that we just finished was kind of showing you how to just randomly spawn trees without any sort of growth pattern at all.
[22:02] But what I want to show you next is how to create logic in PCG that follows natural rules for how forests actually grow.
[22:14] Okay, so what I'm going to do here is just disconnect my static mesh spawner.
[22:19] And we need to think about this a little bit.
[22:22] So let's kind of give ourselves some space here.
[22:26] So we've got this system set up.
[22:28] We bring in our landscape data and then we call out points that are too steep and we transform them so they're pointing straight up.
[22:39] And then we spawn our meshes here at the end.
[22:43] But what we want to do is figure out, we want to spawn some points that represent where the oldest parts of the forest are.
[22:54] Those are going to be like where the forest started growing at the very beginning.
[23:00] And so what I'm going to do is I'm going to take my surface sampler here with its density filter.
[23:09] And I'm going to duplicate this set of filter attributes by range nodes.
[23:16] And we're just going to come over here.
[23:18] And what I want to do is define a little bit more strict rules for the way that these first, like the center of the forest is going to get created.
[23:29] So I only want to spawn points that are between negative five and five.
[23:35] So what we're saying here is that our forest started in an area that was like ideal conditions where the terrain is relatively flat.
[23:47] And for our surface sampler here, I want to reduce significantly the number of points that we're spawning.
[23:57] So right now we're spawning 0.1 points per square meter.
[24:03] And what I want to do is reduce this a lot.
[24:06] I'm going to set it to 0.05 points per square meter.
[24:11] So these points that I'm creating represent the centers, the oldest parts of the forest.
[24:17] And I only want a few of those centers.
[24:21] So let's go ahead and turn on our debug view for this and see what we're getting now.
[24:30] Okay, so you can see I'm getting some points over here and the points are mostly only spawning in the flat areas.
[24:40] And I also want to edit my density filter a little bit.
[24:45] So let's take a look at that.
[24:48] Let's come over here to our density filter.
[24:51] And oh, it looks like 0.3 and 0.6 are good values.
[24:55] So let's stick with those.
[24:57] And then let's come over here and we have our transform points node.
[25:01] We need one of those for these points as well.
[25:04] So let's go ahead and plug in our inside filter to our transform points so that we can make sure that all of our points are pointed straight up and down.
[25:16] And they have good scale values just like we set up before.
[25:20] So let's go ahead and turn off debug for that and turn it on for this.
[25:26] And you can see that we've got these little clumps of points in these areas here.
[25:33] Now, the next thing that we want to do is we're going to call each of these points kind of a center of the forest.
[25:42] And we're going to spawn more points from each of these positions.
[25:46] So this is kind of a cool feature of PCG which allows you to spawn points from other points.
[25:54] So what I can do is use a node called create points grid.
[26:00] And this is going to spawn some additional points for us.
[26:04] And what we need to do is define how big these grids are.
[26:10] And so I'm going to say we want to make these grids 2,500 by 2,500 by 1.
[26:19] So each of these is 25 meters square.
[26:23] And we're going to make the cell sizes 200.
[26:27] Now these cell sizes are basically what's defining the size of our trees.
[26:33] So if we make the cell size 2 meters by 2 meters, what that means is if I have a point there,
[26:39] no other points are going to spawn inside that kind of 2 meter square space.
[26:45] So it gives the tree a little bit of breathing room.
[26:50] Okay, and the next thing that we want to do is copy points.
[26:55] So this is our copy points node.
[26:58] And this is going to take the points grid points that we created.
[27:02] And that's going to be our source.
[27:04] And we're going to copy these points to our target,
[27:08] which is each of these other points that we're using to scatter.
[27:13] So let's go ahead and take a look at what our results are.
[27:16] Now that we've created grid points and then copied them to all of our forest centers.
[27:23] And holy cow, it looks like we've created a ton of points.
[27:30] And it's really kind of hard to see what's going on because all of these new points that we've created
[27:37] have the exact same density value.
[27:39] They all have a density value of 1.
[27:42] So there's basically a grid of individual points around those original like core forest points that we created.
[27:50] But their density value is 1.
[27:52] So let's fix that.
[27:54] So we need to come over here to our copy points and we need to add another node called attribute noise.
[28:03] And what this node is going to do is it's going to fix our density values.
[28:07] Right now, our density values are all 1 for these points.
[28:11] But if I pull this out and connect it, our attribute noise node is going to allow us to set and we need to set our input source here to density.
[28:25] And we're going to set it to be between 0 and 1.
[28:29] So if I stop previewing these points and start previewing these instead, now you can see I've got these grids of points.
[28:38] And I've set their density values to random numbers and it's a little bit easier to make out what's going on.
[28:44] So we've just spawned ourselves a ton of points and each one of these is potentially going to represent a tree in our forest.
[28:54] And the trees are growing out from those center points that we defined initially.
[29:00] Okay, but right now, all of these points that we've created for ourselves are very regular.
[29:06] They're in a perfect grid.
[29:08] And so what we need to do next is add a transform points node.
[29:13] And we're going to just scatter them out a little bit more.
[29:17] So our goal with this node is to mess up this really nice, perfect, regular grid that we have and create something that's a little bit more natural looking.
[29:29] So we're going to offset, rotate and scale our points just a little bit.
[29:34] We're going to offset them by negative 400 in each of the X and Y dimensions.
[29:45] And then positive 400 for our maximum value.
[29:52] And then we also want to randomly rotate them.
[29:54] So we're going to set this to negative 180 to positive 180 so they can be anywhere in that 360 degree range.
[30:03] So let's stop previewing these points and preview these instead.
[30:08] And now you can see that we've messed up those grids so that our points are kind of randomly offset and randomly rotated.
[30:18] Now, I think it's apparent that we have just like entirely too many points.
[30:23] So again, we can use our density filter to remove some of these points that we don't want just to kind of thin this out and give us a more realistic amount of points.
[30:35] I'm going to use the density filter a lot because right now we have way too many points.
[30:41] I'm going to say, hey, get rid of anything that's not between 0.9 and 1.
[30:46] And so let's start previewing this guy here.
[30:52] And you can see that I've removed a ton of those points and we just kind of have a core set of points left.
[31:00] All right, now we need to figure out, you know, we decided at the beginning of this project that we wanted to spawn the big trees at the center of our point clouds here.
[31:15] And we want to kind of fall off so that we've got our medium trees further out from the big trees and then at the edges we want to spawn the little trees.
[31:26] And so we need to figure out a way of calculating how far away from those centers we are.
[31:34] And before we do that, I'm just going to come back here to our initial surface sampler and I'm going to set the point extents.
[31:46] And the reason that I'm doing this is so that we can get some better distance values.
[31:51] I'm going to set our point extents to 1, 1, and 1, just so these initial points that we're spawning are very small.
[31:59] That's going to give us like more fine control over this distance that we're about to calculate.
[32:06] So I want to take these points that we've got here and I want to figure out how far away is it from each of these points to the center point where they were initially spawned.
[32:18] And so in order to do that, I can create a node that's just called distance.
[32:27] And so I'm going to take the values coming out of my density filter and plug them into, whoops, they're actually two distance nodes and I put down the wrong one.
[32:38] Wouldn't you know it?
[32:39] We don't want vector distance.
[32:43] We want spatial distance.
[32:45] So these points are the source and our target, if we come back here, our target are these original points that we created at the center.
[32:57] So let's let's turn this debug view off.
[33:00] And now you can see I'm left with only the points that are in the centers.
[33:05] And if we measure the distance between those points and the new set of points that we created.
[33:13] Well, first, before we can do that, we need to set some values over here.
[33:18] We want to set the density of our points to be equal to the distance that we calculated.
[33:24] And we want to set our maximum distance to 2200 just to kind of define that range.
[33:32] And so now what you can see is the points that are nearest to the center have a density value of black and the further away from those centers, the brighter or the higher their density value gets.
[33:49] So it's really easy now to visualize where those centers are.
[33:55] So that's where our tallest trees are going to be planted.
[33:58] And then as we get further away, we're going to spawn our smaller trees in the areas that are further from the centers.
[34:10] So that we were creating this natural progression of, you know, our oldest trees in the middle and then our medium trees and then our youngest trees out toward the edge.
[34:21] But you might have noticed something.
[34:23] We created these grids of points.
[34:25] They were just flat grids.
[34:27] And so now we've got a whole bunch of points that are just floating in the sky.
[34:33] And what we need to do is take all of those points and project them back down onto the landscape.
[34:40] And that's pretty easy to do.
[34:42] We can just create a projection node and plug in our points here.
[34:49] And then we want to connect up our landscape data so that we know where we're projecting from.
[34:57] So I'm just going to come over here to our get landscape data and wire that into our projection target.
[35:04] So now if we hit debug on our projection node, I'm going to save it and force region.
[35:10] And now we can take a look and all of our points have been projected down onto our landscape.
[35:18] And you can see really easily we've got the centers of our forest.
[35:24] And then we've got these nice gradients that fall off from the center out toward the edges.
[35:31] Now there's one other thing that we can do that's kind of interesting.
[35:35] Right here before we do our projection, we can take these points and set their size based on their density value.
[35:47] And in order to do that, I need to create or I need to use a node that's called scale by density.
[35:53] And so I'm going to look for this other node that's called execute blueprint.
[36:00] And what this node is, is it's a container that has a bunch of blueprints that are available to use with it.
[36:08] So there's this drop down here blueprint element type.
[36:13] And I can drop this down and I can find which blueprint I want to apply.
[36:18] So these are a bunch of additional nodes that they didn't make into separate PCG nodes,
[36:24] but they're like blueprints that you can apply inside a PCG.
[36:29] And so I'm just going to do a search for and there it is scale by density.
[36:34] So I'm going to plug the data coming out of my distance node into scale by density.
[36:40] And now I can use scale by density to set the minimum size that I want my points to be and the maximum size that I want my points to be.
[36:50] And in this case, I'm doing something a little bit unintuitive.
[36:55] My minimum scale points are the biggest ones.
[36:59] That's the areas that are black.
[37:01] And my maximum scale points are the smallest ones.
[37:05] Those are the areas that are white.
[37:07] And so I've kind of flipped this on its head and inverted it.
[37:11] And what it's doing is it's taking the points that are black and setting their scale value to one.
[37:17] But then as we go down from black to white, it's scaling the points down to a minimum of 0.5.
[37:26] So now I can take this point or this output here and plug it into projection.
[37:32] And what we're going to see is these points update so the points in the middle stay really large.
[37:38] But then as we move further away from those centers, the points get smaller.
[37:45] So I hope it's apparent to you how we're kind of imitating the way that nature works with this PCG system.
[37:55] We've kind of defined some areas that are the oldest spots in our forest.
[38:00] And then we're moving away from those oldest spots.
[38:04] And we're going to spawn our largest trees in the old spots of the forest.
[38:10] And then our younger trees are going to move out from those centers.
[38:15] So let's go ahead and finish up our graph here.
[38:18] The next thing that we need to do is take these nodes that we kind of split out at the beginning.
[38:24] I'm going to move these over and we're going to filter out.
[38:27] We don't want again, we don't want trees spawning on steep cliffs.
[38:32] So we're going to filter out our points based on their rotation range.
[38:38] So we're just going to wire these nodes in here.
[38:41] These are the ones that we created previously and nothing has changed there.
[38:46] So we're just going to keep them as they are.
[38:48] The transform points node is the same.
[38:52] But over here at the end, this is where things get a little bit interesting.
[38:58] Because we're going to be filtering our points into three different stages.
[39:05] If we take a look again at the trees that we have, or three different sets rather.
[39:11] So we have our big trees, our medium trees, and our little trees.
[39:15] And so we're going to split out the points that we have into those categories based on how far away they are from the centers.
[39:24] So let's go ahead and we'll create a density filter here.
[39:28] And this density filter, we're going to go from zero to 0.4.
[39:36] So those are the dark areas in our graph, the closest to the center.
[39:43] And then we'll just copy this point.
[39:46] And our medium trees, we're going to spawn between the values of 0.4 and 0.6.
[39:54] And then our smallest trees, we're going to spawn between the values of 0.6 and 1.
[40:03] So now we have three separate tracks.
[40:06] And we've divided this up so we can spawn the three different types of trees.
[40:12] So let's go ahead and take a look at each of these.
[40:15] If we kind of move our window over here.
[40:18] So right now we're looking at all of our points.
[40:21] But let's go ahead and look at these points here.
[40:24] So if I look at this set, these are our tallest trees.
[40:29] And then we've got our medium trees like this.
[40:34] And we've got our smallest trees like this.
[40:38] So we've divided this up into three different categories.
[40:43] And the next thing that we need to do is because we've divided these,
[40:47] you can see that for our smallest trees, they all have kind of high density values between 0.6 and 1.
[40:55] And we need to fix that so that they can have proper density values again.
[41:00] And so we're going to add this node called attribute noise.
[41:04] And this is going to reset our density values here.
[41:08] So we'll select attribute noise and we'll set our input source to density.
[41:15] And that's going to give us the full range of values on our points again between 0 and 1.
[41:23] So when we use this density filter, we kind of changed our density so we only had really bright points.
[41:30] And now we use this attribute noise node to change those values again.
[41:36] So we have density that fills the full range between 0 and 1.
[41:41] And now, so this density filter, the purpose of this one was to split it into three different groups.
[41:49] And now we can use another density filter to remove some of these points because right now our tree density is just a little bit too high.
[41:57] So I'm going to add another density filter there and I'm going to set this one to 0.2 to 1.
[42:04] And that's going to remove some of our points so we just, so we don't have quite so many trees.
[42:10] All right, and we're going to go ahead and do the same thing that we just did with our other two categories.
[42:17] So I'm going to copy and paste this attribute noise node here.
[42:22] And so each of these categories is going to be for a different scale tree and we can have different densities for each of them as well.
[42:32] So I'm also going to copy this density filter here.
[42:41] And we'll set this one to 0.8 because we want just a few really large trees.
[42:49] And then we're going to set this medium one to 0.9.
[42:52] So we're going to have just a few medium trees and then lots of these little trees, mostly because they don't take up very much space.
[42:59] Okay, so if we turn on debug for all three of these, you can see now we have our largest trees here in our centers.
[43:10] And then we have our medium trees around them and then we have our smallest trees around them.
[43:21] So we've created these points following kind of these natural laws where our tree growth expands out from the center where the oldest trees are in the middle and the youngest trees are at the edge.
[43:35] And now all we have to do is take our static mesh spawner here and we need to make three copies of it.
[43:41] And each of these spawners need to have this one needs to have the large trees, the medium trees, and then our small trees down here.
[43:49] So what I'm going to do is just go ahead and go through this list that we've got and remove all of the trees that are small from this one.
[43:59] And we're going to remove our medium trees.
[44:05] They're the ones that are called bull.
[44:08] So there's our large trees.
[44:10] Let's go ahead and spawn those and see what we have.
[44:13] Yeah, so now you can see our kind of old growth forest areas there.
[44:20] And then around those we want to spawn our medium trees.
[44:24] So I'm going to go ahead and remove the trees that are called half and also the trees that are called small.
[44:39] And we'll wire this up.
[44:41] And now we have our medium sized trees and you can see they're growing kind of in the areas adjacent to the larger ones.
[44:52] And let's go ahead and turn off our debug filters here.
[44:57] And then the last thing that we need to do is remove our full trees and our half trees.
[45:03] So we just have our small trees left in this third static mesh spawner here.
[45:10] And now we just have small trees left so we can wire that in.
[45:14] And so let's save that and we'll take a look.
[45:18] And now you can see we have a forest that's growing kind of in a very logical way with our tall trees first,
[45:28] then our medium trees and then our small trees.
[45:32] And the groupings make logical sense.
[45:36] Now there are some trees that are kind of close together here, some things that we might want to take care of.
[45:42] But I hope what you can see that I've illustrated here is that we've used our PCG graph to define these natural laws.
[45:54] And we're able to build a system that spawns trees according to these rules that we come up with.
[46:00] So our graph is kind of getting complex here, but you can see we spawn these initial points that were that define the center points of our forest.
[46:11] And then off of those points, we created these points on this grid.
[46:17] We noise them up here with our transform and then we thin them out with our density filter.
[46:26] And then we calculated the distance from each of those points back to the center so that we could figure out which points are in the middle and how far away the points are from that middle.
[46:39] And then we scaled the points so the points in the middle were larger and the points toward the edges are smaller.
[46:47] Then we projected the points back onto our landscape.
[46:51] We filtered them by how steep the slope is.
[46:55] And then we set our rotation again so that we can make sure that all of the points are facing up and down and that they have some rotation and scale variety.
[47:05] Then we split our points out into three groups based on the density.
[47:11] And at this point, that density contained the distance from the center.
[47:15] So our points that are between zero and point four from the center became our tall trees.
[47:21] The points that are between point four and point six became our medium trees.
[47:25] And then the points that are between point six and one became our small trees so that we're able to spawn different types of trees depending on how far away they are from the distance of our forest.
[47:40] So to me, this is really cool that we're able to have this power to define these natural laws.
[47:48] Now there are more natural laws than we've defined here.
[47:52] Some trees get more sunlight than others and they might grow more depending on their access to water.
[48:00] So trees that are at lower elevations might grow more so there are all kinds of natural laws that you can define.
[48:07] But here we've kind of made them grow from centers outward.
[48:13] And to me, this is just really cool.
[48:16] So let's go ahead and take our mannequin and go for a stroll and explore this forest that we've created.
[48:24] So here you can see our nice tall stand of grass that represents the center here.
[48:31] And then as we progress further away from the center, we've got our medium trees here, medium trees, and then we've got our small trees out here toward the edge.
[48:42] And they're following those rules that we set down for first defining the centers of our forest, then spawning medium trees around the center, and then smaller trees around the edges of those centers.
[48:59] Alright, to me this is just fascinating. I love this stuff.
[49:04] Now one thing that you might notice, if we look at our trees, there is something missing.
[49:09] I'm looking down here at the base of these trees and our trees are spruce trees.
[49:14] They have pine needles on their branches, but we don't have any pine needles down here underneath the trees.
[49:23] So we need to find a way of somehow making these trees, create kind of pools of pine needles underneath them so they feel a little bit more naturally rooted to the forest floor.
[49:40] And that's what we're going to talk about in next week's video.
[49:43] I'm going to show you how to make these trees tell the landscape that it needs to have a pine needle material around each of the trees to make the trees feel like they fit naturally into the landscape.
[49:59] And that they've been, you know, as they've been growing for the last couple of decades, they've been dropping pools of pine needles that have accumulated at the bottoms of each of these trees.
[50:12] So yeah, that's the video that we're going to go over next week and it looks great, believe me.
[50:17] So I hope that you'll come back for that one.
[50:20] And in the meantime, thank you so much for watching and I hope you have a great week.



---

## Captured Frames

- [3:50] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_000.jpg
- [4:22] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_001.jpg
- [8:09] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_002.jpg
- [9:55] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_003.jpg
- [13:20] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_004.jpg
- [17:36] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_005.jpg
- [18:06] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_006.jpg
- [19:59] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_007.jpg
- [24:30] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_008.jpg
- [26:23] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_009.jpg
- [27:23] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_010.jpg
- [28:44] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_011.jpg
- [30:08] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_012.jpg
- [30:52] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_013.jpg
- [34:08] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_014.jpg
- [35:10] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_015.jpg
- [37:38] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_016.jpg
- [43:10] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_017.jpg
- [45:18] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_018.jpg
- [48:24] tutorials/frames/how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep/frame_019.jpg

---

## Structured Notes

### Core Technique
Two escalating approaches to spawning a forest with **static/CPU PCG**: (1) a basic random-scatter graph (Surface Sampler → Density Filter → slope filtering → Transform Points → Static Mesh Spawner), then (2) an advanced "natural growth" graph that seeds sparse forest-center points, grows a scattered points-grid outward from each center, computes each point's distance back to its center to drive both point scale and tree-size selection, and splits the result into three static mesh spawners (large/medium/small trees) so trees get logically smaller with distance from the forest's "oldest" core.

### Summary
Part one builds the simplest possible PCG forest: `Get Landscape Data` → `Surface Sampler` (creates randomly-distributed points on the landscape surface, each carrying a random 0–1 `Density` attribute, inspectable via A/attributes and D/debug-visualize) → `Static Mesh Spawner` loaded with 14 spruce-tree mesh variants from a free FAB pack ("Temperate Vegetation Spruce Forest"). The raw result is comically over-dense and has trees growing sideways out of cliff faces, so three fixes are layered in: a `Density Filter` (keep only points with density between 0.3–0.6) to thin the count to a realistic level; a `Transform Points` node with **Absolute Rotation** checked (X/Y: ±5° for slight natural tilt, Z: ±180° for free yaw) so trees point straight up regardless of terrain slope, plus scale randomization (0.7–1.5); and two `Filter Elements by Range` nodes filtering on `Rotation.Pitch` and `Rotation.Roll` (keep only −35° to 35°) to remove points on cliffs too steep for a tree to plausibly grow. The graph's random **Seed** (on Surface Sampler) can be changed at any time to instantly generate a different forest layout/variation. Part two rebuilds this from scratch with ecological logic: real forests grow outward from old "seed" trees via dropped pine cones, so the graph first samples a sparse set of low-density **forest-center points** (tight pitch/roll flat-ground filter, very low points-per-square-meter), then for each center uses `Create Points Grid` + `Copy Points` to scatter a dense local grid of candidate tree positions around it, randomizes their density via `Attribute Noise`, scrambles the regular grid via `Transform Points` (offset ±400, full 360° rotation), thins with another `Density Filter`, then critically uses a `Distance` (spatial, not vector) node to measure each point's distance back to its originating center and **overwrites the Density attribute with that distance value** (capped at a 2200 max) — meaning "density" now encodes "how far from the forest's oldest core." That distance-as-density value drives a `Scale by Density` blueprint-element node (inverted: closest-to-center points scaled largest, ~1.0; farthest scaled down to ~0.5) before a `Projection` node drops the (previously flat-grid, floating) points onto the actual landscape surface. The same steep-slope filtering and up-facing Transform Points from part one are reapplied, then the points are split into **three tiers** via three `Density Filter` ranges on that distance-derived density (0–0.4 = large/oldest trees, 0.4–0.6 = medium, 0.6–1 = small/youngest), each re-randomized with its own `Attribute Noise` (since the filter step leaves density clustered) and further thinned per tier (large trees kept sparse via an aggressive filter, small trees kept dense), then routed to three separate `Static Mesh Spawner` nodes each loaded with only the correspondingly-sized tree meshes. End result: a forest with tall old-growth trees clustered at each center, medium trees forming a ring around them, and small young trees at the outer edge — teased to get a pine-needle-litter ground detail pass "next week."

### Key Steps
**Part 1 — Basic forest:**
1. New empty PCG Graph ("PCG Forest") dropped on the landscape, box scaled to ~120×120×60 to cover the terrain.
2. Three-node minimum graph: `Get Landscape Data` → `Surface Sampler` (creates randomly scattered points on the landscape surface; each point gets a random `Density` attribute 0–1, viewable via the A/Attributes panel or D/debug-visualize toggle) → `Static Mesh Spawner` (Mesh Entries populated with all 14 mesh variants from a spruce-tree asset pack — tall/medium/young variations).
3. Add a `Density Filter` node between Surface Sampler and Static Mesh Spawner; set Lower/Upper Bound (e.g. 0.3–0.6) to discard most points and bring the tree count down to a realistic density.
4. Add a `Transform Points` node (after Density Filter): check **Absolute Rotation**, set Rotation Min/Max X and Y to a small range (e.g. −5° to 5°) for slight natural tilt, Z to the full range (−180° to 180°) for free yaw around the up-axis — this forces trees to point straight up regardless of the terrain slope they landed on (unchecked Absolute Rotation would instead *add* to the terrain-aligned rotation). Also set Scale Min/Max (e.g. 0.7–1.5) for height variety.
5. Add two `Filter Elements by Range` nodes (inserted before Transform Points, after Density Filter) — one targeting `Rotation.Pitch`, one targeting `Rotation.Roll` — each with Filter Min/Max constants (e.g. −35 to 35) and "keep points inside the filter" selected, to remove points on slopes too steep for a plausible tree.
6. Wire the final filtered/transformed points into the Static Mesh Spawner. Changing the **Seed** value on the Surface Sampler node instantly regenerates a different random forest layout.

**Part 2 — Natural growth pattern (advanced):**
7. Duplicate the Surface Sampler + Density Filter + slope-filter chain to create a second, stricter branch: tighten the pitch/roll filter range (e.g. −5° to 5°) and drastically reduce Surface Sampler's points-per-square-meter (e.g. 0.1 → 0.05) to get a sparse set of **forest-center points** (the "oldest" spots).
8. Add a `Create Points Grid` node sized to define local tree spacing (author: 2500×2500×1 grid extent, cell size 200 — cell size controls minimum spacing/breathing room between candidate tree positions).
9. Add a `Copy Points` node: Source = the Create Points Grid output, Target = the sparse forest-center points — this stamps a full local grid of candidate points around every center.
10. Add an `Attribute Noise` node (Input Source = Density, range 0–1) right after Copy Points, since all copied grid points otherwise share a Density of exactly 1.
11. Add a `Transform Points` node to break up the regular grid: Offset Min/Max ±400 on X/Y, Rotation Min/Max −180° to 180° on Z.
12. Add another `Density Filter` (e.g. keep 0.9–1) to thin the now-excessive point count down to a manageable number.
13. Back on the original Surface Sampler (the one generating forest-center points), set **Point Extents** to (1,1,1) — shrinking the center points themselves improves the precision of the distance calculation that follows.
14. Add a **spatial** `Distance` node (not the vector-distance variant) — Source = the thinned scattered points, Target = the original forest-center points — to compute how far each scattered point is from its originating center.
15. Feed that distance value into the points' **Density** attribute (overwriting the earlier random noise value), capped at a Max Distance (author: 2200) — points near a center get low/black density, points far away get high/white density.
16. Add a `Scale by Density` node — found via the generic **Execute Blueprint** node's Blueprint Element Type dropdown (search "scale by density") rather than as a dedicated built-in node — with Min Scale mapped to the darkest/closest points (author sets this inverted: min scale = 1.0 for closest, max scale = 0.5 for farthest) to make old-growth-adjacent trees larger.
17. Add a `Projection` node (Points input = the scaled points; Projection Target = `Get Landscape Data` output) to drop the still-flat/floating grid points down onto the actual terrain surface.
18. Re-apply the same steep-slope `Filter Elements by Range` (pitch/roll) and up-facing `Transform Points` (Absolute Rotation, small X/Y tilt, full Z yaw, scale variety) from Part 1 to this new point set.
19. Split into three size tiers using three parallel `Density Filter` nodes on the distance-derived density value: **0–0.4** (closest to center = large/old trees), **0.4–0.6** (medium), **0.6–1** (farthest = small/young trees). Since each filter clusters its output density near one end of its range, add a fresh `Attribute Noise` (Density, 0–1) after each to restore full random variety within that tier, then an additional `Density Filter` per tier to independently tune how many trees of each size appear (author: large trees filtered aggressively sparse at 0.8–1, medium at 0.9–1, small left denser at 0.2–1).
20. Route each of the three tiers into its own `Static Mesh Spawner`, each populated with only the mesh entries matching that size class (full/tall trees; half/medium trees; small/young trees) — producing large trees clustered at centers, medium trees ringing them, and small trees at the outer edge.

### UE Systems / Blueprints / Settings
- **Asset pack used:** "Temperate Vegetation Spruce Forest" (free, FAB) — 14 mesh variants spanning full-grown to young trees.
- **Core PCG nodes:** `Get Landscape Data`, `Surface Sampler` (Points per Square Meter, Point Extents, Seed), `Density Filter` (Lower/Upper Bound), `Transform Points` (Offset/Rotation/Scale Min-Max, Absolute Rotation toggle), `Filter Elements by Range` (Target Attribute e.g. Rotation.Pitch/Roll, Filter Min/Max via Constant nodes, Inside/Outside Filter output), `Static Mesh Spawner`.
- **Advanced-graph-only nodes:** `Create Points Grid` (Grid Extent, Cell Size), `Copy Points` (Source/Target), `Attribute Noise` (Input Source attribute, output range), `Distance` (spatial variant, not vector — Source/Target points), `Execute Blueprint` node with Blueprint Element Type = **Scale by Density** (Min/Max scale, invertible), `Projection` (Points, Projection Target = landscape data).
- **Key attribute reuse pattern:** the generic `Density` point attribute is repurposed multiple times for different meanings across the graph (random thinning value → distance-from-center value) — density is "just a float," not semantically fixed.

### Difficulty
Advanced (Part 2) / Intermediate (Part 1) — Part 1 is an accessible basic PCG scatter; Part 2 requires understanding point-attribute repurposing, spatial distance calculations, the Execute Blueprint node's blueprint-element system, and chaining multiple filter/noise passes to build emergent, ecologically-motivated placement logic.

### UE Version
Not explicitly stated; continues the UE 5.7-era PCG series baseline from Episodes 1–4 (this episode uses static/CPU PCG rather than Episodes 2–4's runtime/GPU approach).

### Tags
pcg, blueprint, pipeline, intermediate, advanced, ue5-7

---

## Related Entries
- `tutorials/introduction-to-procedural-content-generation-pcg---episode-1.md` — Episode 1, establishes the basic Create Points Grid → Transform Points → Static Mesh Spawner pattern this episode's Part 1 mirrors (using Surface Sampler instead of Create Points Grid for landscape-conforming placement).
- `tutorials/adding-multiple-detail-meshes-to-landscapes---procedural-content-generation-pcg-.md` — Episode 4, the prior episode in the series (runtime/GPU grass+stones masking) — this episode explicitly pivots to static/CPU PCG for larger objects (trees), contrasting with Episodes 2–4's GPU compute-shader approach.
- Next episode in this series (adding pine-needle ground litter under each tree) is the direct continuation of this video's end-teaser — look for a title about landscape detail/ground cover tied to tree placement, likely "Automatic Landscape Tree Blending."
