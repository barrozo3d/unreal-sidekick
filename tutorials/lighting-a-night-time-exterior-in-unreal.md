---
title: Lighting a NIGHT-TIME exterior in Unreal
source: YouTube
url: https://www.youtube.com/watch?v=1LfiYtKDsac
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/lighting-a-night-time-exterior-in-unreal/
frame_count: 0
---

# Lighting a NIGHT-TIME exterior in Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=1LfiYtKDsac)
**Author:** William Faucher
**Duration:** 29m22s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back to William Fochai here.  I want to preface this video by saying that while I'll be using Unreal in this tutorial,  just about everything in this video can be applied to any renderer.  Whether you're using Unreal yourself or Blender, V-Ray, Redshift, Octane, whatever.  It's all more or less the same because lighting is lighting.  And while there are a few technical differences from one program to another, the fundamentals  are all the same.  Now, I get a lot of questions about how to do nighttime lighting because I'll admit it's  tricky.  But before you skip ahead to the good stuff, wait a second.  We need to observe how cinematographers light their night scenes in actual movies.  I promise you, this is going to help you.  Bear with me.  Understanding how movies are lit for night shots is essential to getting a good result.


### Important Film Breakdowns [1:01]
**Transcript:** Let's take a look at some classic film shots here and break down the lighting they used.  And first off, you'll notice when you look at these, you may realize that something feels  a bit off.  That is not real moon light.  You can clearly tell that this is a big, bright, artificial light source.  We can clearly see that the light is coming from two different directions at once, which  is a telltale sign that it's not natural light.  Why don't they just use moon light?  The reason being, it's because moon light is way too dark.  Sunlight is roughly 100,000 lux in brightness.  While moon light is between 0.25 and 1 lux, which means the sun is 100 to 400,000 times brighter  than moon light.  Even with modern cameras with incredible low light performance, it's just not enough light  to nail a correct exposure without getting too much noise in the shot.  You're going to need to crank up that gain or the ISO to ridiculous numbers, and that's  just no bueno.  But secondly, notice how all the shots here are very cold or blue in color temperature.  All of them.  Which is funny, because moon light is actually not blue.  Science tells us that moon light is actually a bit more red than sunligh...


### Skillshare [4:33]
**Transcript:** And that is what we're going to do right now.  We're going to light this shot right here entirely from scratch.  And after a sponsored message.  So a big thank you to Skillshare for sponsoring this video.  As you're all well aware by now, Skillshare is an online learning platform you can use  to find thousands of inspiring high quality classes in order to learn any skills you've  ever dreamt of picking up.  Need to learn about getting started in Unreal for Archivist?  Skillshare had you covered with Yahoo!  Jessams class on Unreal Engine for Architecture.  As a freelancer myself, I'm trying to learn more about SEO and ran fish and introduction  to SEO strategy for entrepreneurs, has taught me just about everything I need to know on  the topic.  Skillshare's classes are curated, they're ad-free, new premium classes come out every  week, and it's worth mentioning that the entire catalog of classes now offers subtitles  in Spanish, French, Portuguese, and German.  So, at first, 1000,000, my subscribers, to click the link down below, we'll get a one  month free trial, so you can start learning right away on the go, even on your phone.


### Getting Started [5:35]
**Transcript:** And now, let's get started in Unreal.  Alright, so now that we're in Unreal, the first thing you're going to notice is that I'm  using UE4, and there are a few reasons I'm not using UE5 at the moment.  First and foremost, because foliage does not look quite as good in UE5 yet, so I'm sticking  with UE4 right now, primarily for stability, and slightly better quality you get with foliage  assets.  And there are a few other reasons as well, but we'll get into that a little bit later.  So you'll see here, I'm pretty much exclusively using Megascans assets here, including the  tree.  The trees are all the brand new Megascans tree assets, so you can recreate the scene  yourself very easily.  So what we're going to do here is we're going to delete every single light in the scene  and start off with a blank slate.  And just like that, you'll see we've got nothing left.  It's totally dark.


