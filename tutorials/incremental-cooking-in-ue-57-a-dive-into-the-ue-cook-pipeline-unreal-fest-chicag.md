---
title: Incremental Cooking in UE 5.7: A Dive Into the UE Cook Pipeline | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=6L4Mz4FtMuY
author: Unreal Engine
ingested: 2026-09-04
ue_version: "UE 5.8 (title says 5.7 -- see notes)"
tags: [pipeline, automation, cpp, advanced, ue5-7, ue5-8]
extraction_status: complete
frames_dir: tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/
frame_count: 14
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Incremental Cooking in UE 5.7: A Dive Into the UE Cook Pipeline | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=6L4Mz4FtMuY)
**Author:** Unreal Engine
**Duration:** 45m35s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi, my name is Matt Peters.
[0:03] I'm on the Foundation Core Data Pipelines team.
[0:05] I'm responsible for most of the code in Ucook
[0:07] on the Fly server, which runs the Cook.
[0:09] My team has been working on the IncrementalCook performance
[0:11] feature for a while, and it's ready for use in 5.8.
[0:14] I'm describing today what it is, how to enable it,
[0:16] and how to write code that complies with its requirements.
[0:20] We'll start off with concepts, and then how to enable it.
[0:22] From there, move on to how to write your classes
[0:24] and work with it, and then what you should expect
[0:26] from the code now and in the future.
[0:29] Therefore, starting with the context.
[0:32] Unreal is a runtime game engine and a tool set.
[0:35] Our most important two guiding principles are, it just works.
[0:38] You don't have to enter a lot of settings
[0:39] and work around engine limits and content or game code.
[0:42] The engine aims to have solutions in the engine layer
[0:44] that solve almost all problems well.
[0:46] And maximal tech, maximal art, best in the world,
[0:49] graphics, audio, performance, and engine features.
[0:52] These two principles conflict.
[0:54] Having the best performance sometimes requires
[0:56] content-specific tweaks.
[0:58] Having giant data sets makes analyzing those data sets
[1:01] too expensive, doing both at once as a goal with the score
[1:04] rather than a binary pass or fail.
[1:06] The approach that we've taken over the past few years
[1:08] in the cook is a hybrid approach.
[1:09] We make the default path for content constrained
[1:12] in as fast as possible, but we allow class authors
[1:15] to deviate from those constraints with the caveat
[1:17] that custom code requires custom compliance.
[1:20] Class authors have to write hooks and boilerplate
[1:22] to work with our constraints.
[1:24] The example relevant to this talk is manual declaration
[1:26] of dependencies rather than auto detection.
[1:28] I'll discuss how to do that in the section
[1:30] on writing classes.
[1:33] Cooking is part of the data build.
[1:35] It is responsible for transforming content
[1:37] from an editor format into something consumable
[1:39] by the user.
[1:40] In Unreal, this transformation is accomplished
[1:42] by what is in principle a simple and straightforward
[1:44] solution, load packages, run transform hooks, and save them.
[1:49] The hooks apply transforms described by the authors
[1:51] of content types in Unreal.
[1:53] Here on the right are the most common hooks
[1:55] for the transformation.
[1:59] Begin cache for cook platform data
[2:01] and is cache cook platform data loaded
[2:02] are used for the most expensive and flashy transforms.
[2:05] Texture compression, mesh simplification,
[2:08] and having cached in DDC derived data cache for years.
[2:11] But there are other transformations that are not cached.
[2:13] And besides transformations, there's object
[2:15] and byte manipulation work necessary to load
[2:17] and save a package.
[2:19] Most of the cookers work is spent doing those load,
[2:21] transform, save operations.
[2:23] We're experimenting with changes to this basic model,
[2:26] but in 5.8, this is the way.
[2:29] That's cooking, long time behavior, straightforward.
[2:32] What is incremental cooking?
[2:33] It is an optimization.
[2:35] I put up the costs of the steps of a Lyra cook.
[2:37] It takes 145 seconds.
[2:40] Loading and saving every package that should be staged
[2:43] to the runtime dominates the cook.
[2:45] The remainder is relatively minor bookkeeping.
[2:47] This is simple and straightforward, but also redundant
[2:50] and wasteful.
[2:51] During project development, project teams
[2:53] don't just cook once, they iterate and cook repeatedly.
[2:56] And loading and saving every package every time is redundant.
[2:59] Cutting that time out and just verifying
[3:01] that everything is up to date only takes four seconds.
[3:04] So we should follow, don't repeat yourself.
[3:06] Don't redo load save of a package
[3:08] that you already loaded saved in a previous cook.
[3:11] And a word, caching.
[3:13] In three words, caching, aka memoization.
[3:17] Cache invalidification is one of the two hard problems
[3:20] in computer science.
[3:22] It requires knowing the inputs.
[3:23] If your transformation is a mesh simplification
[3:25] with some heuristics and constants,
[3:27] then those constants are part of the input.
[3:29] And every asset is at least one dependency
[3:31] beyond the bytes of the source package,
[3:33] the C++ code that executes the transformation.
[3:36] That code couldn't, in theory, change at any point
[3:38] to say, oh, I want to insert this extra byte here.
[3:41] And in general, you have a giant soup of C++
[3:44] that is reading data from anywhere
[3:45] and you need to record all of those dependencies.
[3:49] We tried caching in a form of incremental cooking before.
[3:51] At that time, we called it iterative cooking.
[3:54] Incremental is a rename that we use
[3:56] to distinguish the two algorithms.
[3:58] And iterative cooking's general flaw
[3:59] was that it didn't capture all of the inputs.
[4:01] It only captured package dependencies
[4:03] and config dependencies.
[4:05] And this image on the right,
[4:07] I have illustrated its most common failure.
[4:09] Detecting that the mesh U asset on disk changes
[4:12] is insufficient.
[4:13] You also have to detect when the U static mesh serialize
[4:16] function changes and recook the mesh in that case as well.
[4:20] Despite missing some inputs, iterative cook
[4:22] worked well for some licensees.
[4:24] They didn't change code or other dependencies frequently.
[4:26] And it was a game changer to recook just one package
[4:30] when you're editing rather than recooking the entire game.
[4:33] But for many other licensees, working in some,
[4:35] but not all cases, is as bad as working in no cases.
[4:38] And most game teams abandoned iterative cooking
[4:40] for the slow but sure full recook.
[4:44] Incremental cooking, which we want to distinguish
[4:46] in that previous more naive version of iterative cooking
[4:48] is a promise to capture all of the dependencies.
[4:52] The C++ code most obviously, but also config values
[4:55] and asset registry queries and command line arguments
[4:58] and non-package files and others.
[5:00] Some of these we can capture automatically.
[5:02] U properties and C++ classes drive the auto-generated
[5:05] serialization and those are known to reflection.
[5:08] We can hook into T object pointer dependencies
[5:10] for package dependencies and into the config API
[5:13] for reads of config values.
[5:15] But others we can't.
[5:16] Custom serialization code,
[5:18] cached pointers and manager systems,
[5:21] reads of disk data outside the Unreal package system.
[5:24] For those we will have to capture the dependencies
[5:26] through maximum effort.
[5:28] They have to be manually declared
[5:30] and we will do so for all engine classes.
[5:33] Part of that manual effort however,
[5:34] does end up in licensee code.
[5:36] This is what I meant earlier by custom code
[5:38] requires custom compliance.
[5:40] But we hope these will be few and easy to declare.
[5:44] Here's an example class that demonstrates a dependency
[5:46] we can't auto-collect due to custom C++ code.
[5:49] They call the gconfig here, internally call our hooks
[5:52] and automatically report the config dependency.
[5:55] And this works fine for the first call
[5:56] at the top of the function.
[5:58] But the second call to gconfig is made once
[6:01] and the result stored in a static function variable.
[6:03] Since the call to gconfig is made just once,
[6:05] we record it as a dependency of the first instance.
[6:08] They get saved but then we don't see it
[6:10] and don't record it for any other instances.
[6:12] Meaning we don't recook their packages when it changes.
[6:15] This class therefore requires manual effort.
[6:17] We can declare the config value manually
[6:19] and the class is appended to class schema.
[6:22] We want to capture automatically wherever possible
[6:24] but when it is not, this kind of manual effort is required.
[6:29] So capturing dependencies is the basis of incremental cook.
[6:31] First to note about the two types of dependencies.
[6:34] Most obviously there are runtime dependencies.
[6:36] Runtime dependencies cause other assets
[6:39] to be pulled into the cook.
[6:40] One part of the cook process I haven't mentioned yet
[6:42] is the graph search.
[6:43] The cook loads and saves packages but which ones?
[6:46] The answer is the project settings in the asset manager
[6:49] tell it an initial list of assets,
[6:51] the levels, the characters, the global inventory items.
[6:54] And all of those assets have dependencies
[6:55] of other packages that they rely on.
[6:58] A material references textures,
[6:59] a level references quests and conversations
[7:01] that can occur in the level.
[7:03] The cook does a graph search over the packaged vertices
[7:06] and the runtime dependencies are its edges.
[7:09] This is independent of whether we are cooking
[7:10] incrementally or not.
[7:13] The other kind of dependencies are build dependencies.
[7:15] Build dependencies are dependencies
[7:16] that cause a package to change.
[7:18] I and I settings that parameterize transformations,
[7:21] shader files that have to be compiled into the package,
[7:24] an instance level package that gets embedded
[7:26] into the cooked version of a level
[7:27] that refers to that instance.
[7:29] These are the dependencies that we have to capture
[7:31] to know when we need to re-cook a package.
[7:35] So I note there is one interesting detail
[7:37] about incremental building.
[7:38] The build dependencies are metadata about the package.
[7:41] They are the list of things that can cause it to change
[7:43] and need to be re-cooked.
[7:44] The interesting point is that those build dependencies
[7:47] can also cause themselves a change.
[7:49] Does that cause a chicken and the egg problem
[7:51] because we need a new build dependencies
[7:52] to know that the old build dependencies will change?
[7:55] No, because the list of build dependencies cannot change
[7:58] unless one of the old build dependencies changes.
[8:01] In my example here, for a texture synthesis asset
[8:04] that transforms its input texture based on some settings,
[8:07] it might have an I and I values
[8:09] specifying the input texture in the settings.
[8:11] We capture those settings and that I and I value
[8:13] as the build dependencies.
[8:15] The jungle synthesis settings can change
[8:17] and cause a re-cook of the texture,
[8:19] but it's not possible that we need to consider
[8:21] the new urban synthesis settings as a build dependency
[8:24] unless one of our old build dependencies, the I and I values,
[8:27] changes to point to it.
[8:29] So we're safe.
[8:30] We can rely on a change in the old list of build dependencies
[8:33] to decide whether we need to re-cook
[8:34] to gather the new list of build dependencies.
[8:37] This is a relatively internal implementation detail,
[8:39] but I thought it was an interesting one
[8:41] and we do rely on it, so I wanted to mention it.
[8:45] I've mentioned some examples of build dependencies.
[8:47] What's the list we've encountered so far?
[8:49] I'll show the current list later, but to sum it up,
[8:52] any build dependency from any source
[8:53] can be described in a special function
[8:55] that a class author writes.
[8:57] That's our catch-all.
[8:58] Additionally, we have a short list of the types
[9:00] we've encountered used by engine classes.
[9:02] The source package itself, the C++ class schemas
[9:05] that we captured from an Unreal build tool,
[9:08] the C++ serialization code,
[9:10] which has to be manually declared,
[9:12] I and I values, and the bytes of other packages.
[9:15] There are a few extra types I'll mention later,
[9:17] but this is a good set to understand the gist
[9:19] of what we are collecting.
[9:22] Another breakdown in dependencies
[9:23] is time of runtime dependencies.
[9:25] Runtime dependencies are independent of incremental cooking,
[9:27] but are important for an understanding
[9:29] of cooking in general.
[9:30] There are multiple types of runtime dependencies in Unreal.
[9:34] Hard dependencies are required for the package
[9:36] to function and are automatically loaded.
[9:38] Soft dependencies are required to be available on disk,
[9:40] but can be loaded later in response to player action.
[9:44] Both of those are declared to the cook.
[9:46] True soft dependencies are not required
[9:48] to be present in the staged game.
[9:50] Something else can add them to the game if it wants them,
[9:53] and those are hidden from the cooker.
[9:55] Besides that hard versus soft access, there is one more,
[9:58] editor-only versus used in game.
[10:01] Editor-only references include preview content
[10:03] and build dependency-only content.
[10:05] They are marked by Unreal build tool or native serialization
[10:08] and are not included in the cook.
[10:10] That's it for the type of dependencies.
[10:12] Now back to how we gather build dependencies.
[10:15] So with incremental, we promise to gather all dependencies
[10:19] either through automation or through maximum effort.
[10:22] What so far can we gather automatically?
[10:24] The easiest to gather is class schemas.
[10:27] We have reflection data of classes,
[10:29] you properties from Unreal build tool.
[10:31] We can hash their names and types.
[10:33] That's an automatic solve for the previous pervasive problem
[10:36] for iterative cook.
[10:37] Changes to class U properties now automatically calls
[10:40] recooks of the packages using them.
[10:43] Other easy dependencies are those read
[10:45] through a relatively small API that we can hook into
[10:48] and record.
[10:49] Config files, console variables, F command line get.
[10:54] One caveat with those API recordings,
[10:56] caching is a problem as I mentioned before.
[10:58] Storing the results of a command line option
[11:00] in a function static bool is a common small optimization
[11:04] and doing that prevents us from noticing the read
[11:05] of that dependency on the next instance
[11:07] of the class that gets saved.
[11:09] We have a plan to detect those,
[11:10] I'll mention that in future work.
[11:13] A type of dependency that wasn't originally behind an API
[11:16] was the use of data from U objects in other packages.
[11:19] We knew that would be an issue since some of those
[11:21] are sneakily loaded by string and undeclared,
[11:24] so we created a T object pointer wrapper for U object star.
[11:28] We now can hook into the dereference of T object pointer
[11:31] to detect reads of other packages during the cook.
[11:34] Other dependencies are difficult or nigh impossible
[11:37] to capture automatically.
[11:39] A change to C++ serialization code is the primary example.
[11:43] C++ doesn't provide reflections,
[11:44] so how can we capture that?
[11:46] We have some ideas for heuristics,
[11:48] but for now we rely on manual recording of those.
[11:53] Fix it or fail is not the only option for classes
[11:55] with hidden or undeclared dependencies.
[11:57] We have an opt out system that we call hybrid incremental.
[12:01] If a package opts out of incremental,
[12:02] then it will always re cook,
[12:04] even if its dependency evaluation
[12:06] determines that it is unchanged.
[12:08] This is done on a native class by a native class basis.
[12:11] Packages contain multiple U object instances.
[12:13] For example, a material package has a U material
[12:16] along with U material expression
[12:18] and U material function inside it.
[12:20] The serialization of any of those classes
[12:23] could include hidden dependencies
[12:24] that impacts the bytes of the package containing them.
[12:27] So on a class by class basis,
[12:28] you can specify which classes are known
[12:30] to have hidden dependencies
[12:31] or at least are not known to not have hidden dependencies
[12:35] and opt those out.
[12:37] And this applies for each U object class,
[12:38] not just to each asset class.
[12:40] A material package could be opted out
[12:42] if it uses an opted out U material expression,
[12:45] even though the only asset in the package
[12:47] is the top level U material.
[12:50] Opting out is a default for all non-engine classes,
[12:52] but most projects will need to change that
[12:54] since many of their packages
[12:55] contain project specific classes.
[12:57] Instructions on how to do that later.
[13:00] Here are the two classes in engine
[13:02] that are currently marked as not skippable.
[13:04] Both are relatively new classes
[13:05] that we are still working on making compliant.
[13:10] To sum up how we improved the previous legacy iterative
[13:14] attempt at incremental cooking.
[13:16] Previously, we had dependencies from packages
[13:18] as calculated during editor save
[13:20] and recorded in the asset registry
[13:22] and a recording of every config setting
[13:24] that was read during cooking.
[13:25] Besides those, no other dependencies are tracked.
[13:28] Most importantly, class schemas were not tracked.
[13:31] Improving that model required slow and broad changes.
[13:34] T object pointer, gathering reflection data
[13:36] from property serialization,
[13:38] recording the list of class instances per package
[13:41] in the asset registry, creating the Zen server op log
[13:44] to store the dependency data
[13:46] and the increased sophistication
[13:47] of the cooker's search and load code,
[13:49] including skip only editor only
[13:51] and the ability to make other decisions like it.
[13:54] Put that all together and we have the plans
[13:56] for a fully robust system.
[13:57] We still have some edges to smooth, however,
[13:59] and it will require maintenance forever.
[14:02] No more maintenance and any other core feature, hopefully,
[14:04] but it is another one on the pile.
[14:09] That's it for background.
[14:10] Let's talk about how to turn it on.
[14:13] First, you need to set up some prerequisites.
[14:14] These are on by default in 5.8,
[14:16] but if you've turned them off during experimentation
[14:18] and earlier releases, you need to re-enable them.
[14:21] Derived data cache, cache is the most expensive transforms,
[14:25] which for most projects are dominated
[14:26] by shader compilation, texture compression,
[14:28] and mesh transforms.
[14:30] A cold, full, or re-cook is usually several times slower
[14:33] than a warm, full re-cook, where cold and warm
[14:36] refer to the population of DDC.
[14:39] Incremental cook, cache is more than DDC does,
[14:42] but they work together and DDC is required
[14:45] for good performance, even when cooking incrementally.
[14:48] DDC has been around since before UE5
[14:50] and their instructions for managing it online.
[14:53] It should be easy to set up,
[14:54] and of course, it is on by default.
[14:56] A newer piece of our tools,
[14:58] but that has still been present for several releases,
[15:00] is ZIN Server as the storage for DDC.
[15:04] Before ZIN Server, the binary bobs stored in DDC
[15:07] were stored as loose files on disk.
[15:09] ZIN Server instead aggregates them
[15:11] into its internal database
[15:13] and reduces the profile IOCost.
[15:15] That is doubly important when the DDC storage
[15:18] is on a network drive rather than the local disk.
[15:21] The settings for DDC that configure it to be stored
[15:23] in ZIN Server are stored in engine.ini.
[15:27] ZIN Server is required for incremental cook,
[15:29] but configuring it this way as the storage for DDC
[15:31] is optional, but highly recommended, and the default.
[15:37] Build machines are a special case,
[15:38] and there's one point specific to them.
[15:40] They can share a common close by network DDC server
[15:44] rather than having a local one that copies up
[15:46] to a shared DDC server.
[15:49] The instructions for setting that up
[15:50] are described at these pages.
[15:52] This helps with sharing of cache data between machines
[15:55] that trade off the responsibility
[15:56] for continuous integration builds.
[16:00] In addition to storing DDC,
[16:02] ZIN Server can also store the output of a cook,
[16:05] the U-asset files.
[16:07] This system was in beta in 5.7,
[16:10] and is now the default in 5.8.
[16:12] It is required for incremental cook.
[16:15] There might be some issues integrating it
[16:17] into your workflow.
[16:18] Notably, the intermediate cooked files
[16:20] are no longer available on disk,
[16:23] and you may have some tools that expected them to be there.
[16:26] You can disable it for an immediate fix when integrating
[16:28] by overriding this I&I value,
[16:31] but we recommend that you switch back to it
[16:33] as soon as possible.
[16:35] You can get the files back on disk if necessary
[16:37] by running the ZIN export command,
[16:39] or you can change your tools to talk to the ZIN server
[16:41] directly without needing the files present on disk.
[16:44] Switching the ZIN store is highly desirable,
[16:47] not just because it enables increment to cook,
[16:49] but also because it reduces IO costs,
[16:50] and because our future tools will be relying on it.
[16:53] If you have any problems using it,
[16:54] let us know on Epic Pro support.
[16:58] Incremental cook and ZIN store
[16:59] also require staging your files as IO store.
[17:01] This has been the default since 5.0,
[17:03] and we are relying on it for all our future tools.
[17:07] In case it is relevant for build farm workspaces
[17:09] or any other reason,
[17:10] the disk location of the ZIN store data for the cook
[17:13] is next to the DDC data,
[17:15] and that's determined by the environment variable
[17:18] UE local data cache path.
[17:20] The format of the data in that location
[17:21] is a private implementation detail.
[17:23] We won't provide deprecation when it changes,
[17:25] and you should access it through the ZIN servers API.
[17:30] And some notes about why incremental cook
[17:31] relies on ZIN store.
[17:33] The primary reason to use it is reduction of IO costs,
[17:36] and we could have implemented incremental cook
[17:38] to store its extra data in loose files,
[17:40] but we decided not to make that fallback path
[17:42] and spend the time instead on advancing cook features
[17:45] for our expected workflow.
[17:47] Cook package data and incremental cooks metadata
[17:49] is stored in a container called an Oplog,
[17:52] specific to the project,
[17:53] the project's workspace on disk,
[17:55] and the target platform.
[17:57] Oplog is short for operations log,
[17:59] and is a common technique in database design
[18:01] to efficiently avoid data races.
[18:03] Operations are given a sequence order,
[18:04] and the current state is defined by the in-order traversal
[18:08] of those operations.
[18:10] From the perspective of the cook,
[18:11] this implementation detail is hidden,
[18:12] and the Oplog is used as a key value store
[18:15] where the key is package name,
[18:16] and the value is the cooked package plus its metadata.
[18:20] The most important metadata for incremental cook
[18:22] is the list of dependencies.
[18:24] We will add other data in the future,
[18:26] and there's an interface for writing your own metadata
[18:28] as well through iCook artifact.
[18:30] The API for all this reads and writes data
[18:32] as compact binary, which is similar to JSON,
[18:35] but is binary encoded instead of text encoded.
[18:38] Our preferred tool for viewing the data in ZIN server
[18:41] is the HTTP interface it serves up.
[18:43] You can click through from the dashboard to your Oplog
[18:45] and see the list of packages,
[18:47] and click on each one to materialize the files on the disk,
[18:50] or view the compact binary as JSON.
[18:54] That's it for prerequisites,
[18:56] proceeding to the config values
[18:57] specific to incremental cook.
[19:00] Incremental cook relies on the collection of dependencies.
[19:02] This is enabled by default in 5.8,
[19:04] and the legacy iterative system that skips it
[19:06] is toggled off.
[19:08] There's a small cost to this collection.
[19:10] It costs a few percentage points of CPU time
[19:12] and increased storage usage.
[19:14] The percentage value is about the same
[19:16] on small projects and big projects.
[19:20] Collection of the dependencies is on by default,
[19:22] but cooking incrementally using those dependencies is not.
[19:25] By default, all packages are re-cooked every cook,
[19:28] as they were in 5.7 and earlier.
[19:31] The recommended way to cook incrementally
[19:32] is to pass in the command line argument
[19:34] dash cook incremental.
[19:36] This will make that single invocation of the cooker
[19:38] cook incrementally.
[19:40] There's an INI setting to manage the same behavior toggle
[19:43] as the command line,
[19:44] but we are recommending not turning that on for 5.8.
[19:47] Wait until we have finished bulletproofing
[19:49] every edge case before turning it on
[19:51] automatically for all cooks.
[19:53] For local cooks to the editor,
[19:54] rather than typing in an additional command line option,
[19:57] there's some settings you need to click.
[19:59] These can be left on most of the time for local work,
[20:01] but you will need to uncheck them manually
[20:02] if you notice any suspicious behavior
[20:04] that might be related to incremental cook.
[20:06] Suggest that workflow to your content creators with caution.
[20:09] You do not want to train them to always try a full re-cook.
[20:14] There is standard guidance that we expect to be given
[20:16] for a long while yet until incremental cook
[20:19] has proven itself conservative
[20:20] for most projects over a long period.
[20:23] Do not cook release builds with incremental cook.
[20:27] Even a 0.1% chance of stale data being sent out
[20:31] to end users is too high.
[20:33] Incremental cook should be used for local cooks,
[20:35] CIS, and QA builds.
[20:38] Use a full cook when making your release candidate.
[20:43] I mentioned before that by default,
[20:44] all of the C++ classes in your project
[20:46] opt out of being incrementally skippable.
[20:49] This is to prevent us from making a bad assumption
[20:51] that from day one,
[20:52] all of your project's types
[20:53] have fully declared their dependencies.
[20:55] Once you've added or validated those,
[20:57] here's how you opt your types back in.
[20:59] Incremental class, script package, allow list,
[21:01] and editor.ini, it uses the special token project route.
[21:05] The Lyra sample project already has an example of doing that.
[21:09] If some of your types are compliant and others are not,
[21:12] add the incremental class, script package, allow list setting,
[21:14] and then add a deny list setting
[21:16] for each non-compliant type.
[21:19] Opting out classes is usually only needed for a short time
[21:22] because it is relatively easy to add the hidden dependencies,
[21:25] but sometimes it can be complicated
[21:26] and need to stay around.
[21:27] You world and you blueprint, for example,
[21:29] took us a while to implement.
[21:33] When you've done a cook that you wanted to be incremental
[21:35] or when you were unsure whether it was,
[21:37] how can you tell whether it is on?
[21:39] There are two log statements
[21:40] that indicate incremental cooking.
[21:42] The first is at the beginning of the cook,
[21:44] either log cook, full cook,
[21:45] or log cook, incremental cook is logged.
[21:49] The second is at the end of the cook
[21:50] and reports a number of packages cooked,
[21:52] either new or re-cooked, and a number of packages skipped.
[21:57] Other than logging by design,
[21:58] the output of the cook is supposed to be indistinguishable
[22:01] between re-cooked and incrementally skipped cooks.
[22:06] One of the desired features of incremental cooking
[22:08] is having a farm do most of the cook
[22:10] and having developers sync that down
[22:11] and incrementally cook on top of it.
[22:14] With Zen Store and incremental cook,
[22:15] this is done by exporting a snapshot from the Zen server
[22:18] that cooks the initial build
[22:20] and importing the snapshot into the Zen server
[22:22] that is cooking incrementally.
[22:24] The farm machine cooks and after it is done,
[22:26] the entire build script calls OplogExport.
[22:29] Zen Store cooks still include some files written to disk
[22:33] rather than the Oplog.
[22:35] We expect to reduce these in the future,
[22:36] but always support them.
[22:38] To transfer cook results between machines,
[22:40] you need to include those in the Zen server snapshot.
[22:44] Zen OplogExport does the export with an optional arguments
[22:48] to embed those loose files before doing so.
[22:51] And the arguments of the export command
[22:52] allow you to direct the results to a file,
[22:55] cloud-based storage or another Zen server.
[22:58] On the developer's local machine,
[23:00] you use the corresponding Zen Oplog import command
[23:02] pointed to the same storage that you exported to,
[23:05] and your state becomes the same
[23:06] as if you had previously cooked locally.
[23:09] You can now cook incrementally and incrementally skip
[23:12] any packages with no dependency changes
[23:14] from the farm's environment.
[23:18] That's it for how to turn on incremental.
[23:19] It is intended to satisfy the principle of it just works
[23:23] with the one dial being whether you pass
[23:25] dash cook incremental or not to the cook commandlet.
[23:28] But custom code requires custom constraints.
[23:31] And so we need to talk about the API you can use
[23:33] to make your C++ types compliant.
[23:36] If your types don't override, serialize, postload,
[23:39] pre-save or other functions used are in the cook
[23:42] or don't add hidden dependencies,
[23:43] then you won't need to use this API.
[23:45] But scrutinize your types carefully
[23:47] before you draw that conclusion.
[23:48] Sometimes U-class or U-struct code can be called
[23:51] from the cook entry points on other classes.
[23:55] First up, project management caveat.
[23:58] If your data build has false skips bugs,
[24:01] developers can fix those, fix a bad build
[24:04] by doing a full re-cook.
[24:06] If that becomes a common problem-solving technique
[24:09] because it happens frequently,
[24:10] then it will train yourself or your team
[24:12] to always try it whenever there is a weird error
[24:14] in the cooked results.
[24:16] And that training means that you pay the price
[24:18] for a full re-cook at times even long past
[24:22] the point of the missing dependency being fixed.
[24:25] Avoid getting into that situation.
[24:28] Unlearning those habits can take a long time.
[24:30] Air strongly on the side of caution
[24:32] before opting your types in to incremental cooks
[24:35] as part of your developer's local workflow.
[24:39] In your native class, there are two primary entry points
[24:42] for declaring dependencies.
[24:44] If your dependencies are global,
[24:45] shared by every instance of your class,
[24:47] then you can hash the value of your dependencies
[24:49] and the static append to class schema function.
[24:53] Like changing the class's U properties,
[24:55] any change to the hash created by this function
[24:57] causes a re-cook of every instance of the class.
[25:01] This is where you should add a version and bump it
[25:03] to manually record changes to the C++ serialization code.
[25:07] For dependencies that only occur on some of your instances
[25:10] or are parameterized by data on the instance,
[25:13] you implement the virtual onCookEvent function
[25:15] and handle platform cook dependencies event.
[25:18] This event in that function is called
[25:20] after a successful package saved during cook
[25:22] while collecting all of the automated dependencies.
[25:26] It is more expensive than append to class schema
[25:28] because it runs for every instance
[25:29] and stores some data for every instance,
[25:31] but is still cheap compared to loading and saving the package.
[25:36] Dependency is declared an onCook event
[25:38] or constructed through static functions
[25:39] on the fCook dependency class.
[25:41] These are the types that class has available in 5.8.
[25:45] File for non-package files on disk,
[25:47] package for dependencies on other packages,
[25:50] console variable in config,
[25:52] and native class in asset registry query.
[25:55] The asset registry query compares the list
[25:57] of package names returned by a query.
[25:59] It does not automatically add those packages
[26:02] as package dependencies.
[26:04] And finally, for everything else, a function type.
[26:07] You write a function, define its arguments,
[26:09] and report the function name and arguments to the cooker
[26:12] for calling again later in future cooks.
[26:15] That API for the function dependency
[26:17] touches on an important part of the algorithm
[26:19] that we need to make clear.
[26:21] When you record a cook dependency,
[26:22] you're not just recording a hash value,
[26:24] you're recording an explanation
[26:26] for how to calculate the hash value.
[26:28] You provide the explanation by passing through
[26:30] the function name and the parameters
[26:32] that should be passed to it.
[26:33] For a file dependency, you would provide
[26:35] the hash file function and the file name,
[26:38] and the cooker then knows to call the hash file function
[26:40] to read that file from disk and hash its content.
[26:44] At the beginning of the next cook,
[26:45] when deciding whether to skip the package,
[26:47] we will load those arguments,
[26:48] find the function name from the op log,
[26:51] run the function, and compare the function's new value
[26:54] or current value to the stored value
[26:56] that we also load from the op log.
[26:58] Those are equal skip if there's a different re-cook.
[27:02] These dependency functions are run every cook
[27:05] for every instance.
[27:07] You should make them use as little data as possible
[27:09] and be as fast as possible.
[27:12] Append the class schema on the other hand,
[27:15] is similar in principle to DGC keys.
[27:17] It is called once per process
[27:19] and does not need to be parameterized.
[27:21] Gather all the data you want and the order you want it,
[27:23] pass it to the hasher,
[27:24] and it is thrown into the class's schema.
[27:27] That schema is included in the overall hash
[27:29] for any package containing instances of the class,
[27:32] and if it changes, we re-cook.
[27:35] The native class schema hashes are collected automatically
[27:37] for any class instances in the package,
[27:39] so you can also record them manually if necessary.
[27:42] In on cook event, you can create a native class dependency
[27:44] and record the class name parameter,
[27:46] and in evaluation time, we read that parameter
[27:48] and look up the class's current schema hash
[27:50] for comparison to the stored version.
[27:54] Here's an example of Append the Class schema,
[27:56] the latest version used by you, Static Mesh,
[27:58] and UE5 main.
[28:02] This version has some changes beyond the version in 5.8.
[28:05] Those changes were added because the render and NANI teams
[28:07] found they were already bumping some DDC versions
[28:10] every time they changed C++ code,
[28:12] and they knew they needed to invalidate
[28:14] the incremental cook as well when those changed.
[28:17] Adding GUIDs and versions used in DDC keys
[28:20] is a commonly useful technique that we recommend
[28:22] for Append the Class schema.
[28:25] These two APIs together are an extent
[28:27] of the commonly encountered requirements
[28:29] for managing incremental cook code.
[28:31] There's one more point to consider
[28:32] that is relevant to some projects, cook artifacts.
[28:35] Cook artifacts manage runtime data
[28:37] that is loaded outside of Unreal's linker load system,
[28:40] outside of packages or bulk data.
[28:42] Examples in engine code include shader libraries
[28:44] and asset registry.
[28:46] The API for that is ICOOK artifact.
[28:50] Artifacts need to support incremental cook as well
[28:52] because they are commonly implemented
[28:53] by collecting data from packages that load and save,
[28:56] and in incremental cook, packages can be present
[28:58] in staging without being loaded and saved
[29:00] during the current cook.
[29:02] Therefore, ICOOK artifact has some functions
[29:04] to interact with incremental cook.
[29:06] In general, ICOOK artifacts manage files
[29:08] of your own format that are saved
[29:10] into the cook output directory or the ZinStore op log.
[29:13] ICOOK artifact has functions to incrementally load
[29:15] and invalidate those files.
[29:18] There are examples of using this API and the artifacts
[29:20] for the shader library, validation
[29:22] and the cookers global data.
[29:26] That's everything for the new code, you need the right.
[29:28] A lot to take in, but I think when viewed
[29:30] in the development environment with some engine classes
[29:32] to use as examples, it will be straightforward.
[29:35] And to the extent that it does not turn out to be the case,
[29:37] let us know on EPS and we'll continue documenting
[29:40] and improving it.
[29:42] Now let's talk about the diagnostic tools we have so far.
[29:47] The primary expected problem with incremental cook
[29:49] is what I mentioned before, stale data at runtime.
[29:52] This is caused by an event we call a false incremental skip.
[29:56] A package should have been recooked
[29:57] because if we were to recook it, it would be changed,
[30:00] but we didn't know that and skipped its cook
[30:01] and kept the old version.
[30:03] The primary tool we have for detecting these
[30:05] is incremental validate.
[30:07] This is a cooker mode that is intended to run repeatedly
[30:09] in a persistent workspace that keeps syncing new changes.
[30:13] You can invoke it after syncing by passing dash
[30:15] incremental validate to the cook commandlet
[30:17] or by running the incremental validate build graph task.
[30:20] It works by calculating whether it should skip
[30:22] each package as normal for incremental cook,
[30:25] but then saving the skippable packages anyway
[30:27] and comparing the new version against the old version
[30:30] that it would have kept.
[30:31] It is built on top of the diff only technology
[30:33] we've had for the past 10 years
[30:35] for investigating indeterminism
[30:37] and provides the same feedback
[30:38] about what is different in a new package.
[30:40] C++ call stacks and new property names
[30:42] along with other data.
[30:44] Use that information to find the code
[30:46] that has hidden dependencies.
[30:48] A common failure that incremental validate reports
[30:50] is that C++ serialization changed
[30:52] without a bump to append to class schema.
[30:56] By default, incremental validate
[30:57] does not modify the workspace,
[30:59] but you can change that and let it write new versions
[31:01] after diagnostics with the dash incremental validate
[31:04] allow write parameter.
[31:06] Unfortunately, the determinism problems
[31:08] that cause the creation of the diff only tools
[31:10] still exist in various places today
[31:12] and we continue fixing them as we find them
[31:14] and they cause a problem for incremental validate.
[31:17] The algorithm gets confused as a change
[31:19] to the package that it didn't predict.
[31:21] It's a good idea to fix indeterminism issues
[31:24] along with false incremental skips.
[31:25] You should use incremental validate job
[31:27] to diagnose both of those.
[31:31] Here's some sample output from incremental validate.
[31:33] This is a complicated case and export changed
[31:36] the U objects and F names that serialized
[31:39] and that creates several knock on diffs
[31:41] in the packages header.
[31:43] This one was caused by indeterminism
[31:44] in a field that lists optional imports.
[31:47] The field was not needed at runtime
[31:48] and removing it fixed the diff.
[31:51] This one was more typical.
[31:52] It shows that a single value in an export has changed.
[31:56] This one was again indeterminism,
[31:57] a single integer in a U object
[31:59] that was calculated indeterministically.
[32:00] We fixed it by updating the calculation
[32:02] of the value to be deterministic.
[32:06] The next tool, incremental compare
[32:08] gives less diagnostic information
[32:10] but is simpler and gives one extra piece of information
[32:12] that incremental validate does not.
[32:14] It runs cooker twice back to back first incrementally
[32:17] and then a full re cook and reports
[32:19] ads, modifies and deletes.
[32:22] Incremental validate does not report the ads and deletes.
[32:24] You need incremental compare for those.
[32:26] Some bugs can cause missing or added runtime dependencies
[32:29] in the incremental cook and incremental compare
[32:31] reports when there is results
[32:33] in a different set of stage packages.
[32:36] Incremental compare runs outside the cook
[32:37] so it is only available as a build graph script.
[32:40] After the two cooks, it runs a diff cook command
[32:42] that to compare the two sets.
[32:46] Those are the tools we have for diagnosing false skips
[32:48] but what about the opposite problem?
[32:51] A false re cook is when incremental cook
[32:53] decides it needs to re cook a package
[32:55] but the package turns out to be identical.
[32:57] False re cooks are less problematic than false skips
[32:59] because they are only a performance cost
[33:01] rather than the incorrect runtime behavior
[33:03] but fixing them is important for optimizing your cook.
[33:06] Recall the end of cook log message I mentioned
[33:08] that reports how many packages were incrementally skipped.
[33:11] If the skip number is lower than you expect
[33:14] for a small set of changes
[33:15] then you should investigate whether false re cooks occurred.
[33:19] Run the incremental cook with the command line
[33:21] dash cook dot diagnostic dot modified.
[33:24] It will write out a file with the end of cook
[33:25] with an explanation for why each re cook package was re cooked.
[33:29] For each one it prints out the top level reason
[33:31] for the re cook either the target domain key change
[33:34] or a more edge case reason such as not previously cooked.
[33:37] And if the target domain key change
[33:39] it prints out which dependencies caused it to change.
[33:42] In this case the BP sky sphere package re cooked
[33:45] because you static mesh is class schema changed
[33:47] and the package contains a you static mesh.
[33:51] You should investigate the code making a dependency
[33:52] if it seems spurious.
[33:54] For now this metric doesn't report
[33:56] whether the package ended up different
[33:57] it just reports why it re cooked.
[34:01] Another tool for understanding the dependencies of packages
[34:04] you can look at the list of dependencies
[34:05] for a package in the metadata in the Oplog.
[34:08] The Oplog is viewable in the HTTP dashboard
[34:10] provided by Zen server.
[34:12] This is the recommended mechanism for viewing package data
[34:14] and metadata stored in Zen store cook results.
[34:18] Navigate to the dashboard at the Zen servers host name
[34:20] and port by default local host 8558.
[34:24] The projects available in workspaces reported
[34:26] to Zen server listed there click on the project
[34:28] in the workspace you want and then click the target platform
[34:30] link for the cook you want.
[34:32] And then this displays the list of cook packages
[34:34] searching click on the package you want.
[34:36] This that page is where you could download the package data
[34:39] it also has the cook artifacts that contain the dependencies
[34:41] which is what's on the screen to the right.
[34:43] Here we see the be weapon fire package
[34:45] has various dependency types function package config
[34:50] native class and redirection target.
[34:54] It has further data for build dependency sets
[34:56] a performance feature we are still developing.
[34:58] This view will remain the recommended view
[35:00] for the dependency features we continue to add.
[35:03] Viewing those dependencies can give you a sense
[35:05] of how broadly some of your packages gather
[35:07] build dependencies compared to others.
[35:11] False recooks are one drain on performance
[35:12] of incremental cook but there is another
[35:14] the overhead that occurs every cook.
[35:16] We call this the null recook time
[35:18] because it is the time observed
[35:19] when no changes have occurred.
[35:21] It includes a prologue dependency evaluation
[35:24] in an epilogue the prologue is engine
[35:27] and cook command let's start up time.
[35:30] The epilogue includes updating cook artifacts
[35:32] and calculating chunk assignments.
[35:34] And in the body of the cook we have to evaluate
[35:36] all of the incremental dependencies
[35:38] which takes a seconds to minutes
[35:40] when the package counts are in the thousands to millions.
[35:43] We're continuing to profile and optimize the null recook
[35:46] both to cash more of its calculations
[35:47] and to reduce the time taken for the operations
[35:50] that can't be cached.
[35:51] You may want to do the same to look at engine issues
[35:54] that are disproportionately large on your project
[35:56] or to look at some of your own functions
[35:58] that you have in the prologue and epilogue
[35:59] and optimize those.
[36:02] Here's my favorite profiler view of the Lyra null cook
[36:05] it's from Superluminal a third party profiler
[36:07] which uses event tracing for Windows.
[36:10] It's the standard child display in the butterfly view
[36:12] that is a feature of many profilers.
[36:15] In this case we can see 22 seconds
[36:17] for the body of the cook command let
[36:19] and of that nine seconds are in startup packages
[36:21] five in global shaders, two in asset registry
[36:24] and 2.7 in dependency evaluation.
[36:27] Dependency evaluation is the lowest hanging fruit here
[36:30] but reducing unnecessary startup packages
[36:32] will get the biggest long-term gains.
[36:35] Unreal Insights is another profile that we use
[36:37] and it sometimes provides information
[36:39] that the third party profilers do not.
[36:41] It relies on manually coded events
[36:43] but we have thousands of those now
[36:44] and it gives a pretty complete picture.
[36:46] In the case of this Lyra null cook
[36:48] it's giving roughly the same information
[36:50] as third party profiler but you should check it out
[36:52] as a first pass for investigations
[36:54] that it often directs you immediately to the hotspots.
[36:59] That's it for the diagnostic tools
[37:00] going back to the topic of robustness testing
[37:02] what kind of errors can you expect?
[37:05] The most difficult to diagnose is a false skip
[37:08] after an undetected change to native serialization.
[37:11] The symptom is a crash in package serialization
[37:14] with the victim often different than the cause.
[37:17] When an incrementally cooked build crashes in serialization
[37:20] start by checking out change history and source control
[37:23] to see if any class has recently changed
[37:25] native serialization without a version bump.
[37:28] Stay warning replays on the other hand
[37:30] are the easiest to diagnose.
[37:31] A warning existed, there was a fix for it
[37:33] but the warning is still being printed when cooking
[37:36] and the warning is prefixed with incremental replay.
[37:39] Incremental replay means that we are skipping
[37:41] the re-cook of the package but when it last cooked
[37:43] it logged warnings or errors and we recorded them
[37:45] for replay every time the package is skipped.
[37:48] If the problem should be fixed but the incremental replay
[37:50] remains then you have a missing dependency
[37:52] that you need to add to detect the presence of the fix.
[37:57] The other class of difficult problems
[37:58] are the ones that you overlook.
[37:59] A mesh was modified but it still displays the old value
[38:03] or behavior of an enemy was supposed to be changed
[38:05] but it is not.
[38:06] These could be caused by for example
[38:08] an undetected change to a config value.
[38:10] To find these we recommend strongly relying
[38:12] on incremental validate to give you the rigorous
[38:14] and precise information and to repeat the guidance
[38:18] from earlier do not cook release builds
[38:20] with incremental cook.
[38:22] Don't allow the possibility of overlooked stale content
[38:25] going out to end users, do full cooks for release candidates.
[38:30] Some discussion of the results we've seen internally
[38:32] on our test projects and production projects.
[38:36] Lyra designed to be the smallest project
[38:38] that demonstrates everything, cooks around 4,000 packages
[38:41] and even a full cook is quick at 2.7 minutes.
[38:44] The meaning of quick is context sensitive however,
[38:47] what is quick for CIS is not quick for local iteration.
[38:50] A no cook is 28 seconds, a five times reduction,
[38:53] a better workflow for local iteration.
[38:56] City sample has eight times as many packages
[38:58] and five times a full cook time at 14 minutes.
[39:00] A no cook is only 2.5 times the no cook time of Lyra
[39:04] at 68 seconds so better relative improvement.
[39:07] And Fortnite 1.5 million packages, 10.5 hours
[39:11] of single process cook time.
[39:13] Fortnite is big enough to benefit from multi-process cook,
[39:15] I've shown the timings for one, four and eight cook workers.
[39:19] The eight cook worker time is 1.5 hours,
[39:21] a dramatic improvement over single process
[39:23] but still far too high for frequent feedback
[39:25] on the build farm.
[39:27] A no cook that brings that time down to 30 minutes,
[39:31] ironically a few minutes longer in the multi-process case
[39:34] because of the time to spin up cook workers.
[39:36] Note that the no cook is not an empty cook
[39:38] in Fortnite's case because some packages,
[39:40] the classes I mentioned earlier,
[39:42] are not incrementally skippable for now.
[39:45] So part of that 30 minutes is a recook of 2,500 packages.
[39:50] I mentioned so far the full cook and no cook times
[39:53] but those don't cover the case of invalidations
[39:55] whether genuine from churn or spurious.
[39:59] For your effective performance under production churn,
[40:01] the typical cook, how much of the cook surface
[40:03] you are commonly causing to recook
[40:05] from the changes going in is what's important.
[40:08] On Fortnite that typical cook is 611,000 packages,
[40:11] about one third of the full cook number of packages
[40:13] and that cuts our one hour savings
[40:15] down to only 35 minute savings.
[40:18] On your projects, hopefully the recook count
[40:20] will not be so high because you will have fewer engine
[40:22] changes and many of your asset types
[40:24] will rarely need to be recooked.
[40:26] For us on Fortnite this invalidation rate
[40:28] is a high priority to optimize.
[40:30] It's still second in priority after the no cook however,
[40:32] we think that the no cook is more important
[40:34] for making feasible some improvements to local workflows.
[40:39] For robustness results internally,
[40:40] we've been using incremental cook
[40:41] on large test projects with production churn
[40:43] and scrutinizing it for errors
[40:45] that are caused by incremental cook.
[40:47] We also run incremental validate on that churn.
[40:50] In 5.8, incremental validate reports 1,600
[40:52] of our test packages that have false skip errors
[40:55] out of millions of packages
[40:56] but most of those are due to indeterminism.
[40:59] The errors that are confirmed to be caused
[41:01] by hidden dependencies which we know
[41:02] because they go away when we force a recook occur rarely
[41:05] around one in a thousand submissions.
[41:08] Again, we expect licensee results to be
[41:09] at a higher robustness level because of a reduced number
[41:11] of changes to the code that drives
[41:13] your engine on the issue assets.
[41:17] That's the summation of everything you should expect
[41:19] from incremental cook in 5.8.
[41:20] We're still working on it for multiple reasons.
[41:23] We have some known improvement ideas
[41:25] that I'll talk about next.
[41:27] Beyond that though, we expect to continue maintaining
[41:29] and improving the system.
[41:31] Here are the ideas that are immediately on our mind.
[41:34] For robustness patching some of the holes I mentioned.
[41:37] The biggest source of undeclared dependencies
[41:39] is C++ serialization changes.
[41:41] Is there a way we can detect those?
[41:44] A simple idea for a heuristic is to add markers,
[41:46] macros or otherwise and C++ files and functions
[41:49] that indicate when the source code of the function changes
[41:52] there should be an automatic bump to the class schema
[41:54] for classes using the function.
[41:57] And that can be enforced by Unreal build tool.
[42:00] For example, the virtual UObject serialize function
[42:02] on a class.
[42:03] Maybe we can even automatically add those serialize functions
[42:06] to the class schema hash.
[42:09] Command line tracking is a current hole
[42:11] in dependency tracking.
[42:13] Command line flags are parsed for many classes
[42:15] and some of those change cook behavior.
[42:17] We have a plan designed for a new API to replace
[42:19] the manual calls the FParsParam on F command line git.
[42:23] Using that API will automatically add dependency
[42:26] on the parsed token to the package
[42:28] that is active when it is called.
[42:30] And for the static function variables
[42:32] that I gave you an example of earlier,
[42:34] we haven't thought of a way to automatically handle those
[42:36] but we have thought of a diagnostic we can use
[42:38] to detect them and then manual review
[42:40] of the detection reports can lead to adding
[42:42] the required manual dependencies.
[42:45] The idea is to cook twice in the same process
[42:47] and report any differences in dependencies recorded
[42:50] between the two cooks.
[42:53] For performance, our immediate next plans
[42:54] are around improving no cook time.
[42:57] We could evaluate dependencies in parallel.
[42:59] They're currently evaluated in serial.
[43:01] That's two seconds in a library cook
[43:02] but multiple minutes in larger cooks.
[43:05] We also plan on profiling and optimization
[43:07] of the single threaded calls
[43:08] for system specific dependency calculations.
[43:10] U materials and U blueprints
[43:12] are the highest calls currently.
[43:14] And we plan to change the engine's I cook artifacts,
[43:17] asset registry and shader libraries
[43:19] to do more of their finalization incrementally
[43:22] and avoid redundant calculations every cook.
[43:25] Unrelated to CPU time
[43:26] but still an efficiency feature of the cook,
[43:28] we plan to fix a case of unbounded disk space usage
[43:31] in the incremental cook op log.
[43:33] As changes are made to the project over time,
[43:35] packages are marked deleted or no longer referenced.
[43:38] Currently, those deleted assets remain in the op log
[43:41] taking up disk space if nothing else.
[43:43] This is not yet a significant issue
[43:45] because full op log clears still happen
[43:46] from time to time and clear those out.
[43:49] But as full op log clears become rarer,
[43:51] pruning these unused assets will be more important.
[43:54] We plan to add a pruning step
[43:56] to Zen servers op log based on timeouts.
[44:00] And lastly, improvements to the tools.
[44:02] Incremental validate and incremental compare
[44:03] give good feedback
[44:04] but they rely on being run ahead of time
[44:06] or on the problem being reproducible.
[44:08] What about examining a staged incremental cook
[44:11] for false skips after it's already been made?
[44:13] The opportunities are somewhat limited
[44:15] because the intermediate data is not saved
[44:17] but there may be some good diagnostics we can find anyway
[44:19] and maybe there's debugging data we can save
[44:21] to enable even more.
[44:23] More concretely, I mentioned that incremental compare
[44:25] provides less diagnostic data than incremental validate
[44:28] which it does because it examines only
[44:30] the on disk output of the cook
[44:31] rather than reading data from memory during the cook.
[44:34] We want to try improving it by getting call stacks
[44:36] for the bytes that differ
[44:38] based on reading the packages into a buffer
[44:41] and the same way that incremental validate
[44:42] gets those call stacks by monitoring the differences
[44:45] when the packages are written out to a buffer.
[44:49] And some improvements planned to the C++ API,
[44:52] the current function dependency requires
[44:54] writing custom martialization code
[44:56] for the arguments that you want to record for your function.
[44:59] We want to replace that with the U struct
[45:00] containing your arguments which then gets automatically
[45:02] marshaled using Unreal build tools reflection.
[45:06] All of that is currently on our backlog
[45:08] but we're also interested in hearing from you
[45:09] about how incremental cook works for your cases
[45:11] and what we should prioritize for improvement.
[45:14] Please give incremental cook a try on your project
[45:16] and let us know how it goes.
[45:18] That's all for my presentation, thanks for listening.
[45:21] Thanks Du pref.
[45:25] Once again thank you.
[45:27] Thank you everybody.
[45:33] Thanks.



