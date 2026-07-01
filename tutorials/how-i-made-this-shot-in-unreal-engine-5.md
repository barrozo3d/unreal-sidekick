---
title: How I Made This Shot in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=HbGJyQVq3tk
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [path-tracer, photogrammetry, rendering, lighting, environment, materials, movie-render-queue, davinci-resolve, post-production]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-shot-in-unreal-engine-5/
frame_count: 7
---

# How I Made This Shot in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=HbGJyQVq3tk)
**Author:** William Faucher
**Duration:** 14m31s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In a video I made a few months ago, I 3D scanned my old, reliable acts and I made these  3 shots in Unreal Engine 5.  Now a lot of you asked me to make a video about how these shots were made.  So here it is.  I'll show you my workflow and process from start to finish, from the 3D scanning part  to mesh clean up and texturing, to flushing out the environment in Unreal Engine 5, lighting,  rendering, and color grading as always.  Now full disclosure, this video is sponsored by Catchering Reality and I use Reality  Capture to scan this acts.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_000.jpg

### 3D Scanning [0:32]
**Transcript:** I have many tutorials on 3D scanning, but this time around the process was a little bit  different.  Reason being, the acts itself has many different material types.  A well aged wooden shaft, high carbon steel, a leather sheet with brass rivets, so I wanted  to make a high quality asset that rendered cleanly in Unreal Engine because I knew this  would be a close up shot.  And when you're doing a hero shot like this, the 3D models need to hold up to a whole  lot more scrutiny.  So step one, scanning the acts itself with the help of photogrammetry.  To make my life a whole lot easier, to not have to move the camera around so much, I mounted  the acts on the ceiling with a rotatable arm.  That way the camera can stay fixed on a tripod and all I need to do is spin the acts at  5 degree increments and taking photos from every angle.  The chunker camera rig you see here is a cross polarized setup.  The purpose of this flash and filter is to cut out all reflections on an object, giving  you a very matte look, which is ideal for photogrammetry because you need consistency between photos.  And when you have reflections, note reflections shift and change based on view angles, right?  Which is no bueno.  Once a loop was done, I lowered the camera and shot another loop until all angles of  the act were shot.  With the photos taken, I hopped into reality capture, aligned the cameras, as you'll  see here, we get a point cloud preview of what the act would look like.  And generated a 3D model based on those photos.  Now I did run into one issue and that's the shininess of the edge of the blade itself.  Looking closely here, even with a cross polarized setup, it's really hard to remove  reflections on some near chrome like metal.  And on top of that, there is just not much in the way of feature point.  It's too smooth, too polished, too mirror like.  You'll see that the result is not great.  That polished metal means the scan in this area will not turn out well unless I use this  stuff.  A subscanning spray, which is kind of magical.  What it does is it covers a surface with texture allowing you to scan your object and get  better, cleaner result.  So the best part is it just fades away over time on its own.  There's no need to clean it off.  It kind of blows my mind.  So that allowed me to get a much cleaner scan to work with.  Now it's still not perfect.  I brought it into the brush for polishing and retapology.  For don't wanna wear a retapology is the process of cleaning up your mesh, going from this  kind of wireframe to this to get a cleaner topology.  Again, you can see that entire workflow in this video right here linked below so I don't  bore you with the details.  Now I actually repeated this whole process twice, one version with the leather sheets and  one without.  Then using a Boolean operation in the brush, I was able to get a proper separate piece  of geometry for the sheet itself, giving me clean overhang and a slightly more realistic  look.  It's really nice to have granular control over separate pieces of the geo like that.  Now bringing the polished model back into reality capture, then I generated the textures  from the photo taken, which we get for free as part of the photogrammetry process.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_001.jpg

### Texturing [3:56]
**Transcript:** That provide a good foundation to work from, but it's really only the base color that  we get, the albedo map.  I needed to bring this texture into the substance painter because we need to ensure proper, fitically  based material definition between the various types of surfaces.  Wood, steel, leather and brass.  Like I said, the base color and normal map texture we get out of reality capture is fantastic.  Working in painter however just allows us to push this even further.  With our model exported, our textured, exported out of something painter, now the time to jump

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_002.jpg

