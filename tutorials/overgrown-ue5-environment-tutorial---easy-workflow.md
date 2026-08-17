---
title: Overgrown UE5 Environment Tutorial - Easy Workflow
source: YouTube
url: https://www.youtube.com/watch?v=9926HB1PA-c
author: Polygonflow Dash
ingested: 2026-08-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/overgrown-ue5-environment-tutorial---easy-workflow/
frame_count: 0
frame_status: pending-selection
---

# Overgrown UE5 Environment Tutorial - Easy Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=9926HB1PA-c)
**Author:** Polygonflow Dash
**Duration:** 12m20s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py overgrown-ue5-environment-tutorial---easy-workflow <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] What if we could turn an empty environment into a forgotten, overgrown ruin in just a few minutes?
[0:06] In this tutorial, I will show you how to transform an ordinary building into a post-apocalyptic scene using Dash.
[0:13] We will scatter vegetation, create natural overgrowth with masking, and add climbing-wise in just a few simple steps.
[0:20] So let's get started.
[0:23] So, we are starting with the Quixel unfinished building scene.
[0:27] I have already cleaned it up a bit by removing a few objects, and I've added an Ultra Dynamic Sky Blueprint for the lighting.
[0:34] First, I want the focal point for the scene, so let's bring in a main object.
[0:39] I'll open the Dash Content Browser, switch to my DecoGun library, and simply drag a motorcycle model into the scene.
[0:46] After this, I tweak the lighting a bit to make the bike stand out more.


### Material Edit [0:57]
**Transcript (timestamped):**
[0:57] Assets from the Dash libraries come with fully editable materials.
[1:02] I open the Material Editing panel from the Tools panel.
[1:05] If you don't see it, just click on this icon to find it.
[1:08] Let's adjust a few settings like the color, roughness, and the dirt amount.
[1:16] Now it's time to start adding vegetation.


### Surface Scatter [1:32]
**Transcript (timestamped):**
[1:36] I have already downloaded a few Megascans plans.
[1:39] Any assets you download from Thab or Bridge will automatically appear in the Dash Content Library.
[1:45] While holding Ctrl, I simply drag them into the scene and choose Scatter here.
[1:51] From here, I can adjust the density, scale, and various masking options.
[2:04] The falloff settings are especially useful.
[2:07] I'll make just a few clicks with our de-gut and interesting layer of ground vegetation.
[2:13] We can also use objects as masks.
[2:16] For example, I will add the motorcycle to the proximity mask section.
[2:20] By adjusting it, I can keep the area and the bike cleaner.
[2:24] But I can also invert it.
[2:35] Next, let's create vegetation growing along the walls and pillars.
[2:40] I select a couple of foliage groups, hold Ctrl and drag them onto the ground, and choose Scatter on Selection.
[2:56] After a few adjustments, I select the walls and pillars where I want the plants to appear and add them to the proximity mask section.
[3:04] I can invert the mask and find between the falloff and the noise mask until I'm happy with the result.
[3:35] If I ever need to, I can convert the procedural instances into Unreal Fallage using Convert Instances to Fallage from the Dash toolbar.
[3:45] But keep in mind that after converting, the Scatter is no longer procedural and becomes a standard foliage actor.
[3:54] Let's add some vegetation to the stairs as well.
[3:57] I select the surfaces and scatter the plants just like before.
[4:17] This time, I will increase the surface line value, so some of the plants naturally hang over the edges.
[4:32] But we're not limited to the ground. We can also scatter directly onto the motorcycle.
[4:38] I will use the English Ivy Pack, but I only want a few of these assets.
[4:42] Instead of scattering immediately, I hold Ctrl, drag onto an empty area, and choose Placing Grid.
[4:51] After selecting the plants I want, I will create a new Surface Scatter from the Dash toolbar.
[5:01] Now I will assign the selected plants, set the motorcycle as the target surface, increase the density, and shape the distribution until it feels natural.
[5:24] Finally, I will use an empty actor as a mask to keep the engine visible.


### Path Scatter [5:40]
**Transcript (timestamped):**
[5:40] Now let's create some hanging vegetation using the Path Scatter.
[5:44] First, I will draw a spline.
[5:53] Then I select the plants, hold Ctrl, and scatter them onto the spline.
[6:03] Here I just need to adjust the rotation.
[6:23] I can also duplicate splines and add them to the same scatter.
[6:38] And I can even add more Ctrl points whenever I need.


### Vine Tool [6:47]
**Transcript (timestamped):**
[6:48] Now it's time to generate some climbing wines. I will duplicate my empty actor to use it as my wine's origin.
[6:58] From the Dash toolbar I will choose the Wine tool.
[7:02] First, I will assign the origin actor, choose the Spiller as the target surface, and Dash generates a fully procedural wine.
[7:23] Naturally, I can add more surfaces if I want to.
[7:27] From here I can tweak the settings, add more branches, and even replace the default leaves with any foliage assets I want.
[7:54] But if I need more artistic control, I can also draw wines manually using the Draw Wine tool.
[8:19] I can spend forever tweaking these, but this already looks pretty good. I will quickly generate a few more around the scene.
[8:28] With this tool it's surprisingly fast to create an environment that's completely taken over by nature.
[8:35] Time to add some more details. I will place a few props, like this fuel can.


### Physics Tool [8:41]
**Transcript (timestamped):**
[8:44] Then I use Dash's physics tool to quickly create some believable brick piles. I can select this brick, choose Physics drop from the Place menu, and when it's seconds I have a nice pile.
[9:02] I will duplicate it and place it somewhere else in the scene.


### Decals [9:15]
**Transcript (timestamped):**
[9:17] Next, let's add a few decals from the Content Browser.
[9:30] This can also be scattered procedurally.
[9:56] Finally, I will add a few wall splatters to give the environment a little more history.


### Background & Details [10:10]
**Transcript (timestamped):**
[10:12] To make the scene feel larger, I will add a few ruined buildings in the background. So these assets only exist inside my project's Content folder, but Dash can index them as well.
[10:24] In the Dash Content Browser, I will switch to the Project Library, select the folder containing the assets, and click Compute.
[10:36] Dash automatically text everything, making it easy to search large asset libraries by their properties.
[10:47] I will pick this one and drag it into the scene.
[10:58] And here I can also add a few trees.
[11:05] And I can download a couple more Megascans assets and rearrange a few elements.
[11:30] I will give the motorcycle one final color adjustment so it stands out a bit more. And after a few lighting tweaks, here is the final result.


### Outro [11:35]
**Transcript (timestamped):**
[11:44] So, using just a handful of Dash tools, we have transformed the empty building into a lush, abandoned scene while keeping the entire workflow fast and fully procedural.
[11:54] If you'd like to try Dash yourself, you can download this for free using the link below. Thanks for watching and I see you in the next tutorial.



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
