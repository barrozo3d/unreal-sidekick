---
title: Lessons Learned from Building a Very Large Open World Game in UE5 | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=AalP65lrtpo
author: Unreal Engine
ingested: 2026-07-22
ue_version: "UE 5.6"
tags: [pipeline, automation, editor-scripting, pcg, animation, niagara, level-streaming, blueprint, cpp, intermediate, ue5-6]
extraction_status: complete
frames_dir: tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Lessons Learned from Building a Very Large Open World Game in UE5 | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=AalP65lrtpo)
**Author:** Unreal Engine
**Duration:** 37m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] and so on.
[0:02] Hi. Welcome. This is Lessons Learned from Building a Very Large Open World Game in UE5. It's about
[0:08] our work on some lot of k-2. I probably should have picked a snappier title, but I'm an engineer,
[0:13] so you get where you go. We're going to focus on a few key areas, mostly focused on our
[0:19] experience, what we learn, what we might do differently. I'm not here to tell you what
[0:23] to do because we might not even know what we're doing. So we're going to focus on tools, then
[0:29] move on to plugins, managing scales, that's dealing with the size of a game, a bit about
[0:34] how we set up our actors and our data management there, and then a small section on animation
[0:41] as well. So who am I? I'm Sam Dark. I'm a programmer at Unknown Worlds. There's a few
[0:48] of the things I've worked on. There's a bunch of other stuff that you'll never see because
[0:52] cancelled games are fun. I've done a bit of gameplay, a bit of core tech, and a bit of
[0:57] animation more recently. What is some lot of k-2? Not sure this slide is particularly
[1:05] relevant, but I thought it would be a few months ago. Open World Survival Crafting Game. It's
[1:10] Underwater, which is quite unique for games. It's early access, so everything I'm talking
[1:15] about here is just the start, not even halfway through, to be honest. There's loads more
[1:21] development to come, which means all of the stuff I'm talking about is just a baseline,
[1:25] and we're making sure we have headroom to finish the rest of the game. Single player,
[1:30] franchise is historically single player, but we've now added full player co-op, which has its
[1:34] own kind of challenges. And we currently use 5.6, that's what we shipped on, but we're currently
[1:42] upgrading to 5.7, and I assume we will look at 5.8 at some point in the near future. And it's
[1:48] cross-platform, so it's out on PC and Xbox at the moment, and we may or may not do other platforms
[1:52] in the future. So we're going to start with tools. So the first thing we kind of came across while
[2:01] thinking about how we're going to architect the game is placing everything. We have a large map
[2:06] that's currently worked out about three kilometres by one and a half kilometres. That's only a
[2:11] small percentage of the map, and the Simnautica games are known for dense intricate spaces. They've
[2:17] got caves, you've got lots of little story bits hidden underneath overhangs in rocks, deep in
[2:24] caves. So we have currently 100,000 actors. That's going to increase by a great deal at some point
[2:31] over the course of Early Access. And importantly, we have a handcrafted map, so none of this is
[2:37] procedurally generated at runtime. We make use of some procedural tools, which I'll go over, but
[2:43] it's majority handcrafted map. We have low-end designers hand-placing things, because a lot of
[2:48] the drawer of Simnautica is the story and the world and the level and how kind of hand curated
[2:54] that is. And quite uniquely, we have lots of verticality, so we don't just have one kind of
[3:00] flat terrain. We have terrain, we have caves, we have overhangs, and obviously you can swim up
[3:05] and down, which is relatively unique outside of, say, flying base games. So we had a few options
[3:13] for this. We could brute force everything, just hand-place all the 100,000 actors, but we don't
[3:19] have like a 400-person team of level designers to do that. We could use PCG, but when we started
[3:26] development, it wasn't quite ready yet. We have quite a weird system with multiple landscapes, and
[3:32] there was some issues there. And a lot of the PCG tools that when we started development, to do a
[3:39] volume scattering and placement and things, all assumed that there's kind of a direct line from
[3:44] the sky down to the terrain, which isn't the case if you're deep in a cave underwater. We could
[3:51] just use level instances and blueprints, you know, make a bunch of modular level instances and
[3:55] blueprints, place them around everywhere, use a lot of, get a lot of reuse there. We can make use
[4:01] of some plugins, or we could build dozens of bespoke tools and do it that way. So what we did is we
[4:11] made a bunch of bespoke tools for things like dropping meshes, scattering meshes, dressing
[4:17] props, blind holes for cliffs. We had tools for making the roots of our tree, and we had quite a
[4:23] monstrous tool for placing resources, which I'm going to go over later. Most of these we made
[4:28] using edit widget blueprints. We found them really useful. Some scriptable tools. And we're now kind
[4:36] of in future, we're looking towards PCG now that it kind of better supports what we're doing, and
[4:41] it's moved along a lot in development. Yeah, I can't get that. So we had this problem with
[4:52] this morning resources where we wanted to try doing procedural resources at runtime. So every time
[4:57] you played the game, you'd have a different kind of configuration of resources so that when you played
[5:03] the game the next time they wouldn't all be in the same spot. We wanted to be able to adjust the
[5:07] balance at any time. And we wanted quite a complex rule based system so that resources spawned in a
[5:14] place that makes sense to players. And this is still kind of the case in game. You know, once you
[5:19] found the resource a couple of times, you can find it in a similar place again, following certain
[5:23] rules. And we wanted to be able to spawn this on all sorts of different terrain, landscapes, meshes,
[5:32] under overhangs, not just kind of projected down onto the train from the top. So again, we could use
[5:39] PCG, but it wasn't ready. We could make complex bespoke tools, or we could do simple bespoke tools so
[5:47] we could have something like blueprints level instances where you turn off the blueprints and
[5:52] turn them on to adjust the balance, but they're kind of all in the same place all the time. So we went
[5:56] for the crazy complex bespoke tool, called it world population. It was a bespoke system, basically
[6:06] worked on flood filling the entire map with Raycast. So we'd start from a known location of
[6:11] playable space, you know, just drop an actor in, that's somewhere that the player can be. And then we
[6:16] would flood fill through the entire world doing Raycast to get a full map of where things, where
[6:21] all the playable space in the world is and where then mark points on the surfaces where they could
[6:26] spawn. So you can see that on the right bit there, all little cubes of spawn points where stuff could
[6:30] spawn. We had all the rules and data assets. And then it looked a bit like this, I might need to walk
[6:38] up here and start the video. So that's it flood filling through the entire map. Each one of those
[6:45] green lines is Raycasts. And then red lines, I think, is it placing spawn points behind that. So you
[6:53] can see this is relatively slow just on that small area. And we've got a very large map. But I thought
[6:59] it looked pretty cool. So we had some issues with that. It was slow. It scaled nonlinearly with
[7:09] volume. So you're already having issues with volume rather than areas that make stuff scale slowly. And
[7:14] then it was nonlinear. So the bigger area we had without breaking it up, the slower it got. It made
[7:21] us resistant to changes because we had this big complex tool that we've made ourselves. So every
[7:24] time we wanted to update or change anything, we had to change the tool. It was manual. So you had to
[7:30] manually run this every time you changed any terrain and the level and meshes. If you changed any of
[7:36] the rules, you had to rerun it. And it's unfair to expect every content creator to know about all
[7:42] this system and to manually run it, especially when it's slow. And it could take, in this case, it was
[7:48] potentially up to a couple of hours for large regions. And it was kind of a black box. So because
[7:55] it was all runtime procedural, you couldn't see the result of your changes until you actually hit
[7:59] play and saw it in the game. And you also couldn't see it in the editor. So you couldn't see if it was
[8:04] affecting the visuals of the area. So we designed this beautiful area with all these carefully placed
[8:10] plants and props and foliage and everything else. And then I would spawn the resources on top and it
[8:15] would look terrible. And the important one is players didn't really get much from this. If you
[8:22] play the game twice and the titanium is like three feet to the left, you're actually not going to
[8:27] notice that or care. And it certainly isn't going to make up for all the increased dev time and all
[8:32] of that. So we made world population too. We dropped the runtime requirements. This meant that we
[8:39] could make everything into level. We could see it in the editor preview it. We made editor tooling. All
[8:47] of our resource balance stuff was very deep in data assets, which is not very friendly to anyone. So
[8:53] we made a tooling slate, chucked it in the editor, and then you could edit all the rules there and run
[9:00] all the stuff. We could upgrade to some more complex rules. And then we voxelize the entire map with
[9:07] this process. So what this meant was that instead of running a flood fill of raycasts through the
[9:15] entire map, we voxelize the map, stuck some information in the voxels for what surfaces were in
[9:23] those voxels. It was at one meter resolution as well. And then we only run the rules for actually
[9:28] generating a spawn point for resources on the voxels that meet our rules. And then we stuck it on
[9:35] the build machine overnight so people aren't waiting hours after doing their work. And it looks a bit
[9:43] like this. Again, just a cool debug visualization. I had to slow this down. This completed in, I
[9:48] think, about 15, 20 seconds with this version. But this is it going through the map, marking out the
[9:55] voxels, kind of figuring out what is playable space on it first. Then it marks out all the voxels. And
[10:02] then eventually it will apply the rules on those voxels. So you can see this blue debug thing going
[10:07] along and generating all the voxels and all the surfaces. And then this is some debug information
[10:13] about the rules. So you can see you can fly around the map. You can view this voxelized version of
[10:18] the map. And then you can see the spawn points. Best stuff could spawn. And then we could filter it
[10:23] by all the different rules and preview stuff relatively quickly. Still slow, though. It
[10:31] started off at 15, 20 seconds. Then we added more and more and more map. And then it became 20
[10:35] minutes, 30 minutes. We weren't using all the functionality. And it was introducing bugs when we
[10:45] ran on the build machine overnight. And that's the worst thing to have is when you wake up the next
[10:49] day, you start work, and bugs have been introduced, and no one's even been working on it. And it was a
[10:54] ton of setup. It took hours for people to go into the map and manually set up all these volumes and
[11:00] mark which part of the map was playable space to spawn stuff, which meant we ended up just placing
[11:05] resources manually in the map instead of using this tool we spent months working on. So why don't we
[11:13] just place the resources manually if that's what we're doing anyway? We could use PCG. It's kind of
[11:19] ready at this point. So we don't need a system at all. So you take months to work, put it in trash.
[11:27] But that's okay. Just think about how much time we're saving on maintenance not having to maintain
[11:33] this tool. Forget about all the time we already spent working on it. So what do we learn from this
[11:39] process? You've got to consider maintenance. There was so much maintenance keeping a tool like this
[11:44] going. Every time we wanted to do something different, we had to change the tool. We had to find the
[11:49] time to dedicate to changing the tool. We probably could have slowed down a bit. There was a lot of
[11:56] points there where we could slow down and reconsidered maybe this isn't the right thing to do, maybe
[12:01] there's another approach we can do. Maybe we'll revisit the requirements and ask do we actually need
[12:06] to place these resources procedurally? Or can we just go and delete half the titanium if we want to
[12:13] half the amount of titanium in the map? My personal takeaway from this is prepare engine tools.
[12:21] Epic has a huge team working on great tools and for at least us and most of you, you probably have
[12:28] a much smaller team working on tools than they do. So why don't we in future just make use of the
[12:33] engine tools? And if they don't quite fit our needs, we will save time if we just kind of work with
[12:40] them and extend them or improve them if we need to. PCG is great. I wish we could use it from
[12:48] the start. We couldn't, but now we can. So we're going to start using PCG. We've got some people
[12:53] investigating that currently. And Wasting Work is okay. We learned a bunch of stuff from this.
[12:59] We have a system that we shipped with. We shipped the game with that system. It works great. No one
[13:04] really complained about the resources other than no one can find silver, but that's an up story.
[13:10] Now we're going to talk a bit about plugins. So first issue we came across where we started
[13:17] looking at plugins with seams. We have a bunch of meshes with hard seams. I think every game
[13:25] ever has had this issue. And as you can see on the right, we have kind of a high color contrast
[13:30] art style. So we've got these orange corals. We've got this kind of sand color. We've got bright
[13:36] creatures. And that just makes seams way more visible. You can see the image on the right
[13:40] looks kind of terrible, to be honest. We have a bunch of stuff that helps. So we've got underwater,
[13:46] we've got fog, we've got blur. That kind of helps hide some of it, but it's not perfect.
[13:51] And when I asked one of our environment artists what we would have done without plugins,
[13:56] they just said you can't win the seam battle. So we had a few options with seams.
[14:03] Could you use RVT stuff? Has limitations, set up requirements, memory requirements,
[14:09] performance implications. Could you use decals and skirt meshes? You can see a gift on the right
[14:15] there of some decal stuff going on. But again, this is a bunch of work for the artists, a bunch of
[14:22] placement manual setup. And it kind of only covers some of the cases. And we could use props and
[14:29] foliage to hide stuff, but there's going to be a case where you manage to miss a rock intersecting
[14:34] with the sand. You don't cover it up with some anemone grass or something, and then it's completely
[14:38] visible. And seams really bring out, kind of ruin the immersion for players, more than you would
[14:45] expect from such like a what seems like a minor visual issue. And we did some experiments with
[14:50] mesh distance fields and similar. But again, it wasn't really perfect. And there was still kind
[14:56] of manual setup and stuff we needed to do. So one of our artists asked on the forums, said, hey,
[15:06] anyone help with this mesh seam issue? We found Tor on the forums. He got very interested in our
[15:14] problem, started coming up with ideas. And he made a post process shader for us. We iterated on it
[15:24] over development with him, kind of providing feedback back and forth. Being a post process,
[15:29] cheap on performance. So usually you tend to have a trade off with these sorts of plugins and tools
[15:35] where maybe it looks perfect, but it costs a lot of performance or you turn down the performance,
[15:41] it gets worse and worse looking, but this kind of helped with both. And it just worked. We just
[15:47] chucked in the game, everything worked. We didn't need to change any of our assets. We didn't need
[15:51] to change the way we were addressing levels. We didn't need to start making custom meshes for
[15:58] every single seam between every object in the game. And we couldn't have done that if we wanted to.
[16:02] Our team is not big enough. This is what it looked like. On the left is without it. And on the right
[16:08] is with mesh blend. So yeah, the plugin is mesh blend. You can get it on Fab. I think quite a
[16:15] lot of the games you'll see here at Unreal Fest are using this now. There's not really much to
[16:22] take away from the seam stuff other than mesh blend worked really well, so we're going to keep using
[16:27] it. So the second issue we had where we were looking towards plugins was prefabs. So we wanted
[16:36] a prefab like workflow. Our previous games were in a different engine, but that was more standard.
[16:42] And we wanted nested actors and to continue that way of working.
[16:48] We looked at level instances. They didn't really match the workflow we wanted.
[16:55] We could have transitioned more to the level instance workflow, but we decided we wanted to
[16:59] stick towards prefabs. So we found this prefabricator plugin for UE4. MIT license, free, give it a go.
[17:09] We updated it to UE5, fixed a bunch of crashes, added a bunch of improvements to it.
[17:16] It's now available on GitHub. If you want to check it out, there's no promises of
[17:20] support or anything like that, but the code is there if you want to try it in your own projects.
[17:26] But now we're considering going back to the level instance workflow. Again, it's a bit like the
[17:32] world population tool where we're having to do some maintenance when we do engine upgrades
[17:38] and we're finding that we're not really using the plugin as much as we want to. And then we get
[17:45] new people coming in asking why we're using the plugin. And after a certain point, we found that
[17:50] we weren't really able to justify why we were doing this rather than the normal UE workflow.
[17:57] So what do we learn? Plugins can be hidden miss. But there's no real wasted work if we're using
[18:03] plugins. So if we decided not to use mesh blend for some reason, we wouldn't have really wasted
[18:09] any work. And if we decide to drop the prefabricator plugin, we haven't really wasted too much time
[18:14] there. We didn't go and make a large system on our own. We used something we spent a little bit
[18:18] of time fixing it up. And if we don't use it, that's fine. Plugins aren't just for small teams.
[18:26] I mean, we're not a huge AAA studio, but it's completely fine to use plugins. Someone else
[18:32] has done a lot of work on one very small specific problem usually. And that's a very small specific
[18:38] problem you don't need to put six months of work into if you find a plugin that works for that.
[18:44] Next, we're going to talk about managing scale a little bit. So we have 100,000 actors in the
[18:49] map right now. That could be half a million by the time we launch 1.0. That is a lot of actors in
[18:57] the world. What about the performance? They had no idea what was going to happen with performance
[19:03] when we started placing all this stuff. And we were just kind of seeing what would happen as we
[19:08] started increasing the amount of actors we had. And this isn't just runtime performance. This is
[19:12] also the editor. How's the map going to load when there's 100,000 actors in it? How do we manage
[19:17] all that? How do we organize it? How do we deal with the outliner if it's got 100,000 actors in
[19:22] it? How do we know where things are? How do we move stuff around? What happens if we need to edit
[19:28] all of them? Say we decide really stupidly to raise or lower the entire map by like six meters to
[19:35] make the whole map more shallow. We did that. We're not smart. So we used World Partition and
[19:44] One File per Actor from day one. Genuinely cannot imagine how we would have made the game without
[19:50] these. So it's great that Epic is on all the work there for us. We had a few editor performance
[19:57] issues. These are relatively easy to fix. So we found something that was slow. We traced it with
[20:02] insights because that just works in the editor as well as at runtime. You find what's slow. We had
[20:06] a few issues like we had some problems where once we started getting around 50,000, 100,000 actors,
[20:13] deleting stuff in the map was taking a long time. So we traced it. Traced that back to some reference
[20:18] checks to see if what you're deleting is referenced anywhere and optimised that code a little bit
[20:22] and that problem's gone. And yeah, we did move the whole map. It's kind of a stupid idea, but we
[20:31] did it anyway. And it was relatively easy for the monumental task of moving like 100,000 actors.
[20:38] So we made use of tools, editor widgets, scripts and things like that to do scary things like
[20:45] moving the whole map around. Obviously, I personally wouldn't have advised anyone in our team
[20:50] try and move the whole map by selecting it all in the outliner and dragging it around.
[20:56] We made use of the World Partition Builder commandlets a couple of times. We found them
[21:00] really useful for when you're trying to do things on, say, the whole map, but you don't need to do
[21:05] the whole map at the same time. So much like World Partition does, it lets you load parts of the map,
[21:10] do what you need to do on that part of the map and then shut it down and load it from part of
[21:15] the map. So that's how we did all the world population stuff on the build machine. We had a
[21:18] World Partition Builder command that would open an area of the map around like a world
[21:23] population region, generate all the resources, save them all to a data asset, unload that area and
[21:28] then move on to the next one. We used data layers a bit. This was mostly for like organising
[21:36] like big reworks of the map. So we could turn on the data layers when we're done like reworking
[21:40] an area of the map. And again, we're early access, so we're going to keep doing this as we go forward.
[21:45] Nothing we've shipped already is completely final, which helped, but I think we could have done a
[21:51] lot more with data layers to help organisation and especially more stuff at runtime with those.
[21:58] We also made use of automated testing. So we're doing regular free updates through early access,
[22:04] which means we need to keep shipping things. We just can't manually test everything. We don't
[22:10] have a big enough team for that. It wouldn't be fair on our QA testers to ask them to retest
[22:14] everything in the game every time we put out like a small hot fix. So we have some amount of
[22:20] automated test coverage. I think everyone that's ever talked about automated tests will say exactly
[22:24] the same thing. I wish we had more. But once you actually start getting close to deadlines for
[22:30] shipping stuff, that all goes out the window and then you bring it back again once you've shipped,
[22:34] which is what we're doing at the moment. We have a few different methods. We have some gauntlet
[22:39] smoke tests that run just like basic connecting into a game and making sure the player can move
[22:44] around and stuff. We've got unit tests. We've got functional tests. So we've got some basic things
[22:49] like making sure the player can drown if they run out of oxygen or we make use of gas. So we've got
[22:54] a few tests for some of the gasability stuff, making sure that all works and we haven't broken
[22:59] any of that. And we also have a bunch of validators for blueprints and data assets. We found those
[23:06] are really useful, really quick to set up, really helpful for making sure that all of those things
[23:11] where you're like, especially as an engineer, you think, oh, no one's going to do this because
[23:16] I've put it in a document somewhere and asked them not to. Well, a validator makes sure that
[23:19] actually happens. So I won't talk too much about performance because there's a thousand other
[23:27] talks from people specifically on that. But we found the most useful stuff was aggregating ticks.
[23:34] So moving all of our ticks into subsystems and managers and things, at least for anything more
[23:39] than 10 or 15 of them in the world helped a bunch. Unreal Insights is the primary resource for us
[23:47] for doing performance, trace everything. It tells us pretty quickly where there's a problem and then
[23:52] we can fix it and do some more traces. And we have some automated performance testing which
[23:58] we're going to talk about. We have this performance tours tool thing, photo tours, we call them,
[24:05] where we have a script that runs around the whole map kind of taking screenshots. So we can see if
[24:11] there's anything has changed kind of over a few days, visually, majorly, that we might not be
[24:16] expecting. And then it does performance traces. So we can see, for example, on the bottom there,
[24:20] you can see there's like a big spike in, I think that was CPU game thread time. So we can see a
[24:25] spike when it happens, before we would see it kind of just testing the game and play testing
[24:30] ourselves. You see the spike, figure out, okay, that happened within this one day period, have
[24:36] a look at the change list, figure out what happened and then we can get that spike back down again
[24:40] before it kind of lingers in the project for a year and then we have to go back hunting where
[24:44] the performance issue happened. So what do we learn from managing scale? All the tools we needed
[24:53] were kind of already there. Epic's done a great job with this stuff. So most of what we needed was
[24:58] there already. We have a bunch of headrooms. So I'm not particularly worried about us getting to
[25:04] half a million actors at this point. I think there's, I can't see anything coming up that's going to
[25:08] cause that problem. So once we fix kind of the minor issues we had at like 100,000 actors, we've
[25:13] got a bunch of headroom now. Automation helps, especially at runtime, and especially the smaller
[25:19] team, the more we realized we had to use automation to help there. I think we could use
[25:28] data layers more. I think we should look into them more and we probably will over the next couple
[25:32] of years. So I wanted to talk about our act setup a little bit quickly. So we need gameplay on most
[25:43] things. So Nautica games have this thing where you can have a scanner and you can go and scan
[25:47] corals or call plants or creatures and you get a bit of lore telling you about it. It's one of the
[25:55] kind of core features of the game. And that means we need some amount of gameplay on most things.
[26:00] And if most things is 100,000 actors, they can't all be blueprints and they definitely can't all
[26:05] be ticking and doing all sorts of stuff like that. So most of our things are static meshes. A lot of
[26:11] them are instant static meshes. And we weren't particularly careful about merging all these
[26:18] static meshes into singular actors or blueprints. A lot of things like those corals are actually
[26:24] like four or five different static meshes kind of kitbashed together. So yeah, as I said, we don't
[26:30] want 100,000 blueprints. And we also need surface data for all this stuff. So all of the resource
[26:35] spawning needs to know what surface array casts is hit on, not necessarily the same as like the
[26:40] physics surface data. We need to know if we've hit a coral or a landscape or even we spawn
[26:47] quartz on the inside of those coraldomes, specifically on the pearlescent material inside,
[26:53] not on the yellow material or orange material on the outside. So we needed all that data on a bunch
[26:58] of things that were just static meshes. So we used asset user data for that. Once again,
[27:03] Epic's already done the work for us. And we made a couple of extensions to it just so we could query
[27:08] stuff in blueprint, we could get specific asset data. So we have loads of data on our static
[27:13] meshes. We have data assets for scan data, for surfaces to spawn resources on. That coraldome
[27:20] specifically has some data on it that tells us that the big hammerhead creatures we have that like
[27:24] bashing large round things like coraldomes can ram it. They also ram vehicles and other stuff.
[27:32] And we've got some stuff for adding a gameplay tags as well.
[27:36] It runs off a priority system. So we kind of iterate through different levels on the actor. So
[27:42] if we have a blueprint component for asset user data, we look at that blueprint component first.
[27:47] If there's no data on there or there isn't the component, we then look at the root component.
[27:52] And then if there's nothing on the root component, we actually look at the mesh in the root
[27:55] component. So you can add these asset user data to meshes, which means wherever that mesh is used,
[28:01] whether it's in a blueprint or in our case in a prefab or wherever, that data comes with the mesh
[28:06] and you can query that, which is handy. So this is roughly how it looked. So we have asset user
[28:14] data, can be on components meshes, static meshes, whether that's in a blueprint, a static mesh actor,
[28:20] whatever else. And then we have some other things that aren't kind of static mesh actors or blueprints
[28:25] like volumes and things like that. And then they all go into the prefabs that we kind of
[28:30] copy and paste around everywhere. So what do we learn from this stuff? Having a way to put
[28:38] gameplay on meshes is really useful. We would definitely use the actor data, the asset user
[28:44] data again. We just found that really useful. If anything, I would probably use this more in
[28:52] future on another project and go even further than we did here. And we'll probably skip prefabs in
[28:58] the future. What we found was that fighting against the UE workflow rarely worked for us.
[29:06] All of the tools and systems and everything in Engine are all designed to work well together.
[29:12] And if you try fighting against that, you start losing a bunch of the work Epic is doing to improve
[29:17] stuff. And then you're missing out on a bunch of, or at least we were missing out on a bunch of
[29:22] free work that Epic was doing in the Engine that we didn't have to do. So if we'd use level instance
[29:27] workflow and blueprints and stuff, we would have got more out there. Then briefly, I'm going to go
[29:35] over animations. This is what I've been working on most recently. So we have a bunch of creatures.
[29:45] Basically, none of them are humanoids other than the players. They're all completely different.
[29:51] You can see they're on the right just from some concept art. Basically, none of them even share
[29:55] a skeleton, which is great for optimization, great for performance, great for reusing stuff.
[30:03] As I said, no humanoids other than the players right now. And half of them are physically simulated,
[30:08] which is great. So all of this is expensive. It's expensive to move things around. It's
[30:15] expensive to animate things. And it's expensive to physically simulate things. So we had to do a
[30:20] bunch of work here. We made use of the anim budger. It's one of these nice plugins that Epic just
[30:27] has that you can turn on. We use the Skeletal mesh component managed does all of this for us.
[30:33] It kind of just works out the box by default. And then we made some changes, adjusted the way it
[30:39] calculates the priority for animations. So you can see a bit in the bottom right there. It's
[30:44] prioritizing which creatures and plants and things get the animation updates based on how far they
[30:52] are from the camera if they're in view. And in our case, we've added some extra stuff for
[30:57] prioritizing things like our Leviathans, which are our biggest kind of hero creatures so that we
[31:01] know they're never going to get reduced animation ticks. We lured everything. So pretty much everything
[31:11] we have has like three or four different levels of loading. So we lured behavior trees down to more
[31:18] simplified engines. We lured the animations. We reduced the updates on the animations via the
[31:24] animation budger. And if you swim far enough away from a creature, it gets converted into a static
[31:30] mesh that moves around. And if you swim even further away, it's a static mesh that is actually
[31:35] static. So there's loads of layers of logs there, which is the main way we could improve our performance
[31:42] here. And we use multi-threaded animations where possible. So on the top right there's one of our
[31:49] debug menus where you can see how many of our things loaded in level that are animating are
[31:57] budgeted. So that's the skeletal mesh component managed. We didn't use that from the start. So
[32:02] you can see some of them aren't using that. I wish we had used that on every skeletal mesh we have
[32:08] from the start. It's kind of awkward to backport that stuff later. And we do multi-threading
[32:14] where we can. I think we've been pretty good at making a bunch of the animations as income
[32:18] multi-threaded. And we make use of Niagara for the little particle fish. So when you're swimming
[32:24] around and there's 300, 400 fish swimming around, little tiny ones, they're just Niagara systems.
[32:31] There's, I don't mean there's any way we could have done that with full skeletal mesh fish. And
[32:35] they're tiny, so it doesn't matter. And we're looking into masks soon. Again, we looked at it
[32:41] at the start of development. It's kind of not really ready for what we wanted to use it for.
[32:46] And we didn't really have the time to look into it. But going forward, we're going to look more
[32:49] into masks. And there's been a bunch of talks at the Sunreal Fest, which I'm going to check out to
[32:53] learn more about that stuff. So our animation, we had some issues with animation components.
[33:01] So we originally had every fish in the game had this blueprint component on it.
[33:06] Our creature animation component. And every frame, it was getting all these bits of data
[33:10] from all these other components. Velocity, turn, speed, maximum velocity. The delta between
[33:17] this frame's velocity and last one. So we could use all that information in the anim blueprints.
[33:22] So that had a blueprint tick. And we've got 200, 300 creatures at any time in any frame.
[33:31] Aggregated ticks helped with that. As you can see at the top right, we put them all in an
[33:37] aggregated ticker. But you can see that was 1.8 milliseconds on like a dev machine. And none of
[33:44] this is actually doing any work. This is just grabbing variables from places so that we can
[33:48] use them in the animation later. I moved that stuff to C++ that helped. I mean, it helped quite a
[33:56] lot more than anything else. But it's still a bunch of wasted time we had that wasn't really
[34:02] doing anything of and then just grabbing bits of data from places that already had the data.
[34:08] So this is something we did learn from. We're moving to more event driven animations. So
[34:12] we're at a system where instead of gathering all the animation data on tick, putting it all in a
[34:18] component and caching it, when we move the creature around in our movement component or similar,
[34:23] it pushes the event out. You can subscribe to that in the animation blueprint optionally so you
[34:28] don't get them if you don't need them. And then the fish can subscribe to the data they need for
[34:33] the animation style of that creature. No need to update or tick anything here. It's multi-threading
[34:40] friendly. So all this stuff happens on the thread that it actually happens on. And that stuff can
[34:45] all happen on game threads. And then when we go to run the animations on the animon threads and
[34:50] similar later, the information has already been updated from the event. So we don't need to synchronize
[34:55] any like ticks or updates. So what do we learn? Manuscalable meshes. We're using them on all new
[35:04] creatures. And we're eventually going to go and backport that to any creatures we missed
[35:10] when we were putting the Manuscalable meshes in. I wish we'd looked into masks a little earlier,
[35:17] but we shipped the game without it and it runs pretty well. So we've got some headroom there to
[35:22] start looking into masks now and seeing what we can do with that. I think we should have designed
[35:28] a round loading rather than retrofitting it. So we did get a fair way into development before we
[35:34] started considering how we're going to run 300 creatures, all animating skeletal meshes with
[35:41] large amounts of bones. Some of them have physically simulated tails and similar.
[35:47] But there's a bunch more for us to learn here. We're only scratching the surface on animation
[35:51] stuff. And I've already seen some talks here this week, but we'll have some information there that
[35:57] we can learn from. So to summarize, we're going to go through the biggest things we learn on this
[36:03] project. This is the biggest one for me, work with the engine, not against it. I think someone
[36:08] said that in the state of Unreal talk earlier. Everything just works better when you're making
[36:14] use of the tools and systems in the way that Epic designed them. It seems obvious, but it's very
[36:19] easy, or at least we found it's very easy to just go off and do something else that we think's better,
[36:24] and it rarely is. So we're going to try working more with the engine systems and not going off
[36:30] and doing our own stuff. Be smart with plugin and tool use. You saw some of our things we learned
[36:38] with tools and how that was maybe some wasted time and how we save some time by using plugins
[36:44] smartly. And automation helped tons. All the photo tours, performance automation stuff we had was great.
[36:53] The automated testing helps. We will definitely be doing more automated testing in future.
[36:58] The more coverage we can get there, the less work we have to do every time we ship an update.
[37:03] And we will be doing a lot of updates. And we have more to learn. There's always more to learn.
[37:08] There's so much more to learn. And that's it for me. I've finished it.



