#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_explicitly_write.py
# @Time      :2021/10/26 17:23
# @Author    :Chen

'selenium 显式等待'
from selenium import webdriver;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"

driver = webdriver.Chrome();

driver.get(url);

WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"好123")))

#参数20表示最长等待20秒
#参数0.5表示0.5秒检查一次规定的标签是否存在
#EC.presence_of_element_located((By.LINK_TEXT,"好123"))表示通过链接文本内容定位元素
#EC.presence_of_element_located()只接收一个参数，所以需要用括号把2个参数括起来。形成一个tuple对象
#每0.5秒检查一次(通过链接文本内容定位标签是否存在)，如果存在就继续向下执行语句，如果不存在，直到20秒后，报TimeoutException(message, screen, stacktrace)

