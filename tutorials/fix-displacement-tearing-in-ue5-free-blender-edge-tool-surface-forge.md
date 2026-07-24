---
title: Fix Displacement Tearing in UE5 — Free Blender Edge Tool (Surface Forge)
source: YouTube
url: https://www.youtube.com/watch?v=jyQCaCJ_eY8
author: Arghanion's Puzzlebox
ingested: 2026-07-23
ue_version: "UE5"
tags: [nanite, displacement, materials, vertex-color, blender, fbx, mesh-import, chamfer, tri-planar, surface-forge, world-forge, modeling-mode]
extraction_status: complete
frames_dir: tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Fix Displacement Tearing in UE5 — Free Blender Edge Tool (Surface Forge)

**Source:** [YouTube](https://www.youtube.com/watch?v=jyQCaCJ_eY8)
**Author:** Arghanion's Puzzlebox
**Duration:** 26m30s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello, everybody, and welcome to Organian's Puzzlebox.
[0:05] In today's video, I want to explore something that's going to be very beneficial to you,
[0:09] whether you use the Surface Forge or not.
[0:12] But if you use Nanite Displacement in Unreal Engine 5, then this video is for you.
[0:17] So if you bring in a shape in Unreal Engine, maybe like a cube or something like that,
[0:22] and you add a surface onto it, and if you have displacement happening on these edges,
[0:29] like here, these very sharp edges, then you will get some serious issues.
[0:33] Now, right now, by default, this particular mesh, because of my Surface Forge setup, isn't
[0:40] displaying any displacement on any of its sizes, because I am using the vertex information
[0:46] in the Alpha channel to basically hide this displacement.
[0:51] So if I go over into my modeling tools, and if I go over into attributes, go to Paint
[0:56] Vertex Colors.
[0:57] I'm going to select RGB and A, and I'm going to change my erase color to Alpha 0 and a
[1:04] black color, press OK, and then I'm going to say Erase All.
[1:08] Then I'm going to press Accept, and now we can see the problem.


### Why edges tear and how [1:10]
**Transcript (timestamped):**
[1:12] So what's going to happen with any particular surface that you bring in in Unreal Engine,
[1:17] or if you generate it in Unreal Engine?
[1:19] If these faces are very sharp and the normals don't actually blend in between the faces,
[1:26] then you will get these issues.
[1:28] So I'm sure there's plenty of people out there who have tried to use Nanodispasement in Unreal
[1:32] Engine and they have had these issues.
[1:34] You get these issues in other software, such as Blender or Substance Painter, or other
[1:41] software where you can use displacement in general.
[1:44] So this video today will resolve this issue by providing you with a tool and also the
[1:48] information required to understand where the problem is coming from and how to resolve it.
[1:53] Now I would like to reiterate that the tool is available for everybody for free.


### Get the Addon for FREE [1:54]
**Transcript (timestamped):**
[1:59] You don't need to have the Surface Forge in order to use this tool.
[2:02] It can just be using your Blender project as a set for free, and then you can use that
[2:07] to translate meshes over into Unreal Engine with an easy to follow workflow that allows
[2:13] you to have nice displacement.
[2:16] If you have any questions about how Vertex Color can help you with displacement, please
[2:21] feel free to reach out.
[2:22] Otherwise, the chamfering option of the tool will work regardless if you have a shader
[2:28] set up in Unreal Engine to take advantage of it or not.
[2:32] And I was going to say, if you want to support the Arganian's puzzle box, feel free to take
[2:36] a look at my Surface Forge project or World Forge project because these tools will greatly
[2:43] help you create massive and beautiful worlds in Unreal Engine 5.
[2:47] Now I'm going to fly over to this mesh over here and you can see that the edges here are
[2:53] not causing this issue.
[2:54] This is not geometry.
[2:55] This is just displacement that is being done right now.
[2:58] I am using a world-aligned texture, meaning that right now wherever I move this mesh,
[3:04] these textures will always stay in place and they have a natural sort of curve to them.
[3:11] But more importantly, I needed to modify this mesh so that it has a nice transition from
[3:16] one face to another.
[3:19] And this is what my tool in Blender is going to do for you, but also you're going to understand
[3:24] how you can do it yourself regardless if you're using the tool or not.
[3:28] And that's going to be a setup of chamfering or beveling or whatever.
[3:33] I think it's just the chamfer is the correct sort of term for this.
[3:38] But where we also can also apply another technique is going to be vertex painting on any of the
[3:44] channels which is going to hide displacement in those areas.
[3:48] And that's important as well, especially for more complex meshes.


### Addon Explanation - with GRAPHICS [3:51]
**Transcript (timestamped):**
[3:51] So I put together a little bit of a display here.
[3:54] So I want to show you what the Edge Mask Painter is going to do for you.
[3:59] Now when we have a mesh like a cube or something like that, I generally recommend basic shapes
[4:04] for displacement.
[4:05] I don't think you should use displacement on complex shapes such as body armor or things
[4:11] like that.
[4:12] Even unless you have a very specific big plate, maybe something like a large area.
[4:19] But generally if you're doing it for micro detail on surfaces that are very complex
[4:24] with overlapping geometry, and especially overlapping UVs or messy UVs, then you're not going to
[4:31] have a very good time.
[4:32] So you generally want to use basic shapes such as cubes, cylinders, pyramids, things
[4:38] like that, or just large rectangular shapes with small modifications.
[4:43] Just you'll see what I mean in a bit.
[4:46] Now what we're trying to do here with this tool, we're trying to detect every sharp edge
[4:49] by an angle calculation, and then paint a vertex mask to switch displacement off in
[4:54] those areas, or chamfer so displacement flows around the corner.
[4:58] Now obviously chamfering, so displacement flows around the corner, is the preferred
[5:03] method here.
[5:04] But that also implies that you have clean UVs.
[5:06] So this face to this face has a nice transition of UVs, or you're using tri-planar for the
[5:12] texture so that it wraps around the object from X, Y, and Z projection points.
[5:18] Now you have to build for clean topology.
[5:21] So as boxes, panels, trims, simple geometric shapes, these are the ones that are going
[5:29] to work well.
[5:30] Now if you go over into what the tool can do for us, we have a find every sharp edge.
[5:36] So we are using an angle threshold.
[5:38] So for example, a cube has 90 degree sort of angle.
[5:43] So if we go above 90 degrees to 95, for example, there is no edge on this cube that's going
[5:48] to be larger than 90 degrees.
[5:51] Okay, but there's a plenty, obviously all the other edges are under 90 degrees.
[5:56] So it's going to detect all of them.
[5:58] So that's going to be very useful.
[5:59] Again, if you have a more complex shape here, something like multiple faces, then based
[6:04] on this angle, we will be able to detect those edges.
[6:07] Now if we go over into paint mode, so here is an interesting thing.
[6:11] By default, a cube is going to have only eight vertices on this cube.
[6:17] So the problem with vertex painting is going to be that it needs all these points in order
[6:21] to add its vertex information.
[6:24] So right now I'm trying to paint all the edges, but as you can see, it's just one full block
[6:29] of white color, meaning that it's fully painted in white.
[6:33] As I increase my subdivisions, you'll notice that I'm adding more vertices, which allows
[6:38] for my vertex color information on the edges to have a higher resolution.
[6:44] So if I, for example, increase the vertices on this cube to 386, I can get some pretty
[6:49] clear lines on the edges here, where I can have the vertex paint painted on and thus
[6:54] displacement to be disabled in those areas.
[6:57] Now I can also have a fall off sort of scenario here where I could do that.
[7:03] So I have a fall off between the edge and the furthest point from the edge based on how
[7:08] the vertex will be applied.
[7:11] Now one thing here, I'm going to move on to the chamfering point.
[7:16] This is going to be the issue that you're going to encounter.
[7:19] So let's say we have a sharp 9 degree displacement tear over here.
[7:23] So these two edges are coming into contact with each other.
[7:29] So the displacement above this surface will just simply sort of like go through, right?
[7:36] It will literally intersect and it will look odd or it will create a tear or you'll be
[7:40] able to see inside the mesh and it just looks wrong.
[7:43] Okay, but with our chamfering effect on the right, you can see there, we're adding a sort
[7:48] of like, I mean, even one chamfer of one segment, even doing this is still going to allow the
[7:54] normals to kind of curve, which will mean your displacement will have a higher chance
[7:58] of succeeding of going around the quarter.
[8:02] But as we increase that resolution, it will have a better transition.
[8:05] So at some point, three, four segments will be enough to have the perfect displacement
[8:11] all around.
[8:13] So just to recap here, right?
[8:16] This is just vertex mask, kill it at the edge.
[8:19] So that kills displacement at the edge.
[8:22] And then you can also use chamfer to carry the displacement around.
[8:26] Okay, what I would say is that obviously we're chamfering, you're adding more geometry on
[8:32] edges while with vertex masks, you're adding more geometry across the whole mesh in general.
[8:37] But obviously you can do manual subdivisions as well if you want, just on those edges.
[8:42] So it's really up to you, but I personally would go with the chamfering if that's available.
[8:47] So let's go into Blender and see how all of this works.


### Using it in Blender [8:50]
**Transcript (timestamped):**
[8:50] So here we are in Blender with a default cube in scene.
[8:54] We're just going to go over first into edit preferences.
[8:57] And I want to go to add ons, click on this arrow and install from disk.
[9:01] This is assuming you're using Blender 5.0, but this add on will work from Blender 3.2
[9:08] and above.
[9:09] So if you click on install from disk and you go over to wherever you've got the add on
[9:12] downloaded, which you can get off my Patreon for free, then you can go in here and double
[9:19] click it.
[9:20] I'm not going to do it again, but obviously you can double click it and that will install
[9:23] it.
[9:24] Once you've done that, you can press N on the keyboard.
[9:28] And this will open this panel over here.
[9:30] So I've pressed a space over there.
[9:32] This will open this panel over here and you can go over into edge mask.
[9:35] This is the name of the add on.
[9:37] Okay.
[9:38] So what it's giving us is giving us some options where we can import an FBX.
[9:41] So if you press that button, you can import any FBX that you've got.
[9:45] And you can click also this button to export the selected mesh and it will add a suffix
[9:50] called the mask at the end of the name of the mesh when you export it.
[9:54] So that's what the FBX round trip is.
[9:57] Now we here have a detection.
[9:59] It says it is detected a mesh with eight vertices and six faces.
[10:03] You can click on the face type breakdown to give you here over sort of like a bit of a
[10:08] display of whether you have any N guns on it or anything like that.
[10:12] Right.
[10:13] So you have to, you'll just see a breakdown of the selected mesh in terms of details of
[10:18] its composition.
[10:20] Then we have a edge threshold detection.
[10:23] So we're going to keep that as default of five.
[10:25] And if we have in here preview edges, if we click this button, it will create a preview
[10:29] of the edges detected.
[10:31] Okay.
[10:32] Now, obviously, if you change this to 95, for example, and then you refresh it, then
[10:37] you can see that there's no edge detected anymore, because obviously we're above 90.
[10:43] If we put this at 90 and then we do a refresh.
[10:47] Oh, sorry.
[10:48] Let me just go a little bit like that.
[10:51] See, you just have to be like 89 or something like that.
[10:54] Right.
[10:55] Just do a refresh and then you can see in there that it has detected it.
[10:59] Obviously you can change the color of this if you want.
[11:02] And if you've moved the mesh around and the edge detection stays in place, just click
[11:06] refresh and then that will move it to where that was.
[11:09] Okay.
[11:10] Now we're going to be able to turn it off as well if you want.
[11:13] Now, the first, the next thing you will get is got Trist to Quads.
[11:17] So what this means is that if you have triangles in your mesh, so for example, if I edit this,
[11:24] okay, and then I, you know, like, for example, I could add in here or, I don't know, you
[11:30] know, from this point to this point, I'm just going to use the knife tool here just to create
[11:36] it.
[11:37] Okay.
[11:38] So now I've got two triangles.
[11:39] Okay.
[11:40] You can see in here that if I do a face type breakdown, it says it's got two triangles.
[11:44] Okay.
[11:45] So if I say Trist to Quads, then you can see it's removed that triangle, those two triangles
[11:50] over there so that it cleans the mesh up a bit for us.
[11:53] Obviously, when you import back into Unreal Engine, it will automatically triangulate the
[11:57] mesh anyway.
[11:58] Next, the next thing is Vertex Mask mode.
[12:02] So here we can actually paint the edge.
[12:04] So if we preview the edges again, we'll be able to see them and I can then paint the
[12:09] edge mask.
[12:10] Now if I want to preview this like that, you'll notice that it kind of looks the same.
[12:16] There is actually Vertex Color information across the whole mesh right now in white,
[12:20] but we can't really see the black because there's just not enough vertices.
[12:25] So with this, you want to go into Edit Mode and I'm going to select it and subdivide it
[12:30] a few times like that.
[12:32] Okay.
[12:33] And now if I go in here and paint edge mask and preview again, this is how that looks
[12:39] like.
[12:41] This is why Vertex Information is very important for us to have.
[12:46] Now you can also increase the rings here.
[12:50] So for example, we could go to like that, paint it, preview it, and that's where that
[12:55] is the falloff rings.
[12:57] And we also have the curve.
[12:59] So we can increase this curve and then paint and then preview.
[13:05] But if I decrease the number of rings, paint, preview, this is kind of what we want.
[13:11] Maybe a bit more falloff, maybe something like that.
[13:16] So now the displacement will be masked all around these corners in Unreal Engine 5 if
[13:22] your material shader allows for that workflow to work.
[13:26] Now if we want, we can go into Chamfer Mode.
[13:30] So in Chamfer Mode, we can now check the topology.
[13:34] So it says here this mesh is good.
[13:36] It can, you know, mesh looks clean for chamfering.
[13:40] And then we have in here a width and number of segments.
[13:44] So then if we do chamfer sharp edges, let me just remove this preview.
[13:49] You can see that the edges have been chamfered.
[13:52] But let me try now and increase the width and also number of segments and chamfer edges.
[13:57] And you can see it's already chamfered and it's also applied a smooth to the mesh.
[14:04] So that's how this cube looks like now.
[14:08] And what I'm going to do, I'm going to export this cube and bring it over into my Unreal
[14:12] Engine project.
[14:13] I'm just going to go over here and I'm just going to keep it as name as export masked.
[14:19] So export it.
[14:20] Now I'm going to go in Unreal Engine and play in there.


### Importing in Unreal Engine 5 [14:22]
**Transcript (timestamped):**
[14:22] When Unreal Engine, I'm just going to bring in my export masks cube.
[14:27] And over here, it's already going to have a Nanite.
[14:30] So if you type in Nanite, this will be already built.
[14:33] But then I also want to type in vertex.
[14:35] So it says here you have a few options have replace ignore or override.
[14:39] So if you go over it says specify how vertex color should be imported.
[14:43] And if it's replace, then import the mesh using the vertex color from the translated
[14:47] source.
[14:48] It will come with the vertex information from Blender.
[14:51] If we choose ignore, it will re-import, keep the existing mesh vertex colors.
[14:57] Actually, sorry, I think this is the ignore the vertex color from the translated source.
[15:02] In case of a re-import, keep the existing mesh versus the color.
[15:04] So this will actually ignore what vertex information comes with the mesh.
[15:08] And then override will just be override over this color with the specify color.
[15:12] So if you do this, you can just select the color to be overwritten with.
[15:16] We're just going to do a replace and bring that in.
[15:20] I'm going to delete this material as I don't need it, but I am going to drop this mesh
[15:25] over here into the world.
[15:28] I'm going to put it up here.
[15:30] I am going to take the material from this cube and I'm going to put it onto this.
[15:36] Okay, so now let's take a look what's going on here.
[15:41] Have we got any displacement?
[15:43] Have we got anything working as intended?
[15:47] So if we go over here into the center of the mesh, you can see some displacement.
[15:53] What I'm going to do actually, I'm going to open this material instance and I'm going
[15:59] to actually go over into my bricks over here, these bricks.
[16:04] And I'm going to look at tiling maybe a 0.5.
[16:09] And as you can, well, 0.5 and I'm also going to change its weight parameters.
[16:16] I'm trying to kind of get it to be a bit deeper maybe.
[16:22] Yeah, actually, let's leave it at one and then I'm going to do this as a one.
[16:28] Okay, so you can see there that the displacement is working across in that center, okay?
[16:35] But it's not working on the edges.
[16:37] This is why the Surface Forge at the bottom has an option where it says, and it use displacement
[16:43] mask, which is turned on and it's currently working on the alpha channel.
[16:48] If we actually go into modeling mode for this mesh and we click on attributes and paint
[16:54] vertex colors, you'll notice these are the vertex colors that we brought over from a
[16:59] blender, okay?
[17:00] Now, here's the thing, this mesh is also chamfered and it's also vertex painted.
[17:06] So if I go in here and I delete this vertex information in this area that came from a
[17:11] blender and now I click accept, now I will actually have displacement on these edges
[17:19] here.
[17:20] They're just not very, how should I say, very well defined to be seen.
[17:26] So I'm going to tweak around with this material a little bit just so we can maybe be able
[17:32] to see a bit better in here what we're doing.
[17:35] You can kind of see the displacement there, by the way.
[17:38] So it's just going to drag this in a bit more like that, okay?
[17:44] So you can see where the displacement is being cut off right at this point right here.
[17:50] And you can see where the displacement then starts where the vertex color information,
[17:54] the alpha information is no longer present.
[17:57] But whenever we hit it again, we then have this fall off where it goes to zero, okay?
[18:02] So this particular issue on these edges here, these tears wouldn't be possible.
[18:07] But here's the thing, if I select this mesh over here and I go to paint vertex color and
[18:13] I just want to paint alpha in white, okay?
[18:19] And then I'll make this a bit smaller.
[18:20] See, I've just painted this entire bit and the reason why it's doing all of this is because
[18:25] I only have one vertex here.
[18:27] I don't have a lot.
[18:29] So I'm going to click accept.
[18:31] And now you'll notice that there's no tear here anymore because we've effectively hidden
[18:35] that.
[18:36] But in the material instance, which both of these meshes share, if I go in here and I
[18:40] use displacement mask, I disable that, okay?
[18:45] Now the system will automatically ignore all the vertex color information and displacement
[18:51] will now happen all across the board, okay?
[18:55] So that's the refinement right there.
[18:57] And like I've said to you, this particular tool and this particular workflow will apply
[19:01] to anything.
[19:02] The Surface 4 obviously can leverage the alpha channel or any of the vertex color information
[19:07] channels to reduce or remove displacement in those areas, wherever they are painted,
[19:13] okay?
[19:14] It doesn't have to be, as I said, just the alpha channel.
[19:16] Like for example, I could go in here and just say I want the red channel to also be able
[19:23] to remove it.
[19:24] So if I go into paint vertex color.
[19:26] Right now, if I select the red channel, you'll notice that it's painted all across.
[19:31] So what I'm going to do is I'm going to erase that, going to press accept.
[19:36] And now you can see we have, as I said, we've got a displacement everywhere, okay?
[19:42] Because I'm no longer, the red channel is no longer, I mean, the red channel is also
[19:46] used, okay?
[19:48] But the alpha, see the alpha is used here and the red channel, but the red channel takes
[19:54] priority because it is the first channel in the chain.
[19:57] So if I disable the alpha channel here in the mask and I press accept, now you'll notice
[20:03] that again, we have displacement everywhere.
[20:05] But if I go to paint vertex colors and I switch over to red channel and I start adding some
[20:11] red information around here, like this, and I'm going to press accept.
[20:16] And you'll notice that I no longer have any displacement in the areas that I've painted,
[20:21] but I do have displacement in the areas that it's not painted.
[20:24] So we could obviously subdivide this particular mesh even further.
[20:28] Now you can see in here that we have a sharp edge transition.
[20:31] And that's because this particular, you know, like this texture here that is being used
[20:36] here may possibly not have, you know, world aligned textures enabled or it's not enabled
[20:44] in such a way that it allows for that transition to be invisible.
[20:49] So for example, we could do something like this here, see that?
[20:52] So now the transition is disabled.
[20:54] Obviously, the surface forge is a very powerful tool that allows you to customize these things
[20:58] and reduce or remove them.
[21:01] So that's not an issue for it.
[21:03] Now very quickly, I want to reiterate what happens if you have a very complex mesh that
[21:07] you're trying to bring in a real engineer and use nanodisplacement and also use this
[21:10] tool on it.
[21:12] If for example, we add a subdivision surface over here and we're going to maybe, you know,
[21:20] increase it a little bit, something like that.
[21:22] Okay.
[21:23] And then let's say we add another modifier, which is a displacement modifier, and we're
[21:28] going to use a texture.
[21:31] And this particular texture, I'm just going to go over into it.
[21:34] I'm going to change it over to maybe something like clouds.
[21:37] Okay.
[21:39] And I'm going to decrease the size a little bit, maybe the depth, something like that.


### using it with Complex Meshes [21:40]
**Transcript (timestamped):**
[21:45] Doesn't really matter.
[21:46] Okay.
[21:47] Now, if I want to detect the edges, so preview edges, oh, sorry, I have to first apply all
[21:54] these.
[21:55] So now you can see these are the edges that it detects based on a threshold of 89.
[22:00] So I'm going to put that to an angle threshold of five.
[22:03] So now it's thinking, well, everything is an edge.
[22:07] So if you're a hammer, everything is a nail to you.
[22:11] So I'm going to increase this to 25, maybe 28, 30, 40, something like that.
[22:17] So it's detecting all of these edges that are going to be problematic for Nanite displacement.
[22:24] These will create tears.
[22:26] But then you're saying, okay, well, if we vertex paint all of this stuff, right, we
[22:31] will resolve the issue.
[22:33] So paint, edge mask, preview.
[22:35] See that?
[22:36] Not enough geometry.
[22:37] So we would need to add more vertices in order to do this.
[22:42] So your next option will be to just chamfer.
[22:45] So I'm going to decrease this width to make them quite small and to segments and then
[22:50] chamfer those edges.
[22:52] And yes, chamfering has worked, but look at what it's created.
[22:57] Okay.
[22:58] This is not exactly an ideal situation.
[23:02] So if we disable the preview, this is not going to look very good.
[23:06] Now I'm going to remove the chamfering and instead I'm going to go for three segments
[23:11] and try to create even more width and then chamfer again, and maybe I'll get a better
[23:16] result.
[23:17] Anyway, this is our complex shape.
[23:19] I'm going to export this into my edge masking folder and I'm going to call this complex
[23:27] just as a thing.
[23:29] And then I'm going to export fbx.
[23:30] I'm going to go back into Unreal Engine.
[23:33] Okay.
[23:35] And I'm going to go wherever I've got this mesh over here.
[23:39] I'm going to import.
[23:41] I'm going to have to quickly go over into my edge mask.
[23:48] And then we have this complex mesh.
[23:50] I'm going to import it and I'm going to drop it into the world.
[23:55] I will now take this particular shader and I'm going to apply it here.
[24:03] Remember in mind that right now we are not using, I think we're not using them, we're
[24:10] using a red channel mask.
[24:12] So I'm going to open the material and I'm actually going to disable the mask entirely.
[24:19] So we're not going to use the mask at all.
[24:22] So this is how the displacement sort of looks like.
[24:26] It's an ideal.
[24:28] It's not horrendously bad, but it's not ideal.
[24:32] I think if we were just displaying the bricks, so I'm going to disable two-in-one material
[24:38] blending just so we have bricks everywhere.
[24:41] This is kind of how it would look like.
[24:44] Again, not the end of the world.
[24:46] We're still getting some stretching over here.
[24:49] This is in world-aligned texture.
[24:51] This is using Triplanar right now.
[24:54] And if we were to disable Triplanar, then the effect would start to get quite bad.
[25:00] I would think because now the mesh is thrown in every possible direction.
[25:06] Again, can work if you maybe you're making like a rock or something like that.
[25:12] I don't see, I can see some tears over here.
[25:17] There's not that many.
[25:19] I'm actually quite surprised that it worked out as good as it did, but overall it's not
[25:25] ideal.
[25:26] The world-aligned textures, some of these tears even here, they're now gone because
[25:31] world-aligned textures generally fixes these kind of issues.
[25:35] You would still have to play around with this geometry and optimize it.
[25:39] But overall, a valiant effort, but I would say stick the basic, more basic shapes if
[25:44] you want a good result.
[25:45] So thank you guys for watching this video.


### Outro [25:46]
**Transcript (timestamped):**
[25:47] Hope you enjoyed a new tutorial from Arganian's puzzle box about the surface forge, but also
[25:52] displacement in general.
[25:53] I do want to expand on that add-on for Blender.
[25:57] I'm going to make it a lot better actually.
[25:59] I've got quite a few features planned for it to effectively automate the process of masking
[26:05] and chamfering and detecting edges and adding bevels and adding custom bevels and selecting
[26:09] edges based on certain properties and chamfering them with much more control.
[26:14] I hope you guys enjoyed it.
[26:15] If you would like to support the Arganian's puzzle box project, then have a look at the
[26:19] surface forge or on fab or look at patreon where I have all my projects available for
[26:25] the price of a coffee.
[26:28] So thank you guys.
[26:29] I'll see you in the next one.



---

## Captured Frames

- [1:00] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_000.jpg
- [4:50] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_001.jpg
- [7:50] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_002.jpg
- [9:59] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_003.jpg
- [13:05] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_004.jpg
- [14:40] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_005.jpg
- [17:50] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_006.jpg
- [22:20] tutorials/frames/fix-displacement-tearing-in-ue5-free-blender-edge-tool-surface-forge/frame_007.jpg

---

## Structured Notes

### Core Technique
Fixing Nanite displacement tearing on sharp edges by pre-processing meshes in Blender with the free "Edge Mask Painter" add-on: detect sharp edges by angle threshold, then either paint a vertex-color mask (imported into UE5 and read by the material to switch displacement off at edges) or chamfer the edges so displacement flows around the corner.

### Summary
Nanite displacement tears wherever two faces meet at a hard angle with unblended normals — the displaced surfaces intersect or split open, in UE5 and in any displacement pipeline (Blender, Substance). The video explains the cause and gives two fixes, packaged in a free Blender add-on (works Blender 3.2–5.0, distributed via the author's Patreon): (1) vertex-mask the edges — kills displacement locally, needs enough subdivision for vertex resolution; (2) chamfer the sharp edges (preferred) — 3–4 bevel segments let the normals curve so displacement carries around the corner, but requires clean topology/UVs or tri-planar projection. Round-trips FBX to UE5 where a material (here Surface Forge's) reads the vertex color channel as a displacement mask. Works best on simple shapes (cubes, cylinders, panels, trims); a deliberately complex displaced blob shows the limits.

### Key Steps
1. **See the problem**: in UE5's Modeling Mode → Attributes → Paint Vertex Colors, select RGB+A, set erase color to black with Alpha 0, Erase All, Accept — with the protective mask gone, displacement tears appear on every sharp edge.
2. **Why**: sharp faces whose normals don't blend make displaced geometry intersect/split at the edge. Two remedies: kill displacement at the edge via a vertex mask, or chamfer so displacement flows around the corner (preferred, but needs clean UV transitions or tri-planar texturing).
3. **Install the add-on** (Blender ≥3.2): Edit → Preferences → Add-ons → Install from Disk; open with N-panel → "Edge Mask".
4. **Detect edges**: the panel reports mesh stats (verts/faces, face-type breakdown incl. n-gons). Set the angle threshold (default 5°; e.g. 89° catches a cube's 90° edges, 95° catches nothing) and Preview Edges; Refresh after moving the mesh or changing the threshold. Tris-to-Quads button cleans triangles first (UE re-triangulates on import anyway).
5. **Vertex Mask mode**: subdivide the mesh a few times first — a default 8-vert cube paints as one solid block; ~386 verts gives clean edge lines. Paint Edge Mask, tune falloff Rings and Curve, Preview.
6. **Chamfer mode**: Check Topology ("mesh looks clean for chamfering"), set Width and Segments, Chamfer Sharp Edges (also applies smooth shading). 1 segment already helps; 3–4 segments give perfect displacement flow.
7. **Export**: the panel's FBX export button adds a `_masked` suffix; there's a matching FBX import button for round-tripping.
8. **Import into UE5**: Nanite is enabled in the import options; set **Vertex Color Import Option = Replace** (Ignore keeps existing mesh colors on re-import; Override floods a specified color) so Blender's vertex data comes through.
9. **Material side**: the Surface Forge material instance has "Use Displacement Mask" reading the **Alpha channel** by default — any vertex-color channel works, but Red takes priority over Alpha (first in the chain). Painting a channel in Modeling Mode kills displacement exactly there, with visible falloff; disabling the mask parameter restores displacement everywhere.
10. **Complex meshes** (subdivided + displaced blob): threshold ~25–40° flags the problem edges; vertex masking fails without heavy subdivision, chamfering "works" but mangles the silhouette. World-aligned/tri-planar textures hide many residual tears. Verdict: keep displacement on basic shapes with small modifications.

### UE Systems / Blueprints / Settings
- **Nanite Displacement (UE5)** — tearing on hard edges is the core problem; displacement driven by material with world-aligned / tri-planar textures.
- **Modeling Mode → Attributes → Paint Vertex Colors**: channel selection (R/G/B/A), erase color w/ alpha, Erase All / Accept — used to inspect and edit the imported mask in-editor.
- **Static Mesh import dialog**: Nanite build option; *Vertex Color Import Option*: Replace / Ignore / Override (+ override color picker).
- **Surface Forge material instance**: Use Displacement Mask (per-channel, Red > Alpha priority), tiling, displacement weight/depth params, two-in-one material blending toggle, world-aligned (tri-planar) texture option.
- **Blender Edge Mask Painter add-on** (free, Patreon; Blender 3.2–5.0): FBX import/export round-trip (`_masked` suffix), mesh detection + face-type breakdown, angle-threshold edge detection with preview color/refresh, Tris-to-Quads, Vertex Mask paint (falloff rings + curve), Chamfer mode (topology check, width, segments).

### Difficulty
Intermediate

### UE Version
UE5 (Nanite displacement; Blender 5.0 shown, add-on works from Blender 3.2)

### Tags
nanite, displacement, materials, vertex-color, blender, fbx, mesh-import, chamfer, tri-planar, surface-forge, world-forge, modeling-mode

---

## Related Entries
- [Creating a Blend Material in Unreal Engine 5 Just Got Easier](creating-a-blend-material-in-unreal-engine-5-just-got-easier.md) — Nanite + displacement enabling on meshes for Dash blend materials
- [GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5](how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin.md) — Nanite displacement via material edit (Actor Switch Nanite)
