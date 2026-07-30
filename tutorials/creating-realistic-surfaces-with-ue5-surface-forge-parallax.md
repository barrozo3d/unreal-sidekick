---
title: Creating Realistic Surfaces with UE5 Surface Forge Parallax
source: YouTube
url: https://www.youtube.com/watch?v=RPEvhresGAk
author: Arghanion's Puzzlebox
ingested: 2026-07-29
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/creating-realistic-surfaces-with-ue5-surface-forge-parallax/
frame_count: 0
frame_status: pending-selection
---

# Creating Realistic Surfaces with UE5 Surface Forge Parallax

**Source:** [YouTube](https://www.youtube.com/watch?v=RPEvhresGAk)
**Author:** Arghanion's Puzzlebox
**Duration:** 33m10s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py creating-realistic-surfaces-with-ue5-surface-forge-parallax <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello, everybody, and welcome to Arganion's Puzzle Box.
[0:05] In today's video, we're going to showcase the capabilities of the Surface 4 using displacement
[0:11] mapping and parallax occlusion mapping.
[0:13] This video is intended for people who want to understand what are the benefits of parallax
[0:17] occlusion mapping versus displacement mapping or the other way around.
[0:22] This system is very scalable and can add a lot of depth and a lot of character to your
[0:27] scene.
[0:28] What you're seeing right now is an example of this used in action in the World Forge
[0:34] as a subset of the system, which allows you to drive a lot of detail that wouldn't be
[0:38] possible without using Nanite displacement or, like I said, parallax occlusion mapping.
[0:45] So if you're interested, stick around.
[0:47] If you've got the Surface 4 and if you don't know how to use these features, then this
[0:51] video is for you.
[0:53] But if you haven't got the Surface 4 and you are interested, take a look on Fab or on my
[0:57] Patreon as it is available there.
[1:00] Right now, it's actually for free on Fab for a limited time.
[1:04] And on Patreon for the price of a coffee, you can have access to it and its future updates.


### General Comparison [1:09]
**Transcript (timestamped):**
[1:09] So yeah, let's begin.
[1:10] There are a few ways to make flat surface look deep in Unreal Engine, at least that I know
[1:15] of.
[1:16] I'm sure there are other ways, but it generally can be real geometry, but it can also be using
[1:22] either parallax occlusion mapping or displacement.
[1:27] And in particular, here, I have two examples, right?
[1:31] You can see in here this is Nanite displacement.
[1:33] And the dead giveaway is the fact that it actually has a silhouette, which this silhouette
[1:38] is being driven by the fact that geometry is displaced based on a height map.
[1:45] And because Surface 4 is a multi-layer system, there are multiple height maps in here, multiple
[1:51] layers that are doing that together.
[1:54] Now, in this particular example here, I am using quite a high displacement value just
[2:00] to illustrate the point.
[2:03] And then this particular scenario over here, we have the same kind of thing.
[2:09] I mean, the same paint, the same, it's not the same mesh necessarily, but they share
[2:14] the same vertex color information, as you can see.
[2:17] But this one is using parallax occlusion mapping with shadows.


### Parallax Occlusion Breakdown [2:19]
**Transcript (timestamped):**
[2:22] So what this means is that this system does have shadow casting capability, which is really
[2:28] quite nice.
[2:29] As you can see here, when I move the directional light around, shadows will react to it.
[2:37] And so will the shadows on the real geometry ones, the Nanite displacement one, because
[2:42] of course, this is actual geometry that is blocking the light.
[2:45] Now, the parallax occlusion mapping technique is using shadow sort of, you know, it's more
[2:51] like a trick, right?
[2:52] It's a parallaxed shadow cast and it's only self shadow.
[2:59] This shadow cannot propagate to anything else.
[3:01] So that's important to know.
[3:03] While with this mesh, as you can see, these shadows here are affected by the geometry
[3:08] of this plane.
[3:09] So that looks different.
[3:10] So there are multiple caveats here.
[3:12] There's obviously going to be cost performance.
[3:15] There's a lot of other things to take into account, but we will be discussing those in
[3:19] a bit.
[3:20] So that's a direct comparison.
[3:21] If we actually switch over to shader view here with multiple layers, so this is using
[3:25] three layers plus water puddles in the same here, you can see that the parallax occlusion
[3:29] map version is a bit more expensive in instructions than this particular material is here, which
[3:35] is just using Nanite displacement.
[3:37] Now, obviously, what I was saying, parallax occlusion mapping is adding some instructions
[3:42] on top, but it's also a very scalable system, meaning that if you start stripping it down
[3:46] of multiple parts, then it's actually going to decrease in performance cost.
[3:51] And also one thing to note is that if we actually open the material instance of this system
[3:57] of parallax occlusion mapping, and we have a look in here, we do actually have options
[4:02] to, for example, disable the parallax occlusion effect and only keep the shadows, which is
[4:08] a bit of a, you know, it's not really going to do much for you in the sense of you still
[4:13] that geometry is going to be gone, the perceived geometry, and you're only going to have these
[4:16] shadows, which I guess it could be useful if you're trying to add some depth.
[4:21] Obviously, the instruction count would have decreased.
[4:24] So again, if we disable this option, you'll notice that this system has become more expensive
[4:30] now because we're also using a height ratio for the, you know, sort of like perceived
[4:34] geometry or fake geometry.
[4:36] And also you can look at, in terms of like, you know, it's actual level of steps, which
[4:43] again will, you know, we have minimum steps, you have maximum steps.
[4:46] So if you go for like, you know, the bare bare minimum, maybe of steps, you'll notice that
[4:52] there's quite a degradation of performance here, sorry, of how it looks.
[4:57] But in theory, this would have become a bit cheaper, although not quite visible, because
[5:02] parallax occlusion mapping has a angle performance cost.
[5:06] So if I actually go in here and, you know, I let's say I go for minimum steps, I want to go to like
[5:11] eight, right?
[5:13] And then I want to do pay OM a max step, something like 64, you'll notice that the shader complexity
[5:18] has not actually changed from an instruction point of view at all.
[5:22] But its actual cost has actually increased.
[5:25] Although now this system looks a lot better than it did before.
[5:28] But bear in mind that shallow angles like this will break the parallax occlusion mapping effect.
[5:33] And the puddles themselves are not parallax occluded, at least not in this version of
[5:37] surface forge, but I am planning on giving an option for that as well, which means that the
[5:42] water in certain cases will be perceived as floating above this geometry at angles like
[5:48] this, right?
[5:49] But you wouldn't really use this kind of angle on a ground floor and you wouldn't have
[5:54] puddles on a wall.
[5:56] So, you know, bear that in mind.
[5:58] But what I was going to say is that you can check for POM complexity debug.
[6:03] So if you actually enable this per layer, this will show you how expensive this material
[6:10] actually is.
[6:11] So you can see in here for the A layer, which is this cobblestone, it's actually not very
[6:17] expensive here.
[6:18] This is why it's full green, but it goes really red in the distance.
[6:21] Okay.
[6:22] And if we actually increase the complexity on all of these layers.
[6:25] So now all, you know, all three layers are showing us complexities.
[6:29] We can now see just how it's very cheap if you look above.
[6:33] So it's actually almost like a zero cost.
[6:35] It's like the shade that itself has no parallax occlusion mapping when you're doing
[6:39] this, because it's not a lot of computation to be done for an angle, you know, from a
[6:43] camera angle point of view.
[6:45] So there's not that much going on.
[6:47] But when you're looking at it from the sideways, this is when the shade that has to
[6:50] do all the heavy lifting.
[6:52] And this is when it has to trick your perception that it actually has depth.
[6:56] Now, if you look over here on the minimum steps, if we turn that to one, for example,
[7:01] you'll notice that now performance has improved.
[7:04] But also if we turn this to something like an eight, I mean, the performance is
[7:07] extremely improved, almost no real cost of no, no extra headroom of cost of
[7:15] computational cost for your system.
[7:18] If you're using parallax occlusion mapping, apart from the initial instruction count.
[7:22] Okay.
[7:23] But like I've said to you, if we now switch over to like, you know, let's just
[7:27] watch its actual, you know, like performance, like how does it actually look?
[7:34] Okay.
[7:34] You might say, you know, from this angle doesn't really look too bad.
[7:37] And maybe it's not even perceivable that you actually have a problem.
[7:42] Like again, this is how big the character is.
[7:44] This is how big the mesh is.
[7:45] You know, at this distance, you can actually use those steps, have a very
[7:48] performing parallax occlusion map, shader and not really suffer the consequences of
[7:53] it. And it's actually more performant than what the nano displaced mesh would be
[7:58] in this particular case.
[7:59] Now, what I would say is that obviously this is because the parallax occlusion mapping
[8:03] has undergone quite a lot of changes for the surface forge to accommodate for some
[8:08] of this and also to perform very well with shadows as well.
[8:11] So we're using quite a bit of, you know, quite a few tricks under the hood to make
[8:16] this look and run better.
[8:19] Also, you can even rotate it.
[8:22] So there's no actual problem.
[8:24] Like for example, if we rotate the mesh, the shadows will also update, right?
[8:30] With that rotation, which means that we have correct shadow displays from POM.
[8:36] If you ever were on the fence of actually using parallax occlusion mapping or not,
[8:41] try the surface forge and parallel occlusion mapping will work for you rather
[8:45] than against you. I'm also experimenting with a new feature, which is parallel
[8:49] occlusion map silhouette.
[8:51] So this particular mesh in here is using parallel occlusion mapping and it has
[8:56] silhouette on the sides, as you can see there.
[8:59] And this is quite obviously quite useful.
[9:01] This is a niche use right now, but I am developing it into a full screen space
[9:07] with a displacement solution that will work alongside parallel occlusion mapping.
[9:11] So again, instead of using nanodisplacement, you could use this and still have these
[9:15] silhouettes on the edges.
[9:16] So that's really neat as well.
[9:19] Now moving on back to parallel occlusion mapping, there's a lot of controls.
[9:24] There's general controls for parallel occlusion mapping and you get these controls.
[9:28] If you go on any particular layer in here, right, like layer A and enable POM.
[9:33] Now you can also disable the shadows of that parallel occlusion mapping per layer.
[9:38] So right now the shadows have been disabled for layer A and the cost of
[9:43] performance has dropped.
[9:45] Again, if you actually enable shadows, this will move the instruction count just
[9:50] slightly ever so slightly.
[9:51] Okay.
[9:53] Other things about the parallel occlusion mapping, you can also control its actual
[9:56] shadow intensity.
[9:58] So you can art direct your shadows and make some extremely moody looking scenes.
[10:03] Something that the displacement tech tech in here from Nanite will not allow you to
[10:09] do, but actually, you know, if you really, really want to play around with this, one


### Using Art Directed POM Shadows with Nanite Displacement [10:10]
**Transcript (timestamped):**
[10:14] thing that you can do, you could go over to the parallel occlusion mapping settings.
[10:19] You could say, you know what, I just want the parallel occlusion map shadows only.
[10:23] Okay.
[10:24] So that means that only the shadows are being casted on all layers.
[10:28] And then you can have a look down here.
[10:31] As long as you got Nanite enabled on this mesh, you can enable tessellation.
[10:36] And obviously the map, my magnitude here is horrendously high.
[10:39] So we're just going to put that down to maybe like a, maybe like a two or one or
[10:43] something like that.
[10:44] But here's the thing.
[10:45] Look at those shadows, right?
[10:46] Look at the difference between here and here.
[10:50] You see how there is a lot of like fake shadows being added because of a
[10:54] parallel occlusion effect.
[10:56] Now I personally would not recommend that you use both of these technologies
[11:00] together if you're going to do this in a video game, right?
[11:03] Because the cost of performance is going to be significant.
[11:07] What I would say you can, you know, you can use parallel occlusion mapping on
[11:12] its own, but if you are doing cinematics or anything like that, then you might
[11:15] want to combine the parallel occlusion map shadows with Nanite displacement for
[11:23] Art Direct in those shadows.
[11:24] Because again, like I've said to you, right, there is a, there's a, there's a
[11:28] actual control here.
[11:30] So if I go into material A again, and I look at the shadow intensity, you can
[11:35] see that that that's shadow that's being added, or you can even invert it, obviously,
[11:40] that wasn't there to begin with.
[11:42] So if we would go and say, you know what, I don't actually want parallel occlusion
[11:47] map for a layer A at all, then you just get the Nanite displacement shadows on
[11:54] that layer, which again, nothing is stopping you.
[11:57] If you want to have parallel occlusion mapping on another layer, but you want to
[12:00] have a Nanite displacement on layer A, that's entirely possible for you to do so.
[12:06] So again, a very flexible system, all due to the fact that surface forge is the
[12:11] driving factor that allows it to happen.
[12:14] So that's kind of the view, so to speak, of parallel occlusion mapping.
[12:20] Paralloc occlusion mapping is not controlled by a weight parameter in the
[12:23] sense of like, well, actually, let me just disable this desolation feature here.
[12:30] And I'm going to go into layer A. Sorry, I'm going to go in here and just say I
[12:34] want to give my parallel occlusion mapping back on.
[12:38] If I can find it, there we go.
[12:40] So I don't want just shadows only.
[12:42] So that was just normal, right?
[12:44] Normal parallel occlusion mapping.
[12:45] If I go over here and I look at the height information, you can see that there
[12:50] is a difference, not in the, so the difference when I change these targets,
[12:55] low, high and so on, the difference is not in the actual how POM is reacting to it.
[13:00] The distance is simply happening due to height blending between the three layers.
[13:07] Okay.
[13:07] But if you do want to change the height of how this parallel occlusion mapping behaves,
[13:12] you can go over into the parallel occlusion mapping or height ratio and increase this,
[13:17] right?
[13:18] You could do something like this.
[13:19] But if you go too high, like I have right now, you'll notice a lot of ghosting,
[13:24] which could be looked at completely bad.
[13:26] At this point, you want to increase your actual steps.
[13:30] So, you know, something like that.
[13:32] Okay.
[13:32] The higher you go, the more steps you will need.
[13:34] Honestly, this is going to make the cost of this proportionally high.
[13:39] And then again, it's going to kind of break the effect anyway, because it's going
[13:43] to make some of these shapes be completely driven.
[13:47] I wouldn't driven upwards or downwards.
[13:50] I wouldn't play around with the reference plane too much, because again, that's going
[13:54] to like maybe it can help you in some situations.
[13:57] But by default, you want to keep that to 0.5.
[14:00] So 0.1 on the POM height ratio is too high.
[14:03] I personally recommend the 0.05 or the 0.03, which gives you just enough depth
[14:09] to make this surface come alive.
[14:12] So that's it for parallel occlusion mapping.


### Nanite Displacement Usage & Options [14:15]
**Transcript (timestamped):**
[14:15] Now we can have a look a little bit on the displacement side of things.
[14:20] And this is a topic on its own, but it's quite a simple system to set as opposed
[14:27] to parallel exclusion mapping.
[14:29] The best way for me to showcase Nanide displacement in general is to just use
[14:34] a plane where there is no Nanide displacement present.
[14:38] And you can see how flat this looks.
[14:40] Obviously, as opposed to this one, it is completely flat.
[14:44] We're using a material instance that is different from that one.
[14:49] But more importantly, right now, we are, you know, if I open it, we, you know,
[14:55] we'd look at it.
[14:57] We're not seeing any displacement and you might not be able to see any
[15:00] displacement because of a number of factors.
[15:03] But first of all, you've got to scroll down in your material instance and make
[15:07] sure that enable tessellation is enabled.
[15:10] If you are in Unreal Engine 5.3, you will not have this option, but you can
[15:15] enable displacement from the main shader.
[15:17] If you don't know how to do that, I do have tutorials on it.
[15:19] So take a look on my channel.
[15:22] I believe there's a, I mean, yeah, there's a story about displacement mapping
[15:25] and tessellation in general that will show you what I mean.
[15:28] But the point is that if you have enabled tessellation and you've got
[15:32] displacement scaling, you know, maybe values like this, right?
[15:35] And you look at it and it's still flat.
[15:37] Then the main reason for that will be based on your mesh.
[15:42] So if you actually open the mesh and you right click it, you have to
[15:46] make sure that Nanite is enabled.
[15:49] Once Nanite is enabled, you can now see the displacement does work.
[15:52] But there is also a scenario in which you might use one of these vast
[15:57] material instances that I have in here that comes with the Surface Forge.
[16:01] And there might be no displacement when you actually enable it and you might
[16:04] be thinking, what the hell is going on?
[16:06] Well, what could happen is you could be using a displacement mask.


### Blend Masks and Painting Mode [16:10]
**Transcript (timestamped):**
[16:11] And if this is enabled, I'll show you what I mean.
[16:14] If this is enabled, currently we're kind of getting some displacement in some
[16:18] areas, but in others we're not.
[16:21] If you bring a, you know, like a, like an actual mesh into your Unreal Engine
[16:26] content folder by default, if you go over to modeling and to attributes
[16:31] and vertex painting, I will have all these channels here.
[16:35] They look like, you know, a bunch of different shades added, but actually in
[16:40] reality, and I will show you this, the way that all of these will come in
[16:46] will be like this.
[16:48] Okay.
[16:49] So that's how the vertex information will look like.
[16:52] So I'll press accept.
[16:53] See, this is how, this is how actually this material would be looking on a mesh
[17:00] applied that's just been, that's just been brought into Unreal Engine.
[17:03] Because it holds vertex information in all three channels plus the alpha.
[17:07] And right now the alpha, which you can see in here, well, actually not the
[17:11] alpha, the green channel currently is acting as a mask to disable, you know,
[17:19] basically displacement.
[17:20] And we can change this.
[17:21] And obviously you do have to have a channel selected, but we can disable this
[17:24] and make it so that it's the alpha channel instead of the green channel or any
[17:28] other channel really.
[17:30] So at this point means that it means that we don't have any displacement
[17:33] because it is being masked away.
[17:36] Now, what we could do, we could go into paint vertex color and we could go and go
[17:41] to the erase color, change this to black and change the alpha to zero.
[17:45] This is very important that you do this.
[17:48] Press OK.
[17:49] And then I want to just paint in the displacement into the, sorry, into the
[17:53] alpha here, and I'm going to hold shift and left click so I can erase.
[17:58] Okay.
[17:59] And as I do this, even if I switch over to the original material, there's still
[18:03] no displacement visible.
[18:05] And right now I'm not painting any layer apart from the alpha.
[18:08] But once I click accept, you will notice that we now have displacement in this
[18:13] area, but only after pressing accept, because that's how vertex color works.
[18:17] It's waiting for you first to paint and then it will apply displacement from the
[18:21] shader.
[18:22] I don't know if they're going to change this in Unreal Engine in future releases,
[18:25] but as a 5.8, this is still the case.
[18:28] Anyway, once you do this and you get displacement there, now you understand
[18:31] that if you paint all of this or if you erase the alpha channel, which we can do.
[18:37] So you erase all and then press accept.
[18:39] Now we can see that we have displacement everywhere.
[18:42] And consequently, if we actually start painting, let's say in the red channel,
[18:47] right now red channel isn't doing anything for us, but maybe the green channel.
[18:53] So again, green channel doesn't seem to be doing anything.
[18:56] And then we can also try the blue channel.
[18:59] And I'm pressing accept and nothing really changed.
[19:03] So we've got to understand why.
[19:05] Well, if we're going to paint vertex color and we select RGB and you switch
[19:09] from original material to lit vertex color, you'll notice that these are already
[19:14] painted.
[19:15] So you want to erase all.
[19:18] And then if we press accept, this is what the mesh should be looking like,
[19:22] because without any vertex information, it will default to the primary layer,
[19:26] which is layer A. So we're going to paint vertex colors and we're going to
[19:30] switch over from lit vertex to original material.
[19:34] Maybe I'll use the green channel and add it over here.
[19:36] And you can see I'm doing the blend there.
[19:39] Also, I can do the red channel here and then I could do the blue channel.
[19:44] And this is based on settings that we've done in our material blending category.
[19:49] And I've got videos on that topic as well.
[19:52] So this is how displacement is in general, you know, done.
[19:57] And it's driven by the ORD map, but it can also be driven by a exclusive
[20:02] height map if you choose so.
[20:04] I've covered that in a previous video.
[20:06] The same logic applies to parallax occlusion mapping as well.
[20:10] But that is the whole point.
[20:11] Now, if you want, you could, for example, go in here and just say, you know what,
[20:17] just don't use vertex color to blend mask anyway.
[20:20] At this point, it just sort of defaults to not using any information whatsoever.
[20:26] But the system will automatically load up, you know, it doesn't like a
[20:30] displacement masking here.
[20:32] It will just assume that there's no, you know, the color information is set to one
[20:37] across the board.
[20:38] What we can do, however, we can enable mesh paint instead.
[20:42] So we can go in here and say add mesh paint to blend mask.
[20:47] So we can enable that.
[20:49] And now the system is expecting us to start painting some information into it,
[20:55] OK, which means that if we let me just put this away, if we look at this mesh,
[21:02] we can scroll the way down here in the mesh painting, select this point,
[21:09] switch this maybe to like a 2048 or something like that.
[21:12] OK, let me just press accept here.
[21:14] Sorry. Obviously, displacement is enabled.
[21:18] We have no color information.
[21:19] Like I said, we have no color information or vertex information
[21:22] because we also disable vertex information to be used for painting.
[21:26] So this placement now has a full rain, has a value across from this layer.
[21:30] So at this point, we can choose to go from modeling mode to mesh paint mode.
[21:35] We can click the add button and now we can paint away.
[21:38] So if I actually paint red, see, I'm adding that in there.
[21:43] And if I go and paint green, then I'm adding this particular texture.
[21:50] But then if I paint alpha, then I am effectively
[21:55] removing displacement, but because the strength of this tool is 0.5,
[21:59] I just put that to one.
[22:00] And now I'm doing all this.
[22:02] Oh, sorry, I forgot to also mention in this particular state,
[22:06] I am using alpha as a driving factor for puddles.
[22:11] But I'm also displacing, you know, mask, displacing the alpha.
[22:16] Sorry, mask of using the alpha to displace to hide the displacement.
[22:21] So I did at this point, if I don't want to use the alpha for that,
[22:27] I could just say, you know what, why don't you just use the red channel
[22:30] for masking displacement?
[22:32] So now displacement will be masked, whatever the red channel is,
[22:37] but not where the alpha is.
[22:39] So if I go in here and I paint in the red channel,
[22:43] you'll notice that displacement is being painted away in this particular place.
[22:49] Not exactly to the level that I would I would be expecting,
[22:53] for whatever reason, it's still allowing some of it to come through.
[22:58] But you can sort of like look in here and see if there's like a height offset
[23:02] that you can you can do, but you also have like the displacement mask power.
[23:06] So let me just try.
[23:09] Oh, there we go.
[23:10] I'm just kind of like creating a hard edge.
[23:13] Usually the this is why I'm using because right now puddles might be pushing
[23:19] displacement through, but this is why I'm using the alpha as an option
[23:23] because this allows me to have a better control alpha being not being part of the
[23:28] blends, while the other ones, the other the other players are using RGB as part
[23:34] of blends, while alpha is just simply a puddles in displacement out.
[23:39] Now, puddles can be moved to a different channel.
[23:42] So if you go over into water puddles here, right now we have them on the alpha.
[23:47] We could put them on to the red channel, for example.
[23:51] So now puddles will show up wherever we've painted red.
[23:55] And as you can see, it's over there like that.
[23:58] So whatever the red channel is present.
[24:00] Now you can view these.
[24:01] You can change over from color view mode to RGB.
[24:05] OK. And this means that if we delete, we start deleting the red channel here.
[24:11] Puddles will disappear.
[24:12] Displacement will come back up.
[24:13] So you know what I mean?
[24:14] So this is how easy that is.
[24:17] But as I said, all in all, there's a lot of discovery to be done around
[24:20] displacement mask displacement itself.
[24:24] But the system is more costly than parallel exclusion mapping.
[24:28] It is using real geometry.
[24:29] You can even bake this and have this mesh, this plane be displaced in this way.
[24:34] And then it becomes a physical mesh.
[24:36] And then it's like that all the time, right?
[24:39] With collisions and everything.
[24:41] It does hold up in play mode as well.
[24:44] But just bear in mind that this displacement currently does not have collision.
[24:48] Your feet will sink through them, through the fake geometry.
[24:53] But if you do bake this and then use, you know, make like a proper collision,
[24:57] you can actually use this to actually collide with this fake geometry that was then baked.
[25:04] So now what I want to show you is a bigger sort of environment that I've been sort of
[25:08] like experimenting with, in which we can see how displacement or parallel exclusion mapping
[25:14] can affect your environmental sort of system.
[25:18] It was part of a ongoing update for the World Forge into what we are going to call as the Omni Forge.


### Surface Forge - Landscape Integration [25:19]
**Transcript (timestamped):**
[25:26] Right now we have the Surface Forge implementation into the World Forge for,
[25:32] you know, its landscape feature or let's say, you know, landscape shader.
[25:37] So we're looking at, you know, six deep something FPS, you know, high quality
[25:45] layer, right?
[25:47] For multiple layers, we can see in here we have material ABCD, or you can call that layer ABCD,
[25:54] right? And currently it's not running any displacement or parallel exclusion mapping.
[25:59] Tessellation for the landscape is enabled. This is Unreal Engine 5.3.
[26:03] It's not the latest version, which has a higher performance. I'm just trying to show you this,
[26:07] you know, in a scenario in which you were, you know, we're going to have things stacking against
[26:12] it, so to speak. But when you're looking here, let's just add, let's just enable parallel
[26:16] exclusion mapping and start seeing some results. So I'm just going to go, you know, enable POM on
[26:22] the A channel. Never mind, I'm doing this in play mode. So the FPS will start tanking as it loads up
[26:29] the parameters. So we've enabled that for the A layer, which is this one here. Now we're doing
[26:35] it for the B. I'm actually going to move around a little bit just so we can have a look at the
[26:41] effect. So we have parallel exclusion mapping over here now. And we have parallel exclusion mapping
[26:47] over onto this cliff or whatever side here. Then we can enable it for C and we can enable it for D.
[26:56] Now I'm not going to sugarcoat this right now. We're running on a low amount of steps because
[27:03] we're trying to keep our performance high. This is going to be very important for your, you know,
[27:10] game development. But as you can see right now, let's let the, you know, the FPS stabilize.
[27:16] So it's currently sitting at around 16, 17 MS can go up to 18. Again, this is in high quality
[27:24] for this, but the steps aren't exactly sensational. You can see here, you know, if you look at the side
[27:29] for an angle, it's not that great. So this is where we look at the steps. It's, you know, minimum to
[27:34] two, we could put minimum to one or even to zero if you want. But I would say let's put minimum to
[27:40] four. Now let's put max to maybe like 16 or something like that. And even that is still
[27:46] not amazing, but it's still better. And as we let the FPS sort of like, you know, consolidate,
[27:51] we can still see that our MS has gone up by one now. And we can increase this. So let's just
[27:57] really jump up to 64. And then we'll do a minimum of 16. So now we're getting pretty much high grade.
[28:05] Okay, this is going to effectively increase our cost to something like 20 MS. And this is on a
[28:14] landscape shader that's currently not fully optimized with the entire surface forage flow.
[28:20] I think I'm going to be able to knock down another two or three MS. But now you have almost
[28:25] undistinguishable quality across the entire landscape for parallax occlusion mapping.
[28:32] But with that said, we can now switch over to a Nanite displacement instead. So I'm just going to
[28:38] cut the video here and move on to that just to show you sort of like the difference. This is how
[28:43] it looks with parallax occlusion mapping. Let me show you what it looks with Nanite displacement.
[28:47] As you can see in here, very comparable effect, Nanite displacement, again, in 23 MS when it's
[28:56] enabled. It doesn't look as deep as parallax occlusion mapping did. But that's not to say that
[29:03] you can change the parameters to make this height a lot higher. I just personally, I think I like
[29:09] parallax occlusion mapping more. Now, obviously Unreal Engine 5.3 Nanite displacement wasn't
[29:14] great in performance anyway. Going to 5.8, your performance will boost up by around 30 to 40%.
[29:22] No joke. So Nanite displacement does become a lot more efficient in future Unreal Engine versions
[29:28] and newer ones. But at the same time, parallax occlusion mapping also becomes more efficient
[29:33] in future versions of Unreal Engine as well. With that said, I think the difference in 5.8,
[29:40] we would be seeing a decrease in about three to four MS cost, maybe even more. But again,
[29:46] I do like the look of Nanite displacement as well, although I think parallax occlusion mapping has a
[29:51] bit more depth. You can also see in here that we have a range droplets being cast onto the floor.
[29:59] We also have water leaks onto the sides as well. So right now, we have a lot of systems at play
[30:05] that are currently working in the WorldForge using the SurfaceForge framework. We're also able to
[30:11] like create puddles based on rivers. Now, obviously, this is really make a lot of sense here. So I'm
[30:17] still working on some of these features with Waterflow or Waterpuddles. With that said, there
[30:23] are ways to increase your performance for things like Nanite displacement. So what I mean by this,
[30:30] if we look at the console command, we do have our Nanite tessellation or actually Nanite,
[30:37] I think it was Nanite dicing rate. Yeah, there we go. So I think by default, it's a dicing rate of one.
[30:43] But if you put this to something like believe of five, let's just see if we can spot the difference
[30:49] here. So that's with a one. Okay, that's that's how that looks like. And this is with a five.
[30:57] Now, I believe you can, you know, you can keep going. So maybe like even a 10 or let's just try a 50.
[31:06] So right now I've decreased, you see, it's also even producing errors with a very low dicing rate
[31:13] here. Let me just try also 25. No, 25 is not stable either. What does 0.5 do? You know, 0.5
[31:21] basically breaks it. So you can really go to a minimum value of one. And this in theory is how
[31:32] like I'm just kind of trying to show you here what the difference is as you sort of increase
[31:38] through the dice rates. And the idea would be that especially when you're dealing with a lot of
[31:42] meshes, if you're using dice rate of one, you're going to have the lowest performance. But if you
[31:47] go for a dice rate of like five, you should be getting better performance than with one. But on
[31:54] a landscape like this, it doesn't really seem to be doing that much. At the same time, I would say
[31:58] in future Unreal Engine versions, again, that dice rate does have actually quite a high impact. So


### Outro [32:07]
**Transcript (timestamped):**
[32:07] hopefully this tutorial has showed you what the Surface Forge can do in terms of displacement
[32:14] and parallax inclusion mapping. Stay tuned for this update to the World Forge that will soon
[32:19] becoming live on FAB. And also the new improvements that are going to be coming to Surface Forge
[32:25] and the release of what I call the OmniForge, which will be an accumulation of the Forge projects
[32:33] in a bundle that are all so all tied together. Now, don't fret, you are not going to lose out if
[32:40] you only are interested in the Surface Forge because any update, any sort of particular
[32:47] setting or option that the World Forge or Surface Forge will have, sorry, the OmniForge will have,
[32:54] also the Surface Forge or World Forge or any other of the Forge projects, they will also get parity
[32:59] on those options. So hope you guys enjoyed the video and thank you to my Patreons, thank you to
[33:05] all of my supporters on FAB and YouTube, and I'll see you guys in the next one. Thank you for watching.



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
