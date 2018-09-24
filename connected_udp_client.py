from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class ConnectedUDPClient(DatagramProtocol):

    def startProtocol(self):
        host = '127.0.0.1'
        port = 8000
        self.transport.connect(host, port)
        print('Connected to host: {} and port: {}'.format(host,port))
        self.transport.write(b'Hello World')
        
    def datagramReceived(self, data, addr):
        print("Received %r from %s " % (data,addr))

    def connectionRefused(self):
        print('No one is listening')

reactor.listenUDP(8005, ConnectedUDPClient())
reactor.run()