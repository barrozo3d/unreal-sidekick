---
title: Live Link Hub Tips | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=JdaXti950vg
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [live-link, motion-capture, metahuman, virtual-production, facial-animation, animation, performance-capture, timecode, recording]
extraction_status: complete
frames_dir: tutorials/frames/live-link-hub-tips-unreal-engine-animation-hub/
frame_count: 4
---

# Live Link Hub Tips | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=JdaXti950vg)
**Author:** Unreal Engine
**Duration:** 6m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to the Animation Hub. Today I'm going to show you some tips for setting up and using the Live Link Hub to manage Live Link data. This includes recording data, as well as managing the Live Link streams that can be sent to multiple work sessions. Live Link Hub is a standalone app, as long as you have the plugin enabled, you can go under the Tools menu and launch Live Link Hub. Set it to come up here. So looking at left and right, I can add a source, add my Captury Body. As soon as I do that, I have the subject that is being streamed from my Captury system. This will appear in the Editor menu. You can see on the right I have clients. The clients are the workstations that are on the subnet. These two workstations that are currently on the same subnet that have the Editor launched. This is the one that I'm working with. This is another one. It will also tell you what level the other workstation is launched into. So let's add some more sources. I'm going to add the OptiTrac. I can have multiple systems come in at the same time. OptiTrac here, you can see that appears and immediately Live Link and Editor updates. Now we're going to add I have linked face. So in the face, see it looks like it's disconnected. I have met a human animator running on an iPhone and streaming over Wi-Fi. I'm going to just put in the IP of my phone. This Tony face. You can go ahead and connect. And just like that, we have Tony face is now streaming and also updated in Editor. What's handy with the Live Link hub is you can also add a virtual subject. Virtual subject then simplifies the process of getting body on face. On to a metahuman. I combine them together as one Live Link stream. So I have my virtual Tony here. I'm going to go ahead and choose Tony and his face. Combine the two of those as my subjects. You can see now Tony Green. However, you don't see a virtual Tony in Editor. In order to do that, you need to read broadcast and just like that. I have Tony working and this is my live face speaking to you in real time. Bring back the hub. Things you can also do once you have a Live Link setup is you can. Babe your config. This will default to the Live Link hub content folder. So I can save a config, which I already have one here. And recall the setup, including your virtual subject that you've come through the trouble of creating. Other things to note is there's a plugin directory. So this will show you the plugins. That are available and what's been enabled. You can also if you have other plugins you want to add to the hub, you can add your own directory. Just the plugins are in a different path. But I hadn't posed that. There's also. There's that as well. There's also a settings menu where you can update some of the fault settings. How live link starts up. Something to note on the face is I can go ahead and. Calibrate my neutral pose. From the live link hub when I go ahead. Get my neutral. I'm updating that. You can also note that I don't have the head of orientation and translation coming through from the medic human animator. Because capture is the driving source of the neck and head bone. I want to make sure as well when I go to the virtual. Tony. The publication and rotation of the head. I'm going to keep the parent, which in this case is a capture system. So a re broadcasting have live data there. So I can go ahead and. And create a new session name. And create a slate. That. And all these subjects are active. So go ahead and press the record button. Starts recording. Yes, this is live link data being record. Audio and fake. And then stop. Now that we've made a recording and switched to the recording list. And double click on our last take. I'm just going to move this up here. And you can see we have a timeline here. We can scrub. We can play. One more thing to show you before we finish up is you can actually use your live link. So if you have a live link up. Super useful. Remember, you can see I have system time. You can set things there. I can change this. I would use the subject name. I'm going to use my subject. That is from my opti track system. And you'll know it's gray at the moment. When I enable it turns green, the time code changes. And now my opti track is being used as my time code source. And I have it. That's a wrap.

**Frame:** tutorials\frames\live-link-hub-tips-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Live Link Hub is a standalone app (launch via UE Tools menu) that manages and routes Live Link data from multiple motion capture sources to multiple UE Editor workstations simultaneously. Virtual Subject combines body + face sources into a single stream. Config save/recall persists full setup. Supports recording, timecode sourcing, and plugin extension.