---

## Captured Frames

- [2:37] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_000.jpg
- [4:07] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_001.jpg
- [5:50] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_002.jpg
- [14:20] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_003.jpg
- [15:05] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_004.jpg
- [16:08] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_005.jpg
- [17:52] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_006.jpg
- [20:26] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_007.jpg
- [21:02] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_008.jpg
- [21:46] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_009.jpg
- [22:16] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_010.jpg
- [30:02] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_011.jpg
- [31:35] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_012.jpg
- [39:12] tutorials/frames/incremental-cooking-in-ue-57-a-dive-into-the-ue-cook-pipeline-unreal-fest-chicag/frame_013.jpg

---

## Structured Notes

### Core Technique
Enabling and complying with **Incremental Cook** — Unreal's memoized cook that skips re-cooking packages whose dependencies have not changed — covering its prerequisites (DDC, ZenServer, ZenStore, IoStore), the opt-in config, the C++ compliance burden for custom classes, and `IncrementalValidate` for catching false skips.

### Summary
A conference talk by **Matt Peters** of Epic's Foundation Core Data Pipelines team, who owns most of the code in `UCookOnTheFlyServer`. Cooking is load → transform → save, and loading/saving every package every iteration dominates the cost. Incremental Cook memoizes that, but caching is only as sound as its dependency capture — and the previous attempt, **iterative cooking**, failed precisely because it captured only package and config dependencies, missing C++ code changes. The rename to "incremental" marks the promise to capture *all* inputs. Some are automatic (reflection-driven serialization, `TObjectPtr`, the config API); the rest must be **manually declared**, which is the compliance burden the talk exists to explain. Because a false skip means stale data shipping to users, project C++ classes are opted **out** by default, and release builds should always use a full cook.

