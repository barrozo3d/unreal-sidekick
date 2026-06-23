---
title: Nanite: Everything You Should Know [Unreal Engine 5]
source: YouTube
url: https://www.youtube.com/watch?v=P65cADzsP8Q
author: William Faucher
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/nanite-everything-you-should-know-unreal-engine-5/
frame_count: 5
---

# Nanite: Everything You Should Know [Unreal Engine 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=P65cADzsP8Q)
**Author:** William Faucher
**Duration:** 10m32s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro00:27 - Setup [0:00]
**Transcript:** Hey everyone, welcome back and it's great to see you again with Unreal Engine 5 that  dropped.  Nanite with one of its most defining new features.  So this tutorial is going to be all about Nanite, everything you need to know, its pros  and cons, and of course, its limitations.  So is that being said, let's jump right in.  So for starters, let's talk about how to set it up.  It's really easy to do, it's completely non-destructive and very easy to turn off and  on again if you so desire.  So in order to import an object as Nanite, when you get the following dialog box, make  sure you check the build Nanite box and that's really all you need to do.  It import a mesh as Nanite, but what about converting an existing static mesh into Nanite?  Again, all you need to do is to open up your static mesh editor from the content browser  right here and in the actual static mesh editor, you're going to click on the enabled check  box under the Nanite settings.  It's really as dumb as that.  You can uncheck the enabled box at any time to revert your mesh from Nanite back into a  regular non-nanite static mesh.  It's really simple as that.  The general rule of thumb is if Nanite support that type of mesh properly, you should leave  it on just because of how optimized Nanite is.  But we'll get into those specifics a little bit later in the video.  So now we know how to import a mesh as Nanite and convert it to Nanite.  Let's talk about some of the general notes and things that are just good to know about  Nanite before going through the pros and cons and limitations.

**Frame:** tutorials\frames\nanite-everything-you-should-know-unreal-engine-5\frame_000.jpg

### The Good To Know Stuff [1:31]
**Transcript:** So let's talk about what Nanite is exactly.  Nanite is essentially an extremely efficient way to render triangles on screen.  And the way that's worked is thanks to a feature called cluster calling.  So going into the Nanite cluster view mode right here, you'll notice that your model is  split up into a bunch of individual clusters.  Each color here is represents one cluster.  So clusters adjust based on size on screen, distance, and resolution.  Each cluster here is what's going to get LODed away or just called away the moment that  is not visible on screen.  This allows you to have a, I mean, not per pixel, but almost per pixel level of LOD per mesh,  per object cluster calling, which is often about 128 triangles per cluster.  This is a crazy genius bananas LOD system.  This is how we can get millions and millions of triangles in a scene without frying your  computer.  The LODs are all view dependent and based on these clusters.  So in the event that you want to see some of the stats related to Nanite, what you can  do is go all the way to the console command down here and we're going to be typing Nanite  stats list.  And you'll see right away you'll have all the information pertaining to Nanite right  here.  What's more is that all opaque geometry, so no translocency, no mass geometry, all opaque  geometry can be done on a single draw call, not for each object as it was in Unreal Engine  4.  It's smart enough to only update changes and not the entire frame as usual.  So Nanite has a lot happening under the hood and each one of those things is benefiting  us, the artists, in a very exciting way.  This means that draw calls are not really an issue anymore, at least when it comes to the  amount of instances and the amount of geo on screen.  Now can we hit pixel scale detail with geometry, a triangle that are smaller than a pixel, in  general, no.  That's where Nanite optimizes the geo in a very smart and efficient way.  So this is a feature and a limitation in its own sense.  For those of you coming from a film background, we're kind of using that sub pixel level  of detail there, which we're not going to get with Nanite, but for all intents and purposes,  this is enough.  And one more thing to make Nanite incredibly impressive is that it compresses extremely  well.  A 1 million triangle mesh is about 14 megabytes on disk.  That's smaller than the single 4K normal map.  What?  So what makes this ancient valley tech demo 100 gigabytes is not Nanite, it's the texture  resolutions.  Somebody's texture is 8K, probably even 16K I haven't checked, but all these textures  take up a lot of space on disk.  So the compression that's happening with Nanite under the hood is just insane.  So it's saying that Nanite, despite its flaws, is here to stay.  There's a two impressive to ignore.  And with more, Epic is planning on reducing the Nanite file size even more than that.  Talk about exciting.  So now let's get into the pros and cons.  So starting with the pros, obviously goes without saying the sheer triangle density that  you can achieve with Nanite is its main advantage here.  It can handle millions and millions of polygons on screen at a single time.

**Frame:** tutorials\frames\nanite-everything-you-should-know-unreal-engine-5\frame_001.jpg

