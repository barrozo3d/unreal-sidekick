---
title: How to Create Cinematic Environments in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=Cp7sWfiHcJg
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [environment, world-building, lighting, cloth-simulation, fog-cards, landscape, foliage, level-organization, cinematics, animation]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-cinematic-environments-in-unreal-engine-5/
frame_count: 10
---

# How to Create Cinematic Environments in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=Cp7sWfiHcJg)
**Author:** Josh Toonen
**Duration:** 15m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en if you're creating environments in unreal a lot of beginners fall for this simple mistake they don't add animation into their environments so I want to take you behind the scenes of the samurai sword fight we made for war of being made entirely inside Unreal Engine 5 building the characters animations and environments from scratch and I want to share all the lessons we learned along the way so if you want to improve your environments today I'm going to share nine of my favorite techniques that you can apply to your scenes right away to create depth animation and movement and stick around to the end cuz I'm going to show you two methods to create cloth simulations to add flowing wind to Flags banners and costumes what's up my name is Josh tunin and I've spent the last 8 years working on Hollywood visual effects as an artist and supervisor on movies like Star Wars Deadpool and across the spider Earth and I've started using Unreal Engine on set and to create animated films of my own so let's hop into unreal and pull back the curtain on war of being whenever I'm starting an environment build I always go through these three stages the blockout the camera Cera and then the build Step One is the blockout so in this case we were under some pretty tight deadlines so I started with an asset pack first so I could start using highquality models to start our First Assembly of this environment but usually I'll block out a scene using primitive shapes like cubes spheres and cylinders just to get a simple layout of the scene I'll also include a human scale reference and import motion capture data as early as possible to see how the characters look inside of the environment step two is creating cameras now these don't have to be final shots but you should try to mimic the overall look and Vibe of your scene and make sure that your environment Works shot through the camera lens if your compositions don't work at this blockout stage no amount of high-res geometry or particle effects is going to save your scene you want to view your environment through as many camera angles as possible at this stage so once the camera is set up I'll use that to tweak our blockout and make sure that the layout of the overall environment makes sense for the scene we're trying to shoot and then the third and final step is finishing our build so I'll go in and add decals upres any assets that aren't working close to camera and then add in any lighting and movement through particle effects and find ways to add life and animation into the environment itself and you don't have to over complicate this if I look at our floating rocks here you can see that they're constantly spinning and if I look from a top down view you can see that the volumetric and shadows are moving along with our floating rocks here and if I go into sequencer to see how this is set up all I'm doing is I'm taking these two arch quickel assets and then parenting them to a basic actor this is just an empty actor that we can animate but when we apply animation to the parent then we can start adding in decals and have them parented and move correctly with our arches so we can save some time on texturing these arches since we never really see them up close we can easily move these around and then they'll stay in the same place as they animate throughout our sequence but I'm just using two rotation key frames here and in the curve editor I've selected them and changed their pre- infinity and post Infinity settings to linear so they continue on before and after the key frames and then for the background we kept it super simple because we don't see it close up and we just used some static meshes some Landscapes and Scattered them around not using the landscape tool here and we also O Used an hdri image for our background so we could easily move it around and even rotate it shot to shot but I always like to use a real world image a photograph or piece of video because it's always going to do a better job than CG at grounding your shot in reality one of the reasons I try to block out lighting as early as possible is that it's our way to show off our hard work and show off our environment so if I just disable all of the lights in the scene here you'll see how big of a difference this makes and when our environment is black we don't actually read any of the geometry or detail in our environment so typically if I was just going to start this from scratch I like to start off by backlighting environments especially hallways like this so I would just start off by making a spotlight increasing the attenuation radius and then pushing it back in our scene so that we can backlight our environment and because our surfaces are reflective the position of the ligh has a big effect on how it reflects across our surfaces and then to add some fill light I'll just add some additional spotlights and this way we can be really selective about what parts of our environment we choose to reveal and this is why I like to block out the camera moves early on because from here we can tell right away if something's working or not and we can easily change the position of our light in context previewing one of our final shots we can do the same thing for our backgrounds here and just try to add some lights to bring out the different planes of our objects now less is more so it's typically going to be a better idea to use less lights and make them bigger and affect wider areas as opposed to adding in five or 10 lights in a small area just like this so just spend the time to fish around and find something interesting and if you're ever unsure just go back through your camera view and we can start to preview and move around our lights all right the next environment is the cliff side built by Fonville bear and we use three techniques to build this environment that you can start applying right away now one of the key things that we added in early on were Cloud cards these are just simple planes that we would hide in the background to add depth and atmosphere to our shop now one of the first movies I ever worked on was alien Covenant and one of the locations they shot at in real life is Milford Sound in New Zealand now if you look up images of this place it looks Larger than Life and has real life clouds intersecting with mountains now it's really important when you're trying to add in stylized clouds to ground your work in reality and use real life reference like you can find at milord sound and let real life influence the design and placement of your Cloud cards so if I just select these you can see that they're just really big cards that are one-sided that we can start to move around and place shot by shot you can even add in simple animation to move them left and right to give us some drifting movement and the material is super easy to make if I select this fake fog material all that we're doing is we're changing the blend mode over to translucent and then we're taking this Cloud texture and plugging it into the opacity Channel a little extra thing here is we're adding in this depth fade node and that will take any object and give it a smooth transition when intersecting with objects this way we can take these simple Cloud cards and change the fade distance something in the hundreds so that you can make these soft transitions between different areas of your environment and we didn't stop there we also added in different different cards for our background robots because we'll only see it deep in the background by keeping this as a card we can quickly adjust the layout and placement and rotate it so we still have full control but we didn't have to build a large scale 3D model for something that we're only going to see in the background and to that end a really important lesson we learned on this project is only build what you see one thing we did with our mountains in the background if we get up close here you'll start to see that these are actually just really simple cards and planes as well if you look from the top down it becomes more obvious but ever since unreal 5 and nanite has been released I think a lot of people default to using 3D models and 3D trees but when we're seeing the trees from this far away there's no clear advantage to using 3D models so instead we opted to use tree cards and that way we can paint a bunch of these anywhere we want across the landscape and that way far away in the distance our trees will still hold up and add some rough edges to our Landscapes without taking down our render time and if we see an area that we want to paint on some more trees it's really easy to make those adjustments on the Fly and to add in trees shot by shot now another thing we did which helped the overall team was separating our environment into levels now how does this work levels are just another way to organize all of the actors in your outliner into separate groups so not everyone on our animation team had great workstations where they could show all the lights particles and effects so we just made these effects and G ometry levels so we can still adjust the animation of our actors but we don't have to load in our entire scene in the background and later on we could easily swap out our lighting levels and change it for different times of day and you can fully control your levels inside of sequencer by creating a level visibility track that way we can keep our characters and geometry exactly the same in this wide shot but just change the lighting in time of day which brings us to our our last environment the graveyard and the location of our last battle between the [Music] samurai first we use unreal's landscape tools to create depth and sculpt a custom landscape and there's a few methods we use to add movement and animation into our environment first let's talk about how we use the landscape tool so we just created a small landscape around the center of our scene we have a separate water plane that makes up the water itself and then we're just taking the sculpting tool of our landscape to brush when you're sculpting just click anywhere to raise that surface up or shift click to push it further down and this way we could Block in something that looks fairly complex but was actually quite simple to set up but one thing that's not as well known is using landscape grass in your material landscape grass is a way for us to populate foliage across our entire grass ground and this way we can add a lot of high detail geometry and Fidelity up close and also help hide our character's feet in the ground but we don't have to place anything by hand and if we wanted to change our landscape and paint in different areas in the background this foliage will automatically populate and it'll go on top of any surface it's supposed to and to set this up in the material all you have to do is type in landscape and create a landscape grass output this is the same node we have here and and once you have this new node you can add in an element to your array and then start adding in different landscape grass now landscape grass is an asset just like a material or a blueprint so you can right click in your content browser and type in landscape grass and you'll see that the actor called landscape grass so I use the prefix lgor Katana and when I open this up you'll see that I almost have an identical menu to our foliage system so you can change things like the grass density the scale of each foliage actor and if you want to add random rotation or align it to surface but to be clear you're not locked in to just using grass you can add different assets into these landscape grass materials and we ended up using these to spread out different soldiers katas weapons and pillars across our entire landscape so definitely give this a try in your next environment and lastly here's a few methods that you can use to add movement and animation into your own environments my favorite way is to add add Birds into the background these help create scale by showing the movement and speed of the birds but it also adds that animation and Randomness from real life I tested out all the birds on the unreal Marketplace and I wasn't really happy with any one particular system so we went ahead and built our own background Birds which is now available at unreal forv fx.com Birds we created six drag and drop systems that you can easily bring into any project you use in the future and within two clicks you can drag in your your birds change their speed flight path color and animation and then you never have to mess with it again you can instantly upgrade your scenes and make them feel bigger more complicated and more photorealistic by adding in background Birds into any shot and personally I have not made an environment without using these since they were created you might be surprised how something so small can make such a big impact so go and download these while they're on sale this week only now available at unreal forv fx.com [Music] birs to add in some more movement we added some cloth simulations to our flags and Banners here let's go up close to this flag and take a closer look now to preview a cloth simulation usually you'll have to start simulating your game and now we can see the results of this blowing in the wind now how do you set up cloth for Flags so that they simulate at render time well all you need to do is that you have to set this up as a skeletal mesh actor so create your flag mesh in a software like Blender make sure to tesselate it before you bring it in having extra geometry here will help our simulation so create a simple cloth card then just export this as an fbx file and then just click and drag the file into the content browser to import it and then we want to import this as a skeletal mesh now open it up and we have our skeletal mesh editor and now we have to add in our cloth so you can rightclick on your asset and create clothing data from this section and hit create this will add clothing data but we're not done yet just right click on your mesh again and apply the clothing data the last step is activating our cloth paint and here we can paint anything that's simulated white and anything we don't want to simulate to be black just scroll all the way down into the brush settings and change your paint value to zero for any areas that you don't want to simulate like the corners of our flags now when we deactivate cloth paint we'll see our simulation live in the viewport and then you can adjust any cloth settings in this chaos cloth config under the mass and material options from there you can just drag it into the viewport then we'll add in a wind directional source and we'll use this wind source to adjust the strength and speed of our wind and then to preview your simulation press alt s or go to the simulate button here and now we can see our simulation live in the viewport and make any adjustments while our flag is simulating you can also change the direction of your Wind by rotating your wind direction source to help art direct your shot and you can even add this into sequencer and from here you could adjust your wind to see the different Behavior set the speed to zero or we can set it back to 200 or 2,000 to increase that wind speed so start applying these tips right away in your own environments and this week only background birds will be on sale so right now go over to Unreal forv fx.com Birds and download these right away so you can instantly improve your environments otherwise subscribe for more videos just like this and check out our entire behind the scenes of war of being and we'll break down the entire process that we went through to create the 5 minute samurai sword fight entirely in unreal 5 thanks for watching and I'll see you next time peace

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_000.jpg


