---
title: It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=MJQ-0tmIhQk
author: Karim Yasser
ingested: 2026-06-15
ue_version: "UE 5.x (MegaLights present → UE 5.5+)"
tags: [lighting, interiors, lumen, hardware-ray-tracing, post-process, volumetric-fog, megalights, console-commands, intermediate, advanced, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5/
frame_count: 13
---

# It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=MJQ-0tmIhQk)
**Author:** Karim Yasser
**Duration:** 33m5s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** And today's video is going to discuss interior lighting to do this scene from scratch step by step  and fix indirect lighting issues with Lumin, eliminate the blotches and flickering,  improve volumetric fog and shadows, and understand the approach of interior lighting in Unreal Engine.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_000.jpg

### Project Settings [0:12]
**Transcript:** So to start with interior lighting, we need to adjust first our project settings.  So we can go here in Edit, Project Settings, and scroll down for Rendering.  And we need to use bunch of options actually for Lumin and Red Tracing  and to give our scene these kind of soft shadows in it.  So let's scroll down.  We need first to ensure that we have dynamic global eliminations at the Lumin.  Same goes for reflections.  And here in the support hardware ray tracing, this need to be enabled.  And this one as well, ensure it's enabled.  Use hardware ray tracing when available.  And regarding ray lighting mode, we can adjust it later in our process volume  and test out different settings in it.  Also, we don't need to use generate mesh distance fields as we are going to depend on hardware  ray tracing. Scroll down here. I need to ensure local exposure, highlight contrast and shadow  contrast are set to 1. I just like to have it as default on 1.  And here in the G buffer format, set it to high precision normals.  And if you want to use mega lights, it's fine to turn it on.  I want to keep it on actually because mega lights will give me this kind of soft shadows as well  because it uses grea...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_001.jpg

### Lighting Cleanup - Remove Baked Lighting [2:20]
**Transcript:** So let's first of all ensure we don't have any light in here. Remove all of them.  All of these light actors.  And let's ensure we don't have any reflection actors as well.  Sponential height fog, post-process volume. All of these actors needs to be deleted.  And for our sky, for me it's fine to give it as it is for now as we are going to use it.  Maybe we can try different texture or just hide it with the fog or so.  So for now this is our scene, it's completely black but we would need to ensure it doesn't have  any pre-computer lighting. So I can go to Window, World Settings, and here in Lightmass,  up in this option, reset all of these settings, go to Advanced, and here we can see Light Maps.  They are added already. So let's head for Snowpreet commuted lighting. It's okay.  And here if it doesn't work, select build all levels. And just like that, Light Maps will be zero.  And if it's not updating, you can restart the level directly and it will work.  So now we have our scene ready, it's clean, it doesn't have any big lighting, and all good to go.  So what we will need to do first, in my opinion I need to disable all of these  emissives first of all. So I can go here, set the em...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_002.jpg

### Skylight Setup [4:52]
**Transcript:** let's see if we can control the tent. Yeah, we can. Let's control our tent. I want to have  somehow a night lighting, moody, very soft. So let's try to have it like that. Maybe around  0.5 0.6. It's fine. Save. And for the massive, give me that one. And let's add a folder for lighting.  There is lights, let's call it lighting. Right click on it, make current folders. So anything we  add in here will be dropped automatically to this lighting folder. So I'm adding a boss process  volume, scroll down, enabling infinite extent. So it affects all my environment without the need  to rescale it. Go here in exposure. I'll just go with the very basic exposure, set it to one and  one and start working from this base, also setting exposure compensation on zero. So I can now  select my sky, make it a little bit brighter, you're around 5, probably. And I will need to move  this sphere to our lighting folder and add a skylight. So I can start getting more ambient lighting  in there. And in my opinion, it's very blue currently. So I can go in my sphere and reduce the  saturation of my sky. Go here in the tent and reduce the saturation to going to probably or  2.25. Go back to the skylight and hit...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_003.jpg

### Tone Mapping [7:23]
**Transcript:** turn map our scene without the need to add a lot of lights in there. So let's go to local exposure.  Let's try to set this one to 0.6. And let's keep the highlight contrast as it is. Maybe here for  the two, let's reduce it a little bit. And we can see more details in here already without the  need to add a lot of lights. And let's actually try to add our fog volume, reset the location of it.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_004.jpg

### Fog & Atmospherics [7:54]
**Transcript:** And let's give it a color. Something probably. Just give it one one. Let's try color.  Maybe like that. I just want to give it this color or cyan color. Like it's very saturated actually.  So I'm just trying a new color in here. It's not like blue or very blue night. It's enabled for  the metric fog. And actually it's too bright outside. So I can use the value of it to make it  better. Yeah, like that. And if I try to hide the sky sphere, it might be really looking better,  but our skylight will not be working good. So we need to keep it actually. So let's keep our fog  like that. And let's try to add a spotlight. So it's more like outside or exterior lighting.  Let's give it like this. Let's disable this nabbing. And here let's try to make this 100 maybe a thousand.  That it's right actually to go very crazy number like 10,000. So good color. Let's get the same  hue from here. It's the 94. And almost 2.7. It would be good. Let's try to make the cone smaller.  That. And let's try to add very strong volumetric scattering, but you'll see why I'm doing this now.  Let's get back to the another view board. Switch it to on left. And I can right click on this light.  Go to pilot. And I ca...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_005.jpg

### Fix Ray Tracing Shadows [12:11]
**Transcript:** will work much better. Cosratorate shadows doesn't work perfectly with submeshes, especially like translucent  meshes or so. So we can try it like this. And let's try to increase the attenuation radius a little  bit. Try 1500. This is too much actually my opinion. Back intensity, but I can reduce it like 5000  or try 2000. Yeah, maybe 2000 is good. And this increases the volumetric scattering to 100 probably.  As you can see now it's very soft. Like it's already much better. And if I try to increase the  outer context just increases the intensity here. So I can try 40. And so it could be adding more  intense light as the fall of is going to be sharper. So it's stick to 20 could be good. And here for  this light it's very very sharp currently as you can see. These shadows are too sharp. So we can  increase the source radius like that. And the source radius basically increases the size of the  light itself. So as you can see this yellow sphere is the source radius. And the bigger it becomes  the softer the shadow will be. Let's actually try to add another  I just need to plug my light in that better way. So this should be better actually.  So let's try here to increase the source rad...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_006.jpg

### Soft Shadow & Specular Fix [14:16]
**Transcript:** or actually before fixing it. If we try to see it from a chrome bowl let's apply a chrome  material to it. We try to see it from here. As you can see there is a big big sphere from our  light source. So in order to fix it there is two ways. You can go down here and reduce the  specular scale. But that will make you lose your specular reflections on your meshes.  Or you can increase this one soft source radius. Increasing it will make it softer. So it will  be more diffused and much better. So we can get back here. And as you can see the soft source radius  is already making it much much better softer. And it does make more sense actually as light source.  So let's reduce this light source a little bit. So as you can see now it's very soft like that.  Maybe the fog is too thick and we will reduce it. And the soft source radius could be reduced as well.  Maybe 200 could be good. So now our light is very very soft actually and it's not eliminating

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_007.jpg

### Adding Lights & Polishing [15:36]
**Transcript:** everything in the scene like that. It's not very good. I'm just limiting it to this specific  place. So it's feeding out and it looks much better. And if we try to make it like that could be  even better. Like this. So it's even softer. You can try a lot of things in here actually.  But let's stick to it like this. You might notice there is some noise still in here. This is  related to Lumin and yeah same goes here. So we will need to fix it for sure. But I think the  intensity is too much for now. Let's reduce the intensity a little bit. Maybe it's still too intense.  I think 1000 could be good. Yeah, let's give it 1000 but reduce the volumetric scattering.  Let's try 80 could be good or actually let's give it on thread.  Yeah, 100 could be good. Yeah, 100 is good. And here for indirect light intensity if we try it  more. Because you can see it adds even more to your eye in there. Let's stick to two or three  could in our case. And here's still I want to add more lighting actually to fill in these very  dark shadows. So I can use other point lights probably. Let's add one here.  And it's very very sharp right now. So we need to fix it. As you can see this very sharp  doesn't work ...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_008.jpg

### Post Process Color Grading [21:44]
**Transcript:** adding more effects in there. So we can use convolution bloom if you want to have  a different shape of the bloom like that.  But as you can see, this is not very good. This is too much. And it's not working as expected.  So let's reduce it. We can just keep it on one or two. Maybe.  Two could be good. One. Maybe 1.5. And for chromatic aberration,  we need slightly more chromatic aberration.  Still a wind one. Look at exposure. We can adjust the shadow contrast now. Instead of the  0.6, we can have a light layer number like that. Same goes for highlight contrast if we want  to reduce it. So it affects our exterior lighting like that. But I like it. I actually  just give it as it is. Or if you wanted to increase it to have more contrast in there.  For detailed strength, I like to increase it. Maybe 1.2. But that will affect our highlights.  So we need to get back to our bloom and reduce it. One.  And major effects. Let's add some more sharpen and slightly. That in color grading,  I like to reduce the shadow saturation. Let's try to wind 4.5. And in the gain.  Maybe I can give it a little bit of finish or close attempt.  But this is too much actually. Maybe increase it.  So it's the ...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_009.jpg

### Fix Lumen Noise [25:18]
**Transcript:** So this is already the best version of looming that it is possible. You might notice this kind of  flickering in here and in there as well. So we will need to use this console command.  R.looming.c.in.radiosity.visualized.prox.  As you can see now, this is how the Omin is trying to work. So that's why it's  flickering a lot. We can fix that by using R.looming.c.in.radiosity.emisphere from resolution.  And the default value of it currently is 4. So let's try 32. So it's already much better.  So this is 4. As you can see it's very, very fast and it's trying to update very fast way.  This is slightly better now. So we can try to use that to fix this problem. Let's get back to zero.  And here we can increase the lumensine lighting quality and lumensine data. Let's say post 4.  And this affects our lumensine view. We can go here in lumensine and see it probably.  As we can see now, our process volume, we try to set this one to the lowest possible.  Like a lot of objects are already removed from the renderer of the domain.  So increasing it will make it better. And here in final gather quality, let's try to increase it for.  And in advanced settings, if you wanted to use lumensine to red...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_010.jpg

### Improve Volumetric Fog Sampling [30:03]
**Transcript:** how you think about it if you have a light source or a big opening like that and how you can  use effects, your shadows make it softer and get even better lighting. And we have still one  thing left. We can see here in the volumetric fog, it could be even better. So we could try  our dot volumetric fog. Let's try grid pixel size. Divoled value is eight. And if you are going  lower you will basically get better fog. But be careful with it because it could draw  when you were to be performance and it might crash. So I'm trying to go to four.  As you can see now four is even softer and much, much better. This is eight. It's not looking good.  This is 16 if you want to get bad. This is four. This is one. As you can see one is very, very soft  because it's casting the volumetric shadowing actually from these meshes. So that's why it's  looking very soft and good. Let's give it to three. It could be good in this case. And there is  another one actually which is a red size z. It's default value is 128 and you can go higher.  So let's try 512. See how it looks. This is 512 and this is 128. This is 32. 32 as you can see  it's really, really bad. So you'll need to increase it. 12 could be go...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_011.jpg

### Quick Note [32:41]
**Transcript:** Render lighting. I hope you enjoyed it. And don't forget to join our discord community if you  want to get more tips and learn more about lighting, the environment, characters, anything related  to game art. Feel free to join our discord community and stay in touch with other talented people  so that's it for today's video. See you next time.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_012.jpg


---

## Structured Notes

### Core Technique
Complete interior Lumen HWRT lighting workflow from a clean scene — build-order: project settings → clean slate → sky base → PPV exposure → single exterior spotlight with volumetric fog → fill lights → color grade → fix Lumen flickering with hemisphere resolution console command → improve volumetric fog quality with grid sampling console commands.

### Summary
Karim Yasser (AAA professional) walks through the full process of building cinematic interior lighting for a restaurant/cafe scene in UE5 from scratch. The approach relies on Lumen Hardware Ray Tracing with MegaLights enabled, a single high-intensity Spotlight as the exterior moon source, and Exponential Height Fog for volumetric atmosphere. The tutorial's most distinctive value is two sets of specific console commands: one to fix Lumen's screen probe flickering noise (`r.Lumen.ScreenProbes.Radiosity.HemisphereFromResolution`) and one to improve volumetric fog softness (`r.VolumetricFog.GridPixelSize` / `r.VolumetricFog.GridSizeZ`). Scene progression captured across 13 frames from pure black → near-final cinematic moody interior.

### Key Steps

#### 1. Project Settings (Edit → Project Settings → Rendering)
- `Dynamic Global Illumination Method` → **Lumen**
- `Reflections Method` → **Lumen**
- `Support Hardware Ray Tracing` → **true**
- `Use Hardware Ray Tracing When Available` → **true**
- `Generate Mesh Distance Fields` → **false** (not needed with HWRT)
- `Local Exposure Highlight Contrast` → **1**, `Shadow Contrast` → **1**
- `GBuffer Format` → **High Precision Normals**
- `MegaLights` → **enabled** (soft shadows without point-light config overhead)
- Restart editor after changes.

#### 2. Clean Slate — Remove All Existing Lighting
- Select and **delete all light actors** (DirectionalLight, PointLights, SpotLights, RectLights)
- Delete all **Reflection Capture actors** (SphereReflectionCapture, BoxReflectionCapture)
- Delete **Exponential Height Fog** and **Post Process Volume**
- Keep the sky sphere actor for now
- Go to `Window → World Settings → Lightmass → Advanced` → hit **Invalidate Lightmass** or **Build All Levels** to zero out all Light Maps
- **Disable emissive materials** temporarily so they don't pollute the Lumen GI base

#### 3. Add Post Process Volume — Base Exposure
- Add a `Post Process Volume`, tick **Infinite Extent**
- `Exposure → Metering Mode` → Manual, set **Min/Max Brightness = 1, 1**, `Exposure Compensation = 0`
- This locks exposure so light changes are predictable as you build the scene

#### 4. Skylight — Night Ambient Base
- Adjust Sky Sphere texture saturation (sky material → reduce saturation, target ~2.25 to desaturate the blue night tone)
- Set Sky Sphere emissive intensity ~**5**
- Add a **Skylight** to the lighting folder, set intensity ~**0.5–0.6** for night mood
- Result: very subtle cool ambient in the interior (frame_003: interior nearly black, windows glowing white)

#### 5. Local Exposure Tone Mapping (PPV)
- `Post Process Volume → Local Exposure` → `Highlight Contrast = 0.6` (pulls shadow detail into dark interior without adding lights)
- `Shadow Contrast` adjust as needed (~2.0)
- This brings out interior detail before any fill lights are placed

#### 6. Exponential Height Fog — Atmosphere
- Add `Exponential Height Fog`, reset location
- Set **Fog Inscattering Color** to a muted cyan/night tone (avoid oversaturated blue)
- Adjust **Fog Density** via the value/brightness (too bright = fog washes out interior)
- Enable **Volumetric Fog** on the EHF component

#### 7. Exterior Spotlight — Main Moon/Sun Source
- Add a **Spotlight** as the exterior light source (moon or filtered daylight through window)
- Initial settings: **Intensity = 10,000**, small **Inner/Outer Cone Angle** (~20° outer), **Attenuation Radius = 1500–2000**
- Color: hue 94, saturation ~2.7 (cool blue-white moonlight)
- **Volumetric Scattering Intensity = 80–100** (creates visible god-ray shafts through windows)
- Use **Right-click → Pilot Light** in the viewport to fly the spotlight through the window opening and aim it into the interior without guessing position values
- `Indirect Lighting Intensity = 2–3` to boost bounce light into dark corners

#### 8. Source Radius vs. Soft Source Radius — Shadow & Specular Fix
- **Source Radius** = makes the light source physically larger → **softer shadows**, but also enlarges the specular highlight on reflective surfaces (can look wrong on chrome/metals)
- **Soft Source Radius** = diffuses the specular reflection only, keeps shadow softness → **use this for interiors** where you want soft shadows without a giant specular blob
- Workflow: increase Source Radius for shadow softness, then dial in Soft Source Radius (e.g., 200) to fix the specular — verify with a chrome sphere placed in the scene
- Do NOT reduce `Specular Scale` to fix the specular blob — it removes reflections from all geometry

#### 9. Fill Lights
- Add **Point Lights** in the darkest interior corners as fill
- They will initially have sharp shadows — apply the same Source Radius trick for softness
- Keep fill lights at low intensity (they're supporting, not primary)
- Use `Outer Cone Angle` adjustments on the spotlight to control falloff sharpness

#### 10. Post Process Color Grading
- `Bloom` → Convolution Bloom, Intensity **1–1.5**
- `Chromatic Aberration` → slight (0.5–1.0)
- `Local Exposure Shadow Contrast` → reduce from 0.6 toward 0.4 for more shadow detail
- `Detail Strength` → **1.2** (adds micro-contrast, sharpens surface detail)
- `Shadow Saturation` → reduce to ~**0.45** (desaturates deep shadows for a filmic look)
- `Gain` → slight warm/finish tint

#### 11. Fix Lumen Screen Probe Noise / Flickering
The main two console commands for interior Lumen quality:

```
// Debug view — shows how Lumen screen probes are sampled
r.Lumen.ScreenProbes.Radiosity.Visualize.Proximity 1
// (set to 0 to turn off)

// Fix flickering — raise from default 4 to 32
r.Lumen.ScreenProbes.Radiosity.HemisphereFromResolution 32
```

Also in PPV → Lumen GI:
- `Lumen Scene Lighting Quality` → increase (e.g., 4)
- `Lumen Scene Detail` → increase (e.g., 4)
- `Final Gather Quality` → **4**
- `Ray Lighting Mode` (Advanced) → `Surface Cache` or `Hit Lighting` — test both

#### 12. Improve Volumetric Fog Sampling
Two console commands — significant visual improvement for interior fog shafts:

```
// Horizontal fog grid resolution — default 8, lower = softer/better
// Warning: very low values (1) can crash — use 3–4 for production
r.VolumetricFog.GridPixelSize 4

// Vertical fog grid resolution — default 128, higher = better
r.VolumetricFog.GridSizeZ 512
```

Values to compare:
- GridPixelSize: 16 (bad) → 8 (default) → 4 (good) → 1 (very soft, risky)
- GridSizeZ: 32 (bad/noisy) → 128 (default) → 512 (clean)

### UE Systems / Blueprints / Settings

**Project Settings → Rendering:**
- Dynamic GI = Lumen | Reflections = Lumen
- Support HWRT = true | Use HWRT When Available = true
- Generate Mesh Distance Fields = false
- GBuffer Format = High Precision Normals
- Local Exposure Highlight/Shadow Contrast = 1
- MegaLights = enabled

**Actors:**
- Skylight (intensity 0.5–0.6, adjust sky sphere saturation)
- Exponential Height Fog (Volumetric Fog = true, muted cyan color)
- Spotlight (10,000 intensity, cone ~20°, attenuation 1500–2000, Source Radius + Soft Source Radius)
- Post Process Volume (Infinite Extent)

**PPV Settings:**
- Exposure: Manual, Min/Max = 1, Compensation = 0
- Local Exposure Highlight Contrast = 0.6
- Final Gather Quality = 4
- Lumen Scene Lighting Quality = 4
- Lumen Scene Detail = 4
- Bloom Convolution Intensity = 1–1.5
- Detail Strength = 1.2
- Shadow Saturation = 0.45
- Chromatic Aberration = 0.5–1.0

**Console Commands (paste in UE console `~`):**
```
r.Lumen.ScreenProbes.Radiosity.HemisphereFromResolution 32
r.VolumetricFog.GridPixelSize 4
r.VolumetricFog.GridSizeZ 512
```

### Difficulty
Intermediate / Advanced

### UE Version
UE 5.5+ (MegaLights feature referenced; Lumen HWRT available since UE 5.0 but MegaLights is UE 5.5+)

### Tags
`#lighting` `#interiors` `#lumen` `#hardware-ray-tracing` `#post-process` `#volumetric-fog` `#megalights` `#console-commands` `#intermediate` `#advanced` `#youtube` `#ue5`

---

## Frame Analysis

**frame_000:** Target reference — moody restaurant interior, dark with warm light through large windows, chairs and tables, very cinematic. Pre-production reference.

**frame_001:** UE5 editor early stage — restaurant with warm ambient, light fixtures active, relatively bright overall. Project settings done.

**frame_002:** After lighting cleanup — mostly dark interior, minimal window light, World Settings panel visible.

**frame_003:** Skylight + PPV added — interior almost completely black; windows show pure white blown-out exterior. Shows how dark a zero-bake Lumen interior starts before building up lights.

**frame_004:** EHF added — slight cool/cyan tint appearing in the atmosphere. Interior still very dark but atmosphere is taking shape.

**frame_005:** Spotlight piloting — large white blown-out fog beam visible in the scene (the spotlight being positioned through window). Thick volumetric fog test.

**frame_006:** Exterior spotlight configured — blue-cool moonlight spilling through windows. Restaurant interior visible. Details panel showing Source Radius / spotlight settings.

**frame_007:** Source Radius overexposure issue — the entire scene is blown out / overexposed. This shows the problem when Source Radius + specular is too large.

**frame_008:** Fill lights added — warm red/orange light from right side (fire or lamp prop). Scene darkening toward the intended mood.

**frame_009:** Color grading applied — restaurant looking polished and cinematic. PPV color grade panel visible on right.

**frame_010:** Lumen debug view — Lumen ScreenProbe radiosity debug visualization (dots/probes visible on all surfaces). Console command `r.Lumen.ScreenProbes.Radiosity.Visualize.Proximity 1` active.

**frame_011:** Improved volumetric fog — soft god-ray shafts through windows. `r.VolumetricFog.GridPixelSize 4` applied.

**frame_012:** Near-final result — dark moody restaurant interior, excellent soft shadows, subtle volumetric, cinematic color grade. Very close to target frame_000.

---

## Related Entries

- [[lighting-interiors-in-unreal-engine-5]] — William Faucher's interior lighting tutorial (same topic: Lumen + HWRT + path tracer reference, light bleeding fix, Diffuse Color Boost). Shares: `#lighting` `#interiors` `#lumen` `#hardware-ray-tracing`
- [[how-i-use-lumen-in-aaa-projects-unreal-engine-5]] — Same author (Karim Yasser), HWRT vs SWRT selection, Final Gather Quality, Ray Lighting Mode. Shares: `#lumen` `#hardware-ray-tracing` `#post-process`
- [[lumen-explained---important-tips-for-ue5]] — Lumen internals, surface cache, emissive best practices. Shares: `#lumen` `#global-illumination` `#hardware-ray-tracing`
- [[things-to-know-about-lumen-unreal-engine-5]] — Project settings for Lumen (DX12, HWRT, VSM). Shares: `#lumen` `#project-settings`
- [[designing-visuals-rendering-and-graphics-with-unreal-engine]] — Full Epic rendering docs (Lumen, post-process, volumetric fog). Shares: `#lumen` `#rendering` `#post-process`