---

## Captured Frames

- [6:45] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_000.jpg
- [9:50] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_001.jpg
- [10:15] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_002.jpg
- [16:08] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_003.jpg
- [24:20] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_004.jpg
- [28:14] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_005.jpg
- [30:44] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_006.jpg
- [33:40] tutorials/frames/lessons-learned-from-building-a-very-large-open-world-game-in-ue5-unreal-fest-ch/frame_007.jpg

---

## Structured Notes

### Core Technique
Production postmortem of scaling a handcrafted 100,000-actor open world (Subnautica 2, Unknown Worlds) in UE5.6 — covering bespoke editor tooling vs. engine tools (PCG), World Partition + One File Per Actor, asset user data for gameplay-on-meshes, and animation budgeting/LOD strategies.

### Summary
Sam Dark (programmer, Unknown Worlds) walks through what worked and what was wasted effort building Subnautica 2's 3km × 1.5km handcrafted underwater map with 100k actors (targeting 500k by 1.0). The recurring lesson: "work with the engine, not against it" — their months-long bespoke "World Population" procedural resource-spawning tool (raycast flood-fill, later voxelized) was ultimately scrapped in favor of manual placement + PCG, while engine-provided systems (World Partition, One File Per Actor, Anim Budgeter, World Partition Builder commandlets, Unreal Insights) delivered the real scale wins. Also strong endorsements of the Mesh Blend post-process plugin (FAB) for hard mesh seams, and asset user data for attaching gameplay/scan/surface data to plain static meshes instead of 100k Blueprints.

