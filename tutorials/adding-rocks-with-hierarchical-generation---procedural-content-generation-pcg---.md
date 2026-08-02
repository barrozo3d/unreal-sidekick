---
title: Adding Rocks With Hierarchical Generation - Procedural Content Generation (PCG) - Episode 9
source: YouTube
url: https://www.youtube.com/watch?v=u2hsoBgYUR0
author: Ben Cloward
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/adding-rocks-with-hierarchical-generation---procedural-content-generation-pcg---/
frame_count: 0
frame_status: pending-selection
---

# Adding Rocks With Hierarchical Generation - Procedural Content Generation (PCG) - Episode 9

**Source:** [YouTube](https://www.youtube.com/watch?v=u2hsoBgYUR0)
**Author:** Ben Cloward
**Duration:** 29m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py adding-rocks-with-hierarchical-generation---procedural-content-generation-pcg--- <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to use PCG's hierarchical generation system to efficiently place rocks into our environment. Let's go!
[0:17] Alright, so we're in the middle of a series of videos demonstrating how to use Unreal's PCG system.
[0:25] In the videos so far, I've shown you how to create this forest. Now if you're new to the series, I've placed the playlist for all of the videos down in the description so you can start the series from the beginning if you'd like.
[0:41] When building game environments like this one, rendering efficiency is important. With a tool like PCG, it's very easy to create tens of thousands of objects and really bog down your performance.
[1:00] One of the things that hurts performance is when you have large numbers of objects that render all the way out to the horizon.
[1:11] Rendering lots of objects that are far away can cause serious slowdowns.
[1:17] To help manage that, PCG has a system called hierarchical generation. The hierarchical generation system breaks up the environment into a grid and then we can use our PCG graph to only spawn objects in the cells of the grid that are close to the player.
[1:40] As the player moves around, the closer grids squares activate and further ones become inactive.
[1:48] So instead of keeping our whole world in memory all the time, we only need to load and render the objects that are right around the player.
[2:00] This type of system works well for small objects like rocks that are less noticeable from a distance.
[2:10] So we're going to be using rocks for this example today, but you can use this same technique for all kinds of different types of objects in your environment.
[2:21] Alright, that's enough explaining. Let's get to it.
[2:26] Alright, so the first thing that I want to do today is show you the rocks that I've selected that we're going to be spawning into our environment.
[2:33] I've created a little spot over here kind of off the edge of the map where we've laid out all of our assets.
[2:41] So we have all of our trees and we have all of our small ground cover details here.
[2:48] And on this plane we have the six rocks that we're going to use.
[2:53] I've selected these rock meshes from Megascans and I'll place the link down in the description where you can grab these assets.
[3:02] Now because it's me and I really like to work with shaders and materials, I went ahead and altered these a little bit so they have some moss on top of them.
[3:12] They didn't have that before. Maybe in a future video I'll show you how to do that.
[3:17] I've demonstrated this kind of thing before in my videos, but it's not really the focus of today's
[3:23] tutorial, so we won't be talking about that specifically. But these are the six
[3:30] rock meshes that we're going to be
[3:33] scattering throughout our landscape in today's tutorial.
[3:37] The first thing that we need to do is come down here to our content drawer and I'm going to come to our pcg folder here
[3:45] and I'll just right click and pick pcg pcg graph
[3:50] and we're just going to create an empty graph and I'm going to call this pcg rocks
[3:57] and we can just go ahead and drag our pcg rocks graph into our scene
[4:03] and I'm going to come over here to the size or the scale
[4:07] and I'm going to set it to 120 120.
[4:10] Just we have a nice size graph and now I'm going to center it on our environment.
[4:16] So it's just kind of right in the center of our terrain that we have here.
[4:27] Maybe raise it up just a little bit.
[4:30] Oh and I think it's a little bit too small in the vertical axis, so we'll maybe set the
[4:35] the z scale to 60.
[4:38] All right, so we've got our graph in our environment
[4:43] and there are a couple of settings that we need to set on our graph too. So I'm going to come down here
[4:49] and we're going to set the generation trigger instead of generate on load. We're going to set it to generate on run time
[4:57] because we want the points in our graph to update as the player is moving around.
[5:03] So we don't want to just generate those points once on load. We want to generate them
[5:09] as the player moves. So we'll set that to generate at run time
[5:12] and then we're going to turn on is partitioned.
[5:16] And that is the system that is breaking our
[5:20] points instead of filling the entire bounding box that we added.
[5:25] We're just going to fill the the cells or the chunks of the world that are right around the player.
[5:32] And I'll show you what that looks like in a minute.
[5:35] Now there are two other settings that we need to make sure that we set on the pcg world actor here.
[5:42] We need to make sure that we set
[5:45] the serialization mode to always serialize.
[5:50] And then we also want to turn on
[5:52] treat editor viewport as generation source.
[5:56] Now normally the generation source is the camera that's attached to the player.
[6:03] But because we want to be able to see what's happening in the in the editor as well,
[6:08] we need to make sure that the editor viewport
[6:12] is treated like the player camera so that as we move the viewport around,
[6:17] we can see our points being generated on the fly.
[6:22] All right. So with those settings set, now we're ready to open our graph.
[6:26] So I'm going to double click on my pcg graph that we just created here, pcg rocks.
[6:33] And before I add any nodes here, I need to set just a couple of settings.
[6:38] First, I need to choose use hierarchical generation.
[6:44] And that is what's going to split our graph up into individual chunks
[6:50] and generate points in each of those chunks instead of in the whole graph.
[6:55] And now I want to set my hierarchical generation default grid size.
[7:00] And we're just going to set the grid size to unbounded.
[7:04] And then in the graph itself, we'll manage the size of each individual cell of the graph.
[7:12] Okay. Now with that set, we need to create a
[7:18] create points grid node.
[7:20] And this is what's going to start generating our points.
[7:23] So the first thing that we're going to do is come up here to our grid extents setting.
[7:29] And we're just going to set our grid to be 100,000.
[7:38] And then for the cell size, we're going to set ourselves to be 700.
[7:43] And what this will control in the final output is how far apart the rocks are.
[7:51] How far apart the rocks are spaced.
[7:54] So what this is saying is we're going to have a rock roughly every seven meters in the grid.
[8:01] Now we're going to mess these up in a minute and kind of scramble them around.
[8:06] But this will kind of determine the average amount of space that's around each rock between one rock
[8:13] and the next.
[8:14] So if you want more rocks, you can reduce the cell size.
[8:19] And the rocks will be, there'll be more of them and they'll be closer together.
[8:23] But I think a rock about every seven meters is pretty good for now.
[8:28] Okay. The next thing that we need to do is set our coordinate space to local component.
[8:35] And what that's doing is it's keeping track of the points inside each of the individual cells
[8:41] instead of the whole grid as a single unit.
[8:46] And then we want to set call points outside the volume.
[8:51] So we're just adding points that are inside our grid extents here.
[8:58] Okay. So now we've generated some points.
[9:00] The next thing that we need to do is drag this out and create a change grid size node.
[9:07] Now here we set our hygiene default grid size to unbounded.
[9:15] But here we're actually creating the grid size that's going to be specific for the points that
[9:20] we're generating. And we are going to set our grid size to 1600.
[9:27] And so what this is going to do is it's going to make each of the cells in our grid about 16 by 16
[9:33] meters. And these are the chunks of the world that will contain our objects.
[9:39] Larger chunks mean that there are fewer chunks overall. So the larger your chunks are,
[9:46] the less memory you're going to be using to manage this system.
[9:50] But it's less fine grained. So you kind of have to find a right balance for the type of objects
[9:57] that you're spawning in. And in my case, grid sizes of about 16 by 16 meters is just about
[10:05] right for the rocks that we're going to be spawning.
[10:08] Okay. The next thing that we need to do is drag out and add an intersection node.
[10:15] And what this node is going to do is it's going to tell PCG, hey, we only want to show
[10:20] the grid size or the grid, the cells of the grid that are right around the player.
[10:27] So we're going to drag our points into our primary source and we're going to drag our
[10:32] grid cell volume into our source one. And so now that we've got this connected,
[10:38] we're only going to be generating points right around where the player is.
[10:43] Or right now, when we're not actually in the game, we're going to be generating them where
[10:47] the viewport camera is located. So now that we have our grid points, we've set our grid size,
[10:54] and we've done our intersection operation. We can drag this out and add a grid to our grid
[11:00] we can drag this out and add a debug node, which is going to allow us to visualize
[11:07] what our points look like on the graph. So let's save this and we'll switch back to our landscape.
[11:15] So now you can see we've got our points drawing. And as we move around, our points change and
[11:23] update depending on where the camera is. So as I'm moving around, these points are updating.
[11:35] And you can see how this white area kind of the area around the camera
[11:42] is where our objects are going to be spawning. But I'm kind of hearing you say, hey, there's a
[11:47] couple of problems here. First of all, our points are not on the terrain, they're just kind of floating
[11:55] here on this 2D plane. That doesn't seem right. And our points are just like these gigantic boxes.
[12:07] All right, so there are two problems that we need to solve. First of all, our points are in a grid
[12:12] that's a little bit too regular. So in order to make things feel a little bit more natural,
[12:18] we need to mess up our points a little bit. So they're more organic. And the second problem is
[12:24] the points are in a flat plane right now. And we need to project them onto the grid. So in order to
[12:31] make our points less regular, we can just create a transform points node. And in the series, we've
[12:39] used this node several times before. But what this is going to allow us to do is change the position,
[12:46] the rotation, and the scale of our points. So for position, remember that currently each of our grid
[12:54] cells is 700 by 700. So if we set our offset minimum to be negative 300 to positive 300,
[13:03] what that's going to do is it's going to allow the rock positioned inside that cell to be sort
[13:11] of anywhere inside that cell with a little bit of a boundary so that we make sure that the rocks
[13:19] don't normally overlap each other. All right, so we've given them a range of between negative 3
[13:26] and 3 meters that they can move around inside their cell. And now for our rotation, we're just
[13:33] going to allow our rocks to be anywhere from zero to 360 degrees random. And the nice thing about
[13:41] the rocks that we've selected is they work really well rotated in any direction. And so what we've
[13:49] done there is taken each of our rocks and given them a random rotation anywhere from zero to 360
[13:56] degrees. And we also want to control the scale of the rocks just a little bit. So I'm going to say
[14:03] the rocks can be 70% anywhere from 70% to 150% of their original size. So now we've given them
[14:15] random offset positions, random rotations, and random scales. So each of our rocks is going to have
[14:23] its own unique set of transform offset rotation and scale, just to give us a little bit more
[14:31] variety of our rocks. So now we can cook up our intersection node to our transform points node.
[14:38] And of course, it's going to insert this little node in between that's doing data conversion for us,
[14:46] because the intersection node doesn't necessarily deal directly with points.
[14:51] Okay, so we've got our transform. And now we need to project our points onto our terrain.
[14:58] And that's fairly easy to do because we can just use the projection node. And we'll connect up our
[15:04] points to the projection. And then we for our projection target, we need to use a get landscape
[15:14] data node. And so this will retrieve the information like the height data from our landscape. And we
[15:22] can just plug that right into our projection target. Okay, so we've messed up our points and we've
[15:29] projected them onto the terrain. Now let's add a debug node here and take a look at our results.
[15:43] All right, so you can see that our points are no longer floating up in the air. We've got our
[15:48] points projected down onto our terrain now. And as we move around, you can see that the points spawn
[15:55] in as we're moving. And they're connected with the terrain. I still see a couple of problems though.
[16:06] First of all, like if we take a look at this little hill here, we've got rocks that are sticking to
[16:12] every surface, kind of regardless of the angle of the surface. And if rocks are on a really steep
[16:20] slope, you know, obviously they're going to slide down to a more flat place. So what I want to do
[16:26] is add a couple of more nodes in our PCG graph that will remove rocks that are on steep slopes.
[16:34] So let's go ahead and do that next. So we'll come back here to our graph.
[16:39] And previously in the series, I was using kind of a complex way of doing that, but I found an easier
[16:46] way of doing that. And so I'm going to show that to you now. So I'm going to add this node called
[16:52] Normal to Density. And what this is going to do is it's going to ask you to give it a normal.
[17:00] And the normal we're giving it is 001. And that's a vector that's pointing in the up direction.
[17:06] And so what we're going to do is take a look at the direction that all of our points are facing.
[17:13] And the closer they are to the up direction, the wider or the closer to one, their density
[17:22] parameter is going to be. So if we take a look at the results of this node here.
[17:29] Now each of our points, instead of being solid white, you can see that some of them are gray.
[17:36] And especially the ones that are on this slope, like this one right here, has a darker gray value
[17:43] because it's kind of on a on a steep angle. So the steeper the angle, the darker the point is
[17:50] going to be. And I can now use that value to get rid of points that are darker. So let's do that.
[17:57] So we have our normal dense normal to density node. And I'm just going to drag out and create a
[18:06] density filter node. And this is going to allow us to get rid of points that have our specified
[18:14] range of the density value. By the way, I'm using this term density. It doesn't really mean how dense
[18:21] the points are. It's just a random zero to one value that we're able to assign the points as a
[18:27] parameter. So we can store information like, you know, how steep is the angle that the point is
[18:35] facing. So I've set my normal to density. And now I want to set my density filter. And in my case,
[18:42] I'm going to say, Hey, get rid of any points that have a density value that's darker than zero
[18:49] 0.93. So I'm going to keep all of the points that are between 0.93 and one, but anything that's
[18:56] less than 0.93 as a density value, we're going to get rid of that. So let's hit the D key here to
[19:03] turn on our debug, and we'll save our graph and switch back. And now you can see those points
[19:09] that were on the steep slope of our hill here have been removed. And we can only see points
[19:16] that are somewhere between 0.93 and one. So we've gotten rid of all of our points that were on
[19:24] slopes that were too steep. Alright, so we've pretty much solved all of the problems or the
[19:32] characteristics that we wanted for our rocks. And now I think we're ready to go ahead and take
[19:38] each of these points that we have on our graph. So we're going to go ahead and take all of the
[19:45] points that we have on our landscape and spawn rocks on them. So the way the way we're going to do
[19:51] that is with a static mesh spawner. So I'm just going to drag out here. And we're going to create
[19:59] a static mesh spawner. And this is going to take the points that our PCG graph has created so far
[20:06] and create a rock on each of them. So we have six different rocks we can add here. But for now,
[20:13] let's just add one and see how it looks. So we're going to come up here under our mesh entries. And
[20:19] I'm going to hit a plus and then open up our descriptor. And we'll drop down our static mesh here.
[20:26] And I'll go ahead and add a rock in here. And so let's hit save and switch back.
[20:34] And now you can see instead of our big white blocks, we actually have points that are spawning
[20:41] on our grid. And if I move back here a ways, if you're looking really close, we're going to look
[20:47] at this rock right here. As I move back, you can see it popped out. And it pops in this one's a
[20:55] little bit more obvious because it's dark. So I'll move back. So you can see that as we move away
[21:01] from the rock, it's popping out. And the reason it's popping out is because the grid cells of the
[21:08] hierarchy are being removed as we move our camera around. And this is really efficient because we're
[21:15] only storing points for these rocks in areas that are close to the player. If we want to control
[21:26] the distance where the rocks are being culled, we can come back here to our graph and change the size
[21:33] of our grid. So if we set this to like 800, now we have much smaller grid cells and our rocks are
[21:42] going to be culled much closer to the camera. And if we increase the size of our cells, they're going
[21:50] to be culled much farther away. But I think 1600 for our rocks is a pretty good size.
[21:57] All right, well, let's go ahead and take our mannequin for a spin here. You can see we've got some
[22:05] rocks that spawned in right in front of us. And as we back up, those rocks pop out.
[22:14] And then as we move forward, they come back in. So we're only spawning these rocks right around
[22:21] the player. Oh, you know what? I forgot about one thing. We have a really nice grass here.
[22:29] And in order for the grass to draw in correctly, when we're running around with our player, we need
[22:35] to turn on this command called always build runtime generation resources. We'll set that to one.
[22:42] And now when we run around with our mannequin, we actually get grass that's spawning in as well,
[22:49] in addition to our rocks. Okay, so we've just placed rocks. And they only spawn in
[22:58] in the area that's around the player. And so way off in the distance where the rocks aren't as visible,
[23:06] we're not storing rocks. We're not rendering rocks. And we're saving the performance that
[23:13] otherwise we would be wasting because the distant rocks aren't as visible.
[23:19] All right, this is great. There is one more thing that we can do to improve this a little bit.
[23:25] I did mention that in the distance, and it's it's kind of subtle because the rocks are far away.
[23:32] But the rocks do pop when we get to this spot where they're about to spawn in.
[23:39] And so what we want to do is soften that pop a little bit by allowing the rocks to blend in
[23:45] instead of popping. And so what I can do, oh, you know what, we forgot to add the rest of our rocks
[23:54] to the grass. So for our static mesh spawner here, we just added one, but let's go ahead and add a
[24:00] bunch more entries here. Two, three, four, five, six. So now we've got six rocks. And I'm just going
[24:09] to go ahead and off camera, fill in the rest of the rock meshes. Okay, so now we have our six
[24:17] rock meshes filled in here. And when we switch back to our landscape, now each of our points is
[24:24] spawning one of those six. So we have a little bit more variety in the types of rocks that we're
[24:32] spawning in here. Okay, but I did mention that the rocks are just popping out right now. And what
[24:39] we want to do is make it so that the rocks will sort of fade in instead of popping in. And so what
[24:47] I've done in our static mesh spawner, if we filter here in our search by the word cull, we can see
[24:55] that we have instant start cull distance and instance end cull distance. And for each of our
[25:01] rocks, I've set the start to 3,500 and the end to 4,000. And what this means is at 35 meters,
[25:14] the rock will start fading out. And then at 40 meters, it will be faded out completely. So this
[25:20] is the first part of the equation or the first that the first half of the thing that we need to do
[25:24] to solve this. So set our start cull distance and our end cull distance for each of the meshes in
[25:31] our static mesh spawner. But then we also need to come over to our material for the rocks. And
[25:38] instead of opaque, we need to set this to masked. And when we do that, it's going to expose the
[25:46] opacity mask pin on our root node here. Then we need to add the per instance fade amount node.
[25:55] And this is going to bring in that value that's generated by our start cull distance and our
[26:01] end cull distance. So whatever values we set here, when it gets to the start cull distance,
[26:09] we're going to have a value of white. And then when it gets to the end cull distance, we're going to
[26:13] have a value of black that comes into our material. So if we just hook that up to our dither temporal
[26:20] anti aliasing node here, and then attach that to our opacity mask, now we have a system that will
[26:29] fade out our rocks as they transition from the start cull distance to the end cull distance that
[26:36] we set on our static mesh spawner. So let's save our material changes here. And now watch what happens
[26:42] to this rock as I move away. Instead of popping out, now it's going to do this nice blend transition.
[26:51] I don't know how well you can see that because it's kind of small. Actually, you know what, maybe
[26:57] let's just for now, set our cull distances closer. So this is a little bit more obvious.
[27:04] Okay, I just set them all from 1000 to 2000. And now as we move away, yeah, you can see them
[27:11] kind of fade out, and then fade in as we move around. So this is going to help
[27:18] with the popping that we're getting. So it's just less jarring and less noticeable
[27:24] that the rocks are being culled out. So I'm just going to go ahead and set these all back to
[27:31] 3500 and 4000. And now let's go back, let's just take our mannequin out for one last spin.
[27:43] And we'll take a look at what we've done. So we set up a pcg graph that allows us to
[27:50] add our rocks to our scene. We have a set of six different rocks that we're adding.
[27:56] And each of them has a random rotation, random scale and random position offset.
[28:04] And we've set up hierarchical generation so that our rocks are only spawning right around
[28:11] where the player is and nowhere else in the environment. And this is an efficient way of
[28:17] placing these assets because we don't have to store all of the assets in memory or render them
[28:24] all the way out to the horizon. We can just spawn them in right where they're needed around the player
[28:31] and then get rid of them off in the distance where they're not seen. So pretty cool, a really nice way
[28:37] of efficiently creating assets for your environment. And like I said at the beginning, we did this for
[28:46] rocks today, but you don't have to do it just with rocks. You can use this kind of a system
[28:53] to spawn all kinds of objects. We didn't use this for our trees because trees are really
[29:00] visible way off in the distance, but it does work really well for rocks, which are a little less
[29:07] noticeable if we get rid of them kind of closer to the camera. Alright, thanks a lot for watching
[29:14] today. I'm working on a new video for next week that will hopefully enhance the appearance of our
[29:21] rocks. And I haven't quite figured out how to make it work yet, but if I get it, it's going to be a
[29:26] really exciting one. So I hope you come back next week for that. And in the meantime, thanks a lot
[29:32] for watching and have a great week, everybody.



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
