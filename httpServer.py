import http 
import socketserver
from http import server
import requests
import json
from dependency_injector import containers, providers
from Manager.RoutingManager import RoutingManager
from Manager.RoutingManager import ExampleTest

#Setting up the Depdency injection container
class Setup(containers.DynamicContainer):
    eTest = providers.Singleton(ExampleTest)   
    #life time -> like scoped => object is created for each call
    routingManager = providers.Factory(RoutingManager, eTest = eTest)
    
#Handler assigned to each incoming Http request
class SHandler(http.server.BaseHTTPRequestHandler):

    def SetResponse(self,response):
        self.send_response(response.status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response.json()).encode('utf-8'))

    def do_POST(self):
        router = Setup.routingManager()
        self.SetResponse(router.RedirectRequest(self.headers,self.rfile))
        
PORT = 8001
httpd = socketserver.TCPServer(("localhost", PORT), SHandler)

try:
    httpd.serve_forever()
except :
    httpd.shutdown()