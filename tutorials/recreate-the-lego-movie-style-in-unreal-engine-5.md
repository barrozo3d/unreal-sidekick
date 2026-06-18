---
title: Recreate the LEGO MOVIE Style in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=TufXrvN5Ei0
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/recreate-the-lego-movie-style-in-unreal-engine-5/
frame_count: 10
---

# Recreate the LEGO MOVIE Style in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=TufXrvN5Ei0)
**Author:** Josh Toonen
**Duration:** 15m22s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Make Your Own LEGO MOVIE [0:00]
**Transcript:** We just made this LEGO music video for LEGO Horizon Adventures, made entirely in Unreal Engine 5.  But the lighting was done by recreating filmmaking techniques you normally find on set.  So today, I'll share 8 techniques you can use to improve your lighting, whether you're a 3D artist  or a live-action filmmaker. And I'll teach you some lessons I learned working on across the  Spider-Verse, that you can apply directly after this video. What's up, my name is Josh Tunin,  I'm a director, and for the last 9 years I've been working as a visual effects artist and  supervisor on Hollywood films. I move as like Star Wars, Risesky Walker, Dungeons & Dragons,  and across the Spider-Verse. But I started as a self-taught visual effects artist learning right  here on YouTube. That's why today, I'm holding nothing back, and I'll share the biggest lessons  and takeaways we learned creating the music video for LEGO Horizon Adventures. Combining the world  of Horizon, with Aloy hunting down machines, with the world of LEGO bricks. Make sure to subscribe  down below, and let's dive in. So the most important question is how do we light our characters,

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_000.jpg

### How to Light Characters [0:48]
**Transcript:** and make them look dynamic, and pop off the screen, just like the box art of your favorite LEGO sets?  Well, it turns out there's a simple recipe that you can use over and over again on any visual  effect shot. And I like to call this hot dog lighting. Now stick with me, this is a really good  tip. Let's look at this close-up of Aloy. Well, one of the best way to separate your characters from  the background is to add a strong rim light around the edge of your character, and the brighter the  better. Now I first started to notice this when watching the LEGO movie. If I pause on a frame  like this, you can see the white outlines around the edge of Emmett here on the right and left side.  And once you start looking for this, you'll start to notice it everywhere, and the key ingredient  is having both sides wrapped with light, not just one from your key light. If you look up close,  you'll even notice this yellow light coming from underneath, which gives the same idea of  creating another edge on our character. And this is where hot dog lighting comes into place.  Imagine Aloy is our hot dog running down the middle, and then our lights are going to be our buns  that are surrounding ou...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_001.jpg

### 1 Lesson I learned from Across the Spider-verse [3:04]
**Transcript:** from director Justin K. Thompson, that totally changed the way I look at lighting and animation.  Now the goal here is to think like a painter instead of trying to imitate real life. And it all  starts with a simple question. What color is miles suit? Well obviously, that color is black.  But now if you look at the background instead of miles, what's the only color you can't find  in the background? It's actually the color black. You can see all this fog and atmosphere behind  our characters. But what's important to notice here is the shadows aren't black. The shadows are  actually the color blue. And this is all by design. So by shifting our shadows into a brighter color,  we can emulate depth and atmosphere, but we can also push our characters forward. So in our  nighttime dance sequence, I wanted to make sure every shot follows this rule. The only thing that's  black in this image are the inclines of our LEGO minifigures and their black plastic hair.  Everything else turns into a color. This will punch out our characters to bring them forward  and separate them from all the atmosphere and fog, turning into solid colors in the background.  The same is true in a shot like this. We...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_002.jpg

### Lighting the Machines (Thunderjaw's Cave) [4:52]
**Transcript:** village can come together as friends. Even with Thunderjaw here, you'll notice that the only thing  that's truly black is the front of Thunderjaw's face. Everything else gets lifted and contaminated,  the further into the background it goes. On a frame like this, Thunderjaw's face pops out and  has some dark crisp shadows, and everything else goes bright and hazy into the background.  But if we zoom in on Thunderjaw's head, all of this is driven by the contrast between his shadows  and the fog behind him. But this isn't just limited to nighttime dance concerts. We did the

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_003.jpg

### Bow + Arrow Sequence Lighting [5:25]
**Transcript:** same exact thing during our bow and arrow sequence. If I pause on a frame like this, you'll notice  that the only thing that's black are the characters themselves. Everything behind them goes into this  light blue atmosphere. In this shot, as my eyes about to take down Sawtooth, we're doing the same  thing. The black LEGO piece is really how to create contrast, so his teeth stand out and make his  head and his claws much much easier to read. And even though there's a lot going on in this one  frame, hopefully when you're watching it, it's really simple and easy to understand. So try this  out by adding in layers of fog and depth behind your characters not in front of your characters,  and push it a little further than you're comfortable with. I'm constantly surprised how far you can  push this technique, and it creates so much clarity for your audience. But do you want to know the  biggest struggle we had when lighting characters? There was one mistake that kept happening anytime we

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_004.jpg

