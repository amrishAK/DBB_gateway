from dependency_injector import containers, providers
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.RoutingManager import RoutingManager
from Manager.ServerSwitchingManager import ServerSwitchingManager
from Middleware.RoutingMiddleware import RoutingMiddleware
from Handler.LogHandler import LogHandler
from Handler.DbHandler import DbHandler


'''This class is used to create the container for dependency injection
Life time of Factory - object is create per http request '''

class GatewayContainer (containers.DeclarativeContainer):
    
    #Adding services
    routingService = providers.Singleton(RoutingManager)
    requestRedirectService = providers.Factory(RequestRedirectManager)
    loggingService = providers.Factory(LogHandler)
    dbService = providers.Factory(DbHandler)

    #Adding Managers
    serverSwitchingService = providers.Factory(ServerSwitchingManager,routingService,requestRedirectService,dbService,loggingService)

    #Adding Middlewares
    routingMiddleware = providers.Factory(RoutingMiddleware,routingService,requestRedirectService,serverSwitchingService,loggingService)