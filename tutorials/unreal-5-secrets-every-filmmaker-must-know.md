---
title: Unreal 5 Secrets Every Filmmaker Must Know
source: YouTube
url: https://www.youtube.com/watch?v=0Yc6qJSWet4
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [filmmaking, lighting, cinematics, compositing, depth-of-field, photorealism, chromatic-aberration, lens-effects, rendering, technique]
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
**Transcript:** Now a lot of people have asked me how do I make my renders look cinematic?  And if I had to give the answer in one word, it would be lighting.  Now I've already made some in-depth lighting tutorials that you can check out, but I want  to share one of my favorite resources, Shot Deck.  Here you can find high resolution stills from your favorite movies and analyze why and  where they place the lights.  If you look at all of these different movies, you'll notice one thing in common.  All we have is a person standing in a room.  And yet some shots look boring and others look cinematic.  So what's the difference?  It's the lighting.  Simply the more dynamic the lighting looks, the simpler the lighting setup is.  In this case, it's literally just one key light that's lighting up this entire scene.  Or in shots like this, there's just one main light overhead lighting up his face and another  one coming from the side so that we get this rim light on the side of his forehead and  across the back of his shirt.  So cinematic lighting doesn't come from putting a ton of lights in your scene.  It's from putting one to three lights in the right places.  And oftentimes you just want to light one half of the face by making sure one side has  light and the other has shadow.  It's really important to create contrast between the brightest parts of your image and  the darkest parts.  And the bigger difference between these two, the more contrast you'll have.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_001.jpg

### Lighting Breakdown [2:08]
**Transcript:** So let's break down this lighting setup one light at a time.  The first light are these overhead lights, creating a lot of nice back light and also  fill light across the scene directly coming from these fluorescent lights in the background.  These are just images of fluorescent lights placed in the scene and plugging them into  the emissive channel and letting that do all of the hard work.  The next light is this overhead key light, which is really here to help separate Victor  from the background.  We want to avoid a completely monochromatic image, so getting it a little bit of a warmer  light in here helps separate him from the green background.  The third light is our rim light and this is just brought in to get a little more punch  in style and edge out of our character.  And again, you can see this really starts to light up the edge here and we want to brighten  up Victor's face so our attention goes directly to him.  And then as an accent, into incorporate the glowing eyes into the scene, I wanted to add  in this red under light, which helps tie everything together.  We get a little bit more color and it almost appears like the light is being cast from his  eyes onto the bridge of his eyebrows.  And with these four simple lights, we went from a fairly monochromatic simple scene into  something dynamic and full of contrast and color.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_002.jpg

### How to Animate Your Lights [3:25]
**Transcript:** But here's where a lot of people get it wrong.  Right now we're looking at still images or photographs, but if you want to make movies  and cinema, then you have to make your images move.  And we can do that by adding movement into our lights.  Let's jump into this scene with Mr. Freeze and check out how.  The first technique was taking this rope simulation and adding a light to it by creating  this simple physics interaction using a physics constraint and recording it using take recorder.  And by parenting a light to the simple interaction, we get this subtle but effective light animation  throughout our entire shot.  And you can see the shadows move across Victor's face.  The other technique is animating cast shadows.  As you can see, I didn't want to build a complicated environment, but I wanted the impression  of machinery and equipment moving in the background.  Instead of building complicated geometry, I just took this single spotlight and pointed  it at the background.  And then I found this fan in the Quixel library.  And by placing this directly in front of the light and adding a simple rotation animation  to the fan, the shadow implies a huge environment beyond what we can see in this one shot, but  the environment itself is almost non-existent.  So I hope that gives you a couple ideas to get started to add some quick animation to  your lights inside of sequencer.  The lighting is only one part of the puzzle when making a photo-real image.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_003.jpg

