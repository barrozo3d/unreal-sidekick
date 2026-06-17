---
title: Make Films in Unreal : Everything you need to create your first short (Beginner) Start Here (ep1)
source: YouTube
url: https://www.youtube.com/watch?v=PPRugNC7POA
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta/
frame_count: 17
---

# Make Films in Unreal : Everything you need to create your first short (Beginner) Start Here (ep1)

**Source:** [YouTube](https://www.youtube.com/watch?v=PPRugNC7POA)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 31m0s | 17 section(s)

---

## Raw Data (for Claude Code extraction)


### Unreal Engine Filmmaking: Basic Setup and Workflow Overview [0:00]
**Transcript:** So if you have a little bit of experience with Unreal Engine but you've never made a film  before, then I'm going to show you my basic setup.  How I create a sequencer, bring in some animation, set up some cameras and then start blocking  that out with an environment and then render all of that with the move render queue so  you can bring those frames into your edit and start putting together your film.  So let's get on with that.  So I like to start with a blank project and I just make a project, put it in wherever  I keep my projects, film, like that and then I've got start a content on and then I'm  going to hit create.

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_000.jpg

### Why Use Unreal Engine for Film: Speed and Transmedia Potential [0:40]
**Transcript:** So it'll make that project and while it's doing that I will explain why do I make films  with Unreal Engine rather than a traditional kind of pipeline.  Well the biggest thing is speed.  It's because you get this immediate feedback when you're putting objects around a scene  and you move in the camera and then you move in the lights and then you're doing virtual  scouting and those sort of things.  So that's a huge advantage over the traditional pipeline but also once it's working in Engine  you can then use that story and you can tell it in a different way so you can go into a VR  application or you can go into a game application or so it gives you this potential for a lot

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_001.jpg

### Setting Up Your Project: Blank Project & Starter Content [1:18]
**Transcript:** more transmedia type of events.  Alright so here we have our blank project and I want to put something in here that we  can play with.  So I added that start a content and you can see it in here so there's some objects and  things like that.  We've got some props and things and a table and whatever but then I also wanted to add  a character and I thought ah what we can do is use the third person template and so if  you want to add that you can go into here under the plus and then you're going to add  feature or content pack and then you can add the third person into here so I'm going to  add that and it'll download that and put it in there so all of these things come with  just standard regular Unreal Engine.  I didn't want to download things off the fab asset store or anything like that but that  is one of the massive advantages as well of playing with Unreal is you've got that huge  marketplace on all that content to just pull and kit batch from and I really get you  accelerated into your story so you can kind of enjoy the fun part before you have to worry

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_002.jpg

### Adding Characters to Your Scene [2:20]
**Transcript:** about the kind of technical stuff and building things but once you've got that good template  and that framework then you can level up your environment, your characters, your animation  but you've got a nice sense of the story that I find that so rewarding.  So here we are.  There I've got some characters here so I'm going to go into the mannequins and let's  get going to meshes and I'll go and get a mani drag him into here.  There's our little character and let's bring in Quinn as well so he's got someone to talk  to.  There we go.  Let's get all of it around this so that's our world and then what I'm going to do is just  have them walk along and I'm going to follow them with some cameras and I'll put some  objects in there just to kind of start blocking out a story.  So I'm going to now go in and make a directory just called levels so I'm going to go to new  folder and make a directory called levels or folder called levels and then that's just  good practice to put your levels in the sub directory of there so I'm going to create  new folder.  I'm going to call this film so this is my film and then I'm going to save this level  into here so go file, save current level as and I'm g...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_003.jpg

### Introduction to Sequencer: Your Nonlinear Editor [3:45]
**Transcript:** just calling a film.  So there's my level and if this was a game you'd kind of have blueprints and you trigger  things and trigger movements and all sorts of things on player start when you hit play  but for cinematics and animatics and filmmaking you use the sequencer so the sequencer is your  foundation of storytelling and unreal so you go to right mouse button and then go into  cinematics and then create a level sequence and I call it LS for level sequence and then  I'm calling it film.  There we are.  So double click on that and then that will open up your sequencer so this is your sequencer  and it's like your non-linear editor so you've got your timeline going across here  and then you drag that and that's moving your frames so you've got discrete frames and  then along here is where your drag and put assets and then you'll get animation tracks  along here.  The important thing to do at the beginning is just set your frame rate and since I'm  from a film background I like to work at 24 frames per second so there's my timeline  and now we've got absolutely nothing happening so that's great so I'm happy that it's  a fresh canvas, it's a blank page.  So one of the reasons I brou...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_004.jpg

### FBX Animation: Using Basic Walk Cycles [5:53]
**Transcript:** so we can use some existing FBX animation and so if you go into the animation track and  you hit the plus button it will look into the content directory and basically any animation  that's compatible with this character you'll see it in here and the default one you've  got all these like little animations for arm and thigh but they're kind of testing ones  but there's one for walk which kind of comes with the third person template so I'm going  to add in the mm walk so and it went exactly where I dragged it so I should have really

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_005.jpg

### Best Practices - Setting Sequencers to Start at 1001 [6:25]
**Transcript:** gone to the start frame and put it there but it doesn't matter because you can just move  this over here so I just want to put that in my start frame and if I hit press play there  is he's walking he's walking on the spot so I'm going to have to animate his position.  One thing I tend to do I'm not going to do it now but often I will change my timeline  to start at frame 1,001 and make it 1,001 to say 1,200 whereas the default starts at 0,000  but if you want to change that you go into here this little cog settings button and you  change out anyway let's go and make it proper so 1,001 and then my end frame is going to  be 1,200 so this is my start frame and my end frame and I'm just going to drag this animation  into that area so now if I click my mouse up here it will start playing that starting  at 1,001 and to zoom into this area I'm just going to change the time bar down here like  that so now I'm starting at 1,001 and here's the frame count to that shows you what frame  you currently on now the reason why I do this is because you know see you're starting  at frame 1 and you've got your shot and the character is doing something and you go that's  great but then you go actually ...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_006.jpg

### Understanding Animation Curves and Keyframing [8:32]
**Transcript:** animation and now what I want to do is just animate the character along so I'm going to select him  and here's his position so you can just drag it here and then I can animate here or here so you've  got a choice so the easiest way is if you just hit this little button here you've got little keyframes  so you can add a keyframe here and then you'll see in here it's added to keyframe too and that's my  transform track so this character has got a transform and there it is and that's your overall global  position of the character so I'll go to my end frame and then let's select him and move him  forward like this and then I can hit save there again I can hit that like that and it saves a key  or I'm just going to undo that control Z or you can use here so there's a button here so you can press  that one and save a key that will save a key on all of the transforms so to save individual elements  you're going to the transform then you go into a location then you can save your X, Y, Z or you can  hit all three there and then you've got a key so now you've got an animated key and then as you can  see he's going to start slow and he's going faster because it defaults to a a spline a like a...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_007.jpg

### Blending FBX Animations in the Sequencer [12:55]
**Transcript:** the next one and hopefully I can zoom in here a bit but so now I've got two tracks that are  separate little bits of animation but the thing I love is you can blend these together so if I drag  this one over the top of that one then it's actually going to blend those together so  like that so it starts to blend those animations so it's just fantastic I love that  which is great so I'm going to blend that and then I'm going to extend this by just dragging  this one and it started to repeat that animation so and it's going to drag him a bit more as well  so now what I'm going to do is select my whole character here so if I grab the top it's going to  select the animation and the transform and move those together so I can have that kind of  start here now let's go look so there we go all right so she's waiting hurry up hurry up and then  they're going to start walking so now I'm going to animate her let's go to a first frame here  so look I'm going to save the key on her selected her Quinn pressed save key so save in my location  x1 z and then let's go and translate her along here oh I didn't save my key ah that was one thing  if you want to have automatic keys turned on use this butt...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_008.jpg

### Blocking Out Your Scene: Adding Props and Environments [14:37]
**Transcript:** and then me now she's going to have a chat with him fan that tastic so there's my animation so I  tend to block my animation first and then I'll put that into the environment and then and then  I'll start playing with the cameras and all those sort of things so let's have a look in the  starter content you have a look in the props and then there's a bench there we are grab a bench put  it down there I'm going to just rotate around there we are and then get back into sequencer  alright so they're walking past the bench so let's put something else so let's go into  content browser and she's standing next to what is this one what is that so I'm just going to play  for a little bit and make something stupid just to fill out this

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_009.jpg

### Animating Objects: Opening a Door [15:27]
**Transcript:** inspiration hit me so I'm going to have him walk through a door so he's going to walk through this  door and she's going to follow like she's been waiting there stalking him or something so I just  wanted to show you how to animate something in here so like here I've added the door and we want  swing open as he walks in so we grab the door from the outliner and we drag it into our sequencer  and now we've got a transform here so we can add it a key so let's go and let's open up the transform  go to rotation and I'm just going to grab all three so click there and then as he walks through  I will rotate this now xyz I'm not quite sure let's try oh there we go I got lucky so I'm going to  have that swing through like that so he'll go womp and then we'll have it swing back  and I'll like that and we'll make a little bit of overlap because we live a bit of overlap like that and then  like that so here we go rump  beautiful okay and if I wanted to edit that and play with it you're going to your curves  and then you can change your curve window I'm going to just grab that one rotation  like that and let's have a look let's have him start a bit more dramatic and here in the curves editor  ...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_010.jpg

### Setting Up Cameras: Creating Cine Camera Actors [17:51]
**Transcript:** there we are perfect okay so now I've got some animation I've got a little bit of environment  and then now what I'm going to do is add some cameras so we can animate some cameras so I'm just  going to frame it around like this so this is a little cheat that I like because often I'll kind  of like find a nice angle that I like and and so say I like this angle I'm going to tell  this into a camera that we can then add into the sequence and so what you do is you go up here  to these three little dots and then you say create camera here cine camera actor because it's  cine camera actors got some bells and whistles and things that the regular camera doesn't have so  cine camera actor like that and then that adds it into the outliner so we've got a cine camera  actor there I'm going to change its name to CM for camera wide so there's my wide camera and then

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_011.jpg

### Adjusting Camera Focus and Depth of Field [18:43]
**Transcript:** I'm going to show you how to change the focal distance so I'm just going to pick this frame here  and then I'm going to select my camera and I'm going to drag it into the sequencer so now in the  sequencer it's added a camera cuts track so this is your current camera that's playing and you  can have multiple cameras and then I'm going to select the current aperture and I'm going to  dial it down but it's not really having that much of an effect on it it's a little bit but if you  go into the actual camera here in the details panel it's actually under the lens settings there's  a minimum f-stop and a maximum f-stop so it kind of defaults the lowest point to 1.2 so we can override  that but with just typing 0.2 or something like that and now I can make this like really crazy  out of focus and you've got a lot more control which is something that I like and then you can see  here that they're not in focus so I focus them by going into the focus settings tab here and then  turn on something called draw debug focus plane and you click that on and it basically gives you  a purple wall where that focuses so at the moment it's set at 10,000 units away or whatever it is so  I'm just going t...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_012.jpg

### Cutting Between Multiple Cameras [23:48]
**Transcript:** amazing and then I'm going to go back to the main camera cut track by pressing that button there  and now it'll cut from the long to the wide so there it is there she's waiting it comes through  and then wow look at that so if you want to change your camera cut point you basically grab the  camera click on that camera track and then select the NC it turns into a little arrow thing  and then you can drag that cut point so you can make him start a bit later or I can make that cut  start earlier let's have it here just there so we grab that and just drag it to there like there

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_013.jpg

### Rendering Your Film: Using Movie Render Queue [24:30]
**Transcript:** we are in it cuts there then point so now we're ready to render so I'm going to show you the movie  render queue so pause that and then you find it here under this little clapper load there and you  click on that and then you go into that's your level sequence and here's your settings and the  moment it's got unsaved config which is the default and it basically gives you deferred rendering  and a jpeg sequence but I like to delete the jpeg sequence because I like to have an EXR sequence  it's got a bit more a lot more depth it's 16 bit it's got a lot more dynamic range  and that's what you would use in visual effects compositing so I like to have an EXR sequence  and I changed the compression from Piz which is quite big so the frames are quite large  and I change it to DWAA which is DreamWorks animation uh huh and then I don't need multi-layer  multi-layers if you want to have sub-channels don't worry about it turn that off now and then  deferred rendering that's your basically says use this one rather than path tracing and then we've  got our output here and that's where you put your name and all this sort of stuff so one thing I like  to do is turn on anti-aliasing so I'm going t...

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_014.jpg

### Applying Colorspace Transform in Your NLE [29:22]
**Transcript:** so those frames are now rendered and so I'm going to bring them into my editing package and I'm  using DaVinci Resolve but use what you love and then I'm just going to select first frame  and the last frame and then just drag those put them into here and then it makes them into a  little sequence so let's just grab my long shot drag it into my timeline and then take my white shot  put it in there so now I've got them and as you can see they're a lot darker because this is  not to mapped so I need to apply a color space transform onto it and then DaVinci you go into the color  page and then you select your node I'm going to add a serial alt s to add a serial select that node

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_015.jpg

### Next Steps - Subscribe for Next in the Series [30:00]
**Transcript:** look for color space transform and you drag that onto that node and then we change it in put  color space to srgb and then input gamma to linear and now it looks like it does on the  on inside of Unreal so there you are back to that but now you've got more range to play around  with your colors and things like that and you kind of nerd stuff that compositors like to do  all right well well fun well hopefully that's enough to kind of get you started and kind of point  in the right direction and then make sure that you like and subscribe by page so that you can  follow along for like more advanced versions of this and then get into the thing that I really  love which is virtual production where I use Unreal for making the environments but then use live  action on plates put that into the shots anyway all right nerd you know see you next time bye

**Frame:** tutorials\frames\make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta\frame_016.jpg


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
