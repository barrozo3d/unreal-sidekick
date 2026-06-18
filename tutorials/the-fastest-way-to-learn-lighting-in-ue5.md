---
title: The Fastest Way to Learn Lighting in UE5
source: YouTube
url: https://www.youtube.com/watch?v=dT4Vl3PGe08
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [lighting, hdri, rendering, cinematics, beginner]
extraction_status: complete
frames_dir: tutorials/frames/the-fastest-way-to-learn-lighting-in-ue5/
frame_count: 9
---

# The Fastest Way to Learn Lighting in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=dT4Vl3PGe08)
**Author:** Josh Toonen
**Duration:** 16m56s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** If you're trying to learn Unreal, I think one of the key misconceptions that people have is that they need to keep building new environments.  But there's way more careers that use Unreal Engine than just environment artists.  There's also creative roles in effects, animation, lighting, and working on set in virtual production.  And even if you're building environments, you need to know how to shape the lighting in your scenes to show off all your hard work.  I bet most people who have struggled lighting in CG haven't even tried to light something in real life.  And you don't need expensive film equipment, you can do it with a lamp and your iPhone flashlight.  And you can learn more about learning lighting this way than setting up lights in CG.  And the reason why is real-time feedback.  Well, the same is true in Unreal Engine because you get real-time feedback,  you can try out new creative ideas in seconds.  So if you want to prove your lighting, the number one most helpful exercise is doing a lighting study.  So what if instead of building environments for every new scene, you took one environment,  and did one, two, five, or even ten different looks, and started matching the li...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_000.jpg

### Lighting Framework [1:27]
**Transcript:** My name is Josh Tunin, and for the last eight years, I worked on Hollywood Visual Effects  as an artist and supervisor.  And last year, I worked on set for the virtual production of Avatar, the last airbender.  And when you're using Unreal on set, you need to go through 20 or 30 lighting setups in a single shoot day.  So you need to be fast when you're trying to adapt the lighting in the CG world  to the practical lights on set.  So I developed a framework for myself that I want to share to easily match the light direction of any shot,  whether it's the onset lights in front of you or a still from your favorite movie.  And that's light direction, light size, color, and intensity.  And I'm going to show you what to look for and how to apply these concepts  in this tank environment that I built for a short film that never saw the light of day.  And we'll walk through how to apply these concepts by matching the lighting of this environment.  So this still from the girl with the Dragon Tattoo.  But first, let's start with the groundwork and talk about the three things you need to build

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_001.jpg

### Exterior Lighting in UE5 [2:18]
**Transcript:** any exterior lighting setup inside of Unreal.  All right, so let's take a look at this tank example project.  This was the first of three that we'll get into.  So let's walk through everything that you need inside your scene to create an exterior daylight setup.  It's actually pretty simple.  You just need three different things.  So let me hide all of the lights in the scene here.  And all we need is our directional light, which is our sun.  We have our skylight, which is going to be our fill and bounce light in the scene.  And then we need some way to create a sky.  So Unreal's default sky system is set up by having a sky atmosphere in your scene  and in your directional light.  Search for atmosphere in your details panel.  And then enable atmosphere sunlight.  Unreal also has a volumetric cloud system.  And then you'll get sun direction on the clouds.  Or you can use an HDRI by getting an HDR texture from the website like Polyhaven.  And then plugging it directly into an unlit material.  So you just have your emissive color input.  And then under your content browser, if you press the all folder and type in inverse,  you'll see that there's this object called sphere inverse norm...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_002.jpg

### Light Direction [5:58]
**Transcript:** So let's take a look at our sunlight and see how we can create interesting shapes in our scene.  So if I just disable all of the other lights except for our directional light,  the main goal of lighting is to create interesting looking shapes inside of our scene.  And it's also to bring out the different planes of the objects in our 3D scene.  Depending on where we place our lights, we can draw out the different planes like the  front or the side of this tank here. But the biggest thing to look for when trying to match  the light direction of another image is you want to look at the perspective of the shadows  and they will literally point to where the light is.  Now this is easier to tell in single-source scenes, but we can see the perspective of the characters  shadow across our scene. And if I trace back their shadows to the top of their heads,  they will literally point to exactly where our light is going to be off screen.  So if you look at the shadows on the ground over here, if you just look at the perspective,  it'll point to where you need to place your lights.  And this can be pretty helpful when the sun is really off screen.  Is look at the shadows and think of where are...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_003.jpg

