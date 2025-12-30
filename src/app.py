import os
import logging

from router import route_request
from utils.debugging import maybe_enable_debugpy

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=getattr(logging, LOG_LEVEL, logging.INFO))
logger = logging.getLogger(__name__)

# Attach debugger if DEBUG=true
maybe_enable_debugpy(logger)

def lambda_handler(event, context):
    return route_request(event, context)
