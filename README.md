# RICAL1 — SAM Local Python API (PyCharm Debugging)

- **Python runtime:** 3.12
- **Docs version:** `1.0.1` (see `docs/DOCS_VERSION.txt`)

## Start here
- Debugging runbook: `docs/debugging.md`
- Encyclopedia reference: `docs/PROJECT_ENCYCLOPEDIA.md`
- Decisions (ADR): `docs/DECISIONS.md`
- Debugging changelog: `docs/DEBUGGING.md`
- Docs versioning policy: `docs/DOCS_VERSIONING.md`

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**SAM packaging note:** `template.yaml` uses `CodeUri: src/`, so SAM packages dependencies from **`src/requirements.txt`**.

## Run locally
```bash
sam build --no-cached
sam local start-api --port 3000
```

## Debug with PyCharm (verified)
1) PyCharm: Python Debug Server
- Host: `localhost`
- Port: `5891`
- Path mapping (ONE mapping only): local `<repo>/src` → remote `/var/task`

2) Run SAM:
```bash
sam build --no-cached
DEBUG=true PYCHARM_DEBUG_PORT=5891 sam local start-api --port 3000
```

3) Test:
```bash
curl http://127.0.0.1:3000/health
```

## README change log
- 2025-12-29: Docs-as-artifacts (SemVer), added ADR log, debugging changelog, encyclopedia doc.
- 2025-12-29: Moved Lambda packaged deps to `src/requirements.txt` to fix `No module named pydevd_pycharm`.