### Key Steps
1. **Understand the cost being attacked.** A full Lyra cook profiles at `UCookOnTheFlyServer::TickMainCookLoop` **145,122.86** with `PumpLoads` **97,255.53** and `PumpRuntimeSaves` **47,593.27** dominating; the incremental equivalent is **4,523.59**, almost all in `PumpRequests` `[frame_000]` `[transcript 2:35-3:03]`.
2. **Know why the previous attempt failed.** Iterative cooking captured only package and config dependencies. Detecting that a mesh `.uasset` changed is insufficient — you must also detect when `UStaticMesh::Serialize` changes `[transcript 3:49-4:19]`. Working in some but not all cases proved as bad as working in none, and most teams reverted to full recooks `[transcript 4:33-4:41]`.
3. **Know what is captured automatically**: UProperties and reflection-driven serialization, `TObjectPtr` package dependencies, and reads through the config API `[transcript 5:00-5:14]`.
4. **Know what is not**: custom serialization code, cached pointers in manager systems, and disk reads outside the Unreal package system — these must be declared by hand `[transcript 5:15-5:31]`. The worked example is a `GConfig` read cached in a `static` function variable: because the call happens once, the dependency is recorded against only the first instance `[transcript 5:44-6:05]`.
5. **Prerequisite — DDC.** Required even when cooking incrementally; a cold full cook is several times slower than a warm one. On by default `[transcript 14:21-14:55]`.
6. **Prerequisite — ZenServer as DDC storage.** Aggregates DDC blobs into a database instead of loose files, cutting IO cost — doubly so when DDC lives on a network drive. Configured in `Engine.ini`. Optional but highly recommended and the default `[transcript 14:56-15:33]`.
7. **Prerequisite — ZenStore as cook output** `[frame_005]`. Default in **5.8** (beta in 5.7), and **required** for incremental cook. Setting: `BaseGame.ini:[/Script/UnrealEd.ProjectPackagingSettings]:bUseZenStore`; commandlines `-zenstore` / `-skipzenstore`; also exposed as Project Settings → Packaging → "Use Zen Server as cooked output store" `[frame_005]` `[transcript 16:00-16:13]`.
8. **Expect a workflow break.** Intermediate cooked files are no longer on disk, which breaks tools that expect them. Fix immediately by overriding the ini value, then switch back; recover files with `zen export`, or point tools at the Zen server directly `[transcript 16:15-16:43]`.
9. **Prerequisite — IoStore staging.** Default since **UE 5.0**; `BaseGame.ini:[/Script/UnrealEd.ProjectPackagingSettings]:bUseIoStore` `[frame_005]` `[transcript 16:58-17:05]`.
10. **Where the data lives.** ZenStore data sits alongside DDC data, governed by the **`UE-LocalDataCachePath`** environment variable. The on-disk format is a private implementation detail with no deprecation guarantees — access it through the Zen server API `[frame_005]` `[transcript 17:07-17:28]`.
11. **Understand the Oplog.** Cook package data and incremental metadata live in an **Oplog** (operations log) scoped to project + workspace + target platform — a database technique giving operations a sequence order so current state is the in-order traversal `[transcript 17:47-18:08]`.
12. **Do not cook release builds incrementally.** "Even a 0.1% chance of stale data being sent out to end users is too high." Use it for local cooks, CIS and QA; use a full cook for the release candidate `[transcript 20:23-20:40]`.
13. **Opt your classes back in.** All project C++ classes opt **out** by default, to avoid assuming day-one dependency compliance. Enable in `Editor.ini:[CookSettings]` with `+IncrementalClassScriptPackageAllowList=Allow,<ProjectRoot>` — Lyra ships an example `[frame_008]` `[transcript 20:43-21:07]`.
14. **Opt individual classes out** with `+IncrementalClassDenyList=/Script/MyProject.MyClass` for types that are not yet compliant `[frame_008]` `[transcript 21:09-21:18]`. Epic notes `UWorld` and `UBlueprint` took them a while to make compliant `[transcript 21:27-21:31]`.
15. **Turn it on** with a single dial: pass `-cookincremental` to the cook commandlet `[transcript 23:19-23:27]`.
16. **Confirm it engaged** via two log lines: at the start, `LogCook: Full cook` or `LogCook: Incremental cook`; at the end, counts of packages cooked (new or re-cooked) versus skipped. Otherwise the output is designed to be indistinguishable between the two `[transcript 21:39-22:03]`.
17. **Share cook state farm → developer.** The farm cooks, then the build script calls `zen oplog-export`; the developer runs `zen oplog-import` against the same storage and their state matches a prior local cook, so they can incrementally skip anything unchanged `[transcript 22:06-23:16]`. Zen cooks still write some loose files, so use the export argument that embeds them `[transcript 22:29-22:50]`.
18. **Diagnose false skips with `IncrementalValidate`** `[frame_011]`. A false incremental skip is a package that *should* have been re-cooked. The tool computes the skip decision as normal, then saves the skippable packages anyway and diffs new against kept `[transcript 29:52-30:31]`.
19. **Invoke it** as `-run=cook ... -incrementalvalidate`, optionally `-incrementalvalidateallowwrite` to let it write after diagnostics; or run `Engine\Build\Graph\Tests\IncrementalValidate.xml`, which uses the allow-write form in a persistent workspace `[frame_011]` `[transcript 30:12-30:19, 30:56-31:05]`.
20. **Read the output like `-diffonly`.** It is built on the decade-old diff-only technology and reports C++ call stacks and changed property names. A common finding is C++ serialization changing without a bump to the class schema `[frame_011]` `[transcript 30:31-30:55]`.
21. **Fix indeterminism alongside false skips.** Non-deterministic saves confuse the algorithm; a two-phase mode exists but fixing the indeterminism is better `[frame_011]` `[transcript 31:06-31:29]`. Worked examples: an optional-imports field that was not needed at runtime, and a single integer computed non-deterministically `[transcript 31:43-32:03]`.
22. **Check file history when hunting a hidden dependency** — it is often a change to native serialization `[frame_011]`.

