---
title: Lighting in Unreal Engine 5 for Beginners
source: YouTube
url: https://www.youtube.com/watch?v=fSbBsXbjxPo
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.x (UE5)"
tags: [lighting, lumen, beginners, directional-light, point-light, spot-light, rect-light, virtual-shadow-maps, ray-tracing, emissive, volumetric-fog, hdri, skylight, exposure, soft-shadows, indirect-lighting, william-faucher, beginner, ue5]
extraction_status: complete
frames_dir: tutorials/frames/lighting-in-unreal-engine-5-for-beginners/
frame_count: 0
---

# Lighting in Unreal Engine 5 for Beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=fSbBsXbjxPo)
**Author:** William Faucher
**Duration:** 44m43s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Today we're talking about one of the most underrated aspects of 3D, and that is lighting.  Those of you familiar with my channel know that most of my Unreal Engine videos target  the more advanced users, so I figured I would change it up a bit and talk about lighting  for the absolute beginner.  If you don't know anything about lighting or how it works, let alone how to get things  looking good in Unreal Engine.  This is the video for you.  And just to be clear, in this tutorial we'll be using Lumen and UE5 with a fully dynamic  lighting approach, we will not be learning about baked lighting.  So I'm not going to waste any more time with the intro.  Let's jump straight into lighting right after I tell you about my sponsor.


### CGSpectrum [0:41]
**Transcript:** So a big thank you to CG Spectrum for sponsoring this video.  CG Spectrum is a global top-ranked training provider offering specialized online courses  in real-time 3D, game development, animation, VFX, and digital painting.  They're an Unreal authorized training center and Unreal academic partner, and their courses  include personalized mentorship from industry professionals.  I help develop their real-time 3D technical and virtual production course, I mentor their  part-time myself, and here are a few examples from some of my own students.  So if learning Unreal Engine with the help of an industry mentor is something you're interested  in, do check out the link down below or visit CG Spectrum.com for more info.  You'll get the most practical and up-to-date knowledge, connections, skills, and industry  awareness that studios in both the games and film industry are hiring for.  So thanks again to CG Spectrum for sponsoring this video, and now let's jump straight into  lighting.


### Project Settings [1:35]
**Transcript:** Alright, so now that we're in Unreal, we need to make sure that our project settings  are set up correctly, to make sure that everything behaves as expected, to get the best possible  results, and make the most of what Lumen has to offer.  So we're going to go to the Settings tab up top here, click on Project Settings, and  in the Search Detailed panel, we're going to search for DirectX.  And we need to make sure that our default RHI is at the DirectX 12, and DirectX 11 and  12 SM5 is turned on.  Next we're going to scroll down to the Rendering tab right here, and by scrolling down to the  Lumen section right here, we need to make sure that we have the following Project Settings  set up correctly.  Dynamic Global Elimination set to Lumen.  Array lighting mode set to Surface Cache, Software ray tracing mode set to Detailed Tracing,  Shadowmap Method set to Virtual Shadow Maps Beta, and one more thing that I like to have  turned on is Support Hardware Ray Tracing turned this on, and you'd Hardware Ray Tracing  when available.  Now keep in mind the Hardware Ray Tracing settings are only going to work if you have a GPU  that is capable of hardware ray tracing.  So any of the Nvidia RTX...


### Lighting Basics & Light Types [3:18]
**Transcript:** you everything you need to know about every light that is available in Unreal Engine 5.  And in order to create our first light, we need to go to the Place Actors tab, and in  the little light icon here, you'll have a list of all the available lights.  If you're UI looks a little bit different than mine, don't worry.  You can go to the Window tab, Load Layout, and I'm using the UE4 Classic Layout, just because  I like the way that it is set up.  To me, it works a little bit better, so if you want to follow along, this is the layout  that I am using.  So let's start off with the first light here, and that is the Directional Light.  I'm going to drag and drop this into my scene here, and as you can see, as I rotate around  here, the Directional Light does what the name implies, it behaves a lot like a sun, or  moonlight, or any kind of light that is very directional in nature.  So Directional lights are usually used for exterior environments, or when you want to have sunlight  shining through a window for interior environments.  Now what's really cool about Lumen is that it just works out of the box, and as you can  see here, we've got some nice indirect lighting, lighting up our cha...


