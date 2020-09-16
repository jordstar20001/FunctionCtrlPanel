import socket, asyncio
import utils
import json
class FcpClientManager():
    FUNCID_GEN_SIZE = 10

    sock = None

    subscribed_functions = []
    def __init__(self, server_url_port_tuple):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(server_url_port_tuple)

    def subscribe_function(self, func, name, arg_types):
        function_arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        assert len(arg_types) == len(function_arg_names), "The number of arguments did not match the number of provided arg types."

        f_data = {
            "function": func,
            "name": name,
            "id": utils.random_hex_str(self.FUNCID_GEN_SIZE),
            "args": []
        }

        for i, a in enumerate(function_arg_names):
            f_data["args"].append([a, str(arg_types[i])])

        self.subscribed_functions.append(f_data)

    def begin(self):
        # Send all of the subscribed functions to the server
        temp = self.subscribed_functions[:]
        for t in temp:
            del t["function"]
        print(temp)
        json_dump = json.dumps(temp).encode()
        self.sock.send(json_dump)

        # Listen for any incoming data
        req_json = json.loads(self.sock.recv(1024).strip().decode())
        

        


