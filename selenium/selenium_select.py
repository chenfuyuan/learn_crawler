#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_select.py
# @Time      :2021/10/25 19:12
# @Author    :Chen

'学习selenium的元素定位'
from selenium import webdriver;
import time;

url = "https://www.baidu.com"

driver = webdriver.Chrome();

driver.get(url);

#通过id定位元素
#element = driver.find_element_by_id("kw");

#通过class_name
#element = driver.find_element_by_class_name("s_ipt");

#通过标签中的name属性
#element =driver.find_element_by_name("wd")

#通过xpath语法
#element = driver.find_element_by_xpath('//*[@id="kw"]')

#使用css选择器
element = driver.find_element_by_css_selector("#kw")

print("type(element):",type(element))
print("element:",element)
#输入查询内容
element.send_keys("python3");
#点击百度一下
driver.find_element_by_id("su").click();


#需要暂停一会，等待页面加载，如果立刻进行元素查询，会出现查询不到问题
time.sleep(3);

#driver.find_element_by_**** 可能查询到多个，但默认只返回第一个
#如果要返回对象列表，需要使用到 .find_elements_by_****
print("url:",driver.current_url)
result_list = driver.find_elements_by_xpath('//*[contains(@class,"result c-container new-pmd")]/h3/a')
print("result_list:",result_list)
#依次打开搜索结果
for i,result in enumerate(result_list):
    '''
    if i > 2:
        break;
    result.click();
    '''
    if i > 5:
        # .text 文本内容
        # .get_attribute("属性名”) 获取属性
        print(result.text,result.get_attribute("href"))

time.sleep(3);


driver.back();


#通过 链接的名称 定位元素
#link_element = driver.find_element_by_link_text("hao123")

#模糊定位
#根据部分链接名称 定位元素。  如果名称中包含"hao"就可以定位
link_element = driver.find_element_by_partial_link_text("hao")

link_element.click()

time.sleep(3)

driver.quit();
