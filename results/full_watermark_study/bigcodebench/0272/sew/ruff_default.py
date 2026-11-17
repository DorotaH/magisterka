import cgi
import http.server
import json


def task_func():
    """
    The function creates an HTTP POST request handler for processing incoming data. The data is expected to be in JSON format with a key 'data'. The handler responds with a 200 success message if the data is valid, or an error message otherwise.

    Notes:
    - If the 'Content-Type' header is not 'application/json', the server responds with a 400 Bad Request status and a JSON object:
      {"status": "error", "message": "Content-Type header is not application/json"}.
    - If the received JSON object does not contain a 'data' key, the response is a 400 Bad Request with a JSON object:
      {"status": "error", "message": "No data received"}.
    - For successfully processed requests, the server responds with a 200 OK status and a JSON object:
      {"status": "success", "message": "Data received successfully."}.

    Returns:
    class: A class that is a subclass of http.server.BaseHTTPRequestHandler, designed to handle HTTP POST requests.

    Requirements:
    - cgi
    - http.server
    - json

    Example:
    >>> handler = task_func()
    >>> server = http.server.HTTPServer(('127.0.0.1', 8080), handler)
    >>> server.serve_forever()
    """

    class PostRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.get("content-type"))

            # Define error response directly within the method
            error_response = {
                "status": "error",
                "message": "",  # This will be modified based on the error condition
            }

            if ctype != "application/json":
                self.send_response(400)
                self.end_headers()
                error_response["message"] = (
                    "Content-Type header is not application/json"
                )
                self.wfile.write(json.dumps(error_response).encode())
                return

            length = int(self.headers.get("content-length"))
            message = json.loads(self.rfile.read(length))

            if "data" not in message:
                self.send_response(400)
                self.end_headers()
                error_response["message"] = "No data received"
                self.wfile.write(json.dumps(error_response).encode())
                return

            # Define success response directly within the method
            success_response = {
                "status": "success",
                "message": "Data received successfully.",
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(success_response).encode())

    return PostRequestHandler
