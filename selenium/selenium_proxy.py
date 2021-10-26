#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_proxy.py
# @Time      :2021/10/26 19:29
# @Author    :Chen

'使用代理'
from selenium import webdriver;
options = webdriver.ChromeOptions();

#添加ip代理配置 --proxy-server
#更换ip代理，必须重启浏览器
options.add_argument("--proxy-server=http://117.114.149.66:55443")

driver = webdriver.Chrome(chrome_options=options)

url ="https://www.baidu.com"

driver.get(url)

print(driver.title)

driver.quit();