---
title: Create Cinematic Lighting in Unreal Engine 5 | Physically Based Workflow
source: YouTube
url: https://www.youtube.com/watch?v=nIZpZyCrmMc
author: Andrew Averkin Art
ingested: 2026-08-09
ue_version: "not specified on screen (Lumen/Rect Light ray tracing implies UE5.x)"
tags: [lighting, physically-based-lighting, lumen, post-process, exposure, tone-mapper, local-exposure, rect-light, ray-traced-shadows, color-grading, ambient-occlusion, cinematic, hdri-visualization, interior-lighting]
extraction_status: complete
frames_dir: tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Create Cinematic Lighting in Unreal Engine 5 | Physically Based Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=nIZpZyCrmMc)
**Author:** Andrew Averkin Art
**Duration:** 33m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Creating a strong shot is much more than simply placing a camera and adding a few lights.
[0:05] Every shot is the result of many elements working together.
[0:08] The environment itself, composition, camera angle, focal lens, camera movement, lighting,
[0:13] color, timing and many other artistic decisions.
[0:16] Each of these influences what a viewer noticed, what they feel and ultimately how they perceive
[0:21] your environment and any story you want to tell through it.
[0:24] There are countless cinematography techniques, including different shot sizes, camera angles,
[0:29] framing rules, lens choices, lighting setups, color palettes and many others.
[0:34] You have wide shot, close ups, aerial shots, establishing shots to name just a few.
[0:39] The same applies to lighting, 1 point, 2 point and 3 point lighting, soft light, hard light,
[0:44] rim light, practical lights, motivated lighting and least goes on.
[0:48] This is an entire discipline and an art of form in its own right.
[0:52] In fact, cinematography and cinematic shots are such a vast subject that there is always
[0:57] something new to learn.
[0:58] And it would be impossible to cover every technique, every rule and every artistic approach
[1:03] all at once.
[1:04] But more importantly, simply knowing these techniques isn't what makes a great shot.
[1:09] Every camera angle, every light and every composition have a purpose.
[1:13] That's why before thinking about how to place a camera and how to light a scene,
[1:17] I believe there is a much more important question you should ask yourself.
[1:21] Why?
[1:22] Why should the camera be placed here instead of somewhere else?
[1:25] Why should it move and how?
[1:27] Why should the light come from this direction?
[1:29] What exactly do you want the audience to notice?
[1:32] What emotion are you trying to create?
[1:34] In some cases, a single shot can tell a story, while other times its purpose can be showcasing
[1:39] details of your environment to support the mood and story.
[1:43] So personally, I believe these are the first questions you should answer before thinking
[1:48] about the technical setup itself.
[1:50] And once you understand why you are making certain decisions, choosing the camera angle,
[1:54] focal lens, composition or lighting becomes much more intuitive and natural.
[2:01] Before we start lighting individual shots, the first thing we need is a solid lighting
[2:05] foundation for the entire environment.
[2:07] I like to think about it the same way as real life.
[2:10] Imagine walking into this workshop in the middle of the day.
[2:13] Even if anyone turns on additional lamps or start adjusting the space for a photo or a film scene,
[2:19] the environment already has its own natural lighting conditions.
[2:23] Light enters through the windows, bounces between surfaces, fills shadows area and establishes
[2:29] the overall mood of the space.
[2:30] That's your starting point.
[2:32] The same principle applies in Unreal Engine.
[2:35] Before thinking about cinematic shot, dramatic lightings or adding extra lights for visual
[2:40] impact, first you need to build a believable base lighting setup that works across the
[2:45] entire environment.
[2:46] So, rather than trying to create the final cinematic look immediately, I prefer to approach
[2:51] lighting in two stages.
[2:52] First, establish a strong and believable base for the whole environment.
[2:56] Then, refine and adapt it for the specific needs for each shot.
[3:00] This approach not only makes the process more manageable, but also gives you much more
[3:05] control over the final result.
[3:07] Okay, for demonstration purposes, I am going to hide my final lighting setup so we can start
[3:12] completely from scratch and build everything step by step.
[3:15] One of the fastest ways to create a lighting foundation in Unreal Engine is by using the
[3:20] environment light mixer.
[3:22] You can find it under Window, Environment Light Mixer.
[3:25] And if you open this panel, you'll notice that Unreal already provides all the essential
[3:30] components needed for a standard environment lighting setup.
[3:33] So, I simply go through the list and press all of the buttons.
[3:36] Create Sky Light, Create Directional Light, Create Sky Atmosphere, Create Volumetric Clouds
[3:42] and Create Hide Fog.
[3:43] And just like that, within a few seconds we have the core lighting system for our scene.
[3:48] Now, at this point it's important to understand that these aren't just separate actors randomly
[3:53] placed into the level.
[3:54] They're designed to work together.
[3:56] Think of them as different parts of the same ecosystem, where the directional light represents
[4:01] the sun and defines the primary direction of light.
[4:04] Sky Atmosphere simulates how that sunlight interacts with the atmosphere.
[4:09] Volumetric clouds react to that light and can cast shadows.
[4:12] Skylight captures the result of the entire system and restributes it back into the scene
[4:17] as ambient illumination.
[4:19] And Hide Fog adds atmospheric depths, helping light interact with the air itself.
[4:24] Because of this, changing one element affects the others.
[4:27] Moving the sun changed the atmosphere.
[4:29] The atmosphere changed the appearance of the sky.
[4:32] The sky influenced the skylight.
[4:34] So, everything is connected.
[4:36] We also need to add a post-process volume to the scene, where you can control things like
[4:40] exposure, color grading, contrast, bloom and many of the adjustment that shape the final
[4:46] look of the image.
[4:47] Once you've added it, go to the settings and enable Infinity Extend, Unbound.
[4:52] This simply means that the post-process settings will affect the entire level, regardless of
[4:57] where the camera is positioned at, instead of being limited to a specific volume in the scene.
[5:02] Alright, the first things I want to do is enable real-time capture in the skylight settings
[5:07] if it's not enabled.
[5:08] This allows the skylight to continuously capture changes in the environment.
[5:12] So, ambient light stays in sync with the sky, environment and the overall lighting setup.
[5:18] Also, I'll enable Volumetric Fog in the Exponential Hide Fog settings to get this
[5:22] more realistic atmospheric depth that helps the scene feel more natural.
[5:30] Now, before I start tweaking the light, I want to talk about physically-based lighting, or simply
[5:35] PBL.
[5:36] The main idea behind PBL is that instead of guessing lighting values and changing numbers
[5:41] until something look right, we try to use values that roughly correspond to how light behaves
[5:47] in the real world.
[5:48] Think of it as using reality as a reference.
[5:51] For example, a candle emits only a small amount of light.
[5:54] A ceiling clamp is much brighter, a cloudy day is brighter still, and direct sunlight can be
[6:00] dramatically brighter than all of them.
[6:03] So, physically-based lighting gives us reference values for these situations,
[6:07] so we have a more predictable starting point.
[6:10] It doesn't mean that these values are magically correct for all scenarios,
[6:14] and it definitely doesn't mean that every scene must strictly follow them.
[6:17] The purpose of PBL is simply to establish a believable foundation, using physically-based values.
[6:25] There are many resources where you can find physically-based values,
[6:28] but to make it simple, for this demonstration, I'll use this lighting and exposure chart.
[6:33] And if we look at it, you can see that it gives us a general understanding of how
[6:37] different lighting situations relate to one another.
[6:40] One thing worth mentioning is that you'll notice two different units here.
[6:45] Lux and Lumens.
[6:46] To keep it simple, Lux is usually used for large light sources like the Sun,
[6:50] and it describes how much light reaches a surface.
[6:54] That's why Unreal's directional light uses Lux.
[6:57] Lumens, on the other hand, are commonly used for practical lights,
[7:00] such as lamps, and it describes how much light the source emits.
[7:04] For example, a moonlit night is extremely dark, around 0.5 lux.
[7:10] A low sun during sunrise or sunset is roughly 5,000 lux.
[7:14] A cloudy day is around 20,000 lux.
[7:17] Direct sunlight at noon can reach around 100,000 lux.
[7:21] And some physically-based workflow even use values closer to 130,000 lux for very bright conditions.
[7:29] This chart also provides reference values for practical lights.
[7:33] For example, a candle produces only around 12 lumens.
[7:37] Decorative lights may sit around 300 lumens.
[7:40] Typical interior lighting can be around 1000 lumens.
[7:43] And exterior light sources can be significantly brighter.
[7:47] Another useful part of this chart is exposure.
[7:50] Different lighting conditions naturally correspond to different exposure values.
[7:54] You'll notice that exposure is measured using something called EV, or exposure value.
[8:00] To keep it simple, EV is just a way of describing how bright or dark the final image should appear
[8:05] under certain lighting conditions.
[8:07] For example, an interior scene might sit around EV4, a low sun around EV7,
[8:13] a cloudy exterior around EV10, and bright sunlight close to EV14.
[8:18] So, I am going to use values from this chart.
[8:21] But it's important to say that these numbers are not rules, they are references.
[8:25] They help us understand the relative scale of light.
[8:28] Physically-based lighting doesn't tell you how your final image should look.
[8:32] It simply gives you a logical place to begin.
[8:34] Once that foundation is established, you can always move away from reality to support the mood,
[8:40] composition, or story you want to tell.
[8:42] In other words, PBL teach us how light behaves.
[8:45] And what we choose to do with this knowledge is an artistic decision.
[8:49] Okay, let's start with the directional light.
[8:51] And the first thing I want to do is change its position.
[8:54] Right now, the sun is sitting relatively high in the sky.
[8:57] But for this particular workshop, I want a softer and slightly more atmospheric mood.
[9:02] So, I'll lower the sun a bit close to the horizon and set Y and Z axes to something like minus 10.
[9:08] I don't necessarily want a full sunset, but something close to that golden-hower feeling.
[9:13] And even with this simple adjustment, you can already see how much the atmosphere changed.
[9:17] The entire workshop immediately reacts to the new angle of the sun and becomes warmer.
[9:22] Now, if we look at the chart again, a bright sunny day can reach around 100 000 lux,
[9:28] while an overcast day is closer to 20 000 lux, and a low sun sits somewhere around 5000 lux.
[9:35] For this workshop, I don't want the harsh brightness of midday sunlight.
[9:39] I want something softer somewhere between an overcast day and a low evening sun.
[9:44] So, as a starting point, I'm going to set my directional light's intensity to around 15 000 lux.
[9:50] This scene suddenly looks much brighter than before.
[9:53] And that's completely normal.
[9:54] It doesn't necessarily mean that the light is wrong.
[9:56] It simply means that the rest of our image hasn't yet been balanced around these values.
[10:01] And that's exactly what we'll tackle next using exposure settings.
[10:05] Think of exposure as the way of defining how bright or dark the final image should appear
[10:10] under certain lighting conditions.
[10:12] Just like lux gives us a reference for light intensity,
[10:16] EV gives us a reference for how different lighting situations are typically perceived.
[10:21] So, first, I'll go to the exposure settings in the post-process volume and set exposure compensation
[10:27] to 0, because it makes the image brighter or darker on top of the actual exposure value.
[10:32] But right now, I don't want to compensate the image by eyes yet.
[10:35] I want to start from a clean, physically-based baseline.
[10:39] Then I enable minimum and maximum EV.
[10:42] And if we look back at the chart, we can see that interior scene might sit around EV4,
[10:47] a low sun around EV7, a cloudy exterior around EV10, and bright midday sunlight can reach around EV14.
[10:55] So, I'll set minimum and maximum EV to 7.
[10:59] And now, you can see that the image has become darker.
[11:02] But at the same time, our sun isn't as bright as it was before.
[11:06] So, we can continue improving the settings.
[11:08] Next, I'll use HGRI-I adaptation visualization mode, which you can find here.
[11:14] Show, visualize, HGRI-I adaptation.
[11:17] Think of it as a light meter that helps us check whether our scene behaves the way we expect.
[11:22] If something feels too bright or too dark, this helps to verify whether the scene is behaving
[11:27] correctly instead of relying purely on our eyes.
[11:31] Once enabled, you'll see a histogram appear at the bottom of the screen.
[11:35] Since we've locked our exposure to EV7, you can see that the scene stays around the target value
[11:40] instead of constantly changing.
[11:42] The blue vertical line represents the current average exposure value of the scene.
[11:47] As the lighting changes, it moves left or right to show where the scene falls on the histogram.
[11:52] You'll also notice these two small squares in the center with values that updates as you move
[11:57] your cursor around the scene.
[11:58] The first one is Illuminance Meter, measure it in lux.
[12:02] This tells you how much light reaches a particular surface.
[12:05] If you move over a bright area hit by sunlight, the value goes up.
[12:10] If you move it into a shadow, it drops.
[12:12] The second one is Illuminance Meter, measure it in nits.
[12:15] This tells you how bright the surface actually appears to the viewer after reflecting that light.
[12:20] For example, with our sun set to around 15,000 lux and our exposure locked to EV7,
[12:26] bright areas near the window should naturally give higher values,
[12:30] while darker corners of the workshop will show much lower values.
[12:34] The important thing isn't trying to hit one exact number everywhere.
[12:38] What we are really checking is whether the relationship between bright and dark areas
[12:42] makes sense.
[12:43] If the brighter parts of the scene read brighter and the shadows area read darker,
[12:48] then our lighting is behaving in a believable way.
[12:51] Now all this might sound overhelming.
[12:53] Think of the HDRI visualization mode as a light meter that helps you check whether your scene
[12:58] behaves logically.
[12:59] In practice, you'll eventually want to rely on it.
[13:02] But when you're just starting out, the lighting and exposure chart is a much easier reference.
[13:08] So just try those PBL values first, and this visualization mode will become much more intuitive
[13:14] later on.
[13:15] Now let's tweak the tone mapper.
[13:17] One way I like to think about it is this.
[13:19] We've already established our physically based lighting values for the sun and exposure.
[13:24] And now we're applying a bit of filming interpretation on top of that.
[13:28] The lighting itself isn't changing.
[13:30] We're simply changing how that lighting is translated into the final image.
[13:35] If you go to post-process, then film, you'll find parameters like slope and toya.
[13:40] Think of slope as the overall contrast control of the image.
[13:44] Higher values increase contrast, making the image feel much punchier and more dramatic.
[13:49] Lower values soften the image.
[13:51] Toya, on the other hand, controls how shadows transition into black.
[13:55] Higher values make shadows heavier and darker, causing them to lose detail more quickly.
[14:01] Lower values preserve more information in darker areas and create a softer transition.
[14:06] And here's something interesting to pay attention to.
[14:09] If you look in the curve in the HDRI eye adaptation visualization mode, while adjusting
[14:14] these values, you'll notice that the shape changes.
[14:17] As you lower slope and toya, the curve becomes more stretched and smoother,
[14:21] resulting in softer contrast and more gradual transitions between dark and bright areas.
[14:26] If you increase them, the curve becomes steeper and more compressed.
[14:30] The image gains contrast, highlights become more pronounced,
[14:34] and shadows fall into black more aggressively.
[14:36] So in a way, those controls allow you to shape how the tonal range of your image is distributed.
[14:42] They're not changing the amount of the light in the scene.
[14:45] They're changing how that light is displayed.
[14:47] For this workshop, I prefer a slightly softer look,
[14:50] so I usually reduce slope slightly to around 0.8 and lower toy to around 0.3.
[14:57] Though this will help us to get more information from dark areas.
[15:03] Let's tweak local exposure.
[15:05] This is especially useful for indoor scenes like this one.
[15:09] For example, the area around the windows are much brighter than the deeper parts of the workshop.
[15:14] Without local exposure, you often have to make a choice.
[15:17] Either the exterior looks good and the interior becomes too dark,
[15:20] or the interior looks good and the windows become too bright.
[15:24] Local exposure helps balance those differences.
[15:27] Instead of affecting the entire image, it only adjusts the area that needs a bit of extra help.
[15:33] The two settings I use most often are highlight contrast and shadow contrast.
[15:37] Highlight contrast helps preserve detail and contrast in brighter areas of the image.
[15:42] And shadow contrast allows you to recover a bit more information in darker regions.
[15:47] And that's really the key idea behind local exposure.
[15:50] We're not trying to make everything equally bright and visible.
[15:54] Shadows should still feel like shadows.
[15:56] We're simply improving readability in the areas where important details might otherwise get lost.
[16:01] For now, I'll set shadow contrast to 0.6 and highlight contrast to 0.8.
[16:07] I think this works well.
[16:09] And later, I can tweak those parameters if needed.
[16:12] I hope this wasn't too complicated.
[16:14] But to simplify everything we've just covered,
[16:17] the workflow is actually pretty straightforward.
[16:20] First, using lighting and exposure chart, you establish physically based values for the sun.
[16:25] Then you balance the image using exposure values in post-process volume.
[16:30] Then you can use the HDRI visualization mode to verify that everything behaves as expected.
[16:36] Next, in post-process, you tweak the overall contrast and tonal response of the tone mapper.
[16:41] By tweaking slope and to a values.
[16:43] And finally, you use local exposure to make subtle adjustment to the brightest and darkest area of the image.
[16:49] And now that we established a solid lighting foundation using physically based values,
[16:54] we can start moving into more artistic side of lighting.
[16:58] Since this is an interior scene, one of the most common challenges is simply getting enough
[17:03] natural looking light into the space.
[17:05] So, one technique I often use, placing additional light sources behind the windows,
[17:09] using rectangular lights.
[17:11] This approach often used in architectural visualization,
[17:14] where it's often used not only to boost the amount of light entering the interior,
[17:18] but also to create a softer, more diffused quality of light,
[17:21] resulting in more natural transitions and softer shadows.
[17:25] In fact, some interior setups rely so heavily on these window lights, often referred to as fake lights,
[17:30] that they almost replace the contribution of the skylight,
[17:33] especially when ambient lighting alone isn't enough to achieve the desired look.
[17:38] So, in this case, I'm gonna use rectangular light.
[17:43] In order to see my light sources more clearly, I'm going to temporarily hide the
[17:47] decal icons, since I have quite a lot of them in the scene.
[17:50] To do that, go to show, type decal in the search bar,
[17:53] and under sprites, simply uncheck decals.
[17:56] Now it's much easier to see where all of our light sources are placed.
[18:00] So, I place this rectangular light just outside the window,
[18:04] and adjust its size so that it roughly matches the size of the window opening.
[18:08] Let's say I'll set source width to 50, and source height to around 100.
[18:23] Then I'll duplicate this rectangular light, and place copies just outside each window opening.
[18:28] You can think of these lights as of light portals,
[18:31] which help simulate soft light coming from outside.
[18:41] As you can see, we can barely see the effect of these lights,
[18:44] and that's because we still need to adjust a few settings.
[18:47] The first thing I'll do is select all of my rectangular lights,
[18:51] and change their intensity units to lumens.
[18:53] I'll start with around 15,000 lumens each.
[18:56] Since these are essentially fake lights used to support the interior lighting,
[19:00] there isn't a strict physically correct value for them.
[19:03] The goal is to give the interior a soft and natural boost,
[19:06] while keeping it consistent with our overall physically based setup.
[19:10] Also, I'll set the barn door angle to around 90, and the barn door length to 1,
[19:15] so that the light stays more focused and doesn't spread too much beyond the window opening.
[19:20] Also, I'll adjust the attenuation radius a bit,
[19:23] so that the rectangular light roughly reaches the wall on the right,
[19:26] without shining directly into it.
[19:28] Maybe something like 800s can work.
[19:41] For these lights, in settings, I disable volumetric scattering and set it to 0,
[19:46] because at this point, I don't want them to affect the fog and make it stronger.
[19:52] Now, I can fine-tune the position of the rectangular lights,
[19:55] moving them a little closer to or farther from the windows,
[19:58] so that the light and shadows are distributed more evenly,
[20:01] and don't create unwanted shadows cast by the window frames.
[20:04] And there's the small trick I like to use.
[20:06] I'll rotate the rectangular lights a little, maybe around 20 or 30 degrees,
[20:11] so it feels like the light is coming slightly from above, more natural,
[20:15] like sunlight bouncing from the sky.
[20:17] It also helps keep the upper part of the interior,
[20:20] especially under the roof, slightly darker,
[20:22] allowing the light to focus more on the center of the workshop.
[20:26] Now, let's tweak shadow quality.
[20:28] And this is where ray-traced shadows really help.
[20:31] So, I go to my rectangular lights, find cast ray-traced shadows and enable it.
[20:36] And yeah, you can immediately see the difference.
[20:38] Shadows became much more grounded,
[20:40] softer in a natural way, contact areas look better, and edges are not that fake sharp.
[20:57] We can also push the shadow quality a bit further.
[21:00] Let me switch the viewport to lighting only.
[21:02] As you can see, the lighting already looks pretty clean.
[21:05] But at some areas you can still see some noise.
[21:08] If we take a closer look around the windows, you might notice it.
[21:11] This happens because rectangular lights are relatively large area light sources,
[21:16] and Unreal has to approximate how those light rays bounce and interact with the scene.
[21:20] It's not a huge issue, but if you want to cleaner result,
[21:24] you can go into rectangular light settings, find the ray tracing section,
[21:28] and increase the samples per pixel value.
[21:30] For example, if I set it to 4, you can immediately see the noise start to disappear,
[21:35] and the image becomes more cleaner.
[21:37] You can push it even higher if needed,
[21:39] but keep in mind that render times and performance will also increase.
[21:42] In most cases, somewhere between 2 and 4 samples gives a good balance between image quality and performance.
[21:54] Another thing we can do is play a bit with contact shadows.
[22:00] So I'll search in rectangular light details for the contact shadow length settings,
[22:05] and set it to something around 0.02.
[22:08] And if you look closely, the shadows under small objects become stronger and more defined,
[22:13] making fine details feel more grounded and easier to read.
[22:16] However, be careful with this parameter, because depending on the scale of your scene
[22:21] and the distance between objects, it can sometimes produce inaccurate shadows.
[22:25] I prefer to use it subtly and only enhance the image rather than draw attention to the effect itself.
[22:40] Let's do the same with directional light and enable ray-traced shadows as well.
[22:44] This will give us softer and more natural-looking shadows,
[22:47] especially in areas where small details and contact between objects are important.
[23:05] You can also adjust source angle to make shadows softer.
[23:09] Higher values give softer shadows, while lower gives sharper.
[23:13] It's basically like changing the size of the sun in the sky.
[23:18] Also, let's enable light-shaft occlusion.
[23:29] What it does, it makes volumetric light beams more concentrated, especially near openings
[23:34] like windows, so rays feel more visible and more grounded in space.
[23:38] And if you want to push this even further, you can increase volumetric scattering intensity,
[23:43] for example, set it to 2.
[23:44] But again, be careful, because it's easy to overdo and get that too much fog, too much rays look.
[23:50] So I'll leave it to 1 for now.
[24:05] Now, if you look at the image, you can notice that the whole scene has a bit of reddish, warm tint.
[24:11] That actually makes sense, because we have a lot of wood, a lot of brown tones, our sun is low,
[24:16] so everything together pushes the image into those warm tones.
[24:19] And this is something we can balance.
[24:21] So, for that in post-process, I go to color grading – temperature.
[24:25] By default, it's 6500, which is already a bit warm, so I will lower the value something like
[24:32] 4500.
[24:34] And now you can see how the colors feel much more natural.
[24:37] The reddish tint is reduced, and the image looks more balanced,
[24:40] thanks to the cooler blue tones.
[24:43] Another thing you can experiment with, and this is already more of an artistic decision,
[24:47] is the color grading section.
[24:49] You can play with saturation in color grading global settings,
[24:52] and slightly reduce it, something like 0.9.
[24:55] It just desaturates the overall image a bit, but this really depends on taste and the environment
[25:00] itself.
[25:01] Sometimes you want more saturation, especially in stylized scenes, for example.
[25:05] You can play around with the shadows, mid-tones and highlights, too,
[25:08] to further shape the mood of your scene.
[25:10] For example, if the image starts to feel a bit too flat, you can add a little more
[25:15] contrast to the shadows, or adjust the mid-tones using parameters like contrast,
[25:19] gamma or offset.
[25:20] For example, I can set contrast to 1.1 in the shadows settings.
[25:25] However, this is one of those areas where it's very easy to overdo things.
[25:29] So, whenever I make adjustment here, I try to be subtle and intentional,
[25:33] usually working with relatively small values rather than making drastic changes.
[25:37] At the end of the day, there are no universally correct settings.
[25:40] It all depends on the mood you are trying to create and the kind of lighting you want to
[25:44] achieve for your scene.
[25:46] From this point, we can add more post-processing effects.
[25:49] For example, in the lens tab, I can enable bloom.
[25:51] And here I usually choose the convolution method.
[25:54] It's more expensive in terms of performance, but it gives a more realistic result,
[25:58] especially for cinematic shots.
[26:00] It reacts to highlights in a more natural way, like bright areas slightly glow and bleed into
[26:05] darker areas.
[26:06] Similar to how real lenses behave.
[26:08] You can tweak intensity a bit, but I wouldn't push it too much because it's very easy to get
[26:13] that glowy artificial look and then everything starts to feel fake.
[26:19] Then we can also enable chromatic aberration.
[26:22] I personally prefer to add it later during the final grading stage, either in After Effects
[26:27] or DaVinci Resolve, where I have a bit more control over the effect.
[26:30] However, if you want, you can also keep a very subtle amount of heat here and Unreal,
[26:34] something like 0.2 is enough.
[26:37] If you push it too far, it just looks broken.
[26:52] We can also add a bit of vignette in Image Effects settings,
[26:55] slight darkening around the edges.
[26:57] It helps to focus attention towards the center of the frame, not too strong,
[27:01] just enough so you almost don't notice it.
[27:03] So something around 0.5 works good in this case.
[27:19] Now, if you still want to make the environments a bit darker or brighter,
[27:22] you can change the minimum and maximum EV values a bit.
[27:25] Remember, we're still working with physically based lighting values and from the beginning,
[27:30] I wanted to keep the exposure somewhere between typical interior, which is around EV4 and the
[27:35] low sun, which is around EV7.
[27:37] So, if I want to brighten the entire scene globally,
[27:40] I can simply change the minimum and maximum EV values from 7 to, let's say, 6.
[27:45] So, I still have some room to fine tune these settings, until the scene feels just right.
[27:50] You can also slightly adjust the intensity of the rectangle lights,
[27:53] or fine tune the image using local exposure.
[27:56] It's also totally fine if it's helped to make your image looks better, brighter or darker,
[28:02] depending on your needs.
[28:09] And having these four rectangle lights, one behind each window,
[28:12] also gives us a lot more control over the lighting.
[28:15] If I feel that some areas are too bright or too dark,
[28:18] I can simply tweak the intensity of individual lights.
[28:21] For example, to me, light near the shelf feels a bit too bright.
[28:24] So, instead of 15,000 lumens, I'll reduce it to 10,000 lumens.
[28:29] And the light near the opposite wall, with the door and the mural,
[28:32] also feels too strong.
[28:34] So, I'll lower its intensity to around 5,000 lumens.
[28:37] And that's totally normal, because it's already a creative decision.
[28:41] As you can see, with just a few small adjustments,
[28:43] I can already change the mood slightly, without affecting the overall lighting setup.
[28:48] So, these rectangular lights will also be useful later,
[28:51] when I start setting up lighting on per shot basis.
[28:54] Depending on the camera angle, I can turn individual lights on or off,
[28:58] to achieve the look I want for particular shot.
[29:00] There is one more thing in post-process, that can help small details stand out a bit more.
[29:05] And that's ambient occlusion.
[29:07] Ambient occlusion adds subtle shadowing in areas, where objects touch or where surface meet,
[29:12] helping add a bit more depth and definition to the image.
[29:15] To enable it while using Lumen, you'll first need to enter a couple of console commands.
[29:20] So, just type r.lumen.diffuseindirect.ssao1.
[29:26] And another one, r.lumen.screenpropgather.shortrangeao0.
[29:32] Then, go to post-process, rendering features, ambient occlusion,
[29:36] and enable intensity and radius parameters.
[29:39] If you want to see exactly what ambient occlusion is doing,
[29:42] you can switch the viewport to buffer visualization, ambient occlusion.
[29:46] This makes it much easier to evaluate the effect and adjust the settings.
[29:50] I usually reduce the radius to around 25, maybe 30,
[29:54] so the effect focuses on smaller contact areas,
[29:56] and increase the intensity to something around 0.5.
[30:00] I would recommend being fairly subtle with it.
[30:02] If ambient occlusion becomes too strong, the image can quickly start to feel fake and overly processed.
[30:08] The goal isn't to add obvious dark outlines everywhere,
[30:11] it's simply to introduce a bit of extra depth in areas where objects naturally come together.
[30:16] And sometimes, depending on the scene and lighting setup,
[30:19] it can make perfect sense not to use ambient occlusion at all.
[30:33] Now, I can also adjust a little deposition of the sun to my liking, but mostly along the Z-axis.
[30:51] If I rise it higher to create more of a daytime look, or lower it to simulate a deeper sunset,
[30:57] I'll basically break the PBL setup, and I would need to change the sun's intensity
[31:01] to a different physically based value from the lighting and exposure chart.
[31:05] Adjust the minimum and maximum EV values in the exposure settings,
[31:08] as well as the intensity of the rectangle lights outside the windows.
[31:12] In other words, all of these settings are connected,
[31:15] and changing one means adjusting the others as well.
[31:18] Since we already built our lighting around the golden hours setup,
[31:21] I prefer to make only small adjustments to the sun's positions
[31:24] without dramatically changing the overall lighting conditions.
[31:28] So, let's wrap this topic up. We've covered quite a lot of settings,
[31:34] values and different techniques, and at first it might feel a bit overhelming.
[31:38] But once you understand the logic behind the workflow,
[31:40] lighting becomes much less about memorizing numbers and much more about making intentional
[31:45] artistic decisions. I recommend starting with a very simple lighting setup and improving it
[31:50] step by step. Build a solid foundation first, then tweak it, refine it and gradually add more
[31:56] complexity. You can begin with physically based lighting workflow and rely on physically correct
[32:00] values for your light sources as strong foundation. But don't think of those values as trick rules,
[32:06] they're simply a starting point. In real production, you'll almost always adjust them later,
[32:11] depending on the scene, the mood, the camera angle or the artistic direction.
[32:15] Try to establish a balanced image by controlling your exposure with minimum and maximum EV values,
[32:21] and using the HDRI visualization tool to verify that your lighting behaves as expected.
[32:26] Then refine the overall contrast with the tone mapper and improve shadows readability using
[32:31] local exposure. That gives you a solid base to build upon. From there, you can move into the
[32:36] more artistic side of lighting, adding additional light sources, improving shadows quality,
[32:40] adjusting color grading and applying subtle post-process effects that support the mood of the
[32:46] scene. And I think that's probably the most important takeaway. Physically based lighting
[32:52] gives you a starting point, not a limitation. Don't be afraid to move away from physically
[32:57] correct values if it helps tell the story better, improve the composition or create a stronger
[33:02] emotion response. Sometimes realism is exactly what you need, and sometimes a small artistic
[33:07] adjustment can make the image far more powerful. At the end of the day, lighting isn't just about
[33:12] making things visible. It's also about guiding the viewer's eye, creating depth, shaping the mood
[33:18] and supporting the story you are trying to tell. So use these tools as guidelines, experiment and
[33:23] trust your artistic instincts. Don't be afraid to break the rules once you understand why those
[33:28] rules exist in the first place. And now, with our base lighting in place, we are finally ready to
[33:33] move on to the next stage, adding cameras and refining the lighting for individual shots to achieve
[33:38] a more cinematic look.



