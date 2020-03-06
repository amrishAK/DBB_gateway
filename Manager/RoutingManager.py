import requests

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
    pass



    
        