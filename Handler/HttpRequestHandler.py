from http.server import BaseHTTPRequestHandler
import json
from Startup import GatewayContainer
from Helper.RequestContext import RequestContext

'''absorbs the request and then forward it to the RoutingMiddleware'''
class HttpRequestHandler(BaseHTTPRequestHandler):
    def end_headers (self):
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def SetResponse(self,context : RequestContext):
        self.send_response(context.ResponseCode,context.ResponseReason)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(context.ResponseMessage)

    def ForwardRequest(self):
        context = RequestContext(self.headers,self.path,self.rfile,self.command)
        contextDict = context.__dict__
        print("--->In Request Handler \n Request" + str(contextDict))
        response = GatewayContainer.routingMiddleware().InvokeRequest(context)
        self.SetResponse(response)

    def do_POST(self):
        self.ForwardRequest()

    def do_GET(self):   
        self.ForwardRequest()
        