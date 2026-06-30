---
title: New Physics Tool for Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=pWEnE86hZrM
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [dash, physics, environment-building, procedural, scatter, collision, workflow, content-library, polygonflow, tool]
extraction_status: complete
frames_dir: tutorials/frames/new-physics-tool-for-unreal-engine-5/
frame_count: 6
---

# New Physics Tool for Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=pWEnE86hZrM)
**Author:** Polygonflow Dash
**Duration:** 5m40s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Physics Intro [0:00]
**Transcript:** Hey everyone, Josh Powers with Polygonflow.  Today I want to go over a fun and incredibly useful tool in Dash that will help you take  the details of your environment to the next level.  The Physics tool allows you to take any mesh, including nanite enabled assets, and use  Physics to drop objects all over your scene.  So let's go ahead and fire up Unreal and get started.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_000.jpg

### Physics Overview [0:27]
**Transcript:** So the first thing we need to do is open the tool.  Now there are two ways we can access the tool, but we'll first go over how you can open  it from the main Dash tool bar up here.  All you need to do is click this icon just to the left of the bridge icon.  You'll notice that a new floating bar is popped up underneath the Dash prompt bar, just  like many of the other tools.  This is where we can set up a temporary physics simulation to add a lot of truly random  detail to an environment.  You might also notice that, quite frankly, there aren't a lot of settings up here.  That's because like everything else in Dash, we want this tool to be incredibly powerful  with limited overhead, so that you never have to break your stride from your workflow.  It's designed to give you exactly what you want, with as few settings as possible.  In this first example, we have some objects that we want to drop to the floor.  Of course we could use the scatter tool for this, but if your scene only needs a few  of these items, or you're just wanting to place them in very specific locations, it's  much more efficient to use the physics tool.  So I'm simply going to select my objects, and then I'll simply press the Run simulation  button here, and the assets will automatically be tagged as dynamic, and drop to the ground,  colliding off each other and the floor.  Now if you aren't satisfied with how the assets landed, you can click on the Reset  button.  Then you can just make a few adjustments, and then run the simulation again.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_001.jpg

### Dropping Assets [1:50]
**Transcript:** Note that pressing Reset will only reset selected assets, allowing you to keep the drops  that you like, and try again with the drops you want to improve.  And if you want to reset all, just hold down Control while you press the Reset button,  and it will reset all the objects currently set to dynamic, regardless of what's selected.  Because the assets remain dynamic while the simulation is still running, you can also  grab any asset you want and try again.  If you move them up, and let go, they'll fall back to the ground.  In effect, so long as the simulation is still actively running, and the assets are set  to dynamic through the tool, you can move them around, and they will continue to interact  with the other objects in the world, both static and dynamic objects.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_002.jpg

### Duplicating Physics Assets [2:41]
**Transcript:** Okay, let's go ahead and close the Physics bar, and I'll show you another way you can  open this tool.  We'll first open the Content Library, and we'll find an asset we want to use.  I'll grab this asset here, and drag it into the scene.  Just like with Scatter, we'll want to hold down Control before we let go of the mouse  button.  This will pop up a contextual menu, and we'll simply click on Physics Drop.  This will place the object in the scene, and immediately make it dynamic.  So if we lift up the asset, and then let go, it'll drop back down to the surface right  away.  But let's say we want a bunch of these assets all over the place.  Well, there's a super simple solution.  With the asset or asset selected, just go up to the Duplicate button and press it.  Then we can press the Select button, and continue to duplicate to add even more objects to the  scene.  And just like that, you can add a plethora of physically dropped assets to your environment.  Alright, let's take a look at Switch.  To put it simply, Switch allows you to turn your selected objects to Dynamic while turning  all the unselected objects in the scene to Static.  This way, once you move on from one Physics Drop and are happy with it, you can use this  to make sure that when your next drop occurs, it's not accidentally moving any of your  previous assets placement.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_003.jpg

### Simple vs Complex Physics [3:58]
**Transcript:** The last two buttons on the bar are simple and complex.  This is referring to the type of collision being used.  In many instances, the default, which is simple, will be plenty enough for your scene.  However, you might notice in some cases where dropped objects might be floating a little  above the surface they dropped on.  That's because the simplified collision is being generated on the fly by Dash using the  geometric data of the asset.  In some cases, especially with high fidelity assets like Megascans, the generated simple  collision will be above the surface.  To solve issues like this, just select the Static object and press the Complex button.  The asset will immediately wake up and drop much more accurately to the rendered mesh.  Using Complex is very helpful, but we recommend using it on a case-by-case basis as it's much  heavier to process in simple collision.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_004.jpg

