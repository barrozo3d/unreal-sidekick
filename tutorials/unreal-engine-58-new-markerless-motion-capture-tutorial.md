---
title: Unreal Engine 5.8 NEW Markerless Motion Capture Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=kxsncXh8hhM
author: World Of VFX
ingested: 2026-06-23
ue_version: "UE5.8"
tags: [mocap, markerless, metahuman, live-link, body-tracking, animation, pipeline, workflow, characters, performance-capture]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-58-new-markerless-motion-capture-tutorial/
frame_count: 4
---

# Unreal Engine 5.8 NEW Markerless Motion Capture Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=kxsncXh8hhM)
**Author:** World Of vfx
**Duration:** 4m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Well now you can do your motion capture instead of one religion without any markers and without your motion capture suit. Well in this video we will talk about this amazing plugin. Let's jump into this video. Well, first we need to jump into fab and just go to search and type markerless press enter and you you can find this meta human animator marker less new plugin. Just need to simply click this install plugin and you can see this window. Now I already have installed this, but if you are doing this first time, you can see your unrelangent one, but it's only available for version 5.8. Now let's jump into unrelangent. Well inside of one religion, firstly you need to go to edit, go to plugins and you need to type meta human and you need to turn on all this plugins should turn on after that simply type live link and you need to turn on this live link and control link for live link this to on and restart your unrelangent. That's it. Now you need to import one meta human character. I already imported this meta human character. Now let's start the video. So first of all, go to tools and type live link and you can find live link hub simply click and it will open a newly launched window. This is called live link hub. So after open this, you need to go to live data, click this capture manager select and and this one of video ingest. Click here and browse your footage folder. So now I just have this footage instead of this new folder. Simply select this folder. Now click on this footage, press add to queue, select the footage and press start. Now if you have an audio file, it will automatically calculate your audio files. Now once it will done, simply minimize this. Now you can find this option called capture manager, then import just go inside of this folder. And now right click go to meta human and click this meta human performance and let's rename to meta. Now double click here. It will open a new window. Now select your footage calibration data like this. So now this is the footage you can see just like this. And after that going down, click this body tracking option. Now this is the main part of this video. Now going up, you to select the character which you want to rig with this character. So simply go to this bvgavin and it's loaded. Now this character will rig from this motion. These are the other all the details. No need to worry about. Make sure the facial tracking should turn down and this body tracking as well. And after that, simply press process. Now this is a long shot. So it will take some time to process. Still you can go and have a cup of coffee and it's done. It's took around 20 minutes to take this. And now once you play, you can simply see both the characters are animated. And just look at this. The hand gestures, the face gestures are actually too good. This is already taking the entire motion. Now let me show you how you can use this motion or how you can export this motion to your region. And then you can export this. Well, first of all, for export this, click this export animation. And you can find your folder. So let's export it here and press save. Export range should be whole sequence of processing range. So I just select this processing range. And for the skeleton, I am just using the existing skeleton. So now you need to select the body which body you want to export or which body you want this character animation to be exported. Automatically this SMKY body was selected and now simply press create. And press add. And it's done. Now you can close or you can minimize this. Now go to contained and you can find this option. Double click. You can see the exact character. Now if you notice there's a female body, don't worry. Simply select here and you can change it to male body. And now you can change all the characters which are rigged properly or not. So this is the leg. This is the pant and this is the body. Well, absolutely everything is working perfectly. Now let's minimize this. Close this window. Now go here. Add a new level sequence. And just name it as usual. Normal and press save. Now you need to create a new camera. Select the camera. And now you need to import the character. So simply go to contain browser. Go to meta human. Select this character. Drag and drop into this. So now you have the character in front of you. So now on the next thing. Select the character. Click on this body. Select this plus button. Go to animation. And you can simply select this as meta which you have exported. And now boom. You have that character animation in front of you. Change the frame range to 250 and boom. You are done. Your character is animated successfully. Well that's it for today. I hope you really enjoyed this video. If you learned something new from this today's video, then definitely subscribe. Comment section is open. If you have any doubts, please do comment. See you next time with some more amazing new content. Till then, keep watching. Keep rocking. Wall of VFX.

**Frame:** tutorials\frames\unreal-engine-58-new-markerless-motion-capture-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
UE5.8 markerless motion capture using the **MetaHuman Animator Markerless** plugin from Fab. No suit, no markers, no external hardware — only video footage. Pipeline: install plugin from Fab → enable MetaHuman + LiveLink + Control Link plugins → open Live Link Hub → Capture Manager → Video Ingest → browse footage → process → export animation → import into Level Sequence on MetaHuman character.

