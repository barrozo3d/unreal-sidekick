---
title: State of Virtual Production | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=5SJA1FfRPWs
author: Unreal Engine
ingested: 2026-08-06
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/state-of-virtual-production-unreal-fest-chicago-2026/
frame_count: 0
frame_status: pending-selection
---

# State of Virtual Production | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=5SJA1FfRPWs)
**Author:** Unreal Engine
**Duration:** 42m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py state-of-virtual-production-unreal-fest-chicago-2026 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello, everyone.
[0:02] Hello.
[0:04] Welcome to State of Virtual Production.
[0:07] My name is Brian. I'm one of the product managers on Unreal Engine.
[0:10] I'm going to be stepping you through a bunch of great new features in 5.8 and part of our virtual production roadmap.
[0:16] So we'll lead off with Composure.
[0:19] Our Composure reboot, like, launched in the last release, 5.7.
[0:23] During that time, we've seen a lot of great, you know, a great number of projects.
[0:27] Pick this up. A lot of people doing cool stuff.
[0:29] Like, a really good example of this is Dean here.
[0:31] If you're not following me already, he's got a great channel.
[0:33] He's done a number of deep dives on Composure.
[0:35] He's doing a lot of stuff and also showing how, like, kind of accessible the tool is, even to, like, smaller form creators,
[0:40] in addition to, like, large-scale productions.
[0:43] You know, a lot of work went into Composure, which touches, like, directly on the composing tools,
[0:50] but also, like, kind of this ecosystem of the workflow as a whole.
[0:53] So I wanted to highlight a particular feature, which is the media profile.
[0:57] Like, when we evaluated how to improve Composure, one of the big problems we saw was just how difficult it was to bring in media.
[1:05] Like, so if I want to bring in my camera feed, that was just a very cumbersome process in Unreal.
[1:09] It took, like, maybe five or six assets.
[1:11] You had to juggle all these different panels, and we've centralized that in the media profile.
[1:15] So there's a convenient button at the top of the toolbar to launch it.
[1:19] And this is just kind of your one-stop-shop for all of your inputs and outputs for video, right?
[1:23] So from here, in the same window, you can just add a source, pick where it's coming from, in this case, AJA.
[1:30] And you're going to immediately get, like, a nice preview of the image coming in.
[1:33] You see what you're getting. You don't have to jump around.
[1:36] You're very confident that you can bring this into your shot.
[1:38] And the same goes for the output, right?
[1:42] So you can add an output, pick the port, pick your frame rate, and start the capture right from this panel.
[1:52] For previewing purposes, this is also, like, kind of a place you can monitor the feed, like, at the same time.
[1:58] You don't necessarily have to send it out if you don't want to.
[2:00] You can see them both at the same time, and you can save the layout.
[2:04] So this comes up the same way every time, right?
[2:06] So a lot of times, you're doing a comp. You want to see your input. You want to see your output.
[2:09] Know that they're both running at the same time. Check them both.
[2:14] The media profile lets you do that all in the same place.
[2:18] The media profile is also tied in to the setup of your comp, right?
[2:22] So this is a quick example where you're creating a comp actor.
[2:25] And then when you go to set the texture for your plate, the media profile has this convenience menu.
[2:31] So if you set up your media profile, it's really easy to pick the feed from your media profile.
[2:37] And then likewise, if you want to send it out after you set up your comp, you don't have to go back to another window.
[2:41] You can do that directly from the composure panel.
[2:48] We've also made a lot of improvements to the keyer. This was definitely something that was a limitation in the old version of composure.
[2:55] So when you add a key of two options, you can choose a color, you know, likely green or blue, or you can also choose a clean plate.
[3:04] In 5A, we also have this nice little button that grabs the texture from the incoming feed.
[3:09] Just to make it easy to set that up. And then if you are using a color, we have this nice little preview that lets you pick the color a lot easier.
[3:17] You don't have to hunt around. Like depending on what your context is in Unreal, you might be looking at something else.
[3:24] This pops it up right there so you don't have to go hunt for the plate to pick the color.
[3:30] In addition to the color keyer, in 5A we've also added a Luma keyer just to give you more options for whatever shot you may have in your production situation.
[3:39] And then kind of last but not least, we've added support for ultimate masking.
[3:43] So if you use ultimate, you might be familiar with this, but there are some additional kind of color space considerations to make.
[3:49] And that's all built in to this ultimate masking pass to make that a little bit easier.
[3:55] And then likewise, this is set up the same way, tied to the media profile.
[3:58] So if you're bringing your key and fill through that, it's easy to pick.
[4:03] And then the last thing to be aware of is that, as I was mentioning, there are some special color considerations for how you do the blend.
[4:09] So you're going to want to set this ultimate blend on if you're an ultimate user.
[4:14] Beyond that, just from a quality standpoint, a lot of times we show test scenes with the LED wall, which is kind of like an easy key, right?
[4:24] So it's always perfect.
[4:25] So this is an example where we're starting to intentionally make a bad green screen.
[4:30] I think this one is actually a little bit too good still.
[4:32] But it's something that we've been taking it hard to try to make sure that our keyer is a great out-of-the-box offering.
[4:39] We know that you have other options, but at the very least, you're going to have something good to work with directly from Unreal.
[4:47] Kind of bringing this together is an Anambiz demo, right?
[4:50] So this is something we're just basically plugging.
[4:52] This is an ad for our team.
[4:54] And they're doing an Anambiz demo in the booth.
[4:57] So you can see composer in action live.
[4:59] And this is bringing it together like a lot of other parts of the virtual production ecosystem, like specifically performance capture for body and face.
[5:07] You're going to get some great acting.
[5:09] So I don't encourage you to check this out.
[5:11] They're doing it, I think, like five times.
[5:14] These are the times you won't be able to miss them.
[5:17] And then in addition, I'm told there's a musical guest.
[5:20] So the musical guest is both days at 1.45 and 6.05.
[5:24] I haven't seen this yet.
[5:26] I'm very intrigued to say the least.
[5:29] But definitely check this out to see composer in action.
[5:33] Because it's a great, great way of also, you know, in addition to like this kind of live broadcast setup, it can also be used for visualization.
[5:41] And so this is a different type of shot.
[5:44] And it's just showing how like composer can also be driven by sequencer.
[5:47] So in this case, the plate's being played back by sequencer, the camera's tracked, the camera's being driven by sequencer.
[5:53] And this has been a big point of emphasis, you know, adding to if you're already doing previs in the engine, potentially you can keep that going.
[6:00] Carry that all the way out through postvis as well.
[6:04] And so like in 5.8, a big emphasis here has been on our sequence of support, which is pretty limited in 5.7.
[6:09] Specifically, we now support spawnables, right?
[6:11] So if you have a whole bunch of shots, your shots are likely to be separate sequences with spawnable cameras.
[6:16] You can now reference those cameras in composure, as well as key all of the other properties in the composure composite actor.
[6:27] In terms of layers, so we have a couple new layers to bring up, which is really more performance driven than anything else.
[6:33] So we initially launched with the full shadow reflection catcher, right?
[6:36] So this is the higher quality option, and it uses dual scene captures.
[6:40] But for some of the other projects that are maybe targeting 60 FPS rather than 24 FPS, we have a couple of other options that are a little bit faster
[6:47] and allow you to make like a little bit of a trade off potentially if you want to bias towards performance rather than the full shadow quality.
[6:55] So the single light shadow is an efficient depth only option for shadows.
[7:00] And then we also have a planar reflection option, which uses a single scene capture and can run a little bit faster, right?
[7:08] So for some of the shows that are having trouble hitting 60, these might be better options for you than the full shadow reflection catcher.
[7:17] We also have a number of new passes.
[7:19] So here's a list.
[7:21] Like I wasn't sure how to show these, I think to a larger degree, I think people know what a blur at a dilation pass look like.
[7:27] But you know, this, this, the story of this, this particular area is just about like fleshing out our compositing speed, having it be a more fully fledged compositing system.
[7:35] So we have a number of new options here.
[7:37] I think that this is something that's going to continue like there's just a whole bunch of these, these types of passes that we want to make available that people are accustomed to.
[7:46] On the artist workflow side, there's been some work here just to help the help you manage the materials for the composite meshes that are the plates getting projected onto.
[7:55] So and this is just kind of showing how like you can decide your defaults, you can quickly apply like if you want to use a lit masked material that we provide versus the like the alpha one, like which is more for the key.
[8:08] You can also select a custom material.
[8:10] And we show the materials now in the panel so you can quickly see if you have the right one.
[8:15] A lot of times if you, if you are using the wrong one, you're the like the shots just not going to look very good.
[8:20] And you might be confused why.
[8:22] So this is hopefully giving you a better sense for how to fix up your materials.
[8:25] If you have a more complex setup.
[8:28] And then the last thing to mention is this ability to visualize the composite meshes.
[8:32] So like, if you use it in the last version, you know, you might have been aware that if you unpilot the camera, you know, the scene looks weird, right?
[8:39] Because the plate's being projected onto it.
[8:41] And you just can't really tell what's going on.
[8:43] If you wanted to move something, you're like, what am I seeing?
[8:45] Like you don't know how to pick it.
[8:47] And so that's where this visualize option comes in.
[8:49] If you visualize when not piloting, it's going to, it's going to put this like this little grid visualization on it.
[8:54] And it's easy.
[8:55] It's much easier to see like which mesh is which and actually select the one that you want.
[9:03] Last thing to mention is depth compositing.
[9:06] So depth compositing is kind of like an emerging area.
[9:08] And what we have in 5.8 is a little bit more forward looking.
[9:11] And what we've, what we've sought to do here is basically like lay the groundwork for potential future hardware and software integrations that use depth for, for keying.
[9:20] So this is a synthetic example.
[9:22] This is kind of how we developed the feature where we like basically rendered something out of movie render queue that was like perfect depth.
[9:28] And what this is showing is how this new actor works, which is called the composite depth mesh actor.
[9:33] And what that does is it basically takes a depth map and it basically creates a mesh using world position offset that acts as your composite mesh that basically shows up on the fly as needed.
[9:48] And here's an example of that in action.
[9:52] So this is some data that was provided to us by Leica and uses like a depth map that's provided to us as EXRs.
[10:01] So this is giving us the camera image as well as a depth image.
[10:04] And this is basically like the same idea as before with our synthetic example, but with like kind of a simple, you know, real world example.
[10:11] In this case, I'm just moving a box through to show how it's, you know, like, you know, moving it moving in space moving in depth relative to the, the movie camera image.
[10:25] Next up is motion design.
[10:28] So in live broadcasts, you never get, you don't get the opportunity to have a second take, right?
[10:33] So a lot of the development here has been really focused on playback reliability, making sure that, you know, the first time you play a graphic through it's smooth and reliable.
[10:43] So specifically, that's been a number of perform that has manifested itself in a number of performance optimizations to cloners, effectors, modifiers and shapes.
[10:52] There's also a load page option in rundown.
[10:54] So it basically allows you to like for each graphic preload it before you actually play it.
[10:59] There's also some logic that waits for content to load before taking in a page.
[11:04] So if you go to play it and it thinks it needs to like maybe build some more shaders, it's going to build those before it tries to play it rather than play it in a way that might have hitches.
[11:13] And there's also the ability to freeze a modifier.
[11:15] So you've already set up your content and you're not going to change it anymore.
[11:19] This option to freeze it can potentially give you a little bit more overhead for perf as well.
[11:26] Feature-wise, there is the motion design tools now allow for combined masking.
[11:31] This is something that I think is really, really common, just being able to combine multiple masks when you're creating a graphic.
[11:37] The motion design tools now support up to four masks being combinable.
[11:44] So that's something that wasn't available for that is now in place.
[11:48] Flow enhancement has to do with transition logic.
[11:50] So I think before in the old days, the transition logic had to be like saved with the level.
[11:56] So that meant if you had multiple levels, you would have to like basically reset this up every time.
[12:00] Now that's been like ascitized so you can save the transition logic, reuse it across multiple levels.
[12:08] And again, last but not least on the performance side, there's been a lot of stuff specific to text 3D.
[12:14] So this kind of gave this its own slide just because in addition to the performance enhancements, there's also added blueprint support.
[12:22] You weren't able to put text 3D components in blueprints until now.
[12:27] And there's also been a number of improvements for font scaling and extruding consistency, I think, especially with kind of the non-Latin characters.
[12:34] There are a lot of issues with our text and the way it displayed.
[12:37] There's more control over that now.
[12:40] Last but not least is the text shaping method.
[12:42] This is another like kind of finishing touch just to make sure that the text displays as accurately as possible.
[12:51] Next up is USD.
[12:52] So there's been a number of work.
[12:53] There's a lot of work happening in USD.
[12:54] Some of it is like, you know, going to appear later in future releases.
[12:59] But to me, the most important thing to highlight is this pregen workflow.
[13:03] And to me, the thing that's most interesting is that it's kind of conveying like a pivot from the way we looked at USD before and the way it's going to manifest itself in the engine in the future.
[13:13] So, you know, when you started out, like, you always thought of it like, well, with the FBX file, you know, you would just take this thing, you'd import it into the content browser, you'd be all good.
[13:21] So when USD came along, the initial thought process was basically like, well, we don't really love FBX, like, so this will just replace it.
[13:29] Right. So we just have a USD, we bring it into the engine, and we're all good.
[13:35] But in practice, you know, that's just not really how USD works.
[13:38] Like USD isn't just the file that you import, right?
[13:40] It's its own full composition system.
[13:42] And in the 5.8 release with this pregen workflow, it's starting to like pivot our thought process and like move the paradigm over to this idea that like the USD, like the USD ecosystem kind of lives on.
[13:58] Even after you import it into Unreal.
[14:01] And maybe Unreal is just a sense of being like the real time version of whatever this content is that you're using.
[14:06] So when you bring this in now, like, it's going to be aware of it.
[14:10] Like, I think the most interesting thing to me is that like, like in the FBX world, you would import it, you just throw away the old file.
[14:17] In this case, like, there's now like an awareness that the USD file may live on, right?
[14:21] So if I import the chess set the first time, right, it's going to maybe it brings in the whole thing.
[14:27] I can import it again, or maybe I changed something outside of Unreal into the chess set.
[14:31] And if I re-import it, it's going to be aware of all the pieces already.
[14:34] It's not going to re-import all those pieces.
[14:36] It's just going to give me something that has the deltas, and I'm able to version that once I bring it in.
[14:41] You know, there's a lot more to do here.
[14:43] And I think this is like, you know, there are more native workflows for USD that some of the other packages support.
[14:49] That's something that I think is going to like start to take more, that's going to evolve in Unreal.
[14:56] But to me, this is, I think, really promising because it's starting to treat USD more like it's supposed to, in terms of how you at least you bring it in.
[15:08] So next up we have performance capture.
[15:11] So there's been a number of...
[15:15] Audio didn't work.
[15:17] There was supposed to be a record scratch.
[15:20] But yep, that's Richard Graham.
[15:23] You might be wondering why he's not here presenting this section.
[15:26] Richard couldn't make it to Unreal fast, so I'm going to do my best impersonation of him without the accent.
[15:34] But there's been a bunch of great stuff in performance capture, right?
[15:38] So you saw some of that in the keynote.
[15:40] There's been a big emphasis on like, plusing out all of the tools around performance capture so that you can do a full shoot entirely in Unreal Engine.
[15:48] So this goes from like, bringing things in through LiveLang, monitoring it, managing the shoot and operating it as you go, and then also tying it into other tools like the Vcam.
[16:01] Ticking through the features, the first one to call out is the auto cameras.
[16:05] So in MoCAP Manager there's this convenience option to just drop some cameras in to your MoCAP scene.
[16:10] It'll follow them around and it'll just give you a nice view of what's going on.
[16:15] These are tunable all the same way that you would expect.
[16:18] But it's a nice out-of-the-box option that just lets you add some coverage during your shoot.
[16:25] There's also a face preview option, so when you've set up the faces, the MoCAP Manager will give you a live preview of that just to give you a quick glance at what's going on with your faces.
[16:40] We also have the ability to add and extend the MoCAP Manager, right?
[16:45] So the MoCAP Manager is actually a blueprint-based tool.
[16:48] Since a lot of operators are very familiar with doing this and a lot of operators like to have certain things that they need for their day-to-day ops,
[16:57] there's this ability to basically extend here.
[17:00] So the MoCAP Manager has this nice tool bar on the left.
[17:03] It's got a lot of space for you to add your own stuff.
[17:06] So now there's a mechanism to write up your own Editor Utility Blueprints and then just plug them in there.
[17:12] So your Editor Utility Widget or Widgets can go there as well alongside the ones that we provide.
[17:23] And then last but not least, there's LiveLink Hub.
[17:25] So LiveLink Hub is now production-ready.
[17:28] And I think some of the main things to call out here are the fact that if you saw the media profile from the Composure workflow,
[17:37] this is also available in LiveLink Hub so that you can see what's going on.
[17:42] You can see all of your faces.
[17:43] LiveLink FaceNow transmits the video so you can just grab onto it as a media source.
[17:50] If you're running a reference video of your MoCAP shoot while it's happening, you can see that live as well.
[17:58] And then we've also expanded the recording capabilities so you can initiate recording from LiveLink Hub.
[18:08] On the animation side, there's just a bunch of great new features.
[18:13] I'm not really going to touch on them directly myself.
[18:17] I just encourage you to come check out Frederick and Chase's presentation, which is in this room at 4.30.
[18:27] So yep, that's Thomas Kilkenny.
[18:29] You don't have to wonder why he's not here because he is and he's going to present the next section.
[18:33] Thanks, Ryan.
[18:35] Yeah.
[18:40] My hair is not as nice as Ryan's, but I'm going to try my best here.
[18:43] So yeah, those of you guys who don't know me, my name is Thomas.
[18:45] That is me. Ryan is right.
[18:47] Oh wait, Ryan, you took the clicker.
[18:49] This would be really boring if we just looked at my face the whole time.
[18:53] So yeah, Ryan has given me, graciously offered me the opportunity to share a couple features I've been working on.
[18:59] So I wanted to give you guys kind of a walkthrough of a couple things, rapid fire, and I'll hand it back to Ryan.
[19:03] So first, we have some updates to cinematic assembly tools, or as we like to call them, cat.
[19:08] Sorry, cat.
[19:13] Yeah, that's much better.
[19:16] For those of you guys who don't know, the cinematic assembly tools are our sort of in-house or in-engine shot management system.
[19:23] So they allow you to build templates that we call schemas that define folder structure, asset naming, sub-sequences.
[19:29] So everything that you would need to do to build out a consistent and reusable shot template that you might need to use across your project.
[19:35] So in 5.8, we have added now timeline templates to that portion.
[19:39] So what this now means is that you are able to add on, add the entire schema definition, basically a full sequencer to defines what you need to get built.
[19:47] This means any folders, any level of visibility tracks, any tracks of any kind that can be added.
[19:51] This includes also adding in any sort of spawnables.
[19:55] Actors that you want to spawn by default as part of your process can be added in a predefined.
[19:59] You are also able to do this with sub-sequences.
[20:02] So schemas can now be nested.
[20:04] So you can define, for example, in this case, a lighting subsequence that you want to keep reusing as a default kit.
[20:09] Define that schema, and then inside of the schema for your shot, add as a subsequence, and that can be nested and procedurally done down the line.
[20:16] So whenever you build the assembly for your shot, it will automatically build the lighting sequence, all of the subsequences it may need, all the folder structure naming around it,
[20:22] and that tokenizing any paths through the whole thing.
[20:24] So you can start to build really complex shot templates that you can reuse throughout your entire project.
[20:31] Next up on the cinematic assembly tools, we have added the ability to create levels as well.
[20:37] So previously, this was limited to creating what we call the cinematic assembly assets and the folder structures and the subsequences around that,
[20:45] but you were not able to make any other kind of assets to go along with that.
[20:48] So in 5.8, we've added in the ability to also create levels.
[20:51] So if you are a particular pipeline involves something like a sub level for every shot, or if you're in a one shot, one level per shot kind of workflow,
[20:58] you can define that you want a specific level created alongside that shot when it's built.
[21:03] And you can also automatically link any of these assets to the metadata that's being held on your cinematic assemblies,
[21:09] which conveniently means that you can also make it such that whenever you build this level, and whenever you build it along with the assembly,
[21:15] and then open the assembly for artists to work on it, it will automatically open them directly into that level.
[21:20] So we're sitting right here, if I go ahead and we have the level being created, if I then go ahead and open up that assembly,
[21:26] it will jump me right over to the appropriate level that I'm working in.
[21:29] So there's no longer any need to kind of guess, wait, which shot goes at which level and am I in the right environment and why are my possessibles broken.
[21:35] All this can be procedurally built and assigned and ready to work on whenever an artist wants to jump in to work on those assemblies.
[21:41] So outside of the cinematic assembly tools, I'm letting you know we are done with cinematic assembly tools,
[21:48] we're not done with cats for this presentation, they're sticking around.
[21:51] We have something, Brent, thank you for the wool and the cat.
[21:54] We have something actually entirely brand new that we're adding in 5.8.
[21:57] Before I get into what that is, I do want to ask you guys a question.
[22:02] How many times have you had this exact thing happen to you? And I mean exact.
[22:06] You come up with a great idea, you have some changes that you want to make to a shot to an asset, you want to explore something maybe a little bit more experimental.
[22:13] But Ryan went on vacation and he left the asset checked out and now I'm not able to do anything with it and it's all his fault.
[22:19] So you get this great idea.
[22:21] I'm just going to go make it writable and per force and do some expiration and that way I don't have to worry about it.
[22:26] But you didn't actually do all that good of a job.
[22:28] So maybe, you know, this experiment didn't really work out.
[22:30] I'm not sure that I actually like what I've been doing.
[22:32] So I'm just going to try to get rid of it.
[22:34] But wait, so it does that mean that I have to go do a force get revision to get the old asset back or do I have to do that, that like resolve thing?
[22:42] And when I do the resolve thing, is am I the source or is the source in source control the source?
[22:48] Like which one am I actually trying to push back?
[22:50] And then in the end, you made the whole thing gold.
[22:52] So now every shot just has the gold asset.
[22:54] It seemed like a good idea at the time.
[22:56] I don't really think it worked out.
[22:58] I assume everybody's had like this exact scenario happen to them.
[23:02] If not, that's why we've introduced this new feature called sandboxes.
[23:06] So you might be asking, what are sandboxes?
[23:10] Here's the kind of little log line of it.
[23:12] Sandboxes are contained work areas inside of the editor where every change you make stays locked away until you're ready to merge it into your project.
[23:19] And that's all well and good.
[23:20] But let's kind of walk through what that actually looks like in practice.
[23:23] So sandboxes are a brand new plugin in 5.8.
[23:26] They are activated like you activate plugins the same way as everyone else.
[23:30] And then you can access from there this new sandbox browser where you can build out a design name to a sandbox that you want to work in.
[23:37] You've worked in multi user before.
[23:38] This is going to look extremely similar because it's kind of built on the same paradigm.
[23:42] So you create a sandbox once you're inside of that sandbox, you are now just free to work freely.
[23:47] So in this example here, I decided that I wanted to bring in a samurai from fab to maybe fight only here who's our bad guy from the the slay animation sample.
[23:56] I think that that looks relatively good.
[23:58] So that's an asset that I may want to keep playing around with.
[24:00] You can see in the bottom right hand corner there the list of all the asset changes that have been made.
[24:05] So all those little plus marks are signifying that there are new assets that have been added in the sandbox that are not in the project currently.
[24:11] You can also go ahead and make asset changes.
[24:13] So in this case, I tried to do sort of a gold skirt on only again.
[24:17] It didn't really work out.
[24:18] I don't think that me trying to change things to gold is a trend that I should continue working with.
[24:22] So I'm actually going to go ahead and try to leave that sandbox.
[24:25] So I've now exited the sandbox and when I come back in only skirts back to normal, that samurai is gone.
[24:31] All that work is locked inside of that sandbox and I don't have to worry about it polluting the project content.
[24:35] But I actually did kind of like the samurai.
[24:38] So I think that that's something I do want to keep.
[24:40] So what I can do then is reenter the sandbox.
[24:43] So it's this case I've here gone back in and re-enter my sandbox state.
[24:46] The samurai is back in there.
[24:48] The only asset change is still there and I can choose that I want to persist and keep just the things that I actually like.
[24:53] So I'm going to go ahead and click persist.
[24:55] Again, if you've worked with multi-server for this is a very similar workflow and I'm going to select only the assets that I actually want to keep.
[25:00] So I'm not going to keep the changes to only that went pretty poorly, but I'm going to keep the changes to my level where the samurai was added.
[25:06] And I'm going to keep the actual samurai assets themselves.
[25:09] So once I go ahead and hit persist on that, you can see that they're no longer considered in the change list because they're actually a part of the project.
[25:16] And when I leave out of my sandbox back to my main project content after it reloads the level, that samurai is now included in there.
[25:23] So you can jump back and forth between any number of sandboxes.
[25:26] The work is locked and stays inside of those particular sandboxes until you choose exactly what you want to come out.
[25:32] And then that becomes part of the real project content.
[25:34] So you can work entirely safely.
[25:35] So essentially what it does is whenever you make a change in your project content while you're in a sandbox, that change is actually saved into a sandbox asset store.
[25:44] Jason Walter, who's the lead engineer on this is sitting right over there and he's probably going to tell me that's not actually what it's called.
[25:50] So this is probably an oversimplification that but essentially it's stored in its own version of the asset for the sandbox.
[25:55] When you want to persist those assets back out, they're copied back over to the real version inside of the project content.
[26:01] When you're actually going to load those assets while inside of a sandbox, what essentially we do is when the asset goes to load the project content, the sandbox redirects it to load the versions in the sandbox.
[26:10] And that's fundamentally at a core level.
[26:12] We're just loading you over to use that project content.
[26:15] And then whenever you actually want that back, you have the freedom to persist it back to the real project and go about your normal workflows from there.
[26:22] A couple more things on our side on the virtual camera we've made some adjustments to parenting and platforming.
[26:28] So if you played with the virtual camera before parenting was a little bit of a difficult piece you had to use this sort of dropdown you can see in the upper right corner there in order to pick a parent or you had to rely on an operator on the desktop to handle that portion for you.
[26:39] So in 58 we've had a dedicated parenting browser, which is the thing right here on the on the right side.
[26:44] You can use it to search for actors by their type you can filter just the ones that are closest to you you can search by name.
[26:51] Just anything you would want to do to kind of make that more easily accessible from the V cam directly.
[26:55] You can also attach to sockets directly from here so in this case I'm going to go and say that I want to attach to the pelvis of Oni.
[27:01] There we go.
[27:02] I've done an attachment on now and I'm following around.
[27:04] It's got a little bit of a kind of a funky wobble to it because of the roles.
[27:08] So also directly from the V cam you have per axis inheritance constraints so in the upper right corner there I'm able to choose which axes I actually want to inherit.
[27:16] In this case I'm going to kill the role on this on this parenting so that I can get a bit of a cleaner shot and I can go ahead and record that that way.
[27:23] This previously was limited to only a couple types of actors you could get this type of control when you were attached to a cine camera rig rail or to a cine camera actor.
[27:30] But we've now moved all the parenting over to using the constraint system and as a result this is now freely available on any actor that you want to control.
[27:37] So you have more flexibility to do it on the V cam instead of having to call out to a desktop operator to handle these sorts of things.
[27:44] Last but definitely definitely not least this is my favorite feature of the whole thing I'm not joking.
[27:48] You can now record with spawnables as references and parents.
[27:52] So previously if you were using take a quarter and you wanted to attach to an actor that was in your sequence or you wanted to reference it for something like follow camera looking at it or a look at tracking that thing had to be a possessible.
[28:04] If it was a spawnable as soon as you went ahead and you did the recording it would despawn respond the whole thing would break and you wouldn't be able to do it.
[28:10] So now in 5.8 we have here only is a spawnable in this particular case.
[28:15] We're going to record the virtual camera parented directly onto only through through the sequencer now as a spawnable.
[28:21] So this is just fully supported.
[28:24] There isn't any I don't there's no more bells and whistles to it beyond you are able to parent to spawnables you're able to reference spawnables in your properties and in your exposed variables on blueprints and it will just work.
[28:33] I have been asking for this feature since 421.
[28:37] And I didn't even work at Epic at that time.
[28:40] So this is basically I think the culmination of my entire career is that you can finally do this dang thing.
[28:44] Anybody who's not excited I promise you that there are people on your teams who are very excited because it's been a massive pain in the butt for eight or nine years.
[28:51] Thank you.
[28:52] But yeah, with that, that's everything on my side of things so Ryan's vacation is over he can check that asset back in thank you very much.
[29:00] Thank you.
[29:08] I'm back.
[29:09] I check that asset in I think I had to reset my password but I did do it.
[29:14] Yeah, so back to me here.
[29:17] Next section is for in camera VFX.
[29:20] So our big ticket item for fries VFX is this new option for play playback called Tiled Mipmap video.
[29:28] So this is a new format that provides like a fast and memory efficient plate payback in a single movie file.
[29:36] So if you've if you've used our process EXR workflow kind of works the same way, you know where we only decode the necessary MIP levels and the necessary MIP level tiles based on where it is you place the plate within the scene and where your end display config is looking.
[29:54] This also this format also has smooth scrubbing right so if you can like if you scrub the timeline it's smooth I don't know there's not the whole lot else to say about that.
[30:04] And then kind of last but not least it supports HDR and alpha channels.
[30:09] So Tiled Mipmap video is based on the open APV.
[30:15] It's based on open APV which is part of the Academy Software Foundation.
[30:19] So we've made some upgrades to this which essentially adds these mip mipping capabilities.
[30:25] And so we're working with the foundation to get this stuff checked in over the next month and now that we've shipped it.
[30:30] And we're also going to be like you know going like I will be kind of going to doing the rounds like trying to evangelize this and hopefully we can get some of the other some other applications to support open both open APV and TMV.
[30:46] In practice you know what does this mean right so this is an example play this is one of the plates we use when we test the footage right so it's a 16k plate it's 100 frames like or I do use the 100 frames at least for this example.
[30:57] And in our EXR workflow that's 100 gig right so it's it's a giant piece of it's a giant set of data that we have to copy to all of the end display nodes and play them back.
[31:06] But when we make this into a TMV file it goes down pretty dramatically right so you're getting a single file only two gigs much easier to transfer around.
[31:15] And that's one of the that's basically the main thing that TMV is is geared towards.
[31:21] Hopefully for anybody doing plates.
[31:24] Yeah hopefully for anybody doing plates and unreal like this is this is a nice win and perhaps if people like maybe abandoned unreal for play playback.
[31:34] Hopefully we can win you back with this TMV feature.
[31:39] Also on the end display side we've added support for rendering and display with movie render graph.
[31:45] So there were a number of issues with the prior setup that was based on presets.
[31:50] But now like and displays a fully fledged member of movie render graph so this means that you can do collections modifiers and render layers with their end display content.
[32:01] And specifically this allows you to potentially like use that display to render out maybe you are still doing some post comp before you bring it back in.
[32:08] This is now supported through MRG.
[32:12] Through the setup you can use the deferred or the patch tracer is kind of the same same paradigm where you'll have an end display deferred or an end display path tracer.
[32:20] The previous preset implementation had like a number of different settings and those have been all consolidated into a way that feels a lot more like all the other render nodes in MRG.
[32:29] You can control the DCRA in sequencer or via a graph override.
[32:34] So in the old setup you would have to explicitly set the end display config in every render.
[32:41] You no longer have to do that the end display config is treated just like a camera so if it's in sequencer and you render that sequence it's going to figure out that that's the end display you want to use.
[32:49] And then you also have the option to override it potentially by variables as well like all in the kind of MRG infrastructure.
[32:58] There's file naming tokens that kind of pulls from cinematic assembly tools but all of the different end display items like your node, your viewport,
[33:06] all of those things that you would get from the configuration you can also use them in file naming.
[33:10] And we also have support for stereo rendering.
[33:13] A lot of people use end display to render out stuff that's going to be viewed on headsets.
[33:19] So this is a supported feature via MRG.
[33:22] And the last but not least we still have some work to do here so ICBFX camera support is still to come.
[33:28] Something that didn't quite make it into this release so we're going to have to put that out at the next opportunity.
[33:38] Segueing from end display to render graph like end display rendering was really like kind of like the last missing piece from MRG.
[33:45] It was basically the only remaining thing that wasn't supported in the graph.
[33:51] So now like with that in mind like we're calling movie render graph production ready.
[33:56] Going forward all new features will be implemented in graph.
[34:00] The presets going to start to be phased out.
[34:03] So in practice what does that mean right?
[34:05] So like the one of the additional considerations we had for MRG was like thinking about it,
[34:11] you know like a lot of the emphasis had been on like these more sophisticated setups of doing render layers.
[34:16] I'm having like a potentially really complex rendering setup.
[34:18] But we also wanted to use the graph for simpler setups and that's kind of showing up here as this basic configuration.
[34:24] And this is how we're kind of starting to pivot away from presets.
[34:27] So if you were using a preset you probably familiar this where like if I want to make any changes to the base setup like I have to pop open this preset window.
[34:35] Maybe I want to change the resolution.
[34:37] It's another step to turn off DAPEG.
[34:39] Maybe I want an MP4 instead.
[34:41] And then you know similarly if I want to change the samples I have to add the anti-aliasing.
[34:46] You know there's just a number of steps that go through this right.
[34:49] Same thing for game overrides and you have to remember to accept it.
[34:52] Like if you click off of it and you lose it you have to redo it.
[34:55] So as the next step like the evolution of this is the basic config right.
[35:03] So in the basic config all of the stuff is just right there.
[35:06] You can just change it directly in the panel right.
[35:08] So in this case we're changing the resolution.
[35:10] You can change it to you know from PNG to MP4.
[35:13] You have the path tracer right there if you commonly do path trace vendors right.
[35:17] So you're not having to pop open, contact switch all these different windows.
[35:21] And then in addition there's this ability to you know override it on a per shot basis right.
[35:28] So if you override on a per shot basis you're going to see it there.
[35:31] You're going to get a little indicator that something's been overridden right.
[35:34] So if you're looking at your sequence at a glance you can see which shots have overrides really quickly.
[35:40] The last thing to mention is that it is using the graph under the hood like I think I already said that.
[35:45] But some things to be aware of is that you can save the basic config as a default right.
[35:49] So if there's a certain setup that you always want to show up clicking that button there will have every time movie render queue pops up.
[35:56] You load anything into it is always going to have those same settings.
[35:59] And then you can also save it as a graph config.
[36:01] So basically you take these settings it's going to make a graph for you if you want to use this as a jumping off point to do something more sophisticated.
[36:08] It'll make a graph with all these settings already there for you.
[36:14] Another cool feature to mention is accumulation depth of field.
[36:17] So like this is an example of a shot where like our real-time depth of field breaks right.
[36:22] So like it's kind of the worst case scenario for the way our rendering works like through you know this kind of rack focus through a chain link fence.
[36:30] But with accumulation depth of field it's a new option that you can kind of opt into.
[36:34] We're going to get a nice looking depth of field image here.
[36:38] So there's some additional rendering that happens some additional sampling that happens that's based on the camera setup.
[36:48] But what it allows is like a more path traced style renderer with the deferred renderer.
[36:53] You know like the way that I kind of think about it is that like if you have certain shots that are really depth of field centric.
[37:00] This is something that you may want to apply there and you can pay some additional rendering costs to get that.
[37:05] But it also allows you to keep your look to have keep everything else in the deferred in the deferred workflow for all the shots that don't necessarily need it.
[37:12] So in terms of how it works there's kind of two ways to set it up.
[37:15] So the first way is with a component right so you can just add this accumulation depth of field component to your camera and then potentially change the settings.
[37:23] You know like like the samples for example.
[37:26] There's also an option to override it or use it as a modifier in MRG.
[37:33] So there's an accumulation depth of field modifier you can add that to your graph.
[37:37] When you turn it on you have two options so it can just use the camera default right so this will just pick up and operate only on the cameras that actually have the component.
[37:47] This might be a way that you just only override the settings for example or you can just force it on.
[37:51] So if you force it on you can set the samples everything is managed entirely in MRG.
[38:01] And then another thing the last thing to mention with it is the preview right so while you're working if you have the component on your camera you also have the option to preview it.
[38:10] So it'll run a single frame preview here.
[38:12] If you go into the menu you can opt into it and it will you can see it kind of generating the frame.
[38:19] It's also giving you an indication about how long it takes to render the frame versus the real time.
[38:24] But this will give you like while you're framing up the shot you can you can see the accumulation depth of field in editor as well.
[38:34] There's a number of great shots like that I've already hit YouTube people found this feature pretty quickly when it when it was in Maine.
[38:40] But these are some some renders from Dylan that look just look really great they were they were this was also in the in the state of in the state of in real.
[38:48] A little while ago if you were there but these are just some great shots some great examples of the type of rendering you can do with accumulation depth of field.
[38:58] On the graph side for more sophisticated you know render layers workflow we now have a light modifier so it's going to let you do light variations.
[39:06] So there's a couple things to mention here that are related to it.
[39:09] The first is that there's an additional condition group type for light actors.
[39:13] So this is basically a way for you if you want to use the light modifier to just quickly grab all the light actors so you add this in and then it's automatically going to have all the different light types you can potentially toggle them on and off.
[39:23] But it's just a really easy way to grab all the lights.
[39:26] The reason why you'd want to do that is because you'll then send it to the light modifier right so this is an example where I have like basically three different you know three different changes to my lights you know having them affect world changing the color and changing the intensity.
[39:42] So when you pop this in you can see we've surfaced some really common properties you know color being one of them.
[39:48] And then we also have a dedicated section to intensity right because different light types have different intensity settings.
[39:55] Something to be aware of is that like three of them have the same like the same setting so you have the option to like treat them separately or treat them all together.
[40:03] Just trying to make it really easy to change this since like you know scenes commonly have a lot of lights.
[40:09] And then kind of last but not least there is the ability to just add custom properties.
[40:17] So this this this menu lets you find literally any property on the light if you want to overwrite it.
[40:22] So if there's something specific that you have in your workflow this thing you know you can you can grab any of the properties.
[40:29] This is an example of just you know like the the graph I just made in action right so you can see like I've turned some lights off.
[40:37] I changed the color to green and I made the intensity really really bright.
[40:42] You know in practice I think that like people will have you know much more nuanced modifications that are lights.
[40:48] But I just wanted to show this is to show like okay here's some really really obvious examples of it.
[40:54] So our last feature is presented by a special guest and I'll let them sit I'll let them speak for it.
[41:01] What do you guys want me to say here.
[41:04] Okay now in Unreal Engine 5.8 audio will be completely clean and in sync in movie files out of movie render queue without any pops or artifacts.
[41:17] Really just now after what like 10 years or something.
[41:22] The clock fixes or did you fix this.
[41:26] Be honest.
[41:29] Okay whatever let's do this.
[41:35] Just kidding.
[41:36] Okay anyways clean audio out of movie render queue in Unreal Engine 5.8.
[41:42] What a time to be alive everybody.
[41:46] I did it.
[41:56] That's our show.
[41:57] Thank you for coming.
[41:58] I think we have a little bit of time for questions.
[42:00] If anybody has any.
[42:02] Civilization of each of those mass fragments to fill a buffer with with information about those those fragments.



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
