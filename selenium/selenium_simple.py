#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_simple.py
# @Time      :2021/10/24 20:00
# @Author    :Chen

'selenium简单使用'

from selenium import webdriver;
import time;

#executable_path="D:\production\python_install\chromedriver" 为chrmedriver的绝对路径
#driver = webdriver.Chrome(executable_path="D:\production\python_install\chromedriver")

#如果已经将chrome driver放入环境变量中则无需指定路径
driver = webdriver.Chrome();
driver.get("https://www.baidu.com")

#寻找id为'kw'的元素，在其中输入'python'
driver.find_element_by_id("kw").send_keys("python")
#寻找id为'su'的元素，控制它进行点击
driver.find_element_by_id("su").click();

time.sleep(6)

driver.quit();
