---
title: The Fastest Way to Scatter an Open World Biome in UE5
source: YouTube
url: https://www.youtube.com/watch?v=na4xj_EHdps
author: Aziel Arts
ingested: 2026-08-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-fastest-way-to-scatter-an-open-world-biome-in-ue5/
frame_count: 0
frame_status: pending-selection
---

# The Fastest Way to Scatter an Open World Biome in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=na4xj_EHdps)
**Author:** Aziel Arts
**Duration:** 41m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-fastest-way-to-scatter-an-open-world-biome-in-ue5 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] What's up? In this video, I'm going to be showing you step by step my process for generating
[0:19] this open world environment. We are going to be using a tool that I developed called
[0:24] Asial Arts Quick Scatter. This is a tool that I developed basically because of problems
[0:29] that I was running into and working with many of you all through Asial Arts Academy,
[0:33] building open world environments. There's a lot of technical problems that appear when
[0:38] we're using these tools to generate and scatter large open worlds. Obviously, we have to
[0:43] generate thousands upon thousands of meshes, millions of meshes at times. We need to efficiently
[0:48] separate them to generate at runtime or on load. Some of them need to have collisions.
[0:53] Some of them need to have specific shadow and optimization settings to make them run
[0:57] efficiently at runtime. These are all very technical issues. A lot of times they feel
[1:03] like a huge obstacle to the creative side of environment art, which we all love, where
[1:09] you can actually just really tweak and create the feeling of the forest or the bushlands
[1:13] or whatever the biome is that you're working on the natural biome. That's why I developed
[1:18] Quick Scatter because I felt like there was real need to build a tool that leverages most
[1:23] state of the art PCG spawning workflows that does things the right way to be able to scale over
[1:29] a huge open world. And also that's just blazingly fast to generate and very easy to pick up and
[1:34] start using. So I'm going to be using that tool in this video and you can find a link to grabbing
[1:40] that for your own projects below in the description. All right, let's get into it.
[1:45] All right, so before we dive into the exact steps we're going to take to build this biome, I want
[1:55] to just call out exactly what's happening under the hood here because this is a really important
[1:58] concept for open world environments. We basically have to be very strategic about how we approach
[2:05] them because we want to have beautiful lush natural environments that go on forever,
[2:10] but we can't necessarily generate all of that all at once. And so we have to rely on certain
[2:16] techniques for generating these types of open world environments. The concept that Quick
[2:21] Scatter is built around and is really important here is that we have two groupings of objects.
[2:26] We have our onload objects and we have our runtime objects. Our onload objects are big objects like
[2:33] these rocks or big trees, things that need to have collision, things that we want to be able to see
[2:38] in the distance, but don't need to be as dense generally. And then we have our runtime objects
[2:44] and these are things like these grass and small rocks and ground cover and all this stuff that's
[2:50] really dense around us. All that stuff doesn't need collision. It can be spawned very efficiently on
[2:55] the GPU and it also doesn't need to be spawned all the way into the distance. To achieve this,
[3:00] we need to rely on something called runtime spawning and that is only generating groups of
[3:05] objects that are close to you. So as you move throughout your world, things are loading and
[3:09] unloading to keep your frame rate up to keep memory overhead low, all of that kind of stuff. So
[3:15] you can see that at ground level, things look great. They look awesome. But then when we move up,
[3:20] you can see that this biome is actually only being spawned up to a certain distance. And so as we
[3:25] move forward, you can see areas of that biome loading in. There are lots of techniques for
[3:30] making that loading and not be popping in but smoothly fading in or smoothly scaling up your
[3:36] meshes. That's all done as material functions within your plants. We're not going to cover
[3:40] specifically how to do that in this video. Let me know if that's something that you'd like to see
[3:45] training on and it's something that I also cover within the Academy and I've actually packaged
[3:48] those functions for you in the free azalear landscape material, which you may not realize. So
[3:53] if you are interested in using that asset, you can find a link below. So I basically have two
[3:57] blueprints that are operating here. I have one blueprint that is generating the rocks and the
[4:03] onload objects. And then I have one blueprint that is generating all the runtime plants and things.
[4:08] And so I have two of these blueprints for each of my biomes in this world, which
[4:13] there's three biomes. Actually, there's this bushland and there's the forest over here as well.
[4:18] Quiscata does let you define different biome areas using a biome map, which I'll just go into
[4:23] briefly at the end of this video. But we're going to focus on this bush biome. And then there's also
[4:27] a dunes sand dunes grass biome near the ocean. When I'm thinking about constructing a biome
[4:33] like this, I am usually thinking about two things. First, what are the meshes and objects that will
[4:38] go into a biome like this? And second, how often do they appear and in what pattern? And this seems
[4:44] like a very basic idea, like very obvious idea. But for me, it really helps to separate that in my
[4:50] mind and think about one first, which is what are the objects? And then secondly, how are those things
[4:57] spawned and, you know, what are the noise settings and things like that? That helps me personally.
[5:01] We're going to go and look at the objects that I chose to spawn this biome first. So we'll come
[5:05] over to a level that I've made that's just an empty level. And I've gone ahead and dragged in each of
[5:11] my meshes that I'm using. And this is really helpful too. If you're assembling a group of meshes
[5:16] for a biome, which I did here, I used meshes from different asset packs, which yes, you can do.
[5:21] But the one thing that you can run into when you're assembling a selection of meshes for a biome
[5:27] is that they their color tweaking might be slightly different. The rock might not all be exactly the
[5:31] same hue. And so by dragging them into a level like this, you can tweak them against each other to
[5:38] make sure that they all feel cohesive. So I think all of these runtime meshes came from one asset
[5:43] pack. And then I got these little rocks from fab from quicksul. And then same this bush came from
[5:49] another pack. And then I got these larger rocks from fab. The literally all I did was go here to fab
[5:55] and type in beach rock that those are some of the ones that came up. So they're quicksul. So I went
[6:01] ahead and downloaded those. And that's just from looking at my image reference of rocks that look
[6:06] like the biome that I wanted to generate. Once I have all of these objects in here, and I've tweaked
[6:10] them to look pretty good together, we can see here the clear division between the onload generated
[6:15] objects that need collision and the runtime generated objects that can be really cheaply
[6:20] generated on the GPU really fast at runtime. Okay, so I'm back here in an empty level. And the only
[6:30] thing that I've done in this level here is gone ahead and added a landscape with some shaping to
[6:36] it. And I've gone and added the azl arch landscape material and added a good suitable ground material
[6:43] with a few landscape layers that I've painted in here. Again, linked to that asset below if you'd
[6:47] like to use it on your own project. So the first thing we need to do when we are using quickscatter
[6:51] is enable it as a plugin. If you've gone ahead and installed it, we can come up to the edit and
[6:54] plugins menu and type in quick and spell it correctly. And there we go. AzlArts quickscatter.
[7:00] We will go ahead and enable that and restart the engine if we are prompted. When we do that,
[7:04] we will have a quickscatter menu here at the top, which will open automatically. This gives us some
[7:11] nice shortcuts to tools within quickscatter that we can use to generate things really fast,
[7:15] beat up our workflow. And the first thing we need to do when we add a quickscatter blueprint to our
[7:19] level is just add a quickscatter manager, which is here under blueprints, we'll go and click on
[7:23] that. The quickscatter manager just gives us some helpful, easy shortcuts and buttons that
[7:28] we may need through the creation process. It lets us refresh all of our blueprints at once, for
[7:32] example, it lets us drag in a biome map, which I'll talk about at the end, which lets us define
[7:37] different areas. We will toggle this generate in viewport till we have generation in viewport
[7:41] turned on so that we know if we create a runtime blueprint, it will actually spawn in our level.
[7:46] Next, we'll go ahead, back up to the quickscatter menu and make a quickscatter blueprint. This is
[7:51] a volume. So I'll go ahead and expand this to, you know, encompass my whole world here. And you
[7:56] can see that it is generating insanely fast. I mean, it's just cubes right now. But basically,
[8:00] what I'm doing here is I'm generating the positions of everything on the GPU. So you may have used
[8:05] PCG in the past, and a lot of the PCG nodes are based on the CPU and the whole concept behind
[8:11] quickscatter is that we are generating all of this stuff using purely GPU calculations. And so
[8:16] this lets us do a lot of complicated things very quickly on a lot of points, which I haven't really
[8:22] seen implemented in the same way outside of this tool. And so we're calculating all of this stuff
[8:26] really fast. And then we're spawning it either on the GPU or the CPU. So we can still spawn it on
[8:31] the CPU to have collision if we need. But all the math and stuff of where things should be and
[8:37] they're masking and all the kinds of transformations and things are all being done on the GPU, which
[8:41] makes it blazingly fast. Now we have all of our meshes being generated here, we can go over to
[8:47] the quickscatter settings. Now I'm not going to go over every single setting here in the quickscatter
[8:51] blueprint. I hope they're pretty self-explanatory. I tried to make them very clear and easy to use
[8:55] the whole goal of quickscatter is that it's fast to use. Hence the name. We have our settings
[9:00] separated into different categories. We have our generation settings, which is where we will choose
[9:04] if it's download or runtime blueprint and our grid size and whether we're spawning on landscapes or
[9:10] mesh terrain, because we do support generating on mesh terrain. Then we have our tools, which are
[9:15] my favorite area because this is where I put all the tools that speed up things. We're going to see
[9:19] how we can add our meshes very quickly using these tools. Then we have our mesh spawning section,
[9:24] which will house either our single list of meshes or a data asset, which we'll use for more complicated
[9:30] biomes. We have our transform settings here for all the transformations you might need to do for
[9:35] rotation and position. Then we have our spawn settings. This will let us actually generate
[9:40] meshes without shadow, with contact shadow, with collision, all that good stuff. Then we have our
[9:45] noise pattern, which I'm going to go into a little more detail when we start spawning objects, but
[9:49] this is where we really get the natural spawning pattern that foliage has. We also have masking
[9:54] by biomes, splines, blocking volumes, and landscape layers if you're using it with your landscape
[10:01] layers in your material. I'm going to come over here to an empty folder. The way we calculate
[10:11] complex biomes with Quick Scatter is using data assets. We'll construct a data asset that will
[10:15] have all of our list of meshes in groups, and each group will represent a plant group, for example,
[10:21] or a group of rocks. We'll feed that into Quick Scatter and it will take care of all of the
[10:27] spawning for us. I'll come to an area of my content folder that's empty. I'll click there to focus on
[10:33] that window, and then I'll come up here and choose create mesh group data asset. When I do that,
[10:38] it's going to create a data asset for me that is of the appropriate type for doing this kind of setup
[10:43] for Quick Scatter. I'll go ahead and rename it here. We'll call it DA for data asset. Then I
[10:48] usually like to call it the name of the biome, which would be bushland, and then underscore,
[10:52] and then this will do our onload meshes first, so our big rocks and things. I'll usually give it
[10:58] an OL for to represent onload. Then I'll go over to my Quick Scatter blueprint here as well and
[11:03] rename it because otherwise I can get confused, which is which. I'll just leave the name Quick
[11:09] Scatter and then after it put bushland and then underscore OL for onload. Like I said, we can
[11:16] have this blueprint be a onload or runtime generation type blueprint, which is something that we will
[11:22] go ahead and set here in the generation type. For onload meshes, we're going to go and choose
[11:26] generate onload. There's also generate at runtime here. Then if we're using onload, we can either
[11:31] choose to have it partitioned or unpartitioned. Partitioned is a concept we'll return to in
[11:35] runtime generation, but it basically takes your whole volume area and chops it up and calculates
[11:41] sections, which if you have a many kilometer sized world, you may need to do because depending on
[11:47] what GPU you're using, you can generate only so many points at once in one go, but if we cut it up
[11:52] into partitions or even really big partitions, that can help with calculation time. The fault
[11:57] should work perfectly fine for us for this step. We're going to come over to the tools and mesh
[12:03] spawning. I'm going to expand those two sections. Here we have our spawn type, whether we're spawning
[12:08] these messages on the GPU or the CPU. I usually leave it on GPU when we are just working because
[12:14] it's faster and then when we're ready to bake the meshes into their position in a blueprint or
[12:21] just generate them for a collision and things, we can switch it over to CPU, but GPU lets us just
[12:25] make changes faster and things like that. I can go ahead and drag this data asset here into the
[12:30] mesh data override directly under there. This will go ahead and override any of the meshes that I have
[12:36] here in my mesh list. Here there's an array of meshes with transform settings and weights, and if
[12:42] you would prefer, you can just add meshes into this blueprint like this, but this only really lets us
[12:47] have one list of one type of mesh. When we want to have different groups of meshes, which is what we
[12:52] need for a biome, different groups of meshes with different noise patterns and different densities,
[12:55] we need to rely on the data asset. Basically, when we drag it in, it will directly start to override
[13:02] the mesh list that we have going on here with its transforms and things. So we'll go ahead and open
[13:07] up this data asset and look at what we have. So what you should see here is a completely empty
[13:13] data asset, and the way this works is that we go and hit the plus button to add a group. We can
[13:18] give the group a name like large rocks. We can choose its density, its transform settings, its
[13:26] noise settings, its masking settings, whether we're masking by slope or height, and then here's all the
[13:31] mesh options for that group. So we hit the plus button here or we can add multiple ones. You can
[13:36] do it individually, but what I've done is I've gone ahead and added a handy tool here to automatically
[13:40] add a bunch of meshes very quickly to your data asset, which is maybe my favorite quickscatter
[13:46] feature that I use the most. So I've gone ahead and assembled my meshes here into a folder. So we'll
[13:52] go ahead and control select all of these rock options, my big rock options, I'll go ahead and
[13:57] select all of them. All right, and we will go ahead and drag them into the transfer list here
[14:03] under the tools. And the transfer list is basically a little list that we can use to boot it over and
[14:09] auto fill a data asset like this. So once we've added those transfer objects in, we can choose to
[14:15] either transfer it to the mesh list down here if we're using this mesh list, or to objects in the
[14:21] data table, which is with this button, and we can choose to either replace all of the objects
[14:25] or add them to the existing lists or subtract them. So we'll go ahead and replace them. There's a
[14:30] little option for choosing which mesh group you like to add it to. We only have one, which is index
[14:35] zero here index zero will be fine. So we'll go ahead and transfer objects to data table. And
[14:41] if it doesn't have a group of this number, it will go ahead and make one for you. We'll add it and
[14:45] there we go. Boom. It just added it straight into the mesh variant options. And we have all of our
[14:50] rocks here assembled into this group. Next, I'll go ahead and add my bushes. So we can go ahead and
[14:56] grab my big bush option. And I'll drag in the transfer list for these. And we will up the group
[15:04] number. So we make a second group for these bushes, and we'll go and transfer to data table. And there
[15:10] we go. Now we have two groups, one for large rocks and one for bushes. Or we'll call them big bushes.
[15:16] So just zooming up here to the top here, this is where the magic happens. So we have two different
[15:20] points per square meter controls for these two different mesh groups. And within each of the
[15:25] mesh variants, we have a weight. So this let's just really fine tune how each of these meshes show
[15:31] up and how dense they are. So if we want a lot of rocks, we would go ahead and up this point per
[15:35] square meter to point one, there we go tons of rocks or point zero one for less. And then we
[15:42] could come into the transform so I could adjust the scale range for the rocks. So I might up them
[15:47] to one to two in size, they have a little bit more size to them. And we could adjust their rotation
[15:52] options. There's a bunch of different stuff in here. One thing I do want to do for these rocks
[15:56] is align them more closely to the surface. And that is what we do here with the align to surface
[16:01] rotation option. Basically, this is how strongly the mesh aligned to the angle of the landscape that
[16:07] it is bonning on. So whether it points up straight up and down, that would be aligned to surface zero,
[16:12] and then one would be fully aligned point five by default. So I'll go ahead and up it to one. So
[16:17] those meshes are fully aligned so we don't get any gaps in the bottom and full further than that,
[16:20] I will also push them down into the landscape a little bit. So we'll come to the z position offset
[16:25] and we'll just go negative 10 here. And that will push them down just a little bit into the
[16:29] ground just so they kind of look like they're submerged. And here's a situation where we have
[16:34] our general transform settings. But for example, this rock here looks too tiny compared to the
[16:40] other ones. So I have a general scale range and transforms here. But if I need to override that
[16:45] on a particular object, I can do that. So I can come to that mesh and I can choose to
[16:49] click this checkbox, which will override the transforms on this particular mesh. And then
[16:53] we can go ahead and up it to like two to three. And then that will up that mesh and that will
[16:59] also have to adjust its align to surface and its z position so that it matches the other ones.
[17:04] There we go. So that's how we go ahead and fix individual meshes. Okay. And the bushes here,
[17:08] I think they're a little bit too large. And if you're not sure about size here, one tip is that
[17:15] I like to drag in a little character just to compare how big things are when I'm spawning them
[17:21] against a human. For me, that helps me feel the scale of the space. Obviously you could walk around
[17:26] and kind of check it. And I also recommend you do that. But if we come over to our content browser
[17:31] and come up to all, then we come to engine content. And if we just search character, there's a little
[17:36] human character here. So I'll just drag them in. And this will help me check. Okay, I think this
[17:41] bush is a little bit too generous compared to this character. So we'll come back to our bush
[17:45] settings here, come to transform, and we'll lower it down to like 0.5 to one in our scale range.
[17:51] We'll just be a little bit smaller. Okay, so let's talk about noise. And this is really
[18:01] important. This is a kind of something that's going to have a huge impact on the look of how
[18:07] these plants are spawned across the landscape because random spawning is great, but and it works
[18:13] pretty okay for these rocks. But for something like bushes, there's a natural clumping pattern that we
[18:17] should see that is reflected in nature. And so the way we achieve that is through spatial noise. So
[18:23] if I come down here to the spatial noise section, expand it, we have a few different settings that
[18:28] control the look of our clumping pattern or dispersion is really the correct ecological term
[18:35] for it. We have the size of our noise pattern, which we'll look at in a second. We have the
[18:39] strength of how it affects and cuts out plants. Then we have the scale by the noise. So how big of
[18:46] a variation in size are there between the inside of clumps and the outside, for example. And then
[18:51] we have a seed for the noise because you might have the same size and settings for the noise of
[18:56] different plants, but then you might want different seed patterns for them. Let's quickly increase
[19:01] the density of our bushes so that we can really see what the noise is doing. So I'm gonna up it
[19:05] all the way to one, which will create an insanely dense bushland for me. Also, just want to mention,
[19:11] extremely fast, you can see it spawn like almost instantaneously. So I'm gonna come over here to
[19:15] this spatial noise strength, and we will go and up it to 0.8. Generally, a range between 0.5 and
[19:21] 0.8 is where I tend to adjust my noise to. But you can see that once we do that, it will start to
[19:25] cut off the meshes in some areas. And if we adjust the size of the noise up to 3000 or 2000, you
[19:33] can see that it creates much larger clumping patterns. Or if we drop it down to 1200, which is
[19:38] what I think I'll use for this one, you can see this gives us some great patterns to our bushes
[19:43] here. So then we could go and choose to lower the strength back down to 0.45 to give it be it less
[19:49] aggressive. I'm actually going to keep it at 0.8, but I will go ahead and lower the density of the
[19:54] bushes down to 0.1, which will give me some nice clumping and density within those bushes, but won't
[20:00] be too aggressive in cutting them out. Okay, so once we have our onload meshes here, generating the
[20:06] way we want, we can go ahead and start to generate our runtime meshes. Follow the same process here,
[20:10] I could even duplicate this existing quickscatter blueprint. So I'll right click on it and edit
[20:15] and duplicate, I'll rename it to be instead of onload, we'll call it RT for runtime. And in this
[20:22] one, we'll go ahead and make a new data asset. So I'll come up here to the quickscatter drop down,
[20:27] make a new data asset. And this one, we will rename and call DA bushland underscore RT for runtime.
[20:35] And we'll drag that in to replace the existing one on the runtime graph. And then let's talk about
[20:40] our generation settings. So when we're doing something at runtime, in fact, I'm going to remove
[20:44] this data asset just so we can see the cubes here, because I think it'll be easier to just
[20:48] look visually at what's happening. So right now, we're generating everything over our whole world.
[20:52] So let's adjust this blueprint to generate at runtime. So we'll come and switch it to generate
[20:57] onload to generate at runtime shouldn't see too much of a change because functionally, it's kind of
[21:02] the same because we're saying generate onload or generate suddenly at runtime. But we're using our
[21:08] camera as generation source for runtime. So it'll just say it'll spawn anyway. So nothing really
[21:13] changes there. But when we go ahead and turn on is partitioned, that will basically take that full
[21:18] generation source and chop it up into partitions, which are basically squares of generation that
[21:24] will calculate just in that square. And because we break up that calculation into those smaller
[21:29] chunks, we can generate a bunch of those chunks up to a certain distance. That's how we do the
[21:34] runtime spawning. So to keep your same density and everything, but now we're just generating in the
[21:38] generation grid size of 1600. Now, the size of these grids is important. And generally,
[21:44] fewer bigger grids will generate faster for you. But obviously, if the grids are bigger, you can't
[21:50] they spawn further, depending on your machine, this is very dependent on hardware and target
[21:55] hardware, what you can get away with. And so I'm going to up it to 6400, which will generate larger
[22:01] grids. And so it'll be still pretty fast. And I'll generate up to a certain distance. The way we
[22:06] choose the distance is here under the advanced dropdown. And this will basically give us a
[22:10] distance that each radius for the grid should be generated at. So if we've chosen 6400 here,
[22:17] we can scroll down here to 6400. And I could adjust the spawn distance here for 6400. I've left this
[22:23] at pretty efficient values for you by default. But if you need to go in and tweak them, you can
[22:28] come in here. Generally, the rule of thumb is that if you're spawning things only at a very
[22:33] close distance from you, you need to use smaller grids and further distance bigger grids, because
[22:39] you can get away with fewer of them. That's the general mindset. But this these are all things
[22:43] need to be tweaked a little bit to your hardware. But I've tried to leave them at pretty good
[22:47] default settings for you. So now we can see that we're generating our stuff at a certain distance
[22:52] away from us, which is great. Now we'll go ahead and drag in our runtime data asset again. So once
[22:59] you've dragged in your new runtime data asset, obviously, the cubes will go away because we're
[23:03] now overriding the mesh list that exists here with the cube. Now let's go ahead and add our
[23:15] runtime meshes into our new data asset. So I will come over to my folder here. I've saved my runtime
[23:21] meshes. So I'll go ahead and add these small plant options first. We'll drag them into the transfer
[23:26] list and choose the group that we want to add them to transfer to data table. Now we can see we have
[23:31] six elements here. And what I'll do is I'll go and increase their density quite a bit. And when
[23:38] we're doing runtime spawning, we get away with a lot denser meshes, which is awesome. So I'll come
[23:43] over here to the points per square meter and we'll up it to something like four, which is crazy. So
[23:48] that'll be spawning pretty well there. And then we'll go to something like our spatial noise and
[23:53] we'll start to make some adjustments here as well. So I want a slightly larger clumping pattern to
[23:59] what it has here, but not quite as big as the bushes. So I'll up this noise spatial noise size to
[24:04] 800. That will create a slightly larger noise pattern. And then I will also increase the noise
[24:11] strength to point eight. So we will still get like areas of clumps, but they will be a little bit
[24:16] more sparse. I'll also up their size just a little bit. So it'll be point five to two instead of one
[24:22] point five, a little bit bigger. Maybe I'll lower the spatial noise strength to point seven. There
[24:28] we go. That looks like a good spread. And remember, we're layering in a bunch of different plants here.
[24:33] So these particular plants don't have to cover the full area. In fact, they shouldn't because then
[24:37] they'll kind of fight with each other. I'm just trying to create, you know, how dense should these
[24:42] particular plants be in their own clumps. Next, we will go add a new group. So first, I should name
[24:47] this to be small plants. Go ahead and contract those settings. And we'll go ahead and add our
[24:52] smaller bushes. So I'll go and add a new group here. And we'll call this small bushes. And then I'll
[24:59] go scroll here to the bushes option here, click on them, drag them into the transfer list. And we'll
[25:04] go and choose the group, which is the second one. So it'll be index one, but you can check here.
[25:09] And I will say transfer objects data table. And I will now have four bush options. So we'll go
[25:15] ahead up their density as well to two points per square meter. And for their spatial noise, I would
[25:20] like to have larger clumps. So up the spatial noise size to 1200. And we'll up the spatial noise
[25:26] strength to point seven. I will create some larger groupings of those smaller bushes. And you could
[25:32] also probably increase the spatial noise seed here. So they're giving them a slightly different
[25:37] noise spatial noise to the small plants. And we'll contract those two, we'll make another group.
[25:43] And this one will be flowers. So come in here and type in flowers. And the order of these groups
[25:49] doesn't really matter. So you know, whatever kind of makes sense to you in terms of the order that
[25:54] you put these things in. So I'll come down here to the flowers, grab all of those, drag them in,
[25:59] we'll make it the group index two, and we'll transfer them. There we go. For this density,
[26:04] we'll up it to point five. I don't want these to be quite as dense as those other plants. But
[26:09] there we go. That looks better. And then look at our spatial noise settings here. I actually feel
[26:14] pretty happy with this spread of flowers, but you could obviously adjust this to be like a little
[26:19] more clumpy or with the noise settings, we will go ahead and add some small rocks. So how you define
[26:26] rocks between your different areas is totally up to you. But for me, I like to just separate, you
[26:31] know, rocks that need collision and rocks that don't. And rocks that don't need collision,
[26:35] they can be spawned at runtime. Rocks that do need collision, they can be spawned on load. We could
[26:39] go ahead and make this just a small rocks. I will come to my little pebbles here, drag those over to
[26:45] the transfer list, up the group number and transfer them. For the number, we'll probably
[26:51] increase them to like one points per square meter. And you might need to just come and check here.
[26:56] They look a little too tiny. So I'll come to the transform and we'll up there transform between
[27:03] like two to three. There we go. That's a little bit easier to see. I will keep their spatial noise
[27:08] settings the same, but I might up their noise C a little bit to three. All right, let's make a new
[27:14] group. Just a note about the seed. The seed can be helpful to if you have a particular noise pattern
[27:19] for like you want there to be bushes and then grass, but only in the area of bushes. That is a
[27:25] situation where you would use the same spatial noise size and seed, but like a different strength.
[27:31] And then you would have the same pattern for those different plants, but then the grass would be
[27:35] kind of seeping out from under the bushes. So the seed can be really useful to either group plants
[27:41] or keep them separate. Okay, so now we come to the my favorite thing, which is ground cover.
[27:47] For me, it's very simple for this environment. I just have some very basic like twigs and things,
[27:54] which I observed from my images that I looked at of the environments that I visited and it is
[27:59] dead grass and twigs. So I'll go and drag those two meshes into the transfer list and up it to four.
[28:06] And this is kind of like a category that I see people miss a lot. Ground cover is very important
[28:11] for giving a environment a feeling of age, because when we look at like a ground in a forest,
[28:17] especially it's really important in forest less so here, but we kind of see the levels of things
[28:23] on top of each other. And that helps give the feeling like there's this environment has been
[28:27] here a long time, there's been time for things to kind of collect and ground cover also helps
[28:32] things feel old because that's where dead leaves and broken branches and things go as they just fall
[28:38] down into the earth or the sand in this case and collect there and cover the ground. So that's why
[28:45] it's called ground cover or some people like to prefer to it more as like debris, so like dead
[28:50] plant matter and things. However you want to think about it, that's just an important layer to have
[28:54] in your world. Otherwise you have a feeling like this plants are just perfectly bond here and they
[29:00] never die and they just disappear. But ground cover and debris and things can be really difficult to
[29:05] spawn without proper runtime spawning techniques because they tend to be pretty dense and so
[29:11] you'll just run into this issue of density pretty quickly. So I've added the ground cover in and we
[29:16] are going to increase the density quite a bit up to one and there we go. We've got some nice ground
[29:23] plants debris and for the transform I might push them slightly down into the ground. I feel like
[29:29] they're slightly floating depending on the mesh you might get this kind of look. So I'll come over
[29:34] to the transform settings and lower the z position like negative five. That was too much. Oh also we
[29:40] want to make sure they are aligned to the surface. That will help. Maybe point four or three. That
[29:46] looks pretty good. I will call this cover. All right so that is how we generate the runtime assets
[29:51] and so we now have our two different categories our runtime and our onload assets.
[29:56] One thing I will mention for runtime generated assets is we come over to the blueprint again
[30:06] and if we come down to spawn settings generally you can get away with switching your shadow method
[30:11] to contact shadows. Contact shadows are kind of like drop shadows. They're almost free from a
[30:18] rendering perspective compared to dynamic shadows and on our very small objects don't tend to need
[30:24] really complex shadowing anyway especially grass and things. So you can save a lot for your frame
[30:28] rate by just switching all of these dense ground cover and plants and things to contact shadows
[30:34] and then what we'll do if we're using contact shadows is we will need to go to our light if it's a
[30:39] directional light or if we're using ultra dynamic sky like I am I will go to the ultra dynamic sky
[30:47] blueprint and I will expand its contents here and look for the directional light here under
[30:52] sun parent there's a directional light so whether you're using a loose one or this one here we could
[30:57] need to go to the main directional light actually I like to search here contact and then we can choose
[31:03] the contact shadow length here and we can you can see increase the length of our contact
[31:09] shadows so that's no shadows and this is contact shadow length added in we also have an intensity
[31:14] if we want to make them a little bit softer so you have a lot of control here and they directly
[31:18] are connected to your directional light so as you move your sun or directional light the shadows
[31:23] also move just like normal shadows so really useful tip here for just optimization and you can also
[31:29] at this point kind of experiment with different distances of spawning here for your world what
[31:34] you can get away with on your hardware density wise which is very easy to come back in here and
[31:39] adjust your density for your ecosystems on our on-load blueprints here so now that we're ready to
[31:45] switch on collisions spawn on cpu and potentially bake their position out into a blueprint this is
[31:51] how we do that we've done make making our changes what we need to do to bake things into a blueprint
[31:56] is switch the spawn type over from gpu to cpu on the on-load blueprint which may depending on your
[32:02] machine may take a little bit longer to spawn it still should be pretty fast again we're not
[32:06] calculating anything on the cpu in terms of where they should be positioned we're just spawning them
[32:11] which is all we really need to do and then once we do that we can come down here turn on collision
[32:17] and if we want to adjust the world position offset distance or call distance we can do that on gpu
[32:21] meshes i've done that automatically for you so once we've made those changes we can either choose
[32:27] to have it spawn instantaneously like this at the beginning of our load or bake it into a blueprint
[32:32] so to bake it into a blueprint we can click on the blueprint here and expand its expand its
[32:38] contents here and we'll scroll down to where it says the pcg on-load graph in its contents
[32:43] we'll click on that and we have some buttons here and we want to click clear pcg links which
[32:49] we'll go ahead and take a minute to to generate and then we'll go ahead and spit out a pcg stamp
[32:55] which is just a blueprint with an instant static mesh for each of the individual meshes that you
[33:01] have in your blueprint here and then their instance positions so it's very efficient and yeah you can
[33:07] nothing needs to be recalculated in terms of position and in terms of all that stuff so they
[33:12] can have collision they can have all the stuff they need to have they can actually just persistent
[33:15] instant static meshes in your world then we want to come over to our on-load blueprint and check the
[33:20] enabled checkbox off which will have it stop calculating anything in your pcg graph and then
[33:26] if you ever need to make changes all you need to do is come over here to the stamp and delete it
[33:30] then come back to our on-load blueprint and go and enable it and then it'll go ahead and spawn
[33:35] everything in again you can make the changes that you need to make and so on
[33:44] all right let's really quickly talk about masking with this one biome but the way we have this one
[33:50] biome show up only in a particular area is using a biome mask and quick scatter set up very well to
[33:56] do this if we come back over to our quick scatter manager blueprint here and we come to our material
[34:03] area which is where i saved my biome map a biome map is basically just a color map that has a different
[34:09] color where different areas of your biome should be and it's mapped to the size of your landscape and
[34:14] the shape of your landscape so you could take a screenshot of your landscape and paint over it
[34:18] you can bring your landscape into gaia and generate different colors you could yeah literally just go
[34:24] into microsoft paint and paint some different stuff there's lots of different approaches everybody
[34:28] has different techniques that they prefer i cover some of those inside azure arts academy
[34:33] but basically this is what we need to just define the areas for this particular biome so i have a
[34:38] few different biomes i have my yellow which will represent my bush biome i have my green which is
[34:42] my forest and then blue is my dune sand dune biome so we're gonna just attach our bush biome to the
[34:49] yellow the first thing i do usually with the biome map that i've just imported and this is just to
[34:54] help it function well as a biome map that's always loaded and always being a referenced is to switch
[34:59] on never stream this helps it be persistent even if we close our project reopen it it still loads
[35:05] this in the type of way that we need to sample it for our biomes so you've baked out your positions
[35:11] then we go ahead and turn on mask compression masks no srgb because i don't want any sort of color
[35:16] conversion in the actual biome map itself i just want it to be straight up and it doesn't need to be
[35:20] you know correct colors or anything it just needs to be unchanged by srgb application so then i'll
[35:25] drag this biome map into the biome definition on the azl quickscatter manager and from there i can
[35:31] go ahead and mask this biome into that particular area so i'll go into my runtime blueprint first
[35:36] and we'll just scroll down in the blueprint to where it says masking biome and we'll just say
[35:40] use biome and then i will go ahead and open up my image again here and i'll just go ahead and
[35:46] sample the color for the yellow biome so i'll go and click on the biome color and hit the eyedrop
[35:52] and choose the yellow and then hit okay and now we're going to only show up in that particular
[35:58] biome areas next i'll go to the onload blueprint here click on that and we'll do the same thing
[36:04] use biome and then mask by the particular color hit okay and now we have our biomes only showing
[36:09] up in that area of the biome map and so i have this other biome here that's going to represent my
[36:14] forest okay so that's one area of masking that we would use to define different areas and you
[36:18] just create two new blueprints for your forest area and you could duplicate your data asset
[36:23] replace the meshes however you want to approach it that is basically the workflow what if we have
[36:27] an area like this so this is an area that i built using an awesome asset pack and so which i will
[36:34] link below if you'd like to check that out but basically we're procedurally generating all of
[36:37] our biome around it but we want this particular area to be handcrafted and cut out from that biome
[36:43] and so that's when we use different types of masking so if i come over to my runtime generation
[36:48] and we expand instead of masking by biome mask by masking general and then this will let me either
[36:54] mask by slope mask by height which sometimes is all you need or mask by an actor or a blocking
[37:00] volume blocking volumes are just really simple volumes you can add to your world like this
[37:05] by coming up to quickscatter and choosing blocking volume this will go ahead and add a volume which
[37:09] we could go ahead and basically plug it into our blueprint so i'll save runtime and then we'll add a
[37:15] blocking volume here the plus button choose the blocking volume and there we go now we're cutting
[37:19] out our runtime meshes so that's a quick way to do it but sometimes you have a more organic area
[37:25] like this shape is kind of not quite square or a circle which is the other type of shape you could
[37:31] use for the blocking volume so we'll go ahead and remove this and i'll delete it and so i have
[37:36] created this spline and the way we create splines really easily is coming up to the drop down in
[37:41] the top left corner choosing modeling and choosing draw spline and we could go ahead and draw a spline
[37:47] shape around where we want then i'm going to go and grab this spline which is spline actor zero
[37:53] and plug that in instead so we'll come to the rt runtime we'll scroll down and we'll choose mask
[38:00] actor instead of mask volume and then i'll use it to choose the spline that i have there and
[38:05] there we go now i've gone ahead and masked out by that spline and i have a bunch of settings to
[38:11] expand it inwards and outwards and we can choose to mask inside a volume or outside of it or inside
[38:18] a path and so that's how we would do a path so if i have another spline over here which represents
[38:23] this path that's cutting through here then i would go ahead and do the same thing come to the masking
[38:28] add a new one add the second spline here and then we could go and starting to work but i
[38:35] could expand it to cut out things a little bit wider so i could come to the mask extend section
[38:39] and up it to 300 and that would extend the mask outwards a little bit maybe 500 so that is the
[38:45] runtime area that's been cut out so we need to also connect these up to my onload and we can
[38:50] actually copy the inputs here so if i come over and i right click and do copy under mask actors
[38:57] come to onload and just paste them in and now both blueprints are getting cut out by the mask
[39:04] actors here which is the single spline path oh i forgot to in the path it still says mask inside
[39:11] volume and if you're never not sure what the masks are actually doing this is really helpful you can
[39:16] come over and up here turn on debug mask points which is showing me that i have a mask volume here
[39:21] and this spline is also being considered as a volume not just a path and so i need to go and
[39:26] switch it from the mask type to mask from inside volume into inside path and there we go now it's
[39:31] just a path and i need to do that on my other blueprint as well and then i'll go and turn off
[39:36] the debugging and there we go now we get a more specific path here so this is the general approach
[39:41] for having areas like this that are handcrafted for a point of interest or a city or something that
[39:47] you need to explore as a character that's more crafted these are just meshes that i literally
[39:51] hand placed in here to create this look and this kind of area around this lighthouse and then i have
[39:58] a road kind of a path walking path coming over here that is how we start to add more definition
[40:03] to our biomes so these left and right of the path are still generated using all the procedural
[40:10] stuff that we just set up but we're just cutting it out in the areas that we need to be like i wanted
[40:14] a specific rock here on the side here so i just you know cut out this area and just hand placed
[40:19] some of these rocks here to create this kind of framing rock as we walk up to the lighthouse
[40:25] all right i hope you found that video helpful and it helps eliminate the process a little bit for
[40:28] generating a really natural and lush looking open world environment like i said you can find a link
[40:34] to quickscatter below this video also if you would like to work directly with me to leverage quickscatter
[40:41] or just other environment art techniques to build your environment for your game whether it's a
[40:46] smaller environment or a more open world environment that is why i built asian arts academy if you are
[40:52] interested in joining the academy you can find a link to jump on a call with me below this video
[40:56] and we can talk about if it's a good fit for you i've worked with hundreds of you on different types
[41:01] of environment art projects and i love teaching and working with you and coming alongside you helping
[41:06] you work and and build the projects that you're passionate about so you can find a link to that
[41:10] in the description for this video more videos to come on quickscatter let me know what you think
[41:15] and if you found this video helpful and i will see you in the next one



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
