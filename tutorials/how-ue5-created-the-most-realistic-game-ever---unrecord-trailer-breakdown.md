---
title: How UE5 Created the Most Realistic Game Ever - Unrecord Trailer Breakdown
source: YouTube
url: https://www.youtube.com/watch?v=VIY1fzRahJY
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [breakdown, realism, camera-simulation, lumen, post-process, ies-lights, dynamic-range, fisheye, body-cam, niagara]
extraction_status: complete
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
**Transcript:** That's fired, that's fired.  Believe it or not, what you're seeing  is not body camera footage.  It's actually a new gameplay trailer from Unrequires,  a first-person shooter unlike anything we've ever seen before.  Using Unreal Engine 5 and the power of Lumen  to make a photo-realistic game like something Twitter  has never seen, and I think that's why I got over 50 million views  in just a single day because it's clear we're reaching  in new heights for photo-realism when it comes to real-time rendering  and video games.  What's up?  My name's Josh Tunin, and for the last eight years  I've been working as an artist and supervisor  on Hollywood films, on movies like Star Wars,  Dungeons and Dragons, and across the Spider-Verse.  And I've been using Unreal Engine 5 on set  and to make films of my own.  And today I want to break down exactly why this looks so real,  and what you can take from this video  to make your games and your films out of Unreal.  Look at this good.  So let's jump right in.  So right at the beginning, something about this  already screams realistic, and off the bat  I can tell you there's two reasons why.  And I think everything I've noticed in this  is really going down to recreating the crapiness  of a body camera to a perfect level.

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_000.jpg

### Fisheye Distortion [1:15]
**Transcript:** The first one is the fisheye lens that they're applying to this.  It's pretty extreme here if you look at how much  the top of this building is arcing.  This is something that's easy to forget  when you're inside a game engine the entire time.  You're going to have perfect boxes, perfect geometry everywhere.  You would expect just a straight line  and immediately they start to break that.  If you want to do this yourself in Unreal,  you have to create a post process material  and then assign that material in your post process volume  that's in your scene.  I won't get too in depth because there's some other tutorials  out there, but I've included the material graph  of an example here to do the same exact fisheye distortion.  And there's also a free download in the description.  And another thing to notice is auto exposure

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_001.jpg

### Auto Exposure [1:58]
**Transcript:** and the dynamic range of the camera.  So what do I mean by that?  Exposure is just how much light you're letting into the camera's sensor.  And you're adjusting how much light you're letting in  so that you can either see the shadows or the highlights.  So when you're outdoors, you're going to expose  for a much brighter light like the sun.  But as soon as he walks in here,  all of that light is going to go away inside the building.  And then the camera would have to compensate  to expose for the shadows so we can see everything.  This happens with our own eyes all the time.  The human eye actually has about 18 to 20  stops of dynamic range.  And that just means that we have 18 different thresholds,  different levels that our eye can adjust to to compensate  for the brightest brights of something like the sun  and the darkest shadows like a room with no light inside of it.  But the crappier the camera,  the lower that dynamic range is going to be.  That means is that at a certain point,  the sun is going to have to clip  and there's going to be no more information  because we have this limited dynamic range.  We can't see the brightest brights  and we also can't see the darkest shadows.  You'll see that the sky and the sunlight is pure white.  It's completely clipped and the shadows are actually completely black.  It's a subtle thing, but we'll see throughout the course  of this video how the auto exposure of the camera  slightly shifts in different ways.  But because we're in this really thin threshold  in this thin band of dynamic range,  that has to fluctuate really dramatically.  And it's something that you'll see in body camera footage  happening subconsciously and they're just mimicking it  perfectly here, which is why it just looks so real  and believable.  We're also on a cloudy day.  I can tell that because there's no hard shadows  on the ground or anything like that.  And an overcast day is typically going to be darker  than a really sunny day, obviously.  But even on an overcast day like this,  if I just step through the frames here,  watch how the sky gets darker  and the exposure starts to shift down.  And as that exposure shifts down,  we actually reveal more trees.  The sky was clipping so much that it was actually hiding  all of these really thin trees and branches in the background.  So let's go into slow motion as he walks through the door here.  So as he walks in, you can see already  the ground is starting to get brighter  as the auto exposure is shifting.  As he goes inside further into these darker shadowy areas,  the sunlight gets brighter.  And that's because of the auto exposure of the camera here.  So another thing that makes us feel extremely believable

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_002.jpg

