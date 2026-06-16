---
title: 3D TRACKED CAMERA FROM AFTER EFFECTS TO UNREAL ENGINE | TUTORIAL
source: YouTube
url: https://www.youtube.com/watch?v=v38O-9KTqx4
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial/
frame_count: 9
---

# 3D TRACKED CAMERA FROM AFTER EFFECTS TO UNREAL ENGINE | TUTORIAL

**Source:** [YouTube](https://www.youtube.com/watch?v=v38O-9KTqx4)
**Author:** Boundless Entertainment
**Duration:** 14m28s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** What's going on guys, it's Sam here and I have a tutorial for you guys today and what  we're going to be doing is taking a 3D tracked camera from After Effects and bringing it  into Unreal Engine.  So there's not a super direct way of doing this so we're going to have to go from After Effects  into Blender and then from Blender into Unreal Engine.  So you might be wondering why would I want to bring a camera from After Effects into Unreal  Engine, why not just put it into Blender and the answer is Quixel Megascans.  So like Blender, Unreal Engine is free to use and what's great about Unreal Engine is  that it has a direct connection with Quixel Megascans and what that is, it's a huge asset  library of photoscan 3D elements and these elements look incredibly realistic because  they're real objects that have been photoscaned into 3D space.  So you have access to thousands of these 3D assets.  So if you're using CGI in your film and you're trying to build a realistic world, this is  a great tool to help you to accomplish that.  And you can only get free access to these assets through Unreal Engine, you can't use Blender  with it, you will have to pay for the assets that you purchase w...

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_000.jpg

### Blender to Unreal Exporter [3:15]
**Transcript:** Xporter.  And also I'll put a link in the description of this video but it's very simple.  You're just going to download and install the add-on and you can then export your camera  from Blender into Unreal Engine.  Okay.  So back in After Effects now, we have our camera 3D tracked and you can now see all of the  points here that we have and it looks like it did a pretty nice job.  So what you want to do is find a surface that looks like it tracked pretty well.  So on our foreground, it looks like we can find a pretty good surface about right here.  So we'll click on these three points and then we'll right-click and hit Create Solid  and Camera.  And now that's going to create a solid and 3D space as well as a 3D camera.  So at this point, we can check it, render our scene and we can see it's following very  nicely to that point in 3D space.  So that looks really nice.  Go back here and select our 3D camera again and what I'm going to do is just find some  points a little further away.  Like these are perfect.  We'll click right here and we're going to create another solid.  Okay.  So the point of this is we're going to have a solid in the foreground and a solid a little  further aw...

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_001.jpg

### Blender [5:23]
**Transcript:** All right.  So we can jump over into Blender and now I'm going to quickly show you how to install this  add on.  So you're going to go edit and preferences and you're going to click on add on and you're  going to click install and now you're going to navigate to your A to blend plugin folder  that you downloaded and you're going to click A to blend to 8 dot P Y and you're going  to hit install add on.  Okay.  And so I've already done that and what you want to do quick is then hit cancel here.  I'm going to hit cancel.  You want to hit install and you want to search up in this box.  AE to blend and you want to make sure that this is checked.  So that's how you know it's activated and this little widget will pop up in the bottom  here.  Okay.  So now we've copied our position and orientation key frames from After Effects.  Now what we want to do is hit create camera.  Okay.  So now you can see way down here is our camera and I'm going to hit numpad the period.  That'll frame it for us.  So you can see it's not in the right place really.  I'm going to show you how to fix that in a minute.  But the next thing we want to do is jump back over into After Effects and now that we're  back i...

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_002.jpg

### Camera Properties [7:59]
**Transcript:** focal length is 50 millimeters.  Now I shot this at 35 millimeters which I know but if you're not sure what your focal length  was and you want to match it up nicely with your camera and after effects, you can go  into the camera settings and you can see it got 37 millimeters which is pretty close.  So we're going to go back into Blender and set this to 37.1.  So we want to make sure that everything is lining up properly.  So what we want to do is add our background image in and we can go down here to background

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_003.jpg

### Background Image [8:34]
**Transcript:** images and check that and we'll go over here to Movie Clip and we'll hit Open and then  I'll navigate to my Movie Clip and we'll click our Image Sequence and we'll open the  Clip.  So I'll just go to my Camera and we'll set our End Frame and it's the last frame that  we have data and now if we go to our Camera, you can see everything is working nicely and  what we can do is just repeat that action for the other two solids that will just give  us a little bit more context of what we're doing in Blender.  Okay so I've copied those other two solids into Blender and you can see everything is  looking really nice here.  Now what we want to do is you can see the grid is up here and it's way out of whack so  we need to fix that and we want this camera and like this solid right here to be on the  floor.  Alright so what we're going to do here is we're going to parent everything to this  ground plane and what we're going to do is click this Camera Transform, we're going to  hit this plane in the background, the plane in the foreground and then last we're going  to select the ground plane and we're going to hit Control P for parent and then hit Object.  So now we can move all of these object...

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_004.jpg

### Exporting this Camera into Unreal Engine [10:41]
**Transcript:** So in order to export a camera to Unreal Engine once you install the blender to Unreal  Engine add on you're going to go up here into the blender for Unreal Engine and what we're  going to do is get out of our active camera here we're going to hit zero.  So we're going to go into our hierarchy here and we're going to select our camera.  Okay.  Now it shows up here in this little box.  What we're going to do is set it to Export Recursive.  We can show we see our camera one is going to be exported and we can now export for Unreal

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_005.jpg

### Export for Unreal Engine 4 [11:17]
**Transcript:** Engine 4 and then we're going to hit Import Sequence and now what we can do is head over  to Unreal Engine.  Alright so I've got this scene here and on real that I've set up and this is the city  we're going to use.  I'm going to hit the tilde key bring up the Enter Console command we're going to hit Control  V and enter and then it's going to ask us to save the asset and you can call this sequence  whatever you want to call it.  So tutorial camera.  Okay.  Hit Save and now you can now see it moves nicely within our scene.  So there you go you have successfully imported your camera from After Effects all the way  into Unreal Engine 4 and now what you can do once you export this is you can bring it  back into After Effects.  Alright so we're back in After Effects and all I've done is imported my footage here.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_006.jpg

### Compositing [12:25]
**Transcript:** So I'm just going to do a little bit of compositing here and I'll show you what we're going  to end up with now with our process.  So I've just put the footage on the bottom and all I've done here is just set it a quick  mask on this area and we're just going to set the mask to add and then on this layer  I just copied my mask from the other comp the basic mask and then tightened it up a little  bit, feathered it out and then I just added this extract effect to it.  If you guys want a more in depth explanation of like some compositing tricks like this  I can do that for you just let me know in the comments.  And then I just added a couple of atmosphere effects from VideoCope pilot.  We can now turn off our tracking solids and I've done this all in the in log format so  it looks very flat right now you can do some nice grading to it in post and I'll show

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_007.jpg

### Final Shot [13:23]
**Transcript:** you guys the final shot here.  So there's your final shot and it's looking pretty good and we successfully taken our  camera from After Effects to Blender into Unreal and we're able to pull off this really  nice image pretty quickly and easily inside of Unreal Engine.  So I hope you guys found this tutorial helpful.  If you did let me know in the comments give a like and also subscribe to the channel for  more content like this.  I'm going to be coming out with a lot more videos, tutorials, cinematography techniques  and things like that.  Also check out my new film Gemini.  It's in process right now we've shot it and I'm just editing as you can see.  I'm going to be sharing a lot of tips and tricks that I learned along the way for you guys.  So if you want to stay tuned to that go ahead and head over to the Instagram if you want  to support the page as well that would be very helpful.  I really want to help you guys learn so you know anything that you would find helpful  let me know in the comments and I'd be happy to try and help you out with it.  So thanks for watching and I'll see you guys next time.

**Frame:** tutorials\frames\3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial\frame_008.jpg


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
