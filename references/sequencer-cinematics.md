# Sequencer & Cinematics — Reference

Sequencer is Unreal Engine's non-linear cinematic editor.

## Core Concepts

| Term | Meaning |
|------|---------|
| **Level Sequence** | A cinematic asset — contains all tracks for a scene |
| **Master Sequence** | A Level Sequence that contains sub-sequences (shots) |
| **Shot Track** | Track in Master Sequence that references sub-sequences |
| **Cinematic Camera Actor** | Physically-based camera — the primary camera for cinematics |
| **Camera Cut Track** | Selects which camera is active at each moment |
| **Binding** | Link between a Sequencer track and an Actor in the level |

## Cine Camera Actor — Key Settings

```
Filmback
  ├── Sensor Width / Height  → physical film/sensor size (e.g. 36x24mm = Full Frame)
  └── Aspect Ratio           → derived from sensor

Lens Settings
  ├── Focal Length           → mm — lower = wider angle
  ├── Min/Max Focal Length   → zoom range
  └── Aperture (f-stop)      → depth of field — lower = shallower DOF

Focus Settings
  ├── Focus Method           → Manual / Tracking / Disable
  ├── Manual Focus Distance  → distance in cm
  └── Draw Debug Focus Plane → red plane for previewing focus in editor

Current Aperture → overrides lens aperture for current shot
Current Focal Length → overrides lens focal length for current shot
```

## Movie Render Queue (MRQ)

### Render Settings
| Setting | Recommendation for Cinematics |
|---------|------------------------------|
| Anti-Aliasing | Temporal (64+ samples) or Path Tracing |
| Samples Per Frame | 32-128 for temporal; 1 for path tracing (accumulation handles it) |
| Temporal Sample Count | 8-32 (motion blur quality) |
| Output Format | `.exr` (16-bit half) for comp pipeline; `.png` for delivery |
| Frame Rate | Match sequence FPS |
| Resolution | 2K/4K or sequence resolution |
| Warm Up Frames | 30-60 for physics/Niagara sims |
| Render Warm Up Count | Engine warm up ticks (30+ for sims) |

### MRQ Passes (for VFX compositing)
- **Beauty** (combined) — always
- **Cryptomatte** — object/material mattes
- **Object ID** — per-object color ID
- **Depth (Z)** — world-space depth for DOF in comp
- **Normals** — surface normals
- **Motion Vectors** — for motion blur in comp
- Enable via `Output → Add Output` in MRQ

## Sequencer Track Types

| Track | Purpose |
|-------|---------|
| Camera Cut | Activates cameras at timestamps |
| Transform | Keyframe actor position/rotation/scale |
| Property | Keyframe any UE property |
| Event | Trigger Blueprint events at specific frames |
| Audio | Play audio assets |
| Fade | Fade in/out |
| Niagara System | Control Niagara lifecycle and parameters |
| Material Parameter Collection | Animate material parameters globally |
| Level Visibility | Show/hide streaming levels per shot |
| Subscene | Embed one Level Sequence inside another |

## Common Cinematic Workflow

```
1. Create Level Sequence (Content Browser > Add > Level Sequence)
2. Open Sequencer (Window > Sequencer)
3. Add Cine Camera Actor to level → drag into Sequencer
4. Add Camera Cut track → assign camera
5. Keyframe transforms and properties
6. Set sequence duration (right-click timeline end)
7. Add to Movie Render Queue (Render button in Sequencer)
8. Configure MRQ settings → Render
```

## Focus Pulling in Sequencer
- Add `Current Focal Length` and `Current Aperture` property tracks
- For Focus Distance: `Focus Settings > Manual Focus Distance` property track
- Or use `Tracking Focus` with an actor binding for auto-follow

## Useful Console Variables for Cinematics
```
r.TemporalAA.Upsampling 1         -- enable TSR
r.MotionBlurQuality 4             -- max motion blur quality  
r.DepthOfFieldQuality 4           -- max DOF quality
r.ShadowQuality 5                 -- max shadow quality
t.MaxFPS 0                        -- uncap frame rate for rendering
showflag.MotionBlur 1             -- enable motion blur in viewport
```