### Into Unreal Engine 5 [4:31]
**Transcript:** into Unreal Engine 5.  With Unreal Open, the first thing I love to do is to set up a basic daylight system using  the environment light mixer.  And in just a few clicks, we've got a fully dynamic sky and clouds, totally free, which  helps us see what we're doing.  I like doing it because I don't like working in a black void.  So having a decent lighting setup to work with is a good starting point.  Now after that, the first step in creating any shot is establishing the composition, the  framing, setting up the camera early on.  Really this should be roughly one of the first things you do.  Place your subject in the frame, place a camera, and get that composition nailed down before  you start spending any time flushing out your scene.  You want to start working on only the things the camera will see.  There's no point in spending hours making a beautiful level, only to realize that most  of your hard work isn't even going to be in the frame.  You get the point.  Then I just move my directional light in the rough direction I want it to come from to  establish the initial lighting path.  But because my end goal here is to render a top quality, no exceptions kind of image,  I went with Unreal's Path Tracer, which is simply put a no BS, Baruch Force approach to  rendering.  The Path Tracer sacrifices all performance and throws it out the window for the sake of  maximum quality.  That's what I wanted for the shot.  Now when I'm working and moving assets around, I do turn the Path Tracer off, but when I'm  testing things out and getting a feel for the lighting, that is when I switch it on.  I've made a tutorial on the Path Tracer here, which was in UE4, but I'll be making an  updated one soon, so be sure to subscribe so you don't miss that.  When it comes to detailing a level, this is going to sound silly.  But a lot of it boils down to opening up the quicksil bridge, finding the assets you  need and adding them to your project.  I like to spend a good half hour or so building a good library before doing anything.  And from there, kitbash away.  My philosophy is to start with the big shapes, like establishing the ground, larger rocks  and trees, plants, there's no need to dive into the details yet.  That comes later.  Don't get bogged down into the details too early.  Now because I'm using the Path Tracer, I can't make use of Nanite, which is on real  way of handling literal billions of polygons on screen at once.  Because Nanite isn't quite real geometry, so to speak, it's what we call virtualized  geometry, and that is not supported by the Path Tracer, at least not now.  So it's crazy as it seems, when I'm using Unreal Engine 5, I need to go disable Nanite,  on the objects, on the model I wanted to use in the shot.  Just be careful, because that can put a lot of strain on your graphics card.  Now with this wide open patch of ground, it's still really not feeling like a forest,  right?  From there, it's just a matter of adding relatively larger scale foliage.  Bushes, shadows cast by larger trees to make it feel like a forest floor.  Because this is pretty close up, there is no need to bring in actual large trees.  I just scaled up these bushes here, so they cast shadows on the axe area.  All we need are some of those busy, patterned shadows, a kind of filtered light look, right?  From there, it is a process of experimentation, moving the sunlight around, trying to find  an angle that looks nice, and adjusting the tree shadow castors accordingly.  It's definitely a bit of trial and error here.  Now this next part is kind of all part of the magic sauce.  So far, you might think I'm really oversimplifying things, but this whole process is the easy part.  And reference, go outside, pay attention to detail, notice the little things.  Notice how the grass grows between rocks.  Notice the difference in the frequency of detail, small, high frequency details, and larger,  lower frequency details.  Make sure your rocks are not all the same scale.  You want variation, but variation in a way that makes sense.  I see students of mine painting rocks everywhere.  At the foliage tool, they go nuts with scale variation, but it's never going to look good  this way, because the randomness is too even, too consistent.  Again, look at reference and notice patterned and how pebbles and sand and mud blend together.  It's really going to open your eyes to how things look and feel natural.  Reference is key.  Do not try to make things from memory.  Your brain will lie to you and your arc will suffer as a result.  Let me explain to you why I'm talking about this.  Take this large rocky, pebbly, mega-scan's model, for example.  You don't need to use this at a one-to-one scale.  A little trick or hacker, call it whatever you want, that I like to use all the time is  to take this bad boy and scale it way down and duplicate it across the ground like this.  Then rotate it to break up the repeating tiling pattern and boom.  We have a sand-like ground.  So landscape mesh, no complex blending material, no displacement, thanks to the paste tracer,  you just know it's going to look good.  That is the kind of detail that is much trickier to nail down with lumen and nanite, because  nanite doesn't really render polygons that are smaller than a pixel.  And you miss out on that sub-pixel detail.  That is why I often opt for paste tracing.  Take this comparison of the exact same scene, one rendered with the paste tracer and another  with lumen and nanite.  The difference in shadow and global illumination detail is day and night.  No pun intended.  Hey so, future will here, I just want to take a moment to say that I am not hating on  lumen here.  This comparison is a testament to how good lumen has become.  But at a frequency, paste tracing is king when it comes to max quality.  Lastly, it's all about the attention to detail.  The final touch is adding leaves and twigs and very small detail that make a complete  world of different when it comes to that last little 5%.  This is the part that people often overlook.  Or just don't push hard enough or just don't have the eye to notice these things.  Here's a quick before and after.  It's a saddle change, but it really ties the whole piece together.  You can also use the details to hide imperfections.  It's kind of a win-win.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_003.jpg

