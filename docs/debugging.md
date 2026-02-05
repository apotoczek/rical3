## PyCharm breakpoint pitfall: debugger attaches but never breaks

A very common failure mode when debugging SAM Local Lambdas with PyCharm is:

- PyCharm shows **“Connected to pydev debugger”**
- The Lambda executes and returns responses normally
- **No breakpoints are ever hit**
- SAM logs show warnings like:

```
pydev debugger: warning: trying to add breakpoint to file that does not exist:
/Users/.../src/handlers/health.py (will have no effect)
```

### Why this happens

Inside the SAM Local container, Lambda code is executed from:

```
/var/task/handlers/health.py
```

There is **no `/var/task/src/...` directory** at runtime.

If PyCharm’s path mapping causes breakpoints to be sent as local paths
(e.g. `/Users/.../src/handlers/health.py`) instead of being translated to
`/var/task/handlers/health.py`, the debugger will attach successfully but
**all breakpoints will be ignored**.

### The only correct PyCharm path mapping

In the **Python Debug Server** configuration, use **exactly one** mapping:

- **Local path:** `<repo>/src`
- **Remote path:** `/var/task`

Example:

```
/Users/amp5/.../axp-rical3-amp5/src  ->  /var/task
```

Do **not** map:
- `.aws-sam/build/ApiFunction -> /var/task`
- repo root -> `/var/task`

Those mappings cause PyCharm to send incorrect breakpoint paths.

### How to confirm the runtime path

You can temporarily log this inside a handler:

```python
print("health.__file__:", __file__)
```

If you see:

```
health.__file__: /var/task/handlers/health.py
```

then your breakpoints must resolve to `/var/task/handlers/health.py`
from the debugger’s point of view.

If PyCharm logs say “file does not exist”, the mapping is wrong.

## Verified local environment (PyCharm 2025.3.2.1)

This project has been verified with the following setup:

### Python / pyenv
- Python version: **3.12.12**
- Environment created with:

```bash
pyenv virtualenv 3.12.12 rical3
pyenv activate rical3
pip install -r requirements.txt
```

### PyCharm
- PyCharm version: **2025.3.2.1**
- Interpreter set to:

```
~/.pyenv/versions/rical3/bin/python
```

### Debugger dependency

```txt
pydevd-pycharm~=253.30387.173
debugpy==1.8.1
```

These dependencies live in:

```
src/requirements.txt
```

### Debug server configuration
- Debug configuration: **Python Debug Server**
- Host: `localhost`
- Port: `5891`
- Path mapping:

```
<repo>/src  ->  /var/task
```

### Running SAM Local with debugging enabled

```bash
export DEBUG=true
export PYCHARM_DEBUG_HOST=host.docker.internal
export PYCHARM_DEBUG_PORT=5891

sam build --no-cached --use-container
sam local start-api --port 3000
```


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