### The Biggest Struggle Lighting Characters [6:11]
**Transcript:** were close up on a character like this. Now what I didn't realize at first is that LEGO bricks are  extremely reflective. They are just shiny plastic bricks after all. But as soon as you stick a camera  on a minifigure's face, you see these white lines on the sides and chin of our character? These  are reflections of lights. Just like when you have a chrome ball behind the scenes of your visual  effects, because this ball is a mirror, you get a reflection of all the lights that are surrounding.  Well, these LEGO characters are no different. Because they're so shiny, anytime you place a  light up close, you'll get this fat reflection that totally covers up their expressions. Now they  were really clever about this in the LEGO movie. By always making sure those lights are to the left  in right of the inclines of their face. So we never have reflections crossing over the eyes or  face. But this is no accident. If you're not purposeful about this, you'll get crazy reflections  that cover up all your characters. Now the way to fix this is to change the position of your lights,  so that there's no reflections in the first place. And this is fine when the sun is really far  away. But ther...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_005.jpg

### Animating Your Lights [8:09]
**Transcript:** reflections appearing. And the way we got around this is by animating our lights. As soon as our  characters move up or down, we are literally changing the transformation of our lights to compensate.  And on really tricky shots like this, we would take a single rectangle light and put it overhead.  But then pair this light to the hips of our characters. That way, if they jump forwards or backwards,  that light is still beaming on their face. And this makes sure that all of the colors on her costume  are readable and not contaminated by the blue and purple lights in the background.  And the real secret here is applying this same exact recipe to every single shot in your film,  with really strong rim lights around Maya's hair, as well as a loy, and even adding in our hot dog  lighting onto our background characters with both purple and orange light. Plus, all of our  background characters are swept up into this blue and purple fog. By the way, if you want to make  your own visual effects and films just like this, check out our free Unreal 5 Crash Course at  unrealforvfx.com slash Crash Course. We'll take you from a complete beginner to making Hollywood  level visual effects and films...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_006.jpg

### Live-Action LEGO Lighting [9:45]
**Transcript:** we were able to use the same exact asset from the game. In the end, we really exaggerated a lot  of the lighting on the Tallnext so that we could get these really clear rim lights to highlight all  the edges and small Lego pieces that make up this asset. Plus, it really helped to exaggerate the  bounce light. As if all these Lego pieces are spread out on a coffee table and the sun is beaming in  from the window, bouncing off and making everything brighter. Next, let's talk about lighting our  environment. Now, so far, most of what you've seen are the final lighting approved versions of  each one of these shots. But these shots don't start off like this and it takes a while to find and  create the right look. Let's take a look at this wide shot, which is one of my favorites from the

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_007.jpg

### Environment Lighting (at night) [10:22]
**Transcript:** final piece. This was lit by Salva Gomez and our art director Simon Rizzo. And if I toggle between  the before and after, you can see how all these small changes can make a really big impact.  Let's walk through the three biggest adjustments we made from our first version to our final version.  The first thing is our rim lights. In this version, everything's a bit dark grey and smoky,  like everyone standing around a burning barrel, as opposed to our next version, which has a lot more  saturated color and really defined rim lights around our objects. Before you could easily miss that  cactus behind Thunderjaw there, but in this shot, we applied our hot dog lighting to our environment  and not just our characters, by surrounding and wrapping both sides of the geometry.  If I look at Thunderjaw here, you can see how much of a difference adding in this top light makes  to help separate it out from the background. But this is also true for things like our watchtowers  and cactuses. And here we're adding in additional lights to exaggerate the light source from these  paper lanterns here and from our blue moon light coming from the sky. Next, let's talk about our fog.  The biggest differ...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_008.jpg

### What makes lighting "cinematic"? [12:25]
**Transcript:** is if you want to make better movies, then you need to make your images move. That's the difference  between still photos and movies. So what that means for us is that we want to animate everything  we possibly can. That means lights from the stage, animating left and right, back and forth,  plus this interactive dance floor, so every step adds another layer of movement and our dance  and crowd, whether there's characters on the dance floor or up in the stadium,  everyone's bouncing around to the beat of the music. We also added movement to the speakers  and the torches to add some nice stop motion rotation and animation. Plus we're adding in camera  shake every time thunder just stomps onto the dance floor. The trick here is just like if you're  writing a good song, you still need to balance all these elements so they work together. So you'll  notice most of the background animation stays in the background. It's just adding some nice bounce  in movement without taking away from our main characters and their performance.  As a thank you for sticking to the end, I want to share one of my top secret pieces of advice  that will completely change all of your shots going forward. And I ...

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_009.jpg


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
