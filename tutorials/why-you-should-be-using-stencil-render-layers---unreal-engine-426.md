---
title: Why You Should Be Using Stencil / Render Layers - Unreal Engine 4.26
source: YouTube
url: https://www.youtube.com/watch?v=QUyznLlnchA
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/why-you-should-be-using-stencil-render-layers---unreal-engine-426/
frame_count: 0
---

# Why You Should Be Using Stencil / Render Layers - Unreal Engine 4.26

**Source:** [YouTube](https://www.youtube.com/watch?v=QUyznLlnchA)
**Author:** William Faucher
**Duration:** 16m57s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back.  It's so nice to see your faces in the middle of this pandemic.  Today we're going to be talking about a really exciting feature called stencil layers.  Now if you have a bit of a VFX background and you've used render layers before, then  you know exactly what I'm talking about.  So render layers and stencil layers are more or less the same thing.  There's a few key differences here, but I'm going to go over that in a video.  So the reason it's so exciting is because contrary to crypto-mat or object ID, stencil layers  actually support that the fields and motion blur right out of the box.  So you get a perfect alpha mask right in the EXR file.  And you get way more control over how you want to split your scene up, contrary to crypto-mat.  So without further ado, let's just get started.


### Setup [0:38]
**Transcript:** Alright, so now that we're in Unreal, I've got a very simple setup here.  I'm using the Unreal apartment scene, very simple camera, nothing too fancy.  So the purpose of this lesson is to jump into render layer and how we set these up.  Okay?  In this case, I'm going to want to separate both the foreground and the background.  So everything that's on the table here is going to be a one render layer and everything  that's in the background will be its own layer as well.  So before we get started, I'm going to assume that you know how to use the movie render  queue.  If you don't know how, I suggest you go watch this video up here right above because I  don't want you to get lost, okay?  So I'm going to be going a little bit fast if you've never used movie render queue before.  So go check that video out so you know what I'm talking about before we get started.  So moving on, let's go to the window tab up here.  Go to the Cinematics movie render queue.  So I've opened the movie render queue, I've already added my sequence.  I'm going to go to the Settings tab here.  Now what you want to do, okay?  And then start setting up your render layers is you're going to go to the deferred rend...


### Setting Your Render Layers [1:58]
**Transcript:** Once that's there, you're going to see there's nothing there.  So you're going to right click and create and be layer.  And I'm going to call this layer foreground, all right?  So let's hit accept and close the movie render queue.  Now I'm going to select everything in my scene that I want to be part of the foreground,  okay?  So I'm going to select these plants, like these, like this, the books, and this.  I'm going to go up to the foreground, right click, click add selected actors, two selected  layers.  Click on this.  Now just to make sure that everything works, you can click the little toggle visibility  here, click the little eye.  And you'll see, oh, oops, I forgot one of these plants here, here and here.  I'm going to add these to my cell, like the layer.  And you know, just for good measure, I'm going to add this chair as well to my foreground  layer.  All right, so now we've got my whole background here and we've got the foreground layer  here.  So what we need to do next, let's go back to the movie render queue, go to cinematic, movie  render queue, back to our settings, different rendering, and in the none layer here, click  on foreground, the layer that we just created...


### Best Practices and Notes [6:34]
**Transcript:** So here are a few things that you're really good to know, neither of the best practices  when it comes to using the stencil layers.  You should be assigning your desired actors to your layers.  You should be adding the layers to the stencil layer in a deferred renderer tab.  So selecting default layer, checkbox, will contain everything that is not in a specified  layer.  Each layer increases render time by 100%.  You need to disable the tone curve in a color output tab because layers will not add  together correctly in Nuke if the tone curve is applied.  A black halo will appear around the edges and generally will not look very good at all.  You also should ensure that you disable auto exposure in the post-refless volume.  You should also disable screen percentage or set it to 100 because using a screen percentage  resizing does not support passing the alpha channel through to your renders.


### Pros and Cons [7:25]
**Transcript:** So if someone approves of using a stencil layer, include the scene remade visually stable  between many layers.  The main advantage here is that the stencil layer is a much better alternative to object  IDs or cryptomat because it supports depth of field, motion blur, etc.  Cryptomat or object ID do not support these things and you need to render a separate,  depth passes, motion vector passes and assemble this in Nuke afterward.  It's a lot of trouble and if you don't have Nuke, it's a real pain to work with.  An update advantage is the alpha channel contains a mask of pixels that are actually written  to a given layer and you have much better control over what layers get written compared  to object IDs which have zero control.  You can assign whatever actor or shape or object that you want to any given layer whereas  the object IDs you have no control over what gets assigned to what.  Now the cons however is that the render time increases with each additional layer and  if not possible to get an exact match to what you see in the engine, there is no perfect  way to convert back to Unreal's look when you're working in post production in Nuke or  any other composer.  This has been ...


### Combining Layers in Nuke [8:38]
**Transcript:** Okay so we're in Nuke now and I've already brought in my new render here that I just got  from the movie Renekue.  So the first thing you'll notice is the colors might seem off and this is totally normal  because we disabled the tone curve which means we're getting a linear sRGB image.  Okay so and Nuke have the tendency of linearizing everything you bring into it.  So don't be surprised the colors look a bit different.  That's fine.  The first thing you want to do, we got our EXR file here so we want to add two shuffle  nodes next.  Okay we need one shuffle node per render layer.  So we're going to go shuffle, bring one here and shuffle again, bring the next one here.  So I'll get double-click my shuffle layer here.  Now I'm in my input layer, I'm going to select on RGB, I'm going to go to Final Image  default layer and here I'm going to click on Final Image foreground because the foreground  is the render layer that we created.  That's how I named it.  So it'll be named whatever you named it in Unreal.  Now this will click so you'll see right away we've got render layer A and render layer  B. So we got the foreground and we've got the background.  We got nicely separated elements...


### Notes from Epic [11:12]
**Transcript:** This is where Epic clearly tells us that things are never going to be a perfect match.  Okay, so don't take it from me.  Take it from Epic.  As always, when it comes to compositing and post production with Unreal footage,  it's always a compromise.  It's not there yet.  There's it's unreal.  Still have the long way to go.  What for, you know, proper compositing work, but they said themselves,  sorry, Epic has said themselves that, you know, it's not perfect, but it's good enough.  So as you can see, comparing again, it is in fact, you know, not too bad.  Okay, and I'm pretty sure that an advanced compositor who's not me, I am  and by all means not a professional compositor.  Okay, I barely know my way around Nuke, but someone who's very good in Nuke or any,  you know, a full-time compositor will probably know how to work with Steve's  alphas a lot better than I do.  So, so one of the major advantages of using the merge note here is the following.  So I'm going to just for simplicity's sake, I'm going to set this merge note back to over.  Okay, if you can deal with the black haloing around the edges,  which to be honest, if I didn't know where to look, I probably wouldn't notice.  I...


### Useful Compositing Notes [14:07]
**Transcript:** Some of the main things you should know when recombining these layers in nuke is that you  should color correct each individual layer by using the alpha channel as a mask for each  color grade note.  And when you're merging the layers, you really need to merge with plus or also known as add.  Merging will plus will provide a much more accurate result.  But the typical over a over b can be used in some cases if you know,  the result is acceptable.  It is totally your call.  You have to use your creative judgment on this.


### How To Color Grade Individual Layers [14:40]
**Transcript:** So if I wanted to go ahead and grade the foreground separately, I'm going to add another shuffle node.  Okay, and I'm going to sit this here.  Set this to foreground.  And I'm going to go ahead and add a grade node right here for my foreground.  So in the mask, I need to make sure I connect my grade to the mask of my foreground layer here.  And in mask here, I'm going to select final image foreground alpha.  Now in my grade node, I can go ahead and add a tint.  You know, make this blue on make my whole foreground layer blue or, you know, orange, whatever.  But we get nice masking, right?  So this is how you would grade it because we're using a plus node and not over,  right?  Not a correct merge.  It's not a over b.  It's a plus b.  You need to use masks on any of your grade notes.  Okay, that's just something you should probably keep in mind.  So using render layers is almost more powerful than using unreal's new crypto mat because it's support that the field that support motion blur,  although post process effects will be rendered correctly in your render layer passes.  Okay.  Well, whereas cryptomat or object IDs with the movie Reneku will not support that the field,  they won't...


### Outro and Thanks [16:47]
**Transcript:** So guys, once again, I hope you've learned a little something.  I hope this has helped you out.  Leave a comment down below if you have any questions whatsoever.  Don't forget to like and subscribe and I'll see you guys next week in the next video.



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