### The Secrets to Photorealism [4:45]
**Transcript:** So how do you make a photo-real render?  Well, let's break down the word photo-realism.  You need your renders to look like a photograph, meaning all the imperfections you get from shooting  through a camera lens.  Now, a shortcut to make your shots look more cinematic is to create shallow depth of  field with your lens.  This is how we get the large orbs and bokeh in the background of our images.  Now there's multiple ways to do this and I want to walk through both depending on your  shot.  Now, in sequencer, this is controlled within the camera.  I'll expand my Cine camera here and our two most important settings are going to appear  right at the top inside of sequencer.  And that's aperture and focal length.  Vocal length is the amount of zoom we have on our lens, which greatly affects the composition  of our frame and aperture controls the depth of field.  So the lower the number, the more out of focus, and the higher the number, the more focus  we'll have.  Now, if you're looking for a magic number, I usually start around two, but you can always  cheat this lower down to something like 1.4.  But be careful, as soon as you're getting into anything below one, we're creating a lens  that would never actually work in real life.  So we're stretching and breaking reality further than we really could.  So naturally, it'll look less photorealistic if we start breaking the rules.  Now, you should also know that the focal length will change the amount of depth of field  as well.  So that we zoom in here, you can see how shallow our depth of field is.  And just remember, a wider lens is going to have less depth of field and a zoomed in  lens is going to have shallower depth of field.  The more you zoom in, the more out of focus the background is going to be.  And to take this even further, the best practice is to add in extra dynamic particle effects  and decals into the background.  So we actually have more reason to see bokeh inside of our shot.  So by taking these Niagara particle effects and moving them further in the background  or closer to the camera, we can increase or reduce the amount of depth of field they contribute  and putting them really close to the lens can give you some really interesting results.  So try adding in snow, rain, blowing leaves, or any small particles close to camera and  try this out.  Now there's two types of lenses, spherical and anamorphic.  A spherical lens will have a circular bokeh and an anamorphic lens will have a stretched  oval bokeh.  A spherical is a bit more true to life or anamorphic is associated with a lot more imperfections  and a dirtier image.  This doesn't automatically make your shots look cinematic, but it can dirty up your image  in a way that most people don't associate with CG.  They associate it with Hollywood films.  So by mimicking these anamorphic qualities in your CG renders, you can get more photorealistic  results.  Now changing between spherical and anamorphic bokeh inside of Unreal is really simple.  Select your camera and then go down to the lens settings and this squeeze factor setting  and we can use this to squish down our bokeh shape.  So if we change this from one to two, this will make our bokeh a lot thinner, but it also  stretch our image by twice the width.  So all we have to do is go into our film back, go to your sensor width and then just divide  this by two and you can see we'll get the same exact resolution we had before, but now  we have nice anamorphic oval bokeh.  And here's a small tip.  Sometimes if you're going really shallow on your depth of field, you can start to break  some of your materials in the background.  But thankfully there's an easy fix.  One thing you might notice if you have a semi-transparent or translucent object in the background  is it might seem at first like they're incompatible with the depth of field system inside  of Unreal.  But fixing this is really easy.  Here we have our translucent fog material and a fipress on the brown box and type in  D-O-F for depth of field.  You want to make sure this translucency pass is set to before depth of field.  Now when I apply this and we see the changes in the scene, you'll see that it starts to  react naturally like you'd expect through a camera lens.  Now the last step to make a photo-real image is compositing.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_004.jpg

