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