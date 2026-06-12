---
title: Unreal Engine 5.5 Release Notes
source: Epic Documentation
url: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-5-release-notes
ingested: 2026-06-12
ue_version: "UE 5.5"
tags: [release-notes, animation, sequencer, control-rig, metahuman, lumen, path-tracer, megalights, physics, ml-deformer, mutable, ue5-5]
extraction_status: complete
page_count: 3
---

# Unreal Engine 5.5 Release Notes

**Source:** [Epic Documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-5-release-notes)
**Pages crawled:** 3
**Ingested:** 2026-06-12

---

## Raw Documentation Content


### Unreal Engine 5.5 Release Notes
**URL:** https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-5-release-notes

Unreal Engine 5.5 Release Notes | Unreal Engine 5.7 Documentation | Epic Developer Community Table of Contents What's New? The release of Unreal Engine 5.5 continues to improve the UE5 toolset. This release delivers improvements in a wide variety of areas, including Animation, Rendering, Virtual Production, Motion Design, and more. This release includes improvements submitted by our community of Unreal Engine developers on GitHub. Thank you to each of these contributors to Unreal Engine 5.5: a-canary, aharvi, Akymbo-Humanoid, AlbinBernhardssonARM, aliemci, alikomurcu, ALiwoto, Almax27, Ambrosiussen, arkadiusz-filip, batlam987, ben-mkiv, BenjaminHill, BenVlodgi, BlenderSleuth, bmwhitley, brorbw, bunnylacey, Caffiendish, chriszuko, colonelsalt, Corey-Downing, David-Vodhanel, dgiannetti-riot, dorgonman, DoubleDeez, DPons97, drandall-microsoft, Duroxxigar, duyaokun, dwdamien, dyanikoglu, dzeligman, Ebrahim-Mottaghi-Rezaei, Edstub207, efokschaner, erebel55, ersenal, ersh1, exxello, foobit, Frigerius, gamethread, GaoYuanBob, Garashka, gnu-enjoyer, GracesGames, grafikrobot, Gusten, hozuki, HSeo, hui211314dd, ilkeraktug, IvayloH, jashking, jdperos, Jernias, jerobarraco, jinsongh2, jorgenpt, jppiiroinen-h13, jpritchard1010, just-bank, KaosSpectrum, kdada, kdbn, KeithMorning, KeithRare, KirillAlekseeenko, klukule, kronok, laycnc, ligazetom, lightbringer, lijenicol, liuhao0620, LizardThief, Losdrew, lxcug, MagForceSeven, MarcusSvensson92, MaximeRobinot, Maxmystere, maxon887, Meidozuki, MinusKube, mr0ptimist, mrobitaille-riot, najmm01, nickdarnell, nicoell-threedy, nikitakrutoy, ohmaya, pasotee, PetterVMC, PFGschen, phantom10111, PhDittmann, PICO-XR, ppchavan001, pramanc, projectgheist, pzychotic, r-vaillant, ramiroagis, rdunnington, reapazor, RiotAlam, rmobbs-ml, sadunkit, sheepandriy, Sigma-Erebus, Skylonxe, sleeptightAnsiC, slonopotamus, Sluggernot, SRombauts, StalkMen, stanley1108, StefanZimecki-Sharkmob, sunwtGitHub, supuo, TechNXGEN, teddemunnik, tgraupmann, Th3Fanbus, TheLumbee, tigerjang, tntnkn, TroutZhang, Tt-Wes, TwentyPast4, uextm, Urkaz, user37337, Vaei, Vesros, vgpechenkin, vorixo, Voulz, Wellwick, whalefood, xeru98, zachlute, zeaf Character and Animation Sequencer Usability Unreal Engine 5.5 brings usability improvements to Sequencer, enabling cinematic artists to control their view of contents within a sequence, gain easier access to properties, and filter viewport by sequence contents. This provides a more controllable interface to reduce workflow fatigue, helping users to create faster. Customizable Filtering Isolate or Hide Selected Bindings, Tracks, or Channels Hotkey Support for Hide, Isolate, and Show All Overlay Window for Properties of Bindings, Tracks, Sections, Channels, and Keys Toggle to Filter Viewport Selection of Sequence Contents Take Recorder now generates thumbnails based on your recorded cameras Dynamic Sequencer Dynamic Sequencer provides users the ability to better define dynamic operations of data to enhance interactive cinematic experiences. Core Functionality: New Default Binding Type - Replaceable that can be dynamically bound at runtime to a different object Creating Custom Binding Types - More control over how an Object is bound in Sequencer Conditionally control a track row's or section's active state Time Warp a Sequence, Subsequence, or Skeletal Animations with an authorable Curve Override and animate the Transform Origin of a Subsequence or Shot Animation Mode: Animation Layers Animation Layers allow users to create motion on non-destructive layers for added control and flexibility. This takes advantage of the Section workflows in Sequencer while adding a simpler, cleaner interface for managing those Sections/Layers with lots of improvements to the usability. Core Functionality: Create Layer from Selected Multi Object Layers Merge Selected Layers Additive and Override Mute, Lock, Select Animatable Weights Rename, Duplicate, Delete Modular Control Rig (Beta) Modular Control Rig moves into Beta, adding many quality of life improvements refining the user interface to help build rigs faster. Module Variants enable Modules to be easily updated. Schematic Overlay UX improvements. Module Hierarchy simplification New Modules: Quadruped Modules Vehicle Modules Native Bipedal module support for common skeleton types (Vicon, Mixamo, mGear, HumanIK, Motive, XSens, Advanced Skeleton). Rig Variants (Experimental) Rig Variants are highly experimental tools for upgrading and swapping Control Rig Modules and Functions, enabling animators to swap rigs non-destructively to a different variant for backwards and forwards compatibility. Upgrade and swap Control Rig Modules and Functions with a new variant. Mutable Customizable Characters and Meshes (Beta) Mutable generates dynamic skeletal meshes, materials and textures at runtime for creating character customization systems and dynamic content. Hidden surface removal to prevent z-fighting and implement object layering and interaction. Ex: jackets over shirts over the base body. Mesh and texture merging to reduce draw calls. Morph baking to reduce GPU load. Baked texture effects such as layering and decal projection to reduce GPU load. Graph-based editor. Skeletal Editor (Production Ready) The Skeletal Editor is now Production Ready with general improvements and visual feedback updates for working with Character Meshes within the Skeletal Editor, enabling quicker and simpler workflows for painting and editing weights on skeletal meshes. Isolation of meshes Robust weight transfer tools Edge Face Selection with Grow/Shrink/Flood support LOD alternate Skin Weight profile editing Improved viewport wireframe and bones display Improved Component Editor Lasso selection Experimental Quad Mesh editing Bones marquee selection multi-editing Animation Deformers You can now craft more realistic animation effects such as contact deformation or better cartoon-style squash-and-stretch, with the new ability to spawn custom deformers inside Control Rig, and easily apply them to characters in Sequencer with a single click. There’s also an Animator Kit plugin containing a collection of ready-made Control Rigs with built-in deformers—including Lattice, Camera Space Lattice, and Sculpt—that you can use during animation or as examples for building your own rig-driven deformers. ML Deformer ML Deformer brings high quality offline mesh deformations into real-time by leveraging Machine Learning. Examples of this are muscle and quasi static cloth simulations. For UE 5.5 the ML Deformer adds some additional features that can improve the runtime deformations. Changes from 5.4 to 5.5 Added support for painting masks, directly in the viewport of the ML Deformer editor. Ability to provide a mask per training animation/geom cache input, limiting the training data to a specific area. Added a pose mixer tool to the Maya plugin for ML Deformer, which can be used to improve training data. Improved workflow issues resolved based on feedback from internal and external teams. Physics Control The Physics Control plugin allows you to add simple, intuitive, and powerful physically based controls to either a blueprint using a component, or to a character using an animation graph node. This helps you gain the benefits of emergent physical motion of static and skeletal meshes, whilst still retaining artistic and gameplay control. Refined Control Profile API that can be applied to either the Physics Control Component or to the Rigid Body With Control animation graph node Improved Control Profile Asset Editor Simplified Creation of Control Profiles Choosers Choosers have arrived and are production ready in 5.5. Choosers provide a robust game context asset selector with a lot of excellent additional features and debugging. While the driver was animation originally, we exposed Choosers to be able to select nearly any type of asset for the release. This can encompass multiple levels of complexity, from simple random selectors to database-driven logic involving 1000s of animations. Audio Driven Animation for MetaHuman Animator Generate high quality facial animation from audio to quickly deliver convincing facial performance in MetaHuman Animator. Use audio assets in MetaHuman Animator to generate facial animation. Quickly delivers animation for all MetaHuman facial controls, including inference of upper face gestures. Works with various voices and languages. A fully local, offline solution, suitable for batch-processing audio. To learn more about audio driven animation, read the Audio Driven Animation for MetaHuman documentation. Optimized MetaHumans in UE With release 5.5 we've taken the optimization approaches used to great success to bring MetaHumans to UEFN and applied the same techniques to UE MetaHumans. Now when exporting MetaHumans, users will be able to request either: Cinematic (Complete) - Existing 'full-fat' MetaHumans with original resolution assets or, High , Medium and Low (Optimized) - Optimized MetaHumans with baked textures and reduced complexity. This enables the average size of a cinematic MetaHuman to be reduced from 800MB to just 60MB, with only minor loss of fidelity when the High (Optimized) option is selected. This feature also introduces the MetaHuman Component, which consolidates the important configuration options for your MetaHuman. This provides a unified interface for users to further configure their MetaHumans by allowing them to turn on/off character animation features at certain LODs, enabling a trade off between performance fidelity. To learn more about optimized MetaHuman, read the Optimized MetaHuman in Unreal Engine documentation. Rendering MegaLights (Experimental) MegaLights is a new Experimental feature that allows artists to add hundreds of dynamic shadow-casting lights to their scenes. Artists can now light scenes playfully without constraints or impact on performance. With MegaLights, lighting artists, for the first time, can use textured area lights with soft shadows, lighting functions, media texture playback, and volumetric shadows on consoles and PC. For more information, see MegaLights Lumen Improvements Release 5.5 includes multiple improvements to Lumen HWRT performance, focusing on being able to ship Lumen at 60hz on consoles. There are also several notable improvements which increase the quality of Lumen global illumination (GI) and reflections. Lumen now supports hit-lighting for GI, a more expensive and accurate way to calculate GI, which avoids some of the limitations when using Lumen with static meshes. Another important improvement is the new reflection denoiser that substantially improves the sharpness of low roughness reflections as well as new support for translucency with refraction in reflections. Hardware Raytracing Release 5.5 has made many improvements to the underpinning systems which all fall into the external-facing hardware raytracing category (HWRT). These lower level systems all impact the performance and capabilities of Lumen, Path tracing, and Light Baking. There are improvements to asynchronous evaluation of raytracing code, improvements to caching and better management of acceleration structures. The intent of these changes is to make it feasible to utilize HWRT at higher refresh rates on platforms for which there is hardware support. For more information, see Hardware Ray Tracing . Path Tracer In Release 5.5 the Path tracer is Production Ready. This means the Path Tracer is fully featured and now it can also act as reference for Atmosphere and Volumetric clouds. It also has a new Spatio-Temporal denoiser for offline Rendering through Movie Render Queue and Movie Render Graph as well Linux support. It is expected that some in development or experimental features will not work with the Path Tracer despite its Production Ready status. For more information, see Path Tracer . Path Tracer Volumetrics In Release 5.5, the Path Tracer now supports reference quality rendering of both the sky ... [truncated]

