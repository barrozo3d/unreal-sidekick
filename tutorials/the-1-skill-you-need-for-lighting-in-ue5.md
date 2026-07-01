---
title: The #1 Skill You NEED For Lighting in UE5
source: YouTube
url: https://www.youtube.com/watch?v=jAz4Lb93gwY
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [lighting, character, portrait, cinematics, practical-lights, rectangle-light, workflow, technique, upstage-lighting, shadows]
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
**Transcript:** If you want to improve your lighting in CG,  the number one thing you have to do is practice.  And thankfully, real-time rendering has made it easier  than ever.  Now you can get instant feedback.  So instead of waiting around for half noisy renders,  you can jump right into the creative parts of lighting.  But I think there has to be a little bit of a mindset shift  around lighting in real time.  Because now we should be replacing those long render  times with more iterations and crafting the lighting  inside of our scenes.  So today I'm going to cover how I approach portrait lighting  and lighting characters inside of Unreal.  Now I am self-taught in lighting.  But I've spent the last eight years working  as an artist and supervisor working on Hollywood films  on movies like Star Wars and across the Spider-Verse.  And I use Unreal Engine on set and to create movies of my own.  And I first started learning Unreal  because film sets are so expensive.  Once you buy the gear, the lights, the cameras,  and hire the crew, the talent, your stand-ins,  it can cost tens of thousands for just a single shoot day.  By using Unreal Engine, we can practice  and improve our lighting and take all the time we need  using just a laptop.  So today I want to share some of the frameworks  that have really worked for me  and I'll share some of my workflows  to iterate as fast as possible inside of Unreal.  So by the end of this video, hopefully you'll have the tools  and knowledge and confidence to create stunning portrait  lighting and understand how to make your shots  and environments look like your favorite Hollywood films.  Now everyone first dipping their toe into lighting

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_000.jpg

### The Problem with 3 Point Lighting [1:19]
**Transcript:** has probably heard of three point lighting.  The idea that you have a key light, fill light,  and rim light surrounding your actor.  But I think there's a bit of a disconnect with this method.  I was given this advice early on,  but it wasn't clear why something worked sometimes  and other times it didn't.  And I think this loose framework can sometimes  lead to overlighting in simple scenes.  And it doesn't give you that confidence  when going into a scene and knowing exactly  where you should start placing your lights.  Because guess what?  The lighting system in Unreal only has five different lights  that you can use.  And I think there's a tendency to overcomplicate things.  At the end of the day, lighting is simple.  That doesn't mean it's easy, but it is simple.  And we need to think how can we use these five lights  to recreate the type of lighting that you would find  on a film set?  Well, the big concept I want to introduce to you  in this video is upstage lighting.  Now three point lighting is old school,  but by using upstage lighting, you can approach any shot  with characters, set up your camera,  and know exactly where you need to place your key light,  and dress other lights around your scene you need.  And this technique is used in so many of my favorite movies  from big budget action blockbusters  down to intimate indie dramas.  And honestly, it works regardless of genre,  regardless of subject matter,  and gives you really clean, dynamic results every time.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_001.jpg

### The 2 Fundamentals of Lights [2:41]
**Transcript:** But before we get into that, we need to understand  the fundamentals and have a basic vocabulary  for how we need to place lights inside of our scene.  So there's two main factors that we need to know  for portrait lighting, and that's light direction,  and the size of the light.  So let's add some lights into our scene  and start creating a typical three point lighting setup  to see how light direction and the size of our lights  affects our character.  So I'm using this scene which is used in our Unreal  for vfx Fundamentals class where we're covering  how to build four different environments from scratch  and learn all of the fundamentals of Unreal along the way.  Check it out on Unreal for vfx.com slash waitlist.  So for an interior scene, we're really just  going to use these three lights, point lights,  spot lights, and rectangle lights.  So let's start by taking a point light  and dragging it into our scene.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_002.jpg