### Key Steps
1. **Placement tooling** — built bespoke tools with `Editor Utility Widgets` and `Scriptable Tools` for mesh dropping/scattering, prop dressing, cliff blend holes, tree roots; now migrating to `PCG` since it matured (early PCG assumed sky-to-terrain projection, unusable for underwater caves/overhangs).
2. **World Population v1 (scrapped)** — runtime procedural resource spawning via raycast flood-fill from a known playable-space seed actor; nonlinear scaling with volume, up to 2h per large region, black-box results invisible in editor.
3. **World Population v2 (also scrapped)** — dropped runtime requirement, baked spawn points into levels; voxelized map at 1m resolution storing surface data per voxel, rules run only on qualifying voxels; slate editor tooling for rule editing; ran overnight on build machine via `World Partition Builder` commandlets (load region → generate → save to data asset → unload → next). Started at 15–20s, grew to 20–30 min; team ended up hand-placing resources anyway.
4. **Mesh seams** — after trying RVT, decals/skirt meshes, foliage cover, and mesh distance fields, adopted the **Mesh Blend** post-process plugin (from Tor via Epic forums, now on FAB): cheap post-process, zero asset changes, widely used by Unreal Fest games.
5. **Prefab workflow** — updated the MIT `Prefabricator` UE4 plugin to UE5 (on their GitHub, no support); now reverting to native `Level Instances` because maintaining the plugin through engine upgrades wasn't justifiable.
6. **Scale management** — `World Partition` + `One File Per Actor` from day one; traced editor slowdowns (e.g. slow deletes at 50k–100k actors from reference checks) with `Unreal Insights` and patched engine code; used `Data Layers` for organizing map reworks; raised the entire map ~6m with editor widget scripts.
7. **Automated testing** — Gauntlet smoke tests, unit tests, functional tests (drowning, GAS abilities), plus Blueprint/data asset **validators** to enforce conventions ("a validator makes sure that actually happens").
8. **Performance automation** — "photo tours": scripted map fly-through capturing screenshots + performance traces daily, so visual regressions and game-thread spikes are caught within a day and traced to a changelist.
9. **Gameplay on meshes** — `Asset User Data` on static meshes/components (extended for Blueprint queries) carrying scan lore, resource-surface rules (e.g. quartz only on the pearlescent interior material of coral domes), creature-interaction and gameplay tags; priority lookup: Blueprint component → root component → mesh in root component.
10. **Animation at scale** — `Anim Budgeter` / `Skeletal Mesh Component Managed` prioritizes ticks by distance/visibility (Leviathans pinned high); multi-level LOD (behavior trees → simplified logic → static mesh that moves → fully static); ~300–400 background fish are pure `Niagara` particles; moved per-frame animation data-gathering from a Blueprint tick component (1.8ms aggregate) to C++, then to event-driven pushes subscribed optionally in Anim Blueprints (multithread-friendly, no tick sync).

