---
title: "[SUPERSEDED — bad auto-resolution, do not use]"
source: N/A
url: N/A
ingested: 2026-07-20
ue_version: "N/A"
tags: [superseded]
extraction_status: superseded
frame_status: n/a
---

# [SUPERSEDED — do not use]

This file was created by an incorrect `ingest.py` auto-resolution. The
target source was an Epic Developer Community "Learning" tutorial page:

`https://dev.epicgames.com/community/learning/tutorials/x1pX/unreal-engine-5-7-landscape-series-from-sculpting-to-production-ready-environments`

`ingest.py`'s Epic-community routing treats **every** `dev.epicgames.com/community/`
URL as a talk with an embedded YouTube video and auto-resolves it via a
`ytsearch1:` query. For this specific URL that search matched an unrelated
paid-course trailer ("Architectural Presentation Masterclass – Unreal Engine
5.7" by PolyBoost, 3m31s) which has nothing to do with the actual Landscape
Series tutorial (confirmed by content mismatch: this transcript is about a
Villa archviz scene + Gaia terrain plugin + PCG foliage + first-person mode,
not classic Landscape Sculpt/Paint/auto-material).

The real target turned out to be a **written** (not video) Epic community
tutorial. It is captured correctly at:

`tutorials/unreal-engine-5-7-landscape-series-from-sculpting-to-production-ready-environments.md`

This file is kept (rather than deleted) only because the ingest tooling in
this environment does not permit removing/renaming files; it carries no
INDEX.md entry and should be ignored. A human with delete access can remove
this file safely at any time.
