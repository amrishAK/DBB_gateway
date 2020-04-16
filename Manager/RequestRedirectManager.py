from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
from Handler.LogHandler import LogHandler
import http.client
import json
import datetime

class RequestRedirectManager:

    def __init__(self,log : LogHandler):
        self._log = log

    def RedirectRequest(self,context : RequestContext, endpoint : RoutingEndpoint):
        print("--->In Request Redirect Manager\n Request redirected to http://"+endpoint.Host+":"+str(endpoint.Port)+endpoint.Url)
        client = http.client.HTTPConnection(endpoint.Host,endpoint.Port)   
        self._log.LogHttpInfo(endpoint,context.Command)    
        payload = None if context.Command == 'GET'  else self.AddPayloadToken(context.RequestMessage.read(int(context.Header['Content-Length'])))
        client.request(context.Command,endpoint.Url,payload,{'Content-type': 'application/json'})
        response = client.getresponse()
        context.SetResponse(response.status,response.reason,response.read())
        client.close()
        return context

    def AddPayloadToken(self,payload):
        payloadJson = json.loads(payload)
        payloadJson['PayLoadToken'] = datetime.datetime.now().timestamp()
        print(payloadJson)
        self._log.DataLogger(payloadJson)
        return json.dumps(payloadJson)
        
            