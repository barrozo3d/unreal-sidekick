---
title: Real-World Animation & Rigging Challenges in Production | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=XYMad1EutcA
author: Unreal Engine
ingested: 2026-08-07
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/real-world-animation-rigging-challenges-in-production-unreal-fest-chicago-2026/
frame_count: 0
frame_status: pending-selection
---

# Real-World Animation & Rigging Challenges in Production | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=XYMad1EutcA)
**Author:** Unreal Engine
**Duration:** 50m14s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py real-world-animation-rigging-challenges-in-production-unreal-fest-chicago-2026 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Thanks everyone for joining us for this session about rigging an animation in Unreal.
[0:07] I'm Stéphane, a solution architect at Epic Games, and I'm here to bring solutions, work
[0:14] around tips and tricks around several situations.
[0:19] I faced and I've encountered working with a bunch of different studios, amazing studios,
[0:26] and I wanted to highlight some of them, so I picked a few ones.
[0:34] In addition to rigging and animation challenges, I also wanted to talk about custom tools, because
[0:39] as you probably saw through the title, it's mainly towards pipeline and production, and
[0:48] custom tools in production is kind of a common thing.
[0:52] I wanted to talk about that with a little surprise, about the tool I had changed to
[0:57] work on for a few months, and I wanted to share with you as well.
[1:03] What are the challenges, when, why, how, and the last question is really interesting, why
[1:10] not just reproduce what we're used to doing in the past?
[1:14] That's for the rigging aspect, but mainly for animation.
[1:19] You probably understand why I put that question here, and it will make sense in just a few
[1:25] slides.
[1:27] Let's start right away with rigging challenges, and some of the main topics I wanted to present
[1:32] to you are about skinning, optimization, which is something really important that you're
[1:38] going to see throughout this talk.
[1:42] Down to the modular aspect of control rigging in a production, mostly like working as a
[1:48] team, why it's important and different solutions here with specific videos and step by step,
[1:54] I'm sure it's going to be useful for you.
[1:57] A lot of information during this talk, I'll try to compact everything.
[2:01] If we don't have time for Q&A, don't hesitate, I'll be outside and ready for the wave of
[2:07] questions you may have.
[2:10] So let's start with weight precision.
[2:12] This is something I saw in the past in different situations where you can have a difference
[2:19] between the editor mesh and the render mesh.
[2:24] So you have workaround solution to handle that, meaning that by default, Unreal is handling
[2:32] 8 influences on one vertex, and you can change that through project settings, but also skeletal
[2:41] mesh editor.
[2:43] So if you have more than 8 influences on one vertex, you may end up with this little behavior
[2:52] as I mentioned where during render time, you can have skinning issue or something is happening
[2:58] on the surface of the mesh.
[3:00] So that might be the reason and it's all adjustable through the project settings.
[3:05] So you can have a threshold saying that at a specific moment, you can enable the unlimited
[3:10] bone influence that will help prevent from this situation.
[3:17] It's a bit more visual when you dive into the skeletal machine, because you can see
[3:21] when you select one vertex, the number of influences you have on this specific vertex.
[3:28] So if you have more than 8 at a specific area, and you are visualizing some artifact issue
[3:34] on the render mesh, that's probably why.
[3:37] And you can also use in digital panel the high precision skin weight uses, checkbox story,
[3:45] that uses 16-bit bone weight for the render mesh.
[3:48] So that will allow you to have more influences on your mesh and with the joint and skinning
[3:56] work you may have done on other DCC or in-unware.
[4:00] In 5.8, we have a lot of new things coming with the skeletal mesh editor.
[4:04] And as you can see on the outliner, we have a little lock icon per joint, which allows
[4:12] you to lock joints and weights, which is a really great add for all the auto normalization
[4:20] aspect of it.
[4:21] Meaning that when you're changing the skinning on the joints, you won't affect and it won't
[4:25] be automatically redistributed to a random area, which is really cool.
[4:31] Right away, let's talk about optimization.
[4:35] You need to pay attention to that throughout the entire process, starting with the rigging
[4:40] and inside the skeletal mesh editor.
[4:43] If you are dealing with additional joints that you're not using in the mesh during animation
[4:50] or render time, you may want to pay attention to that because it could add to the performance
[4:56] of the assets.
[4:58] Another cool thing that in 5.8 now, with the right click, you can just remove all unused
[5:04] bones in one go, which is super useful.
[5:07] And yeah, just pay attention to that because sometimes we leave bones like that, no skinning
[5:13] information, just in case, but that might be impactful for the performance.
[5:17] You can procedurally spawn joints through a control rig in the construction events if
[5:23] you need some additional logic without affecting the actual assets that might be shared across
[5:29] a different rig.
[5:34] We know Unreal is handling quite well heavy meshes, but pay attention to that.
[5:39] If you have multiple skeletal mesh in one scene, one shot, that might be affecting the
[5:44] performance.
[5:46] We will see during the animation parts where having a bunch of characters and a lot of
[5:51] control rigs enabled can impact the performance as well, but this is the first step.
[5:57] Try to pay attention to that because it can be impactful.
[6:01] And you also have alternative solutions with subdivision like the Ozen plugin, which is
[6:07] super interesting and really cool to use.
[6:11] More targets are also important.
[6:14] You can have a bunch of different morph targets in your mesh, but too much can be impactful
[6:21] as well.
[6:24] This talk is more about linear content cinematics, but a lot of things that I'm going to talk
[6:29] about can be useful for runtime purposes as well.
[6:32] But if it's just for cinematics, you can go with a high number of morph targets, like
[6:39] MetaHuman has more than 800 morph targets for the face and the body, which is quite
[6:44] high number.
[6:46] But try to be effective and mindful to the number of morph targets you're using as well.
[6:53] Combining and mixing joints and morph targets are really great, but yeah, this is something
[6:58] that can tank your performance if you have a too high number of morph targets.
[7:06] Then with 5.8, we updated the skeletal mesh editor and the morph target's plugin.
[7:13] And now you can easily manage already created morph targets and also the one you can directly
[7:19] authored in the skeletal mesh editor.
[7:22] And we added the ability to flip and mirror the morph targets.
[7:26] So perfect to avoid round tripping.
[7:30] So now let's dive deep into ContraWig.
[7:33] I first started again with optimization.
[7:38] So I saw a lot of different ContraWig setup.
[7:42] And main thing to remember and that's always kind of a challenge is performance.
[7:49] ContraWig is really cool and easy to use and put in place a bunch of different logic.
[7:55] But in the end, sometimes you have some performance issue.
[7:59] And it's difficult sometimes to troubleshoot or to understand what's going on.
[8:04] This is why I wanted to talk about it because we added and improved the tool quite a lot.
[8:10] Execution, number of execution, execution order, functions, using specific setup like
[8:17] for each nodes are there to help you reduce the performance and help you having good performance.
[8:27] Sorry.
[8:29] So here's a video where I'm showing the execution stack, which is your best friend, because
[8:36] it allows you to understand what's going on and the order of the execution of the ContraWig
[8:42] throughout the forward solve event.
[8:45] You always pay attention to that because you can see what's going on.
[8:49] You can see what's running.
[8:51] And through all the tools we have in the ContraWig, you can understand at each step what's going
[8:56] on and if you have something to troubleshoot, where and when you can step in and adjust that.
[9:05] We added all the features, as I mentioned.
[9:08] Now, since 5.7, you can preview nodes, which is kind of the same setup we have on the shader
[9:15] graph system with our material.
[9:19] So it means that if you pause your character in ContraWig, you can just use preview nodes
[9:23] to stop the execution at a specific point and step with the shortcut F10, for example,
[9:31] the progression of the execution of the forward solve.
[9:34] So you can understand and see what's going on and when things are breaking, for example.
[9:43] Next thing is pretty common.
[9:44] It has been there for, I think, the beginning.
[9:48] But you can, of course, enable profiling, which allows you to see in microsecond what's
[9:53] going on.
[9:54] So you can see the number of the time it takes to execute one node or a bunch of functions.
[10:01] And this is basic, but I highly recommend to always have a look into it because it helps
[10:07] you understand what's going on and when, for example, you may use, as I mentioned, for
[10:12] each node, sorry, to kind of pack the execution.
[10:16] Because most of the times I often see logic put into the forward solve that needs to be
[10:22] put in the construction events where you can cache, store data, and reuse it in the forward
[10:27] solve.
[10:29] We also added the dependency viewer to the selection of one item, whether it's a joint
[10:35] or a control.
[10:36] You can visualize the connection.
[10:38] So it looks a bit scary and crazy, but that's a good help in the end.
[10:44] You can't break anything, just read on the graph.
[10:49] And yeah, it helps understand if you, for example, in production, you're using a control
[10:54] rig from someone else, helps you really grasp quite quickly what's going on from one item
[10:59] and the connection across it.
[11:01] We also added the highlights or occurrences.
[11:03] This is something a bit hidden.
[11:05] That's why I wanted to talk about it.
[11:06] Where, through right click, you can highlight or select the node used in the graph, highlighting
[11:13] the repetitiveness of a setup.
[11:16] That's something quite often in control rig.
[11:19] It's fine to do that when you are starting your rig, iterating, building stuff.
[11:26] But in the end, repetitiveness can be really cost performance and not the best friend for
[11:32] a nice running control rig assets.
[11:36] So this is where you can build function.
[11:40] At the end, if you want to be really optimized, you can also build what we call rig units,
[11:44] which is a C++ unit that you can have in your control rig, meaning that you will have access
[11:49] to a node as we can have here in the default library of control rig instead of relying
[11:55] on functions.
[11:58] Another challenge that you can encounter is inline bones.
[12:05] Inline bones are the bones that you may have in a chain, like usually the arm or the legs.
[12:12] By default, in Unreal with Mani Manikin, we can handle that through the corrective joints.
[12:17] There are more like leaf joints, so they're not following the normal flow of a hierarchy.
[12:23] It can be used as this, and you can build on top of it what we call ribbon control or
[12:27] bendy control through a chain.
[12:33] In a linear context, sometimes it's not really built like that.
[12:37] You have a really normal chain with a top parent and a child following the natural flow
[12:44] of a hierarchy, and that can cause a bit of a challenge.
[12:49] So if I highlight the joints here, you can see on the arm, I've got a bunch of bones
[12:54] on the arm chain.
[12:57] And here in this setup, one workaround is just to use IK2 bone as is, and you can skip
[13:03] the bone in between.
[13:04] But for the leg, you can see that the orientation is a bit clunky, funky, and not really well
[13:10] aligned, so it can give to Unreal hard time to understand what's going on.
[13:16] Not finding the correct orientation, and the last item could get a bit crazy.
[13:22] And I found the setup that was quite quick and easy to use through a full body IK node,
[13:28] where you can just specify the item you want.
[13:31] And this node will help you create a nice setup without having to create an additional
[13:38] IK chain on top of this existing one, and it's kind of just streamlining the overall
[13:43] process.
[13:45] So this is the setup where I'm using a prey-to-input behavior type of this node, and using the
[13:53] preferred angles, you can specify a pull vector.
[13:56] And it was kind of an easy workaround that I wanted to share with you, because as I mentioned,
[14:00] it devoid you to create crazy setup on those kind of chains, which are a bit difficult
[14:06] to handle.
[14:09] And we have tons of nodes in control that you can use and reuse without having to step
[14:15] into really complex and custom setup or function.
[14:21] And with this kind of chain, this is the setup you can build, as I mentioned, ribbon control,
[14:26] so you can drive and slide along the chain and create nice effects, and your animators
[14:32] will be really happy with this kind of setup.
[14:36] Another kind of challenge we can have is IKFK switch.
[14:41] I wanted to bring that up because my sounds basic as well, but it can be a bit tricky.
[14:47] So here we have an example with an FK and IK switch, and you can see I don't have any
[14:52] swap or modification on the position of the arm and the pull vector, and I can move around
[14:58] all the controls.
[15:00] When you're dealing with control rig, you can have a situation or everything is working
[15:05] in the control rig assets and preview viewports, but inside Sequencer, it behaves differently.
[15:13] And that's because you need to communicate between Sequencer and control rig.
[15:17] And what happens is that for FK and IK switch in control rig, you can build quite simple
[15:22] setup where you're just retrieving the bone position from the default solver, could be
[15:28] FK or IK and vice versa.
[15:30] But in Sequencer, you will have like a snap issue if you don't specify another setup.
[15:38] This is covered in the rigging workshop we gave a few months ago with more than 10 hours
[15:43] of free contents.
[15:44] I will talk about that a bit later again.
[15:46] But this is an example you can use.
[15:50] And it's all based on condition and Booleans, meaning that you will need to check the state
[15:55] of the actual solver and be sure to reset this value to be able to key the item not
[16:03] used during the solver that kind of slipping if you're using IK or FK.
[16:09] It's heavily depending on the send event node.
[16:12] And if you use the send event node without conditioning the whole setup, you will end
[16:17] up with something that kind of working, but when you will move the body around, it will
[16:22] start to deteriorate and freeze.
[16:25] So it's all based on this condition.
[16:28] And this is the overall setup that I really and highly recommend you to use for seamless
[16:34] and nice IK switch.
[16:40] Deformers.
[16:41] We love deformers.
[16:42] And here I wanted to highlight the control rig implementation of it.
[16:46] You can use deformers inside Sequencer, but as a rigger, you will of course want to put
[16:53] that in a rig and give a control specific behavior and be more in details with it.
[17:02] So here's the video of a complete setup and workflow through this rig.
[17:08] And you can manage everything through the Skeletal Mesh Editor.
[17:11] And here the example I'm using is by using Polygroup.
[17:15] So you can just paint area you want.
[17:18] You can use also a secondary skin layer, but here it's simple to do this approach.
[17:25] It's kind of the same thing.
[17:26] So through the Skeletal Mesh Editor, you can specify an area.
[17:29] So this is the head here.
[17:31] And this is for a squash and stretch setup.
[17:35] You can manage everything to the Skeletal Mesh Editor in terms of specific areas I mentioned
[17:40] and then retrieve that inside first the deformer graph where you have the kernel nodes, which
[17:45] is where you define the function of the deformer.
[17:49] So we shipped a bunch of different default functions you can use.
[17:52] This is a squash and stretch already available for you that you can use out of the box like
[17:56] this.
[17:57] And see at the right of the details panel, you got the HLSL code that you can also adjust
[18:04] and modify.
[18:06] I'm using a read skin mesh nodes at the top, which is really important if you want to stack
[18:11] and use multiple deformer at once.
[18:13] And here I'm through the white map inputs and retrieving the attributes I used to create
[18:20] the polygroups.
[18:21] So I'm just exposing a variable to reuse that in Control Rig.
[18:26] So once I put in place this setup, I can jump in Control Rig to retrieve that and adjust
[18:31] it.
[18:35] And in Control Rig, this is basic and straightforward setup.
[18:38] I'm going to talk about other ones afterwards, but you can use the add deformer nodes.
[18:43] Make sure to right click and refresh variables to actually see the variables we're exposing
[18:48] the deformer graph.
[18:49] Here's just a game to use a specific control or a joint and specify a specific position
[18:57] and expose animation channel to play with this deformer.
[19:02] And with just this setup, I'm able now to use the deformer.
[19:07] And as you can see here, I'm not using any animation blueprint, so it's pretty straightforward.
[19:11] But one little aspect of it is that you will not be able to record and save the animation
[19:19] you're doing here in an animation sequence, for example.
[19:23] I'm going to talk about that right after.
[19:25] So another example I did here is this little guy.
[19:30] I don't have a name frame, but maybe it's like I guy, I don't know.
[19:33] So he's running the deformer, the same squash and stretch function I showed you.
[19:38] It has some physics on the lashes and playing as well on some multi-hole curve attributes
[19:45] for the eye and the pupil.
[19:48] I wanted to highlight that to show that you can expose a bunch of different settings from the deformer.
[19:54] And you can expose that to your animator or to yourself if you animate.
[19:58] And you can also adjust and animate that inside sequencer, which is really useful.
[20:04] So no limits, tons of possibilities, which is really fun, with something already here for you,
[20:10] which is the squash and stretch function.
[20:15] So I showed you this example with the little guy named Dustin,
[20:20] where I just created polygroups, mapped that into the deformer graph, and then in the control-v.
[20:28] As I mentioned, the other setup that we need to use and put in place if you want to record this data
[20:35] into an animation sequence is to have this setup where instead of using just one control-v,
[20:41] you're using a secondary control-v where you put in place the add deformer node I showed you.
[20:48] And this control-v will be mapped to the animation blueprint.
[20:51] And the skeletal mesh will just gather the animation blueprint and will be assigned to it.
[20:57] So it will read the secondary control-v, read the deformer,
[21:01] and the existing control-v will be used just to author and create animation.
[21:06] You will need to map that to a joint, and even if you don't have any skin information, that's fine,
[21:12] but this is useful and needed if you want to save the data through an animation sequence.
[21:18] The animation blueprint is the main guy here to handle that.
[21:23] Otherwise, you don't need that, you just need your deformer graph and one control-v.
[21:28] This is the setup I showed with the Dustin character.
[21:35] Let's talk a bit about RBF interpolation.
[21:38] It might be challenging to jump into Unreal and start to build that through the common way,
[21:43] which is the animation blueprint.
[21:45] So you will need to create a pose asset and then use pose driver nodes.
[21:51] And it might be a bit tricky and you don't have the visualization,
[21:56] like the easy visualization of it.
[21:58] Let's say I want to move the arm, etc.
[22:00] So you will need to use animation sequence.
[22:02] And it's a bit tricky and not really visualized enough.
[22:08] And I love to be able to tweak and adjust and visualize what I'm doing.
[22:13] So in control rig, the spherical pose reader node is really useful and streamline the overall process.
[22:19] It outputs a normalized value, as you can see here,
[22:22] that you can hook up to a set-curve value of using plane shapes or offset transform nodes.
[22:28] Really simple to use.
[22:29] You just specify the driver item, which is the wrist joint here.
[22:34] And you can see the debug with the line and the little cone.
[22:38] And you can literally visualize what is the RBF interpolation,
[22:42] meaning that you can trigger another joint or another blend shape
[22:46] based on a specific angle.
[22:48] So control-ring, streamline, all of that.
[22:50] Which is super cool.
[22:54] Now, we talked about production earlier.
[22:57] Being modular is super important.
[23:00] So I wanted to talk a bit more in details about three different layers of being modular with control-ring.
[23:09] First, two functions with variants, modular control-ring, and the data-driven approach.
[23:16] The last test is kind of a bit hidden, but super useful and powerful.
[23:20] It's kind of the top layer, a bit more complex, but so much powerful.
[23:27] So first is the function here.
[23:29] So one way to be modular and to deploy a specific setup and function across different control-ring
[23:35] is to use function as a public function.
[23:38] So you can have a control-ring asset storing all the function you need.
[23:42] And you can then use what we call variants.
[23:45] Something maybe not really known, but variants will allow you to tag your function.
[23:51] It's already shipped with default tags that you can manage through the project settings.
[23:58] You can create your own tags with a specific color.
[24:01] You can go fancy.
[24:02] And then in the end, the other cool thing with variants functionality is that based on your control-ring assets,
[24:12] you'll be able to manage the updates of your function.
[24:16] So through the bulk edit button at the top here,
[24:19] you can propagate the updates function just based on these control-ring assets or throughout the entire project.
[24:28] So it's really powerful to manage the progressing of your production in terms of rigging.
[24:34] So let's say you have V3 or V4 of your function.
[24:37] You'll be able to manage and adjust that and deploy it across your project or per asset.
[24:44] The second layer is modular control-ring, which is really useful when you have like a ton of characters.
[24:50] You will need to jump into building modules that can be a bit tricky if you're not really familiar with control-ring.
[24:56] But in the end, it allows you to be fast and completely modular when you just have to literally drag and drop the modules you need
[25:05] and be able to build control-ring in just a second.
[25:08] So this is really useful for junior rigors that are joining the team or for layout artists
[25:14] building a quick control-ring to put in place the rough first pass of animation and so on.
[25:21] We have a bunch of modules already shipped in the engine and on 5.8 we also created physics modules that you can use and reuse.
[25:29] For example, if you have a quad rig with a tail, you can just drag and drop and create dynamic chains on it quite quickly.
[25:37] And you can of course jump into the graph and analyze everything.
[25:43] Last approach is the data-driven approach.
[25:45] So this is a long video, so I do my best to cover everything.
[25:49] So here I've got the structure assets.
[25:52] It's not mandatory, but you can create that to pre-define your variables and what you need.
[25:58] So it's an additional asset.
[26:00] So here I've just like a rig element key variable, so it's mainly based on joints and other variables.
[26:07] Then I've got the primary data assets.
[26:09] This is the one you really need and you can start from there directly.
[26:13] I'm just retrieving the structure variable here, but you can create your own variables here.
[26:18] It could be Boolean values, it could be a Flots variable and so on.
[26:22] I'm not defining anything here.
[26:24] I'm just creating the empty slots ready to be used and adjusted afterwards.
[26:30] Then I create a data assets and this is where I define and specify everything.
[26:37] As I mentioned, this setup is all based on joints and in addition,
[26:43] I'm using a variable name type which is going to be used for metadata.
[26:49] So I'm just specifying joint name, metadata name and also the other variable I expose
[26:57] is the shape of the controls, changing the scale, offset, etc.
[27:04] The data asset here is the one we're going to use to adjust, modify,
[27:08] everything and deploy easily everything throughout your project.
[27:14] And then in the Skate Town Mesh Editor, I'm assigning these data assets inside the asset details panel.
[27:23] And through that, I will be able to gather and get back to these data assets
[27:29] and hook everything inside the control ray.
[27:34] Next is in the control ray.
[27:37] We're going to use that first in the construction events,
[27:42] meaning that I'm going to store the data I created and I'm defining in the data assets.
[27:49] So through the get user data node in the construction events,
[27:54] I'll be able to retrieve the information I put in place in the data assets.
[28:00] I'm just highlighting here the use of import skeleton node
[28:03] because you can be fully procedural and just import any incoming Skate Town Mesh through this node.
[28:09] If you want to be fully modular and flexible,
[28:12] you just have to change and switch the preview Skate Town Mesh assets.
[28:16] And here I'm retrieving my data assets as an array, array type,
[28:21] so I can hook that up into a for each node.
[28:24] And I will see all the inputs I specified inside this for each node if I unfold it.
[28:31] Then I'm mapping that into a custom function.
[28:34] And all that setup is about dynamically spawning controls and solve them in a FK solve.
[28:42] So through this function and these data assets,
[28:45] I specify the joint name I want to map and a metadata name.
[28:51] You can also go and fetch individual variable inside this data asset if you want.
[28:56] You don't need to be to use the full array of the structure variable I showed.
[29:02] You can just expose a Boolean value that can be used.
[29:04] For example, if you have multiple characters and say,
[29:07] okay, this one has just two legs, four legs, a tail, etc.
[29:14] And then I have another function where I'm just retrieving the data I cached in the construction events,
[29:19] which are the names of the joints and the metadata name.
[29:25] So here I used two joints in the data assets.
[29:29] It spawned the control and I've got the solve of the control in the FK type.
[29:34] And the last step is to show you how flexible it is.
[29:37] So let's add additional joints through the data assets.
[29:41] So I'm going to add two index or three indexes here.
[29:45] So additional joints of the spine.
[29:48] All manage through the data assets.
[29:51] And the goal here is to give the ability to the artists, technical artists,
[29:55] to manage everything through the data assets and just save.
[29:59] And this will deploy the logic into the control rig.
[30:02] And you just have to compile the control rig.
[30:05] And as you can see, it spawned the spine control with the metadata name assigned
[30:11] and retrieved in the forward solve.
[30:14] You can also blueprint the compile action inside the blueprints.
[30:19] So this is fully procedural and modular.
[30:24] Main control is the data assets.
[30:27] And it's a really nice way to be even more modular,
[30:31] apart from the other solution I showed.
[30:37] It's a bit tricky.
[30:38] On this stage, you have a question.
[30:40] But just to sum up a bit, it's like data assets is managing everything.
[30:45] And you can deploy that across control rig.
[30:47] And you just have to save the data assets and compile the control rig.
[30:50] And you see the new updated items you define.
[30:55] I wanted to talk about physics as well.
[30:58] On 5.8, we added the control rig dynamics.
[31:01] Because it was a bit challenging to put in place physics inside the control rig.
[31:06] We added that a few months ago.
[31:10] Control rig physics is super cool if you want to go and dive deep into implementing physics
[31:15] in your assets.
[31:16] But now with control rig dynamics, you can, through just three nodes,
[31:22] easily put in place dynamic or kinematic item in your rig.
[31:28] I just used two nodes in the construction events where I spawned the solver.
[31:34] And then I'm using the spawn chain nodes where I define the items.
[31:40] And in the forward solver, I'm just stepping the solver to actually see what's
[31:43] going on and run the physics.
[31:46] This node, the spawn physics chain, is really useful and powerful.
[31:50] And it streamlines everything.
[31:52] Inside, you find everything you need by specifying the first item of your chain.
[31:57] And you also have the terminator item here that you can specify to end
[32:02] the chain at a specific point.
[32:04] And as you can see, you can quickly add physics on top of any existing logic,
[32:08] which is here, IK on the arm.
[32:11] This is also depending, as we mentioned earlier, of the execution order of your
[32:16] control rig.
[32:17] So you need to put the step physics solver nodes at the end of your forward
[32:21] solver.
[32:23] And here another example, let's pick another chain.
[32:25] So I'm picking the spine.
[32:28] And then I'm just using the terminator item input to specify when I want to end
[32:33] this dynamic chain.
[32:36] That's literally it.
[32:38] No more fancy setup.
[32:40] With just this node, you can control everything.
[32:43] You can, of course, expose some of the things you have here by the two outputs
[32:48] area you have and retrieve that in forward solve if you want runtime
[32:53] behavior, for example.
[32:55] And inside this node, you have all the things exposed for you, like the strength
[33:00] of the physics.
[33:01] And sometimes it would be tricky to adjust and manage the physics with the
[33:08] control physics.
[33:08] So now it's quite easily exposed.
[33:11] And one great addition is the curves input here, where you can specify based on
[33:17] the position of your item in the chain, specific values of the strength, for
[33:24] example.
[33:24] So first item will be strength of five.
[33:27] And the last one, if you put a 0.5 value, would be 2.5, et cetera.
[33:32] Really easy to manage now.
[33:35] Another thing to talk about, which could be a bit challenging, is hair and
[33:39] groom.
[33:40] So focusing on the control way and rigging aspect and animation, one of the
[33:46] main questions was often to try to be able to manage physics and both manual
[33:52] control over the groom assets.
[33:55] So we recently added a workflow where you can use both.
[34:00] So you can have the control of how much of the physics you want to run and then
[34:05] add on top of it a control rig.
[34:08] So this is a completely new workflow through Dataflow assets.
[34:13] And it's a bit of a process to put in place.
[34:16] So I got a link for you with some documentation that will help in the
[34:20] process.
[34:21] But this example you can see here is based on the sample pack, the content
[34:25] example pack we have on Fab.
[34:27] Free that you can download and analyze and see the map we have here with this
[34:32] girl and the ponytail.
[34:33] So inside the Dataflow assets, you can create a specific logic where you can
[34:39] manage your skin information and reuse that, project that into the groom
[34:43] assets and hook a control rig asset on top of it.
[34:49] This is a quick highlight.
[34:49] This is why I put in place this talk from Mikael Forot, which is one of the
[34:57] engineers in charge of this feature.
[34:59] It's a talk from last year and he covers all the workflow and some crispy
[35:06] details if you want to be more into it.
[35:09] I mentioned the rigging workshop earlier and this is also the link of the full
[35:15] more than 10 hours of free contents recorded for you.
[35:18] Really great if you want to dive into control rig and have all the details you
[35:23] need to be a pro rigger in Unreal.
[35:28] Let's dive into the animation challenges here.
[35:30] And the main topics are the following ones, mainly with adoption down to
[35:37] custom tooling.
[35:40] First challenge is adoption because we've been used to animating in
[35:47] all the DCC and it's always difficult to go and start animating from scratch in
[35:52] a new software.
[35:54] But as I mentioned here, it's not just a software, it's an engine.
[35:58] So it might be difficult to dive into it, understand what's going on.
[36:01] So when you open up Unreal, you have a scene, but you don't see any timeline
[36:07] and it might be heavy to handle.
[36:10] So that might be one of the first challenge you may encounter when you step
[36:14] into animation.
[36:16] Even just the structure.
[36:18] Unreal is not just like a file that you can save.
[36:21] It's an engine and it's all based on the project.
[36:24] You have the U project.
[36:26] Inside you have a U map, which is where you have, it's just a container of U assets.
[36:32] And inside you can have level sequencer where you manage your shots, you manage
[36:39] your animation, your cinematic, and everything is happening through this asset here.
[36:45] And usually in production, a level sequencer is looking like that with a lot
[36:51] of track, subtract, and it's a bit difficult to dive into it and understand
[36:57] what's going on.
[36:58] So that's why it's kind of the first challenge.
[37:01] And we worked hard to make it easier and to bring to you features and tools
[37:06] that ease and streamline the process.
[37:09] One of the first is in this kind of situation, you can leverage the use of
[37:14] the sequence navigator, which is this little icon here, where in one click you
[37:19] can visualize everything inside your sequence.
[37:23] So when you are animating, you want to focus on animation, of course, but in
[37:28] production, you want to understand what's going on and where things are placed,
[37:32] what are you dealing with, and if you have a specific actor inside the sequence
[37:36] or where it is placed.
[37:37] So this is a good tool to use and understand what's going on on the large
[37:42] and deep hierarchy inside the sequencer.
[37:48] So next to this adoption is the management of the setup.
[37:53] So animation in Unreal is handled through the animation mode.
[37:58] And inside, you have a bunch of tools available for you.
[38:02] And this animation mode, as soon as you turn it on or select a control through
[38:06] Control Rig or the Control Rig track, you will have access to all the common tools
[38:11] you may want to use as an animator.
[38:13] You can see at the top left, you have the Curve Editor, Constraining tab, where you
[38:16] can find space switch, constraints, and so on.
[38:21] We also have the sets, as you can see here, with a bunch of color to create your
[38:25] own sets on any character.
[38:28] And we also have, as you can see, a new timeline here above the Curve Editor.
[38:37] So connecting with the points we talked about earlier with adoption, this is super
[38:41] important because when you are inside a sequencer, most of the times it was really not really
[38:49] friendly to manage a handle because you have to scroll down, select, et cetera.
[38:55] We added a bunch of filters that can help in that matter.
[38:59] But with this new functionality, which is like a compact and simplified timeline, in
[39:03] one click, you can just compact the timeline and focus on your animation.
[39:09] This is super useful because it's kind of helping animators to adapt and dive into Unreal
[39:16] with a more familiar environment.
[39:19] And you can quickly now adjust and put your Curve Editor inside just below your timeline
[39:27] and you can manage everything quite easily now, which is super convenient and helpful.
[39:33] Everything you do that can be saved as a layout through the Window tab.
[39:40] And you can have multiple viewports, of course, and you can now more than ever easily put
[39:46] in place your animator or animation environments.
[39:51] Cool feature as well, I'm going to go back to that with constraints, is the ability to
[39:54] easily offset your keys.
[39:57] And everything is fully customizable through a right click on your timeline.
[40:04] We added in 5.8 a lot of things through shortcuts and we also exposed keyboard shortcuts, a
[40:11] tab where you can specify and put in place all the shortcuts you want.
[40:18] If you are an animator, you know that's kind of mandatory to have shortcuts, so you can
[40:22] map almost everything here.
[40:28] And constraints as well can be a bit challenging on specific workflow, so I wanted to share
[40:31] with you some tips and tricks.
[40:34] And to put in plain constraints in Unreal is quite easy, through the Animation mode and
[40:38] the Constraining tab and the constraints, you just have to select Control and just pick
[40:45] the type of constraint you want.
[40:46] Through the little dots, you can specify and adjust your constraints and you just have
[40:50] to specify the other item you want to parent, the first control you selected.
[40:57] Little message at the bottom right saying that it might be more convenient and stable
[41:06] to use spawnable actors, so it stays and lives inside the Sequencer.
[41:11] So if you have spawnable actors that might be more stable to use spawnable actors that
[41:17] are just regular actors inside the Sequencer.
[41:22] Another thing I wanted to share, if you want something even more robust and stable, it's
[41:28] really depending on the situation and setup of course, but you can also, instead of using
[41:32] controls, just use joints or bone to constrain your item.
[41:38] Maybe your control is hidden or not spawned yet or you have a specific big logic, so if
[41:45] you can't find the control, you may end up with a specific behavior of the constraints.
[41:50] So mapping the joints can be more useful at some time.
[41:56] And another thing that might be a bit tricky is of setting the constraints.
[42:00] So through the new timeline here, it's easier, really and way more easier to manage that
[42:07] because depending on where you are with your scrub head in the timeline, you can just use
[42:14] that to offset everything after that.
[42:19] This is always as well short keyable if you want and why it streamlines this kind of situation
[42:26] and operation because using the basic Sequencer view, if you're not selecting all the keys
[42:32] involved in the constraints, you may end up with breaking the constraints.
[42:39] And why you may be tempted to use the bar you can see at the top and that's not the
[42:45] best thing to do because it not really brings the entire section of all the keys involved
[42:52] in these constraints.
[42:53] So a little tip is to hide these bars and just rely on keys if you're not dealing with
[42:59] the simplified timeline and just select everything, make sure you select everything and offset
[43:03] that.
[43:06] On 5.8 we also improve the constraint stability with the render.
[43:11] Sometimes on heavy constraint assets, you could have like a difference or different behavior
[43:18] or results during render time and this has been improved on 5.8.
[43:26] About optimization, we also added a new feature and this is a common scenario where you have
[43:31] a shot with a bunch of control ring and actor and you can quickly tank the performance.
[43:36] You have work around by using specific view modes.
[43:39] You can change as well the scalability settings but be careful, this can cause to recompile
[43:44] the shaders, you can text time.
[43:46] But with 5.8 we added this auto-paking system.
[43:50] So you can see at the top in the Sequencer, we have the little flame icon and what it
[43:55] does is just streamlining the use of linked animation sequence.
[44:00] So it means that with the right click you can use the auto-paking and this will bake
[44:06] the actual animation you have in the Sequencer and give you the ability to quickly switch
[44:12] between this animation sequence track you just created and the control ring.
[44:17] So you can see here by default when you do the operation you are on the control ring
[44:23] track and you have access to the animation sequence track as well.
[44:29] This little flame icon allows you to quickly switch between the two of them.
[44:34] So by doing that if you have a bunch of control you can just kind of cache the animation meaning
[44:39] that you will be able to hide the control ring track and this kind of ease the performance
[44:44] and you can have a big gain in performance.
[44:47] Anytime you can go back to the control ring, adjust your animation, save and as it is a
[44:52] linked animation sequence it will automatically update the animation sequence and then you
[44:57] can switch back and forth.
[45:00] So end of the day just like streamlining the use of linked animation sequence and helping
[45:05] you to reduce the amount of manual work you have.
[45:09] You can have.
[45:12] And to end with all of that, as I mentioned in production you always have to deal with
[45:18] custom tooling so I wanted to dive a bit more into Editor utility widgets.
[45:24] So one of the first use of Editor utility widgets when it comes to animation is the
[45:29] use of Anim Picker.
[45:32] This is Oscar my little cat and I've got a name picker that I created here and we don't
[45:39] have like a template of a name picker out of the box but with the Editor utility widgets
[45:44] you can easily create and iterate and be creative with any anim picker and it's really powerful
[45:52] and it's kind of the first use you may want to do in with animation and with custom tooling.
[45:59] So I just wanted to highlight that.
[46:02] You can do that quite easily in Unreal through the Editor utility widget assets which is split
[46:09] into two sections which is the design parts and more scary parts which is the graph parts.
[46:15] It looks complicated but for this kind of scenario it is really not complicated it's
[46:21] just a repetition so it's just based on selection, selector control or you can create a function
[46:26] to add a specific combo like Shift select or Alt select to select a bunch of controls
[46:32] or Deselect other controls.
[46:36] So Editor utility widgets kind of push the boundaries of all the tools that you already
[46:42] have for you and we've been working on hard so it's kind of giving you the additional
[46:48] possibility to create your own tool and be even more productive, effective and creative.
[46:54] And I wanted to finish on another custom tool that I've been working on for a few months
[47:04] thanks to all the feedback from awesome studios and animators like even internally and also
[47:14] other animators in the industry.
[47:17] So I found a name which is Sam for Solo Animation Mode.
[47:21] I thought Animation Mode was cool but kind of a bit referencing to the Animation Mode
[47:28] we have in Editor.
[47:30] So this is coming from a situation I had when dealing with animation in Unreal because in
[47:37] Unreal we can animate in real time with all the details, everything's going on the scene
[47:43] and sometimes on some shots you have like a lot of things in the scene, a dark lighting,
[47:49] lot of elements or assets that can be a bit annoying to deal with when you're animating.
[47:57] So this tool allows you to quickly get rid of everything in addition to the character
[48:05] you want to animate.
[48:06] So it's kind of a focus mode and I added a bunch of features throughout the development
[48:11] of this Editor GT widget.
[48:14] And here you can see a kind of a classic sequential structure with some cameras, camera cuts,
[48:21] actor, blueprint and skeletal mesh.
[48:24] So through one selection I'm able to isolate the character, bring up a specific environment
[48:30] with a specific lighting so you don't have the emissiveness of the controls, you can
[48:34] enable shadows and it's just pulling a temporary camera with a lighting map to it.
[48:41] That will allow you to have like a flat and simple lighting.
[48:44] At any moment you can bring back your lighting from the scene and you can also hide what
[48:49] we call sprites which is the icons of the different actor of your scene.
[48:54] This is something I heard a lot from the animators just to streamline and focus easily and simply
[49:00] on the animation.
[49:02] I also added the toggle camera cut functionality where you can toggle between the solar animation
[49:07] mode camera and the cameras present in your sequencer and also the addition the silhouette
[49:14] mode and the background modes that you can also customize and adjust.
[49:19] And also the actor tag which is a feature that allows you to tag actors and use tags
[49:24] instead of selection.
[49:29] And to finish I created a Nidhi C tag, the doc where you have all the information, everything
[49:33] covered inside it and all the information is out there.
[49:38] It comes with the sample pack and the tool itself so it's free, it's for you guys and
[49:43] I'm waiting for your feedback.
[49:45] I want to keep developing that and just to give you some ideas I want you to iterate
[49:50] from that, analyze this little tool and help you in the adoption of animation in a row.
[49:57] And with that I think we're all good.
[50:00] Thank you.



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
