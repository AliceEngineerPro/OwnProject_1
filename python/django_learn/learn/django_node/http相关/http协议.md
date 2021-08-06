# Http协议
## Http概述
http:超文本传输协议  
浏览器和internet通讯  
**请求-->相应**
- http是<font color=red>无状态协议</font>
- ftp是有状态

url: 统一资源定位器-->网络协议://域名:端口/路径  
## 请求协议
### 请求格式
```c
请求首行  // 请求方式 请求路径 协议 版本号 eg: GET /index.html HTTP/1.1  
请求头信息  // 请求头名称:请求头内容 eg: host:localhost  
空行  // 用来与请求体分隔  
请求体  // GET没有请求体,只有POST有请求体  
```
![](https://pic.amfc.ltd/learn/python/django/http_response_request.jpg)
### request(请求头)
![](https://pic.amfc.ltd/learn/python/django/http_request.jpg)
- accept: 接受
- accept-encoding:可解压体
- accept-language:可识别语言
- connection:连接时长(默认3000ms)
- cookie:token
- host,:authority:域名主机
- user-agent:用户代理

### GET请求
1. http请求默认为GET请求
    - 没有请求体
    - 数据在1K内(有范围)
    - GET请求数据会暴露在url中
2. GET请求常用操作
    - 在浏览器的地址栏中直接给出url的一定是GET请求
    - 页面的超链接一定是GET请求
    - 提交form表单是默认为GET请求,可以设置POST请求

### POST请求
1. 数据不会出现在地址栏中
2. 数据没有上线
3. 有请求体
4. 请求体出现中文,进行url编码

## 响应请求
### 响应内容
```c
相应首行;
响应头信息;
空行;
响应体
```
### response(响应头)
![](https://pic.amfc.ltd/learn/python/django/http_response.jpg)
- content-encoding:解压格式
- content-type:传输格式
### general(all)
![](https://pic.amfc.ltd/learn/python/django/general.jpg)
- status code:请求状态码

## http状态码
- 200: 请求成功
- 404: 请求的资源没有找到(路径问题)
- 500: 请求资源找到了,但是服务器内部出现问题了(代码问题)
- 302: 重定向(更换url)
- 304: 缓存
![](https://pic.amfc.ltd/learn/python/django/http_304.png)
