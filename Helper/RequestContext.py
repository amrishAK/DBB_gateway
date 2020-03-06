class RequestContext:
    def __init__(self,header,path,requestMessage,command):
        self.Header = header
        self.Path = path
        self.RequestMessage = requestMessage
        self.Command = command
    
    def SetResponse(self, statusCode, statusReason, payload):
        self.ResponseMessage = payload
        self.ResponseCode = statusCode
        self.ResponseReason = statusReason


    

    



