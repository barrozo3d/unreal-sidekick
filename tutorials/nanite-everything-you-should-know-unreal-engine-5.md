---
title: Nanite: Everything You Should Know [Unreal Engine 5]
source: YouTube
url: https://www.youtube.com/watch?v=P65cADzsP8Q
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.0"
tags: [nanite, geometry, lod, cluster-culling, performance, virtualized-geometry, static-mesh, william-faucher, beginner, ue5]
extraction_status: complete
frames_dir: tutorials/frames/nanite-everything-you-should-know-unreal-engine-5/
frame_count: 0
---

# Nanite: Everything You Should Know [Unreal Engine 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=P65cADzsP8Q)
**Author:** William Faucher
**Duration:** 10m32s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro00:27 - Setup [0:00]
**Transcript:** Hey everyone, welcome back and it's great to see you again with Unreal Engine 5 that  dropped.  Nanite with one of its most defining new features.  So this tutorial is going to be all about Nanite, everything you need to know, its pros  and cons, and of course, its limitations.  So is that being said, let's jump right in.  So for starters, let's talk about how to set it up.  It's really easy to do, it's completely non-destructive and very easy to turn off and  on again if you so desire.  So in order to import an object as Nanite, when you get the following dialog box, make  sure you check the build Nanite box and that's really all you need to do.  It import a mesh as Nanite, but what about converting an existing static mesh into Nanite?  Again, all you need to do is to open up your static mesh editor from the content browser  right here and in the actual static mesh editor, you're going to click on the enabled check  box under the Nanite settings.  It's really as dumb as that.  You can uncheck the enabled box at any time to revert your mesh from Nanite back into a  regular non-nanite static mesh.  It's really simple as that.  The general rule of thumb is if Nanite support that type...


### The Good To Know Stuff [1:31]
**Transcript:** So let's talk about what Nanite is exactly.  Nanite is essentially an extremely efficient way to render triangles on screen.  And the way that's worked is thanks to a feature called cluster calling.  So going into the Nanite cluster view mode right here, you'll notice that your model is  split up into a bunch of individual clusters.  Each color here is represents one cluster.  So clusters adjust based on size on screen, distance, and resolution.  Each cluster here is what's going to get LODed away or just called away the moment that  is not visible on screen.  This allows you to have a, I mean, not per pixel, but almost per pixel level of LOD per mesh,  per object cluster calling, which is often about 128 triangles per cluster.  This is a crazy genius bananas LOD system.  This is how we can get millions and millions of triangles in a scene without frying your  computer.  The LODs are all view dependent and based on these clusters.  So in the event that you want to see some of the stats related to Nanite, what you can  do is go all the way to the console command down here and we're going to be typing Nanite  stats list.  And you'll see right away you'll have all the information pert...


### Pros & Cons/Limitations [4:40]
**Transcript:** It's smart enough to update only the thing that change.  It's absolutely fantastic.  Next up is, it's not just the height map anymore.  For those of you who've worked with landscape in the past, it was impossible to get  those overhangs.  Right?  So you've got like landscape caves, that sort of thing.  We couldn't do that with the landscape editor.  But now with Nanite, that's no longer a problem.  Now, we can achieve a certain amount of realism that was just physically impossible to do  with the landscape editor.  And now, thanks to the very fine grain occlusion calling that we just talked about, kit bashing  is easier and better than ever.  For those of you who are not familiar with the content of kit bashing, it's basically  taking a whole bunch of bottles and smashing them together to create a bigger structure.  That's called kit bashing.  And before, in Unreal Engine 4, it wasn't really ideal because you had so many draw calls.  You had to load so many individual models in one time.  And it still had to render those polygons or triangles, even if they weren't visible,  kind of hidden behind the structure, right?  So this makes kit bashing way more readable than it ever has bee...


### When Should You Use Nanite? [9:23]
**Transcript:** space on disk, thanks to its fantastic levels of compression.  So more specifically, a mesh is a good candidate for Nanite if it contains many triangles, or  has triangles that will be very small on screen.  It has many instances in a scene, or if it acts as a major occluder of other Nanite  geometry.  An example of this is a giant cliff face, big closed water type meshes.  Those things are perfect for Nanite.  You guys started becoming an issue when you have like kind of big open ended open geo,  like leads on a tree for example.  Again, this is just a rule of thumb, you don't need to take these two to letter.  Do feel free to experiment and try your own things.  I think even Epic is still in a process of figuring out what works and what doesn't.  And in turn, they are making changes based on the feedback they get from us.  And that my friend concludes this video on Nanite.  I hope that helps demystify Nanite a little bit for you.  If you want even more information, more juicy tips of information, Epic released a  very good two hour live stream with a dev that you can find in the description below.


