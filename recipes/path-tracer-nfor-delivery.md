# Recipe: Path Tracer + NFOR Delivery Pipeline

**Goal:** Set up Unreal's Path Tracer with the NFOR ML denoiser in MRQ for clean, ground-truth renders suitable for final delivery.  
**UE Systems:** Path Tracer, NFOR, Movie Render Queue, Post Process Volume  
**Difficulty:** Advanced

---

## Overview

Path Tracing in UE5 gives physically-accurate, reference-quality renders. Combined with the NFOR (Non-local Filtering with Optimal Regression) denoiser, you get clean output at 256–512 spp instead of the 2048+ spp needed without denoising.

Pipeline summary:
```
Sequencer shot → MRQ (Path Tracer pass + NFOR) → EXR → Grade → Deliver
```

---

## 1. Enable Path Tracer

### In Editor (preview)
1. **Viewport → Show → Path Tracing** — or type `r.PathTracing 1` in the console
2. The viewport accumulates samples in real time (lower right shows sample count)
3. Path Tracing overrides Lumen, TSR, and all real-time approximations

### CVars for interactive preview:
```ini
r.PathTracing 1
r.PathTracing.SamplesPerPixel 16     # Low for fast preview
r.PathTracing.MaxBounces 8
r.PathTracing.MaxRaymarchVolumeShadowSamples 8
```

### Lighting compatibility notes:
- **Works:** Directional Light, Point Light, Rect Light, Spot Light, Sky Light, Emissive materials, IES profiles
- **Does NOT work:** Dynamic Lumen GI (Path Tracer has its own GI), reflection captures (replaced by PT reflections), TSR (Path Tracer accumulates natively)
- **Sky Atmosphere:** works, but verify sky light captures the HDRI correctly

---

## 2. Configure the Scene for Path Tracing

### Post Process Volume — Path Tracing Settings

In your Post Process Volume (or Camera Post Process):

| Setting | Value | Notes |
|---------|-------|-------|
| `Path Tracing → Max Bounces` | 16–32 | 8 = fast, 32 = full caustics |
| `Path Tracing → Samples Per Pixel` | 256–512 (MRQ renders accumulate) | Viewport only — MRQ ignores this |
| `Path Tracing → Max Path Exposure` | 16.0 | Clamp fireflies — lower if bright spots appear |
| `Path Tracing → Enable Reference DOF` | ON | Bokeh-accurate DOF (slower) |
| `Path Tracing → Enable Denoiser` | OFF | Let MRQ NFOR handle denoising |
| `Path Tracing → Enable Emissive Materials` | ON | Emissive surfaces as area lights |

### Camera Settings for Reference Renders

Use a Cine Camera Actor:
- Set real-world focal length (e.g., 50mm, 85mm)
- Set aperture (f/stop) for DOF (e.g., f/1.8 for shallow DOF)
- **Film Format** (sensor size): `Full Frame 35mm` = 36×24mm → affects FOV and DOF
- `Min FStop` and `Current Aperture`: match real lens behavior
- `Focus Settings → Focus Method`: `Manual Focus Distance` or `Track Focus (Actor)`

---

## 3. MRQ — Path Tracer Pass Configuration

### Add Path Tracer Pass

In MRQ Job Settings → `+` → **Path Tracer**:

| Setting | Value | Notes |
|---------|-------|-------|
| `Reference Motion Blur` | ON | Accurate motion blur (stochastic sampling per frame) |
| `Enable Denoiser` | ON → `NFOR` | ML denoiser — see Section 4 |
| `Samples Per Pixel` | 256 | MRQ overrides the PPV value |

### Anti-Aliasing Settings (for Path Tracer)

Path Tracer does not use temporal anti-aliasing. Configure:

| Setting | Value |
|---------|-------|
| `Temporal Sample Count` | **1** | PT accumulates per-sample internally |
| `Spatial Sample Count` | **1** |
| `Override Anti-Aliasing` | ON → `None` |
| `Render Warm Up Count` | **0** | PT doesn't need warm-up |

---

## 4. NFOR Denoiser

NFOR (Non-local Filtering with Optimal Regression) is an ML denoiser that runs per-frame, not per-sample. It requires AOV feature buffers to denoise accurately.

