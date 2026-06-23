---
title: How I Made a Godzilla Cinematic in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=Og9za5-VCag
author: Josh Toonen
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-made-a-godzilla-cinematic-in-unreal-engine-5/
frame_count: 11
---

# How I Made a Godzilla Cinematic in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=Og9za5-VCag)
**Author:** Josh Toonen
**Duration:** 11m56s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Is this even humanly possible? [0:00]
**Transcript:** I'm gonna create my own Godzilla visual effects film to prove you don't need million dollar budgets.  You've seen Godzilla demolish entire cities at the movie theater,  but isn't possible to create these Godzilla level visual effects using completely free software  in the computer you have at home? Well, it's never been easier using Unreal Engine 5.  Godzilla returned to movie theaters in 2014, but you probably didn't know if the director,  Gareth Edward started out just like you and me as a self-taught filmmaker and visual effects artist.  Now, 10 years later, I want to find out what it takes to create these Godzilla level visual effects  yourself. What's up, my name is Josh Tunin, and for the last eight years I've worked as a  visual effects artist and supervisor on movies like Star Wars 9 and even Godzilla vs. Kong.  But more recently, I used Unreal Engine on set for the virtual production of Avatar the last  air vendor. And I've seen just how powerful Unreal Engine is for filmmaking and visual effects.  Now, I want to create my own Godzilla short entirely in Unreal 5, and I want to take you behind  the scenes with me. Subscribe to the channel and let's get started.

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_000.jpg

### Getting Godzilla into Unreal 5 [1:14]
**Transcript:** So there's three big challenges we'll have to tackle. The first, taking Godzilla and bringing  him into Unreal so we can start animating our sequence. Next, how can we create an entire city  that looks believable and cinematic? And lastly, what are those Hollywood visual effects techniques  that you can start applying to take our shots to the next level? So let's start by finding a  Godzilla model that we can bring into Unreal. I did some digging and found a really great model  off of Turbo Squid. It was modeled, textured, and rigged, and no joke. This morning, I was on LinkedIn  and this post popped up on my feet from Sonal Deep. And he was showing off this rig that he made  for a creature so you could animate them directly inside of Unreal using Control Rig. So I sent him a  DM and sure enough, he was down to help out on the project. So I wanted to create Godzilla's first  attack on this city. So I plotted out different cameras and different angles, and to me, filmmaking  is all about perspective. What point of view do we want to tell the story from? To me, the scariest

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_001.jpg

### How to Think Like a Filmmaker in Unreal [2:07]
**Transcript:** perspective is running away from this giant behemoth that could crush you at any second. So the first  step is green-shotting a couple different shots and trying out different camera angles to piece  together a story. To speed things up, I got this Tokyo City asset pack from Big Medium Small.  These had buildings, characters, and storefronts so I could start building out my city street. And even  if it's basic, I can start blocking in these animated shots. I can add some animation to Godzilla,  move the buildings around to create an interesting look, then I took all these crowd characters and

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_002.jpg

### Beginner's Method to Animating Crowds [2:50]
**Transcript:** imported them into Mixamo.com. To this day, Mixamo is super underrated and it's the easiest,  fastest way to get free rigs and free animations directly onto your characters. In this way,  I could get three animations of this crowd running for their lives away from Godzilla.  In Unreal, it's super easy to combine all these animations together and blend between a few,  so you can actually start crafting a performance throughout an entire crowd of people without dropping  a single keyframe. So using this method, I could animate this entire crowd in just a couple minutes.  And now I have my previs. So I rendered out all these shots to assemble them in an edit so I  could add in music and start to find the pace of this intro. Now our animation and our city are  underway, but we're just getting started. Next, we need to transform this one street into an entire  city. So I'll build that next by sent over the previs and animations over to my buddy John  Abinheim over at Watch Me Animator. He's a super passionate animator and he was up for the challenge  of trying to get this whole thing together in just a week. And this was his first time animating  everything inside of Unreal Engine, but he managed to pick everything up in just a single day.  That way he can focus on what he's great at and I can focus on the lighting and effects.  So the next step here is to take this from daytime into night. Now in my head, I thought this

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_003.jpg

### Day to Night Environments Lighting [4:06]
**Transcript:** was going to be easy. You put the hardest part about nighttime is that there's thousands of  lights that we need to recreate. We'll need moonlight, street lights, head lights, office buildings  and storefronts. If we look back at Godzilla 2014, this final battle looked amazing in theaters,  but if you watch it at home today, you can't exactly tell what's happening because it's so dark.  And sure, if the sky is black and the power grid is destroyed, this is probably realistic,  but we didn't start making a monster movie to be locked in the reality. So let's start lighting  up the city. Down at the street level, I started adding in lights around the storefronts to boost  that light onto the characters. Then I added in car headlights and to make Godzilla feel huge,  we need to make sure everything else feels really small. And we can do that by having his foot  traveling down the entire street. Then I animated some explosion lights brighter and darker around  the impacts of each step. The idea here is to add explosions, but we'll get to that later. Next,

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_004.jpg