### UE Systems / Blueprints / Settings
- **Cook hooks** — `BeginCacheForCookedPlatformData`, `IsCachedCookedPlatformDataLoaded`; used for the expensive transforms (texture compression, mesh simplification) that have been DDC-cached for years `[transcript 1:59-2:10]`
- **`UCookOnTheFlyServer`** — `TickMainCookLoop`, `PumpLoads`, `PumpRuntimeSaves`, `PumpRequests`, `TickCookStatus`, `PumpPollables` `[frame_000]`
- **Enable** — `-cookincremental` on the cook commandlet `[transcript 23:25]`
- **Opt-in config** — `Editor.ini:[CookSettings]` → `+IncrementalClassScriptPackageAllowList=Allow,<ProjectRoot>`; per-class opt-out `+IncrementalClassDenyList=/Script/MyProject.MyClass` `[frame_008]`
- **ZenStore** — `BaseGame.ini:[/Script/UnrealEd.ProjectPackagingSettings]:bUseZenStore`; `-zenstore` / `-skipzenstore`; Project Settings → Packaging → "Use Zen Server as cooked output store" `[frame_005]`
- **IoStore** — `BaseGame.ini:[/Script/UnrealEd.ProjectPackagingSettings]:bUseIoStore`, default since UE 5.0 `[frame_005]`
- **Related packaging ini values seen** — `UsePakFile=True`, `bUseIoStore=True`, `bUseZenStore=False`, `bCompressed=True`, `PackageCompressionFormat=Oodle` `[frame_005]`
- **Storage path** — `UE-LocalDataCachePath` environment variable; format is private, access via the Zen API `[frame_005]`
- **Transfer commands** — `zen oplog-export` / `zen oplog-import`, targeting a file, cloud storage or another Zen server `[transcript 22:26-23:08]`
- **Validation** — `-run=cook ... -incrementalvalidate [-incrementalvalidateallowwrite]`, `Engine\Build\Graph\Tests\IncrementalValidate.xml`, built on `-diffonly` `[frame_011]`
- **Log lines** — `LogCook: Full cook` / `LogCook: Incremental cook` `[transcript 21:44-21:47]`
- **Docs** — https://dev.epicgames.com/documentation/unreal-engine/using-zen-storage-server-as-cooked-output-store-for-unreal-engine `[frame_005]`