### Create a Light Rig (How to change your lights fast) [3:30]
**Transcript:** So the best way that I found a set up our lights  so we can start trying out different ideas really quickly  is to add an empty actor into our scene around our character.  And I'll call this our light rig actor.  And from here, it's really easy to take our lights  and sure to set them from stationary to movable  and drag them underneath our actor.  And now it makes it really easy to rotate our lights around  while being focused up and framed on our characters.  So right off the bat, I'm going to tint our light color.  But one thing I like to do is use this use temperature drop down.  Now, going into the cooler ranges above 6,500  tends to not make much of a difference  but using this for our warm lights can really help.  Typically for our backgrounds, I like to set fire lights  to something between 2,000 and 2,500.  But it's really important to note  that this goes insanely saturated orange on character's skin.  So typically, for anything that's on our character's skin,  we'll want to go back on the saturation,  especially on our costume where we want to retain  some of these blues.  Now I'm going to reduce the intensity just a bit.  So we're not clipping on our skin tones,  but we get a little bit of range in there.  And now we can start rotating this around  until we find a nice light direction.  But there's something I want to note about point lights  versus spot lights.  So let's bring in a spotlight into our scene.  Let's also set this to movable.  And let's right click this and attach to our light rig actor.  And let's copy the same exact location of our point light  and paste it onto our spotlight.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_003.jpg

### Spotlights vs Point Lights [5:07]
**Transcript:** Now, if we copy all of the settings from our point light,  so we'll change the intensity to 6,  our temperature to 3,500,  you'll see that we get a nearly identical result  between both of our lights.  The main difference between these two  is that we can focus our spot lights,  so it doesn't affect as much of our environment,  whereas point lights tend to spill light everywhere.  So a lot of times, I like to move point lights around  to find the location of the light,  to find a nice light direction and shadow  on character's faces, and then copy that over to a spotlight.  Another method is to change our outer cone angle  to 90 degrees, because if I rotate this light around,  you'll see that it's not so important,  the rotation of the light.  It's much more important to change the location of our light.  And once we're happy with the position,  it's really easy to go back in and change our cone angle  and really dial that in to exactly where we want.  Another thing we can do is we can cheat our attenuation radius  if we really don't want our lights to affect the environment.  You can decide exactly how far that light's going to cast,  but if you want to keep this true to life,  you definitely want to set this to at least a thousand,  if not higher.  So that's a very quick way to change the direction of our light,  which more importantly is the position or location of our light.  But the next thing we should look at is the size of our light,

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_004.jpg

### Light Size - When to Change It [6:29]
**Transcript:** and how that changes on our scene.  So most people, when they think of lights in Unreal,  they do think of these tiny point lights  or these tiny sources of light.  We can add in a rectangle light,  and just so we can have a direct comparison,  let's copy the location of our light  and change it to the same color temperature.  Now if we compare these two lights,  you'll see that our rectangle light has a much softer, shadow,  and smoother falloff.  And you can see by using this rectangle light,  we automatically get a little bit extra fill on our character.  Now why is that?  The only reason is the size of our light.  Our rectangle light has a larger surface  that it's casting light from.  So if I look at the difference here,  we'll see that we're actually casting light from this square.  And the rectangle light actually has some additional features  to change the size of our light.  So we have our source width and source height.  And if we set this to something like one,  very similar to our point light,  you'll see we get the same exact falloff as our point light  or our rectangle light.  But by increasing the size here,  we get a nice soft shadow across her face  and across her body.  And we could increase the size to make it even softer.  And this can really change how the light appears  on our character's face, especially around their nose,  which is bound to cast a shadow  if you have a really harsh directional light.  So as a rule of thumb, the bigger the light,  the softer the shadows, the smaller the light,  the harsher the shadows.  And I think it's really important to sort of thinking  of lighting in our CG scenes, like lighting on a film set.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_005.jpg

### On-Set Techniques [8:07]
**Transcript:** So it's very commonplace for gaffers  to soften a really harsh light bulb  by adding diffusion to the front of a light.  But once that beyond that is actually taking lights  and bouncing them off of white pieces of cloth  and diffusion to get an even softer light,  we're not casting that light directly at all.  And the way that we can mimic this in our scenes  is not by adding in bounce light  and letting Lumen approximate what that light would be.  But it's by creating dim rectangle lights  that have a really large surface area  like this white piece of cloth  with rectangle lights in our scenes.  The same goes for exterior scenes,  where it's not unexpected to throw these huge A by A grids  of diffusion to really soften the harsh sunlight  across actor's faces.  You can see the difference between the stand-in here  in the middle and the film crew behind him,  where you're getting these really harsh directional shadows  where our actor has a really nice soft fall off to his face.  So just because we have directional sun lights  in our ex-teriors or in our cave scene,  we can say that it would be torch light  that is lighting up our characters,  think of lighting like you're on a film set  and you have these real light fixtures at your disposal.  And the one we're trying to mimic Hollywood films,  the more our CG scenes will start to feel  like your favorite movies.  Another way we can do that with our rectangle lights  is by using these barn door settings.  There's a barn door angle and barn door length.  If you just set this barn door angle to zero,  it'll take these barn doors and really start to focus our light  in a really directional way.  And this is a great way to prevent our light  from spilling all over the scene  and start to focus it at our actor,  especially in these dark interiors,  where we want to be really selective  about where our light is being cast.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_006.jpg

