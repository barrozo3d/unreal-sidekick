---
title: Things To Know About LUMEN [Unreal Engine 5]
source: YouTube
url: https://www.youtube.com/watch?v=CFKNoeUPQGQ
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [lumen, global-illumination, reflections, shadows, nanite, debugging, performance, project-settings, workflow, emissive]
extraction_status: complete
frames_dir: tutorials/frames/things-to-know-about-lumen-unreal-engine-5/
frame_count: 4
---

# Things To Know About LUMEN [Unreal Engine 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=CFKNoeUPQGQ)
**Author:** William Faucher
**Duration:** 13m4s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back, so great to see you.  This is such an exciting time to be alive  because with the Unrelaunchin 5 that just dropped,  Lumen is one of the most highly anticipated features,  one that I've been waiting for ever since UE5  was announced last year.  So, to topic of today's tutorial,  it's going to be all about Lumen,  everything you need to know about it,  all its project settings, how to use it,  and most importantly, all its limitations.  So, with that being said, let's get started.  So, just a disclaimer before we get started here,  because this is an early access version of Unrelaunchin 5,  a lot of things are going to change,  a lot of these new features are pretty much misunderstood  at this point.  You know, by pretty much everyone,  myself included, like I'm raining through  the Nanite documentation,  and I have no idea what's happening.  This is such new tech,  I think it's going to take a while before it becomes the norm.  So, take this tutorial with a ginormous grain of salt.  My main reason for making the tutorial today  is most of it that helps you guys  with some of the issues that I ran into  and how I solved them, okay?  So, don't take this tutorial as the Holy Gospel.  If so, my tricks here help you out, awesome.  If not, that's fine,  because this is not meant to be a full-fledged,  you know, very well-documented,  very well-researched tutorial.  It's just too early at this point.  So, with that being said, now we can get started.

**Frame:** tutorials\frames\things-to-know-about-lumen-unreal-engine-5\frame_000.jpg

### Project Settings [1:35]
**Transcript:** Okay, so now that we're in Unreal,  the first thing we want to do to make sure  that you know, Lutaman is up and running in your scene  or in your project is we're going to need to go  through the project settings.  So, up in the top right-hand corner here,  click on Settings and open Project Settings.  Let's just get through the boring part first.  Now, you'll see on the left-hand side here,  scroll down and there should be a rendering tab right here.  Make sure you click on that and then scroll down  until you see Global Illumination, Reflections and Lumen.  The current settings right here that I have right now  are the recommends that it in for UE5.  So, now that the boring parts are added away,  let's close this.  So, you can see right here,  the only thing I have in my scene is a skylight  and a directional light.

**Frame:** tutorials\frames\things-to-know-about-lumen-unreal-engine-5\frame_001.jpg

### Scene Setup [2:16]
**Transcript:** So, I'm going to go check out my lights here.  You'll see I have both skylight and directional light.  If I hide these, everything goes dark.  So, if I enable only the directional light,  you know, already we're seeing really nice  indirect lighting in here.  And if I enable the skylight on top of that,  we're going to get just a little bit more  bounce coming from the sky.  Now, there's several different ways  of controlling the indirect lighting here.  So, the easiest way to get full control  over your indirect lighting is to select your main light here.  So, in this case, the directional light.  And in the detailed panel,  we're going to search for indirect.  And you'll see right here,  we have indirect lighting intensity.  If I think that's just a 10,  you'll see obviously,  our GI is blown way out of proportion,  but this just gives you an idea  of how you have full control over it.  So, if I want to turn it off entirely,  I consider it down to zero.  And you'll see we have no more GI's.  So, I'm going to set it back up to one,  just so you guys know,  this is one of the ways you can control it.  Now, the next way we can control this with Lumen  is to go into your post process volume,  select this.  And once again, in the details panel,  we're going to search for Lumen.  And we have a few other controls here.  And what's nice with that now,  you can finally choose which type of GI you want.  We got screen space, you got ray tracing.  I'm going to leave it Lumen for now,  but this is finally where you can control it.  You don't need to enable it  with console commands anymore.  And that's awesome.  Now, Lumen also takes care of reflection.  So not just the indirect lighting,  but also reflections.  So what I'm going to do,  I'm going to go create a sphere here,  and drag this up, make it a little bit bigger,  and slap on a Chrome material.  And now you'll see we have reflections on our sphere,  but you'll notice,  things are kind of blurry and they pop a little,  you know, depending on how far you are from the object.  Now, the way I understand it,  and played correct me if I'm wrong,  but Lumen uses HLODs for reflections in this case.  So obviously, I think you're going to get better results  with raytrace reflections.  So, you know, just kind of,  you can play around with the settings here.  Now that I've shown you how to change that  in a project settings,  feel free to experiment a little bit.  I just kind of want to point you in the right direction,  and talk to you guys about the various settings  and why things behave in a certain way.  So again, go experiment with raytracing reflections  as opposed to the Lumen reflections,  but in most use cases,  I think this is going to be plenty fine,  unless you have really,  you really need those clean, sharp reflections  on shiny objects, for example.  So what I'm about to show you right here,  it's quite possible meet the most exciting part  of the entire Unreal Engine 5 revealed.  This blew my mind during the livestream the other day.  So I'm just going to go ahead and do it again  for all of you who didn't watch the stream.  I'm going to go ahead and create a sphere here.  And on this sphere,  I got to slap on an emissive material.  Now notice just by having an emissive material  on the sphere, the sphere is now a light.  It's actually casting and emitting  not only direct light, but indirect lighting as well.  So if I scale this up way bigger,  notice how this sphere is illuminating this entire area.  The fact that this works out of the box,  this is the coolest thing about Lumen, in my opinion.  Yes, the GI that we get from other tools is great,  but man, I did not expect emissive materials  to emit light and not only light, but indirect light.  So I apologize for acting like a five-year-old on Christmas.  This is just really exciting to me.  So with that being said, let's move on to the next point.

