---
title: Lighting Interiors in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=0GYyHDuaPcg
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.3"
tags: [lighting, interiors, lumen, hardware-ray-tracing, path-tracing, indirect-lighting, rect-light, virtual-shadow-maps, light-bleeding, diffuse-color-boost, william-faucher, intermediate, ue5-3]
extraction_status: complete
frames_dir: tutorials/frames/lighting-interiors-in-unreal-engine-5/
frame_count: 0
---

# Lighting Interiors in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=0GYyHDuaPcg)
**Author:** William Faucher
**Duration:** 17m20s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In today's video we'll be taking a look at interior lighting, combining the uses of  Lumen, hardware ray tracing and path tracing. I'm going to show you how you can think of  lighting in a way that will help you pick and choose the mood you're going for. By simply  lighting a couple of different lighting scenarios, it will really help you break down how to  light any given interior. Now, full disclosure, the video is sponsored by Nvidia Studio and Scan  Computers. Everything from the modeling, layout, lighting, rendering, and editing of this video  had been done with the ASUS ZenBook Pro 16 OLED laptop. I don't get to keep the laptop, it's  being sent back and only being used for reviewing purposes. Just before we jump into today's  tutorial, I'm going to take a brief moment to talk about the hardware we're using today.  The ASUS ZenBook Pro 16 OLED laptop runs on a beefy RTX 4070 that allows you to fully utilize  hardware ray tracing and path tracing and tensor AA cores, which is going to help massively when  you're rendering your shots. It's got the CUDA cores you need, which are needed if you plan on  3D scanning things with an app like Reality Capture. And since the 40 series G...


### Project Settings in Unreal Engine 5 [2:11]
**Transcript:** lighting interiors in Unreal Engine 5. Okay, so since we're getting started,  I just want to make sure that you all have the same project settings that I'm using.  I am currently using Unreal Engine 5.3, so by going to Settings up here, we're going to go to  Project Settings. We're going to scroll down to the Rendering tab down here, and you're going to  want to make sure to support hardware ray tracing and turn it on and pass tracing and turn it on  here as well. I'm using Virtual Set-O-Maps and make sure that you hardware ray tracing when available  is turned on. And it should go without saying, but if you want this to work, you need a GPU that  is capable of ray tracing. The GPU in this laptop is an RTX 4070, so you're not going to have any  issues with it. And one last thing, in a search panel up top, we're going to search for DirectX,  and I believe you need to have DirectX 12 enabled. At least, that's what I'm using, and it works like a charm.


### Reference and Lighting [3:03]
**Transcript:** So here we have a scene that I made it Unreal that is loosely inspired by a scene in Game of Thrones,  and before we get started with the lighting, let's look at the reference and try to break down  where the light is coming from. Notice how there is no artificial lighting. The only thing we're seeing  is light pouring in through that doorway at the top of the stairs. That is the only light source,  and the camera is exposing for the interior, making the exterior completely overexposed, and blown out.  And that is what we're going to try to mimic here. Now this laptop handles this scene like an  absolute champ. I'm blazing past 60 FPS without any issues, and if you want to follow along with  this environment in this tutorial and reverse engineer, how to scene with lit, you can download  this project for free here on Gumroad. Link down below. Just to be clear though, it's not going to  look exactly the same because I'm using a lot of mega-scan textures and models in this level,  and I'm not legally allowed to redistribute those assets, but you will have something to work with,  and the lighting will look the same. So what we're going to do now is we're going to completely kill  all ...


### Pathtracing and Ground Truth [7:43]
**Transcript:** so this is why I like using the path tracers sometimes in order to help me figure out, hey,  am I actually doing things right here? So by going to the lit tab here, we're going to go turn on  path tracing, and what the path tracer is going to do is it's going to give you a more ground  screws physically accurate lighting result based on your current lighting settings. This is what  your scene should look like if everything is set up correctly. There should be no tremendous  difference between the two. They should both be pretty similar. And if they're not, then there's  other issue we need to fix. So you'll see we're missing out on a ton of indirect lighting over here.  If you'll notice it's not perfectly black, it's not there, not black at all there. So we need to go  fix that somehow, right? We need to try and rectify this issue. And how do we inject a little bit more  indirect lighting into our scene? We don't want to go ahead and increase the exposure again.  That will work, but it also brightens up everything else. And we don't want that. All we want is to  lift up those shadows a little bit more. So we're going to go ahead and click on our rectlight here.  And we're going to ...


