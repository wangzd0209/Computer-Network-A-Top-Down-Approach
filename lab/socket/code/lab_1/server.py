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