### Pros & Cons/Limitations [4:40]
**Transcript:** It's smart enough to update only the thing that change.  It's absolutely fantastic.  Next up is, it's not just the height map anymore.  For those of you who've worked with landscape in the past, it was impossible to get  those overhangs.  Right?  So you've got like landscape caves, that sort of thing.  We couldn't do that with the landscape editor.  But now with Nanite, that's no longer a problem.  Now, we can achieve a certain amount of realism that was just physically impossible to do  with the landscape editor.  And now, thanks to the very fine grain occlusion calling that we just talked about, kit bashing  is easier and better than ever.  For those of you who are not familiar with the content of kit bashing, it's basically  taking a whole bunch of bottles and smashing them together to create a bigger structure.  That's called kit bashing.  And before, in Unreal Engine 4, it wasn't really ideal because you had so many draw calls.  You had to load so many individual models in one time.  And it still had to render those polygons or triangles, even if they weren't visible,  kind of hidden behind the structure, right?  So this makes kit bashing way more readable than it ever has been before.  And you get amazing performance on top of that.  Now, let's talk about some of the cons and inconveniences and limitations of Nanite.  The first of which is Nanite gets exponentially more expensive, the higher you go in resolution.  This seems like an obvious thing, but Nanite itself won't perform as well, the higher the  resolution, on top of the obvious decrease in performance you'll have in higher resolutions.  Next up is the overdraw, and that can be an issue.  So overdraw is essentially the number of times that Nanite has to draw that pixel.  Overdraw occurs when you have a lot of layers of geo, even if it's buried or below the surface,  sometimes with overdraw it still has to render those pixels, and that can really affect  your performance.  It can get up to two times as expensive or more depending on how much overdraw is happening  at a time.  So it glancing angles, occlusion, calling really starts being a problem.  So in order to help you guys visualize what's happening here, let's go into the overdraw  view mode that comes in UE5.  Now the overdraw view mode here is kind of a heat map, so the hotter it gets, the more  overdraw there is.  The more overdraw there is, the worse performance you're going to get.  So you'll notice that all these glancing angles occlusion, calling, starts to have a hard  time.  So it tests to see if the polygons are triangles are visible, and a glancing angle is really  hard for Nanite to know if it's visible or not.  And this gets even worse as you get like a bird's eye view over your scene, because there's  so much geo in the scene, Nanite is having a really hard time rendering all this properly.  So just to be clear, this is not a global Nanite issue.  This only occurred when you have lots of stacked layers of geometry over one another.  So let us demonstrate right here, and you'll see what I mean.  If we move the camera below the surface, pay attention to how many layers of geometry  are stacked onto one another here.  This was done to achieve a max level of quality on the ground itself to give it as much detail  as possible, but you'll notice that there's a reason why the performance is not as great  as people expected.  So as long as you keep things reasonable, and you don't necessarily go overboard or completely  overkill with the amount of detail here, and you have the layers of stacked geometry kept  to a minimum, your performance will be much better.  Sometimes in this scene, there's up to 10 layers of stacked geometry over 10 centimeters  or 3 inches.  So there's obviously a ton of stacked geo here, which leads to subpar performance.  Now another caveat here is that Nanite does not support the following.  Translucent are max materials, two sided faces, deforming objects such as skeletal meshes  and such.  It does not support desolation or displacement, so those you're wondering why if not working  in UE5, this is why.  And last but not least, it doesn't work so well with what we call aggregate geometry.  So what the heck is that fancy word?  Aggregate geometry is basically anything that's fine detail, so hair, fur, grass, leaves,  trees, foliage in general, all these things are not going to perform very well with Nanite.  Nanite is going to start calling itself apart, it's going to tear itself apart, try and  optimize, and it's just going to try to figure out what to render on screen, and on top  of that, your performance is really going to struggle.  So that's why they don't recommend using Nanite on stuff such as foliage.  Of course, feel free to try it, it's just not recommended.  So as you can see, they're the fair amount of caveats and things to know about when  it comes to using Nanite.  So the question remains, when should you use Nanite?  When should you not use Nanite?  Nanite should generally be used where possible, okay?  You're going to get much better performance, you're going to get better virtual shadow maps,  you're going to be getting some better memory management, and it's going to take up less

**Frame:** tutorials\frames\nanite-everything-you-should-know-unreal-engine-5\frame_002.jpg

### When Should You Use Nanite? [9:23]
**Transcript:** space on disk, thanks to its fantastic levels of compression.  So more specifically, a mesh is a good candidate for Nanite if it contains many triangles, or  has triangles that will be very small on screen.  It has many instances in a scene, or if it acts as a major occluder of other Nanite  geometry.  An example of this is a giant cliff face, big closed water type meshes.  Those things are perfect for Nanite.  You guys started becoming an issue when you have like kind of big open ended open geo,  like leads on a tree for example.  Again, this is just a rule of thumb, you don't need to take these two to letter.  Do feel free to experiment and try your own things.  I think even Epic is still in a process of figuring out what works and what doesn't.  And in turn, they are making changes based on the feedback they get from us.  And that my friend concludes this video on Nanite.  I hope that helps demystify Nanite a little bit for you.  If you want even more information, more juicy tips of information, Epic released a  very good two hour live stream with a dev that you can find in the description below.

**Frame:** tutorials\frames\nanite-everything-you-should-know-unreal-engine-5\frame_003.jpg

### Outro & Thanks [10:26]
**Transcript:** So as always folks, thank you so much for watching and I'll see you all next week.

**Frame:** tutorials\frames\nanite-everything-you-should-know-unreal-engine-5\frame_004.jpg


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
