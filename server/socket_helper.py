from socketserver import TCPServer, BaseRequestHandler as brh
from types import FunctionType

class ClientSocketManager():
    _TCPServer = None
    def __init__(self, ip_port, HANDLER):
        self._TCPServer = TCPServer(ip_port, HANDLER)
        
    def start(self):
        self._TCPServer.serve_forever()
        