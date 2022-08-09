# Preparation

## introduction

1. 这是两个简单的py的udp和tcp连接，仿照书上完成的。

## UDP

### Server

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('0.0.0.0',serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print("yes")
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
```



### Client

```python
from email import message
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('input lowercase sentense:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage , serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

```

## TCP

### Server

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('0.0.0.0',serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print("yes")
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
```

### Client

```python
from socket import *
serverName = '127.0.0.1'
serverPort = 23333
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('input lowercase sentense:')
clientSocket.send(sentence.encode('utf-8'))
modifiedMessage = clientSocket.recvfrom(1024)
print(str(modifiedMessage[0],'utf-8'))
clientSocket.close()
```

