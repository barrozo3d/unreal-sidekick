---
title: UE 5.8 LOCAL & FREE Video MoCap (In 3 Minutes!!)
source: YouTube
url: https://www.youtube.com/watch?v=jS4h-24EnbQ
author: Royal Skies
ingested: 2026-08-02
ue_version: "5.8"
tags: [mocap, metahuman, monocular-mocap, metahuman-animator, live-link-hub, capture-manager, animation-retargeter, fbx-pipeline, beginner, ue5-8]
extraction_status: complete
frames_dir: tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UE 5.8 LOCAL & FREE Video MoCap (In 3 Minutes!!)

**Source:** [YouTube](https://www.youtube.com/watch?v=jS4h-24EnbQ)
**Author:** Royal Skies
**Duration:** 3m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:44] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_000.jpg
- [1:17] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_001.jpg
- [1:35] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_002.jpg
- [1:50] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_003.jpg
- [2:07] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_004.jpg
- [2:13] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_005.jpg
- [2:38] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_006.jpg
- [2:48] tutorials/frames/ue-58-local-free-video-mocap-in-3-minutes/frame_007.jpg

---

## Structured Notes

### Core Technique
Using UE 5.8's built-in **MetaHuman Animator Monocular Footage** pipeline (via Live Link Hub's Capture Manager) to convert a pre-recorded 2D video file into full-body motion-capture animation on a MetaHuman, entirely locally and for free (no paid mocap service, but GPU/CPU heavy).

### Summary
A rapid-fire setup guide (3 minutes) for local, free, video-based mocap new to UE 5.8. Fair warning up front: it's hardware-hungry — the author's own machine (RTX 3090-tier GPU + 48GB RAM, transcribed as "TI 30") crashed repeatedly, so the demo footage shown is actually from a friend's machine, though the steps are identical. Covers the full chain from a clean Epic Games Launcher install through plugin enablement, MetaHuman character creation, ingesting a video file as a capture source, running the MetaHuman Performance solve, and finally retargeting the resulting MetaHuman animation onto the standard UE5 Mannequin skeleton for use outside MetaHuman-specific contexts.

### Key Steps
1. Install **UE 5.8** via Epic Games Launcher; during install, ensure **MetaHuman Creator core data** is checked (can also be enabled later under Options if missed).
2. From Fab, download and install the **MetaHuman Animator** plugin (which includes **Monocular** motion-capture support — transcribed in the auto-captions as "Markalus," confirmed via on-screen UI as **Monocular Footage** capture type) into the 5.8 engine install.
3. Create a new default UE 5.8 project → Edit → Plugins, enable: MetaHuman Animator, Monocular Motion Capture, MetaHuman Core ML, MetaHuman Creator, MetaHuman Live Link, MetaHuman SDK. Missing plugins usually trace back to skipping the MetaHuman install checkbox (step 1) or the Fab plugin (step 2). Restart the editor when prompted.
4. Right-click in Content Browser → MetaHuman → MetaHuman Character, name it (e.g. "test animation"), open it in the **MetaHuman Creator** editor, pick any preset on the left, hit **Assembly** → **Create Full Rig** → **Download Texture Sources** → **Assemble** to generate the MetaHuman Blueprint.
5. Tools → **Live Link Hub** → Live Data → **Capture Manager** → Add Device → **Mono Video Ingest**. Under the device, point it at the folder containing your source video(s), select the specific video, **Add to Queue**, optionally adjust output quality (bottom right; default is fine), then **Start** (device/pipeline named "Mono Video Ingest" in the Devices panel and Take Browser).
6. Once ingest completes, close Live Link Hub. In the Content Browser: Content → Capture Manager → Imports → Mono Video Ingest — the ingested take appears there as a folder.
7. Right-click → MetaHuman → **MetaHuman Performance**, name it, open it. Top right: **Capture Footage** dropdown → select the ingested video. Confirm **Body Tracking** is checked (Capture Type shows as **Monocular Footage** in the Data panel). Drag your MetaHuman character Blueprint into the character slot — it should preview in the viewport.
8. Hit **Process** — this solves the video onto the character's skeleton. Realistic processing time is **hours**, not seconds/minutes (contrast with the "3 minutes" clickbait framing of the video's own title). When done: Save → **Export Animation** → Create.
9. To use the result outside MetaHuman-specific rigs: right-click the new animation → **Retarget Animations**, choose the default UE5 Mannequin as target skeleton, select the source animation, choose an export destination, hit **Export** — produces a standard Mannequin-skeleton animation asset ready for Sequencer/Animation Blueprints.

### UE Systems / Blueprints / Settings
- **Plugins:** MetaHuman Animator, Monocular Motion Capture (Fab add-on), MetaHuman Core ML, MetaHuman Creator, MetaHuman Live Link, MetaHuman SDK.
- **Tools:** Live Link Hub (Capture Manager: Add Device → Mono Video Ingest, Take Browser, job queue with output-format settings), MetaHuman Performance asset (Capture Footage selector, Body Tracking toggle, Data panel showing Capture Type = Monocular Footage, character-actor drop slot, Process button), Retarget Animations dialog (source/target skeleton pickers, defaults to UE5 Mannequin template when no target mesh is assigned).
- **Hardware note called out explicitly:** this is a heavy local compute workload — the author's high-end desktop (~RTX 3090-class GPU, 48GB RAM) still crashed; budget for a multi-hour Process step, not real-time.

### Difficulty
Beginner-friendly instructions (pure menu/plugin/button steps, no scripting), but Intermediate in practice due to hardware requirements and multi-hour processing times.

### UE Version
UE 5.8 (MetaHuman Animator Monocular Footage feature is new to this release).

### Tags
mocap, metahuman, monocular-mocap, metahuman-animator, live-link-hub, capture-manager, animation-retargeter, fbx-pipeline, beginner, ue5-8

---

## Related Entries
- `tutorials/new-unreal-engine-58-metahuman-markerless-mocap-tutorial.md` — the other half of UE 5.8's new MetaHuman Animator mocap suite: **Markerless** (live webcam, no capture-manager ingest step) vs. this video's **Monocular** (pre-recorded video file via Capture Manager) capture mode; shares tags: mocap, metahuman, metahuman-animator.
- `tutorials/unreal5-markerless-mocap-clean-up-process.md` — a natural next step after this video's output: cleaning up the resulting animation curves in Cascadeur once it's back in Unreal; shares tags: mocap, fbx-pipeline.
- `tutorials/how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5.md` (Mimem.ai pipeline, tag `#markerless-mocap`) — a third-party paid alternative doing a similar FBX-import-then-retarget flow, useful to contrast cost/quality against this free, local, monocular-footage approach.
