#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium_douyu.py
# @Time      :2021/10/26 19:46
# @Author    :Chen

'使用selenium 爬取斗鱼直播列表'
from selenium import webdriver;
import time;
import json;

from lxml import etree;

class DouYu:

    def parse_data(self,driver):
        #强制等待3秒，让页面加载完成js
        time.sleep(3)
        # 将 html放入etree中，用于xpath解析
        html = etree.HTML(driver.page_source);

        # 获取当前页面直播列表
        el_list = html.xpath('//*[contains(@class,"layout-Cover-item")]');

        data_list = [];
        #迭代进行组装
        for el in el_list:
            el_dict = {};
            #分别获取 intro,userName,hot,label
            el_dict["intro"]=el.xpath('.//*[contains(@class,"DyListCover-intro")]/text()');
            el_dict["userName"]=el.xpath('.//*[contains(@class,"DyListCover-userName")]/text()');
            el_dict["hot"]=el.xpath('.//*[contains(@class,"DyListCover-hot")]/text()');
            el_dict["label"]=el.xpath('.//*[contains(@class,"HeaderCell-label-wrap")]/text()');
            data_list.append(el_dict);

        return data_list;

    def run(self,category):

        url = "https://www.douyu.com/"+category;
        driver = webdriver.Chrome();
        driver.get(url);
        driver.implicitly_wait(5)
        #最大化浏览器窗口，方便收集数据

        result_file = open("result.text","w",encoding="utf-8")

        number = 1;
        while(True):
            print("第%d页"%number)
            number+=1;
            #parse
            data_list = self.parse_data(driver);

            #save
            #将对象保存到文件中
            json.dump(data_list,result_file,ensure_ascii=False);
            result_file.write("\n");
            #next
            #判断是否有下一页
            next_button = driver.find_element_by_class_name("dy-Pagination-next")
            if next_button.get_attribute("aria-disabled") == "false":
                next_button.click();
            else:
                break;

        print("爬取结束")
        driver.quit();

if __name__ =="__main__":
    DouYu().run("g_CF");





