---
title: Lighting Interiors in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=0GYyHDuaPcg
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5.3"
tags: [lighting, interior, lumen, path-tracing, hardware-ray-tracing, rect-light, indirect-lighting, diffuse-color-boost, volumetric-fog, cinematics]
extraction_status: complete
frames_dir: tutorials/frames/lighting-interiors-in-unreal-engine-5/
frame_count: 8
---

# Lighting Interiors in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=0GYyHDuaPcg)
**Author:** William Faucher
**Duration:** 17m20s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In today's video we'll be taking a look at interior lighting, combining the uses of  Lumen, hardware ray tracing and path tracing. I'm going to show you how you can think of  lighting in a way that will help you pick and choose the mood you're going for. By simply  lighting a couple of different lighting scenarios, it will really help you break down how to  light any given interior. Now, full disclosure, the video is sponsored by Nvidia Studio and Scan  Computers. Everything from the modeling, layout, lighting, rendering, and editing of this video  had been done with the ASUS ZenBook Pro 16 OLED laptop. I don't get to keep the laptop, it's  being sent back and only being used for reviewing purposes. Just before we jump into today's  tutorial, I'm going to take a brief moment to talk about the hardware we're using today.  The ASUS ZenBook Pro 16 OLED laptop runs on a beefy RTX 4070 that allows you to fully utilize  hardware ray tracing and path tracing and tensor AA cores, which is going to help massively when  you're rendering your shots. It's got the CUDA cores you need, which are needed if you plan on  3D scanning things with an app like Reality Capture. And since the 40 series GPU, you can benefit  from DLSS3, which I've talked about in an earlier video right here. It's got 32GB of RAM, a core i9  processor, which handles unreal shader compilation like an absolute champ. The display on this laptop is  absolutely top notch, 120Hz with 100% DCI-P3 and 100% SRGB color coverage, and its OLED meaning  your blacks could be nice and inky. Some notable quality of life features include this nifty  hinged keyboard, which not only feels a lot more natural than I'm typing, but also seem to help  with the cooling. And the trackpad has haptic feedback, which was a nice surprise.  Nvidia Studio is for creator when Nvidia GeForce is for gamers, right down to the drivers.  Even unlike personal desktop workfaces, I'm always using studio drivers just because I find  them a lot more reliable than the game drivers for creative work specifically. If a laptop or  desktop is Nvidia Studio validated, it means that spec and design meet the need of a creator.  You can get Nvidia Studio laptop at scan computers, you can check out the link down below.  I thought it would be fun to make a tutorial using a laptop for a change, because a lot of people  assume that the work I do in Unreal can only be done on a crazy expensive workstation desktop,  and that's just not the case. So let's get started with what you came here for,

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_000.jpg

### Project Settings in Unreal Engine 5 [2:11]
**Transcript:** lighting interiors in Unreal Engine 5. Okay, so since we're getting started,  I just want to make sure that you all have the same project settings that I'm using.  I am currently using Unreal Engine 5.3, so by going to Settings up here, we're going to go to  Project Settings. We're going to scroll down to the Rendering tab down here, and you're going to  want to make sure to support hardware ray tracing and turn it on and pass tracing and turn it on  here as well. I'm using Virtual Set-O-Maps and make sure that you hardware ray tracing when available  is turned on. And it should go without saying, but if you want this to work, you need a GPU that  is capable of ray tracing. The GPU in this laptop is an RTX 4070, so you're not going to have any  issues with it. And one last thing, in a search panel up top, we're going to search for DirectX,  and I believe you need to have DirectX 12 enabled. At least, that's what I'm using, and it works like a charm.

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_001.jpg

