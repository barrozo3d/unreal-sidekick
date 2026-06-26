---
title: Improve Your Renders With Unreal Movie Render Queue PART 1 - Goodbye Sequencer?! (4.26)
source: YouTube
url: https://www.youtube.com/watch?v=FxvF3zncClA
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4.26"
tags: [mrq, movie-render-queue, rendering, anti-aliasing, subsampling, quality, sequencer, console-variables, high-resolution, ue4]
extraction_status: complete
frames_dir: tutorials/frames/improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4/
frame_count: 12
---

# Improve Your Renders With Unreal Movie Render Queue PART 1 - Goodbye Sequencer?! (4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=FxvF3zncClA)
**Author:** William Faucher
**Duration:** 16m23s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey, welcome back.  It's Sonas with Here Faces.  In today's video, we're going to be talking about a little lesser known feature known  as the movie RenderQ.  And this has finally been made production ready as of 4.26.  So it's a pretty new thing.  Just to make it clear, the movie RenderQ is not here to replace the sequencer and the  Q work together.  So think of the movie RenderQ as a DLC or a supplement or add-on to sequencer.  Now some of the notable perks of using the movie RenderQ include much more streamlined  UI, way more rendering features, and much higher quality renders if you so desire.  This video is split up into two parts.  The first part I'm going to be comparing both default settings in both sequencer and  the movie RenderQ, just to show you guys that hey, the renders are actually the same  if you so want them to be.  In part two, I'll be showing you guys how to take things one step further and getting  some of the cleanest, best possible renders I've ever seen come out of Unreal.  So without further ado, let's get started.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_000.jpg

### Enabling Necessary Plugins [0:57]
**Transcript:** Alright, hey guys, let's get started in Unreal.  The first thing we want to do is we need to enable two plugins.  I believe in Forty Point 26, they're enabled by default, but let's just go ahead and  enable them anyway.  So go to the settings tab, up on the top here, click on plugins, and you want to type  in the search bar up here, movie RenderQ.  And two plugins will show up, make sure both are enabled.  You'll have to restart the engine as always.  It's done very long, this is normal.  Now, you're going to want to enable additional render passes as well because this enabled  Kurtomat or object ID.  And if you don't know what that is, I've made a video about it right here.  So without further ado, once you've restarted the engine, let's get started.  So once you've enabled those two plugins, the first thing we need to do is we need to set

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_001.jpg

### Loading Your Sequencer File [1:46]
**Transcript:** up a sequencer.  Now, this tutorial is not going to be about sequencer.  If you don't know what it is or you don't know how to settle up, there's lots of documentation  about this.  Go ahead and assume that you know what sequencer is and how it works.  So sequencer and the movie RenderQ kind of work in tandem.  One does not replace the other.  So we need to go through the Cinematics tab up here and I've already made a sequence.  All right, so I set up a very quick camera here.  Not even any animation.  We've got a lovely environment here that I cannot take credit for.  This is taken from the Megascans Goddess Temple.  Now this is free.  It's a free pack on the Epic Marketplace.  The link is in the description below if you want to go ahead and find it for yourself.  It is a gorgeous looking scene.  All I did was I deleted a bunch of stuff and I changed the lighting a bit so I got  a one and a more sunset feeling.  But the lighting is really the only thing that I did in this environment.  So the first part of this video is I'm going to render both a shot from sequencer and a  shot from the movie RenderQ.  We're going to look at these two still images in Photoshop and we'll be able to compare  result and you're going to see with the default movie RenderQ settings the results are  exactly the same or almost.  We're going to go ahead and hit the RenderQ video button in the Render Movie settings.  I just showed my output past on going to be rendering PNGs and I'm just going to hit  capture movie.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_002.jpg