### Compositing for a Photoreal Image (The 3 Imperfections) [8:47]
**Transcript:** This is the last step of polish that we're putting on our finished renders to give them  even more imperfections and mimic all of the qualities of a camera lens.  And it's really important because if you skip a single step here, your shots won't look  photo-real.  Whether you use After Effects, Nuke or DaVinci Resolve, all these techniques apply.  So let's talk about the three imperfections that you want to add to every single render  to make something that looks CG and make it look photographic.  The first thing I always add in is lens diffusion.  This has the biggest impact and this one step can take images that look really CG and make  them look a lot more photographic.  So what's the biggest reason?  The biggest problem to overcome with CG is a lot of things can end up looking perfect  when they're created in a computer.  But by blurring our image, we can get a lot more imperfection and randomness that you'd  expect coming through a camera lens.  Oftentimes with CG, we'll get really crisp, dark blacks in our image.  But when you're using an anamorphic lens, oftentimes you'll get this really soft glow  coming from your light sources.  And as CG image, you might expect this silhouette to be perfectly black and have no orange  color contaminating some of these shadows.  But because they use these dirty, anamorphic lenses on the Batman, we get a lot of light  contamination coming from our sun source.  And all we have to do to recreate this is blur our image at different intensities,  some really small, and some with really big blur as like values of over 300, and then  just mixing the two together.  And now you can see we get some nice contamination into the shadows while still looking very  realistic.  And we get some additional colors into these dark areas where we had no information or  detail before.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_005.jpg

### Chromatic Abberation (The Right Way) [10:37]
**Transcript:** So on a shot like this, a little bit of diffusion can go a really long way in terms of contaminating  our blacks by adding haze onto our lens and into our environment.  The next step is adding in chromatic aberration.  A lot of times when shooting with cheaper or older lenses, you'll get some color separation  infringing around your brighter areas.  And this is known as chromatic aberration.  Essentially what happens is when light enters your camera lens, if that glass isn't perfectly  fine-tuned, by the time that light travels to hit the sensor of the camera where the images  captured are different wavelengths between the red, green, and blue can travel differently.  And oftentimes this is most notable around the corners of your lens.  Now this is definitely becoming more widely known in CG, but I think a lot of people are  implementing it in the wrong way.  With chromatic aberration, less is more, but it's really important to know how to apply  it correctly.  Let's take a look at this still from the assassination of Jesse James and see how this technique looks  when captured through a real camera.  When we go towards the edge of the frame, you can see that we get blue on one side and  red on the other.  But to really understand what's happening, we have to look at each channel, the red, green,  and blue channel.  If I compare the red channel with the blue channel, if you look at this lamp around the edges  of the frame, you can see that it almost looks like it's being scaled down slightly.  So we're not just offsetting our RG and B channels, we're scaling them to different sizes.  So in Nuke, my preferred technique is to use the God rays and then scale our image larger  or smaller.  This will give us more aberration and differences around the edge, and by using God rays instead  of scale, we'll get more smooth imperfections compared to the traditional chromatic aberration  from inside of Unreal.  Camera lenses will bounce around light and move things slightly differently, as opposed  to perfectly scaling the RG and B channels like you get inside of Unreal.  But it doesn't take long before you start breaking your image.  So again, less is more, and you just want to make sure that you're getting some new colors  introduced around the edges, enough to get some new colors, and some fringing, without drawing  attention to itself when you're looking at the whole image.  So make sure to scale your images, don't translate them to get this separation, because  very quickly this starts to look like an anaglyph 3D movie instead of a nice subtle effect  that will make your shots look more realistic.  And then the last thing I like to add are lens flares.  Whenever you can, it's always best to use real life footage captured through a camera lens,  and by mixing real life footage with our CG renders, it's a lot harder to tell where  one starts and the other stops.  And in my opinion, adding in lens flares are the easiest way to add that last step of  color, polish, and randomness into your scene, while still grounding your shots in real life.  And if you add these three things to any shot, you'll remove that CG curse, some of that  digital perfection that you get from making a virtual scene.  This is the exact method I use when creating the samurai sword fight for War of Being.  By creating simple render templates, I could apply the same lens effects to my entire  film giving each shot a more realistic feel.  And by templating this process and making it extremely quick with just a few sliders,  you can then all your time creating inside of Unreal instead of waiting around for renders.  So if you want to improve your renders inside of Unreal, or even just use the same exact

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_006.jpg

