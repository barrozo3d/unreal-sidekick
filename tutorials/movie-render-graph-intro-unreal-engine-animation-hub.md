---
title: Movie Render Graph Intro | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=0c8-8NSarDI
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [mrq, movie-render-graph, rendering, compositing, layers, hold-out, aov, nuke, vfx, cinematics]
extraction_status: complete
frames_dir: tutorials/frames/movie-render-graph-intro-unreal-engine-animation-hub/
frame_count: 4
---

# Movie Render Graph Intro | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=0c8-8NSarDI)
**Author:** Unreal Engine
**Duration:** 11m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hi, welcome to the animation hub. My name is Sean and today we're going to have a look at how to use movie render graph to render out shots and layers. So, we got this cool agor project here. We're going to grab a shot of this big guy kind of ripping the doors apart and then it's this cat looking thing comes jumping out of the way here. So, let's go over here and if you right click and go to cinematics going to movie render graph. You can name it whatever you want. here. And let's double click. And let's have a look real quick in movie render graph. Here we go. So, a lot of these nodes and things should look pretty familiar if you're used to the movie render graph kind of legacy config. A lot of stuff is in here. In movie render graph, we just kind of exposed a lot of the more common settings that people are going to want to use like warm-up settings, game overrides, game output settings, you know, where you can change where where you render to, what sort of resolution. Just in the interest of time, we're not going to go over every single one. You can find a lot of videos and documentation out there on that. So, movie render graph itself, you have your render globals and then you have your actual layers here. So here is one example layer. The first thing that we're going to do is we're going to just drag this apart here and give ourselves something. We're going to delete this. We don't want to render JPEGs. Let's do EXRS here for now. And now in movie render graph, there's this notion of collections and modifiers. Collections are just groupings of actors in your level, right? So if you pull here, start typing collection, you'll see this collection. And then you add a condition group. And there are multiple ways how you can grab actors in your level. You you can grab it by layer, you can grab it by tag, you can grab it by type, you can grab by suble. Here we're going to do it by actor name where you're just typing. So we're just going to hit a star here. And that's just going to grab every actor in our level. So we can control everything. Now the name is very important because everything in the graph concatenates from left to right from input to output. So if you were to have multiple collections named no name and they were all different. Whatever the last one is, it's just going to concatenate down and it's just going to take the last one and that's what's going to be no name when you go into output. So make sure to give your collections a name. We're just going to see all here. Now let's have a look at what a modifier is. So if you go modifier, disconnect this for now. So what you do is you feed in a collection and then you mess with it per layer. So you'll see is is hidden cash out shadow as well hidden effect indirect hold out. So it's the same as if you were to just grab beta here and just set them to hold out. So hold out will be it will render black in the primary rays but it will still be visible to shadows and it'll be visible to reflections and refractions and GI effect indirect while hidden is if you have it hidden like this do you want that to still be in your lumen scene with reflections and GI and the same thing with hidden shadows. Do you want it to catch that? So for this scene we're going to render our set and our background in one layer. We'll render beta here the big guy in another. We'll render gamma which is the cat thing and another and then maybe these cool 2D effects that they're doing in a fourth layer. So we need to make collections for all of these. So let's copy paste here. Pull this. We're going to name this D beta. And let's get here named beta. And if you ever wonder if you got the right thing in your layers, pick something else. If you select this little arrow thing or hit this little arrow thing, it'll select whatever this is. And now let's get gamma gamma over. And now we're going to want to get all of our effects here. Same as the effects and the effects are called. So we see dust, we see sparks and then the 2D effects is just this project 2D effect. So here do star dust star sparks and then star Great. So, we have all of our collections. Now, we're going to use these collections to hide things, unhide things, make things visible, and make things not visible. The one thing we want to do is go back into this all, and we probably don't want to be turning on and off our lighting layer by layer because we want it all to be lit and shadowed and everything the same way. So what you can do is you can add another condition group and instead of putting this to add, you can subtract. Meaning whatever you put in here is going to subtract from this collection. So we're going to flip this over here to actor type. And then here, let's type light. And we want to grab all of our lights. So, point light, skylight, back light. So, we're going to leave all of our lighting alone basically. So, now we're going to start making our layers. This is what your render frames are going to be called. So, let's just name SBG. Pull this over here. Drag this. And again, you need to name these uniquely. So, let's go. M BG hold fold out here. So, this is going to be everything that we want held out in the BG layer. So, we're going to grab beta and we're going to grab gamma and we're going to set those to hold out. And then now, let's go grab our effects. Since these are additive effects, we're just going to turn these off. So, we're going to set hold out to off and is hidden to on. So, we want to hide them. We want to cast shadows while they're hidden. And we want to affect indirect while they're hidden. So, we want them to be in the luminency. And go ahead and plug that in. And that layer is done. So, now what we want to do is we want to make a beta layer. We want to make a gamma layer and now we also an effect layer. So what you can do is you can just pull off and drag up here and it'll automatically make the outputs for you. Very handy. And then here remember we didn't name this. All right. So biz and now let's just copy and paste some of this stuff for the sake of time. So now this would be beta uh hold out. So we want gamma and everything else held out in the beta layer. And we want the effect turned off but still influencing lighting on him mainly GI since we're turning all off here. Now remember beta is a part of that all group beta beta. Let's do this. Come in here and beta is on. And we're going to turn hold out off. We're going to say is it real? So, just walking through this, we turned everything to hold out. We made sure that beta was not held out and it's turned on. And now we have the effects turned off so that it can still influence lighting but not be part of the actual rendered scene. And we just want to do the same thing now for gamma. So, pull down here, pull this off. We're going to switch this to gamma. Switch gamma over to beta for the hold out. Same thing here. Gamma gamma. There's our gamma layer. And now we just want to do our effect here. Pull this down. So effect pull out. And that's going to be everything. And then now we just want to make sure that our effect are on. Let's take is hidden off. These stuff you can find. It doesn't need to be overridden. There we go. So now we have our four layers if you hit save. Let's bring our movie render queue back over here. Pull this down. Switch this over to movie render graph. And now let's load our graph. Here we go. And if we hit render, we should see four layers rendering. So now we see beta knocking out the background. We see gamma here. See beta on his own layer. We see our effects layer here. Now if we open Nuke and we bring everything in push this over plus and we can have a look. Now we see beta here. We see gamma jumping out. We have a look at the individual layers. You see that everything's holding out. But it's still shadowing and it's still reflecting. Let's have a look at our effects here. You see the effects here still have emission and we've split everything out into layers that we can mess with individually and comp. So hopefully that was informative and helpful. Please check out the details of this video for more

