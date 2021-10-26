#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_headless_setting.py
# @Time      :2021/10/26 19:20
# @Author    :Chen

'selenium无界面模式配置'
from selenium import webdriver;

#实例化配置对象
options = webdriver.ChromeOptions();
#添加无界面配置
options.add_argument("--headless")
#添加禁用gpu
options.add_argument("--disable-gpu")
#实例化driver
driver = webdriver.Chrome(chrome_options=options)

url = "https://www.baidu.com"

driver.get(url)

print(driver.title)

driver.quit();