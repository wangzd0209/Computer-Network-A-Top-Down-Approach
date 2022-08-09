# Wireshark_DPCH_lab

## Introduction

1. 整体实验比较简单。

## Question And Answer

![image-20220727142819886](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727142819886.png)

![image-20220727144818966](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727144818966.png)

![image-20220727144848394](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727144848394.png)

1. > udp

2. >使用67和68 port_number，与pdf上相同

3. >Client MAC address: 1a:2c:1c:ce:45:4c (1a:2c:1c:ce:45:4c)

4. >option中包含的字段和值不同

5. > 前四个 Transaction ID: 0x55d1b58f
   >
   > 第二个 Transaction ID: 0xbd130095
   >
   > 表示DHCP报文的ID，避免多个主机的DHCP报文接收混乱。

6. | number/     | source       | destination     |
   | ----------- | ------------ | --------------- |
   | 1/discovery | 0.0.0.0      | 255.255.255.255 |
   | 2/offer     | 192.169.99.1 | 192.168.99.112  |
   | 3/request   | 0.0.0.0      | 255.255.255.255 |
   | 4/ack       | 192.169.99.1 | 192.168.99.112  |

7. >DHCP ip:   192.169.99.1

8. >DHCP ip:   192.169.99.1
   >
   >Your (client) IP address: 192.168.99.112

9. >Relay agent IP address: 0.0.0.0 
   >
   >意味着没有中介

10. >在Option字段中，表示当前连接的路由器和对应的子网。

11. >Option中的 Requested IP Address字段提供的

12. >可使用这个IP地址的时间。我实验中的租约时间12小时。

13. >释放这个IP地址。如果客户端的 DHCP 释放消息丢了，服务器会依然认为这个IP地址被占用。