**Frame:** tutorials\frames\things-to-know-about-lumen-unreal-engine-5\frame_002.jpg

### Troubleshooting & Tips [5:49]
**Transcript:** So I think most people understand how Lumen works in theory.  It works pretty darn well out of the box.  That's pretty straightforward.  That whole process of indirect lighting  is very straightforward once you know how to control it  and how to enable in your project.  But I think where people run into issues with Lumen  is with things that are kind of unrelated to Lumen  and one of those things is Nanite.  So I think Nanite is pretty new tech.  I don't think many people really understand what it's doing.  I'm not one of those people who know what it's doing.  So I'm gonna help troubleshoot some issues  that I ran into playing around with Nanite and Lumen  and you'll see right here that we have two trees.  And now one of them looks substantially better than the other.  So let's pay attention to the right hand tree here.  And let's zoom in close and now all our shadows  are here and our mesh.  And as soon as we zoom out,  you'll see the shadows just disappear.  And then when you get further enough away,  all the leaves just disappear.  Everything just sitting with their tree,  our tree is just kind of falling apart  as we move further away.  But the other one is fine.  Why is that?  The only difference between these trees  is that the right hand tree right here is Nanite  and the left hand tree here  is just a regular aesthetic mesh with no Nanite being used.  So Lumen works very well with the aesthetic mesh here.  We got some nice shadows going on in here.  Tonight highlights happening on the leaves themselves.  But the Nanite tree just looks really bad.  And obviously I use this as an example  because Epic has clearly stated that Nanite  and Lumen don't work so well with very thin meshes  because everything is kind of mesh distance field based.  So because of that, having thin, very thin plain models,  it's not gonna work super well.  There's a reason why there's little to no foliage  in the Unreal Engine 5 demo so far.  This is exactly why.  Okay, I'm not saying you can't get good results with foliage,  you can.  That being said, if you're running into issues  with your lighting and your models  or just not looking very good,  try making sure that they're not converted to Nanite.  Import them as a regular aesthetic mesh.  All right?  Importing as a regular aesthetic mesh  could be a very simple way of troubleshooting  what's causing your issues and your scene.  Now the next issue that I've had  and I've seen other people struggle with  is the shadows.  Now you'll see that I've placed a wrecked light  right next to the table in the chairs here  and you'll notice hopefully you can see in the video  but these shadows are incredibly noisy.  They don't look very good and the shadows are a little too sharp  for considering the size of this light.  Ray Trace shadows looked better in 4.26  as opposed to the Lumen shadows.  So how do we fix this?  And of course, in true Unreal Engine fashion,  the solution to this is you guessed it,  a console command.  I'm really annoyed by this.  I really wish that Epic would do away  with these solutions that are solved with console commands.  I just wanna have a slider or a check box something  in the light instead of having to deal  with a million console commands in the project, right?  So the first of which, so paying attention  to the shadows here.  Now the first console command we're gonna use  so going at the bottom left hand corner of the screen here,  it's great because now the console command  is the menu is always there.  And I'm gonna type in the following.  r.shadow.virtual.smrt.raycount local.  I'm gonna bump this up to something like eight.  And now hopefully you guys can see that  the difference there are shadows are suddenly way less noisy.  Okay, and then there's another console command  that we can enable to help with the softness of these shadows.  And that is the following.  smrt.sample.raylocal8.  And then you notice that the shadows got a little bit softer.  They're still not great.  Like this just looks really weird.  We got this kind of just,  we clearly got some soft shadows happening,  but we also have this weird hard shadow happening.  Okay, so this seems to be a limitation of Lumen.  I think it's again, this is a work in progress.  There's still a lot of unknown.  So my understanding is that this is at somewhat  of a limitation of the virtual shadow map that Lumen uses.  And the solution to that is either to back up  a little bit more or use a slightly smaller light.  So notice how if I make this smaller,  the, it does feel a little bit better.  But again, this is not a real solution.  Now I'm not a rendering engineer  so I don't actually know what's happening under the hood here.  I just wanted to show you guys the two console commands  which are found in the Epic documentation.  I will include these console commands  and the link to the documentation  in the description below.  To go check that out, do read the documentation.  There's a lot to unpack here.  I just wanted to troubleshoot some issue  that I ran into myself.  So the last issue that we're gonna talk about right now,  and this is something that you may or may not run into.  This is something that I ran into this morning  and hopefully this helps someone out.  So we're gonna go ahead and create a light up here.  I'm gonna create a directional light.  And I get this light shining in here.  Like that.  Now you'll be wondering, okay,  I need to increase my indirect lighting, right?  To get some of that sweet, sweet bounce happening.  But you'll notice I'm not getting any bounce whatsoever.  No bounce at all.  Why is this?  Now the reason I couldn't, you know,  try bumping up my intensity perhaps, right?  And this is more of like a screen space GI.  This is not the true lumen that we've  going to custom to seeing in the exterior level.  And the reason why I'm not getting any proper  indirect lighting in my apartment scene here,  is because of this H.D.R.I dome here, okay?  I have like a dome texture.  This is from an ever motion package.  And so I have a dome out here.  And it's not casting shadows.  No shadows are cast, but even though there's no shadow  being cast, it's in fact, it's blocking the light,  even though the light is shining in my scene.  So if I go ahead and I delete this, suddenly,  notice how boom my apartment scene is flooded with light.  All that GI works now and everything works as expected.  So I'm going to turn down my indirect lighting again,  because obviously way too strong.  But now we've got some some good proper GI now.  That's the reason.  So lumen uses some kind of ray tracing under the hood.  Even though the light was shining through the window,  just fine, it wasn't the GI aspect of lumen,  it was not able to reach the inside of my apartment scene  because of that H.D.R.I dome.  So it's important to keep that in mind.  This is one of the things I just kind of had to fiddle around with  and discovered by accident.  So hopefully, I'm not the only one who ran into this issue.  Hopefully, it helps you out or some of you out at least.  And so guys, that concludes this tutorial.  This was very much a crash course.  This is not intended to be a full,  fledged lumen tutorial.  This is still early access.  Things are going to change,  but I figured I'd help you guys kind of figure out  what some issues are running to or  and what those solutions to those issues can be.  Was that being said, thanks so much for watching,  and I'll see you all in the next video.

