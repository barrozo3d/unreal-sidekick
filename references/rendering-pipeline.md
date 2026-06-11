# Rendering Pipeline — Reference

## Lumen (Global Illumination & Reflections)

Lumen is UE5's fully dynamic global illumination and reflections system.

### Hardware vs Software Lumen
| Mode | Quality | Cost | Requirements |
|------|---------|------|--------------|
| Software Lumen | Good | Medium GPU | Any DX11+ GPU |
| Hardware Ray Tracing Lumen | High | High GPU | DX12 + RTX/RDNA2 GPU |

### Key Settings (Project Settings > Rendering > Global Illumination)
```
Dynamic Global Illumination Method: Lumen
Reflection Method: Lumen
Lumen Scene Lighting Quality: 1-4 (1=fast, 4=best)
Lumen Scene Detail: controls capture range
Lumen Final Gather Quality: 1-4
Max Trace Distance: how far rays travel (cm)
```

### Lumen Console Variables
```
r.Lumen.TraceMeshSDFs 1                    -- use mesh SDFs (better quality)
r.Lumen.Reflections.Allow 1               -- enable Lumen reflections
r.Lumen.DiffuseIndirect.Allow 1           -- enable Lumen GI
r.RayTracing.GlobalIllumination 1         -- enable hardware RT GI
r.Lumen.ScreenProbeGather.ScreenTraces 1  -- screen-space traces for detail
```

---

## Nanite (Virtualized Geometry)

Nanite allows importing millions of polygons with minimal performance impact.

### When to Use Nanite
- High-poly assets (rocks, buildings, detailed props)
- Assets visible at many distances (no LOD needed manually)
- **NOT suitable for:** animated skeletal meshes, masked materials, runtime-generated meshes, translucent materials

### Enabling Nanite
- Static Mesh Editor → Nanite → Enable Nanite Support ✓
- Or bulk enable: select meshes in Content Browser → right-click → Nanite → Enable

### Nanite Console Variables
```
r.Nanite.MaxPixelsPerEdge 1.0    -- quality (lower = higher quality, more cost)
r.Nanite.Tessellation 1          -- enable displacement tessellation (UE 5.3+)
showflag.NaniteVisualization 1   -- visualize Nanite clusters in viewport
```

---

## Path Tracing

Full path-traced rendering in the viewport — offline quality for cinematics.

### Enabling Path Tracing
- Viewport > View Mode > Path Tracing
- Or: Post Process Volume → Rendering Features → Path Tracing

### MRQ with Path Tracing
```
Output Settings:
  Samples Per Pixel: 512-2048 (higher = less noise, slower)
  Max Bounces: 8-32
  Filter Width: 2.0 (reconstruction filter)
  
Post Process Volume:
  Path Tracing: Enabled
  Max Bounces: matches MRQ setting
```

### Path Tracing vs Lumen
| | Path Tracing | Lumen |
|---|---|---|
| Quality | Ground truth | Good approximation |
| Speed | Slow (offline) | Real-time |
| Use case | MRQ final renders | Preview / real-time |
| Emissives | Physically correct | May need adjustment |
| Glass/SSS | Accurate | Limited |

---

## TSR (Temporal Super Resolution)

UE5's built-in upscaling solution — renders at lower res, upscales to target.

```
r.TemporalAA.Upsampling 1        -- enable TSR (replaces TAA)
r.ScreenPercentage 67            -- render at 67%, upscale to 100% (perf boost)
r.TSR.History.ScreenPercentage 200  -- history buffer quality
```

---

## Post Process Volume — Key Settings for Cinematics

```
Exposure:
  Metering Mode: Manual (for cinematics — full control)
  Exposure Compensation: EV correction
  
Bloom:
  Method: Convolution (film-quality bloom)
  Intensity: 0.5-2.0
  
Color Grading:
  White Balance, Shadows/Midtones/Highlights wheels
  Crush Blacks, Filmic Tone Curve
  
Depth of Field:
  Method: Circle DOF (fast) or Bokeh DOF (cinematic)
  Focal Distance, Depth Blur F-Stop (control with Cine Camera instead)

Vignette Intensity: 0-1
Chromatic Aberration: 0-1 (subtle = 0.1-0.3)
Lens Flares: Intensity, Threshold
Film Grain: Intensity
```

---

## GPU Lightmass

For offline pre-baked lighting — higher quality than real-time Lumen for static scenes.

```
Enable: Project Settings > Rendering > Enable GPU Lightmass
Build: Build > Build Lighting Only (uses GPU)
Quality: GPU Lightmass Settings on WorldSettings actor
  GI Samples: 512-2048
  Stationary Sky Light Samples: 512
```

---

## Render Performance Tips for Cinematics
- Disable real-time in viewport during GPU Lightmass baking
- Use `r.ScreenPercentage 100` for final MRQ renders (don't upscale final output)
- Enable `High Quality Translucency Reflections` in Post Process Volume for glass/liquids
- Set `Shadow Quality` to max via `r.ShadowQuality 5` for offline renders
- Use `Cinematic Quality` scalability preset before MRQ render
