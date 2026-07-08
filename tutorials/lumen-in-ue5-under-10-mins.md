---
title: Lumen in UE5 Under 10 Mins
source: YouTube
url: https://www.youtube.com/watch?v=RSImMVfCnYQ
author: Karim Yasser
ingested: 2026-07-08
ue_version: "UE5 (version unspecified)"
tags: [lumen, global-illumination, hardware-ray-tracing, software-ray-tracing, surface-cache, hit-lighting, ambient-occlusion, reflections, post-process, console-commands, project-settings, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/lumen-in-ue5-under-10-mins/
frame_count: 12
---

# Lumen in UE5 Under 10 Mins

**Source:** [YouTube](https://www.youtube.com/watch?v=RSImMVfCnYQ)
**Author:** Karim Yasser
**Duration:** 9m19s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** You might never know that Lumen is ruining your scene performance and yet you cannot get  the target quality that you are aiming for.  So in today's video we will discuss steps for Lumen that will improve your lighting immediately.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_000.jpg

### Project Settings [0:12]
**Transcript:** So first of all we need to go to project settings to ensure we have the proper setup for our  project.  So go here down into rendering and first of all we need to ensure we have dynamic global  eliminations that the Lumen and same goes for reflections method.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_001.jpg

### Software Ray Tracing [0:26]
**Transcript:** And then if we wanted to use software ray tracing which is the cheapest option that  Lumen can use that will work on low profile hardware and this basically is using the  mesh distance fields to trace against and it uses the detailed tracing of the mesh distance  fields for the first two meters and then it fall backs to global tracing which is using  global distance field and it's better and faster for calculation.  So in order to ensure we are using software ray tracing we need to have use hardware ray  tracing when available to be turned off and support hardware ray tracing to be turned off  as well and generate mesh distance fields to be enabled and also we need to go here in  platforms in windows and we ensure we have shader and roll six enabled so we can start using  it.  Software ray tracing is still have some limitations it's not supported for all type of meshes  and it needs a meshes having a specific thickness at least 10 centimeters to ensure we don't  have any light leaking and still it's not supporting a lot of materials or shaders like  the word position offset and there are a lot more that is still limited unlike the hardware

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_002.jpg

### Hardware Ray Tracing [1:29]
**Transcript:** ray tracing which supports a wide variety of options and to ensure we can use it the best  option quality is first to turn off generate mesh distance fields so we are not falling back  to software ray tracing because by default and really get back to it to save some more  performance and then we need to ensure support hardware ray tracing is turned on and use hardware  ray tracing when available is turned on as well and in this method it uses more accurate  representation of the triangles and pixels of the screen so it can have more details in  here and we can visualize it by going to let Lumen and Lumen scene currently it's using  something called surface cache but if we get back here to our project and change it  just little ray lighting mode to headlighting for reflections and also we need to ensure we  don't override it in here.  So now as you can see it has better representation of the mesh is it surface cache it's lower  resolution and this is it lighting for reflections it's already better and even headlighting is  much better and we will go in depth in them.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_003.jpg

### AO With Lumen [2:34]
**Transcript:** Also we need to ensure that we are using better ambient collusion because by default if we  wanted to go here in buffer visualization and scroll down to ambient collusion is set  to white which is not actually working with ambient collusion at all but Lumen is working  with it on its own calculations so in order to have better ambient collusion we have  to go here scroll down for allow static lighting ensure it's turned off and if you want to  use screen space ambient collusion with Lumen you can use these two console commands.  First one is R.Lumen the screen prop gather the short range AO set it to zero and the second  one is R.Lumen.diffuseandar.ssao we need to set it to one and now if we go here in our  boss process settings go to ambient collusion we can control the ambient collusion as you  can see it affects our scene and if we go here in buffer visualization scroll down to  ambient collusion we can see it now so it's working as before and you can override that  with these console variables and you can control it here as well you can increase the quality  of it you can control the power the intensity of these settings and that's instead of keeping  Lumen using its own AO calculations on its own if you want to override it with screen space ambient collusion.  There is another option as well related to screen tracing by default it's set to scene color but I

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_004.jpg

### Screen Tracing [4:01]
**Transcript:** tend to set up to anti-aliasing scene color because it supports translucency in a better way and  it reduces the flickering from the small immersive sources so it will give you much better quality and  more consistent and then here in our boss process settings we can go down and explore these settings.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_005.jpg

### Surface Cache Vs Hit Lighting For Reflections Vs Hit Lighting [4:19]
**Transcript:** First of all a lighting mode if we go here in Lumen Lumen scene service cache basically is trying to  represent these meshes in a lower resolution so it can get the indirect lighting and reflections  from it but it's not using hardware ray tracing so if you want to use hardware ray tracing you can  go to headlighting for reflections and also this one is really important for mirror reflections or  shiny surfaces so it will give you better reflections in it and as you can see it already has  better details and this one headlighting for reflections it uses better shadowed rays with the  reflection bus so it can give you much better reflections and representation in your scene but it  can fall back to surface cache in the second bounces but here in headlighting it's much better because  it uses these rays not only for reflections it's also using these rays for indirect lighting  bounces and reflections as well so technically this is much higher in cost but it gives you the best  possible quality from Lumen so we can notice it in here this is headlighting for reflections as you  can see it's not perfect in here but headlighting is much better already and this is service cache  the cheapest option possible so let's set it to headlighting which is a best possible option in here  but it's the most expensive option as well there is also an advanced option there is diffuse

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_006.jpg

### Diffuse Color Boost [5:45]
**Transcript:** color boost actually multiplies your base color values or diffuse values in your materials  and that increases the indirect light bounces but this is basically incorrect but it's really useful  if you want to have much better indirect lighting in your scene and it's closer to what actually the  past tracing is doing so if we try to set it to four as you can see it's really really bright  currently and that has a lot of indirect lighting and if we wanted to visualize it we can go to Lumen  Lumen scene and as you can see it's really bright this is one as you can see this is default color  values in here this is two this is three this is four so the max you can go is four and usually  these values are recommended to stay between one and two so you are not multiplying it by very high  number but it could be very useful for areas that you don't have a lot of indirect lighting in  there and you don't want to increase the amount of lights or indirect light intensity in your lights

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_007.jpg

### Sky Light Leaking [6:47]
**Transcript:** also there is a skylight leaking which is really useful if you have a skylight and your interior  is still a little bit dark you can quickly go here and increase the leaking and you might  not sit in here as you can see this is a very subtle here in this scene I actually don't recommend  to use this option a lot except in a few places let's go to reflections here first of all we can

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_008.jpg

### High Quality Translucency Reflections [7:06]
**Transcript:** use a high quality translucent reflection as you can see it gives you much better reflections  on your glass and if you go here in lumen lumen scene and turn off this one and get back here  and ensure it surface cache your reflections will not work really good as you can see here it's  giving you much better details on the translucent or reflective surfaces same goes for max roughness

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_009.jpg

### Max Roughness To Trace [7:37]
**Transcript:** and if we wanted to visualize it better go to let lumen did get it reflection rays and here  everything that is not in red is not getting calculated with lumen reflections probably so what  happens if we increase this number it will start including more objects in there and it's almost  everything added in there so that will give us better reflections so as we can see now this is  before and after it's tremendously changing these meshes in here and giving it better and better  reflection quality as you can see it's already much better and more cinematic but for sure this  affects your performance a lot so if you are aiming for performance you might need to reduce this  number below than you're going for and this is controlled by your roughness maps or your roughness  multipliers in your materials the more meshes you have with lower roughness value that will  affect your performance as well and you might not know why and here for max reflection bounces

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_010.jpg

### Max Reflection & Refraction Bounces [8:40]
**Transcript:** this is related to how many reflections you will see inside your reflections same goes for max  reflection bounces if we try to will give you slight better details in very small objects what the  aim is to get closer to what post tracing can actually achieve so that's basically it for lumen if  you want to have more details we created a session before it was a live session around four hours  and you can get it for free if you joined our community and ask it for your free license of it so  feel free to join the community from the link down below and ask for your free license so you can  get it and watch it thank you so much for watching and see you next time

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_011.jpg


---

## Structured Notes

### Core Technique
A settings-only Lumen quality/performance pass: choose Software vs Hardware Ray Tracing correctly in Project Settings, pick the right Ray Lighting Mode (Surface Cache vs Hit Lighting for Reflections vs full Hit Lighting) per shot, hand Lumen's Ambient Occlusion over to Screen Space AO via two console variables when needed, and tune a handful of Post Process Volume Lumen knobs (Diffuse Color Boost, Sky Light Leaking, High Quality Translucency Reflections, Max Roughness to Trace, Max Reflection/Refraction Bounces) — each knob traded explicitly against its performance cost.

### Summary
9m19s rapid-fire Lumen settings guide by Karim Yasser, framed around the idea that misconfigured Lumen is silently killing scene performance without visibly explaining why. Starts in Project Settings → Rendering: confirm Dynamic Global Illumination Method and Reflection Method are both set to Lumen. Explains **Software Ray Tracing** (cheapest, works on low-end hardware, uses Mesh Distance Fields for detailed tracing within the first 2m then falls back to the Global Distance Field) — enabled via Generate Mesh Distance Fields ON, Support/Use Hardware Ray Tracing OFF, plus Shader Model 6 enabled under Windows platform settings; limitations: unsupported for some mesh types, requires ≥10cm mesh thickness to avoid light leaking, doesn't support World Position Offset or several other materials/shaders. Explains **Hardware Ray Tracing** (best quality, traces actual triangles instead of distance fields) — enabled via Generate Mesh Distance Fields OFF (skips the SWRT fallback, saves perf) plus Support/Use Hardware Ray Tracing ON. Covers the three **Ray Lighting Modes** visible under Lumen → Lumen Scene: **Surface Cache** (default, cheapest, lower-resolution mesh representation for indirect lighting/reflections, no hardware ray tracing), **Hit Lighting for Reflections** (uses hardware rays specifically for the reflection pass, much better mirror/shiny-surface quality, but falls back to Surface Cache on second bounces), and full **Hit Lighting** (uses hardware rays for indirect lighting bounces *and* reflections — highest quality, highest cost, closest to path tracing). Ambient Occlusion: Lumen calculates its own AO by default (Allow Static Lighting must stay OFF, and the AO buffer visualization shows white/inactive by default because it's Lumen-driven, not SSAO); to override with Screen Space AO instead, set console variables `r.Lumen.ScreenProbeGather.ShortRangeAO 0` and `r.Lumen.DiffuseIndirect.SSAO 1`, then tune AO in the Post Process Volume as normal (power, intensity). Screen Tracing: switch from default Scene Color to **Scene Color: Anti-Aliased** for better translucency support and less flicker from small emissive sources. Post Process Volume Lumen knobs: **Diffuse Color Boost** (multiplies material base/diffuse color to fake extra indirect bounce light — physically incorrect but useful and closer to path-traced results; recommended range 1–2, max 4, very bright at 4). **Sky Light Leaking** (brightens dark interiors lit by a Skylight; author calls it subtle and advises using it sparingly, only in specific spots). **High Quality Translucency Reflections** (significantly improves reflections on glass/translucent surfaces; visibly worse without it under Surface Cache mode). **Max Roughness to Trace** (visualized via Lumen → Lumen Scene → "Reflection Rays" debug view — anything not shown in red isn't getting Lumen reflection rays; raising this value includes more/rougher meshes in reflection tracing for much better quality, at real performance cost; meshes with lower roughness values via roughness maps/multipliers cost more here even without realizing it). **Max Reflection Bounces** and **Max Refraction Bounces** (more bounces = better detail on small objects, closer to path-traced accuracy, but pricier). Video closes pointing to a free ~4-hour deep-dive session available to the author's community.

### Key Steps
1. **Project Settings baseline** [0:12] — Rendering tab: confirm Dynamic Global Illumination Method = Lumen and Reflection Method = Lumen.
2. **Choose Software Ray Tracing** [0:26] — for low-end hardware / cheapest cost: `Generate Mesh Distance Fields` = ON, `Support Hardware Ray Tracing` = OFF, `Use Hardware Ray Tracing when available` = OFF; also enable Shader Model 6 under Platforms → Windows. Caveats: needs ≥10cm mesh thickness (else light leaking), unsupported for some meshes/materials (e.g. World Position Offset).
3. **Choose Hardware Ray Tracing** [1:29] — for best quality: `Generate Mesh Distance Fields` = OFF (skips falling back to SWRT, saves perf), `Support Hardware Ray Tracing` = ON, `Use Hardware Ray Tracing when available` = ON. Traces actual triangles for more accurate per-pixel detail.
4. **Pick a Ray Lighting Mode** [4:19] — Lumen → Lumen Scene panel: Surface Cache (cheapest default) → Hit Lighting for Reflections (better mirror/shiny reflections, still Surface Cache on 2nd bounce) → full Hit Lighting (best quality: HWRT for both indirect lighting and reflections, highest cost). Visualize the difference live in the Lumen Scene debug view.
5. **Ambient Occlusion source** [2:34] — leave `Allow Static Lighting` OFF so Lumen computes its own AO (buffer visualization will show white/appear "off" — that's expected, it's Lumen-driven). To use Screen Space AO instead: console commands `r.Lumen.ScreenProbeGather.ShortRangeAO 0` and `r.Lumen.DiffuseIndirect.SSAO 1`, then adjust AO power/intensity in the Post Process Volume.
6. **Screen Tracing mode** [4:01] — Post Process Volume → set Screen Tracing to **Scene Color: Anti-Aliased** (instead of default Scene Color) for better translucency handling and reduced flicker from small emissive light sources.
7. **Diffuse Color Boost** [5:45] — Post Process Volume → Lumen (Advanced) → multiplies base/diffuse color to inject extra fake indirect bounce light; keep between 1–2 in most cases (max value 4, visibly overblown at that extreme); useful for under-lit areas without adding more actual lights.
8. **Sky Light Leaking** [6:47] — brightens dark interiors under a Skylight; subtle effect, author recommends targeted use rather than scene-wide.
9. **High Quality Translucency Reflections** [7:06] — enable for meaningfully better reflections on glass/translucent surfaces; without it (Surface Cache mode) reflections on those surfaces look noticeably worse.
10. **Max Roughness to Trace** [7:37] — debug-visualize via Lumen → Lumen Scene → Reflection Rays (non-red = excluded from Lumen reflections); raising this value includes more/rougher surfaces in reflection tracing for a big quality jump at a real performance cost — lower it if targeting performance; watch for meshes with low roughness values (via maps/multipliers) silently costing more here.
11. **Max Reflection / Refraction Bounces** [8:40] — raise for slightly better detail on small objects / more accurate multi-bounce reflections and refractions, closer to path-tracing results, at added cost.

### UE Systems / Blueprints / Settings
- **Project Settings → Rendering** — Dynamic Global Illumination Method / Reflection Method = Lumen; Generate Mesh Distance Fields; Support/Use Hardware Ray Tracing when available.
- **Platforms → Windows** — Shader Model 6 must be enabled to use Software Ray Tracing.
- **Software Ray Tracing** — Mesh Distance Field-based; cheap; ≥10cm mesh thickness required; unsupported for WPO and some materials/mesh types.
- **Hardware Ray Tracing** — triangle-accurate; best quality; higher cost.
- **Lumen → Lumen Scene panel** — Ray Lighting Mode selector: Surface Cache / Hit Lighting for Reflections / Hit Lighting; also hosts the Reflection Rays debug visualization.
- **Console variables** — `r.Lumen.ScreenProbeGather.ShortRangeAO 0` + `r.Lumen.DiffuseIndirect.SSAO 1` to hand AO to Screen Space AO instead of Lumen's own calculation.
- **Post Process Volume → Lumen settings** — Diffuse Color Boost (1–2 typical, 4 max), Sky Light Leaking, Screen Tracing mode (Scene Color: Anti-Aliased recommended), High Quality Translucency Reflections, Max Roughness to Trace, Max Reflection Bounces, Max Refraction Bounces.
- **Buffer Visualization → Ambient Occlusion** — shows white by default under Lumen-driven AO; only reflects real values once SSAO override console vars are set.

### Difficulty
Intermediate (assumes familiarity with Project Settings, Post Process Volumes, and console variables)

### UE Version
UE5 (version not stated in video)

### Tags
`#lumen` `#global-illumination` `#hardware-ray-tracing` `#software-ray-tracing` `#surface-cache` `#hit-lighting` `#ambient-occlusion` `#reflections` `#post-process` `#console-commands` `#project-settings` `#intermediate`

---

## Related Entries
- [[how-i-use-lumen-in-aaa-projects-unreal-engine-5]] — same author's deeper AAA-workflow Lumen guide covering HWRT/SWRT selection by project type and additional Post Process quality knobs — natural follow-up/companion to this settings overview
- [[this-one-setting-will-fix-lumen-noise-in-unreal-engine-5]] — same author, single console-command fix for Lumen GI flicker/noise; pairs well with this video's console-variable AO override tip