### Summary
4m51s World of VFX quickstart tutorial for UE5.8's built-in markerless mocap. Plugin: MetaHuman Animator Markerless (search in Fab); only available in UE5.8. Required plugins: MetaHuman (all), Live Link, Control Link for Live Link. Workflow: Tools → Live Link Hub → Live Data → Capture Manager → Video Ingest → select footage folder → Add to Queue → Start; audio detected automatically. After processing (~20 min for long footage): import result as MetaHuman Performance asset → configure body tracking → select target MetaHuman character → Process. Export animation via Export Animation button (processing range, existing skeleton, SMKY body). Import into Level Sequence: drag MetaHuman to scene → select body → + → Animation → select exported asset.

### Key Steps
**Install plugin:**
1. Open Fab (in-engine or fab.com) → search "MetaHuman Animator Markerless" → Install Plugin
2. Plugin is only available for **UE5.8** — requires UE5.8 or later

**Enable plugins:**
3. Edit → Plugins → search "MetaHuman" → enable all MetaHuman plugins
4. Search "Live Link" → enable **Live Link** and **Control Link for Live Link** → Restart Unreal

**Import a MetaHuman:**
5. Bring a MetaHuman character into the project (via Bridge or existing asset)

**Live Link Hub — Ingest footage:**
6. Tools → search "Live Link" → open **Live Link Hub** (opens in a new window)
7. Go to **Live Data** → click **Capture Manager** → select **Video Ingest**
8. Click Browse → select footage folder → footage appears; audio files auto-detected
9. Select footage → **Add to Queue** → **Start** → processing begins (allow ~20 min for long clips)
10. Minimize hub while processing

**Create MetaHuman Performance:**
11. After processing: Content Browser → Capture Manager → import folder with results
12. Right-click → MetaHuman → **MetaHuman Performance** → rename (e.g., "meta")
13. Double-click MetaHuman Performance asset → select **Footage Calibration Data**
14. Scroll down → **Body Tracking** → expand (this is the main config section)
15. Select target character (the MetaHuman you imported) → **Process**
16. Wait for processing (~variable duration); facial tracking can be enabled if needed

**Export animation:**
17. Click **Export Animation** → choose folder → Save
18. Export Range: **Processing Range**; Skeleton: **Existing Skeleton**; Body: **SMKY body** → Create → Add
19. Animation asset is now in Content Browser

**Apply animation in Level Sequence:**
20. Create new Level Sequence → name and save
21. Drag MetaHuman character from Content Browser into viewport/Sequencer
22. Select character → click the body section → **+** button → Animation → select the exported meta animation
23. Set frame range as needed → animation plays on character

**Fix body type if wrong:**
24. If character shows wrong gender body: select the body mesh in Sequencer → change from female to male (or vice versa) using the dropdown

### UE Systems / Blueprints / Settings
- **MetaHuman Animator Markerless** (plugin, Fab) — video-based markerless mocap; no suit required; UE5.8+ only; face + body tracking from regular video
- **Live Link Hub** — UE5.8 standalone mocap ingest tool; accessed via Tools menu; Video Ingest mode for footage; queue-based batch processing
- **Capture Manager** → **Video Ingest** — select folder of footage; auto-detects audio files; queues for processing
- **MetaHuman Performance asset** — created from processed mocap data; links footage calibration to target character; Body Tracking section controls body solve
- **SMKY body** — body skeleton export target in MetaHuman Performance; standard MetaHuman body skeleton
- **LiveLink + Control Link** — required plugins for Live Link Hub communication with UE5 editor
- **Body Tracking** — main setting in MetaHuman Performance; choose target MetaHuman character; enable/disable face tracking separately

**⚠️ Version note:** Tutorial targets UE5.8; plugin not available in earlier versions.

### Difficulty
Beginner. Simple plugin workflow; no rigging knowledge needed. Processing time is the main cost.

### UE Version
UE5.8 (plugin unavailable in earlier versions)

### Tags
mocap, markerless, metahuman, live-link, body-tracking, animation, pipeline, workflow, characters, performance-capture

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:29] tutorials/frames/unreal-engine-58-new-markerless-motion-capture-tutorial/frame_000.jpg
- [1:27] tutorials/frames/unreal-engine-58-new-markerless-motion-capture-tutorial/frame_001.jpg
- [2:40] tutorials/frames/unreal-engine-58-new-markerless-motion-capture-tutorial/frame_002.jpg
- [3:53] tutorials/frames/unreal-engine-58-new-markerless-motion-capture-tutorial/frame_003.jpg

## Related Entries
- `the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56.md` — comparison of 4 mocap solutions (UE5.6); MetaHuman Animator Mono Video Ingest (similar but requires calibration video); pricing comparison
- `unreal-engine-58-release-notes.md` — UE5.8 release notes; context for what else is new in 5.8
- `this-free-plugin-changes-filmmaking-forever-unreal-5.md` — alternative animation approach: Mixamo + OneClick Control Rig (no mocap required)