### Make Point Lights look like Area Lights [9:58]
**Transcript:** But I don't think a lot of people know  that you can actually change the size of your point lights  and spot lights by using the source radius options.  By raising the source radius to something like 50 or 100,  you can start to see that we get some really nice  soft lighting on our character's face here.  And we get a very similar result  to what we get from our rectangle light.  Now one other thing you can do is change your source length  and this will change your light from a point light  into a light tube.  We'll see that it actually creates a long source length here.  Now if we add a chrome ball into our scene,  it'll make it really obvious what this change in source length  does to our reflections and our specular.  And you can see that it creates a direct relationship  on our reflections and also how soft the light becomes  as it's cast.  Now this doesn't affect our shadows  as much as it affects how light is cast in the scene.  So you'll still get shadows that look like a point light.  If I rotate it around, it won't change the shadows  but it will change the reflection  and how the diffuse light is cast onto our scene.  And this is the same trick I used for these tracers  in this tank scene, which I'll actually cover next week  in another light study tutorial  and we'll see how we can take these same lighting techniques  and apply them to environments.  Another important note is making sure our lighting

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_007.jpg

### Practicals - Motivate Your Lighting [11:27]
**Transcript:** is motivated.  And this is done on set by using something called practicals.  So these are light fixtures that will be placed  inside of the frame that are used to motivate  additional lights that are off camera.  So these could be hotel lamps or even candle lights.  And even though it looks like this candle light  is what's lighting our entire scene,  there's additional lights being used outside of the frame.  This is used by a lot of different DPs  but you'll see it all the time in Roger Deacon's work.  And it's a great way to make lighting  in your scene feel naturalistic  even when we're adding in additional lights.  So in this case, we have our two torches behind us,  which give us a reason to believe  whatever light we put next to our actress.  Whether it's a harsh point light  or a soft rectangle light,  just the fact that we have these lights right next to her  will make our lighting a lot more forgiving  even if it's not exactly true to life,  like a really small light source that you would get  from a torch.  In fact, if I turn off this light,  this is how much light is actually being cast  on our actress from the scene itself.  And oftentimes in interiors,  this is how you'll start lighting your scene.  So you'll build up your lighting one light at a time.  So in this case, let's keep our rectangle light.  And another thing that we get for free  by using this rectangle light is the eye light  that we get in the reflection of our character's eyes.  So if I zoom in further on our camera here,  you'll see that we get this nice soft square.  And it actually lines up to the size and shape  of our rectangle light.  So if I doubled the width again,  we would start to see that in the reflection of our eyes  as long as we have our eye shader set up correctly here.  Another subtle thing that isn't obvious at first,  but is a really nice rule of thumb  when blocking in interior scenes  is to make the focal point, the character,  make that the brightest thing in your scene.  It's a subtle thing when your eye immediately knows  where to look as opposed to adding in a really bright  point light in this background.  But this can really start to make our scene look unbalanced  and not have a clear motivation of where we're supposed to look.  In real life, we'd probably have more brightness cast  onto our walls from these torch lights.  But again, that's why it's really important to know  what reality should be and then make conscious creative choices  to create the world that we want to see on camera.  So oftentimes we would add in a rim light  and a fill light here, which don't get me wrong.  It can look very nice, but in a dark cave scene like this,  this can turn every setup that we have into studio lighting,  like you'd expect to see on a sound stage  as opposed to something that you'd find  by capturing this location in real life.  So I've started to walk back from using fill lights  and rim lights, although I definitely do like rim lights.  I think those are a nice way to separate our characters  from the background.  But I think the more important technique to know

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_008.jpg