### Sky Creation [6:27]
**Transcript:** Let's start from scratch.  So the first thing I like to do before I do anything at all is to establish a sky.  But in this environment, we don't really see the sky that much, but you may want to  have a starry night sky.  So what we're going to do is we're going to go to the content browser and in the engine  content folder, make sure that you have the show engine content button turned on here.  We're going to search for sky and we're going to filter by blueprint class.  And here we have the BP sky sphere.  We're going to drag and drop this into a scene like that and you'll see now we have a sky.  Now this sky blueprint has been around since the day unrelentioned four came out pretty  much.  It is old, but it is pretty useful to get a kind of a basic sky system in there if you  need it.  So what we're going to do now is with the BP sky sphere selected, we're going to go  to the details panel and we're going to adjust the sun height right here.  Turn this down like that.  And next, let's say something like that.  There we go.  And now we're going to change the stars brightness right here and crank that up a little bit.  And you'll see that's a very simple and effective way to get st...


### Moonlight [8:18]
**Transcript:** a directional light and the directional light is going to be our moon light, so to speak.  So I'm going to go to lights and drag and drop a directional light in my scene like that.  I got to move it closer so I can select it more easily.  And two things, make sure we set it to movable.  And in a search detail panel again, I'm going to search for atmosphere and we're going  to turn on atmosphere sunlight.  The only reason I have this checked on is because now I can use the control L shortcut  to move and rotate the directional light and really fine tune it the way I want it to.  It's really just a handy tip that is good to know about.  So what I want is for my moon light, so to speak, to really highlight our hero asset.  And our hero prop here our main subject is this lantern and back over here, right?  So I want to make sure that my directional light is really highlighting the edges here.  I really want it to give a nice rim light to it.  So I'm going to fine tune it kind of like this until it really illuminates all of those  edges because when it comes to lighting nighttime scenes, silhouette is probably the most  important thing.  Silhouette is what you're going to see is what's ...


### Volumetric Fog [10:07]
**Transcript:** The next step involves adding some fog because the fog here, especially in Unreal, is really  going to help us get that depth that we need.  So let's go ahead and create that right now.  We're going to go to visual effects here, exponential height fog and drag it into our  scene.  And just like that, we're starting to get somewhere, right?  It went from looking like total crap to this in one click.  But first, there are some critically important things we need to change before we move on.  The first of which is changing one of your project settings.  We're going to go to the setting tab up top here, go to project settings, and we're  going to search for fog up here.  And here is where you want to have support sky atmosphere affecting height fog.  Make sure this is turned on.  You may have to restart on real.  If you do, go ahead and do so before moving on.  Now once that project setting has been changed, we're going to select our exponential  height fog and go to the details panel.  And we need to set the fog and scattering color to black and set the directional and scattering  color here to black as well.  The reason we're doing that is because exponential height fog is purely add...


### Skylight [17:03]
**Transcript:** The next step involves adding a skylight because we need to kind of go out of skylight to  lift up these shadows a bit because the shadow here are pitch black.  There's no bounce light here.  So the skylight's going to help us with that.  So we're going to click on lights here.  Add a skylight in our scene like this.  And we're going to set this light to movable.  I'm going to set the sky disinterested to one.  And I'm going to uncheck lower hemisphere of solid color.  So now you'll see these shadows.  If I hide the skylight.  See that difference it makes it really helps lift up those shadow.  Now this is a little bit too bright for my taste.  I may actually turn that down to 0.5.  There we go.  So now we've got a pretty decent lighting set up done.  Now we need to arc direct it and make it a bit more bluish because that's the  arc direction I want to go for.  It's what we're used to seeing in movies.  Night time scene do look pretty good when they're lit blue.  Even though if not, technically physically accurate.  So I'm going to select my directional light here.  And in a details panel, we're going to make this color a little bit bluish.  Not too much.  Be very careful not to ove...


### Practical Lights [18:27]
**Transcript:** So the next step involves adding practical light.  So a practical light is an actual working light that appears in the scene.  So it can be a household lamp, a TV, car headlights.  And in this case, it's going to be the candles that are inside each one of these lanterns  over here.  So we're going to go ahead and add a point light inside each of these lanterns.  Like this.  Now this is way too bright.  So I'm going to turn this intensity down to one.  And I'm going to change the color to something more orangey like that.  And I'm going to change it to movable.  I'm going to make sure that it is actually inside correctly.  There we go.  And now I'm going to go ahead and do the same for each and every one of these lanterns  in the scene.  So I will fast forward this.  Now, just like that, adding these practical lights here really helps these lanterns pop  a little bit.  It adds that extra warmth in it.  We get that nice teal and orange look when combined with the blue fog.  So these kind of help add a little bit more interest to our scene.


