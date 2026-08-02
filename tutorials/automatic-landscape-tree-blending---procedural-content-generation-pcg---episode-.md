---
title: Automatic Landscape Tree Blending - Procedural Content Generation (PCG) - Episode 6
source: YouTube
url: https://www.youtube.com/watch?v=VtvM-OkZYDk
author: Ben Cloward
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/automatic-landscape-tree-blending---procedural-content-generation-pcg---episode-/
frame_count: 0
frame_status: pending-selection
---

# Automatic Landscape Tree Blending - Procedural Content Generation (PCG) - Episode 6

**Source:** [YouTube](https://www.youtube.com/watch?v=VtvM-OkZYDk)
**Author:** Ben Cloward
**Duration:** 39m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py automatic-landscape-tree-blending---procedural-content-generation-pcg---episode- <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to automatically add dirt and roots under all of your PCG trees.
[0:09] Let's go!
[0:16] So, we're in the middle of a series of videos about using Unreal's PCG, or Procedural Content Generation.
[0:24] In last week's video, I showed you how to grow this forest.
[0:29] I'll link the playlist for the whole series down in the description if you'd like to go back and watch the previous episodes.
[0:36] One of the things that we noticed when we made this forest last week is that we need a way to connect these trees to the ground.
[0:47] The Procedural Content Generation system is doing a great job of placing, you know, hundreds of trees all over our landscape,
[0:56] but the trees right now just kind of feel like they're plunked down, and there's nothing that's connecting them to the landscape.
[1:05] Generally, real trees, when they grow, especially like, so these are pine trees, they're going to be dropping pine needles and creating kind of a little skirt around them with dirt and roots and pine needles.
[1:20] And these don't have that, they're just kind of sitting on top of our landscape instead of being tied in and connected to it.
[1:28] Let me show you some examples of what I mean.
[1:31] Alright, so I found a couple of images here, so we've got a nice pine tree here, and what happens with pine trees is they drop their needles on the ground, and the needles are acidic.
[1:42] And so they make the soil around the tree not as friendly for the grass.
[1:49] And so you get this area where, so you've got nice grass here, but then right around the tree where it's dropped its needles on the ground, you're going to get less grass growing, and you also end up with these roots growing out from the tree.
[2:03] Here's another example, got a nice pine tree here, and a bare spot under the tree where it's got roots and pine needles.
[2:12] And then here again, another example, dirt and roots and pine needles under the tree.
[2:18] And in our unreal scene, we don't have any of that, we just have grass as if there were no trees growing there.
[2:28] Now, it would be totally possible to just go in and paint dirt and roots, paint a material under each of these trees.
[2:39] You could do that, but the problem is that PCG is super flexible, and all I need to do is change one number, the random seed for the placement of these trees,
[2:53] and they're instantly going to be regenerated all in different locations.
[3:00] And so if I were going to go in and manually paint dirt material here, that would kind of defeat the purpose of PCG,
[3:08] because after that I wouldn't be able to change my trees anymore or update the graph that's being used to generate the placement of the trees.
[3:19] So what I need is an automated method that's tied to the trees themselves that will add that dirt and root mask underneath each of the trees.
[3:31] And if I make changes in my PCG graph, I want it to automatically update.
[3:37] And that is exactly what I'm going to show you today.
[3:41] You guys, I'm really excited about this one.
[3:44] What I'm going to show you is not specific to PCG.
[3:47] So you can use this system for any objects that you place on a landscape.
[3:53] Really, it doesn't have to be generated with PCG, but this is so cool and flexible.
[3:59] I really wanted to throw this in here, even though it's not strictly using the PCG system or it doesn't depend on it.
[4:08] So the process that we're going to go through today, I'm going to show it to you in five steps.
[4:13] So let's take a look at those.
[4:15] All right, so here's what we're going to do.
[4:17] We're going to create an automatic tree dirt generation system.
[4:22] And here are our five steps.
[4:23] So first, we need to create an asset that's called a runtime virtual texture.
[4:29] And I've talked about these a couple of times on the channel before, but it's not something that we've used extensively, at least not in my videos.
[4:37] So the first thing that we're going to do is create a runtime virtual texture asset.
[4:41] And this is a texture that's going to hold the information that we need and it will become our mask to indicate where the dirt and the roots go.
[4:52] Then we're going to add a runtime virtual texture volume to our level.
[4:58] And we're going to point that volume at our runtime virtual texture asset.
[5:03] Our third step is to set the tree meshes that are in our PCG graph to render into our runtime virtual texture.
[5:16] And then we need to update the trees material so that it is rendering into the runtime virtual texture.
[5:23] And finally, we're going to change our landscape material so that it will read the runtime virtual texture and use it as a mask to determine where our root and dirt material needs to go.
[5:39] So we're telling the trees to write their data into a texture.
[5:44] And then we're using that texture in the landscape material to figure out where to put the root and dirt material.
[5:52] So that's the overall process.
[5:54] Let's go ahead and jump in and get started on it.
[5:57] So the first thing that I need to do is open up my content drawer.
[6:01] And I'm going to come in here to my terrain shaders folder.
[6:05] You know, obviously you can put your asset wherever you would like, but I'm going to put mine in this folder that I've created called terrain shaders.
[6:12] So I'm just going to right click in here.
[6:14] And for the type I'm going to search for runtime and I want to create a runtime virtual texture.
[6:22] So there it is.
[6:23] And I'm going to call this terrain tree dirt and hit enter.
[6:34] And then let's open up this asset.
[6:37] So here is our terrain.
[6:39] Whoops, I spelled that wrong.
[6:41] There we go.
[6:42] Terrain tree dirt.
[6:45] And there are a lot of settings here.
[6:47] Normally when you use a runtime virtual texture on a landscape, what you're doing is writing the color and the normal and the roughness.
[6:57] And so you can see by default the virtual texture content is set to have color and normal and roughness and specular.
[7:08] We don't need any of that.
[7:10] We want to make our runtime virtual texture as cheap as possible.
[7:14] So we don't need all of these individual channels.
[7:17] So I'm just going to drop this down and pick mask for and that's going to make our RVT just a single texture with four channels in it that we can write to.
[7:30] And I can also change some things here that will make this a lot cheaper.
[7:35] So I'm going to change our size of virtual texture in tiles.
[7:40] I'm going to reduce this down to 32.
[7:44] And then the size of each virtual texture tile, I'm going to reduce this down to 128.
[7:53] And then I don't think we need any border padding at all.
[7:56] So I'm just going to reduce this to one.
[7:59] The idea is we want to make these tiles in our virtual texture just as small as possible so that it'll be really fast to write to them.
[8:08] And then I can also set the number of low mips to remove.
[8:13] I can set this to something like four.
[8:16] Our goal here is to reduce the resources that we're using.
[8:21] We don't need to write high resolution textures in this case because we're just creating a mask for where the dirt goes under our tree.
[8:29] All right, so we've created terrain tree dirt and I'm just going to go ahead and save this.
[8:35] So that's our first step.
[8:36] The second step that we need to do is we need to come in here to our level and we need to add a new element.
[8:46] So I'm just going to hit this plus button here and type runtime and I need to create a runtime texture volume.
[8:59] So there's our runtime texture volume that we've created.
[9:03] And there are two main settings that we need to adjust on our runtime virtual texture volume.
[9:10] The first one is we need to point it to our virtual texture.
[9:14] So I'm going to write that I'm going to drop this down and we need we named ours terrain tree dirt.
[9:21] And here it is.
[9:22] So I'm going to plug that in.
[9:24] And the next thing that we need to do is size it to the proper size of our landscape.
[9:32] And to do that, that's really easy.
[9:34] We just have this tool called bounds aligned actor.
[9:38] And so I can just drop this down and pick my landscape and then hit set bounds.
[9:43] And now that that runtime virtual texture volume is automatically set to the size of my terrain.
[9:55] The nice tools built in will just when I hit that set bounds button,
[10:02] it'll set the dimensions of my runtime virtual texture volume to be the dimensions of my terrain.
[10:09] So I'm all set there.
[10:13] All right.
[10:14] The next thing that I need to do is change my tree meshes so that they render into my runtime virtual texture.
[10:21] And in order to do that, I need to pick my PCG graph.
[10:25] So here is the PCG graph that we created last week.
[10:29] And this is the graph that is spawning our trees.
[10:34] So I'm going to switch over to this graph here.
[10:38] Our tutorial video last week was almost an hour long.
[10:41] And I explained how all of these nodes work to generate the positions of our trees.
[10:46] But all we need to concentrate on today is these last three nodes here.
[10:51] This one is spawning our tallest trees.
[10:54] This one's spawning our medium height trees.
[10:57] And then this one's spawning our smallest trees.
[11:01] And you can see each of these three static mesh spawner nodes has a list of which tree meshes it's spawning.
[11:10] And so what I need to do is select this.
[11:13] And for each of these trees, I need to open this up and come down here to the runtime virtual texture section and add a runtime virtual texture there.
[11:25] Now, just to make it easier on myself, I can use the search filter here at the top
[11:29] and just type runtime.
[11:31] And that will show me just the properties of the runtime virtual texture for each of these four trees that I've added here.
[11:39] Okay, so I can just hit the plus button here and then drop this down and tell it which runtime virtual texture I want to write to.
[11:48] And in my case, it's terrain tree dirt.
[11:52] And so I'm just going to set that for each of the trees in my list here.
[12:05] All right, so I've told my four tallest trees to write into the runtime virtual texture.
[12:11] Let's go ahead and set that up as well for my three medium sized trees.
[12:18] So I'll just hit the plus button and select my terrain tree dirt RVT from the dropdown.
[12:26] All right, so my meshes are all set up and I can save my PCG graph.
[12:33] And then, okay, so I created a runtime virtual texture.
[12:37] I created a runtime virtual texture volume for my terrain.
[12:42] And I told my individual meshes to write into that volume.
[12:48] Now, the next thing that I need to do is open up the material for those meshes and tell them how they need to write into the runtime virtual texture.
[13:00] So this material is being applied to my trees.
[13:05] And the trees are writing base color and metallic and specular and roughness.
[13:10] All the material properties this material is writing out.
[13:14] But in order for it to write into my runtime virtual texture, I need to add a runtime virtual texture output node.
[13:27] And here you can see the inputs for base color and specular and roughness.
[13:32] These are all of the things that you could write out into your runtime virtual texture.
[13:37] If I switch back over to my RVT, you can see that there are various formats for the runtime virtual texture.
[13:45] And in my case, I'm only using mask for.
[13:49] So if we switch here to our material again, the only input on the runtime virtual texture output node that I'm going to be able to use is mask for.
[14:00] Because my runtime virtual texture only has mask for.
[14:05] So in this case, we're just going to start out really simple.
[14:09] All I have to do is tell it, hey, where whenever I'm rendering the tree, just write a value of one into mask for.
[14:18] And that's it.
[14:19] Like I'm just writing white where the tree is and passing that into mask for.
[14:26] So I'll save my tree material.
[14:30] And now we're ready to use that mask that the trees just wrote.
[14:36] Actually, let's take a look here really quick.
[14:39] If we take a look at our runtime virtual texture now, I'm wondering if we can actually see our trees in the texture itself that we just wrote.
[14:50] Yeah, did you see that?
[14:52] See all these little white dots?
[14:55] Those are all of the trees that are writing themselves into the texture.
[15:00] You can actually see what's happened in our runtime virtual texture there.
[15:05] So now the only thing that's left is to switch over to our landscape material here and sample our runtime virtual texture so that we can use it as a mask to determine where our dirt needs to go.
[15:21] So I created a whole series of videos on this material for our landscape.
[15:27] And so I'm not really going to go over what this is doing.
[15:30] We just need to jump in here and add our runtime virtual texture.
[15:35] I'm going to create a runtime virtual texture sample.
[15:41] And this is what we're going to use to bring in the information from the runtime virtual texture that we just created.
[15:50] So runtime virtual texture sample.
[15:53] I'm going to drop this down and pick our terrain tree dirt RVT.
[15:59] And now this mask for pin that's coming out here.
[16:03] And I'm going to create a component mask node.
[16:09] We're just going to use the red channel for now.
[16:13] We've written white into all four channels.
[16:16] So red, green, blue and alpha, they're all the same.
[16:19] They're just white.
[16:22] But I'm just going to filter this out so we're only looking at the red channel.
[16:26] And I'm going to take this and wire it into my color because I just want to see the color of the mask.
[16:33] So let's save this and we'll switch back to our landscape now.
[16:38] And what you're going to see if we switch over to unlit is that each tree now has a big white splotch underneath it because the tree has been rendered into the runtime virtual texture.
[16:51] And you can see it's really low resolution and chunky, but that's okay because we're just using this as a mask to determine where our trees are.
[17:02] So we can take this mask and use it as a blend to blend in a new material that we add, a new layer that we add in our landscape for where the dirt should be applied underneath our trees.
[17:20] Alright, so so far everything's working great.
[17:23] We just need to switch over to our material here and use a mask.
[17:29] So this is the grass portion of my material and I'm blending between kind of lush green grass and kind of rocky dry grass based on the altitude.
[17:43] So here's my altitude mask and I'm using a height Lerp and then blending between those two types of grass.
[17:49] And then I blend between that and my cliffs and my snow and all the other things.
[17:55] But what I want to do is come in here and insert a new material.
[17:59] So I'm going to create a new blend material attributes node.
[18:06] And we're going to blend between our grass material and a new material that I make that has the dirt and the roots in it based on that runtime virtual texture map that we just created.
[18:20] So I can grab this and wire it into the alpha of my blend material attributes node.
[18:29] And now I can connect this up to, you know, wherever my grass used to be going.
[18:36] Now I'm going to use this instead.
[18:39] So I've got both my grass and my roots material blending in here.
[18:45] So just going to take this and wire it in wherever that grass material used to be.
[18:53] Okay, so the only thing that's left now is to create a material just like I've created for my grass here.
[19:01] I need to create a material for my roots and my dirt.
[19:07] So if we take a look at the fab store, here is the material that I found on the fab store.
[19:13] It's a Quixel Megascans material that is really nice looking.
[19:17] It has dirt and leaves and roots.
[19:20] And you can tell it's made specifically for the purpose of creating these areas that are underneath trees.
[19:29] And so this is the material that I grabbed.
[19:31] Now, obviously you can use whatever material you want for yours, but this is the one that I found that I thought was pretty good.
[19:39] I'll link this down in the description so you can find it pretty quick.
[19:43] All right, so to build this material, the style of materials that I use for landscape just to reduce the number of texture samples that are required are with a color and a roughness texture.
[19:59] And I call those CR and with an NOH texture that has normal occlusion and height.
[20:08] And so what I did is I took those textures that I downloaded from fab and I repacked them so that I have the first texture.
[20:17] Let's just go ahead and create these as I'm explaining it.
[20:21] We'll create a texture object and I'm going to drop this down.
[20:28] And I think I can just search by roots.
[20:31] Yeah, there we go.
[20:32] So I've got this ground forest roots texture that looks like that.
[20:41] And I'll just copy and paste that one.
[20:43] That one has our color and our roughness in it.
[20:46] And then this one I'm going to drop down and pick the NOH version of the texture.
[20:54] That one has our normal, our occlusion and our height in it.
[21:00] And now I need to plug these texture objects into the type of layer that I want.
[21:07] And in my case, I want to use a node called simple layer.
[21:12] This is a material function that we created in the previous series of videos.
[21:17] So I can just plug my color and my roughness into that and my normal and my occlusion and my height into that as well.
[21:26] And now I need to specify the scale of the parameters that I want.
[21:32] By the way, if you want to know how to create this, I'll link the playlist for this series where we went over all the principles and features of landscape materials.
[21:44] That's an interesting one as well, but it's a little outside the scope of what we're doing here.
[21:50] So I'm just going to set my scale of this material to be 237 centimeters or two and a third meters.
[22:00] So now I have my material set up.
[22:03] I've got my dirt and my roots and I can pass this material into my blend network here into the B slot.
[22:14] So I'm bringing in my RVT mask here and I'm using it to blend between my grass and my roots and dirt material.
[22:31] So I'll save this and we'll switch back to our landscape and see what we get.
[22:36] And now, take a look.
[22:40] So we've got our trees and underneath each tree is an area where I've got roots and dirt.
[22:49] And you guys, I think this is just fantastic.
[22:52] The really cool thing about it is if I take my PCG graph here, I'm just going to tear this off and float it.
[23:00] So here we have our landscape.
[23:02] Here's our complex PCG graph.
[23:05] Here's the node that creates points on the surface and I can change this node and rescatter my trees really easily.
[23:14] So this is my random seed that's determining where all the trees are placed and kind of the entire graph is based off of that one seed.
[23:24] So if I change the seed to any other arbitrary number, it's instantly going to come up with a new tree placement for me.
[23:34] And my runtime virtual texture is going to update and that wherever that dirt and roots go is going to automatically go with these trees.
[23:45] So every time I switch my random seed here, it's going to regenerate a different configuration of trees.
[23:58] And the dirt that is with those trees is going to just automatically update right along with it.
[24:06] And to me, this is just super cool.
[24:08] I just love this stuff.
[24:10] Okay, now we have our dirt spawning underneath our trees and it looks pretty good.
[24:19] But there are a couple of bonus features that I want to give here at the end of the video to improve the look.
[24:27] So let's switch back to our landscape material here and I want to just wire our, I want to wire our mask into our color again and just take a look at our landscape.
[24:40] So you can see here, I'm just going to set this to base color so we can just see the mask.
[24:47] You can see this mask is really chunky and there are a couple of things that we can do to improve this.
[24:54] If I change the mask so that it's white in the center and then falls off to black at the edges, we can use a height, Lerp blend to blend between our dirt root material and our grass material around it.
[25:10] And that's going to look a lot nicer.
[25:12] So let's go ahead and do that.
[25:14] So when we set up our tree material to write into our runtime virtual texture, we just set it temporarily just to a solid value of one.
[25:25] But we can do a lot better than that.
[25:28] What we want to do is make it fall off so that right in the center, it's going to be white and then it gets darker as it goes out to the edges.
[25:37] So let's go ahead and do that.
[25:39] The first thing that we need to do is create a local position node.
[25:45] So what this node does is it gives us the position local to the pivot point of the tree.
[25:53] And we don't really care about the tree height.
[25:56] We're just kind of rendering the tree from top down into our RVT.
[26:01] So if I take the X and the Y coordinates and I find the length of those X and Y coordinates, what this is going to do is tell me how far away from the center of the tree from the top down are we currently.
[26:18] And now I just need to do a few things.
[26:20] So this is going to give me a mask that's black in the center.
[26:24] And as we get further away from the center, it's going to turn white.
[26:28] But we just need to do a few things to adjust this mask so that it will be so that it will work well for our case.
[26:36] The first thing that I'm going to do right now, the mask is black in the very center.
[26:41] And I'm going to subtract 40.
[26:44] And what this is going to do is give us an area of about 40 centimeters right around the center of the tree that is going to be solid white.
[26:55] Now it's black right now, but we're going to flip it white at the end using a one minus.
[27:01] So I'm going to subtract 40.
[27:05] And then I'm going to multiply by 0.007.
[27:12] And then I'm going to saturate the result of this just to clamp it between values of zero and one.
[27:19] And then finally at the end here, I'm going to use a one minus to flip it around.
[27:24] So now it's going to be white in the center and then getting darker as we move away.
[27:30] So I'm going to plug this into our mask for hit save and we'll switch back to our landscape.
[27:36] And now you can see instead of just a solid mask, I actually have a nice fall off gradient where it's white in the middle and it falls off and gets darker toward black on the outside.
[27:48] Really nice. So let's switch over to our landscape material again.
[27:54] So here's where our mask is coming in.
[27:58] And what I want to do is use a height lerp.
[28:03] And this is going to allow us to blend using the height of our dirt and root material.
[28:13] So if I open this material here, you can see that the alpha channel here is the height data and the roots are white and then the dirt is kind of a darker color.
[28:24] So the dirt in between.
[28:25] So this is showing how far away from the surface is each pixel and my roots are kind of bumping out and everything else is a little bit darker.
[28:35] So what we want to do is blend using our height here.
[28:40] So on our height, we're going to for a transition phase, I'm going to plug our mask that we created here into the transition phase.
[28:51] For the height texture, I'm going to plug the height of our trees and then for the contrast, I'm going to give that a value of one.
[29:02] And so let's take a look at the mask that we just created using our height lerp.
[29:07] If I grab the output of our alpha here and drag it over, I'm just going to wire that into our base color now and save it.
[29:16] Now we can take a look at our landscape again.
[29:19] And now you can see I've got a solid mask here in the center.
[29:24] And then as we fall off, our height map from our material is breaking this up.
[29:30] So you can see I've got these roots sticking out of the sides and we get a much more detailed mask.
[29:38] So let's use that mask to now blend between our grass material and our dirt and roots material.
[29:48] So here's our alpha channel coming out of our height lerp and we can just wire that now directly into our blend material attributes node.
[30:00] So now you can see those roots from the material stick out nicely and kind of blend with the grass around them.
[30:07] And it just gives us kind of a more realistic mix between the dirt and roots and the grass.
[30:15] All right, very cool.
[30:17] Now there are a couple of more things that we can do right now.
[30:21] Our landscape is creating puddles.
[30:24] But the puddles and the dirt and roots material don't really interact with each other very well.
[30:31] And I think it would be more natural if we used our dirt and roots material to get rid of puddles.
[30:40] So wherever we have puddles right up against a tree, let's go ahead and change our shader so that we can remove those.
[30:48] So I'm going to switch back to our terrain material here.
[30:51] Here's our material function that's creating our puddles.
[30:55] And right now we have a mask that determines where the puddles can go.
[30:59] And it's just set to one.
[31:01] And so what I can do is come over here to the result of our height lerp.
[31:07] And I'm just going to add a one minus here to flip this mask around.
[31:11] Because right now this is going to be white where the dirt and the roots are and black where they're not.
[31:17] And I want the inverse of that.
[31:19] So I'm going to use a one minus node.
[31:22] And I'm just going to plug this in as our puddle mask so that wherever the grass, so that wherever the root and dirt is,
[31:34] we're going to remove the puddles from our environment.
[31:38] So now you can see we've got our dirt here and our roots.
[31:42] And we have puddles, but they don't actually come right up to the base of the trees.
[31:49] Alright, that's pretty cool.
[31:51] Now the other thing that we can do is we're using the logic in our material to determine where our grass can grow.
[32:01] And we're doing that right here.
[32:04] So this is the base grass mask that we created a couple of episodes ago.
[32:09] And we want to do something very similar with what we just did with the puddles.
[32:13] Where we multiply our grass mask by the inverse of our roots and dirt.
[32:24] So that we can get grass to not grow in the areas that are right around our trees.
[32:30] So I'm just going to wire this in here.
[32:33] Now when we switch back to our landscape.
[32:35] Now we've made it so this grass that's growing here will never grow in the areas where we have dirt and roots.
[32:47] Alright, so we've masked out our dirt and roots from our puddles and from our grass.
[32:52] And there's one more thing that we're going to do right here at the end of the video.
[32:57] And that is we can also use this runtime virtual texture mask that we've created to actually deform our terrain.
[33:05] Now one thing that trees do is the roots grow into the soil and they grab onto the dirt and they bump it up a little bit.
[33:17] And so if we want our trees to feel fully integrated with the landscape.
[33:22] What we can do is create a mask that allows us to offset the terrain just a little bit.
[33:31] So it's being bumped up and deformed by the roots of the tree.
[33:36] So let's go ahead and do that.
[33:38] The first thing that we need to do is come over here to our tree material where we're writing the mask.
[33:48] And this is that gradient that we just created where it falls off from white to black as we get away from the center of the tree.
[33:56] And what I'm going to do is add an append many node here.
[34:00] Our mask for input here is actually it actually has four channels.
[34:06] So if we wanted to we could write four different masks from our tree into our runtime virtual texture.
[34:13] Right now we're only using one of them.
[34:16] This is a mask that goes from white to black from the center of the tree out to the edge.
[34:22] And now if we want to we have the opportunity to write three other masks.
[34:29] Well we don't have to actually need three masks.
[34:32] We just need one more and this is the one that's going to bump up the the bump up the landscape around the trees.
[34:40] So I'm going to take our local position length just like we had before.
[34:44] And this time I'm going to subtract 15.
[34:49] This is going to be a smaller ring than this one is.
[34:53] So I'm going to subtract 15 and then I'm going to multiply it by 0.01.
[34:59] And then again I'm going to saturate and one minus here.
[35:04] So now we've got a slightly different mask and we'll write that into the green channel.
[35:10] So let's hit save here.
[35:12] And if we come over here to our content drawer now if you look at our terrain tree dirt mask here you can see that I'm writing a different color into the red channel that I am into the green channel.
[35:25] And if we come here to our landscape material for our mask for here I can create another component mask and set this one to green.
[35:37] And now I'm pulling in the smaller mask that I can use to offset the ground around the trees.
[35:47] Let's go ahead and plug this mask directly into our color again just so we can see what it looks like.
[35:53] And so this is the mask that we're going to be using to deform the ground around the trees.
[35:59] So yeah let's go ahead and do that.
[36:02] So I'm going to create an append many node and this is going to be our X, Y and Z offset for our world position offset.
[36:15] And I just need a value of 0 in our X and our Y because I don't want to move vertices around on the horizontal plane.
[36:24] I only want to move them vertically.
[36:26] So I'm going to take that mask that I just created.
[36:29] I'm going to multiply it by a value of 35.
[36:34] This is in centimeters by the way so I'm just bumping up the terrain just a little bit.
[36:39] 35 centimeters where it's solid white and I'll plug that into the Z or the B channel here.
[36:48] And now I can take that RGB value that I created and we can plug this into our world position offset.
[36:56] So I'm going to move this over here.
[36:58] There's our world position offset input pin and I can just wire my RGB value from that.
[37:05] And that's going to take that mask that I just created and it's going to use it to bump up our terrain.
[37:11] So let's save this and we'll switch back to our scene.
[37:17] And now you can see that right around the trees our terrain is being lifted by the roots of the tree.
[37:25] Let's go ahead and switch our material back to the normal view.
[37:29] Yeah, so right around each of the trees our landscape is being lifted so that it's a little bit more of a natural blend with the trees themselves.
[37:41] And so wherever there's a tree I'm kind of bumping up the landscape right around it so that that tree feels like it's grounded and it's connected to the landscape and it's fitting in.
[37:53] So I've got dirt, I've got roots and I've got the landscape kind of bumping up where the tree is grabbing the landscape and pulling it up just a little bit.
[38:03] So we've successfully blended our trees in with our landscape and feel that made them feel a lot more connected and natural.
[38:13] Let's go ahead here just at the end and switch over to our mannequin and run around the level just a little bit so we can see kind of the results of our work.
[38:26] So we've got our trees blending into the landscapes. They are masking out the puddles correctly.
[38:34] No grass will grow right around the base of our trees and we've done a great job of connecting and blending the trees in with the rest of what's happening in our landscape.
[38:50] I don't know about you guys but I just think this stuff is super cool and I'm excited to share it with you.
[38:55] So I hope you enjoy this video. We're going to do some continue doing some more PCG work next week.
[39:01] So be sure to come back for that one. In the meantime, have a great week everybody.
[39:19] .



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
