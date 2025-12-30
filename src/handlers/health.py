from utils.responses import json_response

def handle_health(event, context):
    return json_response({"status": "healthy"})
