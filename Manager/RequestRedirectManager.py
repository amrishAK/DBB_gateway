from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
import http.client

class RequestRedirectManager:

    def RedirectRequest(self,context : RequestContext, endpoint : RoutingEndpoint):
        print("--->In Request Redirect Manager\n Request redirected to http://"+endpoint.Host+":"+str(endpoint.Port)+endpoint.Url)
        client = http.client.HTTPConnection(endpoint.Host,endpoint.Port)       
        payload = None if context.Command == 'GET'  else context.RequestMessage.read(int(context.Header['Content-Length']))
        client.request(context.Command,endpoint.Url,payload,context.Header)
        response = client.getresponse()
        context.SetResponse(response.status,response.reason,response.read())
        client.close()
        return context
        
            