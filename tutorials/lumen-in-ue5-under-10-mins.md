---
title: Lumen in UE5 Under 10 Mins
source: YouTube
url: https://www.youtube.com/watch?v=RSImMVfCnYQ
author: Karim Yasser
ingested: 2026-07-08
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/lumen-in-ue5-under-10-mins/
frame_count: 12
---

# Lumen in UE5 Under 10 Mins

**Source:** [YouTube](https://www.youtube.com/watch?v=RSImMVfCnYQ)
**Author:** Karim Yasser
**Duration:** 9m19s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** You might never know that Lumen is ruining your scene performance and yet you cannot get  the target quality that you are aiming for.  So in today's video we will discuss steps for Lumen that will improve your lighting immediately.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_000.jpg

### Project Settings [0:12]
**Transcript:** So first of all we need to go to project settings to ensure we have the proper setup for our  project.  So go here down into rendering and first of all we need to ensure we have dynamic global  eliminations that the Lumen and same goes for reflections method.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_001.jpg

### Software Ray Tracing [0:26]
**Transcript:** And then if we wanted to use software ray tracing which is the cheapest option that  Lumen can use that will work on low profile hardware and this basically is using the  mesh distance fields to trace against and it uses the detailed tracing of the mesh distance  fields for the first two meters and then it fall backs to global tracing which is using  global distance field and it's better and faster for calculation.  So in order to ensure we are using software ray tracing we need to have use hardware ray  tracing when available to be turned off and support hardware ray tracing to be turned off  as well and generate mesh distance fields to be enabled and also we need to go here in  platforms in windows and we ensure we have shader and roll six enabled so we can start using  it.  Software ray tracing is still have some limitations it's not supported for all type of meshes  and it needs a meshes having a specific thickness at least 10 centimeters to ensure we don't  have any light leaking and still it's not supporting a lot of materials or shaders like  the word position offset and there are a lot more that is still limited unlike the hardware

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_002.jpg

### Hardware Ray Tracing [1:29]
**Transcript:** ray tracing which supports a wide variety of options and to ensure we can use it the best  option quality is first to turn off generate mesh distance fields so we are not falling back  to software ray tracing because by default and really get back to it to save some more  performance and then we need to ensure support hardware ray tracing is turned on and use hardware  ray tracing when available is turned on as well and in this method it uses more accurate  representation of the triangles and pixels of the screen so it can have more details in  here and we can visualize it by going to let Lumen and Lumen scene currently it's using  something called surface cache but if we get back here to our project and change it  just little ray lighting mode to headlighting for reflections and also we need to ensure we  don't override it in here.  So now as you can see it has better representation of the mesh is it surface cache it's lower  resolution and this is it lighting for reflections it's already better and even headlighting is  much better and we will go in depth in them.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_003.jpg

### AO With Lumen [2:34]
**Transcript:** Also we need to ensure that we are using better ambient collusion because by default if we  wanted to go here in buffer visualization and scroll down to ambient collusion is set  to white which is not actually working with ambient collusion at all but Lumen is working  with it on its own calculations so in order to have better ambient collusion we have  to go here scroll down for allow static lighting ensure it's turned off and if you want to  use screen space ambient collusion with Lumen you can use these two console commands.  First one is R.Lumen the screen prop gather the short range AO set it to zero and the second  one is R.Lumen.diffuseandar.ssao we need to set it to one and now if we go here in our  boss process settings go to ambient collusion we can control the ambient collusion as you  can see it affects our scene and if we go here in buffer visualization scroll down to  ambient collusion we can see it now so it's working as before and you can override that  with these console variables and you can control it here as well you can increase the quality  of it you can control the power the intensity of these settings and that's instead of keeping  Lumen using its own AO calculations on its own if you want to override it with screen space ambient collusion.  There is another option as well related to screen tracing by default it's set to scene color but I

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_004.jpg

### Screen Tracing [4:01]
**Transcript:** tend to set up to anti-aliasing scene color because it supports translucency in a better way and  it reduces the flickering from the small immersive sources so it will give you much better quality and  more consistent and then here in our boss process settings we can go down and explore these settings.

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_005.jpg

### Surface Cache Vs Hit Lighting For Reflections Vs Hit Lighting [4:19]
**Transcript:** First of all a lighting mode if we go here in Lumen Lumen scene service cache basically is trying to  represent these meshes in a lower resolution so it can get the indirect lighting and reflections  from it but it's not using hardware ray tracing so if you want to use hardware ray tracing you can  go to headlighting for reflections and also this one is really important for mirror reflections or  shiny surfaces so it will give you better reflections in it and as you can see it already has  better details and this one headlighting for reflections it uses better shadowed rays with the  reflection bus so it can give you much better reflections and representation in your scene but it  can fall back to surface cache in the second bounces but here in headlighting it's much better because  it uses these rays not only for reflections it's also using these rays for indirect lighting  bounces and reflections as well so technically this is much higher in cost but it gives you the best  possible quality from Lumen so we can notice it in here this is headlighting for reflections as you  can see it's not perfect in here but headlighting is much better already and this is service cache  the cheapest option possible so let's set it to headlighting which is a best possible option in here  but it's the most expensive option as well there is also an advanced option there is diffuse

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_006.jpg

### Diffuse Color Boost [5:45]
**Transcript:** color boost actually multiplies your base color values or diffuse values in your materials  and that increases the indirect light bounces but this is basically incorrect but it's really useful  if you want to have much better indirect lighting in your scene and it's closer to what actually the  past tracing is doing so if we try to set it to four as you can see it's really really bright  currently and that has a lot of indirect lighting and if we wanted to visualize it we can go to Lumen  Lumen scene and as you can see it's really bright this is one as you can see this is default color  values in here this is two this is three this is four so the max you can go is four and usually  these values are recommended to stay between one and two so you are not multiplying it by very high  number but it could be very useful for areas that you don't have a lot of indirect lighting in  there and you don't want to increase the amount of lights or indirect light intensity in your lights

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_007.jpg

### Sky Light Leaking [6:47]
**Transcript:** also there is a skylight leaking which is really useful if you have a skylight and your interior  is still a little bit dark you can quickly go here and increase the leaking and you might  not sit in here as you can see this is a very subtle here in this scene I actually don't recommend  to use this option a lot except in a few places let's go to reflections here first of all we can

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_008.jpg

### High Quality Translucency Reflections [7:06]
**Transcript:** use a high quality translucent reflection as you can see it gives you much better reflections  on your glass and if you go here in lumen lumen scene and turn off this one and get back here  and ensure it surface cache your reflections will not work really good as you can see here it's  giving you much better details on the translucent or reflective surfaces same goes for max roughness

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_009.jpg

### Max Roughness To Trace [7:37]
**Transcript:** and if we wanted to visualize it better go to let lumen did get it reflection rays and here  everything that is not in red is not getting calculated with lumen reflections probably so what  happens if we increase this number it will start including more objects in there and it's almost  everything added in there so that will give us better reflections so as we can see now this is  before and after it's tremendously changing these meshes in here and giving it better and better  reflection quality as you can see it's already much better and more cinematic but for sure this  affects your performance a lot so if you are aiming for performance you might need to reduce this  number below than you're going for and this is controlled by your roughness maps or your roughness  multipliers in your materials the more meshes you have with lower roughness value that will  affect your performance as well and you might not know why and here for max reflection bounces

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_010.jpg

### Max Reflection & Refraction Bounces [8:40]
**Transcript:** this is related to how many reflections you will see inside your reflections same goes for max  reflection bounces if we try to will give you slight better details in very small objects what the  aim is to get closer to what post tracing can actually achieve so that's basically it for lumen if  you want to have more details we created a session before it was a live session around four hours  and you can get it for free if you joined our community and ask it for your free license of it so  feel free to join the community from the link down below and ask for your free license so you can  get it and watch it thank you so much for watching and see you next time

**Frame:** tutorials\frames\lumen-in-ue5-under-10-mins\frame_011.jpg


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