### Camera Movement [4:33]
**Transcript:** is the camera movement.  One thing in particular that's interesting here  that I don't see in games like Call of Duty  or Titanfall is the amount of rotation of the camera.  It's actually rolling left and right,  which is a thing that kind of just takes you off-kilter,  doesn't let you really focus in  if you're trying to aim and get really precise  and something competitive like those games.  But when this is more about the experience  and recreating real life situation with body camera footage,  so now I'm sure you're wondering  how can I create this handheld camera animation at home?  Well, there's actually a really simple answer,  unreal created an iPhone app called Unreal Remote,  where you can use your iPhone to create tracking data.  It really adds to that and adds a randomness  that you don't typically see in a video game.  The hands are not centered in the middle of the frame,  which again, it just adds to the randomness,  but also the realism.  Shot fired, shot fired.  The textures here are obviously super detailed.  You get all these really nice and detailed spec hits right here.  The specular here is coming because there's a window,  this really bright light behind them,  so we can feel that reflection  of this really bright light behind us.  But at the same time, look at how dark his hands are.  There's literally no information in this section here  because it's a black suit, a black gun.  This also has to be one of the most realistic recoil  this gun here drives the hands to move  all around in different places, which is very believable.  There's also no muzzle flash here,  which is really interesting.  If you've ever shot a gun,  you typically aren't actually going to see a muzzle flash.  It's a thing that you see in Hollywood movies.  It looks really cool, a nice big explosion  at the front of the gun,  but when you have a handgun, something like this,  like a 45 caliber,  there's not going to be a gigantic muzzle flash  like you might see with more military grade rifles.  And you can see how the smoke travels  from the barrel of the gun,  and as he moves forward, the smoke travels behind him.  It's not just a 2D card that kind of floats out there,  like you might see in Visual Effects.  Each little puff of smoke is traveling back in space,  which is definitely a Niagara simulation.  They're very simple, but very effective  when you combine the character animation,  the movement of the camera,  and throw everything together in the scene.  Another thing here that's interesting,  but pretty subtle,  is a hone of light from the flashlight that he has.  There's an actual shape to this,  and they found a way to take off the CG stink  from something like this, like a spotlight,  which typically would have a very uniform cone coming out.

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_003.jpg

### Lighting [7:06]
**Transcript:** If you use an IES light,  this is a pretty typical in Visual Effects,  and they have this in Unreal Engine as well.  You can upload real life profiles,  which will shape the direction of the light,  and how that is sent out,  so that it's not a uniform soft cone of light,  but it mimics the glass coating in front of a flashlight,  which is typically gonna be pretty uneven,  and because of that, you'll have spots in the middle,  which are really focused light, so it's brighter,  and it'll have different rings at different depths,  depending on where the glass would be.  Just having this in here doesn't have to be perfect,  but it adds that little bit of randomness,  and helps make it feel believable.  So in extreme shadowy areas like this,  where there's absolutely zero information  on the entire right half of the screen here,  now you'll see that this flashlight,  which felt pretty dim,  now this spotlight is actually overexposing,  and blowing out the camera here,  just like the sky was earlier,  which again, just gives us a clue to how dark this is,  makes it feel very, very believable,  so that what's clipping here is also clipping  just like the sky, but again,  because we have such a limited dynamic range in this camera,  as we walk into the next room, you'll see  that this flashlight should get darker,  and it will, because they're doing their job on this one.  And if you were wondering,  hey, wait, is this real footage, is this a video game?  The few areas where you can just start to see,  it not quite mimicking real life,  is just in areas like this,  and you don't quite get a sense of shadow underneath,  characters interact with shadows differently,  they're just not as dynamic,  Lumen just takes a little bit of time to catch up  to movable actors, like these characters,  I'm nitpicking at this point,  but again, just this is something to learn from here.  But something, again, that just really makes us feel  believable is the reflection here,  and the fact that this reflection is clipping as well.  Something about Unreal is that the scene exists  in high dynamic range,

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_004.jpg

