from socket import *
import datetime

serverName = "127.0.0.1"
serverPort = 8088

i = 10
while i > 0:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    try:
        begin_time = datetime.datetime.now()
        clientSocket.sendto("ping".encode(), (serverName, serverPort))
        while True:
            data, addr = clientSocket.recvfrom(1024)
            if data.decode() == 'PING':
                end_time = datetime.datetime.now()
                i = i - 1
                break
            else:
                print(data)
                continue
    except timeout:
        print("Ping timeout")
        i = i - 1
    else:
        rtt = (end_time - begin_time).microseconds / 1000.0
        print("ping rtt ", rtt)

