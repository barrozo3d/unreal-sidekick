# Solo Filmmaker Cinematics Pipeline

Full production pipeline for solo cinematic/narrative work in Unreal Engine 5. Each stage maps to the user's established tools. Use this as a reference when answering questions about "where something fits" in the workflow.

---

## Stage 0 — Pre-Production

**Goal:** storyboard → animatic → shot list → location scout (digital)

| Task | Tool |
|------|------|
| Storyboard / shot list | Paper / Canva / Storyboarder |
| Digital location scout | UE5 editor viewport, walk around FAB environments |
| Previz layout | Polycam scan → UE5 import → rough MetaHuman placement |
| Reference gather | OverCrowd early crowd placement, rough Niagara FX |

**Key settings:** Enable `Realtime` in viewport, set `Engine Scalability` to Medium for previz speed.

---

## Stage 1 — Environment Assembly

**Goal:** final environment ready for shooting

| Task | Tool |
|------|------|
| Base world | FAB marketplace environments (pre-lit preferred) |
| Procedural scatter / detail | Polygonflow Dash |
| Terrain | Landscape + Dash terrain tool |
| Lighting pass (rough) | Directional Light (Ctrl+L sun angle) + Exponential Height Fog |

**Version note:** `[UE5.6+]` Substrate materials are production-ready — FAB assets may use legacy or Substrate; check in Material Editor.

---

## Stage 2 — Character Pipeline

**Goal:** MetaHumans in costume, ready for animation

| Task | Tool |
|------|------|
| Base character | MetaHuman Creator → Blueprint Companion |
| Custom body/creature | YVO3D body gen → Faceform Wrap retopo → 2DNAX → MetaHuman |
| Wardrobe | FAB wardrobe packs (Polyphoria armor, etc.) rigged to MetaHuman skeleton |
| Voice/face prep | 11 Labs → audio file; OVR Lipsync → jaw bone drive |

**Gotcha:** Custom Metahuman creatures require a matching Physics Asset — duplicate from standard MetaHuman and adjust collision capsules for non-human proportions.

---

## Stage 3 — Performance Capture (Mocap)

**Goal:** all body and face performances captured and processed

### Body

| Scenario | Tool | Output |
|----------|------|--------|
| Multi-person, complex action | Move.AI Move Pro (6× GoPro 10, 4K60) | FBX per performer |
| Single performer, quick iteration | Move.AI Move One (single cam) | FBX |
| Budget / phone-based | QuickMagic AI (Android/phone) | FBX |
| AI video replacement | Kling 01 + Kling Elements | video composite |

### Face

| Scenario | Tool |
|----------|------|
| Dialogue + expression | iPhone + Rococo head rig → MetaHuman Animator |
| Budget face | QuickMagic AI (face cap mode) |

### Processing in UE

1. Import FBX → `Skeletal Mesh` panel → target skeleton: `metahuman_base_skel`
2. `IK Retargeter` → source: imported FBX rig → target: MetaHuman skeleton
3. In Sequencer: drag retargeted animation onto MetaHuman's `Animation` track
4. Face: MetaHuman Animator → export `.uasset` → `Facial Animation` track in Sequencer
5. Lip sync: OVR Lipsync asset → drive `Jaw_Open` morph target via Blueprint or Sequencer

**Version note:** `[UE5.5+]` Animation Layers allow non-destructive additive corrections on top of mocap — use for hand polish, idle breathing, root motion fixes.

---

## Stage 4 — Scene Assembly in Sequencer

**Goal:** all shots cut together, cameras set, full scene plays back correctly

### Sequence hierarchy (for multi-scene projects)
```
Master Sequence (L_Master.uasset)
  └── Shot_01 (sub-sequence, 1 Level per shot or shared level)
  └── Shot_02
  └── Shot_03
```

### Track order (standard)
1. `Director Track` — camera cuts
2. `Cine Camera Actor` track(s) — Black Eye Cameras or manual Cine Camera
3. MetaHuman tracks — one per character
4. Crowd tracks — OverCrowd spawn/despawn events
5. Niagara VFX tracks — emitter activation
6. Audio tracks — dialogue + ambience + SFX
7. `Event Track` — Blueprint triggers (explosions, door opens, lights flicker)
8. `Level Visibility` track — show/hide sub-levels for scene transitions

### Key settings
- `Evaluation Type`: `Always Re-evaluate` for physics-driven characters
- `When Finished`: `Keep State` for hero assets, `Restore State` for environmental props
- `Cinematic Quality` mode: enable via `Cinematic Viewport` overlay (hides HUD, locks camera)

---

## Stage 5 — Crowds

**Goal:** background population that matches scene scale

