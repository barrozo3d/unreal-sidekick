---
title: Introduction to Substrate Materials | Unreal Engine 5.7
source: YouTube
url: https://www.youtube.com/watch?v=d1ncs8M6Lkg
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5.7"
tags: [substrate, materials, physically-based-rendering, layered-materials, car-paint, carbon-fiber, advanced, rendering, ue5-7, shading-model]
extraction_status: complete
frames_dir: tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/
frame_count: 4
---

# Introduction to Substrate Materials | Unreal Engine 5.7

**Source:** [YouTube](https://www.youtube.com/watch?v=d1ncs8M6Lkg)
**Author:** Unreal Engine
**Duration:** 8m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay everyone, welcome to a new highlight video. Today we're taking a closer look at substrate, which is enabled by default, starting with Unreal 5.7 and onwards. Substrate introduces a new approach to material rendering and data storage, giving us more flexibility and control over how materials are built and evaluated. With the option to choose between two GBA formats, one focused on state-of-the-art visual fidelity and another optimized for performance. Now let's take a deeper look at what is substrate. Substrate is Unreal's engine next-generation material framework. It lets artists build layered, physically accurate surfaces with far more control than the traditional material system. As we look at the substrate slab node, you can see how the interface is organized into layers of visual behavior. At the top, we have reflectivity driven by F0 and F90. This defines how light responds at glancing and facing angles. Below that is the roughness section, which controls microsurface detail. And further down, we can opt into advanced features like fuzz or glint materials, which introduces tiny sparkling highlights to make that car paint material shine the way it should be. The slab medium controls how light travels through a material layer. Using the MFP node or short for mean free path, defines how far light travels inside a material before it's absorbed or scattered. This enables advanced effects like tinted carbon materials. By tuning Albedo and thickness, we can shape exactly how color and light blends beneath the surface. Let's talk about the substrate operators. With substrates, materials are no longer flat shaders. They are physically layered systems designed to behave like real world materials, with legacy support still available when required. Using the different substrate operators, we can stack these layers to achieve these advanced effects. The vertical coat operator lets you physically layer materials on top of each other. The top slab must be transmissive, allowing light to pass through and interact with the layers below. Using MFP and thickness to control how deep the light travels and how the coated slabs blend together. The horizontal mix operator works like a more advanced lurp node, blending two slabs smoothly across a surface. You can control the foreground coverage at each pixel, creating natural material transitions. The coverage operator acts like a mask, controlling how much of a slab shows through. Think of it as revealing dirt patterns or selective surface detail. Substrate select is one of the newer additions to substrate. It doesn't blend two materials together, it chooses one slab or the other, and only that slab is evaluated. In this example, the selection mask is used to choose between two materials. If the mask value is greater than 0.5, material be selected, otherwise material A is used. This is a specially useful for switching between shading models that can't be blended using traditional methods. The ad operator sums two slabs lighting, however it's not recommended. It breaks energy conservation and quickly leads to unrealistic blown out materials. Use it only for very stylized effects. Let's put this into practice creating a carbon fiber material. All right, I'm in my viewport. Now, before I start creating a material, let's go into edit project settings and I'm going to type in substrate. Now, let's take a look at the different options here and let's focus on the G-Buffer format. Adaptive G-Buffer is substrates modern format, storing only the channels and material needs. It enables the full feature sets and is the default for shadow model six. Plendable G-Buffer is the legacy format optimized for lower end and shadow model five hardware, keeping compatibility with the old material and decal workflows. Now, for creating a material, we're gonna keep adaptive G-Buffer. Let's go ahead and create our first material sets. Now, everything looks relatively similar in terms of shadow graph. Now, for carbon fiber, we're going to be creating two coats, my top coat, which is gonna be the clear coats and then later a base layer. Let's start with the first one. So, I'm gonna put a constant three value of black here and put the F zero to a value of OO15. Then, I'm gonna create a parameter for the roughness so I can create maybe a math effect later. And then, I'll look for mean free paths. I'm gonna connect the MFP to the corresponding SSS MFP, create a constant three color node in which I'll be able to control the transmittance color for that tinted carbon effects. Now, we're gonna add the thickness node a little bit later. Just gonna press C here and comment my clear coat just to clean things up. So, now we created the top layer. Now, let's create the bottom layer, which is gonna be the carbon fiber. So, I'm just gonna copy and paste that substrate slab and let's start creating that bottom layer. Now, for the F zero, I'm gonna use a scientific approach and use OO1725. I'm gonna load up my materials and then I'm just gonna connect these to the associated nodes. So, I'm just gonna multiply this so I can control the roughness of the carbon material, connect that to the roughness. Now, I'm gonna do the same now for the carbon material. Use a flattened normal so I can control the intensity, connect that to the normal. And one last step, optional to control my UV stretching, connect these two to my textures. And now we created that carbon fiber on the layer. Now, all we have to do is connect these two together. So, I'm gonna be using that vertical layer operator. Let's connect the clear coat of the top layer and then the carbon on the bottom. Now, let's control that thickness and use that thickness node and connect that into the top thickness and connect that to the front material. Now, if we apply that material instance on the shadeable, we should be able to control that color transmittance and have some very interesting tinted carbon effects. Another example is car paint. Substrate nails the flake glints and layered reflections with formal realistic control. Here's a simple diagram showing how real car paint works. Light passes through the clear coats into the colored base layer and then hits the metallic flakes beneath. Now, if we put that into practice, this is going to be my top layer, the clear coats, just like carbon fiber and then base coats in the middle. And then under will have the flakes where I'm going to be using that glint density node. Now, I'm going to connect the base and the flakes with a horizontal blend layer and then connect that to the bottom of the vertical layer with the clear coat sitting on top. Now, let's try this material on this beautiful barn find classic car. And with some really nice close ups here, I can play with the values such as the roughness, the metallic and just see how the coating works here. I'm going to go into third layer, which is the flakes and just control those flake colors. I can control the flake density as well as the roughness. Just to showcase the power of substrate and the power of its layering. Now, let's take a look at another added material applied to the car, this time using the coverage weight node. I can really dial in the rust, playing with the different layers here on the car paint, giving me overall more control on my material. Playing with the metallic value and the roughness map, giving it extra contrast. Now, in terms of setup very similar to the metallic paint, I've just connected my texture maps here in the base. And what I've done here is I'm using the horizontal blend so I can blend between the two. And then I've added this coverage weight node on the top, which is essentially going to be my dirt layer, connecting this to the vertical layer, just giving me control on each layer paint of the car. And this is the result we get. I hope you enjoyed this video and see you in the next one.

**Frame:** tutorials\frames\introduction-to-substrate-materials-unreal-engine-57\frame_000.jpg


---

## Structured Notes

### Core Technique
Substrate is UE5.7's new next-generation material framework enabled by default (SM6). Replaces traditional PBR with physically layered slabs. Core node: Substrate Slab (F0/F90, Roughness, Fuzz, Glint, MFP for subsurface/transmission, Thickness). Operators: Vertical Coat (stack layers, top must be transmissive), Horizontal Mix (lerp between slabs), Coverage (mask-based slab), Substrate Select (binary choose), Add (avoid — breaks energy conservation). Demonstrated on carbon fiber (clear coat + tinted transmission + carbon layer) and car paint (clear coat + base + metallic flakes with Glint Density + Coverage Weight for rust/dirt).

### Summary
9-minute official Epic highlight video introducing Substrate materials in UE5.7. Substrate enables physically layered material systems vs the traditional flat PBR shader. Two G-Buffer modes: Adaptive (Shading Model 6, default, full features) and Blendable (SM5, legacy compatibility for decals/older workflows). The Substrate Slab node organizes material properties into: top (F0/F90 reflectivity), roughness, optional Fuzz/Glint, and medium (MFP for transmission depth and tinted SSS). Operators combine slabs: Vertical Coat stacks layers physically (top must be transmissive to let light through), Horizontal Mix blends two slabs with a mask, Coverage is a mask-controlled reveal, Substrate Select binary-chooses one slab, Add sums lighting (not recommended). Practical demos: tinted carbon fiber (clear coat → tinted MFP → carbon fiber layer → Vertical Layer), car paint with flakes (Glint Density node + Horizontal Blend for base+flakes → Vertical Layer with clear coat), and rust/dirt via Coverage Weight node.

### Key Steps
1. **Enable Substrate** — enabled by default in UE5.7; check Project Settings → search "Substrate"
2. **Choose G-Buffer format**:
   - Edit → Project Settings → search "Substrate" → G-Buffer Format
   - **Adaptive G-Buffer**: SM6; full Substrate features; default for new projects
   - **Blendable G-Buffer**: SM5; legacy compatibility; required for old decal workflows
3. **Substrate Slab node** — primary building block; replaces traditional Material output node; organize properties:
   - Top: **F0** (reflectivity at facing angle), **F90** (reflectivity at glancing angle)
   - Middle: **Roughness** (microsurface detail)
   - Optional: **Fuzz** (soft fabric highlights), **Glint** (car paint flake sparkle)
   - Medium: **MFP** (Mean Free Path node — defines how far light travels inside material before absorption/scattering; enables tinted SSS/transmission); **Thickness** (how deep light penetrates)
4. **Vertical Coat operator** — physically stacks two slabs; top slab MUST be transmissive (MFP + Thickness set) to let light through to bottom layer; controls clear coat over base
5. **Horizontal Mix operator** — blends two slabs smoothly across surface; foreground coverage at each pixel; like a lerp between two full material slabs
6. **Coverage operator** — mask-based reveal; controls how much of a slab is visible; used for dirt/rust patterns revealing over base coat
7. **Substrate Select operator** — binary: mask > 0.5 → slab B; else → slab A; no blending; for incompatible shading models
8. **Carbon fiber demo**:
   - Clear coat slab: F0=0.015, Roughness parameter, MFP → SSS MFP, Thickness constant, Color = tint
   - Carbon fiber slab: F0=0.01725, roughness texture × multiply, normal flattened intensity, UV controls
   - Vertical Layer operator: clear coat (top, transmissive) → carbon fiber (bottom)
   - Apply as Material Instance → control tint color + roughness per shot
9. **Car paint with flakes demo**:
   - Clear coat slab (top)
   - Base coat slab (middle)
   - Flake slab with **Glint Density node** → controls sparkle
   - Horizontal Blend: base coat + flakes → combined bottom layer
   - Vertical Layer: clear coat (top) → horizontal blend (bottom)
10. **Rust/dirt layer** — Coverage Weight node → connects on top of Vertical Layer; controls rust reveal via texture mask; adjust metallic + roughness per layer

### UE Systems / Blueprints / Settings
- **Substrate** — UE5.7 next-gen material framework; enabled by default; controlled via Project Settings → "Substrate"; replaces traditional PBR material output with layered slab system
- **Adaptive G-Buffer** — Substrate format; SM6; stores only channels material needs; enables full Substrate feature set; default for UE5.7+ projects
- **Blendable G-Buffer** — Substrate format; SM5; legacy compatibility with old decal workflows and lower-end hardware; same as "SM5" shading model path
- **Substrate Slab node** — primary material building block; properties: F0, F90, Roughness, Fuzz, Glint, MFP input, SSS MFP, Thickness; replaces Diffuse + Specular + Normal inputs of traditional material
- **MFP (Mean Free Path) node** — defines subsurface light travel distance and tint color; drives transmission effects (tinted carbon, skin SSS); inputs: Albedo (SSS color), Thickness
- **Glint Density node** — car paint flake sparkle; connects to Substrate Slab Glint input; control glint density and roughness per slab
- **Vertical Coat operator** — physically stacks slabs; top layer must have MFP+Thickness for light to transmit through; used for clear coat over base
- **Horizontal Mix operator** — lerp between two slabs using coverage mask; creates natural surface transitions (e.g., blend base coat + metallic flakes)
- **Coverage operator** — mask-based slab reveal; used for dirt/rust patterns layered over painted surface
- **Substrate Select operator** — binary slab selector; no interpolation; needed when two shading models can't be blended (e.g., Fabric vs Metal)
- **Add operator** — sums slab lighting; NOT recommended; breaks physical energy conservation; only for stylized effects

### Difficulty
Intermediate-Advanced. Substrate replaces the traditional material output entirely — users migrating from PBR must rethink material structure as layered slabs. The Vertical Coat transmissive requirement and MFP setup are non-obvious for first-time users. Carbon fiber and car paint examples provide good starting templates.

### UE Version
UE5.7 (Substrate enabled by default; experimental in earlier UE5 versions; Adaptive G-Buffer = SM6 only)

### Tags
substrate, materials, physically-based-rendering, layered-materials, car-paint, carbon-fiber, advanced, rendering, ue57, shading-model

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:54] tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/frame_000.jpg
- [2:42] tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/frame_001.jpg
- [4:56] tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/frame_002.jpg
- [7:11] tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/frame_003.jpg

## Related Entries
- `how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin.md` — Polygonflow Dash material editor (traditional PBR approach)
- `i-textured-the-entire-environment-using-a-single-texture.md` — Color Curve node for stylized material coloring (UE5.6)