### Reference and Lighting [3:03]
**Transcript:** So here we have a scene that I made it Unreal that is loosely inspired by a scene in Game of Thrones,  and before we get started with the lighting, let's look at the reference and try to break down  where the light is coming from. Notice how there is no artificial lighting. The only thing we're seeing  is light pouring in through that doorway at the top of the stairs. That is the only light source,  and the camera is exposing for the interior, making the exterior completely overexposed, and blown out.  And that is what we're going to try to mimic here. Now this laptop handles this scene like an  absolute champ. I'm blazing past 60 FPS without any issues, and if you want to follow along with  this environment in this tutorial and reverse engineer, how to scene with lit, you can download  this project for free here on Gumroad. Link down below. Just to be clear though, it's not going to  look exactly the same because I'm using a lot of mega-scan textures and models in this level,  and I'm not legally allowed to redistribute those assets, but you will have something to work with,  and the lighting will look the same. So what we're going to do now is we're going to completely kill  all of our lighting, and we have to create a daylight system using the environment light mixer,  as always. So by going to the window tab up here, we're going to go to the environment light mixer,  create skylight, atmospheric light, sky atmosphere, and height fog, and next we're going to create a  post-brosit volume, and drag it into our scene here, and make sure we set it to unbound. Make  sure to select right here. You'll see this is really important for pretty much everything moving  forward in this video. So you'll see obviously this is very underwhelming. When it comes to interior  lighting, indirect lighting is everything, and that's the main takeaway here. The easiest way is to  increase the brightness of your skylight, because this is our main source of light. Notice in our  reference, we don't have any sunlight coming in there. The sun is probably pointing in a totally  different direction. We only want skylight coming in. So we can select our skylight, and we can  increase intensity scale to something ridiculous, like 20 or 100. 1000. You'll see we're starting to  get a little bit more lighting coming into our scene, but you'll see, you know, it's not really  great. It's very splotchy, and I think that's really just because it's a limitation of  lumen right now with the skylight. It just doesn't have enough sample to work with. And so,  when that doesn't work, what's next? We can increase the exposure of the scene. So we're going to go  to the post-process volume, and we're going to search for EXP, and I got to check these three boxes  here and uncheck Apply Physical Camera Exposure, and we can adjust the exposure this way.  Now again, this brightens everything up, but it's still pretty splotchy. Not really what we're  going for. It's not really what we want. And we get this really not so great looking blue fog,  and that's because we want to make sure to be select our exponential high fog, and turn on volumetric  fog. You'll see why this is important later. Now, in order to give your skylight a bit of a boost,  you can also increase the brightness of your directional light to something like, I don't know,  like 800 or something, and that will also help inject a lot more light, because as you increase  your directional light, it increases the brightness of your sky as well. So it kind of goes both ways.  Honestly, I think about in here, it's probably a bit too strong. I would rather play around with  the exposure later. So now we are getting a bit of a better result over here, but still, this is  not what we're going for. And the reason why, because the indirect lighting quality of lumen is  great, volumetric does not have enough samples to really get a high quality render from such a tiny  light source coming in through that window. So we need to fake it, and in order to fake it,  we're going to go ahead and create a rect light over here, and drag that over here,  and loosely shape it to the, well, shape and size of our doorway here. So by increasing these  or its width, and the source height, like that, loosely matching the size of it, the skylight does  inject a little bit of indirect lighting, but it's just not enough. You're not getting enough  consecutive bounces here. So we need to inject some direct lighting with the help of direct light  here to really get some better results. Okay. So with our rect light, we're also going to increase  the attenuation radius, and maybe set the value to something like 800. And now, notice how we are  getting a much more interesting look, all because we've introduced a bit of direct lighting,  it's okay to fake things. Now, I'm going to create, I can change the color a little bit, make a  little bit cooler, and there you have it. We're already having a much bluer look to our scene.  And already we are about 60% of the way there. But you'll notice that these areas here are still  very black, not very good looking. What more can we do? We don't want to increase the exposure,  we want to increase the indirect lighting values. Sometimes, looming can be a little bit tricky,

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_002.jpg

