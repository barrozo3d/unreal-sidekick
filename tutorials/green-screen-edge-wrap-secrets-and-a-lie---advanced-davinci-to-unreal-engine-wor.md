---
title: Green Screen Edge Wrap SECRETS (and a LIE!) - Advanced DaVinci to Unreal Engine WORKFLOW
source: YouTube
url: https://www.youtube.com/watch?v=t7Q1UiBr8e8
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: ["edge wrap", "light wrap", "green screen", "blue screen", "DaVinci Resolve", "Fusion", "chroma key", "color space transform", "linear sRGB", "camera tracking", "FBX import", "media texture", "Scene Capture 2D", "render target", "material parameters", "sequencer", "virtual production", "compositing"]
extraction_status: complete
frames_dir: tutorials/frames/green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor/
frame_count: 23
---

# Green Screen Edge Wrap SECRETS (and a LIE!) - Advanced DaVinci to Unreal Engine WORKFLOW

**Source:** [YouTube](https://www.youtube.com/watch?v=t7Q1UiBr8e8)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 99m4s | 23 section(s)

---

## Raw Data (for Claude Code extraction)


### Edge Wrap Example & Introduction [0:00]
**Transcript:** With Visual Effects compositing, one of the tricks we use to integrate a blue screen  or green screen into an environment is an inkled edge wrap.  My edge wrap basically takes that background and blurs it, pulls some of that colour a little  bit over your extraction, just helps it sit into the plate a little bit better.  Until now, we've had to do that in post-production, so you do that in After Effects or to use  your new stuff like that.  Since I'm doing offline virtual production, I like to pre-extract my blue screen, green screen,  and then put that on a media texture inside of Unreal Engine so you can see it into the environment.  You'll be advantage of like fog and all that sort of things.  It's brilliant.  But one thing that I've not been able to do is edge wrap.  But now, I've got a way of doing it, and I'm going to show you how to do that in this video,  so you can put it in your filter.  Okay, so with this video, I've made time stamps, because I'm going to go over some of the things

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_000.jpg

### Coming Up (Video Overview) [1:00]
**Transcript:** again that I've done in my other videos, but I've got updates and improvements.  So the first thing I'm going to do is take the blue screen, green screen, and then do an extraction.  And then I'm going to show you how to make that utility pass for doing the edge wrap itself.  And so you see some blurs and some stencil nodes and things like that.  And then I'm going to show you what that would do in regular traditional 2D-type comp.  So when you blur the background and then you put your character over it and then you edge wrap that, how we'd normally do it.  And I want to kind of move that process into the engine rather than doing it post, because I like to do everything that I can  from the comp world inside the engine, because it's great fun.  Okay, so I'm going to show you that.  I'll go over, in this case, I've got a bigger slider.  So I've got a longer slider so I can do bigger moves.  I'm going to show you the way I do my camera tracking again.  So if you don't have a camera move, then just get that bit and then go to the next bit where I import that into the engine.  And then I'll show you again how I make my media texture, but then I'll show you how I make my sub part of tha...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_001.jpg

### Green Screen Extraction Workflow in Da Vinci Resolve Fusion [3:00]
**Transcript:** So I'm going to give you a quick overview of my blue screen extraction.  It's pretty much the same as my other videos, except I do some little bits at the end of the color space, which I'll get into.  And then at this point here, this is what I used to create the edge wrap mat, which we then use in engine to kind of pull some of that light wrap over our extraction, but not over our background.  Okay, so very quickly, we've got a green screen, blue screen, and then we've got a noise reduction just to take the edge off this because in engine, there's no noise in the actual renders, where I shouldn't be.  And so when you put your plate in, you wanted to look the same in that it doesn't have noise in it or green, and then you add that afterwards.  And then you either add it with a post process volume in engine, which I don't do, I add it inside the, I'm pointing to the color page in the color page there. Hello.  So I, anyway, so we've got our green screen extraction and this time I am using ultra kea and I will try different kers, which see which everyone gives me the best edge.  So what I kind of work is this part of my script here is basically what I used to pull the key. So if I pre...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_002.jpg

### Colour Pipeline Updates - Color Space Transform for Unreal Engine (Linear sRGB Export) [7:45]
**Transcript:** But this gets me a lot closer. And this is thanks to someone in the comments. So this was derauche, who basically said, why don't you put a color space transform in and then do this. And then I was like, you know, I was kind of trying to keep it round trippy.  So I didn't have to touch anything in the end. I was like, yeah, let's just try it. See if it was. And it was like, you know, that's a really good idea. And I really like it. So I've changed my process, my pipeline to incorporate this. So thank you, derauche for leaving that comment. And yeah, do anyone leave comments. Thank you very much. You know, I need your support and your help to kind of improve this.  So what I'm doing here is I'm adding a color space transform. And the reason why is currently we're looking at our diffusion page in, I don't know what the correct color space world gamut thing is that it looks at. But I know that there's a lot up here.  So this little window here is your lots. And I know that inside of Unreal Engine, it is using a linear to SRGB. So the actual internal mechanics of the color space, like some some sure somebody from Unreal, that's not how it works. But I think the internal kind of color s...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_003.jpg

### Creating the Edge Wrap Utility Pass [13:50]
**Transcript:** So then you can point to those frames and if you overwrite them, it'll just update in engine straight away, which is great, but also it's kind of dangerous because you can overwrite things.  So be careful with your saver nodes. Great. So that's this part. So that's our extraction. And now if you're just joining me in the timestamps.  So we're where we used to be except for that little bit about here, which will be our secret and do anyone that's just sat through this last part.  Alright, it was adding the workspace transform. So I'm exporting these as linear SRGB.  Okay, and I've got a resize node. So it's now a UHD resolution.  Okay, so this makes our extraction. And then this part of the script is for our utility pass.  So what we have here is a bunch of maths effectively, which I'm going to use to edge ramp. So I'm going to blur the background in Unreal and then pull some of that blur over the edge of my extraction.  And then I'll help sit sit it in and then I'll put bloom over everything and that will kind of mush it all together as well, but they'll be kind of nice kind of balancing kind of levels.  Now I've got a red, green and blues. I've got a GBA. So I've got different lev...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_004.jpg

### Stencil Node for Edge Mattes [17:10]
**Transcript:** So I'm using a channel boolean and you can see here I've used a copy operation and I've set these these default to whatever they are like alpha or foreground or red foreground green foreground or whatever it is.  But you just go in here and you can find the black or white there's lots of other things here and quick at doing it you press that and then you type in B LA and it will hop to a pointing. It'll hop to it computer second monitor camera B camera.  It'll hop to your whatever you type in like that. So I've got copy black black black and then alpha is the alpha. So that's pointing it to there. And then this one now this channel.  I've made this one the red the red channel and then this one popped into the green and the blue and you can see here like that one's now blue is alpha foreground green alpha foreground and then just add a multi merge at the end.  That's this note here that one there grab that and then you just pipe them all together and it over's the mall and makes it into RGB multi utility utility pass I call it.  So there we are now at the moment it's 3840 by 2160 and because again that's like now you've got eight K's worth the video in your image media source files....

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_005.jpg

### Traditional 2D Edge Wrap Compositing Demo [19:45]
**Transcript:** And that kind of stuff so that's if you're doing kind of real time stuff then just change all of this to movie files effectively nice low res age 62.  So I just want to show you now how I would do edge rap in a traditional comp so you take your background you blur it you put your extraction over that and then you pull in some of that background on top and you add that in using that edge rap mat.  And then I'll show you how we're going to do that inside of unreal live inside of unreal.  Exciting. Okay, so I'm just going to make a background up and put this character over it for giggles be back in a moment.  So I had a little play and I made a background image to put him in and I made it with AI.  I couldn't help myself as quick and so I apologize.  But I just need a background with some contrast and bright light so kind of see roughly what how you would do edge rap or light rap as some people call it in the in the olden days when you did post compositing outside of unreal engine.  I've got my background there it is and then I've got my foreground here we go and then we're just putting him over the background here so there is over the background and tradition and the what you'd like ...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_006.jpg

### Setting up Unreal Engine for Media Plates [23:45]
**Transcript:** And so that's why I've made this utility pass and so we're going to bring this utility pass effectively do the same thing in engine so that's what we're going to do now.  So we're in Unreal Engine and I've got a default level so it was just file new level and I deleted some of the bits I didn't need and I've made a directory called media and I'm going to bring in our and make that media plate.  And so we'll just do that sort of stuff and again this is stuff I did on my last video but it's always fun to get a refresher isn't it.  So right mouse button image media source going to the media and then image media source I am S underscore extraction.  So grab that one double click on that then go to sequence path and press those three little dots there and then we will navigate to our extraction and so you click on the I think any frame but I'm going to click on the first and then it open.  And then to see it's in there you just press open here on the top and then it will play your extraction sometimes sometimes it will sometimes it won't but there it is so we've got it and then you can drag your thing along here to make sure it's working.  Look at that guy.  Okay and then I'm going to h...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_007.jpg

### Creating Media Player & Media Texture [25:20]
**Transcript:** I am S call this utility and these names just totally optional arbitrary that I'm again I've gone to the sequence path clicking the three little dots go to my you extraction utility I've called it and then open that one hit there so there it is.  Cool very fab and it's safe.  Close that so now we've got our two image media sources and now we're going to create media textures for those I'm just do the image media extraction first so right mouse button and then we go back into media and then we want to create a media player.  And then we click on video output media texture asset you hit yes so like that so you got media player so I call it MP we call this extraction.  And then MP extraction videos the media texture I like to call it.  MT media texture and then I just like to call it the same thing there you are now if I go into the media player extraction double click on that and then I tell it which piece to use so I'm going to use the IMS extraction double click on that and then hit save.  So now this media player is going to play this media source and that media player will send that source onto the this media texture and then that media texture is what you feed into your material...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_008.jpg

### Setting up Sequencer & Media Track [32:10]
**Transcript:** Let's just I'm going to change it back now just to translucent just to mess with everyone but I've got the option now because I've got the alpha fed into the opacity mask and the alpha fed into the opacity and I got a divide on so now I got all the kind of different options that we can use when we come to use the media the material instance.  Okay, all right, so save this one here apply and then kill that window now I am going to just grab a simple plane there's my plane and I'm now going to drag this media texture my material sorry onto that plane and there it is so there's my video inside of here which is rotate you round like that.  And so at the moment it's using that frame that it was parked on inside my media player so the way to kind of update the media player is by putting a media track inside of a sequencer.  So I'm going to set up a sequencer and you just say a right mouse button and then level sequence which is in cinematics and create a level sequence and I don't have less level sequence and I'm just going to call this.  What should we call it light wrap edge wrap light wrap.  Edge wrap okay double click on that so now I've got a sequencer I basically need to make a med...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_009.jpg

### Introducing Scene Capture 2D for Background Blur [36:45]
**Transcript:** But you can come back now and see the, imagine we did all the camera tracking and it's all working and then we're going to show you how to the edge wrap thing because that's exciting.  Alright so to the edge wrap part, okay.  Wimli, Wimli, Wimli, Wimli, Wimli, we're back in and we've got our FBX camera with the media plate attached to it and that way it feels like it's locked to the ground.  But if you're doing a locked camera then you didn't need to know any of that because this works with any sort of camera.  So at this point now we're going to use that utility pass to make the edge wrap tool.  So as you can see I've sort of turned things off, let me just turn off the exponential height plan and the sky atmosphere just so we can kind of see the effect of this because we want something bright behind him.  So I've just added a sphere. So I'm going to add a sphere and then ideally if this was photographic we get some of that light wrapping round onto him.  And to do that let's go and create the media texture first.  So we've got our media player here for this plate and now I need to make another media player and a media texture for the utility pass.  Right mouse button going into ma...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_010.jpg

### Aligning Scene Capture 2D View & Render Target [44:50]
**Transcript:** It needs a texture target which is this thing.  And then it sends that picture to the render target.  So we go back into our master material.  And now we're going to feed this render target into here.  So that's our render target.  And we're going to multiply this by that.  Well, I can do the red, green, blue or alpha depending on how wide we want it.  But I'm just going to add a molt.  Multiply node and then let's feed in the alpha.  And then we should see.  Now the edge.  So what we've got here now is a difference in size.  So what I need to do is basically match these two.  So we've got a render target and you can sort of see here.  Let me change that one.  So we've got our image of me like this thing.  It's projected on top of this render here.  On top of this image.  So we need to match this to that because this lines up perfectly with our character.  But that doesn't.  So if I just plug this one into here like that, you'll see this lines up.  But this one doesn't.  So this kind of effectively changed the aspect ratio of this image and the field of view to match this.  And that is a little bit trial and error.  So I'm going to show you how I do that.  There we go.  Hit apply. ...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_011.jpg

### Refining Scene Capture 2D (DOF) [51:10]
**Transcript:** So it's kind of adding this on top of itself.  And then I look for focal distance of the scene capture 2D, and we turn on this one, depth of field, and it's anything there at the moment.  But if you make it 0, it kind of defaults to 1, then, oh, look at this, you see, it started blooming all of this on there.  So if I make it solid, like it's now everything sharp, not getting any bloom, but if I go this way, now we're getting bloom over that bright area.  So then we hit save that.  And that's kind of set up.  Effectively, what I'm going to do is go inside the material and make a little variable, little expose the brightness value that we can then edit in the sequence.  But for now, if I just grab this sphere and move it around, you can see that it's like brightening up the edge.  So if I just play this, you can see that edge wrap is working.  It's working. It's maybe a little heavy.  But we'll go and give you a variable that will change that in the sequencer.  So I'm going to add another sphere here.  So here we go. This one is got a different color on it.  So it's taking that color and it's wrapping it around.  So if you've got something hot here, and you're going to get that colo...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_012.jpg

### Exposing Edge Wrap Intensity Parameter [53:00]
**Transcript:** I'm going to press one.  And then I, what's this called, converter parameter, that was it.  So I'm going to add a parameter called edge wrap or light wrap as some people call it, I call it edge wrap.  And then I'm going to multiply that by that value.  So M for multiply, we can drag off here and then put your edge wrap into there.  And then that into there. And then we can, we don't have to go into a material instance.  I could just, you know, go into here and type .4 into name press apply.  And it will change the value of this.  And I can go in there, .2. And you might want to do that.  Or what you can do is, since this is a parameter, if I add a material instance,  I'll be able to edit that as a material instance.  Or I can, yes, yes, yes, yes, yes, yes, save that.  Or I'm just going to try this now.  I don't know if it's possible, but I'm without a material instance.  If I bring this plate into the sequencer, and then I hit plus for a static mesh component,  and then see if I can get the material component, material slot, material parameters,  then I can go into here. And then the one I just made, did I give it a name?  It's all like edge wrap, yeah. So edge wrap.  And if I go i...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_013.jpg

### Editing Material Parameters in Sequencer [59:00]
**Transcript:** Wherever you are, let me find it.  Here it is.  So there's my FBX camera.  And you can find it.  So here's the actual camera.  And then on...  Well, that's actually...  There's the camera.  And then on top of that camera, I added another camera.  So they're on the same...  Along that same vector.  I use your...  Along that same vector from the eye to...  You know, the camera's pointing this way.  So if you add another camera onto that as a child,  and you can push it forward and backwards,  it will still work with all the tracking and all that sort of stuff.  That's fantastic.  That's what I did with this camera.  And then I've pushed it back along that plane.  And so if you push it back along that plane,  and when the camera moves,  it's going to jump because I've got an animation there.  But you can kind of see here, actually animating that and moving it forward,  at the beginning of the shot.  So you can go wider and further back,  and then you can zoom in.  Well, not a zoom, but an actual track in.  So you can track along that axis.  And then what you can also do,  you can track along that axis,  but you can also pan until, along that axis too.  And then all of this will still ...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_014.jpg

### Clean Version of Cyberpunk Intro [63:00]
**Transcript:** So before we cut to the bonus section,  I'm just going to show the complete opening video of this  without anything on top of it,  and me talking or anything like that,  just so you can kind of have a look  and see where we ended up.  All right, thanks again.  Bye.  With Visual Effects Compositing,  I want to add tricks and use to integrate a blue screen,  or green screen into an environment,  it's an ink called Edge Wrap.  My Edge Wrap basically takes that background,  it blurs it, it pulls some of that color,  a little bit over your extraction.  It just helps it sit into the plate a little bit better.  But until now, we've had to do that in post-production.  So you do that in After Effects,  or to use more new stuff like that.  But since I'm doing offline virtual production,  I like to pre-extract my blue screen, green screen,  and then put that on a media texture inside of a real engine,  so you can see it into the environment.  You'll be advantage of like fog and all the rest of the things.

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_015.jpg

### BONUS Section: In-depth Camera Tracking Intro [64:00]
**Transcript:** It's brilliant.  But one thing that I've not been able to do is Edge Wrap.  But now, I've got a way of doing it,  and I'm going to show you how to do that in this video,  so you can put it in your filter.  Okay, so those have stayed for the bonus section  on the camera track.  This bit's for you.  So I'm going to show you what how I can retract this  in the future past wherever I am.  Confuse myself.  So we've got our plate.  Here we go.  Our green screen plate.  And there it is.  There's our shot.  And you can see that I've added some extra little reference markers  on the wall.  And those were just like,  Velcro, I've so got a white Velcro,  because that's my screen,  and I've got some black bits on it.  And I've got some white Velcro on these things.  So I just made a little,  gave it a few more tracking markers around the spot,  around the plate,  so to help the camera tracker.  So that's good.  And then you can see it.  Nice.  Look at that.  Nice long move.  Wee!  And then I'll probably cut to a little insert of the camera tracker.  And then on the last video,  I said, oh, it's just a little camera.  And it's like, no, you're right.  It's not a little camera.  It's quite heavy...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_016.jpg

### Setting up Camera Track Node [69:30]
**Transcript:** So the plate.  I need the edge of the frame to be like bang on with the actual camera track.  Then I would have to have a lens distortion either applied to the renders or you  understood the plate.  So that everything is totally rectilinear like a computer computer.  It only draws like a there's two points between the top of the line and the bottom of the line.  It's like a straight vector.  Whereas in a real camera, it kind of bows and bends depending on the lens itself.  So if you want bang on absolute accuracy, then you would add a lens distortion or an  undistort to the plate first or afterwards.  But in my case, I only kind of care about what's in the middle of the frame.  Because that's why my character is walking.  And I got bigger fish to fry.  So now we've got our camera track done.  We want to make it into a 3D camera track.  So at the moment, this is all the camera tracking kind of 2D sort of calculations and stuff.  And basically what we do now is export this to the solve.  So you go to solve, then you get an export, and then you hit export here.  And it will give you some things.  And it always seems to put it like over here or somewhere.  You watch this.  So there's m...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_017.jpg

### Scaling World (Merge 3D) for Unreal Engine [75:00]
**Transcript:** Just makes it easier.  That's where my character will be standing.  That would be in the plane.  So I'm just going to bring this around like that.  And then come down a little bit in the Z.  I mean, the Y.  Like that.  So that feels like, you know, these were the light stands.  And they feel like they should be vertical.  But maybe that would quite.  Let me give it a bit more rotation.  Ooh!  Let's feel like that.  There you go.  Let's go get it to the edge of the screen.  Okay.  All right.  That feels a bit better.  Okay.  And then we're going to adjust this inside of Unreal.  I'm going to show you how I do that.  But I just like to get it ballparky.  Great.  So there is my camera oriented.  How I want it.  And then you can see that's moving along now.  Doing its animation.  Beautiful.  Okay.  Now the other difference that I did from last time  is I changed the scale of the world  and I do it in the Merge 3D node.  So when you come to export this with the FBX,  there's a scale option there.  But no matter what I was doing,  it was always coming in pretty much the same or just all the way over the place.  But anyway, Merge 3D,  if you go into that, transform in there.  This is the ...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_018.jpg

### Importing FBX into Unreal Engine [81:40]
**Transcript:** So great.  That's done.  So now I have my camera track as an FBX.  And that is exported to the disk.  And the next thing I'm going to do is now go into a real engine  and bring that in and line it all up.  This is where I left everyone else.  But you hardcore as you're going to be thrilled to bits  with this part.  So I have my plate fantastic.  So what am I going to do now?  So we're bringing the FBX into the actual level.  And then we bring the camera into the sequencer.  So I have to bring it in through this one.  Not you have to go file import into level.  So it's not file import.  You go file import into level because it reacts differently.  And then I'm going to go into where I put it,  which was in here, the FBX.  So we hit that button.  And so we put it into a level.  So I'm going to go into my level.  And I made one called camera.  And I'm going to hit OK.  So it's going to give you some options here.  So if I open this up, if you look at the root node,  there's all those shapes.  So we have the ground plane.  And then we have the little squares that we used as the reference.  And that's why I wanted to try and merge them all together.  And it also brings in like the camer...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_019.jpg

### Using Disable Depth Test for Alignment [90:00]
**Transcript:** And now what you can do is if you, why is that moving on now?  So you should feel like he's standing in the right spot.  Like when it's, when it's, because the camera's moving and he's moving.  But when you look at it, not from the camera, it should feel like he's not sliding around.  Okay, one thing I'm going to do now just to help you find out where his sweet spot is from distance from the camera.  Is I'm going to go into his material.  And then change the material in here to if you look for depth.  See this disabled depth test.  If you turn that on, it basically disables it.  And you apply.  So now he won't, he will always be on top of whatever's behind him.  So there is no depth on there, which is great for in this case, because you can get him in the right 3D space.  But if you want to put things in front of him, then you have to come up with other tricks, which I did on my last video.  But I will, we'll come to that problem in a minute.  Alright, so let's, let's kind of, I'm just going to find that sweet spot.  So I'm going backwards and forwards.  So it's a feet.  So you still sliding around a bit.  Let's bring him forward.  At some point, you'll feel like he's locked.  Well...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_020.jpg

### Fixing Ground Intersection (Scaling Camera) [94:40]
**Transcript:** So what I'm going to do is just scale him closer to the camera.  So he'll be relatively the same in world space.  I mean, in screen space, but in world space, he'll be closer.  So I'm just going to show you what I'm going to do.  So I'm going to take my actor, go into my media, my master material, and then disable depth test.  So depth, depth test.  I'm just going to move it up here.  So if I hit disable depth test, so now it's not disabled.  And then here apply, you see like his feet are intersecting the ground.  And then I'm just going to open up another window.  So I go to window viewport, click on viewports.  So this is the same scene, but from a different angle.  There it is. So in world space, you see right here, I'm going to hit G just to hide everything.  And then come over here. So you see there he is, there's his plane, and he's intersecting the ground.  But what we can do to fix that is if we select the camera in the sequencer,  and that's what you owe it there.  I left it, I left it dark because I probably got me here.  I'll be like that.  If I go now into my camera, and you can scale it, set to 50, because that's what we scaled our world by.  And you see, if I open up ...

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_021.jpg

### Thanks for Watching! [97:40]
**Transcript:** There he is like that. I can make him pushing back now.  So I can scale him up again.  Whoa, wrong one.  I can select the camera and scale the camera back.  And so he looks the same in the world, but you can see here.  He's in the different screen space, world space.  It's not getting a bit spacey.  And there we are.  So that's how we get around that problem.  So now we've got our camera in 3D space.  And our character in 3D space.  And we can have him not being a depth testy-holdy-outy thing.  There we go.  So now I'm going to go back to the video and then carry on the rest of it  for those people that didn't want to sit and watch and figure out and do 3D camera moves  and all that sort of business.  So now it's at the end of the video for you.  And you know what, just thank you for watching.  And I'm really enjoying making all these videos.  So thanks for all your support and for all your likes and comments and subscribing.  So I really appreciate it.  And now I have to find another video for you to watch.  Ah, this one here is really good if you've not seen it.  It's one of my favorites.  Okay, all right. See you there.  Bye.

**Frame:** tutorials\frames\green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor\frame_022.jpg


---

## Structured Notes

### Core Technique
A comprehensive advanced workflow combining DaVinci Resolve Fusion green screen extraction (with linear sRGB color space transform and a multi-channel utility pass), a real-time edge/light wrap effect inside Unreal Engine using Scene Capture 2D + Render Target + custom material parameter, and a full bonus section on DaVinci 3D camera tracking and FBX import into UE for moving shots.

### Summary
At 99 minutes, this is Dean Yurke's most in-depth compositing tutorial. It covers three areas: (1) an updated DaVinci Fusion extraction pipeline with an added color space transform (source camera space → linear sRGB) so the extracted footage looks correct inside Unreal's linear color pipeline, plus a three-channel utility pass (RGB = different softness/blur levels of the alpha edge) for driving the edge wrap; (2) implementing edge/light wrap inside Unreal Engine using a Scene Capture 2D actor pointed at the background, sending its output to a Render Target that is fed into the plate's master material as a multiply/blend operation — the DOF of the Scene Capture drives the blur/glow width, and an edge wrap strength parameter is exposed into Sequencer for animated control; (3) a bonus deep-dive into DaVinci camera tracking, FBX export scale tuning, and importing moving camera shots into UE (File > Import Into Level, actor parenting for scale correction, Disable Depth Test for alignment). The "lie" in the title refers to the fact that edge wrap in UE is an approximation, not a perfect real-time match to post-comp edge wrap.

### Key Steps
1. In DaVinci Fusion: add a Color Space Transform node after your keyer; set Input to your camera's native space (e.g., Blackmagic Film Gen 3), Output to Linear sRGB — matches Unreal's internal color space.
2. Build the extraction script: Noise Reduction → Green/Blue Screen Matte node → garbage matte shape → key refinement.
3. Build the utility pass: from the extraction alpha, create three blurred/softened versions at different radii; use Channel Boolean nodes to pack them into R, G, B channels of a combined utility EXR sequence.
4. Export extraction as linear sRGB EXR sequence; export utility pass as a separate EXR sequence (can be lower res for performance).
5. In Unreal Engine: create Image Media Sources for both extraction and utility; create Media Player + Media Texture pairs for each; build or duplicate a master plane material feeding both textures.
6. Set up a Scene Capture 2D actor in the scene positioned to match the camera view of the background environment.
7. Create a Render Target asset; assign it as the Scene Capture 2D's output texture.
8. In the plate material: multiply the Render Target texture by the utility pass alpha channel; expose an "Edge Wrap" scalar parameter; apply this on top of the extraction.
9. Adjust Scene Capture 2D's depth of field (Focal Distance = 0 starts blur) to control edge glow softness.
10. In Sequencer: add the plate mesh as a track; add Static Mesh Component → Material Parameters → Edge Wrap scalar; keyframe to animate edge wrap intensity per shot.
11. (Bonus camera tracking) In DaVinci Fusion: track the plate footage with the 3D camera tracker; set a ground plane; scale the world in the Merge 3D node (e.g., ×50); export as FBX.
12. Import FBX: File > Import Into Level; use a sub-level folder; UE imports camera + geometry hierarchy.
13. Parent the FBX camera as child of a root actor; scale the root actor to compensate for size mismatch; translate/rotate to align camera to the scene plate.
14. Use Disable Depth Test on the plate material for alignment; re-enable after positioning.

### UE Systems / Blueprints / Settings
- Image Media Source / Media Player / Media Texture (two pairs: extraction + utility)
- Sequencer: Media Track, Material Parameter Track (scalar Edge Wrap parameter)
- Scene Capture 2D actor (Render Target output, Depth of Field settings)
- Render Target asset
- Custom master plane material: extraction texture + utility pass multiply + edge wrap scalar parameter
- Material parameter: Convert to Parameter → "Edge Wrap" scalar (exposed to Sequencer)
- Disable Depth Test material flag (alignment aid)
- File > Import Into Level (FBX camera with hierarchy)
- Actor parenting + scale/rotate root actor for camera alignment
- DaVinci Resolve Fusion: Color Space Transform, Channel Boolean, blur nodes, utility pass packing (external)
- UltraKey / DeltaKey / other keyers in Fusion (external)

### Difficulty
Advanced

### UE Version
5.x (no specific sub-version stated)

### Tags
edge wrap, light wrap, green screen, blue screen, DaVinci Resolve, Fusion, chroma key, color space transform, linear sRGB, camera tracking, FBX import, media texture, Scene Capture 2D, render target, material parameters, sequencer, virtual production, compositing

---

## Related Entries
- `green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-.md` — Composure EP3: lit material and improved DaVinci extraction techniques referenced here
- `green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin.md` — Composure EP2: camera projection setup and fog/depth fix that this tutorial extends
- `green-screen-overscan-secrets-and-a-lie---your-ultimate-vfx-save-series-bonus.md` — companion "secrets and a lie" bonus video in the same VFX series
