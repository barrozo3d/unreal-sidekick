---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# MetaHuman — Reference

MetaHumans are high-fidelity digital humans from Epic's MetaHuman Creator, importable into UE via Quixel Bridge.

## Asset Overview

| Asset | Location | Description |
|-------|----------|-------------|
| `BP_MetaHumanName` | `MetaHumans/Name/` | Main character Blueprint |
| `SKM_Name_FaceMesh` | `MetaHumans/Name/Face/` | Face Skeletal Mesh |
| `SKM_Name_BodyMesh` | `MetaHumans/Name/Body/` | Body Skeletal Mesh |
| `MetaHuman_ControlRig` | `Common/Common/` | Full-body Control Rig |
| `Face_ControlBoard_CtrlRig` | `Common/Face/` | Facial rig for Sequencer |
| `metahuman_base_skel` | `Common/Female/Medium/.../` | Skeleton for FBX import |
| `RTG_MH_IKRig` | `Engine/Plugins/MetaHumanCreator/Animation/Retargeting/` | Optimized IK retargeter |
| `IK_MH_IKRig` | same | MetaHuman IK Rig (source rig) |

## Required Plugins
- Groom
- Rig Logic Plugin
- Live Link
- Live Link Control Rig
- Control Rig
- Megascans

## Required CVars (added automatically on first Bridge import)
```ini
[ConsoleVariables]
r.GPUSkin.Support16BitBoneIndex=True
r.GPUSkin.UnlimitedBoneInfluences=True
r.SkinCache.CompileShaders=True
r.SkinCache.DefaultBehavior=0
SkeletalMesh.UseExperimentalChunking=1
fx.Niagara.ForceLastTickGroup=1
```

---

## MetaHuman Component (UE 5.5+)

Controls animation feature quality per LOD. Found in BP_MetaHumanName > MetaHuman component.

| Property | Default | Description |
|----------|---------|-------------|
| `Enable Body Correctives` | LOD 0 | Volume-preserving skin deformation |
| `Facial Animation LOD Threshold` | LOD 2 | Rig Logic evaluates up to this LOD |
| `Enable Neck Correctives` | LOD 0 | Neck volume fix on extreme rotations |
| `Neck Procedural Control Rig LOD Threshold` | LOD 0 | Keep in sync with neck correctives |

**Performance dial:** Lower thresholds = faster; raise for cinematic quality.

---

## LODSync Component

Synchronizes 8-LOD face with 4-LOD body so they transition together.

| Property | Notes |
|----------|-------|
| `Num LODs` | 8 (default); -1 = auto detect |
| `Forced LOD` | -1 = auto; 0 = force highest quality |
| `Min LOD` | Floor LOD regardless of screen size |
| `Drive components` | Body, Face — set other parts as Passive |

---

## LOD Specifications

| LOD | Head Verts | Body Verts | Hair | Blendshapes |
|-----|-----------|-----------|------|-------------|
| 0 | 24,000 | 30,500 | Strands 50K | 669 |
| 1 | 12,000 | 7,600 | Strands 25K | — |
| 2 | 6,000 | 3,350 | Cards 30K verts | — |
| 3 | 2,500 | 1,507 | Cards 15K verts | — |
| 4 | 1,300 | — | Cards 10K verts | — |
| 5+ | 560–130 | — | Cards/Mesh | — |

## Platform LOD Support

| Platform | Best LOD | Max Texture | Hair Type |
|----------|---------|-------------|-----------|
| PC (Epic) | 0 | 8192 | Strands + Cards |
| Mac | 0 | 8192 | Cards |
| iOS/Android | 3 | 2048 | Cards |

---

## Animation Methods

### 1. Custom FBX Animation
```
1. Import FBX → select metahuman_base_skel in Skeleton dropdown
2. Select MetaHuman in level → click Body component
3. Anim to Play field → drag animation asset
```

### 2. Sequencer + Control Rig
```
1. Drag BP_MetaHumanName into level
2. Create Level Sequence; add MetaHuman to it
3. Body track → MetaHuman_ControlRig (full body controls)
4. Face track → Face_ControlBoard_CtrlRig (facial expression controls)
5. Select controls in viewport → press S over Sequencer to keyframe
6. Disable Snap to Grid for precise facial rig control
```

**Bake animation:**
- Right-click Body track → Bake Animation Sequence
- Or: Create Linked Animation Sequence (live link, keeps sequence connected)

