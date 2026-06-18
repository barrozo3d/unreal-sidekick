---
title: The #1 Skill You NEED For Lighting in UE5
source: YouTube
url: https://www.youtube.com/watch?v=jAz4Lb93gwY
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [lighting, cinematics, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/the-1-skill-you-need-for-lighting-in-ue5/
frame_count: 11
---

# The #1 Skill You NEED For Lighting in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=jAz4Lb93gwY)
**Author:** Josh Toonen
**Duration:** 17m40s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** If you want to improve your lighting in CG,  the number one thing you have to do is practice.  And thankfully, real-time rendering has made it easier  than ever.  Now you can get instant feedback.  So instead of waiting around for half noisy renders,  you can jump right into the creative parts of lighting.  But I think there has to be a little bit of a mindset shift  around lighting in real time.  Because now we should be replacing those long render  times with more iterations and crafting the lighting  inside of our scenes.  So today I'm going to cover how I approach portrait lighting  and lighting characters inside of Unreal.  Now I am self-taught in lighting.  But I've spent the last eight years working  as an artist and supervisor working on Hollywood films  on movies like Star Wars and across the Spider-Verse.  And I use Unreal Engine on set and to create movies of my own.  And I first started learning Unreal  because film sets are so expensive.  Once you buy the gear, the lights, the cameras,  and hire the crew, the talent, your stand-ins,  it can cost tens of thousands for just a single shoot day.  By using Unreal Engine, we can practice  and improve our lighting and take al...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_000.jpg

### The Problem with 3 Point Lighting [1:19]
**Transcript:** has probably heard of three point lighting.  The idea that you have a key light, fill light,  and rim light surrounding your actor.  But I think there's a bit of a disconnect with this method.  I was given this advice early on,  but it wasn't clear why something worked sometimes  and other times it didn't.  And I think this loose framework can sometimes  lead to overlighting in simple scenes.  And it doesn't give you that confidence  when going into a scene and knowing exactly  where you should start placing your lights.  Because guess what?  The lighting system in Unreal only has five different lights  that you can use.  And I think there's a tendency to overcomplicate things.  At the end of the day, lighting is simple.  That doesn't mean it's easy, but it is simple.  And we need to think how can we use these five lights  to recreate the type of lighting that you would find  on a film set?  Well, the big concept I want to introduce to you  in this video is upstage lighting.  Now three point lighting is old school,  but by using upstage lighting, you can approach any shot  with characters, set up your camera,  and know exactly where you need to place your key light,  and dress othe...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_001.jpg

### The 2 Fundamentals of Lights [2:41]
**Transcript:** But before we get into that, we need to understand  the fundamentals and have a basic vocabulary  for how we need to place lights inside of our scene.  So there's two main factors that we need to know  for portrait lighting, and that's light direction,  and the size of the light.  So let's add some lights into our scene  and start creating a typical three point lighting setup  to see how light direction and the size of our lights  affects our character.  So I'm using this scene which is used in our Unreal  for VFX Fundamentals class where we're covering  how to build four different environments from scratch  and learn all of the fundamentals of Unreal along the way.  Check it out on Unreal for VFX.com slash waitlist.  So for an interior scene, we're really just  going to use these three lights, point lights,  spot lights, and rectangle lights.  So let's start by taking a point light  and dragging it into our scene.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_002.jpg

### Create a Light Rig (How to change your lights fast) [3:30]
**Transcript:** So the best way that I found a set up our lights  so we can start trying out different ideas really quickly  is to add an empty actor into our scene around our character.  And I'll call this our light rig actor.  And from here, it's really easy to take our lights  and sure to set them from stationary to movable  and drag them underneath our actor.  And now it makes it really easy to rotate our lights around  while being focused up and framed on our characters.  So right off the bat, I'm going to tint our light color.  But one thing I like to do is use this use temperature drop down.  Now, going into the cooler ranges above 6,500  tends to not make much of a difference  but using this for our warm lights can really help.  Typically for our backgrounds, I like to set fire lights  to something between 2,000 and 2,500.  But it's really important to note  that this goes insanely saturated orange on character's skin.  So typically, for anything that's on our character's skin,  we'll want to go back on the saturation,  especially on our costume where we want to retain  some of these blues.  Now I'm going to reduce the intensity just a bit.  So we're not clipping on our skin tones,  but we...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_003.jpg

### Spotlights vs Point Lights [5:07]
**Transcript:** Now, if we copy all of the settings from our point light,  so we'll change the intensity to 6,  our temperature to 3,500,  you'll see that we get a nearly identical result  between both of our lights.  The main difference between these two  is that we can focus our spot lights,  so it doesn't affect as much of our environment,  whereas point lights tend to spill light everywhere.  So a lot of times, I like to move point lights around  to find the location of the light,  to find a nice light direction and shadow  on character's faces, and then copy that over to a spotlight.  Another method is to change our outer cone angle  to 90 degrees, because if I rotate this light around,  you'll see that it's not so important,  the rotation of the light.  It's much more important to change the location of our light.  And once we're happy with the position,  it's really easy to go back in and change our cone angle  and really dial that in to exactly where we want.  Another thing we can do is we can cheat our attenuation radius  if we really don't want our lights to affect the environment.  You can decide exactly how far that light's going to cast,  but if you want to keep this true to life,  yo...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_004.jpg

### Light Size - When to Change It [6:29]
**Transcript:** and how that changes on our scene.  So most people, when they think of lights in Unreal,  they do think of these tiny point lights  or these tiny sources of light.  We can add in a rectangle light,  and just so we can have a direct comparison,  let's copy the location of our light  and change it to the same color temperature.  Now if we compare these two lights,  you'll see that our rectangle light has a much softer, shadow,  and smoother falloff.  And you can see by using this rectangle light,  we automatically get a little bit extra fill on our character.  Now why is that?  The only reason is the size of our light.  Our rectangle light has a larger surface  that it's casting light from.  So if I look at the difference here,  we'll see that we're actually casting light from this square.  And the rectangle light actually has some additional features  to change the size of our light.  So we have our source width and source height.  And if we set this to something like one,  very similar to our point light,  you'll see we get the same exact falloff as our point light  or our rectangle light.  But by increasing the size here,  we get a nice soft shadow across her face  and across her ...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_005.jpg

### On-Set Techniques [8:07]
**Transcript:** So it's very commonplace for gaffers  to soften a really harsh light bulb  by adding diffusion to the front of a light.  But once that beyond that is actually taking lights  and bouncing them off of white pieces of cloth  and diffusion to get an even softer light,  we're not casting that light directly at all.  And the way that we can mimic this in our scenes  is not by adding in bounce light  and letting Lumen approximate what that light would be.  But it's by creating dim rectangle lights  that have a really large surface area  like this white piece of cloth  with rectangle lights in our scenes.  The same goes for exterior scenes,  where it's not unexpected to throw these huge A by A grids  of diffusion to really soften the harsh sunlight  across actor's faces.  You can see the difference between the stand-in here  in the middle and the film crew behind him,  where you're getting these really harsh directional shadows  where our actor has a really nice soft fall off to his face.  So just because we have directional sun lights  in our ex-teriors or in our cave scene,  we can say that it would be torch light  that is lighting up our characters,  think of lighting like you're on a f...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_006.jpg

### Make Point Lights look like Area Lights [9:58]
**Transcript:** But I don't think a lot of people know  that you can actually change the size of your point lights  and spot lights by using the source radius options.  By raising the source radius to something like 50 or 100,  you can start to see that we get some really nice  soft lighting on our character's face here.  And we get a very similar result  to what we get from our rectangle light.  Now one other thing you can do is change your source length  and this will change your light from a point light  into a light tube.  We'll see that it actually creates a long source length here.  Now if we add a chrome ball into our scene,  it'll make it really obvious what this change in source length  does to our reflections and our specular.  And you can see that it creates a direct relationship  on our reflections and also how soft the light becomes  as it's cast.  Now this doesn't affect our shadows  as much as it affects how light is cast in the scene.  So you'll still get shadows that look like a point light.  If I rotate it around, it won't change the shadows  but it will change the reflection  and how the diffuse light is cast onto our scene.  And this is the same trick I used for these tracers  ...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_007.jpg

### Practicals - Motivate Your Lighting [11:27]
**Transcript:** is motivated.  And this is done on set by using something called practicals.  So these are light fixtures that will be placed  inside of the frame that are used to motivate  additional lights that are off camera.  So these could be hotel lamps or even candle lights.  And even though it looks like this candle light  is what's lighting our entire scene,  there's additional lights being used outside of the frame.  This is used by a lot of different DPs  but you'll see it all the time in Roger Deacon's work.  And it's a great way to make lighting  in your scene feel naturalistic  even when we're adding in additional lights.  So in this case, we have our two torches behind us,  which give us a reason to believe  whatever light we put next to our actress.  Whether it's a harsh point light  or a soft rectangle light,  just the fact that we have these lights right next to her  will make our lighting a lot more forgiving  even if it's not exactly true to life,  like a really small light source that you would get  from a torch.  In fact, if I turn off this light,  this is how much light is actually being cast  on our actress from the scene itself.  And oftentimes in interiors,  this is how y...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_008.jpg

### Upstage Lighting [14:20]
**Transcript:** is upstage lighting.  Now, upstage lighting is actually pretty simple.  So if we created an invisible line  where our actor is looking, we can call this our 180 degree line  or our eye line.  Because typically when you have two actors talking in a scene  and you're doing shot reverse shot,  we're gonna want our camera to stay behind this line  so we can easily make sense of the geometry of the scene  and we know that character one is talking to character two.  But this is also useful for upstage lighting.  So upstage lighting is the idea that our key light  is going to be behind this 180 degree line.  And as long as we keep our key light on this side,  it's really hard to go wrong with any light position.  And it's really just up to taste on where we want to place it  beyond this line.  Now, what this does is it forces our light  to always give us this rembrandt lighting  or this little triangle that we get underneath the eye.  Now, if we want it to be softer and flatter,  we can move our light further away  or if we want it to be really moody and contrasty,  we can move it right beside our actor's head.  But by keeping it behind this 180 degree line,  it's really easy to get a nic...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_009.jpg

### Unreal Fundamentals [16:31]
**Transcript:** So if you want to use some of these techniques  where you struggle learning on real and the past,  this entire environment was built  for my upcoming Unreal Fundamentals course,  which is aimed at getting people  whether you're a complete beginner  or you're an industry professional trying to migrate  over to these Unreal workflows.  We go step by step through creating four different environments  and teach you all the techniques and workflows  that you need to know along the way.  So you can start creating environments on your own,  covering all the different subjects like lighting,  effects, creating assets inside of Unreal,  working with characters and rendering out sequences  with AOVs and compositing them inside of new.  To create VFX shots and films.  So I put out a wait list, we're only accepting 50 people  because I want to make sure that this actually works  and answers all the questions that people have  as they're learning.  And we're going to be really hands on  with this first group of people.  So make sure to sign up if you want a little bit more support  when learning Unreal for the first time.  Go over to Unreal for VFX.com slash wait list  and you'll be the first t...

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_010.jpg


---

## Structured Notes

### Core Technique
Building a reusable light rig actor in UE5 for efficient character lighting: parenting lights to an empty actor, using temperature for warm/cool contrast, Source Radius for shadow softness, Source Length for tube lights, Rectangle Light for large soft sources, and upstage (behind-the-eye-line) lighting for cinematic Rembrandt-style character illumination.

### Summary
Josh Toonen teaches the single most important skill for cinematic character lighting in UE5: understanding how to place light relative to the camera-character axis and building a reusable light rig actor. Viewers learn to parent multiple lights to an empty actor (the rig) so they can test directions by rotating the rig without repositioning individual lights, use color temperature for warm/cool contrast instead of just brightness, tune Source Radius for shadow softness, extend Source Length for tube light aesthetics, and apply upstage lighting (key light behind the 180-degree line, similar to Rembrandt) for dramatic cinematic character illumination.

### Key Steps
1. Create a light rig actor: Quick Add → Empty Actor → name it "LightRig"; set Mobility = Movable.
2. Add all character lights as children of the rig actor: drag each light onto the rig in the Outliner.
3. Rotate the rig 360° to test all possible key light directions — find the angle that creates the most interesting shadow pattern on the character's face.
4. Use Temperature rather than Color for warm/cool control: enable "Use Temperature" on the light; warm fire = 2000–2500 K; cool moonlight = 6500–9000 K.
5. Adjust Source Radius for shadow softness: small radius (1–5) = crisp hard shadows; large radius (50–100) = soft diffuse shadows; choose based on light source size in the story.
6. Extend Source Length to convert a Point Light into a tube light: Source Length = 50–200; affects the shape of specular highlights on shiny surfaces.
7. Try upstage lighting: position the key light behind the actor (past the 180-degree line between camera and subject) so it creates a Rembrandt triangle on the near cheek and a strong rim on the back; this is the most cinematic single-light position.
8. Use a Rectangle Light for large area sources (windows, bounce cards): Rectangle Width and Height control the physical size; larger = softer shadows.

### UE Systems / Blueprints / Settings
- **Light Rig Actor**: Empty Actor; Mobility = Movable; all character lights parented; rotate rig to test directions without moving scene lights
- **Temperature**: Enable "Use Temperature" checkbox on any light type; 2000–2500 K = warm firelight; 4000 K = natural daylight; 6500–9000 K = cool night
- **Source Radius (Point/Spot Light)**: 1–5 = sharp shadows; 50–100 = very soft shadows; matches physical light source size
- **Source Length (Point Light)**: Extends Point Light into a tube/capsule shape; changes specular highlight shape on reflective surfaces
- **Rectangle Light**: Width and Height properties set physical dimensions; larger dimensions = softer shadows; good for windows and bounce panels
- **Upstage lighting**: Key light positioned behind the 180-degree eye line (between camera look direction and character); creates Rembrandt triangle on near cheek; physically motivated by fire, window, or practical behind the subject

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
lighting, cinematics, rendering, beginner

---

## Related Entries
- [[the-fastest-way-to-learn-lighting-in-ue5]] — 4-factor framework for direction, size, color, intensity
- [[unreal-5-secrets-every-filmmaker-must-know]] — 1–3 light setups and animated shadow rigs
- [[how-to-actually-improve-your-films-vfx-dune-in-unreal-5]] — backlight key placement and invisible lights for reflections