---

## Structured Notes

### Core Technique
Nine techniques for cinematic UE5 environments: (1) 3-stage pipeline (blockout → camera → build); (2) rotating floating objects via parent empty actor + two keyframes + curve pre/post-infinity Linear; (3) HDRI for background + background robot card; (4) cloud/tree/mountain cards (plane mesh + translucent material + cloud texture in opacity + Depth Fade node); (5) backlit key light + selective spotlights; (6) landscape sculpting + Landscape Grass output in material for auto-populated foliage/props; (7) Level organization (geometry/effects/lighting as separate sub-levels); (8) background birds (asset product); (9) cloth simulation on skeletal mesh flags (Chaos Cloth + wind directional source).

### Summary
Josh Toonen shares 9 environment techniques from War of Being, a samurai fight cinematic made in UE5. Stage 1 (blockout): asset packs + primitives + human scale ref + mocap data early. Stage 2 (cameras): set up cameras early — if composition doesn't work at blockout, nothing will save it. Stage 3 (build): decals, upsres, lighting, movement. Animated floating rocks: parent multiple assets to empty actor → 2 rotation keyframes → Curve Editor: set Pre/Post-Infinity to Linear for continuous rotation. Background: HDRI rotatable shot to shot; background cards for robots/scenery not seen close-up. Cloud/tree/mountain cards: translucent plane + cloud texture → opacity → Depth Fade node (fade distance in hundreds); add simple translation keyframes for drifting. Lighting: backlit spotlight (push into scene, control surfaces via reflective material roughness); fill with additional spotlights; selective reveal; less lights/bigger radius. Tree cards: paint anywhere on landscape vs 3D tree models — prefer cards for distant trees. Level organization: separate geometry/effects/lighting into sub-levels → Sequencer Level Visibility Track controls what's loaded; teams with weak workstations load only what they need. Landscape Grass: Landscape Grass Output node in material → Landscape Grass asset (prefixed LGO_) → define foliage/prop array → auto-populates on landscape brush. Cloth simulation: export flag as skeletal mesh FBX with tessellated mesh from Blender → import as skeletal mesh → Right-click → Create Clothing Data → Apply Clothing Data → Cloth Paint (white=simulate, black=anchor, zero for corners) → Chaos Cloth Config settings → Wind Directional Source → Alt+S to preview in viewport → add Wind track in Sequencer for animation control.

