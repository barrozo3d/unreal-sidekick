---
title: Recreate the LEGO MOVIE Style in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=TufXrvN5Ei0
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [lighting, cinematics, rim-light, fog, depth, niagara, character-lighting, compositing, stylized, workflow]
extraction_status: complete
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
**Transcript:** and make them look dynamic, and pop off the screen, just like the box art of your favorite LEGO sets?  Well, it turns out there's a simple recipe that you can use over and over again on any visual  effect shot. And I like to call this hot dog lighting. Now stick with me, this is a really good  tip. Let's look at this close-up of Aloy. Well, one of the best way to separate your characters from  the background is to add a strong rim light around the edge of your character, and the brighter the  better. Now I first started to notice this when watching the LEGO movie. If I pause on a frame  like this, you can see the white outlines around the edge of Emmett here on the right and left side.  And once you start looking for this, you'll start to notice it everywhere, and the key ingredient  is having both sides wrapped with light, not just one from your key light. If you look up close,  you'll even notice this yellow light coming from underneath, which gives the same idea of  creating another edge on our character. And this is where hot dog lighting comes into place.  Imagine Aloy is our hot dog running down the middle, and then our lights are going to be our buns  that are surrounding our characters. And the more you push this, the better your characters will look.  This looks even better when you add two colors instead of just one,  drapping on each side of your character. So during the daytime, we'd have sunlight on one side  and blue light on the other, and it can look even better at nighttime. The goal is to think like an  illustrator and create these bright white lines around our characters. You can see in this shot of  Varle how extreme we're pushing the rim lights to create really graphic edges and lines on our  characters. And to tie them into the environment, this look is made by making gigantic rectangle lights  on the side of each character. We'd have our white neutral light hitting the face,  and having the other reflections match the color of the environment. But it's important to note that  these are not real reflections. All this lighting color is fake. Like this purple hue here,  matching the purple of the fog. We're exaggerating the lighting to make it look like the background is  wrapping around our character. And that wrap is what makes it hot dog lighting. And the best way to do  this is to make sure the lights are behind your characters. The next time you're lighting a  character, think how can I add more shape and outlines to the rim lights? Because even in a shot  like this, you only need one or two lights to really make a big difference.  Next, let me share a trick I use on these shots that I learned from across the spiderverse,

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_001.jpg

### 1 Lesson I learned from Across the Spider-verse [3:04]
**Transcript:** from director Justin K. Thompson, that totally changed the way I look at lighting and animation.  Now the goal here is to think like a painter instead of trying to imitate real life. And it all  starts with a simple question. What color is miles suit? Well obviously, that color is black.  But now if you look at the background instead of miles, what's the only color you can't find  in the background? It's actually the color black. You can see all this fog and atmosphere behind  our characters. But what's important to notice here is the shadows aren't black. The shadows are  actually the color blue. And this is all by design. So by shifting our shadows into a brighter color,  we can emulate depth and atmosphere, but we can also push our characters forward. So in our  nighttime dance sequence, I wanted to make sure every shot follows this rule. The only thing that's  black in this image are the inclines of our LEGO minifigures and their black plastic hair.  Everything else turns into a color. This will punch out our characters to bring them forward  and separate them from all the atmosphere and fog, turning into solid colors in the background.  The same is true in a shot like this. We want Maya and Aloy dancing together. So now both  characters have dark inclines, but our background character, Varro back here, isn't important in this  shot. So we'll shuffle them off into the background. And this is all done by placing fog cards  in atmosphere behind our characters. This way our fog has zero contamination on our characters,  but has full contamination on the background. And we push this a lot further in compositing.  Now the goal in this video is to improve your creative eyes, so hopefully now you can see these  shots in a totally different light. And in case you're wondering, this isn't just limited to LEGO  minifigures. This works for any character or creature you can think of. In this shot, we have  Thunderjaw, the final boss of the game, but we're inviting him to the dance party so the whole

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_002.jpg

