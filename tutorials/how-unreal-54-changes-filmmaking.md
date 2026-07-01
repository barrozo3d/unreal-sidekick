---
title: How Unreal 5.4 Changes Filmmaking
source: YouTube
url: https://www.youtube.com/watch?v=NiOgmvMBcxk
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5.4"
tags: [ue54, motion-design, nanite-tessellation, mrg, retargeting, material-designer, motion-matching, filmmaking, new-features]
extraction_status: complete
frames_dir: tutorials/frames/how-unreal-54-changes-filmmaking/
frame_count: 8
---

# How Unreal 5.4 Changes Filmmaking

**Source:** [YouTube](https://www.youtube.com/watch?v=NiOgmvMBcxk)
**Author:** Josh Toonen
**Duration:** 9m38s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### What's inside Unreal 5.4? [0:00]
**Transcript:** Unreal 5.4 just came out with huge updates for filmmakers and visual effects artists.  Now you can make music videos, commercials, and freelance work using Unreal 5 for free.  Now you don't need Cinema 4D, After Effects, and Photoshop.  Now you've got motion design and text tools that render all in real time.  And rendering just got a huge upgrade that gives your indie vfx workflows all the tools and power of a big budget visual effects studio.  And lastly, you can use this new Nanite update to immediately improve your environment.  If you don't know me, what's up? My name is Josh Tunin and for the last eight years,  I've worked in Hollywood visual effects.  As a visual effects artist and supervisor on movies like Star Wars,  Dungeons & Dragons, and across the spiderverse.  And I started using Unreal Engine every day on set for the virtual-production  of Netflix's Avatar the Last Airbender.  So let's break down my top three updates that you can start using in Unreal 5.4.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_000.jpg

### C4D in Unreal 5 - The Motion Design plug-in [0:50]
**Transcript:** Now you can add text, in titles, and create motion graphics for TVs,  documentaries, and logos.  And there's easy animation tools and presets to add to anything in your scene.  Working with text and vectors used to be a pain in Unreal 5.  And a lot of people would flip flop between Cinema 4D and Unreal.  But now it's super easy using the motion design plugin.  Just enable the motion design plugin and you'll have access to this new motion design tab.  Now you can create 2D or 3D text by selecting your fonts directly in Unreal.  And you can add vector logos by importing .sbg files.  It's never been easier to create movie titles,  logo reveals, or any type of motion graphics work easily and haul in real time.  You can even create custom graphics using their shape tools and rulers  to create title slides just like this.  But to create 3D graphics, all you need to know are the Cloner and Effector tools.  Cloners are an easy way to take a collection of objects  and clone them into new groups or shapes.  Cloners create these 3D shapes, but effectors allow you to animate and modify these.  So now you can create real time procedural animation  by dragging these effectors around or animating them through your scene.  I'm also in love with the new animation tools like the animation presets  and modifiers that help you create transition, bounces, and wiggles without keyframing anything yourself.  Now you can add in title slams, zooms, and other common motion graphic presets  all ready for you in Unreal.  So try out these new animation presets to add motion graphics into your next project.  I absolutely love this new motion design toolkit  and I'm going to make more tutorials covering it in depth.  So make sure to subscribe if you want to see more.  Now with Unreal 5.4, Unreal now has Photoshop.  Or should I say Material Designer?

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_001.jpg

### How Material Designer works [2:40]
**Transcript:** For you Adobe users, now you can edit any material using layers just like in Photoshop.  Instead of using the material node graph, now you can build out materials by adding in new layers,  gradients, and masks that you can edit all in engine and bring your motion graphics to life  just like in After Effects.  But once you learn the tools, you'll render faster inside of Unreal,  and you can add 3D into your arsenal.  So you can design and create all in real time.  As a friendly reminder, if you want to import logos and graphics into Unreal,  make sure Unlit Mode is checked if you want that logo to be unaffected by the lighting.  Otherwise, if you want that logo to react to lighting just like it's in that real 3D scene,  then just uncheck Unlit Mode.  So now you can design and animate your own motion graphics,  saving you more time to be creative.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_002.jpg

### Update to Nanite (Add Displacement in your Material!) [3:30]
**Transcript:** The next update you have to start using is Nanite.  Specifically, Nanite Tessilation.  Nanite allows you to put billions of polygons in your scene at the same time.  But Nanite got a huge improvement with Unreal 5.4 with Nanite Tessilation.  Now you can dynamically change your displacement in real time, in the viewport.  Displacement takes a 2D image and adds 3D detail so your objects look good up close.  Using this method, you can create better looking terrains just like in this demo from Marvel 1943.  Rise of Hydra.  I tried this out in my Dune project file,  and now I can modify and control this displacement in real time and change it per shot.  So to enable this feature, you just need to file these four steps.  First, go to your plugins and enable Nanite Displaced Mesh.  Next, go into your config folder and open up DefaultEngine.i and I.  I'll leave this text in the description, but just copy and paste these two command variables  into your renderer settings and then press Save.  And make sure to close down and reopen your project.  And then the last two steps for your 3D object in your scene,  just make sure to right click on this mesh and enable Nanite in your content browser.  And in your material, make sure to plug in a displacement texture and enable Tessilation.  And now you can dynamically add detail and displacement to any object inside of Unreal.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_003.jpg

### Other Exciting Updates in UE5.4 [4:55]
**Transcript:** Lastly, I want to cover the huge update they made to rendering in Unreal.  But before that, I want to share some other highlights that you don't want to miss inside of Unreal 5.4.  This first update will let you add animation to any character even if you're not an  animator yourself. Using the new one-click Retargeting update, now you can just right click on any  animation inside of Unreal. And it'll automatically transfer this animation to any other character  in your project. So now you can download any animation from MixMo.com, right click it inside  of Unreal and transfer it over to any character. The next update is Motion Matching, which will give  you AAA level animations and transitions to your characters have realistic weight and physics.  This project file isn't available yet, but it'll be free in the upcoming months so you can  deconstruct this and apply these techniques to your own films and projects. For you visual effects

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_004.jpg

### Movie Render Graph [5:45]
**Transcript:** artists and filmmakers, rendering just got a huge upgrade with the new movie render graph.  You can turn your complicated render settings into easy customizable menus.  This will give you all the power of a big budget visual effects studio all from your home computer.  So to switch over to the movie render graph, it's really easy. Inside a sequencer, you're going to  do the same thing and press on this little movie clapperboard to launch your render. But instead of  clicking here to change our movie render cue settings, let's click on this little arrow and replace  this with a graph instead. Now when we click on our settings, we have a new menu which is the default  render graph. Now all of our render settings are in this top graph here in our warm-up settings,  global game overrides and global output. All the defaults you're used to are exactly the same  and to change your file path and resolution, we just go to our global output settings and change  the directory or final resolution. Now if you want to add an extra layer into our outputs tab,  all we have to do is go on the left hand side and press on the plus icon to add another output.  Now we can rename this to data passes and now let's create another layer. So now I'll just drag  off a branch from our default layer. Let's create a new deferred render which is just our viewport  and Unreal. And then let's pull off an EXR sequence, create a new render layer, we'll call this  data passes and just plug this in. And then to enable our data passes, just click on your deferred  render tab, then we'll expand all of our details. Let's add an additional post process material and  let's include our world depth and our world position. Then just press save and we're going to render  out the same exact way. We'll go back to move your render queue and press on render local. Now if  you want to make those customizable menus, all you need to know is you need to create some user  variables. And here's how you do it. On the left hand side, all you do is press on the plus icon

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_005.jpg

### Make Custom Menus in MRG [7:35]
**Transcript:** next to variables and now we have all the data types that we're used to. But the really fast way  to modify any setting and turn it into a variable can be done by right clicking. So if I wanted to make  my output directory customizable, all I'd have to do is right click on our global output settings,  expose the output directory as a new pin and then just right click on here and promote this  to a variable. Just like that. Now the biggest reason everyone's upgrading to the movie render  is all the tools around isolating different objects in your scene. But personally, I like to use  crypto mats or object IDs which work in Newq or After Effects as a way to isolate any object inside  of your scene. This way you're not restricting yourself and baking it down. You can change up  these mats and grab an ID for any object in your entire scene. But there are some huge caveats  with the movie render graph that you have to know. The first is that landscapes are not fully  supported. Spongebobal actors aren't supported as well. So any object that has that little lightning  bolt icon next to it won't render out using the movie render graph. You should also know most people  aren't talking about Unreal 5.3 is free forever. But Unreal 5.4 you'll have to start paying for licenses  if your company makes over a million bucks in revenue. So overall my first impressions for  Unreal 5.4 are mixed. There's a lot of potential, a lot of new features. But if you don't plan on

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_006.jpg

### Overall First Impressions and Final Thoughts [9:00]
**Transcript:** taking advantage of these new features right away, I wouldn't recommend upgrading to Unreal 5.4  just yet. Personally, I'll just be upgrading to take advantage of the motion design tools and  make sure to subscribe if you want more tutorials on how to use it. But for everything else,  I'll be sticking with Unreal 5.3. Let me know in the comments what you think is the most exciting  feature and I might cover it in the next video. Otherwise, if you're new to Unreal, check out our  free Unreal 5 Crash Quartz over at Unreal for VFX.com slash Crash Quartz and make sure to subscribe  to the channel for more Unreal filmmaking and visual effects breakdowns just like this. Thanks for  watching and I'll see you next time. Peace.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_007.jpg


---

## Structured Notes

### Core Technique
UE5.4 feature overview for filmmakers. Top 3: (1) Motion Design plugin — Cinema 4D-like motion graphics with Cloner/Effector tools + SVG import + animation presets; (2) Nanite Tessellation — real-time displacement on any mesh; (3) Movie Render Graph — layered render output with user variables for customizable presets. Plus: one-click retargeting from Mixamo, Motion Matching, Material Designer.

### Summary
9-minute overview by Josh Toonen of UE5.4's top updates for filmmakers. Motion Design plugin adds real-time motion graphics (text, SVG, 3D Cloner+Effector, animation presets/bounces/wiggles) inside UE — reduces need for Cinema 4D. Nanite Tessellation enables real-time parametric displacement (enable plugin + DefaultEngine.ini config + mesh Nanite enable + displacement texture in material). Movie Render Graph replaces MRQ for layered render output with render layers, data passes, and user-exposed variables for custom menus. One-click retargeting transfers any animation to any character. Mixed first impressions — author mainly upgrading for Motion Design only at time of recording.

### Key Steps
1. **Motion Design plugin**:
   - Edit → Plugins → enable "Motion Design" → restart
   - New Motion Design tab in viewport toolbar
   - Create text: 2D or 3D, select fonts directly in UE
   - Import SVG logos: File → Import → .svg files supported
   - Shape tools + rulers for custom graphics
   - **Cloner** — take collection of objects → clone into shapes/groups (grids, circles, paths)
   - **Effectors** — animate/modify cloners procedurally; drag effector around scene or keyframe
   - Animation presets/modifiers: title slams, zooms, bounces, wiggles — no keyframing required
   - Logo import tip: Unlit Mode = unchecked (logo reacts to lighting); Unlit Mode = checked (flat logo, unaffected by scene light)
2. **Material Designer**:
   - Layer-based material editing (like Photoshop layers)
   - Add layers, gradients, masks directly in UE
   - Alternative to node graph for material creation
3. **Nanite Tessellation** (UE5.4):
   - Enable Plugins → "Nanite Displaced Mesh"
   - Config folder → DefaultEngine.ini → add two console variable lines (provided in description)
   - Close and reopen project
   - Content browser → right-click mesh → Enable Nanite
   - Material → add displacement texture → Enable Tessellation
   - Result: real-time 3D displacement adjustable per shot in viewport
4. **One-click Retargeting** (new UE5.4):
   - Right-click any animation in Content Browser → retarget to any other character in project
   - Instant Mixamo animation transfer to any project character; no manual retarget setup
5. **Motion Matching**:
   - AAA-quality animation transitions with realistic weight/inertia
   - Project file to be released free (not available at video time)
6. **Movie Render Graph (MRG)**:
   - Sequencer → clapperboard → arrow → Graph mode
   - Default graph: Warm Up → Global Game Override → Global Output Settings → Deferred Render → JPEG Sequence → Render Layer
   - Add data passes: drag branch from default layer → new Deferred Render → EXR Sequence → new Render Layer (name "data_passes") → connect; in Deferred Render: Additional Post Process Materials → World Depth + World Position
   - User variables: left panel → + next to Variables → pick data type → right-click any setting → Expose as new pin → right-click pin → Promote to Variable = creates customizable menus
   - Cryptomatte/Object IDs still supported
   - **Caveats**: Landscapes NOT supported; actors with lightning bolt icon (splineable/Blueprint actors) NOT supported
7. **Licensing (important)**: UE5.3 and earlier = free forever; UE5.4+ = license fee if company earns >$1M revenue

### UE Systems / Blueprints / Settings
- **Motion Design plugin** — UE5.4; Cloner + Effector paradigm (similar to Cinema 4D MoGraph); real-time rendering; SVG import; 2D/3D text; animation presets
- **Cloner** — Motion Design tool; duplicates and distributes objects in grid/circle/path patterns
- **Effector** — Motion Design tool; procedurally animates Cloner distributions; drag-to-animate or keyframe
- **Material Designer** — UE5.4 layer-based material authoring alternative to node graph; Photoshop-like layers/gradients/masks
- **Nanite Displaced Mesh plugin** — enables Nanite tessellation; requires DefaultEngine.ini changes (two console variables) + project restart + per-mesh Nanite enable + displacement texture in material
- **One-click Retargeting (UE5.4)** — right-click animation → Transfer to Character; no IK rig setup needed for basic retargets
- **Motion Matching** — animation system for natural blending between states; uses animation database; project file coming
- **Movie Render Graph (MRG)** — node graph render system; replaces MRQ; supports render layers (multi-pass), data passes (world depth, world position), user-exposed variables for preset menus; cryptomatte supported
- **MRG Render Layer** — isolates geometry into separate render passes; named layers output separately
- **MRG User Variables** — expose any setting as a variable via right-click → Expose as Pin → Promote to Variable; creates UI parameters for the preset
- **MRG Caveats** — Landscape actors not supported; Blueprint/splineable actors (lightning bolt icon) not rendered
- **UE5.4 licensing** — UE5.3 and earlier: free forever; UE5.4+: royalty/license if annual company revenue exceeds $1M (check current Epic licensing for latest terms)

### Difficulty
Beginner overview. Each feature area is covered at a high level — enough to know what's available and how to enable it, not a full deep-dive on any single system.

### UE Version
UE5.4

### Tags
ue54, motion-design, nanite-tessellation, mrg, retargeting, material-designer, motion-matching, filmmaking, new-features

---

## Related Entries
- `how-to-use-the-movie-render-graph-in-unreal-engine-58---simple-setup-for-filmmak.md` — detailed MRG setup (UE5.8); fixes multi-camera render bug
- `nanite-everything-you-should-know-unreal-engine-5.md` — comprehensive Nanite deep-dive
- `non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — animation layering complement to motion matching
- `how-to-make-blade-runner-in-unreal-5-step-by-step.md` — also by Josh Toonen; beginner pipeline tutorial
