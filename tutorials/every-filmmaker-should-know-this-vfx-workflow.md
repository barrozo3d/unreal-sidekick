---
title: every filmmaker should know this VFX workflow
source: YouTube
url: https://www.youtube.com/watch?v=g4DIDafH4lM
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/every-filmmaker-should-know-this-vfx-workflow/
frame_count: 10
---

# every filmmaker should know this VFX workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=g4DIDafH4lM)
**Author:** Josh Toonen
**Duration:** 21m56s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### The Hidden Secret to Hollywood Visual Effects [0:00]
**Transcript:** Did you know every visual effect shot in every single movie you've seen has to go through this one  step? Compositing. Most people think of compositing as replacing green screens with backgrounds that  are impossible to build yourself. But if you understand the art of compositing, you can take your  video game quality renders and make them look just as good as your favorite Hollywood movies.  That's what I'm going to teach you today. How to add atmosphere, lens flares, and that secret  sauce that makes your shots look more realistic than ever before. I spent the last 10 years working  as a compositing artist and supervisor on Hollywood movies like Star Wars, Riza Skywalker,  and across the Spider-Verse. And the longer I've done this, the more I've realized you can  condense all this knowledge into four easy steps that you'll learn by the end of this video.  We're going to break down this shot from my upcoming course Unreal Filmmaking. With Unreal Engine 5,  you can design and storyboard your movie without being an illustrator yourself and go from idea  to final film using the screenshot method. You can spend all day on your virtual film set and start  designing each shot through th...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_000.jpg

### Use Stock Footage for Instant Realism [1:21]
**Transcript:** node graph, I have my Unreal render. And this is a good start, the lighting all works, but there's  something about it that still feels too perfect, synthetic, and CGI. So the first thing you want to do  if you want to make your shots look more realistic is you need to add real life footage or stock footage.  When working on Hollywood movies, the first thing we're adding every single time is smoke and  atmosphere, because that's exactly what you'd expect to see on a real film set. For this scene here,  if we jump ahead to the bottom of this script and look at the final render, I wanted to capture  this feeling of this whole ship being in meltdown mode, like the whole thing could explode at any  second. So we'll add in dust and atmosphere, but I also want to find some high velocity steam  elements as if pipes are bursting as the ship is about to explode. So in working inside of Nuke,  at the very top of your script, you'll always have your background render. And as we work our way  down this script, we're going to get closer and closer to our camera. So first we'll break down  the stock footage of our smoke and steam elements. And then as we get closer to our camera,  we'll also bre...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_001.jpg

### Layering 2D Elements into 3D Space [4:12]
**Transcript:** 2D stock footage and place it in our 3D world, matching the same exact camera move that we had in  Unreal? Well, the easiest way is with the image plane node. By plugging our stock footage into  these image plane nodes, we can start placing them in our 3D world. All we need to do is plug in  our stock footage into the image input and then we need to plug in our 3D camera.  Now when working in Unreal, it's super easy to export your 3D camera. Inside of Sequencer,  just right click on your camera and then by the export button. And now we can export this as an  FBX file. That means that when we come back into Nuke, we can create a brand new camera by pressing  tab in the node graph and then searching for our camera. And then in the properties bin, we can  read in a file. Just navigate to your file, find that camera dot FBX file. And then we can load  in that same camera move that we had in Unreal. This will allow you to match the movement of your  3D camera. And then by creating multiple copies, we can fill our entire room with this dense  smoke and atmosphere, just like this. Now the first milestone or checkpoint I'm looking for when  blocking in my stock footage like this is that th...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_002.jpg

### Build Depth with Layers [5:40]
**Transcript:** of your stock footage is you want to offset the starting time of the stock footage. If you look  closely, you can see that I'm just using this one piece of stock footage for all the steam  elements in the background. But if I don't offset the timing, you can see here that all the  steams are starting on the same exact frame. It is kind of ruined the illusion of this natural  organic motion that you'd expect on a real film set. So by creating these time offset nodes and  delaying the start time of each stock footage, this will add that real life randomness and make our  entire setup more realistic. Once the motion of our stock footage is correct and everything feels  like it's the right scale and the right speed, the next thing we want to focus on is the depth.  We want to create layers of depth in the foreground, mid ground and background of our image.  When you're setting up stock footage with the image plane node, if I double click on this image  plane here, you can see that we have this distance control. And right now I could lower this distance  to move the stock footage closer to my camera, or I could increase the distance to push it further  away. So the most important thing ...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_003.jpg

### Framing Your Characters with Elements [7:36]
**Transcript:** everything's working correctly. One pro tip here is that whenever I'm setting up a piece of stock  footage in the foreground, you want to make sure that it's not directly covering up your character's  face. When you have fog and atmosphere like this, it can really flatten out your entire image.  And ultimately, the point of all these shots is to make eye contact with your characters,  not to be amazed by all the special effects going around them. So a pro tip here is I like to split  my image into these three triangles whenever I'm setting up stock footage in the foreground.  We want to keep this biggest triangle where our character is completely clean,  so we don't have any atmosphere covering up our character's face. But with these two triangles  on the side, these are going to be our hot zones where we can load up as much dense,  smoke, and atmosphere as we want. Hopefully by looking at this now, you can see that we're loading up  all this smoke and atmosphere on the sides, but we're keeping our character clean the entire time.  Once you're happy with the overall motion and depth of your stock footage, the last thing we need

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_004.jpg

