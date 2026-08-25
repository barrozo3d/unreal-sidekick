---
title: UE5 Curve Editor SECRETS: Buffer Curves & Smart Snap Keyframe Tricks
source: YouTube
url: https://www.youtube.com/watch?v=9g0K4GOACis
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, curve-editor, sequencer, buffer-curves, tween, bake, workflow, technique, keyframes, tools]
extraction_status: complete
frames_dir: tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/
frame_count: 4
---

# UE5 Curve Editor SECRETS: Buffer Curves & Smart Snap Keyframe Tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=9g0K4GOACis)
**Author:** Unreal Engine
**Duration:** 14m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Welcome back. In this video, we're going to take a look at some different techniques to work with animation data, specifically when it comes to the curve editor. And we're going to take a look at shot 40. So, in our uh project here, I'm inside of shot number 40 right here. This is the level sequence I've opened, and we're taking a look at the characters running down the corridor. Now, I'm going to go ahead and just work with the Anom work project. I've also muted the baked animation subsequence and I've brought back up the control rig live an animomwork subsequence because inside of here is the beta character with all of the original key frame data uh from the original animator. So with this in mind, there's one other thing I want to do and that is to actually add a camera cuts track into this sequence right here. Uh I don't have an easy way to get in and out of this camera view. And so if I add a camera cut track, because I'm sort of breadcrumbming my way back down into this level sequence, this subsequence here, uh I am able to access the camera using this camera cut track boop to get in and out. Now, this works even though I don't have a camera in this particular sequence because I'm loaded in through this larger sequence and this larger sequence actually has the camera in it. So, because I'm in a sequence with a camera and then I'm deeper into a subsequence by adding a camera cut track, I can still access that camera from the above inherited level sequence. So, little tip for you there. Now, uh that's just giving me a little button that I can get in and out of the camera. It's not super important for what we're doing today, but I find it useful. So, what I'm going to do is I'm going to select my beta character and I'm going to twirl them down and click on the control rig. This will automatically kick me into animation mode if I'm not already there. But if you're like, "Wait a minute, where's my rig?" Try hitting G. G is game mode and it's the thing that always shows and hides control rigs and it might be the the easiest way to get lost of like where are my controls. Anyways, so here's what we're going to do. We are going to modify some of the animation data. But before we do, I'm going to show you some different techniques I like to use when animating uh in Unreal Engine. So, I'm going to grab the body control for Beta character running around here. Now, the body control is sort of the main thing driving the character's motion. And I'm going to use the LZ, which is the up and down. Now, he has this up and down bounce as he runs around. I've even messed with this in a previous video where I made them, you know, I've adjusted the way that the uh up and down works. But before I make any changes, let me give you a tip. I want to buffer curve everything. I want to basically have Unreal take a snapshot of whatever these curves currently look like so I can always get back to them if I don't like my changes later. So to do that, I'm going to go ahead and do that for the entire character. Now, I could select all the controls a couple different ways. I could drag select, you know, do a marquee select and just try to grab everything this way. That's going to grab everything that's visible, but then there's some stuff that might be hidden. So, one thing I like to do is over here in the top right corner, we have our anim outliner. When I select a control, it'll also show things in the NM details down here. But what I can do is where we have beta beta control rig. Uh, by the way, there's more stuff up here because we have gamma in the shot as well, which is the little uh four-legged quadriped character. What I'm specifically working with the big guy. So, I'm going to find beta. Here's his control rig, and I'm going to altclick on the beta control rig. Alt clicking will almost act like a selection set and it'll grab everything inside of that that selection that that section. Uh I can also just alt click on spine for example and it'll grab everything inside of the spine hierarchy and down. Now you'll notice it's grabbing everything down below it which is you know helpful potentially but if you're just like oh I just I wish I could just alt click on arm and just get the arm things. I don't want all the configure controls and everything else. I just want the arm section. You can do that. I can switch my atom outliner up here in the top left corner. There's a little dropdown where I can flatten the modules. And if I flatten the modules, it actually sort of takes away some of the hierarchy behaviors of this editor. So now I have the beta control rig. And you can see I have the spine stuff, the neck stuff, all these different things. For example, the arm, and they're no longer cascading down into a different hierarchy system. So now if I alt click on left arm, it'll actually just grab that section. So now I've just created a way to use selection sets inside of my anim outliner. Very handy. Now for what I'm trying to show you here, this does not help us. I'm going to go ahead and undo that. I'm going to go back and I'm going to unflatten the modules. And now I'm going to go back and just say altclick on the control rig as a whole. That grabs everything in my character. All the different controls, hidden or not, they're all selected, right? Lots of stuff grabbed. I'm going to go back to my sequencer curves. Lots of things here in the curve editor. grab everything. I'm going to rightclick and I'm going to buffer curves. There's a lot of different curves here, so I'll just go I'll just buffer all of them. Boop. And what that's going to do is, in case you're not familiar with buffer curves, maybe you've done this in Maya, maybe this is new to you. Uh, what buffer curves allow you to do, if I select my body control, I can show you. I'll specify just the LZ, the up and the down, right? The, uh, the bounce of his run. And what this will do is if I make a change to something, maybe I want to have them jump higher. I'll just move these curves up like that. And you'll see I'm left with the ghost of animation past, right? These little ghost icons of where these curves used to be. When I make changes, whether I delete curves, whether I change the timing of things, whether I just change the values, whatever, I can see where the animation data used to be. whenever I did that snapshot, that's what the buffer curve is holding in place. And if I make a bunch of changes and say, "Oh, you know what? I don't like what I've done. I wish I could go back." It's a really easy way to instead oft Z undoing a million times. I can just select the curve, rightclick, and say swap buffer curves. Boop. And it sends me back to the version I had previously. Now, you can see that I now have a ghost of where I just had changed things to, right? So, I'm allowed to have one snapshot per curve buffered at any given moment. So, I'll go ahead and swap it back. Right now, if I want to say, you know what, discard what I'm currently doing, just set me back to whatever's currently in the buffer, whatever the current ghost is, I can say apply. Boop. And it'll set me back to whatever the ghost is. So, you have to keep in mind which one you have ghosted, whether it's your current or your new stuff, right? Or the old or the new, whatever. But buffer covers are really, really handy in keeping the workflow in a non-destructive spirit. It's a destructive workflow in that I am changing the animation curves, but I can easily go back or at least compare with what was originally there, which makes my life a lot easier. And if I want to say, oh, you know what? I want to change this and you know, I like this curve more now. I wish I could just make this the new buffer. That's fine, too. Right click, just do a new buffer curve. Boop. Makes a new snapshot. And so that will now be what it holds in memory. So, that's the first thing when you're dealing with a lot of different key frame data. And that's the thing, that's why I grabbed every single control on the character because if I go grab his head control, you can see that his head control also has buffer curves for everything, right? So, every single thing on this character is now buffered. Now, I don't believe this will persist if you close Unreal and reopen it. I think you need to buffer every time. I think that's the same in most tools. But, uh, while you're working here, super super handy. Now, the next thing I want to show you are a couple just easy filters, things you should know about when working with animation data. I'm going to just keep focused on the body control. And actually, let me jump back into my camera view so I can track with the character. Right here it is running around. Uh, and actually, let's let's maybe mess with the rotation instead. So, let's say I were doing something with the rotation channels in X, Y, and Z. Uh, first of all, graph editor. Couple things you want to know. If I select rotation controls, I can hit this button here, or I can rightclick and go to oiler filter, or I can also go to filter and find oiler filter here. Three different ways to get to the same thing. The oiler filter is a very, very commonly known and very useful uh tool that you'll find in almost every graph editor in 3D. Helps with over rotations, gimbal lock issues, different things like that. You're going to want to know where that is. So, that's where that lives. You can also access a variety of different filters by hitting this button or right clicking and going to filter. And this is where you're going to find all kinds of useful things. Forier transforms are going to have things for highpass and lowass basically smoothing algorithms. You can go to Butterworth here, a popular smoothing algorithm. There's also simplify, smart reduce. There's a bunch of different things here you might want to know about. But not everything is uh similar to where here we have these tolerance sliders. Smart reduce. We can, you know, adjust these values. Some operations like the oiler filter or the smart snap don't have settings. You just hit them and you hit apply. Let me give you an example of what some of these things can do. Uh let's say that I'm dealing with a lot of the key frames. I'll go ahead and just grab everything on beta control rig, right? Lots of data. Alt click on that. Get everything. Let's say that for whatever reason I want to deal with all of the animation data all at once. Now, I can change the view mode to maybe normalize mode, and that'll show me all the key frame data in one big spaghetti soup. Probably not that helpful, but you know what? We're going to do it. If I pull all this up, it's a little bit sluggish because I've got, you know, thousands of key frames on, well, yeah, thousands of key frames on thousands of controls, a lot of data selected. I can go to bake. And you might know bake as something that you can do where you, you know, you take a curve and actually maybe I'll show you this one at a time. If I take the body control and I take, you know, just one of these things. If I take a curve and I select it and I hit bake, it'll add keys on every single frame of that curve. That's typically what we know bakes to be. However, we can also in mass I can grab every single thing on this character, you know, get everything to populate. I'll grab all the different key frames and we can reduce bake. I can use the bake tool and change the interval from bake on ones to maybe say h bake every five frames. And if I now say go ahead and apply that, it will now bake the animation data on fives. And even though it already had, you know, more dense data, it now reduces the density of the data. And so now it's taken my animation, baked it down onto fives. And uh it's a little bit of an odd way to do things, but maybe if I, you know, I'll focus in on just the body for a second. And you can see here what this has done. If I focus on just the LZ once again, this is why buffer curves are really handy. That just reduced the density of my key frames by a lot. But if you're like, oh no, maybe I've lost some useful information. You know, a lot of the running still works, right? He's still running, but we've definitely lost some of that zest. That's what the buffer curves are useful for because now we can compare. Maybe I'll go back to the absolute view here. Uh we can compare whatever the curve currently looks like to what it was before. So if I need to come and change maybe the up and down, maybe that uh five key frames was a little bit low resolution for you know some of the data here. I can easily go back and through the buffer curve I can see where the data used to be. So, you know, if I need to make some adjustments, tweak some timings, tweak some values, it makes it pretty easy to see where I came from and, you know, what I might want to preserve if I need to make some adjustments. So, now I don't know, hopefully that's helpful. It's a little bit of an odd use case to show you this, but the main thing I wanted to show you is that you can take really dense key frame data and you can use the bake tool not just to bake animation down on ones, but to unbake it to a a more sparse uh key management situation. And uh by combining that with buffer curves, it allows you to see what the data looked like before and after. That way, if you need to make any adjustments, you know, maybe you had something useful that oh, we lost this extreme right here on this frame. I can just kind of tweak the timing of some of these and uh you know keep a little bit more of that spirit intact. And the last thing I'll mention, we will cover this in a future video, but I just want to point out that here in the curve editor, the other thing that you will probably notice is that we have a wonderful tween tool, right? Already built in here inside of our curve editor. We do have one up here in the uh tween button here. This will give us one for our viewport, all the different modes. We also have this one down here. And these can be set to different things. There's a bunch of great hotkeys. We'll cover it more in depth, but uh these tween tools super super handy for blending and adjusting curves, not just individually, but as a whole. You know, we have all kinds of cool things. Lots of different options. The one that I'll point out to you just really quickly. I'll go ahead and just keep using my up and down. This time I'm actually going to go and turn off the buffer curves. I don't want to see them right now. So, I'll turn that off and then I'll reselect my curve. Now, the buffer curve stuff is gone out of the way. Uh, one thing when you're doing with a lot of keys, for example, all the different stuff I had on this character, I can set this to smooth and rough. And what that's going to do, if I select all these curves, if I go to smooth, it'll start to reduce the amount of contrast from key to key or rough will add contrast. And so, this is a quick way I can just keep click click click and I'll smooth out the animation overall or click click click add more bumpiness to it. And so if you're dealing with, you know, lots of key frame data, one of the really common use cases of that is something like motion capture where maybe you have some jittery or buzzy motion capture. And the smooth rough um tween tool can be really really handy, especially in that combination with buffer curves. And of course, one last thing just to show you this, I can select everything on this character once again, grab all of the key frame data, rightclick, and I can just say, hey, swap buffer curves. And this will set everything in this animation back to the original way that I had it. So now, even though I baked everything down to fives and changed all kinds of stuff, I can pretty much go back to any control and it's going to have all the original animation data before I baked before anything went weird and I'm back to normal. Super easy. Hopefully that was helpful. A good general overview of some of the really common things you might want to find in the curve editor. In the next video, we're going to talk animation layers for a even more non-destructive approach to editing animation data. See you there.

