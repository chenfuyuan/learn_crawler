#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_switch_frame.py
# @Time      :2021/10/25 21:43
# @Author    :Chen

'切换窗口frame 进行qq空间登录'
from selenium import webdriver;
import time;

url = "https://qzone.qq.com/"

driver = webdriver.Chrome();

driver.get(url)

#切换窗口frame
#如果不缺换窗口，接下来的一系列操作会报错
#driver.switch_to.frame("login_frame")
frame = driver.find_element_by_id("login_frame");
driver.switch_to.frame(frame)

#点击，切换到账号密码登录
driver.find_element_by_id("switcher_plogin").click();

driver.find_element_by_id("u").send_keys("qq号")
driver.find_element_by_id("p").send_keys("qq密码")
driver.find_element_by_id("login_button").click();


