---
title: UE 5.8 LOCAL & FREE Video MoCap (In 3 Minutes!!)
source: YouTube
url: https://www.youtube.com/watch?v=jS4h-24EnbQ
author: Royal Skies
ingested: 2026-08-02
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/
frame_count: 0
frame_status: pending-selection
---

# UE 5.8 LOCAL & FREE Video MoCap (In 3 Minutes!!)

**Source:** [YouTube](https://www.youtube.com/watch?v=jS4h-24EnbQ)
**Author:** Royal Skies
**Duration:** 3m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ue-58-local-free-video-mocap-in-3-minutes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So Unreal 5.8 just came out with their own video to motion capture software and you'd like to try it yourself.
[0:05] Not a problem.
[0:06] Fair warning though, you're gonna need a pretty strong computer for this.
[0:09] I have a TI 30 and about 48 gigs of RAM and that was not enough.
[0:13] My computer kept crashing.
[0:14] So the recorded footage of this animation working is actually from my friend, but the steps to get it working are the same.
[0:20] To start you're gonna have to download the Epic launcher.
[0:22] Then from the launcher you hit plus and you get the 5.8 engine.
[0:25] And then make sure MetaHuman creator core data is checked when you install.
[0:29] But if you forget to do this, you can just go to options and check it to apply it later on.
[0:33] So don't sweat it.
[0:34] You also need to go to the fab market and download the MetaHuman animator, Markalus motion capture plugin.
[0:38] Then once you have the plugin, you install it to 5.8.
[0:41] Once you've done this, you make a new default 5.8 project.
[0:43] You go to edit plugins, MetaHuman animator, Markalus motion capture, MetaHuman core ML,
[0:49] MetaHuman creator, MetaHuman live link and MetaHuman SDK.
[0:53] If you don't see these plugins, it's probably because you did not check the MetaHuman stuff during installation.
[0:57] And if you don't see the Markalus mocap data, it's because you forgot to install the plugin from fab.
[1:02] Regardless, once you've got all these checked, Unreal will want to restart.
[1:05] And right after that, the first thing you want to do is create a new MetaHuman character that will
[1:08] receive the animation.
[1:10] Right click MetaHuman, MetaHuman character.
[1:12] Just name it something like test animation, double click it and then open the MetaHuman creator editor.
[1:17] On the left, just click any preset you want and hit assembly.
[1:20] And at the top, create a full rig, download the texture sources.
[1:24] Down here, hit assemble, which will create the MetaHuman character blueprint, which you can find right here.
[1:29] Once you have it, you go to tools and then if you scroll down under live link hub, go to live data,
[1:34] capture manager, add device, model video and jest.
[1:38] Select it here.
[1:38] Under devices, select the folder that has all the videos you want to capture.
[1:42] Select the video that you want animations from and add to queue.
[1:45] At the bottom right, you can change the settings of the output quality.
[1:48] I just leave it at default and then hit start.
[1:51] Once it's complete, you can close the live link hub and in your asset browser, content,
[1:55] capture manager, imports, mono video and jest, you will find a folder for the video we just ingested.
[2:00] Then you right click MetaHuman, MetaHuman performance.
[2:04] Just name it something like test animation, click it to open it.
[2:06] At the top right, select the capture footage and select your video.
[2:10] Then you scroll down and make sure body tracking is checked.
[2:13] And then under here, you're going to want to drag your character into this slot right here.
[2:17] You should see a show up in this window.
[2:19] Then you just hit process and this will start to map the video to your character's skeleton.
[2:23] Now this process usually takes a few hours and when it's over, you just save, export your animation
[2:29] and create.
[2:30] Now you will have a MetaHuman mocap animation and if you want to turn this into an Unreal 5
[2:34] animation, just right click retarget and if we just hit the default mani skeleton and select
[2:39] the animation that we just created, export the animation, decide where we want to export it
[2:44] and hit the export button.
[2:45] Now we have the retargeted animation.
[2:48] And you're done.
[2:49] Hope that helps and as always I'll be having a fantastic day and I'll see you around.



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
