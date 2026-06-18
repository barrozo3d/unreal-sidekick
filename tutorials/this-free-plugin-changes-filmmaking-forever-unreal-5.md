---
title: This Free Plugin Changes Filmmaking Forever [Unreal 5]
source: YouTube
url: https://www.youtube.com/watch?v=LUoUVC5tXCo
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [animation, control-rig, rigging, sequencer, beginner]
extraction_status: complete
frames_dir: tutorials/frames/this-free-plugin-changes-filmmaking-forever-unreal-5/
frame_count: 4
---

# This Free Plugin Changes Filmmaking Forever [Unreal 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=LUoUVC5tXCo)
**Author:** Josh Toonen
**Duration:** 16m0s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Download the One-Click Control Rig for Free! [0:00]
**Transcript:** Introducing the one-click control rig. With this free plugin, you can add animations to any 3D character and design your own action scenes in Unreal Engine 5.  And don't worry, you don't have to Brig, Model, or animate anything yourself.  Just follow along, and I'll show you how to start with any 3D model and end by creating your own action scene from scratch.  Download the one-click rig right now at Unreal for VFX.com slash Rig. You can get started with any 3D model that you can find online.  My favorite resources for this are ArtStation, TurboSquid, and CGTrader. But as long as you have a .fbx or .obj file, you're ready to get started.

**Frame:** tutorials\frames\this-free-plugin-changes-filmmaking-forever-unreal-5\frame_000.jpg

### Prep any 3D model to be Unreal-ready [0:30]
**Transcript:** I'll leave a link down below for one of my favorite creators on ArtStation, Random Things, who has hundreds of different characters that you can add into your scene.  Now there's a couple things you should know to guarantee that everything's going to work when you import this model into Mixamo.com.  The first is we want to remove any rig associated with this character. We want Mixamo to completely replace any existing rig, so all we're going to do in Blender is remove it.  To do this, I'm just going to take our original mesh right here, and I'm going to drag it outside of the hierarchy of this armature.  Armature is just a rig inside a blender, so if I bring it outside of that scene collection, that'll separate it from our rig, and then I'm going to delete the entire rig, so there's no chance that we export the rig with this file.  And as a last step, I'm going to remove this armature modifier right here. Now our model is prepped, and we just want to make sure that the height of our character is correct before we transfer it over to Mixamo.  Just click on this little ruler icon, which is the measuring tool inside of Blender. I'm going to go to the front Y-axis view, and now I can j...

**Frame:** tutorials\frames\this-free-plugin-changes-filmmaking-forever-unreal-5\frame_001.jpg

### Auto-rig your characters with Mixamo.com [1:30]
**Transcript:** Someone who's six feet tall would be 1.82 meters tall, so if we want to make them six feet, let's set this to 1.82, and then we'll grab our character and press the S key to scale them up.  Now our character should be ready to export over to Mixamo.com.  Let's select our character, and make sure there's no rig attached. Now let's go to File, Export, and we can export this as a .fbx file.  I'm going to limit this export to selected objects only, and we're ready to export this out. Otherwise, if you're experiencing any issues, you can also export this as a .obj file.  I've never had any issues importing a .obj file.  The one thing I've found is that you want to multiply the scale of your scene by 10 units before we export it over to Mixamo.  So now let's upload our 3D character to Mixamo.com. Just log in to Mixamo.com and make a free Adobe account if you don't have one already.  Now on the right side, let's upload our character. So I'll just click and drag our character and upload them to Mixamo.  Now let's use their auto-rigger tool to generate a rig for free. Just line up the chin, wrists, elbows, knees, and growing.  And depending on your character, you can select the detail of you...

**Frame:** tutorials\frames\this-free-plugin-changes-filmmaking-forever-unreal-5\frame_002.jpg

### How to Improve your Animations in Sequencer [9:28]
**Transcript:** So let's try to find an animation for Master Chief that makes him feel strong and have him pose at the end.  If you go to Mixamo.com, you can type in RIFLE and find a bunch of cool animations where that character is already holding a rifle, which will really help us out.  And I found this animation called RIFLE NEAL TO STAND.  I'm also going to download an idle animation, which will be Master Chief holding a rifle in place with some simple, Keep Alive animation.  So now I can take that animation and just drag it into our content browser, and because we've already set up our character, we don't need to import the mesh, we just want to import the animation itself, and just assign it to the skeleton of your character, and we'll press import all.  So let's add that animation, I'll type in NEAL TO STAND, and we'll slide this to the front.  Cool, so we have something to start it off, but we need to transition it into this RIFLE idle animation, and we can just line that up back to back.  You can see there's a bit of a pop when we transition between these two animations, and this is more obvious when we're not looking through our camera, kind of teleports backwards.  So to fix this, we don...

**Frame:** tutorials\frames\this-free-plugin-changes-filmmaking-forever-unreal-5\frame_003.jpg


---

## Structured Notes

### Core Technique
Complete OneClick Control Rig workflow: preparing a character in Blender (remove armature), uploading to Mixamo for auto-rigging, importing back to UE5, and blending multiple animations in Sequencer using motion blend.

### Summary
Josh Toonen introduces the OneClick Control Rig plugin as the foundational tool for UE5 filmmaking with custom characters. Viewers learn the full pipeline from preparing a 3D character in Blender (removing the existing armature and scaling to real-world height) through Mixamo's marker-based auto-rigging and back into UE5 with a fully functional Control Rig. The tutorial covers blending multiple Mixamo animations together in Sequencer using motion blend, demonstrated with a rifle kneel-to-stand transition.

### Key Steps
1. In Blender, open the character file; select the armature → X → Delete; the mesh should remain without any rig.
2. Scale the character to real-world height using Blender's ruler tool (N panel → View → Ruler); match height to ~1.75m for average male.
3. Multiply the export scale by 10 units before exporting FBX from Blender (export scale = 10 to match UE5's unit scale), or export as OBJ at default scale.
4. Upload to Mixamo.com: click Upload Character → place the 7 auto-rig markers (chin, left/right wrists, left/right elbows, left/right knees, groin) → proceed to get the rigged FBX.
5. Download the Mixamo-rigged character as FBX; also download desired animation packs (e.g., rifle pack).
6. In UE5, import the rigged character FBX (Skeletal Mesh, create new skeleton); then install the OneClick Control Rig plugin (Edit → Plugins).
7. In Sequencer, add the character and animation tracks; right-click animation clips to use Motion Blend → match bone = hips to seamlessly chain rifle kneel → stand → idle animations.

### UE Systems / Blueprints / Settings
- **Blender prep**: Remove armature (select armature → X → Delete); ruler tool (N panel) for real-world height check; FBX export scale = 10
- **Mixamo markers**: 7 points: chin, L/R wrists, L/R elbows, L/R knees, groin; Mixamo processes and returns rigged FBX
- **OneClick Control Rig plugin**: Edit → Plugins → "OneClick Control Rig" → Enable; right-click skeletal mesh → Create OneClick Control Rig
- **Motion blend in Sequencer**: Right-click animation clip → Motion Blend Options → Match Previous Clip → Bone = pelvis/hips

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
animation, control-rig, rigging, sequencer, beginner

---

## Related Entries
- [[how-to-animate-spider-man-in-unreal-engine-5-for-beginners]] — next-level Control Rig editing: additive tracks, Pose Library, bone attachment
- [[unreal-5-animation-made-easy-free-download]] — short companion promo for the same OneClick Control Rig plugin
- [[how-to-make-blade-runner-in-unreal-5-step-by-step]] — beginner pipeline that uses Mixamo rigging as a core step
