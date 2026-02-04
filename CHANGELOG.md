# Changelog

## 2025-12-29
- Docs: Versioned docs artifacts + SemVer policy in `docs/`.
- Docs: ADR log in `docs/DECISIONS.md`.
- Docs: Encyclopedia reference in `docs/PROJECT_ENCYCLOPEDIA.md`.
- Debugging: Added `docs/DEBUGGING.md` debugging-only changelog.
- Debugging: Fixed SAM packaging by moving Lambda deps to `src/requirements.txt` (CodeUri: src/).

## 2025-12-30
- Docs/Config: Aligned remaining legacy naming references to `rical3`.
- Debugging: Made debugger attach code tolerant of missing `pydevd-pycharm` (warns instead of crashing when DEBUG=true).

## 2025-12-30
- Added `make test-local` target for pyenv-aware SAM local build and `/health` smoke test.
