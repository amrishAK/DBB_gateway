from dependency_injector import containers, providers
from Manager.RequestRedirectManager import RequestRedirectManager
from Manager.RoutingManager import RoutingManager
from Middleware.RoutingMiddleware import RoutingMiddleware

'''This class is used to create the container for dependency injection
Life time of Factory - object is create per http request '''

class GatewayContainer (containers.DeclarativeContainer):
    
    #Adding services
    routingService = providers.Singleton(RoutingManager)
    requestRedirectService = providers.Factory(RequestRedirectManager)

    #Adding Middlewares
    routingMiddleware = providers.Factory(RoutingMiddleware,routingService,requestRedirectService)