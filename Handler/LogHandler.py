import logging
import json_log_formatter
import json
from  Helper.RoutingEndpoint import RoutingEndpoint 


'''LogsHandler handles all the log related works, it logs infos i.e. (all the requests and response) and errors
Seprate log file is maintained for HttpInfos, HttpErrors, ServerSwitchingInfo, ServerSwitchingErros
all the files will be in the log folder under handlers'''

class LogHandler:
    
    def __init__(self):
        #log formatter
        jsonFormat = json_log_formatter.JSONFormatter()
        #httpLogger
        httpLogHandler = logging.FileHandler(filename="logs/http.json")
        httpLogHandler.setFormatter(jsonFormat)
        self.httpLogger = logging.getLogger('http')
        self.httpLogger.addHandler(httpLogHandler)
        self.httpLogger.setLevel(logging.INFO)
        #server Switch logger
        ssLogHandler = logging.FileHandler(filename="logs/ss.json")
        ssLogHandler.setFormatter(jsonFormat)
        self.ssLogger = logging.getLogger('http')
        self.ssLogger.addHandler(httpLogHandler)
        self.ssLogger.setLevel(logging.INFO)                                                                                                                                                                                               
        #error logger
        errorLogHandler = logging.FileHandler(filename="logs/error.json")
        errorLogHandler.setFormatter(jsonFormat)
        self.errorLogger = logging.getLogger('http')
        self.errorLogger.addHandler(httpLogHandler)
        self.errorLogger.setLevel(logging.ERROR)
        #data logger
        dataLogHandler = logging.FileHandler(filename="logs/data.json")
        dataLogHandler.setFormatter(jsonFormat)
        self.dataLogger = logging.getLogger('http')
        self.dataLogger.addHandler(httpLogHandler)
        self.dataLogger.setLevel(logging.INFO)

    def LogHttpInfo(self,endpoint:RoutingEndpoint,method):
          self.httpLogger.info(method, extra=endpoint.__dict__)

    def LogHttpError(self):
        pass

    def LogSSInfo(self):
        pass

    def LogSSError(self):
        pass

    def DataLogger(self):
        pass
