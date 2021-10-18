#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_timeout.py
# @Time      :2021/10/18 10:23
# @Author    :Chen

'学习 request的超时时间'
import requests;

url = "https://twitter.com";

response = requests.get(url,timeout=3)

print("结束")
