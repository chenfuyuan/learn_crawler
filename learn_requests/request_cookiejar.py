#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_cookiejar.py
# @Time      :2021/10/18 10:11
# @Author    :Chen

'学习cookiejar 和 dict 转换'
import requests;

url="https://www.baidu.com"

response = requests.get(url)

print("response.cookies = ",response.cookies)

#CookieJar -> dict
cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
print("cookiejar->dict:",cookie_dict)

#dict -> CookieJar
cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
print("dict->cookiejar:",cookie_jar)

