from socket import *
import sys
import os
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('127.0.0.1', 8084))
tcpSerSock.listen(5)
while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message = tcpCliSock.recv(1024).decode()
	print(message)
	# Extract the filename from the given message
	print(message.split()[1])
	filename = message.split()[1].partition("/")[2]
	print(filename)
	cacheFileName = filename.replace('/', '-')
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	try:# Check wether the file exist in the cache
		f = open("WEB" + filetouse[1:], "rb")
		outputdata = f.read()
		f.close()
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
		tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
		tcpCliSock.send(outputdata)
		print('Read from cache')
		# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
			c = socket(AF_INET, SOCK_STREAM)
			hostn = filename.replace("www.","",1)
			print(hostn)
			try:
				serverName = hostn.partition('/')[0]
				# Connect to the socket to port 80
				c.connect((serverName, 80))
				askFile = ''.join(filename.partition('/')[1:])
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				#fileobj = c.makefile('rwb', 0)
				#fileobj.write("GET ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
				#c.send(("GET "+"http://" + filename + " HTTP/1.1\r\n").encode())
				#c.send(("Host: localhost:8084\r\n").encode())
				#c.send(("Connection: keep-alive\r\n").encode())
				c.send("GET ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
				serverResponse = c.recv(1024)
				# Read the response into buffer
				#serverResponse = fileobj.read()
				#buffer = c.recv(4096)
				# Create a new file in the cache for the requested file.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				filename = "WEB/" + filename
				filesplit = filename.split('/')
				for i in range(0, len(filesplit) - 1):
					if not os.path.exists("/".join(filesplit[0:i + 1])):
						os.makedirs("/".join(filesplit[0:i + 1]))
				tmpFile = open(filename,"wb")
				serverResponse = serverResponse.split(b'\r\n\r\n')[1]
				tmpFile.write(serverResponse)
				tmpFile.close()
				tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
				tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
				tcpCliSock.send(serverResponse)
			except:
				print("Illegal request")
				break
		else:
			# HTTP response message for file not found
			tcpCliSock.send("HTTP/1.0 404 Not Found\r\n".encode())
			tcpCliSock.send("\r\n".encode())
			tcpCliSock.send("404 Not Found Cant Find such file " + filename + "\r\n".encode())
		# Close the client and the server sockets
		tcpCliSock.close()
tcpSerSock.close()
