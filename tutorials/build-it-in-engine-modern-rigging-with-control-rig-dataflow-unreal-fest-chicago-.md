---
title: Build It in Engine: Modern Rigging with Control Rig & Dataflow | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=wmC4S3Woj5I
author: Unreal Engine
ingested: 2026-07-24
ue_version: "UE 5.8"
tags: [control-rig, rigging, animation, chaos, geometry, pipeline, advanced, ue5-8]
extraction_status: complete
frames_dir: tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Build It in Engine: Modern Rigging with Control Rig & Dataflow | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=wmC4S3Woj5I)
**Author:** Unreal Engine
**Duration:** 37m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Welcome to Building it in Engine with Control Rig and Dataflow.
[0:06] So thank you so much for coming to our talk today.
[0:09] And also really glad to see you here at Unreal Fest Chicago.
[0:13] Okay, so I'm Chase Cooper.
[0:15] I run product for the rigging technology in Unreal Engine.
[0:20] So my history involves character development in games such as Fortnite.
[0:26] And before that, I worked in visual effects building hyper realistic creatures such as Hulk and the Avengers, Star Wars stuff, Rango, and assembling a bunch of works for the Warcraft movie.
[0:38] Hi, I'm Jim Van Allen.
[0:41] I specialize in physics and destruction at Epic.
[0:44] I've been there for about seven years.
[0:46] And before that, I was at ILM for about nine years, working on a lot of movies, doing destruction for like Pacific Rim.
[0:53] And like it was been really fun this week walking around Chicago because we worked on Transformers 3 and we destroyed all these buildings.
[0:59] So it's kind of deja vu walking down the street like, oh, I did that.
[1:02] So that's about me.
[1:05] All right.
[1:06] So can ask you guys a question.
[1:08] Who here knows what Dataflow is?
[1:11] If you can raise your hand.
[1:13] Oh, okay.
[1:15] Not a lot of people.
[1:17] So if you didn't know about Dataflow, you really should because it is awesome.
[1:23] And so throughout this talk, basically, we're going to show you is what Dataflow can do and what it's capable of.
[1:30] And we're going to talk a lot about skeletons today.
[1:34] Skeletons are the core of making characters work in Unreal.
[1:38] That probably is not new knowledge to you.
[1:42] But I want to make sure you understand how skeletons do work in Unreal and kind of break it down at a high level.
[1:50] So skeletons in Unreal work a bit differently than a lot of other software.
[1:54] Skeletal meshes act as a bucket that holds the mesh geometry and the skin weight deformations.
[2:01] The skeleton asset holds all the bones and transforms.
[2:05] And the nice thing about this structure is that the skeleton can drive multiple skeletal meshes.
[2:10] And you can easily share bones and skeletal structures for a different geometry.
[2:16] And so Dataflow generates content procedurally.
[2:19] So it can generate skeletons procedurally and plug directly into skeletal meshes, changing the skeleton asset.
[2:26] And so what really excited me when I first saw these tools and being a rigor and Unreal was that the possibility of not having to hand-build skeletons for control rigs.
[2:39] And so Dataflow is able to generate some pretty remarkable skeletons.
[2:44] These skeletons are all procedurally generated through Dataflow.
[2:48] And you also get skin weights during the same process.
[2:51] So I wanted to try these tools out, mixing generating skeletons from Dataflow and then seeing how that would work in control rig.
[3:00] So why would I want to do this?
[3:04] Because at the end of the day, if this works, my rig is truly 100% procedural.
[3:10] You generate the entire skeleton and weights in Dataflow.
[3:14] You generate all the rigging logic in control rig.
[3:17] And you're in Unreal in a real-time engine.
[3:23] So of course, a good simple test would do the trick.
[3:27] I thought the centipede with 100 or so legs was a nice example of that simple.
[3:32] So this skeleton and weights were built in Dataflow procedurally.
[3:36] And then I procedurally build a rig on top of it.
[3:39] And this rig is agnostic to the underlying skeleton.
[3:42] So in control rig, we have a node called the locomotor.
[3:45] And it procedurally lets you animate walking movement by adjusting limbs and the body based on the parameters.
[3:51] And so I can yank this control around and the rig will try to go to it and all the legs will animate.
[3:56] So while this is a really cool looking rig, the true exciting part of this,
[4:01] is it makes the entire animation completely procedurally built.
[4:05] So pretty much everything you're seeing here outside the model,
[4:09] in Unreal, is completely procedural.
[4:12] So I can swap this entire asset out with another centipede-like creature if I wanted and get very similar results.
[4:22] Okay, so a bit more practical example.
[4:24] In Unreal, we can also build rigs with modules in our modular control rig system.
[4:29] And to keep with our zebra theme of this Unreal Fest, I took this quadruped zebra
[4:33] and wanted to see how the skeleton would hold up to a rigger placing rig modules on it,
[4:38] prepping it for animation production.
[4:40] And so as you can see, we get a pretty usable result.
[4:44] It worked just fine.
[4:48] Okay, in Unreal Engine 5.8, we have a new system called Control Rig Dynamics.
[4:52] So it's a particle based physics system for rigs,
[4:55] and it's meant to be fast and used at runtime with control rigs.
[4:59] So you can author dynamic chains on characters for all sorts of things like ponytails and costumes.
[5:04] It's really a nice artist friendly way to author costume stuff and hair,
[5:12] because it's particle based, it's really fast.
[5:16] So Dynamics isn't a replacement for controlled physics that we added last year in 5.6,
[5:23] but more of a complementary system.
[5:25] It's designed to be easy to use, requiring as few nodes as possible to get a usable result.
[5:31] Because it's focused on runtime and it's particle based,
[5:34] we've measured it's about five times faster than the controlled physics nodes.
[5:39] So I originally saw Dataflow building skeletons and immediately had ideas for skeletonizing with control rig.
[5:47] So combining this with the new Dynamics tools, trees came to mind.
[5:52] Trees can be very difficult.
[5:54] So I started talking with the Dataflow team, and they had asked me for a single control that would let them animate trees.
[6:01] So while it's great for character skeletons, this works very well with trees and other complex assets.
[6:07] This tree would be pretty much next impossible to rig by hand.
[6:10] I mean, I could do it, that would be almost pretty torturous.
[6:13] So I'm able to leverage the new control dynamics tools by building a wind system using forces.
[6:20] You can add forces in here.
[6:22] So I'm using some control rig nodes to generate a noise field and plug that into a dynamics forces node.
[6:28] I can then animate this control to kind of give me an art direct on wind.
[6:32] So you can see I can even like visualize the wind vectors as I move this control around,
[6:37] and it gives me like a nice little looking wind.
[6:40] And so all of this is procedural generated, very similar to the previous examples I showed you.
[6:45] And this would have taken a very long time to build by hand.
[6:48] But now I have a fully animatable tree.
[6:50] So we're going to look at the bones here.
[6:52] You can see it built me a pretty nice skeleton, and it's quite usable.
[6:59] Okay, so I can take that same Dataflow skeleton graph in a new tree,
[7:04] and the same control graph and plug it all up.
[7:06] And with a few clicks, this is the results.
[7:09] Completely different tree, but same control and functionality.
[7:14] And so, and I can swap between different skeletal meshes too.
[7:18] So I've essentially built like a little tree generator.
[7:23] So there we go, just swapping between all these little trees that I've generated.
[7:27] So it would let me rapidly build, you can see how you could rapidly build a forest or vegetation
[7:33] that you know maybe you need for hero animation or anything else you can need.
[7:37] And the wind all works.
[7:39] I can use that animated around.
[7:44] So I thought it'd be good to take a little bit of a look at the actual process of this.
[7:49] Generating a skeleton in Dataflow and then building a rig.
[7:52] It's the thing that Jim and I have always kept talking about during making a lot of this content for the talk
[7:58] is like how easy these tools are.
[8:00] Yes, it's a graph, but they're very intuitive.
[8:04] And the results you get from it and from it being so easy is quite phenomenal.
[8:09] So, and that's been a real joyful process too.
[8:11] So I'm in Dataflow here and we're going to go more details in a little bit,
[8:16] but just kind of showing you the process of how you interface with Dataflow
[8:19] and how I was able to generate these tree skeletons.
[8:22] So we have some parameters you can add the node and I can preview the bones in here.
[8:27] So it gives you a nice view of like what it's going to do.
[8:30] And so anytime I want to change that after I've brought in the control rig,
[8:33] I can go back to the Dataflow graph and all that data will propagate into the control rig.
[8:38] So here I have a bunch of, I have a tree and I can swap it out for like another tree.
[8:48] Okay, so I'm making the rig procedural in doing here.
[8:55] Cool. So yeah, you get a lot of flexibility and I can go back to Dataflow graph
[8:58] and basically change it and it'll update my rig for me and I have all the dynamics and particle system.
[9:06] Okay, so another use case. In 5.8 we built this fun little zebra guy.
[9:11] You might have seen around Unreal Fest.
[9:14] And so the rest of this talk is going to focus on like a lot of physics and skeleton generation.
[9:20] I wanted to take a moment to talk about a really exciting feature that we added in 5.8 with Dataflow.
[9:25] And a requirement for building a face rig on this guy was we wanted to work on a lower resolution mesh
[9:31] and then use a higher resolution mesh for like a slightly better quality or final render.
[9:37] It's just much easier to work on the lower version of the sky.
[9:40] And so Dataflow ended up being the perfect tool to help with this.
[9:44] And so we wrote a transfer node in Dataflow and it lets you transfer rig attributes such as morph target blend shapes,
[9:52] skin weights, and any other mesh data to another skeletal mesh.
[9:58] And so as I mentioned, what's great is about Dataflow is its simplicity.
[10:02] And this transfer node doesn't take a lot of technical expertise or wiring.
[10:08] This is mostly the graph at its simplest form.
[10:12] You can get pretty crazy with it if you wanted to.
[10:15] But this is mostly what we used for the zebra and you can specify what kind of data you want to transfer over to the other mesh.
[10:22] And that's mostly it. And it was a pretty painless process.
[10:28] So let's see this workflow in action.
[10:31] Here's our animation on the lower as mesh and it's pretty good.
[10:35] And this would probably be totally passable.
[10:37] And this is a real time scene.
[10:39] So I'm just kind of zooming in so you can see the silhouette.
[10:42] And if you look at the edges, you can see you can kind of see the edges.
[10:45] We don't really want to see it.
[10:47] We really like the silhouette to be nice and smooth.
[10:49] And while you can see it on the edges of the character and silhouette,
[10:53] that's propagating to the rest of the mesh.
[10:55] So I've used Dataflow to make a high res version.
[10:59] I'm just going to swap it out.
[11:01] And as I swap it out, we get a really nice mesh that smooths out our character
[11:07] and no loss of performance with an improvement in visual quality.
[11:16] And so it just gives it that nice little extra 10% on your final animation.
[11:21] Cool.
[11:25] Pass it to Jim.
[11:26] Alright. Thanks Chase.
[11:28] Hey everybody.
[11:30] So I'm going to talk a little bit about, we're going to take a step back
[11:33] and talk about what Dataflow is and I'll tell you the story of where it came from.
[11:37] So Dataflow is a node based asset editor similar to Blueprint
[11:40] or Houdini or any of those node based things you've probably used.
[11:44] There's two key points that drove the development of Dataflow.
[11:48] The first one is for us as destruction artists, our lives are filled with sorrow.
[11:53] And the reason for that is because people always change our assets.
[11:57] So you can spend a few hours or a few days or even a few weeks working on something
[12:01] and if it changes your toast, you have to go back all the way back to the beginning and do it again.
[12:07] And so Dataflow is wonderful because it's a non-destructive workflow.
[12:11] So now when we get our new asset, we just plug it in
[12:14] and all the settings that we've worked on are still there.
[12:17] I'm going to skip the create recipes for a minute, but the next thing is the managing the asset pipeline.
[12:24] So we, the thing that really drove Dataflow for us was we had a massive game that had hundreds of destructible assets.
[12:31] There's no way we're going to be able to do it all without working nights and weekends.
[12:35] In fact, we'd still be working on it now, but we built Dataflow in order to process and manage all of that.
[12:42] And so now that game pretty much runs itself even now when they're updating and adding new assets.
[12:47] And it's pretty great.
[12:49] You probably, I think there was only one person who'd heard of Dataflow before today.
[12:53] And so you probably missed Cedric Hayo's talk last year at Unreal Fest.
[12:57] I threw in a link, but you can just Google it.
[13:00] And it's pretty great. It just shows you more in-depth stuff, mostly regarding the destruction pipeline.
[13:06] Okay, so we have a Dataflow use case here, which is Pinata.
[13:11] We took this asset and we want to hollow it out and fill it with candy.
[13:16] Some of you who have used Unreal for a while know that this is really stupid, that you wouldn't actually do this.
[13:22] You'd do Niagara or something like that.
[13:24] But it's really fun.
[13:26] So that's why we're doing it.
[13:28] In this case, what we're going to do is we are going to convert this mesh to a volume.
[13:35] We have brand new tools available in UE5-8.
[13:40] Let's see. Is it going to play?
[13:43] Sorry, my movie's not playing.
[13:46] Okay, there it goes.
[13:47] Yeah, and we also have some really cool visualization tools and ways to see what you're doing, what you're working on.
[13:53] In this specific example, we're creating two volumes inside the mesh,
[13:58] one of which we're going to pass on and do some stuff with later.
[14:02] And then the second one we're going to use as a Boolean against the original mesh.
[14:08] There it is. That's the interior surface of our hollowed out llama.
[14:13] We're going to do our little Boolean operation and then we'll run it through a uniform fracture node
[14:19] and there we have a nice clean fractured hollow llama.
[14:23] It's pretty cool.
[14:26] Okay, and now here's the volume that we had from the last slide.
[14:31] Sorry, again. Okay, there we go.
[14:34] And so what we're going to do is we're just going to take that volume and fill it with spheres
[14:38] and we're going to convert those spheres to points.
[14:42] If you view it too deany, this is probably really familiar.
[14:45] We're going to split those points into three different groups
[14:50] and then we're going to add a piece of candy to each group
[14:55] and we're going to adjust the colors, so on and so forth.
[15:00] And here's our result.
[15:03] So regarding the bullet point about sharing recipes, I didn't do any of this.
[15:07] This was created by my co-worker Jack Oakman.
[15:10] And you might be thinking, okay, that's great for him and for me because I get to use this stuff,
[15:15] but you'll probably never bother to go and make this on your own.
[15:19] Well, actually, you can get a version of this graph if you download the content examples
[15:24] and open the physics destruction level.
[15:26] We have one in here and we have a whole bunch of other data flow graphs in there.
[15:30] If you want to check them out and see some of the nodes, if you're like me,
[15:34] I just don't care about UVs and all of that boring setup stuff.
[15:38] So I let Jack do it all for me.
[15:40] And so I can just grab and adjust it and whatever I need to do.
[15:46] Another cool thing is you can expose attributes to users who are kind of dumb like myself.
[15:52] And so in this example, it's like what if management or the supervisors come back,
[15:57] they say we want four times as many pieces, right?
[16:00] Before data flow, you have to go back and redo your whole thing.
[16:03] It's never going to look as good.
[16:05] But now we just plug in a new number and this is what, 256 pieces instead of 25 or whatever it was before.
[16:13] That's pretty sweet.
[16:15] But wait, then they come back and they say, okay, we can't use the llama.
[16:18] It's copyrighted or something.
[16:20] We can't use candy because kids get cavities.
[16:24] So what if we use this mesh?
[16:26] In this case, with data flow, it's no problem at all.
[16:28] We just plug in this static mesh.
[16:30] We plug in these other little static meshes to replace the candy and we're good to go.
[16:36] I'm going to play it one more time because I think it's awesome.
[16:38] It makes me happy.
[16:43] Okay, so here's another thing.
[16:45] So what if they come back then?
[16:47] I don't know how many of you have used geometry collections, but still kind of new for some people.
[16:52] It's only like eight years old or six years old or something.
[16:55] But what if they come back and they say, okay, we need this to be a skeletal mesh.
[16:59] We can't use your simulation.
[17:01] We need the animators want to like do stuff with it and make it spin around and whatever.
[17:06] That happens a lot more than you might think.
[17:09] And so I bet you didn't know this because I don't think anybody knows this except for me.
[17:15] So you can right click and export your geometry collection to a skeletal mesh,
[17:21] which is really, really cool and really, really useful.
[17:25] And so in this example, all I did was do that right click to skeletal mesh and did a simulation,
[17:33] recorded it in take recorder, dropped it in the sequencer,
[17:37] and now I can make it go forwards and backwards and I can spin it around and do whatever I want as though it's a skeleton.
[17:45] So here's why that might be relevant if you're into rigging and animation.
[17:53] So mesh is made of discrete parts can be split during conversion to geometry collection and exported to skeletal mesh,
[17:59] which is what I just showed you, but you can also do it for things like this.
[18:04] It's a super simple trick, but it's extremely useful.
[18:08] Oh, by the way, before I forget, you can do templates.
[18:13] You can build your own templates and you can use templates that we've already created.
[18:17] You can use the template that I'm about to show you today in UE5-8.
[18:27] However, if you're like me, I didn't check to see if there was a template because our engineers are so fast,
[18:32] they checked it in without me knowing, so I built this myself.
[18:36] But anyways, here's to show you just how simple this is.
[18:39] We just take our static mesh, yada yada, we convert him to a geometry collection.
[18:45] You can see here, we call them bones in geometry collection, but they're really just parts of mesh parts.
[18:51] And so we have him all separated out into pieces and then we create a skeletal mesh.
[18:58] And that's just two nodes in Dataflow.
[19:02] We do another one to bind it to the skeletal mesh.
[19:05] I did cheat a little bit here.
[19:07] I added my own custom node that I made to try to do a round of parenting and just set it up
[19:14] and a little bit of naming to make it easier to work with.
[19:20] And then here's the final result.
[19:22] So I took the results that we just were looking at, spent about like 10 minutes reparenting a few bones,
[19:28] and now I have a skeleton.
[19:30] It's pretty cool.
[19:31] We'll see him again in a minute.
[19:35] Okay, so now I want to talk about trees.
[19:39] So I don't know if you've simmed trees before or not, but they are the worst.
[19:43] I hate trees.
[19:45] They either look perfect and nobody even knows that you did it, or they look weird and you get in trouble
[19:51] and then everybody freaks out because the trees look terrible and yada yada yada.
[19:55] You may have been there, I don't know.
[19:57] So after, I've got a lot of years of experience, I'm going to be honest with you guys.
[20:02] And so my solution for tree simulation is to trick someone else into doing it.
[20:08] And so we had a tree simulation come up and that's exactly what I did.
[20:12] I tricked my colleague Jack Oakman into doing it.
[20:15] And Jack is a bulldog.
[20:17] He won't give up on things even though they're impossible like trees.
[20:20] And so they started doing heavy, heavy geometric analyzing development.
[20:28] And what they ended up on was a way to build a medial skeleton that I think Chase showed you earlier.
[20:35] We built these pseudo skeletons to help with fracturing and managing crazy assets like this.
[20:43] And so the whole time I was watching this from afar without wanting to actually work on trees because I hate them.
[20:50] But just watching and plotting and scheming on how can I trick our engineers into adding the nodes to make these into real skeletal meshes.
[21:00] Because I don't care about fracturing trees, but I do want to do fun skeletal mesh trees and I want to do stuff like this.
[21:10] And so that was super fun and super easy.
[21:13] I'll show you how we set this guy up in a minute.
[21:20] And so that leads me to a thing we call mesh medial skeleton sampling, which we just call skeletonization because it's just less of a mouthful to be honest.
[21:32] This is brand new in Unreal 5.8.
[21:36] Hardly anybody knows about it, so you can go home and be the first at your company or wherever you work to use it.
[21:43] And people think you're really smart and cool.
[21:45] They thought I was until they see this talk and then they realize how easy it is.
[21:49] And I'll be back to whatever.
[21:52] But that's okay. That's okay.
[21:55] So what we're doing here is we're using spheres to sample medial axes throughout a mesh.
[22:00] Spheres are created by sampling points inside the shape.
[22:03] And wherever a sphere can touch two sides of the mesh is where we stop the sphere.
[22:08] And then we go in and look at connection and create connections by looking at the proximity and the shared points on the mesh.
[22:15] It's super complicated, but it's also super cool and easy to use.
[22:19] It's just one node.
[22:22] And so then we take the connected pieces.
[22:24] We add a second node called simplify medial skeleton.
[22:27] And what it does is it looks at all those spheres and follows the central shape and gives you a rational number of bones.
[22:36] The results are then simplified using an edge collapse algorithm similar to mesh simplification.
[22:42] And that's pretty, pretty cool.
[22:45] And so then this is our resulting skeleton.
[22:48] You can see there's it's not perfect.
[22:50] It's not really even too close to perfect, but it's a lot better than starting from nothing.
[22:55] And so you can export this immediately to the skeletal mesh editor and fix it up, which is what I did at first until I started writing some of my own data flow nodes, which you can do as well.
[23:07] And so in this case, we added a node that finds the hips and names everything.
[23:12] I don't know about you, but for me, the worst part of this is renaming all the bones.
[23:16] I absolutely hate that.
[23:18] So we got some nodes to rename bones, reposition them and do something that kind of makes sense.
[23:24] Now you're not going to send this to the animators right away, but it's still pretty dang close.
[23:31] Okay.
[23:33] And so I got to admit, I did a whole bunch of quadrupeds and is working like a charm.
[23:39] It's working great.
[23:40] We loved it.
[23:41] Did a bunch of bipeds, ragdolls.
[23:43] I'm not going to show you any of that because I showed Chase and the rigging team and those guys.
[23:49] They don't care.
[23:50] They don't want bipeds and quadrupeds because they already have all their skeletons and all their ragdolls are already developed.
[23:56] And you guys probably do too, I'm guessing.
[23:58] If you don't, you could download Manny and have it today.
[24:02] So this however got their attention because they don't have a prebuilt octopus rig and they don't have any rigs for a lot of these weird creatures.
[24:12] And so this is where this method starts getting really interesting and I think really useful as well.
[24:20] We're going to look at this graph here.
[24:24] Yeah.
[24:25] And all we do is we have our mesh.
[24:27] We run the default medial sampling node.
[24:32] We get our little spheres.
[24:34] We run a simplified node and it's even better.
[24:37] And then we're also running a subdivide node here to get more even distribution, get more joints out in the tentacles.
[24:45] And then that guy's good to go.
[24:49] I'm going to look at this guy with you guys.
[24:52] So this Centipede is a super weird.
[24:55] He's kind of creepy.
[24:56] He gave me nightmares.
[24:57] I'm going to be honest for a little while, but it's okay.
[25:00] I'm over it now.
[25:02] But so if you go home and you download UE5-8 and you start trying to use this and your models, it doesn't work.
[25:10] And you say that guy Jim is an idiot.
[25:12] He was lying the whole time.
[25:14] No, I wasn't lying.
[25:15] But some models are kind of messy, right?
[25:18] So models that are made up of a lot of different parts, the skeletonization isn't going to work as well on those.
[25:24] So what we did with this guy is he's already built in parts, different parts.
[25:30] So we just took the center part and made this kind of worm-like skeleton to represent his body pretty easy.
[25:38] And then we had all the legs and the antlers, whatever they are, the weird things, antennae and the tail thingies.
[25:47] That's my technical term.
[25:49] We had all that stuff as separate meshes.
[25:51] So we just ran that through Dataflow.
[25:53] We get really nice, really easy legs.
[25:55] It really is that easy.
[25:58] It's insane.
[25:59] I was telling Chase, I think it feels like magic, to be honest, or like what I would expect AI to be like.
[26:06] I feel like I'm using AI even though I'm not.
[26:09] None of this is AI.
[26:10] It's all our engineer named Jimmy Andrews.
[26:13] Anyways, we run a node.
[26:15] We made a node to parent the legs to the main body and we have a centipede.
[26:24] And here's the skeleton in the Skeletal Mesh Editor.
[26:28] Yeah, and again, the real story here now is I don't have to trick people anymore.
[26:33] I can just run it through Dataflow.
[26:37] I'm going to talk just quickly about this kraken as well.
[26:41] In case you guys go home and try to do this on some of your weirder meshes,
[26:46] this is another one where we had the tentacles and the legs were separate objects.
[26:54] So we just separated them out and ran them so that we could get fine-tuned control over the tentacles and the legs.
[27:01] And then we just plopped in the big shell thing because it's not going to deform.
[27:07] I had to do a little bit of skinning on it afterwards, but overall it's really, really easy to turn out creatures like this.
[27:15] And here's some results.
[27:18] You can make the creatures fight each other.
[27:20] This is all dynamic.
[27:21] There's no animation in here at all.
[27:23] These are all just kind of dynamic, trying to make them fight each other basically.
[27:30] It's just super fun for me at least.
[27:35] Okay, talk about a couple of dragons just to show you more examples.
[27:44] Yeah, these are really interesting to work with.
[27:47] They've got horns, they've got teeth, they've got wings, they've got claws.
[27:52] So they're a little bit harder than the quadrupeds and bipeds,
[27:55] and even the tentacled creatures were almost too easy.
[28:00] So yeah, so I'm going to show you the data flow graph here,
[28:03] and I'm going to talk a little bit about the properties that we're using.
[28:06] You guys obviously probably haven't used this at all.
[28:10] I'm assuming no one here has ever used this, but maybe after the fact you'll go back and try to use it.
[28:16] I'll just go over some of these properties.
[28:18] They might not mean anything now, but hopefully they'll make sense later.
[28:22] So we're going to just start with the static mesh.
[28:24] We bring them in there.
[28:26] We drop our medial skeleton sampling node on there.
[28:29] Really the only value I use is this one called min cluster error to split.
[28:36] You kind of up-increase that to get rid of a lot of the extra bones that are being created.
[28:42] It's super easy.
[28:44] I wouldn't really mess with a lot of the other values.
[28:47] And again, I should mention this stuff is all like, this is stuff is hot off the press.
[28:52] So all of this is brand, brand new.
[28:54] So we haven't really worked it out too much.
[28:57] So some of the naming might be a little weird.
[28:59] Some of the values might feel a little weird, but it's so easy to use.
[29:02] I think you can hopefully ignore or deal with that.
[29:08] So after we, yeah, one other thing, there's a max spheres value which is set to a thousand.
[29:14] And everybody I know's first instinct is to change that to say, okay, I want 25 bones.
[29:19] So they reduce that to 25, but the max spheres is actually more of like a number of samples rather than a spheres thing,
[29:26] or rather than like the number of joints you're going to end up with.
[29:30] Anyways, we drop a simplify node.
[29:33] And then we did drop a second simplify node, which I do because Jimmy Andrews told me to.
[29:40] I don't know why, but it does, it gives you just a second thing or a second pass at simplifying.
[29:46] And then we, all we did on that one is turn off prevent edge surface intersections,
[29:51] and that just cleans things up a little bit more.
[29:54] And we get our skeleton.
[29:58] And again, the skeleton is a little goofy because I didn't run any extra nodes to clean them up,
[30:03] but still come on.
[30:06] That's crazy.
[30:08] And that's literally three nodes, four nodes.
[30:11] I know, I guess five nodes technically.
[30:15] Yeah.
[30:17] I'm going to show this guy just because he cracks me up.
[30:20] The same kind of thing though.
[30:22] We have another skeleton.
[30:24] And you can see here, it's really cool, at least to me, to see all of the detail that the algorithm is picking up.
[30:32] It's picking up all the little spines going down his back.
[30:34] It's got his horns, his wings, his toes, his tongue, his eyes.
[30:40] It's really, really amazing.
[30:43] And then here's after simplification.
[30:45] We still have a few extra joints that we don't really want, but that's okay.
[30:49] We go in.
[30:50] In this example, I just cleaned it up in the Skeletal Mesh Editor because it was easier.
[30:55] All we did was get rid of some extraneous bones, but we did keep the tongue because it's hilarious,
[31:02] and I think the eyes got deleted at one point, so we added those back in.
[31:07] Here's one more dragon.
[31:10] You've probably seen this guy before.
[31:13] We used him because he's just super complicated with all the crazy stuff going around on his head.
[31:19] You can see here, the algorithm is picking up all of his whiskers and horns and fingers and all that sort of thing.
[31:28] Here he is simplified.
[31:30] And then here he is after running a custom node.
[31:33] I built a dragon node because it was fun to do and also because the quadruped node wasn't really doing it for us, for the dragons.
[31:42] But it's pretty sweet.
[31:43] You can add values to add as many spine bones as you want, as many tail bones, as many neck bones.
[31:51] In this case, I just have it just keep everything on the head because there's so much weird stuff going on there.
[31:57] It's easier to just keep it all and then I can deal with it later.
[32:01] You can see we're picking up the toes.
[32:04] Yeah, it's really cool.
[32:06] Yeah, as mentioned, I did make some new data flow nodes and we're like I said, this stuff is all so new.
[32:12] We're still kind of working out what extra nodes we need.
[32:15] I'm hoping we'll get some out in the very near future to help you guys with this stuff.
[32:20] You can write your own, but I'm hoping we'll get this into some sensible fashion very soon.
[32:28] And here's the dragon.
[32:29] This guy is 100% dynamic.
[32:31] His head's constrained to a cube.
[32:33] That's the only thing going on there.
[32:35] And then, ah, watch out.
[32:38] Oh no.
[32:40] Yeah.
[32:42] Okay.
[32:43] And then this is my last example for this stuff.
[32:47] We got the starfish.
[32:49] This was modeled again by my colleague who I trick into doing everything, Jack O'Chaman.
[32:55] This model is interesting because it was intentionally made to be really difficult to work with.
[33:01] So this thing has a full set of teeth.
[33:03] He's got eyes.
[33:04] He actually has a tongue and a huge like mouth cavity modeled in there.
[33:08] And so it's really hard for any volumetric or volumetric algorithms to go in and work.
[33:16] And this, if you just use this straight up, it will not work with the skeletonizer.
[33:20] I can tell you now.
[33:22] So don't try it.
[33:24] Or go ahead and try it.
[33:25] And then you'll see.
[33:26] You'll see that I'm right.
[33:28] Sorry.
[33:31] But yeah, so it was made to protesting flesh and cloth and I don't know why cloth, but anyways, flesh and all these things intentionally made to be difficult.
[33:41] So what we did is we said, okay, all we're going to do is we're just going to voxelize him.
[33:48] And so I don't know how many of you all know about voxelizing, but it's pretty, pretty straightforward thing you can do in U.
[33:55] I just went into the modeling mode and voxelize them and use the settings until I got something like this.
[34:02] This gets rid of all that internal stuff and just gives me an approximation of the model.
[34:06] And so it's another cool thing about data flow is you don't have to work on your final asset when you're setting this stuff up.
[34:13] You can work on anything and then plug in the actual asset at the end and it will still get rigged.
[34:19] The skeleton will still get applied to it.
[34:21] So it's really great.
[34:23] These are the results.
[34:24] It's pretty straightforward, but also really nice.
[34:27] It makes me happy.
[34:29] And then here's here he is in the skeletal mesh editor.
[34:34] In this case, we, sorry, we did the, that geometry collection to skeletal mesh trick that I showed you earlier.
[34:43] We did that for the eyes and teeth and then combine the two skeletons.
[34:47] So we kind of, kind of got that for free.
[34:50] Yeah, I'd say we got that for free.
[34:53] And then for this guy, I'm going to be honest.
[34:56] Again, I tried moderately hard to have him fight one of the other creatures.
[35:03] But he's just, he's kind of lame.
[35:05] He doesn't do it.
[35:06] He just falls over.
[35:07] I couldn't get anything.
[35:08] I couldn't get him to do anything cool.
[35:10] So we did this.
[35:11] We made a starfish gun.
[35:13] And, you know, it really makes me happy.
[35:19] I hope we can release this so you guys can play with it.
[35:21] And so now we have him shooting down the, yeah.
[35:25] So the, the, the dragons are floating and then the weight of the starfish actually slows them down.
[35:31] So last night we were at dinner and everybody's talking about their favorite game and this and that.
[35:36] And I kind of had to put my head down and say my favorite game is shooting dragons with starfish.
[35:43] It was really fun.
[35:44] I spent way too much time on this.
[35:49] So there he is.
[35:50] Yeah.
[35:51] And then in case you are curious and want to learn more about data flow, they dropped a massive number of docs today to my surprise.
[36:00] But we caught it at the last minute and added this slide.
[36:04] So we have a QR code if you want to grab that, or you could also just search Epic developer community data flow.
[36:11] They dropped like, I think five, four or five new docs that will help you get going.
[36:17] It's really great.
[36:18] We have a really, really great team.
[36:21] And, and yeah, they're constantly updating data flow and adding new stuff.
[36:26] And it's really, really cool.
[36:28] I hope you guys can be part of it with us.
[36:31] And then here's my, my final results.
[36:36] This is 100% dynamic creatures.
[36:40] They're interacting with the destruction, the destructible assets.
[36:44] They're interacting with some trees that you'll see in a second.
[36:50] Yeah.
[36:54] And oh yeah, I do want to mention.
[36:57] So we've realized that this is kind of silly and dumb.
[37:00] And I hope you're okay with that.
[37:03] But I hope you also get a sense of the real world use for this is insane.
[37:09] So I've already started using the skeletonization for all of my type of work, which is a lot more boring, but still cool stuff like cables, plants, trees, chains, all the things that are kind of horrible to work on.
[37:26] You can run through the skeletonizer and just get a skeleton right away and be off to the races.
[37:32] And then I think there'll also be serious implications for, for people rigging and setting up creatures.
[37:40] So I think that's cool.
[37:42] Yeah.
[37:43] That's it.
[37:44] Thank you so much.
[37:45] I think that's it.
[37:46] Yeah.
[37:47] Yeah.
[37:48] Thanks.
[37:56] Yeah.