| Scale | Tool |
|-------|------|
| < 50 agents, hero behavior | OverCrowd plugin — full MetaHuman LOD, rig, behavior |
| 50–500 agents, background | OverCrowd + AnimToTexture LOD falloff |
| 500–5000+ agents, distant fills | Niagara crowd simulation (sprite/mesh particles with animated textures) |

**Workflow:**
1. OverCrowd Actor → assign MetaHuman + behavior preset
2. In Sequencer: keyframe crowd count, spawn region, animation blend weights
3. Far background: Niagara emitter using AnimToTexture-baked crowd flipbooks

---

## Stage 6 — Lighting

**Goal:** final cinematic lighting — PBL-based, scene-specific

| Light type | Use case |
|------------|----------|
| Directional Light | Sun/moon — adjust Ctrl+L for angle; Lumen HWRT for accurate shadows |
| Sky Light | HDR ambient fill; use `Real Time Capture` mode for indoor setups |
| Point / Spot / Rect Light | Practical lights (torches, lamps, screens) — use real-world lux/candela values |
| Exponential Height Fog | Atmospheric depth; combine with Volumetric Fog for god-rays |
| Post-Process Volume | Exposure (EV100), color grading (curves/LUT), Depth of Field, Bloom |

**PBL values (reference):**
- Overcast day exterior: EV 12–14
- Direct sunlight exterior: EV 14–16
- Interior natural light: EV 8–10
- Candlelit interior: EV 4–6

**Version note:** `[UE5.8+ prod-ready]` MegaLights — mass dynamic area lights with Lumen; now production-ready. Use for final renders with complex practical light setups. Was experimental in 5.5–5.7.

---

## Stage 7 — Rendering (Movie Render Graph)

**Goal:** high-quality EXR sequences per shot

### Quick setup `[UE5.6+ — Movie Render Graph]`

1. `Window → Movie Render Queue` → `+Job` → select Level Sequence
2. Switch to **Movie Render Graph** mode (top-right toggle)
3. Graph node chain:
   ```
   [Renderer: Path Tracer]
   → [Denoiser: NFOR / Intel Denoiser]
   → [Output: EXR Sequence (DWAA compression)]
   → [Output Settings: frame padding 4, output dir]
   ```
4. **Temporal samples:** 32–64 for finals, 8 for dailies
5. **Spatial samples:** 1 (Path Tracer handles convergence)
6. **Warmup frames:** 8 (prevents Lumen/shadow artifacts at frame 0)

### Multi-pass EXR (for DaVinci composite)
- Add `Render Pass` nodes: Beauty, Diffuse, Specular, AO, Depth (Z), Normals, Cryptomatte
- Enable `Accumulation DOF` `[UE5.8+]` for physically accurate bokeh on hair/groom

### Camera bug fix `[UE5.7]`
- Video textures (Media Player) desync with accumulation mode — set `Frame Open/Close` to exact frame boundary (0.0 / 1.0) in MRG Output Settings.

---

## Stage 8 — Composite (DaVinci Resolve + Fusion)

**Goal:** EXR sequences → final grade → delivery

| Step | Tool |
|------|------|
| Import EXR sequences | DaVinci Media Pool → EXR timeline (32-bit float) |
| Color space | Input: Linear sRGB (matches UE output) → timeline: ACEScct or DaVinci Wide Gamut |
| Green screen integration | Fusion: keyer → Color Space Transform (camera native → Linear sRGB) → Composure utility pass |
| Edge wrap (if using Composure) | UE: Scene Capture 2D → Render Target → plate material multiply |
| Grade | Color page: wheels + curves + Power Windows |
| Delivery | Rec.709 H.264/H.265 or DCI-P3 ProRes for cinema |

**OCIO setup `[UE5.X]`:**
- Edit → Project Settings → Color Management → enable OCIO
- Assign the same OCIO config used in DaVinci for frame-accurate preview in UE viewport
- Use the `OCIO Display` post-process material to preview final grade inside Sequencer

---

## Common Gotchas

| Problem | Cause | Fix |
|---------|-------|-----|
| MetaHuman T-poses at sequence start | IK Retargeter not baked | Bake retarget to new anim asset before Sequencer use |
| Crowds disappear in MRQ render | OverCrowd not flagged as cinematic-visible | Enable `Cast Shadow` + `Render in Main Pass` on OverCrowd component |
| Path Tracer flicker on glass | Insufficient samples | Increase to 64+ spatial samples or use Denoiser |
| DaVinci EXR looks blown out | Wrong color space on import | Set Input Color Space to `Linear sRGB`, not `Rec.709` |
| Sequencer audio out of sync | 48kHz vs 44.1kHz mismatch | Project Settings → Audio → set to 48000Hz; export from 11 Labs at 48kHz |
| Lip sync jaw overdrive | OVR Lipsync gain too high | Reduce `Jaw Bias` and `Smoothing` in OVR Lipsync component settings |
