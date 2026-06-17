---
title: Green Screen Cards are DEAD! Camera Projections in Unreal Engine change EVERYTHING! (Composure EP2)
source: YouTube
url: https://www.youtube.com/watch?v=VbLziZfiyD8
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin/
frame_count: 16
---

# Green Screen Cards are DEAD! Camera Projections in Unreal Engine change EVERYTHING! (Composure EP2)

**Source:** [YouTube](https://www.youtube.com/watch?v=VbLziZfiyD8)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 50m0s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### The secret power of Camera Projection in Composure [0:00]
**Transcript:** Welcome to part two of Composure, the joint of blue screens inside of Unreal Engine for offline and real-time virtual production.  The huge advantage that Composure has is that it's using camera projections, so it allows us to take footage from that camera and put it onto a long flat surface.  So I'm re-checking this right now onto a curved surface, and so it's capturing the shadows, and so we can now improve our integration into environments.  The first thing I'm going to do is I'm going to show you my blue screen process. I've got like a smallish room. I've got a fold out blue screen, and I'm just going to set that up and show you the kind of lights that I use to make it key better.  So the blue screen that I've got isn't quite blue, it's a kind of de-saturated blue-ish screen. For what I do is I've got a 4GVM 800D RGB light, and they're pretty cheap, used off eBay, and I kind of put them evenly around the screen.  So I'm going to turn this one on, and you can kind of see that it's throwing a general light over there. But because these are RGB lights, you can go into the RGB mode and change the color of the light to kind of match your overall color temperature of the background, ...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_000.jpg

### Cinematic blue screen lighting on a budget [2:15]
**Transcript:** And then thanks to the power of Unreal, it's taking the global illumination of characters and actors, and it's bouncing those back onto the plate, and it's great.  So watch that video after you've watched this one, if you haven't seen it, if you have seen it, thank you, and then go and watch it again, because it's great.  Alright, but on this episode, we're going to do the opposite, we're going to take the same feed, but we're going to use a blue screen, and we're going to put that blue screen onto this composite actor, and it can be any shape, but the default one is like this, that curve surface that you sort of beginning, and then you can put it into your environment, and your environment can reflect that object as well, so it's really good.  And so we're going to show you how to do that. So we're starting off with this room, because I don't want to have to build it again and bore you, but the first thing we're going to do is add a new media profile.  What's that you ask? Well, on the last episode, I see, yeah, I did the thing where I take a media player, and we use that to take the feed from the camera, the USB or the DVI, and we make a media player, and then we use Composure to...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_001.jpg

### Why Media Profiles are useful [5:30]
**Transcript:** And then you hit refresh media properties. So now I can save this. And then that now every time we just look for this new media profile, it will give you this live feed.  And if you're in play mode or in simulate mode, it won't turn it on or off. So that's great. So thank you Ryan. We're going to close this down.  So now we're going to add a composure actor. So we go into window, virtual production, composure, then we place a composite actor.  And the first thing we do is we associate the camera with the one that's in the scene. And this is the camera I had last time. And I had spent ages kind of getting it right and sort of finding out where it should be.  You can use lots of other software that does this for you, but I didn't.  I'm a professional. We do it by eye.  Okay, so select here from the camera choice. And then I'm going to choose the any camera that I've got in the scene. So you click on camera component.  So that's that one. And now what we're going to do is we're going to add a under plate layer. I'm going to add here a place composite mesh actor.  And then this has made this wonderful huge composite mesh actor.

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_002.jpg

### Setting up Composure. [7:15]
**Transcript:** So under here where it says at the moment, it's just using that color bars. So it's using the color bars. And then so here you can choose a media profile. So we click on that.  And then we can just choose the one that's active. Click on that. And now it's projecting it through here. So it's made it a massive object.  So I'm just going to scale this down because it's way too big for me. And where it's going to scale him down to something a little bit bigger than a man.  So we put that just there. Push him into the world. There it is. Okay.  And then come back here and push him up a little bit. One just says above the law. And then if I go into on a wireframe, you can see it's just this this shape here.  And I'm going to put the screen. Let's see the guy we're going to put him about here in the middle of the room.  So let's just take this object and just put it around about here. And that's where it's going to land on. So you can see here this camera. There's my camera.  And it's going to project this image.  So you're on to here. Camera mapping as someone reminded me it's called I call it camera projections, but we'll see what the SEO does.  Okay, back on to lit. And then let's go t...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_003.jpg

### Building the Composite Actor from scratch [8:45]
**Transcript:** So I'm going to now I'm looking through the perspective, but if I look through the this camera, the cine camera actor.  You'll see it looks like feed, but it's not because it's projected onto that thing. So let's grab our composite mesh actor.  I'm just going to move him back there like that. You can see the shapes moving away and where that shape where it's hitting it. It's kind of projecting onto there.  So now that we've got this, this guy is now, oh, by the way, that's me. That's my standing.  I talked him all the time. We have conversations. He's a lot of fun. It doesn't say much, but he is a lot of fun.  So actually, as you can see here, the way where his feet kind of feel right on the floor is where you kind of put this mesh actor.  So yeah, like I was saying, in the olden days, when I had a card, this card would intersect the floor.  So you would lose all the shadows and you'd kind of have to do that thing where I would take the card and sort of scale it towards the camera.  But then it's not in the right depth. And the great thing about this is that you can focus it on this, you can focus the camera on this plane and the depth of the field will work as well.  Ooh, all righ...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_004.jpg

### Live Chroma Keying: Settings for better skin tones [12:20]
**Transcript:** And then I'm going to play with my red way and see what that does.  And basically, this is how I do a king is I slide things and see if it makes it better or worse.  So that's making it a bit better.  And then you've got alpha threshold that just makes things thinner like so.  So there is our key.  There's no great. And so, right, what about the rest of this stuff around here?  Okay, we'll get rid of that because this composite mesh actor is only going to project on to the texture is only going to project on to the composite mesh actor.  So we can grab our composite mesh actor and just scale it a bit.  So I'm just going to scale that geometry.  Okay, there's pretty much where I want my screen to be.  So there we go. And I'm going to put him back into look through my cine camera actor, which is the one that's associated with this plate and move them across there a bit more.  So there's our guy in our room.  And then what I can do now, just get up and run around.  And see if this works.  Hi, how you doing?  Great.  Stage next.  It was just me.  Yeah, particularly.  So I don't tend to do live virtual production.  I do pre-recorded virtual production.  So I basically use the camera fil...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_005.jpg

### How to record high-quality Media Outputs [16:10]
**Transcript:** So that was the EXR and the base name.  And then there's what else is there.  Other options for cropping and stuff.  I don't know.  But this is the fun part.  Save this.  And then you hit ready, start capture.  And so now it's going to cool those.  And I'm going to run around on my blue screen.  Hi, and still it's not a very good key because I'm not using a very good DVI output.  It's currently recording at 60 frames a second.  I don't know how to change it.  You can figure that out and let me know in the comments.  All right, on to the way I normally do it now.  Before we move on to the next thing, I just wanted to show you that the composite mesh actor  doesn't have to be this shape.  It can be any shape.  So if we go into our perspective window, so at the moment I've got, there's this screen.  That's the one that came as default when you press the add stuff here, place composite mesh actor.  That's what comes in.  But when I open this up, you can use any of these objects in the scene.  So we can even use wolfies.  So there's a wolf.  That's gone crap wolf.  So I'm going to say use wolf.  Select the object, right mouse button, apply unlit material.  And so now it's only projectin...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_006.jpg

### Projecting video onto custom 3D shapes (and Wolfie!) [19:50]
**Transcript:** So the software is important.  It's just more creating those elements.  In this case, I've got the match move, and I'll show you how I bring that in.  But if you want to learn how I do match moves, or if I do keys inside of divinci,  then watch my previous video on edge wrap secrets.  Or there's another one on keying and stuff.  Those, I'm going to put a little insert just to help forgotten.  The name has changed, but the principles are the same.  OK.  So onto the next bit.  Back in Unreal Engine, now we're going to set up our video playback of that image sequence  that we just recorded and made an extraction for.  Now, the way Unreal works is that you have in the sequencer,  you have that image media source, which looks at all those frames.  It sends that to a media player, and then that media player sends that to a media texture.  And it's kind of messy like that, so you can swap out your image media source  for like a file media source or a different piece of footage.  So it kind of makes sense, but it's a bit of a mess.  We need to kind of set up.  So you just kind of get used to it.  So we're going to do that now, and so we're going to bring in our image media source.  So writ...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_007.jpg

### The Offline Workflow: Preparing EXR sequences [23:40]
**Transcript:** Media.  Yeah.  All right.  So now we're back in our composer land.  So I'm going to place a composite actor.  And then I'm going to associate that composite actor with the camera.  So I'm going to use this one.  That's one that's in the scene.  And then I'm going to look through that camera.  There it is.  So that is pretty much what we shot from.  And I hand my camera at the end of my slider.  So this is what that represents.  So now I'm going to go to the plate layer.  And here we've got our signal.  And it's using just the SIMPTY bars.  So now I'm going to use instead of using the default composite mesh actor,  which was that really big one.  I'm going to bring in the custom one that I made earlier.  So I'm going to go to my content browser,  jam, and bring in this shape here.  So I'm going to put you back around about there.  And now I'm going to associate this into the plate layer.  So there's my shape.  I'm going to drag it and put it into this plus square box.  So now, and this is associated with the plate layer.  And it doesn't know what material to give this.  So we select this right mouse button.  Apply Unlit Alpha Material.  So this is projecting this media texture.  So ...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_008.jpg

### Integrating Image Media Sources in the Sequencer [27:15]
**Transcript:** And you can see along here, it's given as a transform.  The thing is, I want to use this camera  because it's got all the right settings  and it's in the right position.  So I need to move this camera over to where this camera is.  And I've been trying math and stuff,  and eventually on a video, I'll work it out.  But for now, I can't work out how to get that one over there  because every time I add an actor in a hierarchy,  they'll jump around so something's funky.  So we're going to budget.  So that is the technical term for having to go.  So I'm just going to add an actor,  and I'm going to zero this one out,  because this camera came in relative to where I put it  inside of DaVinci Resolve.  Now one of the things it needs to be scaled up a little bit  because I couldn't quite work out whatever the scale is.  I kind of guess it, and then I scale it in here.  So I'm going to scale it relative from this world origin.  So basically, we add an actor,  and then we parent the camera onto this actor.  And now if I select my root actor,  I can orbit this around.  And the idea is to kind of, I know it's terrible,  but the idea is to kind of line this up  with my camera that I shot the pl...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_009.jpg

### Importing external Camera Match Moves properly [31:00]
**Transcript:** and it was kind of eating into my shadows.  So there was two things I can do.  I'm going to do the easiest thing.  We just put some objects there.  So make it dark.  But I could go into resolve and add a bit more of a shadow  or we could put an object in here and add a bit more shadow.  But for now, it's good enough because I'm just so happy  to have shadows in my scene that are real and in the plate.  Which is awesome.  Yes.  Okay.  Thank you and real.  Next.  So we have all the bits to our puzzle,  except for the puzzle itself.  And the puzzle will be a nice environment  that we're going to put this into.  And we've projected that with our composure  onto a composite mesh actor with the curved surface.  So we've picking up the shadows on the ground,  which is amazing, fantastic.  And now we're going to do the fun part,  which is putting that all together under one actor.  And then we can move around that within our environment,  doing some virtual scouting.  Normally what you would do would be to do storyboards  of what the scene you want to make  and maybe do an animatic and then kind of know what your lighting would be  for your blue screen, green screen.  And then you'd like y...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_010.jpg

### Aligning virtual and real-world cameras [35:20]
**Transcript:** And then I'll hit accept.  And then I will render at my sequence.  Bb-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b.  So ideally, we'd be using Translucency for our renders.  However, unfortunately, there are a couple of things for filmmakers  that Translucency is kind of fighting against.  And that is, I like to add some exponential height fog to my scene.  But, if I go and make it nice and strong like a dude,  food. Then you can see that it's affecting the background but not this plate and I can't  work out how to embed this into there. So that's one issue and then the other thing  as a filmmaker, we like to add some VDB's, heterogeneous volumes, sparse volume textures  etc. And they aren't quite working in the way that I'd like. So if I move him backwards,  he's kind of see that it's not being held out by this foreground. So this, our foreground  plate is kind of acting as if it's on the background. So that is not ideal either. So the  two things that I like to use to make my shocks look a bit more atmospheric aren't quite  working in unless I always want it in front. So what we have to do is we go into our composite  mesh actor and we change the material type to app...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_011.jpg

### The "Fog Problem" with standard media plates [39:10]
**Transcript:** pencil then click it it's going to bring up this material instance and then we click on  the folder here and that will navigate us to where the master material lives. Now we  don't want to mess with the master material we want to make a copy of this so I go right  mouse button duplicate and then I give it a name, do that and then I'm going to move  that into my local directory so I'm going to grab you and just drag it into my composure  and I'm going to move that one there. I'm going to go to my composure and now we can edit  this without messing up everything else not that I would do that. So now we've got our material  I'm going to replace the one that's currently on my composite mesh actor by dragging it  into here. So now I'm using mid if I don't know why it adds that but it does there's my  name of my texture there. So that means this is now using my custom version so double click  on that one. Now I don't know all the ins and outs of this composure material setup and  I'm sure there's some engineers who are cringing right now but what I'm going to do is change  and I don't know what these are but I know that the opacity mask if I add a dithered temporal  to both of these opac...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_012.jpg

### The Fix: Building a Dithered Mask Material [42:45]
**Transcript:** this you can see here that it is over black and so what I need to do is use the version  where he's not over black and he's actually using an extended edge so let's go and find  that one. So here's one where my edges are being extended outwards and so now rather  than being black it's going to have the colour of these edges going over this background.  So again not ideal and not simple but that's the way around it. So here we go. So we're  getting some of that detail now it's not perfect because I'm changing the background quite  drastically from what I was shot but that's how I do it. So if we come back into our 3D  we can now see that our piece of geometry because it's now a masked piece of geometry and we can  grab our steam and move it around and it'll pass through that geometry and kind of work in a way  that feels a bit more sort of working with depths and stuff. So that's absolutely fantastic but the  compromise is that you know the edge is a bit more nasty and it's more work to create the extended  edge version of the plate but it's a tradeoff isn't it? Okay so now we've got all of our pieces  I want to bring in our kind of fancy environment into this scene so what I'm goin...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_013.jpg

### Final Composite: Integrating into a marketplace environment [46:30]
**Transcript:** we can inhabit and so you find a spot that looks kind of good and I'm going to go to about here  I'm going to grab my composite mesh actor I'm going to grab the bundle and then just pull this  to where I want it to be press that button there so then you're viewing the camera and now if I grab  the root position I can move this around and find a nice spot you can rotate it  there we go and I found somewhere around about here so I added some vehicles and characters and  animated those and also put some VDBs in for some smokes and then the other thing that I did  was that we can color correct our main plate layer by going into plate layer and then you can see  what I've got one on here already but I'll just turn that one off and then so we go to plus here  and then add a color grade pass and then in here we can change the contrast we can change gamma we  can change the colors so you can kind of nudge them all around and get them to fit in better to your  plate or you might want to adjust your plate by adding a post process volume etc etc so yeah there's  more tools to throw at than I can fit in this tutorial and now one more thing before we say goodbye  I want to show you my render se...

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_014.jpg

### Rendering Secrets: MSAA and fixing fireflies [49:15]
**Transcript:** subscribe so that you'll be on the bell notification button ping-bong and then you won't miss that one  and in the meantime here's the finished version and thanks for watching see you next time bye

**Frame:** tutorials\frames\green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin\frame_015.jpg


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
