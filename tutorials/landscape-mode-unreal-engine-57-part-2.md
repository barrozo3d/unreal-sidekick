---
title: Landscape Mode (Unreal Engine 5.7) Part 2
source: YouTube
url: https://www.youtube.com/watch?v=IADB2OR8XCk
author: R SH
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/landscape-mode-unreal-engine-57-part-2/
frame_count: 0
frame_status: pending-selection
---

# Landscape Mode (Unreal Engine 5.7) Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=IADB2OR8XCk)
**Author:** R SH
**Duration:** 15m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py landscape-mode-unreal-engine-57-part-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello, everyone, and welcome back to Unreal Engine, Landscape, Sculpting, and Modeling Series.
[0:09] This is Episode 2, Ram here, sharing with you, as I promised, how to use height maps to generate
[0:20] a really good-looking realistic terrain.
[0:24] So what did we do last time?
[0:28] I'm actually loading the same level that we created, my land.
[0:33] This is where we basically finished off our terrain modeling, the sculpting.
[0:41] Just a recap, I went over the sculpt tools for you, sculpt, erase, smooth, flatten, and
[0:48] so on and so on.
[0:49] We went over the brush types, fall off, what those tools do, and the tool strength, brush
[0:58] size, fall off, and of course, other options.
[1:02] And most importantly, we went through how to use layers to really optimize and create
[1:13] a much, much better and manageable terrain.
[1:18] This is basically where we ended up.
[1:20] I'm going to save the level, and we're going to actually create a new land.
[1:28] To do that, I'm going to create a new level.
[1:32] So I'm going to choose basic, create.
[1:37] I'm going to delete this guy, and making sure our third-person blueprint is the game override.
[1:49] Now, like last session, what we need to do is go to landscape mode to get a flat grid.
[1:58] If you remember, we did go over all of the location rotation.
[2:03] We don't need to deal with any of this here, because we're going to actually use a height
[2:08] map, which is this side of the panel.
[2:13] Import from file.
[2:14] You see we have everything here again.
[2:17] All of that resolution, scale, and component number is there.
[2:20] I'm going to save this and call this new land lake.
[2:27] There's going to be a lake in there.
[2:30] New land lake.
[2:32] And back to landscape mode.
[2:36] We don't have anything yet.
[2:38] Now we want to actually import height map.
[2:43] Before we import height map, let me go over this alpha brush that we imported last session.
[2:50] This is a PNG file that we can actually use it for height map, because it follows the same
[2:56] principles.
[2:57] It is a square.
[2:59] It's 1080 by 1080.
[3:01] And it is PNG.
[3:02] It is 16-bit.
[3:03] However, of course, this is not what we want to create.
[3:07] But why I opened it is it follows the same principles.
[3:10] Whenever we were going through the sculpting with the stamps, brightness represents elevation.
[3:17] And darker you get, less elevation you get.
[3:20] So for example, those black spots, basically there's going to be zero elevation there.
[3:25] So it's going to be flat.
[3:26] So keep that in mind.
[3:28] Our height maps are going to follow the very, very same principles.
[3:32] Now we need to actually import them from files.
[3:36] However, we don't have one yet.
[3:38] So what I like to do is introduce you to this website.
[3:44] I love this website.
[3:45] It actually allows you to go to a certain part of the world and generate height map based
[3:53] on that.
[3:54] I already went to this area I like.
[3:58] This is around my area, around Vancouver.
[4:03] And let's actually go to, okay, around Coltus Lake.
[4:09] Actually, this part is in US apparently, which is fine.
[4:14] That's okay.
[4:15] Now, take a look here.
[4:17] A few things you need to pay attention to.
[4:20] So this area in real size, it's actually 6.4 kilometer by 6.4 kilometer.
[4:29] Now we can change certain things here.
[4:33] So if you actually know the area, if you have the latitude and longitude, you can literally
[4:38] enter it here and go.
[4:40] I actually changed the output width and height to 2048 by 2048.
[4:45] It just adds a little bit more resolution.
[4:48] Make sure output format is 16-bit.
[4:52] Normal mode is set to smart.
[4:55] And by the way, you could change the view of this as well.
[5:01] However, I just go to the Topo one.
[5:04] I chose this area because it does actually have a bunch of mountains.
[5:10] Maybe actually I move here a little bit.
[5:13] It has a bunch of mountains.
[5:15] It has a lake.
[5:16] It has another tiny lake.
[5:18] It actually has kind of like a river type line, which, and all of that can be by the
[5:25] way, modified later on.
[5:27] So I am going to, yeah, let's stick to this area and maybe actually go here.
[5:36] I shouldn't be too picky, but I am anyways.
[5:38] All right, you know what?
[5:40] Let's just do it this way.
[5:42] Now when we are happy with the location, we are happy with the size of the map.
[5:47] We just say generate height map.
[5:50] It's going to calculate save.
[5:53] I'm going to call it height map.
[6:00] You could also generate an Albedo map as well if you want to use it as a reference or do
[6:07] kind of like very, very rough texturing for painting references.
[6:11] You can generate the same thing, but make sure you change it to imagery.
[6:15] When you are done here, let's go back to Unreal Engine.
[6:19] I am going to now say, you got nothing by the way here.
[6:24] There is nothing here.
[6:25] So we say import from file.
[6:27] We choose the file we have.
[6:28] Oh, look how it looks.
[6:30] You see all of the elevation, everything looks there.
[6:34] And there you have it.
[6:37] Now you are not bound.
[6:41] And again, you may say, well, this is not what I need.
[6:43] Yeah, I know.
[6:44] That's fine.
[6:45] But you can always try and see how it looks.
[6:49] I'm going to press fit to data.
[6:51] It's already fitted, but sometimes you may have a different setup.
[6:55] I'm going to say import, look at it.
[7:00] All right.
[7:01] This is actually quite nice.
[7:02] It's quite neat.
[7:04] So if you look at the map that we created, actually I'm going to import it in my textures
[7:13] so we can load it later on.
[7:17] All right.
[7:22] So this was the map.
[7:24] Look, you have the map.
[7:27] This is what was generated.
[7:31] And there you go.
[7:34] This is the area.
[7:35] Now let's just assume that's what we need.
[7:38] It's working well.
[7:40] Now I'm going to undo this.
[7:43] And I'm going to raise this scale to 100.
[7:47] Remember I told you the scale of 100 by 100 by 100, especially on Z, doesn't actually
[7:57] do anything unless you actually have that height map and it sets the elevation.
[8:01] So look at it right now.
[8:03] It already exaggerates the elevation that you have.
[8:07] Now you see the mountains are a lot higher.
[8:11] Now this area is basically the water area.
[8:16] So that's why it's really low.
[8:17] So if we add an ocean later on, it's just going to be here.
[8:21] And let's go to the selection mode.
[8:24] I just want to see where my...
[8:26] Okay, I'm going to bring my...
[8:32] All right.
[8:38] So if I press play, there you go.
[8:41] There's our character.
[8:44] So it is very steep.
[8:47] So this is like too much, right?
[8:49] This is like too much.
[8:51] So we're going to undo this.
[8:54] Okay.
[8:56] Instead of 100, let's go back to, let's say, 40 this time and press import.
[9:08] Okay.
[9:10] Not bad.
[9:12] Not bad at all.
[9:13] Maybe we go 50 and import.
[9:18] We can keep it there.
[9:19] We don't have to be too picky.
[9:21] I'm going to go back to selection mode, making sure that my player start is somewhere reasonable.
[9:28] Okay.
[9:31] So he's not falling to its death.
[9:39] There you go.
[9:44] This is not bad.
[9:45] This is quite good.
[9:46] It's not sliding down.
[9:49] I actually like the setup.
[9:51] And let's actually zoom back.
[9:55] This is what you get.
[9:57] Now you may say, well, okay, I got the base of what I needed, right?
[10:03] I got the base of what I needed.
[10:05] Now you can even do more.
[10:08] Maybe you want to, I don't know, create a ramp.
[10:11] So we go to landscape mode.
[10:13] You want to create a ramp from this point to this point.
[10:30] And let's do ramp width.
[10:32] The falloff is also wide.
[10:38] We just say add ramp.
[10:40] Nice.
[10:41] Very nice.
[10:43] Here's your ramp.
[10:45] I'm going to go and add a little bit of smoothness here.
[10:51] There you go.
[10:55] So you can see now, after getting the base of the terrain I want, I can sculpt and add
[11:02] more stuff.
[11:04] What I'm going to do, I'm going to go back to my stamp.
[11:11] Instead of this guy here, I'm going to do the reptile one.
[11:21] Let's go with the sculpt.
[11:24] And let's, okay.
[11:27] Nice.
[11:30] Very nice.
[11:33] And let's smooth it out with the same stamp.
[11:39] So it's actually adding noise here.
[11:41] Good.
[11:44] So you can see very, how simple.
[11:46] We can use that height map that we just created, right?
[11:52] Use that height map and create the basic terrain in our Unreal Engine for our game.
[12:03] So what's going to happen next?
[12:05] We have to do a lot with this.
[12:06] We can add water.
[12:08] We can paint this land.
[12:11] Or the other one.
[12:12] We can add other components to it.
[12:14] Now we have the freedom of doing a lot.
[12:17] You know what?
[12:18] One of the mistakes I made was I should have actually added this ramp.
[12:23] Not there.
[12:24] I should have created a layer.
[12:25] So I'm just going to rename the main one, main terrain.
[12:30] Okay.
[12:31] I'm going to create a new layer.
[12:33] It's going to be a landscape editing layer.
[12:37] And rename it this time.
[12:41] Let's just say ramps.
[12:42] So this one is going to have all the ramps that I need.
[12:50] Where did we create it?
[12:52] Let's go from here all the way to here.
[13:02] Okay.
[13:10] Can I go higher than this?
[13:12] 15,000 perhaps?
[13:13] Oh yeah.
[13:14] There you go.
[13:15] 25,000.
[13:16] Okay.
[13:17] So it's quite wide.
[13:18] Okay.
[13:19] There you go.
[13:20] I think we're going to get a decent ramp here.
[13:23] Wow.
[13:24] Look at it.
[13:25] Very nice.
[13:26] Very, very nice.
[13:28] So we got a ramp.
[13:29] Maybe it's a little bit...
[13:30] All right.
[13:31] Maybe this one.
[13:35] Okay.
[13:36] So we got a ramp here.
[13:37] Now again, if you go back to our layers, we can remove it, hide it, and add more to it.
[13:48] I'm going to smooth out this area.
[13:55] Maybe a little bit more strong.
[14:00] Okay.
[14:09] I'm using the alpha map just to add the noise I need as I'm smoothing it.
[14:16] Okay.
[14:17] Perfect.
[14:18] Same here.
[14:21] Nice.
[14:22] It's getting there.
[14:27] All right.
[14:52] So we are basically done.
[14:55] As promised, in the next episode, I'm going to show you how to paint your landscape in
[15:04] a very, very cool way.
[15:05] It's going to be quite a dynamic experience using layers again and using the landscape
[15:14] material.
[15:15] Landscape material is not a typical material in Unreal Engine.
[15:18] All you know in the typical material likely does not apply directly.
[15:24] It's the same principle, but the landscape material itself has a built-in structure
[15:31] specifically for landscape painting.
[15:34] With that in mind, I will leave you here to experiment a little bit.
[15:40] What I would like to ask you is, come back for the third episode.



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
