
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_health_status():
    return {"status": "UP", "service": "training-lab"}


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404, "Not Found")
            return

        response = json.dumps(get_health_status()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", "8080"))
    server = HTTPServer(("127.0.0.1", port), HealthHandler)
    print(f"Health API running on http://127.0.0.1:{port}/health")
    server.serve_forever()
