# rical3 — SAM Local Python API (PyCharm Debugging)

- **Python runtime:** 3.12
- **Docs version:** `1.0.3` (see `docs/DOCS_VERSION.txt`)

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
- Ensure `pydevd-pycharm` matches your PyCharm build (pinned in `src/requirements.txt`).
  - Example: PyCharm `2025.3.1` → `pydevd-pycharm~=253.29346.142`.
  - Verify the packaged version: `python -c "import pydevd_pycharm; print(pydevd_pycharm.__version__)"`

2) Run SAM:
```bash
sam build --no-cached
DEBUG=true PYCHARM_DEBUG_PORT=5891 sam local start-api --port 3000
```

3) Test:
```bash
curl http://127.0.0.1:3000/health
```

## Local SAM smoke test

To quickly verify that the project builds and the local API starts correctly,
you can run a pyenv-aware smoke test that:

- builds the SAM application
- launches `sam local start-api`
- calls the `/health` endpoint
- fails fast if anything is misconfigured

```bash
make test-local PYENV_ENV=<pyenv-environment-name>
```

Example:

```bash
make test-local PYENV_ENV=rical3-py312
```

This uses `tools/test_local_sam.sh` under the hood and ensures the correct
pyenv environment is active before invoking the SAM CLI.


## README change log
- 2025-12-29: Docs-as-artifacts (SemVer), added ADR log, debugging changelog, encyclopedia doc.
- 2025-12-29: Moved Lambda packaged deps to `src/requirements.txt` to fix `No module named pydevd_pycharm`.

## 2025-12-30
- Replaced lingering legacy naming references with `rical3`.
- Debugger attach now warns (instead of crashing) if `pydevd-pycharm` is missing.

## 2025-12-31
- Debugging: Pin `pydevd-pycharm` to the current PyCharm build to avoid debugger version mismatches.

## 2025-12-31
- Debugging: Align `pydevd-pycharm` with PyCharm `2025.3.1` (build `253.29346.142`).