### Times of Day [11:06]
**Transcript:** But that done.  Before rendering, I decided to have a little bit of fun.  Just the tries in different times of day, I went for an overcast feel and a night time shot.  Really, this is purely creative work.  Having fun with the various lighting tools in Unreal, I recommend watching my dedicated  lighting tutorial right here to learn the basics, as there are a hundred ways to light  a shot and all of them are valid.  You just need to know what you're going for and the tools available to you.  For the overcast day, I simply use a skylight with an htri found on htrihaven.  And for the night time shot, it's really just the blueish direction of light and I added  a point light to simulate campfire.  With our shots done now, we move on to the rendering and collocrating phase.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_004.jpg

### Rendering [11:48]
**Transcript:** So I'm going to be rendering these out at max quality using the movie render queue.  Here we can determine the resolution we want, the console variables we want, and the anti-aliasing  or sampling settings.  Then the post-process volume under the path tracing tab, I'm going to disable the denoiser  because I will denoise myself in the vintage resolve, but we're going to get into that  real soon.  In the movie render queue, be sure to delete the deferred rendering tab and add the path  tracing tab instead because we want the path tracer.  Always render in 16 bit exr to get the highest bit depth, which gives us flexibility and  post.  In color output, be sure to disable the tone curve.  And under anti-aliasing, override anti-aliasing should be checked, set AA metad to none, and  with the path tracer, 16 by 16 is a good starting point.  Troubleshooting path tracer renders is really easy.  It's your shot to noisy, you need more samples.  That's all there is to it.  In the output tab is where I determine my desired resolution, and in this case, I want  4K.  When you're ready, hit that render local button, and wait.  The path tracer is way slower than a deferred renderer, so go make a sandwich or something,  and come back later.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_005.jpg

### Davinci Resolve Denoising [13:04]
**Transcript:** 6 hours later.  Now, I've talked about this in many videos.  I even have a whole video dedicated to color grading and vintage resolve, but really,  this part of the process is where you really make your render shine.  Color grading is entirely subjective.  What one person might like, another person won't.  There isn't a good or bad way to grade.  It's all about the taste and getting to look you want.  I don't want to spend too much time on nitty-gritty here, because again, I've made two whole videos  on color grading and resolve already.  The one thing I do want to show you, however, is denoising and resolve.  Because the path tracer by nature is going to be substantially grainyer than when you use  the deferred rendering.  In the free version of resolve, select your imported clip and go to the fusion page, press  SHIFT, space, and add the noise reduction tool.  From there, your denoise setting will be on the right.  If you own the $300 studio version of resolve, you can add the noise reduction in the color  page, which is, by far, my preferred way of working.  I generally don't really enjoy using fusion.  So here's a quick before and after of each of the three final renders I did.  You may or may not like the direction I took, and that's okay.  But that being said, I hope you found this video helpful.  I hope I hit with able to shed a little bit more light on my rendering workflow.  Thanks so much for watching, and as always, happy rendering.

**Frame:** tutorials\frames\how-i-made-this-shot-in-unreal-engine-5\frame_006.jpg


---

## Structured Notes

### Core Technique
Axe hero shot workflow: Reality Capture photogrammetry (cross-polarized + scanning spray for shiny metal) → ZBrush retopo → Substance Painter PBR → UE5 Path Tracer (Nanite disabled) → MRQ 16-bit EXR, no denoiser, 16×16 samples → davinci-resolve denoising + color grade. Environment built camera-first; scaled-down Megascans rocks used as sand/pebbles; large-scale bushes as shadow-casting "trees."

