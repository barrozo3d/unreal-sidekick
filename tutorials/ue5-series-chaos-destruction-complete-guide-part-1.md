---
title: #UE5 Series: Chaos Destruction | Complete Guide Part 1
source: YouTube
url: https://www.youtube.com/watch?v=1DK46of-Syg
author: SARKAMARI
ingested: 2026-07-20
ue_version: "Not specified (Chaos Destruction UI matches UE5.3-5.5 era; Brick fracture flagged experimental in-editor)"
tags: [chaos, destruction, vfx, fracture, cinematics, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# #UE5 Series: Chaos Destruction | Complete Guide Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=1DK46of-Syg)
**Author:** SARKAMARI
**Duration:** 47m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, Reza here, welcome back to my channel and to another Unreal Engine tutorial.
[0:06] Today we're diving into Chaos Destruction, a powerful tool that lets you create cinematic quality visuals in real time,
[0:16] even in large scale destruction heavy scenes, all while maintaining precise artistic control.
[0:25] This is the first video in a three-part series where I will walk you through the Chaos Destruction system step by step.
[0:36] By the end of this lesson you will learn how to set up destruction in your level, including creating your first geometry collection
[0:47] and exploring the various fracture types available in Chaos Destruction.
[0:55] Together we will create your very first fracture simulation.
[1:00] We've got a lot to cover, so let's get started.
[1:17] Here I am inside the editor, what I have is a very simple scene.
[1:30] I intentionally kept it simple and tried to stay away from fancy demos right off the bat because we need to understand the principles,
[1:39] we need to understand the tools before we dive into anything complex.
[1:45] So not to worry, I will walk you through the whole process from start to finish and try to tackle all the tools that you need to create your favorite destruction scene.
[1:57] First things first, we need to load the plugins.
[2:00] So I'm going to go into edit and to plugins and what we're looking for is chaos.
[2:06] Obviously we have different types of outcomes from chaos, but what we want right now is
[2:14] we want to search for chaos Niagara, chaos solver, I'm going to scroll down and we want to have chaos caching as well.
[2:26] I'm just going to have a brief look to make sure we're not missing out of anything in particular.
[2:32] If you want to incorporate USD obviously you can bring in chaos caching USD which is quite useful with cloth and marvelous designer.
[2:42] We may have a couple of sessions on those as well, but for now I'm just going to go and hit restart.
[2:48] What I have is a folder where I keep all of my Quixel Megascan assets and I created a folder for chaos.
[2:57] So anything that is chaos destruction related, I store that into this folder.
[3:03] First things first, we need to change the mode.
[3:06] We go from selection to fracture shift six, we'll get this menu opened up for you.
[3:16] And you can see just like modeling, we have few sub menus and each sub menu can be used
[3:22] not necessarily in a sequential order, but there is some sort of a logic into this which we will find out really, really quickly.
[3:31] Now where should we start?
[3:33] Where is the first step?
[3:35] Let's say I want to break these assets and I want these guys to collide with either the ground or this asset right here.
[3:48] So ideally we would like to move this guy up.
[3:52] I'm just going to make sure that it's right on top of the asset that I have.
[3:57] And we would like to simulate this once this statue hits the rock, it breaks apart.
[4:04] The first step is to create a geometry collection asset.
[4:11] So destruction in chaos system always begins with the geometry collection asset.
[4:18] These assets can be created from one or more static meshes.
[4:23] It means that I can bring this, let's say clay pot right here and select both of them and create a geometry collection out of them.
[4:33] It can be created from blueprints with static mesh components in it or even other geometry collection.
[4:41] So you may have a geometry collection already.
[4:44] You want to nest that in another geometry collection.
[4:47] You can do that as well.
[4:50] How to create a geometry collection by using the first menu.
[4:55] The new button here on their generate is your first step.
[5:00] So with the object or actor selected, I'm going to go select new.
[5:07] And it says where do you want to save it?
[5:10] I'm going to save it under chaos because it's related to my chaos destruction scenario.
[5:16] I'm going to go create geometry collection.
[5:21] What basically happens here is this geometry is now ready to be fractured.
[5:29] We have fracture hierarchy here, which explains how many pieces this will break down into.
[5:38] So you can keep track of your counts or pieces or as chaos destruction calls it bones in here.
[5:49] Then we have the properties of whatever you're selecting in here.
[5:55] And in level statistics, it says how many levels of fracture or destruction you have applied to this mesh.
[6:05] So all three windows or pains view settings, level statistics and fracture hierarchy needs to be open
[6:16] so you can adjust attributes and properties to refine your fracture.
[6:24] Once our geometry collection gets created, you may have noticed that we have the parent here in the fracture hierarchy.
[6:31] There is no sign of any child or children because we haven't fractured this geometry collection yet.
[6:39] We see the level statistics set to level zero.
[6:42] We have number of bones, number of pieces set to one simply because we have one object.
[6:49] And there's really not much to play around with in the view settings.
[6:52] We keep looking at these three windows as we move forward.
[6:57] These three windows play a huge role in our optimization side of chaos destruction.
[7:05] Also, this geometry collection can be viewed here as well.
[7:10] We get number of properties to deal with such as materials to be added to begin with,
[7:16] which we will explore in future lessons.
[7:19] In the outliner, I have my GC statue, the geometry collection appearing on the level as well.
[7:27] Now you may ask one question that Reza, is there any condition as what asset would be a good asset
[7:34] to be nominated for geometry collection?
[7:37] There are actually two conditions.
[7:39] The first one, the geometry collection should be watertight.
[7:43] What does it mean?
[7:44] It means that asset or number of assets that you're nominating to be geometry collection
[7:50] should have no open faces or edges.
[7:54] If you have those, that will lead into poor performance during simulation.
[7:59] The second condition, if you're creating number of geometry collections right next to each other,
[8:05] so you select all of them, you go to new and create one geometry collection out of
[8:09] number of assets, make sure there is no intersection.
[8:13] Make sure there is at least a tiny gap in the middle of them because there is a tendency
[8:18] of one object pushing another out if the objects are intersecting right at the beginning.
[8:24] During simulation, you will see odd things happen.
[8:28] Now how to simulate, let's say there is no fracture, we just want to see that falls and we just want
[8:33] to check the collision.
[8:35] Any assets that you bring in and you set to fracture mode gets a collision.
[8:40] So I can go into four dots, selecting the simulate and then click on the play button
[8:49] and you can see the object will drop and the collision works beautifully.
[8:55] I'm going to stop the simulation.
[8:57] Now before we wrap up this chapter, let's actually fracture this piece and see how
[9:03] chaos destruction works.
[9:04] That's very easy.
[9:06] Once you have the geometry collection ready, simply select the geometry collection.
[9:12] We go to the simplest form of fracture which is uniform Voronoi and that is going to give us
[9:19] sort of a similar volume across the shape, evenly spaced bones.
[9:24] So I'm going to select that.
[9:26] You can see first one is uniform Voronoi, minimum, maximum and we tend to start low.
[9:33] Remember if you start high, there's a tendency for artists to add layers of fractures on top
[9:39] of each other and if you start high, the second layer of fracture is going to target every single
[9:47] fractured piece and break those apart.
[9:50] So before you know it, you run out of memory and Unreal Engine might crash.
[9:55] So we keep those values relatively low for our first level.
[10:01] Then we have materials and I will talk about how to add internal materials.
[10:06] Right now it's set to automatic, meaning that the internal materials get default external
[10:12] materials what you have specified.
[10:15] We in the common fracture rollout, we have seeds.
[10:19] Then we have noise which gives you a little bit of Perlin noise for these lines right here.
[10:29] So you can see we have a volume with multiple sides.
[10:33] That's the term that Unreal Engine uses to define how many pieces it will cross this piece right here.
[10:43] So although we have specified 20 cuts, we might not actually get 20 because as you can see this one
[10:51] right here doesn't really cut this piece right here.
[10:57] You may want to try with different number of seeds to try different combinations,
[11:02] but for now if I set the amplitude to five, you can see all of a sudden we get a little bit of
[11:09] irregularities like this which is going to give us a slightly non-uniform result.
[11:17] You can play around with the frequency, lower the frequency to get a slightly different result as well.
[11:23] And with that out of the way, I'm going to hit fracture.
[11:27] You may have noticed that in the fracture hierarchy, I have now 19 pieces.
[11:33] So one of these guys didn't make it to the geometry collection that we have.
[11:39] So we don't get 20 unless you have a cube relatively the same size within this volume.
[11:46] You're not going to get exactly this number.
[11:48] You usually get a lower number than minimum and maximum vornosites.
[11:54] And you can see we have now level one.
[11:57] And this level one indicates the number of fractures, number of children that belong to the first level
[12:04] or in this case, first level is level zero, which is this guy right here.
[12:10] I'm not going to hit fracture again because once you create that, you've got to cancel out of this.
[12:15] If you fracture again, then you are going to introduce the second level which targets the
[12:20] fractured pieces, and it's going to fracture that to even smaller pieces.
[12:26] So I'm going to sort of jump out of that.
[12:29] You can see that in the view settings, it shows all the levels.
[12:34] You can go and select level zero, which is the parent.
[12:37] You can select the level one, and that includes these 19 children.
[12:43] And you can kind of explode them to see what sort of combination you get from the first fracture.
[12:52] As you can see, and if you're unhappy with that, you can easily go into reset and reset that removes
[13:01] these levels and you can start over.
[13:04] But let's just hit simulate and see what type of result we're getting.
[13:08] By the way, shift B is going to showcase the individual bones as separate colors.
[13:17] It gives you a really good indication what sort of cut you're dealing with, where the object is
[13:23] going to fracture. Ideally, you want to go in there and type in show and see show bone colors
[13:31] under your geometry collection. That's another way to use instead of shift B.
[13:36] I tend to use shift B to see the visualizations of each bone and shift B to toggle that off.
[13:45] With those out of the way, let's go and hit simulate.
[13:49] And you can see the asset fractures into multiple pieces.
[13:57] Let's do that again and visualize.
[14:01] So fairly straightforward.
[14:03] Let's say you're not happy with this, you go reset, reset, and then level one has been removed.
[14:09] And if I go into fracture hierarchy, there is no children.
[14:13] All right, with that out of the way, let's replace this guy with just a simple plane
[14:20] and explore types of fractures that we might encounter.
[14:26] Let's go to the next chapter and explore the types of fracture that we have in unreal engine chaos destruction.
[14:41] So let's talk about the type of fractures. The first one is the easiest one and that is a uniform
[14:48] fracture. Uniform tool uses Voronoi algorithm to create fracture patterns.
[14:55] Once you select your geometry collection, you go into uniform, you can see these patterns
[15:01] and they're really evenly spaced. Typical fracture that you see in a window crack,
[15:09] but still not my absolute favorite because everything is kind of the same size more or less.
[15:17] What you can do to make it more interesting if those lines are too straight is to play around
[15:23] with noise as we explored in the previous chapter, give it amplitude, give it frequency,
[15:29] so it appear more a little bit jagged. Apart from that, we've got minimum Voronoi sites,
[15:35] maximum Voronoi sites, how many pieces you will get, you can randomize it, overstay with one
[15:41] in this particular example and go fracture. You can see these lines are very straight.
[15:50] If I cancel out, select this one, go to reset, reset that and fracture that again this time
[15:59] with a degree of noise. Once I start fracturing, you can see the jagged edges here which is
[16:09] the result of noise rollout. So I would say that's the only bit I always include in the uniform
[16:17] fracture to make it slightly look more interesting. To select all of it, I'm going to go under select
[16:25] all. We have fracture already in place, so I'm going to cancel out and click away. We have those
[16:33] pieces. Remember, I can go ahead and shift B to see the original material or shift B to look at
[16:41] the fracture individual pieces. And then now I simulate and you can see things will break apart.
[16:50] So really not much into it, very straightforward. I'm going to jump out of the simulation. I'm going
[16:57] to go ahead and reset my geometry collection to remove the fracture so we can explore the next
[17:03] type. The next type is called cluster. And once I apply this, you immediately notice the chaos,
[17:14] the non-uniform model. So this tool actually extends from uniform fracture. It is kind of
[17:22] linked to uniform fracture. It uses the same Voronoi algorithm while in the uniform method,
[17:30] we have a really even distribution of sites of pieces. The cluster method randomizes, introduces
[17:39] close proximity islands, resulting in more varied fracture platform. So all in all, there is really
[17:48] not a huge difference. But if you're aiming for a little bit of randomness, a little bit of variety,
[17:55] this can get you there quite easily. Now if I go ahead and fracture, you can see that we've got
[18:05] well, more pieces. What we specified was eight and eight. But we also have something called cluster.
[18:13] And clusters are like groups, we have a whole rollout for generating clusters. But you can see
[18:21] immediately that we're getting far more pieces to play around with, which immediately looks more
[18:28] attractive and better. So a little bit of randomness into the mix, and we're getting a far better
[18:37] result. If I go into my fracture and have a look at my hierarchy, you can see that we all in a
[18:46] sudden introducing 82 bones, 82 pieces, you can see that in level one of my level statistics window
[18:56] as well. So you got to be very careful. If you're planning on using this for your level one, then
[19:02] you need to go gentle with extra levels that you may want to add to your geometry collection.
[19:10] So that's that, there is nothing really to it, the rest is more or less similar to the uniform
[19:17] fracture method. I'm going to select that, go into reset to remove that so we can explore the
[19:23] third one. Now the third fracture method is called radial. And you may have immediately noticed from
[19:33] the look of it that the radial fracture generates again, Voronoi sites that radiates outward from
[19:42] the center point. The center can be adjusted using the gizmo right here. So remember that never move
[19:52] the object, always look at these gizmos instead and try to sort of move them to adjust the fracture
[20:03] point from the center to wherever you want to move it to. A few important things to be
[20:11] mindful of with this radial that you can see that we have some extra attributes at our disposal.
[20:18] The first one that is actually quite important is this angular steps. And that is simply the
[20:26] number of angular steps right now we have one, two, three, four, five, I can increase that to 10.
[20:34] And then we get 10 angular sites. So that one is easy adds to the number of sites adds to the
[20:43] complexity. And the second one is angular step, which is going to offset each radial step spins
[20:51] it if you look at it from the top. So zero to 10 to 50, you can see there's a change in the direction
[21:02] of our sites, not a huge change to what you're doing. Honestly, if you're not using per point
[21:11] variability, which we will get to that. The next one is radius. So if you feel like this crack,
[21:18] this radius, the outer radius, the first one is a bit too small, you can readjust it, let's go 100.
[21:25] And you get a far bigger radius. So if the object that is colliding with, let's say this piece of
[21:32] glass or this geometry collection is bigger, and your original radius is small, that's how you
[21:39] actually fix it. And then you go to step you have 12345 number of steps, you can actually increase
[21:47] that to 10. And this will add to the number of sites that gets generated out of that collision.
[21:55] So kind of be easy on that one, especially I noticed with very high step radius that can
[22:02] create a little bit of unpleasant result. So I'm going to set that with something like six,
[22:07] which makes the result more pleasant. Next one is radial step exponent, again, related to these
[22:16] internal rings. So the lower this number, the higher the resolution is inside this outer ring
[22:25] right here. If I bring this up all the way to something like 10, you will see a huge reduction
[22:32] in the complexity of our simulation. So you can either use one or slightly lower than one,
[22:41] something like point five, to just add a little bit of resolution to what you do.
[22:46] Then we have radial min step and radial noise, and both are going to add noise and a slight
[22:55] resolution to these internal rings. So if I let's say put point five in there, the area of
[23:02] destruction will be not as clean and uniform when I hit fracture, I might actually introduce a little
[23:11] bit of that something like two should be enough. Now one thing that is going to be extremely useful
[23:18] because still after these changes, everything looks very uniform is this per point variability.
[23:26] And that is going to usually misplace these individual slices and gives you a very chaotic
[23:35] look, something that you perhaps are looking for or you expect to see based on your reference.
[23:41] The first one, radial variability is going to misplace these lines, you can see how these lines
[23:48] are kind of connected together at certain points. It's going to move them up and down, so it doesn't
[23:55] look like a complete confined closed ring. So if I go in there and put something like five,
[24:02] you can immediately see how we bring a little bit of chaos and noise into this area. If I increase it
[24:10] to something like 50, that clearly shows you what it's doing is just going to completely mess up this
[24:18] ring. And it looks more, I would say real for lack of better word, I'm going to
[24:23] ever so slightly just readjust my center break. So you kind of see what exactly is happening
[24:31] immediate chaos with one attribute. And to me, that's far more effective that radial noise
[24:39] and angular noise that you may want to have to be assigned to these lines or to these rings.
[24:47] I'm going to tone that down ever so slightly to something like 15. So it looks a lot better.
[24:53] And the next one is perhaps the most effective if you're looking for chaos, which is angular
[24:59] variability. And that is going to displace each site within this ring. So if I put a relatively
[25:08] small number like five, you can immediately see that even without radial variability, how it
[25:16] sort of changes the direction of these internal rings. And it's completely non uniform. Now I can
[25:25] sort of push that to a kind of unrealistic number like 15. And you can see that is a total chaos.
[25:32] I noticed that working with these two numbers will give you a really, really cool result.
[25:39] And of course, the last one, axis variability, again, looks at the direction of the rotation,
[25:47] which is in centimeter and try to displace the verenoid sites even further. So I can just turn
[25:54] off these two and have a look at what this one does. And you can see again, another type of
[26:01] randomness and chaos that it brings into your fracture. So very effective, incredibly powerful,
[26:11] you can get really, really cool results with the combination of these three, and get the fracture
[26:19] tweaked the way that you want. Obviously, we always want to have our gizmos enabled. And we
[26:26] always want to have the center as our gizmo so we can gradually or manually change that in our
[26:35] fracture. So that should do it for a quick overview of the radial fracture. I'm going to go ahead
[26:44] and go fracture and click away. And if I break, you can see it breaks first from the center point
[26:54] and then breaks further into these lines. Cool. I'm going to reset that. And let's talk about the
[27:04] next one, which is called the planar. The planar fracture tool creates planar cuts in the geometry.
[27:13] So making deliberate cuts easier. Again, you can move that to whatever you want. And in here,
[27:24] we have use gizmo on so it's good that we can actually see. Now when you go to rotate, remember,
[27:31] I mentioned that in the radial fracture as well, do not move the object unless it's intentional,
[27:37] you have a strong reason to do so. Rotate the plane. Now with that, you can introduce a little bit
[27:46] of noise. You can introduce a little bit of frequency to it and start fracturing. And you can see from
[27:54] that point that we had that plane, we have our cut. Also, you may have noticed that the gizmo
[28:01] snaps back to the center every time you fracture. And that is because of this center on selection,
[28:09] which we also have in the radial as well. So if you don't want that to happen, you can actually
[28:14] turn that off. And I can now move this guy here and rotate that again, and fracture. And now I have
[28:26] two cuts, two levels as a result. The first level gave me two pieces. The second level gave me
[28:33] four pieces. So very straightforward, really, I can turn off the snap, rotate this to this degree.
[28:41] You can see how deliberate this one is. And this time, it's not going to snap back to the center
[28:47] because we turned off center on selection and fracture. And now I have my cut here, very similar
[28:54] to cut tools in other DCCs that you expect. And it's for fracturing a piece intentionally into
[29:02] multiple sections. You can see I have now level one, level two, level three. And in here, it clearly
[29:10] specifies that this is level one, the first two children and each children have further siblings
[29:18] or children. We have number two. And two cubes came out of the first two cube. And eventually,
[29:25] these last children. So very straightforward in the hierarchy. And in the level statistics that
[29:32] you can see that we end up having six pieces with the three cuts, very straightforward. I'm going to
[29:41] go and select all pieces, go reset and reset to explore next type, which is slice. Now slice builds
[29:54] on the planar fracture tool, allowing you to define the number of cuts that you may want to have.
[30:02] You can see right now, if I reposition my camera ever so slightly, you can see I have one, two,
[30:10] three cuts, which been specified three cuts, three cuts and one cut. You can go and change that you
[30:17] can say I want to have five cuts in X. So now along X, you get to have one, two, three, four, five
[30:25] cuts, just like planar and reposition it. So I can go in there and reposition the plane. And with
[30:35] five cuts in X and three cuts in Y and only one cut in Z, I get to have 48 uniform pieces. And you
[30:45] can go ahead and individually select each one. And let's say I'm going to cut that one to two
[30:53] and to two and fracture. And this one gives me nine individual pieces as well. So very
[31:00] straightforward. Again, just like before, we have noise. And we can group fractures, which is on by
[31:07] default. And there is really not much to it. I can go ahead and explode the sections. And you can
[31:14] see how many sections we have just one underneath because of the slice Z zero to one set to one.
[31:21] And then extra pieces on the top here, and individual pieces that we specified,
[31:27] just like planar, you can rotate that and position that however you want, and get the ideal result.
[31:36] Now I'm going to go select all reset. And get to the next one, which is not really as important.
[31:45] Brick fracture, which is experimental and generate customizable break pattern for, I don't know,
[31:53] a specific scenarios where you feel like you really need break patterns, that is going to get the job
[31:59] done for you. Although there is a notification in Unreal Engine documents saying that this will
[32:07] get a significant update. So what you have right now may not be the case in the future version.
[32:15] So right now, if I go fracture, you can see nothing happens because with brick,
[32:21] the depth is also important. You can see we have a brick length, brick height and brick depth.
[32:28] And perhaps the reason that it's not working because this is a very thin plane, I can go and
[32:35] increase that ever so slightly as soon as I do that, you can see these layers are coming up.
[32:40] So I can sort of change that however I want, like so, to have more or less bricks in there,
[32:49] we have different type of bonds stack English, which is basically looking at the pattern. If I
[32:57] look at it from the top, let's look at it from the top, you can perhaps see more clearly what
[33:04] exactly is happening in here. So different types of bricks. And once you're happy with what you have,
[33:12] you go on fracture, you cancel out. And now I've got individual bricks to deal with.
[33:21] I'm generating 31 pieces out of that fracture type. And the next type would be mesh.
[33:29] The mesh fracture tool uses the shape of a static mesh to define what type of fracture pattern you
[33:38] want. You can have a character running through a closed door. So you see the pattern on the
[33:45] fractured door, these type of scenarios that doesn't happen too often. So what should we bring,
[33:52] let's say bring a cylinder, we push that in, move it up, position it. And eventually,
[34:00] the intersecting surface is going to be one piece, the rest of it is going to be one piece.
[34:05] So it's going to produce two bones, two extra pieces for us. I'm going to select the
[34:11] fractured object, the collection geometry object, I'm going to go and select mesh.
[34:17] And then the most important bit is mesh cutting, cutting actor, nominate what static mesh you
[34:26] would like to use. I'm going to use cylinder two, that name pops up here. And simple cutout or single
[34:36] cut is what we are looking for at this point. So I'm going to go and select my geometry collection
[34:43] and go fracture. Now if I move this piece up, you can see I have two children, one is the whole,
[34:52] the cutout. And the second one is the rest of the geometry collection. If I go ahead and
[34:59] simulate, you can see that piece will get cut out and get detached from the geometry, the plane that
[35:07] we have. And the last one would be custom. And with custom, it kind of is the most flexible
[35:15] option. It allows you to sort of manipulate the fracture diagram as an independent entity.
[35:24] What it's going to do, it's going to put some of these into one right here. So if I select my
[35:31] collection, geometry collection and go custom, you can see first thing you may have noticed,
[35:37] I'm going to get pattern, which you can set to centered, which is going to be our cluster right
[35:43] here. So I can increase the variability, you can see immediately, we're getting something very
[35:50] similar to what cluster usually gives us. And you can add number of sites. So increase the
[35:59] resolution, let's go 50, I'm going to reduce that one to 30, or increase that to 100. And you can
[36:06] see how that is going to bring chaos, again, very similar to cluster. The next one would be uniform,
[36:11] which as the name suggests, is actually the uniform that you're using right now. With those two off,
[36:17] it gives us exactly uniform with the rest of the information, including noise that you can add.
[36:25] And then this one gives you grid, which you can again, get the same result using slice or planar,
[36:34] if you want to. And of course, the rest of it, based on the vertices of your mesh,
[36:40] and individual selected bones that you can select. So that is a quick look on how these fracture types
[36:51] contribute to the look of the project. Now, one thing that I have not mentioned yet is the
[37:01] tolerance of the breakage. So up to this point, you have seen me doing selecting this, go to uniform
[37:10] and fracture. And once the collision happens, you can see everything breaks apart. But we never
[37:18] talked about the tolerance, why they're breaking apart, how they're breaking apart, and what is the
[37:25] glue factor, what if we want to have certain pieces attached together. So we have maybe one or two
[37:33] breakage or two cuts, but not more than that. So let's go to the next chapter. While it's directly
[37:40] connected to your fracture type, it's something that actually your geometry collection controls.
[37:49] So let's go to the next chapter and talk about that as well.
[38:00] Now, before we wrap up this first part of chaos destruction step by step tutorials,
[38:06] because obviously the video is getting a bit long, let's talk about glue strength or
[38:14] the breakage ratio or as we call it in Unreal Engine, damage ratio. What do I mean by that?
[38:23] Let me select this model right here and create a geometry collection out of that. So I'm going to go
[38:29] into chaos, call that pot GC for geometry collection pot. So we can break that. And then I'm going to
[38:39] go into uniform, just zooming in on the pot. And let's create 50 by 50 sites. So it generates
[38:54] more or less 45 to 50 bones for us. I'm going to give this a little bit of amplitude for the noise
[39:03] and very low frequency. And let's go fracture. Now it's all good. Let's simulate. Nothing happens.
[39:16] Because up to this point, without you even knowing, I lowered the damage ratio on any of these
[39:25] objects, I can move it even higher to intensify the impact, nothing happens.
[39:32] The reason is, if I look at my geometry collection pot in the outliner, go to its details panel and
[39:42] scroll down, we should get damage rollout. By default, we have index zero, which looks into level zero.
[39:51] And it says, how much strength you want me to put onto this destruction? Do you want me to
[40:01] have a very high threshold, which in that case, nothing is going to break apart, or you want to
[40:08] have a relatively lower ratio for your damage model. So as soon as it hits any collision object,
[40:17] it breaks apart. Once it breaks apart, then it looks into any further levels that you have.
[40:24] And if you have a sort of fracture pattern on your level one, so you can have more pieces,
[40:33] then it looks to index one to break those pieces even further. So without tweaking that attribute,
[40:42] you're really not going to get much of a result. So now with this index zero set to 500, if I go and
[40:53] play, it breaks apart. I can even intensify it further or lower the ratio. So it means that a
[41:04] slightest touch to any collision object, and all of these pieces will come out. Look at that. Bam.
[41:13] So that's a very important part of your geometry collection that you need to be mindful of, and
[41:22] you need to set right off the bat. If I go and set that one to let's say 500,000, I believe the
[41:30] default is 5 million, you will see some resistance, I'm going to lower this down to 50000, and you can
[41:38] see it breaks apart. But some of these pieces eventually glue together. So I'm going to press
[41:48] Shift B so I can kind of see that and switch to selection mode. So it's much easier to see for
[41:55] you guys, run it again. Not much really happening right now. So I'm going to lower this
[42:04] to 50000, and things are start breaking. Now, if you want to have more layers to be added
[42:17] to this model, you sure can. I'm going to go select all and with everything selected, I'm going to go
[42:25] and apply the second uniform. This time, I'm going to set that to maybe 20, 20. So each piece,
[42:35] each bone will get fractured further. And I'm going to introduce still a little bit of noise,
[42:43] maybe 0.2 for frequency and fracture again to go to my second level. So for the first level,
[42:53] I'm generating 39 pieces, which you can see by the way, like this, the exploded view.
[43:03] All right, now I know how many pieces have been created. And I have already successfully fractured
[43:09] everything. Now we need to kind of look at the damage ratio. So selecting the geometry collection,
[43:19] go to damage ratio, you can see the index zero, it is 500,000, I'm going to lower it down to 50,000.
[43:28] And the second one, I'll lower it down to 500. So it breaks first from level zero.
[43:37] And perhaps it's going to keep some of it. But as soon as the rest of the group from index zero,
[43:44] hit any collision object, because of this low threshold for damages, they're going to break
[43:52] into further pieces. I might as well bring that one to 50. So it's really obvious to see,
[43:59] we don't have any third level of destruction, we don't have any index three. So this one is
[44:06] clearly ineffective at the moment. So now I'm going to click, it breaks, and it even breaks
[44:14] into smaller pieces, as you can see, I'm going to lower the tension again from 50,000 into 5000
[44:25] from my index zero for my level one, and lower index one, which is level two, to even a lower
[44:34] value to make sure that everything falls apart super easily. I'm going to simulate.
[44:44] And you can see clearly we have different pieces falling apart in no time.
[44:52] So understanding damage values that you set for your geometry collection is extremely important.
[45:02] I didn't talk about that right at the beginning, because understanding fracture was to me more
[45:07] important. And once you understand the types of fracture, then how much fracture you actually
[45:13] want to apply, you definitely need to pay a visit to damage threshold, which is by the way,
[45:19] only one of the important attributes that can get your result. Obviously, we have damages,
[45:28] we have dampening, we have force fields that we are going to explore. But you can see by changing
[45:34] one attribute, I'm getting so many different variations. I'm going to bump this up to 50,000.
[45:41] And now those smaller pieces are not going to break that easily, you can see that. So pretty cool
[45:48] stuff, really good results that you can get with damages and setting your damage threshold
[45:57] properly before or after you do the simulation. And if you wish to tweak that, even further.
[46:04] All right, that should do the trick for one lesson. In the next lesson, we're still going to deal with
[46:11] basics, we're going to talk about selection some more, we're going to talk about edits,
[46:16] we're going to talk about cluster. And within utilities, we are going to pick some of the very
[46:21] important ones, like the material or tiny geometry, to be able to fully understand how chaos
[46:30] destruction works. And hopefully in the third video, we get to more exciting stuff. In the third
[46:37] video, we get to practice with some fun projects, because we already understand fully how destruction
[46:46] works. And we can take it from there. All right, that should really do the trick. I truly hope you
[46:53] guys found the tutorial, the video useful, and use that in your own projects. And until the next one,
[47:03] see you guys later.



---

## Captured Frames

- [2:00] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_000.jpg
- [3:06] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_001.jpg
- [5:00] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_002.jpg
- [9:49] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_003.jpg
- [17:14] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_004.jpg
- [19:33] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_005.jpg
- [27:13] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_006.jpg
- [40:53] tutorials/frames/ue5-series-chaos-destruction-complete-guide-part-1/frame_007.jpg

---

## Structured Notes

### Core Technique
End-to-end foundations of **Chaos Destruction**: enabling the plugins, switching to **Fracture Mode**, building a **Geometry Collection**, applying each of the 7 fracture types (Uniform, Cluster, Radial, Planar, Slice, Brick, Mesh, Custom), and controlling breakage via the **Damage Ratio** (per-level threshold).

### Summary
Reza (SARKAMARI) opens Part 1 of a 3-part Chaos Destruction series with a deliberately simple scene (a statue + a rock/crate) so the focus stays on principles rather than a flashy demo. He covers plugin setup (Chaos Niagara, Chaos Solver, Chaos Caching, optionally Chaos Caching USD for cloth/Marvelous Designer work), the Fracture Mode workflow (`Shift+6`), creating a Geometry Collection from one or more static meshes (or nested Geometry Collections), the two conditions an asset needs to be a good GC candidate (watertight geometry; no intersection between adjacent GCs — leave a small gap), and a first uniform Voronoi fracture + simulate pass. The video then surveys all 7 fracture types in detail (their unique parameters, typical use, and pitfalls), and closes with the critical-but-easy-to-miss **Damage Ratio** rollout that actually controls whether/how a fractured object breaks apart on collision.

### Key Steps
1. **Enable plugins**: Edit -> Plugins -> search "chaos" -> enable **Chaos Niagara**, **Chaos Solver**, **Chaos Caching** (add **Chaos Caching USD** if importing cloth/Marvelous Designer via USD) -> Restart editor.
2. **Switch to Fracture Mode**: `Shift+6` (from Selection Mode) opens the Fracture Mode toolset with three panels that must stay open together: **View Settings**, **Level Statistics**, **Fracture Hierarchy**.
3. **Create a Geometry Collection**: select one or more Static Mesh actors (or existing Geometry Collections to nest) -> Generate rollout -> **New** -> choose a save folder -> **Create Geometry Collection**. Two hard requirements for a good candidate: (a) the mesh must be **watertight** (no open faces/edges, or simulation performance suffers), (b) when combining multiple assets into one GC, leave a small gap between them — intersecting geometry causes objects to push each other apart oddly during simulation.
4. Fresh GCs start at **Level 0** with 1 bone (the whole mesh, unfractured) — visible in the Level Statistics + Fracture Hierarchy panels.
5. **Simulate without fracturing** first to confirm collision alone (four-dots icon -> Simulate -> Play) — any fracture-mode asset automatically gets collision.
6. **First fracture**: select the GC -> **Uniform (Voronoi)** -> keep Min/Max Voronoi Sites low to start (high values + repeated fracture passes on every child piece can explode piece count and crash the editor from memory pressure) -> add a little **Noise** (Amplitude/Frequency) to break up perfectly straight Voronoi lines -> **Fracture**. `Shift+B` toggles bone-color visualization (or check "Show Bone Colors" under the GC) to preview cuts before simulating. **Reset** clears fracture levels to start over; fracturing again on an already-fractured GC adds a *second* level that fractures every child piece individually (multiplies piece count fast).
7. **Fracture type survey** (each applied via the Generate/Fracture rollout on a selected GC):
   - **Uniform** — Voronoi-based, evenly spaced pieces (classic window-crack look); add Noise for realism.
   - **Cluster** — extends Uniform with randomized close-proximity islands ("Clusters" grouping rollout) for more varied results from the same site counts (e.g. 8x8 input still yielded 82 bones in the demo) — watch piece-count growth before adding extra fracture levels.
   - **Radial** — Voronoi sites radiating from a movable center gizmo (never move the object itself, move the gizmo). Key attributes: **Angular Steps** (site count around the ring), **Angular Step** (rotational offset per ring), **Radius**, **Radial Steps** (ring count), **Radial Step Exponent** (lower = higher inner-ring resolution), **Radial Min Step** / **Radial Noise** (adds irregularity to ring spacing). **Per-point variability** trio — **Radial Variability**, **Angular Variability**, **Axis Variability** — is called out as the most effective way to break up an artificially uniform radial pattern; Angular Variability in particular gives strong chaotic results even at small values (~5-15).
   - **Planar** — deliberate straight cuts via a rotatable/movable plane gizmo; **Center On Selection** toggle controls whether the gizmo re-centers after each fracture (turn off to keep cutting from a manually offset plane for successive deliberate cuts, building up Level 1/2/3 hierarchies).
   - **Slice** — Planar's multi-cut big brother: set explicit cut counts per axis (X/Y/Z) for uniform grid-like breakups (demoed: 5 cuts X x 3 cuts Y x 1 cut Z = 48 pieces).
   - **Brick** — experimental (flagged by Epic docs as subject to significant future changes); needs sufficient mesh depth to work (fails silently on a too-thin plane) — Brick Length/Height/Depth plus bond patterns (e.g. Stack, English) control the brick layout.
   - **Mesh** — cuts using the silhouette of a separate static mesh as a cutting tool (e.g. a cylinder used as a "hole punch") — set the **Mesh Cutting Actor** to the tool mesh, choose **Single Cut**, then Fracture; produces two bones (the cutout + the remainder) — classic "door with a bullet hole / breach pattern" use case.
   - **Custom** — most flexible; a **Pattern** dropdown (Uniform / Cluster-like / Grid / mesh-vertex-based) applied to independently selected bones, effectively re-deriving the other fracture types' looks under one tool.
8. **Damage Ratio (breakage threshold)** — the actual on/off switch for whether a fracture reacts to collision: select the GC -> Details panel -> **Damage** rollout -> per-hierarchy-level **Index** entries (Index 0 = Level 0, Index 1 = Level 1, etc.). High values (millions — default around 5,000,000) = very resistant, low values (tens of thousands or less) = breaks apart on the slightest touch. Each level's index must be tuned independently — a low Index 0 with no Index 1 tuning means Level 1 children won't cascade-break further. Demonstrated on a 45-50 bone pot: Index 0 from 5,000,000 down to 500 made it shatter instantly; adding a second fracture level and lowering both Index 0 and Index 1 (e.g. to 5,000 and lower) produced cascading multi-level collapse.

### UE Systems / Blueprints / Settings
- Plugins: Chaos, Chaos Niagara, Chaos Solver, Chaos Caching, Chaos Caching USD
- Fracture Mode (`Shift+6`) panels: View Settings, Level Statistics, Fracture Hierarchy
- Geometry Collection asset (Generate -> New); nestable from multiple static meshes or other GCs
- Fracture types: Uniform (Voronoi), Cluster, Radial (Angular Steps/Step, Radius, Radial Steps, Radial Step Exponent, Radial Min Step, Radial Noise, Radial/Angular/Axis Variability), Planar (Center On Selection), Slice (per-axis cut counts), Brick (experimental; Length/Height/Depth, bond pattern), Mesh (Mesh Cutting Actor, Single Cut), Custom (Pattern: Uniform/Cluster/Grid/vertex-based)
- `Shift+B` — toggle bone-color visualization (or "Show Bone Colors" property)
- Damage rollout: per-level **Index N** damage/breakage threshold (high = resistant, low = fragile); defaults around 5,000,000
- Two GC-candidate rules: watertight geometry (no open faces/edges); no intersection when combining multiple assets into one GC (leave a small gap)

### Difficulty
Intermediate

### UE Version
Not stated by the narrator; editor UI (Fracture Mode toolset, Damage rollout, Brick-fracture "experimental" warning) matches the UE5.3-5.5 era Chaos Destruction toolset.

### Tags
#chaos #destruction #vfx #fracture #cinematics #intermediate

---

## Related Entries
- Physics in Unreal Engine (`tutorials/physics-in-unreal-engine.md`) — Epic documentation reference covering Chaos Destruction (fracture, fields, anchor constraints) at a higher level; this tutorial is the hands-on walkthrough companion (confirmed gap: only 2 tangential mentions existed before this ingest, no dedicated fracture-workflow video).
- `references/chaos-physics.md` — the skill's synthesized Chaos notes; this entry supplies the concrete step-by-step fracture-type parameters that reference file summarizes.
- Cheap AI Mocap that Actually Works (`tutorials/cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma.md`) — shares `#chaos` `#destruction`, uses Chaos Destruction tangentially inside a broader mocap pipeline.
