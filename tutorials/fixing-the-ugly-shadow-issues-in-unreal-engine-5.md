---
title: Fixing the Ugly Shadow Issues in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=F3XSKXhIAuU
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/fixing-the-ugly-shadow-issues-in-unreal-engine-5/
frame_count: 0
---

# Fixing the Ugly Shadow Issues in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=F3XSKXhIAuU)
**Author:** William Faucher
**Duration:** 7m12s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Those of you using Unreal Engine 5 have probably run into this problem right here.  Where the shadows on the meshes are just really bad.  We've got these gnarly black shadows splotches all over our models.  Fortunately, we have three very easy solutions to fix this problem.  Now, before I go any further, this is not a bug and it's the way that Nanite works with Raytrade shadows.


### Solution #1 [0:23]
**Transcript:** So the first solution is the quickest and easiest.  We're going to select our directional light or whatever light you have that is lighting your scene.  And in the search details panel, we're going to search for Ray.  And you'll see here you probably have cat raytrade shadows set to enabled.  This is likely enabled if you migrated a project from Early Access or UE4 into 5.0.  And we're going to set this to either disabled or youth project settings.  And just like that, our shadows have now been fixed.  I can now rotate my sun and you'll see we no longer have those nasty black shadows.


### Virtual Shadowmaps vs. Raytraced Shadows [1:02]
**Transcript:** Now, some of you might actually want to be using Raytrade shadows.  Because as you'll see right here, just a bit of comparison, Raytrade shadows,  as you can see in this example right here, are vastly superior to the virtual shadow maps  that Lumin uses by default.  And again, taking a look at this example, if you need soft shadows,  you really should be using Raytrade shadows.  They are going to be much better, much softer, virtual shadow maps work great when they are pretty sharp.  But for any kind of diffuse lighting, sometimes it starts to fall apart.


### Solution #2 [1:36]
**Transcript:** So if you do need to have Raytrade shadows in your lights,  there are still two other solutions to this problem.  So we're going to go to the console command menu.  And we're going to use the console command r.raytracing.shadows.enable.tsyde geometry.  And we're going to set this to zero.  And I'm going to explain why that is soon.  By default, this is set to one.  And by setting it to zero, this solves our issue.  This way, we can preserve our Raytrade shadows  and get rid of those nasty splotches.  But there's a caveat here.  If you have a bunch of meshes in your scene that are one-sided,  like this plain example right here,  you'll see this is a one-sided piece of GEO, right?  And you'll see it is not casting shadows anymore.  If I set the enabled two-sided geometry variable back to one,  you'll see it is now casting shadows  correctly the way you would expect.  I'm going to set this back to zero because that's our solution right now.  You'll see it stops casting shadows,  but you'll see if I flip it around,  then it casts shadows as intended.  And the reason for that is very simple.  When you're using Nanite, Raytrade shadows  do not trace against the actual Nanite GEO.  Raytra...


### Solution #3 [3:12]
**Transcript:** The last solution to our problem is to select your Nanite mesh in question.  We're going to open up the Static mesh Editor.  And what we're going to do is we're going to go ahead and click the show button.  And we're going to show the Nanite fallback mesh.  And you'll see it is ever so slightly different.  You'll see it's a little bit more polygonal.  If I show this is the Nanite mesh and this is the fallback mesh.  And you'll see because it's not quite the same shape,  that is what is giving us these nasty shadows.  The fallback mesh is casting the shadow  because the shape is not exactly the same.  So what we're going to do is we're going to set the fallback relative error  in the Nanite settings of the Static mesh Editor.  And we're going to set this to zero.  And we're going to hit Apply Changes.  Now this can take a while.  This also will have a performance impact on your scene.  Just be careful.  So I'm just going to fast forward here real quick.  And now you'll see this is our fallback mesh.  And this is the Nanite mesh.  It's virtually the same.  And as a result, our issues have largely been fixed.  It's not perfect.  As I back up, you'll see we do have a few issues right a...


### Recap [5:11]
**Transcript:** So to recap, the first solution is to disable ray traced shadows on your light.  The second solution is to set this console variable right here to zero.  I will put the console variable down below.  And lastly, the third solution is to set the fallback relative error to zero.  And hit Apply into Static mesh Editor of your Nanite mesh.


### How Nanite works with raytracing [5:33]
**Transcript:** So the reason why this is happening is because of what I said earlier.  Ray traced shadows are traced against the Nanite fallback mesh,  not the Nanite mesh itself, because it is way less performance intensive to trace against  fewer polygons than it is to trace against a very dense model.  From what I can see, the fallback mesh is really just an LOD of sorts,  a lower res model of the Nanite mesh,  that actually seems to have its mesh normals inverted.  As you can see here, just for demonstration purposes,  this would be the inverted mesh, the fallback mesh,  that has its mesh normals inverted.  And because it's slightly lower res,  the polygons don't quite face the same way.  And as a result, it's casting shadows on our Nanite mesh, so to speak.  So the fallback mesh seems to have flipped or inverted mesh normals,  which would explain why disabling the two sided shadows console variable fixes the shadow issue  on our Nanite meshes.


### Outro & Thanks [6:33]
**Transcript:** So I hope this shed the bit of light, no pun intended, on some of the issues he may be having.  And again, the wonky shadows issue is not a bug that is basically by design.  That's just how Nanite works with ray traced shadows.  So it's important to be aware of.  So each one of these solutions has its own pros and cons.  You're going to have to be the one to choose which one works best for you.  So I hope you found this video helpful.  If you did, do consider subscribing and hitting the bell so you know when more videos like this  are available.  As always, thank you so much for watching and I'll see you next time.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
