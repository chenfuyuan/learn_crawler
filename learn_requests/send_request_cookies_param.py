#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_request_cookies_param.py
# @Time      :2021/10/18 9:20
# @Author    :Chen

'通过cookies参数来传递cookie'
import requests;

url = "https://github.com/chenfuyuan";

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
}

cookie_str = "浏览器中抓取到的完整cookie信息:name=value";

'''
cookies = {
    "name":"value"
}
'''

#将cookie字符串转化为cookies字典
def cookie_str2dict(str):
    #return {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookie_str.split(";")};
    result = {};
    for cookie in cookie_str.split(";"):
        name,value = cookie.split("=");
        result[name] =value;
    return result;

#将cookie字符串转化为cookies字典
cookies_dict = cookie_str2dict(cookie_str)
print("转化后的cookies = ", cookies_dict)
#发起请求
response = requests.get(url, headers=headers, cookies=cookies_dict)

#转化为str
content = response.content.decode();
# 判断是否登录成功
# 登录成功的页面存在 Edit profile,未登录没有
if content.__contains__("Edit profile"):
    print("登录成功")
else:
    print("登录失败")