### Lighting Basics & The Magic Sauce [10:09]
**Transcript:** If you remember just earlier, when I showed you the rect light, we had really soft shadows.  That's because the light source was bigger.  But what if I told you that we can get soft shadows with any of the other light actors  that I just showed you?  So right here, I've got my point light selected and I'm going to zoom in here and you'll  see in a detailed panel here, we have source radius.  If I start increasing this like that, you'll notice a bit of a yellow gizmo show up around  it.  That is actually the size of our light.  So we can actually give it a shape and a size.  And as a result, notice what happened to the shadows.  The shadows got soft.  If I make it smaller, back to zero, and make it larger, notice my shadows are getting  softer.  This is what we call the shadow penumbra.  And basically, it really boils down to the larger your light sources relative to your  subject, the softer your shadowed will be.  This is the most important part of lighting.  Understanding how to get soft shadows, understanding when shadows should be soft, is the most defining  part of taking your lighting to the next level.  Because when you have an understanding of how, when, and why shadows are...


### VSM vs Raytraced Shadows [13:18]
**Transcript:** Now with that said, I want to take the time to show you the difference between the default  Lumen virtual shadow maps and ray traced shadows.  So to demonstrate that, I'm going to create a rect light here, drag and drop it here  like that.  And what I want you to pay attention to is the following.  So by zooming in here, you'll see the shadows are kind of sharp, they're soft, but they're  also kind of sharp.  We get this odd banding, we get this artifact here, the same thing here, we get a bit  of a hard edge there.  This is a limitation of virtual shadow maps.  You can't push the shadow penumbra that far before it starts falling apart.  That's where ray traced shadows come in.  This is why I recommend using hardware ray tracing if you have it.  It will make a big difference.  So if I select my rect light here and search for ray, you'll see here I've got cast ray  tracing shadows, I'm going to set this here.  And before I do, pay attention to the quality of the shadows right here.  To enable it, you'll see the shadow got much softer, much better, no more ugly artifacts.  The shadows are just better in every single way.  It's day and night, it's no comparison.  To demonstrate this e...


### Helpers & Guides [16:07]
**Transcript:** Now you might be wondering why I have four random spheres of different colors here.  These spheres are there to help you gauge the exposure and lighting of a scene.  We've got a black one with an albedo of 0.04, because no natural material out there is  pure black.  Cole has an albedo of 0.04, so I'll be using that as my baseline.  We've got a white one with an albedo of 0.85, because the albedo of fresh snow is about  0.8 to 0.9.  No object or material out there reflects 100% of all the light.  Everything absorbs at least a little bit of light, so you don't want any material in  your scene to have an albedo value of one.  It's not physically possible, and it will throw off your lighting.  Then we have a gray ball here with an albedo of 0.18, which is actually the middle gray  value.  You would think that the middle gray value between 0 and 1 is 0.5, right?  50% gray?  Well, not quite.  Exposure is a bit more complicated than that, and it is not linear.  This may seem counterintuitive, but 18% gray is, in fact, the middle gray between black  and white.  This gray ball helps you figure out the correct exposure of a given scene.  At least it should give you a really good starting poi...


### Indirect Lighting [17:45]
**Transcript:** you.  Now one of the main advantages of using Lumen involves the ability to control the indirect  lighting.  So to demonstrate this, I've created an amazing looking house right here.  So by going inside here, we'll see we do have a little bit of indirect lighting coming  in on the top here and a little bit on the side, but it's not very much.  Unfortunately, we have three different ways to control the amount of indirect lighting  using Lumen.  The first and easiest way is to select your light and increase the intensity of your light.  So let's say if I set this to 50, you'll see, as a result, we get way more indirect  lighting coming inside here.  But you know, it's still not very much.  The next thing we can do is, again, selecting our directional light and you'll see here  we have indirect lighting intensity.  If I set this to higher to something like five, you'll see our indirect lighting has  been accentuated quite a bit.  But that leaves us our third option and this is actually the option you should keep in  mind most of the time.  When you're using Lumen, the Albedo or the base color value directly contributes to the  amount of light being bounced around.  So by selecting thi...


### Reflective Objects Quick Tip [20:17]
**Transcript:** Hey, so future wheel chiming in here.  I just wanted to take a quick moment to talk about something I get a lot of questions  about.  And that's in regards to very shiny, reflective or metallic material.  So zooming in here on my chrome ball here, you'll see we get some reflections, but this  doesn't really look like a chrome ball at all, right?  Because everything is black.  This doesn't feel very metallic.  And you might be wondering why the reason for that is because there's nothing to reflect  in the scene.  You have a totally black, empty blank scene.  And as a result, metallic or reflective materials are not necessarily going to look right because  shiny reflective materials are dependent on having something to reflect.  So a quick and easy way to get something to reflect in here is to add an hderi backdrop  like we added earlier.  Like this.  And you'll see right away we have our sky and our environment around it working just fine.  And the reason that's working is because this hderi backdrop has a skylight actor in  it.  So I'm going to delete this and I'm going to create a skylight.  I know I said I wasn't going to show you the skylight in this part of the video, but in  t...


