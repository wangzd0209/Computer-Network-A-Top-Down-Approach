# WebServer_lab

## introduction

1. 这个主要是应用preparation中的TCP连接，主体框架在instruction中。
1. 响应报文的创建要自己查，或是才code中直接复制

## Task

1. 建立一个连接套接字
2. 接受HTTP请求
3. 解释请求的文件
4. 从服务器获取特定文件
5. 创建响应报文
6. 捕获异常

## Code

```python
#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 8088
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        filePath = "C://Users/wangzd/Desktop/计算机基础/network-/socket/lab_1/"
        f = open( filePath  +  filename[1:]) 
        outputdata = f.readlines()
        #Send one HTTP header line into socket
        httpHeader = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\n\n'
        connectionSocket.send(httpHeader.encode())
		#Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        httpHeader = "HTTP/1.1 404 Found"
        connectionSocket.send(httpHeader.encode())
        connectionSocket.close()

serverSocket.close(1)
sys.exit()
```



## Problem

1. 接受的HTTP请求首先转换成str，通过decode()完成。
2. 对于从服务器获取最好是通过open(全路径)来打开，我试过`./`开头没有成功
3. 请求头可以查询或是直接复制

