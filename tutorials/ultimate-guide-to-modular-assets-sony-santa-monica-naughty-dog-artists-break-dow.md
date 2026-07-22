---
title: Ultimate Guide to Modular Assets | Sony Santa Monica & Naughty Dog Artists Break Down the Workflow
source: YouTube
url: https://www.youtube.com/watch?v=gaUcEoh_-AQ
author: Class Creatives
ingested: 2026-07-21
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ultimate-guide-to-modular-assets-sony-santa-monica-naughty-dog-artists-break-dow/
frame_count: 0
frame_status: pending-selection
---

# Ultimate Guide to Modular Assets | Sony Santa Monica & Naughty Dog Artists Break Down the Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=gaUcEoh_-AQ)
**Author:** Class Creatives
**Duration:** 14m52s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ultimate-guide-to-modular-assets-sony-santa-monica-naughty-dog-artists-break-dow <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey, this is Class Creatives, and in this special video edition, we'll discuss how two


### Intro [0:01]
**Transcript (timestamped):**
[0:09] industry professionals create 3D environments with modularity to create incredibly vast
[0:14] and complex worlds quickly and efficiently.
[0:16] This video collaboration with Sierra Division will dive into professional techniques for
[0:21] 3D environment asset creation in the gaming industry.
[0:24] In this video, we'll hear from industry veterans Jacob Norris and John Ariano, who will dive
[0:29] into their process of creating modular environment assets from their work at some of the best
[0:33] studios in the world, such as Naughty Dog and Sony Santa Monica.
[0:36] They'll show us some of the best practices to consider and how modularity and AAA game
[0:40] production is used in modern-day game development.
[0:43] In this video, we'll discuss the power of modular assets and 3D environment design.
[0:48] Environment artists often build entire worlds with individual pieces like walls, pillars,
[0:52] and floors that effortlessly snap together.
[0:55] This is the essence of modularity, enabling incredibly rapid environment creation.
[1:01] Modular assets and 3D environments are individual pieces designed to snap together for rapid
[1:06] environment creation.
[1:08] These pieces use a grid system for easy alignment and duplication, significantly increasing
[1:12] efficiency compared to manual methods.
[1:16] Techniques like vertex painting, trims, decals, and consistent texture density further enhance
[1:22] the visual quality and seamless integration of modular environments.
[1:25] We'll take a close look at how duplicating and snapping 3D asset pieces can be aligned
[1:30] to a precise grid, ensuring perfect alignment every time, eliminating gaps and overlaps.
[1:37] Modularity drastically boosts speed and efficiency, a stark contrast to the slow process of manual
[1:42] scaling and fitting.
[1:44] Techniques like vertex painting and trims further refine the visual appeal of these modular
[1:48] environments.
[1:50] From simple rooms to expansive scenes, modular design scales effortlessly using sets, corners,
[1:56] ceilings, and doors.
[1:57] The key takeaway?
[1:59] Modular assets built on consistent grid spacing revolutionize 3D creation, making environment
[2:04] building faster, easier, and more efficient than ever before.
[2:08] Which is why this has become an industry standard for the best AAA game studios in the world.
[2:13] These techniques, often unseen, are industry standard practices employed by major game
[2:17] studios.
[2:18] These studios leverage modular workflows to maximize asset reuse while maintaining
[2:23] unique and engaging environments.


