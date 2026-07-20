---
title: How to Build Scalable MetaHuman Crowds in Unreal Engine | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=wQoa1j4Rgss
author: Unreal Engine
ingested: 2026-07-18
ue_version: "UE 5.8 (MetaHuman Crowds + Collections both experimental)"
tags: [metahuman, animation, performance, blueprint, cpp, worldbuilding, advanced]
extraction_status: complete
frames_dir: tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to Build Scalable MetaHuman Crowds in Unreal Engine | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=wQoa1j4Rgss)
**Author:** Unreal Engine
**Duration:** 43m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So welcome to this session on how to build scalable metahuman crowds in Unreal Engine.
[0:09] Quick introduction, my name's Henry Folkiner. I'm a principal engine programmer on the
[0:13] metahuman engineering team. I've been working in Unreal professionally for about 18 years.
[0:19] And before I joined Epic, I was at a couple of different game developers, mainly Ninja
[0:24] Theory. I'm the engineering lead for metahuman crowds, and I also created metahuman collections
[0:31] that the crowd system relies on. So start with a video. This is the metahuman crowd.
[0:39] This is the sample that we're releasing in fab today. You can see it's pretty diverse
[0:44] crowd. We've got 1,000 metahumans, a lot of different content in there, clothing
[0:49] hairstyles, faces, bodies. And there's one metahuman in particular that I'm looking for.
[0:55] There she is. She's wearing an Unreal Fest shirt. Lovely. Glad you enjoyed that.
[1:02] Yeah, so there's one unique metahuman in the whole crowd, and that's just a demonstrate.
[1:07] Just to give you a little bit of an idea of what you could do with this, that you can do
[1:11] interaction as well. So in this session, I'm going to go through what is a metahuman crowd.
[1:18] So what are we looking at in that video? How is it rendered? Then we're going to talk
[1:22] about how to use metahuman crowds, how you could put one in your project, and some advanced
[1:28] tips as well. How you could go beyond what's in the sample. And then I'm going to talk a
[1:33] bit about metahuman collections, which is a key technology behind crowds. So what is
[1:38] a metahuman crowd? I want to start with some numbers, because this is something that
[1:43] I would always want to see when I was a game developer. As you can see, we're targeting
[1:49] 60 frames a second on almost all devices. So on recent mobile, we targeted 30 just to
[1:56] avoid thermal throttling. But if you look at the unit times across there, you can see it
[2:02] does actually run at 60. And then the only other platform where we didn't get to 60 is
[2:07] the last handheld, which is Switch 1. And that's just the appropriate frame rate for
[2:14] that platform. If you look at the game thread time, you can see there is a bit of headroom
[2:19] available there for gameplay. You can always reduce the spawn count to make more headroom
[2:25] or optimize the content further. So there's quite a lot of flexibility there. And I think
[2:31] this is definitely something that people could really use in a real project.
[2:37] Because of content variety in the crowd, we've got 16 heads, 8 bodies, various hairstyles
[2:43] and clothing. And even on a given item of clothing, colors can be changed per character
[2:49] and still render efficiently. And I think, again, this is pretty representative of the
[2:55] amount of diversity you'd want in a real project. So the first piece of technology that I want
[3:01] to talk about is mass. Mass is a system for simulating large numbers of entities efficiently.
[3:08] It was used for vehicles and pedestrians in the Matrix demo. It's also used in various
[3:14] other projects, Lego fortnight and so on. And in our crowd, each character is a mass entity.
[3:21] We use state tree for the behavior. So they just have a simple wonder behavior where they
[3:25] choose a point and walk to it. Of course, you can do more exciting things if you want.
[3:32] And mass also controls how the entities are visualized. So we've got two tiers of visualization.
[3:39] The characters closest to the camera are actors. And the rest of them are instance skinned
[3:45] meshes. And if I, I'll pause that. You can see that the characters there in gray
[3:54] are the actors and the characters are switching back and forth between actor and instance skin
[4:00] mesh while maintaining their pose. So you don't get an animation pop as they switch.
[4:06] So I mentioned instance skin mesh components. This is a fairly new component. We call the
[4:14] instance is ISKM's for short. That stands for instance skinned mesh as opposed to ISM,
[4:20] which is instance static mesh. So just if you see that reference anywhere else, that's
[4:24] what it means. This is not vertex animated textures. These are fully skinned meshes animating
[4:31] on the GPU. And it runs through Nanite if it's available, but it also works on non-nanite,
[4:37] just the same. So I've got a video here. This is not met human crowd, but this is a blueprint
[4:44] with some instance skinned mesh components on it. And I've got 10,000 instances there.
[4:51] You can see that's running at a solid 80 or 90 frames a second on a PC. So really incredibly
[4:57] efficient. Here's another video. It's the same scene. So 10,000 instances with Nanite.
[5:03] And watch the frame rate in the top left there. You can see it's nice and stable as I'm looking
[5:07] around. And there are different numbers of instances on screen, but that's staying nice
[5:11] and stable. Got the same scene again, but without Nanite. And you can see the frame rate
[5:17] is a little lower. And it varies as you look around. So Nanite's really doing a great
[5:22] job of keeping a stable frame rate. But of course, on non-nanite platforms, you've still
[5:28] got way more efficient rendering than you would if you were using individual skeletal mesh
[5:34] components. So here is something we do a bit differently on the crowd compared to a normal
[5:40] metahuman. There's no instance version of the groomed component. And so what we do
[5:45] is we take standard groom assets that you've used with metahuman creator before. And we
[5:51] convert the card meshes and helmets to skeletal meshes. And we skin them to the individual
[5:58] faces in the crowd. For shorter hairstyles, we use baked grooms, which is just a texture
[6:05] that's rendered as part of the skin. And because we're not using groomed component, there's
[6:11] no physics simulation. So that is something that we lose. And I just have this video just
[6:15] to show the skin inequality that we've got there. So skin nicely to the face. You can
[6:21] still have facial hair. And that will work. Next. So ISK animation, if you've been following
[6:29] this, you might have heard of an in banks. There's also an in sequence transform provider,
[6:34] which is a new thing. It is much more fully featured than an in banks. And it allows
[6:41] you to have things like layered blending. And it does translation retargeting, various
[6:48] other things. So it's much more sophisticated than an in banks if you had looked into
[6:52] that before. And we make good use of that on the crowd. Also, another thing about ASTP
[7:00] is that you can play animations at different offsets. So this is still all one set of
[7:05] instances, but they're playing that walk animation at 100 unique offsets so that you
[7:12] don't really see repeating patterns of animation within the crowd.
[7:17] Next. Each character is made up of multiple meshes. So the top garment, bottom garment and
[7:24] shoes, for example, are all separate. And the reason for that is for instant singe efficiency.
[7:31] You can see the two characters here have the same body type, they're wearing the same
[7:34] clothes. We want to make sure that we can instance those meshes. So we're just using one
[7:42] instant skin mesh component for that shirt across all those different characters, even
[7:47] if they're wearing different clothes on other parts of their body. I've got another image
[7:51] here where I break it out so you can see the different meshes that are used on those
[7:54] two. Their face is unique. And you can see that the hair is unique as well because it's
[7:59] skin to the individual face. But they do share the clothing meshes. And you'll also notice
[8:07] that we merge the body geometry onto the clothes. And the reason for that is the clothing is
[8:12] already unique per body, so there's no loss of instant singe efficiency from doing that.
[8:18] That's just a way we reduce the number of instant skin mesh components we're using.
[8:23] I've got a little quality comparison here just to show the difference between cinematic
[8:28] and cinematic metihuman from metihuman creator and crowd actor. So bottom line is the very
[8:37] little difference. We use Lod2 as the top Lod for the crowd, but that is configurable.
[8:42] You can change that if you want. We're still using rig logic on our crowd actors for facial
[8:47] animation and for volume preserving correctives on the body. And the main difference, as I
[8:55] said before, is there's no groom component, so it's the skeletal mesh groom cards there.
[9:02] You might see that the groom appears a little bushy, a bit thicker on the crowd character,
[9:09] which is on the right. And that's because we're using a master material there. But actually,
[9:13] you could use Translucency in this case since it's not using Nanite. Glad you enjoyed
[9:20] that. Let's go on to the next one. So a comparison between the cinematic metihuman and the
[9:28] instant mesh. So we use Lod4 from the cinematic as our top Lod here. We nail Nanite, of course,
[9:35] there's no rig logic because STP is just a fixed function animation system doesn't support
[9:41] rig logic. What we do is we take your animations and we automatically bake them using rig logic
[9:49] to joint animations. And then that's what we play on the instant meshes. So we still have
[9:56] full facial animation across that entire 1000 metihuman crowd that you saw. We found that
[10:03] Vertex cost was really important to get down, especially for low-end platforms. You think
[10:09] about every Vert you save is a thousand times because of the number of people in the crowd.
[10:15] So we remove the Translucent sections. There's eye moisture and saliva meshes on the original
[10:22] metihuman. Nanite doesn't support Translucency at the moment anyway, so we remove those. And we
[10:28] also reduce from 8 down to 4 bone influences per vertex to reduce the cost. But at these kind
[10:36] of distances that you're going to see these characters, it's not really noticeable in my opinion.
[10:41] And I think it's really impressive just to have that level of animation quality that you can see
[10:47] here across that entire scene. One more thing with the Nanite male fuel for it. We do disable the
[10:58] teeth to save even more Verts, but you can turn them back on. There's a checkbox, so don't worry
[11:02] about that. Just thought it probably wasn't needed due to the kind of animations that you play on
[11:07] background characters. We can get away with that. So a new asset is the metihuman collection asset.
[11:14] It is kind of a container that references source assets. So you drag in your assets from the
[11:21] content browser, so talking about hair, clothing, bodies, places. And it uses a collection pipeline,
[11:30] which I'll get onto, to process those source assets. So that's doing things like fitting,
[11:35] clothing to the bodies, generating those hair meshes. And then those generated assets get saved
[11:43] back into the collection. The collection is cooked, taken with you into the cooked build, and then
[11:49] that's used as a data source when we come to render the crowd. So metihuman crowd pipeline. This
[11:56] is the collection pipeline I was talking about. The one that we use for crowds is metihuman crowd
[12:00] pipeline. The pipeline is kind of the brains of the collection. It defines what slots are available.
[12:07] So you can see along the top there, we've got filter buttons, so you can filter by slots, heads,
[12:15] bodies, top garment, etc. All those different slots that we define. You can make your own pipeline,
[12:20] define your own slots for your needs. The pipeline also processes the assets, so it's generating a
[12:27] separate mesh for the actors versus the instance, meshes, and those are the processing things I
[12:34] mentioned. And then at runtime, the pipeline is responsible for putting those parts together and
[12:40] assembling the character. Finally, we've got the metihuman instance asset, and this kind of goes
[12:46] hand-in-hand with the collection asset. So an instance defines a specific character drawn from
[12:52] items in the collection. So if you can imagine you've got a collection that's got five different
[12:57] shirts in it. The instance is choosing one particular shirt in that particular color to be on one
[13:03] specific character. And I like to think of them as material instances. That's kind of where the
[13:08] name comes from as well. The collection is sort of like the material in the sense that it defines
[13:14] a possibility space for all of the kind of characters that you could make, and then the instance
[13:19] is one specific character. And as it says, you can generate them at runtime as well.
[13:28] So, just going to recap this section. We've got mass, which hosts and visualizes the entities.
[13:35] The sort of layer of characters in front of the camera is going to be your high-quality actors.
[13:41] Instance measures behind that. Metihuman collection references the source assets and stores the
[13:47] generated results. The crowd pipeline processes the assets and the instance defines the appearance
[13:52] of a single character. So let's look at how to create a crowd. I've got two parts here. How to
[14:02] make your own crowd in three steps. So I'll go through that and see how easy that is. And then
[14:06] there's some advanced tips so you can take it beyond what we did. So the first thing you want to
[14:13] do is download our sample. And this is on Fab. It's called Metihuman crowd sample. You can search it.
[14:19] There's a QR code here that takes you straight to the listing. And the reason I'm suggesting
[14:24] starting with that is there's some assets in the crowd that take quite a bit of setup. Like the
[14:30] mass config for example has about 15 different traits on it and it's a lot to set up from scratch.
[14:35] So the easiest thing is to grab the sample. It's got this folder in it called Start a Kit.
[14:41] I'll just go on my great me and that is designed to be migrated into your project.
[14:46] It's just a self-contained minimal set of assets that you can start from.
[14:54] Next step we're going to create our collection and instances. So this is where you bring in
[14:59] your assets and use them to make your crowd. Right-click in the content browser, create Metihuman
[15:07] collection. Once you open that collection, open to its own editor and there's a pipeline
[15:14] property. If you look in the bottom right and you can create an instance of a pipeline there,
[15:19] choose the crowd pipeline. If you expand the properties of the crowd pipeline,
[15:25] there's a property for the animation config. We've got one in the Start a Kit for you,
[15:31] which gives you the idle and walk animation used in the sample. You can add your own and I'll show
[15:36] you how to do that later. And then we're going to add our clothing and hair to the collection.
[15:41] So it's all the same asset types that we support for Metihuman creator, chaos outfits including
[15:47] the resizable ones, skeletal meshes for clothing and groom bindings for hair.
[15:53] If you've got existing wardrobe items that are set up for Metihuman creator, so hidden surface
[15:59] maps, material parameters, you can drag those into the collection and all of that setup carries over.
[16:08] Yes, I point about hidden surface maps. So if you remember back to the slide where I had the
[16:13] meshes separated out and you saw the body geometry most onto the clothing, we used the hidden
[16:18] surface maps of the clothing to figure out which parts of the body to attach. So it's quite
[16:25] important to have accurate hidden surface maps for that. Right, I'm going to take a moment to
[16:33] talk about wardrobe items. It's quite an important concept for collections. And so a wardrobe item
[16:41] is a reference to a source asset like groom binding or whatever. And it's also an item pipeline.
[16:48] And that's that word again, pipeline. So we talked about the Metihuman crowd pipeline.
[16:53] That's a collection pipeline. That attaches to the collection.
[16:56] Items have pipelines as well. And the item pipelines job is to kind of format the source asset that
[17:08] is associated with that wardrobe item for the collection pipeline. So the collection pipeline can
[17:15] accept it. So I've got a little diagram here. On the right, there's the Metihuman crowd collection
[17:21] pipeline. You see the top garment slot has a pin there. So it's sort of like a blueprint. Imagine
[17:26] that like an input pin. And you can see that has a particular data format that that slot is expecting.
[17:35] And there's two different item pipelines that can produce that data format. So there's the
[17:39] Metihuman crowd outfit, item pipeline, and the Metihuman crowd skeletal clothing item pipeline.
[17:44] And each of those can fit in there. And basically this is an API boundary. And what that means is
[17:53] if you make your own pipeline, your own collection pipeline, if your slot, if your clothing slots
[18:01] accepts this same data format that ours do, you can take wardrobe items that have been set up
[18:07] for crowds or from Metihuman creator and use them with your pipelines. So you don't have to redo
[18:12] that work that's being done in those item pipelines. And the other way around as well,
[18:17] if you want to have your own item pipeline, as long as it's as long as it outputs the data in that
[18:22] format that we expect, you can slot that in to our collection pipeline. So it's just enables a bit
[18:29] more reuse of code there. The other thing to be aware of is that the source asset reference from the
[18:36] wardrobe item is editor only. So you're dragging things like groom bindings into the collection,
[18:43] but those original grooms aren't going to be cooked because those are just editor only references.
[18:49] The only things that will be cooked along with the collection are the skeletal meshes that get
[18:53] generated from that groom. So there's two different ways you can bring in wardrobe items into
[19:01] the collection. First one is external. So if you've got a wardrobe item asset in the content browser,
[19:08] that's outside the collection, that's external. So yeah, you might have set it up from Metihuman creator
[19:14] or just for crowds. And if you drag in that wardrobe item into the items panel,
[19:21] it is external, it becomes an external one. And you then click on the item, you'll see on the right
[19:28] that the properties are read only. So you would have to go out to the original wardrobe item
[19:35] asset to edit those and that connection is maintained. So that's useful if you have multiple
[19:40] collections where you want to use the same wardrobe item, for example. The other way is internal.
[19:47] So if you drag an asset, so in this example, I've got this boots outfit asset that doesn't have
[19:53] a wardrobe item asset of its own. I just dragged that straight into the collection.
[19:58] We create an internal wardrobe item within the collection. And so you can see, I've clicked on that.
[20:04] And the properties are editable there and it's all blank ready for you to fill out. So that's just
[20:09] the idea is it's more convenient if you have a lot of clothing or hair or other kinds of assets
[20:15] that you want to bring into the collection. You don't have to go and create extra wardrobe item
[20:20] assets for those before you can import them. You just import them and then you set up the wardrobe
[20:25] item stuff in here. When you're setting up a wardrobe item, you need to choose an item pipeline class
[20:33] and for the crowd, all of the crowd ones have crowd in the name. So it's pretty straightforward
[20:39] to choose the correct one for the source asset. All right, so we've made our collection.
[20:46] We've added our clothing and hair. Next thing we need to bring in heads and bodies. And for this,
[20:50] we use a metahuman character asset. So this is the same asset used by metahuman creator,
[20:58] so you just create your characters in the normal way. If you want to have multiple heads
[21:05] sharing a single body type, that could be a good idea because it means you don't have to have
[21:11] as many different clothing meshes, for example. It's very easy to do. Just start with one character
[21:19] and then if you duplicate that character, they'll have the same head and body and then all you have
[21:24] to do is just edit the head and the bodies will still match. The next theme is entirely determined
[21:30] by the body. So as long as you only edit the head, those heads will be interchangeable across those
[21:36] characters. Next thing is you need to assemble the characters. And that's because the crowd pipeline
[21:45] doesn't do things like bake materials down to textures the metahuman creator does. So we rely on
[21:50] metahuman creator for that. So if you've used metahuman creator before, it's just the same process
[21:56] that you're used to. I would recommend using the joint-sownly rig, however, because the difference
[22:02] between that and the full rig is that the full rig adds blend shapes that are only used on
[22:07] LOD0. And if you're not using LOD0, which we don't by default, you're not getting any benefit from
[22:14] those blend shapes, but they do make the asset take longer to load. So you're not really gaining
[22:19] anything except for load time and disk usage. So I would just use the joints only rig for that.
[22:26] The other thing is you want to make sure all hair and clothing is removed from the character
[22:29] before you assemble when you're going to use it with crowds. And that's because the hair that
[22:35] supplied affects the skin textures and the clothing that supplied affects the body geometry. So just
[22:42] take all that off and then you get the the plain heads and bodies out of there. The next thing is
[22:49] for characters that you're going to use for bodies, you need to export a full body skeletal mesh
[22:55] which is a mesh that has the head and the body merged together in one single mesh. And that's
[23:00] because that's what we use to resize the clothing. If you're using skeletal clothing that's not
[23:06] going to be resized, you still need to do this because the system just requires it. So the easy way
[23:13] to do that is going to the export tab in metheumen creator, choose geometry export, and then make
[23:18] sure full body skeletal mesh is checked and just export that. So it's just one step really.
[23:23] Okay, we've made our heads and bodies. Now we bring them into the collection. So you just drag
[23:29] them into the appropriate zone. If you've got you know if you've got more heads than bodies like we do,
[23:34] we've got 16 heads, drag them into the head zone, and then your sort of body archetypes that you're
[23:40] using drag those characters into the body zone. Because you're just dragging their assets in,
[23:47] they don't have wardrobe items already. They will get internal wardrobe items. So you need to go
[23:52] through and set those up. And really all you're doing is you choose the character item pipeline,
[23:59] and then there are properties in there for face and body mesh and so on. And you just go into the
[24:05] assembled assets that you created before and select those. So it's pretty straightforward.
[24:13] So we've added all the items to the collection. Next thing we need to build the collection. And this
[24:18] is the kind of the long running step where we're generating all of the fitted clothing meshes
[24:24] for each body. We're generating the groomed skeletal meshes and skinning those to the face and
[24:30] all of that stuff. That happens when the collection is built. So if you've made changes to the collection,
[24:36] as we just have the apply button or be lit up, click that button. That's going to apply your changes
[24:42] and build the collection. Later on, if you have changed any of the source assets,
[24:48] those changes won't get picked up automatically. You'll have to come back into the collection
[24:51] over to and click rebuild. The longest running steps in there are cached in the DDC. So even though
[25:01] it will probably take a few minutes, depending on how much content you added the first time,
[25:05] the next time you do it should be significantly faster, like many times faster.
[25:09] So if the collection is built correctly, you should now be able to preview some characters.
[25:18] And once the collection is built, that's the long step out of the way. So you can double click
[25:24] on the items to equip them. And you see they get a little icon in the bottom right there
[25:29] when they're equipped. And then you see the character previewed in the viewport. And you can
[25:33] easily just click around, just apply items. All of the hard work's already done. And it's just
[25:40] switching between different generated measures at that point. So it's really fast.
[25:46] Next, we need to create some instances. There's going to be used for our unique appearances in the
[25:50] crowd. So just right click on the collection asset. You get a similar editor, but it's not exactly
[25:57] the same. You can't drag new items in here. You're just selecting from the ones that are built in the
[26:02] collection. There's also, it's not shown here, but there's a part on the right where you have
[26:09] color properties and whatever, whatever the item supports, basically in terms of being able to
[26:14] change material parameters and so on. And you can set all those up. And you want to create a few
[26:20] instances so that you've got a few different looking people in your crowd. All right, so that's
[26:27] step two done. Step three is set up mass. And this is really quick. So we're almost finished.
[26:34] What you need to do is get the instances that you just created. So select all those. And then
[26:39] you want to drag them onto the character instances array in the mass config, which you can see
[26:46] just on the bottom right down there. I just wanted to show that because not everyone knows that you
[26:52] select multiple assets and drag them onto a property. It's going to save a lot of time if you have
[26:56] a large number of instances. And then the last step is to create the mass spawner. So this is just
[27:03] a standard actor. Just place this in your level. Make sure there's nav mesh. So just place a nav mesh
[27:09] bounds volume to make sure there's nav mesh in the level. And then there's a few properties to set up
[27:13] on the mass spawner. So we've got spawn count. There's the mass config, which is the thing we just added
[27:19] the instances to. There's EQS asset, which comes in and start a kit. And then you want also want to
[27:26] make sure that auto spawn on begin play is checked down at the bottom there. Assume you want them to
[27:33] spawn on level start. So all of that stuff I just did. And there we go. That's it. Cool. All right.
[27:44] So let's see how you can go a bit beyond what we've done.
[27:51] So the next thing to know is in a real project you might have different kinds of character in your
[27:57] crowd. So maybe you want to have different mass configs that have different behaviors.
[28:04] And maybe characters that look completely different to each other that just have different
[28:09] configs basically. You can do this and it will still be visualized as a single crowd with one set
[28:16] of actors. All you have to do is make sure that the log perms struct on the mass configs matches.
[28:23] So I've got a little video to demonstrate that. So this is from two different mass configs.
[28:27] And then I'm going to switch to debug view. And you can see it's just one set of the high quality actors
[28:32] there. So that's quite convenient. Next thing is you don't have to go and create all those
[28:40] instances by hand. You can create them procedurally if you want to. There's a property on the mass
[28:44] config called appearance provider class. And you can plug in a C++ or blueprint class here.
[28:52] There are blueprint nodes that allow you to generate an instance from scratch and select items,
[28:59] set material parameters, et cetera. And a function on the appearance provider is called every
[29:06] time an entity spawns. So you can give it a unique instance for every single entity in the crowd if
[29:12] you want. And all procedurally generated. So something to be aware of with collections is that
[29:23] it becomes quite a large single asset if you've got a large amount of content in your
[29:28] collection. So remember I said all of the generated assets, so all of the fitted clothing
[29:34] meshes, et cetera, they get stored back into the collection. And that can get quite big.
[29:39] In our sample, the crowd collection is about 1.2 gigabytes. And there's no granular loading there.
[29:45] So the whole thing gets loaded at once. And that's just something that we'd like to improve in
[29:51] future. It's just because this system is still in experimental. So what I would recommend,
[29:58] if you have different kinds of character, maybe they have completely different faces and different
[30:05] clothing anyway, like I've got this example here, you know, in a medieval setting, maybe you'd have
[30:09] knights, merchants and peasants. If they don't share anything, you might as well just have them in
[30:13] different collections. The instances, as long as those collections still all use the same pipeline,
[30:21] the instances will be interchangeable. So it's a bit like when you're using material instances,
[30:25] it doesn't really matter what the base material is. You can still plug them into any material slot.
[30:31] That's the same kind of idea.
[30:38] Next thing is, all those generated assets, you can actually unpack them. And so you can inspect
[30:43] them in the content browser. This is really useful for debugging. If there's one particular mesh that
[30:49] hasn't come out right, you can just unpack it and go and look at it. Also helps with profiling. If
[30:54] you want to see, or where is that 1.2 gigabytes being spent, you can go and look at the sizes of
[31:00] the individual assets and kind of, yeah, just inspect that. The collection still works in this unpacked
[31:07] state so that the references to those unpacked assets are maintained, so you can still run the game.
[31:16] You can rename those assets if it helps you to find a specific one, for example.
[31:19] But worth noting that the next time you rebuild the collection, it's going to discard all of those
[31:27] references and regenerate the assets back inside the collection. So, yeah, you can sort of play around
[31:35] in this state, but the next time you rebuild, it's going to be back how it was.
[31:42] All right. So a problem that we had is we want to be able to have different colors on different
[31:49] crowd characters while they're using the same mesh. But with the Instant Skin Mesh component,
[31:54] you still just have one set of material slots. So you have to use the same material instance
[32:00] across all of the instances of that mesh. Now, what we can do is we use Per instance custom data.
[32:06] You might have come across this before because it's on the Instant Static Mesh component as well.
[32:11] And so we use a setup like this in the material where you've got the Per instance custom data node
[32:18] that reads from floats that are specific to an instance on the Instant Skin Mesh component.
[32:27] And then the actor version of that material will just use a regular material parameter,
[32:31] and then we have a switch between them. And there is a bit of setup in the item pipeline,
[32:36] so in the wardrobe item where you can make the association between that parameter. So primary color
[32:43] in this case and those indices in the Per instance custom data. So that when you're
[32:50] in the Metahuman instance editor and you're setting the color of your character,
[32:55] you only have to set that once. And then the pipeline takes care of rooting that color to the
[33:00] right place, whether it's on the actor or the instance mesh. There is a debug display that helps
[33:10] you to track the efficiency of this. So if you've got custom clothing that's using different
[33:18] material instances across your crowd, you might find you're using way more Instant Skin Mesh than you
[33:26] expected to. And you can use this to find exactly which assets are causing that and monitor
[33:34] your instant sing efficiency. Next, I talked before about how to change the animations that we use.
[33:43] So the animation selection in our crowd is super basic, basically just the logic that you see here,
[33:48] it's almost literally that code, where we're just choosing the anim based on the speed
[33:52] that the character is moving. You can make your own, you do have to put some please plus plus in
[33:58] your project, but you don't have to change the engine, you can just make a new class in your project.
[34:04] So the first step for that is to add your animations into the anim config. If you remember before,
[34:10] we added this anim config asset into the collection. You can just go back and edit that.
[34:16] We've got idler walk, you can add run, sit, whatever your characters need to do.
[34:22] And then you need to make your own animation selection processor for mass. So this, any setting here,
[34:30] disables R1 so that your one won't be fighting with it, then you just take our code from the
[34:38] the class that's written on the slide here. It's only about 70 lines, so it's a really simple class,
[34:44] put it in a new class in your project, and then implement the anim selection logic that you want.
[34:52] Then for the actor, the anim blueprint actually has full control over which anim's are selected.
[34:58] The only limitation is that you have to be able to synchronize with the instance mesh.
[35:07] When the instance mesh becomes an actor, or when the character swaps from an instance mesh to an actor,
[35:13] the anim blueprint will get a function call to say, here's what animation the instance was playing
[35:21] and the exact position so that the anim blueprint can match that pose. And then it's basically the same
[35:25] in the opposite direction. The animation blueprint has to be able to provide the animation that's
[35:32] playing and the position within that animation so that the instance can pick up where the
[35:36] anim blueprint leaves off, but apart from that, while the anim blueprint is active, it can decide
[35:45] how to choose what anim is playing. So for interactivity, I just want to come clean a little
[35:56] bit. What I showed in the video before when I was interacting with that character,
[36:01] we didn't do it the right way. We just put some animation blueprint, that's not like,
[36:06] active blueprint logic in there that makes that work. You would probably want to do this using
[36:13] state tree or some other kind of mass control to do it properly to make sure that that interactivity
[36:20] persists correctly across the different, you know, when the character is instance as well.
[36:29] So you probably would need to write C++ if you need significant interactivity.
[36:34] If you just want a passive crowd that walks around like ours, then what you have out of the box
[36:41] should be good enough. There are a couple of known issues. I might have mentioned metheumen crowds
[36:49] is experimental in 5.8 as is the collection system. We did find that when an instance character switches
[36:57] over to being an actor, the motion vectors that are rendered not quite right. And so if you have
[37:03] motion blur enabled, you get a little pop of motion blur, which is unfortunate. We've disabled motion
[37:08] blur on our crowd scenes. If you need to ship with motion blur, you may have to do a bit of investigation
[37:14] to figure out what's going on there. The other thing is the mass processing queue. So this is
[37:21] a new way of scheduling mass processes that was enabled quite late in the 5.8 release cycle.
[37:28] And so we found it cause some issues with the crowd processes. So we've had to turn it off.
[37:35] So just something to be aware of.
[37:38] Now I'm going to take a step back from crowds and talk about collections in general.
[37:47] So collections are a general system. Crowds is based on it, but crowds is just one possible pipeline.
[37:55] You can make your own pipelines. I've got an example here on the right of a pirate. Maybe you want to
[38:02] have a pipeline that supports, you know, has slots for hats, eyepatches, earrings, things like that,
[38:09] priority stuff. You can have it apply your own optimisation. So you can, you know, take
[38:15] metheumen character meshes as input, like we do with the crowds, and then, you know, choose your
[38:20] own lords, you adjust the skinning, whatever you want to do, all the optimisations that you
[38:26] perhaps automate on assembled characters. Now you can do it in a non-destructive way.
[38:33] And anytime your characters change, you can just rebuild the collection and have those optimisations
[38:40] or customisations automatically reapplied. And also wanted to call out that items in the collection
[38:47] can be any asset type. So you could have audio for voices. So perhaps you have a slot that
[38:54] is, you know, a set of voice phrases or something like that. And then for each instance, you can
[39:00] choose what kind of voice that particular character has, or the way they walk, or, you know, tattoos,
[39:07] magic effects, other things like that you could do. I think a way that's useful to think about
[39:14] instances is as an API for the character's appearance. You can take the visual logic that you have,
[39:21] and separate that out from your game code into your collection pipeline. So for example,
[39:30] I mentioned earlier, we have skeletal meshes for the hair cards. But for short hair styles,
[39:38] the hair is rendered as part of the skin. But when you're setting up the instance, you don't
[39:45] need to know about that. Just the pipeline takes care of that distinction. So you could imagine
[39:52] if you have assets that interact with each other, like maybe you have a knight of a clothing that
[39:58] has a hood. And when that clothing is worn, then the hair needs to be displayed in a different way.
[40:06] That's something that your pipeline could take care of. And then your actor logic doesn't need to
[40:11] know about it. So something else I wanted to mention is the instance asset. You don't need
[40:20] mass to use that. That's just something we were using for crowds. You can also have a normal actor
[40:25] blueprint that takes a metahuman instance. And you can see I've got some logic over here.
[40:33] All you do is you call get get assembly output on the instance. And then you get this struct.
[40:40] And I've got face mesh and body mesh on there, for example, and materials. That's completely
[40:46] defined. That's struct by the pipeline. So if you make your own pipeline, you can have your own data
[40:53] and use that to initialize your actor's appearance. All right, I've got a little video just to show
[41:01] this in action. So I'm editing an instance here. And then I go back to the content browser. I drag
[41:07] the instance into the level viewport. And that spawns the actor blueprint that's defined by the
[41:13] pipeline. And then I can even animate it in sequencer. I can go back to the instance editor and
[41:23] change colors, change items while it's animating. That connection between the actor and the instance
[41:29] is maintained. So it's quite a versatile system. It's quite a lot you could do with that.
[41:34] I wanted to mention mutable because I think if anyone in the audience has used mutable or looked
[41:42] into it before, you might be seeing some similarities. And it does solve a similar problem to what we've
[41:49] got with collections. What I would say is if you're already using mutable and it works for you,
[41:57] then there's no problem continuing with that. It is much more mature than collections. It's much
[42:02] more battle tested. It's used in Fortnite. So it's stable and it has the granular loading
[42:09] that collections doesn't have yet. Whereas on the other hand, with collections, you can do more
[42:15] powerful transformations. The pipelines are defined in C++. So you can call any engine function
[42:22] from a pipeline and you have a lot more flexibility. But they're experimental, you might run into issues.
[42:29] So that's what I'd say about that. It really just depends on your project and your specific needs.
[42:37] Okay, so let's recap. I talked about how metahuman crowd is rendered and what the different
[42:46] features are and the different assets that are involved in that. Should have to set up your own
[42:53] crowd with your own assets and how to take it beyond what we've done in the sample. And we look
[42:58] at collections and what else you can do with them. And with that, I'd like to thank you all for
[43:03] coming and I think we have a bit of time for Q&A.