### Using Movie Render Queue For The First Time [3:08]
**Transcript:** So once you've got your sequence set up, you got your camera established, you know, you  got your framing right, we're going to go ahead and look at the movie RenderQ for the  first time.  So where do you find that?  You find it up here in the Windows tab.  Click on Window, go to Cinematic Movie RenderQ.  Click on that and your window will pop up.  So this is not a brand new thing.  This came out in 4.25 but I think believe that it is now production ready as of 4.26.  So what we're going to do is we're going to hit plus the plus render button right here.  Click on that and add the sequence that we just created.  Now you're going to have your job setting and output.  So don't worry about this, just click on Unsaved Config right here.  You're going to get another window that shows up.  So I'm going to, so you got, this is a pretty straightforward tool.  I really like it.  It's clean, it's concise, so I, you got output, rendering and settings.  I'm going to go ahead and click this and I'm going to delete the JPEG sequence because  I don't want to render in JPEG.  So I'm going to go into setting and we click on setting up here, you have a ton of options  to show up.  So you got the anti aliasing stuff, console variables and output, you can choose the output  stuff files that you want and the rendering mode that you want.  So I'm going to go ahead and add PNG sequence 8 bit because that's what my sequence would  render in.  The further rendering, you can kind of leave that as is output.  Now one thing that I really want to look at here is the anti aliasing setting.  Now this, this setting right here is a game changer by default.  It's just leaving a default settings.  It's going to, you can see right here, anti aliasing method is done as great out.  If you override it, you can change it.  For now, I'm going to leave it off.  So I'm going to not override anti aliasing by default.  The movie render queue uses the anti aliasing method that your project is using.  So sequence, so what you're getting sequence is what you're going to get in the movie render  queue if you leave this off.  So for now, I recommend leaving this off.  And because we want to get the same render from sequencer and movie render queue, right?  So what that done, choose the output path, make sure everything's okay, hit accept, render  local and a new movie, new window will pop up.  And there we go, it's rendered.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_003.jpg

### Render Comparison A [5:33]
**Transcript:** So now let's jump in Photoshop.  Okay, so I've opened up the renders here.  Two still images.  So this one, this is the image from sequencer and this is the image from render queue.  As you can see, there are some subtle differences, but for the most part, it is the exact same  render.  So the difference is that you see your mostly noise related.  You know, as I zoom in and toggle this layer on and off, there's some minor differences,  but for the most part, it is negligible.  Like if I didn't know any better, I wouldn't even know that there's a difference.  So by not touching any of the AA settings, the anti aliasing settings in the movie render  queue, you're going to get the same result as you did in sequencer.  So that's kind of a safe thing.  That's really good to know because I don't want it to be different, right?  Not yet.  So that's how you render it, you know, normally.  So guys, you don't need to take my word for it.  I've included all the renders that I'm going to be making throughout this video down in  the description below.  So you can go ahead and download them and see for yourself, see what's your best.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_004.jpg

### Movie Render Queue Benefits [6:35]
**Transcript:** So why would we even use the movie render queue when by default, the results with compared  to sequencer are going to be almost the same.  We're going to be looking at four things that make the movie render queue a complete game  changer.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_005.jpg

### Streamlined UI [6:48]
**Transcript:** So the first thing that we're going to talk about is just what kind of goes without saying,  and that's the cleanliness of the UI.  Everything is kind of found in one place.  You want to add a setting, you want to add a render pass, you want to add another file  format, everything is accessible right here.  So for example, if you want to render out both EXR and a JPEG sequence, well, now you  can.  So you can add render multiple file formats at once.  In sequencer, you could not.  You could also add multiple render passes, you have full control over it.  You have full control over a bunch of things.  This is one of the things that makes the movie render queue just a little bit more peeling  than the sequencer.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_006.jpg

### High Resolution Tiled Render [7:22]
**Transcript:** So another cool feature that was included in the release is the addition of the higher  resolution setting.  So what the high resolution tab is going to do is it's essentially going to.  I think you can see here in the Unreal documentation, it is going to render four different tiles.  And it's allows you to get four times the resolution of whatever.  So if you render, you know, each tile is 4K, then that means you're going to get a massive  file.  Now the downside of this is you're not going to.  It's not doesn't support any of the screen space stuff.  So, you know, like reflections, convolution, bloom, lens flare, motion blur, that sort of  thing is not going to render correctly.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_007.jpg

