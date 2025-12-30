# Project Encyclopedia

## Overview
rical3 is a minimal Python AWS Lambda HTTP API intended for local development with AWS SAM and reliable debugging via PyCharm.

## Architecture
- Entry point: `src/app.py` (`lambda_handler`)
- Router: `src/router.py` dispatches on path + method
- Handlers: `src/handlers/*` implement endpoints
- Utilities: `src/utils/*` shared response and debugging helpers

## Runtime model (local)
In SAM local, the built artifact is mounted to `/var/task` inside the container. This is the authoritative root for breakpoint paths.

## Debugging model
The project uses `pydevd-pycharm` to connect from the container to the IDE.
Canonical mapping: local `src/` → remote `/var/task`.

## Glossary
- SAM: Serverless Application Model
- CodeUri: path to Lambda code package root (this repo uses `src/`)
- /var/task: Lambda working directory
