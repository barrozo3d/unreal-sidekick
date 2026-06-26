---
title: Give me 14 minutes and you'll make cinematic renders
source: YouTube
url: https://www.youtube.com/watch?v=BG_zYneV3mo
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [cinematics, vfx, materials, world-position-offset, flipbook, smoke-card, lighting, paper-2d, rendering, movement]
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
**Transcript:** Starting with tip number one, adding in stock footage.  The best way to add movement is to add movies into your 3D theme.  And there's nothing more realistic than real-life footage.  I love creating stock footage that loops forever.  So anywhere we go in our environment, we can see that motion in real time.  And it's like making a film on a real film set.  So if you want to create fire animations that loop forever, you can use paper flipbooks.  Just make sure in the your plugins menu that you have the Paper 2D plugin enabled.  Now to make a paper flipbook, all we need to do is import each frame from our fire footage.  And this is really easy to prepare.  So inside of Premiere, let's create a new composition.  And then all I'm going to do is set my frame size to 512 by 512  and change our time base or our frame rate over to 24 frames per second.  Then we just need to export this as a PNG sequence.  But I'm going to do one thing before we do that.  Right now, this footage is 20 seconds long, and this can overload your machine pretty quickly.  So instead, let's create a small section of our fire footage.  And then we can delete before and after.  And let's create a looping animation by alt clicking and dragging the same clip  before and after.  And then I'll select all of these and use the Shift D hot key,  which will cross fade at the beginning and ending of each clip.  Now what this does if I have loop playback enabled,  is if I just render out this middle clip with the beginning and ending cross dissolve,  when I play this back, you'll see that this fire perfectly loops.  And you can't see where the fire starts and where it ends.  And if you want to adjust this further, you can just click all three clips and slide them  before and after to find the perfect moment to loop your footage.  So once you have your clip looping correctly, just go to export and we'll change our format  over to a PNG sequence.  And just make sure you have an underscore as the last character in your file name.  And then press export.  Then all you need to do is press control A to select all your files and drag them into your  content browser. Now all of our images will come in as a texture.  But we need to convert these into a flipbook.  So all we need to do is shift click over all of our textures.  And then under sprite actions, we'll just press on create sprite.  This will create a duplicate of our textures, but now we have this new sprite with this cyan color.  From here, just shift click to select all of our sprites,  and then we can right click here and create a new flipbook.  And then just open this up and now you'll see our flipbook in motion.  Now one thing you might need to do is under your default material, scroll down and  under the material property overrides, set the blend mode to additive.  And this will punch out the black background of your stock footage and replace it with  transparency. Then just take your flipbook right here in the content browser and add it into your  scene. And now we have this animated fire that we can move anywhere inside of our scene.  And that could be behind any actor or super close to the foreground.  Pretty cool. Plus you can make duplicates and copy these around.  Now if you duplicate enough of these, you will start to notice that they're perfect clones of one  another. So a good tip here is that you can slightly vary the play rate by changing this from  a value of one to 1.02 and the other ones to 1.04. And then they won't be carbon copies of one  another. Plus it's always a great idea to add depth by placing multiple versions in the foreground,  mid ground and background. By the way, if you want more shortcuts and templates to learn  Unreal faster than ever, then you should check out my course Unreal Fundamentals.  I'll thank you from a complete beginner to making your own action scenes and mastering  filmmaking in Unreal 5. It's on sale right now at unrealforbifx.com slash fundamentals.  I'll leave a link down below. Let's get back to the video. Let's move on to tip number two,

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_001.jpg

