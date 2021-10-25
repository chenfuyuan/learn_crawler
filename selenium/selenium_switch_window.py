#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_switch_window.py
# @Time      :2021/10/25 21:31
# @Author    :Chen

'selenium 切换标签'

from selenium import webdriver;
import time;

driver =webdriver.Chrome();

url = "https://www.baidu.com";

driver.get(url)

#点击hao123链接会打开一个新标签页
driver.find_element_by_link_text("hao123").click();

print("当前url:",driver.current_url)

#进行标签切换
#1. 获取当前所有标签页句柄构成的列表
current_windows  = driver.window_handles
print("current_windows",current_windows)
#2. 切换标签
driver.switch_to.window(current_windows[1])
print("切换后的url:",driver.current_url)

time.sleep(3)
driver.close();
time.sleep(3)
driver.quit();