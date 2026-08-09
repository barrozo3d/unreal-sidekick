---
title: Achieving Realistic Cross-Platform Characters: A UE5 Pipeline Approach | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=EL8N3rdIUIM
author: Unreal Engine
ingested: 2026-08-09
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/achieving-realistic-cross-platform-characters-a-ue5-pipeline-approach-unreal-fes/
frame_count: 0
frame_status: pending-selection
---

# Achieving Realistic Cross-Platform Characters: A UE5 Pipeline Approach | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=EL8N3rdIUIM)
**Author:** Unreal Engine
**Duration:** 36m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py achieving-realistic-cross-platform-characters-a-ue5-pipeline-approach-unreal-fes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, welcome to Unreal Fit's EdgeCaco 2026.
[0:05] It's my great honor to be here to share our team's key technical breakthrough with
[0:11] the developer from all over the global.
[0:14] I'm Bing Liu.
[0:16] My 20-year career spans from CG to China's gaming industry.
[0:21] I joined the AXO game in 2016 to architect and later our next generation, Unreal Engine,
[0:28] Art Pipeline, overseeing both Art and Animation Center.
[0:33] Today, I will speak about achieving realistic cross-platform character on Unreal 5 pipeline
[0:39] approach.
[0:40] Let's go over our self-developed complete character pipeline, program on release games.
[0:48] With that, I will pass the stage to Iris to continue our presentation.
[0:54] Thank you.
[0:55] Thank you, Mr. Liu.
[0:56] And thank you, everyone.
[0:57] Yeah.
[0:58] This is Iris.
[0:59] I'm really glad to be here.
[1:02] And yeah, before we talk about technology, please allow me to give a brief introduction
[1:07] of AXO Games and its journey with Unreal Engine.
[1:10] Okay.
[1:11] So as a top Chinese game developer, AXO Games creates realistic and stylized games for mobile
[1:17] and PC with many finished titles out in the market.
[1:21] And it has launched dozens of times and went from Unity over to Unreal Engine.
[1:27] And along the way, AXO Games refined the production process to make great gains for global users.
[1:34] Its first UE game is DragonRaja, as well as China's very first UE4 mobile MMORPG.
[1:43] And there is a live makeover known for its gorgeous character presentation.
[1:48] Okay.
[1:50] So today, we'll tell a story in three acts.
[1:52] First, what we learned during the UE4 era.
[1:55] And second, how UE5 changed our rendering pipeline.
[1:59] And third, why we choose Matter Human and how we extend it for our characters.
[2:06] So first, I would like to introduce live makeover, which is one of our representative works.
[2:12] It combines fashion, home customization and open-ended world, all built on UE4.
[3:12] Yeah.
[3:16] So live makeovers, patented AXO Palo dynamically generates colors with Unreal Engine.
[3:26] And our optimization lets mobile outfits reach 400k plus polygons alongside 100 plus adjustable
[3:34] visual options.
[3:36] And strong visuals help it lead a global female game space with over 50 million global players.
[3:43] But getting there wasn't easy.
[3:45] Developing live makeover brought three significant technical challenges.
[3:51] So first one is that tons of unit clothes require complex materials and transparent rendering
[3:58] and sorting were tricky.
[4:00] And high poly and high drug call causes performance issues.
[4:06] As you can see, we built a massive library of high fidelity fabric materials.
[4:10] And what we're showing here is just only a small part of the full pipeline.
[4:17] And let's zoom in.
[4:19] So when it comes to detailed costume design, we mainly rely on layered material matching
[4:26] and combination.
[4:28] And a good example is our floral ornaments, which are made by stacking multiple translucent
[4:34] setting layers.
[4:36] And here is another small detail with large visual impact.
[4:40] We added three metallic specular highlights.
[4:44] And it creates another layer of material richness and guides the player's eyes toward the most
[4:49] important part of the outfits.
[4:53] And for our traditional Chinese closing series, when we went beyond visual reference, we collaborated
[5:00] with Chinese leading Sichuan embroidery artisans.
[5:05] And many of the embroidery structures were developed with direct guidance from real craft
[5:10] people.
[5:12] And that's actually changed our process.
[5:15] Instead of asking how do we make this look in brighters, we asked how is this actually
[5:21] made in real life.
[5:22] So that question gave us better art and better technical decisions.
[5:28] And take a closer look and you will see the natural stitch trajectories on these embroideries.
[5:35] And we studied lots of real archival craft references to recreate genuine handwork details
[5:41] and assimilate tiny gloss shapes by tidally packed silk threads.
[5:48] But accuracy was the only beginning.
[5:50] Once we understood the traditional material, we could combine it with fantasy elements
[5:55] to give players a more like a unique and refreshing look and experience.
[6:03] So we started mixing materials that normally would not appear together in real life.
[6:08] We redesigned classic patterns, changed proportions, and introduced unexpected surface combination.
[6:15] And that balance actually became part of the identity of life makeover.
[6:22] So take this mermaid outfit as an example, it pushed the idea even further.
[6:28] And our 3D artist and the TA iterated again and again to create iridescent highlights
[6:35] and a smooth transition between scales and the skin.
[6:39] And we could see that the boundary was actually the hardest part.
[6:42] If it is too sharp, it looks attached.
[6:45] But if it's too soft, the scale is just a loose structure.
[6:49] And the final result should feel like one continuous surface which we have achieved successfully.
[6:58] So we used dynamic reflection and normal variations to mimic how the scales undulate and wrap naturally over the skin.
[7:06] And layers of materials also helped build that translucent, keratin style dabs for each piece.
[7:12] And zooming close, and you will spot fine details on every single fish scale.
[7:17] It looks absolutely amazing.
[7:20] And we also add overall color gradients, blending, and random sparkling spackles into the material.
[7:26] And paired with diamond style decorative parts, the whole outfits feel even more immersive and dreamy.
[7:35] So beautiful translucent arts that are easy to admire, but they are much harder to source.
[7:41] So the next question was, how do we manage a large library of translucent costumes without turning every asset a special case?
[7:51] So we built a large library of multilayer translucent fashion assets to reduce transparency,
[7:58] sorting narrows, and improve production efficiency.
[8:01] We established a unified workflow for both the arts and engine team.
[8:07] And here's the whole pipeline works.
[8:09] So first we sleep the translucent parts into separate sub-mushers to simplify later sorting.
[8:16] And next we sort them by garment category, like, you know, skirts, accessories, clothes, and by priorities set by artists.
[8:25] And we also sort certain special pieces based on their bond positions.
[8:30] And finally, our programmers find and result with the OITs algorithm.
[8:35] And next I'll show you one of our newest outfits and it shows the great visuals we can get on mobile.
[8:43] As you can watch, look at three things, the overlapping translucent layers, the silhouette during motion, and stability of the highlights.
[10:06] Okay. So now let's move to UE5 finally.
[10:11] And it allowed us to push character rendering even further.
[10:14] And we keep aiming to make top-tier character visuals run well on every platform.
[10:20] And this brings us to our new project, Silent Whispers, built entirely on UE5.
[10:27] Three, two.
[10:34] Welcome to your gilded cage. You came right back to me.
[10:40] The judgment begins now.
[10:44] I command you. Live.
[10:50] My mission is to lend your life.
[10:54] You don't remember me.
[10:58] I'd stay this place forever.
[11:01] If it means you never had to bleed again.
[11:04] Struggle. This is your destiny.
[11:08] Wait for me.
[11:10] It will fight away. It will lead me back to you.
[11:14] Let the world fall into silence.
[11:18] Run. Don't look back.
[11:24] One of us can survive this. Let it be you.
[11:29] You must remember me.
[11:34] You will never be free of me.
[11:38] The game begins.
[12:18] I feel something so right.
[12:22] I don't feel wrong and faint.
[12:26] I feel something so wrong.
[12:30] I'm doing what I feel need.
[12:33] I could lie. I could lie. I could lie.
[12:37] Everything that kills me makes me feel alive.
[12:41] I've been lovin' sleep.
[12:45] I've been thinking about the things that we could be.
[12:49] But baby I've been lovin' prayin' hard.
[12:53] Say no more countin' dollars. We'll be countin' stars.
[12:57] Baby I've been lovin' busy sleep.
[13:01] Dreamin' about the things that we could be.
[13:05] Baby I've been lovin' prayin' hard.
[13:09] Say no more countin' dollars. We'll be, we'll become stars.
[13:13] We'll be watchin' bro. We can remember the lessons I learned.
[13:16] Say no more countin' dollars. We can remember the lessons I learned.
[13:32] Okay, so what you just saw is a PV of our new title, Silent Whispers,
[13:37] which is Fantasy Urban Romance with Cardinette 3D graphics.
[13:42] We pair premium visual and the story-focused gameplay,
[13:46] aiming to set a new benchmark for this type.
[13:49] And compared with live makeover, one major focus has changed.
[13:53] We, uh, male character design and rendering has moved to the center of our pipeline work.
[14:01] So we'll now look at four practical UE5 modules, materials and substrates,
[14:06] megalights, mobile lighting and shadows, and mobile hardware ray tracing.
[14:11] And now I will show you a real-time gameplay demonstration of Silent Whispers.
[15:06] Silent Whispers
[15:36] Silent Whispers
[15:46] Okay, so materials were already a big strength in our UE4 pipeline.
[15:51] And for our new game, we keep that advantage and push it further.
[15:56] So we switched to UE5's new substrate material system with key three benefits.
[16:02] So first, artists gain more direct control and higher flexibility.
[16:07] For example, artists can add its F0 and F90 values on their own.
[16:13] And second, updated the BRDF and advanced PBR deliver more physically accurate and lifelike results.
[16:21] And third, the tree-based material topology gave us richer and more flexible way to combine material behavior.
[16:32] So for our game, closing is not just a background decoration.
[16:36] It is open the subject of the short.
[16:39] And since our costumes feature lots of clothes off shorts, material quality is extremely important for us.
[16:45] And thanks to Substrate, we're able to achieve much higher fidelity costume rendering.
[16:50] But Substrate also brings adaptation trouble mobile.
[16:54] So it's really tough to keep mobile visuals matching the PC build perfectly.
[17:00] And we may target it optimization and costume changes.
[17:05] And next, let's look through how we make closing assets in our 3D pipelines.
[17:12] So as we all know, menswear and women's wear begin with different design logic.
[17:17] Male outfits often use fewer stacked layers and less structural complexity.
[17:23] So that puts more pressure on the overall silhouette, proportion and a few carefully chosen focal points.
[17:31] And the empty areas are not truly empty.
[17:34] When decoration becomes quieter, the fabric quality becomes louder.
[17:40] So we studied a lot of types of for mains clothes like plan weave, twill weave and roguish.
[17:48] For example, plan weave is the most fundamental structure with a one-to-one wrap,
[17:53] wrapped interlacing that produces a smooth and even surface.
[17:57] And you will find it in cotton shirts, linen, wood blend and poplin.
[18:06] So compared with female outfits, our mainswear focuses more on local refinements,
[18:13] overall silhouette and fabric texture.
[18:16] For large low contrast closing areas, we add fine woven textures,
[18:22] subtle wrinkles and varied stitching details to enrich the surface.
[18:26] And with substrate's accurate physical rendering, we deliver more realistic and high-quality closing visuals.
[18:34] So we already have a mature high-quality closing production pipeline.
[18:41] It's fully validated on mobile, balancing great visuals and stable performance.
[18:46] With skill material and texture for different devices, which unifies the visual experience for players from all the platforms.
[18:56] So this setting shows the improvement clearly.
[18:59] The production techniques begin in life makeover, and by integrating substrate into our pipeline,
[19:05] we improve the way light travels through and across the fabric.
[19:10] And the difference is subtle, but it changes the entire impression.
[19:14] The shirt no longer looks like a surface with setting texture.
[19:17] It begins to look like just a set-in.
[19:22] And now let's move from materials to lights.
[19:26] I will walk you through our Magalite Sync demo and show you how we built a massive dynamic lighting environment using programmable workflows.
[19:34] So traditional lighting pipelines limit artists a lot.
[19:40] Hardware limits always block better visual effects.
[19:43] So specifically, we have three main troubles.
[19:46] So the first was limited total light count.
[19:50] In traditional analytic lighting calculation, each additional light source introduces a linear performance cost,
[19:58] which means the team has to strictly control the number of lights.
[20:02] And the second was heavy manual setup work.
[20:06] Dynamic lights need costume blueprint codes for life cycle and fall off twigs cost lots of time and bug fixes.
[20:15] And third one was particle lights.
[20:19] Poor performance make us replace real particle lights with a massive billboard, which restricts our creative design.
[20:29] So instead of calculating every lights one by one in traditional pipelines,
[20:35] Magalites intelligently sample the lights that matter most for each pixel that we've used and reuses and cleans up those results over time.
[20:45] So artists can place many more dynamic lights in the same, including shadow casting lights without the cost of growing directly with a number of lights.
[20:56] So check out this demo scene.
[20:59] So how do we get realistic lighting for a complex environment like this?
[21:04] So as you can see in this footage, our scene runs on Magalites.
[21:10] Hundreds of dynamic lights updates in real time together.
[21:14] Total render cost to stay almost unchanged and we break the link between light count and performance cost in classic real time rendering.
[21:24] And next, let's look at our lighting setup.
[21:27] We use Niagara modular stack to build a scalable large procedural light system and three different program programmable light parts combine to make the amusement parks light show.
[21:41] So the first module controls the street lamps.
[21:44] You can see many connected light strips in the video.
[21:47] Every strips has more than 10 individually controlled bombs such such dense dynamic lights used to cost too much performance and management work before.
[21:57] And now every bomb cast a real light with specular diffuse and volumetric scattering and controlled by Niagara's procedure features bombs turn on step by step to match the camera changes.
[22:13] And the second module controls the ferries well.
[22:17] So unlike streets lengths, this one focuses on real time patterns line sequences.
[22:24] We use Niagara to make a switchable procedure system for all the wheels dynamic lights.
[22:30] As you see in this footage, we can light up tested on the wheels central lawn and with time procedural control,
[22:38] light spread outward from the center in the radio pattern across the whole wheel for rhythmic visuals.
[22:46] And third module controls the carousel.
[22:48] Besides basic color adjustment, we use Niagara to dry settings like volumetric scattering as show in this in this footage color shift outward from the carousel center and we boost volumetric scattering when certain lights turn on to build a dreamy atmosphere.
[23:08] So switch to components render mode for full light control lighting artists to King pick any light type and tweak each lamp's parameters freely.
[23:19] And they can also adjust IEI's profile as and light functions.
[23:26] And this is an actual gameplay for our game.
[23:38] So let's go.
[24:02] Yeah, and as a girl, I'm genuinely amazed to when the lights turn on step by step.
[24:07] So basically we have concluded five practical tips to maximize output with minimal cost.
[24:13] So first stick to base rendering by default.
[24:16] And second turn on component rendering only when needed.
[24:20] And third restrict to light boundary renders and force merge cluster lights.
[24:26] And the last one is that the layer setup, which means high quality with component rendering for close range and low cost base rendering for distance view.
[24:38] So now let's talk about optimizations from a bio hardware.
[24:42] Well mobile games mean a lot to our team and players.
[24:46] We always want to create great visuals on our platforms, including mobile devices.
[24:53] So first I would like to introduce the upgrades from a bio lighting and shadow rendering.
[24:58] Our new title silent whispers has lots of movie style costings and need high quality lights and shadows.
[25:06] And as for life maker were powered by you for it only used to one directional light in its render pipeline, but for silent whispers with switch to two defer rendering to support many more dynamic lights.
[25:21] And when there is a light, there should be a shadow.
[25:24] If the number of lights increases, but the shadow cannot keep up the result will look, you know, kind of strange or weird.
[25:32] And mobile hardware has limited performance.
[25:35] It needs lots of effort to reach high quality and enough quantity.
[25:40] For example, we cash shadow as much as possible for directional and a local lights.
[25:47] And also we adjust to shadow map bias algorithm to fix issues such as Peter panning and shadow acne.
[25:54] So for close up shots like this spotlight shadow flaws become very obvious on fingers.
[26:04] We can fix it by raising shadow map resolution or turning on contact shadow.
[26:12] On my hardware, there's another easier way we manually adjust the shadow position and size to feed the camera view.
[26:21] This boost the shadow quality without extra complex algorithms or performance loss.
[26:26] As you can see in the right picture, the finger shadow looks much better.
[26:33] And right now a mobile gains poor quality indirect allies ruins the cinematic feel a lot and to boost our players immersion we upgraded the indirect light system from a bio compared with life makeover.
[26:49] The updates less characters get subtle shadows inside dark areas and adds richer indirect light details, even though indirect light is low frequency.
[27:01] We also aim to match PC visual standards, which matters most when indirect light works as the main lighting source.
[27:10] As seen in this picture, faint light leaks on the characters arm in dark areas and this comes from low proposition and missing SSO effects.
[27:21] And this is small artifact but it breaks the physical relationship between the arm and the environment.
[27:30] And now compare the improved results.
[27:34] So now this the arm can sit naturally above the hand drill and the contact feels grounded and the lighting belongs to the same thing.
[27:44] Okay, so now let's look at the mobile hardware ray tracing.
[27:48] So when it comes to reflections or indirect specular, lots of modern props make reflections very noticeable to fix light leakage and the visual flaws we swapped our old reflection props for real time ray tracing.
[28:06] We now use both SSR and hardware ray tracing on mobile.
[28:12] Mobile hardware ray tracing still cost heavy performance and among common ray tracing uses like shadow, AO and GI.
[28:21] It seems ray tracing provides the best value we use for reflections, especially in things full of smooth shining objects.
[28:32] And okay, so this one is a reflection effect with SSR only.
[28:38] It misses a lot of content and now the right picture as ray tracing.
[28:44] It mixes many areas where SSR fails to generate reflections.
[28:49] And now you will see a video around entirely on mobile with our mobile rendering.
[28:54] It keeps great visual quality even on mobile devices.
[29:01] So let's take a look at the video.
[29:31] Let's take a look at the video.
[30:01] Yeah, so for the final part, let's move from rendering the character to building the character.
[30:07] So we picked matter human for three main reasons.
[30:11] So first it has full rig and DNA tools.
[30:15] We get ready-made high-quality standard character assets directly.
[30:20] And second, it fits perfectly with UE5's animation pipeline, make animation work more smooth and efficient.
[30:29] And third, it supports realistic stylized looks and we can tweak it well to run on limited mobile hardware.
[30:38] So matter human comes with full rig and DNA systems.
[30:43] It works really well, even with our stylized character models.
[30:50] And matter humans controls work great for animators, but how do we adjust to every facial muscle shape?
[30:58] So blind shape defines facial muscle forms.
[31:01] It sets a base for character expression, quality realism, and looks.
[31:06] And animators use controllers to arrange performances and final emotional expressions.
[31:15] Every key facial shape builds up character expressions and all of them matter a lot.
[31:21] So we use MH Expressions web app to get standard reference prototypes and make sure all expressions meet our standards.
[31:31] Actually, Apex official MHCC documentation offers recommended layered adjustment workflows like this.
[31:38] And throughout our development, we constantly found ourselves turning to Apex official pages where we hit a wall.
[31:46] And the answers were always practical and clear.
[31:50] And I think it's one of the reasons we're able to move as fast as we did.
[31:54] So if you're working in a UU5 system, making it your first stop.
[32:00] So for example, the left column has a top 13 influential expressions out of all 351.
[32:09] And this plus split symmetric poses on the right are our first priority group.
[32:15] And our three artists and needs repeated tuning to guarantee all follow-up expressions turn out correct.
[32:22] And all in all, MHCC give us a complete facial expression pipeline.
[32:27] But no matter how sophisticated the system, the accuracy of those face shapes is the foundation of everything.
[32:37] And now let's move to the body rig part.
[32:41] Original Matter Human only has a small number of corrective bones on limited spot.
[32:46] It is not enough for high quality body movements in silent whispers.
[32:50] So we used the post editor inside Matter Human for Maya to expand the full body skeleton.
[32:57] We added full body multi-direction post creatives and twisted bones.
[33:03] And these helps keep body volume and natural muscle deformation during big complicated movements.
[33:13] Well, in addition to using helper bones and maintain the intended silhouettes,
[33:19] we also spent quite a bit of effort on the interaction between the characters body and closing.
[33:26] So for example, when the arm bends, the sleeve cop gets pulled backwards and translated accordingly.
[33:34] And when the character sits, the pantomalags are lifted naturally.
[33:38] And this more details helps sell the realism of the closing.
[33:43] And in Engine, we reconstruct the setup from data stored in the DNA and use control rig to reproduce the driven relationship authors in Maya.
[33:55] And we also expose secondary controls in blueprint so the response can be tuned for garments with different lines, cards and silhouettes.
[34:05] And this gives us a reusable and scalable closing driving framework for production.
[34:13] So we have cowards, materials, translucency, lighting, shadows, ray tracing, face show expressions, body rigs and closing interaction.
[34:25] That is a lot of technology, but our final conclusion is not about feature, it's about how to choose.
[34:32] So across all of these systems, three principles guide our cross-platform character development.
[34:39] So the first one is performance first. Stable frame rate matters in everything.
[34:46] So for mobile especially, we balance visual and performance carefully to avoid frame jobs from overheating.
[34:54] And second is controllable visual quality.
[34:58] We don't rely too heavily on technology driven solutions.
[35:03] Instead, we'll put more emphasis on artcrafted assets so the game can scale across a wide range of devices.
[35:12] And third one is reusable workflow.
[35:15] We build on the stable existing pipelines and add new text step by step.
[35:21] And this workflow scales well for cross-platform character production.
[35:27] Yeah, so I think that is for today's presentation and I hope this can give you something useful to take back to your own projects.
[35:34] And these breakthroughs are the result of years of efforts of Mr. Bing Liu and his art team and also Nuva Lamp, the OxalSkames engine team.
[35:45] And now for the Q&A session, we're happy to have Mr. Shen Chen with us.
[35:50] He's the shift rendering engineer for OxalSkames and Nuva Lamp.
[35:55] And he's dipping the technical weeds on everything we've shown today.
[35:59] Thank you.



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