**Frame:** tutorials\frames\ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks\frame_000.jpg


---

## Structured Notes

### Core Technique
Curve Editor workflow tools: (1) **Buffer Curves** — snapshot current animation state; swap/apply/replace to non-destructively compare and revert; buffer every control via Alt+click in Anim Outliner; (2) **Bake** — bake on ones (densify) OR bake every N frames (reduce density); (3) **Tween tool** smooth/rough modes for rapid curve contrast adjustment; (4) Euler filter and other filters accessed via right-click or filter button. Key insight: buffer first, then bake/reduce, compare with ghost, hand-correct discrepancies.

### Summary
14m25s official UE5 Curve Editor secrets tutorial (instructor: Sir Wade, ACOM project, Shot 40 — Beta running in corridor). Shows how to buffer all controls at once via Alt+click on Control Rig in Anim Outliner (selects full hierarchy). Buffer Curves: right-click → Buffer Curves → creates ghost; right-click → Swap Buffer Curves (toggle between current and buffered); right-click → Apply (revert to buffered); right-click → New Buffer Curve (update snapshot). Buffer does NOT persist across sessions. Anim Outliner flatten modules: removes hierarchy cascading so Alt+click on a section (e.g., left arm) selects only that section without children. Camera cuts track in a sub-sequence inherits camera from parent level sequence. Bake: can bake on ones (densify) OR bake every N frames (reduce/unbake); useful for reducing mocap data density. Tween tool: smooth/rough modes for mass curve smoothing or adding contrast; useful for noisy mocap. Filters: Euler filter (fix gimbal lock); Butterworth (smooth); Smart Reduce; Simplify. All filter access routes: right-click curve, filter button, or specific right-click sub-menu.