### Enable in MRQ

In Path Tracer pass settings:
- `Denoiser` → **NFOR**

NFOR automatically uses Albedo, Normal, and Depth buffers as features. No manual AOV setup needed.

### NFOR Quality vs Speed

| `Samples Per Pixel` | Quality | ~Render Time (per frame, RTX 5070) |
|--------------------|---------|------------------------------------|
| 64 spp | Good for motion, some grain | ~30s |
| 256 spp | Excellent for statics | ~2 min |
| 512 spp | Reference quality | ~4 min |
| 1024 spp | Ground truth | ~8 min |

NFOR takes ~10–30 seconds per frame post-render (CPU denoising).

### NFOR Limitations
- Can smear fine detail (hair, fabric threads) — increase spp if this occurs
- Does not work across frames (each frame is denoised independently)
- Requires CUDA-capable GPU for GPU denoising (falls back to CPU)

---

## 5. Console Variables for MRQ Path Tracer

Add `Console Variables` setting in MRQ job:

```ini
# Core PT settings
r.PathTracing.MaxBounces 32
r.PathTracing.SamplesPerPixel 256
r.PathTracing.MaxPathExposure 16.0
r.PathTracing.EnableEmissive 1
r.PathTracing.EnableReferenceDOF 1

# Environment / Sky
r.PathTracing.VisibleLights 1           # Direct light sampling
r.PathTracing.SkyLight.BatchSize 16

# Performance
r.PathTracing.GPUCount 1                # Use 1 GPU (set to 2+ for multi-GPU)
r.PathTracing.AdaptiveSampling 0        # Uniform sampling for compositing consistency

# Disable conflicting features
r.Lumen.Reflections.ScreenTraces 0
r.DynamicGlobalIlluminationMethod 0     # Disable Lumen
r.ReflectionMethod 0                    # Disable Lumen reflections
```

---

## 6. Output: EXR + Color Space

### For ACES/ACEScg Delivery

MRQ Output settings:
- `Color Output` → `ACEScg` (Linear, wide gamut)
- Disable tonemapper overrides in the PPV for clean linear output
- `Bit Depth`: 32-bit float EXR

### For Rec.709 / sRGB Delivery

- Keep default UE tonemapping active
- `Color Output` → `sRGB (Gamma 2.2)`
- `Bit Depth`: 16-bit half-float EXR (sufficient for display-referred)

### File Naming for VFX Pipeline

```
{project}/Renders/{shot}/pt_v{version}/{shot}_{frame}.exr
```

---

## 7. Delivery Specs Checklist

| Spec | Value |
|------|-------|
| Format | EXR sequence (16-bit half or 32-bit float) |
| Color space | ACEScg (comp) or sRGB (client direct) |
| Frame rate | Match project (24, 25, 29.97, or 30 fps) |
| Resolution | 1920×1080 min; 3840×2160 for VFX shots |
| Head/tail handles | +/- 10 frames beyond cut points |
| Naming | Shot_v001_####.exr (4+ digit frame numbers) |

---

## 8. Troubleshooting

| Problem | Fix |
|---------|-----|
| Fireflies (bright spots) | Lower `Max Path Exposure` to 8.0 or 4.0 |
| Caustics missing | Enable `Enable Caustics` in PT settings; increase bounces to 32+ |
| NFOR smears hair/detail | Increase spp to 512; or disable NFOR and use Optix |
| DOF looks wrong | Enable `Reference DOF`; check aperture is not f/22 or too closed |
| Sky is too dark | Check Sky Light → Real Time Capture is ON; verify HDRI exposure |
| Render is too slow | Reduce bounces to 8; use 64 spp + NFOR; reduce resolution and upscale |
| Motion blur artifacts | Enable `Reference Motion Blur`; check temporal sample = 1 |

---

## References
- `references/rendering-pipeline.md` — Path Tracing CVars, NFOR, settings table
- `recipes/mrq-multipass-exr.md` — Full MRQ pass configuration
- Tutorial: `tutorials/designing-visuals-rendering-and-graphics-with-unreal-engine.md` — Path Tracer + NFOR denoiser section
