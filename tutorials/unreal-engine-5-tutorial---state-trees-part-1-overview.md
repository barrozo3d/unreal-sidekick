---
title: Unreal Engine 5 Tutorial -  State Trees Part 1: Overview
source: YouTube
url: https://www.youtube.com/watch?v=MuWRxuz1bjE
author: Ryan Laley
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-5-tutorial---state-trees-part-1-overview/
frame_count: 0
frame_status: pending-selection
---

# Unreal Engine 5 Tutorial -  State Trees Part 1: Overview

**Source:** [YouTube](https://www.youtube.com/watch?v=MuWRxuz1bjE)
**Author:** Ryan Laley
**Duration:** 10m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal-engine-5-tutorial---state-trees-part-1-overview <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome to a series that many of you have requested me to cover, which
[0:07] is State Trees.
[0:09] Now State Trees were introduced in Unreal 5, coming at which point it was, but one of
[0:13] them, and it keeps, again, updated with new exciting new features, and I'm pretty happy
[0:18] with where it is right now.
[0:20] So I decided to do a video series about it, explaining how it works and why you'd want
[0:24] to use it over, say, behavior trees, and various things like that.
[0:29] Now let's go through some of the basics first before we start showing examples of how to
[0:33] actually use one.
[0:35] And let's jump in.
[0:36] So the very first thing you need to do is enable the plugin form.
[0:42] So go to your plugins and just search for State Tree.
[0:47] We're in Unreal 5.5.4, so it wasn't turned on by default in this one.
[0:51] It may change for future versions, but we have to make sure you've got Gameplay State Tree
[0:56] turned on, and this is State Tree for AI slash Gameplay Behaviors.
[1:00] Now this is an important note, is difference between State Tree and Behaviors is a behavior
[1:06] tree is exclusively really for AI.
[1:09] But this can be used for things that are not AI.
[1:11] You can do it for doors, you can do it for chests, you can do it for targets, you can
[1:15] do all sorts of things, not just AI.
[1:17] So it's really quite more flexible.
[1:19] So turn it on, it will ask you to restart it, and you're good to go.
[1:25] OK, so to create a new State Tree, all you have to do is go into your browser, go to
[1:30] AI, artificial intelligence, and go to State Tree.
[1:34] You're given two extra components here.
[1:37] So the State Tree component is the State Tree for all the generic actors.
[1:42] So let's say you want to do one for a door, that would make sense to do one for that.
[1:46] If you want to do one for an AI actor, so like a character running around, for example,
[1:50] you get the State Tree AI component.
[1:52] Now, this one is important because this one gives you guaranteed access, as you can see
[1:56] here, to the AI controller and the actor that's running that component.
[2:01] So let's say I want to do an NPC with this.
[2:03] I'm going to click on that.
[2:08] And we'll do NPC generic.
[2:12] And let's open this up.
[2:13] So let's explain what you're seeing here.
[2:16] So there's three sections.
[2:17] You've got the asset details, tabs on the left here, you've got the State Tree in the middle,
[2:21] and you've got the details panel on the right.
[2:23] The details change based upon what you have selected.
[2:26] But most importantly is our State Tree in the middle here.
[2:29] Now, much like Havy Tree, you do start with a root node.
[2:33] And that's very important because that's where you start.
[2:36] Now you can add new states, but click on new state, and you can see it's got another state
[2:39] here.
[2:40] And take note of the hierarchical design of a State Tree.
[2:44] This is what is determining what should go next.
[2:48] The root will go into one of its first child, evaluate it, and then run that one.
[2:54] And if it's got two children in a root, if it fails this one, it will then go to the
[3:00] second one, and so on and so forth.
[3:03] Now these can also have their own children states as well.
[3:07] So if I want to do add state child state, as you can see, it's going to make a child
[3:13] of this one.
[3:14] Now, to order for this third one here, this one I've got selected here, for that to
[3:19] in order to run, it has to be true for the first one, its parent, and then true for itself.
[3:29] This is what we call a leaf node.
[3:30] In other words, a tree will keep going down branches until it finds a leaf.
[3:35] And the leaf is what executes.
[3:38] At the end of the leaf, you'll see it says root, with a little arrow pointing up.
[3:43] It's the default transition rule.
[3:46] So what happens when it ends the leaf here, it was a transition to the root,
[3:50] back to the beginning.
[3:52] Now, one thing to note about this is that you can actually change this to be
[3:55] wherever you want.
[3:56] So we can change it to transition to other things by using the transitions tab on the
[4:00] details.
[4:02] So one thing that's good about state trees versus behavior trees is that you have full
[4:07] flexibility about where to send different states based on different, upon different
[4:11] conditions.
[4:12] And you can have multiple transitions too.
[4:14] So you can add one here and do another one for different things.
[4:17] So this is the trigger for when the state's completed, but you can do one for when
[4:20] the state's filed, it'll do a different thing.
[4:23] Okay.
[4:23] So you've got lots of different extra options to choose from when dealing with
[4:29] transitions.
[4:32] Speaking of the dust panel, let's take a look at what you have available to you.
[4:35] So first up, we've got the parameters.
[4:37] The parameters are just variables that you assign to your tree.
[4:41] So let's say, for example, we have a vector and let's rename it and we call it location.
[4:51] There's the parameter for the location.
[4:53] Okay.
[4:55] And we can promote that to the parameters in the global parameters.
[5:00] And that is going to appear in the parameters for this state tree.
[5:06] So I can actually set it now from outside the state tree.
[5:12] Over here.
[5:16] The enter conditions are your conditions for when it should enter that state or
[5:20] leaf.
[5:21] For example, you can do various different comparisons.
[5:23] So you've got ones that are built in here such as ball compare, float compare,
[5:27] integer compare, trigger whereas tags.
[5:29] So state trees work really well with MAs tags built in.
[5:32] It's great.
[5:34] You can also make your own conditions, as you can see from the top button up here.
[5:39] Then you have the selection utility.
[5:40] This is determining when it should select that one leaf or branch.
[5:45] By default, you have a weighting associated to it, but you can add other things to it
[5:48] as well if you wanted to.
[5:50] So let's say you want to do an enum input and it would do like a selector basically
[5:55] based upon the enum entry.
[5:58] Just delete that.
[6:01] Then we've got tasks.
[6:01] Tasks are your meat of your state tree.
[6:05] This is where all the code executes for the various different tasks that you want to happen.
[6:11] Then you got transitions, which we've seen already what they do.
[6:16] On the left hand side, we've got details about the asset itself.
[6:18] So it contains information about the entire state tree, including its parameters,
[6:22] so global parameters that belong to the state tree, as well as evaluators and
[6:28] global tasks, more about evaluators and global tasks in another video, but we'll
[6:32] come back to those soon.
[6:35] One thing you'll note though is because we chose the state tree for AI, you got
[6:39] access to the actor context and the AI controller that is running this state
[6:43] tree really good and handy to have.
[6:48] So how do you actually apply a state tree to an actor?
[6:51] Well, let's go ahead and create an NPC, a new character.
[6:59] And in our character, we'll give it a mesh and an animation.
[7:07] Bring it down there.
[7:10] Like so.
[7:13] And we want to give it the AI controller as well.
[7:17] So let's go ahead and create an AI controller.
[7:23] Like this.
[7:30] And assign it to our class here.
[7:34] Searching AI controller and AI NPC.
[7:37] There we go.
[7:38] So this is now using that controller.
[7:41] So for that controller to run the state tree, we're going to go into the controller,
[7:45] add and search for state tree.
[7:49] You want to choose state tree AI.
[7:53] Now on the right hand side, you can choose what state tree you want it to run.
[7:55] So we're going to choose our one there.
[7:57] And as you can see, we can plug in values straight away.
[8:01] From the location here, it all comes through and gets pulled through.
[8:04] So everything you make global as a parameter will access and reach over
[8:08] from the actor side of things.
[8:09] So you can send other information through if you want to use it.
[8:14] Very handy.
[8:17] And also note that it says start logic automatically.
[8:20] This means that yes, it will start automatically.
[8:22] You don't have to call run behavior tree like you would with behavior trees.
[8:25] It'll just run.
[8:25] But you don't have to do that if you turn that off and we're going to run it.
[8:29] But you don't have to do that if you turn it off and wanted to start when you want it to.
[8:33] We just drag out the state tree there and take the start logic.
[8:37] Something simple as that.
[8:38] OK, so we're going to turn it on to be automatic.
[8:43] And compile and save that.
[8:46] OK, so.
[8:49] Let's put our NPC in our scene here.
[8:52] And we still need a nav mesh.
[8:53] So let's put a nav mesh in there.
[8:58] OK, so let's check out with P.
[9:10] There we go.
[9:11] So the nav mesh is what determines where the AI can travel to.
[9:15] So very important that you have that P on your keyboard
[9:18] will turn that preview off and on so you can see if it is covering the level as intended,
[9:23] which is great.
[9:26] That's the basics of the state tree.
[9:27] Now, obviously, there's lots more to cover.
[9:29] We'll be covering that in the future videos.
[9:31] In the next episode, for example, we'll be making our AI characters run around randomly
[9:35] using a state tree to control that behavior.
[9:37] We want to watch that next episode.
[9:38] Head on to patreon.com for slash Ryan Lely,
[9:41] where you can watch all my videos early from just one dollar a month.
[9:44] You can also get access to these project files and many others from other tiers
[9:48] for private sessions, many other benefits to a massive thank you to all our supporters
[9:53] over on Patreon and YouTube members.
[9:55] Thanks for watching.
[9:56] Make sure you subscribe and I'll see you next time.
[9:58] I have one.



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