### audio-driven-animation-for-metahuman
**URL:** https://dev.epicgames.com/documentation/en-us/metahuman/audio-driven-animation-for-metahuman

Table of Contents

### optimized-metahuman-in-unreal-engine
**URL:** https://dev.epicgames.com/documentation/en-us/metahuman/optimized-metahuman-in-unreal-engine

Table of Contents


---

## Structured Notes

### Core Topics
Animation improvements (Sequencer usability, Dynamic Sequencer, Animation Layers, Modular Control Rig Beta, Skeletal Editor production-ready), MetaHuman Optimized pipeline, MegaLights experimental, Path Tracer production-ready, Lumen HWRT improvements, Choosers production-ready, ML Deformer improvements, Mutable Beta, Physics Control refinements, Audio-driven animation for MetaHuman

### Summary
UE 5.5 is a major release focused on animation tooling and rendering quality. Sequencer gains Dynamic bindings, Animation Layers (non-destructive), and customizable filtering. Modular Control Rig enters Beta. MetaHuman gets a major optimization overhaul (Cinematic/High/Medium/Low pipelines; new MetaHuman Component). MegaLights is a new Experimental feature for hundreds of dynamic shadow-casting lights. Path Tracer hits Production Ready with Spatio-Temporal denoiser. Choosers are now Production Ready as a general asset selector.

