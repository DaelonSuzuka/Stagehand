# Vision: Bottom-Up Automation

Stagehand is a software Stream Deck built in the opposite direction.

The Stream Deck is **top-down**: it started as buttons plus a curated list of
predesigned actions, grew more actions as users asked, and bolted on basic
macros later. The vendor must think of your use case before you can have it.

Stagehand is **bottom-up**: the core primitive is (was) an arbitrary code
execution engine. Trigger routing lives in the core; what happens when a
trigger fires is unbounded. Nobody has to have thought of your thing.

## The Ladder

Each layer is the same primitive at increasing altitude:

1. **Inline code** — anything, immediately, in an action body.
2. **Personal utility layer** — named tasks and helpers you write for
   yourself (`config/tasks/*.js`, helpers). You don't wait for upstream.
3. **Shared utility layer** — the community trades pieces of layer 2.
   Files are the substrate; the YAML/JS config format is deliberately
   paste-able.
4. **Plugins** — the end state: full Python, can contribute UI and new
   trigger sources, not just helpers.

## The Trust Cliff (recent, accidental, useful)

For ~7 years the engine was `exec()` in the host interpreter — no isolation,
by choice ("I like to live dangerously"); the operator was the safety
mechanism. The QuickJS/Roadie migration (2026) traded that fidelity for
reliability, creating a boundary as a side effect: layers 1–3 can only do
what services expose, which makes layer-3 sharing structurally casual, while
layer 4 remains full-trust and deserves installation friction.

The fidelity loss is a known, temporary regression, not the end state. The
plan: a reasonable JS stdlib (pure-JS tier ships as helpers; host tier as
services under the H-5 ISR-shaped policy; time-shaped operations become fire
events, never blocking calls). The "you can do anything" property lives on
at layer 4 — and possibly via a future user-written-services or inline-python
escape hatch; undecided.

## Distribution (workshopped 2026-07, no decisions yet)

Python cannot give per-plugin dependency isolation (one interpreter, flat
`sys.modules`); every plugin ecosystem picks a lie — Home Assistant installs
into its own venv at load, Anki vendors everything, Blender/QGIS declare a
provided runtime. Current working synthesis for Stagehand:

- **Transport**: tagged GitHub repos into a user-space `config_dir/plugins/`
  (which does not exist yet — today the loader only scans the source tree).
- **Dependencies**: keep the `packages/` vendoring mechanism (a hand-rolled
  PEP 582), but run `uv pip install -t` at plugin-install time on the user's
  machine — fixes compiled wheels, keeps the venv pristine, blast radius is
  the plugin folder. `-t` limits: `.pth`-dependent and post-install-script
  packages (pywin32 species) don't work; upgrades are wipe-and-reinstall.
- **Doctrine**: provided runtime — plugins should prefer what the app ships
  (PySide6, httpx, numpy, ...); vendoring covers the pure-Python margins.

PyInstaller bundles and the PyPI route are dead (see summary.md); loader
cleanup decisions are downstream of this design settling.

## Related

- [summary.md](summary.md) — current architecture and distribution status
- [architecture/plugins.md](architecture/plugins.md) — loader mechanics
- [plans/roadie-hardening.md](plans/roadie-hardening.md) — H-5 concurrency policy
