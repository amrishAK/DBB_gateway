import logging

'''LogsHandler handles all the log related works, it logs infos i.e. (all the requests and response) and errors
Seprate log file is maintained for HttpInfos, HttpErrors, ServerSwitchingInfo, ServerSwitchingErros
all the files will be in the log folder under handlers'''

class LogHandler:
    
    def __init__(self):
        pass

    def LogHttpInfo(self):
        pass

    def LogHttpError(self):
        pass

    def LogSSInfo(self):
        pass

    def LogSSError(self):
        pass