### Key Steps

**3-stage environment pipeline:**
1. Blockout: primitives (cubes, spheres, cylinders) + asset pack for quick layout; add human scale ref + mocap data
2. Camera: set cameras early; evaluate all compositions at blockout stage; tweak layout based on camera view
3. Build: decals, upres close-camera assets, lighting, particle effects, animation

**Animated floating objects (continuous rotation):**
1. Add an empty Actor to scene
2. Parent mesh assets to the empty actor (drag onto it in Outliner)
3. Add rotation keyframes (2 keys, start + end)
4. Curve Editor: select keyframes → set Pre-Infinity + Post-Infinity to Linear → object rotates continuously

**Background composition:**
- HDRI: Sky Sphere/Sky Light → real photo; rotate shot to shot for different BG feel
- Non-hero background objects: use 2D cards; never build 3D models for background-only elements
- Cloud/fog cards: plane mesh → translucent blend mode material → cloud texture → plug to Opacity → add Depth Fade node (fade distance ~hundreds) → soft blending with environment
- Add simple translation keyframes for drifting movement

**Lighting approach:**
1. Start with spotlight pushed deep into scene behind/above environment → backlit shapes visible, shadows created
2. Increase Attenuation Radius to cover whole environment
3. Add selective fill spotlights; bigger lights affect wider areas (fewer lights is better)
4. Preview through camera cuts to evaluate in context
5. Lower Material Roughness on surfaces → more reflection → more dramatic backlight reads

