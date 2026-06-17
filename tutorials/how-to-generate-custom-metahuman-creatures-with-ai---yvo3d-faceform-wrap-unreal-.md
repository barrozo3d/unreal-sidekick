---
title: How to Generate Custom Metahuman Creatures with AI - YVO3D, Faceform Wrap, Unreal Engine 5.6 -Part I
source: YouTube
url: https://www.youtube.com/watch?v=PEObW2odtXI
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.6"
tags: [custom-metahuman, ai-character, yvo3d, faceform-wrap, metahuman-creator, creature, fantasy, ai-pipeline, metahuman-animator, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-/
frame_count: 25
---

# How to Generate Custom Metahuman Creatures with AI - YVO3D, Faceform Wrap, Unreal Engine 5.6 -Part I

**Source:** [YouTube](https://www.youtube.com/watch?v=PEObW2odtXI)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 43m6s | 25 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro: Build Custom MetaHumans [0:00]
**Transcript:** Have you ever wanted to create your own sci-fi or fantasy or horror metahuman creatures,  but don't have the time, money or experience to learn a complicated character pipeline?  Well, in this video, I will show you how to go from a simple, chachypti prompt all the  way to a fully rigged, custom metahuman fantasy creature, ready for professional, great,  facial animation that you can capture with any camera.  You can create endless humanoid creatures with fairly compelling results.  And the best part is we will be using tools that are very cheap or completely free.  So if you want to get started making metahuman creatures as quickly and cheaply as possible,  this one's for you.  Oh yeah, this is all in Unreal Engine 5.6.  So some of my earliest videos on this channel featured custom metahuman creatures like

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_000.jpg

### Past Examples & Limitations [0:50]
**Transcript:** Marvin the Talking Pig, some creepy but jovial orcs, troll, and gigantic joe, a gigantic  Sasquatch.  These characters were awesome, but I couldn't make them myself.  I had to hire talented character artists who used complex tools like Metapype and Maya  to convert these characters I had found on the marketplace to metahuman.  And honestly, as a filmmaker who kind of stumbled into using Unreal Engine, this always looked  way beyond my skill set.  I'm not a traditional animator or 3D modeler.  I'm a guy who figured out how to use some mocap software and metahuman animator, which  isn't too hard.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_001.jpg

### Pipeline Overview (YVO3D + Wrap) [1:45]
**Transcript:** But recently, thanks to a community member named Zen on my Discord, we've figured out  what I think is a very compelling pipeline to generate high quality custom metahumans  using AI tools and without expensive software like Maya.  Now the two main pieces of the pipeline that make this possible are a program called  RAP by FaceForm and EVO3D, the AI3D mesh generator.  RAP is the tool used to wrap the metahuman topology around your AI generated mesh, so that  it can be used in the metahuman creator to generate your custom metahuman.  And then you can use any camera to animate that character's face with metahuman animator.  RAP has an indie license that costs $570, as well as two professional licenses.  But they offer a 30 day fully functioning free trial, so you can follow this tutorial  nearly for free.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_002.jpg

### Cost Breakdown [2:52]
**Transcript:** The only money you will have to pay is a minimum $10 for a subscription to EVO3D.  And that $10 will get you about 4 or 5 mesh generations, and in my opinion EVO3D is  worth it as far as I can tell, but we will get to that in a minute.  So you could use this tutorial to convert any humanoid character to a metahuman, one  that you might find on FAB or a third party marketplace.  You would just bring the character mesh into RAP instead of the AI generated one.  So this means that high quality custom characters like the ones I've used on my channel can become  available to anyone willing to follow this tutorial.  Now we are still working out the body and wardrobe pipeline, but you can see we did have

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_003.jpg

### Works with Any Character Mesh [3:41]
**Transcript:** some success in creating some custom armor for our goblin character.  You will see there is a ton wrong with it, but with the right tools and prompts I think  we can get a pipeline created that would include custom modular clothing.  And I should mention this is not meant to replace a professional pipeline for cinematics  or games, at least with the AI component.  This is very experimental, but as you can see I think it yields really interesting results.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_004.jpg

### Creating Prompt Images [4:23]
**Transcript:** So you will begin the process by creating prompts in chat GPT 4.0 to generate detailed,  accurate reference images.  The prompt itself specifies that the image should clearly show the head and upper shoulders.  The character looking directly into the camera with a neutral expression, mouth and lips  closed, and flat neutral lighting with minimal shadow or specular details.  And once you nail the prompts, which I've included free in the video description, it's  super easy and fun to generate tons of character variations.  I use chat GPT for the image because it had by far the best prompt adherence.  At least for someone like me who isn't much of a prompt wizard, you can see here the  initial image and the final metahuman results and how it changes quite a bit along the  pipeline.  However, I really think the quality of the final result depends on the quality of the  initial input image.  Once your generated 3D mesh needs to fit the parameters of the metahuman generator.  Unfortunately, chat GPT has really strong guardrails, so generating anything like realistic  gore or even mild nudity was impossible.  Including just generating shirtless characters, unless you add stylized to it.  ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_005.jpg

### Zombie Prompts with Mage [5:56]
**Transcript:** called Mage.  And Mage was great for realistic gore, but it was really tough to control and honestly,  the results were a bit too graphic for YouTube.  Even though the 3D generated model and the final metahuman look stylized enough, there  was something about the uncensored images that Mage would think it would get flagged.  Today for the tutorial, instead of doing a zombie, I'm going to do this fantasy dragon-ling

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_006.jpg

### Uploading to YVO3D [6:29]
**Transcript:** character, which was made using the included prompt.  And just to be clear, I'll be making just the head.  The armor that you see in these shots is from the medieval armor pack from Polyphoria.  So after generating the image, you upload it directly to Evo 3D, and this part is fast,  you get a detailed 3D mesh in about 10 minutes at a minimal cost.  Like, I think it's about $2 per mesh with high quality 4K textures.  And as you can see, I generated a lot of meshes.  It was really fun because it got the head meshes pretty accurately, especially once I got  the original image prompt down.  I did try to generate a full body and head mesh combined, which you can then wrap and generate  a metahuman out of.  But you can see that the quality of the head really goes down when you try and generate  the whole body.  And that's why I've pursued this pipeline of generating the head and body separately

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_007.jpg

### Separating Head and Body [7:42]
**Transcript:** and merging them, which is a little more difficult and we're still figuring out, but the  quality is so much higher.  Now these meshes look incredible at first glance, but much of that detail, you know, the  shadows and their reflections, is baked into the textures and not actually modeled geometry.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_008.jpg

### Enhancing Materials in Unreal [8:02]
**Transcript:** However, you can still enhance details significantly by adjusting the normal map intensity in  the material instance in Unreal, which adds a lot of depth and detail under direct lighting.  You can also change properties like the roughness, which is great for metallic characters,  like this robot, or wet or slimy creatures like the mermaid.  You really want to get your initial prompt image to have as few shadows as possible, since  they can get baked into your character material and make it look like they have heavy makeup  on.  And as you will see, the topology of these meshes is not that great.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_009.jpg

### Why Wrap is Necessary [8:43]
**Transcript:** So face form wrap makes retopology super easy.  There's no Maya required.  This part of the process looks tedious, but really isn't too hard and becomes very quick  once you get the hang of it, maybe 10 to 20 minutes.  After wrapping, you get clean metahuman topology ready to head to Unreal.  So finally, we imported into metahuman creator fine tune and used metahuman animator to bring

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_010.jpg

### Importing into MetaHuman Creator [9:08]
**Transcript:** it to life with performance capture.  And the results are honestly stunning, given how little manual effort goes into it.  Sure, clean up is needed, especially around eyes and lips, but it's minimal.  And of course, that depends on what your use case and standards and personal taste are,  for me, this is interesting enough to make this pipeline worth pursuing.  So future episodes will cover generating wardrobes, modular clothing for overcrowded simulation,  and even custom body shapes.  So stay tuned.  Remember this pipeline isn't meant to replace professional character artists, but it opens  up amazing creative possibilities, especially for creating tons of sci-fi or fantasy creatures  like this.  All prompt references and assets are included below.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_011.jpg

### Assets & What’s Coming Next [10:05]
**Transcript:** So please explore, experiment, and let me know what you create.  All metahumans you see in this video, including a pack of eight zombies, will be available  for sale, either on Patreon or Fab.  The link will be below.  Of course, these will be available completely free for my amazing Patreon subscribers,  as well as anyone who purchased a beta copy of Overcrowd, who have all been super patient  and supportive.  And you'll be happy to know that Overcrowd is almost ready for Fab.  It may even be by the time I finish this video.  Either way, the link will be below as soon as that's ready, and you'll know if you bought  it on Patreon as well.  Also huge thanks again to Zen for his help developing this workflow.  Check out his channel link below, and Zen's services are also for sale if you want someone  to create a metahuman for you using this pipeline.  Alright, if you found this helpful, like, subscribe, and please consider joining the Discord.  Alright, keep watching for the full step by step tutorial on custom metahuman creature

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_012.jpg

### Full Tutorial Begins [11:13]
**Transcript:** heads.  Okay, so I'm going to try and show you in the most efficient way possible how I went from  this portrait image that was generated in Chatchy PT40 to a fully functioning metahuman.  So I've already talked about all the different pieces of this pipeline, but I'll just go  over them again really, really quickly right here so you can kind of just follow along.  And so here we are in Chatchy PT40, and you start by generating your reference image  that you'll feed to the 3D model generator.  And the way you do that is using a prompt like this, and this is pretty, you know, pretty  long, and I made it, I tried to design it in a way that, you know, gives a bunch of ideas  for characters.  So the whole idea was something that, you know, people could just take and paste into  Chatchy PT40 and get a reference image of their own and start, you know, generating  right away, and it would have all of these parameters that are needed in order to get  a nice clean generation.  So I will include this whole prompt in the folder of assets that I will link below in  the description so that you can follow along with the tutorial.  So anyway, once you generate the character that you like that is ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_013.jpg

### YVO3D Setup & Export [12:48]
**Transcript:** you'll need to do the $10 subscription, which gives you 500 credits, which I think will  give you about four generations, you know, or maybe two heads and two full bodies.  So not much, but it's enough to do the bare minimum.  And the thing that you want is this real 4K generation.  That is what will give you, you know, the really quality textures.  You know, I suppose you could try the free version and try upscaling it, but yeah, I think  it's worth it for this.  And those 500 credits will go fast, but that will be enough to do a couple generations.  So go ahead and grab that one.  Okay, so let's come over to our 3D AI workspace, and then down here, you'll see where you  can actually prompt the 3D model through text, but I didn't really like the results of  that.  You'll burn through your credits pretty quickly.  It's better to use an image.  So here you'll select your polycount, and, you know, when doing the head, you know,  you can go all the way up to 200,000 polygons, but honestly, it feels a little overkill.  I feel like it, you know, past 100,000, it's not really adding too much geometry.  I guess if you have like a lot of sort of crazy protrusions or something, but for our ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_014.jpg

### Using Blender [15:40]
**Transcript:** Okay.  So we're going to use Blender to convert the model to an OBJ.  So it can be pulled into RAP as well as extract the texture files.  So go ahead and just open up Blender and hit A and delete to delete the default cube  by by cube.  And we'll go to import and we'll do dot GLB.  And then you can just go ahead and select the model you downloaded and import that.  And there we go.  And okay.  How do I move around Blender?  Okay.  Hold down middle mouse and move around.  And then you can switch to the on-lit version here.  All right.  That's looking pretty good.  Okay.  So we're going to extract the textures that come with the 3D model.  So go ahead and click on that and then come up here to the shading tab.  And then that will open up this window.  And down here.  We'll see.  We're looking at the material and these orange things are the 3 textures that are putting together  the material.  So we have our base color that's giving them all the actual color.  We have a metallic roughness mask and then we have a normal map.  All right.  So let's just go ahead and select that.  That'll show up over here.  So this little menu here and go to image and save as.  And here you can see I've a...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_015.jpg

### Wrapping in Faceform Wrap [18:23]
**Transcript:** mesh that we have generated because what we got from the 3D generator from EVO  3D is not a great topology and I'll show you that once we pull it into here.  And in order for it to work with the metahuman creator, it needs to match the metahuman topology.  And so you need a piece of software like this that can take the metahuman topology and  rap it around this.  And so that's how I know how to use this.  And I will show you how to do that right now.  So over here in the graph, we are going to create some load geometry nodes.  So this first one we will use to load the metahuman topology.  So I'll click on that.  And then here you'll see there's a metahuman body topology and a metahuman head topology  that will be included in the project files linked below in the description.  So let's grab the head and open that up.  And when that comes in, let's zoom out here.  It's going to look like that.  So come down here and let's set the rotation to minus 90.  And it's going to be up there and down all to move.  Gosh, every 3D software is like different controls to move around.  Anyway, all right.  So that's our metahuman topology.  Let's go ahead and create another load geometry node.  And ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_016.jpg

### Using Cartoon Wrap [24:29]
**Transcript:** And we're going to start adding points to these.  OK.  So what does that mean?  I'm going to start clicking over here  and assigning points on this geometry  and then lining up corresponding ones on this geometry.  And that's basically to be like, oh, the corner of the eye  on this mesh goes in here.  And like the corner of the mouth goes here and so on.  And we'll do some parts around the horns  to make sure we get some of this geometry to wrap around those.  And the more points you can put the better,  I've been doing between 50 and 100 points  based on how much extra geometry there is.  So we'll just get started.  And we'll see how far we get with this one.  I don't think it should be that many, but we'll see.  So the first thing I'm going to do  is come over to this left geometry tab, which corresponds  to this area over here.  And where it says symmetry, I'm going to turn on x symmetry.  So now you can see as I'm moving my cursor,  there's a corresponding point over there.  So let's just start with these.  And you see there's a one and a two there.  And then you'll see up here, point count is two.  And then over here, point count is zero, right?  OK.  So we want these to stay ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_017.jpg

### Clean Up the Mesh [28:29]
**Transcript:** and it should do the wrap for us.  And now this is sped up about 10X,  but you can see the metahuman topology  start to form over the AI generated topology.  Okay, that's looking pretty good,  but what we wanna do is we wanna actually add another node  over here, wanna add a brush node.  And this will allow us to sort of clean up the wrap.  And the way we wanna set this up is to take the cartoon wrapping  and plug that into the far left node here.  And then we're gonna take this load geometry one.  We're gonna bring it down to this third one here.  And then we're gonna take the other load geometry.  And we're gonna bring that down.  We're gonna put it in the second one there.  Okay, and so it's gonna start to look like this.  So what we wanna do with the brush node selected  is we wanna kinda clean up the geometry here.  And so we've got the wireframe turned on.  And if you don't see the wireframe,  you can scroll over here and click on that.  You can also hide it.  And right now it says display mode texture.  Let's switch this to color.  I think it makes it a little bit easier to see.  And so you can see kinda like these areas  where the meshes creased over all this wrap  did real...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_018.jpg

### Transfer Textures [32:06]
**Transcript:** Rapt.  Save.  This is fine.  And so now we need to get the newly wrapped textures out  as well.  And so we do that with a texture transfer node.  So we'll just grab one of those and put that in there.  And then we wanna take the output of the cartoon wrapping  and we're gonna put this into this middle node here.  And then we're gonna take the output from this geometry  up here and put that into this first node down here.  Okay, and if we have the transfer texture node selected,  we can come up here and click on our viewport 2D  and you'll see that you have the unwrapped,  the properly unwrapped mesh here.  And if you come and look at our input up here,  this is what the texture originally looked like.  So this is what we want to export here.  But you'll see that the resolution is low here.  So we can turn this up to 4096 by 4096.  There we go.  And that looks much better.  And you'll see that there's like some empty space up here.  We can fix that by just adding an extrapolate image node.  So pull that off and right click,  extrapolate image and we'll click on that.  And that should just automatically generate that great.  And now we can right click on this  and we can save this ou...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_019.jpg

### Import to Unreal [34:38]
**Transcript:** All right, so let's quickly make sure we have all the plugins  we need.  So we need to get all of the metahuman plugins installed.  So just search for those and select all of those.  Yes, and yes.  And we don't need that last one and go ahead and restart.  Okay, so the first thing we want to do is import the assets  that we created.  So I'm gonna grab the demonwrappedOBJ that we exported  out of wrap and just drop that right in there.  And what we're gonna do is in the offset rotation,  we're gonna put 90 degrees and let's import that.  All right, and that is looking good.  And let's get the textures in here now.  We want those three wrapped materials.  So you can just grab all three of them and bring them in here.  Okay, and so now we can just go ahead and right click  and we can create a metahuman character.  We'll call this guy demon.  So let's go ahead and open and up we have some  missing plugins.  So just go ahead and enable missing and it will probably  ask to restart and just go ahead and do that.  Go ahead and save.  All right, let's go ahead and open up demon.  All right, and we want to go to the head tab

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_020.jpg

### Rig to MetaHuman [36:10]
**Transcript:** and we want to go to conform and we're gonna go to from template.  And this is where we will select the mesh that we have created.  So let's go ahead and put that in there.  And just go ahead and click conform.  All right, and that looks pretty good.  So this looks really good actually.  Let's go ahead and make that bigger.  This is also the part where if you had something kind of  messed up mouth, for example, you could blend  one of these preset mouths or something and that would fix that.  So if you have some weird deformations or if you want to fix the nose,  obviously we like how that looks, that's what we want it to look like.  But say you wanted to change it to something else,  you just throw that in there and you can change it to a more human  nose, but we don't want to do that.  Okay, great.  Let's see, I don't see anything that needs any fixing.  If we come back to it, let's see,  sometimes I like to go to the teeth and just click that tab  and it will pull back the lips and you can just kind of make sure  the mouth is working properly that way.  But that looks pretty good.  Let's kind of, let's make his teeth like, you know.  Anyway, you can mess around with that.  That ...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_021.jpg

### Textures, Body & Eyes [37:55]
**Transcript:** And we can also change the body over in this tab.  And if you click on the body tab and then come over to model,  you know, you have all of these things that you can change,  you know, you can really sculpt your own, you know,  character as much as you want.  But I'm actually interested in a tab here that should be here.  And that is the, you know, original metahuman bodies.  And you can actually enable that if you don't see that here  in your project settings, you can go up to project settings  and you can scroll down to the plugins over here  and click on the metahuman character  and go to show compatibility mode bodies  and go ahead and close that.  And I think you just have to close the character creator  and just open it back up.  And now if we go to body and model and great,  we have the fixed compatibility  and you can see all the original metahuman bodies there.  So I am just gonna put some armor on this guy  because I don't have time to do the whole body  for this tutorial that will be in a later video.  But let's just do the normal male tall body type.  And that's just because I have like some armor  that can fit this guy.  Okay.  And if you click on the materials tab ove...

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_022.jpg

### Material Tweaks [41:17]
**Transcript:** and here is the demon and we can go ahead  and open up that blueprint.  And you can come and click on the viewport  and zoom on in and that's looking pretty cool.  But if we wanted to modify the material a little bit more,  we could click on that and come over here  and double click on the face.  And in the material instance,  we can come down to the normal  and we can actually increase the strength of that.  I like to turn that up a little bit.  There we go, just make those normals pop a little bit more.  You could go even more if you wanted to.  You can of course change the roughness  and I think we can make him a little slimy or so  we can turn the roughness down.  They'll give him a wet appearance.  And then I have some assets that I've added to my project  that I'm gonna use to help finish this.  So I have some eye materials that are really cool  from these modular orcs  and let's see what would look good on this guy.  If we select the face and come to the eye materials here,  let's go with this crazy demon looking eye.  Yeah, that's kind of cool, right?

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_023.jpg

### End – Final Look & Wrap-Up [42:54]
**Transcript:** And then I'm just gonna slap some of this modular armor  from Polyphoria on this guy and I'm gonna call it a day.

**Frame:** tutorials\frames\how-to-generate-custom-metahuman-creatures-with-ai---yvo3d-faceform-wrap-unreal-\frame_024.jpg


---

## Structured Notes

### Core Technique
Generate a fantasy/sci-fi creature head image in ChatGPT 4.0, convert to 3D mesh with YVO3D ($10/generation), extract textures in Blender, use Faceform Wrap (RAP) to retopologize the AI mesh onto MetaHuman head topology with correspondence-point placement, then import into MetaHuman Creator UE 5.6 to create a fully rigged custom creature MetaHuman that works with MetaHuman Animator.

### Summary
Part 1 of Charlie Driscoll and community member Zen's AI MetaHuman creature pipeline for Unreal Engine 5.6. The tutorial focuses on head generation only: use ChatGPT 4.0 with a specific prompt (included in description) to generate a creature portrait with neutral expression and flat lighting, upload to YVO3D for 3D mesh generation with 4K textures (~$2 per generation), extract textures in Blender (base color, metallic roughness, normal), then perform wrap retopology in Faceform Wrap (RAP) using x-symmetry and ~50-100 correspondence points to map MetaHuman head topology onto the AI mesh. The wrapped mesh and textures are imported into MetaHuman Creator UE 5.6 via Conform from Template, material overrides are set, eyes can be swapped, and the resulting MetaHuman is fully compatible with MetaHuman Animator for performance capture.

### Key Steps
1. Generate creature portrait in ChatGPT 4.0 using the provided prompt (neutral expression, mouth closed, flat lighting, facing camera); iterate until desired look is achieved.
2. Upload image to YVO3D; select polycount (~100K polygons recommended); enable real 4K textures; generate 3D mesh (~10 min, ~$2); download GLB.
3. In Blender: import GLB; go to Shading tab; locate and save three texture maps (base color, metallic roughness, normal) via Image → Save As.
4. Export mesh as OBJ from Blender (File → Export → OBJ).
5. In Faceform Wrap (RAP): create two Load Geometry nodes — one for MetaHuman head topology OBJ (provided in tutorial files, set rotation -90), one for AI creature OBJ.
6. Enable X-symmetry; place ~50-100 correspondence points on both meshes (eyes corners, mouth corners, nose, ears, horns/protrusions, forehead).
7. Add Cartoon Wrap node; connect both geometries; run wrap (result shows MetaHuman topology conforming to creature shape).
8. Add Brush node; connect wrap output; use Relax brush to clean up mesh artifacts.
9. Add Transfer Texture node; connect wrapped geometry; set resolution to 4096x4096; add Extrapolate Image node; right-click → Save Output for base color and normal textures.
10. In UE 5.6: enable MetaHuman plugins (restart if needed); right-click content browser → Create MetaHuman Character; name character.
11. Head tab → Conform → From Template; select wrapped OBJ; Conform.
12. Use Blend tab to fix any deformations (lips, eyes, nose); Teeth tab to verify mouth.
13. Body tab → show compatibility mode bodies (Project Settings → Plugins → MetaHuman Character → Show Compatibility Mode Bodies); select appropriate body type.
14. Materials tab: enable texture overrides; add face texture slots; import wrapped base color and normal; adjust in Unreal (increase normal map intensity, change roughness for wet/slimy look).
15. Swap eye materials if desired (custom eye materials from modular packs).
16. Create Full Rig; download MetaHuman to project via MetaHuman Creator.

### UE Systems / Blueprints / Settings
- ChatGPT 4.0 (character image generation with provided prompt)
- YVO3D (AI 3D mesh generator; $10/500 credits; real 4K textures)
- Blender (texture extraction from GLB: base color, metallic roughness, normal; OBJ export)
- Faceform Wrap (RAP) — retopology tool; Indie $570 / 30-day free trial; correspondence point wrapping, Cartoon Wrap, Brush (Relax mode), Transfer Texture, Extrapolate Image
- MetaHuman Creator UE 5.6: Conform from Template, Blend tab, Teeth tab, Body tab (compatibility mode bodies), Materials tab (texture override), Create Full Rig
- MetaHuman Animator (face capture, fully compatible with resulting character)
- Polyphoria Medieval Armor Pack (for body clothing in demo)
- UE 5.6 MetaHuman plugins (enable in project)

### Difficulty
Advanced

### UE Version
5.6

### Tags
custom-metahuman, ai-character, yvo3d, faceform-wrap, metahuman-creator, creature, fantasy, ai-pipeline, metahuman-animator, ue5

---

## Related Entries
- `how-to-generate-custom-metahuman-bodies-with-ai---yvo3d-faceform-wrap-2dnax---un.md` — Part 2 of this pipeline (body generation + Maya/2DNAx fix)
- `moveai-unreal-engine-54-motion-capture-short-film-using-custom-orc-metahumans---.md` — production using custom orc MetaHumans (created with professional version of this process)
- `how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal.md` — uses custom MetaHumans from 3D Scan Store in gladiator crowds
