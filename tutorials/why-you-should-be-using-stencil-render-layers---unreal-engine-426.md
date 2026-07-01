---
title: Why You Should Be Using Stencil / Render Layers - Unreal Engine 4.26
source: YouTube
url: https://www.youtube.com/watch?v=QUyznLlnchA
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4.26"
tags: [stencil-layers, render-layers, movie-render-queue, compositing, alpha, exr, nuke, depth-of-field, motion-blur, vfx, pipeline]
extraction_status: complete
frames_dir: tutorials/frames/why-you-should-be-using-stencil-render-layers---unreal-engine-426/
frame_count: 10
---

# Why You Should Be Using Stencil / Render Layers - Unreal Engine 4.26

**Source:** [YouTube](https://www.youtube.com/watch?v=QUyznLlnchA)
**Author:** William Faucher
**Duration:** 16m57s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back.  It's so nice to see your faces in the middle of this pandemic.  Today we're going to be talking about a really exciting feature called stencil layers.  Now if you have a bit of a vfx background and you've used render layers before, then  you know exactly what I'm talking about.  So render layers and stencil layers are more or less the same thing.  There's a few key differences here, but I'm going to go over that in a video.  So the reason it's so exciting is because contrary to crypto-mat or object ID, stencil layers  actually support that the fields and motion blur right out of the box.  So you get a perfect alpha mask right in the EXR file.  And you get way more control over how you want to split your scene up, contrary to crypto-mat.  So without further ado, let's just get started.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_000.jpg

### Setup [0:38]
**Transcript:** Alright, so now that we're in Unreal, I've got a very simple setup here.  I'm using the Unreal apartment scene, very simple camera, nothing too fancy.  So the purpose of this lesson is to jump into render layer and how we set these up.  Okay?  In this case, I'm going to want to separate both the foreground and the background.  So everything that's on the table here is going to be a one render layer and everything  that's in the background will be its own layer as well.  So before we get started, I'm going to assume that you know how to use the movie render  queue.  If you don't know how, I suggest you go watch this video up here right above because I  don't want you to get lost, okay?  So I'm going to be going a little bit fast if you've never used movie render queue before.  So go check that video out so you know what I'm talking about before we get started.  So moving on, let's go to the window tab up here.  Go to the Cinematics movie render queue.  So I've opened the movie render queue, I've already added my sequence.  I'm going to go to the Settings tab here.  Now what you want to do, okay?  And then start setting up your render layers is you're going to go to the deferred rendering  tab.  Click on this and there's going to be a stencil clip layers tab here, okay?  You're going to want to click on the stencil layers and click on the little plus, okay?  It's as element, okay?  So it's going to say none.  Click on none and you can do browse layers.  It brings up the layers tab up in the top right hand corner here.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_001.jpg

### Setting Your Render Layers [1:58]
**Transcript:** Once that's there, you're going to see there's nothing there.  So you're going to right click and create and be layer.  And I'm going to call this layer foreground, all right?  So let's hit accept and close the movie render queue.  Now I'm going to select everything in my scene that I want to be part of the foreground,  okay?  So I'm going to select these plants, like these, like this, the books, and this.  I'm going to go up to the foreground, right click, click add selected actors, two selected  layers.  Click on this.  Now just to make sure that everything works, you can click the little toggle visibility  here, click the little eye.  And you'll see, oh, oops, I forgot one of these plants here, here and here.  I'm going to add these to my cell, like the layer.  And you know, just for good measure, I'm going to add this chair as well to my foreground  layer.  All right, so now we've got my whole background here and we've got the foreground layer  here.  So what we need to do next, let's go back to the movie render queue, go to cinematic, movie  render queue, back to our settings, different rendering, and in the none layer here, click  on foreground, the layer that we just created.  Okay, now it's also very important to have a accumulator includes alpha checked right  here.  You may need to just one of your project settings.  It's going to tell you a message, you're going to pop up saying, hey, this project that  you need to be enabled, make sure we go ahead and do that.  Now you may think that you need to go ahead and add another render layer for your background.  Fortunately, you don't need to do this.  So if you see here, it says add default layer and you check this, what this does is everything  that's not in a layer, it's going to be rendered as its own thing as its own layer.  So let's say for example, in your background, you have hundreds of thousands of other objects,  you don't need to select all of those and add those to a new background layer.  Okay, so just checking this, it understands that if something is not in a layer, it's going  to be part of its own default layer.  So very handy tip to know.  Before we hit accept, there's one more thing we need to add.  Okay, so we need to go through the settings tab up here and we need to add color output.  Click on this, now color output here, it may be minimized at first, click on this and  you want to click on disable tone curve.  Okay, so the reason for this is epic states that if you don't disable the tone curve, you're  going to have some black halos happening around the render layers in your mask and your  alpha is not going to come out right.  Okay, so it's very important to disable the tone curve.  This means that your image will be rendered in linear SRGB space, which is great for compositing.  You should be compositing in linear space to begin with.  So what's that done?  Okay, I've already set up my console variable for sub sampling.  I've got my anti-aliasing temporal sample count set to 8.  Our anti-aliasing set to none.  EXR 16 bit.  It has to be EXR.  If not going to work, if you just use PNG or JPEG or whatever.  So make sure ESR sequence is checked with multi layer.  Any output tab, make sure that you have your output pass set correctly.  And once again, okay, going back to the deferred rendering tab here, make sure that a accumulator  includes alpha.  Super important.  Otherwise, your mask will not work.  So a few caveats that you should know about here.  So using stencil clip layers, drastically increases your render times.  So for each layer, for each extra layer that you have, it's going to increase your render  times by 100%.  Because it needs to render the entire scene for each individual layer.  So in this case, we've got the foreground and we've got the default layer.  So it's going to take already by default two times longer to render on top of which it  takes even longer because you're including the alpha.  So it's going to increase, it says here, this adds 30% to cost to decimulation.  So you should not enable it unless necessary.  Okay?  So it's going to take 30% longer because of the alpha.  And it's going to take 200% longer because you've got two render layers.  All right?  So now that all of this is set up, we can click the accept button.  We're going to render local and we're going to send it over to Nuke.  I'll be using Nuke, but you can probably use any compositing package of your choice.  You can be fusion or after effects, whatever.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_002.jpg

### Best Practices and Notes [6:34]
**Transcript:** So here are a few things that you're really good to know, neither of the best practices  when it comes to using the stencil layers.  You should be assigning your desired actors to your layers.  You should be adding the layers to the stencil layer in a deferred renderer tab.  So selecting default layer, checkbox, will contain everything that is not in a specified  layer.  Each layer increases render time by 100%.  You need to disable the tone curve in a color output tab because layers will not add  together correctly in Nuke if the tone curve is applied.  A black halo will appear around the edges and generally will not look very good at all.  You also should ensure that you disable auto exposure in the post-refless volume.  You should also disable screen percentage or set it to 100 because using a screen percentage  resizing does not support passing the alpha channel through to your renders.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_003.jpg

### Pros and Cons [7:25]
**Transcript:** So if someone approves of using a stencil layer, include the scene remade visually stable  between many layers.  The main advantage here is that the stencil layer is a much better alternative to object  IDs or cryptomat because it supports depth of field, motion blur, etc.  Cryptomat or object ID do not support these things and you need to render a separate,  depth passes, motion vector passes and assemble this in Nuke afterward.  It's a lot of trouble and if you don't have Nuke, it's a real pain to work with.  An update advantage is the alpha channel contains a mask of pixels that are actually written  to a given layer and you have much better control over what layers get written compared  to object IDs which have zero control.  You can assign whatever actor or shape or object that you want to any given layer whereas  the object IDs you have no control over what gets assigned to what.  Now the cons however is that the render time increases with each additional layer and  if not possible to get an exact match to what you see in the engine, there is no perfect  way to convert back to Unreal's look when you're working in post production in Nuke or  any other composer.  This has been stated by Epic time and time again.  If it comes from them, I'm going to take their word for it.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_004.jpg

### Combining Layers in Nuke [8:38]
**Transcript:** Okay so we're in Nuke now and I've already brought in my new render here that I just got  from the movie Renekue.  So the first thing you'll notice is the colors might seem off and this is totally normal  because we disabled the tone curve which means we're getting a linear sRGB image.  Okay so and Nuke have the tendency of linearizing everything you bring into it.  So don't be surprised the colors look a bit different.  That's fine.  The first thing you want to do, we got our EXR file here so we want to add two shuffle  nodes next.  Okay we need one shuffle node per render layer.  So we're going to go shuffle, bring one here and shuffle again, bring the next one here.  So I'll get double-click my shuffle layer here.  Now I'm in my input layer, I'm going to select on RGB, I'm going to go to Final Image  default layer and here I'm going to click on Final Image foreground because the foreground  is the render layer that we created.  That's how I named it.  So it'll be named whatever you named it in Unreal.  Now this will click so you'll see right away we've got render layer A and render layer  B. So we got the foreground and we've got the background.  We got nicely separated elements here.  So if I click the alpha, we got a perfect alpha for both of our renders.  So this works fantastically.  We can see right away, this is a great way of combining things together.  Now the next thing you want to do is we're going to create a merge node.  Okay so I'm going to do foreground over background and you'll see right now this looks pretty  good but there's a major thing that you should know about.  Unreal states that you need to be merging with plus and not over.  So right now we set this to, by default, it's set to over and you'll see in theory the  result should look the same for the beauty path.  So here we've got a beauty path and here we've got our merge node.  So you'll see you've got this odd hallowing over the basically over everything around everything.  This is because we're using over and not plus.  So at the clearly state you need to use plus.  So we're going to go ahead on my merge node.  I'm going to click on this.  I'm going to set this to plus.  Okay, right away now we're getting a better, much more similar result.  Now it's not perfect.  It's not exactly the same.  Togging in between the two are beauty paths and our merge nodes.  This is normal.  Epic themselves has clearly stated in their livestream on Twitch that the results are never  going to be a perfect match.  Okay, so I'm putting a link to this Twitch stream in the description below.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_005.jpg

### Notes from Epic [11:12]
**Transcript:** This is where Epic clearly tells us that things are never going to be a perfect match.  Okay, so don't take it from me.  Take it from Epic.  As always, when it comes to compositing and post production with Unreal footage,  it's always a compromise.  It's not there yet.  There's it's unreal.  Still have the long way to go.  What for, you know, proper compositing work, but they said themselves,  sorry, Epic has said themselves that, you know, it's not perfect, but it's good enough.  So as you can see, comparing again, it is in fact, you know, not too bad.  Okay, and I'm pretty sure that an advanced compositor who's not me, I am  and by all means not a professional compositor.  Okay, I barely know my way around Nuke, but someone who's very good in Nuke or any,  you know, a full-time compositor will probably know how to work with Steve's  alphas a lot better than I do.  So, so one of the major advantages of using the merge note here is the following.  So I'm going to just for simplicity's sake, I'm going to set this merge note back to over.  Okay, if you can deal with the black haloing around the edges,  which to be honest, if I didn't know where to look, I probably wouldn't notice.  If I hadn't, if I didn't have the comparison with the original beauty pass,  it would probably be okay.  And like I said earlier, an advanced compositor is probably going to know how to work  around this this, because I'm a dumbass when it comes to compositing work.  I'm not very good.  I know the basics, but I'm not going to pretend that I know what I'm talking  about when it comes to compositing.  So we're going to just for fun here.  I'm going to go add some text.  So I got some text here with Hello World written and I'm going to go ahead and merge this.  Okay, with our background.  Okay, so I got this overlayed on top of our background.  I'm going to move it around a bit.  I'm going to move it like right here, let's say.  And I'm going to merge this over this.  And now you'll see this is the one of the major advantages.  You can go ahead and like sandwich some text or other elements between both of your render layers.  And you get a pretty nice alpha.  So you can kind of see here the text.  You got the perfect alpha cut out between the text.  So if I wanted to add, you know, a person in there between the table and the  back in the living room, I could do that.  So this is just one of many reasons why I prefer using stencil layers over cryptomat.  Because you have full control over how you can split your scene up.  So what again, moving this around and it's pretty nice to just have this really nice alpha,  especially you know, it kind of fades in nicely.  It's it's pretty good.  It's not bad, right?  So the stencil layers feature here really start bringing on real one step closer to VFX.  Territory.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_006.jpg

### Useful Compositing Notes [14:07]
**Transcript:** Some of the main things you should know when recombining these layers in nuke is that you  should color correct each individual layer by using the alpha channel as a mask for each  color grade note.  And when you're merging the layers, you really need to merge with plus or also known as add.  Merging will plus will provide a much more accurate result.  But the typical over a over b can be used in some cases if you know,  the result is acceptable.  It is totally your call.  You have to use your creative judgment on this.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_007.jpg

### How To Color Grade Individual Layers [14:40]
**Transcript:** So if I wanted to go ahead and grade the foreground separately, I'm going to add another shuffle node.  Okay, and I'm going to sit this here.  Set this to foreground.  And I'm going to go ahead and add a grade node right here for my foreground.  So in the mask, I need to make sure I connect my grade to the mask of my foreground layer here.  And in mask here, I'm going to select final image foreground alpha.  Now in my grade node, I can go ahead and add a tint.  You know, make this blue on make my whole foreground layer blue or, you know, orange, whatever.  But we get nice masking, right?  So this is how you would grade it because we're using a plus node and not over,  right?  Not a correct merge.  It's not a over b.  It's a plus b.  You need to use masks on any of your grade notes.  Okay, that's just something you should probably keep in mind.  So using render layers is almost more powerful than using unreal's new crypto mat because it's support that the field that support motion blur,  although post process effects will be rendered correctly in your render layer passes.  Okay.  Well, whereas cryptomat or object IDs with the movie Reneku will not support that the field,  they won't support motion blur or any other post process effects like that.  So you need to actually render out a desk pass, need to render emotion vectors and to get the cryptomat masks to form correctly.  Having render layers is also super beneficial because it allows you to actually choose what kind of ID you want.  So you can choose I want if I want to just the plant, just the plants to be in one layer.  If I want to just a flower pot to be in the render layer, you can do that.  Okay.  So I'm going to delete this because it's really ugly.  But this is how you would go ahead and setting up your render layers in Unreal Engine.  This is a very powerful new tool, super handy.  It's not perfect.  Epic themselves is clearly stated that it's not perfect.  You're never going to get a perfect one to one match.  But you know what?  It's a great start.  It's something that I can work with.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_008.jpg

### Outro and Thanks [16:47]
**Transcript:** So guys, once again, I hope you've learned a little something.  I hope this has helped you out.  Leave a comment down below if you have any questions whatsoever.  Don't forget to like and subscribe and I'll see you guys next week in the next video.

**Frame:** tutorials\frames\why-you-should-be-using-stencil-render-layers---unreal-engine-426\frame_009.jpg


---

## Structured Notes

### Core Technique
Stencil / Render Layers via Movie Render Queue: assign actors to named layers in the Layers panel, then configure MRQ Deferred Rendering → Stencil Clip Layers. Each named layer renders as a separate EXR pass with alpha. **Key advantage over cryptomat/object ID**: stencil layers support depth of field, motion blur, and all post process effects. Default Layer checkbox = everything not in a named layer = free background layer. Compositing requirement: merge layers with **plus** (add), not over, in Nuke/Fusion. Epic confirms perfect pixel match is not achievable.

### Summary
16m57s William Faucher stencil/render layers tutorial using UE4.26 Movie Render Queue. Workflow: create layer (Layers panel → right-click → new layer → name "foreground") → assign actors → configure MRQ Deferred Rendering → Stencil Clip Layers → assign layer → enable "Add Default Layer" for background + Accumulator Includes Alpha + Tone Curve OFF + EXR only. Caveats: +100% render time per layer + 30% for alpha. Nuke compositing: shuffle nodes per layer → merge with plus (not over) → grade layers using alpha as mask. Epic confirmed: not a perfect match to beauty pass but acceptable. Advantages over cryptomat: DOF + motion blur support; full control over actor assignment.

### Key Steps
**Create layer and assign actors:**
1. Window → Layers (or right-click in Outliner) → Layers panel appears
2. Right-click in Layers panel → Create → name it "foreground"
3. Select all actors you want in foreground (plants, books, props, etc.)
4. In Layers panel → right-click layer → **Add Selected Actors to Layer**
5. Toggle layer visibility (eye icon) to verify all intended actors are assigned

**MRQ setup:**
6. Window → Cinematics → Movie Render Queue → add level sequence → click Settings
7. Deferred Rendering tab → **Stencil Clip Layers** section → click + → click "None" → **Browse Layers** → select "foreground" layer
8. Check **Add Default Layer** → background = everything not in a named layer (no need to manually assign all background objects)
9. Check **Accumulator Includes Alpha** ⚠️ required; may prompt to update project settings
10. Add **Color Output** tab → disable **Tone Curve** ⚠️ required (without this: black halo around layer edges in composite)
11. Set **EXR Sequence (multi-layer)** as output format ⚠️ PNG/JPEG will not work
12. **Disable Auto Exposure** in Post Process Volume
13. **Screen Percentage = 100** (resizing breaks alpha channel passthrough)
14. Anti-Aliasing → TSR, sample count 8+; AA override = None
15. Render Local → EXR file contains both layers as separate channels

**Nuke compositing:**
16. Import EXR → add two **Shuffle** nodes (one per layer): input layer RGB → "Final Image: foreground" / "Final Image: default"
17. Alpha channel in each shuffle = perfect alpha mask per layer (supports DOF/motion blur blending)
18. Add **Merge** node → A = foreground, B = background → ⚠️ set operation to **plus** (add) not "over" → "over" causes black halo around edges
19. To grade layer separately: add Shuffle node (foreground alpha) → Grade node → connect alpha output to mask input → grade only affects masked area
20. When using plus merge: must use alpha masks on all color correction nodes (not automatic as with over)

### UE Systems / Blueprints / Settings
- **Layers panel** — UE actor grouping system; Window → Layers; right-click to create layers; assign actors via right-click menu
- **Stencil Clip Layers** (MRQ Deferred Rendering tab) — add per-layer EXR output; each named layer = full scene render with that layer isolated
- **Add Default Layer** (MRQ) — automatically renders everything not in a named layer as its own pass; avoids manual assignment of all background objects
- **Accumulator Includes Alpha** (MRQ) — required for alpha mask in output EXR; prompts project settings update on first use
- **Tone Curve = OFF** (MRQ Color Output) — required for correct layer compositing; with tone curve on, layers have incorrect luminance and black halos appear at edges
- **EXR multi-layer** — only format that supports stencil layer passes; PNG/JPEG incompatible
- **Screen Percentage = 100** — rescaling in MRQ breaks alpha channel propagation through render layers
- **Merge with Plus/Add** (Nuke/Fusion) — Epic-specified requirement; "over" compositing causes black halos; plus = additive blend that reconstructs original correctly
- **Render time cost** — +100% per additional named layer; +30% for alpha channel; plan accordingly for multi-layer renders

**Pros vs cryptomat:**
- Supports DOF, motion blur, post process effects (cryptomat does NOT)
- Full manual control over which actors go in which layer
- Perfect alpha in EXR without separate depth/motion vector passes

**Cons:**
- Significant render time increase per layer
- Not a pixel-perfect match to original beauty pass (Epic confirmed)
- Requires EXR workflow

### Difficulty
Intermediate. Setup is straightforward; compositing in Nuke/Fusion requires understanding of merge modes and alpha masks.

### UE Version
UE4.26 (also applicable in UE5 — process is the same)

### Tags
stencil-layers, render-layers, movie-render-queue, compositing, alpha, exr, nuke, depth-of-field, motion-blur, vfx, pipeline

---

## Related Entries
- `unreal-to-davinci-resolve-workflow---aces-srgb.md` — color pipeline from UE to DaVinci (Tone Curve OFF same requirement)
