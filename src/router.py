from handlers.root import handle_root
from handlers.hello import handle_hello
from handlers.health import handle_health
from utils.responses import not_found

def route_request(event, context):
    path = (event or {}).get("path") or "/"
    method = ((event or {}).get("httpMethod") or "GET").upper()

    if method == "GET" and path == "/":
        return handle_root(event, context)
    if method == "GET" and path == "/hello":
        return handle_hello(event, context)
    if method == "GET" and path == "/health":
        return handle_health(event, context)

    return not_found(f"No route for {method} {path}")