### Improving your Render Quality with AA Subsampling [7:58]
**Transcript:** So use this with caution.  Now we're going to go ahead and add anti aliasing.  And this is where thing get really interesting.  This is what makes the movie render queue such a big deal.  Right now in order to increase the quality of your renders, now the render allows you to  get some sub sampling.  Okay.  So what you're going to do is you're going to override anti aliasing.  We're going to change the anti aliasing to none.  All right.  Don't panic.  It's fine.  Your renders are not going to have no anti aliasing.  You get bring increased the sample count.  All right.  So we're going to go ahead and set this to 64, which means it's going to have 64 subsamples  between the frames and they're going to give you an extremely clean render.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_008.jpg

### Console Command Menu [8:44]
**Transcript:** So the next thing you want to do, if we're going to go ahead and go to setting here and  add console variables.  Now according to the unreal documentation, which the link of which will be included in the  description below.  So tell us right here in the documentation that Unreal Engine makes ray tracing possible  through the use of de-noiating techniques that do rely on temporal history.  When using high resolution tiling and disabling temporal anti aliasing, you may need to adjust  the following console variables for better results.  And they're talking about the four console variables down here.  So we're going to go ahead and we're going to copy those into our movie render queue.  So you go to make sure you have the setting console variable in your list here.  And console variables, you're going to want to click a little plus, the first one up here  on the top, click on the plus, and you're going to go ahead.  We're going to go ahead and paste the console variable from the list.  OK.  So if we got it right here, all right.  We're going to copy paste this now.  Be sure that you don't copy paste everything with the zero.  OK.  Make sure you only copy the text because the actual number is included here.  So this is zero.  If I wanted to be on, it said it to one, but we're going to have it zero.  So a mistake I made yesterday was I copied all of it, the whole thing was a zero.  And my render didn't work.  I was wondering why it said the console variable doesn't exist.  Blah, blah.  So just make sure the only copy of the text and paste it into your thing.  All right.  Now add another one.  I'm going to go copy this again.  Get this one.  Add another refraction denoiser, reflection denoiser.  Put that there.  And the shadow denoiser.  One more.  OK.  So now that these console variables are done, we can go back to the anti-aliasing tab.  Just make sure that you know, 64 samples.  You can hit accept.  Once that's done, you're going to go to output tab.  Make sure that your output directory is OK.  So once it's left you to your output folder, you are ready to render.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_009.jpg

### Rendering in High Quality [11:03]
**Transcript:** So hit accept.  So before rendering, I've actually gone ahead and I made a little animation  from my camera over nine frames.  OK.  So just kind of give you guys an idea.  I got my camera here.  And over nine frames, it's going to move like this.  I'm going to go ahead and turn pretty much turn off all that to field.  Because I want the everything that's blurred to be motion blur only.  And you're going to see why in just a second.  All right.  So I'm going to set this to like F16 right here to just basically eliminate all  that to field.  So the only blur that we're going to get is going to be motion blur.  OK.  Now going back to the movie render queue.  Now that we're ready, just going to go make sure everything's  OK.  Yeah, everything's there except.  And now you're just ready to hit render local.  The window is going to pop up again.  So you can see it's going real slow.  You can see the sub sample count here going up.  So from 0 to 64.  And it's going to pop.  Going up.  And it's going to pop.  So what is doing right now just to kind of explain what's happening is the amount of  sample tickets is this amount of sub sampling that's going to happen.  So it's going to give you a much cleaner render.  Your motion blur example.  They're going to be much better.  There's going to be less, much less noise in your image as well.  It is much longer to render.  That is a given.  But what you're about to see soon when we compare the render from this and in  sequencer is your image is going to be much, much cleaner this way.  So the longer render time in my opinion are absolutely worth it.  So now that this is done, I'm going to go ahead and render the same shot with sequencer.  OK.  So we're going to be able to compare the animated frames from sequencer and the movie render  queue.  So I've made sure you my output directory is OK.  New folder, PNG, 1080p.  You can go ahead and click catcher movie.  It's selected.  Now obviously sequencer is much faster rendering it, right?  It's real time.  We're almost.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_010.jpg

