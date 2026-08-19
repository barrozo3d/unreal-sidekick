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
> UNMEASURABLE -- topic coverage 4 files. Verify against Epic docs.
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

# Audio & MetaSounds — Reference

**Source:** Epic Documentation (`tutorials/metasounds-in-unreal-engine.md` — 19 pages)  
**UE Version:** 5.0+ (MetaSounds); 5.8 adds Node Config, Templates, WASAPI

---

## What MetaSounds Is

MetaSounds is UE5's **node-based procedural audio DSP engine** — it replaces Sound Cues. Each MetaSound is its own audio rendering engine: renders asynchronously in parallel, sample-accurate timing (1/48000s resolution), independent rendering format per sound (sample rate, buffer size, channel count).

**Key difference from Sound Cues:** MetaSounds are a DSP graph that generates audio procedurally, not just triggers and plays pre-made audio files.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **MetaSound Source** | A sound source asset (plays audio in 3D or 2D space) |
| **MetaSound Patch** | Reusable sub-graph embedded in other MetaSounds |
| **Preset** | References a base graph with overridden inputs — avoids graph duplication |
| **Interface** | Defines inputs/outputs for a MetaSound (e.g., `UE.Source.OneShot` adds `On Play`, `On Finished`) |
| **Trigger** | Sample-accurate event signal — drives timing and state changes |
| **Wave Player node** | Plays audio files; supports loop, seek, sample-accurate concatenation, pitch modulation |

---

## MetaSound Editor

- **Open:** Content Browser → right-click asset → Edit / double-click
- **Play button:** Live preview with real-time parameter widgets (knobs/dials)
- **Output meter:** Real-time loudness on the graph output
- **In-graph widgets:** Knobs, sliders, buttons for live input parameter control
- **Audition menu** `[5.8]`: Preview per platform (Low/Medium/High pages)

### Standard node creation
Right-click → search node name, or drag a pin into empty space → search.

---

## Output Formats

Set in `Details panel → MetaSound Output Format`:
- **Mono** — default for spatialized/attenuated sources
- **Stereo** — for music, ambience, 2D sounds
- Remove `UE.Source.OneShot` interface for persistent (looping) sounds

---

## Key Nodes for Narrative/Cinematic Work

| Node | Use |
|------|-----|
| `Wave Player (Mono/Stereo)` | Play audio file; loop, seek, pitch, concatenation |
| `Random Get (WaveAsset:Array)` | Pick random variation from array |
| `Trigger Repeat` | Clock / BPM-driven pulse |
| `AD Envelope (Audio)` | Attack-decay shaping of a signal |
| `Stereo Delay` | Ping-pong reverb/delay |
| `Ladder Filter` | Low-pass filter for warmth/muffling |
| `Crossfade (Audio, N)` | Blend between N audio signals |
| `LFO` | Low frequency oscillator for modulation |
| `MIDI To Frequency` | Convert MIDI note number to Hz |
| `InterpTo` | Smoothly interpolate a value over time |
| `One-Pole Low Pass Filter` | Simple smoothing filter |
| `Map Range Clamped` | Remap a value range (e.g., pawn speed → gain) |
| `Execute Trigger Parameter` | Call a trigger input from Blueprint |
| `Set Float Parameter (Audio)` | Set a MetaSound float input from Blueprint |
| `Spawn Sound Attached` | Attach MetaSound to a component in world space |
| `Spawn Sound 2D` | Play MetaSound as non-spatialized 2D audio |

---

## Audio in Sequencer `[5.8]`

- **Audio track**: drag a Sound Wave or MetaSound Source asset onto a Sequencer track
- **Control Bus track** `[5.8]`: animate audio mix parameters over time on the timeline
- **Control Bus Mix track** `[5.8]`: snapshot-based mix automation
- **MRQ audio support** `[5.8]`: improved audio export in Movie Render Queue/Graph

### For dialogue in cinematics
1. Create Audio Component on MetaHuman Blueprint
2. Assign MetaSound Source with dialogue wave + OVR Lipsync sync
3. In Sequencer: add `Audio` track → reference the AudioComponent
4. Keyframe volume, pitch on the track; or use Control Bus Mix for scene-wide audio mix

---

## Blueprint Integration

```
Event BeginPlay
  → Spawn Sound Attached (Sound: YourMetaSound, AttachToComponent: CharacterMesh)
  → [Store AudioComponent reference]

[On event/trigger]
  → Execute Trigger Parameter (AudioComponent, InName: "DialogueLine")
  → Set Float Parameter (AudioComponent, InName: "EmotionIntensity", InFloat: 0.8)
```

---

## Presets

1. Right-click a MetaSound Source → **Create MetaSound Preset**
2. Override any input parameter in the preset without duplicating the graph
3. Changes to the base graph auto-propagate to all presets

---

## Graph Composition (MetaSound Patch)

- Create `MetaSound Patch` asset (not Source) for reusable sub-graphs
- Add as a node inside any MetaSound Source
- Useful for: reverb chains, dialogue processors, shared music stems

---

## MetaSound Pages (Experimental) `[5.8]`

Define quality tiers (Low/Medium/High) with different graphs or just different default input values. Platforms select the right page at cook time. Set via `Project Settings → Engine → MetaSounds → Pages`.

---

## Audio Insights `[5.8 — Production Ready]`

- `Window → Audio Insights`
- Loudness metering, signal flow visualization
- Live monitoring and event logging
- Useful for diagnosing dialogue clipping and mix issues

---

## Common Patterns for Cinematic Work

### Ambient atmosphere with player-reactive wind
```
On Play → Noise → LPF → Stereo Mixer
PawnSpeed (Float Input) → InterpTo → Gain modulation
→ Blueprint: Event Tick → Get Player Velocity → Map Range → Set Float Parameter "PawnSpeed"
```

### Dialogue trigger from Sequencer event track
1. Sequencer → **Event Track** → `+Event` at desired frame
2. Bind to Blueprint function: `PlayDialogueLine(LineID)` 
3. In Blueprint: `Execute Trigger Parameter` on Audio Component → MetaSound plays correct line

### Procedural music system (BPM-driven)
See `tutorials/metasounds-in-unreal-engine.md` → "Creating Procedural Music with MetaSounds" section.

---

## MetaSound Node Configuration (Experimental) `[5.8]`

- Dynamic interface configuration at runtime
- `Node Update Transform API` — change node behavior without rebuilding graph
- Enables runtime-authored audio systems

---

## Audio Subtitles (Beta) `[5.8]`

- `Window → Subtitles` or via Project Settings → Audio → Subtitles
- Per-platform overrides (mobile vs desktop)
- Level Sequence preview without PIE
- New Blueprint functions: `SetSubtitleEnabled`, `SetSubtitleLocale`

---

## Gotchas

| Problem | Fix |
|---------|-----|
| MetaSound not spatialized | Ensure `Attenuation Settings` is set on MetaSound Source |
| Dialogue out of sync in MRQ | Use MRQ audio export `[5.8]` — set audio track properly |
| `On Finished` not firing | Only present with `UE.Source.OneShot` interface — don't remove it for one-shot SFX |
| Persistent sound keeps playing | Remove `UE.Source.OneShot` interface for looping/ambient sounds |
| Parameter name mismatch | Input name in MetaSound graph must exactly match `InName` in Blueprint call |
| 44.1kHz vs 48kHz mismatch | Project Settings → Audio → `Audio Mix Sample Rate: 48000` |