### Pathtracing and Ground Truth [7:43]
**Transcript:** so this is why I like using the path tracers sometimes in order to help me figure out, hey,  am I actually doing things right here? So by going to the lit tab here, we're going to go turn on  path tracing, and what the path tracer is going to do is it's going to give you a more ground  screws physically accurate lighting result based on your current lighting settings. This is what  your scene should look like if everything is set up correctly. There should be no tremendous  difference between the two. They should both be pretty similar. And if they're not, then there's  other issue we need to fix. So you'll see we're missing out on a ton of indirect lighting over here.  If you'll notice it's not perfectly black, it's not there, not black at all there. So we need to go  fix that somehow, right? We need to try and rectify this issue. And how do we inject a little bit more  indirect lighting into our scene? We don't want to go ahead and increase the exposure again.  That will work, but it also brightens up everything else. And we don't want that. All we want is to  lift up those shadows a little bit more. So we're going to go ahead and click on our rectlight here.  And we're going to scroll down to indirect lighting intensity. So I'm going to bump it up to  something like five to exaggerate it a little bit. And you'll see, hey, we're starting to get a lot  more indirect lighting into our scene. It's already looking a whole lot better. Now keep in mind,  this is not a physically accurate setting. Your changes here will not be mirrored in the path tracer  because what's happening here is a surface is reflecting five times more light than it is  receiving, which is physically impossible. So use this was caution, use it only more of a subtle  art direction kind of feature. Okay. Now another issue that I'm noticing is our shadows here are very

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_003.jpg

### Soft Shadows, Hardware Raytracing vs Virtual Shadow Maps [9:21]
**Transcript:** harsh. Right. Again, if I turn on the path tracer, you'll notice that shadows are very, very  soft here, right? It look really, really good. And I don't, I'm not seeing that we're getting  these really hard shadows here. There's something feels off. And the reason for that is because of  virtual shadow maps when it comes to very, very soft shadows, you're just kind of hitting that  limitation there. So in order to fix that, we're going to select our rectlight again. And we're  going to search for ray trace. And we want to make sure we cast ray shadows on and pay attention  to the sheer difference here. No, especially notice on the wall here, this before and this after,  before and after. The shadows are so much softer. So we're getting much, much better  softer shadows here now. When you need to really, really soft shadows, there is no way around using  hardware ray tracing. And that is where RTX GPUs come in really, really handy. Another reason it  incredibly important to add direct lighting, even your ishersine is mostly indirectly lit,  is because of specular highlights. Now pay attention right here on the pillar on the left hand  slide here. I wanted to give it like a, you know, running water kind of look like it would very damp.  If I hide my rectlight right now, and I only rely on the indirect lighting from Lumen,  and I'm going to go ahead and increase the exposure here just for clarity sake. Notice how it  doesn't look wet. And the reason for that, at least it's my understanding, Lumen's indirect lighting  is not going to contribute to specular highlights, at least not very much. You can clearly tell right  here that there is just no real specular highlights. We completely lost that wetness that it had,  right? And so that is why it's really important to inject that direct lighting to make that surface

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_004.jpg

### Bonus Tip 1 [11:12]
**Transcript:** look wet. Now bonus tips number one, if ever you notice this kind of like light bleeding in your  interiors, this is actually something that's pretty common. You'll notice like along the edges,  you just got this weird light that seems to be, the skylight that's coming through the walls,  you need to go ahead and add some light blockers to the exterior of your level. And what I mean by  this is these large white cubes, right? It's literally just a big white cube that I place underneath my  level to make sure that light is being blocked correctly. Because as we saw earlier, the skylight has  some very low resolution sampling, which makes it very splotchy. And sometimes, at least my understanding  is that you just need more geometry to block that light coming in. So again, if I were to just  lower this cube right here, notice how we're getting a whole bunch of light that's bleeding into  our scene here? Just lifting this big cube up here. Whoa, that light gone. That is how you can fix  light that's leaking into the corners of your wall. It's very frustrating, but fortunately,  with light blockers, it's a very easy fix. Now, let's say you wanted to have some light shaft or  some god rays coming through the window, you can absolutely do that too. So what we need to do is  grab our directional light here and rotate it so that the sun shines through the doorway.  And we can angle it the way that we want to, something like that. And you'll see it injects  quite a bit of indirect lighting into our level as well. And we got these light shaft here,  thanks to the volumetric fog that we turned on in our exponential height fog earlier. See,  if I turn off volumetric fog here, it's going to be a totally different look. And we don't get those  light shafts coming through. If I want to make that light shaft even stronger, we can simply just  increase the volumetric scattering intensity even higher. So I haven't already set it to 10 here.  By default, there'll be one. You might not even see it, but if we increase the late 50,  100, you'll see it's a very, very strong god ray shining in our scene now. And already we're getting  quite a bit of indirect lighting bouncing up and lighting the rest of our scene. This doesn't match  the reference we were going for, but I still just wanted to show you that it is something you can do.  But for now, I'm just going to go back bring it back up here because that's not the look I wanted.  Every single light hand had its own volumetric scattering intensity. You'll see in my rectalight,  I already had it cranked up to six. If you want more fog like that coming in, which we do have in  our reference here, that is how you can control that. Bonus tip number two, there's one more

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_005.jpg

