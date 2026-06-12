# Recipe: MetaHuman → Sequencer → MRQ Cinematic Pipeline

**Goal:** Set up a photorealistic digital human (MetaHuman) in a Sequencer shot, animate it, and render with MRQ at full quality.  
**UE Systems:** MetaHuman, Quixel Bridge / MetaHuman Creator, Sequencer, Control Rig, MRQ  
**Difficulty:** Advanced

---

## Overview

MetaHuman is Epic's photorealistic digital human system. This recipe covers the full cinematic path:

```
MetaHuman Creator → Download → Level → Sequencer → Animate → MRQ → Deliver
```

MetaHumans include:
- High-fidelity head + body mesh with LODs
- Hair (Groom asset — strand-based)
- Clothing (can be replaced)
- Pre-rigged body + face skeleton
- Physics-simulated hair and clothing (optional)

---

## 1. Get a MetaHuman into Your Project

### Option A — MetaHuman Creator (Web/In-Editor)

1. Open **MetaHuman Creator** in editor: `Tools → MetaHuman Creator`  
   (or via `dev.epicgames.com/metahuman`)
2. Create or select a MetaHuman character
3. Click **Export to UE** → assign to your project
4. Wait for Quixel Bridge to download the assets (~3–10 GB)

### Option B — Quixel Bridge (Legacy)

1. Install Quixel Bridge plugin if not present
2. Bridge → MetaHumans tab → select character → Add to Project

### Result
After download, the MetaHuman appears in Content Browser at:
```
/Game/MetaHumans/<CharacterName>/
  BP_<CharacterName>       ← Blueprint actor (place this in the level)
  <CharacterName>_Face     ← Face skeletal mesh
  <CharacterName>_Body     ← Body skeletal mesh
  Hair/                    ← Groom assets
```

---

## 2. Place MetaHuman in a Level

1. Drag `BP_<CharacterName>` from Content Browser into the viewport
2. Position using `W/E/R` (translate/rotate/scale)
3. **Do NOT scale MetaHumans** — they are built at exact 1:1 scale

### LOD Setup for Cinematic Quality

MetaHumans have 8 LODs (LOD0 = highest). For cinematics:

1. Select the MetaHuman Blueprint in the level
2. In Details panel → **BP_<Name> → LOD Settings:**
   - `LOD Bias`: **-4** (force highest LOD at greater distances)
3. Alternatively: force LOD0 via `r.ForceLOD 0` for entire scene during render

### Hair Rendering Settings (Groom)

For each Groom component on the MetaHuman:
- `Details → Groom → Strands Density`: **1.0** (100% for cinematic)
- `Details → Groom → Simulation`: ON only if you need physics; OFF saves render time
- Enable Groom in MRQ: add `Console Variables → r.HairStrands.Enable 1`

---

## 3. Animate the MetaHuman in Sequencer

### 3a — Basic Body Animation

1. `Window → Cinematics → Sequencer` → create or open Level Sequence
2. `+ Track` → `Actor to Sequencer` → select the MetaHuman Blueprint
3. Under the MetaHuman track: `+ Track → Animation Track`
4. Drag an Animation asset onto the track

**Compatible animations:**
- Any animation on the UE5 Manny/Quinn skeleton (same skeleton)
- Custom animations via Control Rig or imported from Blender/Maya

### 3b — Facial Animation (Level Sequence)

MetaHuman faces are driven by Control Rig curves (52 FACS shapes):

1. In the MetaHuman track: `+ Track → Control Rig Track`
2. Select the **Face_ControlBoard_CtrlRig** asset
3. Add keyframes on face controls directly in Sequencer  
   OR use **MetaHuman Animator** (iOS/Windows face capture app) to drive the rig via Live Link

### 3c — Facial Animation via Performance Capture

If you have facial performance data:
1. `MetaHuman Animator` plugin → `Tools → MetaHuman Animator`
2. Import video or use Live Link source
3. Bake to Sequencer as Control Rig keyframes

### 3d — Control Rig for Body Posing

For manual pose control:
1. `+ Track → Control Rig` → select `MetaHuman_ControlRig`
2. Controls appear: `root`, `pelvis`, `spine_01..05`, `hand_l/r`, `foot_l/r`, etc.
3. Enable `FK/IK Switch` via `ik_hand_l`, `ik_foot_l` controls for limb IK

---