### Key Steps
**Buffer Curves (snapshot before editing):**
1. Open Anim Outliner (top-right in Sequencer animation mode) → find character's Control Rig entry
2. **Alt+click** on the Control Rig entry → selects ALL controls (hidden or visible) in the hierarchy
3. In Curve Editor: right-click → **Buffer Curves** → creates ghost overlay for all curves simultaneously
4. Now make edits; ghost shows where animation was at snapshot time
5. Right-click → **Swap Buffer Curves** — toggles between current and buffered state (back and forth)
6. Right-click → **Apply** — reverts current curve to the buffered snapshot
7. Right-click → **New Buffer Curve** — updates the snapshot to the current state
8. Note: buffer does NOT persist when UE is closed/reopened; buffer every session start

**Anim Outliner hierarchy selection tricks:**
9. Alt+click on any entry = selects that entry + all children recursively
10. Top-left dropdown → **Flatten Modules** → removes hierarchy; Alt+click now selects only items in that exact section (not children) — useful for section-specific selection sets
11. Unflatten modules when done to restore hierarchy behavior

**Camera cuts in sub-sequences:**
12. Inside a sub-sequence: add a Camera Cuts track → references the parent level sequence's camera automatically; no camera actor required in the sub-sequence

**Viewport control rig visibility:**
13. Press **G** in viewport → toggles Game Mode → shows/hides control rig handles (most common cause of "where did my rig go?")

