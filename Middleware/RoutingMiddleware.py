from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.ServerSwitchingManager import ServerSwitchingManager
from Manager.RoutingManager import RoutingManager
from Handler.LogHandler import LogHandler
import http.client
import json

'''Routing Middleware absorbs the request from the request handler and 
    routes the request to the apropriate service'''

class RoutingMiddleware:

    def __init__(self, routingManager : RoutingManager, requestRedirectManager: RequestRedirectManager, serverSwitch : ServerSwitchingManager, log : LogHandler):
        self._routingManager = routingManager
        self._requestRedirectManager = requestRedirectManager
        self._log = log
        self._serverSwitch = serverSwitch

    def InvokeRequest(self,context:RequestContext):
        try:
            print("--->In Routing Middleware \n Request Invoked")
            self._currentEndpoint = self._routingManager.GetServiceUrl(context.Path)
            return self._requestRedirectManager.RedirectRequest(context,self._currentEndpoint)
        except (ConnectionRefusedError,TimeoutError) as ex :
            #code to change the primary and handle things
            return self._serverSwitch.SwitchServer(context,self._currentEndpoint)
        except Exception as ex:
            context.SetResponse(500,"Internal Gateway Error",str(ex).encode('utf-8'))
            return context