### Dynamic Range [9:02]
**Transcript:** so basically all the light is being calculated  in full dynamic range,  so all the information is there,  and then basically we're compressing it  in our post-processing to make it appear  like this body camera footage.

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_005.jpg

### Materials Geometry [9:17]
**Transcript:** And now if we wanna look at the materials and the geometry,  a lot of these surfaces are very rough,  meaning that they have no reflection.  So when you're looking at something like a brick  or a wall, or something that's very dusty,  which is a lot of this room,  even walls will typically have some amount of specular,  but when they're just coated with dust,  like an abandoned building would be for, you know,  let's say five to 10 years plus,  there's gonna be so much dust matting down the walls.  We get some areas where we have these reflections  close to very, very bright light sources,  where we do see a hit of reflection,  there's puddles on the ground,  but right next to that we can see this is very, very reflective,  and then the rest is completely matte.  Reflections are something that are pretty tricky  to get right in real time.  Lumen does a good job, but matte surfaces, rough surfaces,  generally look better.  I think it's safe to assume that almost all of the ground rubble  is photogrammetry, not Quixel, in this case,  although I'm sure they're using some assets here and there,  but I would definitely say just based on the amount of resolution  that we're getting out of a lot of the ground detail,  that they're definitely still using photogrammetry,  just like Quixel is with their assets.  And that is unrecorded.  So hopefully that helps you have a better understanding  of how cameras work, how we can recreate those cameras  in a digital world inside of Unreal Engine.  So like the video if you learned something,  go wish list the game on Steam,  and if you want to learn more about Unreal Engine,  VFX and filmmaking, hit subscribe on my channel,  and I'll make more breakdowns  just like this in the future.  Thanks for watching, I'll see you next time.  Peace.

**Frame:** tutorials\frames\how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown\frame_006.jpg


---

## Structured Notes

### Core Technique
Breakdown of six realism techniques from the Unrecord game trailer (body-cam FPS using UE5): fisheye lens post-process, limited dynamic range auto exposure simulation, physical camera movement with roll, IES flashlight profile, Niagara smoke particles, rough photogrammetry materials. Core insight: UE renders in full HDR internally, then post-processes to simulate a low dynamic range body cam — "crapifying" the render is what makes it photorealistic.

### Summary
10-minute breakdown by Josh Toonen analyzing why the Unrecord game trailer (50M views in one day) looks like real body cam footage. Six identified techniques: (1) extreme fisheye distortion via post-process material; (2) limited dynamic range auto exposure — sky clips to white, shadows to black, exposure shifts when crossing indoor/outdoor; (3) camera rolls left/right + off-center hands + Unreal Remote iPhone app for physical randomness; (4) IES flashlight profile for uneven realistic beam; (5) Niagara 3D smoke particles from gun barrel; (6) rough photogrammetry surfaces for abandoned building realism. UE renders in full HDR then compresses to simulate body cam limited dynamic range.

### Key Steps
1. **Fisheye lens** — create post-process material with barrel/fisheye distortion math → assign to Post Process Volume in scene; tutorial files include example material graph + free download
2. **Auto exposure (limited dynamic range)**:
   - Body cams have ~5 stops vs human eye's 18-20 stops
   - Sky + sunlight clips to pure white; deep shadows clip to black
   - Auto exposure shifts compensation as camera moves indoor/outdoor → visible exposure shift
   - In UE: Post Process Volume → Auto Exposure settings; tune min/max EV to simulate the narrow band
   - Overcast day = no hard shadows; exposure still shifts with environment light level changes