### Upstage Lighting [14:20]
**Transcript:** is upstage lighting.  Now, upstage lighting is actually pretty simple.  So if we created an invisible line  where our actor is looking, we can call this our 180 degree line  or our eye line.  Because typically when you have two actors talking in a scene  and you're doing shot reverse shot,  we're gonna want our camera to stay behind this line  so we can easily make sense of the geometry of the scene  and we know that character one is talking to character two.  But this is also useful for upstage lighting.  So upstage lighting is the idea that our key light  is going to be behind this 180 degree line.  And as long as we keep our key light on this side,  it's really hard to go wrong with any light position.  And it's really just up to taste on where we want to place it  beyond this line.  Now, what this does is it forces our light  to always give us this rembrandt lighting  or this little triangle that we get underneath the eye.  Now, if we want it to be softer and flatter,  we can move our light further away  or if we want it to be really moody and contrasty,  we can move it right beside our actor's head.  But by keeping it behind this 180 degree line,  it's really easy to get a nice, dramatic looking shot  and it gives us a really clear position  of where we need to place our light.  Now, we can change the height of our light and the position,  but we always know roughly where our key light should be.  Now, from here we can still add in our rim lights  and at least we're aware of how and where we might add in our fill.  But oftentimes you can get away with your lights  by knowing exactly where to place it in your scene  to get a nice looking result.  I wish there was more to it,  but it just takes a lot of practice to dial in exactly  where we need to place our lights  to make them interesting to look at,  but also to be in line with whatever your taste is  for the scene you're trying to make.  So try using this technique, find that 180 degree line  and place your key light on the opposite side  and push it in every direction,  try different locations to see how they change  the feeling of the lighting in your scene.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_009.jpg

### Unreal Fundamentals [16:31]
**Transcript:** So if you want to use some of these techniques  where you struggle learning on real and the past,  this entire environment was built  for my upcoming Unreal Fundamentals course,  which is aimed at getting people  whether you're a complete beginner  or you're an industry professional trying to migrate  over to these Unreal workflows.  We go step by step through creating four different environments  and teach you all the techniques and workflows  that you need to know along the way.  So you can start creating environments on your own,  covering all the different subjects like lighting,  effects, creating assets inside of Unreal,  working with characters and rendering out sequences  with AOVs and compositing them inside of new.  To create VFX shots and films.  So I put out a wait list, we're only accepting 50 people  because I want to make sure that this actually works  and answers all the questions that people have  as they're learning.  And we're going to be really hands on  with this first group of people.  So make sure to sign up if you want a little bit more support  when learning Unreal for the first time.  Go over to Unreal for VFX.com slash wait list  and you'll be the first to know once it's ready.  So leave a like if you learned something new  and make sure to subscribe to Stick Around  because we'll be covering that tank lighting study  next week and go over how we did three different  lighting scenarios and how you can do the same  for your own scenes.  Thanks for watching and I'll see you next time.  Peace.

**Frame:** tutorials\frames\the-1-skill-you-need-for-lighting-in-ue5\frame_010.jpg


---

## Structured Notes

### Core Technique
**Upstage Lighting** for character/portrait work in UE5. Two fundamentals: light **direction** (position/location of the light source) and **size** (source area → soft vs hard shadows). Upstage rule: place key light behind the **180-degree eye line** (the invisible line where the character is looking). This guarantees a Rembrandt-style shadow triangle under the eye and prevents flat studio lighting. Pair with a **light rig actor** (empty actor parent → all lights as children) so you can rotate the entire rig around the character quickly.

### Summary
18-minute Josh Toonen tutorial (Hollywood lighting TD; Star Wars, Spider-Verse). Argues that 3-point lighting is too loose a framework — instead introduces **Upstage Lighting** as the #1 skill for character lighting in CG. Demonstrates using a light rig actor (parent empty actor) with attached movable lights to iterate quickly. Covers: point light vs spotlight (point to find direction, spotlight to constrain spread); rectangle lights (soft shadows from large source area, barn doors to focus, eye catch light in characters' eyes); Source Radius and Source Length to make point/spot lights behave like area lights; **practicals** (in-frame light sources that motivate off-camera key lights). Mindset: make the character the brightest thing; fewer lights is better; study film sets and real lighting rigs for reference.

### Key Steps
1. **Create a Light Rig Actor**:
   - Add an empty actor to the scene (Add → Empty Actor); name it "Light Rig"
   - Add lights (Point Light, Spot Light, Rect Light) and set them to **Movable**
   - Drag-attach lights as children under the Light Rig actor
   - Rotate the Light Rig parent to orbit lights around the character; translate to adjust distance/height
2. **Color temperature**:
   - Use **Use Temperature** toggle on lights; warm range (2,000-2,500K) for practical/fire lights on backgrounds
   - CAUTION: very warm temperatures (2000K) make skin tones go extremely orange — reduce saturation if targeting skin
