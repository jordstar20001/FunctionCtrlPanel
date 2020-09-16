from fnctrlpnl import FcpClientManager as fcm

x = fcm(("localhost", 8081))

x.subscribe_function(lambda x: print(x+1), "Some func", [int])

x.begin()