3. **Camera movement** — body cam rolls left/right (not just pitch/yaw); adds disorienting realism; hands are not centered; use **Unreal Remote** (free Epic iPhone app) to generate physical camera tracking data with real-world randomness
4. **IES flashlight**:
   - Import real-world IES light profile (light distribution data file)
   - Apply to spotlight → flashlight cone becomes non-uniform (brighter center, rings from glass imperfections)
   - In dark rooms: flashlight clips/overexposes consistent with camera's limited dynamic range
5. **No muzzle flash** — realistic choice: small caliber handguns have minimal muzzle flash; only Hollywood exaggerates this
6. **Niagara smoke** — gun barrel smoke is 3D Niagara particle simulation; each puff travels backward in 3D space as player moves forward (not a 2D card/billboard)
7. **Rough materials** — abandoned building = surfaces coated in dust → near-zero specularity; some puddles = high specularity contrast; reflections in windows also clip consistent with dynamic range
8. **Photogrammetry ground** — ground rubble texture detail level suggests photogrammetry (not just Quixel); real scan geometry for maximum ground resolution
9. **HDR → SDR compression** — UE renders everything in full HDR internally; post-process compresses/clips to simulate body cam's narrow dynamic range → this is the key technique: don't limit your lighting, limit your camera's ability to perceive it

### UE Systems / Blueprints / Settings
- **Post-process material (fisheye)** — custom material with barrel distortion UV math; assign to Post Process Volume; free example in tutorial description
- **Post Process Volume → Auto Exposure** — min/max EV settings; tune to simulate limited body cam dynamic range; exposure shifts automatically with environment luminance
- **Unreal Remote** — free Epic iPhone app; generates physical camera tracking data with real-world device motion; adds roll, micro-jitter, and physical randomness to in-engine camera
- **IES light profile** — real-world light distribution data file; import to UE → apply to spotlight → replaces uniform cone with measured non-uniform distribution from actual flashlight glass patterns; available free online for many fixture types
- **Niagara smoke particles** — 3D volumetric particle emission from gun barrel; each particle has velocity and persists in world space as player moves; use Mesh Renderer or Sprite Renderer with low count for subtle effect
- **Dynamic Range simulation** — Lumen renders full HDR; Post Process Volume compresses to SDR clip range to simulate camera limitation; sky overexposure + shadow underexposure = believable body cam effect
- **Lumen limitation** — movable actors' shadows can lag slightly behind the character; visible in close inspection; ambient shadowing on characters near walls not as tight as static baked lighting
- **Photogrammetry assets** — ground rubble in Unrecord appears to be photogrammetry (fine surface variation + real edge micro-geometry); Quixel also photogrammetry-based but Unrecord may use custom scans

### Difficulty
Reference/Analysis. Not a step-by-step tutorial — a breakdown for understanding what to replicate. Implementing all techniques requires: post-process material skills, exposure tuning, IES file import knowledge, Niagara basics.

### UE Version
UE5 (Lumen-powered; UE5.0 era based on game's development timeline)

### Tags
breakdown, realism, camera-simulation, lumen, post-process, ies-lights, dynamic-range, fisheye, body-cam, niagara

---

## Related Entries
- `how-to-make-unreal-look-more-cinematic.md` — complementary take on camera simulation techniques (focal length, DoF, film grain)
- `how-to-actually-improve-your-films-vfx-dune-in-unreal-5.md` — cinematic camera secrets including noise tracks
- `how-to-add-camera-shake-in-unreal-engine.md` — CameraShakeBase BP for procedural camera movement
- `lumen-explained---important-tips-for-ue5.md` — Lumen GI system used in Unrecord