### Lighting the Machines (Thunderjaw's Cave) [4:52]
**Transcript:** village can come together as friends. Even with Thunderjaw here, you'll notice that the only thing  that's truly black is the front of Thunderjaw's face. Everything else gets lifted and contaminated,  the further into the background it goes. On a frame like this, Thunderjaw's face pops out and  has some dark crisp shadows, and everything else goes bright and hazy into the background.  But if we zoom in on Thunderjaw's head, all of this is driven by the contrast between his shadows  and the fog behind him. But this isn't just limited to nighttime dance concerts. We did the

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_003.jpg

### Bow + Arrow Sequence Lighting [5:25]
**Transcript:** same exact thing during our bow and arrow sequence. If I pause on a frame like this, you'll notice  that the only thing that's black are the characters themselves. Everything behind them goes into this  light blue atmosphere. In this shot, as my eyes about to take down Sawtooth, we're doing the same  thing. The black LEGO piece is really how to create contrast, so his teeth stand out and make his  head and his claws much much easier to read. And even though there's a lot going on in this one  frame, hopefully when you're watching it, it's really simple and easy to understand. So try this  out by adding in layers of fog and depth behind your characters not in front of your characters,  and push it a little further than you're comfortable with. I'm constantly surprised how far you can  push this technique, and it creates so much clarity for your audience. But do you want to know the  biggest struggle we had when lighting characters? There was one mistake that kept happening anytime we

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_004.jpg

### The Biggest Struggle Lighting Characters [6:11]
**Transcript:** were close up on a character like this. Now what I didn't realize at first is that LEGO bricks are  extremely reflective. They are just shiny plastic bricks after all. But as soon as you stick a camera  on a minifigure's face, you see these white lines on the sides and chin of our character? These  are reflections of lights. Just like when you have a chrome ball behind the scenes of your visual  effects, because this ball is a mirror, you get a reflection of all the lights that are surrounding.  Well, these LEGO characters are no different. Because they're so shiny, anytime you place a  light up close, you'll get this fat reflection that totally covers up their expressions. Now they  were really clever about this in the LEGO movie. By always making sure those lights are to the left  in right of the inclines of their face. So we never have reflections crossing over the eyes or  face. But this is no accident. If you're not purposeful about this, you'll get crazy reflections  that cover up all your characters. Now the way to fix this is to change the position of your lights,  so that there's no reflections in the first place. And this is fine when the sun is really far  away. But there's also shots like this where we need to create this really strong blue reflection  while avoiding any reflections on her face. Now there's no immediate cheat codes for something like  this. You just got to change the position. But one thing that also helps is changing the size of your  light. The bigger your light is, the bigger those reflections will be. In this shot of Emmett,  you can see that the reflections are really small and thin, like these long light tubes on the left  and right side of his face. But oftentimes what we would do in a shot like this is simply make our  light size a lot bigger. So instead of making a standard rectangle light overhead that's something  like this, we would make it huge. And we'd push it further away outside of the view of the camera.  So in this case, we had a blue light that affected her hair and a neutral light that affected her face.  And most of the time, you can remove these reflections by moving your lights further and further away.  But this gets a lot more complicated as soon as your character starts jumping around and dancing  throughout a scene. If I step through this shot, this was by far the hardest one to avoid these white

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_005.jpg

### Animating Your Lights [8:09]
**Transcript:** reflections appearing. And the way we got around this is by animating our lights. As soon as our  characters move up or down, we are literally changing the transformation of our lights to compensate.  And on really tricky shots like this, we would take a single rectangle light and put it overhead.  But then pair this light to the hips of our characters. That way, if they jump forwards or backwards,  that light is still beaming on their face. And this makes sure that all of the colors on her costume  are readable and not contaminated by the blue and purple lights in the background.  And the real secret here is applying this same exact recipe to every single shot in your film,  with really strong rim lights around Maya's hair, as well as a loy, and even adding in our hot dog  lighting onto our background characters with both purple and orange light. Plus, all of our  background characters are swept up into this blue and purple fog. By the way, if you want to make  your own visual effects and films just like this, check out our free Unreal 5 Crash Course at  unrealforvfx.com slash Crash Course. We'll take you from a complete beginner to making Hollywood  level visual effects and films using Unreal 5. I'll leave a link in the description below.  Next, let's talk about lighting our creatures. Now personally, I always like to shoot reference  footage in real life whenever I can. And this project was the perfect opportunity to build the  real life Lego Tallnext Set and see how it reacts to light. This way, I could try out some extreme  color combinations to figure out our color palette for the nighttime dance sequence. And by  shooting this through a real lens, you'll start to notice all the small imperfections and details.  Because we were working directly with Carilla, the game studio behind Lego Horizon Adventures,

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_006.jpg

