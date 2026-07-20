# Knowledge Gap To-Do List

Generated 2026-07-20 from a library-wide gap analysis (301 ingested tutorial
entries checked against SKILL.md scope + all references/*.md). Skill focus is
cinematics/real-time VFX/rendering, not gameplay/multiplayer programming —
gaps below were chosen within or adjacent to that focus and verified against
actual INDEX.md content before being listed, not guessed. Ingest with
`python ingest.py "[URL]"` from this directory, then run the mandatory
extraction pass (see SKILL.md).

## Pending

- [ ] **Unreal Insights / performance profiling** — zero dedicated entries for
  profiling render-heavy scenes; `#insights`/`#profiling` never appear as
  tutorial headers.
  Source: "Performance Profiling with Unreal Insights (Basics)"
  https://www.youtube.com/watch?v=etkLE6BEKoM

- [ ] **Chaos Destruction FX (dedicated walkthrough)** — references/chaos-physics.md
  has synthesized notes but only 2 tangential tutorial mentions; no ingested
  video walks through fracture/destruction end-to-end.
  Source: "UE5 Series: Chaos Destruction | Complete Guide Part 1"
  https://www.youtube.com/watch?v=1DK46of-Syg

- [ ] **Traditional Landscape sculpting & auto-material** — only the new
  UE5.8 Mesh Terrain system has a dedicated entry; classic Landscape
  sculpt/paint/auto-material workflow has zero dedicated headers.
  Source: Epic Developer Community Learning — "UE 5.7 Landscape Series: From Sculpting to Production-Ready Environments"
  https://dev.epicgames.com/community/learning/tutorials/x1pX/unreal-engine-5-7-landscape-series-from-sculpting-to-production-ready-environments

- [ ] **Take Recorder for cinematic capture** — surfaces only twice as a
  side-mention inside Chaos Cloth and Backrooms tutorials, never as its own
  workflow.
  Source: "Unreal Engine 5.4: Take Recorder Driven Cinematics"
  https://www.youtube.com/watch?v=h2aL7jEg_xw

- [ ] **Advanced Sequencer — Subscenes/nested sequences** — zero dedicated
  entries on multi-shot Subscenes track organization despite
  references/sequencer-cinematics (or similar) existing as a general reference.
  Source: "Unreal Engine: Understanding Subscenes in Sequencer"
  https://www.youtube.com/watch?v=5pK6JmarYhM

- [ ] **Motion Matching for cinematic characters** — mentioned exactly once,
  in passing, inside a 162-page general animation reference; no dedicated
  tutorial, and framed for cinematics rather than gameplay.
  Source: "How to use 500+ Motion Matching Animations for Cinematics in Unreal Engine 5"
  https://www.youtube.com/watch?v=d_YyHUk_C-4

Note: YouTube channel names for the 5 non-Epic sources above could not be
confirmed via fetch (JS-rendered pages return only title/footer) — all titles
and URLs were independently returned by live web search and match their
stated topics, but verify channel/publish date before/while ingesting.

## Ruled out (already covered — do not re-suggest)
PCG (Procedural Content Generation), World Partition, nDisplay/virtual
production, Movie Render Graph.
