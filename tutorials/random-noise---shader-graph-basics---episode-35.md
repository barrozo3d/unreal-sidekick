---
title: Random Noise - Shader Graph Basics - Episode 35
source: YouTube
url: https://www.youtube.com/watch?v=5v6tvkb63XU
author: Ben Cloward
ingested: 2026-07-20
ue_version: "Not specified (UE5.x)"
tags: [materials, shaders, pbr, blueprint, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/random-noise---shader-graph-basics---episode-35/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Random Noise - Shader Graph Basics - Episode 35

**Source:** [YouTube](https://www.youtube.com/watch?v=5v6tvkb63XU)
**Author:** Ben Cloward
**Duration:** 27m17s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Today, I'm going to show you how to create and use a noise hash. Let's go!
[0:11] So we're actually going to do two things in today's video. I'm going to show you how to create a noise hash,


### Create a Noise Hash [0:15]
**Transcript (timestamped):**
[0:17] and then we're going to use it to improve the interior mapping shader that we've been working on.
[0:23] If you're interested in interior mapping, go back and watch last week's video that shows the
[0:29] core of the technique. Today we're going to be expanding on it. Before we start work on the noise,
[0:37] I first want to show you why we need it. There are a lot of uses for noise in shaders, but today


### Why We Need It [0:38]
**Transcript (timestamped):**
[0:44] we're going to be using it to randomize the rooms in our virtual interior. Right now, our shader just
[0:51] has a single room, and so we need to add a parameter to control how many rooms we want.
[0:58] This is really easy. All I have to do is add a VEC2 parameter. I just hold down the 2 key
[1:05] and click the left mouse button like that. And then I can use this parameter to multiply by my
[1:13] incoming texture coordinates. And then I can type in the number of rooms that I want
[1:21] vertically and horizontally. So let's say that I want a grid of 4x4 rooms in my building. I can
[1:29] just type in 4 and 4, multiply that by my texture coordinates, and then pass that value in. And now
[1:38] I have a building with 4x4 interior rooms. And like I said, if you didn't see last week's video,
[1:45] be sure to go back and watch that to take a look at how I created this illusion that my
[1:52] preview cube here has an interior. So I can use this value here to control how many rooms
[2:00] we're adding. And if I add 8x8, you can see that now I have a pretty big building with tons of
[2:07] rooms in it. But what you can see here is you can start to see the reason that we need a noise
[2:15] hash. Right now, every single one of my rooms in this building looks exactly the same. They're all
[2:22] using the one value for the back wall, the four value for the left wall, and the three value for
[2:30] the right wall. So all of these rooms are exactly the same as all of the rest of them. So my building
[2:37] would look a lot more realistic if I could randomly choose to use the 1, 2, 3, or 4 as the back wall
[2:45] and make the other walls random as well. So that's what we're going to be doing today. I need to create
[2:53] a way to generate random numbers so that I can mix up which wall is showing on each of the sides
[3:02] in each of the individual rooms. And that's what a noise hash is for. So noise hash is basically a
[3:09] random number generator. We take incoming data like our UV coordinates here, and we scramble it up so
[3:17] that it's random, so that as random as we can make it. It's tricky because we have to do this
[3:22] scrambling in a way that doesn't create a repeating pattern. Alright, so let's go ahead and get started.
[3:28] I'm going to open up my content drawer here, and I'm going to right click and pick a new material
[3:37] function. And I'm going to call this function hash 2, 3, and I'm calling it 2, 3 because we're inputting
[3:46] a vector 2 value, our texture coordinates here, and we're going to get a color, a random color,
[3:52] which is a vector 3 value out. So here's my brand new hash 2, 3 function. I'm just going to dock it
[4:02] right here. And we're going to get started building. So the first thing that we need is our input value.
[4:09] So I'm just going to do a filter for input and bring in a function input. And down here, we're
[4:16] going to set our function input to be a size of vector 2, because it's going to be taking in our
[4:23] UV coordinates. Now by default, I can just add the regular texture coordinate node as my default
[4:32] input. So I'm just going to wire my texture coordinate node into the preview socket here
[4:38] so that when it's not connected, it'll use the regular texture coordinates as default.
[4:45] Okay, so we need to take these texture coordinates and just scramble them all up. Right now,
[4:50] they look really nice and uniform. I got this beautiful gradient going from black to red
[4:55] and from black to green. And I want to just mix these all up as much as I can. So the first thing
[5:02] that I'm going to do is create two component masks, one for the red channel or the U coordinate


### Component Masks [5:03]
**Transcript (timestamped):**
[5:11] and one for the green channel or the V coordinate. And now I'm going to make three unique
[5:18] three channel vectors using just these two input coordinates. So I'm going to use my append many
[5:24] node. And I'm going to create three of these vectors. So I'm going to create three append many
[5:30] nodes like this. So now I just need to build my three vectors. And so the way that I'm going to do
[5:38] this is x, y, x, y, x, x and x, y, y. So basically making three, three vectors out of a VEC two.
[5:51] So I'm going to do x, y, x. And I'm going to do y, x, x. And then I'm going to do x, y, y. So I
[6:09] basically just scrambled up my two incoming vectors in three different ways. And now for each of these,
[6:19] I'm going to do a dot product between the vector itself and sort of a semi random number.


### Dot Product [6:20]
**Transcript (timestamped):**
[6:31] So for each of these, I'm going to do a dot product. I'm going to create those random numbers in a
[6:37] second. But first, I want to do another append many. And I'm going to use each of these as the x,
[6:49] y, and z components of a new vector that I've created by these vectors that I've scrambled up.
[6:58] All right, so for each of these, I need another random number. So hold down the three key and click
[7:05] to create three kind of random number values. So for this first one, I'm going to use a value
[7:18] of 127.1, 311.7, 74.7. And for my next one, I'm going to use 269.5, 183.3, and 246.1. And then
[7:38] finally, I'm going to use 113.5, 271.9, and 124.6. All right, so I'm just going to do a dot product
[7:50] between these random number values and the vectors that I created. Just give myself a little bit more
[7:59] space here and finish up these dot products. Okay, so you can see how I've scrambled up the
[8:10] components of my incoming UV coordinates. And then I've done three dot products with these kind of
[8:16] semi random number values. And then I've brought the results of those back together. Now I'm going
[8:24] to do a little bit more scrambling up, I'm going to take the result here and pass it through a
[8:32] sine function. And then I'm going to take the result of that and multiply it by another kind
[8:41] of semi random number. So this number is 43,758.5453123. Can't get much more random than that. So we're
[9:00] going to multiply the results of our sine here with that crazy number. And then for the result of
[9:08] everything, we're going to do it, we're going to pass it through a frack node, which will return
[9:16] just the decimal portion. So if there are any integer values there, or whole numbers, it's
[9:21] going to drop those off and just just return what's on the right side of the decimal, just the
[9:29] decimal value. Okay, so we'll pass this into our output result. And you can see that I'm getting
[9:38] some really nice random noise. I don't know how well that's going to show up on YouTube. I can see
[9:46] it pretty well that there's this kind of random scrambled noise here, but it's possible that the
[9:51] YouTube compression algorithm will get rid of that. We'll just have to see. But basically what I've
[9:59] done is I've done, I created three vectors out of my incoming UV data, then I dot producted them with
[10:08] random numbers, pass them through a sine and multiply by this other really crazy random number.
[10:15] And the result of that is a noise hash, which basically takes my really nice, beautiful,
[10:23] gradient incoming data. And the result is something that's really random going out.
[10:33] And that's what I need to create the effect that I'm looking for in my interior cube mapping effect.
[10:40] But there's also a lot of other applications that we can use this data for. We're going to be
[10:46] looking at another application of this maybe next week or the week after as we continue to expand
[10:53] our interior cube mapping effect. Okay, so I'm going to go ahead and save this and we're going to
[10:59] bring it into our cube mapping shader and I'm going to show you how to use it. All right, so here we
[11:05] are back in our interior mapping shader. And I just need to add that hash material function that I
[11:10] created. So I'm going to open up my content drawer again, and add my hash two three function. Now the
[11:17] function takes a VEC two for an incoming vector. And so I'm going to take my texture coordinates
[11:26] multiplied by my room count value here. And the first thing I need to do is add a floor node,
[11:36] which is basically rounding down. So I'm rounding down my texture coordinate values. Then I'm going
[11:46] to pass that into my hash two three. And that's going to give me random numbers based on my incoming
[11:55] UV coordinates. Okay, and then once I have this random data, I'm just going to connect this to
[12:02] my base color here really quick so that I can show you what we're getting. So because we're passing in
[12:09] our UV coordinates rounded down, you can see that I get for each individual room in my building,
[12:15] I get a random color. And in order to make this random data a little bit more useful,
[12:23] instead of just a random color like this, I want each room to have for the red, green,
[12:29] and blue channels of the random value, I want those to either be zero or one, not just some
[12:36] random number. And so instead of using the hash two three data as it is, I'm going to add a round
[12:45] node here, so that we round either up or down, so that each of my red, green, and blue channels is
[12:52] going to either be, it's either going to be zero or one. All right, now I need to use this random
[13:01] data. And what I'm going to do, I'm going to use it for two different things. I'm going to
[13:06] choose a random side or a random wall to be the back and the sides. And I'm also going to
[13:14] randomize whether or not to mirror the wall, so that it's showing the inverse of what it is. And
[13:23] I'll get even more random values that way. So in order to do that, I'm going to add another
[13:29] split components node. And now I need to set up my random mirroring. So in order to randomly mirror


### Random Mirroring [13:35]
**Transcript (timestamped):**
[13:40] each of the sides, I need to add a couple of Lerp nodes here. And I'm going to add a couple more of
[13:50] these VEC3 values. So for each of the VEC3 values, I'm going to set them up to be 1, 1, 1. And then
[14:03] each of them, I'm going to choose various of these ones and invert them and make them negative. So
[14:14] I'm just going to wire these 1, 1, 1 values into my Lerp. And down here on this Lerp as well.
[14:28] And now we're going to negate some of these. So on this first one, I'll negate the first value.
[14:34] I'll just make it negative 1, 1, 1. The second one, I'll negate the second value. So 1, negative 1, 1.
[14:44] This third one, I'm going to leave it as is 1, 1, 1. And then on this bottom one,
[14:49] I'm going to change it to negative 1, 1, 1. Okay, so we're all set there. And now I'm going to
[15:00] Lerp between these based on my random numbers. So here's my random number from the red channel
[15:06] that I'm wiring into the first alpha here and the random number from my green channel that I'm
[15:12] wiring into the second alpha here. So now I've randomized whether or not I'm using negative 1,
[15:18] 1, 1 or 1, negative 1, 1. And then the same with these as well. So I'm going to take these values
[15:27] and multiply them together. And then I'm going to multiply this data that I've just created
[15:40] by the result that's coming out of here that I'm using as my coordinates to look up my cube map.
[15:46] So I'm going to take this final value here and multiply it by my random values here.
[15:54] And let's take a look and see if we use this for our cube map lookup instead of what we are getting
[16:01] before. So right now we have 1 as our back wall and they're all not mirrored. But if we wire this
[16:11] value in here, now you can see we're either getting a 1 or a 2. And in each of those cases,
[16:21] the 1 or the 2 is either mirrored or not mirrored. So we've got some really cool random data here.
[16:27] We're using either 1 or 2 and the values are either flipped or not flipped. Well, we can go even
[16:36] further and do even a little bit more randomization. We can use the 3 or the 4 also as the back wall.
[16:45] So let's go ahead and do that. We're going to add one more lerp here.
[16:50] And I'm going to blend between this and the swizzled version of this. So if I add a swizzle node,
[17:03] then I can take the swizzle, I can switch x, y, and z for y, x, z. And so this is going to flip it
[17:12] so that the front and the back and the sides are swapped. And I'm going to use my third random value
[17:21] here coming out of my hash to determine whether or not to swap the front and the back with the
[17:30] sides. So I'm going to take this third value and plug it into my lerp node here so that I'm either
[17:38] swizzling those values or not based on that third random number. And now if I take this and plug it
[17:44] into my cube map, now you can see I've got tons of randomness going on. For every room, I can either
[17:53] use 1, 2, 3, or 4. And for each of those, I can either mirror it or not. So what this does is it
[18:02] makes each individual room look unique in my building. And it gives me a lot more realistic looking
[18:11] results. All right, so we still have a long way to go for our interior mapping effect,
[18:18] but we have managed to add a really nice randomness to it in this week's video. Next week, we're going
[18:25] to take a look at how to create textures and actually create the shader that makes the building
[18:32] look like a building instead of a bunch of randomly mirrored 1, 2, 3, and 4 numbers. So we're going to
[18:40] add a little bit of polish to our shader and make it actually achieve the effect that we're going for.
[18:48] All right, so the next thing that we need to do in today's video is switch over to Unity.
[18:53] And I'm going to show you how to do the same effect there with our hash values and our random
[19:00] numbers to make a more realistic looking interior. So let's switch over to Unity and take a look at
[19:06] this there. All right, here we are in Unity. And I'm going to walk you through the changes that I've
[19:11] made in Unity, similar to the changes that I made in Unreal to create the randomized room effect.
[19:19] Okay, just like we did in Unreal, the first thing that I did is add a multiply node here
[19:25] so that I'm multiplying my UV coordinates by the number of rooms that I want. In Unreal,
[19:31] we were doing eight rooms. So you can see how I can increase my multiply values here and select
[19:39] how many vertical and horizontal rooms that I want to create in my building.
[19:45] All right, the next thing that I did is I started working on our randomness portion of the shader
[19:51] here. You can see that just like in Unreal, I took the floor of my UV coordinates. And then I also
[19:58] created a subgraph in Unity called hash two three. So let's open that up and take a look at it. So
[20:06] here is a subgraph in Unity. And in order to create an input for a subgraph in Unity, I need to use
[20:12] the blackboard. So here's my blackboard here. And I can just hit the plus button and then choose
[20:19] what size or type of data that I want to bring in. And in this case, I was going to be using my UV
[20:25] coordinates. And so I created a vector two variable. And I named it UV. And then I grabbed that value
[20:32] and dragged it into my graph like this. And I took my incoming UV values and I used the swizzle node
[20:41] to arrange them as x y y y x x and x y y. Oh, looks like I made a mistake here. This should be
[20:55] x y x x y x x and x y y. Then I took the dot product of my swizzle and these crazy
[21:06] number values here 127.1, 1, or 311.7, 74.7. And for my second one,
[21:16] 269.5, 183.3, and 246.1. And then for my third one, 113.5, 271.9, and 124.6. These are just kind of
[21:32] random numbers to multiply or to do a dot product with my data. Then I combined the results
[21:41] and I passed that through a sine wave. And then I multiplied that by my other crazy number,
[21:48] which is 43,758.5453123. Maybe I'll put these values down in the description. So it'll just
[21:58] be easier for you guys to copy and paste them. Then I passed the result through the fraction
[22:04] node and output the result in an output called hash. Now, when you're controlling the output
[22:11] in Unity, you use the graph inspector. So here's my graph inspector. You can see that I have


### The Graph Inspector [22:12]
**Transcript (timestamped):**
[22:18] one output that's called hash and it's a vector three. One thing that I forgot to mention and
[22:26] unreal is when you're using the sine node to create a hash function like this, sine can be
[22:33] different depending on which platform you're on. So if you're running this data on a Mac,
[22:38] or if you're running it on a mobile device, or if you're running it on PC,
[22:42] you might get different results. So this hash function is what we call a non-deterministic
[22:49] hash function. That means different graphics hardware might interpret it differently. And
[22:55] you might get different results out of this hash function depending on what platform you're running
[23:00] it on. The other problem with using sine is that different graphics hardware has different ways of
[23:09] optimizing the sine function. And sometimes if you give this, if you give this hash function a
[23:17] really large value, it can break down and start exhibiting patterns. The goal of a hash function
[23:24] is to not have patterns. But this one does show patterns if you give it really large numbers.
[23:30] However, I happen to know that in the use case of a building, we're only using very small numbers.
[23:36] And so this one works. But if you are using your hash function on lots of different platforms,
[23:42] and you're passing it in really large values, you might want to look around for a more robust,
[23:50] deterministic hash function that can handle those kind of edge cases. In our case, we don't need that.
[23:59] But in some cases, you might need to use a stronger, more robust hash function.
[24:07] All right, so back in our shader, we pass our floored UV coordinates into our hash function.
[24:13] And then we round the results. So for each channel, we're either getting one or zero.
[24:20] Then we split those results out into the red, green and blue channels.
[24:25] And we use those random, so we get basically three sets of random numbers. And we're going to use
[24:31] the red and green random numbers to blend between our two input vectors here. So we're using a vector
[24:40] negative one, one, one, one, one, one, one, one, one, one. And then down here on the bottom,
[24:46] just our standard one, one, one, one, and then negative one, one, one, one. And so we're lerping
[24:52] between these two vectors based on our green random numbers. And we're lerping between these
[24:59] two vectors based on our red random numbers. Then we multiply our results together.
[25:06] And then we come up here and grab the values that we were using to look up our cube map.
[25:15] And we multiply those by the random values that we created. Then we use a swizzle node. And this
[25:23] is what we're doing to determine to either use the sides or the front and the back as the back
[25:31] of our rooms. So we take our result and we swizzle it Z, Y, X. And then we learn lerp between our
[25:40] regular result and our swizzle result based on our third set of random numbers from our blue
[25:46] channel here. And so then we take that, and we use that to look up our sample cube map. And we get
[25:55] results where we're using either the left, right, the front or the back. And it's either mirrored
[26:01] or not. And we got lots of randomly generated room values. Okay, now like I said, I've been using a
[26:10] cube map for displaying our results. That's just sort of this test cube map. And it just has these
[26:16] numbers mapped to it. Next week, I'm going to show you how to make a proper cube map with walls and
[26:22] ceiling and floor. And we're also going to create a texture that is used for the outside of the
[26:28] building. And we're going to finish up creating this shader so that we actually have something that
[26:33] looks like a building instead of just a bunch of random mirrored numbers. So I hope you'll come back
[26:39] next week for that. And hopefully we can finish up our interior mapping effect and put some polish
[26:46] on it. If not, we'll have to finish it up the week after I don't know if I'll have enough time in
[26:52] next week's video to fit in all of the polish things we want to do or not. But we'll see.
[26:58] All right, thanks for watching, everybody. I hope you enjoyed the video and have a great week.



---

## Captured Frames

- [1:30] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_000.jpg
- [4:30] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_001.jpg
- [5:35] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_002.jpg
- [9:40] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_003.jpg
- [12:15] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_004.jpg
- [15:05] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_005.jpg
- [17:50] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_006.jpg
- [21:05] tutorials/frames/random-noise---shader-graph-basics---episode-35/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a from-scratch **noise hash material function** (`Hash23`: Vec2 in → pseudo-random Vec3 out) in Unreal's Material Editor using scrambled component masks, dot products against "magic number" constants, sine, a large multiplier, and a Frac node — then using that hash to randomize which wall texture and mirroring state each room shows in an interior-cube-mapping shader, applied identically (with node-name differences) in Unity Shader Graph.

### Summary
Episode 35 of Ben Cloward's "Shader Graph Basics" series (27m17s), a direct continuation of a prior interior-mapping episode. Problem: multiplying incoming UVs by a room-count Vec2 parameter (e.g. 8×8) tiles a single interior-mapping "room" across a grid, but every room looks identical since they all sample the same fixed wall indices — a random-number generator per room is needed. Builds a new Material Function `Hash23` (Vec2 in, Vec3/color out) entirely from math nodes (no built-in noise texture): take the input UV, build three scrambled 3-component vectors from it via Component Mask + Append Many combinations (XYX, YXX, XYY), Dot Product each against three hardcoded "magic number" Vec3 constants (127.1/311.7/74.7, 269.5/183.3/246.1, 113.5/271.9/124.6), Combine the three dot-product results into a new vector, pass through Sine, multiply by another large magic constant (43758.5453123), and finally apply a Frac (fractional-part) node to produce the final pseudo-random 0–1 output — explicitly non-deterministic across GPU vendors/platforms (sine implementations vary) and prone to visible patterning at very large input magnitudes, but adequate for small-scale use cases like this one. Applied to the interior shader: Floor the room-space UV coordinates (so every point inside one room shares the same hash input) → feed into `Hash23` → Round each channel to a hard 0 or 1 (not a smooth random value) → use the red/green channels to Lerp between (1,1,1) and per-axis-negated vectors (feeding two Lerp nodes wired to a shared multiply) to randomly mirror the room on each axis, and the blue channel to Lerp between the un-swizzled lookup vector and a YXZ-swizzled version (swapping front/back with left/right) — multiplying the mirrored/swizzled result into the cube-map lookup vector yields a building where each room randomly shows one of 4 wall variants, independently mirrored, from a single small test cube map. Second half of the video rebuilds the identical system in Unity Shader Graph: a Blackboard-exposed Vec2 "UV" subgraph input, Swizzle nodes (XYX/YXX/XYY, with an on-camera correction of an initial mistake) instead of separate Mask+Append Many, the same three magic-number Dot Products, Sine, multiply, Fraction, and a Graph Inspector-configured Vec3 "hash" output — functionally identical to the Unreal version, wired into the same Lerp-based mirroring/swizzling logic.

### Key Steps
1. Identify the need for per-instance randomness: tiling one interior-mapping "room" via `TexCoord × RoomCount` (a Vec2 parameter) produces a repeating grid where every room is visually identical — a hash/random-number function driven by each room's UV is needed to vary wall selection and mirroring per room.
2. Create a new Material Function (`Hash23`): add a Function Input sized Vec2 (with a regular TexCoord node wired as its default preview value), representing the incoming UV.
3. Scramble the input into three distinct 3-component vectors: Component Mask the input into separate U/R and V/G channels, then use three Append Many nodes to rebuild them in different component orders (X-Y-X, Y-X-X, X-Y-Y).
4. Dot Product each scrambled vector against a distinct hardcoded Constant3Vector "magic number": (127.1, 311.7, 74.7), (269.5, 183.3, 246.1), and (113.5, 271.9, 124.6).
5. Combine the three dot-product scalar results into a new vector (Append Many/Combine), pass through a **Sine** node, then **Multiply** by a single large magic constant (43758.5453123).
6. Apply a **Frac** node to the result (keeps only the decimal/fractional portion, discarding any integer part) and wire to the function's output — this is the final pseudo-random Vec3 hash value; note it is a non-deterministic hash (sine implementations differ across GPU vendors/platforms) and can show visible patterning at very large input magnitudes, though this is not an issue at the small UV scale used here.
7. Use the hash in the interior-mapping shader: **Floor** the room-space UV (so the entire room shares one random value) → feed into `Hash23` → **Round** each output channel to a hard 0 or 1 (rather than using the raw continuous random value) → Split Components to access the red/green/blue random bits separately.
8. Random mirroring: build two pairs of Vec3 constants — (1,1,1) vs. an axis-negated variant (e.g. −1,1,1) for one axis, and (1,1,1) vs. a different axis-negated variant (e.g. 1,−1,1) for another — Lerp between each pair using the hash's red and green channels as the alpha, then multiply the two Lerp results together to get a combined per-axis mirror vector.
9. Random wall-set selection: build a Swizzle node that reorders the lookup vector's components (e.g. Y-X-Z / "ZYX" style swap) to swap which cube faces are treated as front/back vs. left/right, then Lerp between the un-swizzled and swizzled lookup vectors using the hash's blue channel as alpha.
10. Multiply the final mirrored + selectively-swizzled vector into the coordinate used to sample the interior cube map — the result: each room in the grid independently and randomly picks one of the source cube map's wall variants and independently decides whether to mirror it, producing a non-repetitive building interior from a single small test cube map.
11. **Unity Shader Graph port:** identical structure using a Subgraph with a Blackboard-defined Vec2 "UV" input, Swizzle nodes directly (instead of separate Mask + Append Many) for the XYX/YXX/XYY scrambling, the same three magic-number Dot Products, Sine, Multiply by 43758.5453123, Fraction, and a Vec3 "hash" output configured via the Graph Inspector; the rest of the mirroring/swizzling Lerp logic is ported unchanged.

### UE Systems / Blueprints / Settings
- **New Material Function created:** `Hash23` (Vec2 input → Vec3/color output), built from Function Input, Component Mask, Append Many, Dot Product, Constant3Vector, Sine, Multiply, Frac nodes.
- **Interior-shader integration nodes:** Floor, Round, Split Components (Component Mask), Lerp (×3, for mirroring and wall-set swizzle selection), Swizzle (component reorder for wall-set selection), Constant3Vector (1,1,1 and negated-axis variants).
- **Exact magic-number constants used:** dot-product vectors (127.1, 311.7, 74.7), (269.5, 183.3, 246.1), (113.5, 271.9, 124.6); post-sine multiplier 43758.5453123.
- **Key caveat called out:** hash functions built on Sine are **non-deterministic across platforms/GPU vendors** (Mac/mobile/PC can produce different results) and can exhibit visible repeating patterns at very large input values — acceptable here due to the small UV-scale input range, but flagged as a reason to seek a more robust deterministic hash for other use cases.
- **Unity equivalents:** Subgraph + Blackboard input, Swizzle node, Sine, Multiply, Fraction, Graph Inspector (output type/name configuration).

### Difficulty
Intermediate/Advanced — requires comfort with vector math, dot products, and material functions; the "magic number" hash construction is presented as a recipe to copy rather than something to derive from first principles.

### UE Version
Not explicitly stated (Material Editor node set consistent with recent UE5.x; direct continuation of a prior interior-cube-mapping episode in the same series).

### Tags
materials, shaders, pbr, blueprint, intermediate, advanced

---

## Related Entries
- `tutorials/input-vectors---shader-graph-basics---episode-9.md` — same "Shader Graph Basics" series (Ben Cloward), also comparing Unreal Material Editor and Unity Shader Graph node-for-node; shares tags: materials, shaders, blueprint.
- No other ingested unreal-sidekick tutorial currently covers procedural noise-hash construction or interior/cube mapping shaders — check `references/materials-shaders.md` for related node reference once cross-updated.