---

## Captured Frames

- [3:20] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_000.jpg
- [6:33] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_001.jpg
- [9:44] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_002.jpg
- [11:14] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_003.jpg
- [14:01] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_004.jpg
- [16:01] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_005.jpg
- [18:08] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_006.jpg
- [20:31] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_007.jpg
- [22:05] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_008.jpg
- [24:25] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_009.jpg
- [25:51] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_010.jpg
- [29:20] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_011.jpg
- [30:00] tutorials/frames/create-cinematic-lighting-in-unreal-engine-5-physically-based-workflow/frame_012.jpg

---

## Structured Notes

### Core Technique
A two-stage lighting workflow for interior cinematic environments: first build a **physically-based (PBL)** base lighting foundation for the whole level using real-world lux/lumen/EV reference values (not eyeballed numbers), then layer artistic "fake"/practical lights, shadow-quality tuning, and post-process grading on top of that foundation once it's already believable.

### Summary
Demonstrates lighting a wooden interior workshop scene from scratch. Stage 1 — foundation: Environment Light Mixer (Window → Environment Light Mixer) one-click-creates the core ecosystem (Sky Light, Directional Light, Sky Atmosphere, Volumetric Clouds, Exponential Height Fog), which the video stresses are interdependent (moving the sun changes the atmosphere, which changes the sky, which changes the skylight). A Post Process Volume is added with Infinity Extend (Unbound) so its settings apply everywhere. Skylight Real-Time Capture and Volumetric Fog are enabled. The directional light is angled low (~golden-hour) and set to a physically-referenced intensity (15,000 lux) using a lighting-and-exposure reference chart (lux for large sources like the sun, lumens for practical lights; example anchors: moonlight ≈0.5 lux, low sun ≈5,000 lux, overcast ≈20,000 lux, noon sun ≈100,000 lux; candle ≈12 lumens, interior ≈1,000 lumens). Exposure is then locked to a physically-referenced EV range (interior ≈EV4, low sun ≈EV7, overcast ≈EV10, bright sun ≈EV14) via Post Process → Exposure (Exposure Compensation = 0, Min/Max EV both set equal, here 7) rather than eyeballed, and verified with the **HDRI Eye Adaptation** visualization mode (Show → Visualize → HDR Eye Adaptation), which overlays a histogram plus an Illuminance meter (lux, light hitting a surface) and a Luminance meter (nits, what the viewer actually perceives) so the artist can confirm bright/dark relationships read correctly rather than hitting one "correct" number everywhere. Film tone-mapper Slope/Toe are then tuned as a separate "filming interpretation" layer on top of the physical values (Slope = overall contrast, Toe = how shadows crush toward black; lower both — ~0.8 / ~0.3 — for a softer look with more shadow detail), and Local Exposure (Highlight Contrast / Shadow Contrast, e.g. 0.8 / 0.6) is used to keep bright window areas and dark interior corners both readable without flattening the whole image. Stage 2 — artistic layer: Rect Lights are placed just outside each window as "light portals" (fake practical lights, source size matched to the window opening, intensity in lumens e.g. ~15,000, Barn Door Angle ~90°/Length ~1 to keep spill contained, Attenuation Radius tuned to reach but not overshoot the far wall, Volumetric Scattering disabled per-light to avoid over-fogging, and a slight rotation of ~20-30° so the light reads as bouncing down from the sky rather than coming in flat) — then Cast Ray Traced Shadows is enabled on both the rect lights and the directional light for grounded, soft, natural shadow falloff, with per-light Ray Tracing → Samples Per Pixel (2-4) raised to clean up noise around large area-light sources, plus a small Contact Shadow Length (~0.02) for extra grounding on small objects, Light Shaft Occlusion for visible god-rays at the windows, and Volumetric Scattering Intensity tuned carefully (left at 1, not pushed to 2) to avoid an overly foggy look. Color Grading Temperature is pulled down from the 6500K default to ~4500K to counteract an overly warm/reddish cast from the wood + low sun combination, with optional Saturation/Contrast/Gamma/Offset tweaks per shadow/midtone/highlight range kept subtle. Post-process finishing touches: Bloom (Convolution method preferred for a more realistic, filmic highlight bleed over the cheaper default method), a very light Chromatic Aberration (or defer that to grading software like After Effects/DaVinci Resolve), a subtle Vignette (~0.5), and Ambient Occlusion — which under Lumen requires two console commands first (`r.lumen.diffuseindirect.ssao 1` and `r.lumen.screenprobegather.shortrangeao 0`) before the Post Process → Ambient Occlusion Intensity/Radius controls take effect; Buffer Visualization → Ambient Occlusion helps evaluate the effect directly; radius reduced (~25-30) and intensity kept modest (~0.5) to avoid a fake over-processed look. Individual rect-light intensities are then hand-adjusted per area (e.g. one dropped from 15,000 to 10,000 lumens, another to 5,000) as a final artistic balancing pass, with the video noting these same per-window rect lights will later double as per-shot toggleable lights once cameras are introduced.

