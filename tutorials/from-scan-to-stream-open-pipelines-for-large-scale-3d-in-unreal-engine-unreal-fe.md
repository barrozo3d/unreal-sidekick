---
title: From Scan to Stream: Open Pipelines for Large-Scale 3D in Unreal Engine  | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=5ehoHM-uzRQ
author: Unreal Engine
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: needs-review
frames_dir: tutorials/frames/from-scan-to-stream-open-pipelines-for-large-scale-3d-in-unreal-engine-unreal-fe/
frame_count: 0
frame_status: pending-selection
---

# From Scan to Stream: Open Pipelines for Large-Scale 3D in Unreal Engine  | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=5ehoHM-uzRQ)
**Author:** Unreal Engine
**Duration:** 38m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** ASR hallucination in 'Full Content': 'thank' x10 in last 50 content words. Review and truncate the affected section before extracting.

---

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py from-scan-to-stream-open-pipelines-for-large-scale-3d-in-unreal-engine-unreal-fe <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] I'll be chatting about how to bring large-scale 3D data sets into Unreal using a few different
[0:06] open-source pipelines and what to do with them once they're in.
[0:12] So just a little bit of an intro about myself.
[0:14] My name is Arkun and I'm a lead researcher at the Carlton Immersive Media Studios.
[0:19] We're a research lab based out of Carlton University in Ottawa, Canada.
[0:23] I have a background in architecture and turned into Game Dev a few years ago and went down
[0:28] this path mainly focusing on immersive arcfiz and digital twins.
[0:33] So I work a lot in Unreal Engine making these twins for architecture, especially for heritage
[0:38] buildings that are undergoing restoration rehabilitation, places where you might want
[0:42] to document and then visualize and also manage large data sets.
[0:48] And on top of that, I wanted to share what I've learned.
[0:50] So since a lot of my journey in Unreal has mainly been self-taught, so I became a content
[0:55] creator under ThirdSpace Interactive where I share tutorials, tips, tricks, devlogs of
[1:01] projects that I'm actively working on, mainly just to share my learnings with the community
[1:07] and then also helping out developers, showing them the ropes and helping them on their projects.
[1:13] So the role that I'll be mainly speaking about today is my work at Sims.
[1:17] We have five main research streams and work at the intersection between heritage documentation
[1:22] and real-time 3D.
[1:24] And the talk today will mainly focus on these three streams in particular.
[1:30] So we got our start in digitizing historic places, buildings, museums, and so on, into
[1:36] point cloud and photogrammetry models.
[1:38] We then use these as reference to create fully-fledged heritage BIM models, HBIM, and this includes
[1:45] all the disciplines, so shell, interior, MEP, structural, and then we bring them into real-time
[1:50] 3D software.
[1:52] What you can see in the background is a web version of one of our digital twins.
[1:56] And we also work with digital twins in game engines, Unreal, to be specific, which is
[2:00] primarily my role at the office.
[2:04] So this talk is going to focus on a few different topics, all increasing in complexity as we
[2:08] go.
[2:09] First, we'll chat about a problem that we ran into a few years ago, and that's mainly
[2:13] around the sheer amount of data that we were collecting and needing to display for these
[2:19] large-scale heritage projects.
[2:21] And we'll explore this through a case study of the university campus where I work, and
[2:26] the three file types that we'll mainly be focusing on are point cloud, photogrammetry,
[2:30] and BIM.
[2:31] We'll go through three open-source tools that we created to be able to bring these in for
[2:35] runtime streaming and talk about just how to prep these models and actually use them
[2:40] in Unreal.
[2:42] So let's start off with the problem.
[2:45] A lot of the projects that I work on at Sims are confidential.
[2:49] These are heritage sites undergoing restoration or rehabilitation, government facilities, places
[2:54] where people are very particular about where their data is stored.
[2:58] That means that there are a lot of data and file types produced.
[3:00] So a moment a tool says, you know, upload your data to our servers, we'll handle the
[3:04] conversion for you, we'll handle the hosting for you, that conversation unfortunately dies
[3:08] pretty quickly.
[3:09] The data for us usually isn't allowed to leave the room, let alone the building.
[3:13] So we have to figure out workarounds with local servers and local tools.
[3:17] And this quickly became a problem for us since the tools that we needed to actually support,
[3:21] you know, hundreds of gigs to terabytes scale 3D are mostly cloud first.
[3:27] So we turned towards open source.
[3:30] And the landscape wasn't particularly encouraging for runtime streaming.
[3:33] For point clouds, the main tools that we found were Poetry and Antoine.
[3:38] Both are great, but both are web first.
[3:41] For meshes, the closest thing that we found was OBJ2.tiles, which converts it to a 3D
[3:47] file, which handles partitioning, but it has its own unique problems, including baking
[3:52] full textures onto each tile, which quickly blows up file sizes.
[3:58] And then for BIM, and I'm mainly focusing on IFC here, I know Datasmith Runtime is
[4:01] an option, but for IFC at least, the only options were experimental.
[4:05] So you have the asset importer plugin and the datasmith plugin as well.
[4:09] And the list of libraries that I have shown up here are only the ones that are maybe compatible
[4:14] with Unreal.
[4:15] The rest that we were finding were mainly web first.
[4:18] So what happens if we try to brute force all of these tools to spawn them into Unreal?
[4:24] We get something that I like to call nightmare fuel.
[4:27] The reality is poor optimization.
[4:30] I won't go through this entire list, but files for the datasets that we were working with
[4:34] are huge.
[4:35] So, you know, what we would hope would be a simple runtime import quickly blows up file
[4:39] sizes, memory budgets, and ruins frame rate.
[4:43] And for BIM in particular, we were getting the geometry, but we were losing the semantic
[4:46] data, the very thing that makes it a building information model in the first place.
[4:52] So we decided to build our own pipelines, three of them in particular.
[4:56] The first one for point clouds, second for photogrammetry, and the third for BIM.
[5:00] All three are open source.
[5:02] And I'll note that the first two point cloud and photogrammetry are available today in
[5:06] fragments.
[5:07] We're planning to release later this summer.
[5:10] So there's no cloud step anywhere in this chain.
[5:12] Unless you choose to host the data in your own S3 bucket, everything can be converted
[5:16] and hosted locally.
[5:20] Now before I get into the tools, I want to grant us on one main case study.
[5:25] So when I got accepted to do this talk, I knew I had to find a dataset that was large
[5:29] enough to actually put both push both Unreal and these pipelines to its limits.
[5:34] Ironically, the topic that I picked was centered around data sovereignty and data security.
[5:39] So the projects that I've already applied all these pipelines to, I can't actually talk
[5:43] about.
[5:44] So I picked one that's instead near and dear to where I work, and that's the Carleton
[5:48] University campus.
[5:51] For the campus, we have 47 BIM models, landscape model of the site, 100 or so gigabytes of
[5:57] point clouds, and around 25 gigs of photogrammetry.
[6:00] And this scales up as well to the terabyte scale.
[6:03] The scale and complexity of these models, however, are a good fit for showcasing what
[6:07] this tech can do.
[6:09] And this will be the baseline that we anchor on.
[6:11] And I had some help from my lovely team at the lab to build out an entire scene of the
[6:16] campus, which you can see here is nice and empty, just waiting for us to populate it.
[6:21] So we'll be adding our models to the scene as we go through the talk.
[6:26] So let's begin with point clouds.
[6:28] With our web digital twin that I showed earlier, we're using an open source library called
[6:32] Poetry, which streams point clouds directly to the platform.
[6:37] We're porting over that same library into Unreal.
[6:39] It didn't really work for us with the way that Poetry organized its data.
[6:43] We wanted something that was compatible with the cesium for Unreal plugin, cesium's open
[6:47] source 3D tile reader for the engine.
[6:50] So we can always customize this if we decide to do so in the future.
[6:55] And because this already existed, there was no point in reinventing the wheel there.
[6:59] And that's when we came across a library called N-Twin.
[7:02] It's an open source point cloud indexer that takes your raw scan as a last file and then
[7:07] chops it into a spatial auktree so that a web-based viewer can stream it into its relevant
[7:13] chunks.
[7:14] And it's been around for close to a decade, but unfortunately they deprecated their support
[7:18] for 3D tiles a few years ago.
[7:22] But that's not a big deal for us since 3D tiles is also an open source spec for streaming
[7:27] massive 3D scenes easily.
[7:30] And conveniently the tiling structure was near identical to N-Twin.
[7:36] We just needed to do a little bit of file conversion and create something called a tileset manifest
[7:40] JSON that our Unreal plugin knows how to serve it into our scene.
[7:45] And here are the results of the pipeline.
[7:47] It's essentially a Python wrapper that uses these existing libraries to get from point
[7:51] A to point B.
[7:53] We start off with an E57 or a last file as the main input.
[7:57] We use N-Twin to spatially partition it into Ept's auktree format to give us a folder full
[8:02] of lovely tiles.
[8:04] And then we do a little bit of conversions to get that to a GOB file, which 3D tiles
[8:09] needs, and then generate an optimized and more importantly a geolocated tileset JSON
[8:14] manifest.
[8:16] And after a final compression we're left with a 3D tile folder with a manifest that we can
[8:21] point towards Unreal.
[8:23] And of course we can parallelize the entire process to batch convert our point cloud models.
[8:29] And the script itself is fairly simple to run.
[8:31] You can input a single file, a whole directory of files, and you can set the amount of point
[8:38] cloud models that you'd like to batch convert in one go.
[8:41] And here you can also specify geolocation and compression.
[8:45] And because we're able to parallelize a lot of this, the only restriction really is in
[8:49] our memory, how much RAM you have, and CPU cores.
[8:54] For the point clouds of the university campus, we were able to convert the full set in around
[8:57] four hours with eight parallel workers.
[9:00] My CPU had 16 cores.
[9:02] And due to spatial partitioning and compression, first to las and then to our additional Gzip
[9:07] compression, the output size was actually 65% smaller.
[9:11] And of course all of these were computed locally on my one lonely workstation.
[9:18] So bringing that into Unreal, we can see the details of the hierarchy that is output by
[9:22] the Octree pipeline.
[9:24] It's a spatially aware algorithm.
[9:26] So you can see that the Octree doesn't create tiles exponentially for each step up in LOD.
[9:31] But rather it's only generating tiles where there's actually detail, where the point count
[9:35] is over a preset threshold.
[9:37] And it adds these tiles by layering detail on top of each other, layering tiles on top
[9:41] of each other, until you get the target amount of detail.
[9:46] And on the Unreal side, it's basically a simple step of enabling the season for Unreal
[9:50] plugin, adding an MT3D tileset actor, and then pointing the actor towards a URL, which
[9:56] in this case is just a file path, meaning that you can either serve it locally or from
[10:00] a remote bucket like S3.
[10:04] So what does it look like at the end?
[10:06] Centering back on our Carlton campus scene, in just a few seconds we're able to load around
[10:10] I think 12 to 14 point clouds.
[10:13] And we can isolate in the scene to get a better view of what was imported.
[10:16] Each of these scans here represent different efforts that Sims has done over the campus
[10:20] throughout the past decade as the campus has grown and evolved.
[10:24] And as we zoom into different spaces, we can see that the amount of detail increases as
[10:27] per the instructions of our optimized tileset hierarchy.
[10:34] So next up we have photogrammetry.
[10:37] This was supposed to be the exact same playbook.
[10:40] Try to find the N2 equivalent that was also open source wired through that same Python
[10:45] wrapper script.
[10:47] And hopefully we'll be done in a couple of days, maybe a week if we're optimistic about
[10:50] it.
[10:51] The reality was that photogrammetry just does not have the same ecosystem of libraries built
[10:56] up.
[10:57] No one's really spent the time to build an open source equivalent of N2 for meshes.
[11:02] The few converters that did exist targeted much smaller models and they were mainly targeted
[11:06] again for web viewers.
[11:08] So often these had their own underlying problems around performance and file size.
[11:14] So we were back to square one and had to build something completely from scratch.
[11:19] And interestingly enough, we landed on Blender for this, which might sound strange because
[11:23] I know that Blender is typically a DCC platform, not really a pipeline tool.
[11:28] But most interesting part for us is that Blender is completely open source as we all know,
[11:32] but it has a very mature library of mesh editing tools built up over the last couple of decades.
[11:38] So we have a lot of information, B mesh operations, UV and wraps, texture baking, all of it's
[11:42] been built in, and most importantly, all of it's available through the Blender Python
[11:45] API.
[11:47] Which means that we can run Blender headless and have multiple Blender sessions running
[11:50] in parallel through command line.
[11:53] So this opened the door for batch processing, which now revealed that photogrammetry had
[11:58] its own set of problems that we need itself.
[12:02] So firstly it was detailing itself.
[12:05] If we were to take inspiration from existing tools, we learned that they do these uniform
[12:10] grid cuts with even tiles everywhere.
[12:13] That's sort of ignorant to the geometry that lies within.
[12:16] This doesn't really work for photogrammetry where details in a heritage space aren't exactly
[12:20] even.
[12:21] You know, a cornice or an ornamental detail in a room would be significantly more complex
[12:25] than the wall or the floor that's beside it.
[12:28] So it doesn't make sense to treat each of these spaces the exact same.
[12:32] Instead we can learn from how n-twin handles point clouds and use this spatial octree.
[12:37] Basically, we create a box, split it recursively into eighths, and then the important thing
[12:42] here is we need to make sure that that recursion is adaptive.
[12:46] So every tile that we create, we check it against a triangle threshold, which in our
[12:50] case is around 20,000 triangles.
[12:53] If a tile falls under that threshold, we stop, we call it a leaf tile.
[12:58] If it falls over it, then we continue splitting until we satisfy the LOD depth.
[13:03] And this way we're basically able to follow complexity and minimize the amount of tiles
[13:07] produced and thus keep the file size down.
[13:11] And here are the LODs that we can create with this adaptive spatial partitioning.
[13:16] Whereas with the point cloud data, we were constantly adding layers on top of one another
[13:21] as we zoomed in to get detail with mesh we want to replace the tiles entirely.
[13:26] And that means that we now need to also address texture.
[13:30] With point clouds, this wasn't really a problem since it's just a vertex color on a point.
[13:35] With mesh you have these large open source textures.
[13:38] Sorry, we have these large source textures.
[13:40] And the way that our open source libraries currently handle this is, leads to something
[13:45] called texture redundancy.
[13:48] That's where the existing tool takes 16k texture, let's say, and then bakes it into
[13:53] each and every tile.
[13:54] So a tile under 20,000 triangles might normally be like a megabyte in size, now balloons up
[14:00] to 50 megs or more depending on the size of your texture.
[14:03] And imagine that at the scale of an entire mesh.
[14:05] So if we look here, we have 256 tiles times 50 megabytes each.
[14:11] And when we were to actually select the UVs of this tile, we can see that it only uses
[14:15] a fraction of the texture.
[14:17] So of course, we add a baking step.
[14:20] Blender smart UV project also exposed via the Python API gives each tile its own unique
[14:25] 1024 by 1024 texture.
[14:28] And you can see in this case, we're able to get the exact same details from a much smaller
[14:31] texture.
[14:32] So same size everywhere for these textures and unique for each tile.
[14:37] And because the tiles vary in physical size, as you go through the LODs, this also adapts
[14:42] our text density for free.
[14:43] So now we're not only creating mesh LODs, we're also creating texture LODs.
[14:50] And then thirdly, we have this thing called an LOD ladder.
[14:53] So it's a budget driven rule where we hold this 1024 by 1024 texture for as long as possible
[14:58] until the total text will count for an entire model is achieved.
[15:02] For a 16k texture that's around LOD 3.
[15:06] And once we cross that budget, we drop resolution to a 32 pixel floor.
[15:11] And that way, once we've achieved the target fidelity of the photogrammetry model, we adapt
[15:16] subsequent LODs and never really invent detail where it didn't exist already in the source
[15:21] texture.
[15:23] And this side by side compares the results of that adaptive texture technique.
[15:28] For our test model, we were able to achieve the source texture resolution by LOD 5 when
[15:33] you're right up and close to the building.
[15:35] For the open source alternative, LOD 0 because it didn't handle any decimation or optimization
[15:40] for the texture.
[15:41] And for the cloud converter, it was around LOD 6 with its Draco compression.
[15:48] And what comes at the other end, pipeline works in a very similar way.
[15:52] We write a folder of GLB tiles plus that tiles JSON manifest.
[15:57] Same 3D tiles format used for point clouds, very similar pipeline.
[16:02] So CZM4 Unreal reads it the exact same way.
[16:05] It's the same URL pattern, same on-premises conversion process.
[16:10] How does it scale with complexity?
[16:12] Typically, we're dealing with models in a 1 to 10 million triangle range.
[16:16] And we can see that the script is able to convert that fairly well.
[16:19] But in the name of science, we needed to test if it would work with the source model from
[16:23] a photogrammetry authoring software.
[16:25] Now anyone that's probably ever made a photogrammetry model knows that the output is usually really
[16:30] large and needs to be simplified before we can do anything useful with it.
[16:34] In our case, that number was around 90 million.
[16:36] And that's around a 10 gigabyte sized input for an OBJ model and a 32K texture.
[16:44] So we ran it through our pipeline and it came out to around 3.8 gigabytes of streamable tiles.
[16:51] Which is around a 62% reduction.
[16:54] And for the same model, both the open source and the cloud converter weren't actually
[16:57] able to finish the processing and they failed at that step.
[17:03] And what is the time to convert look like?
[17:05] As you can imagine, it scales with complexity.
[17:07] So for a 900,000 triangle model, we were around three minutes.
[17:11] For a 9 million model, we were around 40 minutes.
[17:14] And then for a 90 million model, it's around five hours.
[17:17] So it definitely scales, but it scales linearly.
[17:20] And for the campus models, because they're all in that 1 to 5 million triangle range,
[17:25] and we were able to batch convert all of them in parallel, we were able to get all of them
[17:28] done in around two hours.
[17:31] So coming back to our Carlton scene, we can see that we're able to import it in just a
[17:35] few seconds.
[17:36] And with photogrammetry, it takes a little bit more time to slowly filter through and
[17:39] increase the LODs.
[17:41] And we can isolate in the scene to see it a little bit better.
[17:44] And what we have here is a drone scan of a new rail line that was being installed on
[17:48] the campus, plus this lonely building off in the distance that we still need to connect.
[17:53] And hopefully I can show this video to the university as my bid to fly the drone over
[17:57] it again.
[17:59] But as we zoom in, you can see that more details get added.
[18:03] OK, so this is the third pipeline.
[18:06] It's the one that's taking the most time to produce, and the one that I'm most excited
[18:10] to share.
[18:11] This is Fragments for Unreal, our solution for BIM streaming in Unreal.
[18:15] It's the only one of the three that's still under active development, hence why we're
[18:18] planning to open sources later this summer.
[18:22] So how did this all begin?
[18:25] About a year ago, my co-developer, Hyro, posted a short video on LinkedIn.
[18:29] He had taken that open company's Web Fragments stack.
[18:32] He'd wired it through this thing called the Google's Flatbuffers schema and figured out
[18:36] how to get BIM models, spawning in Unreal in around five days.
[18:40] When I saw this hop up on my feed, I immediately messaged him, and that started a 12-month
[18:45] collaboration where we've been basically turning this from its proof of concept into an actual
[18:50] plugin that can hold a campus-scale scene at a reasonable frame rate.
[18:56] So why build an entirely new tool?
[19:00] We'd already taken PointCloud and Photogrammetry, shown that we can convert it to 3D tiles, and
[19:04] there is existing support for IFC for 3D tiles.
[19:08] So we'd already proven that we can build it ourselves.
[19:11] However, the gap was something that we saw in the existing tool ecosystem that is best
[19:16] articulated with this side-by-side comparison.
[19:19] So looking at these three columns, we have the most popular file types that are used
[19:24] in Unreal and also outside, which is Datasmith, 3D tiles, and IFC.
[19:30] Datasmith is a great offline importer.
[19:32] You get Dataprep, which is awesome for creating recipes that are reusable, a full per-element
[19:37] control for materials, merging, LODs, baking nanite, and all with the hierarchy and the
[19:44] metadata preserved.
[19:46] But it's built for offline use.
[19:48] Runtime streaming is limited, and everything lives inside the application when you package
[19:52] it, which balloons the size of your executable.
[19:56] And that last point really matters for us, because we typically deploy through Kubernetes
[20:00] and pixel streaming.
[20:02] So that means that the bigger the app, the slower the cold start.
[20:05] What we want is a thin skeleton with the data living on the server pulled in when needed.
[20:12] And 3D tiles would be the natural second option.
[20:15] Great runtime performance hosted on a local server or remote.
[20:19] It loads in in a fraction to a couple seconds, depending on the speed of your read-write to
[20:24] the server.
[20:26] But in order to get there, it has to merge everything into a spatial hierarchy.
[20:29] You're still able to keep selection through per-vertex metadata, but you lose per-element
[20:34] control.
[20:35] And then you're generally stuck with whatever the base material came from your authoring
[20:40] software like Revit, unless you do a little bit of finagling.
[20:44] And then there's IFC itself.
[20:46] 30 years of validation in the AEC industry, vendor-neutral, and it's rich in metadata
[20:51] that's baked into each and every element.
[20:53] The catch, however, is that support in Unreal is mainly experimental.
[20:57] We were getting the geometry coming in, but the semantic data wouldn't always follow.
[21:02] So we have three formats, three strengths, three let's call them deal breakers.
[21:06] When fragments came along, Hiro and I saw a way to take the best of all three and put
[21:10] it into one plugin, which we're hoping that can be fragments Unreal.
[21:17] And there's a more personal reason as well.
[21:19] At Sims, everything that we build, campus and national scale already streams through
[21:24] this schema on the web.
[21:26] But the question that we would always get from clients is, how do you actually make
[21:29] it look realistic?
[21:30] So instead of trying to reauthor every one of these assets specifically for the web,
[21:35] we began wondering how we could bring fragments straight into the game engine.
[21:39] Give it the fidelity that only Unreal can get with data smith per element control and
[21:44] trying to get that streaming performance of 3D tiles.
[21:50] So how does fragments handle performance on the web?
[21:53] It's essentially a structure of arrays.
[21:56] It's a runtime optimized version of an IFC file where it does all of the preprocessing
[22:03] for figuring out what to instance.
[22:05] So you have these parallel pools of instancing.
[22:07] So how the web fragments handle that, and I won't go through all of these, but you're
[22:11] able to get 3JS instance meshes, an LOD system, and with wireframe when you're far away, full
[22:17] geometry when you're up close, Frostam Culling, Picking, Transparency, all of that other fun
[22:22] stuff that's already supported with 3JS.
[22:25] So we need to somehow figure out how to port all of this logic into Unreal.
[22:32] And before I get into how we did all of that, I want to actually show how to create a fragment
[22:35] model itself.
[22:37] Pyro has created a repo on our GitHub, and that's called IFC to Fragon.
[22:42] Also for all the repos that I'm mentioning, I'll have a QR code at the end that you can
[22:44] scan.
[22:45] So with this, you simply just upload your IFC model into a web viewer.
[22:51] And the import process converts it all to a fragment that you can download.
[22:54] And what you can see here is us running it locally.
[22:57] We're just pulling the repo, running it through MPM, and then loading in our files.
[23:02] And when you convert a fragment file, it also compresses it down to optimize it for that
[23:06] runtime streaming that I mentioned.
[23:08] So a 250 megabyte model like this one gets saved and compressed as a 17 megabyte model.
[23:14] So not only is it optimized for streaming, it's also optimized for storage.
[23:22] But where do we actually start with performance?
[23:25] Once I got my hands on the initial plug in about a year ago, we quickly realized that
[23:28] we had to reimagine the entire architecture for how to handle runtime streaming, since
[23:34] obviously Unreal doesn't work like the web, although there are some similarities in the
[23:37] concepts that we'll use.
[23:40] With the original plug-in, we were able to load in a single model in around 10 minutes.
[23:45] And we were getting a performance of 22 frames per second, which unfortunately is cut off
[23:49] from this.
[23:50] And even when we tried to spawn the mesh asynchronously so it wouldn't block the entire game thread,
[23:54] the time didn't really go down.
[23:57] So my initial focus from then onwards became on runtime performance, while Hiro has mainly
[24:01] been focusing on functionality and feature use cases that we've been slowly merging together
[24:05] over the last few months.
[24:09] And I could spend an entire talk just on the nightmare I spent in Unreal Insights, but let's
[24:16] just focus on the results of our performance.
[24:19] The first thing we looked at was Instancing in Unreal, which is supported through instant
[24:22] static meshes or hierarchical instant static meshes and their components.
[24:27] For our use case, hierarchical components made the most sense, since they allow for
[24:31] per instance culling, which gives us both the performance benefits, especially for frustum
[24:35] and occlusion culling, with how the engine handles each of these components.
[24:41] And this is the streaming pipeline that came from that, since Instancing made it a lot
[24:45] easier.
[24:46] And this is what it looks like today.
[24:47] We basically take our .frag file, which is the fragment file, we decompress it on a
[24:51] worker thread, use flat buffers to parse it and build a hierarchy.
[24:56] And then we split that hierarchy into shell and interior.
[25:01] With the shell, we're able to create a hierarchical LOD system that then generates an LOD2 proxy,
[25:07] so just a unified mesh of the exterior envelope, all merged into one shell, and then an LOD1,
[25:13] which are spatially partitioned cells, where we're bringing that idea again from 3D tiles.
[25:19] And then once the initial load is complete, we're only populating the building envelope
[25:23] into our scene.
[25:25] And then once the user activates the building, and that's either done by clicking on it to
[25:28] activate or through distance proximity, we can begin to lazy load in the interior models
[25:34] and generate their LOD1 meshes at runtime.
[25:39] So what does that actually mean?
[25:40] For a model like this, we're actually able to defer a lot of the triangles and therefore
[25:44] a lot of the work that needs to be done to first populate it into the scene.
[25:49] By loading the shell first, we're only having to deal with 260,000 triangles that we process
[25:53] initially, so it only takes a couple of seconds to load into the scene.
[25:57] And then when you activate the interior, we're lazy loading in the remaining triangles, which
[26:01] was around 10.6 million in this case, so almost 98% of our triangles get deferred.
[26:09] And to give you a visual of how our HLOT system works, LOD2 is this merged cell proxy, one
[26:14] unified mesh.
[26:16] Then when you actually activate the building, you get these per cell merged meshes, which
[26:21] are merged by their spatial region and also by their floor.
[26:24] And these also cast shadows when hidden, which is important because for runtime, we can't
[26:31] rely on Nanite and virtual shadow maps.
[26:34] So a lot of our processes are CPU bound and every millisecond helps.
[26:38] So now by having these runtime hidden shadow casting for LOD1, we're only having to deal
[26:44] with 134 shadow casting primitives instead of 26,000 shadow casting primitives.
[26:50] That also helps with runtime performance.
[26:52] Every little bit helps.
[26:54] And you can see what the individual components look like on the far right.
[26:59] And then we have our material system.
[27:00] So with our Fragments Master Material, we're able to leverage per instance custom data
[27:05] to add individual control out of each of our components.
[27:10] So slot zero basically controls base color and highlighting, slot one controls opacity
[27:15] masks to control visibility on and off, and dither fading to control ghosting.
[27:20] Slot two controls position offsets for reveal animations.
[27:24] And that really helps us get into the simulation space a little bit more.
[27:27] And in general, a lot of this material up animations are happening on the GPU.
[27:31] So we're able to offload a lot of that to make our performance even more optimized.
[27:37] And you might be thinking to yourself, with this HLOT system, how do individual instances
[27:42] say interactable if we're dealing with these merged meshes at different distances?
[27:46] So for that, we created a specific blueprint called select at screen position, which selects
[27:51] the individual instance by being spatially aware.
[27:54] So wherever you click, it auto promotes those cells and only the cells around where you
[27:59] actually need to select your components.
[28:01] You can see everything else stays at that unified mesh merged hierarchy.
[28:05] And this again really helps when we're trying to do everything we can for performance.
[28:11] And speaking of blueprint nodes, we've created quite a few.
[28:14] Most of the ones on the left will be part of the initial release of our plugin.
[28:18] And again, this will be open source since we really want the community to just take
[28:22] this up and be able to help us build this into something that is sustainable and performant.
[28:29] And the ones on the right hand side are the ones that were created specifically for this
[28:32] demo.
[28:33] And if there's interest in them being used for the wider audience, then we can of course
[28:38] include that in the plugin as well.
[28:41] So after all that work, where does it leave us on performance?
[28:44] So we've got a single building, the model loaded in just a few seconds.
[28:47] And in those few seconds, it's also creating all of those LODs at runtime.
[28:51] So other than creating the fragment file itself, there is no pre-processed step.
[28:57] A single building sits around the 120 to 130 frames per second when you're in the thick
[29:01] of it.
[29:02] And when you're farther away, you're getting in that 140 to 150 range.
[29:05] And this is all on a 4080 GPU.
[29:09] And you can see as well just a little bit of a teaser, but we have some PBR materials
[29:12] that have been applied to this model.
[29:16] And I'll get into how we're doing that in just a second so that we can avoid having
[29:20] just the basic materials that you get from a modeling software like Revit.
[29:25] But on the campus scale, how does it work?
[29:28] The 47 fragments take about five seconds each.
[29:32] So right now, the full campus comes in around five minutes.
[29:35] And that's including, again, generating all those LODs, building the hierarchy, applying
[29:39] materials, placement overrides, all happening at runtime.
[29:42] And obviously, this is sped up for the presentation to around 10 seconds.
[29:46] So with all 47 in the scene, you can see that we're holding around 60 to 70 frames per
[29:51] second as you navigate, which works pretty well for runtime imported BIM at a campus scale
[29:56] without any baking or cooking step in the editor.
[30:00] And once we load everything in, we can see with our LOD debugger that clicking on buildings
[30:05] auto promotes them to active, and then clicking on different buildings, demotes the previous
[30:10] and promotes the new.
[30:12] And this really helps us minimize the number of complex meshes and geometry that's in the
[30:16] scene.
[30:17] And we're also lazy loading in those interiors, which explains the hitches that you can see
[30:20] there as the interior models populate in.
[30:23] And you can see that as well with the antenna on the roof of this building.
[30:29] So where do we go next?
[30:30] Obviously, we want to continue improving runtime performance, but we want to offer some options
[30:34] for offline support as well.
[30:37] So with some LOD editor preparation steps, we were thinking that we can generate LOD
[30:42] to proxy in the LOD1 merge cells with their materials and everything offline, save that
[30:48] to the content browser, which would allow us to populate the LOD2 shells immediately into
[30:53] the scene when you first import it.
[30:55] And then we can lazy load in your LOD0 or your actual fragment individual components from
[31:01] the server at runtime.
[31:02] And then optionally, we can also build these LODs as nanites to leverage what the engine
[31:07] already has built in with this virtualization system.
[31:12] And speaking of editor functionality, our initial release will include a couple of main
[31:16] features.
[31:17] So you can load in any fragment model into your scene.
[31:20] In this case, I choose to spawn it at the world origin, but you can just easily choose
[31:24] the base coordinates from your authoring software.
[31:27] And on the right hand side, we can just use our regular editor panel to specify location
[31:31] and rotation offsets.
[31:33] And you can see at the bottom left, we have a little button for saving that placement
[31:37] so that it stays persistent through different sessions, but also on different workstations.
[31:41] And I'll explain how in the next slide.
[31:45] On this left panel, we also have the ability to manipulate materials.
[31:47] And here you can see me reverting these PBR materials that we've applied to the building
[31:51] back to the original that we got from Revit.
[31:55] And we're able to use this panel to isolate and highlight these materials in the scene,
[32:00] again, using our fragments material to control all of this functionality.
[32:04] And then we're able to override these materials as well.
[32:07] So in the case of the red facade, we can apply just red siding.
[32:12] And then for the main beige color that you can see there, we'll apply wood paneling.
[32:17] And again, these PBR textures are also saved between sessions and between workstations
[32:21] and also support runtimes.
[32:23] And nothing is ever really saved in your package build other than the materials.
[32:28] So how do we actually handle this?
[32:30] It's through fragments overrides.
[32:32] So it's a JSON file that's kept at the exact same file location as your fragment model
[32:36] and is auto-generated by our plugin as soon as you try to load in your fragment model.
[32:41] In our case, we hosted this on a local server, but you can just as easily put it adjacent
[32:45] to your object storage bucket or wherever you keep your files.
[32:50] The plugin then reads this override's JSON file at runtime and imports it into the scene
[32:54] and applies the materials, geolocation, or rather the placement changes.
[32:59] And if it doesn't exist, then it reverts back to what the fragment file came with or what
[33:04] the IFC originally came with.
[33:08] And here's a snippet of how you can expand that fragment space material to create a master
[33:11] material with PBR support, animations, weather, and more.
[33:17] So that was a lot of talking and a lot of more diagrams than demos.
[33:20] So now that we have these three tools to stream in BIM, photogrammetry, and point cloud,
[33:25] you can see in the background that we're able to flip through these different models of the
[33:29] same building on the campus at runtime.
[33:31] But how does it look all together?
[33:34] So for that, let's jump into the actual showcase of this tool.
[33:38] Here's our scene with all of the models loaded in.
[33:40] You can see we're able to select a model directly in our scene where it begins to lazy load in
[33:44] the interior elements, including some of the MEP stuff on the roof.
[33:49] All of the elements, excuse me, stay interactable.
[33:52] And we can use the material system to override that into our scene and see all of the relevant
[33:57] pieces of metadata.
[33:58] And we can select another building to do the same.
[34:01] And you can see here we have a couple of nodes that we've created specifically for controlling
[34:05] floor visibility.
[34:06] And that's also why our merge cells are merged by their floor ID to keep this functionality
[34:12] performance as well.
[34:13] Once a floor is hidden, the plugin is able to only detect what is hidden.
[34:18] That way you can only interact with what is still visible, allowing you to zoom in, orbit
[34:23] around, select and see all of the relevant pieces of metadata from that IFC file.
[34:31] And then we can have some fun with materials and build off of the existing plugin's functionality
[34:36] to add category filtering.
[34:38] IFC models are rich in category data.
[34:40] So a lot of the building modeled elements are assigned one when you first model that
[34:45] at your in your authoring software.
[34:47] And we can use this to isolate the building within the scene, decide to show all or none
[34:50] of the components and use a slider to control the opacity.
[34:54] And then if we disable everything and select, let's say, some of the structural categories
[34:58] like columns and floor slabs that allows us to audit the model in some additional and
[35:03] unique ways.
[35:06] And then if we have even more fun with material math, we can get into the simulation territory.
[35:10] And that's where we use animations using world position offsets and a bit more ghosting
[35:14] all handled through a material parameter collection in your blueprint graph.
[35:20] So this specifically we're using for a timeline functionality.
[35:23] We can use the IFC categories, organize the building into its phasing.
[35:27] So we have foundation, superstructure, envelope and MEP rough in and then also this finishes.
[35:33] And then we can use a world offset position note per custom data to animate these into
[35:38] place as the timeline progresses.
[35:41] And we can scrub back and forth as well, see MEP falling into place if we want, we can
[35:45] select it or just zoom in to be able to see how everything stacks together as an assembly.
[35:51] Where I can really see this being useful is connecting this with an actual construction
[35:54] schedule so that you can animate what your construction process will look like in real
[35:59] time.
[36:00] This is just all being read from a JSON file created from a CSV and all simulated in engine
[36:05] as well.
[36:08] And then our second example of simulation is energy simulation.
[36:12] So this is data that we received from the university on energy usage a few years ago.
[36:17] It was a simple CSV that we converted to a JSON so that it could be read by the plugin
[36:21] and we made a material function just to be able to override the colors.
[36:26] And what we ended up with was another timeline indicating the energy usage campus wide over
[36:31] the course of a year.
[36:33] And as we go from fall to winter, you can see how the energy usage spikes and see that
[36:37] both in the top right panel as well as this bottom timeline here.
[36:42] And not only can we see it at the campus scale but also the individual building scale and
[36:47] all of the relevant pieces of information that we got from it.
[36:50] And the part that really excites me about this is we got this from a static export from
[36:54] the university but we can just as easily connect this to live data to be able to see what the
[36:58] actual energy usage is at any specific time from the university.
[37:03] So this could be a really effective tool for simulation.
[37:07] And of course we want to bring all these file types together at the end.
[37:09] So I made this little tool called a comparison slider based off of the split fiction game
[37:14] where I was really interested in the material math that that game was doing.
[37:17] So it's a comparison slider that we can use specifically for ARCVS and slide between the
[37:21] three different file types that we've talked about today.
[37:24] On the left you have your BIM model, in the center you have point cloud and on the right
[37:29] side you have photogrammetry.
[37:31] We usually use this for reality capture model auditing.
[37:35] As I mentioned at the beginning a lot of our heritage BIM models are created from point
[37:39] cloud.
[37:40] So this really allows us to visualize and audit that information to make sure it was actually
[37:44] modeled accurately.
[37:48] And with that I just wanted to thank you all for your time.
[37:50] Here's a QR code of the repos that I mentioned today and happy to answer questions.
[37:54] We have about 12 minutes left.
[37:56] Thanks all.
[37:57] Thank you.
[37:58] Thank you.
[37:59] Thank you.
[38:00] Thank you.
[38:01] Thank you.
[38:02] Thank you.
[38:03] Thank you.
[38:04] Thank you.
[38:05] Thank you.



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