### Environment and World Building Shortcuts [5:04]
**Transcript:** how can we create an entire city that looks believable and cinematic?  I think a huge beginner mistake with Unreal is overbuilding your entire environment. You don't  actually need a 3D model for every single asset in your scene. When there's things really far  into the background, you can actually use images instead of 3D models. At a Visual Effects Studio,  these are known as matte paintings or DMP. By finding real images of cities far in the  background, I don't need to worry about modeling an entire city with all these thousands of lights.  I can just use big images and hide them behind our buildings so you can't tell where one starts  and the other ends. Not only is this more realistic, it's also way faster, so make sure to use this  in your own scenes. So from here, I just duplicated a bunch of images of Hong Kong and placed them  in the background. But to take that one step further, we just need more buildings so it feels  like this complex cityscape. So I grabbed a couple extra models from KitBash 3D. This way, I could  add more variation and height to the buildings and then rotate, scale them up and down, so I can make  these 4 or 5 buildings look like 40 or 50. These models don't always look good up close, but they're  perfect for the background. But now these buildings are completely dark, so I had to add in these  office building lights. So instead of modeling these from scratch, I just took images of office  buildings and turned them into decals with an emissive input so they could literally start  lighting up the rest of the city. And by using real images, it'll make our scene look true to life.

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_005.jpg

### Use this VFX Technique from Godzilla vs Kong [6:32]
**Transcript:** Now this is starting to look pretty cool, but this is where most artists stop. And it's probably  why your shots aren't at that next level. So to take our city even further, I want to use this  technique I first used on Godzilla vs. Kong. Back in 2019, I had my first opportunity as a lead  compositor and it was my job to set the look of the Hong Kong sequence, starting with these first two  shots. And I found a really cool way to mimic volumetric fog. If you look at these foggy images  of Hong Kong at night, you'll see thousands of street lights and all these glowing neon signs  cast volumetric fog into the air. So instead of simulating all of this, it was faster and easier  to create cards in 3D space. Just like you can use cloud cards to create atmosphere, I used these  fog cards to add different color and depth throughout our entire city. Instead of relying on the  volumetric fog system, I just took these simple images of this light follow up and I started placing  them throughout the city. And using a depth fade node, I could spread this out across several buildings  so that light would travel between several different streets. So I placed nice cool blue light in  the sky and have the red and yellow street lights underneath. I even added in orange ones to  accentuate the explosions. So by adding small light sources and glow cards, I was able to transform  this entire city shot to make it look way more cinematic and complex. Now a rock in, but what are  those Hollywood visual effects techniques that you can start applying to take our shots to the next  level? The first thing I had to add was rain. Creating that downtown battle, I'm proud of a lot of

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_006.jpg

### The Secret to Photoreal Rain in Unreal [8:02]
**Transcript:** that work, but they're still part of me that wishes we could go back and add rain into that entire  sequence. Now it's not nearly as simple as just pressing a single button, but now we can create  our own sequence so I had to push it to that next level. So I started off by adding in Niagara  particles to add rain into the shot. Now this was a great start, but something about it seemed a  little too simple and I wanted to push it further in compositing. So I had to render these out as a  separate pass. Now most people way over complicate this part of the process. All we need to do is  copy the camera and the rain into their own sequence and just render that out. And then I can  bring this into Nuke to create the final shot and combine it with live action footage of rain.  I wanted to do the same thing with explosions, smoke, and sparks so we could add in that destruction

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_007.jpg

### Level-Up Your Renders with NukeX [8:53]
**Transcript:** into the city. So I got some spark and smoke elements from compositingacademy.com and brought  those into Nuke. Now is the last step. We just need to right click our camera inside of Unreal  and export that so we can import it into Nuke. And then to mimic our exact camera movement,  I just need to use an image plane node in Nuke and I just plug in my camera and my stock footage  and tell it how far we want to place it in depth and now our stock elements have the same exact  camera move. I also rendered out a depth pass out of Unreal, which we can use in a really cool way.  We can stretch and squash this depth pass to block out all of the things in the foreground so we  can really make it look like those sparks exist in a real 3D space. And now we can blend the smoke  and spark elements with our environment. And I did the same thing for Godzilla's roar,  adding in real footage of smoke and matching the movement and position of Godzilla. And then I got  those final animations back from John so I could swap them out. Now this is super important because  in visual effects so many people think they have to do everything themselves. But that is not true.  You're not limited by your own resources, you're limited by how resourceful you can be.  And that means reaching out to other artists who want to be filmmakers just like you.  So I just re-rendered each shot which was super fast because we're using Unreal Engine.  And then I added my one click compositing template to add in those last lens effects and now  we're ready to render out the final shots. Let's take a look at the final sequence.

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_008.jpg

### Watch the Full Cinematic [10:22]
**Transcript:** And there we go. We're able to build out an entire sequence. But you didn't think that

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_009.jpg

### Join the Godzilla Masterclass (link in bio) [11:18]
**Transcript:** stopped there, did you? Subscribe to the channel, check it out next week and show you how we added  in the plane animation, destruction, tracer fire, musul flashes and fracturing effects to bring  this entire sequence to life. Now if you want to sneak peak and you want to dive deeper into  Unreal filmmaking, then join me for the live Godzilla Masterclass. It's a free event this week and  I'll show you my best secrets to start creating your own films as a complete beginner in Unreal 5.  And we'll show you how to go from that first idea to a finished film. All those links are down  in the description. So check that out, make sure to subscribe and I'll see you next time. Peace!

**Frame:** tutorials\frames\how-i-made-a-godzilla-cinematic-in-unreal-engine-5\frame_010.jpg


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