**Frame:** tutorials\frames\movie-render-graph-intro-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Movie Render Graph (MRG): node-based rendering layer system for splitting a shot into separate comp-ready passes. Key concepts: **Collections** (actor groups selected by name/tag/layer/type) → **Modifiers** (Hold Out or Hidden with options) → **Layers** (named render outputs). Subtract condition groups exclude lights so lighting is consistent across all layers. Each layer outputs independently for Nuke compositing while maintaining shadow/reflection contributions from held-out elements.

### Summary
11-minute Epic Animation Hub tutorial by "Sean" demonstrating Movie Render Graph for multi-layer rendering. Uses a creature fight scene (Beta + Gamma + effects). Shows: creating an MRG asset; setting up EXR output; building collections (actor name wildcard `*`); subtract condition group to exclude lights; building modifiers (Hold Out vs Is Hidden with Cast Shadow / Affect Indirect options); constructing 4 render layers (BG, Beta, Gamma, Effects); unique naming requirement; MRQ integration; final Nuke composite showing each element isolated while maintaining shadow/reflection continuity.

### Key Steps
1. **Create MRG**: right-click in Content Browser (or Sequencer) → Cinematics → Movie Render Graph; double-click to open

2. **Set output format**: delete JPEG node; add **EXR** node instead

3. **Collections** (actor groupings):
   - Drag into graph → type "collection" → add Collection node
   - Add **Condition Group**: select actors by Actor Name (`*` = all), Tag, Type, Layer, or Sublevel
   - **Name every collection uniquely** (name concatenates into output filename; duplicates = last one wins)
   - Example collections: `all`, `beta`, `gamma`, `effects`