### Tip #2: Animate cloth without simulating [3:46]
**Transcript:** adding blowing wind to our cloth. Now believe it or not, this cloth here is not being simulated.  It's actually just using a simple setup inside of the material. By using the same exact  sheet that video games use to add wind to their grass and trees. So how can we add this moving cloth  without simulating anything? Well, let's first start out by editing the material.  So I've reset this material so we're starting with a blank slate. Now most materials start by  plugging in the base color, roughness and normal map. But let's move these out of the way for now  and instead look at this new option, the world position offset. We can use this setting to  offset the geometry that this material is attached to. A really easy way to visualize this is by  typing in simple grass wind. And let's plug this into our world position offset and we can quickly  create default settings by just right clicking and promoting each of these to a new parameter.  For the wind weight, wind intensity and the wind speed. Let's set our wind intensity and our  wind weight to a value of 0.5 and our wind speed to a value of 1. Then just make sure to save or  hit apply and you should see that our tent immediately starts to be animated right here in our viewport.  And this is the simplest way to add this movement onto any object. But one thing that you will  start to notice is that the cloth is intersecting with the wood frame underneath our tent.  So to fix this, let's create a vertex color node. And then I'm going to press the L key and  click in the material graph to create a lurp node. And we'll set our B value to 0 and let's plug the  red vertex color into the alpha. Finally, let's plug the result of this into our world position  offset input. Now let's press save and nothing is going to update just yet, but this will allow us  to select different parts of our mesh and stop it from blowing in the wind. Now this is really  cool. On the top left, let's switch from selection mode over to mesh paint mode. Now on the top left,  you can see that we're in vertex color mode, which means anything that we paint in the vertex color  will be passed on into the vertex color of our material. I'm going to set my fall off to 0.5  and then what we can do is paint on the very top of our mesh. And you can see right away that this  is stopped simulating right on the edge here. If I want to visualize what's going on here,  let's change our color view over to the red channel. And I can see exactly where I painted on the  mesh. How this works is everything that's red is going to turn to a value of 0 and anything that's  not red will have the original wind that we created. And so now I could paint on this object or any  object in our 3D scene and customize the amount of wind. This is great for some of these more complex  structures because all we need to do is turn on our red channel and then we can paint around any  areas that are occluding or have any errors. And you'll notice this door is half red or half transparent.  What you can do by changing your paint color down to a value of 0.4 or 0.5. Then when you paint on top  of the mesh here, it'll reduce the overall movement but it won't turn it off. I could increase this  and continue to paint to reduce it even further. And what's great about this is it's all in real time  interacting through the camera lens. As you can then continue adding decals onto your object.  This birdmark is just a set of decals. So I can slide it and adjust this and it'll react to the wind.

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_002.jpg

### Tip #3: The VFX secret I learned from Gladiator [7:10]
**Transcript:** The next tip to add movement into our image is to add blowing dust and wind. Now there's two  ways to do this. One is with Niagara particle system which I have a separate video detailing how to  make this custom smoke animation from scratch. But I want to show you an easier way to  art direct your frame so you can add a movement and increase the depth so you can art direct your  smoke and blowing wind. Let's start up by creating a brand new material and I'll call this a  smoke card. Now to build this I'm going to access some more hidden textures inside of Unreal.  So to preview this in your content browser click on the settings and make sure that show engine  content is enabled. When this is enabled you can go above your content folder into this all folder  and now you can search for anything inside of Unreal Engine. So let's double click on the engine  folder and let's type in smoke and if you scroll down you should find this T soft smoke texture.  So let's drag this into our material graph. Now what's great about this texture is it's a  tie-label texture meaning that there's no seams or edges which I'll come in handy later. So to  quickly preview this I'm going to plug this into the base color and then I'm going to show you a new  node that you can use to animate your textures which is the panor node. Let's plug this into the UV  input of our texture sample and let's set our x speed to negative 0.25 and right here with this  preview you can see that this smoke texture tiles left and right infinitely which is great. Let's  modify this a little bit further so we can drag and drop these different smoke cards all over our  scene. Let's build a customized speed control by creating two scalar parameters by pressing S  and clicking in our material graph. I'm going to call this speed x and then I'm going to make a  copy and call this one speed y. Then let's drag off of speed x and create an append vector node  which means we can create two different parameters just like we're seeing here with the speed graph  and we can plug them in right here and let's set that speed x value back to negative 0.25  and press save. Now let's take this material and apply it to a plane in our 3d scene. So go to  your quick ad actors menu and let's add in a plane shape and we can move this up and aim it towards  the camera and let's scale this up so we can preview it right here in the scene and then just  click on your smoke hard texture and drag it right on top of that plane. So here we can rotate it  so it's oriented correctly and now let's continue to adjust and modify this. The obvious issue is  that we don't want this to be a thick opaque block so let's change our blending mode over to  translucent and this will change how our material is set up and give us this opacity input.  So let's press the eski and click down to create a new scalar parameter and let's call this opacity.  Now I'll include a link for this down below but I imported this simple texture of a black and white  mask which we can use to keep the center of our image opaque and keep the edges of our image  transparent. So let's drag in our square mask and then let's multiply this by that opacity parameter.  Now when you press save you'll see that we have soft transparent edges and we could reduce our  opacity down to 0.5 or 0.75 to find a good balance. Now our smoke materials pretty much done but you'll  notice that when I slide it into the ground that we get a hard edge and obviously this is not how  smoke would look in real life. So let's add one more node called a depth fade node and let's plug  this into our opacity and then right click on the fade distance and let's promote this to a new  parameter and we can set this to a value of 150. Now when I press save if you look at the seam  it'll instantly go away because unreal is smart enough now to fade our plane by 150 units through  anything it's intersecting. Lastly we can get some weird colors as this goes in and out of the  different parts of our image. Now to make this look a little bit better one thing I'm also going  to do is let's create one more multiply node right here and instead of plugging our smoke material  into the base color let's take our smoke texture and multiply it by our mask and instead for our  base color let's create a vector parameter and plug this into the base color instead and we can  set this to a value of 0.7. This will update our smoke so that it never goes too dark and it'll  also interact with any lights that are in your scene. So from here we can stretch this out and again  add some elements into the foreground, mid ground and background and now we can populate these  throughout our 3d scene. Now the way I like to set this up is we can right click on a material  and create a new material instance we'll call this mi smoke card one and let's apply our material  instance over here. With our material instance we can customize each one of these controls like  the color opacity and speed. This way we can have some smoke cards really close to camera and add  some further into the background. So we can create a smaller one closer to the campfire by creating a  new material instance and just duplicating that with hotkey control D and let's assign this material  over here and then we can scale this down just a bit and let's reduce the opacity because it's a  little bit too in your face at the moment. And what's so cool is you can drag this left and right  until you find the right balance and I could also rotate this to give it a little bit of break up  and look slightly different than the rest of these. And there we go now we have even more blowing  dust in wind and at this point we're getting so much animation and movement. Now to take this to

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_003.jpg

