# Decision Log (ADR-style)

## ADR-0001: Use PyCharm attach debugging via `pydevd-pycharm` in SAM local
- Status: Accepted
- Date: 2025-12-29
- Decision: Use `pydevd_pycharm.settrace()` gated by `DEBUG=true`.
- Consequence: Requires correct path mapping (local `src/` → remote `/var/task`).

## ADR-0002: Documentation is versioned separately from code (Docs SemVer)
- Status: Accepted
- Date: 2025-12-29
- Decision: Add `docs/DOCS_VERSION.txt` + policy doc, follow SemVer.

## ADR-0003: Keep README as quickstart; add encyclopedia-style reference
- Status: Accepted
- Date: 2025-12-29
- Decision: Maintain `README.md` (instructional) and `docs/PROJECT_ENCYCLOPEDIA.md` (reference).
