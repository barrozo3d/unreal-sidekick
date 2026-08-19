---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Materials & Shaders — Reference

## Material Types

| Type | Use case |
|------|----------|
| **Surface** | Standard opaque/translucent geometry |
| **Decal** | Project onto surfaces — bullet holes, blood, dirt |
| **Post Process** | Screen-space effects after scene renders |
| **UI** | HUD and widget materials |
| **Volume** | Volumetric fog/cloud materials |
| **Unlit** | No lighting — emissive-only, VFX sprites |
| **Substrate** | UE 5.3+ unified material model (replaces layered materials) |

## Blend Modes

| Mode | When to use |
|------|-------------|
| Opaque | Default — solid geometry |
| Masked | Two-state transparency (foliage, hair cards) — uses `Opacity Mask` |
| Translucent | Full transparency — glass, water, smoke |
| Additive | Add to background — fire, sparkles, glow |
| Modulate | Multiply background — tinting, shadow overlay |

## Shading Models

| Model | Use |
|-------|-----|
| Default Lit | Standard PBR — most geometry |
| Subsurface | Skin, wax, leaves — light scatters through material |
| Preintegrated Skin | Optimized subsurface for characters |
| Two Sided Foliage | Leaves with backside lighting |
| Hair | Physically-based hair shading (Marschner) |
| Cloth | Velvet, fabric sheen |
| Unlit | No shading — emissive only |
| Eye | Physically-based eye rendering |

## Core PBR Inputs

| Input | Range | Meaning |
|-------|-------|---------|
| Base Color | 0-1 (RGB) | Albedo — no lighting baked in |
| Metallic | 0 or 1 | 0 = dielectric, 1 = metal |
| Roughness | 0-1 | 0 = mirror, 1 = fully rough |
| Specular | 0-1 | Non-metal specular strength (0.5 = default, rarely change) |
| Normal | Tangent space | Surface detail normals |
| Emissive | 0-∞ (HDR) | Self-illumination — drives Lumen emissive GI |
| Opacity | 0-1 | Only for Translucent/Masked blend modes |
| Ambient Occlusion | 0-1 | Baked AO — multiplied with lighting |
| World Position Offset | Vector3 | Vertex displacement in world space |

## Key Material Nodes for VFX

```
Texture Sample        -- sample a texture (UV input optional)
TextureCoordinate     -- UV channel selection
Panner                -- animate UVs (pan texture)
Rotator               -- rotate UVs around a point
Time                  -- current game time (drives animation)
Sine / Cosine         -- oscillation (pulse effects)
Lerp                  -- blend between two values
Power                 -- sharpen gradient (used on masks)
Multiply / Add        -- combine values
Clamp                 -- limit output range 0-1
If                    -- conditional branch
VertexColor           -- read per-vertex color from mesh
ParticleColor         -- read Niagara particle color
DynamicParameter      -- receive 4 floats from Niagara
Fresnel               -- edge/rim effect
Noise                 -- procedural noise (Perlin, Voronoi, etc.)
DistanceToNearestSurface -- SDF distance (requires Distance Field)
CustomDepth           -- read depth of objects with Custom Depth enabled
SceneTexture          -- read GBuffer (normals, depth, etc.) in post-process
```

## HLSL Custom Node

For logic too complex for the node graph:

```hlsl
// Custom node settings:
// Output Type: CMOT Float 3 (or Float, Float 4, etc.)
// Input pins: add them in the Inputs list → reference as local variables

// Example: procedural noise
float2 uv = UV;  // UV is an input pin
float n = frac(sin(dot(uv, float2(127.1, 311.7))) * 43758.5453);
return float3(n, n, n);
```

## Material Instances

- Create from any material: right-click material → Create Material Instance
- Override `Scalar Parameters`, `Vector Parameters`, `Texture Parameters`
- Runtime changes: use `Dynamic Material Instance` (Blueprint: `Create Dynamic Material Instance`)

```
// Blueprint
UMaterialInstanceDynamic* DynMat = UMaterialInstanceDynamic::Create(BaseMaterial, this);
DynMat->SetScalarParameterValue("Intensity", 2.5f);
DynMat->SetVectorParameterValue("Color", FLinearColor::Red);
```

## Material Parameter Collections (MPC)

Global parameters accessible by all materials — drive multiple materials from one place.

```
Create: Content Browser → Materials → Material Parameter Collection
Add to material: MaterialParameterCollection node → select MPC → select parameter
Set from Blueprint: Get/Set Scalar/Vector Parameter Value on MPC asset
```

## Niagara → Material Communication

- **Dynamic Parameter** module in Niagara → reads in material via `DynamicParameter` node
- Inputs: 4 floats per channel (DynamicParameter.X/Y/Z/W)
- Example: drive opacity, scale, color tint from Niagara per-particle

## VFX Material Tips
- Use **Unlit + Additive** for fire, sparks, glow — no lighting calculation needed
- Use **Emissive** with high values (10-100) to make Lumen pick up the light
- **Masked Sprites** for hard-edged particle shapes (debris, leaves)
- **Translucent** for soft smoke, fog — order matters (no depth write by default)
- **Refraction** input on Translucent materials for glass/liquid distortion
