---
title: How to Render Cryptomatte in Unreal (NEW in 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=Ry4-Q8mBjdg
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.26"
tags: [rendering, movie-render-queue, mrq, cryptomatte, object-id, matte, compositing, exr, nuke, william-faucher, beginner, ue4]
extraction_status: complete
frames_dir: tutorials/frames/how-to-render-cryptomatte-in-unreal-new-in-426/
frame_count: 0
---

# How to Render Cryptomatte in Unreal (NEW in 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=Ry4-Q8mBjdg)
**Author:** William Faucher
**Duration:** 5m20s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hi, welcome back to my channel. So one of Unreal's biggest drawbacks has been the lack of  Christmas support. This is something I've been complaining about for years, but as of yesterday,  version 4.26 was released and it is feature packed. However, one of those features that would  barely mention that all, aside from a two-second clip in their release video, was Crucimett Support.  Now, any of the effects artists worth their salt know that this is a huge deal. This makes Unreal  that much more appealing for both CG artists and comfort alike. Now, if you don't know what  Crucimett Support is, it's also known as Object ID, Matte ID, and basically allowed you to get a  perfect mask of any object in your scene without having to do that manually to save you a ton of time.  So, Crucimett is here. It's awesome, so let's dive right in.


### Plugin Setup [0:46]
**Transcript:** All right, so now that we're in Unreal, the first thing you want to make sure is that you've  actually downloaded and installed in version 4.26. That should go without saying, but you never know.  Just a make sure. The next thing we want to do is we want to go to the Settings tab right up here  at the top, click on Settings, and then Plug-ins. In the search bar, you want to type for Render Q.  And once that you've done that, you want to make sure that Movie Render Q additional render  passes is enabled. If it's not enabled, you're not going to get your Crucimett's. So, click  enable, and you're going to have to restart the engine, as always, and don't worry about that.  I'm at the little pop-up saying that it's a beta, and it's a normal. It's a new feature,  so I wouldn't worry too much about it. What's left done, and you restarted the engine,  I want to hand also added some plans in the scene, just to add a little bit of extra complexity,


### Sequencer & Movie Render Queue [1:35]
**Transcript:** and we'll see it together if Crucimett actually supports Opacity on this type of shapes.  We're going to have to go ahead and create a sequence. So, I'm going to go to Cinematics up here,  add level sequence, and you can call it whatever you want. I'm going to call it object ID.  Save. So, a new sequence tab should show up at the bottom here, and you just need to create a camera.  So, I'm going to go create a camera right here. All right. Now, you don't really have to change  anything here. What I like doing is setting the film back to Full Frame DSLR, because as a photographer,  I shoot Full Frame, and it just makes sense to me. The next thing we want to do is, you know,  we don't need to have 150 frames. We can probably have it down to like, you know, let's say 15, okay?  And now, that's time to render. What you need to do is you go to Window up here,  Cinematics, Movie Render queue. So, once you clicked on Movie Render queue, a new window will pop up,  and what you need to do next is click on Render and add Object ID, which is the new sequence that we  just created right now. So, you want to click on Unsafe Config right here, and once again,


### Adding the Object ID Render Pass, and Rendering [2:41]
**Transcript:** another window is going to pop up. So, you got Output Rendering and Settings here. We can go ahead and  click on the JPEG Sequence thing here, delete that. We don't want to be rendering in JPEG.  What you want to do is you want to click on Setting and Add Object ID's Limited. Now, what we have  object ID's limited, the most important thing here, you want to click on Setting Again and Add EXR  Sequence. Okay? If you don't have anything the Output tab, so let me delete that right here,  if you don't have the Output tab and you render, you're not going to get any freeing written.  So, it's imperative that you click on Setting and choose EXR Sequence. I tried it with PNG Sequence,  this didn't seem to work very well or at all. So, make sure that you are in EXR Sequence. So,  make sure you have Output, EXR Sequence, and in Rendering tab have Object ID's. Also, in the  EXR Sequence, make sure that Multi-Layer is checked because otherwise you're going to be rendering a bunch  of images, lots of frames, not so good. In the Output tab, you can go ahead and choose your Output  directory and Resolution, which can lead that 1920 to 1080 and hit Accept. And all you need to do  now is hit Render...


### Opening Cryptomatte in Photoshop [4:01]
**Transcript:** license or Fusion 16 or 17 I think it is now, I don't actually have another way of viewing  these good demands apart from using Photoshop. Now, in Photoshop, you're going to need a plugin  called EXRIO that is free, the link in the description below. And all you need to do now is you go  ahead and you import your files. So, I'm just going to go ahead and grab this one, you know,  Matadie 15, doesn't matter which one. So, I'm going to pop up with EXRIO, just hit Open.  So, once you import your file into Photoshop, EXRIO is going to split up every single render pass  into one layer. So, as you can see here, we got the alpha pass, then we've got the beauty,  and then we've got the crypto-mat here. This is what we're looking for. This is what we want.  So, as you can see, every single layer here corresponds to an individual object ID.  And that's really all there is to it folks. If you dig right into Nuke Infusion,  you'll have your entire sequence, and as you'll see, crypto-mat is working as it should.  So, once again, this is what the pretty straightforward process, the EXR file that you get from


### Outro [5:01]
**Transcript:** Unreal will have a perfectly functioning mat in any software you use, whether it's Nuke,  or Fusion, or Photoshop, whatever. It's a video that helped you out in any way, or if you have  any questions at all, please leave a comment down below. Don't forget to like and subscribe,  and once again, thank you for watching.



---

## Structured Notes

### Core Technique
Cryptomatte / Object ID pass setup in MRQ (new in UE4.26) — enables automatic per-object alpha masks embedded in multi-layer EXR, usable in Nuke/Fusion/Photoshop for isolating any object in post without manual roto.

### Summary
5-minute quick tutorial for Cryptomatte in UE4.26 — the first version to support it. Previously Unreal had no Cryptomatte support, which was a major production limitation. Setup: enable MRQ Additional Render Passes plugin → add Object IDs tab in MRQ settings → render as multi-layer EXR. View result in Photoshop with the free EXRIO plugin, or use natively in Nuke/Fusion. Important: Cryptomatte does NOT support depth of field in masks — see stencil layers for DOF-accurate masking.

### Key Steps

**Requirements:**
1. Settings → Plugins → enable **Movie Render Queue Additional Render Passes** (separate from base MRQ plugin)
2. Restart engine

**MRQ Cryptomatte Setup:**
1. Create a Level Sequence + camera (even minimal sequence works)
2. Window → Cinematics → Movie Render Queue
3. + Render → add sequence → click Unsaved Config
4. Settings → delete JPEG Sequence if present
5. Settings → **Add EXR Sequence** (PNG doesn't work reliably)
6. EXR Sequence settings → check **Multi-Layer** ✓
7. Settings → **Add Object IDs** (this is the Cryptomatte pass)
8. Set output directory + resolution → Accept → Render Local

**Output:**
- Multi-layer EXR file per frame
- Contains: Beauty pass + Alpha + Cryptomatte layers (one per object)
- Each Cryptomatte layer = unique identifier for one object

**View in Photoshop:**
1. Install free **EXRIO** Photoshop plugin
2. File → Open → select EXR file → EXRIO splits into layers
3. Crypto-mat layer shows each object's color-coded mask

**Works Natively In:**
- Nuke (native EXR import)
- Fusion 16/17 (native support)
- After Effects (with EXR plugin)

**Cryptomatte Limitation:**
- Does NOT support depth of field in masks (objects remain hard-edged even if DOF-blurred)
- For DOF-accurate compositing: use Stencil Render Layers instead

### UE Systems / Blueprints / Settings

**MRQ Cryptomatte Config:**
```
Plugins required:
  Movie Render Pipeline ✓
  Movie Render Pipeline Additional Render Passes ✓

MRQ Settings:
  Output → EXR Sequence:
    Multi-Layer: True ✓    // REQUIRED — without this, passes render as separate files

  Rendering → Object IDs:
    [add tab] → renders Cryptomatte pass
```

### Difficulty
Beginner — quick setup; just enabling the right plugin

### UE Version
UE 4.26 (Cryptomatte first introduced in this version)

### Tags
rendering, movie-render-queue, mrq, cryptomatte, object-id, matte, compositing, exr, nuke, william-faucher, beginner, ue4

---

## Related Entries
- `tutorials/why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — Better alternative for DOF-accurate masking
- `tutorials/improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn.md` — Cryptomatte limitations (DOF, slow subsampling)
- `tutorials/how-to-render-passes-with-the-movie-render-queue-unreal-engine-426.md` — Other render passes