### Key Steps
1. Environment Light Mixer (Window → Environment Light Mixer) → create Sky Light, Directional Light, Sky Atmosphere, Volumetric Clouds, Exponential Height Fog in one pass.
2. Add a Post Process Volume, enable Infinity Extend (Unbound).
3. Enable Sky Light Real-Time Capture and Volumetric Fog (in the Exponential Height Fog settings).
4. Position/angle the Directional Light for the desired time-of-day mood (here: low, near-golden-hour).
5. Set Directional Light intensity in **lux** using a physically-based reference chart rather than guessing (workshop example: 15,000 lux for a soft, below-midday look).
6. In Post Process → Exposure: set Exposure Compensation to 0, enable Min/Max EV, and set both to the same physically-referenced EV value for the target lighting condition (here EV7, "low sun").
7. Verify with Show → Visualize → HDR Eye Adaptation: read the histogram + Illuminance (lux) / Luminance (nits) meters to confirm bright areas read brighter and shadows read darker in a believable relationship, rather than chasing one target number.
8. Tune the Film tone mapper (Post Process → Film): lower Slope (~0.8) for softer contrast, lower Toe (~0.3) to retain more shadow detail — watch the HDR Eye Adaptation curve reshape live as these change.
9. Tune Local Exposure: Shadow Contrast (~0.6) and Highlight Contrast (~0.8) to keep both window-bright and interior-dark areas legible without a global exposure compromise.
10. Add Rect Lights just outside each window ("light portals") sized to the window opening; set intensity in lumens (~15,000 starting point, no strict physical target since these are fake supplemental lights); tune Barn Door Angle/Length to contain spill, Attenuation Radius to reach but not overshoot the far wall, disable per-light Volumetric Scattering, and rotate each ~20-30° for a more natural top-down feel.
11. Enable Cast Ray Traced Shadows on the rect lights and the directional light; raise per-light Ray Tracing Samples Per Pixel (2-4) to reduce area-light noise (check via Lighting Only viewport mode); add a small Contact Shadow Length (~0.02) for small-object grounding; enable Light Shaft Occlusion on the directional light for window god-rays; keep Volumetric Scattering Intensity conservative (~1).
12. Color Grading → Temperature: lower from default 6500K toward ~4500K to cool an overly warm/reddish scene; optionally adjust global Saturation and per-range (Shadows/Midtones/Highlights) Contrast/Gamma/Offset subtly.
13. Post-process finishing: Bloom Method = Convolution for realism; light/no Chromatic Aberration (prefer doing it in compositing); subtle Vignette (~0.5); Ambient Occlusion — run the two Lumen console commands first, then set Post Process AO Intensity (~0.5) and Radius (~25-30), checked via Buffer Visualization → Ambient Occlusion.
14. Iterate globally via Min/Max EV (nudge both down together to brighten, e.g. 7→6) and per-light rect-light intensity tweaks as a final art pass; keep individual window lights independently adjustable since they'll later be toggled per camera shot.

