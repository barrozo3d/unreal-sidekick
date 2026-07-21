---
title: A Frame’s Life: Frame Timing, Synchronization, and Latency in UE | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=dKSHw_8vz3I
author: Unreal Engine
ingested: 2026-07-21
ue_version: "UE 5.8"
tags: [frame-pacing, input-latency, vsync, swapchain, profiling, insights, delta-time, jitter, performance, unreal-fest, advanced]
extraction_status: complete
frames_dir: tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/
frame_count: 14
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# A Frame’s Life: Frame Timing, Synchronization, and Latency in UE | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=dKSHw_8vz3I)
**Author:** Unreal Engine
**Duration:** 52m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, welcome. This is a Frames Live, Frame Timing, Synchronization, and Latency
[0:08] in Unreal Engine. My name is Ari, I work in the Technical Developer Relations team here
[0:13] at Epic Games, and yeah, I make presentations like these so you can make games better. I
[0:22] do want to point one thing out for this presentation is that I'm going to be talking about some
[0:26] stuff that are currently in flight, we are currently working on them, and I hope this
[0:32] video is going to be out of date very quickly, but I have a text version available on the
[0:38] Epic Developer Community that I just posted right now, so right now it's just going to
[0:42] be based on the text on the slides, but give me a couple of weeks and I'll fully fill it
[0:48] in, and as soon as any changes happen to any of the systems that I'm going to be talking
[0:52] about in this presentation, I'll update the test article, so the test article will always
[0:56] be up to date, this video will not. So, a Frames Live, basically from Input to Photon,
[1:04] and this journey, well it has, you know, how we measure it, it has a bunch of names, we
[1:08] can call it Input Latency, System Latency, End-to-End System Latency, Click-to-Forum
[1:13] Latency, Motion-to-Forum Latency, this is all generally talking about the same thing.
[1:19] I'm going to be calling it Input Latency in this presentation, but it has a few different
[1:23] meanings, I'll elaborate a bit later. There's a bunch of things that happen from user Input
[1:29] to Photon, and these boxes are only proportional to how the text fit in there, it's not actually
[1:34] like how long they take, and in this presentation I'm going to be focusing a lot on the latency
[1:39] that we as developers can affect. So, when we are making a frame in Unreal Engine, the
[1:44] Engine needs to do a lot of things to draw a frame, we have the gameplay code, animation,
[1:48] physics, and networks that need to happen, we need to prepare the render scene, call
[1:53] the object and make draw calls, we translate the rendering commands into a specific graphics
[1:57] API like DartX 12, Vulkan Metal, even though they all work, similarly they're different
[2:03] enough that we need to have a translation layer between each of them. And then this graphics
[2:08] API, we queue up GPU work by giving them commands, basically saying, hey, I want this to happen,
[2:15] basically a draw call on GPU, and then this, and then this, and then this. And the GPU basically
[2:20] does them at its own leisure, at its own cadence, we can of course sync to it with fences, and
[2:28] then the GPU does this work, and then we finally call percent on the graphics API to enqueue
[2:32] a Shropchain flip, and when the GPU spins this work, it will do that. So, Shropchain,
[2:39] I want to talk a little bit about that, just so that we're all clear on the foundation.
[2:44] So the game has a surface, almost known as technically a buffer, that it has on the GPU
[2:49] that it draws to this, like you can basically think of it as a texture or canvas that it
[2:53] paints to, and the GPU scans out the buffer to the display, and the buffer that is currently
[2:58] being scanned out, we call it the front buffer. The thing is, we do not draw to a buffer that
[3:03] is actively being scanned out, because then like as it's being scanned out, suddenly
[3:07] objects would just pop in. So we lock it, and then the game has another back buffer,
[3:12] sorry, another buffer that we call the back buffer, that it draws to while the front
[3:15] buffer is being scanned out. So this is basically what we're talking about when we say double
[3:19] buffering. So Unreal games use either double buffering, and that's the default for console
[3:23] and mobile, or it uses triple buffering, which is the default on PC, and of course,
[3:29] you can change those defaults. We can use double buffering on all, or triple buffering
[3:35] on all. And the game can wait until vertical sync or v-sync happens to swap them for a
[3:42] smooth transition, and v-sync is signaled at the end of a frame scanout. So we have
[3:46] the front buffer is being scanned out like this, and then the GPU goes v-sync, and during
[3:51] that v-sync is when we swap the buffers around, and then we're ready to render a scanout
[3:57] frame number two. But we can also swap them out without waiting for v-sync, but that
[4:02] introduces tearing. So we can see here front buffer number two starts getting scanned out,
[4:06] and then we just swap them in the middle of a scanout, and then we get half a frame two
[4:10] and half a frame three. And then as an extra step, it is up to the operating system's compositor
[4:17] whether the buffer gets scanned out directly to display or composite it first. I'll get
[4:23] to that compositor, but I also want to talk a little bit about v-sync. So generally, when
[4:29] you turn off v-sync via r.v-sync equals zero, it does result in a lower input latency, which
[4:33] is why eSports and competitive players do that a lot. They don't like that. The cost is
[4:38] screen tearing, which while if you're moving the mouse fast enough or the controller, it
[4:42] can look like this because you're basically flipping the buffers right while we're scanning
[4:47] out. It also gives us less of an ability to absorb hitches by the pipeline. I have a whole
[4:53] section on that, don't worry. So most console games actually have vertical sync equals one,
[4:59] and also many users, me included, prefer no tearing. It's very like jarring and I don't like how it
[5:04] looks. Because of that, I would recommend that if you're making a game and you're trying to decide
[5:09] should you have v-sync on or off, I would say have it on by default and make it an optional
[5:16] thing that the user can opt out of. Or just have it on and just make your frames. Okay, so v-sync
[5:24] and insights, you can actually turn on r.v-sync information insights to get v-sync markers
[5:30] and insights, and it will show you the flipped frame number and misses, as you can see over
[5:35] there. And this is the number that we're using throughout the entire pipeline, like the game
[5:39] thread, the render thread, RSI thread, they all have this like frame number, this is that frame
[5:43] number. And if you make your v-sync, it will show up there. And if you miss a v-sync, it will show
[5:47] this missed. It's, I don't like the bookmarks, so we actually do have a new feature coming
[5:55] soon. I'm really excited about that. We have a dedicated track for v-sync. And it looks like
[5:59] this super sexy, you see green frames there for the v-syncs that you make, and then oranges, red
[6:06] is for the ones that you miss. I don't know when it's coming, but hopefully soon we have a little
[6:11] bit of refactoring of insights to be able to have arbitrary game frame v-sync tracks like
[6:17] that. And I mentioned the compositor. So it basically does what its name implies, it composites
[6:26] windows together into one graphics buffer before sending it to the display. So for example, you
[6:31] can have a game running, you can have a video player and then a browser all in your computer. And
[6:38] basically what the operating system does is that it paints it all into one texture, one buffer,
[6:42] before scanning it out to the monitor. And compositing is not free, it's work that needs to
[6:48] happen, and it usually takes an extra frame. It's like the v-sync is fired on your game, and then
[6:53] you make it, but then the operating system waits one extra v-sync before sending its own. So it
[6:58] takes at least one frame, usually just one frame. The thing is, if we're running in full screen
[7:03] game, we don't need any compositing because we're the only thing being drawn out. And on windows,
[7:09] the compositor is called the desktop window manager. And consoles do also have a compositor,
[7:16] but you generally don't need to worry about it because most of the time, if nothing is
[7:19] overlaid, it will skip it. So you don't have to worry about it. Consoles is just like, don't
[7:22] worry about it. So, but on windows, I think we really want to skip this compositor. Historically,
[7:31] only exclusive full screen skipped the windows compositor. But fun fact, as on windows 10 and
[7:37] dardex 12, at least, I think it might have been some part of the windows 8, anyways, with the flip
[7:42] model swap chain, which is what Unreal uses, I set default, but it's just like, it just works
[7:46] like that, you can't change it. It will automatically skip the windows compositor if you are running
[7:53] in borderless full screen. But not always, it is automatically activated by windows when it
[7:59] detects that the game covers everything on screen. So it's quite cool. So just, you're running
[8:03] borderless windows, guess what? It's performing just as well as exclusive full screen. Also,
[8:08] it is always activated when you have hardware, multi-plane, plane, yeah, plane, pain, multi-
[8:14] pain. I can't, oh, shit, did I get it wrong? Sorry, I was not. Anyways, supported by the
[8:19] hardware. I think it's multi-plane, plane, not planes. Anyways, even when it's windowed or
[8:25] covered by other windows. And I noticed on my work computer, I have an Nvidia card there,
[8:29] that the overlay support is only on the primary monitor, as set in display settings. So if you're
[8:35] a gamer watching this, and you game on your secondary monitor, stop it. You're getting an extra frame
[8:42] of lag, of input lag on Nvidia, because they put all of their overlays in on the primary monitor.
[8:52] You can check whether, like, because I know it works like that on at least my Nvidia card. I
[8:57] don't know if it works like that on AMD and Intel, but you can just download Present Mon,
[9:01] which is Intel's free tool for checking a lot of things. And there's this custom mode that I'll
[9:06] also to put in Present Mode. Stan will tell you whether it's like which window, or which compositing
[9:11] mode Windows is currently using for your game. But in either of these cases, if the compositor is
[9:19] being skipped because of the full screen thing, or because of the multi-plane thing,
[9:25] you can, like, it's basically performing as well as exclusive full screen. And it's more usable,
[9:32] because you can still all tap out of it, and you can have temporarily
[9:36] composited overlays, like the volume bar, if you click on volume, and then suddenly it goes over.
[9:40] And then if you don't have the multi-plane overlays, then it's going to just temporarily
[9:46] composite and then stop it when it's again the only thing on the screen. So exclusive full screen,
[9:51] actually, fun fact, Windows apps can't really do exclusive full screen anymore, at least the games
[9:57] with the Blip model. Windows is lying to you. It just emulates exclusive full screen by still
[10:03] changing the resolution, which is maybe what you mostly want it, but it still uses borderless
[10:08] full screen. So yeah, and if it's the only thing again on screen, it will skip it. And usually,
[10:14] when you're using non-native resolution, when you're sending a lower resolution to the monitor
[10:19] than its native resolution is, then you're making the monitor do the upskilling. And the monitor
[10:24] upskilling is, it's usually a very cheap and plain and fast spatial upskiller, like bilinear.
[10:29] And when I say spatial upskiller, I mean only using data for the current frame, as opposed to
[10:35] temporal upskiller, which uses many frames. Unreal can actually do better quality fast spatial
[10:43] upskilling on the GPU with fancier algorithms. Then we do it via the secondary upscale.
[10:50] Secondary upscale. So Unreal does have two upscaling stages. This is a graphics from the
[10:56] Witcher demo presentation. So the numbers are actually from it also. I say resolution by the
[11:01] third examples, but it's actually what we used on a Witcher demo. So primary upscale is for the
[11:05] main temporal upscaling, like temporal super resolution and media DLSS and all the other
[11:10] plugins are going to hook into that one. But there's a secondary upscale that I don't think
[11:14] that many people know of. I didn't know of that well when I was researching this for optional
[11:19] spatial upscaling. You can set the method that it uses, the algorithm that it uses,
[11:25] via the r.upscale.quality. You can check the C1 for help, just write it, plan into the console,
[11:30] and it will give you documentation or see the source code. It gives you quite a lot of info
[11:34] for all of the methods it uses. And the cool thing about secondary upscale is that Unreal will draw
[11:41] the UI at native resolution after the secondary upscale. So the UI will look super crisp and nice,
[11:48] even though you just upscaled everything else. It's disabled by default, so I think most games
[11:52] aren't using it, although it does kick in if Windows' DPI scale is more than 100%. But in any
[12:01] case, you can set it with the r.secondaryscreenpercentage.gameviewport.cvar. I think because of this,
[12:13] because the whole native UI, better algorithms does it fast, I think secondary upscale is a
[12:18] better alternative to exclusive fullscreen. So I think that should be a mode. If you're offering
[12:24] only borderless window and exclusive fullscreen, which is not real anyways, if you want the player
[12:32] to play it, if the player wants to play at a lower resolution to make it faster, just use the secondary
[12:37] upskiller, because it's going to be just as fast, but it'll look much better. I say that, but maybe
[12:43] not completely replace exclusive fullscreen, because there is the use case scenario where users have
[12:51] a laptop that doesn't have a great GPU, but it has 4K display, and in that case, because you're
[12:58] running on a 4K buffer, it's going to be memory bound. So there's, except anyways, I told you
[13:04] all the facts, you can decide yourself how you want to do it. So the Unreal pipeline, there is a
[13:09] lot of things we need to do in a single frame. We have the game simulation, rendering operations,
[13:13] RxI and GPU rendering, and they all need to complete before a frame v-sync. But in Unreal,
[13:19] we don't do them linearly like that, we kind of like parallelize them, and they intersect a little
[13:23] bit as they're sending data over. When we do things like this, we can do something really cool.
[13:27] We can actually spend like more, we can more than double the time we spent on each stage,
[13:32] and if we zoom out a little bit, even though we're taking like more than two frames to construct
[13:39] our entire frame, because they're all running on threads, we can parallelize them like that.
[13:44] So each is taking more than one frame's time to complete, but they're still running at your target
[13:50] refresh rate like 60 frames per second, or 120 or 5000, whatever, again. But
[13:58] what happens if you pause the game, and suddenly the gameplay code isn't running,
[14:02] and the game thread just like takes almost no time, and it just does this start racing ahead like that?
[14:08] We need breaking in the pipeline. So each part of the pipeline needs to be able to break to not run too
[14:12] far ahead of the rest, because we don't want the game thread to be at frame like 1000 while
[14:17] we're still rendering frame number one. So let's start with the GPU and work our way backwards to the game thread.
[14:24] So the GPU, as one of the last things it does, it writes to the swap chain's back buffer, so it needs
[14:31] the back buffer to be available, and it actually does it in the last post-process pass.
[14:36] And if it's like saying, I want to write to the back buffer now, because I'm going to show it to the user soon,
[14:40] and if all the back buffers are full, it just goes like, well, I'll wait, and it stalls there.
[14:46] We don't really have a marker for that on PC, so if it happens, if you're v-sync bound, we don't say,
[14:51] we're waiting on v-sync, it just looks like a bubble. It looks like the, yeah, it will just say nothing.
[14:59] Sorry about that. I told the team, I want a marker there. We want a marker there.
[15:03] I told the team, I want a marker there. We have it actually on some platforms, but NDA stuff.
[15:11] Like I said, the last post-process pass is the one that writes to the back buffer,
[15:14] and whichever pass that you see in the GPU bubble, like for example here, I turned on RG events,
[15:20] it's just the previous pass. It actually finished already, and it's just waiting on the back buffer,
[15:25] so here it's lying. It's saying, I adaptation buffer took 12.72 milliseconds.
[15:31] It's been 12.72 milliseconds since we started it. We did finish it, but actually over there at the end,
[15:38] that's where you can see that we were waiting on the tone mapper was the last stage in my case,
[15:45] that's what we were waiting on. It's only in the tone, like once we actually are doing something,
[15:50] then we pop the previous thing we were doing, so it's a little bit, you just need to know it. Sorry.
[15:54] For RGi thread, it waits for the previous GPU frame to finish. It's called sinkpoint underscore
[16:04] wait, fence and insights, so you can see there the GPU frame just ended, and then it goes and
[16:10] signals the RGi interrupt thread, which is basically the threat that handles communication
[16:14] between the GPU and the CPU, and then when that is fully handled, it will end the fence. So this
[16:20] is how you see why is it waiting in insights. I think it would be cool if we just click it and
[16:25] we show these arrows automatically. Maybe I'll look into it next year or five times.
[16:30] But the RGi thread also waits on the graphics API when the swap chain fills up. For example,
[16:34] like let's say there's nothing in the swap chain. You can start sending commands to the swap chain
[16:40] through the graphics API. Sorry. Yeah. Like, hey, do this, this, this, this, this, this, this,
[16:45] then present, and then do this, this, this, this, you can send all of these before it even has
[16:49] started working on the first draw call. So you can start queuing up work. But as soon as you call
[16:54] present more often than we have backbuffers available, the graphics API just says, stop,
[17:02] let's not get ahead of ourselves. So Dyronex, for example, will block during present when no
[17:07] backbuffers are available. And you can see there actually that as soon as v-sync is done, Dyronex
[17:13] goes like, ah, we have one available now. And it resumes. Render thread. So the render thread
[17:20] waits for the previous GPU frames, hardware occlusion queries. This is shown as process
[17:27] visibility tasks on the render thread. And it's also shown as sync point weight GPU occlusion
[17:33] on the worker thread. And if you look really close, you can see that it says GPU bound underscore
[17:38] waiting for GPU for occlusion queries on score, see GPU track. Because people were seeing this
[17:45] and they were saying, why is occlusion taking 15.5 milliseconds? That's a lot of work. Is occlusion
[17:54] that slow? It's waiting. It's not doing anything. It's just waiting for the GPU to finish its
[18:00] previous frame. So it's not actual work. Actually, these hardware occlusion queries are also
[18:06] only for non-nanite messages. So if your game is almost completely nanite, and you don't want this
[18:10] to show up in your traces, you can turn them off with R.allow occlusion queries. Again, this is
[18:16] only for non-nanite. Nanite does have occlusion queries, but it's only on the GPU. It doesn't
[18:20] need to make a round trip. But profile, like, don't turn them off. And then suddenly everything is
[18:26] slow. Also, can I like take into account, like I mentioned, it's not busy. It's just waiting. And if
[18:30] you like remove this weight, because you're like, I don't want it to be slow, guess what? It's just
[18:33] going to wait somewhere else because of the frame pacing, because of all the breaks. So let's see a
[18:37] closer look of how hardware occlusion queries looks on the profiler. So we have on the GPU,
[18:44] you can see the begin occlusion test. And then we get a bubble, means the GPU isn't working. We're
[18:49] just sending the data now. And it's a lot of data. So we're sending it there to the RTI Interrupt
[18:54] thread. When it's done, it closes the fence. It handles the data on worker threads. And then it
[19:06] tells the RTI, like, how you can stop waiting now. And over subscription, it's a lot of people
[19:14] have been asking about that. And I just want to clarify what it is, how it works. So
[19:20] Unreal Engine, usually when you make a game, start a game, it will allocate as many threads as there
[19:25] are hardware threads in the system. So like, basically, the CPU cores, and then maybe times two
[19:30] if you have hyper threading or equivalent. And sometimes when a worker thread needs to wait for
[19:35] something, it can allow over subscription. And over subscription is basically a really neat way to
[19:40] tell the engine, hey, I am a thread that basically has its own CPU core allocated to myself, but
[19:48] I'm just going to be waiting for a while. So we're just wasting one of the CPU cores. So how about
[19:53] you just wake up a temporary standby thread and do some work there so we are utilizing
[19:58] all the core. So this basically keeps all the cores busy, even when a worker thread
[20:02] idles while waiting for something. So if you see in your insights that this is over subscription,
[20:07] and you think, what is busy taking up my CPU time? It's not. It's just waiting. It's just a fence.
[20:13] It's a fence, a fence. Okay. And if you disable them because you're like, I don't want this
[20:19] wait, this over subscription shit in my pipeline, then the render thread only waits for new work.
[20:25] It's basically start for work from the game thread. And game thread is the last piece of the puzzle.
[20:32] So the game thread always waits for the start of the previous frames render thread.
[20:38] It also is getting a little complicated now. It also waits for the two frames ago RSI thread.
[20:45] And this fence is to prevent the game and the rented thread from raising ahead together.
[20:49] So it's collecting it to the rest of all the like breaking stuff. And you usually won't hit this fence.
[20:53] You will never see it because by default you have the hard to occlusion queries. But everything
[21:00] that I just described, all of these breaking stuff, this is what Arnold does by default.
[21:04] This is R.game thread sync type zero. Let's visualize it. Because I don't know about you,
[21:14] but this was a lot of complicated words. And it's okay if you cannot disconnect it for a little
[21:18] while because I did also. So let's visualize it. This was the last frame. We can start the next
[21:25] game thread frame already because the previous rendering operations frame has already started.
[21:31] We can start it as soon as the rendering operations start. So we can already start it.
[21:35] We want to start doing the rendering operations, but we can't yet. We barely start it, but we have
[21:40] to wait for the previous GPU frames, hardware occlusion queries. So that is what it's actually
[21:47] waiting for when you see that old subscription thing. And if it's waiting too long and you're
[21:51] like missing dropping frames, like that is because your previous CPU frame was just taking too long.
[21:56] Then it does the RSI thread and that frame actually, it's basically done with all this work.
[22:04] And then it waits until the end of the GPU frame just so that the next RSI doesn't start immediately.
[22:10] And then do the GPU rendering. Okay, let's do one more frame. It cannot start yet because the blue,
[22:16] the rendering operation from the previous frame hasn't started yet. So we need to wait for that.
[22:20] And now we can start the game simulation along with the rendering operations. You can see
[22:26] usually when you are running insights and you see game thread take something and then it says
[22:30] like waiting for tasks, that's it. This is it. Then again, it waits for hardware occlusion queries.
[22:36] You can see there's a big wait there because the previous frame took quite a long time.
[22:41] And then it finishes the rest. From the start of when the game simulation frame starts and to the
[22:51] v-sync of that frame, that is what we in Unreal language call input latency. It's basically when
[22:59] we consume the input to when we flip the frame. So I want to talk about input latency now. We
[23:07] have our own description for it in Unreal. So generally when we're talking about input latency,
[23:11] it's the time for when the user actually pressed an input or like did some motion with VR to when
[23:16] it was actually when they hit the eyeballs. But in Unreal, the input stat over there when you
[23:22] have stat unit, it's actually the time the input was sampled. Not when it was pressed, not when the
[23:28] operating system sent it to Unreal. It's at the start of the game frame to when that frame's back
[23:34] buffer was flipped to the front. For example, here, if the user inputted something during the previous
[23:40] frame game simulation that wasn't consumed by that frame, we don't count it. Input latency is still
[23:46] from the start of the orange frame. So the input latency, you know what it is. So what it isn't
[23:53] is that it isn't the hardware latency. It's not the operating system. It's not the delay if the
[23:57] user presses it before the consuming of the game frame. It's not the composite delay. It's not the
[24:03] scanner through the HDMI cable. It's not the display's processing time or its own scan out
[24:09] or the pixel's gray to gray. I mentioned hits resiliency. Let me describe what it is. It's
[24:16] basically the engine's ability to absorb hits. And it does cost greater input latency. So it's a
[24:24] give and take. And also the game needs to be under frame time budget so we can actually catch up again
[24:28] and fill the pipeline again. So I'm going to give you an example because that was a lot of words.
[24:33] And I'm a visual creature and I hope you are too. Let's say we have a full pipeline. A full
[24:39] pipeline in Unreal looks like this. Six of the frames are in the engine. Two of the frames are
[24:43] basically in the hardware like on the way to the monitor and on the monitor. So let's say frame number
[24:48] one, the first frame that we simulated is currently being drawn on screen. So display scan out.
[24:53] Frame number two, it's being sent from the GPU scan out engine through the wire. It's being sent
[24:58] now. Frames three and four are just waiting in the swap chain's back buffer. Frame number five,
[25:06] it's almost finished on the GPU but we're waiting for v-sync because we don't have a back buffer
[25:09] and we're waiting for it. It's the bubble that I told you about. Frame number six is almost finished
[25:14] on the RSI thread but it's stalled on the graphics API's percent call, the v-sync that I told you
[25:20] like Dardex. The render thread is waiting on the hardware occlusion queries from the previous
[25:26] CPU frame and frame number eight, game thread is done. It is waiting on the previous render thread
[25:32] frame before starting next frame. This is what a full pipeline in Unreal looks like. Six of the
[25:36] frames are like the real frames, the two are kind of like it's out of our hands and we cannot start
[25:41] frame number nine yet. Let's say now frame number one is done. We're doing frame number two, v-sync
[25:47] happens and everything moves up a little bit. However, frame number nine is taking a little bit
[25:52] of time. We actually go over frame time budget. Actually, let's say we go over two frames frame
[25:58] time budget. Actually, let's say we go over three frames frame time budget. But in this hypothetical
[26:05] scenario, our frames are fast enough that are able to catch up because like still there's two full
[26:11] frames in the swap chain like we have like over 100 milliseconds there to catch up. So we finally
[26:16] finished game thread number nine and because we can basically skip the back buffers because like we
[26:21] just take the first one that's available, we're able to kind of catch up and notice that the user
[26:26] at no time missed the frame. So we had a hit, but it wasn't a real hit because we didn't drop a
[26:33] single frame. The engine kind of like, like stutter a little bit, but we managed to catch up before
[26:38] anyone could notice. So you can reduce input latency by sacrificing some hits resiliency.
[26:46] This is great if you're able to keep consistently on the frame budget and you know you don't need
[26:49] that hits resiliency. So now I want to talk about reducing input latency, which should be very
[26:54] important to us as developers because you know sometimes we have action games and we want the
[26:58] input latency to be really low. So of course the first thing we can do is just run at higher frame
[27:02] rate. Super simple because the max number of frames in the pipeline stays consistent across
[27:08] frame rates. Like I mentioned six frames in the engine. So the frame time is not, that one is
[27:15] variable. So for example if you have six frames in the pipeline at 30 frames per second that's 200
[27:20] milliseconds. So if you're running on like you know limited hardware like mobile or a handheld
[27:25] and you're running at 30 frames per second with tg sync type zero, it's 200 milliseconds, quite a
[27:31] lot of input latency. But if you're running 60 frames per second, 100 milliseconds of input
[27:36] latency. Let's say you can even run your game at 120 frames per second, 50 milliseconds. Still with
[27:43] the full pipeline, still maximum hits resiliency, still maximum parallelism. I said it was simple,
[27:50] I didn't say it was easy. You can also throttle the game threat. So you can see the input latency
[28:00] there is quite long and we want to shorten it, but wouldn't it be cool if we could just like move
[28:05] when the game simulation happens? So we're not doing like we're not doing less work,
[28:10] we're just moving when it starts to cut the input latency in half. That's kind of cool.
[28:15] It would be even better if we can make it so that just before the v-sync we can kind of start the
[28:22] work so that it would finish just before it. So this would be basically perfect frame pacing
[28:26] because we start the work so that by the time the gp rendering ends the v-sync happens. This is the
[28:33] least amount of input latency you can get in Unreal. And we would be able to achieve this by
[28:39] throttling the game threat. So there's a way to do it in Unreal, we have a fixed way of throttling it.
[28:45] You can use game threat sync type 2 to kick off the game threat at a fixed time before v-sync.
[28:53] So by default it's always two frames, but then you also get the sync slack milliseconds, which
[28:58] defaults to 10 milliseconds and is maximum one frame. So if you're running 60 seconds you can
[29:04] put it higher than 16.66 milliseconds, meaning that you can have the throttle between two and
[29:12] three frames before the target v-sync. You decide the frame budget, you need to keep to it. So this
[29:21] gives you very consistent delta time, minimal input lag, no hits resiliency, but it's okay because
[29:25] your game is not hitting, right? You should use this for consoles where the hardware is fixed because
[29:32] you need to decide the frame time. So it's currently available on ps4 and 5, xbox one in series and
[29:37] swtich 1 and 2. And you kind of want to do it only when you know what hardware it's actually running on
[29:45] because it's harder to keep to a fixed budget or variable hardware, like for example on pcm mobile
[29:50] where it's like you don't know what you're getting. So we don't support it also because we just don't
[29:53] have those timings. And this is what it looks like. You have two frames that you need to wait at least
[29:59] and then by default, sinks like milliseconds is 10. But so you can see like, oh, there's a little bit
[30:07] of spare time there because this is what is set, we have a little bit of buffer. But if you can't
[30:11] keep to your frame time, if it goes like this, just a little bit over, guess what? You dropped a frame.
[30:15] So you really need to keep your game under budget. There's also an adaptive way to throttle.
[30:24] We have third party solutions that allow you to implement adaptive or dynamic frame thralling on
[30:28] pc. Those are nvidia reflex, amd anti lag 2 and intel xe low latency, otherwise known as intel xe ll,
[30:37] or maybe they call it intel excel, probably not. And they dynamically adjust the throttle based on
[30:42] previous frames. It's a bit of a headache having to implement three fdk's just to make sure your
[30:47] game runs like with lowest input latency on PCs. Your users are going to love it if you can do that.
[30:56] I was considering if I should put this slide in or even not. You can if you want to starve the
[31:01] pipeline. So you can set t.maxfps to a value slightly lower than the displays nvidia refresh rate.
[31:06] For example, if the display runs at 60 and you put maxfps to 59 and 58, you're basically simulating
[31:11] as if your game was underperforming. So this completely drains the pipeline because your games
[31:16] aren't running fast enough to fill it up. Zero hits resiliency because, again, lowest input latency.
[31:22] But the bad thing about it is that it drops a frame or two every second because you're basically
[31:26] telling the game thread like, wait a little, okay, now do it. And then again, I don't have enough time.
[31:30] Ah, the drop the frame. So unless the user's variable refresh rate, then they can kind of like
[31:37] make a little bit of delay there. So the gamers that are watching this presentation,
[31:45] you guys can actually do this already because there are some games that offer unrounded maxfps
[31:50] settings in their settings games. So they can say like, oh, maxfps is 58, 57, whatever. And this
[31:57] will actually starve the pipeline and then it'll get the lowest input latency. But us game developers
[32:02] shouldn't really do it because it is a workaround and a solution. Very unprofessional, don't do it.
[32:07] Rather just get your frame pacing right. But yeah, I've seen esports players or just people
[32:16] that really want low input latency in their single player games to just download the mod that
[32:21] injects the C-var into their game. So like, you know, like I said, I wouldn't recommend this,
[32:26] but also I'm not your mother. So you know you can do it now. I would actually recommend just
[32:30] shortening the pipeline. So if you still want to retain some hits resiliency, but just shorten
[32:34] the pipeline a bit, you can use the r.oneframe thread like C-var. By default, it's one and that's
[32:40] that the render thread can lag behind the game thread by one frame. And that's when they can run
[32:44] both at the same time. Really nice max and parallelism. If you turn it off, the game thread needs to
[32:49] wait until the current frame is done before continuing. It's less parallelism because now
[32:54] the game thread and render thread can't overlap. I'll show you what it looks like.
[32:59] Here we have the situation from before. And this is the default r.oneframe thread equals one.
[33:04] Let's turn it off to zero. And this is what happens. Basically, game simulation needs to now
[33:09] wait for the rendering operations. So this is how it was before we just push it. Sorry, game thread
[33:15] and rendering thread cannot run at the same time. The bad thing about that is we're basically losing
[33:20] an entire core because two of the threads are just they're never running at the same time. So like,
[33:25] one of the core and the hardware is just gonna not do anything. So maybe if if you know this,
[33:29] you can just like there's a you can override how many worker threads it spawns and add one more.
[33:34] I don't know. Anyways, you can even shorten the pipeline even more with game thread sync type equals
[33:41] one. So now this waits for the previous RSI RSI thread frame instead of the two from before.
[33:52] Even less impalency, even less parallelism and even less hitchosiliency. This sounds really
[33:57] so I'll show it. I'll show it. Don't worry. So instead of waiting for the rendering operations,
[34:02] we just wait a little bit longer for RSI for the previous frames are outside. So it went from this,
[34:09] which is like, ah, we have like, basically those two thirds can run at the same time. And now we
[34:14] have like basically like almost three frames that can't run at the same time. But we push the game
[34:21] simulation thread out even more. I don't want to say sorry. This is not, this is not nice,
[34:31] not proper, like shouldn't it just be easy. We do have some future plans. We are reworking frame
[34:37] pissing and Unreal Engine. Hopefully it should be out soon. The plan is for a new model with
[34:42] adaptive frame thralling with adjustable targets. So it works a little bit more like those PC methods
[34:47] like the Nvidia AMD until things what they are doing, but just hardware agnostic and like also
[34:53] not on PC like on everything. So this would give you still shortest impalency, but maximum parallelism
[35:00] and consistent delta time. And this is what it would look like, will look like once it's ready.
[35:06] You set the target slack over there. That's the only kind of thing you have control over. But
[35:10] otherwise, everything else is adaptive. So we base it on previous frames. So you say, I want to have
[35:15] in this case, five to seven milliseconds that I want to have as like a target slack or target buffer
[35:23] because I know that the frames can vary a bit. So I want to not drop a frame if it goes over it.
[35:28] And then if you have enough work that it goes a little bit over that, next frame, the adaptive
[35:34] system will just increase the time a little bit. So we just want this to be always for everything
[35:40] and the default target slack to just be like, so you don't have to worry about it.
[35:44] But so if you're watching this from the future and we already have this like lucky you good for you
[35:49] for the rest of you. But this also gives us maximum parallelism because we can start off the next
[35:57] gain threat frame like that. Yeah. So I talked a little bit about variable refresh rate.
[36:08] Also called adaptive refresh rate, freezing, G sync.
[36:13] Used to be vendor specific. So that's why we have all these names. But now it's vendor agnostic.
[36:17] It's part of HDMI standard since 2.1. So if you're buying a monitor and you're wondering which one
[36:23] should I get, it's all the same. Well, sorry, don't sue me vendors because of course, they do their
[36:31] own. There's extra stuff now. Okay, lawyers will get off my back now. No, no, they do extra, what
[36:39] call it like mounting for it's like, oh, this monitor is great. Okay, so variable refresh rate
[36:44] only helps when your games frames per second can't keep up with the monitor's native refresh rate
[36:48] because it's basically works that so that instead of you just barely dropping a frame like a certain
[36:52] graph before the GPU can just delay the start of the next frame. So if it doesn't have a frame yet,
[36:57] it's like, I'll wait a little bit longer. Oh, no, I got it. Okay, it's like almost imperceivable to
[37:03] the user because we didn't drop the whole frame. So it's just a little bit extra.
[37:08] You can only hold the frame for a limited time though. So like, I think nowadays they can
[37:11] like most triple the like they can, if one frame is 16.6 milliseconds, it can wait like two extra.
[37:19] It varies per monitor. Don't rely on it. Anyways, but if we run out of time, the GPU just resends
[37:25] the previous frame. So now as developers, do you know what you need to do in Unreal or on a PC
[37:30] to enable VRR for your game? Trick question. Just turn on Vsync. Everything else is handled by the
[37:38] user's hardware and also have a little bit crappy performing game so that VRR kicks into save your
[37:43] ass. Okay, measuring. I want to talk a little bit about the numbers inside of Unreal when you do
[37:50] stat unit and stat FPS. The frame time, it's a little bit misunderstood. Some people think it's
[37:56] like the how long the entire frame took stuff like that. No, no, it's literally the wall clock time
[38:02] between the start of game thread frames. So if game thread frame number two, time and game thread
[38:08] number three time and it just minuses them and that's that's the frame. So it's only on the game
[38:14] thread game, the red one underneath that. It's the same time minus idle time. That's the difference
[38:22] between those two. Draw is the same just for the draw thread and also swap 10% is included in
[38:27] the idle time. The R, H, I, T, same GPU. It's just the time the GPU spent doing actual work. So we
[38:34] have a union between all overlapping work basically like the time that the GPU spent being busy.
[38:40] So if you have bubbles in your GPU, it actually doesn't count that, which can be
[38:44] confusing because sometimes like it's the start of the GPU time and the end of the
[38:51] GPU time might be longer than what the actual GPU time says because the CPU just like wasn't
[38:56] sending the data fast enough. Input, the yellow one, it's people think, oh no, my game is not
[39:03] performing well. Like don't worry. Like this is literally just the like when it was consumed to
[39:07] when it was displayed to the user. So it's a bit different from all the other ones. Take into account
[39:12] that when you take a screenshot like this off the frame, these are not the numbers that made up
[39:17] the currently rendered frame. It is the last number from each phase. So if you are rendering
[39:24] frame number one, then it will probably be like the GPU time for that frame. But if a CPU frame
[39:29] is already on frame number four or five, even it will be like that frame's time. So it's kind of
[39:34] like just the last stage of each pipeline. Also, it's not the real numbers. We do smooth them a
[39:40] bit with an exponential moving average. So we always like multiply it by 0.1. And 0.9 is all
[39:49] the previous values to reduce theaters because otherwise they just jump all over the place.
[39:55] But you notice maybe because I have both data FPS and stat units, those two numbers
[39:59] there on top, there's this number there that says 16.50 and it's a little bit different than the
[40:04] frame time which says 16.61. Why is that different? I checked it. It uses a 0.75 smoothing factor
[40:12] instead of 0.9. And the reason, sorry, no reason. It's just old code. I noticed and I was like,
[40:19] that's stupid. So I fixed it in 5.8. So now in 5.8, my new runs, stat, FPS, stat, unit, those two
[40:24] numbers are going to be the same number. Cool. Okay. But as developers, we see a lot of numbers.
[40:29] We see all these numbers. The gamers, they don't see any of these numbers. Now it's a good one.
[40:34] They see only how many v-syncs your game made per second.
[40:42] So the third-party tools, that's what they count. Nvidia app overlay, Windows game bar,
[40:46] Steam overlay, they count how many v-syncs. And that's your frame per second. Also,
[40:51] Presentmon does have a custom view that has the same FPS display. It does default. If you have
[40:56] the basic view of Presentmon, it defaults to counting FPS according to the calls to present,
[41:02] but that's kind of like first in, first out queue to the GPU and it doesn't take into account the
[41:09] shocktank slack. So it's not exactly the frames that are being presented to the user, but I guess
[41:14] it makes sense that they would default to that because the app is literally called PresentMonitor.
[41:19] But just know. And also, digital foundry, they count frames using their own in-house tool called
[41:25] FPS GUI. They call it guy. It also works for consoles, which is the only one that does. And
[41:31] it kind of uses delta between frames to know when a new one has been rendered.
[41:35] We don't have a v-sync counter in Unreal. Of course, you can just use one of these solutions. So
[41:38] you're not really seeing the same FPS number as the users are. We want it, but we need to do some
[41:42] foundational work first. We need to get the flip timing, tracking on all platforms. And Dyrodex
[41:49] kind of like, I think we just kind of got it there. Anyways, we're working on it. It's going to be
[41:53] one of the timers eventually. So if you're watching this video and you're like, was it in yet? Check
[41:58] the text, Ergo. Might have been updated. I'll keep it at the top to say what has been changed.
[42:02] Again, Delta Time. Unreal uses a Delta Time property. And I want to explain a little bit.
[42:09] Delta Time is the amount of time to advance physics, sequences, animations,
[42:13] particles, camera moon, basically the entire gameplay for that frame. And the current frame's
[42:18] Delta Time is literally the last frame's frame time. If we get a hitch, then the next frame's
[42:28] increases. And this is good. This is fine. Because it actually helps the game catch up in game time.
[42:33] It basically prevents the game from getting out of sync with time-based system like audio. So if
[42:38] you have an audio-based game and you have a hitch, you don't want the Delta Time to be fixed, and
[42:44] then suddenly they're drifting apart. So knowing that, we know that Delta Time is variable,
[42:51] is one frame behind, and it adds up to match the total game time.
[42:55] Now I want to talk about something hotly debated. Not just Unreal, but in the game history, Jitter.
[43:04] You might know it as animation error or microstutter. I prefer Jitter. This happens when
[43:10] the simulated Delta Time that you're simulating every game thread is different from the time
[43:14] actually between displayed frames. Because the time between the displayed render frame's static,
[43:20] you know what's being showed to the user, I'm going to say a VRR, you can know that.
[43:24] So the Delta Time value for the current frame, however, is variable, especially if you just
[43:29] had a hitch. So this can cause a mismatch between the simulated time and the time between displayed
[43:34] frames, which means that the camera moment gets simulated more than it was actually like
[43:38] displayed to the user, and then the camera moment and animations feel stuttery.
[43:43] This is Jitter. This is what it is. So to understand Jitter is better, I need to
[43:49] talk about the anatomy of a hitch. And a hitch actually has three effects on frame pacing.
[43:54] First, we have the dropped frames. Basically, the last frame stays on screen a little longer,
[43:59] because we're not sending in new frames, and it just looks like the game's frozen to the user.
[44:04] Then we have the recovery. I don't think it's the official name, but that's what I'm calling it.
[44:08] Where the next frame speeds up simulation by applying a large Delta Time. Like I mentioned,
[44:14] it's equal to the last frame's frame time. And it basically looks like the game was running
[44:18] while the screen was frozen because of this. It's like if the user just closed their eyes
[44:21] and opened it and it kept running. Catches up to all this. It's like, audio, we actually want this.
[44:26] Lastly, I don't see many people talking about this part, maybe because Unreal uses the whole
[44:32] full pipeline thing, but we need to refill the pipeline again, because it emptied. And this
[44:38] only happens when you're not throttling the game thread and not exceeding frame budgets, or like
[44:41] only when you have the full pipeline and relying on its resiliency. So basically what happens now
[44:46] is that the next frames, they run shorter, they're quicker, because there's nothing breaking them.
[44:50] So they have a breaking essence slowing them down. They're not breaking. And that means they have
[44:55] shorter Delta Time. And so this is a hitch. And a jitter is different, because the pipeline basically
[45:04] absorbs the hitch. We don't have any dropped frames. It's good. User got all the frames. But
[45:09] we still get the Delta Time fluctuating because of the recovery and then the refilling of the
[45:14] pipeline. And this is what it looks like. This is Delta Time per frame. And we can see it when
[45:20] it gets a hitch. We get a big Delta Time. And then we get some shorter frames as we're refilling the
[45:25] pipeline. I want to show you a visualization of this. I've seen some presentations that are like
[45:35] they're talking about it by showing the camera dittering and they're showing an animation dittering
[45:39] like I saw Digital Foundry in the game. They're like, look, the animation dittering. I'm like,
[45:44] I can't really see it. Honestly, maybe I'm old or maybe the compression of the animation of the
[45:48] videos and like that. And also the camera is like, I really want to see it, but I just can't.
[45:52] So I made a really contrived example. Still in Unreal. It's a real example that shows us off
[45:58] in a more engineering way. I have a spinning wheel. It is split into 60 sections and it runs one
[46:05] circle per second. So it should move one sixtieth of a frame, meaning that all the lines should always
[46:13] be aligned. So if the lines aren't aligned, if they move like this, that's visualizing ditter.
[46:20] I thought that was a clever solution. And like I said, this is actually running in Unreal. It
[46:24] just turned on awful lot of systems. This is the most extreme I could make it. This is the most
[46:28] extreme version of hits resiliency because I added as much of a hits I could get away with.
[46:36] 90, 90 milliseconds. Not a single frame dropped because the frames were fast enough to catch up.
[46:42] So it's there in the lower right corner. However, I know that online this is probably going to be
[46:48] 30 frames per second. So let's slow it down. You can see there it makes a little jump.
[46:54] And you know what? Let's slow it down even more. Let's zoom in. Let's label it.
[47:00] Here we can see we have a bunch of normal frames where it like rotates one sixtieth.
[47:06] And then we get the absorbed hits where we got a huge delta time because we had the previous
[47:13] frame lagging that long. And then we have super short frames. This is by the way exaggerated.
[47:18] Well, I mean still real. But this is a very contrived example where it's refilling the pipeline.
[47:24] This, even though it's the most extreme you'll ever see it, this is what is happening when your
[47:30] game is deiterring. The animation speed up, slow down a little bit, and it just looks horrible to
[47:36] the user. So it's like we want this ability of the engine in the pipeline to be able to absorb
[47:43] by hits. But wouldn't it be nice if we could do it cleanly? So what can we do? Can we fix the delta
[47:49] time? Well, because of variable refresh rate, the display's refresh rate is not always fixed.
[47:56] Also, this is something I learned. This is fun. Monitors don't usually have round numbers as
[48:02] the native refresh rate. You think your monitor is 60 frames per second? You might need to guess
[48:06] again. My work monitor is 59.95 frames per second. And I went to a database of a lot of models and
[48:18] turns out out of like almost 100,000 of them, less than a third of all monitors there have
[48:23] a native round number. They're all slightly off. And fun fact about Unreal, if you ask,
[48:27] what's my native refresh rate? It says 60 because it only returns as an integer. So my monitor would
[48:36] actually slightly drift the game time half a second every 10 minutes. So, you know, be aware of that.
[48:43] Also, because of audio, video, and desynchronization, for example, if the game hits us,
[48:47] the audio disk keeps playing, the game pauses and then continues because it didn't compensate for the
[48:52] delta time. So what else can we do? Well, I hate pointing out a problem and then just saying,
[48:59] yeah, there's nothing you can do. I made a plugin called delta time smoother that is specifically
[49:04] for this. So it's called delta time smoother plugin. It's smooth delta time for games that don't use
[49:08] game thread throttling. You can download it right there. It's available on GitHub right now. Don't
[49:12] worry. I'll leave this cure code up for a little while. So it has three modes. Don't worry, the
[49:16] cure code is still up there. It has hits absorption mode where for smaller hedges or jitters that can
[49:22] be absorbed by the pipeline. It basically makes it so that a longer delta times have their depth
[49:26] paid by the only the newer shorter delta times we don't average out immediately because then it
[49:31] would raise a little bit. It keeps them completely flat. And in my example that I showed before,
[49:34] the spinning wheel, it completely smooths it out 90 millisecond hits un-norsable.
[49:42] But then it has hits mitigation mode. This is for medium sized hits that can't be
[49:46] absorbed but can be smoothed out. You set the milliseconds come by the way yourself. I don't
[49:49] know what those values are for your game. And that just immediately averages out all the delta
[49:53] times in the queue, which means that matter dropped a few frames. But then instead of having
[49:58] the recovery like that, we just run a little bit faster, which shouldn't be perceivable by the user.
[50:04] And lastly, we have hits pass through mode because sometimes if you get a big hit that's up to 100
[50:10] milliseconds, 200 milliseconds, 300 milliseconds, and if we try to average it out, it's going to run
[50:15] comically fast. No, we just let that go through and hit sorry. But we'll still smooth out the
[50:23] refilling. The reason why I didn't make this as a native engine plugin was because this is
[50:32] the temporary band date until we get the new frame pacing in Unreal, which I think every studio should
[50:36] be using if they can. So takeaways, we're running a little bit over time, but I'm just going to
[50:42] wrap everything up now. So first, go for lowest input latency. Remember, you will not get any hits
[50:46] resiliency. You need to keep all frames under the time budget or you will drop frames. Luckily,
[50:51] we're all professionals here and we don't have any hits in our games. Use the new frame pacing mode
[50:57] once it's out, hopefully very soon. Not yet as of Unreal 5.8. Until then, on consoles, use GTSync
[51:05] Type 2 for best frame pacing, use the sync slack per platform to adjust it. For PC games, use the
[51:12] Nvidia reflex, empty until like 2, until like low latency. It's basically doing the same thing that
[51:16] our new frame pacing will do for mobile and other. I'm sorry. There's no good option. You can use
[51:21] GTSync Type 1, but you lose out in the parallelism. It's just bad. Otherwise, if you need the hits
[51:27] resiliency, then sure, go ahead, use GTSync Type 0 if you absolutely have to. It's the most input
[51:32] lag, but you can just absorb hits. It's quite nice. Remember, higher frame rate reduces input
[51:38] lag even more. And lastly, optionally, pair it with the Delta Time smoother plug-in to reduce
[51:43] theater. That's the end of the presentation. Remember, you can scan this code and the text
[51:47] article will be there before you clap. I want to take a selfie with you all. So I'm going to say
[51:52] entry to one. All of you will yell hi from Chicago. Can we get the house lights a little brighter so
[51:59] I can see this lovely audience? Okay, so let's practice it. Three, two, one. I must say I've had
[52:10] better ones. I collect them. I do this at every Unreal Fest. So I want way more. I want to see
[52:17] waving and I want to see your mouth like gaping up. Okay, everyone ready this time?
[52:23] In three, two, one. That's what I'm talking about. Thank you so much.
[52:32] Have a great Unreal Fest. Thank you.



