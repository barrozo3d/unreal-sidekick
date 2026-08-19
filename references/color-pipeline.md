---
class: topic-reference
verified: partial
sources:
  - tutorials/  (corroboration audit, batch B4 -- see note)
last_verified: 2026-08-19
version_basis: "unknown"
# Origin: model memory. Audited 2026-08-19 (batch B4) -- no fabricated names
# found. Parameters/API symbols remain unverified. Tutorial beats reference.
---
> ## Audit note — batch B4, 2026-08-19
>
> CLEAN. First read 40%; all 8 flags were UI paths (`Bloom -> Intensity`) whose components are well corroborated. Real score 15%.
>
> **Method and its ceiling.** Every term this file asserts was checked against the
> skill's 362 ingested tutorials with `audit_references.py`. That corpus is built
> from spoken narration, so it corroborates what presenters **say** — node and
> tool names — and structurally cannot corroborate what they only **show or
> type**: parameter names, default values, console variables, API symbols.
> **Corroboration finds fabricated names, not wrong values.** Treat parameters and
> code identifiers in this file as unverified until checked against Epic's docs.
>
> Across all of `unreal-sidekick`, the audit found **no fabricated node names**.
> Full detail: `houdini-wand/PROMO_ENTRY_CLEANUP_PLAN.md` (workstream B).

# Color Pipeline — Reference (OCIO, ACES, Grading)

**Source:** Epic Documentation + synthesis  
**UE Version:** OCIO support since 5.0; Color Management settings in Project Settings

---

## UE5 Internal Color Space

UE5 works in **Linear sRGB** internally:
- All lighting, materials, and Lumen operate in linear light
- The viewport applies a **tonemapper** (by default ACES) for display
- MRQ / Movie Render Graph outputs in linear (EXR) unless you override

**Why it matters for DaVinci:** EXR sequences exported from UE are in Linear sRGB. Import them as `Linear sRGB` in DaVinci, not Rec.709 — or the image will look blown-out.

---

## Project Color Settings

`Edit → Project Settings → Engine → Rendering → Default Settings`:

| Setting | Recommended for Cinematics |
|---------|---------------------------|
| `Rendering Color Space` | sRGB |
| `Enable Alpha Channel Support` | Enabled (for compositing) |
| `Default Post Process Settings` | Filmic tonemapper (ACES default) |

---

## OCIO (Open Color IO) Integration `[5.0+]`

OCIO lets you use the **same color transforms in UE as in DaVinci Resolve/Nuke**, ensuring your viewport preview matches your grade.