### Scatter Physics [4:48]
**Transcript:** Lastly, I just want to mention that this tool isn't just limited to individual assets.  The Physics tool can be used on scattered objects as well.  To enable this on scattered objects, just select your scatter instance, click on Set Static,  and then drop your objects on there.  While the simulation is still running, you can even adjust the seat of your scatter tool  and watch as the changes impact the dropped Physics objects, making the entire process  dynamic and non-destructive.  So I hope you were able to get a better understanding of just how powerful and fun it is to use the  Physics tool in Dash.  We will continue to improve and add features to this tool in future updates and look forward  to seeing what you create with it.  Thanks so much for watching and we'll see you in the next video.

**Frame:** tutorials\frames\new-physics-tool-for-unreal-engine-5\frame_005.jpg


---

## Structured Notes

### Core Technique
Dash Physics Tool: temporary physics simulation for environment dressing. Select objects → Run Simulation → Dash tags them as Dynamic and they fall/collide. Reset only selected assets to re-try specific drops. Switch button locks previous drops as Static before continuing. Simple vs Complex collision for high-fidelity assets. Works on Scatter instances too.

### Summary
5-minute Polygonflow Dash tutorial covering the Physics tool for environment detailing. Select any mesh (including Nanite assets) → run simulation → objects fall and collide physically. Key workflow: Reset (selected only) or Ctrl+Reset (all), live-interact while simulation runs (drag assets mid-drop), Physics Drop from Content Library context menu, Duplicate for mass placement, Switch button to freeze previous drops as Static, Simple vs Complex collision (Simple default; Complex for floating Megascans assets). Works on scattered objects too (non-destructively combined with Scatter seed changes).

### Key Steps
1. **Open Physics Tool**: Dash toolbar → click bouncing ball/physics icon (left of Bridge icon) → floating bar appears
2. **Basic drop**: select object(s) in scene → press **Run Simulation** → assets become Dynamic → fall and collide
3. **Reset**: press **Reset** to reset only selected assets; **Ctrl + Reset** = reset ALL dynamic objects
4. **Live-interact**: while simulation running, grab any Dynamic asset, move it, let go → continues falling/colliding in real time
5. **Physics Drop from Content Library**:
   - Open Content Library → drag asset into scene → hold **Ctrl** before releasing → contextual menu → **Physics Drop**
   - Asset immediately placed as Dynamic
6. **Mass placement**: select asset → **Duplicate** → **Select** → continue duplicating → each copy is independently dynamic
7. **Switch button**: makes selected objects Dynamic; all unselected objects Static → prevents previous drops from moving during next simulation pass
8. **Simple vs Complex collision**:
   - **Simple** (default): Dash generates approximated collision on-the-fly; fast but may float above surface for high-detail meshes
   - **Complex**: select the floating Static object → press **Complex** → asset wakes up and drops to actual rendered mesh surface; heavier to process; use case-by-case for Megascans/high-fidelity assets
9. **Scatter physics**: select Scatter instance → click **Set Static** → run physics drops on top; can adjust Scatter seed while simulation running → physics objects react in real time (non-destructive)

### UE Systems / Blueprints / Settings
- **Dash Physics Tool** — Polygonflow Dash plugin; floating toolbar bar; not a native UE feature; requires Dash plugin installed
- **Run Simulation** — Dash Physics toolbar button; tags selected actors as Dynamic; runs UE physics simulation
- **Reset** (selective) — resets only selected Dynamic assets to original positions; allows iterating on specific drops
- **Ctrl + Reset** (global) — resets ALL Dynamic assets regardless of selection
- **Switch** — makes selected Dynamic; makes all unselected Static; essential for multi-pass placement workflows
- **Simple collision** (default) — Dash generates simplified convex hull on-the-fly; may create floating for complex Megascans meshes
- **Complex collision** — uses actual rendered mesh as collision surface; more accurate; processor-heavy; activate per-asset as needed
- **Physics Drop** (context menu) — appears when holding Ctrl while dragging from Content Library into viewport; creates asset immediately as Dynamic
- **Scatter + Physics** — select Scatter instance → Set Static first → physics objects drop on top; Scatter seed changes propagate to physics objects in real time
- **Nanite support** — Physics tool supports Nanite-enabled meshes

### Difficulty
Beginner. The tool is designed for minimal settings and maximum ease. Requires Dash plugin.

### UE Version
UE5 (Dash Physics Tool; Nanite support; no specific minor version mentioned)

### Tags
dash, physics, environment-building, procedural, scatter, collision, workflow, content-library, polygonflow, tool

---

## Related Entries
- `new-ue5-plugin---easy-environment-creation.md` — Dash environment creation workflow (sibling tutorial)
- `new-ue5-plugin---adding-detail-to-your-game-with-dash.md` — adding surface detail with Dash tools
- `procedural-content-generation-framework-in-unreal-engine.md` — PCG for large-scale procedural placement (alternative to Dash Scatter for environments)