**Tree/mountain cards:**
- Create material: Translucent blend mode + tree card texture → Opacity
- Add Depth Fade node for soft edge intersections
- Paint on landscape quickly; easier to adjust than 3D trees; identical quality at distance

**Level organization:**
1. World Settings / Windows → Levels → create sub-levels (Geometry, Effects, Lighting)
2. Move actors into appropriate sub-levels
3. Sequencer: Add Level Visibility Track → control which levels load per shot
4. Lighting: swap lighting sub-levels for different times of day (same geometry, different light)

**Landscape Grass (auto-population):**
1. Landscape Material → right-click → add Landscape Grass Output node
2. Expand array → add Landscape Grass element
3. Content Browser → Right-click → Landscape Grass Type (prefix: LGO_)
4. Open LGO asset → add foliage meshes/actors to array → set density, scale, random rotation, align to surface
5. Paint landscape → foliage auto-populates on painted areas (works for any static mesh, not just grass)

**Cloth simulation for flags:**
1. Blender (or any 3D app): create flag mesh → tessellate (subdivide) for extra geometry → export FBX
2. UE5: drag FBX → import as Skeletal Mesh
3. Skeletal Mesh Editor → Right-click on LOD → Create Clothing Data from Section → Create
4. Right-click → Apply Clothing Data to same section
5. Activate Cloth Paint mode → paint white where cloth simulates, black where anchored; brush Paint Value = 0 for corners (hold points)
6. Deactivate Cloth Paint → cloth previews in viewport
7. Physics Asset / Chaos Cloth Config: adjust Mass, Air Resistance, Stiffness, Damping
8. Add Wind Directional Source to level → adjust Strength and Speed
9. Alt+S to simulate in viewport → rotate Wind Directional Source to art-direct wind direction
10. Sequencer: Add Wind track → keyframe Speed (0 = no wind, 2000 = strong wind)

### UE Systems / Blueprints / Settings
- **Pre-Infinity / Post-Infinity (Curve Editor)**: controls behavior before first and after last keyframe; Linear = continues the curve forever → continuous rotation loop with only 2 keyframes
- **Depth Fade node**: fades material opacity where it intersects with other geometry; used on cloud cards and fog for soft blending
- **Landscape Grass Output (material)**: UE material node; spawns Landscape Grass Type assets across painted landscape without manual placement
- **Landscape Grass Type**: asset defining which meshes to scatter, density, scale variation, alignment options; works for any props (weapons, pillars, soldiers)
- **Level Visibility Track (Sequencer)**: controls which sub-levels are loaded per shot; enables lighting/effects changes without touching geometry
- **Chaos Cloth (UE5)**: successor to APEX Cloth; configure via Chaos Cloth Config (mass, stiffness, air resistance, damping)
- **Create Clothing Data / Apply Clothing Data**: skeletal mesh editor workflow to add cloth simulation to mesh sections
- **Cloth Paint**: paint tool for cloth; white=simulated, black=pinned; sets per-vertex paint weight
- **Wind Directional Source**: actor providing global wind for cloth/particle systems; Strength controls force magnitude
- **HDRI Sky**: background image for outdoor environments; rotatable per shot to adjust ambient lighting

### Difficulty
Intermediate

### UE Version
UE5

### Tags
[environment, world-building, lighting, cloth-simulation, fog-cards, landscape, foliage, level-organization, cinematics, animation]

---

## Related Entries
- how-i-made-a-godzilla-cinematic-in-unreal-engine-5.md (fog cards + DMP background cards + night lighting)
- how-to-actually-improve-your-films-vfx-dune-in-unreal-5.md (backlit key light technique)
- how-i-remade-the-backrooms-using-vfx.md (Exponential Height Fog for environment atmosphere)
