#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_proxy.py
# @Time      :2021/10/18 19:07
# @Author    :Chen

'代理'
import requests;

url = "https://www.baidu.com"

proxies = {
    "http":"http://117.88.83.203:3000",
    #该代理不支持https
    #"https":"https://117.88.83.203:3000"
};

response = requests.get(url,proxies=proxies)

print(response.content.decode())