---
title: Green Screen Integration in Unreal Engine 5.7 Virtual Production got even BETTER! (Composure EP3)
source: YouTube
url: https://www.youtube.com/watch?v=zlZCKT-5pLU
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-/
frame_count: 22
---

# Green Screen Integration in Unreal Engine 5.7 Virtual Production got even BETTER! (Composure EP3)

**Source:** [YouTube](https://www.youtube.com/watch?v=zlZCKT-5pLU)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 29m49s | 22 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction to Composure Improvements [0:00]
**Transcript:** Welcome to Composure Part 3.  This video I'm going to show you some of the improvements that I've come up with  over the last few weeks for using the lit mass material.  For those of you not familiar with Composure, it's Unreal Engine 3D compositing techniques  directly inside of Unreal using live action, bringing in as an image media sequence, putting  on to composite mesh geometry and then placing that inside the 3D environment so you can move  it around almost like geometry, just brilliant.  So I'm going to show you some of those improved techniques right now and this guy over here  is going to help.  My name is Dean Yaka, I'm a visual effects artist and I work in Hollywood motion pictures

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_000.jpg

### Why I Make Nerdy Videos [0:40]
**Transcript:** and I've done so for the last 30 odd years.  So I've worked on Star Wars, Avengers, all sorts of cool stuff, Harry Potter, etc.  What I do in my day job is compositing and environment work and also some immersive stuff  too.  But that's for a studio so it's very expensive but what I do at home is I make films and  my passion is to try and use that high end compositing techniques for bringing up stream  into more affordable low budget Unreal Engine 3D compositing because I want to make films  but I haven't got a studio so this is a way that we get around that.  Hooray for technology.  Alright, so that's me in a nutshell.  Oh no, that's me in the nutshell.

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_001.jpg

### Overview of Key Techniques and Lighting [1:30]
**Transcript:** So in the last video I showed you how to use Composure to project live action footage with  an alpha channel onto geometry inside of Unreal Engine.  One of the things I was doing at the time was using a mask material and I was adding  a dither to it but I was always getting this problem with the edges kind of keeping that  cross hat shape no matter what my anti-aliasing was doing.  And I've figured out a way of improving that and it's really simple and I love it.  And the second thing that I've discovered is how to add lighting to your composite mesh  geometry that's actually in the environment.  So you can take a point light and then shine that in your environment and light up the  all set but it also add light onto your composite mesh material as well.  So it helps sell the illusion that your lights are in there with your character.  It's not quite beable but it's definitely an improvement.  And the last thing I want to show you is improvements I've made to my extraction technique  using DaVinci Resolve Fusion page and the Difference Kier and also some colour pipeline differences  too. So on with what I was going to show you.

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_002.jpg

### Step 1: Matching Real-World Lighting to Unreal [2:33]
**Transcript:** So step one is to create your blue screen and since I'm using an animatic I've matched  my physical camera to where my animatic camera is, same angle, same lens.  I've set up my main key light to match where my sun is and then to the side of it I've  added two lights with an animated flicker on them and that's going to help sell the illusion  that I'm travelling through an environment and there's things passing me in vehicles  and bouncing off buildings.  Now if the lighting on set was very distinct so I had a light moving across the scene then  I'd have to match that inside of Unreal Engine with an animated light.  In this case since it's general flicker we kind of get away with it but one of the awesome  things with the new Composure material is that you can actually receive light from the  digital environment onto your plate lighting.  So now we're going to take this footage and we're going to bring it into my compositing  software in this case it's DaVinci Fusion and then we're going to create an extraction.  So this section covers how to create our image media sequence.  I'm using DaVinci Resolve Fusion page to create the extraction so you can use Nuke or

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_003.jpg

### Stage 2: Extraction in DaVinci Resolve Fusion [3:36]
**Transcript:** After Effects but the principles are the same so the nodes are different but we effectively  need to create the same elements in the end.  So you can kind of skim through this a little bit but the important thing is to make the  edge extended version with the unprimultiplied alpha which I'm going to show you now.  Stage 2 is to bring in the footage we just shot and I pressed 2 here to see the result  and then inside of Unreal Engine it's working in linear SRGB as default so to view what  this footage would actually look like we go under here under the lots and then we go to

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_004.jpg

### Correcting Color Space (Linear to sRGB) [4:07]
**Transcript:** this down arrow and then VFX IO and change it to linear to SRGB and if we brought these  frames in right now this is what it would look like.  So we want to apply our black magic cursor in this case because I shot it with the black  magic we want to apply that same color space transform onto these frames.  So we select our clip press control space and then type in color space transform hit that  one there and then we change our input color space in this case it was the black magic  4.6K film gen 3 and the input gamma and this was shot with the black magic 4.6K film.  Now if I look at the result of this this is now how it looked like inside of Unreal.  So I want to get it just into a little bit of a more comfortable color space by just adding  a color corrector and I'm just going to pull the gamma down a touch.  Now we're going to use the delta keyer to pull an extraction so we press control space  and then type in delta keyer and the delta keyer has a different map keyer built into

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_005.jpg

### Creating a Clean Plate with DaVinci Resolve's Delta Keyer [5:13]
**Transcript:** it.  So if you look here this pink little nodule there and if you look down on the bottom  corner I'm pointing it'll say that's the input so we need to create a clean plate.  Since this is a lock off normally what I would do is just leave the frame use that as a  clean plate but because the lighting is changing so much then I need to create a clean  plate using the actual footage.  So we to create a clean plate we do control space type in clean plate there we are and  make the input the color corrector up here just makes more space.  Then we go into our color so we click on the eyedropper and then we drag that over our  blue or green screen and then if you look here under fill and grow edges if you pull that  it'll basically grow the edge where it was black.  So we want to pull that color around a little bit or the edge and just shrink it down  a bit and then we can change the erode here so that's those two areas where we just pull  it around to make a nice clean plate so we just play with that a little bit.  So we want to try and keep as much as the blue screen as possible but lose as much as  the person.  So now we've got our clean plate we feed that into our delta keyer and we c...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_006.jpg

### Garbage Matting and Refining the Key [6:54]
**Transcript:** going to add a shape here drag that over here and again if I hold down alt I can feed  it into the delta keyer and then make this the garbage map.  So now if I click on this and drag and make a shape around here just making sure I don't  cross over it with my hands and then I'm going to invert this and so now it's getting rid  of all that stuff and I'm just going to soften this area here by changing the soft  texture.  And then to see the result of this kind of moring context I like to put this over a solid  color so I'm just going to grab a background here and then make that some sort of ugly  color that when I put the output of this over the background and look at the result then  I can kind of see a moring context of what we're going to get.  So what I'm going to do next is add another clean plate to do an edge extend so I can make  the colors around these edges more it'll sample from these colors a little bit further  in there and it'll hopefully pour some of that color around.  I'm also going to go into the delta keyer here and change the spill color so we can improve  this by adding a bit more red in there, taking out a bit of the blue and so we're getting  a nicer edge there...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_007.jpg

### Advanced Edge Extension Techniques [8:16]
**Transcript:** space and add another clean plate.  Here we are and then I'm going to add a blur node, blur node there and then feed that  to the input there.  So we've got a blur node and then we're going to feed the blur node into the garbage  mat of the clean plate and then we're going to look at the result of the clean plate and  I'm going to change the mask to be inverted.  So at the moment you can see it's pulling in all of this.  If I change my blur, I make my blur bigger.  It's kind of this is the area it's going to extend.  It's going to take whatever these pixel colors are here and it's going to extend them out.  So I want to thicken up this mat a little bit.  So what I do is I grab our color curves here and then I turn off the red green and the  blue and I just boost the alpha.  I'm thickening up that alpha.  So now it's going to pull from these colors, these edges here.  It's going to extend that.  So then I go to my plate and then I use the grow edges here and we extend that.  So now it's going to extend that color into where it would normally be a little bit black  or a little bit blue.

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_008.jpg

### Channel Booleans and Final Alpha Refinement [9:38]
**Transcript:** Now if I go to my result at the moment it's using the solid alpha of this.  If I go into here, so we need to basically put this alpha on top of this clean plate.  And so we do that by adding a channel Boolean here.  Drag that onto that one and we make the delta key the background and we also make it the  mask.  And then we put our clean plate into the foreground of this and press two to see the result.  And then but if we look at that alpha, we need to change our alpha to the alpha background.  So we're going to keep the original alpha.  And then we go to our result down here.  And then we've got a bit more of our color sample pulled through around our edges.  And it's a bit strong.  So I'm just going to knock it back here under the clean plate.  We go to settings and then we just mix that back a little bit like that.  You see here, like getting a dark edge and pulling it, I'm going to get a nicer edge  like that.  I'm getting a little bleed through here.  So I'm just going to go into my delta keyer into the mat and then just change my highest  and just to clip that out.

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_009.jpg

### Exporting for Lit vs. Unlit Materials [10:51]
**Transcript:** There we are.  So at this point, we could write these files out as a DWA EXR sequence because they are  pre-multiplyte, which means they're over black.  And then in Unreal Engine, when we use Composure, we would use these with the Unlit Alpha  material.  But in my case, I'm using the lit version because we want to have the interactive light  from the environment affect the actual color of our composite mesh actor.  So that will need the edge extended version, the un-pre-multiplyte version.  At this point, I'm just going to create a sequence, an image sequence using a save us,  so save us, add a save us, and then we go into that and then we hit browse into file name,  then we navigate to our directory, and then we give them a name and then use a period  after it because then it will write the frame number and then the file extension.  So hit save.  And now if I was wanting to render these, I would go into Fusion and render all savers.  If that's the only saver that I've got.  If you've got others in the script somewhere, it'll write those two.  So best to just deactivate those.  Okay, that's what I would do, but since I want my un-pre-multiplyte edge extended versions  for my lit ma...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_010.jpg

### Stage 3: Setting Up Composure in Unreal Engine [13:35]
**Transcript:** So we're in Unreal Engine and I've opened up my old animatic and what I'm going to be  doing over the coming months is replacing my digital characters with just placeholders  for my live action characters.  And then I'm going to be improving the fidelity of all the spaceships and the environments  and getting it ready to make as a live action short, which will be the beginning of the  actual film, which is a live action feature.  What a fun.  So this I'm basically going to do a quick recap of what we did in the last video about  how to import that image media sequence and use it on a composite mesh object.  So I kind of will skip over some of these things because you can just watch the previous  video and then I'll get into the differences between the improved version, which is using  that lit composite mesh material.  So we'll be able to use lighting on the actual projected images and we'll also improve  the edge quality when it comes to rendering.  So that's exciting, isn't it?  Yes, it is for me anyway.  So you need to make sure that you've got the Composure plugin active.  So you go into Edit, Plugins and then you search for Composure and then you can see this  one's active and...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_011.jpg

### Creating the Composite Actor and Plate Layer [15:05]
**Transcript:** There we go, Place Composite actor.  And now with the Composite actor we've got our main render layer, which is this and we've  got our shadow reflection layer, which is what we will use when we're using a live action  full plate and then putting digital characters into that and it kind of, that's the first  video that I did with Walfe and into the shadows and stuff onto the plates.  But on this one we're not going to be using that because we're going to be just using  a plate layer and this is where we project whatever's going into this texture onto composite  mesh geometry inside our composite actor scene.  And now with our composite actor we associate our composite actor with the camera and I'm  going to use the camera that I made for my animatic and so we go and go into camera and  then I know that it's called to be camera component.  So now if I go to my plate layer, so the plate layer will project whatever this image is,

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_012.jpg

### Projecting Footage onto Composite Mesh Geometry [16:00]
**Transcript:** either a live signal or our image media sequence, it'll place that onto any object that you  associate here with a composite mesh content.  So I'm going to add an object here that we're going to project this material onto.  So I'm just going to go and add a shape and a cylinder.  So I've got a cylinder here and I'm going to put it here roughly where this character  is.  So I'm going to use that effectively as a screen that I'm then going to project this onto.  So we associate this mesh with this composite mesh content so we can select our model here,  our cylinder and then we drag it into our composite mesh content and then we tell it to  use, select that button there and then you write mouse button and you apply a lit or  unlit and we're going to apply the lit mass material.  And now it's projecting this through the camera onto this object.  So to change this for our image media sequence, we're going to bring that in and we go to

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_013.jpg

### Create Media Texture [17:03]
**Transcript:** Rimehouse button media image media source, call it IMS, plate, double click on that and  then we go and find our image sequence path, our image sequence, select the first frame  and I'm just going to hit open.  So there it is.  This is going to select the edge extended version.  So we save that.  So now we've got our image media plate.  We need to create a media player and a media texture.  So Rimehouse button media media player and then it'll say do you want to create a media  texture asset at the same time you say yes.  Now with our media player, give it a name and then we're going to double click on it  and then we're going to find that image media plate that we just made.  If I double click on it, it'll put it into there.  So that's going to play that in there.  Great.  Let me say okay.  Now the media texture is going to read that media plate.  So now under here under our texture on our composite mesh actor, if we push that into

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_014.jpg

### Create Media Track in Sequencer [18:16]
**Transcript:** there instead of playing that simpty bars, then now play that video.  So now we need to add a media track.  We're going to go to our first frame and now we're going to add our media track and media  track under media track.  We add the media source and R's was called IMS plate.  And so at this frame, we're at 24 frames a second, which is matching our sequencer and  it's saying missing media texture.  So we go right mouse button properties and then under here in the media texture, we have  to associate it with our one called plate MP plate.  And now when we scrub through our timeline, you'll see that it's updating.

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_015.jpg

### The Dither Opacity Mask Fix for Smooth Edges [19:00]
**Transcript:** And then this was kind of what I did before except one thing I wanted to do is because  this is a lit mass material, it's going to give you a binary on or off edge.  And so what I needed to do was to add a diva into the edges and the diva is thing that  does the newsprint.  However, I'm going to change what I did because for two years now, I've been doing this and  I've always had this issue with this cross hatching, not kind of softening, but we've  figured it out finally.  Hi.  Okay, so I'm going to go and find this texture, the actual composite mesh texture.  So I select my model and it's using this M mid comp thing and this is basically this  texture here.  So we need to find this lit mass material.  So the way to find it, if we use this search button here, it just finds you're seen, but  if you hold down old and you see now it looks like a pencil, if you click on that one, it'll  open up the instance and then if you click here, it'll find the actual one in the engine.  So we don't want to edit this, we want to make a copy of this.  So M composite mesh lit mass.  So we go right mouse button and we duplicate this one and we give it another name.  We call it a Dean on the end.  D...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_016.jpg

### Enabling Environment Lighting on Composite Meshes [22:31]
**Transcript:** So I'd have my plate layer.  And then if I wanted to do a colour correct on this, I'd come down to here and the media  passes.  I'd go plus and add a colour grade pass there.  And now I can come in and I can change my gain.  So I was doing that.  But as we move through our time, this is not being affected by the lighting.  And thankfully we've got our animated light on set.  But it's kind of a roof.  So if I'm going to take this light here, there's our little light bulb.  I'm just going to crank this up.  So now we've got this light here.  Now if I want this light to light up this plate, the thing you have to do is you have  to turn off the plate layer.  So if you just disable this, da da.  So now if I move this around, it's actually affecting the plate as well.  At the moment that shape is just this big cylinder.  But if you made that shape more humanly shaped, which I'm going to try an experiment on  the next video, then we'll get much better lighting.  But in this case, I can move this around and it's affecting that.  And you can see it's also making it glossy because it's using the material underneath

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_017.jpg

### Adjusting Specular and Roughness for Realism [23:45]
**Transcript:** there.  So I'm going to go into my composite mesh material.  And then we go into the specular and the default is one.  So we make that zero and we'll make it dull.  And then we also change the roughness to one as well.  And then we hit apply.  Now if I come out of here, you can see that's gone away.  So now when we move this around, he'll be not shiny, which is a good thing.  And then one other thing is that I'm going to add a multiply near to darken this down

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_018.jpg

### Creating a Multiply Color Parameter [24:20]
**Transcript:** or to change the color of it.  So if I turn this off, you can see it's a bit bright, especially if I compare him to the  plate layer.  So now I'm going to go back into this material.  And then over here, after the composite texture, I'm going to add a three constant value.  And I'm going to make this gray.  And I'm going to add a multiply, M. So I'm going to multiply our RGB by this constant.  And then I'm going to swap these two for that.  So this one goes into here.  It says normal.  And the other one goes into here.  It says false.  Now if I hit that, hit apply.  Well, actually, it's on plate layer.  This turn plate layer off.  Now if I hit apply, it says darken it down.  And I can make this darker still.  So let's just go for, okay, hit apply.  So it's a bit too dark.  Let's go and push him up a bit.  And then I can expose this.  Let's make this in a parameter.  So you go right mouse button, convert to parameter.  And I'm just going to call this multiply color.  Color.  And I've hit apply now.  And close this up.  Now I forget to the sequencer.  And I select my composite mesh cylinder.  Bring that into here.  And then under the plus button, if I say static mesh component, then ...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_019.jpg

### Animating Lighting and Using Simulate Mode [26:29]
**Transcript:** Now while we're in here, with the plate layer off, if I change my time, then you can see  that this isn't updating.  So the way to get it to update is you can either just turn this on and off, on and off  like that, and then it'll update.  Or if you want to see it scrub, you're going to simulate mode.  So you press play up here on this one, which is the simulate.  So now as I scrub through, we'll see it update.  And then here I've got my animated light, and I'm animating the brightness of this red  one.  So I'm just going to make it a bit stronger.  You can see as this light animates now, it's lighting up me.  And then I'm just going to undo all of that on my light.  It's going to send you back to normal.  And the other thing that I had on my scene, to help mirror the flickering that I had on  the set, that's my room, is I've also got a light right in front of here, a big rectangular  light.  It'll flicker on the background and also on the plate.  Again, helps you tie it all together.  So I'm just really happy that we've got all of this extra control for doing compositing  type techniques, but in the engine.  And there's one more thing that I wanted to show you.  And currently, our...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_020.jpg

### Composite Mesh vs. Screen Space Texture Mode [27:46]
**Transcript:** So composite mesh is our piece of geometry, and it's projecting our image from our camera  onto that geometry.  And if we come away from the camera, they're actually linked together.  So if I turn this camera off and then move this around, we can kind of move away from  our object, which is really fun.  But one of the issues you can get, sometimes when you're rendering, you might notice you're  getting some hard lines.  And it's sort of relative to the actual geometry itself.  So I might get some kind of weird normals and stuff like that.  So the way to fix that is, I think if you increase the resolution of your geometry, that'll  help.  A bit like one of those subdivided mesh kind of issues that you can get.  But the other thing is if you go back into your main camera, so if we go back into our  main camera, I'm just going to turn that back to lit mode.  If you go into at the bottom of this, so we've got our plate layer selected, and then we  go to mode, and we change that from composite mesh to texture, that now is screen space.  So this will give you the best fidelity that you can get.  However, if you turn off your camera, it's relative to the screen.  So that is the disadvanta...

**Frame:** tutorials\frames\green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-\frame_021.jpg


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
