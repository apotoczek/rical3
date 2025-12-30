# Documentation Versioning Policy

Docs are treated as **versioned artifacts**, independently from code.

## Current docs version
- `1.0.1` (see `docs/DOCS_VERSION.txt`)

## SemVer rules
- **MAJOR**: breaking doc structure/workflow changes
- **MINOR**: new docs / new guidance (backward-compatible)
- **PATCH**: fixes/clarifications/link corrections

## Bump procedure
1. Update `docs/DOCS_VERSION.txt`
2. Update:
   - `docs/DEBUGGING.md` (debugging-only changelog)
   - README “README change log”
   - `CHANGELOG.md` (optional but recommended)
