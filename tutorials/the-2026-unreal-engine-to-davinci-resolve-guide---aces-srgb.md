---
title: The 2026 Unreal Engine to Davinci Resolve Guide - ACES & sRGB
source: YouTube
url: https://www.youtube.com/watch?v=2Q3CybANHKE
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.x"
tags: [rendering, color-grading, davinci-resolve, aces, ocio, tone-curve, linear-srgb, color-science, mrq, exr, pipeline, william-faucher, intermediate, ue5]
extraction_status: complete
frames_dir: tutorials/frames/the-2026-unreal-engine-to-davinci-resolve-guide---aces-srgb/
frame_count: 0
---

# The 2026 Unreal Engine to Davinci Resolve Guide - ACES & sRGB

**Source:** [YouTube](https://www.youtube.com/watch?v=2Q3CybANHKE)
**Author:** William Faucher
**Duration:** 23m23s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro, FAB Sale, Dehancer [0:00]
**Transcript:** Have you ever rendered a shot in Unreal only to find it looks nothing like your viewport?  Things are dark, the colors are all weird, between aces and OTAO configs, it is confusing  and frustrating and that is what we're looking at today.  I made a tutorial for DaVinci Resolve a few years ago, but I'm an eternal student,  I'm always learning, and this revised workflow is so much easier.  Not only will your renders master viewport will improve upon them from there.  What will you, you might ask?  Why bother with yet another app?  Why not just color grade and Unreal?  What's the point?  Great question.  Resolve is specifically designed for color grading and its tools are far more robust  than what Unreal offers.  It is built for giving you complete control over your final image in a non-destructive way.  Color science is complicated, I don't claim to be an expert, so please take all of this  with the grain of salt with respect to your own production needs.  Full disclosure, this video is not sponsored, I do have affiliate links for a dehansure  which they plug in for DaVinci Resolve that we'll be looking at later.  That said, I've just released a free update for EasyFog with performa...


### Render Settings in Unreal [1:19]
**Transcript:** If you don't know how to render in Unreal, this video I made recently has you covered,  with everything you need to know about the latest information.  But for now, here are the important render settings.  The file format I'm rendering in is EXR, which is industry standard and offers the best  rendering quality and bit depth.  We won't be rendering in JPEG or PNG because they really fall apart quickly when you're  editing, color grading or compositing.  Next is color output, and this is probably the most important part of this video.  Color output revolves around the shredded tone curve.  You might have heard about it before, and it's not a bad thing.  Just don't get tone-curved mixed up with tone-mapper.  These are two different things.  If you watched my previous Aces Color Grading workflow, you might remember setting up an  OCEI-O config, finding and downloading a config file online, just to handle the color space  conversion.  But this time, it's unnecessary.  Why?  Because we can do the color space conversion directly into Vinci Resolve, no need for any extra  conversion at render time because we're rendering in linear SRGB, keeping things simple.  To prove it, here are two id...


### Setting up an OCIO Config and Display View [2:39]
**Transcript:** But if you need your EXR file to be rendered directly in Acescg, or you want your viewport  to have a viewport transform, which may be handy in a bit, here is how.  One, ensure you have the OpenColorIO plugin enabled.  Two, right-click in your content browser and create an OpenColorIO configuration file.  Three, open this config file, and type OCEI-O colon slash slash default at the configuration  file path.  The OCEI-O config is now built directly into the engine with no need to download anything.  This is so nice.  Thank you, Epic.  Next, you need linear SRGB and Acescg as the desired color spaces, and SRGB Aces 1.0 SDR  video as the display view.  I'm going to refer to the display view and how it can help you later in this video.  Remember this.  Next, in the color output node of MovieRenderQ, tick is enabled in the OCEI-O configuration,  load the configuration file we just created, in the transform source, put in linear SRGB,  and Acescg as the destination.  Again, I don't even recommend you do this unless you have a reason for needing your  EXR to be an Aces from the get-go.  I just want to show you how it is easy to do.


### Tone Curve: Enabled or Disabled? [3:56]
**Transcript:** Okay, so moving on.  The setting to use in the color output node, you need to ask yourself if you want to render  with the tone curve on or off.  What does this mean for you, the artist?  With the tone curve on, which is default, you get a 1-to-1 match with the viewport.  Here's an example.  On the right, a render, properly transformed the venture resolve, and on the left, the  Unreal viewport.  They are identical.  The downside is this render is not linear, nor Aces, limiting your flexibility and post.  The baked-in tone curve makes color grading harder, even in 16-bit EXR, avoid this for  compositing or doing serious color work in post.  With the tone curve disabled, it outputs linear SRGB, which I recommend.  With minimal tweaking in resolve, you'll get within 99% viewport accuracy, with the added  benefit of full flexibility for compositing matching shots with other renderers, or converting  to a log profile if you want.  That is how I matched an Aces render earlier, because it is a linear image.  That would not work if I left the tone curve on.  So there's no right or wrong choice here.  It just depends on what you need.  Personally, I recommend disabling the tone curve, but I...


### Post Process Volume Blue Correction & Expand Gamut [5:18]
**Transcript:** A few additional things you can set up in your level post process volume are the following.  One, make sure your post process volume is set to unbound, but you can set the blue  correction and expand gamut to zero.  Blue correction can fix some weirdness that occurs in bright blues, and expand gamut  does some fakery to give the impression of wider gamut, but I really struggle to see  any difference, and if anything, it is making your colors wrong.  These are not mandatory, so don't fret if you forgot to change it.  You probably won't even notice.  It's just good to know about.  Okay, that was a lot of info.


### Davinci Resolve [5:53]
**Transcript:** But now we can render out our frames and move on to DaVinci Resolve, which is free to use.  It also has a paid studio version that has a few extra bells and whistles.  That is not absolutely essential.  You can do most of what I'm going to show you here with the free version.  I want to preface that color grading is a very personal thing.  What one person likes, another person might hate.  There are entire channels on YouTube dedicated to just color grading, so the point I want  to drill into you here is that there's no right or wrong way to color grade or shot.  It's all about what you or your client likes in the end.  I just want to show you the tools that you're disposal to get you started, both free tools  and paid ones.  So with DaVinci Resolve open, the first thing we want to do is establish our timeline settings.  By going to File and then Project Management, we want to assign our resolution and desired  frame rate.  My resolution here is 2560 by 1440.  And this video is in 30 FPS, but there's no correct setting here.  Just choose what you want for your project.  You're going to find a bunch of buttons at the bottom here.  You got Media, Cut, Edit, Fusion, Color, Fairlight, ...


### Importing your Renders into Resolve [7:00]
**Transcript:** To import our renders from Unreal, make sure you're on the Edit page.  And here on the left in your Media Pool, right click, Import Media, and select all the renders  and import.  Resolve is smart enough to figure out that your image sequences are going to be one clip.  Once imported, drag and drop the clip onto your timeline like this.


### Converting your EXR Renders Correctly (ACES Transform) [7:23]
**Transcript:** Now if you rendered in EXR before, you know the colors are all kinds of weird.  Everything looks wrong and dark.  We just need to tell DaVinci Resolve how to interpret this render.  This doesn't happen with JPEG or PNG because they are already in 8-bit SRGB, with the  tone curve baked in.  For demonstration purposes, I rendered out the exact same shot in JPEG with the tone  curve left on as is the default, which I will be using as our ground-strewed reference  here.  If we take a side by side comparison here, you'll see we have a match.  So with our shots imported, let's move on to the color page, which is where we will convert  and display our renders correctly and begin color grading them.  So once we are in the color page here, you'll notice I have four rendered right here.  If you don't see that when you import your clips, you can click on the little clip button  up here.  I have one with the tone curve enabled, left by default, one with the tone curve disabled  in linear SRGB, the third one in ACES CG, and the JPEG is my ground-strewed reference.  We know the JPEG matches my viewport in Unreal.  So the way to convert our files correctly is we need to add the ACES transform nod...


### Using a Display View to convert viewport profile [10:24]
**Transcript:** Remain for this.  Let's use it.  In Unreal, click on the lit button here, then OCIO display, then tick enable display,  and load the config file we made.  There's now two drop-down menus.  In the top one, use linear SRGB, and in the bottom one, use the ACES 1.0 SDR video display  view.  In your viewport, we'll now match your linear renders perfectly.  Remember how I said that Unreal's tone curve is not exactly ACES?  This way, our viewport is now displayed in a known profile that matches what you're  converting to in Divinci Resolve.  So one could argue that a good workflow is to set up the viewport transform at the  beginning of your project, author your artistic content with the look done in the viewport,  and render from there with the tone curve disabled like I showed you.  That way, you will never have any surprises.  But remember, it's okay if you don't have a perfect match, too.  The whole reason we're grading in Rousalb is specifically because I don't want it to  match my viewport.  I want to change it and make it better, so don't overthink it.  But also, if I wanted to take this and convert it to a log profile, let's say you've got  some luts that you want to use, instead ...


### Colorgrading your renders (Free tools) [12:01]
**Transcript:** Now that we've gotten our renders correctly converted, we can get started with actually  color grading your shots.  And the beauty of working in Resolve is this non-destructive node-based editing.  So clicking on the Aces transform node here, I'm going to press the Alt S key and that  creates a new node.  So with this new node here, you'll see at the bottom here we got Lift, Gamma, Gain, and  Offset.  As I adjust these, I want you to pay attention to the waveform on the right hand side here.  The waveform tells us where the highlights and the shadows of our shot are.  So as I adjust the lift here, lift means shadows.  And notice how when I adjust the lift, it mostly affects the lower part of the waveform.  It adjusts my shadows.  Gamma is the midtones.  Again, the waveform, mostly the middle range moves here.  It doesn't really affect the shadows or the highlights as much.  Gain is the highlights.  So again, if I move this, notice how the only the upper part of the waveform is being  affected.  And Offset moves everything evenly.  So if I adjust this like that, you'll see the whole waveform does not kind of stretch.  It all moves up or down evenly.  On the right hand side here, you...


### Resolve Studio Feature [18:49]
**Transcript:** Now I'm going to show you one little thing that comes with the studio version of  Resolve.  Again, our library here, I'm going to search for the film look creator and add it to my  graph here.  The film look creator essentially consolidates everything we just did here in one node.  See, we got the exposure, we got the contract, highlight the adjustment.  We've got the vignetting that we added earlier.  We've got bloom adjustments here.  So the way I showed you before does give you way more control, but it is nice to have  everything kind of built into one handy node.  Film grain is one of those things where you either love it or you hate it.  Personally, I'm a sucker for it, so I'm going to use it in these shots.  So again, this is before and this is after I want to showcase one last tool I have under


### Using Dehancer [19:33]
**Transcript:** my belt.  And that is the handser.  I've used the handser on many renders in a path.  And this is how I add some magic sauce to my renders.  It is a paid plugin for Resolve.  This video is not sponsored, but I do have an affiliate link down below where you can  get 10% off all the handser products using the promo code William 10.  The film look creator I showed you just came out with Devinship Resolve 19.  It is largely based off of the handser.  You'll find many of the exact same settings here where the handser really shines, however,  is with its film profiles.  These are based on real film stocks.  And I love this because as someone who dabbles in film photography, I can get my renders  to look like they were shot on these roles of film.  I even have a role of Kodak Portia 800 here on my desk.  And here in Dehanser, I can find the portrait profile.  You have a ton of the juice from and they immediately give you a very good starting point.  It looks really good.  Analog film develops very differently depending on whether you over or under expose it.  So there's a slider here that shifts the colors around a bit the same way.  It is a lot of fun to use.  Dehanser also has some of t...


### Exporting your renders [22:20]
**Transcript:** Once we're done with our grade here, there's two ways to export your shot.  If you just want to export a still image, right click here, grab still and it will show  up in your gallery here.  You can then export it to JPEG or whatever you want by right clicking on it from there.  For video, we move on to the deliver page at the bottom here.  Add the settings you want such as file name and location on disk.  Personally, I like to render an MP4 in H264 or H265 and my general rule of thumb for the  quality of the bit rate is frame rate times 2.  So if I'm rendering a 24 FPS shot, I will set it to 48,000.  If it is 30 FPS, I will set it to 60,000.  When you're ready, click on add to render queue and render your video from there.  And that's it.  I know this was a bit of a wordy and super technical video, but I hope you found it helpful.  Again, all of my easy tools are on sale on fab for the next week, so get them while you  can.  Thank you so much for watching and as always folks, happy rendering.



---

## Structured Notes

### Core Technique
2026 revised Unreal-to-DaVinci Resolve color pipeline — simplified vs prior ACES guide: render linear sRGB (tone curve OFF), no need to download OCIO config (it's built into the engine), convert to ACES in Resolve using the ACES transform node. Covers both tone-curve-on and tone-curve-off approaches and when to use each.

### Summary
23-minute updated color grading guide, marked as a significant improvement over William's earlier ACES guide. Key insight: the OCIO config is now built into Unreal as `ocio://default` — no manual download needed. Render in linear sRGB (Tone Curve disabled), import into Resolve, add ACES transform node, then grade. Shows free tools (Lift/Gamma/Gain, Curves, Vignette) and paid (Dehancer film stock plugin). Export: H264/H265, bitrate = frame rate × 2000 kbps.

### Key Steps

**Render Settings in Unreal:**
1. File Format: **EXR** (not JPEG/PNG — fall apart under grading)
2. Color Output tab in MRQ:
   - **Disable Tone Curve** (recommended) → outputs linear sRGB, full grading flexibility
   - OR keep Tone Curve enabled → 1:1 viewport match but limited grading headroom

**Tone Curve Decision:**
| Setting | Viewport Match | Grading Flexibility | Compositing |
|---------|---------------|--------------------|----|
| Tone Curve ON | Perfect | Limited | ✗ Avoid |
| Tone Curve OFF | ~99% with fix | Full | ✓ Recommended |

**OCIO Viewport Setup (optional but useful):**
1. Enable OpenColorIO plugin in UE
2. Content Browser → right-click → Create OpenColorIO Configuration
3. Config file path field → type: `ocio://default` (built-in, no download needed!)
4. Add color spaces: Linear sRGB + ACEScg; Display View: SRGB ACES 1.0 SDR video
5. In viewport: Lit button → OCIO Display → enable display → load config
6. Viewport now displays in ACES transform = matches Resolve's converted output

**PPV Cleanup (optional):**
- Blue Correction → 0 (fixes blue weirdness in bright areas)
- Expand Gamut → 0 (fake wider gamut, no real benefit — may skew colors)

**In DaVinci Resolve:**
1. File → Project Settings → Resolution + Frame Rate
2. Import renders: Edit page → Media Pool → right-click → Import Media
3. Drag clip to timeline
4. Go to Color page
5. Right-click clip → Add ACES Input Transform → Linear sRGB (for Tone Curve OFF renders)
6. All clips now displaying correctly — begin color grading

**Color Grade Basics (Free Tools):**
- Lift = shadows, Gamma = midtones, Gain = highlights, Offset = all uniform
- Waveform scope: shows if you're clipping highlights or crushing blacks
- Add nodes with Alt+S (non-destructive)
- Vignette: Window shape → use Curves to darken outer areas
- Export: Deliver page → H264/H265 → Bitrate = fps × 2 × 1000 (24fps = 48,000 kbps)

**Dehancer Plugin (Paid, optional):**
- Film stock profiles based on real film emulsions
- Kodak Portra, Fuji Velvia, and many more
- Similar to Resolve 19 built-in Film Look Creator (which is inspired by Dehancer)
- Promo code: William10 for 10% off

### UE Systems / Blueprints / Settings

**MRQ Color Output — Recommended 2026 Settings:**
```
MRQ → Color Output:
  Disable Tone Curve: True   // linear sRGB output
  OCIO Configuration: optional; only needed if you want ACEScg EXR output

Post Process Volume:
  Blue Correction: 0
  Expand Gamut: 0
```

**OCIO Built-in Config:**
```
Content Browser → Create OpenColorIO Configuration:
  Configuration File Path: ocio://default   // BUILT IN — no download needed!
  Color Spaces: Linear sRGB, ACEScg
  Display View: SRGB ACES 1.0 SDR video
```

### Difficulty
Intermediate — requires understanding of color spaces; DaVinci Resolve basics helpful

### UE Version
UE 5.x (current; OCIO built-in config is a newer UE feature)

### Tags
rendering, color-grading, davinci-resolve, aces, ocio, tone-curve, linear-srgb, color-science, mrq, exr, pipeline, william-faucher, intermediate, ue5

---

## Related Entries
- `tutorials/unreal-to-davinci-resolve-workflow---aces-srgb.md` — Older workflow (manual ACES config download)
- `tutorials/the-2025-guide-to-rendering-in-unreal-engine-5.md` — 2025 rendering guide
- `tutorials/path-tracer-explained---unreal-engines-underrated-tool.md` — Path Tracer + Resolve denoising workflow