---

## Captured Frames

- [1:49] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_000.jpg
- [3:54] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_001.jpg
- [7:51] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_002.jpg
- [11:14] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_003.jpg
- [17:21] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_004.jpg
- [26:46] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_005.jpg
- [32:18] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_006.jpg
- [41:07] tutorials/frames/how-to-build-scalable-metahuman-crowds-in-unreal-engine-unreal-fest-chicago-2026/frame_007.jpg

---

## Structured Notes

### Core Technique
Building 1,000-MetaHuman crowds at 60 fps using **Mass** (entities + StateTree behavior), a two-tier visualization (nearby high-quality actors swapping pose-matched with **Instanced Skinned Meshes/ISKM**), and the new **MetaHuman Collection / Instance / Pipeline** asset system.

### Summary
Henry Falconer (principal engine programmer, MetaHuman team; crowds + collections lead) presents the Fab **MetaHuman Crowd Sample** (1,000 diverse MetaHumans: 16 heads, 8 bodies, per-character clothing colors). Performance (approx.): current-gen consoles 60 fps / 1000 MH / 9 ms game / 7 ms render / 16 ms GPU / 70% res / +2.3 GB; recent mobile 30 fps / 500 MH / 720p / +0.4 GB; last-gen consoles and current handheld 60 fps / 200 MH; last-gen handheld 30 fps. ISKMs are fully GPU-skinned meshes (not vertex-animation textures), Nanite-compatible (10,000 instances at 80-90 fps demoed; Nanite stabilizes frame rate). Animation via **Anim Sequence Transform Provider** (richer than AnimBank: layered blending, translation retargeting, per-instance offsets — 100 unique walk offsets). Grooms have no instanced component: card/helmet grooms are converted to skeletal meshes skinned to each face; short styles use baked (texture) grooms; no groom physics. Characters split into instanceable meshes (top/bottom garment, shoes; body geometry merged into clothing since clothing is per-body unique); crowd actors keep Rig Logic (LOD2 top), instance meshes use LOD4 with rig-logic-baked joint facial animation, translucent parts (eye moisture/saliva) removed, 8 to 4 bone influences, teeth optionally disabled.

