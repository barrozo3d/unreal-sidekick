---
title: 3D Tracking Natively in Unreal Engine - FULL TUTORIAL
source: YouTube
url: https://www.youtube.com/watch?v=z9t4XIoNsHY
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/3d-tracking-natively-in-unreal-engine---full-tutorial/
frame_count: 7
---

# 3D Tracking Natively in Unreal Engine - FULL TUTORIAL

**Source:** [YouTube](https://www.youtube.com/watch?v=z9t4XIoNsHY)
**Author:** Boundless Entertainment
**Duration:** 14m28s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro to Camera Tracking in Unreal [0:00]
**Transcript:** What's going on guys Sam here so a few weeks ago we launched Genesis the first 3D camera tracking  plugin built directly into Unreal Engine. Our goal was to take three of the hardest processes  in VFX camera tracking 3D reconstruction and distortion compensation and make them easy.  In today's video I'm going to be showing you how we made that a reality by walking you step by  step through all three processes fully inside Unreal and the best part is you don't have to do  any manual work at all which if you've ever done VFX before is thrilling.

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_000.jpg

### Perpetual License now available [0:34]
**Transcript:** But before we dive in I have a quick announcement. We've just launched the Genesis Perpetual  License option which allows you to buy and own Genesis outright instead of paying for a subscription.  It comes with a free year of updates and then after that you can optionally purchase additional  updates at a discounted rate. We published a public road map linked in the description so you can see  exactly what's coming over the next year and don't forget to use code first 500 at checkout for  15% off any plan, subscription or perpetual while spots are still available. So with that let's  open Unreal and walk through the full 3D tracking process. Alright guys so hopping into Unreal here

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_001.jpg

### Tracking Footage [1:07]
**Transcript:** what we have to do is first enable the Genesis plugin so we'll go up to edit and then plug-ins  and then we'll just search for Genesis. Obviously once you have this installed and we're just going  to enable that and restart. Alright so Genesis is now enabled and we can bring up the window by  clicking right there and you can see I already have it docked in the window here. What I'm going  to do is first just walk through the entire process so the first thing we're going to do is simply  click on choose footage. This is where we're going to choose our tracking footage and in this case  we're going to do this running mask shot right here. So what I did before this is simply went into  Adobe After Effects. You can also use DimitriPresolve Fusion and I created a mask around the subject or  actor running in the foreground and then I just filled that with a gray solid and then rendered the  shot and it's ready for tracking. So that's going to eliminate the moving subject from our footage.  Now we are already implementing an automatic object mask system that will live inside of Genesis.  So you'll actually be able to do this inside of Unreal automatically but for now if you just create  a...

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_002.jpg

### Importing Tracking Scenes [4:16]
**Transcript:** pretty good for I think it's like a 10 second clip or so with all that motion and then obviously  the dense reconstructed mesh. So let's click okay and that's going to automatically load up our  tracking scene to be imported. If you want to import a different tracking scene you can hit choose  directory that's going to take you to your Genesis output directory in your plugin folder. And  that's where you can see these are all the shots that I've tracked. You can import any tracking scene  into any unreal project you wish. Since we clicked yes it's going to automatically load that up  right here for us. And then we just have to set our frame rate which I know this is 23.976.  And then we set our sensor width. So you want to make sure that you get this right because this  is going to also end up determining the focal length because Genesis actually calculates the focal  length of your shot directly from your sensor width and then the tracking data. Getting this right  is really important to make sure that your depth of field is correct when you actually import and  start adding CGI to your scene. In my case this was 27.03 millimeters for the sensor width  and that's from the red comm...

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_003.jpg

### Setting Scene Scale & Orientation [6:33]
**Transcript:** need to do first before we really do much else is we need to set up our scene scale and orientation.  So let's turn off our point cloud right there and we'll go into Genesis and then we'll go into  our scene setup and we're going to choose our tracking scene from the list right here. It's  going to be the name of your footage. We're going to go down here to scale and open up orientation  as well and we're going to click on activate set scale mode and this is where we can actually choose  two points on our mesh and specify the distance between them. Okay so if we just click right here  on the ground you can see it's going to spawn a point and we'll click another point and right  here now we can enter a measurement distance. Alright so if we go into our footage here or into our  camera you can see that we have our footage actually overlaid so let me just pull up my background  plate preview and let's just turn up the opacity to one and we're going to turn our fade range down  to zero. That's just your fade controls so you can see if we start moving this we can actually fade  our background plate into the background. So let's just go through our footage here and kind of see  alright s...

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_004.jpg

### Distortion Compensation [11:25]
**Transcript:** right there that's going to be our camera tracking which is done completely automatically no manual  work except for the masking in the beginning and then the last thing is our distortion which again  is handled completely automatically so if we go in here and we just find our camera I just show you  that briefly if we look here we have a lens component and if we go into our camera I can show you  what exactly that's doing so if we take a look at a shot like right here for example if we go down  here and turn off apply distortion within our lens component this was automatically created and  set up by Genesis with all the proper distortion parameters from our tracking data if we turn off  apply distortion you can see that all this stuff kind of doesn't line up anymore so if we check  that you can see it lines up much much better if we take a look at this point here it's going to  line up much better when that distortion is applied and if we don't apply that distortion which again  is done automatically for you so you don't have to worry about this you can see that it's actually  going to significantly impact how well these objects stick in the frame so if I just go ahead and  kind o...

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_005.jpg

### Compositing in Unreal Engine & Upcoming Features [13:46]
**Transcript:** so I hope you guys found this breakdown helpful I have a ton plan for both the channel and the  genesis community including an in-depth compositing tutorial directly inside Unreal using genesis  and the new version of composure which is legitimately a game changer for VFX and Unreal  I'm going to be doing a breakdown of that process right here and then I'll also be doing a full  in-depth course on it in the genesis community and as I mentioned before we have a ton of new features  in development as we speak which we're planning to release over the next 12 months so make sure that  you grab your copy of genesis below because you do not want to miss out on these prices they're the  lowest that they'll ever be let me know if you guys have any questions thoughts or features you want  to request in the comments and I'll see you guys in the next one

**Frame:** tutorials\frames\3d-tracking-natively-in-unreal-engine---full-tutorial\frame_006.jpg


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
