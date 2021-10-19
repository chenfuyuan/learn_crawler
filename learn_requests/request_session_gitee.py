#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_session_gitee.py
# @Time      :2021/10/19 10:42
# @Author    :Chen

'使用session登录gitee'
import requests;
import re;


def login():
    # session
    session = requests.session();
    # headers
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    # url_1 登录静态页面，用于获取token
    url_1 = "https://gitee.com/login";
    # 发送get请求
    res_1 = session.get(url_1).content.decode();
    # 使用正则表达式匹配token
    token = re.findall('name="csrf-token" content="(.*?)" />',res_1)[0];
    print("token = ",token)

    # url_2 登录
    url_2 = "https://gitee.com/login"
    # 构建登录表单数据
    data = {
        'encrypt_key': 'password',
        'utf8': '✓',
        'authenticity_token':token,
        'redirect_to_url':'',
        'user[login]':'用户名',
        'encrypt_data[user[password]]': '加密后的密码',
        'user[remember_me]': '0'
    }
    # 发送post请求进行登录
    res_2 = session.post(url_1,data=data)
    if res_2.content.decode().__contains__("陈福源"):
        print("登录成功")
    else:
        print("登录失败")

if __name__ =="__main__":
    login()