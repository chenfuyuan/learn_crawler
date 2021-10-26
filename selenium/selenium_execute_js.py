#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_execute_js.py
# @Time      :2021/10/26 16:31
# @Author    :Chen

'selenium 执行js代码'
from selenium import webdriver;
import time;

url="https://xm.lianjia.com/"
driver = webdriver.Chrome();

driver.get(url)

#将浏览器最大化
driver.maximize_window();
#滚动条拖动
js ='scrollTo(1000,1000)'
#执行js
driver.execute_script(js)

time.sleep(3)

#如果页面中看不到该元素时，会报查询不到该元素错误
#通过拖动浏览器滚动条和放大浏览器等操作，使元素可见
driver.find_element_by_xpath('//*[@id="ershoufanglist"]/div/div[1]/p/a').click();