### Live-Action LEGO Lighting [9:45]
**Transcript:** we were able to use the same exact asset from the game. In the end, we really exaggerated a lot  of the lighting on the Tallnext so that we could get these really clear rim lights to highlight all  the edges and small Lego pieces that make up this asset. Plus, it really helped to exaggerate the  bounce light. As if all these Lego pieces are spread out on a coffee table and the sun is beaming in  from the window, bouncing off and making everything brighter. Next, let's talk about lighting our  environment. Now, so far, most of what you've seen are the final lighting approved versions of  each one of these shots. But these shots don't start off like this and it takes a while to find and  create the right look. Let's take a look at this wide shot, which is one of my favorites from the

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_007.jpg

### Environment Lighting (at night) [10:22]
**Transcript:** final piece. This was lit by Salva Gomez and our art director Simon Rizzo. And if I toggle between  the before and after, you can see how all these small changes can make a really big impact.  Let's walk through the three biggest adjustments we made from our first version to our final version.  The first thing is our rim lights. In this version, everything's a bit dark grey and smoky,  like everyone standing around a burning barrel, as opposed to our next version, which has a lot more  saturated color and really defined rim lights around our objects. Before you could easily miss that  cactus behind Thunderjaw there, but in this shot, we applied our hot dog lighting to our environment  and not just our characters, by surrounding and wrapping both sides of the geometry.  If I look at Thunderjaw here, you can see how much of a difference adding in this top light makes  to help separate it out from the background. But this is also true for things like our watchtowers  and cactuses. And here we're adding in additional lights to exaggerate the light source from these  paper lanterns here and from our blue moon light coming from the sky. Next, let's talk about our fog.  The biggest difference between our two images is that our fog is a lot more saturated and blue,  as opposed to dark grey and black. Simon also added some really nice shaping and volumetric fog  underneath our bridge, which also helps pop that bridge forward and makes the whole shot feel  moodier and moonlit. We also went really extreme and pushed the fog even brighter behind our stadium,  which adds a lot more punch and depth to our entire landscape. And lastly, we added a lot more  shaping onto our environment. If you look under the bridge, you'll see that these new lights reveal  all the different planes and geometry detail of the LEGO bricks on the cliff down here.  We also added extra shaping around the watchtower and flooded the center stage with a lot more light,  so that at the end of the shot, you're just looking in the middle. There's also some nice subtle  but effective rim lights on our crowd characters. Whenever you look at concert photography,  they'll flood those entire rooms with fog and lights just like you'll see here. So we added  tons of lights behind our characters in the arena to pop them out, so when they're animating up  and down, make sure that movement is easily readable and graphic. Now one of my strongest beliefs

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_008.jpg