**Internal testing results — cook times (full vs null)** `[frame_013]`

| Project | Full cook packages | Full cook time | Null cook packages | Null cook time |
|---|---|---|---|---|
| **Lyra** (small) | 3,980 | 2.7 m | 0 | 28 s |
| **CitySample** (medium) | 32,467 | 13.8 m | 0 | 68 s |
| **Fortnite** (large) | 1,565,054 | 10.5 h SP / 3.5 h 4MP / 1.5 h 8MP | 2,546 | 30 m SP / 35 m 4MP / 35 m 8MP |

- **Why Fortnite's null cook is not zero** — some classes are still not incrementally skippable, so ~2,500 packages re-cook `[transcript 39:36-39:48]`
- **Multi-process irony** — the 8-worker null cook is a few minutes *slower* than single-process, because of cook-worker spin-up `[transcript 39:31-39:35]`
- **Typical (churn) cook on Fortnite** — 611,000 packages, about one third of full, cutting the saving from ~1 hour to ~35 minutes `[transcript 40:08-40:17]`
- **Robustness in 5.8** — IncrementalValidate reports ~1,600 false-skip errors across millions of test packages, most from indeterminism; errors confirmed to come from hidden dependencies occur around **one in a thousand submissions** `[transcript 40:50-41:06]`