**Frame:** tutorials\frames\things-to-know-about-lumen-unreal-engine-5\frame_003.jpg


---

## Structured Notes

### Core Technique
Early UE5 Lumen crash course and troubleshooting guide. **⚠️ Note: recorded during UE5 early access — some information may be outdated.** Three specific issues addressed: (1) Nanite thin-mesh foliage breaks Lumen shadows → disable Nanite on foliage; (2) noisy/harsh local light shadows → VSM console commands `r.shadow.virtual.smrt.raycount.local` + `smrt.sample.raylocal`; (3) HDRI dome mesh blocks Lumen GI rays even when casting no shadow → delete the dome.

### Summary
13-minute William Faucher early UE5 release crash course on Lumen. **⚠️ Early access era — treat as foundational but verify current behavior.** Covers enabling Lumen in project settings, controlling indirect lighting via `Indirect Lighting Intensity` on lights and PPV Lumen settings, emissive materials as light emitters (highlight moment — Lumen casts GI from emissive), and Lumen reflections (uses HLODs; ray trace reflections better for shiny). Three troubleshooting scenarios in depth: Nanite+Lumen incompatibility on thin meshes, noisy VSM shadows (two console var fixes), and HDRI dome silently blocking all Lumen GI for interiors. Author acknowledges this is early days and recommends checking Epic's documentation.

