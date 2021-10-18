#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_cookies.py
# @Time      :2021/10/18 8:59
# @Author    :Chen

'发送带cookies的请求，进入登录状态'
import requests;

url = "https://github.com/chenfuyuan";

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "cookie": "从浏览器中抓取到的cookie"
}

response = requests.get(url, headers=headers)

#获取响应内容
content = response.content.decode()
# 判断是否登录成功
# 登录成功的页面存在 Edit profile,未登录没有
if content.__contains__("Edit profile"):
    print("登录成功")
else:
    print("登录失败")
