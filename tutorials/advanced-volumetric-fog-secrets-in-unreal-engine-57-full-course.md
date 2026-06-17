---
title: Advanced Volumetric FOG SECRETS in Unreal Engine 5.7 [Full Course]
source: YouTube
url: https://www.youtube.com/watch?v=xbZNHZ-QGyg
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "5.7"
tags: ["volumetric fog", "VDB", "sparse volume textures", "heterogeneous volumes", "exponential height fog", "local fog volume", "fog cards", "media texture", "Lumen", "ray tracing", "CVARs", "sequencer", "filmmaking", "cinematics"]
extraction_status: complete
frames_dir: tutorials/frames/advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course/
frame_count: 18
---

# Advanced Volumetric FOG SECRETS in Unreal Engine 5.7 [Full Course]

**Source:** [YouTube](https://www.youtube.com/watch?v=xbZNHZ-QGyg)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 31m54s | 18 section(s)

---

## Raw Data (for Claude Code extraction)


### What Makes a Movie Cinematic? [0:00]
**Transcript:** What makes a movie really cinematic, especially in the 80s when everyone could spoke?  It's volumetric fogs, smokes, all those sort of things.

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_000.jpg

### Top 5 Volumetric Fog Methods Overview [0:09]
**Transcript:** And I'm going to show you my top five ways of adding cinematic volumetric fog into Unreal  Engine, starting with number one, exponential height fog, followed by number two, local area  fogs. And then number three, fog materials. And then number four, my favorite, sparse volume  textures, aka VDBs. And number five, the old classic fog cards, using video material in  my case, so we can get some animated cool stuff for close-ups.  Let's begin.

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_001.jpg

### Why Volumetrics: Upgrading a Project to Final Quality [0:46]
**Transcript:** The reason for this video is I'm taking my animatic opening scene, which is an orbiting space  station above a derelict earth post-pocalyptic smoke flying into the atmosphere. This spaceship  belches out dust and stuff. And I'm going to level it up to proper final quality. I started  in Unreal 5.1 or 2. And since then, we've had a lot more improvements in the volumetrics  so we can now do sparse volume textures. And we can also do ray tracing as well with volumetrics.  So I'm going to show you how I've improved it and then give you a little quick mini how-tos  so then you can apply it to your own work. Hooray! Alright, so number one, we're going to start

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_002.jpg

### Method 1: Exponential Height Fog Setup [1:23]
**Transcript:** with the exponential height vault. And I'm going to dissolve into that corner over there.  So here we are in Unreal Engine 5.72. And this is the viewport and I'm moving around my  camera in real time. And which is just amazing because we're seeing these beautiful volumet  trick light shafts. And we've got our VDB sparse volume textures. And I'm just moving it  around. The performance of VDBs and SVTs and heterogeneous volumes is a little slow for real-time  applications like games and immersive things. So you have to be kind of a bit more careful.  But I'm doing filmmaking. So all of my stuff is a bit more heavy than game style. So that's  one thing to be aware of. And here we have our scene. And if I turn off my exponential height  fog, you can see that it's pretty basic. So I've got the original geometry from my animatics,  just a bunch of cubes, all formed together in this giant, massive space station. And then I've  got a few sparse volume textures. So you can see why I love volumetrics. They're beautiful,  they give you the illusion of a lot more detail in your scene. And if you look at some of the work  by the masters like Roger Deakins on Blader on a 2049 and he uses Silhoue...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_003.jpg

### Adding the Directional Light [4:04]
**Transcript:** And so now we've got a directional light and some big cubes.  And then we're going to add an exponential height fog. And then the important thing is to type volume

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_004.jpg

### Adding Exponential Height Fog [4:14]
**Transcript:** in your search bar and turn on the volumetric fog. So there's the volumetric fog. And we're not

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_005.jpg

### Enabling Volumetric Fog & Adjusting View Distance [4:26]
**Transcript:** seeing any of the rays yet because of the view distance. So this view distance is the kind of  critical thing that you have to kind of just keep messing around with it. Defaults to 6,000,  which is fine if you're in a small scene, but in these larger scenes, let's make this 100,000.  Okay. And then let's see if we're seeing anything. I'm going to also go into my height fog and  change the falloff density because I don't want it to kind of come down. It's coming down really  refig. So I'm going to change that and make it as low as I can get it. And I think you can start  seeing a little bit of the falloff there. So let's come in and change the fog density, bring that  down. Oh, here we go. So we're getting a sense of that now. That's great. Okay. And then as you  it is a bit of a balancing act, the density of this, the fog density, and then the view  distance. So a combination of those things because as you see, I'm pulling out here and that's  disappearing a bit. So let's make that 200,000 like that. But if I make it too much, let's say five,  then it's kind of going beyond the screen. It's going out there. But you know, you have to dial it  and then keep going. They have to turn y...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_006.jpg

### Advanced: Enabling Ray Traced Shadows with Volumetric Fog [6:14]
**Transcript:** unratraced volumes on the light. So I'm going to go into my light and then search for cast,  or cast volumetrix. Where is it? Cast raytraced shadows and I'm going to change this to enabled.  So now it's casting raytraced shadows, but you can see here they've disappeared because by default,  the fog doesn't work with raytracing. So you have to type in this CVAR, which I'll  angle on the screen there, but here's one I did earlier. It's our volumetrix fog inject raytraced lights,  not zero. Oh no, we want it one. One and so now we've come on the raytraced lights with the fog.  Hazar. For to keep this in, I'm going to go over this a bit later, but the, unless you add this to  your any file or you add it to your movie render queue, you can have to type this in each time you  want to see it in the viewport. What I do, since I'm using a sequencer, is I'll add it to the  sequencer and I'll show you how to do a CVAR track in a bit. Quick gotcha. With large scenes,  as you move further away from an object, the raytracing by default will turn off at a certain  distance. That's called raytraced culling. So if you're not seeing your raytraced shadows  or any shadows on the objects, then you've ...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_007.jpg

### Troubleshooting: Fixing Lumen Global Illumination in Large Scenes [7:51]
**Transcript:** I've weirdness with big scenes. You can see here, as I'm moving away from these objects,  the global illumination is turning off. And that is because the lumensine view distance,  the default is 20,000 centimeters. But you can whack that up to, I think a maximum is 80. So it'll  keep it on for a larger distance. But it will still turn off at that point. There's a limitation on  that. But you can change the type of global illumination. The surface cache, I think, is the default  one. But if you change it to hit lighting, then you zoom out. That'll keep it on. It is more  expensive, GPU-wise. So not for the immersive people. However, I don't care. I'm going large.

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_008.jpg

### Cinematic Cheats: Light Shaft Occlusion and Bloom [8:40]
**Transcript:** All right, back to your programming. So things you can also do to plus this out. And then  I'm going to add a bit more volumetrics to the light. And this is a cheat. This is using  light shafts and light shaft bloom. So if you hit light shaft occlusion, so you select your  directional light, look for light shaft occlusion, turn that on. And it increases that a bit more.  So you turn that down a bit. So this will just add a bit more shadowing to those lights.  So if you're seeing it, then let's see if we can see it in here. Yeah, you can see like that.  So it gives you a bit more. But this is kind of faking it. But that's fine. Everything's faking it.  And then we've also got the light shaft bloom. If you turn that one on, it adds a kind of glow  towards the wherever the center of your sun is. So it kind of adds it towards your sun, basically.  In my case from earlier, I basically put a little sphere where the sun is and a card around the  outside with some god rays on it to make it look a bit more interesting. So now we're going to add

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_009.jpg

### Method 2: Creating Local Fog Volumes [9:48]
**Transcript:** a local fog. So for local fogs, you go into here to the plus button and then you say local  fog volume. There we are. Now this thing here, well, there it is. Let's go and push it. I'm  pushing it. I had a very small one here. So let's go and make him a bit bigger.  And let's make him a let's try 50. There we are. Okay, so this now is basically a sphere with a  falloff on it. And I'm going to change the radial fog density. And this way it will be  stronger in the middle and it will fall off. And then I'm also going to change the height  falloffs because I don't want any height falloffs. So now I've got a bloom, a little bloomy  volume there like that. So I can now give that some color. Let's go and make this  there, that color there. And then I can put that wherever I want. So this is where nice way of  kind of adding kind of denser areas to your scene and doing some nice effects, giving it a

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_010.jpg

### Customizing Local Fog Volumes (Density and Color) [11:00]
**Transcript:** different look. I press, press escape and you can have multiple ones of these. So let's go and  duplicate him and then change the color on that one. Let's say this bit over here. We've got some  blue. Put that over there. And then we can again change the distribution to the way the light  scattering distribution will put more light towards the light and less light away from it.  Kind of makes it look cool. Let's do that on that one too.  Then we get 200.  Yeah well, pretty nuts.  Yeah.  Let's make him much less.  Give it the subtle brush. Turn the other one down too.  So that we've got some cool atmospheric effects with our exponential height fog.  And then we can add a local fog material. So basically you can take any object and give it a

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_011.jpg

### Method 3: Using a Volume Material on Geometry [12:23]
**Transcript:** material and make that a fog material, which I'll show you now. So I'm going to make a duplicate one  of these objects. Here we are putting them over here and then we're going to add a fog material  to this object. I don't tend to use them but I wanted to do a top five and so I had to come up with  one more. Right mouse button go to material and create a material. MMMFonga. Then double click on  that one. And then this select your material output. It needs to be additive and then you change  material domain to volume. And then we add a number three, press three, press mouse button.  And I'm going to add a color here. I'm just going to make him red.  And then under extinction, I'm going to press one to make a single vector parameter.  And then we change that to .01. And then if I hit apply,  and then I'm just going to lower this and then I'm going to drag that foggy material onto this cube.  And there we have a shape with a foggness to it. I'm going to make this as much small as it  seems to like to be a very small number. So there's 0, 0, 0, 5. There we are, then hit apply.  There we are. So you've got some of that shape there. And then I'm going to kill that.  So that is a basic f...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_012.jpg

### Method 4: Sparse Volume Textures (VDBs) Explained [14:52]
**Transcript:** textures are effectively this except the use a VDB to give you this. And then they're very small.  So the smaller these cubes, then the higher resolution detail that you can add. But it will slow down  your performance. So that's your choices. So what a great way by accident to demonstrate what  a VDB is. So I'm now going to go and find one. If I was really smart, I'd be making my own using  Niagara and their fluid Niagara systems to make sparse volume textures, HGNs volumes. But I'm not.  At some point, maybe I'll be brave and try it out. But for now, I'm just going to use  ones that I buy from Fab and then bring that in here. So I went to Jenga FX and grabbed one of  their free VDBs and I just grabbed a single one. So I'm going to go Rhyme House button, import  current folder and grab that single one. You can also use a sequence so you can do animated  explosions or sort of cool stuff. But in this case, I'm just doing a solid mist and I'm going to  hit OK and open that. And because I'm just using the density, I'm going to say import. There's no  fire involved in this one. So just hit import. There we are. So now for the sparse volume texture,

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_013.jpg

### Setting up the VDB Material and Heterogeneous Volume [16:21]
**Transcript:** the VDB, it basically needs to be fed into the sparse volume material, made an instance of that  and then applied onto a HGNs volume. All right. Now there is a default sparse volume material  in the engine. So I'm going to grab a copy of that one. So if you don't see engine content here  and into your content browser, go to the little cog over here and then click engine content and  then that will list all of the things available in the engine to mess with. But if you're not  familiar with there, then it's probably a good idea to not mess with stuff in there. Because if you  mess up the engine, you'll mess up every single project that you've got and then you'd have to  reinstall the engine, which is annoying and not sort of the thing that I have done several times.  Under engine, go to engine content and then down to engine materials. And then in engine materials  at the end, there's one called a sparse, a sparse volume material. And we're going to copy that to  our local area. So going to go up to here. That's where I'm going to put it. I'm just going to drag  it into there. But it'll say, do you want to copy it? And you say, yes, please. So don't move it  there. You copy it here....

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_014.jpg

### Troubleshooting: Increasing Max Trace Distance for VDBs [19:58]
**Transcript:** distance of heterogeneous volumes. Again, to increase performance for games and immersive things.  But we don't want that in this case because we've got a massive world. So there is another  CVAR specifically for this. And it is called our heterogeneous volumes dot max trace distance.  And this will as you increase the amount, I'm not sure what the default is, but there is an  infinite amount. So the maximum is one with lots and lots of zeros over. Just whack it up to as much  as you can make it. And then it'll work in your large volume area. I'm having problems right now  with mine because I've got a planet sized environment. And at several hundred miles, it disappears.  And so if anybody knows, then please let me know in the comments because that would be great  because it's really annoying. But the fact that we've got these is such an amazing thing. So I'm  going to scale this up to 300. I'm going to put it over here into my environment. There we are  like that. And then I'm going to make him a little bit more transparent. And then you can expose  these parameters in the sequencer if you want to animate them, which I do. So but I'm just going to  make this point to make it a bit...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_015.jpg

### Method 5: Fog Cards (Animated Media Texture) [22:19]
**Transcript:** And then for close up type things, I will use a fog card. So I'm going to show you how I do that now.  So a fog card is very simple. It's just a plane with a media texture on it with some fog on it.  And uses transparency. And I'm just going to add one of those into the environment. So right mouse  button. And then we're going to go to media. And then image media source or file media source.  In this case, it's a movie file. I tend to normally use image media sources like an EXR sequence.  But in this case, that's what I've got. So we go to file media source. Let's call it file media source  mist. Double click on that. And then we're going to point to the location. So I'm going to point to  the image and then click on that and then to play it in here, we should see open. Then you'll see  your media playing. And then we say it's safe on that one. So now we're going to make a media player.  So we go to write mouse button media media player. And this will also make a media texture.  So you want both of those. It's very complicated. But it is. It's just this. Okay, press OK.  And then MP for media player. Call it mist. And then media texture. It's called it mist. So  now I'm going to m...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_016.jpg

### Quick Tip: Using Console Variable Tracks in Sequencer [27:04]
**Transcript:** to show you how to do CVALs. Because every time you want to use a CVAL, you have to type it in.  But I, what I do is I add them in my sequencer here. So you go to add and then console variable  track. Add in there. And then right mouse button on that properties. And then under here, this  bit here, where it says add CVAL value, you can basically type in all your different settings here.  So I'm going to say ray tracing calling. I'm going to copy that one right mouse button properties.  Add CVAL and hit paste. And then put a comma after it. And then you put another one in.  Our ray trace polymetric fog inject ray trace lights. Put that in there. Copy.  Properties. See it's there. And you put go to the end, put a comma and then paste that one.  That one, etc, etc. So you can add all of your CVALs there. And if you want to turn them on and off,  you can just disable that track. So you can just turn it on and off like that as well if you want to  change your speed and add some more. So I've got a list on the screen right now of all of the CVALs  that I'm using in my sequence. And since now we can see the fog card in the environment,  I want to add a couple more things to the material. ...

**Frame:** tutorials\frames\advanced-volumetric-fog-secrets-in-unreal-engine-57-full-course\frame_017.jpg


---

## Structured Notes

### Core Technique
A full-course walkthrough of five methods for adding cinematic volumetric fog in Unreal Engine 5.7: Exponential Height Fog, Local Fog Volumes, Volume Materials, Sparse Volume Textures (VDBs/Heterogeneous Volumes), and animated Fog Cards using Media Textures.

### Summary
Dean Yurke covers his complete toolbox for volumetric fog in UE 5.7, motivated by upgrading his sci-fi animatic from a basic block-out to final quality. He walks through each method in sequence — from the global Exponential Height Fog with ray-traced shadow CVARs and Lumen GI tuning, to Local Fog Volumes for area-based color and density control, to applying a Volume Domain material on geometry, to the star technique of Sparse Volume Textures (VDB files imported as Heterogeneous Volumes with the default sparse volume material), and finally to animated Fog Cards using a File Media Source and Media Player. The tutorial also covers Sequencer Console Variable tracks for persisting CVARs across sessions and per-shot render control.

### Key Steps
1. Add a Directional Light, then add an Exponential Height Fog actor and enable Volumetric Fog in its settings.
2. Adjust View Distance (raise to 100k–200k for large scenes) and Fog Density / Height Falloff to taste.
3. For ray-traced light shafts: enable Cast Raytraced Shadows on the Directional Light and set CVAR `r.VolumetricFog.InjectRaytracedLights 1`; fix culling with the raytrace culling CVAR.
4. Fix Lumen GI disappearing in large scenes: raise Lumen Scene View Distance to 80k or switch GI to Hit Lighting mode.
5. Add Light Shaft Occlusion and Light Shaft Bloom on the Directional Light for cheap God Rays faking.
6. For Local Fog Volumes: Place > Local Fog Volume, scale the sphere, tweak Radial Fog Density and height falloffs, colorize, and duplicate for multi-zone atmosphere.
7. For Fog Materials: create a material, set Blend Mode to Additive and Material Domain to Volume; set Extinction to ~0.005 and apply to any geometry.
8. For VDBs: import a VDB file as a Sparse Volume Texture (density only), copy the engine's default SparseVolumeMaterial into the project, make a material instance, assign to a Heterogeneous Volume actor; raise `r.HeterogeneousVolumes.MaxTraceDistance` for large scenes.
9. For Fog Cards: create a File Media Source pointing to a mist video/EXR, create a Media Player + Media Texture, build a material using the Media Texture with additive blending and transparency, apply to a plane in the scene, drive playback via a Media Track in Sequencer.
10. Persist CVARs using Sequencer: Add > Console Variable Track, right-click > Properties, add each CVAR string into the list; disable the track to toggle CVARs off without deleting them.

### UE Systems / Blueprints / Settings
- Exponential Height Fog actor (Volumetric Fog checkbox, View Distance, Fog Density, Height Falloff)
- Local Fog Volume actor (Radial Fog Density, Height Falloff, Scattering Distribution, Color)
- Volume Domain Material (Blend Mode: Additive, Material Domain: Volume, Extinction parameter)
- Sparse Volume Textures / Heterogeneous Volumes (VDB import, SparseVolumeMaterial engine copy)
- Directional Light: Cast Raytraced Shadows, Light Shaft Occlusion, Light Shaft Bloom
- Lumen GI: Scene View Distance, Global Illumination mode (Surface Cache vs Hit Lighting)
- CVARs: `r.VolumetricFog.InjectRaytracedLights`, `r.RayTracing.Culling.*`, `r.HeterogeneousVolumes.MaxTraceDistance`
- Sequencer Console Variable Track
- Media Source / Media Player / Media Texture pipeline for animated Fog Cards

### Difficulty
Intermediate

### UE Version
5.7.2

### Tags
volumetric fog, VDB, sparse volume textures, heterogeneous volumes, exponential height fog, local fog volume, fog cards, media texture, Lumen, ray tracing, CVARs, sequencer, filmmaking, cinematics

---

## Related Entries
- `easiest-vfx-pipeline-ever-with-composite-mesh-actors-in-unreal-engine-57-composu.md` — also uses Media Textures and Sequencer in a filmmaking pipeline
- `create-spectacular-depth-of-field-in-unreal-engine-58-with-the-new-accumulation-.md` — cinematic rendering techniques; Movie Render Graph setup
- `how-to-use-the-movie-render-graph-in-unreal-engine-58---simple-setup-for-filmmak.md` — rendering the final frames of volumetric-heavy shots
