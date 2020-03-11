from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.RoutingManager import RoutingManager
import json

'''Routing Middleware absorbs the request from the request handler and 
    routes the request to the apropriate service'''

class RoutingMiddleware:

    def __init__(self, routingManager : RoutingManager, requestRedirectManager: RequestRedirectManager):
        self._routingManager = routingManager
        self._requestRedirectManager = requestRedirectManager

    def InvokeRequest(self,context:RequestContext):
        try:
            print("In Routing Middleware --> \n Request Invoked")
            host,port,url = self._routingManager.GetServiceUrl(context.Path)
            endpoint = RoutingEndpoint(host,port,url)
            return self._requestRedirectManager.RedirectRequest(context,endpoint)
        except Exception as ex :
            context.SetResponse(500,"Internal Gateway Error",str(ex).encode('utf-8'))
            return context