3. **Point Lights vs Spotlights**:
   - Point lights spill light everywhere; good for quickly finding light direction
   - Once happy with position → copy to Spotlight; use outer cone angle to control spill
   - Starting trick: set Spotlight outer cone to 90° to behave like a point light while finding position; tighten cone once position is locked
   - Cheat attenuation radius if you want light contained (but physically accurate → set radius ≥ 1000)
4. **Light size for shadows**:
   - Smaller source → harder shadows; larger source → softer falloff
   - **Rectangle Light**: Source Width/Height control; at size 1 = same as point light; increase for soft shadows on face/nose
   - Mimics softbox or bounce card from film set
   - **Barn Doors**: set Barn Door Angle to 0 to focus rectangle light beam directionally (like barn door flags on a film light)
5. **Source Radius on Point/Spot lights**:
   - Source Radius 50-100 → soft light similar to rectangle light
   - Source Length → converts point light to a tube light (affects specular reflection shape, not shadow direction)
   - Check with a chrome ball in scene to see specular reflection shape
6. **Practicals**:
   - Add in-frame visible light sources (torches, lamps, etc.) that **motivate** off-camera keys
   - Reality: torch provides almost no light; off-camera rectangle light does the work, but torch gives visual reason to believe
   - Eye catch light: rectangle light creates a soft square reflection in character's eyes (matches light source shape)
7. **Focal point rule**: character (subject) should always be the **brightest element** in the frame; avoid adding bright background lights that compete with the subject
8. **Upstage Lighting**:
   - Draw an imaginary 180-degree eye line: the direction the character is looking
   - Place key light **behind this line** (on the far/upstage side)
   - Any position behind the line is safe; placement within that zone is taste-based
   - Close to the character's head → moody and contrasty (Rembrandt)
   - Further away → softer, flatter
   - Works for any shot: action, drama, close-up, wide
9. **Rim / Fill philosophy**:
   - Rim lights: useful for separating subject from background; use sparingly
   - Fill lights: can make dark interior setups look like sound stage; often better to skip and use Lumen's GI
   - Priority: key light placement (upstage) > rim > fill

### UE Systems / Blueprints / Settings
- **Five light types in UE** — Directional Light, Point Light, Spot Light, Rectangle Light, Sky Light; interior scenes primarily use Point/Spot/Rectangle
- **Light Rig Actor** (empty actor as parent) — rotates all child lights together; faster iteration than moving each light individually
- **Movable light** — required for Lumen to calculate dynamic GI from this light
- **Use Temperature** (on all lights) — set color in Kelvin; more realistic and predictable than HSV color picker; warm = 2000-4000K, neutral = 5500-6500K, cool = above 6500K
- **Rectangle Light → Source Width / Source Height** — physical size of the light surface; directly controls shadow softness (bigger = softer); mirrors diffusion panels / softboxes on film sets
- **Rectangle Light → Barn Doors** — Barn Door Angle (0 = fully closed/focused) + Barn Door Length; shapes the light output like physical barn door flags on film lights
- **Point/Spot Light → Source Radius** — makes point lights behave like area lights; raise to 50-100 for soft shadows; visible as yellow sphere in editor
- **Point/Spot Light → Source Length** — converts the point light into a tube light; changes specular reflection shape on chrome surfaces; does NOT significantly change shadow direction
- **Practicals** — film term: in-frame visible light sources that serve as diegetic motivation for off-camera lights; essential for naturalistic interior lighting
- **Upstage Lighting** — key light placed behind the subject's 180-degree eye line; guarantees Rembrandt lighting (triangle shadow under far eye); removes guesswork from key light placement

### Difficulty
Beginner-Intermediate. No technical UE configuration — pure craft/artistic technique. Fundamentals are simple; mastery requires practice and iterating across many different scenes and characters.

### UE Version
UE5 (real-time Lumen GI assumed; lighting fundamentals apply to UE4+ as well)

### Tags
lighting, character, portrait, cinematics, practical-lights, rectangle-light, workflow, technique, upstage-lighting, shadows

---

## Related Entries
- `recreate-the-lego-movie-style-in-unreal-engine-5.md` — 8 cinematic lighting techniques including bilateral rim lighting and motivated practicals
- `realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — PBL workflow; HDR Viewmode and quantitative lighting calibration
- `if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this.md` — exterior PBL practical walkthrough; EV100 curve; directional light placement
- `the-fastest-way-to-learn-lighting-in-ue5.md` — beginner lighting entry; complements this technique guide
