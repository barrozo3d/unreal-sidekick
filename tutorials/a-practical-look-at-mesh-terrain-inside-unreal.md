---
title: A Practical Look at Mesh Terrain | Inside Unreal
source: YouTube
url: https://www.youtube.com/watch?v=XlbWtoIk-Zc
author: Unreal Engine
ingested: 2026-08-06
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/a-practical-look-at-mesh-terrain-inside-unreal/
frame_count: 0
frame_status: pending-selection
---

# A Practical Look at Mesh Terrain | Inside Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=XlbWtoIk-Zc)
**Author:** Unreal Engine
**Duration:** 132m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py a-practical-look-at-mesh-terrain-inside-unreal <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Unc笛Sep니까D Department of
[0:02] Alpha une каждikad kairat D
[0:09] Makeup
[0:12] Dansand
[0:58] Listen.
[1:20] My fortune.
[1:26] What do we have, Captain?
[1:31] We have land, Mr. Mone.
[1:56] We have land.
[3:26] My God!
[4:26] Hello, hello everyone and welcome back to Inside Unreal, a show where we learn, explore and celebrate everything unreal.
[4:51] I am your host, Dan Hotnick, and today I am joined by Itien Carrier, who is here to talk to us about mesh terrain.
[4:58] This is a very exciting one for me specifically, who is someone who has been an environment artist, so some pretty cool tools here.
[5:08] So let's go ahead and get him introduced. Itien, how are you doing?
[5:12] Hello, I'm doing good and you?
[5:15] Very good, very good. Why don't you let the folks know a little bit about who you are and what we're going to be talking about today?
[5:20] Yes, so as you said, my name is Itien Carrier. I'm a senior technical artist at Epic Games.
[5:29] I've been with you guys for about a year. I've worked also for a while at Ubisoft, developing procedural pipeline for world generation and stuff like that.
[5:39] I'm very excited to have had the chance to work on mesh terrain, that new tech, which is very exciting to me.
[5:49] It's something along my years working on games that have been seeing the limitation of regular landscape and itemap system.
[6:02] It's nice to finally have something that is basically breaking these boundaries.
[6:09] It's a system that's been fairly stagnant for probably the last 20-ish years, if not longer.
[6:17] It's very limited, height map, vertical. We're going to talk about all that in this demonstration.
[6:24] It feels like a real evolution of what we've been used to for so long. I'm definitely excited to jump in and explore all this.
[6:35] Yes, actually, height maps have been around for over 30 years. It was first introduced in very old games, but in the 80s.
[6:47] It was time for a change, I think.
[6:51] Definitely. We have a lot to cover here. I don't want to dilly-dally too much, but I do want to say for folks tuning in live,
[6:58] if you do have any questions for Etienne here about mesh terrain, please leave them in the chat in brackets,
[7:05] followed by your question, and we will gather as many of those as we can throughout the show and toss those to Etienne towards the end of the show.
[7:15] If you have any questions that are not specifically within the purview of this topic, please head over to the EDC,
[7:21] our Epic Developer Community, where we have our forums, documentation, tutorials, and so much more.
[7:28] Plenty of resources over there for the broader ecosystem questions and things like that.
[7:34] Today we're going to be talking specifically about mesh terrain, and I can't wait to jump in.
[7:38] Any other preliminary stuff we want to tackle before we start getting into the nitty-gritty?
[7:44] I'm good. All good to start.
[7:47] Perfect. Perfect. Then once you're ready, we'll switch over to your screen share.
[7:52] All right. Let's do it.
[7:56] It's on.
[7:58] It is on.
[7:59] All right. First, I guess we figured a bit of history for those.
[8:06] I'm imagining most of you are really familiar with the regular landscape system, which is, or in other engines, it's like Ikemap Bay.
[8:16] Here I have a little very small Ikemap, which is 10 by 10 pixel, but just to illustrate the concept, the idea behind regular landscape is that all the data is stored into that 2D texture.
[8:32] The only thing it can do really is, these black and white pixels, the only thing they can do is basically raise or specify like an Ike value, so they can only raise the height of the terrain like this.
[8:49] It's an efficient way to store the height information, but it's really limited in terms of what we can do in terms of shaping up our terrain.
[9:04] We know in the real world, in nature, terrain is not constrained to be only pulled up from a flat ground.
[9:15] You can have overrangs and stuff like that.
[9:18] So really mesh terrain is that idea of now like removing that 2D format to store or terrain data.
[9:27] Now we're working directly with the mesh, so that means that it's almost like regular modeling.
[9:33] You're working on your vertices and your triangles and basically it's a mesh.
[9:40] Now we can still raise the terrain up, but now we can do stuff and move sideways like pull or geometry sideways and create, if we wanted to create floating islands, tunnels and underground caverns and stuff like that.
[10:01] As you see here, this one is in this example.
[10:06] This is basically a texture modifier, which is kind of just like an Ike map.
[10:12] It's using this Unreal logo as our Ike information, but instead of pulling it vertically from the ground, we're able to basically take that modifier and really place it anywhere,
[10:27] anywhere in any angle that we want on our terrain.
[10:32] So we have an old set in the mesh terrain mode, an old set of modifiers that we can use to basically shape up our terrain and basically change the triangles, shape it however we want.
[10:50] So I just wanted to cover that little part to illustrate really the difference between this new system and the old Ike map base landscape and terrain.
[11:05] Yeah, so you can use both meshes and, I mean, this might be bad terminology, but essentially a decal to also extrude.
[11:14] Yeah, I mean, now the Ike map asks that textures, to the textures, we can almost use as a decal now in a sense that we can apply it in any angle.
[11:29] And we can also use it to transfer.
[11:31] And we'll see examples, but we can use that in the texture information also to apply some material right into the way channels,
[11:42] just like the landscape would do the writing into landscape layers to apply like material and stuff like that.
[11:52] But yeah.
[11:55] So, yeah, so and now today, I guess the main, the main feast of what we're going to look at today is like, are we basically built this level here that we did for the Unreal Fest Key?
[12:11] So I'm just going to go and show because for those of you that sort of keynote, it goes fast, like goes by really fast, like showing how it's getting built.
[12:26] But of course, not going into detail of which modifier was used, which asset, how it's assembled together and stuff like that.
[12:36] So we're going to take a look at all of that today.
[12:40] So first thing I would want to, when you guys are working with Mr. Rain, a few things I would recommend doing.
[12:49] So first of all, what you can do is because you'll see you'll have if you create first like a go to Mr. Rain mode, you can create like your base Mr. Rain actor, which will create for you like different.
[13:05] Your machine, basically your mesh partition actor geometry.
[13:11] However, it's not showing some of the stuff under the hood that is not getting shown by default.
[13:17] And you can turn on your like on the outliner filter mesh partition, you can show basically your mesh partition base and your mesh partition build sections.
[13:27] So I'm just going to turn that on.
[13:30] And now under my mesh partition actor, you'll see that I now see my preview sections and then the sections here like this is basically my base.
[13:42] When you first create like a new mesh terrain actor, I'm just going to raise it up a little bit.
[13:51] The preset that you have here and then the yellow lines basically show you how many bases going to create.
[13:59] And the nice thing with Mr. Rain is that since you build everything with modifiers like that base, you're not that initial choice that you make, you're not stuck with it like later on.
[14:10] You can at any point like basically delete your whole mesh, the whole thing, the whole mesh partition actor.
[14:16] And if you keep your modifiers, then you can just reapply your modifiers to the different or bigger.
[14:22] If you need to expand your world, you figured, oh, we're going to build an open world is going to be two by two kilometer and then along production, you realize, oh, actually we need like an extra kilometer like on the north side.
[14:36] You can easily like just delete it create a new one that is bigger and just reply on your modifiers and basically you're not losing is going to be identically the same with that extra zone added.
[14:50] And then we have other tools as well to just expand won't get to detail of those right now, but it's I think it's a it's a nice aspect of Mr. Rain being able to fact that's non destructive and like really deep that the fact you can delete the whole thing.
[15:05] Just keep them at fire and just reapply it afterwards on the new terrain.
[15:11] So so this section again, like you're not stuck with the size of these base section.
[15:17] You can have something that decides automatically like the size of them and really the only impact that might have is you might have like a modifier.
[15:28] If you keep only one section that means that the whole thing needs to be updated when you're working in the.
[15:35] That's you're working on the air in the corner of the map and you have a small modifier that affect just that but because it's a big section, then the whole thing needs to be updated.
[15:48] Having more section means that the only to update if the ones that get affected by a specific modifier.
[15:55] But it's like, what's the right? What's the sweet spot here? It's really like a depending on your project try on errors.
[16:03] And then if you try something you realize, oh, it's updating or my sections are too small or too big, you can just change them afterwards.
[16:13] So that's no problem.
[16:15] So just wanted to point that out and it's useful to have them visible here.
[16:19] And then quick question.
[16:22] Quick question before we continue out there. So we have obviously the main mesh terrain here that was built on the example and then you just added a separate mesh terrain.
[16:29] In a practical sense, is it better to try to keep it to is like few mesh terrain assets for lack of a better term as possible or would it make sense for them to have multiple in a specific scene?
[16:43] I think it could make sense to have multiple depending on the context. Let's say your map, you're having like floating islands, those islands like are separate.
[16:54] Technically, it can, let's say you have five floating islands, like each of them can be separate like mesh partition actor.
[17:02] Over a few plan at some point to bridge them, connect them with a bridge like a terrain bridge or an arch.
[17:10] Then they need to be part of the same one, but or they can all be in the same one doesn't really matter.
[17:18] There's no right and wrong answer. I don't think it makes much of a difference in terms of like the final runtime.
[17:30] But we do have that flexibility basically. You can have more than one or you can have just one and you can change this along the way as well.
[17:40] So here actually I have one base mesh partition actor and I've just wanted to see like further away and have like more distance, which I'm going to hide now for the, just to see like the difference here.
[17:56] They're both overlapping and this one I created like was more lower resolution.
[18:02] The principle one was built so that it's about that one meat. Well, it was one meter per quad and then the Vista one I created to be more like a, I don't remember, but maybe like four or eight meters like a lower resolution since it's the distance in the distance.
[18:20] It doesn't matter that much. But another way that I could have tackled that is I would, I could just like basically create that very large Vista mesh terrain at low resolution and then my main part of my like or terrain.
[18:37] I could have to use also like a remesh modifier to just close the resolution of that center part where I know the gameplay is going to happen to like one meter resolution and then start building from there.
[18:49] So that's one thing we can do as well.
[18:55] Right. So next thing when working with Mr. In that is not on by default is showing like the mesh portion outliner. So we have an outliner that will show all the modifiers only affecting Mr. In.
[19:11] So if you go to tools and you type mesh partition.
[19:17] Outliner and we can go ahead and open that.
[19:21] So here we're going to have a list of all the modifiers that are affecting our terrain.
[19:28] And if we go back to the really beginning of before all the modifiers we have this this bar here with the dots that we can use to days a disabled basically the modifiers that are above.
[19:42] So I'm going to go to the first modifier here.
[19:47] So that just shows them the original terrain and the very first modifier that I have here is is a texture modifier.
[19:55] Then I'll go back here to select it and then maybe I'll also clear the PCG generation and I'll bring it back later.
[20:06] Once we have rebuilt the whole map.
[20:10] So I'm just going to clean up my PCG by home.
[20:16] Right. And so.
[20:19] Yeah, so this initial basically valley.
[20:24] Of course, with Mr. In there's many ways, many roads that lead to the same result. You can achieve things like in many different ways.
[20:34] Here we put this demo kind of pretty fast. So I started from like a generated like I map in a different PCC as a starting point.
[20:43] So I have this I map texture that is valley.
[20:47] That also has a set of so this is applied I can on my again my texture modifier that I placed here and I can just maybe scale it a little bit just for fun.
[20:59] So you guys see like that we actually can move that around rotate it and basically this going to apply your your height.
[21:10] So yeah, I'm just going to bring it back to what it was.
[21:18] I'm also going to hide these these lights that are for were for like the inside of the caverns that were creating like that level effect.
[21:26] I'm just going to turn that off and that light back up.
[21:31] All right.
[21:32] So yeah, back to this texture modifier.
[21:35] So it's using like a displacement here in the properties.
[21:41] I'm using that texture to apply the deformation.
[21:44] But as you see, there's also like materials that are getting applied.
[21:50] And this is achieved with a separate texture.
[21:54] So there's a weight channel sections.
[21:56] So basically what weight channels are is for those who are familiar with the landscape is just like landscape layer that you can then tie and link with the material setup to apply different texture set and stuff like that.
[22:12] But weight channels basically we it's it's it's just like a slow that rebute on your geometry.
[22:21] So it's it can be used for anything.
[22:25] And it's a float so you can use it like in your material, but you can use it as a mask.
[22:31] You can use it in the in the PCG graph to apply like a bio effect.
[22:38] So it's very versatile.
[22:40] But so here, yeah, we're using weight channels or using this different texture here that matches my my map in it, like the red, green and blue represent like different materials that gets applied to the the the measuring.
[22:58] So you can set this up.
[23:00] So basically you can target.
[23:03] You can add as many as you want.
[23:05] Like their first one here.
[23:07] I'm using that texture is going to target like the gravel material with channel.
[23:14] This one the material send and it's using that the channel texture number one.
[23:18] So the green channel and then the another one's using the blue channel texture number two to apply the grass.
[23:27] And then you can add additional one you don't have to reuse like the same texture.
[23:30] You can use an entirely different texture.
[23:32] So basically like the same texture modifier could apply like 99 different material if you if you wanted to or also apply like a mask that would be used by by PCG again.
[23:46] So I think that's an interesting feature of the texture modifier opens up a lot of possibilities.
[23:55] So yeah.
[24:00] So maybe next I can show like because speaking of these weight channels.
[24:05] As you see they're available here but where do these come from on our mesh terrain.
[24:11] Actually what's happening is that we have for each mesh terrain actor we also need to assign like a mesh partition definition asset.
[24:19] And if we go ahead and open this.
[24:24] That's where you assign basically your your material for your mesh partition geometry.
[24:29] And then that's also where you can define your channel.
[24:32] So here I have like a material rock gravel sand grass and then this one was to stop like a create a mask for their remesh modifier.
[24:45] Then there's other bunch of other properties that we can maybe go in details later.
[24:51] But for now that's where you can create your your weight channel.
[24:56] So there's that and then in the material how we pull out these channels that we're writing with the texture modifier.
[25:07] Again if I go back to my definition open the material and I'm just going to show you guys how we can load these weight channels into our material graph here.
[25:20] So it's very like kind of straightforward material.
[25:27] Like we have a part of the graph that's like the rock texture the gravel the sand and the grass and basically we're interpolating between these sets.
[25:38] But here we have basically loading that weight channel mask to do that interpolation that work between our sets.
[25:46] So that's all there is to it like loading a weight channel you use like the mesh partition resource feed that in the mesh partition channel sample.
[25:56] You point to the mesh partition definition that you're using for that specific mesh terrain.
[26:03] And then you just go and select the channel that you want to use and then we have this route node that's going to be used here and then basically blend our material.
[26:14] It's very easy nothing complex here it's quite almost the same as that the landscape workflow so you guys should be quite familiar with that it's not too different.
[26:25] So that's good.
[26:28] All right.
[26:29] So next part in building this terrain next is I started adding like a mountain shapes.
[26:37] So I'm going to go back to my outliner and start showing like the other modifiers that we have which is another.
[26:47] Extra modifier.
[26:49] This one is using a different type map I can show quickly also in where I generated these assets like this one just created in in its knee.
[27:01] Getting these these these shapes it was a way to create but that could come from any DCC basically.
[27:09] But yeah exported some of these.
[27:12] These shapes have another variation here.
[27:16] Yes.
[27:17] So yeah I'm just using that.
[27:19] And as you see like your modifier can be placed in any angle.
[27:25] So this one I wanted to pull a little bit like sideways to create like that that main mountain shape here.
[27:33] And as you see like there's like a strata effect that is happening on the on the side here but that's all part of the material.
[27:42] It's not like specific to the modifier itself.
[27:45] It's just like we define like our terrain material here that the strata texture would only apply like on when the normal is facing a certain way.
[27:57] But there was one thing that we needed to do however is that when applying because underneath before we apply this modifiers we had like a bunch of grass and gravel that was there.
[28:10] And we didn't want any of that on the mountain part here that we just wanted to be a rock.
[28:16] So one thing that we did similar to the other modifier we're using the weight channels to basically specify some value so we can like as you said like the other ones where we had that texture here that is applying like the grass pattern.
[28:32] But here we don't want to apply a specific pattern we just wanted to remove the weight channel value for the grass and the gravel in where that mountain is.
[28:45] So what we did is basically use like the use this option here that is apply item and max blend.
[28:53] So what it does is really it's only creating like a mask where the formation has happened.
[29:03] And then we're using like a black texture to set like kind of the value to zero and then the alpha blend it's set to the minimum value.
[29:12] So the minimum value between black and whatever it was is like zero.
[29:16] So that ended up removing that value where we placed that mountain peak.
[29:25] So yeah, and then these in the height displacement part of it the alpha mod that we're using is like the max value as well.
[29:37] Which is useful when we're also adding a bunch of these together.
[29:42] And let me show you just going to enable the other ones.
[29:46] So as we see here are some of them that are basically overlapping.
[29:54] But because we're using like the max blend mode it's just going to take the max displacement value from what's already there and the way it's going to be used.
[30:06] And then the one that this modifier is getting applied.
[30:09] The default actually is alpha blend.
[30:12] So if I switch that to alpha blend it's going to apply like it's it's creating it's deforming like the base valley shape that I add.
[30:21] So it's in that case it was more useful to use like the other blend mode which is max here which keeps and just basically does the the deformation and apply like that.
[30:35] Rocky shape where I'm pulling it out out of the valley without breaking the subtracting to it if I can see.
[30:48] So that's it for this one.
[30:51] And next part I'm doing a bit of I'm going to show the wireframe here of the.
[31:00] Because the initial terrain that we had was basically we started again from a rectangle so flat grid.
[31:08] So the vertex was like the resolution of our mesh was about like a one meter per quad.
[31:18] Now we're starting to deform and stretching out these triangles as we pull them out with like the various texture modifier.
[31:27] Over next what we want to do is start pulling out like these strata and make them a bit more treaty.
[31:35] But or my triangles as you see are it's not too bad I mean but it's they're not as uniform as they can be they're a bit stretched.
[31:43] So what we have next is this remesh modifier that I'm really enabling right now.
[31:51] And this is this yellow bomb that we see here.
[31:55] I just wanted to affect like this main area is central central part here.
[32:00] So it's currently reapplying that.
[32:03] Remesh operation.
[32:05] So as you see now like I got like uniform triangles again to work with and start adding more detail in that this area.
[32:13] So remesh modifier again it's something that's available here in the mesh terrain mode the remesh one and you can set the target at joint that you want to have.
[32:28] So 100 centimeters so most of my triangles now are roughly one one meter.
[32:34] So yeah.
[32:37] So yeah.
[32:40] Just going to add the wireframe once more and maybe jump to them.
[32:46] Yeah I've this.
[32:48] This was my concept art when we started doing like this this map like I want I needed to have a visual target.
[32:55] So what we want to do next is really from these strata start pulling a little bit the shapes and extrude in them.
[33:03] So that becomes like just create overangs and stuff like that.
[33:08] So again with other texture modifier and this one is using another.
[33:16] Another.
[33:18] Map which looks like this which doesn't show too much but I can show the original one which was generated again here.
[33:33] It's just something like that.
[33:35] It's very basic but I just wanted like to have like a strip.
[33:40] And with like a little bit of strata effect so I just generated that here exported as a map and now I can use as an asset.
[33:49] I have four different variation of these that I can use in various texture modifier to start shaping this up.
[33:58] So I'm just going to re-enable this one.
[34:01] So we can start seeing that effect.
[34:04] As you see it's now as bold using that I map all the my my my geometry creating that nice overang.
[34:14] I've placed my modifier in the the angle that kind of match the the stratification effect from from the material as well.
[34:22] And I got this one is set in maximum maximum mode again.
[34:27] But I have this we can use kind of the same effect but kind of to go again and just carve in also the same thing.
[34:37] So this other one here is actually set in minimum mode.
[34:41] So once it's updated you guys are going to see to actually start like pulling in the word instead which kind of cool.
[34:49] Just just going to re-enable some of the other ones on the side here same principle.
[34:58] This one was set to to carve as well so maybe I can pull it a bit further in just to emphasize.
[35:08] Now it's going to just carve that area.
[35:13] And yeah and then just very simple like modifier like this you start just placing them combining and you can achieve some pretty cool effects.
[35:26] I just have to echo a few things I'm seeing in chat right now which is just like this is so cool.
[35:32] So awesome.
[35:35] For those familiar with the limitations of traditional terrain this is like extremely liberating.
[35:42] This is really cool.
[35:45] Nice. Yeah.
[35:47] I find that as well.
[35:49] I mean I'm super stoked of like playing with this.
[35:52] I have the chance to get involved in the development as well.
[35:56] So it's definitely super cool.
[35:57] So next speaking of cool things we can do.
[36:03] So we've seen like a bunch of texture modifier like moving the geometry but the Booleans are also like a big part of the cool stuff we can do with that.
[36:13] So we go back to a concept here again like creating like caves and tunnels is something else we can do.
[36:22] So that's something we can add here as well.
[36:28] So what I have here I have a few Boolean modifier.
[36:33] I'm just going to enable this one first and maybe show which assets it's actually using.
[36:40] So Boolean modifier you can use either in subtract mode or union this one we want to subtract and it's using this mesh.
[36:50] Which is doesn't have to be super detailed or anything.
[36:58] It's just kind of replicating like that strata lucky effect and just using this as a Boolean here it allows me to basically punch that hole and create that tunnel.
[37:13] And then we have other ones.
[37:17] I have a smaller one on the side here that I can enable and then a larger one here that I added to basically connect the side of the the mountain to the the front and basically bridge the tunnels together.
[37:33] So I'm going to enable that as well.
[37:34] Boolean apparitions sometimes are a bit slower but works very well nevertheless.
[37:46] And one thing I can point out as well is actually these I generated here.
[37:53] So I made like a few variation of these.
[37:56] But the thing to know is that when you're doing the Boolean a person that the triangle and the resolution and basically the edge flow of your mesh is also going to get transferred to the mesh terrain geometry.
[38:15] So if we go here as you can see like these triangles actually really come from my my mesh.
[38:21] All it was triangulated.
[38:24] So that's something to keep in mind if you want to keep deforming that area inside the tunnel.
[38:34] If you want like if you don't need like a high density resolution you can have a mesh that is low resolution.
[38:40] But if you need more resolution you can just change your your Boolean mesh to have more resolution.
[38:46] So that's going to get transferred.
[38:48] So would the with the remesh modifier also help with that.
[38:54] Yeah that's another option as well.
[38:56] Right. Yeah you're absolutely right.
[38:58] If I wanted to if my mesh is low res I'm fine with that but some area I need more resolution I can add a remesh operator here and just start increasing the triangle resolution and that's in a specific area just like we did for that.
[39:15] That mountain center mountain part here.
[39:19] So yeah you can also apply weight channels directly with the Boolean operator.
[39:28] So as you see here it was maybe not fully necessary because it mainly placed inside that mountain that was already kind of removing the grass and the gravel and the sand.
[39:43] But just as just to be sure also added like functionality to that Boolean modifier here at the three different weight channels writing basically setting like the the gravel value the sand and the grass to zero.
[40:02] And I didn't show this before but like you have options to use like a constant value from your mesh you can also use the vertex color.
[40:13] So if my mesh add let's say on the interior here like on the top part or just on the left side or the right side you can have like red vertex color basically set it up or whatever you want but you can reuse that vertex color.
[40:29] To apply like a specific material so that can be quite useful almost like the same way as what we did on the on the base value here where we had the different patterns available from from that texture but just picture this instead being stored in the Boolean mesh vertex color instead of coming from a texture so that's that's quite convenient as well.
[40:55] All right so next a bit more Boolean asset I have a few more that added here this time but in in Union mode to add like a sorry moving too fast here in the viewport but yeah so wait for it.
[41:16] Those are using separate.
[41:21] That's my asset to just treat like an overhang and added these extra formation.
[41:29] So an example of using them in Boolean mode.
[41:33] Then.
[41:38] Once you have your final result you like regular landscape you might want to scatter stuff on your terrain.
[41:46] If we go back to our PCG graph can show you guys how it was.
[41:49] We can read basically the the mesh terrain and the different channels to start doing some scattering on our on our terrain.
[41:58] So.
[42:01] It's going to go to my PCG.
[42:05] And generate once more.
[42:20] I think for it to execute meanwhile I'll go ahead and open the PCG graph.
[42:27] It was not too long to to spawn.
[42:32] So as you see well it's like nothing very complex it's quite simple.
[42:40] Scattering here but as you see like I have some plants and some rocks.
[42:45] That are both like the bush or only spawning where I have like the green area and I mainly focus like the the rock scattering where I have like a gravel that was applied by my different modifiers.
[43:00] So and also before going to the PCG graph.
[43:07] I also managed to add like specific back a little bit of green here on the side where I pulled out the strata and I think it's kind of cool also so maybe I can.
[43:20] Just go and select one of the specific extra modifier.
[43:30] Trying to find the right one.
[43:31] I guess it was this one.
[43:34] With channel.
[43:39] This one bear with me at moment.
[43:43] No worries.
[43:46] Is modifier selection handled just through this?
[43:50] Well, like outliner or is there any way to do it physically in the.
[43:54] Yeah, there's it's still.
[43:56] Something we need to improve.
[43:58] We have if you alt right click somewhere on the terrain.
[44:03] It will show you like the list of modifiers that are actually affecting that that specific area you click on.
[44:11] So it's kind of a shortcut but.
[44:13] Like in a situation like this there's like many modifiers so it's not necessarily easy to know which one.
[44:20] It is but the.
[44:24] Yeah, actually I found the right one right away.
[44:27] But yeah, could you rename these to help with that sort of sort of you.
[44:31] Okay, yeah, definitely.
[44:33] I think like having good naming convention is is a good practice.
[44:38] Like as you see like by default far with to drag and drop like a new texture modifier is just going to be named.
[44:43] Extra modifier.
[44:46] I really took the time to name them like strat aside strat aside overhang strata front rematch modifier, the larger plate.
[44:57] Also, put in a number.
[44:59] strata front, the remesh modifier, the larger plate.
[45:05] I also put in a number.
[45:09] Well, we can do a little side note here
[45:11] because you can basically the order
[45:13] that your modifier is gonna get applied
[45:16] to your terrains, kind of like Photoshop layers.
[45:20] Each modifiers are like a Photoshop layer.
[45:25] So you need to order them properly.
[45:28] And the way we do this is on each modifier,
[45:31] you will find like a priority layer and a sub priority.
[45:35] You're actually, I haven't used like priority layers,
[45:38] but I've just been using the sub priority
[45:41] and I've named them like priority tree,
[45:43] it comes after the priority one.
[45:47] So it's a way for me to visually see
[45:52] in which order there they will get applied.
[45:56] But yeah, to manually name them here.
[45:59] But if you want to, like on a regular open world game project,
[46:04] like I would definitely use the priority layers
[46:08] that we have here, which you can define
[46:11] in your mesh partition definition,
[46:15] you can add the different,
[46:17] like you could have like the base terraforming
[46:19] and let's say like the P O I modifier
[46:23] and then you would make sure that
[46:25] with all your modifiers onto the right,
[46:28] the priority layer and organize them like that.
[46:32] And then afterward, these layers in the definition
[46:38] can be resorted if you, nothing is rock solid or final
[46:42] as you create things, you can always reorganize,
[46:45] insert a new layer in between if you need.
[46:48] And then there's always like the sub priority
[46:50] that's there to help you like sort out
[46:52] the ones that might be on the same layer.
[46:55] So-
[46:56] Yeah, narrowing down like all the, like what features I've,
[46:59] I think are the coolest with this
[47:01] because there's so many amazing features,
[47:02] it's really difficult.
[47:03] But I think for me, one of that standing out right now
[47:05] is just like the non-destructive nature of this.
[47:07] Like I love that.
[47:10] Yeah, that's right.
[47:12] All right, to get back to the, yeah,
[47:15] that effect that I wanted to add
[47:17] back a little bit of green here.
[47:19] So what I did is, so in my weight channel
[47:22] for this specific like strata and texture modifier
[47:25] that I added on the side,
[47:27] that is just pulling that geometry.
[47:30] Instead for the graph channel is that I had this
[47:33] for this specific texture set, like this specific item app,
[47:37] also at this specific mask texture that basically,
[47:44] I generated so that the red channel would present,
[47:47] represent like the one side of the mesh
[47:52] and then the green channel, the other side.
[47:55] And then if I show this in your Disney,
[47:56] I think it makes more sense.
[48:02] Yeah, each of them have,
[48:07] yeah, as you see like the red,
[48:09] it's just like basically like a orientation mask
[48:13] that gets baked down in the texture
[48:15] that represents the deformation.
[48:17] Just as a way basically to be able to tell
[48:21] everything that is facing upward
[48:24] according to that deformation,
[48:26] I would come back and reapply like the grass material
[48:31] on the top and like some of the cornices that this creates.
[48:36] And now this gets picked up by PCG.
[48:40] So, all right, so jumping to our graph
[48:45] for PCG graph, again, this is very simple.
[48:52] There's nothing like there's no sorcery
[48:54] or nothing very complex to argue.
[49:02] Using like the landscape and the surface sampler,
[49:07] you basically start from the mesh portion query node.
[49:11] And this, oh, it works.
[49:13] You can query different things
[49:14] from your mesh partition actor.
[49:16] You can query the base.
[49:18] So basically the base in that case would be just
[49:20] our flat rectangle or initial before any modifier.
[49:26] We have Intermediate, which allows you to specify
[49:29] like a specific priority layer to read from.
[49:33] So if you want to do some PCG operation before,
[49:39] let's say after applying like your base valley shape,
[49:43] but before any of the other mountain shape
[49:46] that would be applied by a modifier,
[49:49] you can get the state of the mesh terrain
[49:53] from this state from before adding other modifiers.
[49:59] So you can do that.
[50:01] And then here, basically it's just,
[50:03] I wanted to get like the final mesh.
[50:04] So it's very straightforward.
[50:06] You just use final.
[50:08] So that will give you a bunch of points.
[50:13] Maybe I can show some debug
[50:19] so that we see what's happening.
[50:26] Well, this will return a surface output.
[50:30] What we can do is two points.
[50:35] Where is it?
[50:39] The point.
[50:43] And debug.
[50:50] So once you query your mesh partition,
[50:54] yeah, by default we'll return a surface type,
[50:59] which is for scattering what you want,
[51:01] you then use just like the surface sampler.
[51:03] Or if you wanted to, because in PCG,
[51:07] you can now like also deform your terrain,
[51:09] you can basically load all the vertices of your terrain,
[51:12] then afterwards you can just transform them
[51:14] and re-inject them into your terrain.
[51:19] And the way to do that would be this.
[51:21] So probably my box, sorry, too small.
[51:25] Like I'm just gonna use absolute.
[51:28] And now I have a bunch of white box.
[51:33] So each of these cube now represent basically
[51:39] represent like a vertex of the mesh terrain.
[51:44] So you can now just, you have access to these points in PCG,
[51:48] you can move them around and then just re-inject them.
[51:51] So that's kind of cool.
[51:53] But yeah, for just basic scattering,
[51:57] that's needed here.
[51:59] So we got our surface and now we're just
[52:03] doing like regular surface sampler to get some points.
[52:07] But as I mentioned, we're scattering like bush
[52:12] where the grass is.
[52:13] And the way to do that is on our partition,
[52:16] mesh partition query,
[52:18] we can also fetch additional attributes on our mesh.
[52:22] So we can fetch any weight channels
[52:25] that exists on our mesh terrain.
[52:27] So we're getting to gravel the sand and the grass.
[52:31] And then that becomes available in our attributes.
[52:40] You should see, yeah, gravel, sand and grass material,
[52:46] float values available here.
[52:48] And then you can do whatever you want with that
[52:52] and use that as a mask and as a filter to sponsor massive.
[52:57] So yeah, I think that's mostly it
[53:00] what I wanted to show today.
[53:06] Starting from this, you should be able to do a lot of things.
[53:11] I haven't touched on some of the modifiers,
[53:14] but yeah, we can go ahead to some questions, I guess.
[53:19] If there's really specific question about seeing
[53:21] some of these other modifier, we can do that as well.
[53:24] Perfect, perfect.
[53:26] Yeah, I hope you're ready
[53:27] because we have quite a few questions.
[53:30] So we're definitely gonna jump into,
[53:34] there's some really good questions here,
[53:35] a lot of really, really positive feedback on this.
[53:38] And I'm echoing that sentiment.
[53:40] This is really dang cool.
[53:43] So yeah, we'll just kind of jump into these,
[53:45] throw kind of as many of them as you as I can
[53:48] in no particular order.
[53:50] One of the questions that we had here
[53:52] was weight channels can handle material masking
[53:54] as we showed there before.
[53:55] Can that be combined with manual vertex color painting
[53:58] to address problem areas or segments
[54:00] that need further refinement?
[54:04] Yeah, I guess.
[54:05] I mean, your weight channels are actually
[54:09] kind of like vertex painting in a sense.
[54:12] It's like it's vertex like attribute
[54:15] that is stored on the mesh.
[54:16] So if you wanted to put that in the context,
[54:21] if you wanted to paint your weight channels,
[54:26] you can use the brush modifier to do that.
[54:30] Maybe we can try this out in this other,
[54:34] just quickly because I haven't shown
[54:35] like the lagging a little bit here.
[54:39] Give it a second to refresh.
[54:42] All right.
[54:46] Just gonna disable this modifier.
[54:51] So yeah, if you wanted to do just like vertex painting
[54:58] kind of effect, just gonna set this like this.
[55:03] You use the brush modifier, the brush modifier,
[55:06] by the way, you can use it to sculpt
[55:10] but also just to paint some weight channels.
[55:12] So I'm just gonna increase the balance here,
[55:15] set it over my little island.
[55:18] And I'm gonna create some basically vertex attribute
[55:24] that I want to paint with this.
[55:25] So let's say we just go ahead and paint some gravel.
[55:30] So I'm gonna set this up here
[55:31] and then go to the paint maps.
[55:35] And now I'm in paint mode as you see.
[55:40] You'll see like a little seam at the edge
[55:43] of the where the bounds is.
[55:44] It's basically capturing part of that.
[55:48] The geometry that is within the modifier
[55:51] and just sitting it in a state that's gonna be instable
[55:55] while we're in the paint mode or the sculpt tool.
[55:59] So that's totally normal.
[56:00] Then you just go ahead and select your channel that you added.
[56:03] I added here upfront, but actually we can add it
[56:08] while the tool is open,
[56:09] I could come in and add this additional channel.
[56:12] So yeah, I can just come in and paint some gravel.
[56:16] If we wanted to just,
[56:17] if it was not tied to a material
[56:19] that now I'm seeing graveled
[56:20] because the material is already pulling
[56:22] that vertex attribute directly.
[56:28] If it was not like an attribute that was used
[56:30] for again, material, you can go to the shaded mode.
[56:34] If it's just like a mask,
[56:36] you want to use for a different purpose.
[56:38] You can just show it like in white and green here,
[56:41] red and just paint your attribute.
[56:43] So this would be your vertex painting basically
[56:46] because you're actually really,
[56:48] this is what it is painting on the vertex
[56:50] from your mesh terrain.
[56:54] Very cool.
[56:55] Yeah, you actually addressed one of the other questions
[56:57] we had tier two, which was,
[56:59] are there traditional terrain tools
[57:01] such as manually painting height information?
[57:02] And it sounds like yes.
[57:04] Yeah, and that's a modifier.
[57:08] So again, you can move that around
[57:10] and just get to move your,
[57:11] actually it's you just painted.
[57:16] I love the non-destructive workflow.
[57:17] I love that.
[57:18] I just can't get over it.
[57:19] It's so cool.
[57:29] And again, we can move this.
[57:33] So it's quite cool for a little POIs,
[57:36] like something you might want to do
[57:39] in part of your level.
[57:42] And you know that someone like art director
[57:46] is going to ask you to move around like five times
[57:49] during projection.
[57:50] Having something like this is very useful.
[57:52] Just for the fact that maybe sometimes,
[57:55] just like having to move it,
[57:56] sometimes it's just,
[57:57] okay, you build a POI in some area,
[58:00] you did a bunch of sculpting
[58:02] because like your initial state of your terrain
[58:06] before building your POI was something natural looking
[58:10] with erosion and things.
[58:12] And you went ahead and sculpted like a flat area
[58:15] for your POI and then,
[58:17] oh, that POI has to move somewhere else.
[58:18] Now you have to bring back what it was originally
[58:22] with like the natural looking state of what it was before.
[58:29] If you put stuff in your modifier like this,
[58:31] it's basically, oh, you don't have to redo,
[58:33] you just basically select your modifier, delete it
[58:36] and boom, it goes back to the original state.
[58:38] So it's a way of like setting your different sculpting effect
[58:44] in different brush modifier and whatnot.
[58:49] I love it.
[58:50] Yeah.
[58:51] Yeah, I love this just even for like
[58:53] considering things like play tests, right?
[58:54] Like you might build a POI,
[58:56] like you're saying that feels really good
[58:57] and it's really cool, but then you realize like,
[58:59] oh, it's actually,
[59:00] the position needs to be slightly to the left.
[59:02] And then doing that traditionally
[59:03] would be such a pain to change,
[59:05] but now that seems like it would be as simple
[59:08] as moving a couple of modifiers, which is awesome.
[59:11] Well, the thing is, also from my experience
[59:13] is like when working on regular landscape,
[59:15] you like technically if you're doing something
[59:18] that you know is going to be at a temporary
[59:20] or it's going to move around you,
[59:22] like the right thing to do would be,
[59:24] you don't want to mess with the base layer
[59:26] because once you sculpt it on your,
[59:29] let's say your landscape base,
[59:31] it's part of that base.
[59:33] So it's part of that layer.
[59:35] You can adjust like further later,
[59:38] like remove what you just painted.
[59:40] You need to kind of erase it and try to redo.
[59:44] So what you would do is create like an additional layer,
[59:46] but then you don't want your during production,
[59:49] you want your stack of layers to become like,
[59:53] like a big list of layers that you don't know,
[59:56] which like that deformation comes from which layer.
[59:59] So normally you want to keep things like these base layers
[60:06] kind of small so that it's easy to debug.
[60:09] But now with modifiers, it's easier to just,
[60:13] okay, this is his own actor.
[60:17] It's easy to add it and remove it later on
[60:21] or move it later on if it needs to.
[60:25] So yeah.
[60:27] Very, very cool.
[60:29] We're getting this question quite a lot.
[60:31] So I figure we'll just tackle it real quick here.
[60:35] Can any of this be done at runtime?
[60:38] Oh, the famous question.
[60:39] The famous question.
[60:40] No, we don't support runtime yet.
[60:46] Like this is still experimental.
[60:49] So it's not gonna be part of like the first,
[60:55] we need to get this out of experimental
[60:57] and making it like a solid feature.
[61:01] And then we'll be able to start looking probably at runtime,
[61:06] but yeah, it's not supported currently.
[61:10] Another question we had here is,
[61:11] does this work with World Partition?
[61:14] Yes, well, that's the whole point of,
[61:16] yeah, that's excellent question.
[61:17] And I should have mentioned this.
[61:18] So thank you to whoever asked this.
[61:22] The whole point of mesh terrain,
[61:26] as you see the base actor,
[61:30] is named mesh partition.
[61:32] And the mesh partition stands kind of for
[61:35] like the fact that it's specifically made
[61:38] for World Partition.
[61:41] So the thing is with mesh terrain,
[61:44] like we have the preview sections here.
[61:46] This is only, it's only like geometry.
[61:52] We have a different representation for runtime.
[61:56] So basically we have compiled sections
[61:59] that are gonna be split specifically to follow up
[62:02] like for to be streamed with World Partition.
[62:07] So, and the way you would set this up is,
[62:10] maybe we can talk a little bit about this,
[62:12] but in the mesh partition definition,
[62:15] we have this whole like build section
[62:18] that you define transformer pipelines
[62:22] and different platforms, different build variants.
[62:26] This is a transformer pipeline here
[62:28] only for the preview, so only its tour,
[62:30] the its tour part, but,
[62:32] and then if I open one of them,
[62:35] right now I'm in, yeah, this example,
[62:37] I'm reusing the same one,
[62:38] but actually let's take a look at this one here
[62:42] because it has more,
[62:44] mesh partition, just gonna open my definition.
[62:55] And this one has a more like a classic setup
[63:00] in terms of build.
[63:01] So we have like a high end and a low end build
[63:06] and then the common transformer, this one,
[63:11] basically contains the collision.
[63:13] So it's like in these transformer pipelines,
[63:16] like a little shopping cart and you set
[63:19] which component it's gonna contain.
[63:22] So this one is, yeah, just set up for the,
[63:28] which one have I selected?
[63:30] Yeah, this is a common one.
[63:32] This one contains the collision transformer.
[63:36] And then if I go ahead and open the high end transformer
[63:42] pipeline, then we add like the,
[63:45] the Stetsk mesh transformer,
[63:46] that's all it contains basically.
[63:49] So that's, if I was not to put any Stetsk mesh transformer,
[63:53] my runtime version of mesh terrain wouldn't add
[63:58] individual but would have like a collision.
[64:01] So it's very flexible, basically,
[64:02] you can configure it however you want.
[64:06] And then, so this is like the build variance
[64:10] and then you have your platform.
[64:11] So you can define how many build variance that you want.
[64:15] And then on my platform, so I have the low end,
[64:19] the low end is using both like the common build variance,
[64:22] which contain my collision and contains the low end
[64:25] build variance, which contains the Stetsk mesh.
[64:29] And then your Stetsk mesh for each build variant,
[64:31] like the high end one, you can add as many level of detail
[64:36] as you want, you can define if it's gonna use
[64:38] nonite or not.
[64:41] So yeah, and it's quite, you can really,
[64:45] and then you can set how many platforms as you want,
[64:48] like if you have a Nintendo Switch, Mobile,
[64:52] PS4, Xbox, PCIN, PC-LOWEN, you can really, yeah.
[64:59] That's quite powerful.
[65:01] Yeah, I'm glad you're talking about that.
[65:03] Oh, sorry, go ahead.
[65:05] Yeah, yeah, and then just remember the original question
[65:07] was about the world partition.
[65:12] So actually in your build variance here for a Stetsk,
[65:18] let's say the high end, you can specify that it's gonna be
[65:21] split section to match world partition runtime grid.
[65:25] So otherwise it's gonna be split,
[65:27] not matching the exact grid, but it's gonna be split
[65:30] to its own predefined values,
[65:34] by the max section complexity.
[65:38] So it's gonna figure out to the met's the how many triangles
[65:44] is gonna put an individual section.
[65:47] So if you want to have larger section
[65:51] than your actual runtime grid and stuff like that,
[65:55] then which grid is gonna get assigned to you as well?
[65:58] You can control from the transformer pipeline here
[66:04] I would add another transformer,
[66:07] I would select world partition actor properties
[66:11] and then I would be able to select, okay,
[66:13] which grid I want this to be assigned to.
[66:16] So let's say I want this one to be on the main grid.
[66:20] That's also where you set up the HLAD layer
[66:24] if it goes into a data layer as well.
[66:27] So that's done to a world partition,
[66:30] or this transformer.
[66:32] Yeah, and I'm actually glad you brought this up
[66:34] because we've actually gotten several questions here
[66:35] regarding this and that is,
[66:37] how does mesh terrain handle collisions?
[66:39] These extremely complex meshes with millions and millions
[66:44] of polygons, that's usually not how you wanna handle
[66:46] collision normally.
[66:48] What is mesh terrain's solution to that?
[66:51] How performance intensive is it?
[66:53] All that sort of fun stuff.
[66:55] Yeah, yeah.
[66:56] So as you saw, actually that's very nice
[67:00] because your collision actor is separated
[67:03] from your visual, so your collision can be,
[67:08] you can set it to be in a different grid
[67:11] than your visual one,
[67:13] so it can be stream at its own distance.
[67:16] You can have, like, since you're able to set
[67:20] many build variants,
[67:23] you can have one collision that is for mobile
[67:27] and one collision that is for ION with its own preset.
[67:31] So, and then, yeah, here in the transformer,
[67:34] you really set how much you want it to be reduced,
[67:38] like simplified.
[67:40] There's a bunch of parameters to basically control
[67:45] the resolution of your collision mesh.
[67:47] And you have very fine control here for platform
[67:51] and to get the exact resolution that you need.
[67:56] And if you want to reuse the same one
[67:59] for all your platforms, yeah, the width set up,
[68:01] it's like here what we did.
[68:04] We're just created a common one
[68:05] and then we're reusing the common
[68:07] on all our different platforms
[68:10] so that way we know our collision's gonna be the same
[68:12] on the whole platform if it's important.
[68:14] Like if you're, like, it's a Fortnite,
[68:16] like it all runs on the same server mobile
[68:20] and other platforms.
[68:23] So it's important that the collision is the same
[68:25] across these platforms.
[68:26] So that's an easy way to control this.
[68:28] But yeah, that's all it's set up.
[68:31] You just set it up here, control your resolution
[68:35] and then once it's generated,
[68:36] you can visualize it in the level.
[68:38] I don't have it generated here.
[68:40] That was gonna be my very next question.
[68:42] So you're really, you're on the ball here.
[68:44] You're getting all these questions
[68:45] before I can even, I can even preempt them.
[68:48] In the same kind of vein, another question we had here
[68:51] that I think is kind of interesting to tackle,
[68:52] which is somebody says,
[68:54] I'm really confused as to how UVs are generated.
[68:58] Well, yeah, UVs, they are done automatically.
[69:03] Right now we only have like one UV set on the mesh terrain
[69:09] or have plans to add more eventually.
[69:11] But right now the UVs they're mainly used to store the,
[69:17] because the white channels that we paint
[69:20] as we did here, painting gravel,
[69:23] it's basically stored on the vertex when we're indeed stirred.
[69:29] But in the end, in the final game, at runtime,
[69:32] I mean, these are not the save on,
[69:37] I guess it's get baked down to a texture
[69:39] and it's not kept as a vertex attribute,
[69:44] which we wouldn't want because as you saw
[69:46] with the different transformer option,
[69:50] like configuring like different LODs,
[69:52] if you were to have a very low res for like load
[69:56] in the distance,
[69:58] you, if your way channel were still like
[70:05] on the vertex attribute,
[70:07] you would basically lose all the details
[70:10] from what you have painted.
[70:12] So it's important to keep this as a texture.
[70:16] So we had just baked down to texture
[70:20] and this texture or the ones we're using,
[70:23] like the UV that we baked is basically for this texture.
[70:27] Maybe I can bake the compile section here.
[70:31] It's a small,
[70:37] so we can see the, some of the baked down texture
[70:41] on some of the compile section
[70:44] just to be straight.
[70:46] Hopefully it won't be too long.
[70:50] I can throw another question in the meantime.
[70:52] Yeah, yeah, yeah.
[70:54] I have one that's pretty big, so I'll hold off on that one
[70:58] because it'll probably take a little bit longer
[70:59] than going through all of this.
[71:03] One question we have here is, does mesh,
[71:06] sorry, excuse me, does mesh terrain require Nanite?
[71:10] No.
[71:12] Exceptional, yeah.
[71:14] But probably recommended when can be done, right?
[71:18] Well, it's a nice, yeah, I mean, yeah.
[71:23] But then I guess it really depends on your target platform.
[71:29] I mean, it's not mandatory.
[71:33] And then could you use?
[71:34] Because instead, as we saw, you can set your own LOD.
[71:38] If you're not using Nanite,
[71:40] you can configure like how many LODs your mesh
[71:43] is gonna generate for runtime.
[71:46] And instead of using Nanite,
[71:47] you just be using regular mesh LOD.
[71:51] And in theory, you could also use the remesh right to go
[71:53] to like a specific density of polygons
[71:57] either higher or lower, right?
[71:58] Yeah, as well, yeah.
[72:04] Another question we have here is,
[72:05] can resolution be controlled per mesh?
[72:07] Which I think we kind of did explain a little bit,
[72:10] but might be worth clarifying.
[72:14] Yes, per mesh portion actor, I guess, was the question or?
[72:21] Yeah, yeah, like I'm assuming they might have like some areas
[72:24] that might be just kind of like a rolling hill or whatever
[72:26] that doesn't necessarily need a extreme amount of density,
[72:29] but maybe there's like a hero point
[72:32] that does have a lot more going on
[72:34] than the one I want to prioritize density of polygons towards.
[72:38] Yeah, absolutely.
[72:39] Then I can go back to the example that we have here,
[72:45] remesh, I did add this specific remesh here to
[72:51] like add more uniform triangle density
[72:53] on my original mountain.
[72:59] So because initially like remember the triangles
[73:02] were a bit stretched because I did pull out this mountain.
[73:07] So yeah, in that case it was to kind of re-uniform,
[73:12] yep, more uniform triangle again,
[73:15] they were sensibly kind of the same resolution,
[73:17] but technically I could have dropped the resolution down
[73:21] or increase it like a much more.
[73:24] And maybe I can like add a new remesh modifier,
[73:30] let's see here to just drop the,
[73:33] let's set that to 99 and just drop the resolution
[73:38] like quite low res.
[73:40] So,
[74:00] since generating, all right, there it is.
[74:20] Taking a moment to update.
[74:24] There's a lot to process.
[74:26] I forgot some things.
[74:31] Looks fine.
[74:38] It's like it's not doing what I wanted to.
[74:43] The sick demo effect.
[74:44] Of course, the nature of live.
[74:48] Sure, what's happening?
[74:55] Hold on.
[74:58] Oh, yeah.
[75:01] When I was doing the demo,
[75:02] I was playing around in the artliner,
[75:06] a mesh portion of the demo.
[75:07] I was playing around in the artliner,
[75:09] I was playing around in the artliner,
[75:12] I was playing around in the artliner,
[75:15] a mesh portion artliner,
[75:17] basically disabling the top modifiers
[75:21] and just showing up to a certain point.
[75:23] So now it's still disabled at this modifier.
[75:27] So I had this new one set it at the top,
[75:30] but it's set to be disabled.
[75:34] The classic hierarchy.
[75:35] Re-nabled.
[75:37] Yeah.
[75:40] Maybe it's kind of the way I set up my demo.
[75:44] My layout as well, it's separated from,
[75:47] so I don't have it always visible,
[75:49] so it's easier to forget.
[75:52] But yeah, as you see now, it's working properly.
[75:55] Now the triangles are dropped to 10 meters, roughly each.
[76:01] So yeah, you can reduce the resolution in some area.
[76:04] Now it's just within the volume,
[76:06] but there's a cool thing you can do.
[76:07] If you combine this with a brush modifier,
[76:10] you can add a brush modifier,
[76:12] set it to write into a weight channel
[76:16] that you can then just paint.
[76:18] And then you can have the remesh operation to pick up on that.
[76:25] There's an option to use an existing weight channel
[76:30] as a mask.
[76:33] Where is it?
[76:35] Oh yeah, density weight channel here.
[76:38] So you can set it up to use a specific weight channel
[76:41] and then select the, well actually have this,
[76:45] like is it test the remesh mask?
[76:47] And so you could use that channel
[76:51] and then just paint it in a technique
[76:53] that should only remesh where we painted.
[76:55] So we do to control instead of just having
[77:01] like a big box of remesh, it's more finer control.
[77:08] Here's a quick question while this continues
[77:11] to do its thing, kind of going back a little bit
[77:13] to the collision side of it.
[77:15] It's my understanding that the collision
[77:19] is handled automatically by mesh terrain,
[77:21] but we did have a question here is,
[77:22] do meshes that you use in mesh terrain need collision
[77:25] or is that automatically converted in the mesh terrain process?
[77:30] If, can you repeat the question?
[77:34] If it's mandatory that it needs a collision or not?
[77:38] Yeah, like so the meshes that they bring in
[77:40] to use with mesh terrain, do they need collision
[77:42] or does mesh terrain handle collision?
[77:44] All you need is the model.
[77:47] No, yeah, all you need, like the ones that I use
[77:49] for instance for like the Boolean operation
[77:52] and stuff like that.
[77:54] Yeah.
[77:55] Like, yeah, no, doesn't need any collision,
[77:58] it's just using the mesh.
[78:02] Let me select one Boolean.
[78:11] Yeah, like this,
[78:15] there's no collision on them,
[78:18] so it's really just the geometry.
[78:24] All right, a big series of questions,
[78:28] kind of an umbrella of questions here that we have
[78:31] come down to performance.
[78:32] So first question, I'm gonna summarize a handful here
[78:36] that I saw, which is that,
[78:38] is there performance considerations at runtime
[78:41] or is this all a baked system
[78:44] and all of that processing time happens before
[78:49] you launch into a real-time scenario?
[78:52] Yeah, it's all get baked down,
[78:55] the process door doing in the other Unreal instance.
[78:59] Like hopefully it's gonna be built soon.
[79:01] I think it just finished now.
[79:03] But yeah, it's in the end at runtime,
[79:05] basically you just have a baked mesh.
[79:09] So there's no, like all the modifiers,
[79:10] they're not there anymore.
[79:14] You just have your mesh, a bunch of texture
[79:17] if you're using any way channel with it,
[79:20] all split up to support like wall partition
[79:24] and like your collision assets
[79:26] is gonna be a separate component as well.
[79:31] So yeah, at runtime it's all just baked down
[79:36] so it makes it very efficient.
[79:39] It's suitable for mobile.
[79:42] The fact also that compared to like regular landscape
[79:47] where you have it like a uniform density of triangles,
[79:53] since it's a baked mesh,
[79:54] you can really drop the flat area on my terrain.
[79:59] Like I don't need like one triangle per meter,
[80:04] one quat per meter that resolution can be reduced
[80:07] quite a lot, the fact that it's mesh and it's baked down
[80:12] and have like good advantage on that front.
[80:18] With the, oh sorry.
[80:21] Yeah, I have my compile section generated now.
[80:24] Yeah, let's do it.
[80:25] Again, just to show this at the beginning,
[80:28] but I have my mesh partition actor by default.
[80:32] The built mesh partition section were not shown.
[80:38] So again, if you go to filter mesh partition
[80:41] and when you bake your compile section,
[80:43] you actually want to see this,
[80:45] need to show like built mesh portion section.
[80:48] Now it's on here.
[80:49] So now I'm able to see compile section.
[80:52] So this is like the runtime version.
[80:56] Of course, like in the it's directly
[80:58] what is shown is the preview section,
[81:00] but I can show them by hitting the little pin here.
[81:03] It's gonna show like my low end and my,
[81:07] yeah, low end and high end version
[81:09] that are gonna be used for different platforms.
[81:13] And so you'd be able to debug the mesh from here.
[81:18] You would also see all the components
[81:22] that are contained in there.
[81:25] So you have your actual sex mesh component.
[81:28] The far field is basically for Lumen.
[81:31] You might want to add this if you're using Lumen.
[81:34] Again, this is defined in the transformer pipeline.
[81:41] This is the high end one.
[81:43] So this one here.
[81:45] So if we look at our different,
[81:48] high end, low end, well, actually you should have here.
[82:01] It's the far field transformer.
[82:03] So yeah, to have that component, you need to add it here.
[82:07] I guess it was using a different definition.
[82:10] Anyway, it's here.
[82:10] We see it here, like the far field mesh component.
[82:14] And yeah, initially I wanted to point out
[82:19] like the different textures.
[82:24] Not this.
[82:33] Not virtual texture.
[82:35] Not this.
[82:42] Not this.
[82:48] Well,
[82:54] I don't remember where it is.
[82:56] It's just ringing.
[82:58] Yeah, sorry about that.
[83:00] There was a place where we could see all the way channels
[83:05] textured available like on the component.
[83:12] And this, yeah, okay, sorry.
[83:14] It's on the main.
[83:16] It's not on this, that's the mesh component.
[83:19] It's directly on the compile section actor.
[83:23] So yeah, this is, well, it's not very representative,
[83:27] but stuff that we painted, I guess, this is this.
[83:32] So it creates.
[83:35] I mentioned it's creating that texture,
[83:38] but it's actually a texture to the array.
[83:40] So all your weight channels ends up inside
[83:43] the same texture to the array.
[83:46] And then you can visualize different slides normally.
[83:53] I don't know why it's locked currently,
[83:55] maybe because there's only one.
[83:56] But if you add more than one, you could see,
[83:59] technically you could have like 32 different slides
[84:02] representing different section.
[84:05] And then this 2D array will be there.
[84:08] You're gonna have one per section.
[84:10] This is a really small map.
[84:13] So you only generated one compile section.
[84:17] It could have changed the preset
[84:19] for like this section complexity.
[84:20] So it maybe would have split this into like four different
[84:24] compile section is set.
[84:25] So, but technically, yeah, you're gonna have one texture array
[84:31] per compile section.
[84:32] If for instance, let's say this was split in four
[84:36] in this left corner here, like the gravel is not there,
[84:41] the weight channel is not there.
[84:43] It's not gonna take any space in the,
[84:45] it's not gonna take a slice into that version
[84:50] of the 2D texture.
[84:53] So it's kind of really,
[84:55] and they're all gonna stream independently
[84:57] per compile section as well.
[85:00] So that makes it kind of quite efficient.
[85:04] Yeah.
[85:07] To wrap up the performance side of it,
[85:10] these are again, they seem like they're much more
[85:12] like in editor considerations or questions here,
[85:15] but we have one that says,
[85:17] on machines with fairly modern hardware,
[85:22] the engine tends to struggle
[85:24] with using mesh terrain in their experience.
[85:27] Do you have any advice or suggestions
[85:30] for number of layers, number of modifiers, things like that?
[85:34] Is it really just kind of throw whatever at it
[85:37] as long as the engine keeps up based off of your hardware?
[85:39] Is there, should they be trying to use like
[85:42] as few as possible?
[85:43] Or is it really just kind of,
[85:45] dependent on obviously hardware,
[85:47] but really just whatever you need to do
[85:49] in order to get the result you want?
[85:51] Sort of.
[85:52] Well, yeah.
[85:53] Of course, if you have like a 32 by 32 kilometer
[85:59] mesh terrain and you're loading it all at once
[86:03] in the world partition,
[86:05] of course it's gonna like struggle.
[86:09] Like mesh portion is made to be able to,
[86:12] technically you could treat like a whole planet.
[86:16] And, but of course you want these like loading it all at once.
[86:20] So like I recommend using like just like part of your,
[86:26] if it's very big and it's lagging
[86:28] and it's taking too much memory,
[86:30] just work on a smaller portion.
[86:34] Load just a small portion in the world partition
[86:36] to work on your terrain.
[86:39] That should help a lot.
[86:40] In terms of modifier, like the number of modifier
[86:45] technically that they all, unless you're, let's say,
[86:49] you have like a hundred modifier
[86:51] and you're working on the base one that,
[86:56] if you do modification on the base modifier
[86:58] and there's 99 modifier to update on top of it,
[87:03] of course it's gonna take more time
[87:04] to rebake the final result.
[87:06] That's why it's also useful when you're working
[87:09] on a specific step in the,
[87:13] if I go back to this one as I have more modifiers,
[87:16] if I'm working on my base,
[87:19] technically there's nothing preventing me from the valley
[87:24] texture modifier to just start moving it around.
[87:27] But if I move it around,
[87:29] of course there's all these other modifier
[87:30] that needs to be in the process as well.
[87:32] So while I'm iterating, it's more common sense to just,
[87:35] okay, I'm just gonna go back to the initial,
[87:39] like just to this stage,
[87:41] do my iteration, move things around.
[87:42] Once I'm happy with that,
[87:44] I just enable all the other modifiers
[87:46] that's gonna help a lot with performance.
[87:48] If you don't do that,
[87:50] and then working at the lower level here in the stack,
[87:54] of course that can slow things down
[87:56] if you have many modifiers.
[87:58] In some cases it will be quite fast as well.
[88:01] Like not all these modifiers overlap all the map here also.
[88:07] So if I'm working on the base here,
[88:13] but only in the corner,
[88:15] and I know that most of these modifiers
[88:18] don't really touch like the base section here,
[88:23] that won't have any impact that there's
[88:25] 100 other modifiers because they don't really affect
[88:28] that section.
[88:30] But yeah, this all things to keep in mind.
[88:33] But once they're generated,
[88:35] I mean the result gets cash,
[88:37] so it doesn't have to rebuild everything all the time.
[88:42] If it hasn't changed,
[88:43] it's just using that cash version.
[88:48] Yeah, hopefully that makes sense.
[88:50] Yeah, last question with that one actually is,
[88:54] is there a way or will there be a way
[88:56] to bake modifier layers?
[88:58] In my experience,
[88:59] high layer counts become very complicated
[89:02] to work with from large open world maps.
[89:06] It's something we did talk about,
[89:09] but we don't have at the moment.
[89:11] That could be useful at some point too.
[89:13] Yeah, technically we could take all of this
[89:17] and transfer it into like a brush modifier
[89:20] that would hold all the new positions
[89:24] for the vertex and just bake things down.
[89:29] It's just not a feature that we have right now.
[89:32] But definitely something possible at some point.
[89:36] Another question we have here is,
[89:37] many tools use landscape height data.
[89:40] How will 3D terrain affect these tools?
[89:44] Oh, well, you can still sample your data.
[89:58] I think you can just,
[90:04] we did this using virtual texture before.
[90:09] Basically we transferred the terrain height
[90:12] into virtual texture.
[90:14] Not the overhangs of course,
[90:15] we're working on the tech
[90:17] to have more like a 3D RVT.
[90:21] But we had some tests with a map
[90:24] that didn't add any overhang
[90:26] and we did bake the height into RVT.
[90:30] So then we were able to sample the terrain height
[90:35] and regularly to RVT.
[90:38] Otherwise, I guess you can,
[90:41] I can get back to, on that question,
[90:45] I can get some answers just to validate some stuff.
[90:50] I would make sure I don't see bullshit.
[90:53] Yeah, no worries.
[90:54] I think there was a way to do it.
[90:58] When we get that answer,
[91:00] we'll put it in a pinned comment on the YouTube VOD.
[91:03] So check back a little bit later.
[91:05] We'll hopefully get a good answer for that one.
[91:08] Another quick one here.
[91:09] And I think this is actually a really good example
[91:11] because we can kind of see it on the UI already.
[91:13] But one of the questions we have is,
[91:14] does mesh terrain also work
[91:16] with traditional landscaping schools?
[91:17] Example, landscape splines for roads, et cetera.
[91:23] Well, it works with the river, the lakes,
[91:28] the water stuff.
[91:31] And you basically just go and add mesh partition components.
[91:37] To the, actually I have an example that I can pull
[91:46] as quickly.
[92:03] It's a really work in progress little demo,
[92:07] but it has lakes and river.
[92:14] And it might look a little cheaty,
[92:16] but it's like the principle is there.
[92:19] So like regular water body,
[92:22] you basically just add mesh partition modifier,
[92:29] then that case like mesh partition lake modifier.
[92:32] And then that's the same regular water body component.
[92:37] And then it's gonna be compatible with mesh terrain.
[92:41] And then you can add it to like carving
[92:45] for the river bed or lake bed.
[92:48] And also apply a specific material,
[92:54] like the gravel and mud.
[92:56] And yeah, so this is supported.
[92:59] In terms of roads, the regular landscape spline roads
[93:04] is not only worse on landscape,
[93:09] but you can do your own road tool with a blueprint.
[93:14] So I have one here that I did,
[93:17] that's basically mix of PCG that generate the mesh,
[93:20] but then it's using like a spline modifier.
[93:24] You can, on your spline modifier,
[93:26] you can specify like the width, the falloff,
[93:32] if it needs to have a separate one in my blueprint here
[93:35] to apply the weight channels
[93:38] that I want to have under the road mesh.
[93:42] Doesn't have to generate a mesh as well.
[93:45] You could just have a spline modifier
[93:47] can be turned into a road tool quite easily actually.
[93:51] So yeah, we don't have this skated.
[93:55] So short answer, we don't have this skated roads,
[93:58] specific tool, the landscape one doesn't work on mesh terrain,
[94:02] but it's easy to make new road tool
[94:07] from the available modifier and blueprints and such.
[94:11] Yeah, I'm looking through,
[94:12] I have like multiple pages of questions here.
[94:15] I was trying to find one very specific,
[94:16] but it sounds like you kind of loosely touched on it.
[94:18] So I wanted to bring it up.
[94:20] I'm going to summarize it based off the best of my memory,
[94:24] but the question was, does mesh terrain work together with PCG
[94:31] in the sense of like, if PCG spawns a tree,
[94:35] it can adjust the terrain at the base of the tree
[94:38] to make sure that it fits appropriately.
[94:40] Like, is there any interconnectivity where like PCG
[94:43] can affect mesh terrain and vice versa?
[94:46] Yes, yes, we can do that.
[94:48] And that's one of the cool things.
[94:50] Like, I think landscape, PCG, you read access only,
[94:54] you can read the landscape,
[94:56] you cannot write back any effect or deformation.
[95:00] Now with mesh terrain, we can do stuff like that.
[95:04] So you guys want me to do a quick example or?
[95:09] Yes, we always have examples.
[95:12] Okay, I'm going to go back to my like smarter level.
[95:17] And I just found the question, by the way,
[95:21] was can PCG influence mesh partition,
[95:23] say there are trees that get placed from PCG,
[95:25] the mesh partition deforms accordingly?
[95:27] That was what I was looking for.
[95:38] All right, so.
[95:40] I'm just going to create a new PCG graph.
[95:55] And mesh terrain.
[96:01] My good to throw like a quick question at you
[96:05] while you're setting this all up.
[96:06] I know, I don't want to split your brain too much
[96:09] because I know I have trouble doing that.
[96:11] So, yeah, let's try to do that.
[96:15] Yeah, this one feels like it would be a pretty simple one here.
[96:18] It says, does mesh terrain support running a multiplayer game
[96:20] set up at this time?
[96:21] And I'm assuming the answer is yes, right?
[96:23] Because this is all like, before runtime stuff, right?
[96:26] So really just using mesh terrain to create a mesh
[96:29] and then mesh is working in multiplayer.
[96:31] Yeah.
[96:32] All right, so we'll start with the mesh partition query.
[96:36] And then we can do a surface.
[96:39] Some pair of.
[96:40] All right, so now my, as you see, my query is happening
[96:44] in the game.
[96:45] I'm going to run a little bit of a demo.
[96:49] So, yeah, we have a query.
[96:51] So, yeah, we have a query.
[96:53] So, yeah, we have a query.
[96:55] And then we can do a surface.
[96:57] Some pair.
[96:58] All right, so now my, as you see, my query is happening
[97:10] like under the ocean.
[97:13] That's because my default is set to base.
[97:17] Now I want to either get the final, but I didn't show it
[97:21] before.
[97:22] So maybe we set it to intermediate.
[97:24] And intermediate layer basically allows you to only
[97:27] choose like a priority layer.
[97:29] Intermediate allows you to pick a priority layer and also
[97:33] a sub priority.
[97:35] So let's say we do this and my modifier are set here.
[97:41] I have only a few ones.
[97:44] So this is my list of modifier that I have added.
[97:47] Sorry, not modifier, but priority layer.
[97:50] So I know like the top wall.
[97:53] Maybe I can get this one micro.
[97:56] I don't have any other ones.
[97:58] So let's add just want to get right after this specific
[98:02] modifier, which is using terrain, macro, skull, or whatnot.
[98:08] So here I can be used the same thing.
[98:11] So terrain, micro.
[98:14] And then you can specify whether you want it to be inclusive,
[98:19] include the deformation from this layer or not.
[98:24] In that case, I want yes, but if you build a system where you
[98:31] want to spawn something, the thing is you don't want to be
[98:40] looking for the word.
[98:42] Like each time you generate, you don't want to get back the
[98:44] result that you have already generated.
[98:46] You will probably don't set this.
[98:48] Actually, I'm going to do something different.
[98:50] Let's say I'm using the PY layer.
[98:54] So I leave it to nothing inclusive.
[98:57] And then what we'll do later on is that we're going to use mesh
[99:02] partition, what's the query?
[99:04] Mesh partition, right.
[99:07] So we're going to spawn stuff.
[99:10] And then from these points, we're going to do a bit of terrain
[99:14] deformation.
[99:16] And we want to write back these deformation into also like a
[99:20] priority layer.
[99:22] But we're going to use like the same name.
[99:25] But since this one is nothing inclusive, every time it's going
[99:28] to read back, it's going to read up to this point without
[99:31] including the deformation from the PY layer.
[99:35] But we're going to write back into it.
[99:37] So that way, we're just always reading before it does it.
[99:41] So there's no recursive.
[99:43] That's the word I was looking for.
[99:45] It doesn't do recursive like this occasion that it's going to
[99:50] pull up and then regenerate and then read the terrain and pull
[99:54] it up every time and stuff like that.
[99:57] If that makes sense.
[99:58] So one way we can set this up.
[100:03] What I like to do is add like a graph parameter and use like the
[100:10] name type and this rename to priority layer.
[100:23] So now I can use that and it did here and then my priority
[100:28] layer is going to be.
[100:31] Instur is doing something.
[100:36] Right.
[100:39] I'm going to set it to PY.
[100:42] I'm going to save right just in case.
[100:46] And then in my right, my partition right, I'm going to use the same.
[100:55] Oops.
[100:56] Yeah, the same type.
[100:57] Well, there's some naming that we need to fix, but type here is
[101:01] the same thing as layer name.
[101:04] All right.
[101:09] And what I want to do is convert my surface to points.
[101:19] And we also want the thing is when we write back the first, the
[101:23] point number has to remain remain the same if we want to query
[101:28] the terrain and write back the result.
[101:30] We cannot change the number of points.
[101:32] Otherwise, it doesn't make much sense.
[101:35] So, but you also need to know what was the original point position,
[101:41] the vertex position from the terrain and the updated position.
[101:45] And the right node here is going to ask you to provide an attribute
[101:51] that represents the position before any like modification.
[101:57] So by default, this is source position.
[102:00] So what we can do is a copy, a copy attributes.
[102:07] So before doing any modification, we're just going to store or position
[102:15] into oops, this copied source position, copy, paste.
[102:28] So now I have my position.
[102:30] I also have my source position that should be the same as my original position.
[102:36] And now I can start doing modification so I can transform points.
[102:52] Then I can raise that by meter.
[103:01] But yeah, I guess if I'm spawning some points, maybe I just want to raise
[103:11] the terrain around my points or if it was trees, maybe we can change the,
[103:18] use it little PCG tree instead as debug.
[103:26] Yes, with the distance node, we can compute distance between,
[103:35] no, actually I want the distance from this to these points.
[103:44] Hmm.
[103:51] Have you played a lot with PCG then?
[103:55] Yeah, a bit, a bit.
[103:56] I'm still a little green on it, but yes, I have been.
[104:02] I've done this before.
[104:03] That was like the distance node, but basically I would just want to take
[104:08] my points here and then compute distance from all of my vertex point
[104:20] and then just generate a ramp so that I can just, but I'm sure like people
[104:27] listening get the point otherwise that you can just scatter your assets
[104:34] and then compute like the distance from your measuring points to these trees
[104:41] and then just use that as a mask to transform your point and just,
[104:45] let's say you raise little bumps around your trees or any other deformation
[104:49] you might want to do.
[104:51] But yeah, as you see, like, technically you can just, once you have your points
[104:57] here and you've copied like the source position, then you can do any operation
[105:02] that you want on your measuring point and write back the result.
[105:07] I mean, we can already see it.
[105:09] Yeah, we can already see it affecting the terrain here just as you made.
[105:12] Yeah, just raise it.
[105:14] Yeah, on the flight like this, sorry.
[105:17] No, no, I don't want to take too much time to take five minutes.
[105:21] Otherwise it was the name again.
[105:23] But yeah.
[105:25] Yeah, no worries.
[105:26] I know we're getting close to the hour, so we might have to lighten around a few of these,
[105:31] but we do.
[105:32] We do have quite a few questions left here still.
[105:34] So one of the questions that we had here is the image you can use as a decal,
[105:40] is it straight black and white or only or can you use textures with RGBA to give you different pictures
[105:48] in the RGB and A that you can switch between?
[105:51] So basically a packed decal.
[105:54] Yeah.
[105:56] Yes, I think you can.
[105:58] Let's select one of our extra modifier here.
[106:04] Yeah, you can use RGBA as you see right now is just like a black and white,
[106:10] but there's like texture channel option here.
[106:14] So if it was RGB, I could select which channel I want to use from the texture I'm using here.
[106:24] So yes, totally we can use, we can pack different deformation in one texture,
[106:30] use them in different modifier and just use a channel that we want.
[106:33] So technically one texture now becomes you can have three different variations and just change the channel to switch variation
[106:41] for that like displacement texture.
[106:45] So that can be a convenient way to have more options within the same modifier.
[106:52] Perfect.
[106:54] Another question we have here that I think is interesting is when would you prefer to use
[106:58] mass terrain instead of terrain exported as a height map, let's say from Gaia.
[107:03] And I mean my inclination is why not both, right?
[107:07] Yeah, nothing prevents you from like that's kind of what I did here was not Gaia,
[107:13] but my base like valley, like whatever's more convenient for whatever project you're working in
[107:20] and the time constraint, if it's faster to do some parts in the DCC and port as height map,
[107:30] and the fact that all of this can be like then combined and modified afterwards makes it very convenient.
[107:38] And like again, like that base valley texture that I have.
[107:47] This one, since it's using on my modifier here, I can still basically modify it in my external DCC,
[107:57] re-import it here and it's going to update automatically because it's going to refresh the one that's getting applied.
[108:05] So you can update all of these at any time and it's going to update on your terrain as well.
[108:13] So you can basically sculpt the base of your terrain and just do some brush in external DCC and keep updating them.
[108:23] Like all the ways, the possibilities you could arrange your pipeline and the way you structure your terrain.
[108:32] If some part you want to sculpt here and the parts you want to do in DCC, you can combine that or whatever you want.
[108:41] I mean, it's a result of possibilities.
[108:46] But yet nothing, I would encourage people to be using all the cool tools available to achieve great results.
[108:55] Another question we had here is, is it a good idea to build non-terrain structure such as buildings into mesh terrain?
[109:06] Are there reasons to avoid that?
[109:09] No, definitely something that was also...
[109:15] It's called mesh terrain but really it's a mesh, like a world partition mesh technology.
[109:24] So anything big that you would want to work on collaboratively doesn't have to be a terrain.
[109:30] I mean, in our mesh terrain presentation at the Unreal Fairest, we showed if you want to build a big spaceship or a building,
[109:41] nothing prevents you from doing that.
[109:45] Of course, keep in mind that currently you don't have much control on the UVs.
[109:52] So if you just plan to apply like a triplanar textures and material, that's fine.
[110:02] But if you really need to control the UVs, that's for now, since we don't have UV-based modifiers yet.
[110:10] I wouldn't go there, but if it's not needed, yeah.
[110:16] Short answer, nothing ties its distinctly to terrain. It can be any mesh.
[110:22] So yeah.
[110:24] I feel like this one's going to be just yes and yes, but we might as well tackle it real quick.
[110:28] The question is, can meshes from Gaia be acted on with Boolean?
[110:32] And can you use PCG Grammar on it?
[110:36] Meshes from Gaia? I mean texture from Gaia?
[110:42] They probably meant textures.
[110:45] Yeah, yeah, I mean, let's say like this valley texture was coming from Gaia, like there's, as you saw, like I applied,
[110:53] like you can apply Boolean at any point.
[110:58] You can insert like a modifier in the stack anywhere you need.
[111:01] So anything can act on anything.
[111:04] You just need to organize your modifier and nothing.
[111:09] There's no limitation.
[111:12] There's no like order of type of modifiers.
[111:15] Like you can add a noise modifier on top of a spline modifier and you can re-add a texture modifier on top.
[111:21] And it can all be sorted in any order that you want and you can do.
[111:27] So yeah, there's no limit on that side.
[111:30] Hopefully that answers the question.
[111:33] Speaking of modifiers, is there a limit or maximum number of modifiers that you can use?
[111:40] That I know of.
[111:43] Is it many until your computer explodes and then you found the limit?
[111:47] I'd say one trillion.
[111:49] That's a question for the engineers.
[111:52] There's probably like a limit somewhere.
[111:55] Like there's probably a tree limit that no one's ever been able to reach.
[111:58] Yeah, it wouldn't be a practical limit for, I would assume almost everybody.
[112:06] One of the questions we had is do you need a brush modifier to paint attributes?
[112:12] Yes.
[112:15] Yes.
[112:16] Simple enough.
[112:17] This one's an interesting question is it says,
[112:19] am I correct that the textures and materials can now do more with the landscape because of the mesh terrain in PCG to create better visuals,
[112:28] emissive, glows, glass, etc?
[112:31] Um...
[112:36] I'm not sure.
[112:39] I guess it's kind of the same it was, but it was for landscape.
[112:46] I mean, you can, it's kind of the same thing in the sense that you can control which material you apply where,
[112:53] like I mean right now you can only have like one material,
[112:57] but within that material you can create any effect that you want which you can control with,
[113:02] with the text about the white channels that you paint,
[113:08] or you apply procedurally or apply with a modifier.
[113:12] So that's, I think it's kind of similar to what landscape is already capable of, but...
[113:22] Maybe people will find ways to do cool things that were not possible before.
[113:30] We're always surprised by what the community comes up with and...
[113:37] Yeah, it's a good question, but I would say no, but I'll be happy to be surprised.
[113:45] That's a, it feels like one of those that you could just try, right?
[113:49] Test it, see what you can get away with.
[113:53] Considering that this works with world partition,
[113:58] I think it's worth kind of touching on this as well.
[114:01] The question is, can this be used for huge open worlds and is there a size limit?
[114:07] Yeah, well that's definitely totally the point of measuring was to be able to tackle large open world landscape.
[114:14] Currently has like limits, technical limits that prevents it from really doing convenience.
[114:22] But world partition is for that and mesh,
[114:27] terrain mesh partition is made for world partition.
[114:30] So that's the right tool to create large world, definitely, yes.
[114:35] The question here is, is it easy or possible to get physical materials working on the channel weight layers?
[114:45] Yes, I didn't show it, but basically in the definition,
[114:55] that's where you would define your physical material and then you can tie it to an existing.
[115:03] It's a rock channel, or you can have dedicated channels that are only for physical material as well.
[115:13] You can reuse them or have dedicated ones, but yeah, that's where you would set this up.
[115:18] It's in the definition here.
[115:23] Easy answer, that's.
[115:25] Love it.
[115:28] Another question we've actually seen a few different variants of this one, so I'll kind of summarize it, but the basic general idea is like how does this work with nav mesh?
[115:37] Is there any concerns, limitations, things like that?
[115:40] No, I mean, it's just like regular.
[115:46] We didn't see no, I mean, it's just there's no, it's not different from any other mesh you would put in the level.
[115:57] You could have modeled all this from an external DCC 3ds Max or Maya, bring this in as a 3D mesh and your nav mesh would be able to like generate
[116:14] the same thing for for mesh partition.
[116:17] There's nothing specific to it.
[116:20] Considering that this works as a layer system where all of these are computed and then an output mesh is, that's the final result.
[116:29] We have a couple of questions here.
[116:32] Basically around that idea, like, can you bake all of this down to one just mesh and have that in the engine?
[116:40] And can you bake all this down to one mesh and then export it out of Unreal into another DCC for maybe, you know, whatever needs they might have for their project?
[116:50] Yeah, we don't have options to bake it down to export it afterward.
[116:57] It does get baked down for like the like we did on that little map before like the generating that the compile section is actually getting it baked down.
[117:08] If we load this one again.
[117:15] So this is the version baked down like that's that's mesh is now like the final version, including all the modifiers, but then the modifiers are not needed anymore.
[117:24] There's we just don't have a way to export that that's mesh.
[117:29] Do we mean?
[117:39] I'm sure it could be done in a bit of code to like the mesh is there somewhere.
[117:44] So there's probably a way to extract it and save it as a fbx.
[117:50] I mean, yeah, if I look at the because it doesn't show you like this that's mesh in the content browser, but it's there on the dude somewhere.
[117:58] So there would probably be a way to maybe some, I don't know.
[118:08] Yeah, and yeah, to my knowledge, there's not a way to do it.
[118:11] But that could be developed easily by anyone, I'm sure.
[118:17] Extract it.
[118:19] Maybe at some point we'll definitely set if it's a request that comes up quite often, like adding functionality in like the mesh terrain mode to like export mesh terrain mesh or something could probably be possible at some point.
[118:41] Another question. Yeah, that I think is pretty interesting is for folks who've been working on previous versions of the engine or maybe they're on this current version of the engine and they built out a world and want to convert that to mesh terrain.
[118:56] The question is, can I just throw a bunch of static meshes together scale and arrange them and then convert them to a mesh terrain after the fact.
[119:06] No, but starting from landscape. That's something we did a couple of times just for tests before you we had the level that was done on landscape so I would go to land like the landscape mode.
[119:20] There's a place where you can export basically your item at the final item out the landscape layer to item up that will to external files, then you can just reimport these files here and reapply them as a texture modifier.
[119:38] So you can easily convert I can that way and landscape into mesh terrain, but if you've assembled like a bunch of mesh and then convinced converting well.
[119:53] It's not totally true because you can put a static mesh in the level and then convert it to have some assets.
[120:03] All right, let's get my floating island example here.
[120:20] I can drag in this the static mesh in the level.
[120:28] Once it's loaded.
[120:29] So I was about to say no, but yes, actually, because I'm not sure if there's you have several mesh.
[120:42] I have to these two different mesh and I've organized in different ways.
[120:50] Now, yeah, only supports one one, but maybe maybe if you combine them in the geometry strip, I could put this all this in a blueprint or something.
[121:04] And then you have a geometry strip merge them into one mesh.
[121:11] Then if you have one mesh, you can then convert it into mesh partition.
[121:15] So you have the convert process.
[121:24] And then boom, now I have this is now a mesh partition actor.
[121:29] I can brush modifier on it.
[121:40] And then.
[122:00] And now start scoping this.
[122:19] So yeah, well, if you it's a single mesh right now, it's crazy, but if you have several mesh, I'm sure there's a way.
[122:26] Maybe something we can add support like the convert option would support like multiple mesh selection.
[122:36] It's probably that complicated.
[122:43] Very cool.
[122:44] I know we're just about to just hit the hour.
[122:47] Do you have time for a handful more questions?
[122:49] The two hours, right?
[122:50] Yes, yes, we just hit the hour.
[122:52] The final hour.
[122:54] Final hour into the final hour.
[122:57] Speedrun just a couple more and then we'll wrap up.
[123:00] Yeah, sure.
[123:02] Perfect.
[123:03] One of the questions we have here went back to where you were showing the water.
[123:12] Splines.
[123:13] Yes, thank you.
[123:14] Now my brain forgot a word.
[123:16] The question here is, does Mesh Terrain work with the new water simulation system, shallow water, river actor?
[123:25] Don't know.
[123:27] Okay.
[123:28] I'm not sure.
[123:29] Another example.
[123:30] Give it a try.
[123:31] See if it works.
[123:34] I'm not too familiar with it.
[123:36] So I, yeah, I wouldn't be comfortable doing it live.
[123:44] No worries.
[123:46] No worries.
[123:47] But we can definitely get the answer and look into it and get back to you guys on this.
[123:53] I'm assuming it's like a different water system than the water type that we have here.
[124:00] Like maybe mentioned simulation.
[124:02] Yeah.
[124:03] So, so yeah, I'm not sure.
[124:06] Okay.
[124:08] We can, we kind of covered this a little bit, but maybe just one final time on this one was, is how does Mesh Terrain affect your time in play and editor?
[124:14] Is it baked every time or is it heavily cached?
[124:17] Yeah.
[124:20] Each time you it pie, it's going to bake the compile section.
[124:24] Usually the first time it's longer, but it's, I mean, if you've done, if you've done modification to it, that is.
[124:35] But you can also set things up so that you're like right now, like I've set up here where you can have a more straightforward version that just makes like the visual mesh and the collision and you don't have like many different build variants just passed in Insta.
[125:02] But yeah, like short answer, if you press the need story that's going to compile the big compile sections, depending on how many variants you have can take longer or shorter, but it's automatic.
[125:17] I mean, otherwise you can do it manually from here, but so it will affect and I think it would be too bad.
[125:26] Someone iterating and sculpting changing a little bit the terrain and then go back and pie to test it out and then going back in Insta to adjust a little bit more slightly and go back doing that back and forth every time could be a bit slow, but it's, yeah.
[125:46] That would only happen based off of a modification, right? Like if you build your own terrain and you don't change anything, next time you go to play an editor, it wouldn't.
[125:54] Yeah, yeah, yeah. If it's already baked and there was no modification, then it's, there's no build that needs to happen or anything.
[126:03] All right, got one more question from from chat here and then I'll throw one final one after you after this one, which is, does master and expose stable collision surface for runtime PCG sampling via World Ray hit.
[126:16] And can it still read baked Gaia masks for per surface data.
[126:23] PCG World Ray it would work. Yes.
[126:27] The Gaia thing. I don't know. I mean, like the Gaia mask.
[126:33] I guess that person means he's transferring Gaia mask onto landscape and is it usually able to to sample the value.
[126:45] Mastering we should be able to do it.
[126:50] But there's like what I know is that we're definitely working like I mentioned RVT before, but we're able to sample the RVT so we can get data from there.
[126:59] Right now, there's working progress on the material cache system that is like more 3d RVT.
[127:05] So we should be able to sample the material cache and basically get any like the material cache would be able to hold like the data from like the painted gravel or any other
[127:15] tearing mask that are used to be able to be able to sample that from any other asset that we would put on the terrain, for instance, but that's stuff that is still working progress.
[127:25] Perfect.
[127:29] Final question for you.
[127:31] Yeah.
[127:33] What would be a good idea if you had that kind of a good idea if you had that kind of a good idea.
[127:40] Perfect.
[127:42] Final question for you.
[127:44] What would be any advice you would give to folks who are jumping into using mesh terrain for the first time.
[127:53] I have fun and explore all the possibilities I mean, and I know a lot of people like they're used to just like a brush workflow like just sculpting manually with a brush.
[128:06] I think it's nice to start integrating additional different type of modifiers and your workflow.
[128:14] I mean, just like for POI, just using like the spline modifier, you have your, actually, let me load again the other level that I have because it's kind of cool to be able to use like a level instance where
[128:36] you can attach like modifiers to them and everything will be at the same time.
[128:42] So, for instance, this, it's a level instance, but I've attached like a spline modifier to my level instance.
[128:51] So I can still, it's at this, but it's very cool to just then, oh, I can just wrap the whole thing, move it around.
[129:01] And then like my, my deformation, like that flattens the terrain around, I come to my POI, doesn't have to be perfectly flat.
[129:10] I mean, you can still add like a different type of modifiers in there, but exploring this type of workflow of using many different modifiers in different contexts and spline modifiers can be quite, quite useful to create many different type of effects.
[129:29] And extra modifier as you see in the other, the other setup here, just combine a bunch of things together and create really cool stuff.
[129:42] The main, that's the main one and mesh modifier as well. I didn't touch on it too much today, but instead of using a texture, just projecting into a 3D mesh, so it's, it's, it can be quite nice as well.
[129:56] And so yeah, that's my advice. Like go ahead, explore different combination of modifiers to achieve your result. Don't, don't stick on you with like the irregular sculpt.
[130:07] I think there's great potential in combining all of these together to shape up your, your terrain.
[130:16] Absolutely. Well, at the end, thank you so much for coming on to talk to us about mesh terrain. I am still blown away by it.
[130:28] It's such a, it's such a cool tool again as somebody who's so used to the traditional, you know, terrain pipeline and limitations of it to have this kind of versatility and ability is just so, again, like I said earlier, liberating, like this just feels like you can just go in and
[130:49] Essentially the mega lights version for lighting artists is we have for terrain artists now where we can just kind of go in and do the stuff that we want now and we don't have to worry too much about the limitations we used to have, which is really cool.
[131:00] Yeah. And big shout out to the, the whole mesh terrain team that worked on this. The, like the core design behind this is very nice. So yeah, my atsauce to all the, the team.
[131:18] Very cool. Thank you. Absolutely. Absolutely. And if you, when you see and talk to them next, let them know that we love this and we want more. Sounds good. Perfect.
[131:30] Well, that is going to wrap up today's Inside Unreal. A huge thank you again to you, Etienne, for joining us today and a huge thank you to everybody for watching as well.
[131:39] This show wouldn't be what it is without you, your time and your questions. And if any of you came through the stream halfway through and wanted to rewatch it, no worries.
[131:49] We post all of our streams in video format that can be viewed on both our Twitch and YouTube channel at Unreal Engine. You could also keep up with the latest news.
[131:58] Shout out to other cool information on all of our socials at Unreal Engine. And if you haven't already, please join us at the Epic Developer Community where we have our documentation tutorials from the
[132:08] community and Epic staff alike forums and much more. But again, thank you so much to you. Thank you so much to everyone for watching and we will catch you all next week.
[132:21] Bye, everybody.



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
