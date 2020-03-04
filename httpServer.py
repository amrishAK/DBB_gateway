import http 
import socketserver
from http import server
import requests
import json

class SHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        response = requests.post(url = "http://localhost:7760/login/login",data=post_data,headers=self.headers)
        self.send_response(response.status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response.json()).encode('utf-8'))
    
    
PORT = 8001
httpd = socketserver.TCPServer(("localhost", PORT), SHandler)
print( "serving at port", PORT)

try:
    httpd.serve_forever()
except :
    httpd.shutdown()