### Key Features Added in UE 5.5

**Animation:**
- **Dynamic Sequencer**: Runtime dynamic object bindings; replaceable binding type; conditional track state; Time Warp; Transform Origin override
- **Animation Layers**: Non-destructive layers over Sequencer sections; additive + override; multi-object; merge layers
- **Modular Control Rig (Beta)**: Module Variants; Schematic Overlay; Quadruped/Vehicle modules; native Bipedal support (Vicon, Mixamo, mGear, HumanIK, Motive, XSens, Advanced Skeleton)
- **Rig Variants (Experimental)**: Non-destructive Control Rig module/function swapping
- **Skeletal Editor (Production Ready)**: Weight transfer, LOD alt skin weight profiles, edge/face selection with Grow/Shrink/Flood, lasso selection
- **Animation Deformers**: Spawn custom deformers inside Control Rig; Animator Kit plugin (Lattice, Camera Space Lattice, Sculpt deformers)
- **ML Deformer**: Mask painting in viewport; per-animation mask input; Maya plugin pose mixer for training data
- **Choosers (Production Ready)**: Game context asset selector; database-driven animation logic; any asset type selector
- **Physics Control**: Refined Control Profile API; improved editor; simplified creation; works with both component and anim graph node

**MetaHuman:**
- **Optimized MetaHumans**: Cinematic (800MB, unchanged) / High / Medium / Low pipelines (baked textures + reduced complexity); 60MB at High quality vs 800MB Cinematic
- **MetaHuman Component** (introduced 5.5): Toggle animation features per LOD (body correctives, Rig Logic, neck correctives)
- **Audio-Driven Animation for MetaHuman Animator**: Generate facial animation from audio; works with multiple voices/languages; local/offline; batch processing