### UE Systems / Blueprints / Settings
- `World Partition` + `One File Per Actor` — "genuinely cannot imagine how we would have made the game without these"; from day one.
- `World Partition Builder` commandlets — batch whole-map operations region-by-region on a build machine.
- `Data Layers` — used for staging map reworks; speaker wishes they'd used more, incl. runtime.
- `PCG` — not viable at project start (multi-landscape issues, top-down projection assumptions); now adopted.
- **Mesh Blend** plugin (FAB) — post-process mesh seam hiding; cheap, no asset changes.
- **Prefabricator** plugin (UE4, MIT) — ported to UE5, published on GitHub; being abandoned for Level Instances.
- `Asset User Data` — on meshes/components; extended with Blueprint query helpers; data assets for scan data + spawn-surface rules + gameplay tags.
- `Anim Budgeter` (`SkeletalMeshComponentManaged`) — works out of the box; custom priority weighting added.
- `Unreal Insights` — primary perf tool, works in editor and runtime; "trace everything".
- Aggregated ticks — move any tick shared by 10–15+ world objects into subsystems/managers.
- Gauntlet, functional tests, asset validators for CI on a small team.
- Mass (MassEntity) — evaluated, not ready for their needs at start; on the roadmap.

### Difficulty
Intermediate

### UE Version
UE 5.6 (shipped), upgrading to 5.7, eyeing 5.8

### Tags
`#pipeline` `#automation` `#editor-scripting` `#pcg` `#animation` `#niagara` `#level-streaming` `#blueprint` `#cpp` `#intermediate` `#ue5-6`

---

## Related Entries
- **How to Start Your Project at 60 FPS and Keep It There | Unreal Fest Chicago 2026** (`tutorials/how-to-start-your-project-at-60-fps-and-keep-it-there-unreal-fest-chicago-2026.md`) — Epic Dev Rel's prescriptive counterpart from the same event: day-zero config and system choices for the scale problems this postmortem hit in production.
- **World Partition in Unreal Engine** (`tutorials/world-partition-in-unreal-engine.md`) — the official reference for World Partition, One File Per Actor, Data Layers, HLOD, and the commandlets this talk leans on.
- **Procedural Content Generation Framework in Unreal Engine** (`tutorials/procedural-content-generation-framework-in-unreal-engine.md`) — PCG v2 docs; the engine tool this team wishes they'd had from the start and is now adopting.
- **PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE** (`tutorials/procedural-world-building-for-ue5---pcg-alternative.md`) — Dash scatter tooling, an alternative take on the same placement problem.
