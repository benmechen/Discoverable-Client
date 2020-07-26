import socket
import datetime
from zeroconf import ServiceInfo, Zeroconf

HOST = '***ENTER IP ADDRESS HERE***'
PORT = 1024        # Port to listen on (non-privileged ports are > 1023)
address = ""

print("#############################")
print("#### DISCOVERABLE SERVER ####")
print("#############################\n")

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
hostName = socket.gethostname() 
serverSocket.bind((HOST, PORT))
print(" > Server started on " + socket.gethostname() + ":" + HOST + ":" + str(PORT))

zeroconf = Zeroconf()

fqdn = socket.gethostname()
hostname = fqdn.split('.')[0]

desc = {'service': 'Discoverable Service', 'version': '1.0.0'}
info = ServiceInfo('_discoverable._udp.local.',
                    hostname + ' Service._discoverable._udp.local.',
                    addresses=[socket.inet_aton(HOST)], port=PORT, properties=desc)
try:
    zeroconf.register_service(info)
    print(" > Discoverable service " + str(desc) + " registered:\n" + str(info))

    while True:
        message, address = serverSocket.recvfrom(PORT)
        string = message.decode('utf-8')
        print(" > Received: " + message.decode('utf-8') + " from " + str(address))
        serverSocket.sendto("dscv_ack".encode('utf-8'), address)
        if "dscv_discover" in string:
            returnMessage = "dscv_shake:" + HOST
            print(" > Discover call from client: " + str(address))
            print(" > Sending handshake: " + returnMessage + ", to address: " + str(address))
            serverSocket.sendto(returnMessage.encode('utf-8'), address)
            print(" > [" + str(datetime.datetime.now()) + "] New client connected <" + address[0] + ">")
        elif "dscv_disconnect" in string:
            break
finally:
    print("\n > Shutting down server [" + str(datetime.datetime.now()) + "]")
    if address != "":
        serverSocket.sendto("dscv_disconnect".encode('utf-8'), address)
    zeroconf.unregister_service(info)
    zeroconf.close()
    serverSocket.close()