### Level-Up as an Unreal Filmmaker [14:11]
**Transcript:** composing template that I used here, you might want to check out Unreal Fundamentals.  If you're new or struggling to learn Unreal and you want to take your work to the next level,  then you should check out our 21-Day Unreal Filmmaking Bootcamp to go from a complete  beginner to an Unreal filmmaker making your own animations and pre-vis inside of Unreal.  I've taken everything I've learned, every cheat sheet, every template, and every resource  and combine them all together in one place.  So take your future in visual effects and filmmaking into your own hands and get started  today.  And make sure to share what you create by the end of the course.  Subscribe below if you want to see more.  Otherwise, check out our behind the scenes of Tesseract's music video for War of Being.  We'll show you exactly how we made the Samurai Swordfight using motion capture and Unreal  Engine step by step.  Thanks for watching and I'll see you next time.  Peace.

**Frame:** tutorials\frames\unreal-5-secrets-every-filmmaker-must-know\frame_007.jpg


---

## Structured Notes

### Core Technique
Three secrets for cinematic, photorealistic UE5 renders: (1) **Lighting** — 1-3 lights max; key + rim + accent; animate lights for realism; shadow-only spotlight + prop for implied environment; (2) **Photorealism** — shallow DOF (Aperture ~1.4–2.0); anamorphic bokeh via squeeze factor + sensor width ÷ 2; translucent material Translucency Pass: Before DOF; Niagara particles in fore/background for bokeh; (3) **Compositing** — three lens imperfections: lens diffusion (multi-scale blur), chromatic aberration (scale RGB channels, not translate; subtle around edges), real-world lens flares.

### Summary
15m3s Josh Toonen tutorial sharing three "secrets" from a Mr. Freeze short film (War of Being). No code/blueprints — pure visual/workflow techniques. Secret 1 (Lighting): reference ShotDeck.com for film lighting stills; 1–3 lights create more contrast/drama than many lights; demonstrated 4-light setup (overhead fill + key + rim + red under-light); animate lights for realism: physics constraint on hanging rope with parented light (creates moving shadows); shadow-animation via fan prop + spotlight (implies complex off-screen machinery). Secret 2 (DOF + lens): Cine Camera → Aperture (~2 default, 1.4 for more blur); focal length controls zoom + DOF depth; Niagara particles in background = more bokeh to show; squeeze factor for anamorphic bokeh; sensor width ÷ 2 to correct scale; translucent fog fix (Translucency Pass: Before DOF). Secret 3 (compositing): three imperfections applied in post (AE/Nuke/DaVinci): lens diffusion (blur image at multiple radii, mix; contaminates shadow blacks with glow), chromatic aberration (scale — not translate — R/G/B at different sizes; God Rays in Nuke for smooth radial separation; keep subtle — check edge of frame only), real-world lens flares footage (composited on top for maximum realism).

### Key Steps
**Secret 1: Lighting**
1. Reference **ShotDeck.com** → search any movie → analyze where lights are placed in each shot
2. Keep 1–3 lights; create contrast (bright key on one side; shadow on other; rim to separate from background)
3. **Emissive channel trick** — place photo of fluorescent lights on mesh → plug into emissive → instant area fill without light actor (photorealistic + no shadow artifact)
4. **Animated light from physics** — add physics constraint to hanging rope prop → parent Point Light to rope → record with Take Recorder; moving shadows across character face
5. **Shadow-animation trick** — place Spotlight pointing at background → put prop (e.g., fan from Quixel) in front of light → add rotation animation to fan → rotating shadows imply a huge off-screen environment

**Secret 2: Photorealism via lens settings**
6. Cine Camera → Sequencer → find **Aperture** and **Focal Length** at top:
   - Aperture: start at 2.0; go to 1.4 for more blur; below 1.0 breaks realism
   - Focal Length: zoom in = shallower DOF + more bokeh in background
7. Place **Niagara particle effects** (snow, rain, leaves) in background → appears as bokeh; move close to lens for artistic foreground blur
8. **Anamorphic bokeh** — select Cine Camera → Lens Settings → **Squeeze Factor** = 2 → bokeh stretches into ovals (but image also stretches 2×); go to **Film Back → Sensor Width** → divide original value by 2 → restores correct image dimensions with oval bokeh
9. **Translucent material DOF fix** — select translucent/fog material → Material Details → search "DOF" → **Translucency Pass: Before DOF** → material now blurs naturally with depth of field