### Bonus Tip 2 [13:42]
**Transcript:** trick we have up our sleeve in order to inject a little bit more indirect lighting into our scene.  Again, this brake physicality, but the really cool tip know about. In our post process volume,  we're going to search for a lumen. And here we've got a neat little tip called diffuse color boost.  I already said it to two, but if I said to one, you'll see our shadows are very dark, right? It's  very pitch black. We could always just increase the indirect lighting of our rectalight, but by  increasing the color boost here, it's going to increase the boost of not our light, but of the  albedo values of our materials. So if I said to two, you'll see we've already  injected quite a bit more indirect lighting into our level here. Again, purely in our direction  thing, there's no right or wrong way to do it. It's just important to know which tools are available  to you. So I hope that helps. So now that I've covered this scene here, how do you light an

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_006.jpg

### Lighting Interiors without natural light [14:40]
**Transcript:** interior that doesn't have any natural light? And that my friend is artificial lighting. So we're  going to hide this here. I have to turn this on here. You'll see here we've got a completely  differently lit scene. I'm not going to go ahead and show you how to place each individual light,  but really it's about breaking down what our lighting is. This is a really quick reference I found  from some old museum somewhere and to notice how there is no natural light here, it's all artificial.  You as a lighting artist need to break down and ask yourself, where is my lighting coming from?  If I turn on my light in my bedroom at night, the light source is your light bulb or your lamp or  whatever. And that's how we need to break it down here. So I went ahead and added some light  fixtures here. We need a physical prop that is there to suggest that hey, there's lighting here.  This is actually what is contributing to the illumination of the scene. Because if I were to  hide these light fixtures here and you just place light, something would feel a little bit odd.  I mean, it feels like something is missing, right? So that's why we need not only add some practical  light props, but really think about where the lights are coming from. And then I just add  as some point lights here and adjusted them to the rough shape of my light source by increasing the  source lights here. You can kind of increase the source lights of any point light.  And I'm just going ahead and place them there. And again, using the exact same trick that we learned  earlier, either the exposure of your post process volume, the global exposure of your scene,  or the indirect lighting intensity of your light, or the diffuse color boost of your post process  volume, right? If I wanted to the two or five, you'll see we made this scene much, much brighter.  Not really the look and going for, but you get the idea. The actual lighting part here is  not very complicated. Again, just to give you one more example, I've used the torch prof that are  on the wall to suggest torch light. And also each point light that I placed, again, it's really just  a simple point might right here that I placed over the torch, each light that I placed also has  a volumetric scattering intensity that I cranked way up to suggest that it maybe took a little bit  moisture in the scene or a little bit of haze or smoke or whatever. That's really it. The key  to interior lighting is just to break down where my lighting is coming from, an understanding,  exposure, indirect lighting, and direct lighting. All right, thanks so much to Nvidia Studio and  Scan Computers for sponsoring this video. Scan Computers are one of the leading resellers on  Nvidia Studio laptop and desktop in Europe. If you're looking for an Nvidia Studio laptop,  then check out their range at the link down below. So thanks so much for watching everyone.  I hope you found this video helpful and as always folks, happy rendering.

