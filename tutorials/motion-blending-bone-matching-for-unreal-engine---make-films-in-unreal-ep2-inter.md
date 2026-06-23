---
title: Motion Blending / Bone Matching for Unreal Engine - Make Films in Unreal : (ep2) (Intermediate)
source: YouTube
url: https://www.youtube.com/watch?v=JxHYt9vFQD8
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter/
frame_count: 8
---

# Motion Blending / Bone Matching for Unreal Engine - Make Films in Unreal : (ep2) (Intermediate)

**Source:** [YouTube](https://www.youtube.com/watch?v=JxHYt9vFQD8)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 14m32s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction & The Problem with Blending Standalone (Root Motion) Animations [0:00]
**Transcript:** So Brock had a question about blending standalone animations and the ones that I've been doing  on the earlier video were all in place animations so everyone's like walking on the spot and then  you blend them together and they blend really nicely and then you just put a translation on it and  that's kind of like the video game process but what he was doing was more using not motion capture  but I'm going to say motion capture type stuff where you've got the root position animated and  it's kind of built into the animation so when you try and blend the two they'll both go back to  their root position so somebody would be walking along like this and then the other animation cycles  here and it'll go knee to that so I'm going to show you how we get around that thing is crossed  okay so he showed me the two pieces that he was using and they were from Mixermoat so if you've  not been to Mixermoat mode before then head over to Mixermoat it's free and I think it's Adobe  and they've got tons of like animation packs and cycles and things all for free and it's fantastic  so grab some stuff there and I'm just going to download the two pieces that he showed me and then

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_000.jpg

### Downloading Animations from Mixamo (Swagger Walk & Idle) [1:03]
**Transcript:** we'll bring those into Unreal so you type in your your thing you're looking for here and he had swagger  so I'm going to click on that one there swagger walk and you can see he's walking  on he's not walking on the spot so he's like actually got a translation built in and you can put  in place here if you needed to so this is kind of what we used to inside of Unreal and then for like  for characters and stuff and then you add a translation to your kind of third person player thing  I don't know I do filmmaking rather than video game type stuff so that's how I roll  so I'm going to turn off in place so this is what I'm sure he had and then we're going to export  this character so we go to download and then we're going to have it as fpx frames per second  let's make it 24 with skin I think I'm going to keep it with skin on and then no keyframe  reduction so I'm going to hit download and then it'll last me probably somewhere to put it  no it's actually just downloaded it into my downloads area fantastic and then let's just go  on looking here for the other one I think it was idle type that in there I think it was that one  so we select that idle and again hit download download with skin blah blah blah blah 24 frames  yep and then I'll probably download it over here hurry so there's my two and that's it now we  done with Mixamo so I've loaded up Unreal Engine 5.61 and I've got a blank scene and I've made a  direct recall Mixamo just to put the content in and so we're going to import those two fpx's so you

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_001.jpg

### Importing FBX and Setting Up in Unreal Engine 5 [2:40]
**Transcript:** write mouse button import into current folder and then we'll drag one or time I just grab the idle first  and then it's going to run all these things and I'm leaving it blank for now I'll go over it later  I'm just going to import and then I'm going to grab my character and just pull him into the scene

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_002.jpg

### Creating a Level Sequence and Adding the Idle Animation [3:00]
**Transcript:** there is and then I'm going to add a secret a sequencer so write mouse button cinematics new level  sequence and I'll record it at less mix more okay I'm double click on that that'll open up our  sequencer and it changed the frame rate to 24 frames because we're going to movie and then I'm  going to grab this character and then bring him into the sequencer and now under animation I'm going  to hit plus and then we're going to find that idle idle animation and my frame zero so now if I press play  there we go we can see that character is doing an idle perfect now okay so idle idle idle and then  as you know if you pull the end of this it will just keep the animation to these little bars it'll  keep the animation cycle so I think these are nice cycles there we are great that's how I stand  I'm not doing anything okay so now we're going to grab the next piece of the puzzle which was  a right mouse button important current folder and it was his swagger walk  okay with that one and this one I'm going to tell it to use the same skeleton oh it's actually  knows to use that same skeleton because it's looked all bones and gone oh is there anything  else in unreal with this configuration it knows that it's going to use this same skeleton so  that's good I'm going to hit import it should bring in that asset now you see if I was a professional

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_003.jpg

### Importing the Second Animation & The Blending Issue Demo [4:30]
**Transcript:** what I should have done was to press import animation only and then just choose the existing skeleton  that way we didn't have duplicate skeleton so it doesn't do anything bad it's just you've got  lots of extra junk just sitting in your directory all right sorry there we go swagger walk  that's got animation there's this animation sequence so back into sequencer and now I am going to  go over to here and I'm going to hit plus on the animation and then we're going to find the swagger  walk so this skeleton is compatible with these two animations so hit swagger walk and now you'll  see it he walks along like that and there he is there so at the moment we go bonk bonk bonk bonk  and this will actually work if I drag this over to here since the guy was starting at the beginning  from zero zero zero it should actually quite blend quite well oh yeah there's a see there's a  bit of a slide there and what I'll do is I'll do the other way around I'll put this over here because  this is what was in brox video he sent me a little clip of the issue he was having and so it was  more like this so he was walking along do do do do do and I he added it he added like bottled up  against here and he was walking along like this and then rather than coming to stop he goes back to  his initial position and if I blend these two by just dragging them over the top of each other he'll  kind of go skate back to it like he's getting blown like that you see right okay so we don't want  that so what we do is we do bone matching I think it's called something like that and what we're

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_004.jpg

### THE FIX: Using Bone Matching in Sequencer [6:14]
**Transcript:** going to do is going to select the animation clip right mouse button and then we've got here match  x and y translation all those things so what we're going to do is take I'm going to just turn those  off and go match this bone in the previous clip so if we match the hips of this clip it should  match the hips of that clip let's have a look so let's go back to the beginning now it's not so  let's try something else properties it match x and y translation okay need that on okay so there  we go so you need those on that's the trick what don't don't don't there's no great  so again right mouse button on here I had Matt I turned that off and he didn't match the x and y  translation you can also match match the height as well there we go and we can also match the  the which ever one it was the ure okay so room now I wonder if they can also do you know because  here like he's he's doing his wash with shimmy with his feet I know that we could actually try  and match his foot with it so let's try his right let's try his right right toe or something

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_005.jpg

### Matching Specific Bones (Hips, Feet) for Better Blends [7:32]
**Transcript:** let's find a foot left leg left foot so it's going to we're going to match the left foot of this one  with the left foot of the previous clip so see how that works so so look there he is his foot  sticking so which we should probably match the other foot so right mouse button match with this  bone in the previous clip right foot for I can type it in foot f o t let's try the right foot  this time so now when we go back here hey that's a little bit a little bit better  well not quite though but it was never designed for that but that is how you do your bone match  and I would probably go to this one I mean you can get all fancy but I would go to match this bone  I would match the hips and then you know it's a little so we can kind of maybe slow that down a  little bit so moving the animation I'm pulling them apart so they're going to overlap slightly  differently so it's find a nice point where they might blend better yeah that's not so good that one  okay okay body  let's grab these over here and then we'll take we can take this idle animation again actually we  can just add in back here so add animation plus add that same idle I'm going to just push him on  the beginning like that now these will bring again slides I think I have to do bone matching for this  one so you see that it's got that little view so what we can do  let's try matching this clip with the previous one let's try a different bone to match  let's try another bone it's going to move move through the different bones see if any any a better than  the others it's going blend these a bit more so I'm blending the animations over the top of each  other a little bit better so there we are you mean ideally you want to find an animation  that queues up a little bit more naturally like if you could find an idle where it would be more

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_006.jpg

### Bonus: Adding a Layered Control Rig for Custom Animation Overrides [10:20]
**Transcript:** in that kind of position I guess rather than that twisty turn but that's basically the principle of  it okay so the next thing is since we've got this now and so we want to do some adjustments on top  of this what we can do is we can add a layered control rig and so a control rig is every single  fbx character that you bring in or every single model that you bring in that's a skeletal mesh  comes with a fk control rig which is basically the forward kinemation which is your bone rotations  so everyone has that you can get the really nice fancy ones like if you're bringing the sk manny  and you've got these lovely things with a big yellow triangle everywhere and you've got  inverse kinematics and that's all stuff that's great if it's already set up for you but in this case  there won't be anything like that so they'll be but they'll be the bone rotation so we can add an  additional layer of animation on top of this so you go to wherever you want and then I'm going to  just go into here press plus and then control rig and then here you turn on layered so it  it layered there's all the control rigs that are available but I think really the one we want is  this one yeah these I don't think these would work if I tried them but I'm not going to so we  want this one which is the fk control rig and that basically gives you all the bones so on top of  this animation so let's say when he starts we wanted him to be till looking another direction so  I'm just going to grab his hip here I'm going to go into local rotation world at the moment there's  local change it to rotation so I'm going to rotate oh that's his hip so we want to change his hip  we want to change his his funny spine there we are so I can move his spine around so if I'd just  turn him this way just for example press play now and there he's all backward so I mean that's  probably not what you want however in fact you can do that brilliant isn't it so I'm going to turn  that back so you can basically put an animation on this so let's have a look so we're going to start him off  like this he's looking over here I'll put his head look around there turn his head around I can also  grab in here in the animal outline I can grab his head makes it a bit easier so we can find that move  that over there so I'm looking over there I'm going to save keys for this so let's look so we'll save a  key so I can if I do one up here it'll save it for everything the whole head so the position rotation  scale whatever and then you see it's done a triangle which means it's linear which you don't really  want that so I'm going to right mouse click on that change that to cubic let's try the cubic auto  and you set up your types of keys here so I'm going to keep it on cubic auto like that and I'm  going to move to another frame let's have him look around over there like that and then  going to turn on auto key which we is that one there so every time you move something it'll  automatically save a key for what has been moved so so then we're adding that on top it's looking  and then he's going to move his head again so he's got a key and we rotated that a little bit  earlier so we're saving another key for here and as he starts coming forward we're going to rotate  that around a bit more move his head back  so hopefully that helps and if it doesn't I'll do another one okay all right see you bye so thank  you Brock for leaving the question and for anyone else wanting an answer to something random please  type it in the comments and I'll try and get to it and now if you're looking for something else  that's fun and edgy-mocational to watch then this video on Ragdoll is really fun and you get to  learn a lot about Ragdoll surprisingly all right see you there and thanks for watching

**Frame:** tutorials\frames\motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter\frame_007.jpg


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