### Summary
William Faucher's full production breakdown for three axe hero shots in UE5. 3D scanning: cross-polarized flash rig on tripod, axe mounted on ceiling with rotating arm (5° increments); subscan spray for shiny blade edge; ZBrush retopo and cleanup; Boolean for separate leather strap geometry; textures baked from Reality Capture, refined in Substance Painter (wood/steel/leather/brass PBR). UE5: camera and composition first; Path Tracer (not Lumen) for sub-pixel shadow and GI quality; Nanite must be disabled for Path Tracer compatibility. Environment scaling trick: giant Megascans rocks scaled down to sand-sized; large bushes scaled up for tree-shadow effect without needing actual large trees. MRQ: delete deferred rendering, add Path Tracer tab, 16-bit EXR, no tone curve, AA=none, 16×16 PT samples, disable denoiser. DaVinci: fusion Noise Reduction (free) or Color page (Studio).

### Key Steps

**3D Scanning:**
1. Mount subject on ceiling with rotating arm → camera on fixed tripod → rotate subject at 5° increments
2. Use cross-polarized flash setup to eliminate reflections for photogrammetry consistency
3. For shiny metal: apply subscan spray (fades naturally, no cleanup needed) → re-scan
4. Import photos to Reality Capture → align cameras → generate model
5. ZBrush retopology: clean up scan mesh into production-ready topology
6. Repeat for separate elements (with/without leather strap) → Boolean to separate geometry
7. Back into Reality Capture: generate albedo + normal map from photos

**Texturing:**
1. Export model + RC textures → Substance Painter
2. Set up multiple material IDs (wood/steel/leather/brass) with proper PBR maps
3. Export roughness/metallic/AO maps for UE5 import

**UE5 environment:**
1. Environment Light Mixer: add quick skylight + directional light for working visibility
2. Set up camera FIRST → nail composition before building environment
3. Quixel Bridge: spend 30 min building asset library (big shapes first — rocks, trees, ground)
4. Path Tracer: disable Nanite on all objects (required for Path Tracer compatibility)
5. Scaling trick: download large Megascans rocky/pebbly model → scale WAY down → duplicate across ground as sand/pebbles → rotate for variation
6. Shadow casting trick: scale up bush meshes to create large tree-like shadow patterns without full trees
7. Reference real environments: note frequency of detail variation, how grass grows between rocks, scale of pebbles vs rocks

**Rendering (MRQ Path Tracer):**
1. MRQ: delete Deferred Rendering tab → add Path Tracer tab
2. Color Output: disable Tone Curve → linear 16-bit EXR
3. Anti-Aliasing: override AA = None; samples spatial = 16, temporal = 16
4. Post Process Volume → Path Tracing → disable Denoiser (denoise in DaVinci instead)
5. Output: 4K resolution → Render Local → wait hours

**davinci-resolve:**
1. Free version: fusion page → Shift+Space → Noise Reduction tool → adjust settings
2. Studio version: Color page → Noise Reduction (preferred)
3. Color grade to taste; experiment with different times of day (overcast, night)

### UE Systems / Blueprints / Settings
- **Path Tracer**: brute-force rendering mode; far better sub-pixel shadow/GI quality vs Lumen; disable Nanite on all objects (Nanite = virtualized geometry, unsupported by Path Tracer); much slower
- **Environment Light Mixer**: Window → Environment Light Mixer; adds Sky Atmosphere + Directional Light + Skylight in one click
- **Nanite + Path Tracer incompatibility**: must disable Nanite per-mesh for Path Tracer to render correctly; increases GPU strain
- **Subscan spray**: temporary scanning spray that adds texture to reflective/smooth surfaces for photogrammetry; fades naturally
- **Cross-polarized flash**: eliminates view-dependent reflections in photogrammetry; requires polarizer on lens + polarizer on flash at 90°
- **MRQ Path Tracer tab**: replaces Deferred Rendering tab; required to use Path Tracer in renders; set AA to None + use PT samples
- **Reality Capture**: photogrammetry software (RealityCapture/Capturing Reality); outputs albedo + normal map from photos

### Difficulty
Intermediate–Advanced (photogrammetry + Path Tracer)

### UE Version
UE5

### Tags
[path-tracer, photogrammetry, rendering, lighting, environment, materials, movie-render-queue, davinci-resolve, post-production]

---

## Related Entries
- create-spectacular-accumulation-depth-of-field-in-unreal-engine-58.md (another advanced rendering mode — Accumulation DOF)
- fixing-common-ue5-issues-changes-in-50.md (rendering project settings — Path Tracing project setup)
