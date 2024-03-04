import http.server
import socketserver
import os

# Define the directory to serve files from
root_dir = os.path.abspath(os.path.dirname(__file__))

# Define the MIME types mapping
mimetypes = {
    '.html': 'text/html',
    '.js': 'application/javascript',
}

# Extend the SimpleHTTPRequestHandler to use custom MIME types
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ext = os.path.splitext(path)[1]
        return mimetypes.get(ext, 'application/octet-stream')

# Change the current directory to the root directory
os.chdir(root_dir)

# Start the server
with socketserver.TCPServer(("", 8000), CustomHandler) as httpd:
    print("Server running at http://localhost:8000")
    httpd.serve_forever()