---
title: How UE5 Created the Most Realistic Game Ever - Unrecord Trailer Breakdown
source: YouTube
url: https://www.youtube.com/watch?v=VIY1fzRahJY
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown/
frame_count: 7
---

# How UE5 Created the Most Realistic Game Ever - Unrecord Trailer Breakdown

**Source:** [YouTube](https://www.youtube.com/watch?v=VIY1fzRahJY)
**Author:** Josh Toonen
**Duration:** 10m52s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** That's fired, that's fired.  Believe it or not, what you're seeing  is not body camera footage.  It's actually a new gameplay trailer from Unrequires,  a first-person shooter unlike anything we've ever seen before.  Using Unreal Engine 5 and the power of Lumen  to make a photo-realistic game like something Twitter  has never seen, and I think that's why I got over 50 million views  in just a single day because it's clear we're reaching  in new heights for photo-realism when it comes to real-time rendering  and video games.  What's up?  My name's Josh Tunin, and for the last eight years  I've been working as an artist and supervisor  on Hollywood films, on movies like Star Wars,  Dungeons and Dragons, and across the Spider-Verse.  And I've been using Unreal Engine 5 on set  and to make films of my own.  And today I want to break down exactly why this looks so real,  and what you can take from this video  to make your games and your films out of Unreal.  Look at this good.  So let's jump right in.  So right at the beginning, something about this  already screams realistic, and off the bat  I can tell you there's two reasons why.  And I think everything I've noticed in this  is really...

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_000.jpg

### Fisheye Distortion [1:15]
**Transcript:** The first one is the fisheye lens that they're applying to this.  It's pretty extreme here if you look at how much  the top of this building is arcing.  This is something that's easy to forget  when you're inside a game engine the entire time.  You're going to have perfect boxes, perfect geometry everywhere.  You would expect just a straight line  and immediately they start to break that.  If you want to do this yourself in Unreal,  you have to create a post process material  and then assign that material in your post process volume  that's in your scene.  I won't get too in depth because there's some other tutorials  out there, but I've included the material graph  of an example here to do the same exact fisheye distortion.  And there's also a free download in the description.  And another thing to notice is auto exposure

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_001.jpg

### Auto Exposure [1:58]
**Transcript:** and the dynamic range of the camera.  So what do I mean by that?  Exposure is just how much light you're letting into the camera's sensor.  And you're adjusting how much light you're letting in  so that you can either see the shadows or the highlights.  So when you're outdoors, you're going to expose  for a much brighter light like the sun.  But as soon as he walks in here,  all of that light is going to go away inside the building.  And then the camera would have to compensate  to expose for the shadows so we can see everything.  This happens with our own eyes all the time.  The human eye actually has about 18 to 20  stops of dynamic range.  And that just means that we have 18 different thresholds,  different levels that our eye can adjust to to compensate  for the brightest brights of something like the sun  and the darkest shadows like a room with no light inside of it.  But the crappier the camera,  the lower that dynamic range is going to be.  That means is that at a certain point,  the sun is going to have to clip  and there's going to be no more information  because we have this limited dynamic range.  We can't see the brightest brights  and we also can't see the darkest sha...

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_002.jpg

### Camera Movement [4:33]
**Transcript:** is the camera movement.  One thing in particular that's interesting here  that I don't see in games like Call of Duty  or Titanfall is the amount of rotation of the camera.  It's actually rolling left and right,  which is a thing that kind of just takes you off-kilter,  doesn't let you really focus in  if you're trying to aim and get really precise  and something competitive like those games.  But when this is more about the experience  and recreating real life situation with body camera footage,  so now I'm sure you're wondering  how can I create this handheld camera animation at home?  Well, there's actually a really simple answer,  unreal created an iPhone app called Unreal Remote,  where you can use your iPhone to create tracking data.  It really adds to that and adds a randomness  that you don't typically see in a video game.  The hands are not centered in the middle of the frame,  which again, it just adds to the randomness,  but also the realism.  Shot fired, shot fired.  The textures here are obviously super detailed.  You get all these really nice and detailed spec hits right here.  The specular here is coming because there's a window,  this really bright light behind them...

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_003.jpg

### Lighting [7:06]
**Transcript:** If you use an IES light,  this is a pretty typical in Visual Effects,  and they have this in Unreal Engine as well.  You can upload real life profiles,  which will shape the direction of the light,  and how that is sent out,  so that it's not a uniform soft cone of light,  but it mimics the glass coating in front of a flashlight,  which is typically gonna be pretty uneven,  and because of that, you'll have spots in the middle,  which are really focused light, so it's brighter,  and it'll have different rings at different depths,  depending on where the glass would be.  Just having this in here doesn't have to be perfect,  but it adds that little bit of randomness,  and helps make it feel believable.  So in extreme shadowy areas like this,  where there's absolutely zero information  on the entire right half of the screen here,  now you'll see that this flashlight,  which felt pretty dim,  now this spotlight is actually overexposing,  and blowing out the camera here,  just like the sky was earlier,  which again, just gives us a clue to how dark this is,  makes it feel very, very believable,  so that what's clipping here is also clipping  just like the sky, but again,  because we have...

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_004.jpg

### Dynamic Range [9:02]
**Transcript:** so basically all the light is being calculated  in full dynamic range,  so all the information is there,  and then basically we're compressing it  in our post-processing to make it appear  like this body camera footage.

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_005.jpg

### Materials Geometry [9:17]
**Transcript:** And now if we wanna look at the materials and the geometry,  a lot of these surfaces are very rough,  meaning that they have no reflection.  So when you're looking at something like a brick  or a wall, or something that's very dusty,  which is a lot of this room,  even walls will typically have some amount of specular,  but when they're just coated with dust,  like an abandoned building would be for, you know,  let's say five to 10 years plus,  there's gonna be so much dust matting down the walls.  We get some areas where we have these reflections  close to very, very bright light sources,  where we do see a hit of reflection,  there's puddles on the ground,  but right next to that we can see this is very, very reflective,  and then the rest is completely matte.  Reflections are something that are pretty tricky  to get right in real time.  Lumen does a good job, but matte surfaces, rough surfaces,  generally look better.  I think it's safe to assume that almost all of the ground rubble  is photogrammetry, not Quixel, in this case,  although I'm sure they're using some assets here and there,  but I would definitely say just based on the amount of resolution  that we're getting out o...

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_006.jpg


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
