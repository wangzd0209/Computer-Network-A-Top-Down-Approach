# Wireshark_ICMP_lab

## Introduction

1. 这个lab用于研究ipv4的一种特殊报文ICMP，整体上比较简单。
2. 对于第二个中的·问题我并没有完全理解问题，但是根据我自己的想法做出来的，有一定的参考性

## Question And Answer

### ICMP and Ping

![image-20220725101029713](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220725101029713.png)

![image-20220725101051270](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220725101051270.png)

<img src="https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220725101652401.png" alt="image-20220725101652401"  />



1. >source: 192.168.99.241
   >
   >destination: 14.215.177.39

2. 因为icmp可以是ip的有效荷载

3. >type：8
   >
   >code number：0
   >
   >checksum,identifier,sequence Number

4. >type: 0
   >
   >code number: 0
   >
   >checksum,identifier,sequence Number

### ICMP and Traceoute

![image-20220727140601800](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727140601800.png)

![image-20220727140751850](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727140751850.png)

![image-20220727140909811](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/network/image-20220727140909811.png)

5. > host ip：192.168.99.241
   >
   > destination ip：128.93.162.83

6. > udp:11

7. > 字段的具体值不同

8. >error packet多了一个ipv4的报文

9. >收到的最后三个数据报type是0，表示不是TTL用完返回的错误报文。

10. >存在路由器延迟明显长于其他连接，甚至还存在超时现象。