---

## Captured Frames

- [3:51] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_000.jpg
- [6:33] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_001.jpg
- [8:25] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_002.jpg
- [10:08] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_003.jpg
- [14:19] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_004.jpg
- [18:56] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_005.jpg
- [24:34] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_006.jpg
- [28:30] tutorials/frames/build-it-in-engine-modern-rigging-with-control-rig-dataflow-unreal-fest-chicago-/frame_007.jpg

---

## Structured Notes

### Core Technique
[UE5.8 required] Fully procedural rigging: generate skeletons + skin weights from any static mesh with Dataflow's new mesh medial skeleton sampling ("skeletonization") nodes, then build skeleton-agnostic rigs on top with Control Rig — including the new particle-based `Control Rig Dynamics` system for runtime secondary motion.

### Summary
Epic's Chase Cooper (rigging product lead) and Jim Van Allen (physics/destruction, ex-ILM) show how Dataflow — a non-destructive, node-based procedural asset editor — can generate complete skeletons and skin weights for arbitrary meshes (trees, centipedes, octopi, dragons, starfish), which Control Rig then rigs procedurally so the whole character setup is 100% in-engine and re-usable across swapped assets. Along the way they cover the new 5.8 `Control Rig Dynamics` particle physics (≈5× faster than 5.6's Control Physics nodes), a Dataflow transfer node that moves morph targets/skin weights between low-res and high-res skeletal meshes, and the right-click "geometry collection → skeletal mesh" export trick for making animatable props from fractured/multi-part meshes.