## 4. Camera Setup

For cinematic MetaHuman shots, match real camera specs:

1. Place a **Cine Camera Actor** in the scene
2. Add to Sequencer: `+ Track → Camera Cut Track` → assign the camera
3. Camera settings for close-up portrait:

| Setting | Value | Notes |
|---------|-------|-------|
| `Sensor Width` | 36mm | Full Frame 35mm |
| `Focal Length` | 85mm | Classic portrait lens |
| `Current Aperture` | f/1.8 | Shallow DOF for cinematic feel |
| `Focus Settings → Actor to Track` | MetaHuman head bone | Keep face in focus |
| `Focus Settings → Draw Debug Focus Plane` | ON (while setting up) | Visual aid |

---

## 5. MRQ Setup for MetaHuman Render

### Key Settings

**Anti-Aliasing:**
- `Temporal Sample Count`: 8
- `Spatial Sample Count`: 1
- `Render Warm Up Count`: 64 ← important for hair/cloth simulation to settle

**Console Variables to add:**
```ini
# Force highest quality LOD
r.ForceLOD 0
r.ForceLODShadow 0

# Hair quality
r.HairStrands.Enable 1
r.HairStrands.Shadow.Enable 1
r.HairStrands.RaytracingProceduralSplits 4

# Groom strands density override
r.HairStrands.StrandsVoxelSize 0.5

# Skin subsurface scattering (if using Lumen)
r.SSS.Scale 1.0
r.SSS.SampleSet 2

# Eyes
r.RefractionQuality 3

# Shadow quality for close-ups
r.Shadow.RadiusThreshold 0.001
r.CapsuleShadows.Quality 3

# Disable Lumen for Path Tracer (if using PT)
# r.DynamicGlobalIlluminationMethod 0
```

**Render Pass:**
- For hero close-up shots: **Path Tracer** (ground truth hair, SSS, reflections)
- For background/mid-distance: **Deferred** with Lumen (faster, still high quality)

### Path Tracer-Specific for MetaHuman:
- `r.PathTracing.MaxBounces 16` — adequate for skin SSS
- `r.PathTracing.SamplesPerPixel 256` — clean skin and hair
- NFOR denoiser: ON (handles hair strands well at 256+ spp)

---

## 6. Common MetaHuman Issues

| Problem | Fix |
|---------|-----|
| Hair disappears in Path Tracer | Add `r.HairStrands.Enable 1` to MRQ Console Variables |
| Face LOD switches during render | Add `r.ForceLOD 0` to Console Variables |
| Skin looks waxy/plastic | Check `r.SSS.Scale 1.0`; verify lighting has at least one direct source |
| Eyes look dull | Use `Reference Reflections` in PT or add a strong HDRI sky light |
| Cloth/hair jitter between frames | Increase `Render Warm Up Count` to 128; enable `Flush Cache on Warm Up` |
| Animation plays at wrong frame | Verify Sequencer frame range matches animation asset length |
| MetaHuman too small/large | Do NOT scale — adjust camera instead; MetaHumans are 1:1 scale |
| Face animation not baking | Use `MetaHuman Animator → Bake to Sequence` before MRQ render |

---

## 7. Rendering Hair with Path Tracer

Hair (Groom) rendering is one of the most expensive parts of MetaHuman renders. Optimization options:

| Approach | Quality | Speed |
|----------|---------|-------|
| Full strand PT + NFOR 256spp | Reference | Slow (~3 min/frame) |
| Full strand Deferred + Lumen | Very good | Medium (~30s/frame) |
| Strand ↔ Card crossover (LOD2+) | Good | Fast (~10s/frame) |
| Cards only (LOD3) | Acceptable | Very fast |

For hero shots: always use LOD0 (full strands). For mid-distance shots: LOD1 or LOD2 is visually identical.

---

## References
- `references/sequencer-cinematics.md` — Sequencer, Cine Camera, Level Sequences, MRQ
- `references/rendering-pipeline.md` — Path Tracer, Lumen, TSR
- `references/niagara-vfx.md` — Groom Fluids (not MetaHuman-specific, but relevant for hair)
- `recipes/mrq-multipass-exr.md` — Full MRQ pass configuration
- `recipes/path-tracer-nfor-delivery.md` — Path Tracer + NFOR for close-up render quality
- Tutorial: `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Control Rig, Sequencer, MRQ
