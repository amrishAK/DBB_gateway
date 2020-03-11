# DBB_gateway
- httpServer.py is a shoter version will help in better understanding
- run Gateway.py to host the service at port 8001
- the service redirects all the requests to another service
- The service enpoint and url is are picked dynamically from routes.json
- enpoint can be added and modified by changing the routes.json
### URL TEMPLATE
    http://ip:port/MSA/actionPointUrl
    
    where,
        MSA - microservice name
        ip - gateway ip
        port - gateway port
    
    example: http://localhost:8001/HS/login/login
