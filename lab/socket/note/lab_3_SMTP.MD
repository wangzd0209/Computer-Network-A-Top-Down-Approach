# SMTP

## Introduction

1. 通过SMTP协议完成邮件的发送
2. [SMTP协议的发送流程](https://blog.csdn.net/JavaMoo/article/details/54897033)
3. [一个很有用的回答](https://blog.csdn.net/qq_35414878/article/details/80725759)

## Code

```python
from socket import *
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.163.com"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    clientSocket.close()
    exit(0)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()
    exit(0)
    
# Login
loginCommand = 'AUTH LOGIN\r\n'
clientSocket.send(loginCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
    print('334 reply not received from server.')
    clientSocket.close()
    exit(0)

# Send username
username = 'wangzd0209@163.com'
usernameBase64 = base64.b64encode(username.encode()).decode()
usernameCommand = usernameBase64 + '\r\n'
clientSocket.send(usernameCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
    print('334 reply not received from server.')
    clientSocket.close()
    exit(0)
    
# Send password
password = "JANLFFWEMKFTLCCT"
passwordBase64 = base64.b64encode(password.encode()).decode()
passwordCommand = passwordBase64 + '\r\n'

clientSocket.send(passwordCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
    print('235 reply not received from server.')
    clientSocket.close()
    exit(0)

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <wangzd0209@163.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')
    clientSocket.close()
    exit(0)

# Send RCPT TO command and print server response. 
rcptToCommand = 'RCPT TO: <wangzd_image@163.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')
    clientSocket.close()
    exit(0)
    

# Send DATA command and print server response. 
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '354'):
    print('354 reply not received from server')
    clientSocket.close()
    exit(0)

# Send message data.
message = "From: wangzd0209@163.com\r\n"
message += "To: wangzd_image@163.com\r\n"
message += "Subject: Hello My Friend\r\n"
message += msg
clientSocket.send(message.encode())
# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')
    clientSocket.close()
    exit(0)
 
# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '221'):
    print('221 reply not received from server')
    clientSocket.close()
    exit(0)

clientSocket.close()
```

## P

## roblem

1. 注意username和password需要用base64转换
2. 对于password要用授权码，在@163.com在设置中打开