**Bake (densify or reduce density):**
14. Select controls → Curve Editor right-click → **Bake** → interval options:
    - "On Ones" → adds a key on every single frame (densify; e.g., for baked export)
    - Every N frames → bakes at lower density (e.g., every 5 frames = reduce/unbake for sparse editing)
15. Buffer curves first! Baking at low density loses high-frequency detail

**Euler filter:**
16. Right-click curve → **Euler Filter** (or Filter button → Euler Filter) → fixes gimbal lock and over-rotation artifacts on rotation channels; no settings; just Apply

**Smoothing filters:**
17. Right-click → Filter → **Butterworth** — lowpass Fourier smoothing; adjust tolerance; good for general jitter
18. **Smart Reduce** — reduces keyframe count while preserving curve shape within tolerance
19. **Simplify** — removes redundant (flat/collinear) keys
20. **Smart Snap** — rounds sub-frame keys to whole frames (see companion tutorial for full workflow)

**Tween tool (smooth/rough):**
21. Tween button in Curve Editor toolbar (or animation viewport toolbar)
22. Select all curve keys → set mode to **Smooth** → click repeatedly to smooth out jitter and reduce key-to-key contrast (good for noisy mocap)
23. Set mode to **Rough** → click to increase contrast/emphasis between keys
24. Combine with buffer curves: smooth, compare with ghost, hand-correct important extremes

