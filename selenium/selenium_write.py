#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_write.py
# @Time      :2021/10/26 16:54
# @Author    :Chen

'测试 selenium的页面等待'
from selenium import webdriver;
import time;

url = "https://www.baidu.com"
driver = webdriver.Chrome()

#隐式等待
#设置之后的所有元素定位操作都有最大等待时间十秒，在十秒内会定期进行元素定位，超过设置十秒会报元素定位失败错误
driver.implicitly_wait(3);

driver.get(url);

el = driver.find_element_by_xpath('//*[@id="lg"]/img[1000]')

print(el)