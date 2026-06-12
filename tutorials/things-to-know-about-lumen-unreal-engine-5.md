---
title: Things To Know About LUMEN [Unreal Engine 5]
source: YouTube
url: https://www.youtube.com/watch?v=CFKNoeUPQGQ
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/things-to-know-about-lumen-unreal-engine-5/
frame_count: 0
---

# Things To Know About LUMEN [Unreal Engine 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=CFKNoeUPQGQ)
**Author:** William Faucher
**Duration:** 13m4s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back, so great to see you.  This is such an exciting time to be alive  because with the Unrelaunchin 5 that just dropped,  Lumen is one of the most highly anticipated features,  one that I've been waiting for ever since UE5  was announced last year.  So, to topic of today's tutorial,  it's going to be all about Lumen,  everything you need to know about it,  all its project settings, how to use it,  and most importantly, all its limitations.  So, with that being said, let's get started.  So, just a disclaimer before we get started here,  because this is an early access version of Unrelaunchin 5,  a lot of things are going to change,  a lot of these new features are pretty much misunderstood  at this point.  You know, by pretty much everyone,  myself included, like I'm raining through  the Nanite documentation,  and I have no idea what's happening.  This is such new tech,  I think it's going to take a while before it becomes the norm.  So, take this tutorial with a ginormous grain of salt.  My main reason for making the tutorial today  is most of it that helps you guys  with some of the issues that I ran into  and how I solved them, okay?  So, don't take this tu...


### Project Settings [1:35]
**Transcript:** Okay, so now that we're in Unreal,  the first thing we want to do to make sure  that you know, Lutaman is up and running in your scene  or in your project is we're going to need to go  through the project settings.  So, up in the top right-hand corner here,  click on Settings and open Project Settings.  Let's just get through the boring part first.  Now, you'll see on the left-hand side here,  scroll down and there should be a rendering tab right here.  Make sure you click on that and then scroll down  until you see Global Illumination, Reflections and Lumen.  The current settings right here that I have right now  are the recommends that it in for UE5.  So, now that the boring parts are added away,  let's close this.  So, you can see right here,  the only thing I have in my scene is a skylight  and a directional light.


### Scene Setup [2:16]
**Transcript:** So, I'm going to go check out my lights here.  You'll see I have both skylight and directional light.  If I hide these, everything goes dark.  So, if I enable only the directional light,  you know, already we're seeing really nice  indirect lighting in here.  And if I enable the skylight on top of that,  we're going to get just a little bit more  bounce coming from the sky.  Now, there's several different ways  of controlling the indirect lighting here.  So, the easiest way to get full control  over your indirect lighting is to select your main light here.  So, in this case, the directional light.  And in the detailed panel,  we're going to search for indirect.  And you'll see right here,  we have indirect lighting intensity.  If I think that's just a 10,  you'll see obviously,  our GI is blown way out of proportion,  but this just gives you an idea  of how you have full control over it.  So, if I want to turn it off entirely,  I consider it down to zero.  And you'll see we have no more GI's.  So, I'm going to set it back up to one,  just so you guys know,  this is one of the ways you can control it.  Now, the next way we can control this with Lumen  is to go into your post process...


### Troubleshooting & Tips [5:49]
**Transcript:** So I think most people understand how Lumen works in theory.  It works pretty darn well out of the box.  That's pretty straightforward.  That whole process of indirect lighting  is very straightforward once you know how to control it  and how to enable in your project.  But I think where people run into issues with Lumen  is with things that are kind of unrelated to Lumen  and one of those things is Nanite.  So I think Nanite is pretty new tech.  I don't think many people really understand what it's doing.  I'm not one of those people who know what it's doing.  So I'm gonna help troubleshoot some issues  that I ran into playing around with Nanite and Lumen  and you'll see right here that we have two trees.  And now one of them looks substantially better than the other.  So let's pay attention to the right hand tree here.  And let's zoom in close and now all our shadows  are here and our mesh.  And as soon as we zoom out,  you'll see the shadows just disappear.  And then when you get further enough away,  all the leaves just disappear.  Everything just sitting with their tree,  our tree is just kind of falling apart  as we move further away.  But the other one is fine.  Why is that?...



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
