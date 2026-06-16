---
title: Unreal Engine for Filmmakers - Cinematic Camera Settings & Setting up Virtual Camera
source: YouTube
url: https://www.youtube.com/watch?v=gFO0qhdLKec
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came/
frame_count: 9
---

# Unreal Engine for Filmmakers - Cinematic Camera Settings & Setting up Virtual Camera

**Source:** [YouTube](https://www.youtube.com/watch?v=gFO0qhdLKec)
**Author:** Boundless Entertainment
**Duration:** 14m44s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** What's going on guys Sam here and in today's tutorial I'm going to go over how you can make your renders as cinematic as possible coming out of unreal engines specifically for filmmaking so I already did kind of a specific episode on this on path tracing but today I want to go over just like general techniques that you can use to make your renders look as cinematic as possible.  So let's get right into it so the first thing we're going to talk about here is setting up your camera so you guys can see we have this shot here and we just kind of slowly push in and we.  Rack focus into the background so you can see our background.  And that's pretty much what we got here so very basic shot but lots of detail and lots of things going on the foreground background I have a huge city in the background okay so this is one technique.

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_000.jpg

### Lens choice [0:50]
**Transcript:** That you can use to kind of make your scenes look a little more cinematic per se using a bit of a longer lens can actually help you kind of get that cinematic look a lot of films are shot on a little bit longer lenses that's kind of changing now but traditional the films are often shot on slightly longer lenses and what's great about Unreal Engine is that you have a lot of control over how you're going to be framing your shot and also capturing your scene so you can kind of hide shortcomings on Unreal Engine.  By doing things like using slightly longer lenses and what that's going to do is using a longer lens collapses the depth in your scene a bit so if I set this out to like to a wider field of view for example if you go back to 24 millimeters we can actually see a lot more depth and we can see like you know how far away this is how far away these buildings are from us and if I turn off the exponential height fall care because that's also helping.  So we can see much better how far these objects are away from us okay so that's certainly a look that you can go for if we go back to our 47 millimeters here now we've collapsed a lot of this depth in our scene can see a lot of detail ...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_001.jpg

### Setting up the Camera [2:24]
**Transcript:** I'm just going to drag one out here into the scene okay drag this back approximately where we want our camera to be all right now what we can do is go into our camera and we're going to pilot it and we can position it basically how we want to this isn't bad we're at 35 millimeters we're losing a lot of what made that other camera look pretty good so what we can do is go down here and we go into our camera settings and now the first thing

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_002.jpg

### Filmback [3:07]
**Transcript:** them to talk about here is our film back so we have 16 by nine digital film right now and that's decent but if we want to get a little bit more sensor size we can change it to 16 by 90 s l r and now as you can see that's made our field of view much wider  okay so let me just quickly explain the field of view and sensor width versus focal length relationship is in the real world when we're shooting on a digital cinema camera you have full frame sensors you have super 35 sensors you have micro 4th  3rd sensors and there are several others but those are pretty much the three main ones the difference is the size of the sensor so if you're shooting on a micro 4th  sensor and you're using a 35 millimeter lens you're going to have a much more cropped image than if you're using a full frame sensor just to demonstrate that I'm going to make the size of this  sensor really small okay so for demonstration purposes this isn't mathematically accurate but we'll say we'll say that that is the size of a micro 4th  3rd sensor we're on the same focal length of lens we're on a 35 millimeter lens right here and our aperture is 2.8 we're going to actually take this down to 1  okay so aperture is 1 so y...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_003.jpg

### Cinematic Camera Settings [5:39]
**Transcript:** change our aperture back to 2.8 or so so going to our post process and you can also do this with the post processing volume so that you  don't have to apply it to all the different cameras in your scene and you'll just have the same look for each camera but I'm just going to do it in this particular camera  so you guys can see and then you can change it for each different shot if you have different shots in the scene so what I like to do sometimes is use this  bloom feature and that's just going to give us these really nice looking this nice looking highlight roll off here and you know obviously you can go way too far  with it but if we just go back and then kind of bring it up just a little bit somewhere around like three or so that's going to look really nice and it's going to give us a  bit more of a filmic look it's going to have that bit of glow to it which is nice that looks good and we can go down here to our chromatic aberration sometimes I like to add a little bit of this  nothing too crazy obviously that's way too far so maybe 0.5.4 is going to give us just a little bit of that distortion which can look kind of nice looks a little more  organic you know we can go down int...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_004.jpg

### Fog [7:50]
**Transcript:** cinematic so the next thing is fog so what we can do when we're not in path tracing mode is we can go into our exponential height fog so we'll take  exponential height fog and we're just going to drag it into our scene and immediately you can see what that's doing is as a DP  what you always want to do is add as much depth to your scene as possible okay one way to do that is by using a certain type of lens  which we already talked about another way to do that is by adding atmosphere particles and other elements in the air to your scene that are going to give the audience details as to where things are located in your scene in terms of the depth  so now you can see this building looks dark this building looks brighter and as we go back the buildings look more and more in the distance because you can see there's more fog in front of them  so that's just a really simple way and we can go into our exponential height fog you can increase our fog density a little bit which I like to do maybe we'll go up to point one see what that does so that looks really nice you know we can change the height  fog so if you don't want it to be all the way up into this guy so if you want to see some of t...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_005.jpg

### Frame Rate [10:50]
**Transcript:** another big thing here is we talked about motion blur already but in terms of getting a cinematic look what we want to do is set this to 23.976 frames per second a lot of game developers make the mistake of  rendering at 60 FPS 100 FPS 120 FPS that's not really helpful unless you're doing slow motion you want your your shutter angle at 180 degrees when you're shooting at 23.976 frames per second if you shoot something or render something in a higher frame rate from Unreal Engine when you play it back it's not going to have any motion blur for gaming that's generally a good thing you know people don't really like motion blur when they're trying to game in terms of cinematics that is not a good idea  because your shot is going to essentially look like a video game cutscene or even just straight out of a video game and that's not what you want you want it to look like a movie and films are shot at 24 frames per second you're getting a certain amount of motion blur when you're shooting at 24 frames per second at 180 degree shutter angle and if you increase the frame rate your footage is going to look really really smooth and it's not going to have that nice motion blur just keep that i...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_006.jpg

### Composition [12:03]
**Transcript:** back into our scene gives us information about where things are in our scene and it also shows the depth of our scene so go back to our camera here we see this is right along the side and it's going back into our scene that's just showing us how far each thing is in relation to where we are so things like that shooting along walls shooting along objects that lead back into your scene is a great way to show a little more depth and it's a good compositional tool so the next thing is we have our foreground element we have something leading into our background we have our mid  ground element right here okay now let me show you guys what that does if I just get rid of this look how flat the scene looks in comparison you know because we just we have our foreground elements and then we just have our background you know this is our far background in the distance now if I turn this on suddenly our scene is much more interesting this gives us a lot more depth information about our scene and it also gives us something to kind of focus on like another focal point of our image now it gives us a lot more visual interest we're also  kind of mixing things up because we have these lines going up an...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_007.jpg

### Final Thoughts [13:52]
**Transcript:** religion go check out the path tracing tutorial that I did as well as the tutorial I did on how to use fog with path tracing it's a really powerful tool and it's  something that's really nice coming out of Unreal Engine 4.27 you can just see right there I changed it and it gives you so much more realistic results so don't  forget to check that out I'm working on a lot of new content for you guys trying to come out with filmmaking and  Unreal Engine course so if that is interesting to you guys make sure you subscribe once again don't forget to  like this video comment any future videos that you'd like me to do and also subscribe to the channel  that really helps me out thank you guys for watching and have a good one

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came\frame_008.jpg


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
