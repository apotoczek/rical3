from utils.responses import json_response, bad_request

def handle_hello(event, context):
    qs = (event or {}).get("queryStringParameters") or {}
    name = (qs.get("name") or "").strip()
    if not name:
        return bad_request("Missing required query parameter: name")
    return json_response({"message": f"Hello, {name}!"})
