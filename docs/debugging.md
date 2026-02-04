# Debugging Changelog

## [Unreleased]

## [1.0.3] - 2025-12-31
- Aligned `pydevd-pycharm` with PyCharm `2025.3.1` (build `253.29346.142`).

## [1.0.2] - 2025-12-31
- Pinned `pydevd-pycharm` to the current PyCharm build to avoid debugger version mismatches.

## [1.0.1] - 2025-12-29
- Moved Lambda packaging requirements to `src/requirements.txt` (SAM `CodeUri: src/`).

## [1.0.0] - 2025-12-29
- Established known-good PyCharm + SAM Local debugging flow using `pydevd-pycharm`.
- Canonical path mapping: local `src/` → remote `/var/task`.
