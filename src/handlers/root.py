from utils.responses import json_response

def handle_root(event, context):
    return json_response({"message": "OK. Try /hello?name=Alice or /health"})