### Key Steps
1. **Get the sample**: Fab "MetaHuman Crowd Sample" — migrate its **Starter Kit** folder (pre-made Mass config with ~15 traits, anim config, EQS asset).
2. **Create a MetaHuman Collection** (right-click in content browser) — set Pipeline = MetaHuman Crowd Pipeline — assign the Starter Kit anim config.
3. Add clothing/hair: same asset types as MetaHuman Creator (Chaos outfits incl. resizable, skeletal-mesh clothing, groom bindings). Existing wardrobe items carry over hidden-surface maps + material params (hidden-surface maps determine which body parts merge into clothing — keep them accurate). External wardrobe items (dragged asset, read-only props, shared across collections) vs internal (dragged raw asset, editable in-collection). Item pipelines with "Crowd" in the name format sources for the collection pipeline — the slot data format is an API boundary, so custom pipelines interoperate both ways.
4. Heads/bodies: MetaHuman Character assets. Duplicate a character and edit only the head to share one body across heads (fewer clothing meshes). **Assemble in MetaHuman Creator with the joints-only rig** (full rig's blend shapes only serve LOD0, unused by crowds) and **strip all hair/clothing first** (they contaminate skin textures / body geometry). For bodies, export a **Full Body Skeletal Mesh** (Creator: Export - Geometry Export) — required for clothing resize.
5. Drag heads into the Head zone, bodies into Body; set their internal wardrobe items to the character item pipeline and point face/body mesh at the assembled assets.
6. **Build the collection** (Apply): generates fitted clothing per body, groom skeletal meshes skinned to faces; DDC-cached (first build minutes, rebuilds much faster). Source-asset changes need a manual Rebuild. Preview by double-click-equipping items.
7. **Create MetaHuman Instances** (right-click collection): pick built items + set color/material parameters — "material instances" of the collection's possibility space; can also be generated at runtime.
8. **Mass setup**: multi-select instances and drag onto the Mass config's Character Instances array; place a Mass Spawner actor + NavMesh Bounds Volume; set spawn count, Mass config, EQS asset, Auto Spawn On Begin Play.
9. **Advanced**: multiple Mass configs render as one crowd if their LOD params struct matches; procedural appearances via the config's Appearance Provider class (BP/C++ per-spawn instance generation); collections are one big asset (sample: 1.2 GB, no granular loading yet) — split disjoint character types into separate collections (instances stay interchangeable if pipelines match); unpack generated assets for debugging/profiling (rebuild discards); per-instance colors via **Per Instance Custom Data** (ISKM) + material parameter (actor) with a switch, mapped in the wardrobe item — one instance parameter drives both, plus an instancing-efficiency debug display; custom anim selection = add anims to the anim config + replace the ~70-line Mass anim-selection processor (project C++, no engine changes); actor AnimBP has full control but must sync pose/position bidirectionally on actor-instance swaps; real interactivity should use StateTree/Mass (the demo's ABP hack does not persist across instancing).
10. **Known issues (5.8)**: motion-vector pop on instance-to-actor swap (sample ships with motion blur off); the new Mass processing queue caused problems — disabled.
11. **Collections beyond crowds**: custom pipelines (own slots: hats, eyepatches...; own optimizations, non-destructively reapplied on rebuild); items can be any asset type (voices, walk styles, tattoos); instances work without Mass — an actor BP calls Get Assembly Output for a pipeline-defined struct (face/body meshes, materials); drag an instance into the level, animate in Sequencer, live-edit colors/items. vs **Mutable**: Mutable is mature/battle-tested (Fortnite) with granular loading; collections allow more powerful C++ pipeline transformations but are experimental.