### Soft Shadows, Hardware Raytracing vs Virtual Shadow Maps [9:21]
**Transcript:** harsh. Right. Again, if I turn on the path tracer, you'll notice that shadows are very, very  soft here, right? It look really, really good. And I don't, I'm not seeing that we're getting  these really hard shadows here. There's something feels off. And the reason for that is because of  virtual shadow maps when it comes to very, very soft shadows, you're just kind of hitting that  limitation there. So in order to fix that, we're going to select our rectlight again. And we're  going to search for ray trace. And we want to make sure we cast ray shadows on and pay attention  to the sheer difference here. No, especially notice on the wall here, this before and this after,  before and after. The shadows are so much softer. So we're getting much, much better  softer shadows here now. When you need to really, really soft shadows, there is no way around using  hardware ray tracing. And that is where RTX GPUs come in really, really handy. Another reason it  incredibly important to add direct lighting, even your ishersine is mostly indirectly lit,  is because of specular highlights. Now pay attention right here on the pillar on the left hand  slide here. I wanted to give it like a, you know...


### Bonus Tip 1 [11:12]
**Transcript:** look wet. Now bonus tips number one, if ever you notice this kind of like light bleeding in your  interiors, this is actually something that's pretty common. You'll notice like along the edges,  you just got this weird light that seems to be, the skylight that's coming through the walls,  you need to go ahead and add some light blockers to the exterior of your level. And what I mean by  this is these large white cubes, right? It's literally just a big white cube that I place underneath my  level to make sure that light is being blocked correctly. Because as we saw earlier, the skylight has  some very low resolution sampling, which makes it very splotchy. And sometimes, at least my understanding  is that you just need more geometry to block that light coming in. So again, if I were to just  lower this cube right here, notice how we're getting a whole bunch of light that's bleeding into  our scene here? Just lifting this big cube up here. Whoa, that light gone. That is how you can fix  light that's leaking into the corners of your wall. It's very frustrating, but fortunately,  with light blockers, it's a very easy fix. Now, let's say you wanted to have some light shaft or  some god r...


### Bonus Tip 2 [13:42]
**Transcript:** trick we have up our sleeve in order to inject a little bit more indirect lighting into our scene.  Again, this brake physicality, but the really cool tip know about. In our post process volume,  we're going to search for a lumen. And here we've got a neat little tip called diffuse color boost.  I already said it to two, but if I said to one, you'll see our shadows are very dark, right? It's  very pitch black. We could always just increase the indirect lighting of our rectalight, but by  increasing the color boost here, it's going to increase the boost of not our light, but of the  albedo values of our materials. So if I said to two, you'll see we've already  injected quite a bit more indirect lighting into our level here. Again, purely in our direction  thing, there's no right or wrong way to do it. It's just important to know which tools are available  to you. So I hope that helps. So now that I've covered this scene here, how do you light an


### Lighting Interiors without natural light [14:40]
**Transcript:** interior that doesn't have any natural light? And that my friend is artificial lighting. So we're  going to hide this here. I have to turn this on here. You'll see here we've got a completely  differently lit scene. I'm not going to go ahead and show you how to place each individual light,  but really it's about breaking down what our lighting is. This is a really quick reference I found  from some old museum somewhere and to notice how there is no natural light here, it's all artificial.  You as a lighting artist need to break down and ask yourself, where is my lighting coming from?  If I turn on my light in my bedroom at night, the light source is your light bulb or your lamp or  whatever. And that's how we need to break it down here. So I went ahead and added some light  fixtures here. We need a physical prop that is there to suggest that hey, there's lighting here.  This is actually what is contributing to the illumination of the scene. Because if I were to  hide these light fixtures here and you just place light, something would feel a little bit odd.  I mean, it feels like something is missing, right? So that's why we need not only add some practical  light props, but really ...



---

## Structured Notes