### Key Steps
**Enable Lumen:**
1. Edit → Project Settings → Rendering → Global Illumination: **Lumen**; Reflections: **Lumen**
2. Scene needs at minimum: Directional Light + Skylight

**Control indirect lighting:**
3. Select Directional Light → Details → search **Indirect** → **Indirect Lighting Intensity** (0 = no GI from this light, 1 = default, 10 = blown out GI)
4. Post Process Volume → search **Lumen** → set GI type and Reflections type (Screen Space / Lumen / Ray Tracing)

**Emissive materials as lights:**
5. Apply emissive material to any mesh → it emits both direct and indirect light via Lumen automatically (no light actor needed); scale emissive multiplier for brightness

**Troubleshoot 1 — Nanite thin-mesh shadows (foliage):**
6. If shadows disappear or geometry breaks when zooming out on foliage → mesh is Nanite-enabled
   - Fix: select Static Mesh asset → uncheck **Enable Nanite** (or import without Nanite)
   - Regular Static Mesh without Nanite works correctly with Lumen lighting + shadows

**Troubleshoot 2 — Noisy/harsh local light shadows:**
7. Open console (bottom-left) → type console vars:
   - `r.shadow.virtual.smrt.raycount.local 8` → reduces noise in virtual shadow maps for local lights
   - `smrt.sample.raylocal 8` → softens shadows from local lights
   - If shadows still look weird: reduce light size or move camera further from the light; this is a VSM limitation in early UE5

**Troubleshoot 3 — HDRI dome blocking Lumen GI:**
8. Scene has exterior light + interior room + HDRI dome mesh for sky background
9. Even if dome mesh has **no shadow casting** enabled, Lumen's ray tracing still treats it as an occluder → no GI bounce reaches the interior
10. Fix options: (A) delete the HDRI dome; (B) use Sky Atmosphere + Sky Light instead (Lumen understands sky systems natively); (C) ensure HDRI dome material has `Is Sky` flag enabled

### UE Systems / Blueprints / Settings
- **Indirect Lighting Intensity** (per-light) — how much this light contributes to Lumen GI/bounce; 0 = no indirect from this light; useful to control which lights drive the GI
- **PPV Lumen settings** — Post Process Volume → search "Lumen"; choose GI method (Screen Space GI / Lumen / Ray Tracing); reflections method; control per-scene
- **Emissive lights via Lumen** — any mesh with an emissive material emits GI automatically; Lumen calculates full indirect lighting from emissive surfaces; revolutionary vs baked-only pipelines
- **Lumen reflections** — approximated using HLODs; blurry at distance/on movement; for clean sharp reflections on glossy surfaces use Ray Trace Reflections instead
- **Nanite + Lumen thin-mesh incompatibility** — Lumen uses mesh distance fields for GI; thin meshes (foliage, leaves) don't generate usable distance fields with Nanite; shadows disappear as camera moves away; fix: disable Nanite on thin/foliage meshes
- **Virtual Shadow Maps (VSM)** — Lumen's shadow system for local lights; can be noisy; `r.shadow.virtual.smrt.raycount.local` (noise) + `smrt.sample.raylocal` (softness) console vars improve quality; fundamental limitation in early UE5
- **HDRI dome GI occlusion bug** — HDRI sky meshes block Lumen ray paths even with shadow casting disabled; Lumen cannot distinguish "I should ignore this for GI" without the `Is Sky` material flag; using Sky Atmosphere + Skylight is the safe alternative

**⚠️ Early Access Caveats:**
- This video is from UE5 initial early access release
- VSM console variables may have changed names or may now have UI equivalents
- Nanite + foliage situation has improved significantly in UE5.1+
- HDRI dome GI occlusion fix (Is Sky flag) is the modern solution

### Difficulty
Beginner-Intermediate. Project settings and basic setup are simple. Troubleshooting requires console command familiarity.

### UE Version
UE5 (early access; UE5.0; some fixes have been incorporated into later versions)

### Tags
lumen, global-illumination, reflections, shadows, nanite, debugging, performance, project-settings, workflow, emissive

---

## Related Entries
- `it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5.md` — modern interior Lumen setup; Lumen + hardware ray tracing; console vars for flickering fix
- `if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this.md` — PBL exterior with Lumen sky color boost and skylight leaking settings
- `realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — PBL workflow using Lumen for physically-based results
- `the-perfect-sky-light-in-unreal-engine-5.md` — skylight setup (ambient + reflections); `Is Sky` flag for HDRI dome fix
