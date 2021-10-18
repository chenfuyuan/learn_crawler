#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_params.py
# @Time      :2021/10/18 7:56
# @Author    :Chen

'发送携带参数的请求'
import requests;

url = "https://www.baidu.com/s"

#带有参数的url
url_param = "https://www.baidu.com/s?wd=python"

#构建请求头字典
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

#构建参数字典
params = {
    "wd":"python"
}

def send_success(response):
    text = response.content.decode();
    return text.__contains__("python_百度搜索")


#直接在url携带参数
response_1 = requests.get(url_param,headers=headers)
print("在url中添加参数方式是否发送请求成功?",send_success(response_1))

#使用参数字典携带参数
response_2 = requests.get(url,params=params,headers=headers)
print("传入参数字典方式是否发送请求成功?",send_success(response_2))