**Rendering:**
- **MegaLights (Experimental)**: Hundreds of dynamic shadow-casting lights; textured area lights; lighting functions; media texture playback; volumetric shadows on consoles
- **Path Tracer (Production Ready)**: Reference atmosphere + volumetric clouds; Spatio-Temporal denoiser for MRQ/Movie Render Graph; Linux support
- **Lumen**: HWRT performance improvements for 60hz on consoles; hit-lighting for GI; new reflection denoiser; translucency with refraction in reflections
- **Hardware Raytracing**: Async evaluation improvements; better acceleration structure management; enables higher HWRT refresh rates

**Characters:**
- **Mutable (Beta)**: Runtime dynamic skeletal mesh/material/texture generation; hidden surface removal; mesh/texture merging; morph baking; graph-based editor

### UE Version
UE 5.5 (2024)

### Tags
release-notes, animation, sequencer, control-rig, metahuman, lumen, path-tracer, megalights, physics, ml-deformer, mutable, ue5-5

---

## Related Entries
- `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Sequencer, Control Rig, Animation Layers details
- `tutorials/metahumans-in-unreal-engine.md` — MetaHuman Component, Optimized pipeline in depth
- `tutorials/designing-visuals-rendering-and-graphics-with-unreal-engine.md` — Lumen, Path Tracer, MegaLights details
- `references/version-tracker.md` — All UE version comparison
