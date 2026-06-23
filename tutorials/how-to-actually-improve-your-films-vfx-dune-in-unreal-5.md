---
title: How to ACTUALLY Improve Your Films + VFX (Dune in Unreal 5)
source: YouTube
url: https://www.youtube.com/watch?v=Qun6BB6Q2tg
author: Josh Toonen
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-actually-improve-your-films-vfx-dune-in-unreal-5/
frame_count: 9
---

# How to ACTUALLY Improve Your Films + VFX (Dune in Unreal 5)

**Source:** [YouTube](https://www.youtube.com/watch?v=Qun6BB6Q2tg)
**Author:** Josh Toonen
**Duration:** 9m51s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Are you struggling to make your visual effects look as cinematic as your favorite Hollywood movies?  Well, don't worry, because all you need are these three shortcuts that I learned  recreating this war on a rackess from Doom Part 2.  Made entirely in Unreal Engine.  What's up, my name's Josh Tunin, and for the last eight years of work as a visual effects  artist and supervisor on movies like Star Wars, Dungeons & Dragons, and across the Spider-Verse.  And I started using Unreal Engine every day on set for the virtual production of Netflix's  Avatar the Last Airbender. And today, all you need are these three secrets to create cinematic  visual effects that you can start applying right after this video. Subscribe to the channel,  and let's get started.

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_000.jpg

### Lighting [0:40]
**Transcript:** So let's create this war on a rackess. Tunin people ask me, how do I make my renders look more  cinematic? Now it all starts with lighting, and this is where most beginners mess up. You might  be thinking we need to add lighting so it's light up our entire environment. This can usually make  your entire landscapes and characters look flat and boring. Most people get stuck adding lights when  we really need to focus on creating shadows. So if you want an instant shortcut to make contrast  in shadows in your image, then place your key light behind your actor. And the same is true whether  you're lighting a character or an environment. We can see our sun and create a lens flare in our  shot. This is great for the daytime, but the same applies for nighttime. We just need to convert our  sunlight into moonlight. So just like before, let's add that key light in behind our actors.  And now you can see all the surfaces and planes of our entire city. We can see the lights on top  and the shadows behind it to create a punchy contrasty image. Another beginner's mistake that you

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_001.jpg

### Invisible Lights [1:40]
**Transcript:** might be making is adding in all this light across your environment. Even though this doesn't make  sense at nighttime. Instead of shining bright lights on top of our whole environment, looking at  some references from some of my favorite movies, you can see that most of these nighttime shots  are reflecting these bright lights instead of having them cast directly into the scene. You can get  clever when you're in Unreal. By hiding invisible lights, we can add a bunch of well-placed  spotlights and lowering the roughness in the material of our city. All the surfaces will look more  reflective and shiny and we can fake some of those cool reflections that you'll see in your  favorite films. Now to take this one step further, I attached a simple point light to the Ornithaucer.  Even in a high speed chasing, we'll have that backlight right behind our character.

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_002.jpg

### Photography vs Cinematography [2:33]
**Transcript:** But let's stop right there. What's the difference between photography and cinematography? Photography  is only dealing with still images. But cinematography is all about making images that move. After all,  we're creating movies. Looking at the sequence from Dune, there's not a single shot here where the  camera isn't moving. And I think this is the biggest difference between static environment renders  and creating visual effect shots that look right out of your favorite Hollywood movies.  And I think this becomes obvious if we go look back at the original Star Wars pre-puls. These were  some of the first movies where they were experimenting with full green screen stages and digital environments.  You're doing lines against a blue curtain and it's really hard work. It's difficult to make that  believable. I don't know if I have. Pretty much every set has blue screen even if it's just out of  window or something. It's everywhere. People say why am I doing it? Is it the real question? Why not?  I think the biggest reason some of these shots don't hold up isn't because of bad visual effects.  It's because we have two actors standing still in the middle of this room with a static camera.  So let's start by animating our cameras and our characters. First, I'm going to start by animating

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_003.jpg

### Animating Characters [3:43]
**Transcript:** the characters, our ornithopters. And we're just going to set two key frames to have it fly through  space. Then let's add some rotation so we're getting a little bit of movement in our flight path.  Now to animate the wings, something really cool inside of Unreal Engine is that you can put a sequence  inside of a sequence. So I can just focus on animating the wings flying up and down and I can just  click and drag this into my new timeline to start combining the two together. Super easy.  Then we need to animate the camera. Try to think how would a real camera operator shoot this scene?

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_004.jpg

### Animating Camera [4:17]
**Transcript:** How far away would a plane or helicopter have to be to capture this footage in real life?  What type of lens would that camera operator use? The key here is to start simple. Start with two or  three key frames to block in your shot and get the timing down before you add in 10 or 15 different  key frames. Then continue to refine your timing until you're happy. What to take this to the next level,  a little secret is that you can generate camera shake entirely inside of sequencer. If you want to  mimic real life handheld cameras that cameras moving up and down rotating left and right,  you want to add noise to the translation and rotation of your camera. You need both to create  realistic handheld camera shake. We're just getting started. Now we have our animation, but we're missing  something huge. We're creating a war scene so we have to add explosions. This is where a lot of

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_005.jpg

### Explosions [5:05]
**Transcript:** people mess up. If you want your renders to look as good as your favorite films, then the name of  the game is photo realism. People think we need to use video game techniques to create our visual  effects, but that is not the way to approach filmmaking in Unreal. Most people don't know it's super  easy to add footage into Unreal. I got these explosions for free from my buddy Alex over at  Compositing Academy. By creating an image sequence in Unreal, we can load in any footage and even  use ones that have high dynamic range. Just drag that image sequence into your viewport and then  drag that into sequencer. Now you can slide this left and right just like an editing timeline.  Perfect that timing, change the size, scale and rotation, but we're not done yet. To take this  one step further, we can add in point lights where our explosions are and animate them brighter to  make these explosion blasts feel huge. Now they cast light dynamically in the environment just like  the real thing. I also modified the material and added a depth fade node so I could slide this  anywhere around our environment without getting any hard edges or seams. It's a simple trick,  but just animating the intensity of these lights and timing them to the movement of our final  explosion suddenly this pretty simple trick starts to become convincing. Now we get this interactive  light on the environment, on our atmosphere and casting onto our ornithopters. This is why  Unreal Engine is the ultimate filmmaking tool. You can make all of these adjustments all in real time  just like you're on a movie set. Rendering in Maya, Blender or Cinema 4D can take minutes or  hours to render out a single frame from your movie. It becomes impossible to imagine making a 10  minute, 20 minute or 90 minute film, but when working in Unreal it's not two times or 10 times  faster, it's exponentially faster because we're not waiting around for our final renders or focusing  on the creative parts of visual effects and filmmaking. We're not done yet. If we want our shots to

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_006.jpg

### Lens Flares [7:13]
**Transcript:** look photoreal, then we need to make sure our renders look just like a photograph, meaning  matching all the imperfections that you find shooting through a camera lens. That means we have to  add in lens flares. Don't worry, we don't have to go crazy with this, but we do have to add  something if we want our shots to look photoreal. Unreal Engine has some lens flare presets,  but these do not look photorealistic. Again, we're using these video game techniques and trying to  pass them off is photoreal and it's never going to work. So to amplify these explosions, I found  real life footage and images of lens flares and lens dirt so that I could composite them with my  final shot. By animating these with the impacts of each one of the explosions, we can start to create  something that looks perfectly photoreal. This is that hidden step that will make your shots look  true to life. Whether it's night times in explosions or adding an lens flare for your sun,  you cannot skip over this. As a last step, I threw on my one click compositing template. This adds

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_007.jpg

### Compositing [8:15]
**Transcript:** in 10 different lens effects that you'll find in every single photograph. All the things that I add in  every single time when I'm working on Hollywood films, I combine all of these settings into one  template with easy use sliders so you can apply that feature film look to your Unreal renders.  Look, if you're new to filmmaking, are you struggled learning Unreal in the past? I believe anyone  can start making Hollywood level films using Unreal Engine 5. I've already held 500 artists just  like you start making films from home inside of Unreal Fundamentals. You can go from a complete  beginner to an Unreal filmmaker in just 30 minutes a day without knowing how to code, how to model,  or how to animate. And by the end, you'll be able to create your own movies that look just like  your favorite Hollywood films. Get started right now at Unreal for VFX.com slash Fundamentals.  Or click the link down below and create your own visual effects in films today. Let's take a look at  the final shot.  I hope that gives you some ideas on how to level up your Unreal renders and make them look like  your favorite movies. My last video, I wrote this entire environment in just 24 hours inside of  Unreal 5. If you want to see how I did it step by step, join me in my free Dune Master class  over at unrealforvFX.com slash Dune. Click the link in the description and sign up today.  Otherwise, subscribe to the channel for more visual effects and filmmaking videos just like this.  Thanks for watching and I'll see you next time. Peace.

**Frame:** tutorials\frames\how-to-actually-improve-your-films-vfx-dune-in-unreal-5\frame_008.jpg


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