### Jon Arellano | Maya [2:26]
**Transcript (timestamped):**
[2:31] My name is John Ariano, and today I want to go ahead and just share with you guys some
[2:37] tips and tricks when it comes to modularity.
[2:40] So to start things off, first thing I want to show you guys is basically how we can kind
[2:45] of go about making a nice little corner piece here that snaps and works together with our
[2:51] other kit pieces.
[2:54] So right here I have a nice little 4 meter wall section.
[2:58] Let's go ahead and duplicate this.
[3:00] Move it on over here.
[3:03] And I'm going to go ahead and duplicate this model and use this nice little script that
[3:06] I use a lot for this kind of stuff, which is going to be this nice little mirror tool
[3:09] here.
[3:10] It's basically just this one little line of code, this mail script, so feel free to
[3:15] utilize that.
[3:16] I'm going to go ahead and start off by rotating this around and trying to make sure that it
[3:20] snaps too as best as I possibly can with my other kit piece that is on the grid.
[3:25] Let's go ahead and just try to line it up.
[3:26] I'm purposely going to kind of mess it up a little bit here or just kind of be a little
[3:29] bit off just so I can clearly show you guys how we can kind of fix this stuff.
[3:32] Let's go ahead and delete that.
[3:33] Assign just a nice little lambry material right here.
[3:37] Cool.
[3:38] So I'm going to go ahead and start off by selecting all the vertices that are going to line up
[3:43] with this kit piece right here.
[3:45] So I'm just going to go ahead and just select all these.
[3:47] I want to deselect any of the ones that are going to be on this side of the right side
[3:51] of this corner here.
[3:52] So let's go ahead and just deselect these vertices real quick.
[3:57] Cool.
[3:58] All right.
[3:59] It's not the end of the world if we had them, but just to make sure that this thing snaps
[4:02] together nice and perfectly.
[4:03] I'm going to start off by holding D and V, and I'm going to go ahead and just snap my
[4:07] vertices right here.
[4:08] Let's go ahead and start off by just moving it on one axis just on this green axis right
[4:13] here.
[4:14] I'm going to go ahead and just snap it to my kit piece that is on the grid, which is
[4:16] this one.
[4:17] That's the first step.
[4:18] The next thing we're going to do is we're going to go ahead and snap it on the other
[4:21] axis, this red one here.
[4:22] I'll just go ahead and just deselect these vertices that I don't mind kind of pulling
[4:27] away.
[4:28] So just deselecting that corner edge there.
[4:30] Hold D and V. Now I can just go hold X or V just to snap it to my model that's on the
[4:36] model that is on the grid.
[4:38] And there we go.
[4:39] Now we have a nice little corner piece.
[4:41] So next thing I want to go ahead and share with you guys is actually going to be the
[4:47] importance of making sure that our materials and our kit pieces work with our text density.
[4:53] So to kind of start things off, I want to go ahead and just show you guys what the UVs
[4:56] look like on this model here.
[4:57] I'm going to go ahead and just hit 6 just to kind of reveal the texture here.
[5:02] Take a look at these UVs.
[5:03] So because I'm using a 1024, sorry, 2048 size texture, and I'm aiming for a text density
[5:09] of 1024 per meter, as you can see, my tileable texture goes over this model twice.
[5:16] So if I were to go ahead and duplicate this model, for example here, it's going to go
[5:19] ahead and snap up perfectly because, you know, it's going to line up perfectly and seamlessly
[5:23] because these two models are the exact same.
[5:25] And because both of their edges end up ending on the edge of my tileable, it's going to
[5:31] work just fine.
[5:32] Now this is all well and great, but let's say we had another kit piece such as this one
[5:36] right here.
[5:37] Let's take a look at these UVs, at least for this, you know, flat wall.
[5:41] In fact, I'm just going to go ahead and just auto unwrap it here, just move it off to the
[5:44] side, set my text density just so it is proper.
[5:47] Let's go ahead and move this piece right here and this one right here.
[5:52] Hold D, hold V just to kind of snap that.
[5:55] Cool, cool, cool, cool.
[5:56] All right, great.
[5:58] So right now, because my kit piece right here is also four meters, I should be able to go
[6:03] ahead and line this thing up just fine.
[6:06] If I go ahead and make sure that my UVs also line up with my texture.
[6:09] So I'm just going to go ahead and move this piece over.
[6:12] And because my UVs line up on the edge there and just to be sure I can go ahead and make
[6:16] sure that they snap, but this is just kind of one of the benefits of making sure that
[6:19] your kit pieces, you know, are in fact on the grid so that when you do need to kind of
[6:23] tile seamlessly, you definitely can.
[6:26] Now that we know that this piece goes right there and that'll be so we'll go right here
[6:29] and it should end up tiling nice and easy.
[6:33] So this is really great.
[6:34] Let's say we had a nice little two meter piece though, because I am working with a textile
[6:38] density of 1024 per meter and because I am using a 2K, I actually should be able to go
[6:43] ahead and cut this model in half if I need to.
[6:46] So let's just go ahead and just add a couple of edge loops right here in the middle.
[6:49] One right there and one right there.
[6:52] Let's go ahead and just kind of get rid of these just in case I ever needed to.
[6:56] But this is just one of the benefits of kind of working with a texture that lines up with
[7:01] our kit pieces and works with our textile density.
[7:04] Now if I wanted to go ahead and just like let's say duplicate this model over here, it
[7:07] should line up nice and seamlessly.
[7:10] Cool.
[7:11] Sweet.
[7:12] But yeah, obviously there's ways that we can kind of hide seams in game in an engine.
[7:16] We can always add pillars or cover some things up with foliage and that's all well and great.
[7:21] But if we can kind of, you know, plan a little bit early on and, you know, make sure that
[7:24] our kit pieces are snapping to the grid and ongoing with the grid and obviously working
[7:29] with our tileable textures, we can have a nice kit that works together seamlessly and
[7:35] get all the benefits when it comes from that.
[7:38] Now the last trick I want to go ahead and show you guys is because, you know, a lot
[7:41] of times in kit pieces we're utilizing things like trims and tileers and, you know, things
[7:46] that repeat very often.
[7:48] You know, we can actually start to blend a lot of our kit pieces and break up some surfaces
[7:53] with, you know, lots of different techniques including like vertex, paint and obviously,
[7:57] you know, just layering pieces of geometry.
[7:59] But another technique I want to go ahead and share with you guys is blending with when
[8:02] it comes to blending our kit pieces together is using decals.
[8:06] So right here I have this nice little floor piece right here.
[8:09] I'm just going to go ahead and snap it right there for us.
[8:11] Whoops, make sure that it kind of lines up.
[8:13] Yeah, perfect.
[8:14] All right, sweet.
[8:15] I also have this nice little decal for us to use here.
[8:18] I'm going to go ahead and start off by using this decal as a kind of a way to kind of,
[8:21] you know, just skirt this model to the floor.
[8:24] But start off by just going like this and having a nice little piece of geometry that
[8:28] kind of floats on top of this model here.
[8:31] I can always, you know, do this in engine or I can also bring this in as its own little
[8:34] kit piece if I need to.
[8:36] But let's go ahead and say we floated it right there.
[8:38] It'll be using a nice alpha transparency so it'll kind of, you know, blend there flawlessly
[8:42] and seamlessly.
[8:44] Now if I wanted to go ahead and use it on a kit piece like this, I would just need to
[8:47] make a custom piece.
[8:48] Let me show you how I can go ahead and do that.
[8:50] I'll go ahead and just duplicate this model.
[8:53] I'll go ahead and start off by just selecting.
[8:55] Let's just go ahead and select these trims down here.
[8:58] Shift select.
[8:59] Get rid of these guys.
[9:01] I'm going to go ahead and just grab these vertices and I just want to go ahead and just
[9:04] float it right off of my model.
[9:07] Just ever so slightly, right?
[9:08] Just so we don't get any sort of Z fighting going on.
[9:10] Let's go ahead and assign my, oops, decal here.
[9:19] I'm going to go ahead and just project it.
[9:25] So I'm going to apply.
[9:29] Whoops, wrong axis.
[9:32] There we go.
[9:33] Oops.
[9:34] Always got to get the right one here.
[9:35] Maybe it was the right the first time.
[9:37] Nope, it was not.
[9:39] Cool.
[9:40] There we go.
[9:41] You seem to go ahead and rotate this off to the side here.
[9:44] Hold D, hold V, snap it down to the grid.
[9:50] And then we should be all set.
[9:54] So now basically we can have like a decal that basically lines up.
[9:57] I know this kind of looks a little bit splotchy, but now this is a great way that we can go
[10:02] ahead and make sure that things kind of blend together.
[10:04] Let me go ahead and fix these a little bit here.
[10:07] Because it's a decal, I shouldn't have to worry too much about text.
[10:10] And so as long as it doesn't look, you know, super duper bad.
[10:13] Let's go ahead and just kind of scale it up just a little bit here.
[10:15] Our text I didn't see will come from our Tyler's.
[10:18] But this is a nice little way that we can at least utilize, you know, some decal work
[10:23] there.
[10:24] And there we go.
[10:25] We can get, we can blend two of our pieces of geometry together, just using, you know,
[10:29] some form of decaling or some sort of script model just to kind of blend things.
[10:34] And that's all I got for you.
[10:35] See you next time.