### Tip #4: My favorite lighting trick (animate lights) [12:17]
**Transcript:** the next level the one thing we haven't discussed are these flickering lights for our campfire which  adds this extra layer of intensity and movement. Now there's two quick ways to do this. The first is  we can drag in any light and whenever I'm imitating fire I always like to change the color mode to  use temperature and we can set this down to a value of 2500 which will give this rich orange color.  Then you can just delete any keyframes and instead right click on the intensity detail right here  and let's override this with a float perlin noise. If you look up close you'll see this new curve  that's creating random values throughout our timeline. To adjust this we can right click  and then find our perlin noise channels and increase the amplitude which is the total value that will  go up and down in our intensity. So right now I'll set this to a value of four but you'll notice that  the intensity is going into negative values which is not what we want. Though to fix this we can  also create a new additive track on top of this and we can offset our intensity by a value of  positive four and now we get all the randomness of that curve without getting any negative values  in our intensity and from there you just continue adjusting the position until you're happy with  your result. You can also change the color of these smoke cards so you get interactive light from  the fire itself. I added some additional smoke cards back here which are colored orange and even  though they might not look great on their own when you add them behind some fire elements they  start to combine and feel like combustible smoke coming right from these flames.  So try this out on your own projects to make your shots more cinematic. Now if you're new to  Unreal or you struggle learning in the past don't worry you should check out my Unreal filmmaking  bootcamp, Unreal Fundamentals. I'll teach you how to build your own film sets, animate your  own characters and make your own action scenes in just 30 minutes a day. Plus you'll get all of my  templates, cheat sheets and project files that I use on my own freelance projects. I'll design to  make Unreal easy so you can focus on the fun creative filmmaking side of Unreal 5. Just go to  unrealforvfx.com slash fundamentals or click the link in the description below. Otherwise press  subscribe for more in-depth Unreal 5 guides and breakdowns just like this and click the video here  to see how I made an Nintendo Switch commercial in just 24 hours. I'll see you in the next video.  Peace!

**Frame:** tutorials\frames\give-me-14-minutes-and-youll-make-cinematic-renders\frame_004.jpg


---

## Structured Notes

### Core Technique
Four techniques to add movement to UE5 renders for a "cinematic" feel: (1) looping fire flipbooks via Paper 2D, (2) cloth/fabric wind using Simple Grass Wind → World Position Offset + vertex-color masking, (3) animated smoke cards using Panner node + T_SoftSmoke engine texture, (4) flickering fire lights using Perlin Noise Float curve in Sequencer.

### Summary
Josh Toonen defines "cinematic" as adding movement to otherwise static renders and gives 4 practical techniques. Looping stock footage fire via Paper 2D flipbooks (cross-dissolve loop trick in Premiere → PNG sequence → sprites → flipbook → additive material). Cloth simulation replacement using Simple Grass Wind node in material WPO, with vertex-color mask painted in Mesh Paint Mode to freeze specific areas. Smoke cards built from UE engine's tileable T_SoftSmoke texture with Panner animation, translucent blend mode, Depth Fade for seamless ground intersection, and Material Instances for per-card tuning. Flickering campfire light via Perlin Noise Float override on Sequencer light intensity, with additive track offset to prevent negative values.

