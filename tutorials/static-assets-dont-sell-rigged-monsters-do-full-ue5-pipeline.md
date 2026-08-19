---
title: Static Assets Don't Sell. Rigged Monsters Do. (Full UE5 Pipeline)
source: YouTube
url: https://www.youtube.com/watch?v=IUyufiqS3RE
author: Andrew Vish
ingested: 2026-08-19
ue_version: "UE5.3"
tags: [rigging, skinning, blender, epic-skeleton, twist-bones, control-rig, ik-rig, retargeter, foot-roll, curve-editor, physics-asset, post-process-deformation, lods, marketplace, fab, character-pipeline, advanced, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Static Assets Don't Sell. Rigged Monsters Do. (Full UE5 Pipeline)

**Source:** [YouTube](https://www.youtube.com/watch?v=IUyufiqS3RE)
**Author:** Andrew Vish
**Duration:** 26m49s | 15 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Asset Sales under the Professional License [0:00]
**Transcript (timestamped):**
[0:00] So I uploaded these monsters to Fab and I already have sales. And here's the interesting part.
[0:06] Half of them wear professional licenses. What that is, I'll tell you in a bit. You know,
[0:11] game developers don't buy cheap static meshes. I mean, they do buy, but for now they can get
[0:18] them for free. They also buy assets with real value, assets that work out of the box and save
[0:24] their time. And what makes this monster ready is not the static mesh. It's everything that happens
[0:31] after the model is done. Rigging, skinning, Epic Skeleton conversion, animations, basic slots,
[0:38] a full Unreal Engine project set up. And you know, this is the part of the pipeline almost
[0:44] nobody shows. Skinning and rigging still remain a mystery. There is barely any public material that
[0:51] explains what actually works. Most 3D artists make just static meshes because it's easier. And
[0:57] that's exactly why this niche has so few competitors. My main niche is clothing for
[1:04] metahuman, over 800 assets generating passive income for me every single month. Monsters are
[1:11] my second niche. Same platform, same principle, high entry barrier and readymade solutions.
[1:17] In this video, I'll show you my pipeline, how to take a finished monster model and turn it into
[1:23] a market ready product. From static mesh to the fab upload. But fair warning, this is an advanced
[1:30] level pipeline. I won't be explaining the basics at every step. Otherwise, this video would turn
[1:36] into a 10 hour marathon. But even if you are not there yet, watch it once and you will understand
[1:42] why these assets sell and why AI services trying to sell you all to rigging with the promise of a
[1:49] game ready character are simply lying to you. Why they are lying, you'll see at the skinning stage.


### Creating an Unreal Engine Project [1:56]
**Transcript (timestamped):**
[1:56] So we start by creating a clean Unreal Engine project on version 5.3. So the presentation
[2:02] will use the basic version of the scene with default lighting settings. From the template,
[2:08] we'll pick a few animation assets that we'll need to later on from calibrating the skinning.
[2:15] In Blender, we import the mannequin and create a separate collection for it. And this mannequin
[2:22] will serve as a reference. The benchmark will build our monster's rig against. After that,
[2:29] we import the animation assets we pulled out of Unreal Engine and we'll set those assets up. So
[2:35] they will work properly on the imported mannequin, which further down the line will let us verify
[2:43] that our monster's rig is correct. And I begin constructing the monster's skeleton itself from


### Rigging in Blender [2:45]
**Transcript (timestamped):**
[2:49] scratch. And here you might ask, where exactly am I supposed to put this or that bone? And the
[2:57] underlying principle is that although the skeleton isn't an exact match for an anatomical skeleton,
[3:04] we can still use knowledge of anatomy to build a genuinely effective rig. And believe me,
[3:11] creating a functional high quality rig is far simpler than it might seem at first glance.
[3:17] So we build the bone structure for controlling the lower limbs step by step, make it symmetrical,
[3:24] and then move on to the upper limb. And the upper limbs are what most often expose the quality of
[3:30] a rig during animation. Real anatomy matters here too, but 3D rig has its own nuances.
[3:37] After laying out the clavicles, we can move on to the shoulder. As before, we pay attention to the
[3:44] position of the shoulder joint and reproduce the main bone structure of the upper limb. And believe
[3:51] me, there are plenty of nuances here that you simply can't ignore. As with the lower limbs,
[3:58] we use the symmetrized tools and move on to building the bone structure for the fingers
[4:04] and the toes as well. It's a fairly delicate process that takes a lot of patience. And we
[4:10] can roughly assess whether the skeleton is built correctly even before the skinning stage.
[4:15] For example, by trying to curl the fingers into your fist. And the next stage is skinning. As a


### Skinning in Blender [4:19]
**Transcript (timestamped):**
[4:21] base, we use the automatic weights generated by Blender's algorithm. Of course, it's not that
[4:28] simple. And there are a lot of nuances to keep in mind here. And one of the best available tools
[4:34] in this case is Smooth, which sometimes works real magic. Personally, I don't like painting weights
[4:42] by hand, but sometimes it's practically the only way to get the deformations you want. For instance,
[4:50] here I want the clavicles to be less dependent on head and neck movement,
[4:56] with the main deformation load staying within the leg. But you shouldn't allow an abrupt cutoff
[5:02] of influence either. Areas next to large joints always demand special attention. So in this case,
[5:09] I find the humerus's influence on the adjacent body area to be pronounced. And there's almost
[5:16] always room for extra smooth iterations under the armpits. And following the same logic,
[5:23] I keep improving the skinning in other areas of the body. I immediately move and check every
[5:30] joint to make sure the deformations look right. In this case, you can even use a few tricks with
[5:36] the mirror modifier while doing the skinning, just to save time. And it's very important to
[5:43] understand how twist bones work, what functions they perform, and what the nuances of working with
[5:50] them are. And of course, we integrate them into our monster skeleton for all limbs. This is a
[5:58] fairly important and significant process. And there is no point in rushing in it. There are plenty
[6:04] of small nuances. But believe me, they play a big role. Adding twist bones to the skeleton structure
[6:10] requires uploading the skinning profile for their limbs. So I do this on separated parts of the mesh,
[6:17] so I can safely and non-destructively apply the update to the limbs first, and then integrate
[6:24] them back into the original mesh. All of these steps can be done in vanilla blender with no
[6:30] extra add-ons or dependencies. This is a method that delivers reliable results and has been proven
[6:36] on many assets. We can physically stitch them back onto the body of our monster, or rather onto
[6:44] its copy. Select and merge the border loops, which lets the vertex weights from different body areas
[6:50] blend together organically. And now we have everything we need to do a proper twist correction
[6:56] based on the bones we added, together with their skinning. This is the groundwork for the later
[7:03] implementation in the Unreal Engine project. This, and many other things, is what goes on behind the
[7:10] scenes of a truly great skinning result. And you know, this is probably one of the most important
[7:16] stages. And rest assured that the techniques I'm showing here, topic of skinning in general,
[7:23] largely remain a mystery to this day. But even with excellent skinning and great skeleton,


### Bone Orientation & Epic Skeleton [7:25]
**Transcript (timestamped):**
[7:29] we still can't just export it from Blender to Unreal Engine and expect everything to work perfectly.
[7:36] You've probably noticed that the skeleton belonging to the mannequins looks rather strange in Blender.
[7:42] And that's not without reason. In theory, of course, we can use Blender style bone orientation
[7:49] in an Unreal Engine project. But believe me, there are plenty of reasons not to. So in short,
[7:57] the next stage is converting the skeleton to the epic skeleton format. And this is the stage that
[8:02] doesn't forgive carelessness. So basically, we have to reproduce roughly the same bone orientation
[8:10] the mannequin has. And of course, this applies to every single bone in the skeleton. The upper
[8:17] limbs, including the twist bones, and of course, the lower limbs with their corresponding bones.
[8:22] And there are a lot of different things and nuances. And now in Blender, we can evaluate
[8:29] whether our bones are oriented correctly by using the template animations we imported earlier.
[8:35] The result can look painful if a bone is oriented incorrectly. And of course, besides the bones
[8:43] that directly drive deformation, we should also take care of other bones that serve utility
[8:49] functions, such as IK bones, which are the foundation for many important mechanics in
[8:55] Unreal Engine. So now, after the whole series of validations, checks and fixes, I can finally move
[9:02] on to exporting the skeleton and the skeleton mesh into Unreal Engine. Now we can head back to our


### Unreal Engine Setup [9:07]
**Transcript (timestamped):**
[9:09] native environment on Unreal Engine. And I start the work by setting up the basic folder structure
[9:16] that will hold our main assets. Next, we want to import in the skeleton mesh itself. And so that


### Material Setup in Unreal Engine [9:22]
**Transcript (timestamped):**
[9:23] it doesn't look set in gray, we need to create a material for it. So we do that in the corresponding
[9:29] subfolder. This is the base material. For the skeleton mesh, we'll be using an instance for it.
[9:36] We add a node for the base color. We've added the other nodes for the remaining textures.
[9:43] Then we created a material instance, loaded the textures we need, set up their attributes,
[9:49] and applied them into the instance we created. Now our monster looks interesting, maybe even a
[9:56] little handsome. And we move on to the next stage. Since Unreal Engine is a game engine, we want to


### Character Blueprint Setup in Unreal Engine [9:59]
**Transcript (timestamped):**
[10:02] be able to play as our monster. And this stage is about setting up the character blueprint. And if
[10:09] you think we can just get away with swapping the mannequin skeleton mesh for our monster here,
[10:15] the result may be a bit depressing. We add a little magic in the skeleton mesh settings.
[10:21] And while it's not exactly marked ready yet, at least it doesn't hurt your eyes as much.


### Animation Assets in Unreal Engine [10:28]
**Transcript (timestamped):**
[10:28] And the next big stage is about how we can set up the animation assets so they look correct
[10:34] on our monster. And on top of that, emphasize his aggressive beastly nature. As a base, we'll of
[10:41] course be using the assets that belong to the mannequins from the template. Besides that,
[10:48] the end product going to the marketplace has to be original and self-contained,
[10:53] with no external dependencies. So the next step is to copy the animation assets from the template
[11:01] into our own folder and make them depend on our monster skeleton. But this probably won't work.
[11:11] If it were all that simple, that might not be any need to record a video like this. Of course,
[11:18] there's another way that gives a much better result. Now this is starting to look like something I'd
[11:24] want to see. And do we really have to repeat all of that for every single animation? Is there really
[11:32] no other way? Of course there is. Although it's still useful to know the basic method of transferring
[11:39] animations. But the other more recommended approach is using a retargeter based on IK rigs. Now that
[11:47] I've set up the IK rig, I can build a retargeter on top of it, which lets me transfer animation
[11:54] assets from one mesh to another conveniently and with far more control. And of course, even at this
[12:01] stage I can start doing some basic sculpting of the animation so it looks more organic. But even
[12:08] here Unreal Engine plays a dirty trick on us. Because some animations, locomotions specifically,
[12:15] give a pretty questionable result. Still, no reason to despair. We can deal with this and
[12:21] end up with excellent animation assets. One way or another, by the end of this stage, you and I
[12:27] will have animation assets that are local to the Monster's project. And of course, I'll go through
[12:33] them and polish them up. Another typical asset we use in all our projects is the preview blueprint.


### Preview Blueprint in Unreal Engine [12:36]
**Transcript (timestamped):**
[12:41] Its main role is to present our monster as non-playable character. But at the same time,
[12:48] it's also a handy way to calibrate questionable skin and animations. I place instances of this
[12:55] blueprint around the scene and then assign specific animations to each of them individually.
[13:01] Now our monster won't be so bored. He's got some buddies in this cruel world. And we move on.
[13:08] And the next module is about creating and setting up the control rig. I should say right away that
[13:14] we won't be building control rig completely from scratch. We'll use the ready-made control rig
[13:20] from the mannequin template. After that, that's exactly why it's there. But believe me, it's
[13:26] not as simple as it might seem at first glance. The control rig is a fairly complex thing,
[13:33] in one that doesn't always work reliably. That said, setting it up is definitely worth the end
[13:40] result. And then we can move on to integration the control rig with our monster. I start that work
[13:47] by stripping the control rig of the extra controllers our monster doesn't have. And that applies not
[13:53] only to the controller hierarchy, but also to certain parts of the node graph. Next, since this
[14:00] project is commercial and will be distributed on the marketplace, we should make sure the controller
[14:06] shapes are visually accessible and controllable to use. So we go through all the main controllers
[14:13] one by one and fix up their appearance. There are several ways to achieve the result you want here.
[14:20] And the main thing is not to forget to hit save and compile often. So now I'm wrapping up the
[14:27] setup of the upper body controllers and moving on to set up the lower body controllers one by one.
[14:34] In places, I allow myself a bit of artistic deviation from the standard. For example,
[14:41] here I think our horseshoe shape widget will fit better. And of course, I don't forget the
[14:49] opposite side of the limbs. As for the IK controllers of the lower limbs, there are certain nuances
[14:56] that cost me quite a bit of blood back in the day. Mainly, it comes down to the fact that
[15:02] the foot roll mechanism is implemented in a fairly complicated way, but it's very nature.
[15:09] Plus, there are certain bugs in the controller itself. Also, we somehow need to set up the
[15:16] transforms for the heel and t-bones, which physically don't exist in our skeleton, but
[15:22] are required for the foot roll mechanics to work. So we do this using temporary controllers that act
[15:30] as a sort of transform buffer. I place this controller where the heel bone should be.
[15:36] Then I create a child controller that will act as a nominal t-bone and carefully nudge it to
[15:44] where I'd want the real t-bone to be. That leads to the contact point of the front surface of the
[15:51] foot. I know, guys, it might seem complicated, but this is exactly what gives you the opportunity
[15:57] to actually earn money on marketplaces. So next, we transfer our t-bones and heel bones onto the
[16:03] controllers, use a bit of symmetry magic, and we get a working foot roll mechanism. Although,
[16:11] it's a little short on aesthetics, let's do it like this. Yeah, it's better, I think. Of course,
[16:19] this still isn't the perfect version, but we can do better. I'll play with the scale a bit,
[16:25] tweak the locations a little, and now the controller looks market ready. And at this point,
[16:32] I got the arch to check whether this rig works with a real animation. And it works. Of course,
[16:39] this is far from everything. The fingers, for example, still need more work, and there are a
[16:46] few other details to fix. But now we have a solid foundation for processing animation assets. Okay,


### Fixing Animations & Curve Editor in Unreal Engine [16:53]
**Transcript (timestamped):**
[16:54] now we have a tool that lets us work with animation assets right inside Unreal Engine.
[17:00] And our main task here is first, to fix the flaws in the existing animations. And second,
[17:08] to give them a character that fits this monster better, to make the movements more predatory
[17:14] and aggressive. We can do that by baking the animation onto the control rig. There's quite a
[17:20] large number of ways to fix an existing animation using the control rig. Working in the curve editor
[17:26] is one of my favorite methods. This approach can turn out to be fairly difficult, especially for
[17:34] anyone who has never used this tool before. But with a bit of practice and my tips, you won't be
[17:42] able to imagine working comfortably with animations without it. And my main task here is to make the
[17:49] feet stay planted firmly on the ground, remove small noise and jitter, and clean up unnecessary keys.
[17:57] Now that we've locked the feet firmly to the ground, we can lower the body a little so the monster
[18:04] stays nice and squat. And obviously, the arm position is grating on my eyes right now,
[18:12] and probably yours too. And that's just as easy to fix without breaking the tempo and character
[18:18] of the animation using the curve editor. And as a result, we get an idle animation that's free
[18:24] of retargeting flaws and has the correct pose. Next, we can move on to editing the following
[18:32] animation. In our case, that will be fall loop. For each animation from the template, I'll try to
[18:38] demonstrate different techniques so that you can end up with a whole toolkit to use while working on
[18:45] your own projects. For example, here we'll work directly with the keys in the sequence track.
[18:52] That's also a valid and sometimes quite convenient way of editing animations. But even so, curve editing
[18:59] remains the surgical scalpel, which lets you dystic finish animations effectively. And now our monster
[19:06] knows how to fall beautifully. And as we all know, if you want to learn to fly, you first have to know
[19:13] how to fall. Let's move on. So I don't think there is much point in going into detail right now
[19:19] about the techniques and mechanics I use to edit the animations that follow. It's an active iterative
[19:26] process. And you have to keep in mind that sometimes there is simply no easy elegant solution that's
[19:34] instantly fixes an animation's flaws. You'll have to spend a certain amount of time manually
[19:40] editing almost every single frame to get a decent result. So by editing animations isn't the only


### IK Mechanics [19:45]
**Transcript (timestamped):**
[19:46] job we have to do. We also need to make sure that IK mechanics work as before we'll draw inspiration
[19:54] from the assets in the third person template. The Unreal Engine developers have thoughtfully left
[19:59] us a dedicated control rig here, which fits our needs perfectly. All that's left for us to do is
[20:06] update the skeletal mesh to our monster and accordingly swap the reference to the updated
[20:13] version of control rig in the corresponding node of the animation blueprint. And I'll have to disappoint
[20:19] you if you thought that was all there is to it. Because for this system to work, we need to edit
[20:26] our animations one more time. In short, the problem right now is that the IK bones don't take part in
[20:34] the animations. This can be fixed in various ways, using Blender for instance, but I'm going to
[20:41] suggest a slightly different approach, which uses a small control rig right inside Unreal Engine to
[20:48] solve the problem. All that's left now is to go through all the animations again and rebake them
[20:54] so that the IK bones follow the movements of the corresponding bones from the main skeleton exactly.
[21:02] It's really not that much work compared to the previous animation edit in stage,
[21:07] but the result is definitely worth it. Another important asset, one without which we can't


### Physics Asset in Unreal Engine [21:09]
**Transcript (timestamped):**
[21:12] publish the project on the marketplace, is the physics asset. Every skeleton mesh in the project
[21:19] has to have a corresponding physics asset. And here too, we could have used the readymade solution
[21:25] from the mannequin, but I want to build this asset completely from scratch. Although automatic
[21:31] generation still leaves a lot to be desired. I get rid of the obviously unnecessary physics
[21:38] primitives, as well as the primitives on the right side of the body. Then we work through the remaining
[21:44] primitives in detail. For example, we align them and adjust them so their volume covers the geometry
[21:52] of our monster's body as fully as possible. For some body parts, I prefer boxes over capsules.
[22:00] I carefully adjust the newly created primitive so that it covers, in this case, the hand specifically.
[22:07] Now that I have a satisfactory result for the body and the left limbs, I can mirror the primitives
[22:15] over to the right limbs. Even though it looks correct at first glance, don't be fooled. Unreal
[22:21] Engine won't let you get an acceptable result right away. So the next step is setting up the
[22:27] constraints. And I start by simply deleting the existing constraints, keeping only the ones in the
[22:35] central part of the body. Then one by one. I start dialing in limit values so that the behavior of
[22:42] each limb, or in this case, the head gives an organic realistic result during the simulation.
[22:50] I assign the constraints to the limbs manually, stepping from the child element of the hierarchy
[22:56] up to the parent. And I tune their parameters the same way, relying mostly on my own intuition and,
[23:04] of course, on the behavior I get from the simulations. So now we can check how the whole
[23:10] limb is going to behave during simulation. So in my opinion, it looks pretty good here.
[23:17] We'll get rid of the overlap with the body of a bit later, of course. Using mirroring,
[23:23] I reproduce the constraints on the symmetrical half. But it's not that simple. Unreal Engine
[23:30] keeps dropping stones into our boots here too. We quickly set up all the necessary constraints
[23:36] for the left lower limb, following the example of the left arm. We tune their parameters and
[23:44] test how the physics looks. Don't pay attention to the foot for now. I'll set that up later.
[23:51] And finally, the moment of truth, the drop test. So the monster seems to fall satisfactory,
[23:59] but there's a certain flow here. We need to make sure the limbs and the body don't overlap with
[24:06] each other. So I go through the different groups of primitives, enabling and disabling collision
[24:12] where is needed and where it isn't. And I keep testing this work over and over.
[24:18] A strange pose like this one is the result of a couple of primitives intersecting somewhere.
[24:25] Or you get a case where instead of lying calmly on the ground, the monster starts sliding off
[24:31] somewhere or performing wild breakdowns moves. And once we fix all of these flows, we now have
[24:38] a physics asset that falls absolutely correctly. We assign it as an attribute of the skeletal mesh
[24:45] itself. And next, you and I will create an animation blueprint that will be used to handle


### Post-Process Deformation in Unreal Engine [24:46]
**Transcript (timestamped):**
[24:51] post-processing deformations. For it to work correctly, we'll need one more control rig,
[24:58] one that contains the calculation from the twist correction. And I'll do a bit of cleanup here,
[25:06] get rid of the nodes that make no sense for our skeletal mesh and tidy things up a little for
[25:13] purely aesthetic reasons. Then in the animation blueprint, we need to do a literally basic setup
[25:20] that takes the input pose and connects it through the control rig to the output pose. The control
[25:28] rig here is the very asset we were setting up just a moment ago. And now I need to verify that what
[25:35] we've set up is valid. So I rotate the hand and I see a smooth distribution of the deformation
[25:42] across the forearm. For comparison, take a look at what happens when this isn't working. Okay,


### LODs, Cleanup & Final Steps [25:49]
**Transcript (timestamped):**
[25:49] right, we have literally just a few final steps left. One of them is setting up the LODs. Once
[25:56] again, we'll use the asset that comes with the mannequins as a base. All we'll need to do here
[26:02] is edit the reduction settings a little. Now we have to tell the skeletal mesh itself which LOD
[26:09] it should reference, set the number of LODs and generate them. And this makes our project look
[26:16] more professional. After that, I cleaned the project of any extra files that have already
[26:23] served their purpose. I also don't forget that we need to take several screenshots or renders
[26:30] to present our product on the marketplace. This amended our requirement from the reviewers on
[26:36] FAP. Then I prepared everything for the FAP submission and uploaded the project to FAP.
[26:42] And now I just watched it sell while working on my next project. Join my discord community. See you there!



---

## Captured Frames

- [2:15] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_000.jpg
- [3:17] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_001.jpg
- [4:34] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_002.jpg
- [6:44] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_003.jpg
- [8:29] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_004.jpg
- [9:43] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_005.jpg
- [11:47] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_006.jpg
- [14:13] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_007.jpg
- [15:44] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_008.jpg
- [17:26] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_009.jpg
- [20:48] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_010.jpg
- [22:15] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_011.jpg
- [23:51] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_012.jpg
- [25:35] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_013.jpg
- [26:02] tutorials/frames/static-assets-dont-sell-rigged-monsters-do-full-ue5-pipeline/frame_014.jpg

---

## Structured Notes

### Core Technique
A commercial-marketplace (Fab) character pipeline overview: taking a finished static monster mesh from Blender through custom rigging/skinning, Epic Skeleton conversion, and a full Unreal Engine setup (materials, character blueprint, retargeted + hand-polished animations, Control Rig, physics asset, post-process twist-correction deformation, LODs) to produce a "game-ready" asset that actually works out of the box — contrasted against AI auto-rigging services the author calls out as overselling what they deliver. This is a high-level walkthrough/showcase video, not a step-by-step settings tutorial — most steps are described narratively over B-roll rather than demonstrated with exact values, so treat it as a pipeline map to follow up with dedicated technique tutorials (several are cross-linked below) rather than a standalone how-to.

### Key Steps
**Blender side (rigging & skinning):**
1. Create a clean UE 5.3 project; export a handful of mannequin animation assets from the template.
2. In Blender, import the UE mannequin skeleton as a benchmark/reference the custom rig will be validated against, plus the pulled animation assets.
3. Build the monster's skeleton from scratch, bone by bone — lower limbs first (symmetrized), then upper limbs/clavicles/shoulders (most visible source of rig-quality issues during animation), then fingers/toes. Anatomy knowledge informs bone placement even though the rig isn't an anatomically exact skeleton.
4. Skin using Blender's Automatic Weights as a base, then refine: the Smooth brush handles most cases; hand-painting is reserved for cases automatic weights can't fix (e.g. decoupling clavicle deformation from head/neck movement while keeping leg-area influence dominant). Pay special attention to blending zones near large joints (humerus influence, armpit smoothing) to avoid abrupt influence cutoffs. Mirror modifier tricks speed up symmetric skinning.
5. Add twist bones to all limbs by working on separated/duplicated mesh parts (non-destructive), transferring the updated skinning back, then stitching the parts back onto the main mesh by merging border-loop vertices so weights blend organically across the seam. This groundwork feeds later UE-side twist correction.
6. Convert the custom skeleton's bone orientation to match Epic Skeleton conventions (not Blender-native orientation) for every bone including twist bones and utility/IK bones — validated in Blender by testing the imported template animations against the new rig; misoriented bones produce obviously broken deformation.

**Unreal Engine side:**
7. Set up project folder structure; import the skeletal mesh; build a base Material + Material Instance (base color + supporting texture nodes) so the monster isn't gray.
8. Character Blueprint: swapping in the monster's skeletal mesh directly on the mannequin BP looks broken by default — requires adjusting skeletal mesh component settings to get an acceptable starting result.
9. Animation transfer: naively re-parenting template animation assets to the new skeleton doesn't work well. The recommended method is an **IK Rig + Retargeter** (build an IK Rig on the monster skeleton, then a Retargeter on top) for controlled, higher-quality animation transfer versus the basic/manual transfer method.
10. Build a **Preview Blueprint** — non-playable instances placed around the level, each with a different animation assigned — used both to present the asset and as a live calibration tool for spotting bad skinning/animation.
11. **Control Rig:** start from the mannequin template's ready-made Control Rig rather than building from scratch; strip unused controllers (hierarchy + node graph) that the monster doesn't need; redesign controller shapes for marketplace-grade usability. Foot roll needs manual **heel and toe/t-bone transform buffers** via temporary controllers (since those bones don't physically exist on the custom skeleton) — placed, child-parented, nudged into position, then wired via mirroring to get a working foot-roll mechanism; verified against a real animation.
12. **Animation fixing:** bake existing (retargeted) animations onto the Control Rig and fix them in-engine — primarily via the **Curve Editor** (called out as the most surgical/precise tool) for foot-planting, removing jitter/noise, cleaning redundant keys, and repositioning body/arm poses; the Sequencer track keyframe view is used as a secondary, sometimes more convenient editing method for other clips (e.g. a fall-loop animation). Described as an iterative, manual, frame-by-frame process with no universal shortcut.
13. **IK bones:** the third-person template's dedicated Control Rig is reused for IK setup, retargeted onto the monster mesh and wired into the Anim Blueprint. Because IK bones aren't driven by the base animation data, every animation must be rebaked a second time through a small in-Unreal control rig so IK bones follow their corresponding main-skeleton bones (an alternative to fixing this in Blender).
14. **Physics Asset:** built from scratch rather than reusing the mannequin's (auto-generation is a rough starting point only) — prune unnecessary/duplicate-side primitives, then manually fit remaining primitives to body geometry (boxes preferred over capsules for some parts), mirror left-side primitives to the right. Constraints are deleted and rebuilt manually per-limb (child→parent order), tuning angular limits by intuition + simulation feedback, then mirrored to the symmetric side. Iteratively drop-test the ragdoll, toggling collision between primitive groups to eliminate limb/body interpenetration and pose glitches until the fall result looks physically correct.
15. **Post-process deformation:** a dedicated Control Rig (built earlier for twist correction) is wired into the Anim Blueprint (Input Pose → Control Rig node → Output Pose) to smooth deformation across joints like the forearm during rotation — verified visually against the uncorrected result.
16. **LODs:** reuse the mannequin's LOD asset as a base, tweak reduction settings, assign it as the skeletal mesh's LOD source, set LOD count and generate.
17. **Marketplace prep:** clean up unused project files, capture marketing screenshots/renders (Fab reviewer-required), then submit/upload to Fab.

### UE Systems / Blueprints / Settings
Skeletal Mesh import & Epic Skeleton conventions; Material / Material Instance (base color + texture nodes); Character Blueprint (skeletal mesh component override); IK Rig + IK Retargeter (animation transfer between skeletons); Preview/NPC Blueprint pattern for asset calibration; Control Rig (stripped-down mannequin template CR, custom controller shapes, temporary heel/toe transform-buffer controllers for foot roll, mirroring); Curve Editor and Sequencer keyframe track editing for animation cleanup; a second small in-engine Control Rig for baking IK-bone motion into animations; Physics Asset Editor (primitives, angular constraints, mirroring, ragdoll drop-test iteration, per-group collision toggling); Anim Blueprint (Input Pose → Control Rig → Output Pose wiring for post-process twist-correction deformation); LOD reduction settings/generation; Fab marketplace submission requirements (screenshots/renders, professional license).

### Difficulty
Advanced — explicitly framed by the author as an advanced-level pipeline overview that skips explaining fundamentals at each step ("otherwise this video would turn into a 10 hour marathon"). Best suited to viewers who already know Blender rigging basics and UE's Control Rig/IK Rig systems, using this as a map of the full commercial pipeline rather than a from-scratch lesson.

### UE Version
UE 5.3 (stated explicitly in the transcript at [1:56]).

### Tags
rigging, skinning, blender, epic-skeleton, twist-bones, control-rig, ik-rig, ik-retargeter, foot-roll, curve-editor, physics-asset, ragdoll, post-process-deformation, animation-blueprint, lods, fab-marketplace, character-pipeline, monster-character, advanced, youtube, ue5

---

## Related Entries
- **[Ragdoll Physics are Insanely Easy in Unreal 5](ragdoll-physics-are-insanely-easy-in-unreal-5.md)** — dedicated deep-dive on the Physics Asset Editor's rigid bodies and angular constraints that this video's Physics Asset step (drop-test, per-limb constraint tuning, collision toggling) only summarizes at a high level.
- **[Physics in Unreal Engine (Epic Documentation)](physics-in-unreal-engine.md)** — full physics reference (Rigid Body Dynamics, constraints/joints, Ragdoll) useful for filling in the physics-asset details this video skips.
- **[Build It in Engine: Modern Rigging with Control Rig & Dataflow | Unreal Fest Chicago 2026](build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-.md)** — a fully procedural, in-engine alternative to this video's manual Blender rigging/skinning workflow (Dataflow skeletonization auto-generates skeletons + skin weights); useful contrast on where UE5.8 rigging tooling is headed versus the hand-built Blender approach shown here.
- **[Control Rig in Unreal Engine (Epic Documentation)](control-rig-in-unreal-engine.md)** — official reference for the Control Rig system this video relies on for the character rig, foot-roll controllers, and the post-process twist-correction rig.
