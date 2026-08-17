---
title: UNREAL ENGINE 5 FOR CHARACTER ARTISTS | Tutorial | Texture & Materials
source: YouTube
url: https://www.youtube.com/watch?v=DrirPMH5TwI
author: Jared Chavez
ingested: 2026-08-17
ue_version: "5.3.2 (continuation of Part 1, same project; not restated verbally this episode)"
tags: [materials, pbr, textures, pipeline, intermediate, ue5-3]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UNREAL ENGINE 5 FOR CHARACTER ARTISTS | Tutorial | Texture & Materials

**Source:** [YouTube](https://www.youtube.com/watch?v=DrirPMH5TwI)
**Author:** Jared Chavez
**Duration:** 19m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Welcome back to Unreal 5 and using it for Character Art Part 2.
[0:05] So where we left off last time was we brought our models into Unreal.
[0:10] We got the model set up and we brought it into our content browser,
[0:14] allowing for us to drag and drop into the scene.
[0:17] Now, the next part of the process that we're going to want to tackle is we're going to want to import our textures.
[0:23] So let's go back up to our original content folder that we created for ourselves.
[0:28] And I noticed I actually forgot to create one of the folders, so I'll come here and create a new folder and name this Textures.
[0:36] And then inside of this, this is where we're going to deposit all of the textures for this asset that we're going to use.
[0:42] So we'll go ahead and right click on here, come up to our import, and then we are going to locate our assets that we need for this.
[0:52] Once you found those, I'm going to go ahead and drag and drop all of them in here.
[0:57] So I will open all of the textures that I need.
[1:00] Now, one thing that you may notice is we're getting all of this stuff popping up over here and it says some of the images are being imported as normal map.
[1:09] That is usually correct.
[1:11] So here's the normal maps that I'm using for this model and all three of those were converted to be processed as a normal map.
[1:18] Now, what that means is when it's reading the image, it's going to interpret that information correctly.
[1:24] Some of these other maps that are brought in like this one, this one, this one, this one, this one, and this one.
[1:30] These are not normal maps, so we don't want that processed as a normal map.
[1:34] Now, I'll go ahead and show you guys what I mean.
[1:36] But first, I wanted to also illustrate something about your projects when you are working with Unreal.
[1:42] You'll see this little star down here in the left hand corner.
[1:45] What that means is that means that this is an item that hasn't been saved yet.
[1:49] So in order to save it and make sure that this asset exists in the project for future projects when we open it, we're going to go ahead and select all of these and then right click and come to save.
[2:00] So that's going to save all of these to this project to ensure that they're available for us the next time we open it.
[2:07] Okay, so now let's talk about something really quickly.
[2:11] So when I mentioned that these images are being brought in as normal map, what I mean is if we double click on this image, we're going to open up our image and we're going to see this, right?
[2:23] So there's a couple of things that I want to take note of in this window.
[2:27] The first one is going to be this compression setting.
[2:30] What this compression setting is doing is this is where the image was being set to normal map.
[2:35] So you can see here, we have a couple of different compression settings.
[2:39] It's automatically selecting normal map based on the image being brought in.
[2:43] It just kind of interprets that information.
[2:45] I don't know how it does it, but it does.
[2:47] So it assigns it to this normal map.
[2:49] Now, if we open up one of the other images, you're going to see that the compression setting is just set to the default compression setting, which is what we want.
[2:58] We're going to want this for all of our other maps except for our normal maps.
[3:02] There are going to be extra cases where sometimes we might be using masks or grayscale or some of the different settings, but for the most part defaults probably going to be fine.
[3:12] And normal map is going to be what you're going to need assigned for your normal map.
[3:16] So the last thing that I wanted to mention is you may notice that I have a couple of these maps called RMA.
[3:23] What these maps are is these are going to be compressed images with multiple texture inputs put into one file.
[3:30] So if we go ahead and turn off all of these and just isolate our red channel, you can see here is my roughness channel.
[3:37] This is going to be all of my roughness information stored specifically on to the red channel.
[3:44] Now, if we turn on our green channel, you can see that this is the metalness map and our blue channel is our ambient occlusion.
[3:51] And occasionally you can pipe something into the alpha channel for this project.
[3:56] I didn't have anything piped into there, but if I wanted to, I could have also done that.
[4:01] So we'll turn this all back on and you can see it's a crazy colorful information.
[4:06] That's just because of all of the information from these individual image channels being composited together to create something that looks crazy like this.
[4:14] Now, before we move into the next process, what I wanted to point out is one button that we're not going to check yet because I want to illustrate what exactly this is doing.
[4:24] And that is going to be our sRGB button.
[4:27] Right now you'll notice that it's checked in this image.
[4:30] We're going to leave it that way until we get to our next step.
[4:33] And all of the other ones, it is turned on or turned off depending on what the image is and how it interpreted the image.
[4:40] So since it interpreted this as a normal map, it automatically turned that off.
[4:45] But if we look at our Albedo, it's on and our RMA, it's on.
[4:49] So we'll come back to this here in a second after we set up our materials back here in our materials folder.
[4:56] This is where I'm going to want all of our materials to reside.
[4:59] Now, when it comes to unreal, one of the important things that you're going to want to do is you're going to want to create a master material.
[5:06] So what that is is that's going to be a material where you're going to create all of your parameters inside of and then from there, we're going to create a child of that material.
[5:16] So anytime you update the master material, all of the children are going to get that same information applied to it.
[5:22] So to do that, we're going to come up here to our material button.
[5:26] We'll click that and we're going to just name this character base material underscore M for master.
[5:37] And you'll see now we have a material.
[5:39] We have that little icon in the left hand corner.
[5:41] If you don't want to right click this and save it, you could also open up the window like this and you can hit this button up here to save this asset.
[5:51] Now, once you've opened up your material, you're going to be prompted with something that looks like this.
[5:56] This is going to be our basic blueprint of piping things in.
[6:00] Now, if you want to, you could just go about doing this very simply, which is not the way that I'm going to do it, but just to illustrate.
[6:08] You can come to our content and then our textures.
[6:13] And you could just drag and drop this image in here and then pipe it in.
[6:18] I'm not going to do that just because I want to start from a fresh canvas and I don't necessarily want to have this information in here.
[6:26] So what we're going to do is we're going to delete that in on our keyboard.
[6:30] We're going to hit tab and it's going to bring up this search window.
[6:33] We'll look for texture sampler.
[6:38] And you'll see right here, we have this texture sample.
[6:42] You do have a bunch of other parameters as well that you can add to this.
[6:46] We'll just go ahead and start with a normal texture sample right off the bat.
[6:50] So you'll see that the texture is already assigned here.
[6:53] I don't necessarily want that.
[6:55] I kind of just want something generic.
[6:57] Because we loaded the starter content for this project, we're going to be loaded with a bunch of different images that you can just start with.
[7:05] So I'm going to assign this 127 gray as my texture sample base color.
[7:11] So what we're going to do is we're going to pipe this in.
[7:13] So we will just drag this RGB directly into our base color and you'll see that we are getting some color on our material, which is great.
[7:22] That's exactly what we want.
[7:23] Now, the next one that we're going to bring in is we're going to do our normal map, which we will do a texture sample for that as well.
[7:34] So we will just duplicate this because we're going to need three of them.
[7:38] So we'll copy that, paste another one.
[7:41] And this one we're going to use as our normal map.
[7:45] So we will just drag this RGB into our normal and you'll notice things look kind of funny.
[7:52] That's because this isn't being read as a normal map.
[7:55] So we will come down here and find a normal in here to assign to it.
[8:01] So we're going to do this base flatten normal.
[8:03] So like that.
[8:04] And one thing to keep in mind that's happening is like I mentioned at the beginning, this normal map is being brought in and interpreted as a normal map.
[8:13] Same thing is happening when I'm piping in this texture.
[8:16] You'll see here, this texture sampler switch to normal map versus up here.
[8:21] It was on linear color.
[8:22] So that is going to distinguish between the two of them, what it's being read as by the material.
[8:29] So next from here, we're going to deal with our RMA texture.
[8:33] Now, this is where things get a little bit tricky is we had three separate channels.
[8:38] We had our RG and B channel, each one corresponding to a different texture map.
[8:43] So that's how we're going to pipe it in into our material.
[8:47] So we'll drag this up here.
[8:48] So this is our roughness channel.
[8:50] So we'll find our roughness, pipe that in there.
[8:53] Our G is going to go up here into metallic and our B is going to go into ambient occlusion.
[9:01] Now you can see our ball looks a little bit different.
[9:04] It's it's got some roughness going on.
[9:06] It's got some shininess going on.
[9:07] And that's kind of what we want.
[9:09] So we'll just make one last change here, which is going to be to change this to a flat color.
[9:17] So we will do something like this.
[9:19] And once I save this, I know that this is probably going to have some issues and it's not going to look exactly like we want it to.
[9:27] We're going to have to do a couple of other steps in order to bring this to a place where we can actually start to use it.
[9:33] So let's save that and we will close this and then come to our content browser again.
[9:41] And we can come to our materials.
[9:43] And as I mentioned, our master material is going to be the parent.
[9:48] And what we're going to do from here is split off a child of our master material so that we can start assigning to our model.
[9:56] So let's right click on here and we're going to create a material instance.
[10:00] So what this material instance is going to be is this is going to be an instance of the parent that's going to only have a couple of slots to plug things in inside of our material.
[10:11] So let's go ahead and name this.
[10:12] We'll name this armor plates underscore M.I. for material instance.
[10:20] So we're going to have to create a couple of different instances, but we'll just open this up first before we do anything.
[10:25] Opening up our material, it doesn't really look like much.
[10:29] We don't have the access or ability to really slot any of our textures in.
[10:34] That is because we didn't give that functionality in our master material.
[10:38] So that's what we're going to do next.
[10:40] We're going to come back in here and we're going to right click on all of our texture samples and we're going to go to convert to parameter.
[10:47] Now what that's going to do, it's going to allow us to name it.
[10:50] So we'll name this color.
[10:55] We'll name this one normal and we will name this one RMA.
[11:06] Now we want to save this and over in our material instance.
[11:11] Now you can see that we have all of this information propagated into our material.
[11:17] So we can come and turn all of these on and what that's going to allow us to do is that's going to allow us to come in and slot in new texture images to our material.
[11:27] So let's do that real quick.
[11:28] So we will put this one here, our normal map in the normal map and then our RMA into our RMA slot.
[11:36] Now if we save that, we should be good to slot that on our character.
[11:43] If we select this model, we could just slot them in right here, but that's only going to be slotted in on this model.
[11:50] I want to make sure that this is consistent and stays this way all the time.
[11:54] So I'm going to come to my meshes folder and I'm going to open this up and then back in my content browser.
[12:00] I'm going to try and figure out which one goes where so it doesn't go on that one.
[12:06] It should go on this one if I memory serves me correctly, which it does.
[12:12] So now we have our first material assigned.
[12:15] There's a couple of issues that are going on with this and I will talk a little bit more about that.
[12:20] But first, let's go ahead and create some other material instances for ourselves so that we can pipe in the rest of our materials.
[12:28] So we'll right click, create a new material instance.
[12:33] We'll name this shirt underscore M I open this come to our textures and we're going to open our window like this so that we can just plug all of this.
[12:50] Information in a little bit easier.
[12:53] We'll drag that in drag our normal and drag our RMA save that.
[13:00] Now we have our second material will create another instance and we're going to name this lapsed underscore M I open this up, enable all of these and plug our RMA.
[13:19] And we're going to add our last set of textures in.
[13:26] So once we have that we're going to come back over to our model reopen this up and we're going to slot in the other materials.
[13:38] So we'll get that assigned and then we'll assign our shirt and then we will save this.
[13:43] Let's close this window real quick.
[13:45] And now you can see in here, all of our models have those materials assigned to them, which is good.
[13:52] That's what we want.
[13:53] We want to be able to come into our content browser and just drag and drop this anywhere that we want and always have the materials assigned to it.
[14:01] So that is good to have this in place.
[14:04] If you take a close look on here, there are a couple of things that you may not necessarily notice.
[14:11] But I noticed because I was the one that authored this model and there are some issues that are standing out to me.
[14:18] The first one is going to be how shiny everything is.
[14:21] So when looking at this model, one thing that stands out to me right away is everything kind of feels like it's wet.
[14:29] Now that isn't supposed to be the way that it's supposed to look.
[14:33] Look, there are, there is supposed to be some material variation going on on this model where the rubber is a little bit more dull.
[14:40] The painted metal isn't quite as shiny.
[14:43] The silver is still pretty shiny.
[14:45] And up here, the down material on the collar has a little bit of shine to it, but not too much.
[14:51] So I noticed that that is an issue.
[14:53] This isn't necessarily the way that I initially intended to author my materials.
[14:58] So what's causing that?
[15:00] Well, as I mentioned earlier, the textures and sRGB are the cause of this.
[15:06] So what we're going to do is we're going to come over to our RMA texture for our first texture set and we are going to uncheck this sRGB button.
[15:17] Now you can see here, especially if we look at the metal, how much that changes the quality of the texture.
[15:24] You can see this looks a little bit more accurate to what you probably expect.
[15:29] And the reason for that is because when the images are first being brought in with sRGB turned on, it's interpreting the information from those images as if they are an sRGB export from whichever texturing software that you export them from.
[15:45] When I export my textures, I'm exporting them out as linear images.
[15:49] So that's how they need to be interpreted.
[15:51] If I don't have them interpreted that way, it's going to compress down all of the information.
[15:56] It's going to take the curve on our image and make adjustments to it in order to interpret it as sRGB.
[16:03] So this is one of those things that's a little bit of a caveat when using Unreal is you have to know this because if not, you'll probably just bring your character model in here, apply your materials, and you'll notice that things kind of look off.
[16:18] So that's going to be something we're going to do for all of just these RMA images.
[16:23] And again, this is purely because these are black and white linear images, and that's how they're supposed to be interpreted, not as sRGB images.
[16:31] So we will turn that off and you can see the effect it has on our flaps makes them just a little bit less shiny.
[16:41] And then we will also do it on our last image, which is going to be the shirt.
[16:49] And you can see our rubber now looks a little bit more like rubber and less shiny, and it has more of that material read that we're expecting from it.
[17:00] So now we have our materials set up, we have our texture set up, so we'll just save these so that next time we open them, they are working as intended.
[17:15] The last thing that I wanted to mention is that if you by some chance are working in substance painter or marmoset and you export out your normal maps, one of the common issues that I do see people kind of fall into is them bringing in their normal map and their normal map facing the incorrect way and how it's interpreting that.
[17:35] So if that's something that you are dealing with, you can come inside of your image as well for your normal map and you can adjust that by flipping your green channel.
[17:44] So coming down here to our texture tab and opening that up, you will see this flip green channel.
[17:51] If I flip this, you'll see that our image actually is working incorrectly.
[17:55] It looks as though like the bevels on the corner are lighting and properly up here.
[18:01] There's this shadowing that's happening when in reality this is being hit by light from above.
[18:06] So it shouldn't look that way.
[18:08] So we'll want to make sure that if we see any weirdness going on with our model that we just check our normal map to ensure that everything is rendering properly.
[18:18] Now that's the way to get your textures and your materials in here and just some of the quirks and nuances to check for in order to make sure that things are being read the way that they are intended to when you bring your textures and assign them to your materials inside of Unreal.
[18:34] Now the last thing that I wanted to mention is one of the great things about Unreal is we have a lot of flexibility here with this master material.
[18:42] So if we really wanted to do more, we could come in here and slot different things in here to give us more control.
[18:49] We could even slot in consistent number values in order to play with different parameters.
[18:56] So if we wanted to create just a consistent color for this and not be able to pipe in our texture image, that is something that we could do as well.
[19:04] Same thing with metallic or roughness or any of these channels.
[19:07] So there's a lot of flexibility and that's what's so powerful about Unreal is it allows you to really kind of hit bash a lot of different elements together in order to get something really powerful and complex.
[19:20] So hopefully you found this helpful.
[19:22] Next time we'll be talking about setting up our scene as well as lights and getting things rendered out.
[19:28] So make sure to follow and subscribe.
[19:30] I'll see you guys in the next one.
[19:31] Okay, bye.



---

## Captured Frames

- [3:23] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_000.jpg
- [6:00] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_001.jpg
- [8:53] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_002.jpg
- [10:47] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_003.jpg
- [15:17] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_004.jpg
- [17:44] tutorials/frames/unreal-engine-5-for-character-artists-tutorial-texture-materials/frame_005.jpg

---

## Structured Notes

### Core Technique
A production-standard Unreal texture/material pipeline for a character asset: import textures with correct compression settings (Normal Map vs. Default, and the sRGB-vs-linear caveat for packed maps), build a parameterized **Master Material** with a channel-packed RMA (Roughness/Metallic/AO) texture sample, then spin off multiple lightweight **Material Instances** from it — one per surface/material group — so every future placement of the model automatically carries the correct materials.

### Summary
Continues directly from Part 1 (model already imported). A Textures subfolder is added to the project's content structure, and all texture files for the asset are imported at once via right-click → Import in the Content Browser. Unreal auto-detects some images as Normal Maps based on their content and sets their **Compression Setting** to Normal Map automatically (as opposed to the Default compression setting used for color/data maps) — this is called out as generally correct behavior, but worth verifying per-image. Unsaved imported assets show a small asterisk/star indicator in the corner; select all and right-click → Save to persist them to disk. The video's asset uses **RMA packed textures** (Roughness in the Red channel, Metalness in Green, Ambient Occlusion in Blue, with Alpha available but unused here) — demonstrated by toggling individual channel visibility in the texture viewer to isolate each grayscale map before recombining. A **Master Material** ("CharacterBaseMaterial_M" convention, suffixed `_M` for Master) is created in the Materials folder as the single place all shared parameters live; any later Master Material edit propagates to every child instance. Rather than dragging texture assets directly into the material graph (which would hardcode them), each map slot is built from a generic **Texture Sample** node (Tab → search "Texture Sample") with a neutral default texture (Starter Content's "127 gray") — one Texture Sample for Base Color (RGB output → Base Color input), one for Normal (RGB output → Normal input, with its texture's own Compression Setting confirmed as Normal Map — note the node itself displays "Normal Map" vs. "Linear Color" depending on what its assigned texture's compression is set to), and one for the packed RMA map, whose **R/G/B channels are split out individually** and piped to Roughness (R), Metallic (G), and Ambient Occlusion (B) respectively — plus a flat-color Specular input added manually. Each of the three Texture Sample nodes is then right-click → **Convert to Parameter** and named (Color, Normal, RMA) so they become exposed, swappable slots on any child instance — a Master Material's Texture Sample nodes are NOT swappable from a child instance unless explicitly parameterized this way. From the Materials folder, right-click → **Create Material Instance** spins off a child (naming convention `_MI` for Material Instance, e.g. "ArmorPlates_MI") per distinct surface/material group on the model (armor plates, shirt, straps, etc. — repeated per group); opening an instance shows checkboxes to enable each parameter and slot in that group's specific Color/Normal/RMA textures. Materials are assigned **on the Static Mesh asset itself** (open the mesh in the Static Mesh Editor and assign per Material Slot), not on a placed instance in the level — since asset-level assignment persists for every future drag-and-drop of that mesh into any scene, while level-instance assignment only affects that one placed copy. **Critical gotcha #1 — sRGB on packed data maps:** the model initially reads as uniformly "wet"/over-shiny because the RMA (and other non-color, linear-data) textures were imported with **sRGB enabled** by default; since these packed maps are exported as linear data (not gamma-corrected color), leaving sRGB checked causes Unreal to misinterpret/compress the value curve. Fix: open each RMA (and any other linear/data map) texture asset and **uncheck the sRGB checkbox** — immediately corrects material response (e.g. metal reads properly matte/reflective instead of uniformly glossy). Save after fixing. Note: sRGB should stay ON for genuine color maps like Albedo. **Critical gotcha #2 — inverted normal maps:** normal maps exported from Substance Painter or Marmoset sometimes read with incorrect Y-orientation, producing inverted-looking shading (bevels appear to catch shadow where they should catch light, or vice versa) — fixed per-texture via the texture asset's Texture tab → **Flip Green Channel** checkbox. The video closes by noting the Master Material's flexibility extends further: any input (color, roughness, metallic, etc.) can alternatively be wired to a plain constant/parameter value instead of a Texture Sample, for materials that don't need texture-driven variation at all.

### Key Steps
1. Add a Textures subfolder inside the project's asset folder structure; right-click → Import to bring in all of the character's texture files at once.
2. Review each imported texture's **Compression Setting**: confirm true normal maps were auto-detected and set to "Normal Map," and that color/data maps stayed on the Default compression setting; select all newly imported assets and Save (watch for the unsaved-asset asterisk indicator).
3. For channel-packed textures (e.g. RMA: Roughness=R, Metalness=G, AO=B, optionally Alpha), verify the packing by toggling individual RGB channel visibility in the texture asset viewer.
4. Create a Master Material in the Materials folder (e.g. `CharacterBaseMaterial_M`).
5. Build the graph from generic **Texture Sample** nodes (Tab → "Texture Sample") assigned a neutral placeholder texture (e.g. Starter Content's 127 gray) rather than dragging in real texture assets directly: one for Base Color (RGB → Base Color), one for Normal (RGB → Normal, confirm its assigned texture reads as "Normal Map" not "Linear Color" in the node), and one for the packed RMA map (split R → Roughness, G → Metallic, B → Ambient Occlusion); add a flat Specular value manually.
6. Right-click each of the three Texture Sample nodes → **Convert to Parameter**, naming them (e.g. Color, Normal, RMA) so they become swappable on child instances. Save the Master Material.
7. In the Materials folder, right-click → **Create Material Instance** for each distinct surface/material group on the model (naming convention `_MI`); open each instance, enable the exposed parameters, and slot in that group's specific Color/Normal/RMA textures.
8. Open the target Static Mesh asset (not a level instance) and assign each Material Instance to its correct Material Slot, so the assignment persists for every future placement of that mesh.
9. If the shaded result looks uniformly too glossy/"wet": open the RMA (and any other linear/data) texture assets and **uncheck sRGB** — leave sRGB checked only on true color maps (e.g. Albedo).
10. If normal-mapped surface shading looks inverted (light/shadow reversed on bevels): open the normal map texture asset → Texture tab → toggle **Flip Green Channel**.
11. Save all edited textures and materials so changes persist on next project open.

### UE Systems / Blueprints / Settings
- Texture asset: Compression Setting (Default vs. Normal Map), sRGB checkbox, Texture tab → Flip Green Channel
- Material Editor: Texture Sample node (Tab-search), RGB channel split-out (R/G/B pins), Convert to Parameter (right-click)
- Master Material (`_M` suffix convention) vs. Material Instance (`_MI` suffix convention, Create Material Instance from right-click)
- Material inputs used: Base Color, Normal, Roughness, Metallic, Ambient Occlusion, Specular
- Static Mesh Editor: per-slot material assignment (asset-level, persists across all future placements) vs. level-instance assignment (does not persist)
- RMA channel-packing convention: R=Roughness, G=Metalness, B=Ambient Occlusion, Alpha=free/unused here

### Difficulty
Intermediate (assumes the Part 1 groundwork; introduces real production concepts — parameterized master materials, channel-packed textures, and the sRGB/linear-data distinction — that go beyond pure beginner content)

### UE Version
5.3.2 (direct continuation of Part 1's project; not restated verbally in this episode).

### Tags
materials, pbr, textures, pipeline, intermediate, ue5-3

---

## Related Entries
Part of Jared Chavez's "UE5 for Character Artists" series — this is Part 2, texture/material setup.
- [UNREAL ENGINE 5 FOR CHARACTER ARTISTS | Tutorial | Getting Started](unreal-engine-5-for-character-artists-tutorial-getting-started.md) — same series, Part 1: covers the FBX import (Combine Meshes + Do Not Create Material) that produces the empty Material Slots this episode fills in.