### Core Technique
Interior lighting workflow combining Lumen + Hardware Ray Tracing — using path tracer as ground-truth reference to validate lighting, fixing light bleeding with geometry blockers, boosting indirect lighting with Lumen Diffuse Color Boost, building believable artificial-light scenes with practical props + light actors.

### Summary
17-minute tutorial on lighting interior scenes in UE5.3. Covers a complete workflow from reference analysis to execution: using path tracer to verify lighting accuracy, ray-traced shadows for soft penumbras (vs VSM limitations), light blocker geometry for sky light bleeding, Lumen Diffuse Color Boost to lift shadows, and the principle of using physical prop light fixtures to ground artificial lighting.

### Key Steps

**Project Settings (UE5.3):**
- Support Hardware Ray Tracing ✓
- Hardware Ray Tracing When Available ✓
- Path Tracing ✓
- Virtual Shadow Maps ✓
- Default RHI = DirectX 12

**Workflow Philosophy:**
1. Analyze reference: identify single vs multiple light sources, natural vs artificial
2. Start with darkness, build up from primary source
3. Use Path Tracer as "ground truth" check — compare to Lumen result
4. If they look very different → fix the lighting, don't fight the renderer

**Natural Interior Light (window/doorway only):**
1. Place Rect Light at window/doorway opening
2. Scale to match opening
3. Set Source Width/Height to fill opening
4. Enable Cast Ray Tracing Shadows → soft shadows through space
5. Use Indirect Lighting Intensity to amplify bounce if needed

**Using Path Tracer as Reference:**
- Viewport → View Mode → Path Tracing
- Compare shadow quality: if PT looks better → VSM limitations; enable "Cast Ray Tracing Shadows" per light
- Compare brightness: if PT is brighter → need more indirect lighting in Lumen

**Fix Soft Shadows with Hardware Ray Tracing:**
1. Select Rect/Point/Spot Light
2. Details → search "ray trace" → **Cast Ray Tracing Shadows** ✓
3. Massively improved shadow softness vs VSM at large source radius

**Fix Light Bleeding / Sky Leaking Through Walls:**
- Add large Static Mesh cube (white, invisible to player) BELOW and around the exterior of building
- Acts as light blocker → prevents sky light sampling artifacts bleeding through thin walls
- Common in tight interiors or buildings without thick enough geometry

**Boost Indirect Lighting (Lumen Diffuse Color Boost):**
- Post Process Volume → search "lumen" → **Diffuse Color Boost** (default 1.0)
- Set to 1.5–3.0 → amplifies albedo contribution to bounce light without changing direct lighting
- Non-physical but artistically controllable

**Artificial Interior Lighting:**
1. Add physical light fixture props (not just invisible lights)
2. Match a light actor to each fixture prop position
3. Point/Spot Light for focused fixtures
4. Rect Light for panel/strip lights
5. Enable Cast Ray Tracing Shadows for soft fixture falloff

### UE Systems / Blueprints / Settings

**PPV Lumen Settings for Interiors:**
```
Lumen > Diffuse Color Boost: 1.0 (default) to 3.0 (lifted shadows)
Lumen > Final Gather Quality: 2-4 (higher = cleaner GI)
```

**Key Tip: Specular Highlights:**
- Even mostly indirectly-lit scenes NEED a direct light component for specular highlights
- Without direct light → surface normals flatten → scene looks wrong
- Principle: add a small direct fill even when primarily indirect

### Difficulty
Intermediate — assumes Lumen basics; covers practical workflow decisions

### UE Version
UE 5.3 (RTX GPU required for hardware ray tracing)

### Tags
lighting, interiors, lumen, hardware-ray-tracing, path-tracing, indirect-lighting, rect-light, virtual-shadow-maps, light-bleeding, diffuse-color-boost, william-faucher, intermediate, ue5-3

---

## Related Entries
- `tutorials/lighting-in-unreal-engine-5-for-beginners.md` — Prerequisite beginner lighting tutorial
- `tutorials/lumen-explained---important-tips-for-ue5.md` — Lumen internals and best practices
- `tutorials/path-tracer-explained---unreals-underrated-tool.md` — Deep-dive on path tracing (WF)
- `references/rendering-pipeline.md` — Lumen + Path Tracing settings
