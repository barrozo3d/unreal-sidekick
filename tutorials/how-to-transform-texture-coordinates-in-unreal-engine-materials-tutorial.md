---
title: How to Transform TEXTURE COORDINATES in Unreal Engine Materials (Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=Wb9hJqPcAwQ
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial/
frame_count: 10
---

# How to Transform TEXTURE COORDINATES in Unreal Engine Materials (Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=Wb9hJqPcAwQ)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 15m51s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction to Texture Manipulation [0:00]
**Transcript:** So I have an object with a texture on it and I want to rotate the texture, scale it or translate it about.  And I want to get how, so I've made this video, so remember how to use a texture coordinate in a material.  So inside Unreal Engine, and I'm going to create an object, put a material on it with a texture,  and then I'm going to animate that texture in the sequencer.  So we go and grab a plane, so square plus button shapes and then a plane, through.

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_000.jpg

### Creating a Master Material and Importing Textures [0:32]
**Transcript:** So there's our object, and now we're going to create a material.  So in our content browser, write mouse button, material, material, and then mm from master material, and then plane.  And then we're going to bring it in our texture.  So write mouse button, import current folder, there's my texture.  And then we go into the material, and there's our base material, and then we're going to bring in the texture, just drag it into there,  and then we're going to connect our RGB to our base color, and to our missive.  And now we hit apply, go to lower this, and then find our plane object, and then drag our material onto that plane.  So there's our object, now I'm going to go into my material.  So now we've got our texture, and then normally from here, you've got this one says UVs.

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_001.jpg

### Using the Texture Coordinate Node [1:21]
**Transcript:** From that, we're going to pull out a noodle, and then it's going to look for texture coordinate here.  And then this allows you to apply math functions onto your texture coordinate.  Now texture coordinate, normally with the UV tile, you've got these little islands of UVs,  and UVs are effectively wrapping paper, so this is going to take this image, and it's going to wrap it onto this geometry,  depending on where these polygons are.  So as I select these, and you can see where it's corresponding on this tile.  So normally you don't want to select everything, this would be your texture coordinate,  and then just moving the whole thing, because you can see here it's doing crazy things to your textures,  basically messing it all up.  So that's not a good thing, but what I can do is take my logo, and then just put it in this area,  and here is the corresponding piece of tile that I would need to put it,  but I'd need to scale it, rotate it, and push it around, and say I've got some monotographics,  I could put it over here in the material, so that's one of the reasons why I would do it.  So first thing I want to do is add an add math function.

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_002.jpg

### Setting Up Texture Translation (U & V) [2:32]
**Transcript:** And now the add is expecting two coordinates, we want the u and the v, so we need a two constant.  But if you use the two here, if you press two, these don't allow you, I don't think so anyway,  allow you to manipulate them nicely in the sequencer to make a parameter out of them.  So I add an append, so we go to the b here, and I'm going to drag a noodle out and look for append,  append vector, like that, and append is looking for two values, and it's going to make the first one,  the u and the second one, the v. So we're going to add a one to create a constant, I think they're called constants,  and then we're going to convert it to a parameter, write mouse button, convert to parameter,  and we're going to call this one trans u, okay, and then we're going to drag that into a,  and then we're going to make another one by pressing one, and then write mouse button, convert to parameter,  trans v, or you can say x and y, whatever, anyway, then we're going to drag that on into our append.  So now we've got nothing, we're not doing anything, but in fact we are, but we're just doing it by zero.  So if I click on my trans u, and then change the default value to say,  oh, you can see it mo...

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_003.jpg

### Texture Tiling vs. Clamping [4:12]
**Transcript:** sample, if you go under here in this little triangle, it's saying sample source from texture  if you change that, the default is, is a wrap, which means that it just tiles the texture,  but if we go to clamp, it will just have one instance of that texture. So now if I translate this  along, you can see it's, we've pushed it all the way off, which is great. Okay, so we've got an ad,

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_004.jpg

### Adding a Custom Rotator for Texture Rotation [4:41]
**Transcript:** next thing I want to do is I want to rotate the texture. So to rotate, we now go into here,  we drag this, we drag it off, and I'm going to now add from here, so we're going to go and drag a  noodle and look for custom rotator, custom rotator here, I'm going to feed this into the UVs here.  So now this is looking for a rotation angle, so I'm going to press one,  drag it into there, and then I'm going to make this parameter to, write my sputon, convert to  parameter, rotate, and then the default value is there, if I turn this, you can see that,  oh there it is, it's rotating it, the nice thing is it's rotating it from the center,  not from the original center of the image, which is up here. So if I go back into my position there,  and then I go into my rotate, it'll rotate it around there. So it depends which order you have  these, so this is the order to have them. So you do add here, that's your translation, then you put  your rotation, and now we've got our rotation, and we've got our translation, and so next thing

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_005.jpg

### Scaling Textures using "Scale UVs by Center" node. [6:01]
**Transcript:** you want to do is do a scale, and there's a new scale, her scale was really hard, I was trying to  figure out a nice way of doing it, and I was getting all confused, but then found, if you come off  here, there is a one, I think it's a newer one, I think it's in five, it's not in form,  called scale, by center, so scale UVs, by center, you put that in there, and now it's looking for  a scale value, you could, if you want to do a uniform scale, which means that both sides of the  same amount, you could just put in a one parameter here, I'll just do it, if we go one, put it in here,  and then let's just convert that to a parameter, and then if I go in here and I change the value,  like that, you can see, like it's scaling uniformly, so that's great, very nice, but I want to scale  my x and my independently, so I'm going to add an append node, try to get a node, go append, append vector,  so that's now looking for two values, and so we will go for press one, put it in there,  press in one, press the click on there again, then we're going to convert these into parameters,  scale U, and then this one here, convert to parameter, scale V, and they're both default zero,  that's why we see ...

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_006.jpg

### Creating and Applying a Material Instance [8:13]
**Transcript:** instance, so write mouse button, create material instance, MI, plain,  and we double click on now, before I do that, I want to then apply that material instance onto  this piece of geometry, it should look the same, now if we go into this material instance,  now here under global scale at parameter values, these are all the ones that we just made into  parameter in our master material, so we can, we can now turn on this, and if we animate this here,  you can see it live in engine doing its thing, so that's why you do that, because it's brilliant,  it's brilliant, let's move that across like that, there we are, so we can turn these on, and then we  can move our things like that, boring, boring, boring, boring, boring, now if we want to animate these in

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_007.jpg

### Animating Texture Parameters in Sequencer [9:20]
**Transcript:** our sequencer, then we're going to first create a sequencer, so write mouse button, cinematics level  sequence, and then open up our sequencer, now what we do is we add, slow with this down, we're going  to add our object into our sequencer, so grab our plane, drag it into our sequencer, and then  under here, under the plus button, we're going to go into the component, so go into here,  static mesh component, and then under our static mesh component, we'll see the one to slot for  lambda, our material parameter, so if we go under the material parameter there, add that, then in here  now, if I go to plus, these are all of the ones that we just made our parameters, so we can add  the rotate in here, and that's our current setting, so we can move it here too, like that, so we can  so put it here, and then we've actually, I've got keyframe on this button here, so it's actually  saved a keyframe there, move my timeline, let's go and rotate another way, like that now,  we've got a rotation, so I can add another one there, another one there, woo woo woo, so now this is  going to be rocking, look at that, brilliant, and so you can go in there, hit plus, you can add our  translation, and ou...

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_008.jpg

### Combining Textures with Linear Interpolate (Lerp) [11:11]
**Transcript:** and this is what we had earlier, and then I'm going to take this image and then lurp them together,  and linear interpolate, and then put that over here using the power of the map, so I'm going to go into  the master material for this object, and it's using a master material, and when you buy things from  fab, like I did for this object, this is from Decagon, it's great, they make wonderful assets,  and not sponsored, and in here, often they'll use a master material, and they've got some fancy  setups with normals, and speculars, and blah blah blah blah, but all I care about is adding something  into the base color, now it's not normally a good idea to add it into your master material,  because any material instance will be, this will trickle down into, but for now, and the sake of speed,  I'm going to add it into my master material, so I'm going to take the demo material made,  and that's our group of fancy nodes, so I'm going to select all of these, control C, and then go  back into our master material, I'm just going to paste them, control V, into there, into here,  and now what I want to do is I want to combine this base color, which is this is the Albedo,  and they've got some...

**Frame:** tutorials\frames\how-to-transform-texture-coordinates-in-unreal-engine-materials-tutorial\frame_009.jpg


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
