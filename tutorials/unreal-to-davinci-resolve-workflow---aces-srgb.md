---
title: Unreal to Davinci Resolve Workflow - ACES & sRGB
source: YouTube
url: https://www.youtube.com/watch?v=Bo3BvhGdaUo
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4 & 5"
tags: [rendering, color-grading, davinci-resolve, aces, ocio, color-science, mrq, exr, vignette, film-grain, chromatic-aberration, pipeline, william-faucher, intermediate, ue4, ue5]
extraction_status: complete
frames_dir: tutorials/frames/unreal-to-davinci-resolve-workflow---aces-srgb/
frame_count: 0
---

# Unreal to Davinci Resolve Workflow - ACES & sRGB

**Source:** [YouTube](https://www.youtube.com/watch?v=Bo3BvhGdaUo)
**Author:** William Faucher
**Duration:** 30m43s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey, welcome back William Fosha here.  Now I talk a lot about the importance of color grading your renders.  So now come to time to show you how I do things and what my workflow is for getting my  renders out of Unreal and into DaVinci Resolve for color grading.  I'm going to show you two ways of doing things in this video.  We've got the easy idiot proofway and the ace's workflow, which is actually a whole  lot easier to use than you might think.  Now for the record I do not claim to be the leading expert in color science.  In fact in my experience the deeper I dive into color science the less I understand.  We got IDTs and ODTs that are the color primaries and linear workflow.  What I'll be showing you in this video is what worked for me for both Procnoe projects  and production work, but definitely take it with a grain of salt.  If some of you watching do happen to be very well versed in color science and I'm in  a mistake do let me know in the comments below I will gladly stay and correct it on  the matter.  So let's get started with the important render settings in Unreal before we get started  in DaVinci Resolve right after a message from my sponsor.


### Skillshare [1:09]
**Transcript:** So a big thank you to Skillshare for sponsoring this video.  You guys know what skillshare is by now, but for those of you who don't it's an online  learning platform you can use to find thousands of inspiring classes on just about any  topic you want.  Whether you're thinking of a career change or you just want to pick up a new hobby.  If you're new to Unreal Engine and you want to make films and want to learn more on a  topic, Skillshare had you covered with cinematic captures in show to virtual filmmaking in Unreal  Engine.  And for myself prior starting this channel I had no idea how to use DaVinci Resolve and  OD things class on video editing in DaVinci Resolve really helped me hit the ground running  and get these videos out.  Skillshare's classes are curated, they're ad free, new classes come out every week, and  even if English is not your first language subtitles in Spanish, French, Portuguese,  and German are available.  So the first 1000 of my subscribers to click the link down below will get a one month free  trial so you can start learning right now.


### Into Unreal [2:06]
**Transcript:** And with that out of the way let's jump into Unreal and set up what we call OCIO.  So here I am back in Unreal.  You'll see I'm using Unreal Engine 5 Preview 1, but don't worry, you can use absolutely  any version of Unreal, whether it's UE5 Early Access or UE4.  The process here is exactly the same.  And before we get started I'm going to assume that you have an understanding of how the  movie render queue works.  If you don't know how, I already have a tutorial on that right here, so go check that out  when it comes to time to render.  Now in this tutorial I'm going to show you both the Aces workflow and the non-Aces workflow.  And for those of you who don't know what Aces is, it is the Academy Color Encoding System  which is basically the industry standard color space workflow that we use in film, VFX  and animation.  Even if you don't want to use Aces, the process is pretty much the same.  This is not an Aces specific workflow.


### OCIO Configs [2:59]
**Transcript:** The first thing we need to do before doing anything at all is we need to download an OCIO  config.  And so OCIO is OpenColorIO, which is an open source color pipeline, which is really focused  towards film, VFX and animation usage.  OCIO is where we get all of that Aces information that we need to render correctly.  So I've included a link down below where you can find all of the Aces config that you  may need for your own production.  But don't go ahead and download this whole thing.  This is like five gigabytes.  It is a huge file.  We don't need all this.  In this video, we're going to be using the Aces 1.2 config.  You can find it right here on the right hand side.  I'll also have a link directly to this if you want it down below.  At the bottom here, you'll find the OpenColorIO config Aces 1.2.  Download that and extract the zip file.  You're going to see why this is very important in the next step.  So back and unreal, we're going to go to our content browser.  And I'm going to make a new folder right here.  Call this OCIO underscore configs.  And in this folder, we're going to go right click again, go to miscellaneous.  And we're going to create an OpenColorIO configuration....


### IMPORTANT Render Settings [5:39]
**Transcript:** And we're going to start setting up our important render settings in the movie render queue.  These settings are absolutely critical.  So we're going to click on unsafe config here.  And these are the default settings.  I'm going to delete JPEG sequence.  And I'm going to add three more tabs.  The important ones here are anti-aliasing, color output, and EXR sequence 16 bit.  So EXR sequence is going to be your file format.  EXR is pretty much the best file format for rendering in.  It is a container for data that can hold 32 bit float data.  It's fantastic.  So we can leave the EXR setting the default anti-aliasing on a set of temporal count to 16,  set the override the anti-aliasing to none.  And the important one here is color output.  I see this one forgotten all the time, but it is the most important one.  So in the color output tab, we have MISC.  We're going to click on this OCEIO configuration.  And here I'm going to show you both the Aces approach and the non-Aces approach.  So if you don't want to use Aces, that's OK.  The process here is almost the same.  So starting off with the Aces workflow, we're going to click on OCEIO configuration is enabled.  We're going to load i...


### Into Davinci Resolve [8:46]
**Transcript:** And the reason I'm using this over any other package is because it's free.  I've included a link to DaVinci Resolve install page down in the description below.  So you can go ahead and find it right there.  Now DaVinci Resolve does have a paid studio version of it, which does have a few extra  bells and whistles.  But for the most part, most of what you'll be learning about today can be done with the  free version.  Now guys, once again, I want to be clear about is this is not intended to be an all-in-compassing  Bible of DaVinci Resolve colligating.  There are entire YouTube channels dedicated to only colligating in DaVinci Resolve.  So bear with me.  This is more intended to be a quick long tip video, all right?  So this is what you see when you load DaVinci Resolve for the first time.  You'll see at the bottom the important thing here, we have a whole bunch of menus.  We've got the media tab here.  We've got the cut page.  We have the edit page.  Then we have the fusion page, color, fair light, and the delivery page.  Now don't worry, we don't need to use most of these.  The ones we're going to be using is the edit page here, the color page right here, and  the delivery page rig...


### IMPORTANT Project Settings [10:20]
**Transcript:** So with that said, we're going to click on the file button up top here, go to project  settings, and this is where you're going to set up your entire project setting.  Now by default, the resolution is HD.  For my own sake, I'll be using 4K, but this is going to depend on your project, of course.  The timeline frame rate is going to be in 24 FPS.  If you're using another frame rate, you can choose it here.  But the important setting here is the color management tab over here on the left hand side.  We're going to set the color science to ACES CCTV.  We're going to choose ACES version 1.2 because that is a config file that we downloaded.  I think 1.3 seemed to be the latest, but I have not found a config file for ACES 1.3.  Next we're going to set our ACES output transform to Rec 709.  And that's all we need to do.  We're going to hit the save button and we'll be ready to go.  So now the next part of the process is to import our renders.  You'll see on the left hand side of our edit page, we have the media pool.  And this is where we're going to import our shots.  So I'm going to right click, import media.  And this is where I'm going to import the image sequence that we rendered ou...


### Importing Renders [11:34]
**Transcript:** rent queue.  For those of you wondering how do we convert image sequences into a video file?  This is how.  So I'm going to click on one, shift click to get them all in here and hit open.  And the venture resolve is going to understand that this is a sequence.  So it's not going to import every single frame independently.  So now we can drag and drop our shot into our timeline like this.  And now you'll see we have our entire animated shot in here.  So now I'll be color grading my nighttime scene that we saw in my previous video right  here.  But you'll notice that the colors feel totally wrong.  Like they're completely off.  This is not what we want.  And that's normal.  Okay.  Now the next part of the process is to tell the venture resolve how to read our images.  We need to right click on our clip here.  Go to ACE's input transform.  Go to color space conversion.  And we're going to convert this to ACE's CG.  And now the colors feel a bit more right.


### IMPORTANT Input Transforms [12:36]
**Transcript:** Now I've also brought in two other clips here for those of you who didn't use ACE's.  So if you didn't use OCIO and you only disabled the tone curve in the color output settings  of the movie render queue.  This is how you need to tell the venture resolve to correctly transform your renders.  And you'll see here, this is why it's really handy to name your files correctly.  So here I have no tone curve.  And here I have ACE's CG.  So I can clearly tell them apart.  I don't need to rack my brain trying to figure out which one is which.  So here you'll see if I just bring in these clips into the timeline, the colors are obviously  completely wrong.  They are oversaturated.  They look like crap.  What do we need to do?  So I'm going to right click here, go to ACE's input transform, color space conversion,  but we're not going to set this to ACE's CG because we didn't export it in ACE's CG.


### Unreal Comparisons [13:27]
**Transcript:** I see a lot of people doing this and it's wrong because if I do that, it got a bit better,  but it still looks completely wrong.  Your colors are going to be oversaturated and then crappy.  We need to right click ACE's input transform, color space conversion and set it to SRGB linear.  And now this looks correct.  This should match what you had in your Unreal Engine viewport pretty much.  This render here was rendered in ACE's CG.  So I'm going to right click ACE's input transform, color space conversion, ACE's CG.  And now you'll see these two renders match pretty closely, but you might notice that  the ACE's one has a bit more yellow in the brightest parts of the green wall.  Notice if I toggle between the two ACE's CG has way more yellow in it.  And from what I understand, that would probably have to do with the fact that ACE's CG  has a much wider color gamut than SRGB.  Taking a look at this diagram right here, you'll see that ACE's CG encompasses a much  broader range of colors than the limited SRGB space, especially in the greens.  Notice how there's way more range of greens in the ACE's CG one?  That would account for the difference in greens that we're getting here on the ...


### Color Grading Workflow [15:37]
**Transcript:** So we'll see we have these spaghetti neutrals here.  Every node is non-destructive, so we can go ahead and add another node by doing the Alt-S  shortcut to make another corrector node.  So I can go ahead and just change the white balance, for example, make this crazy warm  or something.  And if I realize that I don't like it, I can just delete it.  It's a non-destructive process.  It's kind of like layer-based editing, but better.  So we're going to get into these a little bit later.  Next, here we have our timeline right here.  So this is how we can kind of cycle through our shot.  At the bottom here, we have the color wheel.  And in the color wheel here, you might be a little bit intimidated because now we have  like, lift, gamma, gain, offset.  What does that mean?  It sounds really scary, but don't worry.  It's very simple to understand.  Lift will adjust mainly your shadows.  Gamma will affect mainly your midtones.


### Color Page UI [16:34]
**Transcript:** Gamma will affect mainly your highlights.  And offset, it's kind of going to shift everything evenly.  In the middle here, we have a histogram where we can adjust our image with the help of curves  like this.  And on the right, we have the waveform.  And you might, depending on your version of Resolve, it might be parade.  It might be VectorScope.  It might be something else, histogram like that.  Personally, I love leaving you that waveform because this is really going to help us visualize  if we are clipping highlights or clipping blacks.  Overall, the waveform is a fantastic tool.  And on the right hand side here, we have the FX library.  And this is where we have a whole bunch of effects we can add, like, radial blur and glow  and halation and all sorts of stuff.  For the sake of this tutorial, I'm not going to dive into all of these, but do feel free  to experiment with some of these.  So now that we have a brief explanation of the UI out of the way, let's get started.  With our first grade.  And so by selecting my node right here, I'm going to hit the Alt F shortcut.  And I'm going to right click on it and add a node label.  And I'm going to call this tone because my first ad...


### Vignetting [23:04]
**Transcript:** And we're also going to click on this right here and you'll see why now we can change the shape of this.  And I'm going to go back to my curves adjustment right here.  And I'm going to grab the top point here and bring it down.  And you'll see this is kind of what we're doing here.  We're adding a subtle vignetting effect.  Just be careful not to go overboard with that.  And you don't need to grab just this point here.  You can also grab one in the middle.  It's going to change how the mid tones or highlights are affected.  So I'm just going to do a very subtle effect like that.  And if I toggle it on and off, you'll see it's a pretty dramatic impact on the scene.  It helps us focus on the center of the shot a little bit.  It helps frame the image just a little bit vignetting into one of my favorite things.  I add it to most of my renders and most of my photographs actually.  But you know, some people hate it.  Some people love it.  Do whatever you like.  We can go back here and change the shape of it if we want to like that.  So really all we're doing here is just some kind of mask to shape the light a little bit in our scene.  I could also make another node here where I wanted to...


### Chromatic Abberation [25:34]
**Transcript:** So I'm going to show you my process for adding chromatic aberration, even though I wouldn't need it in this shot here.  So we're going to go ahead and add the chromatic aberration node here.  Next, we're going to right click add node add layer mixer.  Like that.  And we're going to right click again, add node add a corrector and a corrector is really just another default standard color grading node.  We're going to plug this one here.  We're going to place it underneath the chromatic aberration and we're going to plug this one into the bottom one of the layer mixer.  And so what's happening now is if I crank up the chromatic aberration like crazy, you'll see that the chromatic aberration is appearing everywhere in the frame like absolutely everywhere.  Even over here and I don't want that it's showing up in the grass.  I only want it to show up in the high contrast areas because that's how chromatic aberration works in real life with real lenses.  So what we're going to do is we're going to use this node here to mask out only the bright areas.  And that way chromatic aberration will only be applied there.  So you're going to want to make sure you have the eye dropper tool selected ...


### Film Grain [28:40]
**Transcript:** I'm going to set the preset to 35 millimeter 400T.  And I may increase the opacity of it.  Make it a little bit stronger just for effect.  And in fact, I'm not even sure if you are going to be able to see the film grain on YouTube  because of YouTube's compression and noise reduction.  So again, I'm just showing you what my process is.  Not necessarily for the final result.  And that's pretty much it.  If I select all my notes here and I hit control D, this is before and this is after.  Before after.  It was a pretty simple process, but we really managed to push our shot to the next level  with just a few notes like this in a completely non-destructive way.  So I know this was a lot to unpack here, but hopefully it made sense and you're able to push  your own renders to the next level yourself.  And now the last thing we need to do is render this video out.  So what we're going to do now is we're going to go to the bottom here and where it is like  a rocket ship, that's the deliver page.  And that is where we're going to render out this video.  So for those of you wondering how we convert a image sequence into a video, this is how.  So click on the rocket ship down here and you're ...


### Exporting Your Video [30:03]
**Transcript:** Next, you can choose the format you want, the codec you want, the resolution, your frame rate,  and the quality.  For the most part, you can leave it the default and it's going to work pretty well.  Next, the last thing you need to do is hit the add to render queue button  and hit render all.  And that's it.  You've rendered out your video.  Everything is done and you now have a video that you can play,  upload to YouTube, art station, share it to your friends and family.  Thank you so much for watching.  I hope you found this video helpful.  If you did, do consider subscribing and leaving a comment down below.  And as always, happy rendering.



---

## Structured Notes

### Core Technique
Original Unreal-to-DaVinci Resolve color workflow — older tutorial requiring manual ACES 1.2 config file download, full OCIO setup in Unreal, and full color page walkthrough in Resolve including ACES vs. sRGB linear import transforms, Lift/Gamma/Gain grading, vignette, chromatic aberration with mask isolation, film grain, and export.

### Summary
30-minute original color grading guide (older workflow). Requires downloading ACES 1.2 config from GitHub and setting up OCIO manually in Unreal. Two workflows shown side-by-side: ACES CG (exports in ACES color space) vs. non-ACES (Tone Curve disabled, exports linear sRGB). Both import into Resolve with specific input transforms. Includes full color grade walkthrough: waveform reading, non-destructive node editing, chromatic aberration isolation to highlights, film grain. **For newer/simpler workflow see 2026 Guide.**

### Key Steps

**Download ACES Config (older workflow only):**
1. Search "aces-dev GitHub" or use link from description
2. Download: ACES 1.2 config ZIP (NOT the full 5GB package)
3. Extract locally

**OCIO Setup in Unreal:**
1. Content Browser → right-click → Miscellaneous → OpenColorIO Configuration
2. In config asset, set Configuration File Path to the extracted `config.ocio` file path
3. Color Spaces to add: **ACEScg** + **sRGB Linear**
4. In MRQ → Color Output tab → OCIO Configuration: enabled → load config
5. Source: **Linear SRGB** (what UE outputs) → Destination: **ACEScg** (for ACES workflow)

**Non-ACES Workflow (simpler):**
- MRQ → Color Output → just disable Tone Curve
- No OCIO config needed
- Resolve will receive linear sRGB

**Resolve Project Settings:**
- File → Project Settings → Color Management tab
- Color Science: **ACES CCT**
- ACES Version: **1.2**
- ACES Output Transform: **Rec 709**

**Importing and Input Transforms in Resolve:**
- For ACEScg renders: right-click clip → ACES Input Transform → Color Space Conversion → **ACEScg**
- For Linear sRGB (no ACES): right-click → ACES Input Transform → Color Space Conversion → **sRGB Linear**
- Common mistake: applying ACEScg transform to a non-ACES render → oversaturated, wrong colors

**Color Grading Workflow:**
- First node: Tone ("ACE's Transform" node — already applied via project settings)
- Alt+S = add new corrector node
- Lift/Gamma/Gain: shadows/midtones/highlights
- Offset: shifts everything uniformly
- Waveform: use to check clipping and shadow crush

**Chromatic Aberration with Mask (Highlights Only):**
1. Add node → apply Chromatic Aberration
2. Right-click → Add Node → Add Layer Mixer
3. Right-click → Add Node → Corrector
4. Connect Corrector to bottom input of Layer Mixer (the unaffected base)
5. In Layer Mixer node: eyedropper → select bright highlights as mask
6. Result: CA only visible in high-contrast bright areas (realistic lens behavior)

**Vignette:**
- FX Library → Window → draw ellipse → Curves → darken outer area via lift

**Film Grain:**
- FX Library → Film Grain → set preset (35mm 400T etc.) → adjust opacity

**Export:**
- Deliver page → H264 or H265 → bitrate rule: fps × 2000 kbps

### UE Systems / Blueprints / Settings

**OCIO Config in MRQ:**
```
Content Browser → OpenColorIO Configuration:
  Config File Path: [path to extracted aces_1.2/config.ocio]
  Color Spaces: ACEScg, sRGB Linear
  
MRQ → Color Output:
  OCIO Configuration: Enabled ✓
  Transform Source: Linear SRGB
  Transform Destination: ACEScg     // for ACES workflow
  
  OR:
  Disable Tone Curve: True           // for simple linear sRGB workflow
```

**Resolve Color Science:**
```
File → Project Settings → Color Management:
  Color Science: ACES CCT
  ACES Version: 1.2
  Output Transform: Rec 709

Right-click clip → ACES Input Transform:
  → Color Space Conversion → ACEScg   // if rendered in ACEScg
  → Color Space Conversion → sRGB Linear  // if tone curve was disabled
```

### Difficulty
Intermediate — older workflow; requires ACES config file, more setup steps

### UE Version
UE 4 & 5 (works on any version — transcript says "UE5 Preview 1 but works on any version")

### Tags
rendering, color-grading, davinci-resolve, aces, ocio, color-science, mrq, exr, vignette, film-grain, chromatic-aberration, pipeline, william-faucher, intermediate, ue4, ue5

---

## Related Entries
- `tutorials/the-2026-unreal-engine-to-davinci-resolve-guide---aces-srgb.md` — Updated 2026 workflow (simpler, no config download needed)
- `tutorials/the-2025-guide-to-rendering-in-unreal-engine-5.md` — 2025 rendering guide
- `tutorials/path-tracer-explained---unreal-engines-underrated-tool.md` — Path Tracer + Resolve denoising
