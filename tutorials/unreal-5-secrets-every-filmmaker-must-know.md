---
title: Unreal 5 Secrets Every Filmmaker Must Know
source: YouTube
url: https://www.youtube.com/watch?v=0Yc6qJSWet4
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [lighting, cinematics, camera, post-process, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-5-secrets-every-filmmaker-must-know/
frame_count: 8
---

# Unreal 5 Secrets Every Filmmaker Must Know

**Source:** [YouTube](https://www.youtube.com/watch?v=0Yc6qJSWet4)
**Author:** Josh Toonen
**Duration:** 15m3s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Do your renders look like a video game? [0:00]
**Transcript:** Unreal Engine is great for filmmaking, but the last thing you want is for your renders  to look like a video game.  So why don't your 3D renders look as cinematic as your favorite movies?  It's not because of the software, it's because of your technique.  All you need is Unreal Engine 5 and these three tips that you can start applying right  after this video.  So if you're ready to stop playing games and start making movies, subscribe to the channel  and together we'll break down three Unreal secrets to create cinematic, photo-real renders.  What's up?  I've been tuning in for the last 8 years I've worked on Hollywood visual effects as an  artist and supervisor.  I move these like Star Wars, Dungeons & Dragons and across the spiderverse.  And I started using Unreal Engine 5 on set in virtual production and to create animated  films of my own.  So I want to share 3 secrets that I learned from an upcoming Mr. Freeze short film made  entirely an Unreal Engine that you can use to immediately improve your renders.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_000.jpg

### How to make Renders look Cinematic [0:50]
**Transcript:** Now a lot of people have asked me how do I make my renders look cinematic?  And if I had to give the answer in one word, it would be lighting.  Now I've already made some in-depth lighting tutorials that you can check out, but I want  to share one of my favorite resources, Shot Deck.  Here you can find high resolution stills from your favorite movies and analyze why and  where they place the lights.  If you look at all of these different movies, you'll notice one thing in common.  All we have is a person standing in a room.  And yet some shots look boring and others look cinematic.  So what's the difference?  It's the lighting.  Simply the more dynamic the lighting looks, the simpler the lighting setup is.  In this case, it's literally just one key light that's lighting up this entire scene.  Or in shots like this, there's just one main light overhead lighting up his face and another  one coming from the side so that we get this rim light on the side of his forehead and  across the back of his shirt.  So cinematic lighting doesn't come from putting a ton of lights in your scene.  It's from putting one to three lights in the right places.  And oftentimes you just want to light one h...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_001.jpg

### Lighting Breakdown [2:08]
**Transcript:** So let's break down this lighting setup one light at a time.  The first light are these overhead lights, creating a lot of nice back light and also  fill light across the scene directly coming from these fluorescent lights in the background.  These are just images of fluorescent lights placed in the scene and plugging them into  the emissive channel and letting that do all of the hard work.  The next light is this overhead key light, which is really here to help separate Victor  from the background.  We want to avoid a completely monochromatic image, so getting it a little bit of a warmer  light in here helps separate him from the green background.  The third light is our rim light and this is just brought in to get a little more punch  in style and edge out of our character.  And again, you can see this really starts to light up the edge here and we want to brighten  up Victor's face so our attention goes directly to him.  And then as an accent, into incorporate the glowing eyes into the scene, I wanted to add  in this red under light, which helps tie everything together.  We get a little bit more color and it almost appears like the light is being cast from his  eyes onto the bri...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_002.jpg

### How to Animate Your Lights [3:25]
**Transcript:** But here's where a lot of people get it wrong.  Right now we're looking at still images or photographs, but if you want to make movies  and cinema, then you have to make your images move.  And we can do that by adding movement into our lights.  Let's jump into this scene with Mr. Freeze and check out how.  The first technique was taking this rope simulation and adding a light to it by creating  this simple physics interaction using a physics constraint and recording it using take recorder.  And by parenting a light to the simple interaction, we get this subtle but effective light animation  throughout our entire shot.  And you can see the shadows move across Victor's face.  The other technique is animating cast shadows.  As you can see, I didn't want to build a complicated environment, but I wanted the impression  of machinery and equipment moving in the background.  Instead of building complicated geometry, I just took this single spotlight and pointed  it at the background.  And then I found this fan in the Quixel library.  And by placing this directly in front of the light and adding a simple rotation animation  to the fan, the shadow implies a huge environment beyond what we ca...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_003.jpg

### The Secrets to Photorealism [4:45]
**Transcript:** So how do you make a photo-real render?  Well, let's break down the word photo-realism.  You need your renders to look like a photograph, meaning all the imperfections you get from shooting  through a camera lens.  Now, a shortcut to make your shots look more cinematic is to create shallow depth of  field with your lens.  This is how we get the large orbs and bokeh in the background of our images.  Now there's multiple ways to do this and I want to walk through both depending on your  shot.  Now, in sequencer, this is controlled within the camera.  I'll expand my Cine camera here and our two most important settings are going to appear  right at the top inside of sequencer.  And that's aperture and focal length.  Vocal length is the amount of zoom we have on our lens, which greatly affects the composition  of our frame and aperture controls the depth of field.  So the lower the number, the more out of focus, and the higher the number, the more focus  we'll have.  Now, if you're looking for a magic number, I usually start around two, but you can always  cheat this lower down to something like 1.4.  But be careful, as soon as you're getting into anything below one, we're creating a le...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_004.jpg

### Compositing for a Photoreal Image (The 3 Imperfections) [8:47]
**Transcript:** This is the last step of polish that we're putting on our finished renders to give them  even more imperfections and mimic all of the qualities of a camera lens.  And it's really important because if you skip a single step here, your shots won't look  photo-real.  Whether you use After Effects, Nuke or DaVinci Resolve, all these techniques apply.  So let's talk about the three imperfections that you want to add to every single render  to make something that looks CG and make it look photographic.  The first thing I always add in is lens diffusion.  This has the biggest impact and this one step can take images that look really CG and make  them look a lot more photographic.  So what's the biggest reason?  The biggest problem to overcome with CG is a lot of things can end up looking perfect  when they're created in a computer.  But by blurring our image, we can get a lot more imperfection and randomness that you'd  expect coming through a camera lens.  Oftentimes with CG, we'll get really crisp, dark blacks in our image.  But when you're using an anamorphic lens, oftentimes you'll get this really soft glow  coming from your light sources.  And as CG image, you might expect this silho...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_005.jpg

### Chromatic Abberation (The Right Way) [10:37]
**Transcript:** So on a shot like this, a little bit of diffusion can go a really long way in terms of contaminating  our blacks by adding haze onto our lens and into our environment.  The next step is adding in chromatic aberration.  A lot of times when shooting with cheaper or older lenses, you'll get some color separation  infringing around your brighter areas.  And this is known as chromatic aberration.  Essentially what happens is when light enters your camera lens, if that glass isn't perfectly  fine-tuned, by the time that light travels to hit the sensor of the camera where the images  captured are different wavelengths between the red, green, and blue can travel differently.  And oftentimes this is most notable around the corners of your lens.  Now this is definitely becoming more widely known in CG, but I think a lot of people are  implementing it in the wrong way.  With chromatic aberration, less is more, but it's really important to know how to apply  it correctly.  Let's take a look at this still from the assassination of Jesse James and see how this technique looks  when captured through a real camera.  When we go towards the edge of the frame, you can see that we get blue on one side...

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_006.jpg

### Level-Up as an Unreal Filmmaker [14:11]
**Transcript:** composing template that I used here, you might want to check out Unreal Fundamentals.  If you're new or struggling to learn Unreal and you want to take your work to the next level,  then you should check out our 21-Day Unreal Filmmaking Bootcamp to go from a complete  beginner to an Unreal filmmaker making your own animations and pre-vis inside of Unreal.  I've taken everything I've learned, every cheat sheet, every template, and every resource  and combine them all together in one place.  So take your future in visual effects and filmmaking into your own hands and get started  today.  And make sure to share what you create by the end of the course.  Subscribe below if you want to see more.  Otherwise, check out our behind the scenes of Tesseract's music video for War of Being.  We'll show you exactly how we made the Samurai Swordfight using motion capture and Unreal  Engine step by step.  Thanks for watching and I'll see you next time.  Peace.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_007.jpg


---

## Structured Notes

### Core Technique
Three cinematic secrets from the Mr. Freeze short film: efficient 1–3 light setups (key/rim/accent), animated light rigs driven by physics rope and fan rotation for organic shadows, and three compositing imperfections (lens diffusion, chromatic aberration, vignette) that make renders feel photographic.

### Summary
Josh Toonen reveals three production secrets used in his Mr. Freeze short film that elevate UE5 renders from "CG" to cinematic. Viewers learn a disciplined 1–3 light framework with key, rim, and accent roles, how to create organically moving shadows by parenting a spotlight to a physics-rope-simulated chain and a rotating fan, and the three compositing imperfections (lens diffusion with fall-off, correctly-positioned chromatic aberration, and vignette) that simulate real camera optics. Depth of field settings from the Cine Camera round out the tutorial.

### Key Steps
1. **Minimal light rig**: Use only 1–3 lights total; Key light = primary illumination and separation from background; Rim light = punch and silhouette; Accent under-light = colored fill from below for stylized effect.
2. **Animated pendulum shadows**: Create a physics rope constraint (Physics → Rope Component or Blueprint) with a spotlight attached at the end; record the rope swinging with Take Recorder; parent the spotlight to the rope end bone for organically moving shadow patterns.
3. **Fan rotation shadows**: Place a fan mesh with rotation animation (Sequencer transform track); position a spotlight behind the fan so its blades cast rotating shadow patterns onto the character.
4. **Cine Camera depth of field**: Aperture = f/2.0 for shallow DOF; note that focal length affects composition (longer = compression, closer background; shorter = wider, more space around subject).
5. **Lens diffusion**: Apply a post-process lens diffusion material; set Opacity/Fall-Off = 0.75 so the blur is stronger at frame edges and falls off toward center.
6. **Chromatic aberration**: Enable in Post Process Volume → Lens → Chromatic Aberration; set to affect only the frame edges (not uniformly — real lens aberration is strongest at the periphery); value = 0.5–1.0.
7. **Vignette**: Post Process Volume → Lens → Vignette Intensity = 0.4–0.6 for a subtle darkening of the frame corners.

### UE Systems / Blueprints / Settings
- **Light roles**: Key light (1 directional/spot — primary separation); Rim light (1 spot behind — silhouette punch); Accent under-light (1 small colored point — stylized fill)
- **Physics rope + spotlight**: Rope Component (Physics → Cable Component plugin); Spotlight attached to rope end; Take Recorder captures rope swing; parent Spotlight to rope end socket
- **Fan rotation animation**: Static Mesh fan; Sequencer rotation track looping; Spot Light positioned behind fan blades
- **Cine Camera DOF**: Current Aperture = 2.0; Focus Method = Manual; Manual Focus Distance set per shot; note: Focal Length affects field of view AND composition
- **Lens diffusion material**: Post Process Material in PPV Post Process Materials slot; Opacity = 0.75; stronger at edges
- **Chromatic Aberration**: Post Process Volume → Lens → Chromatic Aberration Intensity = 0.5–1.0; Chromatic Aberration Start Offset = center of frame (aberration only at edges)
- **Vignette**: Post Process Volume → Lens → Vignette Intensity = 0.4–0.6

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
lighting, cinematics, camera, post-process, compositing, beginner

---

## Related Entries
- [[the-fastest-way-to-learn-lighting-in-ue5]] — 4-factor lighting framework (direction, size, color, intensity)
- [[the-1-skill-you-need-for-lighting-in-ue5]] — light rig actor and upstage positioning
- [[improve-your-vfx-with-lens-flares-anamorphic-tutorial]] — lens flare and chromatic aberration in Nuke compositing
