---
title: How I Use Lumen in AAA Projects | Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=yspmZJ6YjpM
author: Karim Yasser
ingested: 2026-06-23
ue_version: "UE5"
tags: [lumen, lighting, rendering, ray-tracing, distance-fields, performance, environment, technical-settings]
extraction_status: complete
frames_dir: tutorials/frames/how-i-use-lumen-in-aaa-projects-unreal-engine-5/
frame_count: 4
---

# How I Use Lumen in AAA Projects | Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=yspmZJ6YjpM)
**Author:** Karim Yasser
**Duration:** 7m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** April 5, 2022. This is when Lumen was firstly introduced in Android Engine 5. And since then, a lot of videos took about the requirements to have Lumen works well. And mostly they mentioned the light values, the base color values for materials, and the indirect light intensity. But if you think that these three options are the only options that control Lumen, they are completely wrong. And that's because Lumen has different types, different approaches, and that depends on the project type, the target hardware, and the specs and quality you want to get. So in this video, I will show you how I use Lumen in the Tribal A projects I work on. First of all, we need to go in project settings, then rendering, and we can scroll down here and we can see support hardware ray tracing. This is related to the project overall to support hardware ray tracing work not. So it's not only related to Lumen, but if you want to use hardware ray tracing for Lumen, you can use it. And we have mainly two things. Like as you can see here, the hardware ray tracing, and the other one, which is the cheaper option and works on why the range of hardware specs, which is the software ray tracing. So in order to use software ray tracing, we can turn off the support hardware ray tracing, or we can keep it for other purposes, and just keep this one disabled. So this is the use hardware ray tracing when available. This triggers Lumen to use ray tracing support when the specs or the hardware can do it. Otherwise, you will fall back to software ray tracing. So what actually the types of software ray tracing are, we have two things. They are here in software ray tracing category. You have first to use the generateMeshDistanceFields that could be added for each static mesh you import into your project, and then you can control that mode for it from software ray tracing port. We have detailed tracing and global tracing. Simply detailed tracing uses the MeshDistanceFields, which is more accurate and works with each mesh individually. And the global tracing uses the global distance field, which is less end resolution, and it's not as accurate as the detailed tracing. So what we can see here, we can go to showflag options, visualize meshDistanceFields, and we can see here this is really low resolution. We try to select and open this static mesh editor. Let's go to build options. And as you can see, this asset has really thin geometry in here. Notice what will happen if we try to go here and increase the distance field resolution scale. Let's try to name it for example, and that will increase the memory for sure and maybe increase the disk size, but this is super accurate now. It respects this thin geometry and reads the details in much, much better way. So if you have really thin geometry like wall sealing, so you can fix it with this option, or you can rescale it and increase the thickness of the static mesh itself. But if you cannot do that, you can do that here in the static mesh editor. So that's for the meshDistanceFields. The other way to use software ray tracing is to use the globalDistanceField. As you can see, this is really low resolution. So it's not representing the exact same details that we want. So this saves more memory and it makes the projects run faster, but it lacks the details, especially within really small distances or really focused areas, but it works really well with really large world scale environments. So you can switch between them based on your project preferences, and personally, I prefer to use the meshDistanceFields if I'm going to use software ray tracing. And we have also the other way, which is using hardware ray tracing. So here we can use hardware ray tracing when available, and that will enable and give us the option to use it with the recommended or the required hardware specs. And that default here is to use SurfaceCache. So SurfaceCache is that she is the way to use Lumen for hardware ray tracing, and we still have other ways which are higher in resolution. And also it gives better details, but that will take or consume more from the performance. So we have headlighting for reflections. This is more accurate for reflection surfaces. So here if we try to go in there, as we can see the reflections on the water surface, we can scroll here for post process volume. And I believe I was using that lighting. So if I try to switch to SurfaceCache, as you can see the reflections are not really good, you still see some black reflections here. They are not too accurate. And especially if you are using really high quality reflections, this will not work for you. So you might need to use headlighting for reflections or headlighting. But they have some differences because headlighting is way more expensive than headlighting for reflections because it projects more rays into the indirect lighting paths. So it gives you much more accurate results, but it's not reliable for games. So what I personally use is to work with SurfaceCache and sometimes I don't even want to use hardware ray tracing. But I have to ensure that I keep my meshes working perfectly. I have the proper distance field for the meshes and they have the proper thickness and they have proper materials and everything like that. And also there are other things that depend or have some work to do with Lumen. And if you want to recreate this scene, I have a step-by-step, a full breakdown that I'm going to do for this scene specifically. So we can get this kind of result here, as we can see for a golden hour, how you can set up the lighting, the values that we have in here. And the sky values, the proper exposure, and everything that works fine for the environment. So you can get this kind of balance in here. I will have it live in a workshop that is going to be happening really soon. So if you want to get your hands on this scene and start to know how to use Lumen in more details and understand the differences in more practices and how I can actually use it and unlock all these features and settings that I use in my projects and realize this scene. You can register in the workshop link. I will add in the description below. It's going to be completely for free. And you can get all the details and behind the scenes for this environment lighting step-by-step from setting up the sky, setting up the directional lights, setting up the exposure and balance to recreate this beautiful golden hour lighting. Also to understand more about Lumen from practical approach in the industry and connect with others while they are asking more questions about Lumen and the lighting in there. So make sure to register, to attend, and get your seat to join us in this free workshop to start reliving your projects in a proper way as I do in trivially projects. Thank you so much for watching and see you there in the workshop.

