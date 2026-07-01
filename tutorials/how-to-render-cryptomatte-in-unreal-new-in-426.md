---
title: How to Render Cryptomatte in Unreal (NEW in 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=Ry4-Q8mBjdg
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4.26"
tags: [cryptomatte, object-id, mrq, render-passes, compositing, exr, nuke, photoshop, movie-render-queue]
extraction_status: complete
frames_dir: tutorials/frames/how-to-render-cryptomatte-in-unreal-new-in-426/
frame_count: 6
---

# How to Render Cryptomatte in Unreal (NEW in 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=Ry4-Q8mBjdg)
**Author:** William Faucher
**Duration:** 5m20s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hi, welcome back to my channel. So one of Unreal's biggest drawbacks has been the lack of  Christmas support. This is something I've been complaining about for years, but as of yesterday,  version 4.26 was released and it is feature packed. However, one of those features that would  barely mention that all, aside from a two-second clip in their release video, was Crucimett Support.  Now, any of the effects artists worth their salt know that this is a huge deal. This makes Unreal  that much more appealing for both CG artists and comfort alike. Now, if you don't know what  Crucimett Support is, it's also known as Object ID, Matte ID, and basically allowed you to get a  perfect mask of any object in your scene without having to do that manually to save you a ton of time.  So, Crucimett is here. It's awesome, so let's dive right in.

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_000.jpg

### Plugin Setup [0:46]
**Transcript:** All right, so now that we're in Unreal, the first thing you want to make sure is that you've  actually downloaded and installed in version 4.26. That should go without saying, but you never know.  Just a make sure. The next thing we want to do is we want to go to the Settings tab right up here  at the top, click on Settings, and then Plug-ins. In the search bar, you want to type for Render Q.  And once that you've done that, you want to make sure that Movie Render Q additional render  passes is enabled. If it's not enabled, you're not going to get your Crucimett's. So, click  enable, and you're going to have to restart the engine, as always, and don't worry about that.  I'm at the little pop-up saying that it's a beta, and it's a normal. It's a new feature,  so I wouldn't worry too much about it. What's left done, and you restarted the engine,  I want to hand also added some plans in the scene, just to add a little bit of extra complexity,

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_001.jpg

### Sequencer & Movie Render Queue [1:35]
**Transcript:** and we'll see it together if Crucimett actually supports Opacity on this type of shapes.  We're going to have to go ahead and create a sequence. So, I'm going to go to Cinematics up here,  add level sequence, and you can call it whatever you want. I'm going to call it object ID.  Save. So, a new sequence tab should show up at the bottom here, and you just need to create a camera.  So, I'm going to go create a camera right here. All right. Now, you don't really have to change  anything here. What I like doing is setting the film back to Full Frame DSLR, because as a photographer,  I shoot Full Frame, and it just makes sense to me. The next thing we want to do is, you know,  we don't need to have 150 frames. We can probably have it down to like, you know, let's say 15, okay?  And now, that's time to render. What you need to do is you go to Window up here,  Cinematics, Movie Render queue. So, once you clicked on Movie Render queue, a new window will pop up,  and what you need to do next is click on Render and add Object ID, which is the new sequence that we  just created right now. So, you want to click on Unsafe Config right here, and once again,

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_002.jpg

### Adding the Object ID Render Pass, and Rendering [2:41]
**Transcript:** another window is going to pop up. So, you got Output Rendering and Settings here. We can go ahead and  click on the JPEG Sequence thing here, delete that. We don't want to be rendering in JPEG.  What you want to do is you want to click on Setting and Add Object ID's Limited. Now, what we have  object ID's limited, the most important thing here, you want to click on Setting Again and Add EXR  Sequence. Okay? If you don't have anything the Output tab, so let me delete that right here,  if you don't have the Output tab and you render, you're not going to get any freeing written.  So, it's imperative that you click on Setting and choose EXR Sequence. I tried it with PNG Sequence,  this didn't seem to work very well or at all. So, make sure that you are in EXR Sequence. So,  make sure you have Output, EXR Sequence, and in Rendering tab have Object ID's. Also, in the  EXR Sequence, make sure that Multi-Layer is checked because otherwise you're going to be rendering a bunch  of images, lots of frames, not so good. In the Output tab, you can go ahead and choose your Output  directory and Resolution, which can lead that 1920 to 1080 and hit Accept. And all you need to do  now is hit Render Local. So, it's going to render all your frames. Once that's done, your frame  they're written and we can bring these into Photoshop. So, since I don't have a new commercial

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_003.jpg

### Opening Cryptomatte in Photoshop [4:01]
**Transcript:** license or fusion 16 or 17 I think it is now, I don't actually have another way of viewing  these good demands apart from using Photoshop. Now, in Photoshop, you're going to need a plugin  called EXRIO that is free, the link in the description below. And all you need to do now is you go  ahead and you import your files. So, I'm just going to go ahead and grab this one, you know,  Matadie 15, doesn't matter which one. So, I'm going to pop up with EXRIO, just hit Open.  So, once you import your file into Photoshop, EXRIO is going to split up every single render pass  into one layer. So, as you can see here, we got the alpha pass, then we've got the beauty,  and then we've got the crypto-mat here. This is what we're looking for. This is what we want.  So, as you can see, every single layer here corresponds to an individual object ID.  And that's really all there is to it folks. If you dig right into Nuke Infusion,  you'll have your entire sequence, and as you'll see, crypto-mat is working as it should.  So, once again, this is what the pretty straightforward process, the EXR file that you get from

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_004.jpg

### Outro [5:01]
**Transcript:** Unreal will have a perfectly functioning mat in any software you use, whether it's Nuke,  or Fusion, or Photoshop, whatever. It's a video that helped you out in any way, or if you have  any questions at all, please leave a comment down below. Don't forget to like and subscribe,  and once again, thank you for watching.

**Frame:** tutorials\frames\how-to-render-cryptomatte-in-unreal-new-in-426\frame_005.jpg


---

## Structured Notes

### Core Technique
Cryptomatte (Object ID / Matte ID) render pass in UE4.26 via Movie Render Queue. Requires "Movie Render Queue Additional Render Passes" plugin + EXR Sequence output with Multi-Layer enabled. Output is a multi-layer EXR with per-object ID layers usable in Nuke, Fusion, or Photoshop (with EXRIO plugin).

### Summary
5-minute tutorial by William Faucher on rendering Cryptomatte passes from Unreal 4.26 using the Movie Render Queue. Cryptomatte provides automatic per-object masks without manual rotoscoping. Requires enabling the Additional Render Passes plugin, adding Object IDs to MRQ settings, and outputting to EXR (with Multi-Layer enabled). PNG output does not work. Resulting EXR contains alpha, beauty, and per-object cryptomatte layers viewable in Nuke, Fusion, or Photoshop via the free EXRIO plugin.

### Key Steps
1. **Enable plugin** — Settings → Plugins → search "Render Q" → enable "Movie Render Queue Additional Render Passes" → restart (ignore beta warning)
2. **Create sequence** — Cinematics → Add Level Sequence; add camera; keep frame count short (15 frames sufficient for test)
3. **Open MRQ** — Window → Cinematics → Movie Render Queue → Render → add sequence via big Render button → click "Unsafe Config" to open settings
4. **Configure MRQ output**:
   - Delete JPEG Sequence (default)
   - Settings → Add Output → **EXR Sequence** (PNG does NOT work for cryptomatte)
   - In EXR Sequence settings: enable **Multi-Layer** checkbox (critical — without this you get many files instead of one multi-layer EXR)
5. **Add Object ID pass** — Settings → Add Rendering → **Object IDs Limited** (adds cryptomatte data to EXR)
6. **Set output** — Output tab: set output directory + resolution → Accept
7. **Render** — Render Local
8. **View in Photoshop** — install free EXRIO plugin (link in description) → File → Open → import EXR → EXRIO splits all layers: alpha, beauty, crypto_mat_XX layers per object; each layer = individual object ID

### UE Systems / Blueprints / Settings
- **"Movie Render Queue Additional Render Passes" plugin** — enables Object IDs and other additional render passes in MRQ; must be enabled before cryptomatte is available
- **Object IDs Limited** — MRQ rendering setting; adds cryptomatte data; must be combined with EXR Sequence output
- **EXR Sequence** — MRQ output format required for cryptomatte (PNG fails); use Multi-Layer option
- **Multi-Layer EXR** — packs all render passes (beauty, alpha, crypto layers) into a single EXR file per frame; enable in EXR Sequence settings
- **EXRIO plugin (Photoshop)** — free third-party Photoshop plugin; opens multi-layer EXR and splits channels into Photoshop layers; enables cryptomatte inspection without Nuke/Fusion
- **Nuke / Fusion** — production-standard compositing tools; cryptomatte layer from UE EXR integrates natively; provides automatic object selection via cryptomatte node
- **Camera film back** — set to "Full Frame DSLR" in the tutorial (personal preference); does not affect cryptomatte output

### Difficulty
Beginner. Straightforward once you know the plugin and EXR requirement. The main trap is outputting to PNG (broken) or forgetting Multi-Layer in EXR settings.

### UE Version
UE4.26 (first version with Cryptomatte support; concepts apply to UE5 MRQ as well)

### Tags
cryptomatte, object-id, mrq, render-passes, compositing, exr, nuke, photoshop, movie-render-queue

---

## Related Entries
- `how-to-render-passes-with-the-movie-render-queue-unreal-engine-426.md` — companion tutorial: how to add Z-depth, world normal, and other render passes in MRQ
- `improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn.md` — additional MRQ tips
- `the-2025-guide-to-rendering-in-unreal-engine-5.md` — comprehensive UE5 rendering guide
- `why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — alternative object isolation method
