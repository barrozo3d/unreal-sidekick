---
title: Path Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH
source: YouTube
url: https://www.youtube.com/watch?v=i6GTbioHD4k
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, scatter, path-scatter, curves, environment-art, world-building, beginner]
extraction_status: complete
frames_dir: tutorials/frames/path-scatter-beginner-guide-to-your-ue5-co-pilot-dash/
frame_count: 3
---

# Path Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=i6GTbioHD4k)
**Author:** Polygonflow Dash
**Duration:** 11m2s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Greetings, I'm Jonathan Polygonflow's Community Director for Dash, our next-gen Unreal Engine plugin that makes creating environments super easy. In this video, I'll be covering one of our many asset creation tools, Pathscatter, which has been significantly improved in Dash 1.4.

**Frame:** tutorials\frames\path-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_000.jpg

### Path Scatter Basics [0:29]
**Transcript:** So let's start by opening the Dash plugin. Since Dash is prompt-based, you're going to need to type Draw to bring up the Draw Curve menu. Then hit Enter to close it. Draw a shape to work with. If you feel that it has too many vertices, you can adjust that by holding Control and dragging with the middle mouse button to reduce the number of vertices in the curve, or add more if you feel that it needs them. You can see that the Curve tool will follow the terrain or any other object as you finish drawing. Next up, you'll need to type Path to bring up the Pathscatter tool. As with most tools in Dash, the window needs to be fully expanded to show all available options on-screen without scrolling. To start, make sure that your curve is selected and then add it to the list of active curves in Pathscatter. Then select an object in the world and add that to the active scatter list. This will auto-populate the path with a default set of parameters. You won't see much at first with this object, so I'll switch to Wireframe to make it more apparent. I'm going to adjust the MinScale and MaximumScale to bring the meshes up to make them more visible. Adjusting density changes how many instances appear along the path. You can assign multiple curves and multiple meshes to each other for even more complex setups. Offset controls the spacing of the instances along the path. Gap creates a uniform gap between each instance. Jitter randomly offsets each instance position along and off the path axis. You can adjust the forward, side, and vertical offset amounts independently as well. Align to curve makes the instances orient themselves along the path direction. Step size controls the spacing between each instance and the alignment resolution. There's also a random rotation option, but that can be combined with align to curve if you want both random and aligned rotations at once. You can set up multiple random rotation ranges per axis. You can also adjust offset along the path by XYZ to manually fine tune where instances land. There's a stagger option that will shift alternating instances to create a staggered pattern. Snap to terrain can be used to make the instances conform to the underlying terrain as well.

**Frame:** tutorials\frames\path-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_001.jpg

### Creating a Quick Scene Using Surface & Path Scatter [6:54]
**Transcript:** Now let's see how to create a super quick environment off the cuff using nothing but surface and path scatter together. I've got my base terrain and I'm going to adjust it a little to give me some variation to play off with Surface Scatter, which means I'll need some terrain height changes and some other adjustments too. Then I'll change the material in Dash to apply dirt procedurally to break up the texture repetition. Once I'm happy with the dirt texture breakup, I'll move over to my collection of static meshes. I've got three versions of the same type of tree in various growth stages and I'll start by using the largest trees first and surface scattering them with some quick adjustments, after which I'll move on to the next group of trees until I've placed all of them. I'm using different growth stages of these trees to help break up the environment so it doesn't look too homogenous. I'm going to pull up the draw tool and create a curve. The shape of the terrain roughly came out to look like a bicycle saddle, so I'll trace around it and get that shape locked in. Then I use Path Scatter to place rocks along the boundary curve. The rocks scatter along the curve edge cleanly, and by combining Surface Scatter (for the trees and ground cover) with Path Scatter (for the rocky boundary), I can quickly build a credible environment without any manual placement.

**Frame:** tutorials\frames\path-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_002.jpg


---

## Structured Notes

### Core Technique
Dash 1.4 Path Scatter: draw a curve in the viewport → assign it and a mesh to PathScatter → instances distribute along the curve with full control over density, scale, spacing, offset (forward/side/vertical), alignment to curve, jitter, stagger, and snap to terrain. Combined with Surface Scatter for complete environment coverage.

### Summary
11-minute Path Scatter guide by Jonathan (Community Director), covering Dash 1.4 improvements. Full parameter walkthrough: curve draw (Ctrl+MMB drag = vertex density), assign curve + mesh to PathScatter, density (instance count), min/max scale, offset spacing, gap (uniform gap), jitter (random offset along/off path), forward/side/vertical XYZ offset, align-to-curve + step size, random rotation ranges per axis, stagger (alternating instance offset), snap to terrain. Multiple curves and meshes can be combined. Second half shows combining Surface Scatter (trees, ground cover) + Path Scatter (rocky boundary) to build a credible environment quickly without any manual placement.

### Key Steps
1. **Draw curve** — type `draw` in Dash → Draw Curve menu → draw shape in viewport; Ctrl+MMB drag left/right = reduce/increase vertex count; curve conforms to terrain.
2. **Open Path Scatter** — type `path` in Dash → expand tool window.
3. **Assign curve** — select curve → add to active curves list in PathScatter.
4. **Assign mesh** — select mesh in world → add to active scatter list; auto-populates with defaults.
5. **Density** — controls how many instances appear along the path.
6. **Min/Max Scale** — scale range for instances.
7. **Offset** — spacing between instances along path.
8. **Gap** — uniform gap between instances.
9. **Jitter** — random offset per instance along and off the path axis.
10. **Forward/Side/Vertical offset** — independent XYZ position adjustment per instance.
11. **Align to curve** — instances orient along path direction; Step Size controls spacing + alignment resolution.
12. **Random rotation** — per-axis rotation ranges; can combine with Align to Curve.
13. **Stagger** — alternating instances offset for non-uniform look.
14. **Snap to terrain** — instances conform to underlying terrain height.
15. **Multi-curve/mesh setup** — assign multiple curves and multiple meshes for complex path networks.
16. **Combined workflow** — Surface Scatter for area coverage (trees, ground cover) + Path Scatter for boundary definition (rocks along terrain edge); no manual placement needed.

### UE Systems / Blueprints / Settings
- **Draw Curve tool** — Ctrl+MMB drag = vertex density control; curve conforms to terrain on draw
- **PathScatter** — curve-driven ISM scatter; multi-curve + multi-mesh support
- **Density** — instance count along full curve length
- **Offset/Gap** — offset = step spacing; gap = forced minimum space between meshes
- **Jitter** — random per-instance position deviation along and perpendicular to curve
- **Forward/Side/Vertical XYZ offset** — manual fine-tune of instance positions
- **Align to Curve** — mesh forward axis follows curve tangent; Step Size = alignment resolution
- **Stagger** — alternates instances between two offset tracks for organic look
- **Snap to Terrain** — Z-axis conform to underlying terrain mesh

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.4)

### Tags
`#dash-1.4` `#scatter` `#path-scatter` `#curves` `#environment-art` `#world-building` `#beginner`

---

## Related Entries
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter guide (same series, complements Path Scatter)
- [[beginner-content-library-tutorial-for-ue5]] — Content Library + placement hotkeys
- [[dash-110---procedural-scatter-presets-in-ue5]] — Dash 1.10: PathScatter presets + Decal/Blueprint actors support
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8: path scatter used for road markings + leaf scatter on curves
