---
title: Fixing the Ugly Shadow Issues in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=F3XSKXhIAuU
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [shadows, ray-tracing, nanite, lighting, rendering, troubleshooting, lumen]
extraction_status: complete
frames_dir: tutorials/frames/fixing-the-ugly-shadow-issues-in-unreal-engine-5/
frame_count: 8
---

# Fixing the Ugly Shadow Issues in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=F3XSKXhIAuU)
**Author:** William Faucher
**Duration:** 7m12s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Those of you using Unreal Engine 5 have probably run into this problem right here.  Where the shadows on the meshes are just really bad.  We've got these gnarly black shadows splotches all over our models.  Fortunately, we have three very easy solutions to fix this problem.  Now, before I go any further, this is not a bug and it's the way that Nanite works with Raytrade shadows.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_000.jpg

### Solution #1 [0:23]
**Transcript:** So the first solution is the quickest and easiest.  We're going to select our directional light or whatever light you have that is lighting your scene.  And in the search details panel, we're going to search for Ray.  And you'll see here you probably have cat raytrade shadows set to enabled.  This is likely enabled if you migrated a project from Early Access or UE4 into 5.0.  And we're going to set this to either disabled or youth project settings.  And just like that, our shadows have now been fixed.  I can now rotate my sun and you'll see we no longer have those nasty black shadows.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_001.jpg

### Virtual Shadowmaps vs. Raytraced Shadows [1:02]
**Transcript:** Now, some of you might actually want to be using Raytrade shadows.  Because as you'll see right here, just a bit of comparison, Raytrade shadows,  as you can see in this example right here, are vastly superior to the virtual shadow maps  that Lumin uses by default.  And again, taking a look at this example, if you need soft shadows,  you really should be using Raytrade shadows.  They are going to be much better, much softer, virtual shadow maps work great when they are pretty sharp.  But for any kind of diffuse lighting, sometimes it starts to fall apart.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_002.jpg

### Solution #2 [1:36]
**Transcript:** So if you do need to have Raytrade shadows in your lights,  there are still two other solutions to this problem.  So we're going to go to the console command menu.  And we're going to use the console command r.raytracing.shadows.enable.tsyde geometry.  And we're going to set this to zero.  And I'm going to explain why that is soon.  By default, this is set to one.  And by setting it to zero, this solves our issue.  This way, we can preserve our Raytrade shadows  and get rid of those nasty splotches.  But there's a caveat here.  If you have a bunch of meshes in your scene that are one-sided,  like this plain example right here,  you'll see this is a one-sided piece of GEO, right?  And you'll see it is not casting shadows anymore.  If I set the enabled two-sided geometry variable back to one,  you'll see it is now casting shadows  correctly the way you would expect.  I'm going to set this back to zero because that's our solution right now.  You'll see it stops casting shadows,  but you'll see if I flip it around,  then it casts shadows as intended.  And the reason for that is very simple.  When you're using Nanite, Raytrade shadows  do not trace against the actual Nanite GEO.  Raytrade shadows trace again to what we call the Nanite fallback mesh,  previously known as the Nanite proxy mesh.  And I'm going to show you an example of how the fallback mesh works  after this third solution.  So setting the console variable back to one,  which it is by default.  Now we have the shadows cast by our one-sided geometry,  correctly.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_003.jpg

### Solution #3 [3:12]
**Transcript:** The last solution to our problem is to select your Nanite mesh in question.  We're going to open up the Static mesh Editor.  And what we're going to do is we're going to go ahead and click the show button.  And we're going to show the Nanite fallback mesh.  And you'll see it is ever so slightly different.  You'll see it's a little bit more polygonal.  If I show this is the Nanite mesh and this is the fallback mesh.  And you'll see because it's not quite the same shape,  that is what is giving us these nasty shadows.  The fallback mesh is casting the shadow  because the shape is not exactly the same.  So what we're going to do is we're going to set the fallback relative error  in the Nanite settings of the Static mesh Editor.  And we're going to set this to zero.  And we're going to hit Apply Changes.  Now this can take a while.  This also will have a performance impact on your scene.  Just be careful.  So I'm just going to fast forward here real quick.  And now you'll see this is our fallback mesh.  And this is the Nanite mesh.  It's virtually the same.  And as a result, our issues have largely been fixed.  It's not perfect.  As I back up, you'll see we do have a few issues right around here.  But it's a whole lot better than it was previously.  And I think it's very mesh-dependent.  Some meshes have been totally fine when I use this solution.  And some meshes have not.  So go ahead and try that.  If you need to have two sided shadows  and you want to keep ray traced shadows on,  this is a decent solution that can get you out of a bind.  So again, if I check this mesh here,  we have these nasty big black splotches on the mesh.  I'm going to open up the Static mesh Editor.  I'm going to hit the fallback relative error down to zero.  And hit Apply Changes.  Once the changes are done, save your model.  You'll see that these black nasty shadows are more or less gone.  And behaving as expected.  So like I said, it's not the perfect solution,  but it can help you out sometimes.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_004.jpg

### Recap [5:11]
**Transcript:** So to recap, the first solution is to disable ray traced shadows on your light.  The second solution is to set this console variable right here to zero.  I will put the console variable down below.  And lastly, the third solution is to set the fallback relative error to zero.  And hit Apply into Static mesh Editor of your Nanite mesh.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_005.jpg

