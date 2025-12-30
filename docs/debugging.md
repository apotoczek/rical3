# Debugging Changelog

## [Unreleased]

## [1.0.1] - 2025-12-29
- Moved Lambda packaging requirements to `src/requirements.txt` (SAM `CodeUri: src/`).

## [1.0.0] - 2025-12-29
- Established known-good PyCharm + SAM Local debugging flow using `pydevd-pycharm`.
- Canonical path mapping: local `src/` → remote `/var/task`.
