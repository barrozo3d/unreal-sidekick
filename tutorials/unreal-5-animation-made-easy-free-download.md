---
title: Unreal 5 Animation Made Easy! [FREE DOWNLOAD]
source: YouTube
url: https://www.youtube.com/watch?v=OLwLqjBtSKk
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, control-rig, mixamo, sequencer, ik-fk, workflow, pipeline, characters, free-download, filmmaking]
extraction_status: complete
frames_dir: tutorials/frames/unreal-5-animation-made-easy-free-download/
frame_count: 2
---

# Unreal 5 Animation Made Easy! [FREE DOWNLOAD]

**Source:** [YouTube](https://www.youtube.com/watch?v=OLwLqjBtSKk)
**Author:** Josh Toonen
**Duration:** 3m2s | 2 section(s)

---

## Raw Data (for Claude Code extraction)


### Create Your Own Cinematics in UE5 [0:00]
**Transcript:** Animating in Unreal just got 10 times easier.  Introducing the one-click rig.  We just made a three-plug-in that makes animation easier than ever before.  Now, anyone can be a filmmaker in Unreal,  without knowing how to rig, how to model, or how to animate yourself.  You don't even need to use expensive motion capture.  That's right, with this plugin, anyone can add characters and start animating in seconds.  Let me show you how it works.  Choose your character!  To start off, you don't need to rig anything yourself.  Did you know you can rig your 3D characters for free using Mixamo.com?  Just upload a 3D model of any character.  Mixamo will auto-generate free rigs and free animations for you to quickly drag and drop into your scene.  You can create entire action sequences and fight choreography just using these animation clips.  But here's the problem.  You can't edit or modify these animations easily in Unreal 5.  That was until now.  If you want to animate characters in Unreal, then you need a control rig.  And the one-click rig will make one for you instantly.  If I want to edit this further, now all I have to do is right click on my character  and then bake this to our control rig.  This will transform our animation clips into animations we can edit.  You can change the arms or legs to fix things like the collisions of the feet  or change things like how a soldier aims their rifle.  And you can modify anything right here inside a sequencer.  You can also clean up motion capture without leaving Unreal using this method.  And lastly, you can start animating characters from scratch all the way from T-Pose to Final Animation,  directly in your viewport.  Using the FK rig, you can modify punches and running animations.  And with IK controls, you can easily fix the feet colliding with your ground plan  or adjust your characters' hands to attach them to a lightsaber or a rifle.  So if you want free animations in your projects, let's walk through how to download and use the one-click control rig.

**Frame:** tutorials\frames\unreal-5-animation-made-easy-free-download\frame_000.jpg

### How to Download and Install the One Click Control Rig [1:46]
**Transcript:** Download the one-click rig right now at Unreal for VFX.com slash rig.  And to add this to your Unreal projects, don't add this to your content folder,  create a new folder called Plugins and paste the download inside.  And then in your content browser, you go to Settings and Show Plugins folder.  Then click and drag the one-click rig and make a copy next to your character.  Now let's apply our one-click rig to our Mixamo character.  Open up the control rig file, just right-click on the background, hover down to refresh, pick your character, and then let's click.  And now your character is ready for animation.  Just drag them into sequencer and you're ready to go.  Whether it's Godzilla swiping down helicopters or soldiers shooting down a horror-to-zombies,  animation has never been easier in Unreal 5.  And I got to give props to Camilla Bianchi who created the one-click rig.  She's a technical animator at Frames Store London and she's worked on some awesome projects like Sanoa's Hellblade 2.  And she's used control rig from the very beginning.  So download the one-click rig and use it for free on your own projects.  And if you're new to Unreal, but you want to start making your own blockbuster films,  join our 21-day Unreal Filmmaking Boot Camp, Unreal Fundamentals.  We'll help you be VFX Studio ready and make your own films in Unreal 5.  Subscribe to the channel for more free plugins and tutorials just like this and I'll see you next time.  Peace!

**Frame:** tutorials\frames\unreal-5-animation-made-easy-free-download\frame_001.jpg


---

## Structured Notes

### Core Technique
Short promotional intro for the free OneClick Control Rig plugin. Pipeline overview: Mixamo auto-rig → UE5 import → OneClick Rig install (Plugins folder) → bake animation to control rig → edit via IK/FK in Sequencer. Created by Camilla Bianchi (technical animator, Framestore London; Hellblade 2). See the full tutorial `this-free-plugin-changes-filmmaking-forever-unreal-5.md` for step-by-step details.

### Summary
3m2s Josh Toonen promo/intro video for the OneClick Control Rig. Short companion to the full tutorial. Covers the motivation (Mixamo animations can't be edited easily in UE5 without a control rig) and the solution (OneClick Rig converts Mixamo skeleton animations into editable control rig keyframes instantly). Install summary: download from unrealforvfx.com/rig → create Plugins folder in project → paste inside → Settings → Show Plugin Content → duplicate and assign per character. Bake animation → Sequencer editing with IK/FK. Use cases: fix feet clipping, adjust rifle aim, clean up mocap, animate from T-pose. Credit: plugin created by Camilla Bianchi (technical animator, Framestore London; Hellblade 2).

### Key Steps
*(Short promo — see `this-free-plugin-changes-filmmaking-forever-unreal-5.md` for full pipeline steps.)*

**Quick install summary:**
1. Download OneClick Rig at unrealforvfx.com/rig
2. In project root: create a folder named exactly `Plugins` → paste downloaded plugin inside
3. In UE5: Settings → **Show Plugin Content** → find OneClick Rig in Content Browser
4. Duplicate the rig asset → place next to character → open → right-click background → Refresh → click character to assign
5. Drag character into Sequencer → right-click → **Bake to Control Rig** → start editing

### UE Systems / Blueprints / Settings
- **OneClick Control Rig** (by Camilla Bianchi, free) — auto-creates Control Rig for Mixamo-rigged characters; supports IK (endpoint goal) and FK (rotation chain) per limb; bakes animation clips into per-frame editable keyframes
- **Plugins folder** — project-level plugin installation; must be named exactly `Plugins` (no dashes); plugin appears in Content Browser after enabling Show Plugin Content
- **Bake to Control Rig** (right-click in Sequencer) — converts clip animation to Control Rig keyframes; enables frame-by-frame editing in Sequencer

### Difficulty
Beginner. Three-minute overview; full workflow in companion tutorial.

### UE Version
UE5

### Tags
animation, control-rig, mixamo, sequencer, ik-fk, workflow, pipeline, characters, free-download, filmmaking

---

## Related Entries
- `this-free-plugin-changes-filmmaking-forever-unreal-5.md` — full 16-minute step-by-step tutorial for the same OneClick Control Rig pipeline; constraints, additive tracks, motion blending
- `stylized-animation-control-rig-characters-in-unreal-engine-5.md` — ACOM modular rig; UE's built-in Control Rig for MetaHumans
- `ue5-constraints-are-easy-parent-constraint-workflow-for-animators.md` — parent constraints; hands-to-weapon workflow