### UE Systems / Blueprints / Settings
- Mass + StateTree (wander), Mass Spawner (spawn count, config, EQS, auto-spawn), NavMesh Bounds
- Instanced Skinned Mesh (ISKM) — GPU skinning, Nanite-capable; Anim Sequence Transform Provider (layered blending, retargeting, per-instance offsets)
- MetaHuman Collection / Crowd Pipeline / Wardrobe Items (item pipelines, hidden-surface maps) / MetaHuman Instance (runtime-generatable)
- MetaHuman Creator: joints-only rig, Full Body Skeletal Mesh export
- Per Instance Custom Data material node + actor parameter switch
- Optimizations: LOD2 actors / LOD4 instances, rig-logic-to-joint baking, 4 bone influences, translucent-section removal
- Perf table (approx): consoles 60fps@1000MH (9/7/16 ms, 70%, +2.3 GB), mobile 30fps@500MH (720p, +0.4 GB), last-gen/handheld 60fps@200MH, Switch1 30fps

### Difficulty
Advanced

### UE Version
UE 5.8 (MetaHuman Crowds + Collections experimental)

### Tags
#metahuman #animation #performance #blueprint #cpp #worldbuilding #advanced

---

## Related Entries
- [New Unreal Engine 5.8 Metahuman Crowd Plugin](new-unreal-engine-58-metahuman-crowd-plugin.md) — short overview of the same plugin; this talk is the full engineering deep dive
- [UE 5.8 - Any Mesh To MetaHuman - Tutorial](ue-58---any-mesh-to-metahuman---tutorial.md) — shares #metahuman; custom characters that could feed a collection
- Unreal Engine 5.8 Release Notes (tutorials/unreal-engine-58-release-notes.md) — 5.8 context (MetaHuman Crowd listed as experimental)