---

## Captured Frames

- [1:30] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_000.jpg
- [3:20] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_001.jpg
- [6:00] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_002.jpg
- [11:00] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_003.jpg
- [16:05] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_004.jpg
- [21:30] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_005.jpg
- [24:45] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_006.jpg
- [28:10] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_007.jpg
- [30:00] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_008.jpg
- [35:10] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_009.jpg
- [38:05] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_010.jpg
- [46:15] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_011.jpg
- [47:10] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_012.jpg
- [49:15] tutorials/frames/a-frames-life-frame-timing-synchronization-and-latency-in-ue-unreal-fest-chicago/frame_013.jpg

---

## Structured Notes

### Core Technique
Deep anatomy of Unreal's frame pipeline — from input sampling to photon — covering swapchain/v-sync mechanics, how each pipeline stage brakes (GTSyncType), the input-latency vs hitch-resiliency tradeoff, delta-time jitter, and every practical lever for reducing input latency (`GTSyncType 2`, Reflex/Anti-Lag 2/XeLL, `r.OneFrameThreadLag`, secondary upscale, VRR). By Ari (Epic Technical Developer Relations), Unreal Fest Chicago 2026; the companion Epic Developer Community text article is the always-current version.

### Summary
52-minute conference talk explaining what actually happens between user input and the frame reaching the display, and how to trade hitch resiliency for input latency. **Swapchain foundations:** front/back buffers, double buffering (default on console/mobile) vs triple (default PC); v-sync swaps at end-of-scanout, disabling it (`r.VSync 0`) lowers latency at the cost of tearing and hitch absorption — recommendation: ship v-sync ON by default with an opt-out. `r.VSyncInformationInsights` adds flip/miss markers to Insights (a dedicated green/red v-sync track is coming). **Compositor:** Windows' DWM adds ~1 frame; UE's flip-model swapchain auto-skips it in borderless fullscreen when the game covers the screen (true exclusive fullscreen no longer exists on Windows — it's emulated); NVIDIA multi-plane overlay only works on the primary monitor, so gaming on a secondary monitor adds a frame of lag; verify compositing mode with Intel's PresentMon. **Secondary upscale:** UE has a little-known second spatial upscaling stage (`r.SecondaryScreenPercentage.GameViewport`, algorithm via `r.Upscale.Quality`) that renders UI at native res afterward — a better alternative to "exclusive fullscreen at lower resolution" except on memory-bound 4K laptop panels. **Pipeline braking (GTSyncType 0, the default):** GPU stalls when no back buffer is free (shows as an unmarked bubble after the last post-process pass); RHI thread waits on the previous GPU frame (`SyncPoint_Wait` fence) and on Present when the swapchain is full; render thread waits on last frame's hardware occlusion queries (the misread "occlusion taking 15ms" is waiting, not work; non-Nanite only — `r.AllowOcclusionQueries`); game thread waits on the previous render-thread start plus a two-frames-ago RHI fence. Oversubscription markers likewise mean "waiting", not work. **Full pipeline = ~6 frames in-engine + 2 in hardware**, so input latency at 30fps ≈ 200ms, 60fps ≈ 100ms, 120fps ≈ 50ms — higher framerate is the simplest latency cut. A full pipeline can absorb a 2–3-frame hitch with zero dropped frames (demonstrated with a 90ms hitch, no drop). **Reducing latency:** `GTSyncType 2` throttles the game thread to start a fixed time before target v-sync (consoles only — PS4/5, Xbox One/Series, Switch 1/2; tune `SyncSlackMS`, default 10ms) for minimal latency and consistent delta time but zero hitch headroom; on PC use NVIDIA Reflex / AMD Anti-Lag 2 / Intel XeLL for adaptive throttling; `t.MaxFPS` slightly below refresh (58–59 on a 60Hz panel) starves the pipeline for lowest latency but drops frames every second — a user trick, not a shipping technique; `r.OneFrameThreadLag 0` and `GTSyncType 1` shorten the pipeline at escalating parallelism cost. **Future:** Epic is reworking frame pacing into a hardware-agnostic adaptive throttle with a target-slack setting (not in 5.8 yet). **VRR:** vendor-agnostic since HDMI 2.1, only helps when under refresh rate, enabled simply by v-sync ON. **Measuring:** `stat unit` Frame = wall-clock between game-thread frame starts; Game = that minus idle; GPU = busy-time union (bubbles excluded); Input = sampled-to-flip only (excludes hardware/OS/display latency); numbers are EMA-smoothed (0.9) and the stat FPS/unit mismatch (0.75 factor) is fixed in 5.8; third-party overlays count v-syncs, which UE can't yet report. **Jitter:** delta time = last frame's frame time; a hitch causes drop → recovery (big delta) → pipeline refill (short deltas), visualized with a 60-section spinning wheel; monitors rarely have round refresh rates (59.95Hz etc. — UE reports integers, causing ~0.5s drift/10min). Author's **Delta Time Smoother plugin** (GitHub) offers absorption / mitigation / pass-through modes as a stopgap until the new frame pacing ships.

### Key Steps
1. Ship v-sync ON by default (`r.VSync 1`) with a user opt-out; enable `r.VSyncInformationInsights` to see flip frame numbers and misses in Unreal Insights.
2. On Windows, prefer borderless fullscreen — the flip-model swapchain skips the DWM compositor automatically when the game covers the screen; confirm with PresentMon's composition-mode column; warn players off secondary-monitor gaming on NVIDIA (overlay only on primary → +1 frame lag).
3. For lower-res performance modes, enable the secondary spatial upscaler (`r.SecondaryScreenPercentage.GameViewport`, algorithm via `r.Upscale.Quality`) instead of "exclusive fullscreen" — UI stays native-res crisp.
4. Read profiler waits correctly: GPU bubble after the last post-process pass = waiting for back buffer; `SyncPoint_Wait` = RHI waiting on previous GPU frame; "waiting for GPU occlusion queries" / oversubscription = fences, not work. Don't "optimize" a wait away — it reappears elsewhere.
5. Cut latency first by raising framerate (pipeline depth is constant in frames, so latency halves from 30→60fps).
6. On consoles, set `r.GTSyncType 2` and tune `r.GTSyncSlackMS` (default 10) per platform for near-perfect pacing — only if you reliably hold frame budget, since one overrun drops a frame.
7. On PC, integrate NVIDIA Reflex, AMD Anti-Lag 2, and Intel XeLL for adaptive game-thread throttling.
8. If some resiliency must stay: `r.OneFrameThreadLag 0` (game/render threads stop overlapping — one core lost) or `r.GTSyncType 1` (waits on previous RHI frame) shorten the pipeline progressively.
9. Fight jitter with the author's Delta Time Smoother plugin (hitch-absorption for pipeline-absorbable hitches, mitigation-averaging for medium ones, pass-through for 100ms+ spikes) until Epic's adaptive frame pacing ships.

### UE Systems / Blueprints / Settings
- **CVars:** `r.VSync`, `r.VSyncInformationInsights`, `r.GTSyncType` (0 default full pipeline / 1 previous-RHI wait / 2 fixed throttle, console-only), `r.GTSyncSlackMS` (default 10ms, max one frame), `r.OneFrameThreadLag` (default 1), `r.AllowOcclusionQueries` (non-Nanite HW occlusion), `r.Upscale.Quality`, `r.SecondaryScreenPercentage.GameViewport`, `t.MaxFPS` (pipeline-starving trick — don't ship).
- **Profiling:** Unreal Insights (`SyncPoint_Wait`, ProcessVisibilityTasks, oversubscription markers, upcoming dedicated v-sync track), `stat unit` / `stat fps` semantics (EMA smoothing 0.9; 0.75 discrepancy fixed in 5.8), Intel PresentMon (composition mode + v-sync-counted FPS), Digital Foundry FPSGui (delta-based, works on consoles).
- **Platform behavior:** flip-model swapchain (always, PC), DWM skip conditions (borderless-covering or multi-plane overlay), emulated exclusive fullscreen, double buffering default console/mobile vs triple on PC, VRR via HDMI 2.1 (v-sync ON enables it; ~2-frame max hold, GPU resends last frame past that).
- **Vendor SDKs:** NVIDIA Reflex, AMD Anti-Lag 2, Intel XeLL (adaptive throttling, PC).
- **Plugin:** Delta Time Smoother (author's GitHub, 3 modes) — interim jitter fix; superseded by Epic's upcoming adaptive frame pacing (post-5.8).
- **Reference:** companion Epic Developer Community text article is kept up to date as systems change; this video is a snapshot.

### Difficulty
Advanced — engine-internals material; assumes comfort with Insights profiling and render-pipeline vocabulary. The actionable CVar recipes are usable by intermediate developers.

### UE Version
UE 5.8-era (stat smoothing fix lands in 5.8; adaptive frame pacing "coming soon", not in 5.8; GTSyncType 2 available on PS4/5, Xbox One/Series, Switch 1/2).

### Tags
frame-pacing, input-latency, vsync, swapchain, profiling, insights, delta-time, jitter, performance, unreal-fest, advanced

---

## Related Entries
- `tutorials/fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro.md` — rendering-performance optimization from the offline/cinematic angle; shares tags: performance.
- `tutorials/best-settings-for-unreal-engine-56---perfect-renders-every-time.md` — settings-level performance/quality tuning; shares tags: performance.
- `tutorials/unreal-engine-57-filmmaking-course---unreal-engine-for-filmmakers-2026-update.md` — where realtime frame-rate/latency constraints meet cinematic workflows; shares tags: performance.
