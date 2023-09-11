# http.server hello sample
# run with `python3 hello.py` and
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT=8000

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		print('request-path:%s' % self.path)
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		message = "Hello, World!"
		self.wfile.write(bytes(message, "utf8"))

print('listennig on http://localhost:%d ...' % PORT)
with HTTPServer(('', PORT), handler) as server:
	server.serve_forever()
