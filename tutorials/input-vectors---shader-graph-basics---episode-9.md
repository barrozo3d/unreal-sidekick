---
title: Input Vectors - Shader Graph Basics - Episode 9
source: YouTube
url: https://www.youtube.com/watch?v=lrc-j7ub28U
author: Ben Cloward
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/input-vectors---shader-graph-basics---episode-9/
frame_count: 0
frame_status: pending-selection
---

# Input Vectors - Shader Graph Basics - Episode 9

**Source:** [YouTube](https://www.youtube.com/watch?v=lrc-j7ub28U)
**Author:** Ben Cloward
**Duration:** 27m29s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py input-vectors---shader-graph-basics---episode-9 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Core Concepts [0:00]
**Transcript (timestamped):**
[0:00] Today, we're going to talk about input vectors.
[0:02] Let's go.
[0:09] Before we jump into using input vectors in Unreal 5 and Unity,
[0:14] I want to step back and talk about the core concepts
[0:16] and illustrate the principles a little,
[0:19] so you'll understand what's going on once we start using these things.
[0:23] First of all, it's important to understand what a vector is.
[0:28] A vector is basically a line between two points.
[0:31] It has a start point and an endpoint or a direction.
[0:37] In computer graphics, we use vectors to find out important information
[0:41] about the scene, like how far from the camera an object is
[0:45] or what direction the surface is facing
[0:49] and whether or not an object should be lit by a light source.
[0:53] Today, we're going to talk about three main vectors.
[0:56] The first is the surface normal.
[0:59] A surface normal, or often just called a normal,
[1:02] is a vector that's stored at every vertex of the model.
[1:07] The direction in the normal is pointing
[1:09] is the direction that the surface is facing,
[1:12] so the normal is perpendicular to the surface.
[1:15] Now, I know there's only one of them shown here,
[1:17] but it's important to know that every point on the surface of the model
[1:21] has its own normal.
[1:23] Surface normals are automatically created by the 3D software you use
[1:27] to create your models.
[1:30] The normals are always one unit long,
[1:33] which is important because many math operations like dot products
[1:38] require that the vectors be the same length.
[1:41] I'll give more details on that later.
[1:44] In the shader, you can use normals to judge the relationship
[1:48] between the model's surface and other objects in the scene
[1:51] like the camera or the lights.
[1:54] Next, let's talk about the camera vector.
[1:58] This is also sometimes called the view vector or the eye vector.
[2:03] It's a line that starts at the position of the camera in the scene
[2:07] and extends into the scene to each point that's being rendered.
[2:12] If we measure the length of the camera vector,
[2:15] that tells us how far away from the camera each point in the scene is,
[2:19] so it gives us the scene's depth.
[2:23] If we compare the camera vector with the surface normals on the model,
[2:27] it tells us what parts of the model are facing toward the camera
[2:31] and what parts are facing away.
[2:34] To do that, we need to normalize the camera vector,
[2:37] which means we're making it one unit in length,
[2:41] just like the surface normals.
[2:43] Once we have a normalized camera vector,
[2:45] we can do a dot product between the camera vector and the surface normal,
[2:50] which will result in a one or a white value
[2:53] if the surface is facing the camera and zero or a black value
[2:58] if it's facing away or perpendicular to the camera.
[3:01] I'll show you a better example of that once we jump into Unreal and Unity.
[3:06] Lastly, we have the light vector.
[3:10] If it's a directional light,
[3:12] the direction of the light vector is a constant value,
[3:15] but if it's a point light,
[3:16] then the light vector starts at the position of the light source
[3:20] and goes to the point that's currently being rendered.
[3:23] Just like with a camera vector,
[3:25] we can measure the length of the light vector to see how far away the light is.
[3:31] And we can compare the angle between the light vector and the surface normal
[3:36] to see how much illumination the surface should receive from the light.
[3:41] Because most modern rendering engines, including Unreal and Unity, use deferred rendering,
[3:47] the lighting calculations are generally done at a later stage in the rendering process,
[3:52] and so you won't need to use a light vector much at all in the materials you make
[3:56] with Shader Graph or the Material Editor,
[3:59] but it's still good to understand what they are.
[4:02] Alright, so now that we've done all of the explaining,
[4:04] let's take a look at some example shaders
[4:07] and show what you can do with the surface normal,
[4:09] the camera vector, and the light vector.


### Surface Normal [4:13]
**Transcript (timestamped):**
[4:13] Alright, so here we are in Unreal,
[4:15] and the first example that we're going to take a look at is something that you can do with just the surface normal.
[4:22] So here in Unreal, I have the vertex normal in world space.
[4:28] So I can get to that just by typing vertex here and pick vertex normal WS.
[4:34] Now, it's really important when you do operations using two vectors
[4:39] that you have both of them in the same space.
[4:42] So I have my vertex normal in world space right now,
[4:45] and don't worry, we're going to get into another video later on where we talk about spaces,
[4:50] world space, object space, tangent space, that sort of thing.
[4:53] So just trust me right now when I say that we need to have our vectors in the same space
[4:59] when we use them together.
[5:02] So for example, here I have the vertex normal in world space
[5:06] and I also have this other vector that is pointed straight up in world space.
[5:12] So I have zero, zero, and one, and this is pointed straight up in world space
[5:18] because in Unreal, up is the Z component.
[5:24] So I have zero, zero, and then one as the Z.
[5:28] So this is pointed up and I'm doing a dot product between my surface normal and the up vector.
[5:35] And what that's going to do is it's going to compare the up vector in world space
[5:41] and the surface normal of my model.
[5:44] And if the normals are parallel or pointed in the same direction,
[5:49] it's going to give me white.
[5:51] And if the normals are perpendicular, it's going to give me black.
[5:55] And then I saturate the result and we'll pass this into base color
[6:00] and emissive to take a look at what happens.
[6:02] So here you can see I've used the surface normal dot product,
[6:06] dot producted it with the up vector.
[6:09] And what this is giving me is a mask where the parts of my model that are facing up are white
[6:18] and the parts of my model that are facing down are black with a nice smooth fall off.
[6:24] Now I could adjust this with some additional math if I wanted to change
[6:28] how sharp this fall off was or that sort of thing.
[6:31] But this is really useful.
[6:33] I can use the surface normal to tell if a surface is facing up or not.
[6:39] And I could use this mask for all kinds of things.
[6:41] If I wanted to apply sand or moss to the top of my model, I could use this as my mask.
[6:50] In fact, I have another video that I created where I do just that.
[6:54] I use this technique to apply an environment material like moss to the top of my model.
[7:01] And I'll put a link to that right here.
[7:03] Go ahead and take a look at that.
[7:05] If you want to expand on this technique and use the normal to create a mask that allows you to apply materials to the tops of your models.
[7:15] Okay, an easier way of doing this in a slightly more efficient way.
[7:20] If you look at what's happening with our math here, in a previous video we talked about the dot product.
[7:26] And we talked about how you multiply the X of the two vectors together and you multiply the Y of the two vectors together.
[7:35] And you multiply the Z of the two vectors together.
[7:38] Well, if we look at this value here and we have these zeros here, these zeros, when we multiply them with the data coming from our world space normal,
[7:48] we're just going to end up with zero for X and Y.
[7:52] And then we're going to end up with Z multiplied by one, which is just going to leave us the value of the Z for the world space normal.
[8:01] So if I want to do this same operation and get the same result without actually having to compute this dot product,
[8:08] all I have to do is add a mask component node and just select the Z component.
[8:16] Because I already know that I'm going to get zero for X and Y and I'm going to get whatever the Z component of the world space normal is for the Z.
[8:26] And so I can get the same result by doing, by just grabbing the Z component of the world space normal as I can with doing a dot product with the up vector.
[8:38] All right, so I wire this into the saturate and you can see I've got the exact same thing and I didn't even have to do a dot product.
[8:46] So pretty cool. That's one use for the vertex normal.
[8:51] And there are all kinds of other things that I could do.
[8:54] I could, if I wanted to, I could mask out instead of the up vector.
[9:01] I could use the Y and now I've got a mask coming from the side or I could use the X and now I've got a mask coming from the front.
[9:15] All right, so that's our first example.
[9:17] That's a use of the vertex normal.
[9:19] And the next example, and this is one that we've seen before on the channel, we're actually going to use the vertex normal and the camera vector together.
[9:30] So let's take a look at this example.
[9:33] Here we have our camera vector, which is the vector that's going from the camera to the surface.
[9:40] And here we have the vertex normal and we're doing the dot product between these two.
[9:46] Now that dot product is going to be white when these two vectors are parallel and it's going to be black when they're perpendicular.
[9:53] So when the surface is pointing toward the camera, we're going to get a white value.
[9:59] And when it's pointing away from the camera, we're going to get a black value.
[10:03] So let's just go ahead and plug this in and see what our result is.
[10:09] And so you can see that our model is white here in the middle and then black around the edges.
[10:15] Let me just change the field of view a little bit.
[10:17] So maybe it's it'll be a little bit obvious, more obvious.
[10:21] What's going on here?
[10:24] I zoom in.
[10:25] You can kind of see that black showing up around the edges, but you'd have to be able to rotate outside of the camera to be able to see the black because the surface is pointing right at the camera.
[10:37] And we're measuring if the camera or if the surface normal is parallel or perpendicular to the camera.
[10:45] Now, the one thing that I should point out about how unreal works is whenever you do a dot product between two vectors, they need to be the same length.
[10:57] And that's why we have normal eyes.
[10:59] So we take the vertex normal and we make it a length of one.
[11:04] And then we take the camera vector and we make it a length of one.
[11:08] And then when we do a dot product, we get the results that we're expecting.
[11:12] Now, the thing about this camera vector is it's already normalized.
[11:16] So if I pass it into this normalize, plug it into this dot product, you see, we get the same result.
[11:23] So this camera vector coming in, I told you before that the camera vector went from the position of the camera to the position on the model that's currently being rendered.
[11:33] And that's true.
[11:35] But in unreal, this node for the camera vector has already been normalized.
[11:40] So it's not the full length from the camera to the position on the model that's currently being rendered.
[11:49] It's just the normalized version.
[11:51] And so we're able to get away with operations like this, where we do the dot product between the vertex normal and the camera vector without doing a normalization.
[12:01] Because the normalization has already been applied to these to these two nodes.
[12:07] Now, if we want to adjust our mask, I can use a power node here like I'm raising it to the power of three right here.
[12:13] So if we plug this in, now you can see I'm getting a little bit more black around the edges and the higher I make this value, the more toward the middle, I'm able to push the effect.
[12:28] So now that I've raised it to a power of eight, I'm actually getting more black and less white.
[12:32] So using this power node, I'm able to adjust the results that I'm getting.
[12:37] I could also use the one minus node if I wanted to do the inverse of what I'm getting here.
[12:43] So I'll pass the result into one minus.
[12:45] And what that's going to do is flip the results around so that I'm getting white on the edges and black in the middle.
[12:52] And if I do that, I'm probably going to need to lower that power back down.
[12:56] Anyway, so this second example is doing a dot product between the camera vector and the vertex normal.
[13:03] And we're getting an effect that a lot of people call a Fresnel effect.
[13:10] And I have another video where I show a really cool use of the Fresnel effect to make cloth.
[13:17] I think I've pointed out this before.
[13:19] But if you haven't seen my cloth shader video where I use the camera vector dot product, dot producted with the surface normal,
[13:29] you can check that out right here.
[13:31] I'll put that link here and also down in the description.
[13:35] All right.
[13:35] So camera vector dot producted with the surface normal gives us a mask that tells us if the surface is facing the camera or facing away from the camera.


### Camera Vector [13:47]
**Transcript (timestamped):**
[13:47] All right, let's take a look at our third example.
[13:50] And this is an example where we're going to want to take the camera vector not normalized.
[13:56] I talked about using this normalized node and making the camera vector unit length and how this one already is normalized.
[14:04] And so it's unit length.
[14:06] Well, how do we create a camera vector that actually goes from the position of the camera to the position on the surface that's being rendered?
[14:14] Let's take a look at that.
[14:15] So I'll just scroll down here.
[14:18] And that's what I've done here.
[14:19] I've created a camera vector by taking the camera's position and subtracting it from the absolute world position.
[14:29] Camera vector minus world position will give me a vector that goes from the position of the camera to the position that I'm currently rendering.
[14:39] So then if I want to know how far that is, I can use this node called length.
[14:44] And what that does is it looks at the vector that I've created here and measures how long it is.


### Camera Mask [14:51]
**Transcript (timestamped):**
[14:52] So what I'm trying to do here is create a mask that is black when the object is near the camera and white when the object is further away.
[15:01] Now, there's tons of uses for this kind of effect.
[15:04] For example, if I wanted to apply raindrops when the model was close to the camera, but fade those raindrops out as the model got further away,
[15:14] I could do that with this example.
[15:16] Also, if I wanted to add a detailed texture to my surface, but then fade that texture out as the model got further away from the camera, this is how I do it.
[15:28] I take the camera position and I subtract the absolute world space position to get the camera vector.
[15:36] Then I measure the length of that vector and then I have two nodes here that adjust the results.
[15:43] What this one does is subtracts a hard coded value or I could expose this as a parameter.
[15:51] And this parameter controls how far away the effect starts from the camera.
[15:56] So if I gave this a value of zero, my fall off mask would start right at the camera and begin to fall off right there.
[16:05] But I've given it a value of 500, which means that my mask will be perfectly black from the point of the camera up to five meters.
[16:16] And then the fall off will start at that position.
[16:19] Now this next divide node here, I'm dividing the result by 5000, which means that from that point where the fall off starts at five meters,
[16:30] it's then going to take 50 meters to go from a value of black to a value of white.
[16:36] So this value here that I'm dividing determines how long or how far into the distance the mask is.
[16:44] So this is my offset and this is my mask length.
[16:48] Well, let's go ahead and move these nodes up and we'll take a look at the result that we get from this technique.
[16:54] So I'm just going to plug this into the base color and also plug it into the emissive color.
[17:03] So here you can see that my sphere is black and then I can zoom out.
[17:09] And as I get to about five meters, you can see that now it starts turning white.
[17:14] And from here to about 50 meters, it's going to go from black to white.
[17:22] So about here, it's a solid white.
[17:24] Then as I zoom in again, you can see that the closer it gets to the camera, the darker it gets.
[17:32] And so I'm doing this again by measuring the length of the vector between the camera position and the model's position
[17:40] and then giving a value that determines where the fall off starts and then how long the fall off lasts.
[17:48] So by measuring the length of the camera vector, I'm able to create this cool fall off mask that then I can use to do all kinds of things
[17:57] that I want to fade out or fade in when they're close to the camera and fade out when they get further away.
[18:05] All right, let's take a look at one last example.
[18:08] And in the diagrams at the beginning of the video, we had the light vector node.
[18:12] So I wanted to show you there is a node in Unreal called the light vector node.
[18:17] And here I've done a dot product with the light vector node and the vertex normal.
[18:23] So what this is going to do is show you how parallel or perpendicular the surface of the model is with the light.
[18:32] But the problem is if I take this node and I plug it into my shader, now you can see that I'm getting this error.
[18:39] And if I mouse over the area, you can see it says light vector can only be used in a light function or a deferred decal material.
[18:47] And what that means is basically Unreal is trying to tell me, hey, we're using a deferred renderer here
[18:55] and we don't want you to do lighting calculations in your material.
[19:00] Basically what this is doing is diffuse lighting.
[19:03] And I don't really need to do diffuse lighting because the engine does that for me.
[19:08] If I disconnect these nodes here and switch to lit mode, you can see that I've got diffuse lighting going on already.
[19:17] And that happens in the G buffer later on in the rendering than what I'm doing here when I'm defining my materials.
[19:25] So even though there is a light vector node available, you can only use it in certain conditions where you're not rendering into the G buffer.
[19:34] So if I were creating a decal or some other kind of material where I wasn't rendering into the G buffer, but I wanted to do lighting,
[19:44] I could do this operation here where I'm doing a dot product between the light vector and the vertex normal.
[19:51] And similar to this dot product here, what this would give me is a gradient that was white when my surface is facing the light
[20:01] and black when it was facing away from the light.
[20:04] And that would tell me how much the surface should be lit by that particular light source.
[20:09] So this is a cool technique, but it's only really applicable if you're creating some kind of weird exotic material that's not rendering into the G buffer.
[20:21] All right.
[20:22] So those are our examples from Unreal.
[20:25] And now let's switch over to Unity and take a look at the examples there.


### Unity [20:29]
**Transcript (timestamped):**
[20:29] All right.
[20:30] So here we are in Unity in Shader Graph.
[20:33] And we're going to take a look at those same three examples, but I want to show you a couple of differences,
[20:39] where Unity and Unreal are slightly different.
[20:42] Okay.
[20:43] So in our first example, we're taking our surface normal and we're using the split node to isolate the G or the Y component of the surface normal.
[20:54] And then we saturate that.
[20:56] And if we plug this into our shader, we're going to see is that same up facing mask that we got in Unreal.
[21:04] So we're taking the Y component of the normal and we're passing that in and it's giving us this up facing mask.
[21:14] Now, the part that I want you to notice here is if I open up my split node, you can see that I'm taking the G component, which is the same as the Y.
[21:25] Whereas in Unreal, I was taking the Z.
[21:29] And that's because in Unreal, we're looking at an up vector that's using the Z and in Unity, Unity is Y up.
[21:40] So we've flipped this thing on its head and we're using the Y axis as our up vector instead of the Z axis as our up vector.
[21:47] So those are two different ways of doing the same thing.
[21:51] They're just different in the different engines.
[21:53] So when you're in Unity, if you want to use up, make sure that you're using Y.
[21:59] OK, so that's our use for the normal vector to create masks.
[22:03] And just like we did in Unreal, you know, you could use the other component to create a front, back mask or a left, right mask.
[22:12] All right. For our next example, we've got the Fresnel term that we created in Unreal.
[22:19] And the one difference here is I want to point out that I'm doing the dot product here between the normal and the camera direction node.
[22:29] So here I've got my camera node with all of its different parameters for the camera and I've got my camera direction coming out of here.
[22:36] But the one difference here between Unreal and Unity is that in Unity, this camera direction is inverted.
[22:45] And so if I want to do a dot product between the surface normal and the camera vector and get the Fresnel term,
[22:52] I actually have to add a negate node in here to reverse the direction of the camera vector in order to be able to perform this operation.
[23:02] So here's my normal, my surface normal, my camera vector negated and I've got my dot product.
[23:08] So if I pass this in, this results into the root or into my master stack, rather,
[23:16] you can see that now I've got white in the middle where the model is looking right at the camera.
[23:21] And then it falls off to black around the edges.
[23:25] And I know that isn't super obvious, which is why I've added this power node in here to kind of increase the contrast.
[23:33] So you can see that a little bit better.
[23:35] Now you can see it.
[23:36] You can see the black on the edge and the white where the model is facing right at the camera.
[23:42] And again, just like we did in Unreal, I can use the one minus node to invert the results and get white on the edges and black in the middle.
[23:52] Just like that.
[23:54] All right.
[23:54] So that's dot product with the surface normal and the camera vector.
[24:00] And for a final example, I've done the same thing here that we did in Unreal where I'm casting a ray or the vector from the camera to the position on the model.
[24:11] So I do the camera minus the model's position.
[24:17] Then I measure the length of that ray that I've cast with this operation.
[24:22] And then here I'm doing the subtract to offset from the the camera position.
[24:29] And I'm also doing the divide to determine how far that mask is going to be.
[24:34] So this is going to give me a mask that starts out black close to the camera and fades out to white the further away from the camera that I get.
[24:44] So this value right here is in meters.
[24:47] And so what this says is I'm going to have black from starting at the point where the camera is up to 9.5 meters.
[24:57] And then from that point to 0.7 meters later, I'm going to fade from black to white.
[25:04] And so if I plug this in, you can see that on my sphere here.
[25:10] This point is the spot on the sphere where we're about 9.5 meters away from the camera.
[25:16] And then you can see that we go for about 0.7 meters around to the side of the sphere.
[25:21] And at this point on the sphere, we're about 0.7 meters further into the scene.
[25:29] Now, if I zoom out a little bit, you can see that as my sphere gets further away, it goes completely white.
[25:36] And if I zoom in, you can see that getting closer to the camera, I become black.
[25:42] So this set of nodes here where we're subtracting the camera position from the world space position and then measuring the length gives us how far away from the camera we are.
[25:58] And then we can adjust the mask to be exactly what we want, starting the distance away from the camera with this 9.5 value here and then dividing by the length that we want our mask to be so that the mask goes from the spot in the scene where we want it to start and then the spot in the scene where we want it to end.
[26:20] So pretty cool.
[26:21] We've got an up vector mask using the surface normal.
[26:26] We've got a Fresnel mask using the surface normal and the camera dot product together.
[26:33] And then we've got a camera distance mask where we create the camera vector and then measure the length.
[26:41] So just like we did in Unreal, we've got the same effects in Unity.
[26:45] And this is a pretty good basic summary of using both the normal vector and the camera vector.
[26:52] All right, that'll about wrap it up for today's video.
[26:55] I hope you enjoyed this one and that you learned something new about input vectors, normal vector, camera vector, and maybe a little bit about light vector too, although we don't use that one too often.
[27:07] All right, be sure to come back next week and we'll talk about more shader goodness.
[27:12] And in the meantime, have a great week, everybody.



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