### Light Size [7:19]
**Transcript:** The next thing we should look at is the size of our light.  And why I say the size of the light is because the larger a light is,  the softer the shadows are going to be.  Think about crisp the shadows of a light bulb are something that's a really small light source  versus a soft box, which is a much bigger, softer area of light.  Now we have to apply this idea to exterior scenes.  So the sun itself relative to us on planet earth is really, really small.  That's why on a sunny day you can look at the ground and see your exact shadow  cut out on the floor.  But on a cloudier stormier day or an overcast day, the sun is casting light into the clouds  and they're diffusing it out across the sky.  That sun now turns into a large soft box filled with clouds.  So let's try to match this still from children of men and switch our sunny sky into an overcast  sky.  I'll just desaturate the color to get us a little bit closer.  And I reset my skylight.  Now when I have my directional light, we start to get these crisp shadows from our tank.  So we can change the size of our sunlight by changing the source angle and the source soft  angle.  And the way you can think about these two knobs is th...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_004.jpg

### Color and Intensity [8:48]
**Transcript:** And that's by matching not just the hue but also the saturation.  And typically you don't want to go very saturated on your directional light because it'll start  to tint all of your materials in an unnatural way.  And then lastly is our atmosphere.  So we go back to our exponential height fog, change that fog in scattering color to get us  a lot closer to our background.  And then in this case, I can change that fog cut off distance to something really high.  So I fog the background buildings and our skydome together.  And from there, start to play around with our fog density.  So that's a quick look at how to apply unreal lighting tools to create exterior daylight scenes.  And believe it or not, this is every lighting scenario when you get down to it.  It's either sunny or it's overcast.  But the only other scenario that we've left out is what if it's night time?

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_005.jpg

### How to Light Night Time Exteriors [9:38]
**Transcript:** Where we don't have a sunlight at all.  So let's take a look at how to emulate night scenes.  And this is not how to make our renders match what night time looks like outside.  But what night time can look like inside of a movie.  And typically the one trick that I've seen over and over again and a lot of these exterior scenes  is by hiding a bright light at the top of our frame.  And typically this light is very large.  It has a big surface area so that it casts a really large reflection on the ground.  This can be seen in this rainy exterior here.  But it doesn't have to be raining to do the same trick.

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_006.jpg

### Lighting Study - Girl with the Dragon Tattoo [10:10]
**Transcript:** You can see that there's no visible light inside of the scene.  It's not a very hazy or foggy scene.  But we have this light that's hidden at the top of frame here.  That's being reflected down on the concrete.  Now it's important here to make sure that our ground material has a roughness below point two.  And you can do this in the material or by adding in wetness decals.  So if we wanted to recreate a lighting scenario like this,  the way I like to organize my project file is by creating different levels for my effects  and lighting.  And that way I can quickly toggle them on and off.  The geometry will stay exactly the same.  But that way I can enable them on and off.  And if I look at this image, I'd say that our key light is definitely this light that's off screen  and reflecting onto our ground.  Now when making a lighting study, you don't have to mimic everything one to one,  but it's worth trying to understand the intention of this original shot.  And they're using this light to silhouette our character and the car here  and make two interesting shapes with our two objects and their shadows underneath.  And we get some volumetrics coming from the top of frame.  So if I want...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_007.jpg