**Revert everything to pre-edit state:**
25. Alt+click Control Rig → right-click → **Swap Buffer Curves** → all controls revert to snapshot; all baking/editing undone in one step

### UE Systems / Blueprints / Settings
- **Buffer Curves** — per-session snapshot; one snapshot slot per curve; ghost visible as gray overlay in Curve Editor; swap/apply/new actions; does NOT persist sessions
- **Alt+click in Anim Outliner** — recursive selection of all controls in hierarchy; essential for bulk operations; Flatten Modules changes behavior to non-recursive per section
- **Bake** (Curve Editor right-click) — densify to ones or reduce to every N frames; unbake workflow: bake every 5+ frames to get sparse editing-friendly keyframes
- **Euler Filter** — standard 3D animation tool; fixes over-rotation/gimbal lock on Euler rotation channels; no settings; right-click or filter button
- **Butterworth filter** — Fourier lowpass; reduces high-frequency noise; tolerance slider
- **Smart Reduce / Simplify** — reduce key count; Simplify removes flat keys; Smart Reduce uses shape-preserving decimation
- **Tween tool** — smooth/rough modes; works on entire selected curves in mass; designed for mocap cleanup
- **Camera Cuts track in sub-sequence** — inherits camera from any parent level sequence; allows camera navigation within a sub-sequence without embedding a camera
- **G key** — viewport game mode toggle; fastest way to show/hide control rig handles

### Difficulty
Beginner-Intermediate. Tools are simple; key insight is combining buffer → edit → compare → hand-correct workflow.

### UE Version
UE5 (ACOM series; content compatible with UE5.0+; Smart Snap in UE5.6)

### Tags
animation, curve-editor, sequencer, buffer-curves, tween, bake, workflow, technique, keyframes, tools

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [1:26] tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/frame_000.jpg
- [4:20] tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/frame_001.jpg
- [7:56] tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/frame_002.jpg
- [11:32] tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/frame_003.jpg

## Related Entries
- `ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — companion tutorial; Lattice tool, view modes, time-scaling, Smart Snap workflow
- `ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — mentioned as next in series; animation layers for non-destructive approach
- `stylized-animation-control-rig-characters-in-unreal-engine-5.md` — ACOM Control Rig intro; Alt+click Anim Outliner tip also covered
