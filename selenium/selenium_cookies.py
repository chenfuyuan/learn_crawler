#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_cookies.py
# @Time      :2021/10/25 22:13
# @Author    :Chen

'selenium操作cookie'
from selenium import webdriver;

url = "https://www.baidu.com"

driver = webdriver.Chrome();

driver.get(url)


#获取cookies字典 列表
#type:list<dict>
print(driver.get_cookies())

#通过名称获取指定cookie
print("driver.get_cookie('BA_HECTOR')=",driver.get_cookie("BA_HECTOR"));


cookies_list = driver.get_cookies();


print("=========生成cookies_list============")
cookies_dict = {};
for cookie in cookies_list:
    cookies_dict[cookie["name"]]=cookie["value"]
print("cookies_dict=",cookies_dict)

print();

cookies_dict_generate = {cookie["name"]:cookie["value"] for cookie in cookies_list}
print("使用推导式生成的字典cookies_dict_generate=",cookies_dict_generate)


#删除cookie
#删除指定cookie
#driver.delete_cookie("BA_HECTOR")
#删除所有cookie
#driver.delete_all_cookies();

driver.quit();