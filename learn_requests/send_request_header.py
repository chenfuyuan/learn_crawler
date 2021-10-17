#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_request_header.py
# @Time      :2021/10/18 7:39
# @Author    :Chen

'发送带请求头的请求'
import requests;

url = "https://www.baidu.com"

#构建请求头字典
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

#发送不带有请求头的请求
response = requests.get(url)

#发送带有请求头的请求
#headers接收一个字典对象
response_1 = requests.get(url, headers=headers)

print("不带请求头的response len = ",len(response.text))
print("带请求头的response len = ",len(response_1.text))
