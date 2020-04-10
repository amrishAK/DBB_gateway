from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.RoutingManager import RoutingManager
from Handler.DbHandler import DbHandler
from Handler.LogHandler import LogHandler
from pymongo.collection import Collection 

class ServerSwitchingManager:

    def __init__(self, routingManager : RoutingManager, requestRedirectManager: RequestRedirectManager, dbHandler: DbHandler, log : LogHandler ):
        self._routingManager = routingManager
        self._requestRedirectManager = requestRedirectManager
        self._dbHandler = dbHandler
        self._log = log
    
    def SwitchServer(self,context: RequestContext,endPoint: RoutingEndpoint):
        try:
            print("--->In Server Switching Manager")
            polling, statusCollection = self._dbHandler.GetStatusCollection()

            if not polling :
                serviceRoutes = self._routingManager._routes['services']
                #upate the data 
                for index in range(len(serviceRoutes)):
                    endPointName = serviceRoutes[index]['Endpoint']
                    querry = {"Endpoint": endPointName}
                    endpoint = statusCollection.find_one(querry)
                    serviceRoutes[index]['Primary'] = endpoint['primary']
                    serviceRoutes[index]['Replica'] = sorted(endPoint['secondary'], key = lambda i : i['age'], reverse=True)

                    if endPoint.Name == endPointName :
                        endPoint.Host =  endpoint['primary']
                
                #check if the selected primary is alive

                #check the status of the atomic quque

                #redirect the request   
                return self._requestRedirectManager.RedirectRequest(context,endPoint)
            else:
                #returns response asking client to wait 
                #polls are the client to select primary
                pass
        except Exception as ex:
            context.SetResponse(500,"Internal Gateway Error",str(ex).encode('utf-8'))
            return context