### Summary
6-minute Epic tutorial demonstrating Live Link Hub for multi-source motion capture streaming (body: Captury, face: Meta Human Animator on iPhone via WiFi + OptiTrack). Shows: adding multiple sources simultaneously; client panel (other workstations on subnet); Virtual Subject (combines body + face into one stream, requires Broadcast to appear in Editor); config save/recall; plugin directory management; face neutral pose calibration; head bone priority when combining sources (Captury drives neck/head — disable head orientation/translation from face source); recording (session name → slate → Record → stop → playback in Recording List); OptiTrack as timecode source.

### Key Steps
1. **Launch Live Link Hub** — Tools menu → Live Link Hub (requires Live Link Hub plugin enabled)
2. **Add sources** (left panel → Add Source):
   - Body: Captury Body, OptiTrack (add simultaneously — sources stack)
   - Face: Meta Human Animator (iPhone over WiFi) → enter phone IP → Connect
3. **Clients panel** (right) — shows all UE Editor workstations on same subnet; indicates which level each is running
4. **Virtual Subject** (combine body + face for MetaHuman):
   - Add Virtual Subject → name it → select body subject + face subject → combine
   - Click **Broadcast** on virtual subject → now appears in UE Editor
5. **Head bone priority when combining**:
   - Face source (Meta Human Animator): disable head orientation + translation
   - Virtual Subject settings: head position/rotation → keep parent = capture system (Captury/OptiTrack drives neck/head)
6. **Face neutral pose calibration** — Live Link Hub → face subject → Calibrate Neutral Pose
7. **Save/Load Config**:
   - File → Save Config → saves to Live Link Hub content folder (includes virtual subjects)
   - Recall config to restore full setup without re-configuring sources
8. **Plugin Directory** — Settings → Plugin Directory; shows enabled plugins; add custom paths for third-party plugins
9. **Recording**:
   - Create session name + create slate
   - Press Record → captures all active subjects (audio + Live Link data simultaneously)
   - Stop → switch to Recording List → double-click take → timeline with scrub and playback
10. **Timecode from mocap** — select timecode source from hub; choose subject (e.g., OptiTrack); gray = disabled, green = active; timecode updates live

### UE Systems / Blueprints / Settings
- **Live Link Hub** — standalone app; Tools menu → Live Link Hub; requires Live Link Hub plugin; manages multi-source Live Link routing to multiple Editor workstations
- **Live Link Source** — hub left panel; Add Source button; types: Captury Body, OptiTrack, Meta Human Animator, ARKit face (iPhone), custom; multiple sources active simultaneously
- **Live Link Clients** — hub right panel; workstations on subnet with UE Editor open; shows current level each workstation is running
- **Virtual Subject** — combines multiple Live Link sources (body + face) into single stream; must Broadcast for it to appear in UE Editor; head priority setting controls which source drives neck/head bones
- **Meta Human Animator** — iPhone app; streams face data over WiFi; enter iPhone IP in hub to connect; face neutral calibration in hub
- **Broadcast** — virtual subject must be broadcast before it appears in UE Editor's Live Link panel
- **Config Save/Recall** — saves entire hub setup (sources, virtual subjects, settings) to Live Link Hub content folder; recall restores without reconfiguration
- **Recording** — session name + slate → Record button → captures all active subjects + audio; Recording List → double-click take → timeline scrub/playback
- **Timecode Source** — Live Link Hub can act as timecode provider; select subject (e.g., OptiTrack) as source; gray = disabled, green = active

### Difficulty
Intermediate-Advanced. Requires physical mocap hardware (Captury, OptiTrack, iPhone). Conceptual knowledge of Live Link, MetaHuman, and bone hierarchy needed to correctly configure head bone priority in Virtual Subject setup.

### UE Version
UE5 (Live Link Hub, Meta Human Animator integration — UE5 era features)

### Tags
live-link, motion-capture, metahuman, virtual-production, facial-animation, animation, performance-capture, timecode, recording

---

## Related Entries
- `lip-sync-in-unreal-engine.md` — lip-sync documentation (empty crawl)
- `live-link-in-unreal-engine-5.md` — general Live Link setup in UE5 (if exists)
