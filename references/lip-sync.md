# Lip Sync in Unreal Engine — Reference

**UE Version:** OVR Lipsync plugin available for UE5; audio-driven jaw bone since UE4; `[5.8]` Audio-driven animation in MetaHuman Animator

---

## Overview of Lip Sync Options

| Method | Quality | Setup | Best for |
|--------|---------|-------|----------|
| **OVR Lipsync (Meta plugin)** | Good | Medium | Auto jaw drive from any audio file; phoneme-accurate |
| **MetaHuman Animator face cap** | Excellent | Requires iPhone + session | Dialogue capture with actor performance |
| **MetaHuman Animator audio-driven** `[5.8]` | Good | Audio file only | No face capture session needed |
| **Manual Sequencer keyframing** | Full control | Slow | Hero close-ups requiring precise artistry |
| **Jaw bone Blueprint driver** | Basic | Fast | Simple open/close without phoneme detail |

---

## OVR Lipsync Plugin

### What it does
Analyzes an audio file or real-time microphone input → drives MetaHuman **viseme morph targets** (phoneme-based mouth shapes) in real-time or offline.

### Installation
1. Download: `fab.com` or `developer.oculus.com/downloads/` → search "OVR Lipsync Unreal"
2. Extract to project `Plugins/` folder → restart UE
3. Enable in `Edit → Plugins → OVR Lipsync`

### Components
| Asset/Component | Purpose |
|----------------|---------|
| `OVR Lipsync` (Actor Component) | Attach to MetaHuman Blueprint; drives visemes |
| `OVR Lipsync Playback Actor` | Standalone actor for offline pre-baked lipsync |
| `UOVRLipSyncContextWrapper` | C++/Blueprint API for runtime control |

### Setup on MetaHuman
1. Open MetaHuman Blueprint (e.g., `BP_Manny_C`)
2. Add Component: `OVR Lipsync`
3. In Details panel:
   - `Sound`: assign your audio (Sound Wave or MetaSound Source)
   - `Smoothing`: 80–100 (prevents jitter)
   - `Jaw Bone`: assign jaw bone name (`FACIAL_C_JawRoot` for MetaHumans)
   - `Jaw Bias`: 0.1–0.3 (prevents over-open mouth)
4. In AnimBlueprint → pass viseme blend values to MetaHuman's facial morph targets

### Blueprint wiring pattern
```
Event BeginPlay
  → Start Lipsync (OVRLipsyncComponent, Sound: DialogueAudioFile)

// In Anim BP's AnimGraph:
Get OVR Lipsync Visemes (Component)
  → Map viseme weights to MetaHuman morph target slots:
    sil, PP, FF, TH, DD, kk, CH, SS, nn, RR, aa, E, ih, oh, ou
```

### Key settings
| Parameter | Description | Range |
|-----------|-------------|-------|
| `Smoothing` | Viseme transition smoothness | 0–100; use 80–100 for natural look |
| `Jaw Bias` | Minimum jaw-open value | 0.0–0.5; use 0.1–0.2 |
| `Gain` | Mouth movement amplitude | 1.0 default; reduce if overdoing |
| `Provider` | Offline or RT (realtime mic) | Use `Offline` for pre-rendered cinematics |

---

## MetaHuman Animator — Audio-Driven Mode `[5.8]`

New in UE 5.8: process a body performance without camera — audio alone drives facial animation.

### Setup
1. In MetaHuman Animator → `New Session → Audio-Driven`
2. Import audio file (WAV, 48kHz, dialogue only — no music/SFX)
3. Animator analyzes phonemes → generates MetaHuman face curves
4. Export as `.uasset` → use in Sequencer `Facial Animation` track as usual

**Limitation:** less expressive than iPhone face capture (no eyebrow, brow compress, lid tighten from performance) — best combined with a body cap from Move.AI.

---

## Jaw Bone Blueprint Driver (Simple Method)