### Key Steps
1. **Understand UE's skeleton split** — the `Skeletal Mesh` asset holds geometry + skin weights; the `Skeleton` asset holds bones/transforms and can drive multiple skeletal meshes. Dataflow generates skeletons procedurally and plugs them straight into skeletal meshes.
2. **Create a Dataflow graph on a mesh** — right-click the asset → Dataflow setup, pick a template from the `Choose Dataflow Setup` dialog (5.8 ships a **Skeletonizer Template**, Subdivision Template, Mesh Split Template, etc. — frame [10:08]).
3. **Skeletonize** — drop a `Medial Skeleton Sampling` node on the static mesh (spheres sample medial axes inside the shape; spheres stop where they touch two sides, connections come from proximity/shared mesh points).
4. **Simplify** — add a `Simplify Medial Skeleton` node (edge-collapse, like mesh simplification). Optionally a second simplify pass with `Prevent Edge Surface Intersections` OFF for extra cleanup, and a `Subdivide Medial Skeleton` node for even joint spacing (used on octopus tentacles — frame [24:34]).
5. **Clean up** — export to the `Skeletal Mesh Editor` to fix stray joints/renaming, or use extra Dataflow nodes (hip-finding/renaming/quadruped/dragon nodes shown are custom; Epic plans to ship more).
6. **Multi-part meshes** — skeletonization struggles on meshes built from many parts; run body and appendages (legs/tentacles) through Dataflow separately, then parent with a node. For messy closed models (starfish with modeled teeth/mouth cavity), voxelize an approximation in Modeling Mode first, rig the proxy, and plug the final asset in at the end — the skeleton still applies.
7. **Rig in Control Rig** — build a procedural, skeleton-agnostic rig; the `Locomotor` node auto-animates walking by adjusting limbs/body toward a dragged control (100-leg centipede demo — frame [3:51]). Modular Control Rig modules also work fine on Dataflow-generated skeletons (zebra demo).
8. **Add secondary motion** — [5.8] `Control Rig Dynamics`: author particle-based dynamic chains (ponytails, costumes, tree branches). For wind, generate a noise field with Control Rig nodes and plug it into a `Dynamics Forces` node; animate one control for art-directable wind with visualizable vectors (frame [6:33]).
9. **Iterate non-destructively** — change the Dataflow graph (or swap the input mesh) and the skeleton, weights, rig, and dynamics all propagate — an instant "tree generator" with one shared control graph.
10. **Bonus tricks** — Dataflow `Transfer` node copies morph targets/skin weights/mesh data from a working low-res mesh to a high-res render mesh (zebra face). Right-click any `Geometry Collection` → export to `Skeletal Mesh` (bones = mesh parts), record sims via `Take Recorder` into `Sequencer` to scrub/reverse them like animation.