**Frame:** tutorials\frames\lighting-interiors-in-unreal-engine-5\frame_007.jpg


---

## Structured Notes

### Core Technique
Interior lighting in UE5 using Lumen + hardware ray tracing. Core approach: (1) Environment Light Mixer for base sky system, (2) PPV for manual exposure, (3) Rect Light shaped to window/doorway opening for direct light injection (Lumen skylight alone too splotchy for tight interiors), (4) Indirect Lighting Intensity boost per light, (5) Diffuse Color Boost in PPV Lumen settings. Use Path Tracer as ground-truth reference to verify Lumen is set up correctly. Physical practical props required to justify artificial light placement.

### Summary
17-minute William Faucher interior lighting tutorial (UE5.3, RTX 4070). Two scenarios: (1) natural light interior (Game of Thrones-inspired — single doorway opening as only light source, camera exposing for interior = blown-out exterior); (2) artificial light interior (museum/torch dungeon). Key challenge: Lumen skylight at high intensity = splotchy indirect; must inject direct light via Rect Light at opening. Three advanced tips: path tracer as ground truth (Lit → Path Tracing to see what scene should look like), Indirect Lighting Intensity on individual lights (non-physical boost, not mirrored in path tracer), Diffuse Color Boost in PPV Lumen settings (boosts all albedo values for more bounce — non-physical). Light bleed fix: large geometry Light Blockers around exterior plugs Lumen skylight leakage. Artificial lighting: place physical fixture prop → place Point Light inside it → Volumetric Scattering Intensity per light for haze/smoke feel.

### Key Steps
1. **Project Settings** (UE5.3):
   - Settings → Project Settings → scroll to Rendering → Support Hardware Ray Tracing: ON; Path Tracing: ON; Virtual Shadow Maps: ON; Hardware Ray Tracing When Available: ON
   - DirectX 12 default RHI
2. **Analyze reference first** — break down: where is light coming from? Single doorway? Practical fixtures? Sun angle? Then replicate
3. **Clear all lights** → delete or start fresh
4. **Base daylight system** (Window → ENV Light Mixer):
   - Create Skylight + Atmospheric Light + Sky Atmosphere + Height Fog
   - Drag PPV into scene → Details → Infinite Extent (Unbound): ON
   - PPV → search "exp" → Metering Mode: Manual; Apply Physical Camera Exposure: OFF; adjust Exposure Compensation
   - Exponential Height Fog → Volumetric Fog: ON (required for god ray shafts later)
5. **Why skylight alone fails for tight interiors**:
   - Skylight intensity cranked high = splotchy indirect (insufficient samples for small aperture)
   - Solution: inject direct lighting with Rect Light shaped to opening
6. **Rect Light at window/door** (main light injection):
   - Add Rect Light → position at exterior of doorway/window facing inward
   - Match Source Width and Source Height to aperture shape
   - Attenuation Radius: ~800 (large enough to fill interior)
   - Color: slightly cool blue (exterior sky)
   - Cast Ray Traced Shadows: ON (much softer shadows; critical for quality)
7. **Path Tracer as ground truth**:
   - Lit dropdown → Path Tracing
   - Compare Lumen vs Path Tracer result; should be similar; large differences = lighting setup issue
   - Use to identify missing indirect in shadowed areas
8. **Indirect Lighting Intensity** (boost GI per light):
   - Select Rect Light → scroll to Indirect Lighting Intensity → set to 5
   - Boosts bounce light from this light source; non-physical; NOT reflected in path tracer
   - Use cautiously as art direction tool only
9. **Specular highlights note**: Lumen indirect barely contributes to specular; always need direct light for wet/shiny/metallic surfaces to appear correctly
10. **Light Bleed Fix** (Bonus Tip 1):
    - Symptom: light bleeding through walls/edges from skylight
    - Fix: place large white Static Mesh boxes (Light Blockers) around exterior of level under/around structure
    - Blocks low-res Lumen skylight sampling from penetrating geometry
