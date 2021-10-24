#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chromedriver_headless_test.py
# @Time      :2021/10/24 19:03
# @Author    :Chen

'测试chrome driver 无界面'
from selenium import webdriver;
from selenium.webdriver.chrome.options import Options;

#设置chromedriver
chrome_options = Options();
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#获取一个driver
driver = webdriver.Chrome(chrome_options=chrome_options)

#发送一个url
driver.get("https://www.baidu.com/")
print(driver.title)

#关闭
driver.quit();