### Color Correction to Blend 2D and 3D Elements [8:34]
**Transcript:** to adjust is the color of our stock footage. Now, whenever you're seeing smoke coming out of a  fog machine or by a campfire, typically you'd expect that smoke to be the color gray, but that's  not what it would look like on a film set. When you have lots of dense atmosphere like this,  smoke isn't just the color gray. Smoke will always become the color of the light that's shining on  it. And because our ship is in meltdown mode, I would expect all this atmospheric fog to become  the color of these red emergency lights in the background. So if I want to color grade our  smoke like you're seeing here, the easiest way to do this is to find the spot after all of our  image planes are merged together, and I can press on the G key to create a color grade node.  Then I can use this multiply control by control clicking on this color wheel, and now I can use this  color wheel to dial in the exact color I want. Now, the best way to do this isn't by looking at the  smoke on its own. It's by looking at the smoke after it's being merged on top of our background.  Once we're previewing our final result, now I can adjust the color using this color wheel here,  and I can dial it in until it's per...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_005.jpg

### Think Like a Colorist [12:27]
**Transcript:** my original render, I'm trying to ask myself, are there any simple creative changes I could make  and isolate the different aspects of my image? For example, at the start of our shot, our astronaut  is looking very, very dark, and he's not punching out from the background. So creating a simple mask  to isolate our character and brighten him up at the beginning of the shot could really enhance  the shot and add a lot of clarity for our audience. Now typically, if you were going to work with  live action footage, you would create a grade node, and then you would create a roto node like we  did earlier, and then you would draw a simple mask around your entire character. And then in our  grade node, we could multiply this up to make it brighter, and we could reduce the gamma to add in  some contrast. But right now, because our roto isn't perfectly aligned to our character,  it's going to look very rough, and we could blur this out like we did earlier, but that means we  need to adjust this roto on every single frame, and it's going to be very hard to get a perfect result.  So rather than doing any of this, there's a much easier way when you render with Unreal Engine.  Let's just delete...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_006.jpg

### Perfect Masking with Cryptomattes [13:34]
**Transcript:** crypto-mat node. And now I can play this back and see the crypto-mat pass from my entire shot.  Now to render this out of Unreal Engine, you need to render out an object ID pass, and this will allow  you to create crypto-mats inside of Nuke or After Effects. So how do you actually use this in a  productive way? We're not going to use the data that we're seeing on screen here. To actually use  this and isolate our astronaut character, if you double-click on your crypto-mat node, and you  make sure that the picker add is selected, so there's this tiny little eyedropper right here.  Once that's set up, we can control-click on all the different objects on our screen,  and this will create a mask for our character. You can also click and drag over multiple masks to  select small details like the hair, eyes, or eyebrows for our character. Now if I press on the A key  to look at the alpha channel, I can see that I have this black and white mask that sticks to my  character for the entire shot. And if I pause on one of these frames, you can see that we even get  the motion blur detail from our character. This will give us a pixel-perfect, accurate mask that we  can use to color grade any p...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_007.jpg

### Easily Create Interactive Lights with Position Data [15:42]
**Transcript:** what if we wanted to make another creative adjustment by adding in a red emergency light in the  background, layering on and off? Well, if we look at our crypto-mat pass, we could isolate a few  of these areas in the background, but this will create a hard-edged mat like we have on our astronaut.  It won't give us this soft, smooth fall-off. So let's use another data pass to do this.  If I view my original render, on the top left, I can see all the different data passes I rendered  out. These actor proxy masks are our crypto-mats, but we also have a world-depth pass and a world  position pass. Now this world-position pass isn't useful on its own. But if you combine this with a  P-MAT or a position-mat node, we can plug this in to our main pipe, and let's make sure that we're  selecting our position data, our world-position pass right here, and then I'm going to swap back our  viewer to RGBA mode. Now if I look at our P-MAT mask, I'm going to click on this center color swatch,  and now I can control-click on any part of my image, and if I press on the A key to look at my  alpha channel, you can see that I have this perfect 3D bubble that can scrub through our entire scene.  This giv...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_008.jpg

### Getting the “Film Look” [18:20]
**Transcript:** Pretty cool, right?  Now the last but most important step to make your shots look more photoreal is we need to imitate  the imperfections of a real camera. The way that I like to do this is I created a template called  the One Click Film Look that you can easily apply to any shot. This takes all the lens effects I'd  normally apply at a visual effects studio and turns them into an easy drag and drop template.  So you can quickly dial in things like lens diffusion, vignetting, and chromatic aberration.  The biggest effect you'll have on your image comes with the lens diffusion.  At the top I have this overall diffusion control, which is the overall mix, and then I have the fall-off  of this diffusion. So if I lower that fall-off, it'll expand all of our light sources to make them  spread out, or we could reduce that glow and make them tighter to each light source by increasing  the fall-off. Typically, I'll set my fall-off to around .75, and I'll dial in my diffusion for each shot.  In this shot, we have this bright torch light that would flare out your camera lens. So we want to  make sure that that's visible, because in the original render, there's no glow or diffusion  happening ...

**Frame:** tutorials\frames\every-filmmaker-should-know-this-vfx-workflow\frame_009.jpg


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
