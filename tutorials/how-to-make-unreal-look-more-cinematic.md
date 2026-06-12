---
title: How To Make Unreal Look More Cinematic
source: YouTube
url: https://www.youtube.com/watch?v=doUDJFKLyZs
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4 & 5"
tags: [cinematics, camera, frame-rate, motion-blur, depth-of-field, film-back, focal-length, aspect-ratio, color-grading, william-faucher, beginner, intermediate, ue4, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-unreal-look-more-cinematic/
frame_count: 0
---

# How To Make Unreal Look More Cinematic

**Source:** [YouTube](https://www.youtube.com/watch?v=doUDJFKLyZs)
**Author:** William Faucher
**Duration:** 29m6s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back. The topic of today's video is cinematics.  Or rather, how to make your renders more cinematic.  Now I know that cinematic is a term that's kind of thrown around a lot.  It's often, it may or may not be misused.  For the sake of this video, when I say cinematic, I mean something that's very filmic.  Something that's very movie-like. Something that you would actually believe yourself seeing in a movie theater.  Right? It's that magical feeling you get when you see this beautifully, well lit, well composed shot.  That just makes you just stare in awe.  And that is what we want in our renders.  And fortunately, it doesn't necessarily take all that much to make your shots go from kind of mediocre to wow.  So let's jump right in.


### Part 1 [0:53]
**Transcript:** So let's start off with the first thing.  There is one thing that is very often overlooked in game engines like Unreal and Unity.  And that is frame rate.  So because Unreal is a game engine, it has at least up until recently been used mainly by game artists.  And in games, the higher the frame rate, the better.  Get that sweet, sweet 60 FPS or even 120 FPS.  The high frame rates have been prized by gamers time and time again.  So that's why you see a lot of shots rendered out of Unreal on art stations and social media  that have been rendered in this smooth 60 FPS.  And while it can look nice, it's not cinematic in the slightest because it tends to look like a soap opera or worse a video game cutscene.  So here's the dirty secret 24 FPS.  No more, no less.  For the love of all that is holy on this good earth, do not render in 48 or 60 or even 120 FPS.  Okay?  So 99% of movie that there are shot in 24 FPS for a reason.  And that's because of motion blur.  Motion blur when shot at 24 FPS and assuming you're using the 180 degree shutter rule will provide the most natural and cinematic looking motion blur you can possibly get.  So in real life with a real camera, shutter speed is what...


### Part 2 [4:43]
**Transcript:** So next time it's how film back in the field work together.  These two things can make your shots really pop.  This is yet another little thing that game artists tend to overlook because depth of field in video games tends to be a little bit annoying and it's  promptly discarded.  But do not overlook how powerful depth of field can be.  Just think of any movie where you have a close up of two characters.  Diff the field is very often used creatively here.  And honestly, depth of field is a great way to just hide all the garbage in your background.  Depth of field is awesome for that.  But now, what's film back?  Film back is kind of a term that you might not be familiar with.  Film back is essentially the sensor of your camera.  So if you imagine like an actual DSLR or a mirrorless camera, the sensor itself, that's what we call the film back.  And you can choose the size of this in Unreal.  This is also how you set your aspect ratio.  In general, at least in real life with a real camera, the larger the sensor, the better it is.  This is why full-frame cameras and medium-former cameras are so sought after because they have a much bigger sensor.  So go ahead and play with the film ba...


### Part 3 [7:35]
**Transcript:** And that brings me to my next point, focal length.  So because 35 millimeter is the default, they are wildly overused.  They're boring.  It's not exciting.  When you want to get really close to your subject, you just get this weird distortion and it doesn't look very good.  It's not flattering to the human face to have a 35 millimeter lens, especially when you get up close.  So go long, go set it to 85 millimeters, set it to 200 millimeters.  And I have another example right here where I compare like a 150 mil lens and a 35 mil lens.  And the difference is just pretty shocking.  So in this case, let's take a look at our focal length.  So right now we're used in this camera.  We have a focal length of 150 millimeters.  Okay, and if we get this very tight shot, very close up, very personal look and with a very nice blurred out that the field.  But look at the aperture.  The aperture is F10.  If I were to set this to 2.8, which is the default, the background is even more blurry.  Okay.  I'm going to leave this at F10 because that's still looked that I wanted.  But let's create a brand new camera.  I'm going to duplicate this camera here.  So we're going to call this one camera wide.  ...


### Part 4 [12:19]
**Transcript:** Most movies we see nowadays are in a format called 2.35 to 1.  235 to 1 is the super wide cinema scope aspect ratio that we're very used to seeing.  You've probably seen it a lot.  You know, it's the black bars and the top and bottom of the frame.  This is a very popular look.  I'm personally I'm a sucker for the 2.35 look.  I love it.  I put it I use it in almost all my render just because I think it looks so awesome.  Now the reason why I think having the aspect ratio is so appealing is because  we instantly have the association with movies.  We've seen it in films.  We've seen it on TV.  If the immediate association you have with it, right?  Does this mean that a movie has to have the 2.35 to 1 aspect ratio for it to be cinematic?  Of course not.  No, I mean, you can find some amazing looking film that have been in 4.3 or 69.  What have you?  2.35 to 1 is just what's popular in trendy nowadays.  Personally, I love it.  But it's up to you.  It's kind of one of those little extra things that are really easy to change and  do or add to your frame.  You can just add to black bars on top of your thing and it's going to kind of help a little bit.  So just because you've added those bl...


### Part 5 [13:54]
**Transcript:** You get the point.  Now the last part of this video involves poke production.  And this is quite easily the most important, most overlooked and most underrated part of this entire process.  I understand the allure of getting everything right in unreal,  getting everything right in your render, hit the render button,  post our station call the day,  but you're shooting yourself in a foot.  When you hit that render button in unreal and you get your frames out,  you're only halfway done.  Anyone who's ever worked in VFX knows that the worth the compositors do is the stuff of legends.  I can't tell you how many times I sense stuff to the render farm and, you know,  they were decent looking renders,  but after I go through the converse and the poke production and color correcting and the colorist,  when I see that final result in theaters or even in our daily meetings,  I am constantly just shocked at the work that poke production people do.  Okay.  Color correcting and editing your footage and post is so important.  God, you really need to start doing this if you haven't already.  It is so critical to making your shots go from mediocre to amazing.  Okay.  And fortunately, there's not t...


### Like & Subscribe, and Thanks! [28:43]
**Transcript:** And that folks concludes this week video.  If you've done everything we've covered here,  including the film back, the death of field,  the frame rate, motion blur, color grading and post production,  if you do all of those things,  your renders should be one step closer to looking a lot more  cinematic than they did beforehand.  So I hope this helped you out.  Thanks so much for watching guys,  and I'll see you all next week.



---

## Structured Notes

### Core Technique
Five fundamentals for making Unreal renders look cinematic: 24 FPS + 180° shutter rule for organic motion blur, full-frame film back for proper sensor feel, long focal lengths (85–200mm) for cinematic compression, 2.35:1 aspect ratio, and post-production color grading in DaVinci Resolve.

### Summary
29-minute cinematic fundamentals video covering the most common mistakes game-artist-turned-filmmaker Unreal users make. Each of the 5 topics is a dimension that separates game-looking renders from film-looking renders. The most critical insight: rendering is only halfway done — post-production color grading is what makes the real difference between mediocre and cinematic. Shooting in 24fps is the single biggest and easiest win.

### Key Steps

**1. Frame Rate — 24 FPS (Most Important)**
- 60 FPS = soap opera effect / video game cutscene
- 24 FPS = cinematic, natural motion blur at 180° shutter
- 180° Shutter Rule: shutter speed = 1 / (2 × fps) → 24fps = 1/48s shutter
- In Unreal: Camera → Shutter Speed = 48 (for 24fps), OR use Motion Blur Amount instead
- DO NOT render at 48, 60, or 120 FPS for cinematic work
- Only exception: slow-motion footage shot at higher fps, played at 24fps

**2. Film Back — Sensor Size**
- Default Unreal camera sensor is small → "video camera" look
- Change: CineCamera Actor → Filmback Settings → choose Full Frame DSLR (36×24mm) or Super 35
- Larger sensor = shallower DOF at equivalent aperture + wider field of view at same focal length
- Film Back affects how much of the scene fills the frame and overall perspective feel

**3. Focal Length — Go Long**
- 35mm is Unreal default → overused, boring, distorts faces when close
- For close-ups: use 85mm minimum, 150mm–200mm for portraits
- Longer focal = background compression (background appears closer) → cinematic look
- To get subject large in frame at 150mm: back the camera up further
- Combined with large aperture (f/2.8–f/4): very shallow DOF, beautifully blurred background

**4. Depth of Field — Use It Creatively**
- DOF hides background flaws, focuses viewer attention
- CineCamera → Current Focal Length + Aperture + Focus Distance
- F/2.8 = very shallow; f/10 = sharper background
- DOF in game dev was often disabled (annoying) — in cinematics, it's essential
- For close-up portraits or product shots: exaggerated shallow DOF looks professional

**5. Aspect Ratio — 2.35:1 Cinema Scope**
- Most cinematic films: 2.35:1 (also written as 2.39:1)
- In Unreal: add black bars in Post Process Material OR crop in Resolve
- Instantly triggers "movie theater" association in the viewer
- Alternative: 1.85:1 (widescreen), 4:3 (classic), 1.78:1 (16:9)

**6. Post-Production (Most Underrated)**
- Color grading in DaVinci Resolve is essential — rendering is only 50% of the work
- William's workflow: render EXR (tone curve off) → Resolve → ACES convert → grade
- Post: contrast, vignette, chromatic aberration, film grain, color temperature shifts
- VFX compositors in production are legendary for how much they improve renders

### UE Systems / Blueprints / Settings

**CineCamera Actor Settings:**
```
CineCamera Actor:
  Filmback → Sensor Width: 36 mm (Full Frame DSLR)
  Filmback → Sensor Height: 24 mm
  
  Current Focal Length: 85–200mm (not 35mm default)
  Current Aperture: 2.8 (shallow DOF) or f/8 (sharper background)
  Current Focus Distance: [distance to subject]

Sequencer → Camera cut track → right-click → Pilot:
  Ensure CineCamera is used (not generic Camera Actor)
```

**Motion Blur / Shutter:**
```
// 180° Shutter Rule for 24 FPS:
CineCamera → Shutter Speed: 48  // = 1/48s = half of 1/24s
// OR
Post Process Volume → Motion Blur Amount: 0.5 (default) — represents 180° shutter at 24fps

// For renders: ensure MRQ doesn't override motion blur to 0
MRQ → Game Overrides → Motion Blur: leave default (don't set to 0)
```

**Aspect Ratio (2.35:1):**
```
// Method 1: Crop in DaVinci Resolve (most flexible)
// Method 2: Post Process Material with black bars on top/bottom

Resolution 4K with 2.35:1:
  3840 × 1634 (exact 2.35:1 crop at 4K width)
```

### Difficulty
Beginner to Intermediate — conceptual knowledge more than technical setup

### UE Version
UE 4 & 5 (concepts apply to any version)

### Tags
cinematics, camera, frame-rate, motion-blur, depth-of-field, film-back, focal-length, aspect-ratio, color-grading, william-faucher, beginner, intermediate, ue4, ue5

---

## Related Entries
- `tutorials/the-2026-unreal-engine-to-davinci-resolve-guide---aces-srgb.md` — Color grading in Resolve
- `tutorials/the-2025-guide-to-rendering-in-unreal-engine-5.md` — 2025 rendering guide (MRQ settings)
- `tutorials/how-to-add-camera-shake-in-unreal-engine.md` — Adding procedural camera shake
- `references/cinematics-pipeline.md` — Cinematics pipeline reference
