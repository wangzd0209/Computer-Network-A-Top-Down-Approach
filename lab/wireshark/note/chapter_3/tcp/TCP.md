# Wireshark_lab_tcp

## 1 introduction

1. 请在完成当前lab的时候一定要看3.5，3.7
2. lab的几乎全部分析都是在http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip这个文件中的 `tcp-ethereal-trace-1`中所获得的，可以到官网下载，也可以在我的github上寻找。

## 2 Question And Answer

### 问题和回答

1. client的IP地址和TCP端口号?

2. gaia.cs.umass.edu的IP地址和端口号？

   - client的IP为 192.168.1.102， 端口为50982
   - sever的IP为 128.119.245.12， 端口为80

   ![tcp_握手](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/tcp_%E6%8F%A1%E6%89%8B.png)

3. 建立自己的连接后client的IP地址和端口号？

   - 这是我自己电脑的连接，IP为 192.168.99.159， 端口为50982。同时对于浏览器的三次握手我们可以发现对于google会同时发三个tcp连接请求，但是只会有一个成功。
    ![tcp握手](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/tcp%E6%8F%A1%E6%89%8B.png)

4. TCP连接中SYN段的序号是什么？什么标识了它是一个SYN段？

5. SYNACK段的序号是？SYNACK段中的Acknowledge属性的值是？gaia.cs.umass.edu怎么确认这个值？什么标识了他是一个SYNACK段？

   - Seq = 0 [SYN]
   - Seq = 0 [SYN,ACK]
   - Acknowledge:set

   ![Acknowledge_field](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/Acknowledge_field.png)

6. TCP包含HTTP POST段的序号是什么？

   - post_segement Seq=1

   ![image-20220711141747515](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711141747515.png)

7. 将含有HTTP POST段作为第一个tcp连接。前六段的序号？什么时候段发送？什么时候接受每个段的ACK？每个段的RTT的值？EstimatedRTT是多少？

   - RTT值

   ![image-20220711144626178](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711144626178.png)

8. 六个段的长度？

   ![image-20220711144752810](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711144752810.png)

9. 对于整个跟踪包，收到的最小可用缓冲区空间量是多少？缺少接收器缓冲区空间是否会限制发送方传送 TCP 区段？、

   - 最小缓冲区为5840。
   - 缺少接收器缓冲区空间会限制发送方传送 TCP 区段，这是因为 TCP 的**流量控制服务**，能够消除发送方使接收方缓存溢出的可能性，使得发送方的发送速率与接收方应用程序的读取速率相匹配。实现的方式是**滑动窗口协议**。

   ![image-20220711145126622](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711145126622.png)

10. 有无重传？为什么？

    - 没有，从图像可知序号与时间基本为线性关系。

    ![image-20220711145008732](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711145008732.png)

11. 接收器通常在 ACK 中确认多少数据？是否可以识别接收方每隔一个接收到的区段才发送确认的情况？

    - TCP累积确认，最好的确认方式是通过自己的连接可以发现有时候是确认两个段有时候确认很多段。

12. TCP 连接的吞吐量（每单位时间传输的节数）是多少？如何计算这个值？

    ![吞吐量](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/%E5%90%9E%E5%90%90%E9%87%8F.png)

13. 慢启动的开始和结束，什么时候变为了拥塞避免？

    ![慢启动](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/%E6%85%A2%E5%90%AF%E5%8A%A8.png)

    ![窗口尺寸](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/%E7%AA%97%E5%8F%A3%E5%B0%BA%E5%AF%B8.png)

    我认为是通过第二种方式检测ssthresh等于cwnd的值是将慢启动转变为拥塞避免的

## 3 Hint And Advice

### 我的错误和卡顿

1. 这是我自己tcp连接的RTT图，可以很清楚的看到十分混乱，因此我通过重新阅读材料才发现这个lab的基本全部都是通过`tcp-ethereal-trace-1`的抓包完成的。![rtt](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/rtt.png)

2. 对于post_segement这里简要说明下PSH提示携带数据，但是书中只是简答的提到了。

   ![image-20220711141747515](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220711141747515.png)

3. 对于慢启动可以同过窗口和MSS的数量获得

