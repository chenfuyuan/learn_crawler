#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_get.py
# @Time      :2021/10/18 6:47
# @Author    :Chen

'使用requests库，发送get请求'
import requests;

#目标url
url = "https://www.baidu.com/"

#向目标url发送get请求
response = requests.get(url)

#打印响应内容
print("response.encoding = ",response.encoding)
print("response.text = ",response.text)

response.encoding = "utf-8"
print("转换为utf-8编码后的response.text = ",response.text)

#解决乱码问题
print("response.content = ",response.content)
#response.content.decode()默认为'utf-8'
print("response.content.decode() = ",response.content.decode())


#response.content type <bytes>
print("type(response.content) = ",type(response.content))
#response.text type <str>
print("type(response.text) = ",type(response.text))
#response.content.decode() type <str>
print("type(response.content.decode()) = ",type(response.content.decode()))


#response响应对象常用的属性
print("================response响应对象常用的属性======================")
#url
print("response.url = ",response.url)
#状态码
print("状态码 response.status_code = ",response.status_code)
#响应对应的请求头
print("对应的请求头 response.request.headers = ",response.request.headers)
#响应头
print("响应头 response.headers = ",response.headers)
#响应中携带的，需要设置的Cookie，返回cookieJar类型
print("响应中携带的，需要设置的Cookie response.cookies = ",response.cookies)
#响应对应请求中携带的Cookie，返回cookieJar类型
print("响应对应请求中携带的Cookie response.request._cookies =",response.request._cookies)
