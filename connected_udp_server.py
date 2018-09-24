from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ConnectedUDPServer(DatagramProtocol):

    def startProtocol(self):
        host = '127.0.0.1'
        port = 8005
        self.transport.connect(host, port)
        print("Connected to the Server")
        
    def datagramReceived(self, data, addr):
        print("Received %r from %s" % (data, addr))
        self.transport.write(data)

reactor.listenUDP(8000, ConnectedUDPServer())
reactor.run()