For basic dialogue without phoneme accuracy — just jaw open/close:

```
// In MetaHuman AnimBlueprint → Event Graph:

Event Tick
  → Get Audio Volume (from Audio Component)   // 0.0 – 1.0 amplitude
  → Multiply (× 50.0)                         // Scale to jaw rotation degrees
  → Clamp (0, 40)
  → Set Bone Transform (Bone: FACIAL_C_JawRoot, Rotation: (0, Result, 0))
```

**Result:** jaw follows audio amplitude — very basic but zero setup cost.

---

## 11 Labs + OVR Lipsync Integration

The user's voice pipeline is: **single performer → 11 Labs voice morphing → OVR Lipsync → MetaHuman jaw**.

### Recommended workflow
1. Record dialogue performance (actor, single mic, 48kHz WAV)
2. Upload to 11 Labs → voice clone/morph → export as 48kHz WAV
3. Import to UE as Sound Wave asset
4. Attach OVR Lipsync to MetaHuman BP → assign the 11 Labs audio
5. In Sequencer: Audio track (for playback timing) + MetaHuman animation (from MetaHuman Animator face cap or audio-driven mode)
6. OVR Lipsync runs in real-time during Sequencer preview and during MRQ render

### Sync tip
OVR Lipsync analyzes audio at runtime during render. For frame-accurate lip sync in MRQ:
- Ensure `Fixed Frame Rate` is set in Project Settings (48fps or 24fps)
- Set MRQ frame rate to match
- Pre-bake OVR Lipsync output using `OVR Lipsync Playback Actor → Bake to Animation`

---

## Manual Lip Sync in Sequencer (Hero Shots)

For critical close-ups where phoneme detail matters most:

1. Import 11 Labs audio into Sequencer `Audio` track → listen to waveform
2. On MetaHuman's `Animation` track → add `Control Rig` layer
3. In Control Rig: create controls for `MouthOpen`, `JawForward`, phoneme morph targets
4. Scrub through audio → keyframe mouth shapes matching waveform peaks
5. Blend between: `sil` (closed), `aa`, `oh`, `oo`, `ee` (vowels), consonant shapes

### Key MetaHuman facial morph targets for lip sync
| Morph | Shape |
|-------|-------|
| `CTRL_expressions_jawOpen` | Jaw drop — main "open mouth" |
| `CTRL_expressions_mouthClose` | Lip seal (for M, B, P consonants) |
| `CTRL_expressions_lipStretchL/R` | Wide EE sound |
| `CTRL_expressions_lipPucker` | OO/W sound |
| `CTRL_expressions_mouthShrugUpper` | Lip curl for F/V |
| `CTRL_expressions_jawFwd` | Jaw protrusion for certain vowels |

---

## Audio Subtitles `[5.8 — Beta]`

Native subtitle system integrated with Sequencer and MetaSounds:
1. `Window → Subtitles Settings`
2. In Sound Wave asset → `Subtitles` array → add subtitle entries with `Time` and `Text`
3. In Sequencer: subtitle display is automatic when Audio track plays the Sound Wave
4. Per-platform override: different subtitle styles for mobile vs desktop
5. Blueprint functions: `SetSubtitleEnabled(bool)`, `SetSubtitleLocale(Locale)`

---

## Gotchas

| Problem | Fix |
|---------|-----|
| OVR Lipsync overdrivesmouth | Reduce `Gain` to 0.5–0.7; increase `Jaw Bias` |
| Lip sync desync in MRQ render | Pre-bake with `OVR Lipsync Playback Actor → Bake` before rendering |
| MetaHuman Animator audio mode misses consonants | Use iPhone face cap for consonant-heavy dialogue; audio-driven works best for vowel-heavy speech |
| 11 Labs audio too quiet for OVR analysis | Normalize audio to -3dBFS before importing to UE |
| Jaw clips through teeth | Set `Max Jaw Open` limit on OVR Lipsync component or add jaw collision in Physics Asset |