### How Nanite works with raytracing [5:33]
**Transcript:** So the reason why this is happening is because of what I said earlier.  Ray traced shadows are traced against the Nanite fallback mesh,  not the Nanite mesh itself, because it is way less performance intensive to trace against  fewer polygons than it is to trace against a very dense model.  From what I can see, the fallback mesh is really just an LOD of sorts,  a lower res model of the Nanite mesh,  that actually seems to have its mesh normals inverted.  As you can see here, just for demonstration purposes,  this would be the inverted mesh, the fallback mesh,  that has its mesh normals inverted.  And because it's slightly lower res,  the polygons don't quite face the same way.  And as a result, it's casting shadows on our Nanite mesh, so to speak.  So the fallback mesh seems to have flipped or inverted mesh normals,  which would explain why disabling the two sided shadows console variable fixes the shadow issue  on our Nanite meshes.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_006.jpg

### Outro & Thanks [6:33]
**Transcript:** So I hope this shed the bit of light, no pun intended, on some of the issues he may be having.  And again, the wonky shadows issue is not a bug that is basically by design.  That's just how Nanite works with ray traced shadows.  So it's important to be aware of.  So each one of these solutions has its own pros and cons.  You're going to have to be the one to choose which one works best for you.  So I hope you found this video helpful.  If you did, do consider subscribing and hitting the bell so you know when more videos like this  are available.  As always, thank you so much for watching and I'll see you next time.

**Frame:** tutorials\frames\fixing-the-ugly-shadow-issues-in-unreal-engine-5\frame_007.jpg


---

## Structured Notes

### Core Technique
Three solutions for Nanite + Ray Traced Shadows splotch bug in UE5: (1) disable RT shadows on the light, (2) set `r.RayTracing.Shadows.EnableTwoSidedGeometry 0`, (3) set Nanite Fallback Relative Error to 0 in Static Mesh Editor. Root cause: RT shadows trace against the lower-res Nanite fallback mesh (with inverted normals), not the actual Nanite mesh.

### Summary
William Faucher explains why UE5 Nanite meshes produce ugly black shadow splotches when using Ray Traced Shadows — it's not a bug, it's by design. RT shadows trace against the Nanite fallback mesh (a lower-res LOD with apparent inverted normals) rather than the actual high-res Nanite geometry. Three solutions with different trade-offs: disable RT shadows entirely, disable two-sided geometry tracing via CVar, or force the fallback mesh to match the Nanite mesh by setting Fallback Relative Error to 0. The comparison against Virtual Shadow Maps (Lumen default) is also shown — VSMs are sharper, RT shadows give better soft shadows.

### Key Steps

**Solution 1 — Disable RT shadows (simplest, loses soft shadows):**
1. Select the directional light (or any offending light)
2. Details panel → search "Ray" → Cast Ray Traced Shadows → set to Disabled or Use Project Settings

**Solution 2 — Disable two-sided geometry tracing (preserves RT shadows):**
1. Open console (~)
2. Enter: `r.RayTracing.Shadows.EnableTwoSidedGeometry 0` (default=1)
3. Caveat: one-sided geometry will no longer cast shadows — flip mesh toward light or use Solution 3 instead

**Solution 3 — Reduce Nanite fallback mesh error (best match, performance cost):**
1. Select the Nanite mesh → open Static Mesh Editor
2. Show → enable Nanite Fallback Mesh to compare with source
3. In Nanite settings: set Fallback Relative Error to 0 → Apply Changes (slow, saves automatically)
4. Result: fallback mesh nearly identical to Nanite mesh, shadows much more accurate
5. Caveats: performance impact; results vary by mesh; not perfect on all assets

### UE Systems / Blueprints / Settings
- **Ray Traced Shadows**: per-light toggle in Details → Cast Ray Traced Shadows; default on migrated UE4/early-access projects is Enabled
- **`r.RayTracing.Shadows.EnableTwoSidedGeometry`**: CVar, default=1; set to 0 eliminates splotches but breaks one-sided geo shadow casting
- **Nanite Fallback Mesh**: lower-res proxy used by RT shadows instead of actual Nanite geo; visible via Show → Nanite Fallback Mesh in Static Mesh Editor
- **Fallback Relative Error**: Nanite setting in Static Mesh Editor; default generates a lossy fallback; set to 0 for exact match (heavy cook time)
- **Virtual Shadow Maps**: Lumen's default shadow system; sharper shadows, less soft than RT; no splotch issue
- **When to use RT shadows**: soft/diffuse lighting scenarios where VSM falls apart

### Difficulty
Beginner (Solutions 1 & 2) / Intermediate (Solution 3 — performance trade-offs)

### UE Version
UE5 (behavior introduced with Nanite in UE5; CVar applies to any UE5 RT project)

### Tags
[shadows, ray-tracing, nanite, lighting, rendering, troubleshooting, lumen]

---

## Related Entries
- fixing-common-ue5-issues-changes-in-50.md (companion UE5.0 RT setup guide — enable HW RT, Lumen reflections, glass fix)
- demystifying-the-skylight-unreal-engine-4-5.md (Skylight + DFAO interaction with scene lighting)
