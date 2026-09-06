# Knowledge Gap To-Do List

Generated 2026-07-20 from a library-wide gap analysis (301 ingested tutorial
entries checked against SKILL.md scope + all references/*.md). Skill focus is
cinematics/real-time VFX/rendering, not gameplay/multiplayer programming —
gaps below were chosen within or adjacent to that focus and verified against
actual INDEX.md content before being listed, not guessed. Ingest with
`python ingest.py "[URL]"` from this directory, then run the mandatory
extraction pass (see SKILL.md).

## Pending

(none — the 6 items from the 2026-07-20 gap analysis are all ingested; see
Completed section below)

> ✅ **D4b target 3 re-measured 2026-08-31 — it was already done, in June.**
> The cross-skill plan carried "Epic docs → `unreal-sidekick`, for the thin
> topics B4 identified (lip-sync, nDisplay/ICVFX, MetaSounds, narrative
> blueprints)" as outstanding work. Measured against the 353 files as they stand,
> **three of the four were already covered — by Epic documentation pages ingested
> on 2026-06-12 and 2026-06-18, before this program began.**
>
> | B4 topic | Entries it is the **subject** of | Passing mentions | Verdict |
> |---|---|---|---|
> | lip-sync | **12** (incl. `lip-sync-in-unreal-engine.md`, Epic doc, 2026-06-18) | 24 | not a gap |
> | nDisplay / ICVFX | **2** (incl. `ndisplay-overview-for-unreal-engine.md`, Epic doc, 2026-06-12) | 22 | covered |
> | MetaSounds | **3** (incl. `metasounds-in-unreal-engine.md`, Epic doc, 2026-06-18) | 0 | covered |
> | narrative blueprints | **0** | 3 | **correctly zero — out of scope** |
>
> ⚠️ **The raw counts would have misled, in both directions.** A substring count
> gives lip-sync **36** and nDisplay **24**, which reads as healthy — but for
> nDisplay only **2** are entries about it; the other 22 are passing mentions
> ("not viewport, not MRQ, not nDisplay", people recalling work on an LED volume).
> Conversely narrative blueprints matches **3 files** and is really **zero**: the
> hits are `fpakprocessedreadrequest system`, and a camera plugin's
> "cross camera (over-the-shoulder **dialogue system**)". *Suspect the instrument
> before the data* — counted by whether the topic is the entry's **subject**
> (title / H1 / tags / headers) rather than by whether the string appears.
>
> 🔴 **Narrative blueprints is not a gap and should not be filled.** `SKILL.md`
> states under **Not in scope**: *"general gameplay/multiplayer programming and
> game-logic Blueprint patterns."* Dialogue systems, quest systems and narrative
> Blueprints are exactly that. **Zero coverage here is the design working, not a
> hole** — recorded so a future gap analysis does not "fix" it.
>
> `unreal-sidekick` holds **19 Epic Documentation entries** in total.

## Completed (ingested 2026-07-20)

- [x] **Unreal Insights / performance profiling** — zero dedicated entries for
  profiling render-heavy scenes; `#insights`/`#profiling` never appear as
  tutorial headers.
  Source: "Performance Profiling with Unreal Insights (Basics)"
  https://www.youtube.com/watch?v=etkLE6BEKoM
  -> `tutorials/performance-profiling-with-unreal-insights-basics-unreal-engine-4-unreal-engine-.md` (extraction_status: complete)

- [x] **Chaos Destruction FX (dedicated walkthrough)** — references/chaos-physics.md
  has synthesized notes but only 2 tangential tutorial mentions; no ingested
  video walks through fracture/destruction end-to-end.
  Source: "UE5 Series: Chaos Destruction | Complete Guide Part 1"
  https://www.youtube.com/watch?v=1DK46of-Syg
  -> `tutorials/ue5-series-chaos-destruction-complete-guide-part-1.md` (extraction_status: complete)

- [x] **Traditional Landscape sculpting & auto-material** — only the new
  UE5.8 Mesh Terrain system has a dedicated entry; classic Landscape
  sculpt/paint/auto-material workflow has zero dedicated headers.
  Source: Epic Developer Community Learning — "UE 5.7 Landscape Series: From Sculpting to Production-Ready Environments"
  https://dev.epicgames.com/community/learning/tutorials/x1pX/unreal-engine-5-7-landscape-series-from-sculpting-to-production-ready-environments
  -> `tutorials/unreal-engine-5-7-landscape-series-from-sculpting-to-production-ready-environments.md`
  ✅ **RESOLVED 2026-07-21 — this note was stale, corrected 2026-08-31.** It used
  to say the entry was `needs-review` because the page is an Angular SPA behind
  Cloudflare that defeated every headless fetch, and that "a human should open the
  page in a real browser". **That was done.** A later session opened it in a real
  browser (Claude in Chrome) and found the page is not text-only: it links a
  **YouTube playlist** of the actual episode recordings by *RamTechies*.
  Episodes 1 and 2 were then ingested properly, with real transcripts and frames:
  `tutorials/landscape-mode-basics-unreal-engine-57-part-1.md` and
  `tutorials/landscape-mode-unreal-engine-57-part-2.md`. The article entry is now
  `extraction_status: superseded-partial` and carries its own notice.
  ⚠️ The erroneous auto-resolution that pass produced — `resolve_epic_community_url`
  matching an unrelated paid-course trailer — was overwritten with a do-not-use
  notice at `tutorials/architectural-presentation-masterclass-unreal-engine-57.md`.
  ⏳ **Open, but not actionable: Episodes 3 (Landscape Materials) and 4 (Foliage)
  are still unpublished.** Playlist re-checked **2026-09-06**: still 2 videos
  (`IADB2OR8XCk`, `rxUsQRcq168`) — unchanged since the 08-31 check, seven weeks
  after the 07-21 one. Re-check the playlist and ingest them the same way
  when they appear — the article page will need another look then too, since its
  body likely lists them once added.
  Playlist: https://www.youtube.com/playlist?list=PLqw4sGRzmvyCs9F_hOSNeyUmFZ8xDBx6J

- [x] **Take Recorder for cinematic capture** — surfaces only twice as a
  side-mention inside Chaos Cloth and Backrooms tutorials, never as its own
  workflow.
  Source: "Unreal Engine 5.4: Take Recorder Driven Cinematics"
  https://www.youtube.com/watch?v=h2aL7jEg_xw
  -> `tutorials/unreal-engine-54-take-recoder-driven-cinematics.md` (extraction_status: complete)

- [x] **Advanced Sequencer — Subscenes/nested sequences** — zero dedicated
  entries on multi-shot Subscenes track organization despite
  references/sequencer-cinematics (or similar) existing as a general reference.
  Source: "Unreal Engine: Understanding Subscenes in Sequencer"
  https://www.youtube.com/watch?v=5pK6JmarYhM
  -> `tutorials/unreal-engine-understanding-subscenes-in-sequencer.md` (extraction_status: complete)

- [x] **Motion Matching for cinematic characters** — mentioned exactly once,
  in passing, inside a 162-page general animation reference; no dedicated
  tutorial, and framed for cinematics rather than gameplay.
  Source: "How to use 500+ Motion Matching Animations for Cinematics in Unreal Engine 5"
  https://www.youtube.com/watch?v=d_YyHUk_C-4
  -> `tutorials/how-to-use-500-motion-matching-animations-for-cinematics-in-unreal-engine-5.md` (extraction_status: complete)

## Completed (ingested 2026-07-20, session 2 — AI/audio/shader/UMG/large-scale-3D backlog)

- [x] **Large-scale 3D streaming (point cloud/photogrammetry/BIM)** — zero
  coverage of Cesium for Unreal, 3D Tiles, or BIM/IFC runtime streaming
  pipelines for AEC/digital-twin work.
  Source: Unreal Fest Chicago 2026 — "From Scan to Stream: Open Pipelines
  for Large-Scale 3D in Unreal Engine" (Arkoon, Carleton Immersive Media
  Studios)
  https://www.youtube.com/watch?v=5ehoHM-uzRQ
  Ingested as: `tutorials/from-scan-to-stream-open-pipelines-for-large-scale-3d-in-unreal-engine-unreal-fe.md`
  (note: source video had no per-sentence caption timestamps — yt-dlp
  captions fallback after a Whisper audio-download failure; frame timestamps
  were estimated from narrative flow rather than exact cues, still landed on
  strong illustrative frames)

- [x] **State Trees (AI/gameplay logic)** — no coverage of the State Tree
  plugin at all.
  Source: Ryan Laley — "Unreal Engine 5 Tutorial - State Trees Part 1:
  Overview"
  https://www.youtube.com/watch?v=MuWRxuz1bjE
  Ingested as: `tutorials/unreal-engine-5-tutorial---state-trees-part-1-overview.md`

- [x] **Behavior Trees / AI Perception / EQS** — no coverage of the classic
  AI stack (Behavior Tree, Blackboard, AI Perception, Environment Query
  System) despite it being foundational UE AI tooling.
  Source: Darklore Creations — "Understanding AI and Behavior Trees - The
  Ultimate Guide [UE5]"
  https://www.youtube.com/watch?v=-hXFCSxAYEI
  Ingested as: `tutorials/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5.md`

- [x] **MetaSounds** — `references/audio-metasounds.md` existed but zero
  ingested tutorials actually demonstrated building a MetaSound graph.
  Sources: Epic Games — "MetaSounds in UE5: From Miniguns to Music"
  https://www.youtube.com/watch?v=3230-FwCts0
  and Taken Grace — "UE5 Audio Beginner Tutorial Learn About Metasounds!"
  https://www.youtube.com/watch?v=0H7PiqIl0Io
  Ingested as: `tutorials/metasounds-in-ue5-from-miniguns-to-music-unreal-engine.md`
  and `tutorials/ue5-audio-beginner-tutorial-learn-about-metasounds.md`

- [x] **Material Editor input-vector / noise-hash shader fundamentals** — no
  tutorial covered dot-product/Fresnel/camera-vector masking or procedural
  noise-hash construction from first principles.
  Sources: Ben Cloward, "Shader Graph Basics" — Episode 9 "Input Vectors"
  https://www.youtube.com/watch?v=lrc-j7ub28U
  and Episode 35 "Random Noise"
  https://www.youtube.com/watch?v=5v6tvkb63XU
  Ingested as: `tutorials/input-vectors---shader-graph-basics---episode-9.md`
  and `tutorials/random-noise---shader-graph-basics---episode-35.md`
  (note: both episodes cover Unreal Material Editor AND Unity Shader Graph
  side by side — Unreal portion is primary/extracted in full, Unity noted
  for the node-name differences it calls out)

- [x] **UMG / widget UI** — no tutorial covered building HUD/UI with UMG at
  all.
  Source: EDUCBA (GameDev) — "Unreal Engine UMG Tutorial — Build HUD & UI
  Systems (Beginner to Pro Guide)"
  https://www.youtube.com/watch?v=cMPQ_W32VzI
  Ingested as: `tutorials/unreal-engine-umg-tutorial-build-hud-ui-systems-beginner-to-pro-guide.md`
  (note: source course is UE4-era; Canvas Panel/anchor/layout-panel concepts
  covered are unchanged in UE5 — flagged in the entry's UE Version field)

- [x] **Metal/PBR reflection-tailoff shading theory** — off-topic for this
  skill's Unreal scope (source video is demonstrated entirely in
  Blender/Cycles, not Unreal) but ingested per explicit request; kept as a
  renderer-agnostic materials-theory reference with a note on translating
  the technique to the Unreal Material Editor.
  Source: "Forgotten Metal Knowledge | Vray, Cycles, Arnold.." (Lucas)
  https://www.youtube.com/watch?v=uz8PIi3ELJg
  Ingested as: `tutorials/forgotten-metal-knowledge-vray-cycles-arnold.md`

## Ruled out (already covered — do not re-suggest)
PCG (Procedural Content Generation), World Partition, nDisplay/virtual
production, Movie Render Graph.
