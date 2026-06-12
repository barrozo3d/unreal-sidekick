---
title: How I Made This Shot in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=HbGJyQVq3tk
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.0"
tags: [rendering, path-tracing, photogrammetry, 3d-scanning, compositing, davinci-resolve, mrq, workflow, william-faucher, intermediate, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-shot-in-unreal-engine-5/
frame_count: 0
---

# How I Made This Shot in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=HbGJyQVq3tk)
**Author:** William Faucher
**Duration:** 14m31s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In a video I made a few months ago, I 3D scanned my old, reliable acts and I made these  3 shots in Unreal Engine 5.  Now a lot of you asked me to make a video about how these shots were made.  So here it is.  I'll show you my workflow and process from start to finish, from the 3D scanning part  to mesh clean up and texturing, to flushing out the environment in Unreal Engine 5, lighting,  rendering, and color grading as always.  Now full disclosure, this video is sponsored by Catchering Reality and I use Reality  Capture to scan this acts.


### 3D Scanning [0:32]
**Transcript:** I have many tutorials on 3D scanning, but this time around the process was a little bit  different.  Reason being, the acts itself has many different material types.  A well aged wooden shaft, high carbon steel, a leather sheet with brass rivets, so I wanted  to make a high quality asset that rendered cleanly in Unreal Engine because I knew this  would be a close up shot.  And when you're doing a hero shot like this, the 3D models need to hold up to a whole  lot more scrutiny.  So step one, scanning the acts itself with the help of photogrammetry.  To make my life a whole lot easier, to not have to move the camera around so much, I mounted  the acts on the ceiling with a rotatable arm.  That way the camera can stay fixed on a tripod and all I need to do is spin the acts at  5 degree increments and taking photos from every angle.  The chunker camera rig you see here is a cross polarized setup.  The purpose of this flash and filter is to cut out all reflections on an object, giving  you a very matte look, which is ideal for photogrammetry because you need consistency between photos.  And when you have reflections, note reflections shift and change based on view angles, right?  Which ...


### Texturing [3:56]
**Transcript:** That provide a good foundation to work from, but it's really only the base color that  we get, the albedo map.  I needed to bring this texture into the substance painter because we need to ensure proper, fitically  based material definition between the various types of surfaces.  Wood, steel, leather and brass.  Like I said, the base color and normal map texture we get out of reality capture is fantastic.  Working in painter however just allows us to push this even further.  With our model exported, our textured, exported out of something painter, now the time to jump


### Into Unreal Engine 5 [4:31]
**Transcript:** into Unreal Engine 5.  With Unreal Open, the first thing I love to do is to set up a basic daylight system using  the environment light mixer.  And in just a few clicks, we've got a fully dynamic sky and clouds, totally free, which  helps us see what we're doing.  I like doing it because I don't like working in a black void.  So having a decent lighting setup to work with is a good starting point.  Now after that, the first step in creating any shot is establishing the composition, the  framing, setting up the camera early on.  Really this should be roughly one of the first things you do.  Place your subject in the frame, place a camera, and get that composition nailed down before  you start spending any time flushing out your scene.  You want to start working on only the things the camera will see.  There's no point in spending hours making a beautiful level, only to realize that most  of your hard work isn't even going to be in the frame.  You get the point.  Then I just move my directional light in the rough direction I want it to come from to  establish the initial lighting path.  But because my end goal here is to render a top quality, no exceptions kind of image,  I went with...


### Times of Day [11:06]
**Transcript:** But that done.  Before rendering, I decided to have a little bit of fun.  Just the tries in different times of day, I went for an overcast feel and a night time shot.  Really, this is purely creative work.  Having fun with the various lighting tools in Unreal, I recommend watching my dedicated  lighting tutorial right here to learn the basics, as there are a hundred ways to light  a shot and all of them are valid.  You just need to know what you're going for and the tools available to you.  For the overcast day, I simply use a skylight with an htri found on htrihaven.  And for the night time shot, it's really just the blueish direction of light and I added  a point light to simulate campfire.  With our shots done now, we move on to the rendering and collocrating phase.


### Rendering [11:48]
**Transcript:** So I'm going to be rendering these out at max quality using the movie render queue.  Here we can determine the resolution we want, the console variables we want, and the anti-aliasing  or sampling settings.  Then the post-process volume under the path tracing tab, I'm going to disable the denoiser  because I will denoise myself in the vintage resolve, but we're going to get into that  real soon.  In the movie render queue, be sure to delete the deferred rendering tab and add the path  tracing tab instead because we want the path tracer.  Always render in 16 bit exr to get the highest bit depth, which gives us flexibility and  post.  In color output, be sure to disable the tone curve.  And under anti-aliasing, override anti-aliasing should be checked, set AA metad to none, and  with the path tracer, 16 by 16 is a good starting point.  Troubleshooting path tracer renders is really easy.  It's your shot to noisy, you need more samples.  That's all there is to it.  In the output tab is where I determine my desired resolution, and in this case, I want  4K.  When you're ready, hit that render local button, and wait.  The path tracer is way slower than a deferred renderer, so go make a sa...


### Davinci Resolve Denoising [13:04]
**Transcript:** 6 hours later.  Now, I've talked about this in many videos.  I even have a whole video dedicated to color grading and vintage resolve, but really,  this part of the process is where you really make your render shine.  Color grading is entirely subjective.  What one person might like, another person won't.  There isn't a good or bad way to grade.  It's all about the taste and getting to look you want.  I don't want to spend too much time on nitty-gritty here, because again, I've made two whole videos  on color grading and resolve already.  The one thing I do want to show you, however, is denoising and resolve.  Because the path tracer by nature is going to be substantially grainyer than when you use  the deferred rendering.  In the free version of resolve, select your imported clip and go to the Fusion page, press  SHIFT, space, and add the noise reduction tool.  From there, your denoise setting will be on the right.  If you own the $300 studio version of resolve, you can add the noise reduction in the color  page, which is, by far, my preferred way of working.  I generally don't really enjoy using Fusion.  So here's a quick before and after of each of the three final renders I did....



---

## Structured Notes

### Core Technique
Full production workflow breakdown for a cinematic still: photogrammetry (RealityCapture) → Substance Painter texturing → UE5 scene composition with Path Tracer → MRQ rendering (16×16 samples, no denoiser, tone curve off) → DaVinci Resolve denoising + color grading. Demonstrates composition-first methodology.

### Summary
14-minute behind-the-scenes walkthrough of creating 3 cinematic stills of a scanned axe. Starts with photogrammetry using cross-polarized flash (eliminates reflections, ideal for PBR scanning), Substance Painter to add material definition beyond base color, then UE5 scene building (composition first → light direction → Path Tracer). Key production insight: set up camera and framing immediately — build only what the camera sees. Denoise in Resolve's Fusion page (free) or Color page (Studio).

### Key Steps

**Photogrammetry Workflow:**
1. Mount object on ceiling arm (object rotates, camera stays fixed on tripod)
2. Cross-polarized flash: flash + polarizing filter + matching lens filter = cuts reflections → matte consistent photos
3. Rotate subject at 5° increments, photograph from each angle
4. Import into RealityCapture → align → mesh → texture
5. Result: base color + normal map from Reality Capture (good starting point)

**Texturing in Substance Painter:**
1. Export mesh from Reality Capture
2. Import into Substance Painter
3. Define PBR material channels: roughness, metallic, specular for each material zone
4. Export textures (base color, normal, roughness, metallic, AO)
5. Import into UE5 as material

**UE5 Scene Setup — Composition First:**
1. **Open UE5** → environment light mixer for quick daylight (Directional + Sky Atmosphere + Sky Light + Volumetric Fog)
2. **Set up camera FIRST** — place subject, position camera, nail composition
3. **Don't build anything outside camera frustum** — waste of time
4. Move Directional Light to rough desired direction
5. Iterate lighting with Path Tracer previews (PPV → Path Tracing tab → Preview mode)

**Path Tracer Render Settings:**
1. MRQ → delete Deferred Rendering tab → add **Path Tracing** tab
2. MRQ → Color Output → **Disable Tone Curve**
3. MRQ → Anti-Aliasing → Override AA → None, **16 Spatial × 16 Temporal** samples
4. PPV → Path Tracing → **Disable Denoiser** (denoise in Resolve instead)
5. Output → EXR 16-bit, 4K resolution
6. Hit Render Local → expect LONG render times (Path Tracer is slow)

**Denoising in DaVinci Resolve:**
- **Free version:** Import clip → Fusion page → Shift+Space → add **Noise Reduction** node
- **Studio version ($300):** Color page → add Noise Reduction in node graph (preferred)
- Color grade as normal after denoising

**Lighting Variations (for multiple shots):**
- Daylight: Directional Light + Sky Atmosphere
- Overcast: Skylight only with HDRI from HDRI Haven
- Night: Directional Light (blue, low intensity) + Point Light (warm, simulates campfire)

### UE Systems / Blueprints / Settings

**Path Tracer MRQ Config:**
```
MRQ Settings:
  Rendering tab: [delete Deferred Rendering] → Add Path Tracing
  
  Path Tracing settings:
    Samples Per Pixel: controlled by Anti-Aliasing tab (not here)
  
  Anti-Aliasing:
    Override AA: True
    Method: None
    Spatial Samples: 16
    Temporal Samples: 16
    // Noisy? Add more samples — that's the ONLY fix
  
  Color Output:
    Disable Tone Curve: True
  
  Output:
    EXR Sequence 16-bit
    Resolution: 4K (3840×2160)

Post Process Volume:
  Path Tracing → Denoiser: Disabled  // denoise in Resolve instead
```

**Quick Daylight Setup:**
```
Window → Environment Light Mixer:
  Create All (Directional Light + SkyAtmosphere + Sky Light + Volumetric Fog)
  // One-click daylight foundation
```

### Difficulty
Advanced — full production pipeline across multiple apps

### UE Version
UE 5.0

### Tags
rendering, path-tracing, photogrammetry, 3d-scanning, compositing, davinci-resolve, mrq, workflow, william-faucher, intermediate, ue5

---

## Related Entries
- `tutorials/path-tracer-explained---unreal-engines-underrated-tool.md` — Path Tracer deep-dive
- `tutorials/the-2026-unreal-engine-to-davinci-resolve-guide---aces-srgb.md` — DaVinci Resolve workflow
- `tutorials/the-2025-guide-to-rendering-in-unreal-engine-5.md` — MRQ render settings reference
