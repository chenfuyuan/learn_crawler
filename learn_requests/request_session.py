#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_session.py
# @Time      :2021/10/19 10:00
# @Author    :Chen

'使用python进行github的登录'

import requests;
import re;  # 正则模块
import time;


def login():
    # session
    session = requests.session();

    # headers
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    #poxies
    proxies = {
        "http":'182.84.144.238'
    }

    # url1-获取token
    url1 = "https://github.com/login"
    # 发送请求获取响应
    res_1 = session.get(url1,proxies=proxies).content.decode()
    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    print("token = ",token)

    # url2-登录
    url2 = "https://github.com/session"
    # 构造表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token':token,
        'password': '密码明文',
        'trusted_device': '',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': 'https://github.com/login',
        'allow_signup': '',
        'client_id': '',
        'integration': '',
        'required_field_87e0': '',
        'timestamp':int(time.time()*1000)
    }
    # 发送请求登录
    res_2 = session.post(url2,data=data)
    print(res_2.content.decode())
    # url3-验证
    url3 = "https://github.com/chenfuyuan"
    response = session.get(url3)
    if response.content.decode().__contains__("Edit profile"):
        print("登录成功")
    else:
        print("登录失败")


if __name__ == "__main__":
    login()