**Frame:** tutorials\frames\how-i-use-lumen-in-aaa-projects-unreal-engine-5\frame_000.jpg


---

## Structured Notes

### Core Technique
Lumen mode selection for AAA projects: Software Ray Tracing (SRT) with Mesh Distance Fields (detailed, per-mesh, accurate for close geometry) vs Global Distance Field (low-res, large worlds) vs Hardware Ray Tracing (HRT) with SurfaceCache (default) / Hit Lighting for Reflections (more accurate, expensive) / Hit Lighting (most accurate, not for games). Fix thin-geometry Distance Field errors by increasing Distance Field Resolution Scale in Static Mesh Editor.

### Summary
Karim Yasser (AAA environment artist) explains Lumen's configuration options beyond the basics. Project Settings → Rendering: "Support Hardware Ray Tracing" enables HRT availability; "Use Hardware Ray Tracing When Available" makes Lumen choose HRT on capable hardware, falling back to SRT. SRT modes: Detailed Tracing uses per-mesh Mesh Distance Fields (accurate, respects thin geometry) vs Global Distance Field (low-res, suited for large open worlds). For thin geometry (walls, ceilings) with bad SRT results: open Static Mesh Editor → Build Options → increase Distance Field Resolution Scale. HRT modes: SurfaceCache (default, balanced performance + quality; some reflection inaccuracy), Hit Lighting for Reflections (accurate reflections, moderately expensive), Hit Lighting (most accurate, full indirect lighting rays, too expensive for games). Karim's preference: SurfaceCache with well-configured meshes (proper distance fields, correct thickness, proper materials) as primary approach; skip HRT entirely on projects requiring broad hardware support.

### Key Steps

**Choose Lumen mode (Project Settings → Rendering):**
1. "Support Hardware Ray Tracing": Enable only if you want HRT available (required for HRT features)
2. "Use Hardware Ray Tracing When Available": Enable to let Lumen auto-pick HRT on capable hardware; disable to force SRT

**Configure Software Ray Tracing:**
- Detailed Tracing (default): uses per-mesh Mesh Distance Fields → accurate, respects individual mesh shapes
- Global Distance Field: low-res fallback; good for large open-world scale; less detail in close range
- Visualize: Show Flags → Visualize → Mesh Distance Fields

**Fix thin-geometry SRT artifacts:**
1. Open Static Mesh Editor for problematic mesh
2. Build Options → Distance Field Resolution Scale → increase (e.g. 1 → 4)
3. Re-build; note: increases memory + disk size

**Hardware Ray Tracing mode selection (Post Process Volume):**
- SurfaceCache: default; balanced performance + quality; some reflection inaccuracy on mirror surfaces
- Hit Lighting for Reflections: accurate reflections; moderately more expensive than SurfaceCache
- Hit Lighting: maximum accuracy for full indirect lighting; not suitable for real-time games

### UE Systems / Blueprints / Settings
- **Support Hardware Ray Tracing** (Project Settings → Rendering): enables GPU HRT support for entire project; required for HRT Lumen modes
- **Use Hardware Ray Tracing When Available** (Project Settings → Rendering / Lumen): toggles Lumen between HRT and SRT dynamically based on hardware
- **Software Ray Tracing modes**: Detailed Tracing (Mesh Distance Fields per mesh) vs Global Tracing (low-res global distance field); set via Lumen scene settings
- **Distance Field Resolution Scale** (Static Mesh Editor → Build Options): multiplier for per-mesh distance field voxel resolution; fix thin-wall SRT errors; increases memory cost
- **Lumen Reflection Method** (Post Process Volume): SurfaceCache / Hit Lighting for Reflections / Hit Lighting; trade accuracy vs performance
- **Mesh Distance Fields**: per-static-mesh implicit signed-distance representation; basis for Detailed SRT; requires "Generate Mesh Distance Fields" project setting enabled

### Difficulty
Intermediate (understanding modes) / Advanced (per-project optimization decisions)

### UE Version
UE5

### Tags
[lumen, lighting, rendering, ray-tracing, distance-fields, performance, environment, technical-settings]

---

## Related Entries
- how-to-create-cinematic-environments-in-unreal-engine-5.md (Lumen setup in cinematic context)
- how-i-made-this-shot-in-unreal-engine-5.md (Path Tracer vs Lumen trade-off — hero shot used Path Tracer because Nanite incompatible)
