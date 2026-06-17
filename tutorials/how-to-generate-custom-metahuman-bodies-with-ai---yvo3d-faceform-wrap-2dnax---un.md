---
title: How to Generate Custom Metahuman Bodies with AI - YVO3D, Faceform Wrap, 2DNAX - Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=5j6wwCsWpD0
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.5"
tags: [custom-metahuman, ai-character, yvo3d, faceform-wrap, 2dnax, maya, metahuman-creator, body-generation, ai-pipeline, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un/
frame_count: 32
---

# How to Generate Custom Metahuman Bodies with AI - YVO3D, Faceform Wrap, 2DNAX - Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=5j6wwCsWpD0)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 35m30s | 32 section(s)

---

## Raw Data (for Claude Code extraction)


### Welcome back & intro [0:00]
**Transcript:** Well, well, well, welcome back to the AI Medi-Human Pipeline tutorial, part 2, the BODY  game.  That's right, this is an intermediate to advanced tutorial.  It ended up using some software that I wasn't really planning, but we'll get to all  that in a minute.  But if you're going to cry about it, you can get out.  Hello, everybody.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_000.jpg

### Why this tutorial is needed (spaghetti arm issue) [0:35]
**Transcript:** So this is a direct continuation of the tutorial that started right before where we learned  how to set up an AI-generated Medi-Human head.  And this video is how to generate a body and combine it with the head.  So we split up the workflow because we got a much better head generation when doing  that on its own.  Well, this is how we create a body that will match the head and, you know, we can attach  it in Medi-Human creator.  So this tutorial, I think, is going to just be a placeholder for this pipeline.  And the reason is it ended up taking, you know, some other pieces of software that I would  prefer not to is that just kind of made the workflow a little bit more complicated than  I would like.  You may have already tried this yourself and run into this, but if you try and use an  AI-generated mesh in the Medi-Human creator for the body and, you know, use the auto-rigger,  it breaks the arms.  You know, the joints just don't quite line up properly and you get this crazy spaghetti  arm thing, which obviously makes it unusable.  So this issue doesn't seem to happen so much if you use, you know, a marketplace character  that you are converting to a Medi-Human.  This really only s...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_001.jpg

### Tools required (Maya + 2D Nax) [2:20]
**Transcript:** And you didn't have to use Maya or, you know, all these other rigging tools to do it properly.  And unfortunately, you know, because of this issue with the joints lining up in Medi-Human  creator, we do have to use Maya and a third-party plugin that you can still try these tools  out for free.  And you know, Maya has a 30-day free trial and the plugin, which is called 2DNACs, uh,  is also available for free for personal use.  So if it's really important that you get, you know, your AI body done, you know, you  can follow this tutorial and you can finish it.  And my goal is that I will do a follow-up tutorial later as soon as this issue is fixed with,  you know, Medi-Human creator, um, or the AI mesh or something, you know, maybe another  tool comes out that makes this process cheaper and easier.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_002.jpg

### Collaboration with Zen [3:15]
**Transcript:** I will definitely do like a follow-up to this tutorial.  But for now, you know, I wanted to make sure that I got like the part two out in a reasonable  amount of time from, uh, you know, releasing the first one so that you can in fact finish  the tutorial.  Oh, and one more thing, you know, just like the first tutorial was this has been a big  collaboration between myself and a community member from my discord named Zen and, uh,  he has his own YouTube channel and he has done a ton of research, uh, and, you know, in  figuring out this pipeline and all the different pieces of software.  And he actually recorded the tutorial starting from Blender all the way through Maya and, uh,  2DNACs and all that.  But I do narrate over the top of it.  So, um, yeah, I don't plan to make tutorials, you know, in this format, you know, in the  future, this was just a kind of as an experiment and see if it saved some time.  But, um, anyway, I think you'll still find the tutorial is, uh, you know, relatively easy  to follow, uh, but it definitely leans heavily on the first tutorial.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_003.jpg

### Generating the body in ChatGPT & Evo 3D [4:22]
**Transcript:** Okay.  Great.  Okay.  So here we are in chat GPT and here is a new image of a head that I generated using the  exact same prompt from the first tutorial.  And I just wanted to generate a different character for this, just kind of keep it, uh, fresh.  And then I have this new prompt here that is meant to generate the body and you paste  in your picture of the head just like this and, uh, execute the prompt and this will generate  a body that will match, uh, your head here and preserve, you know, it'll, you know, grow  the skin out and, and so on.  And of course you can, um, you know, add some modifiers, you know, so down here I added  muscular physique with bi-organic plating, you know, but you could say, you know, make  them, you know, green with boils on their skin or something like that or, you know, even  give them some clothing, uh, which I haven't played around too much with, uh, doing it on  the body itself, but no reason you couldn't do that.  Um, so anyway, I ended up getting this, which I was pretty happy about.  Uh, there is one thing though, you know, you'll notice that the arms here, um, you know,  they don't exactly match the metahuman a pose, uh, the default metahuman...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_004.jpg

### Adjusting arm pose for better wrapping [6:25]
**Transcript:** And it doesn't, it doesn't have to match the, the a pose as you'll see, we ended up doing  the tutorial with, uh, with it in this pose.  Um, it just helps with, you know, when you do the wrap process, it'll help get the arms  a little bit more accurately.  And then you're going to bring your images over to YVO 3D.  And as you can see, I've already, uh, generated the body, you know, so that's what that full  body image generated, uh, I ended up getting this guy here.  And you'll also see, you know, I did the head as well.  And, um, you know, this entire process for the head is covered in the first tutorial,  but I just, you know, use this new head because I wanted to make a new character.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_005.jpg

### Blender setup & exporting meshes [7:08]
**Transcript:** Uh, anyway, uh, just like in the first video, you upload your image down here, uh, first  you select the poly count and, you know, you can just drag it all the way up.  Uh, you know, you might as well get as many polygons as you can since it's going to be doing  the head as well.  Um, then you're going to upload the image, uh, using this button here.  And then you want to make sure the textures are at real 4K.  And, uh, yeah, and then you'll just hit generate and, um, you know, something like this  will come out the end.  And then you can download that file.  All right.  So here we are in Blender in object mode.  And as you can see, we've brought in both the body and the head mesh and we've got them,  uh, in here like that.  And you can remember from the first tutorial that, uh, you know, we brought the mesh into  Blender in order to export all of the textures as well as convert it into an OBJ so that  we can bring it into wrap.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_006.jpg

### Wrapping the body in Faceform Wrap [8:14]
**Transcript:** And you know, we've gone ahead and just done that in this tutorial already, just just kind  of saved some time, you know, so if you need to know how to do that, go ahead and check  that out in the first video.  All right.  Over to face form wrap.  So we're going to pick up right where we left off.  So imagine you just finished your head.  You can actually copy all of these nodes.  You can copy and paste them right next to where they are right now in this workspace here.  So just go ahead and select them and paste them off to the side there.  And we're going to use this exact same setup for the body.  And here you can click these little light bulbs over here to hide the first meshes.  And we can come back over here to our new meshes.  And let's replace this head mesh with the full head and body combined metahuman mesh that  I've provided in the tutorial files.  So you can go to the drive folder that I've linked in the description and you're going  to go to the body and head combined topology folder.  And you want this one, the metahuman combined OBJ.  This is what you're going to download and load into that load GM node in wrap.  So the metahuman body goes in this load GM node on th...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_007.jpg

### Aligning points & fixing mesh issues [10:13]
**Transcript:** So if you remember, we want to make sure that the numbers are staying the exact same  for the point count on each side.  And you can see we're clicking on things like the joints and making sure those points  are aligned.  We are making sure the palvuses are lined up here.  And you can also adjust the height scale of the meshes.  We're lining up the toes here.  We've got one on the big toes and one on the pinky toes.  Now you'll see, Zen actually makes an error here with lining up the points.  He has a couple on the wrong feet.  And that causes an issue with the mesh later in the wrap phase, but we fix it.  All right, that's looking good.  And then what we want to work on is we want to get a rough head as well.  It's not as important since we already wrapped the head.  But we do want to get a rough one so that it lines up well in metahuman creator.  So go ahead and add some points and really focus on the shoulders as well.  Like you can see, we're really lining up like the collar bones and the top of the peck  muscles, the top of the shoulders, and then in the neck there as well.  And if you're having trouble with that material, remember you can always change it by clicking  that to...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_008.jpg

### Wrapping results & saving output [12:30]
**Transcript:** getting confused there.  But that's okay.  We can actually fix that in metahuman creator just by blending some feed in.  So don't worry about that for now.  But if you want, you can select the brush type and you set it to relax and just kind of  relax it a little bit and that will help fix it later.  And then you can just right click on the brush node and go to save output.  And we're going to just jump right into metahuman creator.  Okay, so here we are in metahuman creator and we're going to just drag import our  wrapped full body and head.  So just go ahead and import that.  And here you can set your mesh to the full body and head and switch this to fit from

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_009.jpg

### Importing into MetaHuman Creator [13:23]
**Transcript:** mesh only and import.  And there we go.  And you can see the foot issue which will fix really quickly by going to the blend tab.  And we'll just pull in Bruce to one of the blend sort of spaces and then grabbing those  little circle things you can start to fix the feet and you'll have to kind of, you know,  you'll have to blend some of the other body parts like here you can see we're fixing the  shins in order to get the feet to line up better.  And we kind of have to just kind of move up the body and blend in a proper metahuman  body to make sure we're fixing anything, you know, any issues with our AI mesh.  And you can kind of go around and as you can see we're just kind of messing with it,  seeing what looks best.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_010.jpg

### Fixing feet, hands, and joints with blending [14:10]
**Transcript:** And you know, like the hands in particular, you know, they're kind of mitteny, but we  can change them, blend them into the metahuman hands a little bit and that will help a lot.  And same thing with the forearms, you know, anywhere where there's joints, you know,  we might want to be a little bit more conformed to, you know, the original metahuman mesh.  So you know, we have to sort of sacrifice some of the, you know, shape of our original  mesh in order to get it to work properly.  And but I think that's looking pretty good.  So I think we can go on to the head now.  Okay, so now we can go to the head tab on the left and let's go to the conform section.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_011.jpg

### Aligning the head & fixing neck issues [14:57]
**Transcript:** And under alignment options, change it to scaling rotation and translation and click  adapt neck.  And we still have an issue, but if you go up to transform and click align neck to body,  that should fix it.  And that's looking pretty good.  You know, we can see that it's matching our character in wrap pretty well.  You know, it's a super thick neck, but I think that should work well.  And then you can see there's some issues in the head in the face, like with the eyes  and the mouth, but you can always bring in a, you know, go to the head section and go  to the blend tab and you can start blending in a different, you know, metahuman head  to kind of fix things like the lips or the eyes and just kind of give you a little bit  more, you know, you can shape the face a little bit.  And it's not going to be exactly what it originally looked like, but it's a way to kind  of fix those errors.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_012.jpg

### Exporting body textures from Wrap [15:54]
**Transcript:** So now we need to get the body textures from wrap.  And if we go back to wrap, we'll click on the transfer texture node and you'll see  that it's the head and we need to switch some of these UV numbers.  So down here where it says you go to the very bottom and the bottom right and change it  from 25 to one.  And then where it says you change that to one and that will change it to the body UVs.  And you know, that's that's because we have the combined metahuman head and body mesh.  And this is just selecting the body texture.  So then go to the extrapolate texture node and you can right click on that and that's  where you can export the textures from, save the output rather.  And of course, you know, do that for the normals as well where you'll, you know, you'll  change out that load image node at the very top.  Great.  And so now we can bring in those base color and normal textures for both the body and  the head.  And we can just drag and drop them right into Unreal, bring those textures in.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_013.jpg

### Importing textures into Unreal [17:02]
**Transcript:** Now let's go to the materials tab in our metahuman creator section.  Make sure to check enable texture overrides and then under face add two slots and under  the body and three texture slots normal for the face slots and then base color normal  and body underwear mask for the body.  And we're just going to select a black texture to go in the underwear mask.  And then, you know, we're going to put the base color for the face and normals in those  proper slots.  OK.  And so obviously you can see the materials don't match exactly.  You know, this is just kind of the, you know, the product of doing the body and the face  separately, the, you know, the AI mesh generators and going to get the materials the exact  same.  And, you know, obviously we have this seam.  You can edit kind of the coloring here just in Unreal Engine by just opening up the textures  and you can play with things like the saturation, you know, the vibrance and, you know, contrast  to kind of try and get them to match a little bit better.  You know, but obviously it'll be much easier if you just bring this into either like substance  painter or Photoshop or something like that.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_014.jpg

### Matching materials & fixing seams [18:21]
**Transcript:** But you know, for the most part, you, you know, you can get it to match pretty well here.  You know, if you can adjust the body texture here, you know, we're going to go and just  bring the saturation down on the body texture and that will help kind of match the head  a little bit better.  And we're just going to play with these a little bit more here.  And that's, that's getting there.  That's looking, that's looking all right.  Yeah, something, something like that.  And, you know, you can play with the roughness as well to, you know, change kind of how smooth  the face material is looking.  And, you know, I'm going to come back here and check on the teeth and eyelashes.  With the jaw open, you can see there's still kind of some issues with the mouth.  And we fix that by blending.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_015.jpg

### Fixing mouth issues with blending [19:19]
**Transcript:** So if we go back to the head and blend tab, we can start pulling in some different  heads and just kind of trying them out.  We'll probably want to find a mouth that matches really closely because we'll want to do a  full blend in, in order to get, you know, the entire mouth there.  And so in this case, it looks like we ended up with Kelvin.  And that is looking much better.  Great.  All right.  So we're almost ready to create a full rig for our, our metahuman character.  But of course, you know, you can, if you go to the model tab, you can actually play with  all of these different, you know, sort of parametric parameters.  You know, you, you can adjust it.  You can adjust your AI metahuman body the same way you would adjust, you know, one of  the new 5.6 metahuman bodies.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_016.jpg

### Adjusting MetaHuman body parameters [20:11]
**Transcript:** So you can see we have all these different sliders, all these different controls that  we can use to really, you know, really dial in the shape of our body, you know, whether  we want to make it look a lot closer to the source mesh, you know, we can change like  shoulder width, shoulder height, you know, so whether we're making it look exactly like  the, the source mesh or we just want to make some adjustments, you know, now that we're  here in metahuman creator, that's all, that's all good.  And we can use all of these sliders to do that.  You know, you can increase the muscularity, masculinity, fat height, you know, just feel  free to play with those things.  If you try and adjust, you know, the neck stuff, you'll see that is going kind of crazy,  not a lot of leeway there with us sort of marrying the head to the body.  You know, if you mess around with this and it gets really out of control, you know,  you can always go back to the head tab and go to transform and just click a line neck  to body.  But I think for the most part, you know, you could use the sculpt tool as well to kind  of push some of the geometry around, you know, there we were getting a little bit of control  ov...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_017.jpg

### Downloading textures & creating rig [21:53]
**Transcript:** We're just checking the materials here.  I think it looks fine for the most part.  We can save that and we can download the 4K resolution textures.  And that will apply, you know, the face textures and the body textures from many human  creator.  And you can see we've got kind of those maps in there.  And for some reason, clicking the actual create full rig button got cut out, but make  sure you create the full rig.  And then you'll be able to select a body, ROM animation.  And there we go.  You'll see the, you know, the auto rigging bug that we have after we add a rig to our metahuman.  So this is what we want to fix using Maya and this other plugin by 2DNAC Helix edit.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_018.jpg

### Preparing Maya + 2D Nax setup [22:45]
**Transcript:** And so we're going to walk through that step.  And fortunately, this is free to use for personal and academic use.  So you will be able to at least have followed the tutorial for free.  And same thing goes for Maya.  They have a 30 day trial so you can use it for free.  Anyway, and there isn't too much to installing the plugin.  Just run the install tool for 2DNACs.  And we're just using the provided default project destination folder.  We're not selecting like a custom one or anything like that.  And then you want to make sure you have the metahuman for Maya plugin installed to your  engine.  And that's going to go into your plugins folder in the marketplace section of the plugins  folder.  So go in and find that.  And you want to actually run the executable that's in there.  And make sure that is going to wherever you have your engines installed.  So usually your Epic Games folder.  As you will see here, we have it in there next to our engine.  Now in Maya, you want to make sure you actually have your metahuman plugin enabled.  So do that by going to Windows and Settings Preferences and click on the plugin manager.  Then type in metahuman and make sure this Python script, both th...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_019.jpg

### Exporting MetaHuman from Creator to Maya [24:30]
**Transcript:** And that should be good.  Hit assemble.  Make sure you save beforehand though because it can crash.  And then click assemble and that will build out your metahuman.  All right.  So let's go back to Maya and get our character imported.  So here we are.  We can go up to our metahuman menu up here.  And we're going to want to bring the character that we just exported into here.  So let's go down to the character assembler here.  Click on that.  And assuming that's pointing to the same directory that you exported it to, you should see it  there.  Make sure all of these things down here are selected.  Yeah, whatever these defaults are, that's fine.  Just hit assemble.  And yes.  And there it is.  We have our metahuman imported.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_020.jpg

### Importing into Maya & showing rig issues [25:23]
**Transcript:** And now I can show you what is going wrong with the rig here.  So if you come up to show and go to viewport and turn on the bones, you'll see the skeleton  here, right?  You can see that the shoulder joints and the elbow joints just aren't where they need to  be.  And that's why it's getting all messed up.  So we are going to use the 2DNACS tool to fix the skeleton really easily.  And that will make our rig work properly.  So let's go ahead and turn the joints off.  Again, we're just going to turn off that visualizer.  Then come over here to the rig on the left.  And let's expand this.  And we want to un-parent the LOD0 mesh of the body from the rig.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_021.jpg

### Using 2D Nax to rebuild skeleton [26:11]
**Transcript:** So hold down shift P.  And then un-parent it from the rig.  And then we want to do the same thing for the head as well.  That all that head geometry.  So we want the head all the way, the eyes, the cartilage, all that.  Hold down, select all of those and hold down shift P again to un-parent those from the rig.  And then you can actually just select the rig and delete it.  So we're left with just the geometry itself for both the body and all of the stuff in  the head.  So as you can see, we have just the body mesh and the head mesh.  Now something to keep in mind is the 2DNAX plugin only works with the 2023 and 2024 versions  of Maya.  It doesn't work for 2025 or 2024.2.  All right.  If you come up here to the windows and then go to the plugin manager, there's a problem  where if you have both the 2DNAX plugin and the metahuman plugin enabled, it can cause  it to crash.  So we're going to disable the metahuman plugin and then enable the 2DNAX plugin.  So just go ahead and do that and you can go ahead and close.  And now we can go up to our 2DNAX menu here and go to the character editor under shapes  modeling.  And that will bring up this window here, which is the plugin.  So for sta...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_022.jpg

### Rebuilding character in 2D Nax [29:29]
**Transcript:** So over here under Character Prepare, make sure you have the right project and character  selected.  And we're going to click Body Prepare and select Male for the DNA file.  And this will take a second and there will be the whole body.  And you can go ahead and save that.  Okay.  And if we hit editing mode, that is going to now add the head with the face rig.  And as you can see, that's looking pretty good.  And if we go and show the joints with this little button, you'll see that everything is  where it needs to be.  The elbows and the shoulders are in place.  The face appears to be all in place.  So you can actually come over here and click Prepare Character and then hit Save.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_023.jpg

### Checking fixed joints & controls [30:25]
**Transcript:** And that should get our character ready.  You can come up here and you can see we have the Metihuman Control Board here and you  can kind of click around on here.  Just like you wouldn't Unreal Engine and you can see that the rig is working properly.  That's looking good.  Move the eye around.  Great.  But over in your plugin, you can go to the Character Editing tab and click Export Character.  And we want to select Male if it's a Male and obviously Female if it's Female and then  click Prepare for Export and that will kick out the DNA file and then you can click Export  Character.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_024.jpg

### Exporting character DNA [31:10]
**Transcript:** And that's going to get your character ready to bring into Unreal Engine.  So if we come here, we can see we have the full body DNA files as well as the FBX files  here.  So this Metihuman DNA will be Unreal Engine 5.5.  So I'll show you really quickly how you can convert it to 5.6.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_025.jpg

### Upgrading DNA to Unreal 5.6 [31:34]
**Transcript:** So back in Maya, bring up your plugin manager and we're going to turn off 2DNacks and turn  on our Metihuman plugin.  And then you can come over to your Metihuman menu over here and we want to go down to Expression  Editor.  So select that and upgrade Metihuman DNA under Tools.  And you can find the source DNA, just find the DNA that you just recently exported.  So go ahead and select that.  And the Target Metihuman DNA, just give it a name.  This is what you'll be exporting it as.  So AI, fix, for example, and upgrade.  Great.  And that will say it's exported.  And now you can come back to Unreal Engine.  And we can actually just drag, drop, import our head and body LODs.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_026.jpg

### Importing meshes into Unreal Engine [32:31]
**Transcript:** We can just bring those right into our Content Browser.  Make sure if you have any offset rotation, you can reset that to zero since you won't  need that anymore.  And yeah, make sure you save everything.  And as you can see, we're bringing in the body as well.  And we will have both the body and the head skeletal meshes in here now.  So now you can go back to your Metihuman Creator where we were working on our character and  click Remove Rig.  And you can come over here.  We're going to reset the body and we're going to reset the head as well.  OK, now you can go to Body and click Confirm.  And we're going to select our Body Skeletal Meshes, the LOD one, and put it in the mesh  asset area.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_027.jpg

### Re-importing body & head with fixed rig [33:20]
**Transcript:** And make sure you have fit from mesh and skeleton, and then hit Import.  And there we go.  We have our body.  And then you can go to the Head tab and go to Confirm.  And you could use the static mesh, but you probably want to use the Skeletal Meshes.  We already made so go ahead and swap that one out there.  And make sure that you, your under Scaling Options select None and uncheck Adapt the  Neck and then click Confirm.  And then under DNA File, you'll want to go and find those that fixed DNA file that we  created.  Import Whole Rig selected.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_028.jpg

### Importing DNA & verifying rig works [34:10]
**Transcript:** And so what we're doing here is instead of clicking Create the Full Rig and having it  do it automatically, we're importing the rig that we made in Maya.  And it is identical to the Metahuman one.  So it should work just perfectly with our normal pipeline.  If we hit Import, you'll see it snaps to its default A pose and we'll select a ROM.  And if you hit Play, it is working.  So yeah, you know, there's some issues here.  You can tell like under the Arms and so on, which can be fixed by getting the initial  body pose in the mesh generator to match the Metahuman A pose a little bit better.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_029.jpg

### Common issues & fixes [34:56]
**Transcript:** And I'll show that in the beginning of the video, how you can kind of fix it with the  prompt and silhouette image.  But I think that's going to do it for this video.  It's getting a little bit long and the process to fix the next scene in Substance Painter  was just a little bit long for this video.  But we will definitely cover that very soon.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_030.jpg

### Outro & next steps [35:18]
**Transcript:** And yeah, thanks so much for watching and let me know what you guys create.  Feel free to come by the Discord and show what you're working on.  And yeah, thanks a lot and I'll see you in the next one.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un\frame_031.jpg


---

## Structured Notes

### Core Technique
Generate an AI body mesh in ChatGPT + YVO3D, wrap it to MetaHuman body topology in Faceform Wrap, import into MetaHuman Creator, then use Maya + 2DNAx (free for personal use) to fix the auto-rigging spaghetti-arm joint alignment bug — exporting a corrected DNA file that can be re-imported into MetaHuman Creator for a fully rigged custom AI body.

### Summary
Part 2 of Charlie Driscoll and community member Zen's AI MetaHuman pipeline, focusing on generating a custom body mesh to accompany the AI-generated head from Part 1 (creature tutorial). The core challenge is that AI-generated meshes cause joint misalignment in MetaHuman Creator's auto-rigger (spaghetti arms). The solution requires Maya (30-day free trial) and 2DNAx plugin (free for personal use) to rebuild the skeleton at correct joint positions and export a corrected DNA file. The tutorial covers: ChatGPT body generation prompt, YVO3D mesh generation, Blender export, Faceform Wrap body topology wrapping with combined head+body mesh, MetaHuman Creator import and blending to fix mesh errors, texture transfer from Wrap, Maya import via MetaHuman plugin, 2DNAx character rebuild, DNA export, UE 5.5/5.6 upgrade, and re-import to MetaHuman Creator.

### Key Steps
1. Generate body reference image in ChatGPT using provided body prompt (paste head image + body modifiers); upload to YVO3D for 3D mesh generation with 4K textures.
2. In Blender: import GLB; extract base color, metallic-roughness, and normal map textures (Shading tab → Image → Save As); export as OBJ.
3. In Faceform Wrap: copy head wrap node graph; paste beside it; load combined MetaHuman head+body topology OBJ (provided in tutorial files); load AI body OBJ; align correspondence points on shoulders, pelvis, toes, neck.
4. Run cartoon wrap; save output (right-click brush node → Save Output).
5. In MetaHuman Creator: import wrapped combined OBJ (fit from mesh only → import); use Blend tab to fix foot/hand/joint issues by blending in standard MetaHuman body parts.
6. Align head using Head tab → Conform → Scaling/Rotation/Translation → Adapt Neck → Align Neck to Body.
7. Export body textures from Wrap: change UV number to body UVs in Transfer Texture node; save output; import base color and normal into Unreal.
8. In MetaHuman Creator: enable texture overrides; add body texture slots (base color, normal, underwear mask); create full rig (note: rig will have spaghetti arms bug at this stage).
9. In Maya: enable MetaHuman plugin (Windows → Settings Preferences → Plugin Manager); import character via MetaHuman menu → Character Assembler; confirm in target directory.
10. In Maya: un-parent body LOD0 mesh and all head geometry from rig (Shift+P); delete rig, leaving geometry only.
11. Disable MetaHuman plugin; enable 2DNAx plugin; use 2DNAx → Character Editor → Body Prepare (select Male DNA); switch to Editing Mode (adds head with face rig); verify joint positions.
12. In 2DNAx → Character Editing: Export Character (select Male); Prepare for Export → Export Character → get DNA file.
13. Upgrade DNA to UE 5.6: re-enable MetaHuman plugin in Maya; MetaHuman menu → Expression Editor → Upgrade MetaHuman DNA; select source DNA → give target name → Upgrade.
14. Import fixed FBX meshes and updated DNA into Unreal; in MetaHuman Creator: Remove Rig → reset body and head → import body/head skeletal meshes → import DNA (Import Whole Rig).

### UE Systems / Blueprints / Settings
- YVO3D (AI 3D mesh generator, $10/500 credits, real 4K textures)
- ChatGPT 4.0 (body generation prompt with head image reference)
- Blender (texture extraction from GLB, OBJ export)
- Faceform Wrap (RAP) — retopology wrapping; Indie license $570 / 30-day free trial
- MetaHuman Creator: Blend tab, Head conform tab, Align Neck to Body, texture override slots, Create Full Rig, Remove Rig, Import Whole Rig (DNA)
- Maya 2023/2024 (30-day free trial): MetaHuman plugin (Character Assembler), 2DNAx plugin (free for personal use, Body Prepare, Editing Mode, Export Character)
- 2DNAx Helix Edit plugin for Maya (joint rebuild for AI-generated body meshes)
- Unreal Engine 5.5 / 5.6 MetaHuman Creator DNA import

### Difficulty
Advanced

### UE Version
5.5

### Tags
custom-metahuman, ai-character, yvo3d, faceform-wrap, 2dnax, maya, metahuman-creator, body-generation, ai-pipeline, ue5

---

## Related Entries
- `how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-.md` — Part 1 of this pipeline (head generation); this tutorial continues from it
- `moveai-unreal-engine-54-motion-capture-short-film-using-custom-orc-metahumans---.md` — production using custom orc MetaHumans created via the professional version of this process
- `how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal.md` — production using custom MetaHumans in OverCrowd crowds