### UE Systems / Blueprints / Settings
- **Dataflow** — node-based, non-destructive procedural asset editor (born from destruction pipeline management); graphs are shareable recipes; example graphs ship in Content Examples → Physics Destruction level.
- `Medial Skeleton Sampling` node:
  - `Min Cluster Error To Split` → **the main dial**; increase it to remove excess bones.
  - `Max Spheres` (default 1000) → number of *samples*, not resulting joints — don't lower it expecting a bone count.
- `Simplify Medial Skeleton` node → run twice; on pass 2 disable `Prevent Edge Surface Intersections` for a cleaner result. Full dragon skeleton = ~5 nodes total (frame [28:30]).
- `Subdivide Medial Skeleton` node → even re-distribution / more joints along limbs.
- `Transfer` node → transfers morph target blend shapes, skin weights, any mesh data to another skeletal mesh; minimal wiring (zebra low-res → high-res, no performance loss).
- Geometry Collection → Skeletal Mesh: right-click export, or 2 Dataflow nodes (+1 to bind) — frame [18:56].
- **Control Rig Dynamics** [5.8] — particle-based rig physics, runtime-focused, ~5× faster than `Control Physics` nodes [5.6]; complementary, not a replacement. Forces input accepts noise fields for wind.
- `Locomotor` Control Rig node — procedural locomotion from parameters; rig chases a dragged goal control.
- Docs: search "Epic developer community Dataflow" — 4-5 new official docs dropped at Unreal Fest Chicago 2026.

### Difficulty
Advanced

### UE Version
UE 5.8 (skeletonization nodes, Control Rig Dynamics, Skeletonizer template are all new in 5.8; Control Physics is 5.6)

### Tags
control-rig, rigging, animation, chaos, geometry, pipeline, advanced, ue5-8

---

## Related Entries
- `tutorials/control-rig-in-unreal-engine.md` — Epic's Control Rig documentation (shares: control-rig, rigging, animation) — the baseline system this talk builds on; also see `references/control-rig-animation.md`.
- `tutorials/physics-in-unreal-engine.md` — UE 5.7 Chaos physics reference (shares: chaos, animation) — geometry collections, fracture, and rigid-body foundations for the Dataflow destruction tricks shown here.
- `references/release-notes-ue58.md` — UE 5.8 feature context for Control Rig Dynamics and the new Dataflow skeletonization nodes.
