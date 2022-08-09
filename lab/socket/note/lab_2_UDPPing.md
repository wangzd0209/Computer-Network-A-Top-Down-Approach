# UDPPing

## Introduction

1. 通过UDP协议向服务器发送10个ping包，通过不同的选择，完成返回
2. 通过datetime完成RTT的计算
3. 通过socket.settimeout(1)完成1秒钟后的过时

## C

## ode

### Server

```python
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
	# Generate random number in the range of 0 to 10
	rand = random.randint(0, 10) 
	# Receive the client packet along with the address it is coming from 
	message, address = serverSocket.recvfrom(1024)
	# Capitalize the message from the client
	message = message.upper()
	# If rand is less is than 4, we consider the packet lost and do not respond
	if rand < 4:
		continue
	# Otherwise, the server responds 
	serverSocket.sendto(message, address)
```

### Client

```python
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

```

