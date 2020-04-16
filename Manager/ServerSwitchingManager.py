from Helper.RequestContext import RequestContext
from Helper.RoutingEndpoint import RoutingEndpoint
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.RoutingManager import RoutingManager
from Handler.DbHandler import DbHandler
from Handler.LogHandler import LogHandler
from pymongo.collection import Collection 
import http.client


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
            polling = True
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
                serviceList = self._routingManager._routes['services']
                endpoint = next(endpoint for endpoint in serviceList if endpoint['Endpoint'] == endPoint.Name)
                endpointIndex = serviceList.index(endpoint)
                for host in endpoint['Replica']:
                    #checks the server availability by polling
                    try:
                        print("Polling..." + str(host))
                        client = http.client.HTTPConnection(host['server'],endpoint['Port'])   
                        client.request('GET',"/test")
                        response = client.getresponse()
                        if response.status == 200:
                            print("Primary found")
                            endPoint.Url.replace(endpoint['Primary']['server'],host['server'])
                            endPoint.Host = host['server']
                            endpoint['Primary'] = host
                            print(endPoint)
                            self._routingManager._routes['services'][endpointIndex] = endpoint
                            return self._requestRedirectManager.RedirectRequest(context,endPoint)
                    except Exception:
                        continue
                        
            context.SetResponse(503,"Service Temporarily Unavailable",("Service Temporarily Unavailable".encode('utf-8')))
            return context
        except Exception as ex:
            context.SetResponse(500,"Internal Gateway Error",str(ex).encode('utf-8'))
            return context
