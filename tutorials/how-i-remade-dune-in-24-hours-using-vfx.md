---
title: How I Remade Dune in 24 Hours using VFX
source: YouTube
url: https://www.youtube.com/watch?v=-syj6kFf6e4
author: Josh Toonen
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-remade-dune-in-24-hours-using-vfx/
frame_count: 11
---

# How I Remade Dune in 24 Hours using VFX

**Source:** [YouTube](https://www.youtube.com/watch?v=-syj6kFf6e4)
**Author:** Josh Toonen
**Duration:** 14m10s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Is this challenge possible? [0:00]
**Transcript:** I'm gonna recreate Dune in just 24 hours.  The visual effects of Dune took over a thousand different artists, and each frame took upwards  of 24 hours to render.  And at 24 frames per second, it would take over 591 years to render this out on one computer.  Now, I don't have that kind of time, but I believe anyone can make Hollywood-level visual  effects and films using this secret weapon.  Unreal Engine 5.  My name's Josh Tunin, and I used Unreal Engine every day on set for the virtual production  of Avatar the Last Airbender.  And I've spent the last 8 years working on Hollywood visual effects as an artist and  supervisor.  But today, I want to push Unreal Engine 2 its limits.  So in just one day, I need to build an entire city, animate the flying Ornithopters, and  somehow render out this entire sequence before time runs out.  All without million dollar budgets, and just using free software in the computer I have at  home.  So let's find out if I can recreate Dune in just 24 hours.  The clock starts right now.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_000.jpg

### Modeling the City of Arrakis [1:04]
**Transcript:** Alright, to kick things off, we're going to recreate this scene of the first flight of  the Ornithopters on the planet of Arrakis.  And that means we need to build this entire city as fast as possible.  Now D-Negg or Double Negative was the visual effects studio behind all of the visual effects  on Dune Part 1.  It took them hundreds of artists and over 45 artist years just to complete this.  Now all we have is 24 hours.  So I'm going to start with what I know and start with a cube.  Using the modeling tools, I'm going to build out 10 different buildings that we can clone  and populate around our entire city just to get started.  Now at this point, I'm just worried about the silhouettes, not final details.  So we'll stretch and squash and build some unnatural sci-fi buildings that match the  look and feel of Arrakis from the movie.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_001.jpg

### The VFX Technique I stole from Star Wars [1:55]
**Transcript:** Now that's a start, but I'll be honest, it looks pretty basic, so we need a way to add  lots of detail.  So I want to use a classic trick that I first heard about from the making of Star Wars  a new hope back in 1977.  Now you probably know the trench run of the X-Wings flying through the Death Star, but  how the heck did they make the Death Star look so detailed and complicated?  Well it all starts with one word, griebel.  Now that's not some alien creature, instead of modeling and detailing every last inch  of this practical model that they built with their hands, they would take pre-made model  kits and bash them together on the surface so that they'd get all this complicated detail  without constructing every piece by hand.  So we're going to steal this classic trick to add detail to our models without spending  a lot of time.  So one of the tricks in my tool bag is using this plugin called J-Splacement.  Instead of modeling every last detail by hand, we can use J-Splacement and displace our  model using this texture.  By displacing and adding all this tiny micro detail to our buildings, they're going to  start to feel huge up close.  Awesome, now we got the detail, but there's just one problem, everything starting to look

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_002.jpg

### Create ONE MATERIAL to texture entire cities [3:06]
**Transcript:** gray.  So we need to add in textures.  Now in real life, if you had a 3D model, you'd have to paint every last detail by hand,  and that's usually how it's done in CG.  But again, we literally don't have the time.  So I want to show you another trick that you can use to create entire cities using one  single material.  And that's by using world aligned textures in Unreal 5.  First I'm going to grab some free concrete sand and rust textures from Quixel Bridge, which  is completely free when you use Unreal Engine.  But in the material graph, instead of mapping these textures to a single object, we're going  to map these textures across the entire world.  So we can start by making a concrete base and making sure the scale of our scene looks  correct.  And then we can layer multiple world aligned textures on top of one another to add in those  layers of sand on top and rust underneath.  And then we can change the scale in size of all these different textures and start to break  them up in natural ways to add randomness across the entire city.  And what's even cooler is that these textures will look super high resolution when you look  at them up close.  So now that I have this material, I'm going to apply it to all of our different buildings.  And now we can even preview our displacement with the material on top.  And now it will automatically update based on all the new detail and geometry.  So by mixing displacement and world aligned materials, now we have our first set of buildings.  And I'm going to be honest, now that all the buildings are there, I'm not sure that  this is enough to build out an entire city.  So one thing I want to try is taking those grible textures and use those to create entire  blocks of the city.  So I'm going to take a plane and I'm going to subdivide the crap out of it.  So we have over a million polygons hidden inside this one plane.  And now when I displace it and I apply that world aligned material, suddenly the single  plane can turn into hundreds of buildings all in one go.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_003.jpg

### Why Maya and Blender are holding you back [5:06]
**Transcript:** Put your right hand in the box.  No, it's in the box.  Pain.  Now look, maybe you've used Maya or Blender or other 3D software in the past.  And the biggest restriction is that the more detail and geometry you add into your scene,  the longer you have to wait around to get your final result.  So what's so cool about Unreal Engine is you can literally add billions of polygons  into your scene and it'll still run smooth even on a laptop all in real time.  And all you have to do is enable Nanite.  So I made a couple of variations and now I think we have all of the buildings we need to  start creating the city.  And time check.  Alright, so now we're three hours in and we're just getting started because we still don't  have any of our landscape.  We need to somehow make this infinite expanse of mountains and sand to build out the planet

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_004.jpg

### Creating a Landscape in UE5 with Gaea [5:57]
**Transcript:** of a racquet.  So to create those landscapes, I'm going to use Gaia, which you can download for free right  now.  Gaia is great because we can make these sand dunes and these different mountain structures  all in a really easy procedural way.  And I want to use the same displacement method here where we'll generate these height maps  in Gaia and then import them into Unreal and simply displace our mountains into shape.  So after digging through some tutorials, now we have sand dunes and two different mountains  that we can use and bang bang boom.  I think we're finally done and now we have our Lego kit that we can start building out  the entire planet of a racquet.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_005.jpg

### Building and Rigging Ornithopters [6:40]
**Transcript:** Now we're on hour five.  Look you cannot make a movie without having characters.  So our characters are going to be our Ornithopters.  Now look, I am not a 3D modeler and honestly we are running out of time so fast.  So I'm going to go online and find an Ornithopter model that we can use to start this off.  Now using that cheat code of world line textures is not going to work for this model because  the textures are aligned to the world, not to the object itself.  So when we animate this, you can see the textures slide across as it moves.  So we need to find a different way.  So if we want to create textures that stick onto our model, we have to create the UVs.  Oh God, please no.  We need to texture it.  No.  And we need to rig it all inside of blender.  No.  Now UVing is a soul crushing boring experience but texturing is by far the most fun.  So I brought this in a substance painter and now we can add different metal shaders with  worn edges and start to detail this with brushes, grunges and noise patterns.  And then we'll add on sand and layer it on top of the metal.  So we give this really shiny metallic base and we have this rough sandy surface on top.  Now I'm not planning to see this up close so I'm going to call it quits pretty early here  but I'm pretty happy with the result.  But lastly, in order to animate this, we need to create a basic rig.  So I just made eight bones for all eight wings on the Ornithopter so we can rotate them  up and down and animate the wings and the flypad.  All right, let's get a time check and it is 16 hours in.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_006.jpg

### Assembling the City with our Asset Zoo [8:20]
**Transcript:** Okay, let's pedal to the metal.  If we don't have much time, we need to build the planet.  We need to create the cameras and animate our shots and somehow render this out while  still holding feature film quality.  So let's just jump right into it.  Now that we have our asset zoo, I'm just going to take these models and start building  some of these shots based on the scene from Dune.  So to start somewhere, let's create the city wall.  So on one half we'll build out the rest of the city and on the other half we'll have  our desert landscape.  Let's move these mountains into place and mess around with the rotation of the different  sand dunes and mountains so we can roughly match that original composition.  Now I'm going to use those grievell models for most of the surface and just use our models  to stick out and break up the silhouette of the entire city.  And then we'll build a little capital building at the very end of our cityscape.  Now let's just build this valley and duplicate a couple mountains into the background.  So it feels like we have this distant landscape and I think we got a pretty good base.  Okay, let's add in some fog, clouds and atmosphere and now we're talking.  Now we've got depth and this environment starts to feel huge because we can see those  mountains up close and super far away into the distance.  So now we really have four hours left and we still haven't animated a single thing.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_007.jpg

### Creating the Cameras and Animation in Sequencer [9:35]
**Transcript:** So let's do that next.  So I need to do a little bit of a flight test to make sure these wings work and the motion  blur looks correct just like in the original movie.  So I'm just going to animate these up and down super fast until we get about three different  up and down motions for every single second.  Okay, that's going to be good enough.  Our wings are flapping and now let's take these ornithopters and have them fly through  our scene and plot out a couple different cameras.  A lot of people think that you need to watch movies to get better at filmmaking but it's  simply not true.  You get better at filmmaking by making your own films.  Whether you're a complete beginner or you're trying to take your unreal renders to the  next level, try recreating shots from your favorite movies.  You can start to break down the filmmaking decisions that your favorite directors made  and start to understand why these movies work in the first place.  By the way, if you want to start making your own films in Unreal 5, check out our free  Unreal Crash Course over at onrealforvfx.com slash crash course.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_008.jpg

### Rendering in Less Than ONE HOUR [10:48]
**Transcript:** Okay, so we only have one hour left and like I said, on the original dude, a single frame  would definitely take more than one hour.  So how are we supposed to render out this entire sequence and bring it to that Hollywood  level?  Well, that's why I love using Unreal Engine 5.  Our viewport is in real time, which means our renders can be in real time.  So I'm going to use some of my lightning fast render presets to give us some high quality  renders, but a 30 second clip here will just take 30 seconds to render out.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_009.jpg

### The Last Step for Hollywood-level VFX (Don't Skip This) [11:22]
**Transcript:** So I've gone finally.  No, we're still going.  Let's finish this up.  Alright, so we have these rendered out, but how can we take these to the next level and  get rid of that video game stink that can come with some Unreal Engine renders?  Well, the last step that you can't skip over is compositing.  This is the step that will take our CG looking renders from looking like a video game to  making them look like they were shot through a real life camera lens.  Now I love working in real time, but when you get to the compositing stage, all of that  work slows down to a crawl.  So I don't want to do that, but I want to take all of the lens effects and those photo  real techniques that I use on Hollywood films and apply those to these renders.  So that's why I made the one click compositing template.  This will add a lens flares, lens effects and imperfections.  All the things I would add every day working on a Hollywood film and it'll apply it with  just a couple sliders.  So I'm just going to dial this in right here and render this out.  So we just have a couple second-fleft as we wait for these renders.  Let's take a look at the final result.  So it's finally done.  We created a rackess completely from scratch and made our own action scene in just 24 hours.  Now you don't need a ton of visual effects experience to create Hollywood level visual  effects using Unreal Engine 5.  I believe anyone can start making their own films using these tools.  And I want to help you do the same exact thing.  So if you're a visual effects artist or filmmaker and you have these big Hollywood level ideas  and you want to make them on a zero dollar budget, then join me in the live-doon masterclass,  this Saturday at 1 p.m. Eastern.  I'm going to share all the secrets and make this nighttime war on a rackess and show you  everything I did step by step.  And you don't need to know how to animate, how to model, or how to code.  Then sign up for our free dude masterclass at unrealforvfx.com slash dude.  If you show up, I'll give you this entire project for free.  But if you want to jump in right now and start learning Unreal, we have a free crash course  over at unrealforvfx.com slash crash course.  I'm going to give you the entire roadmap to start as a complete beginner to start working  at these visual effects studios or working on set in virtual production.  So check out those links below, make sure to subscribe, let me know what you think, and  I'll see you in the next video.  Peace.

**Frame:** tutorials\frames\how-i-remade-dune-in-24-hours-using-vfx\frame_010.jpg


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