### Emissive Materials [23:13]
**Transcript:** show you before we start lighting our environment, that's emissive materials.  So I'm going to create what we call an emissive material because Lumen actually allows emissive  materials, glowing materials to emit light as I'll demonstrate right here.  So we're going to right click on our content browser, create a new material.  I'm going to call this emissive.  They're one.  Open this material up and I'm going to create three nodes.  I'm going to present hold the one key and click, present hold the three key and click and  present hold the empty and click.  I'm going to select these two nodes right click convert to parameter and I'm going to call  this one light color.  I'm going to call this one light intensity.  I'm going to plug light intensity into B of the multiply node and plug the light color  into the A of the multiply node and plug the multiply into emissive color.  I'm going to set the light intensity to something like 100 and set the light color to something  ridiculous like a bright flashy or injure something like that and hit OK.  Now we're going to hit save.  I'm going to make this window smaller and I'm going to apply this material to one of  our spheres here.  Like ...


### Lighting your Scene & Daylight [25:21]
**Transcript:** this does work.  So now that we have an understanding of how the lights work, how to bend and shape the  light the way we want.  Now we're ready to get started and light this entire scene here from scratch.  So I'm going to go ahead.  I'm going to delete all of these lights and start off with a completely blank slate.  And you'll see it's a whole lot easier than you might think.  So I'm going to be using the Megascans Abandon apartment scene that you can find for free  on the epic marketplace.  So go ahead and download that if you want to follow along.  Now before we get started, I want to do a little segue into explaining that Lumen  works a lot better with Nanite meshes.  Performance wise, you're going to get much better frame rates if you convert as many  meshes to Nanite as possible.  I've made a dedicated video on Nanite right here so you can check that out if you're  so inclined.  But if I go here to lit, go to Nanite Visualization, Triangles, you'll see everything that had  a colorful triangle on it is actually a Nanite mesh.  This project here, the Megascans Abandon apartment scene, does not have Nanite turned  on by default.  So what I did is in the content browser, I filt...


### GODRAYS! [33:49]
**Transcript:** And there's still one or two more things we can do to really push this scene to the  next level.  And what we're going to do now is we're going to select our exponential height fog, scroll  down, and we're going to turn on volumetric fog.  Because I want to have some god rays shining through here.  And I'm not a huge fan of like the blueish tint that the fog has here.  Switching this to volumetric fog is going to fix that for us.  So by clicking here, you'll see now we got rid of the blueish ugly tint.  And we got a bit more god ray shining through.  You'll see that god rays are not very visible though.  So we can go accentuate those very easily by selecting our directional light and scrolling  down.  And we see here we have the volumetric scattering intensity.  I'm going to set that to 10 to really exaggerate it for effect.  And you'll see now we have god rays shining through our windows thanks to volumetric  fog.  So you'll see environment light mixer, exposure compensation, volumetric fog.  And we've gotten our scene in a very good place.  As I rotate the sun, the fog is going to update automatically.  It is frankly ridiculous how easy it is to get the scene looking so good so q...


### Overcast Lighting [39:19]
**Transcript:** But what if we wanted to make this scene a gloomy, dark, overcast day feel?  How would we do that?  Again, we're going to select all of our lights and start from scratch.  I'm going to select everything except for the PPV and the fog because I want to keep  both of those.  Again, now we have a totally dark scene to work with.  What we're going to do now, we're going to create the HDRI backdrop and drag and drop  it into the scene like this.  I got to move it down a little bit lower.  And just like that, I mean literally one click.  We're in a pretty good place already.  It's not perfect, but as you can see, the HDRI backdrop did a whole lot of work for us.  Right?  We got some nice, soft lighting coming through the door here.  This light coming into the opening in the wall, it looks really good.  Now again, we're only about 80% done.  There's still one or two more things we can do here to really make this.  Okay?  So as you'll see right here in the video, we got a whole lot of jittering in here.  And that's again, usually due to the fact that it's only in direct lighting.  So we're going to add a bit of direct lighting to help with that.  And what we're going to do is I'm going to ...



---

## Structured Notes

### Core Technique
Dynamic lighting with Lumen in UE5 — all light types, soft shadow fundamentals (source radius / shadow penumbra), indirect lighting control, emissive materials as light sources, volumetric fog god rays, HDR environment setups for interior and exterior scenes.

### Summary
Comprehensive 44-minute beginner lighting tutorial for UE5 with Lumen. Covers every light type, the crucial concept of source radius controlling shadow softness, indirect lighting via albedo contribution, emissive Lumen light emitters, using HDRI backdrop for reference and IBL, volumetric god rays, and two complete lighting scenarios from scratch (daylight interior, overcast exterior).

### Key Steps