4. **Exclude lights from "all" collection** (so lighting is identical across every layer):
   - Add second Condition Group to "all" collection → set to **Subtract** mode
   - Filter by Actor Type → add: Point Light, Skylight, Back Light (all light types in scene)

5. **Modifiers**:
   - Feed a collection into a Modifier node
   - **Hold Out**: primary rays = black; actor still casts shadows and appears in reflections/GI
   - **Is Hidden**: fully invisible; sub-options: **Cast Shadow While Hidden** (yes/no), **Affect Indirect While Hidden** (keeps actor in Lumen GI/reflections)

6. **Build layers** (each layer = one render output):
   - **BG Layer** (`sbg`): beta = Hold Out; gamma = Hold Out; effects = Is Hidden + Cast Shadow + Affect Indirect
   - **Beta Layer** (`biz beta`): all = Hold Out; beta = Hold Out OFF (back on); effects = Is Hidden + Affect Indirect only
   - **Gamma Layer**: same as Beta but swap beta ↔ gamma in assignments
   - **Effects Layer**: all on; effects = Is Hidden OFF (visible)
   - Tip: drag output pin downward to auto-create additional layer outputs

7. **MRQ integration**:
   - Movie Render Queue → switch config to **Movie Render Graph** → Load Graph
   - Hit Render → all 4 layers render simultaneously in sequence

8. **Nuke composite**: import all EXR sequences; each element is isolated (primary = black where held out) but contributes shadows/reflections to other layers

### UE Systems / Blueprints / Settings
- **Movie Render Graph (MRG)** — node-based successor to legacy MRQ configs; right-click → Cinematics → Movie Render Graph; right-click → Movie Render Graph in Sequencer
- **Render Globals** — global settings node: warmup frames, game overrides, output resolution, output path
- **Collections** — actor group nodes; condition groups select by: Actor Name (wildcard `*`), Tag, Type, Layer, Sublevel; Subtract mode to exclude; must be uniquely named
- **Modifiers** — hold out or visibility state applied to a collection for a specific layer:
  - **Hold Out**: actor renders black in beauty pass; still visible to shadows, reflections, Lumen GI
  - **Is Hidden** → **Cast Shadow While Hidden**: actor invisible in beauty; still casts shadows
  - **Is Hidden** → **Affect Indirect While Hidden**: actor invisible; still contributes to Lumen GI/reflections
- **Layers** — named render pass outputs; unique names required to avoid output filename collision; output concatenated left to right from collection → modifier → layer
- **EXR output node** — add in place of JPEG; per-layer EXR sequences for Nuke compositing
- **MRQ (Movie Render Queue)** — load MRG asset in MRQ render config via "Movie Render Graph" option; standard MRQ launch and settings apply

### Difficulty
Intermediate-Advanced. Requires understanding of compositing concepts (hold out, shadow pass, GI contribution). The node graph UI is straightforward once the mental model is clear. Most complexity is in correctly assigning Hold Out vs. Is Hidden per layer.

### UE Version
UE5 (Movie Render Graph introduced in UE5.4 as successor to legacy MRQ configs)

### Tags
mrq, movie-render-graph, rendering, compositing, layers, hold-out, aov, nuke, vfx, cinematics

---

## Related Entries
- `make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta.md` — MRQ basics (legacy EXR/TSR workflow); beginner filmmaking pipeline
- `master-cinematic-fog-volumetric-god-rays-in-ue5.md` — AOV pipeline via MRQ (3 passes → Nuke: Detailed Lighting − Lighting Only)
- `lumen-explained---important-tips-for-ue5.md` — Lumen GI; MRQ warmup frames required for Lumen accuracy; surface cache behavior
