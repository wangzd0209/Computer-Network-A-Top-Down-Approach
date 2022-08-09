# wireshark_lab_udp

## 说明

1. 这个lab十分简单，指导书上说小于30分钟就能完成。
2. 请看章节3.3

## Question And Answer

### 问题和答案

![question](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question.png)

1. 从跟踪中选择一个UDP数据包。从此数据包中，确定 UDP 标头中有多少字段，并为这些字段命名。

   ![field](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/field.png)

2. 通过查询Wireshark，确定每个UDP报头字段长度。

   - 8个字节，由4个两字节的的数据组成

   ![length](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/length.png)

3. 长度字段中的值是指的是什么？使用捕获的 UDP 数据包验证您的声明。

   - 长度是(首部 + 数据），95+8=103

   ![image-20220712090221832](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/image-20220712090221832.png)

4. UDP有效负载中可包含的最大字节数是多少？

   - 2byte为2^16 = 65536，因此有效负载的65536-8 = 65528个

5. UDP 的协议号是什么？ 以十六进制和十进制表示法给出答案。

   UDP->17 0X11

6. 观察发送 UDP 数据包后接收响应的 UDP 数据包，这是对发送的 UDP 数据包的回复，请描述两个数据包中端口号之间的关系。(提示：对于响应 UDP 目的地应该为发送 UDP 包的地址。）

   发送端口，是回复的接受端口
