#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_user_agent.py
# @Time      :2021/10/26 19:39
# @Author    :Chen

'替换user-agent'
from selenium import webdriver;
options = webdriver.ChromeOptions();


options.add_argument("--user-agent=Mozilia/5.0 selenium")

driver = webdriver.Chrome(chrome_options=options)

url ="https://www.baidu.com"

driver.get(url)

print(driver.title)
