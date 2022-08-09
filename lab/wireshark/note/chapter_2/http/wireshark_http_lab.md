# WireShark -- Http

## TASK 1

### 1 Question

![question1](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question1.png)

### 2 Picture And Answer

1. request

   ![request1](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/request1.png)

2. response

   ![reponse1](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/reponse1.png)

3. answer

   - `HTTP version：Http 1.1`
   - `Langage：ZH-CN`
   - request的source为我的主机，destination为cs主机
   - status：200
   - `Last-Modified: Fri, 08 Jul 2022 05:59:02 GMT\r\n`
   - `Content-Length: 128`
   - 处理no，source等

4. hint

   ![hint1](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/hint1.png)

   这里是提醒我们Last-Modified总是一分钟，是由服务器设置的。

## Task 2

### 1 Question

![question2](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question2.png)

### 2 Picture And Answer

1. answer
   - 第一个request没有``IF-MODIFIED-SINCE`
   - 第一个reponse有返回
   - 第二个request有`If-Modified-Since: Fri, 08 Jul 2022 05:59:02 GMT\r\n `
   - 第二个reponse `status：304`，同时没有返回

## Task 3

### 1 Question

![question3](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question3.png)

### 2 Picture And Answer

1. picture

   ![task3](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/task3.png)

2. answer

   - 只发了一次http，get请求 number 3489
   - packet 3644 包含了status，3644，3645，3646组成了整个回复
   - `status：200`
   - 三个tcp用于握手，三个内容包

3. hint

   由于tcp只能由4500 btyes，因此会发多个包

## Task 4

### 1 Question

![question4](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question4.png)

### 2 Picture And Answer

1. picture

   ![task4](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/task4.png)

2. answer

   - 发了3次请求，前两个从`ip: 128.119.245.12`,第三个从`ip: 178.79.137.164`
   - 串行发送

## Task 5

### 1 Question

![question5](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/question5.png)

### 2 Picture And Answer

1. picture

   ![task5](https://cdn.jsdelivr.net/gh/wangzd02091/blog_images@main/img/task5.png)

2. hint
