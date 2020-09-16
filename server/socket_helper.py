from socketserver import TCPServer, BaseRequestHandler as brh
from types import FunctionType
class TCPFunctionDelegator(brh):
    callback = None
    def __init__(self, _callback):
        assert _callback.__code__.co_argcount == 1, "Callback must only have one arg: the BaseRequestHandler of the request"
        self.callback = _callback

    def handle(self):
        self.callback(self)

class ClientSocketManager():
    _TCPServer = None
    def __init__(self, ip_port, HANDLER):
        self._TCPServer = TCPServer(ip_port, HANDLER)
        
    def start(self):
        self._TCPServer.serve_forever()
        