### Key Steps

**Tip 1 — Looping fire flipbook (Paper 2D):**
1. Edit → Plugins → enable Paper 2D
2. Premiere: create 512×512 24fps comp → trim fire clip short → alt-drag copies before/after → Shift-D cross-dissolve → export middle section as PNG sequence (underscore as last char in filename)
3. UE: Ctrl-A select all PNG files → drag into Content Browser (imported as textures)
4. Shift-click all textures → Sprite Actions → Create Sprite
5. Shift-click all sprites → RMB → Create Flipbook
6. In flipbook: Default Material → Blend Mode: Additive (punches out black background)
7. Drag flipbook into scene; vary Play Rate (1.0, 1.02, 1.04) across duplicates for variety
8. Layer foreground / midground / background copies for depth

**Tip 2 — Cloth wind without simulation:**
1. Open material → search "Simple Grass Wind" → plug into World Position Offset
2. Promote Wind Weight, Wind Intensity (0.5), Wind Speed (1.0) to parameters → save
3. Create Vertex Color node + Lerp → set B=0 → plug Vertex Color Red into Alpha → plug into WPO
4. Select Mode → Mesh Paint Mode (top-left) → Vertex Color mode
5. Paint areas that should NOT move (Falloff 0.5); visualize with color view → Red channel
6. Partial values (0.4-0.5) reduce wind rather than stopping it entirely
7. Decals applied on top react to wind automatically

**Tip 3 — Smoke cards (animated tileable texture):**
1. Create material → in Content Browser Settings: enable Show Engine Content
2. Navigate to Engine folder → search "smoke" → find T_SoftSmoke (tileable, seamless)
3. Drag T_SoftSmoke into material → add Panner node → connect to UV of Texture Sample
4. Speed X = -0.25; create Speed X / Speed Y Scalar Parameters → Append Vector → into Panner
5. Blend Mode: Translucent → add Square Mask texture × Opacity scalar parameter → soft edges
6. Add Depth Fade node (FadeDistance parameter = 150) → into Opacity → removes ground seam
7. Base Color = Vector Parameter (0.7 gray) × smoke texture × mask → reacts to scene lights
8. Apply to plane → adjust orientation → apply to foreground/midground/background
9. RMB material → Create Material Instance → customize opacity/speed/color per card

**Tip 4 — Flickering fire light:**
1. Add light → Color Mode: Temperature → value 2500K (orange fire color)
2. In Sequencer or Details: RMB on Intensity → Override with Float Perlin Noise
3. Adjust amplitude (e.g. 4) for intensity range
4. Add Additive track on same property with constant value +4 (prevents negative intensity)
5. Color orange smoke cards for interactive fire glow effect

### UE Systems / Blueprints / Settings
- **Paper 2D plugin**: required for flipbook sprite system; enable in Edit → Plugins
- **Flipbook Blend Mode: Additive**: punches out black background transparency on fire/smoke sprites
- **Simple Grass Wind node**: material graph node for procedural wind motion via World Position Offset; inputs: Wind Weight, Wind Intensity, Wind Speed
- **World Position Offset (WPO)**: material output that offsets mesh geometry without simulation
- **Mesh Paint Mode**: selection mode → top-left dropdown; vertex color mode paints red channel into mesh; 0=no wind, 1=full wind (when using Lerp alpha setup above)
- **Panner node**: animates UVs over time; Speed X/Y controls; connects to UV input of Texture Sample
- **T_SoftSmoke**: built-in UE engine tileable smoke texture; find via Show Engine Content → Engine folder
- **Depth Fade node**: fades plane intersection with world geometry by N units; fixes hard plane-ground seam
- **Float Perlin Noise**: Sequencer curve override; creates organic random animation on any float property; set amplitude, add additive offset to prevent negative values
- **Material Instance**: per-instance override of parent material parameters; essential for smoke card variation

### Difficulty
Beginner–Intermediate

### UE Version
UE5

### Tags
[cinematics, vfx, materials, world-position-offset, flipbook, smoke-card, lighting, paper-2d, rendering, movement]

---

## Related Entries
- create-muzzle-flash-gun-fx-for-unreal-5-cinematics.md (Niagara for VFX particles as alternative to smoke cards)
- easiest-vfx-pipeline-ever-with-composite-mesh-actors-in-unreal-engine-57-composu.md (compositing CG into live footage — smoke card approach similar)
