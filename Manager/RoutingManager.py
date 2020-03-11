import requests
from Helper.JsonHandler import JsonHandler

class ExampleTest:
    name = 0
    def __init__(self):
        self.name = self.name + 1
        print("ExampleTEst"+ str(self.name))

class RoutingManager1:
    name = 0
    def __init__(self,eTest):
        self.eTest = eTest
        self.name = self.name + 1
        print("RoutingManager"+ str(self.name))

    def RedirectRequest(self,headers,rfile):
        self.eTest.name += 1
        print("ExampleTEst"+ str(self.eTest.name))
        content_length = int(headers['Content-Length']) # <--- Gets the size of data
        post_data = rfile.read(content_length) # <--- Gets the data itself
        return requests.post(url = "http://localhost:7760/login/login",data=post_data,headers=headers)


class RoutingManager:
    def __init__(self):
        self._jsonHandler = JsonHandler()
        self._routes = self._jsonHandler.LoadJson('Routes.json')['services']
        self._routes = list(self._routes)
    
    def GetServiceUrl(self,path):
        try:
            pathArray = path.split("/")
            service = pathArray[1]
            endpoint = next(endpoint for endpoint in self._routes if endpoint['Endpoint'] == service)
            path = path.replace("/"+service,"")
            return endpoint['Primary'], endpoint['Port'], path
        except Exception as ex:
            raise Exception(ex)
    
        


    
        