### Fill Lights & Rim Lights [19:44]
**Transcript:** Now we are about 90% of the way there.  There is still one last thing we need to do before we're done.  And that's adding fill lights and extra rim lights.  So these are not exactly realistic lights.  These are not something that would be physically accurate.  But cinematographers add these extra lights to fill lights and rim lights to accentuate  the shape and silhouette of things.  Because like I said earlier, silhouette and shape is the most important thing when it  comes to night lighting.  You see here the silhouette of the lantern, the silhouette of our hero lantern up here,  the silhouette of the tree of all the trees.  This is what really stands out.  So we're going to go ahead and add some extra little fill lights and some more rim lights  to make certain things pop a little bit more.  Because as you probably notice, it's going to be really hard to get moonlight to shine  perfectly on all the things you want it to shine on because you know, trees are in the  way and when you move one tree, it just cashed in another area that you don't want.  So we're going to take a page from the cinematographers playbook and make our lives a little  bit easier by adding some individual, s...


### Lighting Channels [24:02]
**Transcript:** Now this brings me to my next point and a very important tool that Unreal has and that's  lighting channels.  You'll see here this wrecked light is affecting both the lantern and the tree here.  I don't want the wrecked light to affect the tree.  So I'm going to use lighting channels to make that light only affect this lantern.  So we're going to select this light here.  I'm going to go to the details panel and I'm going to search for channel.  And you'll see here I'm going to uncheck channel zero.  Suddenly, it doesn't affect the tree anymore, but it doesn't affect the lantern either.  I'm going to turn on channel one.  And now I'm going to select this lantern and make sure that it also has channel one enabled.  And now you'll see it gets that rim light, but this light is no longer affecting anything  else in the scene.  See?  Only this lamp.  And that's what we want.  This is a super handy tool for adding rim lights to objects without having those lights  affect anything else in the scene.  Be aware, however, that lighting channels don't work with Lumen and UE5.  So now I'm going to go do the same thing over here on this light here.  And one thing I like to do it well is fake som...


### Recap & Breakdown [27:19]
**Transcript:** Let's break this down one more time just so you have a bit of a refresher.  So we're going to hide these and hide these.  So we started off with absolutely nothing more than just a starry sky added a directional  light to simulate our moon lights.  Then we added the volumetric fog, which honestly took us 80% of the way there.  Like I said earlier, shaping that volumetric fog with other huge props like this in a  scene is key to getting a very moody atmosphere, right?  Then we went ahead and lifted the shadows a little bit with our skylight like that.  Then we added some local practical lights like this just to help simulate that candle light  a bit.  And lastly, we added a whole bunch of fill lights and rim lights to our scene to make some  of these lanterns stand out.  That this is before and this is after before and after.  Now again, this is pretty subjective.  There's no right or wrong answer here.  You're going to have to be the judge and you're going to have to act direct your scene.  So you may actually prefer the before version.  And that's okay.  I just wanted to take the time to show you that it is a entirely viable approach to just  add a whole bunch of smaller light lik...


### Additional Tips [28:37]
**Transcript:** Now the last thing I would do here is render this shot out using the movie render queue,  which I have the tutorial for right here.  And from there, I would just color grade this a little bit in DaVinci Resolve.  Now I do have a tutorial on color grading in DaVinci Resolve coming soon, so be sure  you subscribe so you don't miss it.  Because at the end of the day, the only thing that matters is the end result.  If your shot looks gorgeous, the client is happy, you're good to go.


### Outro & Thanks [29:04]
**Transcript:** And that is how you can go ahead and light a nighttime shot yourself pretty easily.  And guys, thank you so much for watching.  I hope you found this video helpful.  If you did, do consider subscribing and leaving a comment down below.  And as always, happy rendering.



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