### Render Comparison B [13:27]
**Transcript:** So one image of the rendered, we're going to go right back into Photoshop and  we're going to compare those two rendered between the movie render queue with no  anti-aliasing and a bunch of sub samples versus sequencer, which is the much faster  renderer, but you'll see why I prefer to use the rear end of the queue from now on.  So right here is we've got the sequencer render.  Now if you can see here, you know, there's a bunch of noisy samples.  The motion blur is not great.  It's not very, it doesn't look very good.  But next, this is the movie render queue result.  Now going from A to B, you can see that the movie render queue results are substantially  better.  Just look at noise samples here, right?  On this urn.  This is sequencer, this is the movie render queue.  The motion blur itself alone, look on the side here, it's much softer, much creamier.  The biggest shock to me was in a plant, right?  Look at the noise on the plants here, right?  It is just absolutely a noisy mess.  But here with the movie render queue, everything is clear.  It is very clean.  Okay.  Same with the motion blur.  Look at the out of focus elements here in a motion blur, right?  Look at these temporal AA artifacts, you've got in the ferns up here.  But when I turn on movie render queue, it is a proper motion blur.  I mean, if I didn't know any better, I would think this is a ray traced.  So there you have it.  I mean, yeah, I mean, just look at this right here.  Just everything about the movie render queue renders are so much better.  Okay, now I know I'm at 300% here, but just look at this noise, look at all these artifacts  here.  And then in this render, it's nice and clean.  So I understand this might be hard to see in the video.  If you don't believe me, see for yourself.  I've included this PSD in the description below, download that file and see for yourself  just the wild, massive difference in quality between the two renders.  But just see for yourself, you're never going to be going back to sequencer ever again.  Because this is just this to me as a game changer.  This changes absolutely everything.  So after saying this, I am chance I'm not going to be using sequencer ever again, just because  the difference in quality for me is absolutely worth the extra waiting time.  That being said, sequencer still has some uses here, because if you need the fast render,  you can iterate quickly.  Sequencer is the way to go because they did that much faster.  But if you can afford to wait a little bit, I'm not going to be using sequencer much anymore.  So once again, guys, thank you so much for watching.  Don't forget to like and subscribe and make a world of different for small channels like  mine.  And I'll see you guys in the next video.

**Frame:** tutorials\frames\improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4\frame_011.jpg


---

## Structured Notes

### Core Technique
Movie Render Queue (MRQ) setup for UE4.26 with AA subsampling for dramatically cleaner renders vs Sequencer. Key insight: Override AA → None + high Temporal Sample Count (64) + 4 ray tracing denoiser console variables = motion blur and noise quality equivalent to offline renderers. Side-by-side comparison proves MRQ quality is far superior to Sequencer for final renders.

### Summary
16-minute intro tutorial by William Faucher introducing Movie Render Queue in UE4.26 as the new production-ready replacement for Sequencer's built-in renderer. Part 1 covers: enabling two required plugins, setting up MRQ for the first time, comparing default MRQ vs Sequencer renders (essentially identical by default), then enabling AA subsampling (Override AA → None + 64 temporal samples + 4 console CVars) for dramatically improved quality. High-Resolution Tiled Render feature noted (4× resolution tiles but no screen-space effect support). Conclusion: MRQ with subsampling produces far superior motion blur and noise floor vs Sequencer; author won't use Sequencer for finals again.

### Key Steps
1. **Enable plugins** (Settings → Plugins):
   - Search "movie render" → enable "Movie Render Queue" plugin
   - Also enable "Movie Render Queue Additional Render Passes" (required for Cryptomatte/Object ID)
   - Restart engine
2. **Open MRQ**: Window menu → Cinematics → Movie Render Queue
3. **Add sequence**:
   - Click + (Render button) → browse to your Level Sequence
   - Click "Unsaved Config" to open render settings