### Setup
1. Install the OCIO plugin: `Edit → Plugins → search "OpenColorIO" → Enable`
2. Create an `OpenColorIO Configuration` asset in Content Browser
3. Point it to your `.ocio` config file (e.g., ACES CG config, or DaVinci's ACES config)
4. Assign it to your Post Process Volume or viewport:
   - Post Process Volume → `Color Grading → OCIO → OpenColorIO Configuration`
   - Set `Source Color Space` (UE linear = `Linear sRGB` or `ACEScg`)
   - Set `Destination Color Space` (your display = `Rec.709` or `sRGB`)

### Matching DaVinci Resolve workflow
1. Export your OCIO config from DaVinci (or use the same shared config file)
2. In UE: PostProcessVolume → OCIO → same config + same Source/Dest transforms
3. Result: UE viewport and DaVinci Color page show the same grade preview

### Common OCIO configs
- **ACES CG** → most standard for film; Source: `ACEScg`, Display: `sRGB`
- **DaVinci Wide Gamut / DaVinci Intermediate** → if your DaVinci is set to this color science
- **Filmic Blender** → compatible if coming from Blender pipeline

---

## Post Process Volume — Color Grading

Add to every cinematic scene. `Place Actors → Post Process Volume` → check `Infinite Extent`.

### Key color grading parameters

| Parameter | Description |
|-----------|-------------|
| `Exposure → Exposure Compensation` | EV bias — fine-tune overall brightness |
| `Exposure → Min/Max Brightness` | Clamp auto-exposure range |
| `Bloom → Intensity` | Glow around highlights |
| `Chromatic Aberration → Intensity` | Lens fringing for realism |
| `Vignette → Intensity` | Edge darkening |
| `Grain → Intensity / Size` | Film grain |
| `Color Grading → Global → Saturation` | Overall saturation |
| `Color Grading → Global → Contrast` | Lift/gamma/gain style contrast |
| `Color Grading → Shadows/Midtones/Highlights` | Three-way color wheels |
| `Color Grading → LUT` | Apply a texture LUT (import as `.cube` → UE LUT Texture) |
| `Film → Toe / Shoulder / Black Clip / White Clip` | ACES tonemapper curve controls |

### Applying a LUT
1. Export a `.cube` LUT from DaVinci (or Photoshop/Resolve)
2. In UE: `Content Browser → Import → select .cube → creates Texture 2D LUT`
3. Post Process Volume → `Color Grading → Misc → LUT Texture → [your LUT]`
4. `LUT Intensity`: 0 = no LUT, 1 = full LUT

---

## Per-Shot Color Grading in Sequencer

For narrative work with different looks per scene:
1. Place multiple Post Process Volumes in the level (one per scene/location)
2. In Sequencer → `Level Visibility` track: show/hide volumes per shot
3. Or use **Sequencer Camera Cut** — each cut can blend to a different PPV

### Better approach: Post Process Actor per shot
1. Create Blueprint Actor with Post Process Volume component
2. In Sequencer → bind track to that Blueprint Actor
3. Keyframe `Blend Weight` (0→1) for gradual look changes within a shot

---

## Movie Render Graph — Color Output `[5.6+]`

### EXR export settings
- **Output format**: EXR `DWAA` compression (half-float, good quality/size balance)
- **Color space**: Linear sRGB (matches UE internal)
- **Disable tonemapper** in MRG for raw linear output (recommended for compositing)

### Disabling the tonemapper for EXR
In Movie Render Graph → `Renderer node → Post Process Settings`:
- `Override Tonemapper → None` (or use a custom PP Material that bypasses it)
- Then apply grade in DaVinci on the linear EXR

### Multi-pass for color grading flexibility
Render these passes separately and grade in DaVinci:
- `Beauty` (combined)
- `Diffuse Color` + `Specular` (for per-channel grade)
- `Depth (Z)` (for DOF in comp, independent of UE DOF)
- `AO` (ambient occlusion for grading)
- `Cryptomatte` (object isolation masks)

---

## DaVinci Resolve Handoff

### Correct import workflow
1. Import EXR sequences → Media Pool
2. Set timeline to 32-bit float
3. Right-click clip → `Clip Attributes → Input Color Space: Linear sRGB`
4. Timeline color science: `DaVinci Wide Gamut / DaVinci Intermediate` or `ACEScct`
5. Output transform: Rec.709 (for SDR delivery) or P3-D65 (for cinema)

### If using OCIO in both UE and DaVinci
1. Both use same OCIO config file (shared folder)
2. UE input: `Linear sRGB` → output: `ACEScg` (grade in ACES space)
3. DaVinci input: `ACEScg` → grade → output: `Rec.709` for delivery

---

## Common Color Issues & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| EXR looks blown out in DaVinci | Wrong input color space | Set clip input to `Linear sRGB` in DaVinci |
| Viewport doesn't match DaVinci grade | No OCIO sync | Set up matching OCIO config in both apps |
| LUT looks different between UE and DaVinci | Tonemapper applied before LUT in UE | Disable tonemapper in MRG for raw output; apply LUT only in DaVinci |
| Skin tones too orange after grading | Over-saturated MetaHuman texture | Reduce `Color Grading → Global → Saturation` in PPV; or paint MetaHuman texture layer |
| HDR sky looks flat after export | Auto-exposure baked in | Use fixed exposure (disable Auto-Exposure in PPV) for cinematic control |
| Metallic assets look grey in comp | Missing specular pass | Enable `Specular` render pass in MRG |
