import os

def maybe_enable_debugpy(logger):
    """Attach PyCharm debugger from inside the SAM local Docker container.

    Enable by setting:
      - DEBUG=true
      - PYCHARM_DEBUG_HOST (default: host.docker.internal)
      - PYCHARM_DEBUG_PORT (default: 5891)

    Canonical PyCharm mapping (ONE mapping only):
      - Local : <repo>/src
      - Remote: /var/task

    In SAM local, the runtime paths are like /var/task/router.py (there is no /var/task/src/...).
    """
    if os.environ.get("DEBUG", "false").lower() != "true":
        return

    host = os.environ.get("PYCHARM_DEBUG_HOST", "host.docker.internal")
    port = int(os.environ.get("PYCHARM_DEBUG_PORT", "5891"))
    try:
        import pydevd_pycharm  # type: ignore
    except ImportError as e:
        logger.warning("DEBUG=true but pydevd-pycharm is not installed in the Lambda build: %s", e)
        return

    logger.warning("Connecting to PyCharm debug server at %s:%s ...", host, port)
    pydevd_pycharm.settrace(
        host,
        port=port,
        stdout_to_server=False,
        stderr_to_server=False,
        suspend=False,
    )
    logger.warning("Connected to PyCharm debugger.")
