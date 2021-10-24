#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_method.py
# @Time      :2021/10/25 5:26
# @Author    :Chen

'测试selenium方法'
from selenium import webdriver;
import time;

driver = webdriver.Chrome(executable_path="D:\production\python_install\chromedriver.exe");

driver.get("https://www.baidu.com")


#渲染后的页面代码
#print(""driver.pagesource = ,driver.page_source)

#url
print("driver.current_url = ",driver.current_url)

driver.get("https://www.youtube.com")

time.sleep(3);
#页面后退
driver.back();

time.sleep(3);
#页面前进
driver.forward();

#关闭标签页，如果只有一个标签页则退出
#driver.close();

time.sleep(10)
driver.quit();