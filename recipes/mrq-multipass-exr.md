# Recipe: MRQ Multi-Pass EXR Rendering

**Goal:** Set up Movie Render Queue to output every render pass as a multi-layer EXR sequence for compositing in Nuke, DaVinci Resolve, or After Effects.  
**UE Systems:** Movie Render Queue (MRQ), Sequencer, Post Process Volume  
**Difficulty:** Intermediate

---

## Overview

Multi-pass rendering separates the beauty render into components (beauty, AO, shadows, depth, normals, motion vectors, etc.). This gives the compositor full control without re-rendering.

Two output modes:
- **Multi-layer EXR** — all passes in one .exr file per frame (Nuke-friendly)
- **Multi-file EXR** — one .exr file per pass per frame (DaVinci-friendly)

---

## 1. Add Shot to Movie Render Queue

1. Open MRQ: `Window → Cinematics → Movie Render Queue`
2. Click `+ Render` → select your Level Sequence
3. The job appears in the queue with a default preset

---

## 2. Configure Job Settings

Click the **Preset** icon on the job to open the settings panel.

### 2a — Anti-Aliasing (Quality)

- **Render Settings → Anti-Aliasing:**
  - `Temporal Sample Count`: **8–32** (higher = less noise in motion)
  - `Spatial Sample Count`: **1** (increase to 4+ for maximum quality)
  - `Override Anti-Aliasing`: ON → set to `None` (TSR/TAA fights with accumulation)
  - `Use Camera Cut to Warm Up`: ON
  - `Render Warm Up Count`: **64 frames** (fills temporal history)

### 2b — High Resolution (if needed)

- Add `High Resolution` setting
  - `Tile Count`: 2×2 or 3×3 for resolution above 4K
  - `Overlap Ratio`: 0.25 (reduces tile seams)

### 2c — Console Variables

Add `Console Variables` setting. Key CVars for quality:

```ini
# Lumen quality
r.Lumen.Reflections.ScreenTraces 0
r.Lumen.Reflections.MaxRoughnessToTrace 1.0
r.Lumen.FinalGather.Quality 4

# Shadow quality
r.ShadowQuality 5
r.Shadow.CSM.MaxCascades 10

# Nanite
r.Nanite.MaxPixelsPerEdge 0.5

# TSR (if using TSR, not Path Tracer)
r.TSR.History.SampleCount 32

# Path Tracer (if using Path Tracer)
r.PathTracing.MaxBounces 32
r.PathTracing.SamplesPerPixel 1024
```

---

## 3. Add Render Passes

In the Job Settings panel, click `+` to add render pass outputs:

### Pass 1 — Deferred Rendering (EXR Beauty)

| Pass | Type | Notes |
|------|------|-------|
| **Deferred Rendering** | Main beauty pass | The full lit render |
| **Ambient Occlusion** | AO only | `r.AmbientOcclusion 1` required |
| **Depth (SceneDepth)** | World-space depth | Use for depth-of-field in comp |
| **Normals** | World normals | R=+X, G=+Y, B=+Z |
| **Diffuse** | Raw diffuse contribution | Useful for relighting |
| **Specular** | Raw specular | Isolate specular for grading |
| **Shadow** | Shadow mask | Adjust shadows independently |
| **Bloom** | Bloom only | Can be added in comp instead |
| **Motion Vectors** | 2D motion in UV space | Required for motion blur in comp |

**To add each:** In Job Settings → `+` → `Render Pass` → pick from list.

### Pass 2 — Path Tracer (if using Path Tracer)

Swap Deferred Rendering for `Path Tracer`. Available passes:

| Pass | Notes |
|------|-------|
| **Path Tracer** | Full beauty, ground truth |
| **Albedo** | Unlit material color |
| **Emission** | Emissive surfaces only |
| **Normal** | World normals |
| **Radiance** | Raw incoming light (pre-material) |

**NFOR Denoiser** (recommended): See `recipes/path-tracer-nfor-delivery.md`

### Pass 3 — Stencil / Object Masks

1. In each Actor's **Details → Rendering → Rendering Customizations → Custom Depth Stencil**:
   - Check `Render CustomDepth Pass ✓`
   - Set `CustomDepth Stencil Value` = unique ID (1–255)
2. In MRQ Job Settings → `+` → `Object ID / Custom Stencil`

---

## 4. EXR Output Settings

### Option A — Multi-Layer EXR (all passes in one file)

1. Job Settings → `Output` → set type to **EXR Sequence**
2. Set `Compression`: `Zip` (good balance) or `PIZ` (for effects-heavy shots)
3. Enable `Multilayer Output`: ON
4. All passes write into a single EXR with named layers

**Nuke reads this natively** with `EXR` node → channels listed in the node's properties.

### Option B — Multi-File EXR (one file per pass)

1. Each pass writes its own subfolder: `Output/beauty/`, `Output/depth/`, etc.
2. Better for DaVinci Resolve, which reads one EXR type per timeline track

### Output Path Convention

```
{project_dir}/Renders/{sequence_name}/{shot_name}/{pass_name}/
{file_name}_{frame_number}.exr
```

Token example:
```
D:/Renders/{sequence_name}/{shot_name}/{render_pass}/frame_{frame_number}.exr
```

Set in `Output → Directory` and `Output → File Name Format`:
```
{sequence_name}_{shot_name}_{render_pass}_{frame_number}
```

---

## 5. Color Space

For ACES / ACEScg compositing workflow:
- MRQ Output → `Tonemapper` → disable `Use Post Processing Settings` → set custom tonemapper = None
- Set `Output Color Space` = `ACEScg` (Linear)
- Import into Nuke with `ACES - ACEScg` input colorspace
- Import into DaVinci with project set to ACES color science, input = `ACEScg`

For standard sRGB / Rec.709 delivery:
- Keep default UE tonemapping
- `Output Color Space` = `Gamma 2.2 / sRGB`

---

## 6. Render

1. Back in MRQ main window: click **Render (Local)** or **Render (Remote)**
2. Monitor progress in the queue
3. Check outputs in the defined directory

**Estimate render time:**
- Deferred: ~2–10 seconds per frame (depends on complexity)
- Path Tracer 1024 spp: ~1–5 minutes per frame (depends on GPU)

---

## 7. Compositing Import

### In Nuke:
```python
# Read multi-layer EXR
n = nuke.createNode('Read')
n['file'].setValue('/path/to/frame_%04d.exr')
n['first'].setValue(1001)
n['last'].setValue(1100)
# Access layers: nuke.layers(n) shows all available passes
```

### In DaVinci Resolve:
1. Media Pool → Import EXR sequences
2. Right-click clip → Clip Attributes → set `Input Color Space` = match your MRQ output space

---

## Gotchas

| Problem | Fix |
|---------|-----|
| First frame is black / broken | Add warm-up frames: `Anti-Aliasing → Render Warm Up Count: 64` |
| Depth pass is all white | Change depth output mode to `Linearized` in pass settings |
| Motion vectors look wrong | Ensure `r.MotionBlur 0` is NOT set during MRQ render |
| AO pass is missing | Add `r.AmbientOcclusion 1` to Console Variables setting |
| Path Tracer pass shows noise | Increase spp or enable NFOR denoiser |

---

## References
- `references/sequencer-cinematics.md` — MRQ settings table, render settings
- `references/rendering-pipeline.md` — Path Tracer, Lumen, TSR settings
- `recipes/path-tracer-nfor-delivery.md` — Full Path Tracer + NFOR workflow
- Tutorial: `tutorials/animating-characters-and-objects-in-unreal-engine.md` — MRQ/Movie Render Graph
