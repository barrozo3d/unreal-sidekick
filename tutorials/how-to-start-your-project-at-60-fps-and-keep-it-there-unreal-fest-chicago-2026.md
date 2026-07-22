---
title: How to Start Your Project at 60 FPS and Keep It There | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=DxBKmQ-0kfw
author: Unreal Engine
ingested: 2026-07-22
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-start-your-project-at-60-fps-and-keep-it-there-unreal-fest-chicago-2026/
frame_count: 0
frame_status: pending-selection
---

# How to Start Your Project at 60 FPS and Keep It There | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=DxBKmQ-0kfw)
**Author:** Unreal Engine
**Duration:** 50m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-start-your-project-at-60-fps-and-keep-it-there-unreal-fest-chicago-2026 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Welcome everybody, or should I say, Avast mateys!
[0:05] And really quick, before we get started, please remember to silence your phones.
[0:10] Don't worry about taking pictures of the slides.
[0:12] I'm going to have a QR code at the end, which will take you to my link tree,
[0:15] which will show you an Epic Developer Community article where I wrote all this stuff down for you.
[0:19] So that out of the way, welcome everybody to a talk that I wanted to title,
[0:26] The Journey to 16 Milliseconds Begins with a Single Step, colon.
[0:31] Hitting 60 frames per second with high quality visuals on Gen 9 hardware in Unreal Engine 5, and keeping it there.
[0:42] But character limits foiled my ambition.
[0:45] Speaking of me, hi, my name is Matt Ostelay, I am a principal technical artist on the Developer Relations team at Epic Games.
[0:51] I have been doing technical art for most of the time that I've been in the games industry,
[0:55] and technical art, as we all know, has a very definition of what it means to which company, who does what kind of things.
[1:02] But throughout all of the technical art that I have done, I've always been doing performance.
[1:07] I've always cared a lot about performance.
[1:09] And if we've spoken for more than about 30 seconds, you know I care an awful lot about performance.
[1:14] And it turns out that a lot of people at Epic care about performance.
[1:19] And there is always new technology and tools and features going into Unreal Engine 5 to support that.
[1:26] And when we started, there was a lot of unexplored territory of how do I do this, how do I make this run in Unreal Engine 5,
[1:34] what features should I be using, and over the last five or so years, we've been filling in the gaps on the map ourselves and with the help of a lot of our customers.
[1:42] So partly what I wanted to do today was highlight the work that my colleagues have done to make the Unreal Engine more performant,
[1:49] and also give you a guide on starting, staying, and returning to 60 frames per second.
[1:54] And why specifically do we want to talk about 60 frames per second today?
[1:58] Well, a lot of our players really want that responsive feel in their games,
[2:03] and we know that the hardware is capable of running some really amazing stuff in only 16.66 milliseconds.
[2:10] But we are not going to be talking about going higher than 60 frames per second today,
[2:15] because it turns out going from 30 to 60 is about 14, 15 milliseconds,
[2:22] and then now we're down to 16.66 milliseconds and we want to go up to 120.
[2:26] Great, do you want to do your game thread in 8.3 milliseconds?
[2:30] Eh, that's not what we're talking about today. So we're not going to talk about going higher.
[2:35] That's a lot of effort. So today, like I said, I'm going to do a very, very brief history lesson
[2:38] because I'm going to get really nitty-gritty on what it looks like to build an Unreal Engine game for and at 60 frames per second.
[2:46] We'll talk about how to monitor to make sure that your game is running at 60 frames per second,
[2:50] and what you might need to do to return to 60 frames per second if you stray from the path.
[2:55] So really quickly, history of Unreal Engine part 5.
[3:00] Not going to go too deep into this, but I did want to highlight a lot of the features, the projects, the improvements,
[3:05] and the resources that we've been developing over the lifetime of UE5.
[3:09] And you can see right around 5.3, Adi and I start doing a bunch of talks to give people the information
[3:16] that we have learned about how to get things running in Unreal Engine 5, more performantly, things like that.
[3:21] And you can see also the features that we started to add and improve.
[3:26] PSO pre-caching becomes a lot easier in 5.3.
[3:31] We parallelized the render thread in 5.4, parallelized the RHI thread in 5.5, 5.6.
[3:37] We get fast GEO and runtime cell transformers and all the stuff that we've done for Nanite,
[3:43] foliage, things like that, all to help you make big games running at 60 frames per second on Gen 9 hardware.
[3:52] There was a version of this talk where I went through every single version of the engine,
[3:56] and we're just going to talk about 5.8 because I don't have a whole lot of time.
[3:59] So 5.8, I feel, is the discerning person on Unreal Engine 5.
[4:03] I'm really happy with this release.
[4:05] Megalights and Iris are now production ready, which is going to play into our performance.
[4:09] Fast GEO is beta. A lot of stuff has been smoothed out with Fast GEO.
[4:15] We'll talk about that in a second.
[4:17] The Lumen irradiance field gather, so Lumen light for some lower hardware.
[4:24] Really useful option there.
[4:26] Dynamic Res on PC is now an option, which I'm excited about.
[4:31] And then we've got a lot of shader reduction tools that are coming on in 5.8,
[4:35] as well as some experimental stuff that I'm really excited about,
[4:38] like mesh terrain and Nanite bindless shaders,
[4:41] as well as improvements to the procedural vegetation editor,
[4:44] and world partition streaming insights.
[4:47] And we've come a long way on this journey of learning about the performance of the Unreal Engine
[4:53] and all of our features, building the tools that you need, things like that.
[4:58] I just wanted to share a little bit with that, a little bit of that with y'all.
[5:02] So let's take a lot of those learnings.
[5:04] And this is really everything that I have learned from talking to our customers,
[5:09] from building projects myself, from stuff that we've learned at Epic,
[5:13] about how to really build these huge scale games at 60 frames per second.
[5:19] And this talk is assuming that you have already set up your Unreal Engine studio
[5:24] the epic way.
[5:27] So we're going to tackle this in two stages.
[5:29] It's first day one, day zero really, right after you make the U project.
[5:34] There's some things I need you to do.
[5:36] And then over the course of pre-production and prototyping and things like that,
[5:40] things I want you to keep in mind, features that are in the engine
[5:43] that are going to support you in your ambitions of building these big games at these high frame rates.
[5:49] So let's look at our very first change list, CL1, right?
[5:54] I made a new U project.
[5:55] I disabled some default plugins.
[5:57] I enabled some other plugins.
[5:59] I set some default project settings.
[6:01] And then I added two INI files to my config folder.
[6:04] Default editor settings.INI and default device profiles.INI.
[6:08] And then of course I tag it so that all this stuff shows up in JIRA.
[6:12] And it was, you know, I got the change list reviewed, right?
[6:15] So there are not a lot of project settings, project settings specifically in UE5
[6:23] where I'm like, okay, you absolutely positively have to do this if you want to build a game
[6:28] with high frame rate that runs performately.
[6:30] And there's, it's really like three settings and a bonus.
[6:35] So we all know UMG bindings, right?
[6:38] Where you could like every property in UMG, you could click it
[6:40] and then you could bind it to a function that would update that variable, right?
[6:44] Don't use those.
[6:46] Those are legacy.
[6:47] They are very slow.
[6:48] They're executed every frame.
[6:50] I can see them in your insights traces.
[6:52] Please don't use them.
[6:53] And in fact, what's really cool is if you go into your project settings for the editor,
[6:58] for editor utility widgets and for game widgets, you can prevent them from showing up at all.
[7:05] So you set the property binding rule to prevent and you never have to worry about somebody using
[7:10] UMG bindings in your project.
[7:12] The next one that I'm going to want you to set is the collision complexity.
[7:15] Please set this to use simple collision as complex collision.
[7:20] As Ari and I like to talk about, I can see it in your Chaos Visual Debugger.
[7:25] There's a lot of stuff that is using complex collision and the issue has been compounded by
[7:31] maybe some of you haven't been setting the number of logs in your Danite meshes.
[7:35] And so your fallback meshes, which are used for complex collision, are also your 2 million triangle Quixel Megascans rocks.
[7:41] Complex collision at 2 million triangles is very, very expensive.
[7:46] So we can get ahead of that by just setting this default setting.
[7:51] And then the other thing that I think would be really helpful is create an editor startup map that is nothing.
[7:57] So that when you open the editor, it's faster to get into the editor and the faster it is for you to iterate,
[8:02] I think the better it's ultimately going to be for your project.
[8:06] And this is, I think I'm going to get up on my soapbox here and talk about defaults in the engine.
[8:12] The engine is set up for people learning to make games the first time.
[8:19] Maybe the Saw YouTube tutorial, they downloaded Epic Game, they downloaded Unreal from the Epic Games launcher
[8:25] and they wanted to see this cool shader tutorial.
[8:28] And what I know is that all of my primitive components should have evaluate world position offset disabled,
[8:35] but because that's something that I would have to change engine code to ensure is default,
[8:40] we're not going to set that because what I really don't want is little Timmy learning Unreal for the first time
[8:46] and not know why his world position offset shader isn't working.
[8:49] So there are a lot of defaults in the engine that make it easier to get things done,
[8:55] but when we're talking about big games running at 60 frames per second,
[8:58] we're going to turn a lot of this stuff off by default and make it opt in like complex collision.
[9:03] We're going to opt into complex collision rather than opt out.
[9:07] I'm going to very briefly talk about frame pacing because you're all just going to stay in this room and go to Ari's talk afterward.
[9:13] So frame pacing, there's a console variable that is called r.gt sync type, the default value of zero.
[9:21] That's kind of more or less what you want to use for PC.
[9:24] There's some other stuff.
[9:25] Again, Ari's going to go into this.
[9:26] If we're looking at a mobile project, we're going to use r.gt sync type one and for Gen 9 consoles,
[9:32] we're going to use r.gt sync type two.
[9:34] And if you want to learn more about that, go to Ari's talk after this.
[9:37] He goes into so much depth and I don't want to, I don't want to rain on his parade.
[9:42] Other thing I'm going to do like, okay, right, I've made a U project.
[9:45] I've opened the editor first time before I even get to restarting the editor for anything.
[9:50] I'm going to go in and turn off a bunch of plugins and I'm going to turn on some plugins.
[9:54] The two that I really want you to turn on now so that we can start using them later are data validation and the asset referencing restrictions plugin.
[10:01] Data validation gives you a bunch of tools for to write C++ or blueprint validators for literally everything in your project.
[10:08] And asset referencing restrictions means that effectively I can make sure that nobody references their developer content in the main world map, which is very helpful.
[10:18] You're also going to want to turn off some of these plugins that you might not need.
[10:22] So for example, if I know which source control provider I'm going to use, I can turn off the source control provider plugins that I'm not using, right?
[10:30] It's I'm at a big studio. We only have one source control. I can turn the other ones off.
[10:34] Same thing with like source code editors.
[10:38] You know, some other stuff that you're probably going to want to turn on is going to be like fast GEO, a lot of the procedural content generation framework stuff, geometry script.
[10:45] Those are ones that I usually end up turning on all the time anyways.
[10:49] So I've changed some project settings. I have updated my plugins. Am I running at 60 frames per second?
[10:56] Does anybody raise your hand if you think the first time you open a new project, you're set up to run at 60 frames per second.
[11:03] Nobody. You are all correct.
[11:06] So does anybody know why?
[11:09] No? It's these guys.
[11:11] Here, let me zoom in on that. There we go.
[11:13] So up in the viewport, there is this scalability menu.
[11:17] And you can see that all of the rendering features are set to epic by default.
[11:23] And the epic scalability groups are your 30 frames per second quality mode.
[11:29] So when I'm looking at the editor right now, I am not looking at the game as it would be in 60 frames per second mode.
[11:34] I'm looking at it in quality mode.
[11:37] And so I need a way to change this.
[11:39] And of course, anybody could just go in and click high, right? That's easy enough.
[11:43] But because this is the first change list, nobody else has opened this project yet.
[11:49] I have some things I can do to make sure that all of my developers are going to be looking at the 60 frames per second version of the game.
[11:57] So that is where default editor settings I and I comes into play.
[12:01] So what I'm going to do, I'm going to put this in my config folder, and I have this little scalability group section.
[12:06] And all of the scalability groups are set to two, which is high.
[12:11] And now anytime anybody opens the editor in this project, by default, they're going to get 60 frames per second mode.
[12:18] And if anybody makes any changes to this, or if you want to make sure that everybody's running at the correct version,
[12:23] the edits to this are saved in the engine saved config folder.
[12:28] So if you ever need to reset anybody to defaults or some software we just have to delete our userprefs folder, that's what this is.
[12:36] And this is all going to be in the EDC article at the end.
[12:40] Now, we've got to make sure that the game is also doing that, right? And that's what device profiles are for.
[12:46] This is mandatory if we are trying to run at 60 frames per second.
[12:49] And I love device profiles. They are hierarchical, so I can set up a whole tree of device profiles.
[12:55] Every imaginable setting, texture-lawed groups, every CVAR is something that you can change with a Devost profile and change it all at once.
[13:04] So I know that, like, okay, these are all the settings that I want to be set exactly if I'm running at 60 frames per second.
[13:10] And if you are somebody who has access to the NDA platform folders, we added suggested device profiles
[13:17] for those platforms running at 60 frames per second.
[13:21] So if you have that code in your repo, you can find out what Gen 9 underscore 60 frames per second should look like.
[13:29] So definitely use that as a starting point.
[13:32] One of the things that you are going to be setting in your Devost profiles is your resolution scaling settings.
[13:39] And this is the important one.
[13:42] So what we learned on the Witcher 4 UE5 tech demo last year is to focus on rendering a lot of our resolution-dependent features at a smaller dynamic primary resolution,
[13:54] anywhere between about 810.80.
[13:57] And then using, and that's going to be with your r.dynamic res or r.screen percentage console variables,
[14:03] and then we use TSR to secondary upscale, or to upscale first, to our secondary resolution of 1440.
[14:11] And the reason for this is that we know that TSR can go up to 2x.
[14:18] So you can go from 1080 to 4k, but anything lower than about 1080, you can start to see some quality loss there.
[14:27] And so the thinking here is let's use TSR to go from maybe 800 up to 1440 with r.secondaryscreenpercentage.gameviewport.
[14:38] And then finally we will do a spatial upscale to our final output resolution of 4k,
[14:44] where we'll flip everything to the back buffer and render the UI at the full frame size.
[14:49] And you can tweak the settings here with r.upscale.quality.
[14:52] This is the slide you can take a picture of.
[14:55] If nothing else, when we are thinking about how do we run a 60 frames per second game, in Unreal Engine 5, it is secondary upscaling.
[15:03] We focus on rendering fewer, higher quality pixels, and then doing secondary upscaling to get us all the way up to 4k.
[15:15] Okay, that's the show. Thanks everybody. Really appreciate your time.
[15:18] No, we're not done.
[15:21] So I'm going to put all of this in my default device profiles, I and I.
[15:26] So something, it might look something like this, where I have my project, I have a 60 Hertz project,
[15:32] targeting the Windows platform underscore 60.
[15:35] And I'm going to go through and I'm going to have all of my scalability groups set to 2 for static resolution platforms.
[15:43] Let's set that up a little bit.
[15:45] So r.secondaryscreenpercentage.gameviewport equals 75 is how we go 4k to 1440.
[15:51] And then r.screenpercentage is for static resolution platforms, and that's going to be right around the middle.
[15:57] It's like 900p basically. And then for dynamic res, I'm going to set my frame time budget to 16, maybe 16.66 if you're feeling fancy.
[16:06] And then the min and max screen percentage for dynamic resolution is going to be between 55 and 75, and that's my 800 to 1080 of 1440.
[16:15] So this is the other one, and I'm going to put this in my config folder.
[16:19] And then if I already know that I have a bunch of platforms, I'm going to be supporting.
[16:22] I will put platform specific device profiles and I will set them up automatically from day one.
[16:28] And this is really the big thing for me is I think trying to get, trying to set all this stuff up when you're in the middle of production can be more of a challenge.
[16:37] And so I think if we do it on day one, we don't even have to think about it.
[16:41] We already know that all the console variables are where we want them to be to run at 60 frames per second.
[16:48] The tricky thing with device profiles is you do have to set them.
[16:52] The engine does not have something that goes, ah, you have a 60 frames per second device profile, I'm going to use that one whenever I boot up.
[16:59] You do have to have something that selects the device profile.
[17:02] And there's a few different options for this.
[17:04] There's an example device profile selector plugin.
[17:07] There are some examples in the platform engine, INI folders.
[17:12] And if you want to get really advanced, go look at you Lyra settings local.
[17:16] That's got a lot of logic for setting device profiles.
[17:19] And there's also a device profile selection module and preview device profile selection module that you set in your default engine, or your default device profiles INI.
[17:29] So I'm going to make sure that I have something set up that knows, okay, if I'm booting up on this platform, I need to use the 60 frames per second device profile.
[17:36] And that's great.
[17:38] So now that I've done all of that, I'm going to submit.
[17:41] Great, ship it, we're done.
[17:42] No, we're not done.
[17:44] Because now we have to actually build our game for 60 frames per second.
[17:50] So let's talk about that, right?
[17:51] We're in pre prototype, we're prototype, we're pre production.
[17:54] And we got to figure out what kind of game we're building, right?
[17:57] What features do we want to make use of?
[17:59] What's our platform range that we're targeting?
[18:01] We got to figure out what kind of game we're actually building and how to build it optimally.
[18:06] And I say building optimally because it's about making sure that the hardware is doing the right work of spawning and loading and simulating, rendering, animating and all that fun stuff.
[18:16] There are a lot of systems in the Unreal Engine to help with that, knowing the kind of game that we are building, right?
[18:22] And it means I'm going to start talking about a lot of best practices, asterisk.
[18:29] Not all SES will qualify, no purchase necessary, if hardware prohibited, contact matters.
[18:32] You got to make the game that makes sense to you.
[18:33] I'm making some assumptions about the kind of game that you're trying to make and presenting information most relevant to that kind of assumption.
[18:36] If you don't feel like it applies to you, feel free to ignore it, I'm not your mom.
[18:40] This section is also meant to bring awareness to a lot of the features of the engine, whether or for why you might use them to build the game, right?
[18:48] There is a pretty sharp cutoff between, hey, I can just do it with Blueprint and, oh, I should really be using mass for this, right?
[18:56] And the other way to look at this section is like, if you asked me, here's how I'm going to do it.
[19:01] So when I'm building a large-scale open world game targeting Gen 9 consoles and high-quality visuals at 60 frames per second,
[19:10] one of the biggest decisions I'm going to make is how I populate and build and stream my world, right?
[19:15] So world building, I lump this category of like PCG, world partition, HLODs, and we're also going to talk about our async timing budgets.
[19:23] Because our goals here are, one, to improve iteration and construction times for our developers.
[19:28] I really think that this is a factor in building performant games.
[19:32] The faster I can iterate on my game, the more likely I am to be able to make the change that will bring me back to 60 frames per second.
[19:39] And with world building, we're really thinking about reducing the number of active actors, reducing the number of active components instances, while still representing a large open world.
[19:49] And PCG is a really big part of this. And I'm going to be a bit of a knowledge dump here.
[19:54] So for me, PCG is about empowering artists to work faster and better while still being creative and expressive.
[20:02] Things like the level instance to PCG data asset workflow are really powerful for like, the artist is in control.
[20:08] The artist is in the driver's seat of what is getting spawned.
[20:11] PCG editor mode gives them a lot of control about where things are getting spawned.
[20:15] We can use the Scriptable Tools framework to do a lot more stuff, give the artists a lot of control over how they're building out their world.
[20:22] And 5.8 brings manual editing to PCG. So if you have a graph and you run it, and then you're like, ooh, that tree needs to be a little to the left.
[20:30] We can now do that in 5.8, which I'm excited about.
[20:33] I also think of PCG as a way to enforce building standards.
[20:37] So if all of the stuff that's spawned into the world is constructed exactly the way that I want it,
[20:43] I know that my world is being built the way that I have set in my style guide. I don't have to stress out about that.
[20:48] And of course, PCG is not just for geo, things like the effects, gameplay objects, audio.
[20:53] We can spawn a lot of stuff with PCG, which improves our iteration times.
[20:57] Now, what I'm definitely going to do as I'm building my 60 frames per second large open world game on Gen 9 consoles with high quality visuals,
[21:04] I'm replacing landscape grass types. I'm not using them. I don't like them.
[21:08] They have a CPU cost associated with them.
[21:12] I'm going to replace it with partitioned, hierarchically generated GPU only instances.
[21:19] It is a lot faster. It's faster to generate. There's no CPU overhead associated with it. I just like doing it better.
[21:27] When we are building our PCG graphs, we want to make sure that we are discarding points as quickly as possible.
[21:33] We want to think about how graphs output data for other graphs.
[21:36] A big thing that I need everybody to know is that generate on demand does not just mean when I click the generate button.
[21:45] It means whenever something needs to generate from that PCG graph.
[21:50] So sometimes you might put a perfectly reasonable blocking synchronous load into a blueprint call in your PCG data or in your PCG graphs
[22:00] because you expect that PCG graph to only run in the editor.
[22:04] But sometimes we need to rerun that graph at runtime and you might miss this.
[22:10] So what you can do is mark those PCG components as editor only so that there's no way that they could possibly be run at runtime.
[22:18] And then of course I'm going to use PCG builders to wrap all of my big PCG systems together.
[22:23] There was a really great talk from Chris Murphy and Adrian Loget at GDC.
[22:27] It will be in the links at the end of the show about how to build large scale PCG interoperable systems.
[22:35] So definitely check that one out.
[22:37] I'm going to be using World Partition for my world streaming. I really like using it.
[22:42] Now a while ago there was maybe some talk that the number of streaming grids was how you control like,
[22:49] oh, this is the high detail, the medium detail, the low detail.
[22:53] I'm not a huge fan of that anymore. So instead for like a lot of the smaller detail stuff,
[22:58] I'm going to use that runtime hierarchical PCG generation.
[23:02] The size of your streaming grid, the size of my streaming grid is going to be very project dependent.
[23:07] This is something that as I am working through pre-production, I'm going to be figuring this out.
[23:11] I'm not just going to rely on the default settings in the engine.
[23:14] I am going to use runtime cell transformers.
[23:17] These are great because they take the stuff that is in a World Partition streaming cell
[23:22] and they transform it into a format that is more performant for runtime usage.
[23:28] So FastGeo is beta in 5.8.
[23:31] I don't always like saying epic says blah blah blah, but like use it please.
[23:36] There's a lot of power there to basically do what we think is happening in our brains.
[23:41] When I put a static mesh actor in the world and its mobility is static,
[23:45] I think it should be fairly cheap, but like that is an actor and a component that has to be spawned.
[23:50] And spawning actors and components takes time.
[23:52] So if I can make it not an actor and not a component, it'll be faster to stream in at runtime.
[23:58] For Pi startup, I think we actually have editor or world settings for this
[24:03] to slowly grow the streaming radius when I'm in play and editor.
[24:06] So it helps me get into play and editor faster.
[24:10] Depending on the project, I might need to think about building a custom streaming hash.
[24:14] So I need, you know, if I have a world where I've got a bunch of tunnels and caves, right?
[24:19] I'm super excited about mesh terrain.
[24:21] I might need to think about a different way to stream that than just the default streaming hash set that came in 5.5.
[24:29] And of course I'm going to use data layers for a lot of state swapping.
[24:32] There's a lot of really cool stuff in my colleague Zhikong's presentation about persistence,
[24:37] which unfortunately was at the same time as my pirate talk.
[24:39] But I've got some links of EDC articles that he wrote in the links at the end of the show.
[24:44] And of course level instances and packed actors.
[24:47] I really wanted to talk about these briefly in the context of building large open worlds,
[24:51] because the level instances get baked down into the streaming grid,
[24:56] but a packed level actor is an actor.
[24:58] And actor bounds are what determines which streaming cell it's going to be put in.
[25:02] So if I've got a really big packed level actor that covers two city blocks
[25:08] and my streaming grid is half a city block, now it's always going to be loaded in.
[25:12] So I really have to think about the size of the packed level actors that I'm going to have my artists working with,
[25:19] the size of those level instances and how I'm going to use them.
[25:22] And then finally I wanted to talk about the async streaming budgets.
[25:25] So every frame the engine is going to try to stream in more stuff as we're moving through the world, right?
[25:31] That's add to world.
[25:32] And by default the budget for that is 5 milliseconds.
[25:35] And we can do a little bit of math and we know that 5 milliseconds out of 16 is a lot.
[25:40] So I might tune that down with a couple of different console variables to tune what kind of streaming I'm doing,
[25:47] how much of it per frame, things like that.
[25:49] So I'm going to change those settings.
[25:51] There's a few different console variables there.
[25:53] We'll talk about that at the end of the show.
[25:54] There's also project settings for that.
[25:56] And again, anything that's a console variable can be part of a device profile, right?
[26:00] I am going to use HLOTS.
[26:02] Partly because they are required for hardware ray traced lumen far field.
[26:06] If you want to have lumen, stuff in your lumen scene beyond the default lumen streaming distance,
[26:12] I'm going to have to use HLOTS.
[26:14] If I'm using HLOTS when I'm using HLOTS, I'm going to use the approximated mesh method.
[26:20] And importantly, I am going to check this checkbox called use render LOD meshes.
[26:27] Because what this does is use your fallback meshes.
[26:31] So my 2 million triangle Quixel Megascan rock, I've set a bunch of LOD settings on it for its fallback.
[26:37] And it's, you know, LOD 8 fallback is like 10 triangles.
[26:41] Now that 10 triangle rock is part of the HLOT build, and my computer doesn't run out of RAM
[26:46] whenever I'm trying to build my HLOTS.
[26:48] That checkbox, that's the one.
[26:51] I'm also going to create project specific HLOT layers, right?
[26:56] I know that by default, like you get an instance layer and an emerge layer.
[27:00] I think what I'm going to do in production on my game is I'm going to evaluate whether or not I need
[27:06] an instance layer or fast GEO is going to do most of the work for me.
[27:10] And I can increase the size of my streaming grids so that I don't really have to manage like,
[27:14] oh, and then this is an instance, and then this is a merged mesh, right?
[27:18] But I'm going to evaluate that.
[27:20] And I'm going to think about customizing my HLOT class.
[27:23] Maybe I want to have some functionality on my HLOT for like, oh, that building could be
[27:28] partially destroyed, and I don't want to have to like bake a separate HLOT for it.
[27:32] I can make my own custom HLOT class.
[27:34] I can make my own custom HLOT builder classes.
[27:36] There's a lot of really cool stuff and power within that that I'm going to explore so that I could build my game
[27:42] as a high quality visual on Next-Gen hardware.
[27:46] And of course, I'm going to, because I've set up my Unreal Engine Studio the epic way,
[27:50] I'm going to run my HLOT builds every night after I run my PCG builds every night across a bunch of different
[27:56] agents so that I can amortize that work.
[27:59] How you build your gameplay, of course, has a huge impact, right?
[28:02] There's a whole thread called the game thread, and that's what we're going to talk about here.
[28:06] And this is me very poorly playing Lyra.
[28:08] So my goals with gameplay generally are building extensible systems that everybody can use that fit in my budget, right?
[28:19] I'm going to talk about this very, very briefly.
[28:21] Ultimately, this is up to you, right?
[28:24] Some people can build an entire game without ever writing a line of C++.
[28:28] That's great.
[28:29] Some people don't want to do that.
[28:30] That's also totally fine.
[28:32] But definitely profile it, right?
[28:34] Determine what the right balance is for your project.
[28:36] See if there's something that your engineers should be nativeizing for your designers because you've got a very expensive operation.
[28:43] I'm not going to spend a whole lot of time on this.
[28:46] There are a lot of really great resources on there about how to structure game code correctly, performantly, things like that.
[28:55] Really, I think for me it's a lot about teaching your designers a little bit of computer science and teaching your engineers a little bit of game design so that they all know what they're talking about together.
[29:08] That's all I'm really going to say about that.
[29:10] There's not a lot of secrets there.
[29:12] But how I might want to have my living world built and expressed is a major, major part of performance in these large scale games, these large scale open world, yada, yada, yada, yada.
[29:25] And I call this living world because I've had to find a new word that encompasses these kinds of features.
[29:31] So my goals here are to scale the simulation of my living worlds from maybe tens of actors to hundreds of actors to even thousands or tens of thousands of agents all running around and doing a lot of really cool stuff.
[29:43] And I want to enable those agents that are populating my living world to have efficient activity and navigation throughout that world.
[29:52] So State Tree is going to be a really big part of how I'm building all of these systems.
[29:57] They are tickless as of 5.8. This is really cool.
[30:01] It means your State Tree components are not all ticking every frame.
[30:05] So I'm going to think about now, as I'm starting my game in 5.8, I'm going to think about utilizing async or event driven patterns so that the tree is only evaluating when State needs to change, right?
[30:17] And where possible... Oh, I do want to mention.
[30:20] State Tree is not just for NPCs. It can be used by a lot of different systems.
[30:25] I have heard of somebody that used State Tree to drive their UI transitions. That was really cool.
[30:31] But it pairs really nicely with the environmental query system, which is also not just for efficient navigation.
[30:38] It helps my agents determine where they need to move in the world and how to navigate things like that.
[30:43] I do want to make use of things like linked assets and parallel State Trees, because these are designed to hold reusable behavior.
[30:51] Now, the recommendation that I got from my colleague who works with a lot of these systems is it is a good idea to be prototyping a lot of these State Tree tasks in Blueprint
[31:00] and then nativeizing them to C++ when you're getting pretty close to finalizing those, because we're going to be running these on a lot of different actors.
[31:09] And finally, debugging for the State Tree is now rolled into the animation Rewind Debugger.
[31:16] So keep an eye out for that if you had previously used the one that was just built into State Tree.
[31:21] Now it's just the generalized Rewind Debugger. I wanted to call that out while I was talking about it.
[31:26] Navigation is a really big part of this, and static navmesh can be an option, and there has been some work in this area.
[31:33] Much like a lot of other systems on the rendering side of things, I'm going to go with Dynamic.
[31:38] So Dynamic Navin Vokers are kind of the way to go. The basic idea is a Navin Voker says,
[31:43] I would like some navmesh please, and we generate some navmesh around that thing that has invoked the generation of navmesh,
[31:49] so that I don't have to hold 16 kilometers by 16 kilometers worth of navmesh all at the same time.
[31:56] I can just say, I just need navmesh right now. The added bonus is when you blow something up in your world or you change a data layer,
[32:02] you don't have to rebuild all of the navmesh in order to do that, right? It's all just dynamic.
[32:07] And then I'll probably need some kind of hierarchical system. Maybe I build something with EQS to say,
[32:12] okay, I've got an enemy over there and they need to come toward me, but I don't want them to also be doing navin voke,
[32:18] so they're just going to start walking toward me. I'm going to have a system to help them do that.
[32:23] And then when they get close enough, now they're part of my navmesh.
[32:27] Mass is a really big part of this. When I think about the like, hey, things that we wish we had done or things that I really want people to do
[32:35] when we're talking about tens of thousands of things happening in the world,
[32:40] mass is the answer. So as a general, I'm going to briefly blow through this.
[32:45] So mass is a lot of large scale operations. I have to do a lot of them all at once.
[32:50] And this operates on a struct of arrays. So rather than for each actor, I need to update the transform,
[32:58] update the rotation, and then figure out where they're going next, what mass is basically doing at a very, very high level.
[33:04] It's going, I'm going to update all the transforms, and then I'm going to update all the rotations, and then I'm going to update the goal positions.
[33:11] It's much more efficient computationally. And the other reason that I really want you to be thinking about mass
[33:18] and how it fits into your large scale open world 60 frames per second game is it underpins instanced actors,
[33:25] which I think I'm going to be using instanced actors in my large scale open world 60 frames per second game,
[33:30] because it basically means that when a thing becomes relevant to gameplay, it is fully hydrated actor, blah, blah, blah.
[33:38] And then when it's not relevant, it is an instanced static mesh. This is like disabling tick on your actors on steroids.
[33:46] And Jikong has a bunch of, much more information about this. I realized that his EDC article is kind of the first big one talking about it.
[33:55] So definitely check that out at the end of the show. Like I said, his talk was this morning, sorry, you missed it.
[33:59] And then after this, if you don't want to go to Ari's talk, Jared is talking about basically how to get your brain to think about mass.
[34:07] And then Henry is going to talk about what we can do with mass in the context of crowds, because crowds is usually where I see the mass thing become a really big issue.
[34:16] So, oh boy, I'm running short of time. So I'm going to briefly talk about animation. In 5.8, I'm still using animation blueprint.
[34:25] Anything larger, large scale, or like, oh, I don't want to have an anim BP running this. I'm going to move to something that's mass based crowds or vertex animated textures.
[34:35] Generally, I'm going to be profiling and nativeizing complex processing in my animation blueprint. I'm going to be really careful about, hey, maybe don't update a bunch of attached components every frame.
[34:45] I always see that in insights traces. And I'm probably going to start off, and this is the big one, I'm going to start off using the anim budget allocator from the hop.
[34:54] Because if I realize I need to use it later, there's a bunch of re-parenting that gets really, really messy. So I'm going to just use it out of the box.
[35:01] Simulating your large open worlds is a really big factor of it to write our destruction, how complex our collision is, our trace and object channels, things like that.
[35:10] I think actually this last one is probably the more important one is, you know, that list of world dynamic, world static, pawn vehicle, whatever.
[35:20] You can add to that. That's a project setting, and I think you can add up to like 32. So if you have something that's like, oh, this is an interactable, rather than doing like get all overlapping actors and then doing a cast to see, or even doing an interface call,
[35:35] you can say, okay, this is an interactable object, and my volume can only overlap interactable objects, which means I have fewer things to update overlaps on.
[35:45] And then I know that I've already limited my scope of what I'm going to be overlapping. I'm going to lean really heavily into that.
[35:52] And then if I'm doing a bunch of destructible stuff, I'm going to lean heavily on Dataflow for iteration. Another great talk about that from GDC last year that's linked in the notes at the end of the show.
[36:02] Particle effects are another thing that has a really outsized impact on this. I just really, briefly want to touch on systems as a service.
[36:10] So I talked about this in the in the profiling with Pirates Talk, rather than having like Niagara system actor, Niagara system actor, Niagara system actor, Niagara system actor, I'm going to have a system where there's only one Niagara system.
[36:23] And then I'm going to spawn a bunch of those different particles using Niagara data channels so that I only have one ticking Niagara system.
[36:32] As I'm building everything out, I'm going to have effect types that's going to let me do a lot of really cool scalability stuff, right?
[36:37] So maybe I have more particles show up, or they do more complex logic in my quality mode at 30 frames per second, because I can spend more time on it.
[36:45] The other thing that I'm going to think about with Niagara is using lightweight emitters. If I've got a looping particle that doesn't have to really react to anything in the world, I can use lightweight emitters for things like that.
[36:55] And if you want to learn more about chaos and Niagara, definitely check out Philippe's talk tomorrow at 9am about how Fortnite built a lot of their living world creatures with Niagara.
[37:06] That is basically the Niagara data channel talk. And then Vincent tomorrow at 1145 is talking about optimizing chaos. So there's a bunch of cool stuff in there.
[37:15] Now we get to the meat of things rendering my favorite part. All right, I'm going to have to rip through this. All right, Nanite, you have to set a number of lads on your Nanite meshes.
[37:25] Go into your static meshes, set num lads. I really, really, really need you to do that so that it generates fallback meshes, which are more efficient to ray trace against, more efficient to complex collision.
[37:36] And it means you have something when you need to deploy to Nanite platforms. Just please set a number of lads.
[37:44] And think about the ray tracing proxies. So five, I think five, six, maybe five, seven, we added the ability to have a separate, distinct ray tracing fallback or ray tracing proxy so that I can tune how this is going to look right.
[37:57] If we're using mega lights, now we're using ray tracing for direct lighting. And those ray tracing proxies become really, really important.
[38:05] In my materials, I'm going to set something like max displacement. So if I have a WPO, I'm going to limit how far that WPO is going to move, which is going to help me improve my cluster calling.
[38:16] If I am using displacement and tessellation on my materials, you have to go into the material and enable the displacement fade checkbox.
[38:24] I wish that was on by default. For everybody in this room, go home, figure out all your tessellation materials and just check that checkbox.
[38:32] And of course, I'm going to make sure that I have disabled distances set both pixel programmable disabled distances and WPO disabled distances so that my programmable rasterization falls back to fixed function at a distance.
[38:45] A really important thing with Nanite is reducing bin counts. And the way we reduce our bin counts is by architecting our materials.
[38:53] So the shading bins is the number of unique material instances. So material instance, constant material instance dynamic.
[39:00] And the way that I can reduce the number of those in my project and the number of those in my scene is using custom primitive data and per instance custom data for changing, you know, I want to do a little bit of variety on this thing.
[39:11] I want to tweak the color on this thing. I'm going to use per instance data for that instead. And then if I want to change a global value, I'm going to use a material parameter collection rather than looping through and updating a bunch of material instance dynamics.
[39:23] This is a really big one usage flags is about generating a bunch of shaders. Jason and John are going to talk about this later how they did this in Fortnite 5 8 has per material instance usage flags.
[39:33] So if you have one of those like ooh, the landscape materials also used on a Niagara mesh particle, you all have this I know you do.
[39:40] You can now say, okay, this material instance is the one that's going to be used and generate the permutations for the Niagara one. We're not going to have to generate a whole bunch of permutations.
[39:49] Now this is a big one. Large world coordinate rendering. We have all seen this in every material tutorial that has ever existed since like Zach Parrish in UE3, right?
[40:01] World position subtracted from actor position gives me a vector that I can use with. Well, large world coordinate rendering means that that actually causes us some problems when we are evaluating our base pass.
[40:12] So large world coordinate stuff means that we have to do a little bit of extra transform. The engine has to do some transform on that math.
[40:18] The math gets more expensive if we math it this way. So instead, I'm going to use camera relative stuff as much as humanly possible or periodic world space because anytime I introduce large world coordinate into my material math,
[40:33] it might be part of my performance problems. I am not suggesting that all of you have to go through and audit your materials for this, right?
[40:43] That is about profiling. So if I profile and my base pass is really slow, I might look at my large world coordinate usage in my material.
[40:51] But because we're talking about starting a project at 60 frames per second, I'm going to set this standard early so I don't have to worry about it later.
[40:59] Again, link in the show. One of our rendering engineers wrote an article that was basically like, don't do this, do this instead, and you will find those patterns in your project.
[41:08] Only do it if your base pass is slow. Substrate. Oh, God, I'm going slow. Substrate. My tech artists are going to make a fixed material topology.
[41:18] Substrate slabs are not material layers. That's really important. Every BSDF and blending BSDFs can be very, very expensive.
[41:28] I think generally for the purposes of a lot of people in this room, we're going to have one BSDF. We're going to have one substrate slab.
[41:35] And then maybe as a treat, I will have an extra one for like clear code or slightly different clear code.
[41:42] And again, the artists are not the ones that are going to be making new slabs. Most of it is all going to funnel into one slab.
[41:50] Lumen, I'm using hardware ray tracing. We're really confident in the performance right now. My reflections with Lumen, I'm going to make sure that my roughness to trace value is set appropriately.
[42:02] Because I've seen a lot of projects where like the roughness values in the project is like point, most of it is like point three five, and the default roughness to trace is point four,
[42:12] which means most of the pixels on screen are tracing dedicated reflection rays, which is very, very expensive.
[42:17] So I'm probably going to move that down. And I'm probably going to set the foliage value to just zero just out of the gate.
[42:23] Megalights, I am thinking if I'm going to use Megalights in my project. Yes, they're production ready in five eight. They're great.
[42:31] This is a feature that I can leverage if I need a bunch of lights in my world, right? Because overlaps still matter, mostly for noise, not necessarily for performance.
[42:40] And I do have to get really, really careful about thinking about my instance overlap so that that affects ray tracing performance.
[42:48] The complexity of my ray tracing proxies is also going to affect performance here. I really have to think about that as I'm setting the standards for building my 60 frames per second.
[42:56] And if you are using Megalights, just go all in on Megalights. And wrecked lights are still as a treat. I'm not going to use a lot of wrecked lights in my world.
[43:07] They are still expensive. If I'm using virtual shadow maps, one of the ones that gets everybody is the virtual shadow map projection mask bits.
[43:14] And that is either the softness of my lights or my SMRT settings. So I'm not really going to have a lot of super soft lights with virtual shadow maps.
[43:22] The light overlaps, of course, still matter here as well. Cashing can help, but I'm not going to rely on caching to solve all of my virtual shadow map performance problems.
[43:32] I am going to use resolution, LOD bias. That's something I can set in my device profile. So maybe I have higher resolution shadows in quality mode, lower resolution shadows in performance mode.
[43:42] Virtual texturing, I'm definitely going to use virtual texturing. Huge benefit to memory. I'm going to be very careful about the r.vt.max uploads per frame and r.vt.max uploads per frame.streaming.
[43:53] The top value is for your runtime virtual texture. And the bottom value is for all of your streaming virtual textures. The top value should be low and the bottom value should be high.
[44:06] We've got a really good article and I'm running out of time, so I'm not going to talk about this too much. But I'm going to think about my stack count, which is the number of unique UV sets in a material that affects my virtual texturing streaming performance.
[44:17] Pipeline state objects, PSOs. I'm going to bundle them or I'm going to pre-cache them or I'm going to do both. But I'm doing something. I have to do something with my PSOs.
[44:27] I'm probably going to be doing a lot of pre-caching. And then when I am testing, I'm going to make sure that I clear my PSO cache so that I can see when I'm running locally whether or not I have an issue with my PSO generation.
[44:40] Time of day, I'm going to skip over homework for this one. Simon is talking about NANDite foliage. Later, I didn't talk about that at all today. And then Jason and John are talking about shader reduction Fortnite tomorrow as well.
[44:55] Speaking of another talk that you're going to go to after this is the talk about user interface. The basic idea here is we got to work, think about our layout costs.
[45:03] I'm not going to have Canvas panels at the root of all of my widgets. I'm going to be careful about my invalidations and I'm going to use UMG ViewModel or MVVM to handle the interop of data between all of my systems.
[45:13] Cody is going to talk about all of this tomorrow at 9am. I'm so sorry about that tomorrow 9am slot. Networking, this is a fun one, right?
[45:20] Maybe I want to have 100,000 players or 100 players running around my large 16km open world blah blah blah blah.
[45:26] Cool thing about networking stuff to talk about today. Iris is production and ready in 5.8, so I'm probably going to make use of that.
[45:33] I'm going to make sure that all of the stuff that is networking is opting into replication rather than opting out.
[45:39] I'm going to control the relevancy either with replication graph or Iris's filters. I'm going to think about the frequency of replication, how often does this value need to be updated.
[45:47] And when I'm testing, I'm going to be testing with replication enabled.
[45:51] And of course budgets. I have to have budgets because the budgets help me identify what I need to optimize, right?
[45:58] And when not to optimize. And I'm going to think about should my budget targets be frames per second? Should it be missed v-sync percentage?
[46:05] Should it be dynamic resolution? Should it be a millisecond value? This is something that I am doing very, very, very early in my project so that I can always go back to that.
[46:14] And that is a lot of decisions and a lot of homework. And that was only a third of this talk.
[46:20] But this one's a little easier for me to rip through. So let's think about how we're monitoring for 60 frames per second, right?
[46:24] It's about guiding users to the right choices and knowing when things deviate.
[46:28] So guiding users to the right choices with things like data validators and asset referencing restrictions and our friend the submit tool.
[46:35] All make sure that the standards that we have set for building our world are being enforced at creation time.
[46:42] Monitoring for 60 frames per second is a really big topic, right? Unreal Insights. Everybody on my project knows how to use Unreal Insights
[46:48] because it means that they can profile themselves and they can determine for themselves how performant their systems are.
[46:54] They're really, really cool. Trace regions, I love them. Trace screenshots help me add a lot of context to the thing.
[46:59] GPU profiler too means I don't have to open a GPU capture tool to figure out how long it took for the base pass shaders to run.
[47:06] World streaming insights breaking news. This came out in 5.8 so that I have a heat map.
[47:11] Oh, somebody said, well, so that I have a heat map of the streaming performance of my world overlaid straight into Unreal Insights.
[47:19] This is really, really super cool. Yeah, clap for world streaming insights.
[47:24] Speaking of cool things that have come online on top of things built on top of the Trace server, Chaos Visual Debugger now has a complexity view.
[47:32] Yeah. So this is really, really cool. And of course, I have the Rewind Debugger at my disposal.
[47:38] Now this one is a fun one. So remember when I talked about automated performance testing being really, really important?
[47:43] I'm going to do it every day. And then there was a part at the end of that slot, that talk where I was like,
[47:48] okay, it's build graph and UAT and Gauntlet test controllers and I'm going to run all these tests on Horde and then how I display those results.
[47:54] Ah, that's up to you. Ha ha. We have it now in Horde, a perf trend dashboard in Horde that you can send all of your data to and it will give you all of the graphs.
[48:06] So now finally we have the full picture of like, I run my automated tests on Horde, it reports the results to Horde.
[48:12] I can say, oh, I'm so excited about this one. This literally a dream come true for me. So shout out to Julian Gamble for helping put that together.
[48:21] So returning to 60 frames per second. This is when I think about view modes of like, okay, I know that this is running really, really slow.
[48:27] And so I've got all these cool view modes that we can talk about later. Substrate material count. There's a bunch of really good ones for that.
[48:33] So I can see how many BSDFs are visible. Generally, the returning 60 frames per second for me is a lot about just returning to best practices, right?
[48:43] So maybe I'm going to have to nativeize my expensive animation blueprint operations. I'm going to be reducing my shading bin count.
[48:49] That might be the big issue. Again, a lot of this is going to come down to profiling, figuring out what the big number is, and then we can talk about making it smaller.
[49:00] Yeah, ultimately returning best practices. And of course, we have maybe we get a little dramatic. We do some input latency reduction tricks.
[49:07] Maybe we do some frame generation, or maybe I made too much game and I have to take out some of my game.
[49:14] And that's kind of a bummer to end on. So generally, what I want you to take away from this is the performance of the Unreal Engine is improving.
[49:23] The tools to do so are improving. We can set ourselves up for success by starting off on the right foot.
[49:30] We have to stay vigilant throughout our entire project, and we will eventually have to get back up on the horse.
[49:36] And finally, you can do it. I know you can do it. Thank you, everybody. Really appreciate your time.
[49:43] I don't have time for questions. Stand that QR code. It'll take you to my link tree. You'll find the article and all the notes at the end of the show.
[49:49] Because I ripped through that real quick. Thank you, everybody, so much. I'll see you out in the hallway.



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
