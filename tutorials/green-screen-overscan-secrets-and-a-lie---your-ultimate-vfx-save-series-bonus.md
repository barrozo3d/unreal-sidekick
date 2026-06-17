---
title: Green Screen OVERSCAN SECRETS (and a LIE!) - Your Ultimate VFX Save! (SERIES BONUS)
source: YouTube
url: https://www.youtube.com/watch?v=qe2x-puqVl0
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus/
frame_count: 14
---

# Green Screen OVERSCAN SECRETS (and a LIE!) - Your Ultimate VFX Save! (SERIES BONUS)

**Source:** [YouTube](https://www.youtube.com/watch?v=qe2x-puqVl0)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 26m38s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### What is Overscan? Essential for digital filmmaking & post-production [0:00]
**Transcript:** What is Overscan? Why is it fantastic for digital filmmaking?  And how do we get it to work with Unreal Engine and the vintage result?  I'll show you how.  OK, so you've got this shot and then you bring it into your edit  and you want to reframe it a little bit.  Or you want to add some lens distortion.  Or you want to add some camera shake. Something like that.  Well, if I take this shot and do that,  you'll see around the edge of the frame,  it's just black because there's no data there.  So the bad way of kind of fixing that is to push in on your image.  But then that softens your image.  So ideally, what you'd like is to have your regular frame  but with extra data outside of the frame.  So effectively that frame's bigger.  So what you can do in Unreal Engine is add something called Overscan  and that effectively gives you a percentage extra outside of the visible area  that you can then push around and play with inside your edit.

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_000.jpg

### The Problem with DaVinci Resolve Media Pool [0:55]
**Transcript:** There is an issue that I've got currently with DaVinci Resolve  in that if you bring in images with extra data,  when you bring those into the edit page,  it will throw that data away.  So we have to trick Unreal using a blueprint  into rendering the display window to match the data window.  And that's something that I'll show you later on.  So let's just start with the basic how to use Overscan with regular  Unreal Engine and I'll show you that now.  And then also there's absolutely no reason  why you need to be in a flying car for this.  It was just bored and wanted to play.  So see you in a second.

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_001.jpg

### Adding Overscan in Unreal Engine - Regular Method [1:36]
**Transcript:** So I'm here in Unreal Engine and I'm going to show you how you would  add Overscan to your regular cine camera.  And it's over here.  So you select your cine camera and then you go down to the details panel  and there's one here called Overscan.  And so it's a percentage.  So you'll see as I make this percentage,  we're going to add a 20% Overscan.  And what that will do is basically shrink your C.  Here we go.  Point two.  Don't you see?  It shrunk my image down.  So it's effectively made it bigger.  And let's go for point five.  Like that.  So it's kind of like shrunk it all down.  It's kept me relative in the middle.  Now you could work like this.  But it's kind of like hard to understand what the shot is kind  of looking like effectively.  Because you used to framing for that full size like this.  And you're kind of like you're editing your sequence together  in Engine.  You're cutting your cinematics and stuff like that.  So if you change the Overscan size,  it's going to kind of throw that around.  And so what you do is you crop the Overscan.  So if you turn that on.  So effectively now it looks the same.  But you've got this data window outside of your this area,  this frame...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_002.jpg

### Overscan Renders in Fusion versus the Media Pool [4:36]
**Transcript:** So that little opening sequence was rendered with Unreal Engine.  And I used the overscan function of the camera.  And I made that point too, which gave it 20% overscan.  And so I'm going to bring those into a fusion composition  using Control-Space and then Loader.  And then you navigate to your first frame,  and you click Open.  And so here it's put this image over this background, like that.  So there's my actual render size, but it's got 20% extra outside of this area.  This is called your display window.  And then your data window is that overscan area.  So now if I grab my merge node and just move this,  you can see there's extra data.  There's actually an image outside of there.  And that's great.  So you can apply it, you can do a little camera shakes,  and you can put some lenders distortion on this and all those sort of things.  But the trouble with that is that you have to do it through fusion.  So for every single shot, and I'm doing a feature film,  so I don't want to have to do 1,000 shots in fusion.  So I want to do it in the regular edit page.  But if I bring in a regular edit, so I go into my Media Pool,  and then I go right mouse button, Import Media,  and I'm goi...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_003.jpg

### Blueprint solution: scaling sensor width for DaVinci Resolve compatibility [7:05]
**Transcript:** So that's great.  And then if you want to bring them into the Media Pool  inside of DaVinci Resolve, then I thought what I could do  would just be to turn off the crop overscan.  But I just found out that when you do render like that,  it is only a display thing.  It's still rendering with that data window  and the display window on the other way around.  So I would do it in the same way  that the actual blueprint works.  And the blueprint works by scaling the sensor.  So it turns off the overscan and that amount there.  And the blueprint basically takes the sensor width  and sensor size, and it multiplies that by percentage.  So if I times this, say I wanted a 50% overscan,  I would times this by 1.5.  So you take your number here, sensor width, times 1.5,  and then take the sensor height times 1.5.  And then that way, this will actually render like that now.  So it's all relatively the same, except now my window  is effectively pulled back and it's wider  without changing any of the lens distortions  or field of view or anything.  Or kind of just changes to field of view.  Well, whatever, it looks the same pixel pixel in the middle  if I scale my resolution.  So it's a little bit...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_004.jpg

### Creating an Overscan on Render Blueprint [9:05]
**Transcript:** So here I have a little scene.  It's actually another tutorial that I'm making  on how to tell a movie in 30 minutes.  So basically it goes over how you create a sequencer  and you bring in some animation, now you do some cameras.  Good stuff.  So make sure you watch that after this video.  But I'm gonna use this as an example  of changing the overscan with the blueprint.  So if I just stop this and go to one of the cameras.  So let's find the first camera.  And then I go into the actual camera.  And then I've got my overscan is all turned off.  And then we've got our sensor width and sensor height.  So that is your lens, takes the light  and it focuses onto a sensor in a real camera.  And this is the digital equivalent of that.  And depending on how big an expensive your camera is,  that sensor gets really small for cheap cameras  and then they're bigger and bigger for hassle blads  and big expensive cameras.  And it's about that sort of size for a cine camera  for a movie making.  And so this is probably a little bit bigger digital film.  Anyway, if I change the sensor width  and you'll see the camera effectively gets wider.  So like that.  Okay.  As in the width and then we've g...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_005.jpg

### Rendering with Overscan in Unreal Engine's Movie Render Queue [16:06]
**Transcript:** Okay, so we've got our overscan it in there,  and now we're about to render,  so I'm going to call up my movie render queue,  and it's my existing setting,  so the thing to do is to set this output resolution size  to originally it was 1920,  so I'm going to times it by 1.5,  and then the output resolution by times 1.5,  and you only have to do this once,  and then just to make sure my output directory  is set to the right place, select folder,

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_006.jpg

### Optimal color output settings for overscan EXR frames [16:40]
**Transcript:** and then one thing I've got on here is,  I was rendered with tone map turning off,  so if you add in the settings, you add a color output,  and then I disabled the tone curve,  so this will render in linear SRGB with EXR frames,  so there's lots of dynamic range,  but when you bring them into your project,  then you'll need to apply a color space transform,  press accept, and then we hit render local,  and then it starts compiling that,  it starts running it out,  and you can see on your image here  that the color space looks a bit weird,  it's funky, because it's giving you a linear SRGB preview,  and then also if you look and compare to the size of the frames,  you're getting that extra space around the edges,  so that's great.  So there are some disadvantages with using Overscan,  and the biggest one is that,  because your frames are bigger, then it uses more memory,  so if you're right on the edge of your memory limits,  and you make your frames bigger,  and you've got more information,  then it can cause it to crash,  and you go over those memory limits,

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_007.jpg

### Disadvantages of Overscan - Slower, More Memory and Larger Frames [17:41]
**Transcript:** so that's not a good thing,  and the other disadvantage is that the frames are bigger,  so it takes up more disk space,  and also because there's more information, more detail,  then the frames are gonna take longer to render.

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_008.jpg

### Importing and managing Overscan footage in DaVinci Resolve [17:52]
**Transcript:** Okay, so we are in DaVinci Resolve,  and I'm in the edit page,  and I've got a timeline that's set up,  and I'm just gonna go into the settings of that,  so select your timeline, write mouse button,  timeline, timeline settings,  and then I'm just gonna show you that the resolution  is 1920x1080, which was the size of my original renders,  before I added the Overscan,  and then the important thing is to just check  that mismatch resolution is set to scale entire image to fit,

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_009.jpg

### DaVinci Resolve timeline settings for oversized images [18:23]
**Transcript:** and what that will do is it will bring in your oversized image,  so you've got a full-camage,  it'll bring that in, and it will squash it to fit  inside your timeline,  but it keeps all of the data,  it doesn't recompile or recompress the image,  it doesn't throw anything away,  so if you scale it back to its original size,  it still has all of that pixel information,  so that's the important thing, so that's great,  so we hit okay,  and now I'm going to bring in those sequences,  I'll bring in the original, so I'm gonna create  a new bin, write mouse button,  and just call these shots,  go into those, new bin, original,  original, import media,  and then I'm going to find my original clip,  so go to that one,  and if I select the first frame and scroll down to the end,  and select the last frame,  do inches smart enough to know these are individuals,  friles, and that their individual shots,  and it'll make you the shots,  now if you bring these in,  and they come in as thousands of individual images,  go into your main media page,  and check under media storage,  these three little dots,  that frame display mode is set to sequence,  because it's set to individual,  it bring in ev...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_010.jpg

### Benefits of overscan for Lumen rendering & avoiding artifacts [21:50]
**Transcript:** and uses screen, I don't know what it's doing,  but I know that if you have, oops,  if you have this overscan effectively,  then those problems are kind of moved to the edge,  which is kind of a good thing,  because sometimes, like say you've got an object,  and it's leaving the shot, it's leaving the frame,  and they turn off, but sometimes they kind of turn off  just before there, and there's the sea vars,  and things like that that kind of fix it,  but it's just stuff like that,  if you've got a wider image,  and you're kind of cropped in a little bit,  then you don't have to worry about those things,  so there's an added bonus, hooray!  Okay, so we're gonna apply a color space transform onto these,

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_011.jpg

### Applying Color Space Transform to linear SRGB overscan footage [22:25]
**Transcript:** and also I won't do the zoom here,  I do it in the color page, because I want to do it,  before I do the lens distortions, and all those things,  if I did a lens distortion on this,  it would do it over this, not the original uncroped version,  so let's keep those as is,  and there we're going to go into the color page.  So I'm going to add a color space transform,  so I go into the search there, color space transform,  drag that onto the noodle,  and then going to input color space,  and if I start typing SRG,  it'll find it in this list,  so SRGB, and the input camera is linear,  now it looks kind of nice,  but it's still got this little funkiness on some of the colors here,  so you go into your gamut mapping method,  and change up to saturation compensation,  that kind of gets rid of those weird things,  and I think you've got a knee and toe,  and all those sort of things here,  bi-bi-bi-bi-bi-bi-bi,  so you can play with that afterwards.  There we go, so there's our image,  and now I'm going to apply a transform,  so I'll do all these things before the color space transform,  so if I do a color correction after a color space transform,  then it's doing on the transform,  so if ...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_012.jpg

### Enhancing footage in the Color Page: Lens distortion & camera shake [24:15]
**Transcript:** transform before that,  and then this, basically if I change this to 1.5,  now we're back to where we would've been  before our oversized renders,  so we'll come out of here into our edit page,  just to confirm that the images are matching one to one  in their sizes, okay,  and now we don't really need these underneath,  I'm just going to cut those,  so now we can go into our color page,  and add in say a lens distortion,  so if I go to the library,  and we'll type to lens distortion,  drag that over onto my noodle,  you can see now when I do a lens distortion,  there's data around the outside to pull that through,  and then, you know, what else can you do?  So you can add some camera shakes,  I'm going to add a camera shake in a lens distortion,  I'm going to add the camera shake before the lens distortion,  so we just type in camera,  drag that onto the noodle here,  and it defaults to zoom to crop,  so we can turn that off,  because we've got extra room, it's around here,  and then just hit play,  I'm going to hit loop on there and hit play,  so there's our camera shake,  and then we can change that around,  so that's the brilliance of having some overscan,  is that you're not g...

**Frame:** tutorials\frames\green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus\frame_013.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