### Outro & Thanks [10:26]
**Transcript:** So as always folks, thank you so much for watching and I'll see you all next week.



---

## Structured Notes

### Core Technique
Nanite virtualized geometry system in UE5 — cluster-based per-screen-pixel LOD culling that eliminates traditional LOD chains and lightmap UV requirements, enabling millions of triangles in real-time without draw call explosion.

### Summary
10-minute overview of Nanite in UE5.0. Explains the cluster culling system (~128 triangles per cluster, LOD per cluster per screen pixel/distance), how to enable it (import checkbox or Static Mesh Editor toggle), when to use it vs. not (high-triangle static meshes = yes; tree leaves/foliage = use carefully), key advantages over UE4 (no lightmap UVs, better kit bashing, landscape overhangs), and debug tools (Nanite Cluster View Mode, `nanite stats list`).

### Key Steps

**Enable on Import:**
- Import dialog → check **Build Nanite** ✓
- That's it — mesh is now Nanite enabled

**Enable on Existing Mesh:**
1. Content Browser → double-click Static Mesh → open Static Mesh Editor
2. Nanite Settings → **Enabled** ✓ → Save
3. To revert: uncheck Enabled

**When to use Nanite (good candidates):**
- High triangle count meshes (rocks, foliage clumps, detailed props)
- Meshes with triangles that appear small on screen at a distance
- Meshes with many instances in scene (Megascans rocks, etc.)
- Major occluders (large cliff faces, large closed water meshes)

**When NOT to use Nanite (bad candidates):**
- Open-ended, leaf-type geometry (individual tree leaves)
- Skeletal meshes (not supported)
- Spline meshes (not supported at time of UE5.0)

**Debug / Inspect:**
```
// View Mode dropdown in Viewport:
Nanite Cluster View Mode   -- shows cluster color visualization
Nanite Triangle Mode       -- shows triangle density per cluster

// Console:
nanite stats list          -- prints all Nanite stats to console
```

**Cluster Culling Explained:**
- Each mesh = many clusters (~128 triangles each)
- Clusters cull independently: cluster facing away, behind camera, or too small on screen = culled immediately
- LOD is per-cluster, not per-mesh → ~per-pixel granularity
- Smart enough to only update changed clusters (great for animated/changing scenes)
- This is why kit bashing is dramatically better with Nanite: overlapping geometry that was previously wasteful now gets per-cluster culled

**Landscape with Nanite:**
- Nanite supports landscape overhangs — impossible before UE5
- No longer limited to heightmap-only landscape
- Landscape caves, cliffs with overhangs now achievable

### UE Systems / Blueprints / Settings

**Static Mesh Editor — Nanite Settings:**
```
Nanite Settings:
  Enabled: True / False
  Position Precision: (leave default unless you see Z-fighting)
  Fallback Triangle Percent: percentage of triangles kept for non-Nanite fallback
```

**No Lightmap UVs Required:**
- Nanite meshes don't need lightmap UVs
- Static lighting (baked) is not supported on Nanite meshes — must use dynamic Lumen

**Key Stats from `nanite stats list`:**
- Instance count (Nanite vs non-Nanite)
- Cluster count, triangle count visible vs. culled
- Memory usage

### Difficulty
Beginner — one checkbox to enable, rest is just knowing when/where to use it

### UE Version
UE 5.0 (improved in each subsequent release; displacement and tessellation added experimental in UE5.4)

### Tags
nanite, geometry, lod, cluster-culling, performance, virtualized-geometry, static-mesh, william-faucher, beginner, ue5

---

## Related Entries
- `references/version-tracker.md` — Nanite improvements per UE version (5.0 → 5.4 displacement)
- `tutorials/lumen-explained---important-tips-for-ue5.md` — Lumen (required for Nanite static lighting replacement)
- `tutorials/lighting-in-unreal-engine-5-for-beginners.md` — Lighting Nanite scenes
