# DBB_gateway
- run Gateway.py to host the service at port 8080
- the service redirects all the requests to another service
- The service enpoint and url is are picked dynamically from routes.json
- enpoint can be added and modified by changing the routes.json

### Component Design
- Routes subsequent requests from external users to the leader (i.e the primary node)
- In case of Membership management service failure, the gateway finds the next primary node by polling process 
- The gateway adds the timestamp as the payload token to all the new posts and logs it in the json format 

### URL TEMPLATE
    http://ip:port/MSA/actionPointUrl
    
    where,
        MSA - microservice name
        ip - gateway ip
        port - gateway port
    
    example: http://localhost:8001/HS/login/login


### Procerdure To Run
- Needed Python 3.6
- Needed c++ : Windows => c++ version 2015 | linux => install gcc-c++ 
- Run command to install requirements : Windows => pip install -r Requirements.txt | linux => pip3 install -r Requirements.txt
