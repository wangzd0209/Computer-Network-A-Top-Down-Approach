# ProxyWebServer

## Introduction

1. 完成一个代理的服务器转发请求
2. [lab的要求以及部分代码](https://gitcode.net/mirrors/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES?from_codechina=yes)-这个代码是错误的，不但修改了框架，还不正确，至少在python3中不对
3. 符合python3的一个GitHub仓库，这里面的代码有比较高完成。[代码库](https://github.com/jzplp/Computer-Network-A-Top-Down-Approach-Answer/blob/master/Chapter-2/Socket-Programming-Assignment-4/ProxyServer.py)
4. 强烈推荐有问题的先看最下面的Problem

## Code

```python
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
	#cacheFileName = filename.replace('/', '-')
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

```

## Problem

1. > Create a temporary file on this socket and ask port 80 for the file requested by the client

   这里有两种写法，一种是根据框架使用

   ```python
   fileobj.write("GET ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
   serverResponse = fileobj.read()
   ```

   另外一种是

   ```python
   c.send("GET ".encode() + askFile.encode() + " HTTP/1.0\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
   serverResponse = c.recv(1024)
   ```

   这个问题在很多网上的解答是直接通过

   ```python
   c.send(message.encode())
   ```

   但是我发现这样实际请求的的不是正确的，例如我要请求的是`gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html`,但是这种写法请求的是`gaia.cs.umass.edu/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html`会显示没有找到对应的文件，因此需要自己写一个http请求发送给服务器。