### UE Systems / Blueprints / Settings
Environment Light Mixer, Sky Light (Real-Time Capture), Directional Light (lux, Source Angle, Cast Ray Traced Shadows, Light Shaft Occlusion), Sky Atmosphere, Volumetric Clouds, Exponential Height Fog (Volumetric Fog, Volumetric Scattering Intensity), Post Process Volume (Infinity Extend/Unbound, Exposure Compensation, Min/Max EV, Film Slope/Toe, Local Exposure Highlight/Shadow Contrast, Color Grading Temperature/Saturation/Shadows-Midtones-Highlights, Bloom Convolution, Chromatic Aberration, Vignette, Ambient Occlusion Intensity/Radius), Rect Light (Source Width/Height, lumens, Barn Door Angle/Length, Attenuation Radius, Volumetric Scattering toggle, Ray Tracing Samples Per Pixel, Contact Shadow Length), HDR Eye Adaptation visualization (Show → Visualize), Buffer Visualization (Ambient Occlusion), Lumen console commands (`r.lumen.diffuseindirect.ssao 1`, `r.lumen.screenprobegather.shortrangeao 0`).

### Difficulty
Intermediate — no Blueprint/code work, but requires understanding the *relationships* between multiple interconnected systems (sun angle ↔ atmosphere ↔ skylight, lux ↔ EV ↔ exposure) rather than tuning any single setting in isolation; the physically-based numeric anchors make it approachable for someone newer to lighting theory.

### UE Version
Not explicitly stated (Lumen-based workflow with Rect Light ray tracing and the two `r.lumen.*` console commands implies a recent UE5.x version; no exact point release named on screen or in narration).

### Tags
lighting, physically-based-lighting, lumen, post-process, exposure, tone-mapper, local-exposure, rect-light, ray-traced-shadows, color-grading, ambient-occlusion, cinematic, hdri-visualization, interior-lighting

---

## Related Entries
None yet — first physically-based interior/cinematic lighting fundamentals entry in this library. Cross-link future PBL, Lumen lighting, or per-shot camera/lighting tutorials here.
