# Recipe: Blender → Unreal Engine 5 Pipeline

**Goal:** Move geometry, materials, and animations from Blender to UE5 cleanly — correct scale, normals, UVs, and PBR materials.  
**UE Systems:** Static Mesh Importer, Skeletal Mesh Importer, Material Editor, Nanite  
**Difficulty:** Intermediate

---

## Overview

The Blender → UE pipeline has two main paths:
- **Static Mesh** — props, environments, hard-surface assets
- **Skeletal Mesh** — characters, animated assets with bones

UE uses centimeters (1 UE unit = 1 cm). Blender uses meters by default. Always apply scale before export.

---

## 1. Blender — Mesh Preparation

### Scale and Transforms
- Model at real-world scale in Blender (e.g., a door is ~2 m tall)
- Before export: **Object → Apply → All Transforms** (`Ctrl+A → All Transforms`)
- This bakes scale, rotation, and location into the mesh data

### Topology Requirements
- No N-gons in deforming geometry (quads preferred, triangles OK for hard-surface)
- For Nanite: triangulate on export (UE does this automatically, but explicit is cleaner)
- Remove doubles: **Mesh → Merge by Distance**
- Fix normals: **Mesh → Normals → Recalculate Outside**

### UV Unwrapping
- Every mesh needs a clean **UV Channel 0** (main textures)
- For lightmaps (if using baked lighting): add **UV Channel 1** with no overlaps
- Use **Smart UV Project** for hard-surface, manual unwrap for hero assets
- Leave 2-4 px padding between UV islands for 2048+ textures

### Normal Map Baking (optional, for LOD baking)
```
Render Properties → Render Engine: Cycles
Bake Type: Normal
Space: Tangent
Selected to Active: ON (highpoly → lowpoly)
Margin: 4px
Output: 16-bit PNG, sRGB OFF (normal maps are not sRGB)
```

---

## 2. Blender — FBX Export Settings

**File → Export → FBX (.fbx)**

| Setting | Value | Why |
|---------|-------|-----|
| Scale | 1.0 | Scale already applied to mesh |
| Apply Scalings | FBX Units Scale | Handles Blender-to-UE unit conversion |
| Forward | -Z Forward | UE uses +X forward, -Z aligns correctly |
| Up | Y Up | UE uses Z up, Y aligns correctly |
| Apply Unit | ON | Bakes Blender units into FBX |
| Triangulate Faces | ON (optional) | Explicit triangulation, consistent results |
| Tangent Space | ON | Required for correct normal map rendering |
| Smoothing | Edge (hard-surface) or Face (organic) | Controls how normals are interpreted |
| Armature | ON (skeletal mesh only) | Exports bones |
| Leaf Bones | OFF | UE doesn't use Blender leaf bones |
| Bake Animation | ON (animated assets) | Embeds keyframes |

**Tip:** Use a dedicated FBX export preset to avoid re-setting these every time.

---

## 3. UE — Import Settings

### Static Mesh Import

**Import dialog:**

| Setting | Value | Notes |
|---------|-------|-------|
| Auto Generate Collision | OFF (manual) or ON (quick) | Manual = convex decomposition later |
| Generate Lightmap UVs | ON (if using baked lighting) | Creates UV Channel 1 automatically |
| Import Materials | OFF | Create materials manually in UE |
| Import Textures | ON (if textures embedded) | |
| Normal Import Method | Import Normals | Trusts Blender's exported normals |
| Combine Meshes | OFF (usually) | Keep separate for LOD management |
| Transform Offset Roll | 0° | Leave at default unless mesh is rotated wrong |

### Skeletal Mesh Import

Additional settings:

| Setting | Value | Notes |
|---------|-------|-------|
| Create Physics Asset | ON | Auto-generates ragdoll collision |
| Import Animations | ON | Imports embedded animation clips |
| Animation Length | Exported Time | Full clip |
| Convert Scene | ON | Handles coordinate system |

### Verifying the Import
- Check scale in viewport: humanoid characters should be ~180 cm tall
- Check normals: `Show → Normals` in Static Mesh Editor
- If the mesh appears inside-out: reverse the import normal setting, or flip normals in Blender

---

## 4. UE — Enable Nanite (Static Meshes)

Nanite is the best choice for any high-polygon static mesh asset.

1. Open the Static Mesh asset
2. **Details panel → Nanite Settings → Enable Nanite ✓**
3. Set **Fallback Relative Error** to `0.1` (start here, lower = more detail in fallback)
4. Click **Apply Changes**

**When to NOT use Nanite:**
- Meshes with complex materials (World Position Offset, Pixel Depth Offset, opacity masks)
- Meshes that deform (use Skeletal Mesh)
- Two-sided foliage (limited support, test carefully)
- Spline meshes

---

## 5. UE — Material Setup

### PBR Material from Blender textures

Create a Material in UE:
1. `Content Browser → right-click → Material`
2. Connect texture samples to the appropriate inputs:

| Blender Output | UE Material Input | Texture Settings |
|---------------|-------------------|-----------------|
| Albedo/Base Color | `Base Color` | sRGB = ON, Compression = Default |
| Roughness | `Roughness` | sRGB = OFF, Compression = Masks |
| Metallic | `Metallic` | sRGB = OFF, Compression = Masks |
| Normal Map | `Normal` | sRGB = OFF, Compression = Normalmap |
| AO | `Ambient Occlusion` | sRGB = OFF, Compression = Masks |
| Emission | `Emissive Color` | sRGB = ON, Compression = Default |

**Pack textures** for efficiency: combine R=AO, G=Roughness, B=Metallic into one `ORM` texture → connect to all three inputs via R/G/B extract nodes.

### Material Instance for variation
1. Right-click Material → `Create Material Instance`
2. Expose parameters with `Ctrl+click` on value nodes
3. Use instances for all placed assets — never modify the parent directly

---

## 6. Common Issues & Fixes

| Problem | Fix |
|---------|-----|
| Mesh is 100× too large | Didn't apply scale in Blender before export |
| Mesh is rotated 90° | Add `-90° X rotation` in UE import dialog, or fix in Blender |
| Black/inverted normals | Toggle `Two Sided` in material, or recalculate normals in Blender |
| Seams visible on normal map | Increase UV island padding; check that tangent space matches |
| Animation plays at wrong speed | Frame rate mismatch — set Blender to 30fps or match UE project FPS |
| Skeleton does not match | Ensure bone names are identical if retargeting; use UE IK Retargeter |

---

## References
- `references/rendering-pipeline.md` — Nanite details and settings
- `references/materials-shaders.md` — Material Editor, PBR, instances
- Epic Docs: `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Skeletal mesh import, IK Retargeter
