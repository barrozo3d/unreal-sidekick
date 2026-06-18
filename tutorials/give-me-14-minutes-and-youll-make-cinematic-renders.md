---
title: Give me 14 minutes and you'll make cinematic renders
source: YouTube
url: https://www.youtube.com/watch?v=BG_zYneV3mo
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, lighting, materials, animation, niagara, beginner]
extraction_status: complete
frames_dir: tutorials/frames/give-me-14-minutes-and-youll-make-cinematic-renders/
frame_count: 5
---

# Give me 14 minutes and you'll make cinematic renders

**Source:** [YouTube](https://www.youtube.com/watch?v=BG_zYneV3mo)
**Author:** Josh Toonen
**Duration:** 14m36s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### 4 ways to make your shots more “cinematic” in Unreal Engine 5 [0:00]
**Transcript:** The reason your renders are boring is because they're not cinematic, but most people have no idea what cinematic actually means.  It's actually pretty simple. The art of cinema is the art of the motion picture.  If you want to make your renders more cinematic, you need to add movement into your images.  So in this video, I'm going to give you four easy methods to add movement into your Unreal 5 renders  that I learned from using Unreal Engine on set and making my own animated film.

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_000.jpg

### Tip #1: The secret to more realistic VFX shots [0:23]
**Transcript:** Starting with tip number one, adding in stock footage.  The best way to add movement is to add movies into your 3D theme.  And there's nothing more realistic than real-life footage.  I love creating stock footage that loops forever.  So anywhere we go in our environment, we can see that motion in real time.  And it's like making a film on a real film set.  So if you want to create fire animations that loop forever, you can use paper flipbooks.  Just make sure in the your plugins menu that you have the Paper 2D plugin enabled.  Now to make a paper flipbook, all we need to do is import each frame from our fire footage.  And this is really easy to prepare.  So inside of Premiere, let's create a new composition.  And then all I'm going to do is set my frame size to 512 by 512  and change our time base or our frame rate over to 24 frames per second.  Then we just need to export this as a PNG sequence.  But I'm going to do one thing before we do that.  Right now, this footage is 20 seconds long, and this can overload your machine pretty quickly.  So instead, let's create a small section of our fire footage.  And then we can delete before and after.  And let's create a looping animation b...

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_001.jpg

### Tip #2: Animate cloth without simulating [3:46]
**Transcript:** adding blowing wind to our cloth. Now believe it or not, this cloth here is not being simulated.  It's actually just using a simple setup inside of the material. By using the same exact  sheet that video games use to add wind to their grass and trees. So how can we add this moving cloth  without simulating anything? Well, let's first start out by editing the material.  So I've reset this material so we're starting with a blank slate. Now most materials start by  plugging in the base color, roughness and normal map. But let's move these out of the way for now  and instead look at this new option, the world position offset. We can use this setting to  offset the geometry that this material is attached to. A really easy way to visualize this is by  typing in simple grass wind. And let's plug this into our world position offset and we can quickly  create default settings by just right clicking and promoting each of these to a new parameter.  For the wind weight, wind intensity and the wind speed. Let's set our wind intensity and our  wind weight to a value of 0.5 and our wind speed to a value of 1. Then just make sure to save or  hit apply and you should see that our tent immediately s...

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_002.jpg

### Tip #3: The VFX secret I learned from Gladiator [7:10]
**Transcript:** The next tip to add movement into our image is to add blowing dust and wind. Now there's two  ways to do this. One is with Niagara particle system which I have a separate video detailing how to  make this custom smoke animation from scratch. But I want to show you an easier way to  art direct your frame so you can add a movement and increase the depth so you can art direct your  smoke and blowing wind. Let's start up by creating a brand new material and I'll call this a  smoke card. Now to build this I'm going to access some more hidden textures inside of Unreal.  So to preview this in your content browser click on the settings and make sure that show engine  content is enabled. When this is enabled you can go above your content folder into this all folder  and now you can search for anything inside of Unreal Engine. So let's double click on the engine  folder and let's type in smoke and if you scroll down you should find this T soft smoke texture.  So let's drag this into our material graph. Now what's great about this texture is it's a  tie-label texture meaning that there's no seams or edges which I'll come in handy later. So to  quickly preview this I'm going to plug this into ...

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_003.jpg

### Tip #4: My favorite lighting trick (animate lights) [12:17]
**Transcript:** the next level the one thing we haven't discussed are these flickering lights for our campfire which  adds this extra layer of intensity and movement. Now there's two quick ways to do this. The first is  we can drag in any light and whenever I'm imitating fire I always like to change the color mode to  use temperature and we can set this down to a value of 2500 which will give this rich orange color.  Then you can just delete any keyframes and instead right click on the intensity detail right here  and let's override this with a float perlin noise. If you look up close you'll see this new curve  that's creating random values throughout our timeline. To adjust this we can right click  and then find our perlin noise channels and increase the amplitude which is the total value that will  go up and down in our intensity. So right now I'll set this to a value of four but you'll notice that  the intensity is going into negative values which is not what we want. Though to fix this we can  also create a new additive track on top of this and we can offset our intensity by a value of  positive four and now we get all the randomness of that curve without getting any negative values  in our in...

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_004.jpg


---

## Structured Notes

### Core Technique
Four quick cinematic techniques for UE5: Paper 2D flipbook fire animation, SimpleGrassWind cloth simulation via World Position Offset, animated smoke cards from engine textures, and Perlin noise-driven animated lights.

### Summary
Josh Toonen delivers four immediately actionable tips that elevate static UE5 renders to dynamic cinematics in under 14 minutes. Viewers learn to create fire using Paper 2D flipbooks from exported PNG sequences, simulate cloth wind using a SimpleGrassWind material node, generate smoke cards from UE's built-in T_SoftSmoke texture without additional assets, and animate light intensity with Float Perlin Noise for organic flickering. Each technique is self-contained and reusable across any UE5 project.

### Key Steps
1. **Paper 2D flipbook fire**: Enable the Paper 2D plugin (Edit → Plugins → Paper 2D); export a fire animation from Premiere as a PNG sequence at 512×512; import the sequence into UE5 as a sprite; create a Flipbook asset and set its material to Unlit with Emissive + Opacity Mask inputs.
2. **Cloth wind via SimpleGrassWind**: In a cloth material, add a SimpleGrassWind node connected to the World Position Offset input; set Wind Intensity = 0.5, Weight = 0.5, Speed = 1.0 for realistic cloth movement without physics simulation.
3. **Smoke cards**: In the Content Browser, enable Show Engine Content → go to All folder → search T_SoftSmoke; create a plane mesh with a translucent material using T_SoftSmoke as the Opacity Mask; place multiple cards at varying depths and scales in the scene.
4. **Animated lights with Perlin noise**: Select a Point Light intensity value in the Details panel → right-click → Float Perlin Noise; set Amplitude = 4; add an additive Sequencer track with a +4 offset so the light never drops to zero and flickers realistically.

### UE Systems / Blueprints / Settings
- **Paper 2D plugin**: Edit → Plugins → search "Paper 2D" → Enable; PNG sequence exported at 512×512 from Premiere/AE
- **Flipbook asset**: Right-click sprite frames → Create Flipbook; set frames per second to match source
- **SimpleGrassWind node**: Material node in World Position Offset input; Wind Intensity = 0.5, Weight = 0.5, Speed = 1.0
- **T_SoftSmoke**: Built-in engine texture at Engine Content → All; used in translucent material Opacity Mask
- **Float Perlin Noise**: Right-click any float property in Details → Float Perlin Noise; Amplitude = 4
- **Sequencer additive track**: Right-click intensity track → Add additive key offset +4 to prevent zero crossings

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
cinematics, lighting, materials, animation, niagara, beginner

---

## Related Entries
- [[how-to-actually-improve-your-films-vfx-dune-in-unreal-5]] — explosion image sequences and animated lights technique
- [[master-cinematic-fog-volumetric-god-rays-in-ue5]] — fog and volumetric techniques to pair with smoke cards
- [[unreal-5-hotkeys-every-filmmaker-must-use]] — Sequencer workflow including additive tracks
