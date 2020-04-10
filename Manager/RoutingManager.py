import requests
from Helper.RoutingEndpoint import RoutingEndpoint
from Helper.JsonHandler import JsonHandler

class RoutingManager:
    def __init__(self):
        self._jsonHandler = JsonHandler()
        self._routes = self._jsonHandler.LoadJson('Routes.json')
    
    def GetServiceUrl(self,path):
        try:
            pathArray = path.split("/")
            service = pathArray[1]
            serviceList = self._routes['services']
            endpoint = next(endpoint for endpoint in serviceList if endpoint['Endpoint'] == service)
            path = path.replace("/"+service,"")
            return RoutingEndpoint(service,endpoint['Primary']['server'], endpoint['Port'], path)
        except Exception as ex:
            raise Exception(ex)

    def ChangePrimary(self,endpoint,replicaList):
        pass
    
    def GetReplicaList(self,endpoint):
        pass 