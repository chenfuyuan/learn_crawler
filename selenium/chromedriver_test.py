#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chromedriver_test.py
# @Time      :2021/10/24 18:38
# @Author    :Chen

'测试selenium'
from selenium import webdriver;


#如果driver没有添加到环境变量，需要将driver的绝对路径赋值给executable_path参数
#driver = webdriver.Chrome(executable_path="")

#如果driver添加到了环境变量或将driver放到了python安装路径的/script目录中，则不需要executable_path
driver = webdriver.Chrome();


#向一个url发送一个请求
driver.get("https://www.baidu.com")

print(driver.title)


#推出模拟浏览器，一定要退出，不然会有残留进程
driver.quit()