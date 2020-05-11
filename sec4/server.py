from http.server import HTTPServer, SimpleHTTPRequestHandler


class HTTPRequestHandler(SimpleHTTPRequestHandler): 

    def do_GET(self):
        if self.path == "/keys":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"org.w3.clearkey": {"clearkeys": {"oW5AK5BW43HzbTSKpiu3SQ": "hyN9IKGfWKdAwFaE5pm0qg"}}}')
        else:
            super().do_GET()

httpd = HTTPServer(("", 8080), HTTPRequestHandler)
httpd.serve_forever()