**Project Setup for Best Lumen:**
1. Project Settings → Default RHI: DirectX 12
2. Rendering → Lumen: Dynamic Global Illumination = Lumen
3. Array Lighting Mode = Surface Cache; Software Ray Tracing = Detailed Tracing
4. Shadow Map Method = Virtual Shadow Maps
5. Enable "Support Hardware Ray Tracing" + "Hardware Ray Tracing When Available" (RTX GPU required)

**Light Types:**
| Light | Use Case |
|-------|----------|
| **Directional Light** | Sun / moon; exterior; casts parallel shadows |
| **Point Light** | Omni; light bulbs, candles |
| **Spot Light** | Cone; flashlights, theatre spots |
| **Rect Light** | Soft area light; TV screens, windows, panels |
| **Sky Light** | Captures sky + environment → fills shadows with ambient color |
| **HDRI Backdrop** | IBL environment from HDRI; includes Skylight |

**Source Radius = Shadow Softness (The Magic Sauce):**
- Larger source radius → larger light contact area → softer shadow penumbra
- Point/Spot/Rect: set `Source Radius` in Details panel
- For best soft shadows: enable `Cast Ray Tracing Shadows` per-light (needs HWRT)
- VSM limitation: penumbra artifacts appear at large radius; HWRT shadows = clean soft penumbra

**Indirect Lighting — Three Controls:**
1. Increase light intensity
2. Increase `Indirect Lighting Intensity` on light actor
3. Increase material Albedo (Base Color) value — higher albedo = more bounce light

**Emissive Materials as Lumen Light Sources:**
```
Material Editor:
- Multiply node: LightColor (vector parameter) × LightIntensity (scalar, e.g. 100)
- Plug Multiply → Emissive Color
- High Emissive values (50-200) = visible GI contribution through Lumen
```

**Volumetric Fog / God Rays:**
1. Exponential Height Fog → Details → Enable Volumetric Fog ✓
2. Directional Light → Details → Volumetric Scattering Intensity (1-10)
3. Higher = stronger god rays through windows

**Reference Spheres for Calibration:**
| Sphere | Albedo | Represents |
|--------|--------|-----------|
| Black | 0.04 | Coal / darkest real material |
| 18% Gray | 0.18 | Middle gray; correct exposure check |
| White | 0.85 | Fresh snow / brightest material |

**Daylight Interior Setup (Megascans Apartment):**
1. Place Directional Light → rotate sun angle
2. Atmosphere Sun Light: enabled
3. Place Sky Atmosphere
4. Place Exponential Height Fog (Volumetric on)
5. Place Skylight → Real Time Capture
6. Use Environment Light Mixer (Window → Env Light Mixer) to manage all lights
7. Adjust Directional Light Intensity + Color Temperature
8. Adjust PPV Exposure Compensation

**Overcast Exterior Setup:**
1. HDRI Backdrop → drop in scene
2. Choose overcast HDRI
3. Sky Atmosphere actor for atmospheric scattering
4. Minimal Directional Light (weak fill) + add volumetric fog

### UE Systems / Blueprints / Settings

**Nanite + Lumen Performance Tip:**
- Convert mesh to Nanite → Lumen performance improves significantly
- Nanite Visualization: Viewport → Nanite Visualization → Triangles

**Lumen Project Settings Recap:**
```
Dynamic Global Illumination Method = Lumen
Reflection Method = Lumen
Lumen Scene Lighting Quality = 1 (realtime) to 4 (high quality)
Shadow Map Method = Virtual Shadow Maps
Support Hardware Ray Tracing = True (RTX required)
```

**Environment Light Mixer (Window menu):**
- One panel to control Directional Light, Sky Light, Sky Atmosphere, HDRI Backdrop
- Fast iteration without hunting actors in Outliner

**Cast Ray Tracing Shadows toggle (per light):**
- Select light → Details → search "ray" → Cast Ray Tracing Shadows ✓
- Requires HWRT project setting + RTX GPU

### Difficulty
Beginner — foundational lighting concepts; no prior UE or lighting experience needed

### UE Version
UE5 with Lumen (fully dynamic, no baked lighting)

### Tags
lighting, lumen, beginners, directional-light, point-light, spot-light, rect-light, virtual-shadow-maps, ray-tracing, emissive, volumetric-fog, hdri, skylight, exposure, soft-shadows, indirect-lighting, william-faucher, beginner, ue5

---

## Related Entries
- `references/rendering-pipeline.md` — Lumen settings, Path Tracing, TSR, post-process
- `tutorials/designing-visuals-rendering-and-graphics-with-unreal-engine.md` — Full Lumen docs, Virtual Shadow Maps
- `tutorials/lumen-explained-important-tips-for-ue5.md` — (William Faucher) Advanced Lumen tips
- `tutorials/things-to-know-about-lumen-unreal-engine-5.md` — (William Faucher) Lumen tips overview
