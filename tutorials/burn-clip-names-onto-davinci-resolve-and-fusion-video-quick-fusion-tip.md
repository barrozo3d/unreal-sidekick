---
title: Burn Clip Names onto DaVinci Resolve and FUSION Video (Quick Fusion Tip!)
source: YouTube
url: https://www.youtube.com/watch?v=0YhVHCoHKkg
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "N/A"
tags: ["DaVinci Resolve", "Fusion", "data burn-in", "text node", "expression", "compositing", "metadata", "clip name", "quick tip"]
extraction_status: complete
frames_dir: tutorials/frames/burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip/
frame_count: 5
---

# Burn Clip Names onto DaVinci Resolve and FUSION Video (Quick Fusion Tip!)

**Source:** [YouTube](https://www.youtube.com/watch?v=0YhVHCoHKkg)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 3m57s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Fusion Data Burn-In Intro [0:00]
**Transcript:** So this is a quick tip for adding data burn-ins  onto your fusion composition.  So with a fusion composition, you normally  got multiple elements.  And if you want to add, say, the name onto each element,  I'm going to show you how to do that.  You've got the standard one that comes with the workspace.  And if you're going to workspace and you're  going to data burn-in, that will read your metadata.  And it'll add, say, let's have a look at the clip name.  You can add the clip name there.  And then you can add something else like, like, time  code or something.  But if I go to a fusion composition,  it doesn't know where to get that information from.  So I'm going to show you how we do that.  So in this example, say I want to define the clip name  and burn it into this.  And then the clip name of this element  and burn it over here.

**Frame:** tutorials\frames\burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip\frame_000.jpg

### Custom Burn-In for Fusion Comps [0:45]
**Transcript:** So I'm going to go into my fusion composition.  So I've basically got an A over B. There's my media in.  And that's from my media library, whatever it's called.  And I've got another media in here.  So the thing to do is you add a text node.  So grab a text node.  And I'm going to just connect that to that one.  So it's going to merge that on top.  And then in my text node, I'm going  to click in this text window.  And then right mouse button, make an expression.  So you go to expression.  And then in this part here says text, bracket, whatever  those things are.  Those things, apparently.  Anyway, you delete those.  And you type in the name of this media in.

**Frame:** tutorials\frames\burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip\frame_001.jpg

### Create Expression for Dynamic Text [1:30]
**Transcript:** So actually the name of the node, not the actual clip.  So you just type in media in one, then dot.  And then for the name, it's a clip name, capital C, L, I, P, capital N, A, M, E, dot value, capital V, A, L, U, E, and then press Enter.  And then it pipes that information from this node into your regular text node.  And so you can grab this and move it around and do the sort of things you'd normally do with your text  nodes, which is great.  And so on this next one, this one's using media in three.  So I just grabbed this from over here and pulled in.  Let's just delete it like that.  And I'll just go, what's that expression?  So put that in there, pipe that into there, like that.

**Frame:** tutorials\frames\burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip\frame_002.jpg

### Burning In MediaIn Node Names [2:15]
**Transcript:** There it is.  Cool.  And then grab a text node, put it there, drag it onto that bit.  And then go to the text node, write mouse button.  I first click on that window, write mouse button, connect on expression text bracket bracket, media in.  And then so I was, oh, two.  So this is media in two now.  We, oh, we need a, I can't see media in two.  I'll cut that bit and make it look really professional.  Media into dot, clip name, dot value into there.

**Frame:** tutorials\frames\burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip\frame_003.jpg

### Advanced Fusion Data Burn-In [3:00]
**Transcript:** And there we are.  That's the smaller, it's a smaller element.  So that's why it's bigger.  There you go.  So you've got your two things, you move them around.  And now we've got like the names of multiple things.  And there's a list that Andrew had.  And I'll put it in the description.  But there's a ton of other things that you can, you can add in there.  Look at that.  So there's lots of things you can grab from the media in.  And then you can also do this for loaders,  but I don't know the actual syntax yet.  So when I find out, I'll do a little update video and add it at the end of this one or something like that.  Anyway, brilliant.  Well fun.  So now you can have your data information burnt in on multiple elements in your composition.  Wow.  Look at that.  It's explosive knowledge.  All right.  See you on the next one.  Bye.

**Frame:** tutorials\frames\burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip\frame_004.jpg


---

## Structured Notes

### Core Technique
Using Fusion expressions in DaVinci Resolve to dynamically burn clip/node names from MediaIn nodes onto video composites as on-screen text overlays, enabling multi-element burn-in labels inside a Fusion composition.

### Summary
This is a quick tip (under 4 minutes) for DaVinci Resolve Fusion users, not an Unreal Engine tutorial. Dean Yurke demonstrates how to use Fusion's expression system on a Text node to pull the ClipName metadata from any MediaIn node and display it as a dynamic burn-in label. The method works for each MediaIn independently, so a multi-layer comp can show a different clip name over each element. He also notes that the standard DaVinci Resolve workspace Data Burn-In tool reads metadata automatically but does not work inside a Fusion composition, making this expression approach necessary.

### Key Steps
1. In a Fusion composition, add a Text node and connect its output to a Merge node (over the target MediaIn layer).
2. Click inside the Text node's text input field; right-click → Make Expression.
3. Delete the default expression text and type: `MediaIn1.ClipName.value` (substituting the actual node name, e.g. `MediaIn2`, `MediaIn3`).
4. Press Enter — the Text node will now display the clip name of the referenced MediaIn node.
5. Position and style the Text node as usual.
6. Repeat for each additional MediaIn layer, referencing the correct node name in the expression.

### UE Systems / Blueprints / Settings
- DaVinci Resolve Fusion: Text node, expression editor, MediaIn node metadata (ClipName.value)
- DaVinci Resolve Workspace: Data Burn-In tool (for non-Fusion timelines)
- No Unreal Engine systems involved

### Difficulty
Beginner

### UE Version
N/A (DaVinci Resolve / Fusion only)

### Tags
DaVinci Resolve, Fusion, data burn-in, text node, expression, compositing, metadata, clip name, quick tip

---

## Related Entries
- `green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor.md` — advanced DaVinci Resolve Fusion workflow for green screen extraction
- `green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-.md` — DaVinci Fusion extraction pipeline feeding into Unreal Composure
- `how-to-get-precision-control-in-davinci-resolve---use-shift-drag.md` — another DaVinci Resolve quick tip from the same channel
