class RoutingEndpoint: 
    def __init__(self,endpoint:str,host: str, port : int, url : str):
        self.Name=endpoint
        self.Host = host
        self.Port = port 
        self.Url = url