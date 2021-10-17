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