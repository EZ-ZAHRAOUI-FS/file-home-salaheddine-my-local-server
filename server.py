from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000
DIRECTORY = "www.com"

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    with TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        print("you are SMART JUST TRUST ALLAH AND YHINK")
        httpd.serve_forever()