**Secret 3: Compositing (in AE/Nuke/DaVinci)**
10. **Lens diffusion** — most impactful step:
    - Take render → apply Gaussian blur at very small radius (e.g., 2–5) → mix 10–20% with original
    - Apply same blur at very large radius (e.g., 200–300+) → mix 5–10% with original
    - Combining both creates soft glow and shadow contamination (colored light bleeds into black areas)
    - Mimics dirty anamorphic lens glow from real-world films (e.g., Batman, Jesse James)
11. **Chromatic aberration** (correct method):
    - Separate R, G, B channels
    - **Scale** (not translate) each channel by slightly different amounts (e.g., Red: 101%, Green: 100%, Blue: 99%)
    - Gives more aberration at frame edges, less in center — matches real lens behavior
    - In Nuke: use **God Rays** node scaled at different amounts per channel for smooth radial separation
    - Keep very subtle: visible at frame edge, invisible at center — never draw attention to itself
    - Wrong method: translating (offsetting) channels = anaglyph 3D look, not chromatic aberration
12. **Lens flares** — use real-world lens flare footage (filmed through a camera) → composite on top of CG render → photochemical quality impossible to replicate in CG

### UE Systems / Blueprints / Settings
- **ShotDeck.com** — film reference image database; search by movie/mood; analyze key/fill/rim placement in professional shots
- **Emissive channel as fill** — place image of light fixture (fluorescent, neon) → Material Emissive slot → no light actor needed; scales to any shape naturally
- **Take Recorder** — records live physics/animation in UE5; use for rope swing simulation → captured as animation asset
- **Physics Constraint** — locks object; combined with active physics simulation creates natural swinging; parent light to swinging prop
- **Cine Camera Aperture** — f/2.0 typical start; lower = more blur; below f/1.0 = physically unrealistic
- **Cine Camera Focal Length** — wider (e.g., 24mm) = less DOF; telephoto (e.g., 85mm+) = more DOF separation; affects composition and background isolation
- **Squeeze Factor** (Lens Settings) — stretches/squishes bokeh shape; 1 = spherical; 2 = 2:1 anamorphic oval; must compensate with Sensor Width ÷ 2 to maintain correct render dimensions
- **Translucency Pass** (Material setting) — search "DOF" in material details; change from "After DOF" to **"Before DOF"**; allows translucent/volumetric elements to interact correctly with depth of field
- **Lens diffusion** — multi-scale Gaussian blur composite; not a single blur but a mix of very small (subtle contamination) + very large (glow/bleed) passes
- **Chromatic aberration (correct)** — scale channels at different amounts; use God Rays (Nuke) for smooth radial; NOT translate/offset which looks like anaglyph
- **Real-world lens flares** — film glass flares in front of light source; composite as screen/add blend on top of CG render

### Difficulty
Beginner-Intermediate. Lighting and lens settings are straightforward. Compositing techniques require familiarity with compositing software.

### UE Version
UE5

### Tags
filmmaking, lighting, cinematics, compositing, depth-of-field, photorealism, chromatic-aberration, lens-effects, rendering, technique

---

## Related Entries
- `unreal-5-hotkeys-every-filmmaker-must-use.md` — companion Josh Toonen tutorial; Sequencer workflow + camera controls
- `the-1-skill-you-need-for-lighting-in-ue5.md` — Josh Toonen character lighting deep dive; 180-degree eye line rule
- `the-fastest-way-to-learn-lighting-in-ue5.md` — Josh Toonen exterior lighting study framework; 4-element approach
- `the-2025-guide-to-rendering-in-unreal-engine-5.md` — MRQ render settings (EXR, tone curve, sampling)
- `the-2026-unreal-engine-to-davinci-resolve-guide---aces-srgb.md` — DaVinci post-production pipeline for UE5 renders; ACES transform + color grading