### Jacob Norris | Unreal Engine [10:43]
**Transcript (timestamped):**
[10:43] Hi everyone.
[10:45] My name is Jacob Norris.
[10:46] And I've been in the industry about 20 years now.
[10:49] Worked on games like Uncharted 4, Metal Gear Solid 5, and even most recently on Counter
[10:54] Strike 2.
[10:55] I wanted to talk a little bit about how modularity is used in games, and then show some examples
[11:01] of how we actually set up our projects over at Sierra Division when we're planning asset
[11:06] packs and coming up with ideas for how these modular pieces are all going to fit together.
[11:12] Generally, I'll put together a reference board like this that shows, first of all, what it
[11:17] is that we're trying to create.
[11:20] We come to the decision as to what's in the market currently, what do we feel that the
[11:25] market is missing, and what types of assets would be most useful for not only gamers,
[11:31] game types, but then the developers to actually take full control and make assets that are
[11:37] usable on a wide variety of projects.
[11:41] You can see here, when we were coming up with the idea for the oil rig, it really came down
[11:45] to this idea, first of all, that we hadn't seen an oil rig anywhere else on the marketplace.
[11:52] But second of all, it's quite a bit difficult if somebody wanted to scan something like
[11:57] an oil rig.
[11:58] I mean, getting out there on a boat, setting up the actual process of scanning something
[12:04] like this with a drone or a helicopter would be very difficult.
[12:09] So we felt that an environment consisting of an oil rig, which is hard to scan, hard
[12:13] to find references for, and can be utilized for a number of different projects like industrial,
[12:20] sci-fi, and of course, oil rigs or warehouses would be the perfect asset for us to launch
[12:26] ourselves into the marketplace with.
[12:28] Ref boards like this help us understand and break down environments as to what parts we
[12:34] should create first.
[12:36] So if we look at this oil rig, what's it mostly made up of?
[12:39] Of course, pipes.
[12:41] Pipes are a big one because they need to carry all the oil.
[12:45] They're going to be propping up a large structure like this, metal beams, metal pipes, and then
[12:51] of course, lots of catwalks, cooling systems, control panels, and then sort of these shipping
[12:57] container looking types of rooms and such.
[13:00] So now that we understand our core pieces of metal pipes, metal walls, metal beams,
[13:07] we can break these down and understand how we can create them modularly to now build
[13:11] out this environment out of just a few pieces.
[13:15] And while we're using this concept on simple cylindrical, square, and rectangle shapes that
[13:20] fit into this more machinery type of environment, the same idea can spread across to organic
[13:27] environments, architectural spaces, and pretty much anything that can utilize this idea of
[13:33] repetition, small variation, and smart placement to build intricate, unique, and expansive environments
[13:41] with modular sets like this.
[13:43] Well that about wraps up this video on how professional artists utilize modular environment


### Conclusion [13:44]
**Transcript (timestamped):**
[13:48] pieces to create highly detailed and vast environments for AAA game production.
[13:53] We hope this video was informative on the development process and how you can utilize
[13:57] these workflows in your environment creations.
[14:00] We also want to thank Jacob Norris and John Ariano for collaborating with us on these
[14:04] detailed insights.
[14:05] Future technical videos from Sierra Division will provide further insight into this subject,
[14:10] so please leave us a comment and let us know what you would want to see from both of us
[14:14] in terms of creating 3D environments.
[14:17] Are you using modular environment assets for your personal projects or as a working professional
[14:21] at your studio?
[14:22] Let us know your thoughts in the comments.
[14:25] And don't forget to like and subscribe and we'll see you in the next one.
[14:51] Thank you.



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
