from socket import *
serverPort = 23333
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentense = connectionSocket.recv(1024).decode('utf-8')
    print("yes")
    retsentense = sentense.upper()
    connectionSocket.send(retsentense.encode('utf-8'))
    connectionSocket.close()
