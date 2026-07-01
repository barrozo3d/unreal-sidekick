---
title: Volumetric Cloud Secrets  [Unreal Engine 4 & 5] Works in UE5!
source: YouTube
url: https://www.youtube.com/watch?v=yolGEIrhu0s
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4/UE5"
tags: [volumetric-clouds, sky, environment, art-direction, cloud-mask, engine-content, materials, rendering, vfx]
extraction_status: complete
frames_dir: tutorials/frames/volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5/
frame_count: 4
---

# Volumetric Cloud Secrets  [Unreal Engine 4 & 5] Works in UE5!

**Source:** [YouTube](https://www.youtube.com/watch?v=yolGEIrhu0s)
**Author:** William Faucher
**Duration:** 15m2s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, it's great to have you back.  The topic of today's video is going to concern  how to direct your volumetric cloud.  Now, anyone who's ever used volumetric clouds  at the under a 4.26 knows that they're kind of limited  in what you can do.  There's not much documentation on how to set these up  to have a bit more control.  But fortunately, Chris Murphy over at Twitter  kind of put me on the right track and be aware  that having full control over the placement  of your clouds is even a thing.  So I gotta get credit where credit is due.  Thank you so much, Chris.  You're the best.  Now, with that being said,  I'm gonna take this to the next level  and show you how you can set up your scene correctly  and have full control over the art direction of your clouds.  No, not you, the creepy clown behind you.  And so, why wait?  Let's go.  Okay, so before we get started,

**Frame:** tutorials\frames\volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5\frame_000.jpg

### Setup [0:57]
**Transcript:** there's two things we need to do here.  So first of which is going to the setting top up top,  click on this and make sure,  and then click on the plugin window,  open up the plugins and here we'll search for volume metrics.  Make sure that the volumetric plugin is enabled  if it's not there,  you're not gonna be able to play the volumetric clouds.  So make sure that's enabled,  restart the engine and we're ready to go.  And before we get started,  there's still one last thing we need to do  and that is paying attention to right here.  So notice in my content browser here,  I've got just my content folder.  There is still one thing we need to enable  to access all the settings that we need for this tutorial.  And you'll notice the bottom right here,  we've got view options.  We're gonna click on this  and make sure that show engine content is selected.  And now notice on the left hand side here,  we've got a whole crap load of other folders.  You're gonna see why we need to enable this real soon.  So hang tight.  Now we're ready to get started  and have a little bit of fun with our clouds.  So the first thing we want to do  is we're gonna create a volumetric cloud system.  So you click on visual effects here, volume metrics clouds.  We're gonna click on this, bring them in,  and you'll notice right away,  we're like, okay, cool, we've got clouds,  but by default, they don't look very good, right?  Yes, in the details panel here,  there's a few settings to be can tweak,  but ultimately you don't have that much control  over the art direction of your clouds.  Now, with that being said,  we can edit the material that is in the volumetric clouds  right here.  And we can play around with these settings like this,  but we don't really have control over  the position of the cloud.  And that is what this tutorial is about.  So I'm gonna close this and let's get to the juicy parts  of this tutorial.  So with our new engine content folders here,  let's scroll all the way down to V  where it says volumetric content.  We're gonna click on this folder  and we're gonna click on the tool folder right here.  Cloud compositing, blueprints,  and we have two blueprints right here,  one called BP Cloud Mask Object  and the other one called BP Cloud Mask Generator.  I'm gonna click both of these  and I'm gonna drag these into the scene.  So you'll see one of the actors,  the cloud mask object is freakishly huge,  it is massive.  I'm gonna just gonna move this guy away,  way, way, way over here.  Now, you'll notice nothing really happened  what's happening, right?  What do we want to do here?  So the next step involves changing the material  that's on the volumetric clouds actor.  So we're gonna select a volumetric cloud actor here  and in the volumetric content,  we're gonna go to content, sky, materials,  and you'll see we have a whole bunch of new materials here,  a whole lot.  So for the sake of this tutorial,  I'm gonna use volumetric cloud 0,3 profiles  underscore billowy, drag this into  the material slot of our volumetric cloud actor.  And now, cool, we lost our clouds with next.  To what we're gonna do here,  we're gonna select this BP cloud mask object here.  And we're gonna scale it up by a lot, okay?  So I'm gonna scale this bad way up to like 24, 25,  or something and move him way further away.  But now, notice how the position of our BP cloud  mask object, it has,  gives us full control over the position of the clouds.  So let me get a bird's eye view here  so you can get a better idea of what's happening.  Okay, so now, now we're way high up in this guy.  We can see that, hey, our cloud is moving around.  If I duplicate this, I can have in many clouds that I want.  Now, obviously the shape of this cloud is garbage.  It looks like a hot steaming pile of crap.  How do we fix this?  So we're gonna select the first one here that I created.  In the details panel, I'm going to go ahead  and you'll notice that there's noise settings.  I'm gonna also click the show debug button right here  and you'll notice we've got a kind of a red marker  showing up around where our actor is, right?  So this debug plane here, it's gonna show us  what the shape of our cloud is going to be like, okay?  So in a noise settings, I'm going to increase  the noise intensity by one.  And now you'll notice, hey, something,  the shape of change totally.  And now we're getting a more interesting shape, right?  Now, see how this looks just way, way, way better.  I'm gonna do the same for the other two here.  Set this noise intensity to one.  And now we're getting some more interesting shape.  So right now, just like that, and just a few steps,  we have some much more interesting clouds already.  I'm gonna break change the tiling or the seed rather  right here.  And let's go back to the ground level  and see how this looks.  So now I'm gonna uncheck the show debug.  And now we have full control over the very position  of all our clouds in our scene.  Now let's say, for example, it's cool  that we can play at the cloud,  but we still wanna have a bit more control  over the look of these clouds.  We wanna push it even further.  So there's two things you can do.  We can go back to our volumetric cloud actor here  and play around with the height of our clouds,  the bottom layer, the height of them,  how tall the clouds are like this.  You can choose, there's no right or wrong setting here.  You can do whatever you think looks best,  but we're gonna do here.  We're gonna select the volumetric cloud actor again  and edit this material.  Okay, so again, like I showed you earlier,  we can kinda choose the density of this material.  We can affect the detail of it.  How much detail there is.  There's a whole plethora of different settings.  Again, there's no right or wrong answer.  You're gonna have to be the judge  and just choose what you think looks best.  Now just keep in mind the cloud mask object blueprint here  decides if this directly affects how your clouds look.  So I'm scaling these up or down, moving around.  This has a huge tremendous impact  on the look of your scene.  So you'll notice there's a whole bunch more materials here.  Let's go ahead and see the name of some of them.  You'll notice that what some of them are called,  for example, profiles underscore paint clouds.  So any of the material that have underscore paint clouds  in the material name, they're not going to work by default.  You're going to need to tweak the master material  for this to work with the cloud mask objects.  Okay, and the reason for that is because these paint cloud  materials are made for another type of cloud painting,  which is outside the scope of this tutorial.  So let's see what happens if I drag this paint cloud material  onto our volumetric cloud material.  Okay, I got a drag drag and drop this here.  And okay, our clouds look different,  but you'll notice if I move the cloud mask object around,  we're not affecting the look of our sky anymore.  It doesn't have any effect on the position of our cloud.  We've lost that ability.  How do we fix this?  I'm going to show you how to change this material  so that this works with the cloud mask object.  Okay, so what we're going to do,  you can feel free to duplicate this material  so that you don't overwrite the original.  I'm just going to show you guys what you need to change  in order to get the cloud mask objects to work with these  materials.  So I got to open up this master material here,  and you'll notice that it is a cluster.  It is such a mess of spaghetti noodles,  but don't worry, there's only one thing we need to change.  And let's go here, you'll see there's a texture object  right here called T underscore cloud mask storm.  Okay, right up here, zoom in right here.  This is the texture we need to change.  You're going to find that in volumetric content,  we're going to go to tools, cloud compositing,  render targets, and why is that?  Because what these blueprints are doing,  the cloud mask blueprint, is that they're creating  a render target.  Basically, this is what drives the position of the cloud.  So you'll see right here, we've got Rt underscore cloud mask  underscore zero one.  Let's drag and drop this in here.  We're going to replace that texture  and hit save in the master material.  I'm going to close this.  And now, finally, now we can move our clouds around.  Now you'll notice they kind of look pretty bad.  Don't worry, we can tweak this.  Did lots of we can change again.  So I'm going to open up that material again  by going to my volumetric cloud.  But I'm going to make a material instance  of the paint clouds, so that we just changed, right?  So right click, create material instance,  and drag the material instance into our volumetric cloud  material.  Open up this instance, so we have a much simpler menu  to work with.  And now I'm going to tweak the bias, bottom noise.  Again, guys, there's no right or wrong answer.  There's no right or wrong settings to use.  It's all depend on what you want in your scene.  I just want to show you guys.  How we can tweak these materials,  how we can affect the look of our clouds.  So don't bother with trying to get the exact setting  here because they're kind of irrelevant.  You're going to have to go around and play with this  to get the look that you want.  Now we have full control over the position  of our clouds again.  And you'll notice they look pretty different.  I think these look pretty cool.  So again, I'm noticing that they feel a little bit too tall,  too stretched vertically.  So what I'm going to do is I'm going to change the layer height  and kind of bring you down to a more reasonable level.  And in our Cloud Mask Object, I'm going to play around  with the noise seat again, and noise timings,  something like that.  And just like that, we're trying to get a bit more control  over the look of our scene.  I got to duplicate this.  And maybe even scale this guy, even way bigger.  And you'll notice that just like that,  it is easier than ever to really  art direct your clouds or your skies  the way that you want them to look.  I hope this is making a little bit of sense.  I know it's a lot of information to take in,  but I'm going to delete all this and redo it from scratch

**Frame:** tutorials\frames\volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5\frame_001.jpg

### Recap [11:24]
**Transcript:** just so you guys can get a quick recap of what you need to do.  So I'm going to select everything here and delete that  and delete my volumetric clouds, done.  Start from scratch one more time.  So we're going to add another volumetric clouds here.  And again, we need to go back and play  through our new blueprints, which  is going to be in volumetric content.  If you don't have this folder here,  don't forget to go enable show engine content.  And then we're going to go to the tools, cloud compositing,  blueprints, cloud max object, cloud max generator.  Cloud max object, I'm going to move this guy away,  head the heck back.  And the last thing we need to do now,  set the scale to 25 or something.  And now we just need to change the material  on our volumetric cloud actor.  So I'm going to go find that in volumetric content, content,  sky, materials, and I'm going to use profiles,  BILOE.  Try this here.  And just like that, now we're starting  to get something a bit more interesting.  It's really simple that it works out of the box.  There's not that much to change.  There's no master materials or complex materials  to set up.  This works pretty darn well out of the box.  You can get in the very stylized looks too.  And again, let's go into the bird's eye view.  Just get a better look at what we're doing.  And then we're going to do the bird's eye view.  Just get a better look at what we're doing here.  Something like that.  And I got to change, of course, the noise intensity  of my cloud mask object to something  that I want to break this up even further.  Same with this thing.  Hit it to one.  Break it up further.  And now we have even better control over  to look at our material.  Now, again, I don't like how tall these are.  So I'm going to go into the volumetric cloud  and change the layer height to kind of bring them down  to a more reasonable level.  And we're starting to get some pretty nice looking clouds here.  So I hope this kind of makes sense.  I know it's, like I said, I know it's a lot to take in.  But now, getting the exact look that you want  is easier than ever.  Having the ability to position clouds  the way you want makes such a big impact.

**Frame:** tutorials\frames\volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5\frame_002.jpg

### Bonus Tip [14:05]
**Transcript:** And when you're really trying to get a shot  to look really good and you got your camera all set up  and you just want to look cloud to look perfect,  this is the way to do it.  Now, just one last bonus tip for you guys  in the event that you want to delete your clouds,  what you need to do is select your cloud mask objects,  delete them, but you'll see, hey,  my clouds are still there.  How do I get rid of them?  You just need to go to your cloud mask generator  in your outliner right here.  And you'll see right here where it says render clouds.  And by clicking that, it's going to update your render targets  and all the clouds that you deleted will be gone.  It's really as simple as that.  And that concludes yet another video.  Thank you so much for watching guys.  Again, if you have any questions or something's not working,  leave a comment down below and I'll try to get back to you  if possible.  I can't make any promises,  but don't take it personally if I don't.  It's not because I'm ignoring you, I promise.  So as always guys, don't forget to like and subscribe.  And I'll see you guys next week.

**Frame:** tutorials\frames\volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5\frame_003.jpg


---

## Structured Notes

### Core Technique
Art-direction of volumetric clouds using hidden Engine Content blueprints: **BP_CloudMaskObject** (controls position/shape of individual cloud) + **BP_CloudMaskGenerator** (generates render targets for the mask system). Replace the default volumetric cloud material with curated Engine Content profiles (e.g., `VolumetricCloud_03Profiles_Billowy`). Position cloud mask objects in scene to place clouds exactly. Enable Show Engine Content to access these assets. ⚠️ "Paint Cloud" materials need a render target texture swap to work with the mask system.

### Summary
15m2s William Faucher tutorial on positioning and art-directing volumetric clouds in UE4/UE5. Problem: default volumetric cloud actor has little art-direction control. Solution: Engine Content cloud compositing blueprints — BP_CloudMaskObject (one per cloud formation, scale ~25, Noise Intensity = 1) + BP_CloudMaskGenerator (generate render targets). Must replace default material with one from Engine Content Sky/Materials folder. Show Debug on CloudMaskObject = red preview plane shows shape. "Paint Cloud" materials: must replace T_CloudMask_Storm texture with RT_CloudMask_01 render target in master material, then create material instance for per-cloud tuning. To delete clouds: delete CloudMaskObjects → select Generator → click "Render Clouds" to clear.

### Key Steps
**Setup:**
1. Plugins → search "volumetric" → ensure Volumetric Clouds plugin enabled; restart if needed
2. Content Browser → View Options (bottom right) → enable **Show Engine Content** → engine folders appear on left

**Place actors:**
3. Place Actors → Visual Effects → **Volumetric Clouds** → drag into scene (clouds appear but look generic)
4. In Content Browser → Engine content → VolumetricContent → Tools → Cloud Compositing → Blueprints:
   - Drag **BP_CloudMaskGenerator** into scene (drag far away; it's large by default)
   - Drag **BP_CloudMaskObject** into scene → set scale to ~25 in Details → move to desired cloud position

**Assign material:**
5. Select Volumetric Cloud actor → Details: Material slot → drag from VolumetricContent → Content → Sky → Materials → **VolumetricCloud_03Profiles_Billowy** (or another "Profiles" material) → clouds take new shape

**Art-direct cloud shape:**
6. Select BP_CloudMaskObject → Details → enable **Show Debug** → red preview plane appears showing cloud shape footprint
7. Set **Noise Intensity = 1** → cloud shape breaks up from generic blob into organic form
8. Adjust **Noise Seed** (randomize shape) + scale (larger object = bigger cloud)
9. Duplicate BP_CloudMaskObject → move to different positions → multiple independent clouds
10. Disable Show Debug when done

**Tune cloud appearance:**
11. Select Volumetric Cloud actor → Details: Layer Bottom Altitude, Layer Height, Cloud Shadow Extent → adjust for altitude and vertical thickness
12. Edit material (open VolumetricCloud material) → adjust density, detail noise parameters; no right/wrong values

**"Paint Cloud" materials (optional):**
13. Paint cloud materials (material names containing "paint_clouds") need a texture swap to work with mask system
14. Open paint cloud master material → find **T_CloudMask_Storm** texture → replace with **RT_CloudMask_01** (from VolumetricContent → Tools → CloudCompositing → RenderTargets)
15. Save master material → close
16. Right-click on that material → **Create Material Instance** → drag instance into Volumetric Cloud material slot
17. Open instance → adjust parameters (bias, bottom noise, etc.) without editing master

**Delete clouds:**
18. Select BP_CloudMaskObjects → delete
19. ⚠️ Clouds still visible until: select **BP_CloudMaskGenerator** in Outliner → click **"Render Clouds"** button → render targets update → clouds disappear

### UE Systems / Blueprints / Settings
- **Volumetric Clouds actor** — UE built-in sky component; place once; add material + configure layer height
- **BP_CloudMaskObject** (Engine Content) — hidden blueprint; its world position = cloud position; Scale = cloud footprint size; Noise Intensity (1 = detailed organic shape); Noise Seed (shape randomization); Show Debug = red preview plane
- **BP_CloudMaskGenerator** (Engine Content) — generates render targets that communicate cloud positions to the material system; also has "Render Clouds" trigger button for clearing
- **VolumetricContent** (Engine Content path) — Enable Show Engine Content to access; VolumetricContent → Tools → CloudCompositing → Blueprints / RenderTargets; VolumetricContent → Content → Sky → Materials
- **VolumetricCloud Profiles materials** — ready-to-use cloud materials that work with BP_CloudMaskObject out of the box (e.g., _Billowy, _Layered)
- **"Paint Cloud" materials** — require texture swap: replace T_CloudMask_Storm → RT_CloudMask_01 in master material; then create material instance
- **RT_CloudMask_01** — render target in Engine Content; what drives cloud mask position; must be referenced in paint cloud materials
- **"Render Clouds" button** (BP_CloudMaskGenerator) — re-bakes render targets; must press after deleting CloudMaskObjects to clear stale cloud positions

### Difficulty
Intermediate. Engine Content not visible by default; texture swap in master material adds complexity but is one step.

### UE Version
UE4.26+ / UE5 (confirmed compatible)

### Tags
volumetric-clouds, sky, environment, art-direction, cloud-mask, engine-content, materials, rendering, VFX

---

## Related Entries
- `unreal-engine-masterclass-animate-environments-the-easy-way.md` — cloud animation via Ultra Dynamic Sky (alternate approach)
- `the-perfect-sky-light-in-unreal-engine-5.md` — sky setup context