### What makes lighting "cinematic"? [12:25]
**Transcript:** is if you want to make better movies, then you need to make your images move. That's the difference  between still photos and movies. So what that means for us is that we want to animate everything  we possibly can. That means lights from the stage, animating left and right, back and forth,  plus this interactive dance floor, so every step adds another layer of movement and our dance  and crowd, whether there's characters on the dance floor or up in the stadium,  everyone's bouncing around to the beat of the music. We also added movement to the speakers  and the torches to add some nice stop motion rotation and animation. Plus we're adding in camera  shake every time thunder just stomps onto the dance floor. The trick here is just like if you're  writing a good song, you still need to balance all these elements so they work together. So you'll  notice most of the background animation stays in the background. It's just adding some nice bounce  in movement without taking away from our main characters and their performance.  As a thank you for sticking to the end, I want to share one of my top secret pieces of advice  that will completely change all of your shots going forward. And I call it the gladiator effect.  And of course I'm talking about gladiator from the year 2000. This was directed by the master  Ridley Scott and I think it's one of the best examples of depth and movement in cinema. Let's  break down this shot here so you can understand. In the opening battle, there's tons of fog,  atmosphere, smoke, ashes, debris, sparks, embers. And just adding these into your shots will  probably make them cooler. But there's something that gladiator does to perfection. Now in every shot,  you'll have your camera and you'll have your characters. And what most people do is they'll add  their particles and depth behind their characters. But what they do in gladiator is they put those  particles in between the characters and the camera. And this makes all the difference. Now with  smoke and embers almost touching the camera lens, they're going to move a lot faster and be a lot  bigger, having a bigger effect overall on your shots. Even in a scene like this, most people would  just have two characters talking in an empty room. But not really Scott. Instead, we'll flood the  entire room with candles and the finishing touch is placing one candle right next to the camera lens.  So the easiest way to upgrade your shots is to add particles in between your characters and your  camera. Now our approach for the dance party was to add in confetti. This way we could have particles  swirling around our characters and any opportunity we had, we'd have some out of focus close to  camera and it would add so much more movement and parallax, especially on these shots of thunder  jaw. These are just Niagara particle systems and it's not about how you build them. It's where you  place them in your 3d scene. The only hard part is doing it for every single shot in every single  sequence. But hopefully now when you watch this video you see it in a completely different way  and you have some tips and techniques that you can apply to your own work. If you want to make  your own films, I'll leave a link down below so you can watch the entire behind the scenes process  and I'll take you from the original pitch to the final delivery. Make sure to subscribe down below  for more advice and tips just like this and I'll see you in the next video. Peace!

**Frame:** tutorials\frames\recreate-the-lego-movie-style-in-unreal-engine-5\frame_009.jpg


---

## Structured Notes

### Core Technique
Cinematic lighting for stylized CG characters: 8 principles from a professional LEGO Horizon Adventures music video production. Core: "hot dog lighting" (strong bilateral rim lights wrapping both sides of character); colored shadows (lift blacks to a hue, never pure black in BG); fog layers BEHIND characters not in front; Gladiator Effect (particles between camera and subjects); animated lights parented to characters for dynamic shots.

### Summary
15-minute Josh Toonen (Hollywood VFX, Spider-Verse, Star Wars 9) breakdown of 8 cinematic lighting principles used on the LEGO Horizon Adventures music video in UE5. Not a technical settings tutorial — a creative director-level breakdown. Techniques: (1) Hot dog lighting — two strong rim lights wrapping both sides, exaggerated; (2) colored shadows — BG elements lift from black into a hue (blue, purple), characters stay black for contrast; (3) fog layering — depth fog behind characters, zero contamination in front (fog cards + compositing push); (4) LEGO specular reflection management — move lights to edge of inclines to avoid face reflections; (5) animate lights and parent to character hips for dynamic shots; (6) Gladiator Effect — particles/fog/debris between camera and subjects, not just behind; (7) environment hot dog lighting (rim wrap for environment geometry too); (8) reference everything in real life first (built physical LEGO set, photographed it).

### Key Steps
1. **Hot dog lighting (bilateral rim wrap)**:
   - Place two large rectangle lights BEHIND the character on both sides, wrapping edges
   - Push intensity high — bright white outlines on character silhouette
   - Add two colors: daylight side warm, opposite side cool/blue
   - Larger light → softer/larger reflection; position to avoid face reflections
   - Apply to environment geometry too, not just characters

2. **Colored shadows (never pure black in BG)**:
   - Background shadows should be a hue (blue, purple, etc.) — NOT black
   - Only the character's outline/inclines should be black (maximum contrast = character pops forward)
   - Lift background fog/atmosphere to a saturated color: increases depth, pushes characters forward
   - Fog cards behind characters (zero contamination on foreground character)
   - Push this further in compositing (mist/fog exaggeration)