> **Version discrepancy, worth knowing before you act on this.** The video title says
> **UE 5.7**, but the speaker repeatedly states the feature "is ready for use in **5.8**"
> `[transcript 0:11]`, that prerequisites are "on by default in 5.8" `[transcript 14:14]`,
> and the ZenStore slide reads "Default in 5.8" while noting the system "was in beta in
> 5.7" `[frame_005]`. **Treat 5.8 as the target release**; 5.7 appears to be the shipping
> version at talk time, not the version the feature lands in.
>
> **Whisper naming errors.** The transcript writes **"ZIN Server"** for `ZenServer` in the
> early passage, then spells "Zen Store"/"Zen server" correctly later — the same
> mangled-then-correct pattern seen elsewhere in this batch, and a reminder that one
> correct occurrence does not vouch for the rest. Also "Ucook on the Fly server" for
> `UCookOnTheFlyServer`, "gconfig" for `GConfig`, "I&I value" for `.ini`, and "cache
> invalidification" for cache invalidation. Slide text `[frame_005][frame_008][frame_011]`
> is the reliable source for every identifier above.
>
> **One frame missed its slide:** `[frame_007]` (20:26) caught a cut to the speaker rather
> than the "do not cook release builds" slide, so that warning is cited to narration only.

### Difficulty
Advanced

### UE Version
**UE 5.8** is the target release, despite the video title saying 5.7. The speaker states the feature "is ready for use in 5.8" `[transcript 0:11]` and that prerequisites are "on by default in 5.8" `[transcript 14:14]`; the ZenStore slide reads "Default in 5.8" and notes the system "was in beta in 5.7" `[frame_005]`. IoStore staging has been the default since UE 5.0 `[frame_005]`.

### Tags
pipeline, automation, cpp, advanced, ue5-7, ue5-8

---

## Related Entries
- [Designing Visuals, Rendering, and Graphics with Unreal Engine](designing-visuals-rendering-and-graphics-with-unreal-engine.md) — Epic's own engine-systems reference covering the same 5.7-era generation; shares pipeline-level engine internals
- [Nanite: Everything You Should Know [Unreal Engine 5]](nanite-everything-you-should-know-unreal-engine-5.md) — the mesh transforms this talk cites as among the most expensive DDC-cached cook steps
