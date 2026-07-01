---
title: "What's NEW in the Skeletal Mesh Editor | Unreal Engine 5.8"
source: YouTube
url: https://www.youtube.com/watch?v=EZuBtnS4eMk
author: Proj Prod
ingested: 2026-07-01
ue_version: "UE 5.8"
tags: [skeletal-mesh, skinning, morph-targets, weight-painting, selection-tools, rigging, joints, ue5, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/whats-new-in-the-skeletal-mesh-editor-unreal-engine-58/
frame_count: 7
---

# What's NEW in the Skeletal Mesh Editor | Unreal Engine 5.8

**Source:** [YouTube](https://www.youtube.com/watch?v=EZuBtnS4eMk)
**Author:** Proj Prod
**Duration:** 7m55s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** It was really good today's the special day because I'm really proud of my t-shirts.  Yeah, let me share that with you guys first.  Look at that!  Coming straight from Japan.  Here ya.  Alright, let's go back to business today.  It's all about skeletal mesh editor.  Yeah, what's new in 5.8 and you see that it changed a lot since the first video we did  like in 5.253.  So let me do a quick recap and highlights of what's new in it.  Let's go.  So the first thing I wanted to show is about the core functionality of the skeletal mesh editor.

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_000.jpg

### Core Improvements, Asset editing [0:31]
**Transcript:** In general, Control-PLED-Z is now much more robust and in addition, if you're doing any  modifications, you can now choose to apply them directly or keep them for later.  You also have a kind of stack of all the changes you've made on the bottom left side giving  you a clear overview of what you're doing.  And this is great for iterating and trying out a lot of things before actually applying  and saving the asset itself.  Sometimes you just want to explore and experiment without committing the changes right away,  so this is a really nice addition.  Out of the box, you probably notice new icons at the top of the UI.

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_001.jpg

### Selection Improvements [1:07]
**Transcript:** These are really important and really useful for improving the overall workflow of the skeletal  mesh editor.  You now have the Object Selection mode, which is the current default mode where you  can select the different parts of the skeletal mesh.  Then you also have these new tools where you can switch into Vertex, Edge and Face  selection, as well as Polygroups.  When you switch into one of these modes, it automatically updates the corresponding selection  type and the same applies for Polygroups where you can work directly with vertices, edges  or faces.  So instead of just working in one single block, if I create Polygroups, I can now manage  and select them much more easily from here.  What makes this really powerful is that it comes in addition to a new panel you're going  to have on the side.  Based on your current selection, you can perform a bunch of actions.  The first selection is what you already see at the top, but then you can also manipulate  your active selection, for example by expanding it, growing connected elements, or fully  resetting it back to normal selection behavior.  We also have Soft Selection, which helps when making more organic modifications to the  mesh, that you can also isolate your current selection.  On top of that, there is an isolation mode specifically useful when editing weights.  So for example, if I select just this face, I can use Expand Connected to grow the selection  and then isolate it so I'm only working on that specific area.  From there, I can adjust things like SkinWates or even more Fuggets.  If we circle back to Shotcuts in 5.8, we have now a new keyboard Shotcuts window where  you can customize almost everything, including isolates, expand and all the features we just  covered.  Also the Moff icon you see here is visible thanks to the Moff Target editing tools plugin,  so make sure to enable it if you want to access it.  It's still experimental, but there are more updates coming on that front as well, so stay  tuned.  So as mentioned, if I show the full mesh now, I can select the parts, let's see I'm  selecting this area here.  We're still missing Edge Loop Selection, which is a bit of a shame, because it makes it  harder to select large areas efficiently.  But with this simple selection, I can now go in and use Expand Selection and Simulator.  For example, let's assign a Shotcut to it.  This uses the same Shotcut system as the Modeling Mod selection.  So let's say I map these to Alt plus E.  Number pressing Alt plus E, I can quickly grow the selection to cover the area I need  and then I can press Ctrl plus H to isolate that part.  On top of that, there are icons here that you let you display hierarchy as well.  If you hold Shift and click this icon, you can toggle those options and display the hierarchy  together with the isolated object.  Now if I switch to Edit Waits, on the right hand side, you can see these new icons, and

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_002.jpg

### Lock Joints (Auto normalization) [4:05]
**Transcript:** honestly, that's a huge plus.  It's a real game changer and enables much more advanced workflows for skin editing inside  and real.  If you right-click, you're going to have the option to Lock Joins.  For example, if I'm focusing on this Limb, I can unlock just these three joins.  What that means is that when I modify Waits on one joint, with auto-normalization enabled,  it will redistribute the Waits only across the unlock joins.  In the past, during skinning work, influences could sometimes shift to an intended joins  and mess up your setup, meaning you had to be much more methodical and it was generally  slower and less flexible.  But now with this locking system, any changes I make with only affected joins I've explicitly  allowed, which makes the workflow much more control and predictable.  Much closer to a traditional skinning workflow.  And as I mentioned, beyond the isolated object selection, you can also isolate and refine  selections directly in skinning mode as well.  All of these quality of life features are designed to help you manage and dive deep into skinning  work.  And I'm just scratching the surface here because there are tons of other smaller quality  of life improvements, things that might seem minor, but are actually really important  when you're working in this skeletal mesh editor, with skeletal meshes, morph lagged,  and skinning more flows in general.  It's really important to have a clean and friendly ecosystem to work in.  One small but very useful addition is that unused joins can now be easily removed.

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_003.jpg

### Joints Management [5:35]
**Transcript:** When you right click, you now have the option to remove all the unused elements, which  is quite convenient.  Even if these joins don't currently hold any skinned weight information, they can see  an impact performance, so if you are not using them, you can simply get rid of them quickly  through this new option.  It's just a right click action, and you can clean things up almost instantly.  If you want to go further, there's a lot of more information available in the Rodmap.  As you can see, there's a lot coming, including improvements around morph laggeds,  overall digital quality of life, selection workflows, and many other enhancements.

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_004.jpg

### Morph Targets Editing [6:15]
**Transcript:** And in addition to this little overview, let's talk about blend shapes and the new features  around them.  So now if I select what I want, for example, the face I can go in, use the expand to  connect the selection, and then isolate it.  From there if I go to the morph section and open morph laggeds, I can create a new  morphed lagged.  And what's that done, I can switch into scope mode and focus only on the area I want,  as you can see here.  I can now start sculpting my blend shape directly.  There have also been improvements to the move brush, which now has a slightly different  behavior, with better consistency and a more natural feel to work with.  Overall the traditional sculpting morph through is still here.  You can manage and adjust everything you need quite easily without having to leave and  relang in.  What's new is that once you're done, you can now right click and finally mirror a flip  you morphed a get, and even merge or apply the current weight to morphed a get.  The main ones for me are mirror and flip.  You can directly mirror the morphed a get you just created or duplicate it and flip it.  And it will automatically mirror economy.  This is something that was missing before, so it's really good to see it now.  It changes a lot of things and helps you avoid having to export your skeletal mesh, re-import  it and go through external tools.  Everything now can be authored directly, inside and real, even if you already have existing  morphed nuggets like in this case, where you can still go back and adjust everything.

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_005.jpg

### Outro [7:37]
**Transcript:** And that's it for today guys, I just want you to comment and leave feedback on what you  think about my t-shirts.  See you next week for a new one.  Ciao!

**Frame:** tutorials\frames\whats-new-in-the-skeletal-mesh-editor-unreal-engine-58\frame_006.jpg


---

## Structured Notes

### Core Technique
Overview of UE 5.8 quality-of-life additions to the Skeletal Mesh Editor: non-destructive change stacking, sub-object selection modes (Vertex/Edge/Face/Polygroups), joint locking for safe auto-normalized weight painting, one-click unused joint removal, and in-editor morph target sculpting with mirror/flip support. All workflows stay inside UE — no round-tripping to external DCCs.

### Summary
7m55s Proj Prod highlight reel of the Skeletal Mesh Editor changes in UE 5.8. Covers four main areas: (1) non-destructive asset editing via a change stack with deferred apply/save; (2) sub-object selection modes (Vertex/Edge/Face/Polygroups) with a side panel for expand-connected, soft selection, isolate, and weight-editing isolation — plus a new customizable keyboard shortcuts window; (3) joint locking so auto-normalization only redistributes weights across explicitly unlocked joints; (4) morph target sculpting with right-click mirror/flip directly in-editor. Also notes the Morph Target Editing Tools plugin (experimental, enables Morf icon) and the roadmap for upcoming improvements.

### Key Steps
1. **Change stack (non-destructive editing)**: Make modifications in the Skeletal Mesh Editor — changes queue in a stack visible bottom-left. Choose Apply to commit or defer; Ctrl+Z is now more robust throughout.
2. **Sub-object selection**: Toolbar icons switch between Object (default), Vertex, Edge, Face, and Polygroup selection modes. Side panel appears with selection actions.
3. **Selection side panel actions**: Expand Selection (grow adjacent elements), Grow Connected (flood-fill connected topology), Soft Selection (organic falloff), Isolate (Ctrl+H), and Isolate for Weight Editing (separate mode for skinning focus).
4. **Custom keyboard shortcuts**: New Shortcuts window (accessible from toolbar) — assign any action. Example: Alt+E for Expand, Ctrl+H for Isolate. Uses the same system as Modeling Mode.
5. **Hierarchy display**: Shift+click the hierarchy icon to toggle displaying the bone hierarchy alongside an isolated object.
6. **Enable Morph Target plugin**: Edit → Plugins → enable "Morph Target Editing Tools" (experimental) to get the Morf icon and sculpt tools in the editor toolbar.
7. **Lock joints for safe skinning**: In weight paint / skeleton panel, right-click a joint → Lock Joint. With auto-normalization ON, weight changes on any joint only redistribute among unlocked joints — prevents unintended influence spillover.
8. **Remove unused joints**: Right-click joint → Remove All Unused Joints. Clears joints with no skinned weight (they still cost performance).
9. **Morph target sculpting**: Select mesh area → Expand Connected → Isolate → open Morph section → New Morph Target → sculpt in scope mode. Improved Move brush for natural feel.
10. **Mirror/Flip morph targets**: After sculpting, right-click the morph target → Mirror (creates mirrored copy), Flip (flips existing), or Merge/Apply Weights to Morph Target. Handles symmetry automatically without export/reimport.

### UE Systems / Blueprints / Settings
- **Skeletal Mesh Editor** — main editor; change stack at bottom-left
- **Change Stack** — non-destructive pending changes queue; Apply or discard individually
- **Object / Vertex / Edge / Face / Polygroup selection modes** — toolbar toggle icons
- **Selection Side Panel** — context actions: Expand Selection, Grow Connected, Soft Selection, Isolate, Isolate for Weight Editing
- **Keyboard Shortcuts window** — custom bindings; reuses Modeling Mode shortcut system
- **Morph Target Editing Tools plugin** — experimental; enables in-editor sculpt toolbar (Morf icon)
- **Lock Joints** — right-click → Lock Joint; controls auto-normalization scope during weight paint
- **Auto-Normalization** — redistributes weight only among unlocked joints when Lock Joints active
- **Remove All Unused Joints** — right-click → removes zero-weight joints to reduce performance cost
- **Morph Target panel** → New Morph Target → scope sculpt mode
- **Morph Target right-click actions**: Mirror, Flip, Merge, Apply Weights to Morph Target

### Difficulty
Intermediate

### UE Version
UE 5.8

### Tags
skeletal-mesh, skinning, morph-targets, weight-painting, selection-tools, rigging, joints, ue5, intermediate

---

## Related Entries
None identified in current skill library — first skeletal mesh editor tutorial ingested.