### How to make Tracer Fire [14:25]
**Transcript:** And then the last thing I did that's adding a lot of dynamic energy into the scene  is adding in these tracer fires.  And I'll just quickly show you how I created these because they're actually extremely simple.  All it is is a point light that I've extended the source length of.  So the source length will change a point light into a light tube like an LED light tube,  which is perfect for these tracer fires.  And then attached to these point lights is a cylinder with an emissive texture on it.  And then by animating them together, we can create really simple dynamic tracer fire that reflects  on our tanks and illuminates all of our smoke particles too.  Now if you were just going to do this in Lumen, Lumen doesn't do the same thing as pairing the two  lights and mesh together.  And by adding all of these different elements together, we can create a pretty dynamic scene,  all inspired our single lighting study image.  But if you want to get started and do this yourself, I'll include a download link for the complete  project file of this lightsaber battle. It has characters, environments, and dynamic effects just  like this tank scene. And using the simple framework of light directi...

**Frame:** tutorials\frames\the-fastest-way-to-learn-lighting-in-ue5\frame_008.jpg


---

## Structured Notes

### Core Technique
A 4-factor lighting framework (direction, size, color, intensity) for mastering UE5 lighting: exterior vs interior setups, shadow-traced key light positioning, Source Angle vs Source Soft Angle for shadow crispness, nighttime hidden overhead light, and tracer fire from extended Point Light source length.

### Summary
Josh Toonen presents a systematic framework for learning UE5 lighting built on four variables: direction, size, color, and intensity. Viewers learn how to choose key light direction by tracing from shadows, control shadow softness with Source Angle and Source Soft Angle settings, set up exterior vs HDRI-based interior lighting, use a hidden overhead light trick for convincing nighttime scenes, and replicate the look of tracer fire using a Point Light with extended Source Length. The framework is designed to make lighting intuitive rather than trial-and-error.

### Key Steps
1. **4-factor framework**: Every lighting decision is controlled by (1) Direction, (2) Size, (3) Color, (4) Intensity — adjust one at a time to isolate effects.
2. **Key light direction from shadows**: Study the shadow direction in reference images; trace where shadows point to find where the key light should go (opposite direction).
3. **Exterior setup**: Add a Directional Light + Skylight + Sky Atmosphere (enable "Atmosphere Sun Light" on the Directional Light); adjust Directional Light rotation for time-of-day.
4. **HDRI exterior alternative**: Download HDR from polyhaven.com; create a sphere mesh, flip normals (inverted sphere), apply an Unlit material with the HDRI texture; set the sphere to Movable.
5. **Light size and shadow quality**: Directional Light → Source Angle (sharp / small sun = crisp shadows); Source Soft Angle (overcast / large sky = soft shadows); larger values = softer shadows.
6. **Nighttime hidden overhead light**: Add a Directional Light pointing straight down with low intensity (0.1–0.5 lux); this provides a hint of top-light so characters don't disappear; use only on surfaces with Roughness below 0.2 to keep it invisible.
7. **Tracer fire Point Light**: Add a Point Light; extend Source Length to 200–500 units to convert it from a sphere to a tube shape; this creates the elongated specular highlight of a tracer or muzzle flash effect.

### UE Systems / Blueprints / Settings
- **Directional Light**: Source Angle (shadow crispness — sunny day = 0.5, overcast = 5.0); Source Soft Angle; Atmosphere Sun Light = true (for Sky Atmosphere integration)
- **Sky Atmosphere**: Automatic sky color based on sun angle; requires Directional Light with Atmosphere Sun Light = true
- **Skylight**: Captures environment for ambient fill; Real Time Capture = true in dynamic scenes
- **HDRI sphere**: Static Mesh sphere; negative Scale X = -1 (inverted normals); Unlit material with HDRI texture; rotate to match desired light direction
- **Hidden overhead night light**: Directional Light; Rotation = pointing straight down; Intensity = 0.1–0.5 lux; targets only low-roughness surfaces for specular catch
- **Tracer Point Light**: Point Light; Source Length = 200–500 (converts sphere to tube); IES profile optional

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
lighting, hdri, rendering, cinematics, beginner

---

## Related Entries
- [[the-1-skill-you-need-for-lighting-in-ue5]] — upstage key light positioning and light rig actor
- [[unreal-5-secrets-every-filmmaker-must-know]] — 1–3 light setups and animated shadow rigs
- [[recreate-the-lego-movie-style-in-unreal-engine-5]] — hot dog lighting technique building on these fundamentals