4. **Configure file format**:
   - Delete the default JPEG Sequence entry
   - Settings → Add: PNG Sequence 8-bit (or EXR Sequence for production)
5. **Set output path**: Output tab → set output directory
6. **Enable AA Subsampling** (the main quality upgrade):
   - Settings → Add: Anti-Aliasing
   - Anti-Aliasing Method: Override → set to **None** (this is correct — don't panic)
   - Temporal Sample Count: set to **64** (64 subsamples = very high quality; more = slower)
7. **Add console variables** (for ray tracing denoiser suppression during subsampling):
   - Settings → Add: Console Variables
   - Add 4 CVars from UE documentation (ray tracing denoisers set to 0): prevents denoiser artifacts during subsampling
   - Note: copy text only, not the trailing " = 0" that's already in the value field
8. **High Resolution Tiled Render** (optional for super-high-res stills):
   - Settings → Add: High Resolution
   - Each tile = project resolution; final composite = 4× tiles
   - WARNING: screen-space effects (reflections, bloom, lens flare, motion blur) do NOT render correctly in tiled mode
9. **Hit Accept → Render Local**
   - Observe temporal sub-sample counter climbing (0 to 64 per frame)
   - Expect significantly longer render times vs Sequencer (worth it for quality)

### UE Systems / Blueprints / Settings
- **Movie Render Queue (MRQ)** — production render system; enabled as plugin; UE4.26+; works alongside Sequencer (does not replace it)
- **"Movie Render Queue Additional Render Passes" plugin** — required for Cryptomatte and Object ID passes; separate plugin from core MRQ
- **Anti-Aliasing setting (MRQ)** — Override Anti-Aliasing Method + set to None: disables real-time TAA, instead uses temporal accumulation from sub-sample count; counter-intuitive but correct
- **Temporal Sample Count** — number of sub-frame samples per rendered frame; 64 = very high quality; default is 1 (same as Sequencer); higher = slower render, better motion blur + noise
- **Console Variables setting (MRQ)** — inject console commands per-render without modifying project settings; used to disable ray tracing denoisers during subsampling for cleaner results
- **Ray tracing denoiser CVars** — four CVars from UE docs (r.RayTracing denoisers for sky light, reflections, GI, shadows — set to 0 during MRQ subsampling); prevents temporal artifacts
- **High Resolution Tiled Render (MRQ)** — renders 4 tiles at project resolution for 4× final resolution; good for stills/print; does NOT support screen-space effects (SSR, bloom, lens flare, motion blur)
- **Render comparison** — MRQ default == Sequencer default (same quality if AA override disabled); MRQ + 64 samples = vastly superior motion blur, noise, and edge quality vs Sequencer at any setting
- **Sequencer limitations (by comparison)** — fast but noisy; temporal AA artifacts in motion; no sub-sampling; best for quick iteration previews, not finals

### Difficulty
Beginner-Intermediate. Core setup is straightforward once you know where to find MRQ (Window → Cinematics). The "Override AA to None" instruction feels wrong but is correct — the tutorial explains why. Console variable list comes from UE documentation.

### UE Version
UE4.26 (MRQ made production-ready in 4.26; same core workflow applies in UE5 with some UI updates; High-Resolution Tiled Render screen-space limitation still applies in UE5)

### Tags
mrq, movie-render-queue, rendering, anti-aliasing, subsampling, quality, sequencer, console-variables, high-resolution, ue4

---

## Related Entries
- `improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn.md` — Part 2: MRQ limitations (Cryptomatte slowness, DoF/Object ID, Z-depth) and workflow features
- `how-to-render-cryptomatte-in-unreal-new-in-426.md` — dedicated Cryptomatte/Object ID setup tutorial
- `how-to-render-passes-with-the-movie-render-queue-unreal-engine-426.md` — adding render passes (Z-depth, world normal) in MRQ
- `how-to-use-the-movie-render-graph-in-unreal-engine-58---simple-setup-for-filmmak.md` — MRG replaces MRQ as of UE5.7+ for multi-camera
