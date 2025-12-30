import json
from typing import Any, Dict, Optional

def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    base = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "GET,OPTIONS",
    }
    if extra:
        base.update(extra)
    return base

def json_response(body: Any, status_code: int = 200, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return {"statusCode": status_code, "headers": _headers(headers), "body": json.dumps(body)}

def bad_request(message: str) -> Dict[str, Any]:
    return json_response({"error": message}, status_code=400)

def not_found(message: str = "Not Found") -> Dict[str, Any]:
    return json_response({"error": message}, status_code=404)
