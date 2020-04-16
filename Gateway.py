import http
import socketserver
from Startup import GatewayContainer
from Handler.HttpRequestHandler import HttpRequestHandler 


def run():
    httpd = socketserver.TCPServer(("0.0.0.0", 8081), HttpRequestHandler)
    try:
        httpd.serve_forever()
    except :
        httpd.shutdown()


if __name__ == "__main__":
    run()