11. **Volumetric god rays** (optional):
    - Directional Light → rotate so sun shines through doorway
    - Directional Light → Volumetric Scattering Intensity: 50–100 for visible shaft
    - Each light has individual Volumetric Scattering Intensity → use on specific lights for localized haze
12. **Diffuse Color Boost** (Bonus Tip 2):
    - PPV → search "Lumen" → Diffuse Color Boost (default 1)
    - Set to 2–5 → boosts all material albedo values → more indirect light bounced
    - Non-physical; purely art direction; combines with Indirect Lighting Intensity for shadowed areas
13. **Artificial lighting (no natural light)**:
    - Place physical light fixture props (lamps, torches, candles) to justify light placement
    - Add Point Light inside/above each fixture
    - Increase Source Radius to match fixture size
    - Each light: Volumetric Scattering Intensity cranked up for localized haze/smoke atmosphere
    - Global: adjust Exposure Compensation or Diffuse Color Boost to control overall brightness

### UE Systems / Blueprints / Settings
- **Lumen** — dynamic GI; splotchy in tight interiors with tiny light apertures; fix with direct light injection
- **Environment Light Mixer** — Window → ENV Light Mixer; one-click base sky system (Skylight + Atmospheric Light + Sky Atmosphere + Height Fog)
- **Post Process Volume (PPV)** — Infinite Extent (Unbound) ON; Metering Mode: Manual; Apply Physical Camera Exposure: OFF; Exposure Compensation; Lumen → Diffuse Color Boost
- **Rect Light** — shaped to window/door opening; Source Width/Height match aperture; Attenuation Radius 800+; Cast Ray Traced Shadows ON for interiors; individual Volumetric Scattering Intensity
- **Path Tracing** — Lit dropdown → Path Tracing; physically accurate ground truth; compare to Lumen to verify setup; note: Indirect Lighting Intensity boost NOT reflected in path tracer
- **Indirect Lighting Intensity** — per-light Detail panel setting; multiplies GI contribution from this light; 5 = 5× bounce; non-physical; not mirrored in path tracer; use with caution
- **Cast Ray Traced Shadows** — per-light; requires RTX GPU; essential for quality soft shadows in interiors (VSM limited with large soft penumbra)
- **Diffuse Color Boost** — PPV → Lumen section; boosts albedo of all materials → more indirect light; default 1; non-physical; art direction tool
- **Volumetric Scattering Intensity** — per-light; controls how much this light contributes to volumetric fog shafts; individual per-light control; good for torch haze, shaft through door
- **Light Blockers** — large Static Mesh cubes placed around exterior of level; block Lumen skylight from bleeding through walls; necessary for tight interior scenes
- **Specular and Lumen** — Lumen indirect lighting contributes minimally to specular highlights; always need at least one direct light for wet/metallic/shiny surfaces to render correctly
- **Practical lights** — physical prop fixtures (lamps, torches) must be present to justify and "sell" artificial light placement; light without a practical source feels wrong

### Difficulty
Intermediate. Assumes knowledge of basic UE5 lighting setup. Key advanced concepts: using path tracer as diagnostic, Diffuse Color Boost, Indirect Lighting Intensity, light bleed fix with blockers, per-light volumetric scattering intensity. RTX GPU required for hardware ray tracing features.

### UE Version
UE5.3 (explicitly stated; hardware ray tracing + path tracing; Virtual Shadow Maps; Lumen)

### Tags
lighting, interior, lumen, path-tracing, hardware-ray-tracing, rect-light, indirect-lighting, diffuse-color-boost, volumetric-fog, cinematics

---

## Related Entries
- `lighting-in-unreal-engine-5-for-beginners.md` — beginner companion by same author; light types, shadow softness fundamentals
- `lighting-a-night-time-exterior-in-unreal.md` — nighttime exterior counterpart; lighting channels, practical lights
- `lumen-explained---important-tips-for-ue5.md` — deeper Lumen-specific settings