**Bake to Control Rig (edit existing animation):**
- Body track → + Track → Animation → add clip
- Right-click Body track → Bake To Control Rig → MetaHuman_ControlRig

### 3. IK Retargeting (from other characters)
```
1. Right-click source animation → Retarget Animations
2. Target Skeletal Mesh: MH body skeletal mesh (or identity mesh for runtime)
3. Retargeter: RTG_MH_IKRig (pre-built for MH)
4. Export Animation → choose output folder
```

**Custom retargeter (for non-MH sources):**
1. Create IK Rig for source → Auto Create Retarget Chains + Auto Create IK
2. Create IK Retargeter: Source = IK_MH_IKRig; Target = new IK Rig
3. Add Default Ops → audition in Asset Browser

### 4. Live Link (realtime motion capture)
```
// In MH Blueprint Details panel:
Live Link → Live Link Subject: [your MH subject]
Use Live Link: ✓ (checked)
```

### 5. Runtime Retargeting
- **Translation**: same animation asset on both characters; different body proportions auto-handled
- **Parent Skeletal Mesh**: paste target MH components under source Body; use Retarget Pose From Mesh node
- **Retarget Component** (experimental): add Retarget Component to target; set Source Skeletal Mesh

---

## Materials

| Material | LOD | Features |
|----------|-----|---------|
| `MI_Face_Skin_Baked_LOD0` | 0 | Full — subsurface, animated delta maps, micro-skin normals |
| `MI_Face_Skin_Baked_LOD1` | 1 | Micro-skin normals disabled |
| `MI_Face_Skin_Baked_LOD2` | 2 | Animated maps disabled |
| `MI_Face_Skin_Baked_LOD3` | 3 | Baked normal approximation |
| `MI_Face_Skin_Baked_LOD4+` | 4+ | UseSimpleShading (Default Lit) |
| `MI_Body_Baked` | all | Same base as face; animated maps off |

**Assembly pipelines:**
- **UE Cine**: 8K textures; full quality; ~800MB
- **UE Optimized High/Medium/Low**: baked textures; ~60MB at High

---

## Hair (Groom) Performance

```
// Force cards instead of strands globally (consoles/mobile):
r.HairStrands.UseCardsInsteadOfStrands 1

// Reduce hair sample count (quality vs performance):
r.HairStrands.Visibility.MSAA.SamplePerPixel 2  // default 4

// Disable ambient occlusion from sky light (if not needed):
r.HairStrands.SkyAO 0

// Mobile — force strand-less LOD:
r.HairStrands.MinLOD 3
```

---

## Mobile Configuration

```ini
[ConsoleVariables]
Compat.MAX_GPUSKIN_BONES=75    ; mobile GPU max

; Android/iOS device profile:
+CVars=r.EarlyZPass=3
+CVars=r.Mobile.EarlyZPassOnlyMaterialMasking=1
```

---

## UE 5.8 Additions `[5.8]`

| Feature | Status | Notes |
|---------|--------|-------|
| **MetaHuman Crowd** | Experimental | New plugin — optimized instanced MetaHumans at scale (tens → thousands); seamless LOD transitions; complement OverCrowd with this for ultra-large backgrounds |
| **Mesh to MetaHuman** | Improved | Single workflow converts arbitrary topology meshes to fully-rigged MetaHumans automatically (previously needed YVO3D + Faceform Wrap for custom body types) |
| **Unbaked Textures** | Production | Full control over MetaHuman textures without performance loss — override any texture layer directly |
| **MetaHuman Animator: Audio-Driven** | Production | Pass audio file only (no face capture session) → Animator generates facial curves; ideal with 11 Labs voice + no iPhone setup |
| **MetaHuman Animator: Monocular Body** | Production | Single-camera body capture directly in MetaHuman Animator; lower barrier than Move.AI for quick takes |
| **Batch Processing API** | Improved | Process large volumes of performance capture data end-to-end via API |
| **MetaHuman Animator: Linux/macOS** | New | Platform support expanded beyond Windows |

---

## Notes: What Nanite/Lumen Does/Doesn't Work With
- **Lumen GI**: works with MetaHumans ✓
- **Nanite**: does NOT work with skeletal meshes ✗ (MetaHumans are skeletal)
- **Path Tracing**: works; hair strands are ray-traced (higher cost)