3. **LEGO/shiny character reflection management**:
   - Keep all lights positioned at the edges/sides of inclines — never crossing over face/eyes
   - Larger light = larger reflection; push lights further away + make them bigger
   - For dynamic shots: separate blue hair light from neutral face light (two different sources)
   - For jumping/dancing characters: animate lights to track movement

4. **Animating lights (dynamic shots)**:
   - Parent rectangle light to character's hip bone
   - Light follows character through space — eliminates need to re-light every pose
   - Manually keyframe light transformations for extreme moves

5. **Gladiator Effect (foreground particles)**:
   - Standard approach: particles behind characters
   - Gladiator approach: Niagara particles between camera and characters
   - Close-to-camera particles = faster movement, larger apparent size, more depth/parallax
   - Used: confetti, fog/smoke, embers, candles near camera lens
   - Not about how to build Niagara systems — about WHERE to place them

6. **Real-life reference**:
   - Build/acquire physical object (LEGO set) → photograph under different colored lights
   - Reveals material behavior, reflection angles, color interaction before committing to CG
   - Especially valuable for non-photorealistic materials (plastic, LEGO)

7. **Environment lighting** (wide shots):
   - Apply hot dog lighting to set geometry (watchtowers, trees, bridges)
   - Saturate fog (avoid dark grey → push to blue/purple)
   - Add volumetric fog under bridges/arches for depth
   - Floodlight active areas (stage, dance floor) → push audience's eye to center
   - Use additional local lights to reveal geometry planes not lit by main source

8. **Cinematic movement**:
   - Animate lights in sync with music
   - Animate background elements: speakers, torches, crowd, dance floor
   - Camera shake when large character (Thunderjaw) moves
   - Balance: background motion should enhance, not compete with, foreground performance

### UE Systems / Blueprints / Settings
- **Rectangle Lights** — primary tool for bilateral character rim wrapping; position behind character on both sides; size affects reflection sharpness; parent to character bones for dynamic shots
- **Niagara Particle Systems** — confetti, embers, smoke/fog particles; placement BETWEEN camera and subjects (Gladiator Effect); key insight: placement > build quality
- **Fog Cards / Atmosphere layers** — place fog/mist elements behind character in Z-space to avoid contaminating foreground; layer saturation increases in distance
- **Exponential Height Fog** — environment fog; push saturation (e.g., blue moon scene); shape with volumetric fog for architectural depth
- **Light parenting to characters** — attach light actor to skeletal mesh bone (hips); light follows character motion automatically
- **Keyframed lights** — animate light Transform in Sequencer to compensate for character movement in close-up shots

**8 techniques summary:**
1. Hot dog lighting (bilateral rim wrap) — bilateral rim lights on both sides
2. Colored shadows — lift BG blacks to a hue; keep character inclines black
3. Fog layering — fog behind characters, not in front; compositing push
4. LEGO reflections — position lights at incline edges; size up and push back for clean faces
5. Animated lights — parent to hip bone; keyframe for extreme shots
6. Gladiator Effect — particles IN FRONT of characters, near lens
7. Environment rim lighting — apply hot dog technique to set geometry
8. Real-life reference — shoot physical reference under colored lights

### Difficulty
Beginner (concepts). All principles are cinematography-level creative direction applicable in any render engine. UE5-specific only for Niagara particle placement context.

### UE Version
UE5 (no specific minor version; principles apply broadly)

### Tags
lighting, cinematics, rim-light, fog, depth, niagara, character-lighting, compositing, stylized, workflow

---

## Related Entries
- `realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — PBL data-driven lighting workflow; technical counterpart to this creative approach
- `lumen-explained---important-tips-for-ue5.md` — Lumen GI; understanding real-time lighting behavior for cinematic work
- `master-cinematic-fog-volumetric-god-rays-in-ue5.md` — fog and volumetric lighting in UE5 (technical implementation)
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — Josh Toonen; action cinematics (same author/director)
