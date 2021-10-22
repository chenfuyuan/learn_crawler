#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :xpath_tieba.py
# @Time      :2021/10/22 15:43
# @Author    :Chen

'使用xpath 爬取百度贴吧,爬取帖子标题'
import requests;
from lxml import etree;


class TieBa(object):

    def __init__(self, name):
        self.url = "https://tieba.baidu.com/f?kw={}&fr=index".format(name);
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            #"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
        }
        self.page = 0;

    # 获取响应后的数据
    def get_data(self):
        return requests.get(self.url, headers = self.headers,params={"pn":self.page}).content;

    # 解析数据
    def parse_data(self, data):
        # 贴吧将大部分内容通过注释方式隐藏。要想获取有两种方法：
        # 1. 换更低端的浏览器 请求头
        # 2. 替换掉注释标识，将标签进行释放
        data = data.decode().replace("<!--", " ").replace("-->", " ")
        html = etree.HTML(data);
        #获取所有帖子标签
        el_list = html.xpath('//li[contains(@class,"j_thread_list")]//a[@class="j_th_tit "]')
        #遍历帖子，进行数据组装 key = href ,value = text
        data_list = [];
        for el in el_list:
            temp = {};
            temp["title"]=el.text;
            temp["href"]="https://tieba.baidu.com/"+el.xpath("@href")[0];
            data_list.append(temp);
        print("%s-%s"%(self.page,self.page+len(data_list)))

        return not html.xpath('//a[@class="next pagination-item"]')



    def run(self):
        # url
        # headers
        # 发送请求，获取响应
        data = self.get_data();

        # 存入文件中
        #with open("html_tieba.html","wb") as f:
        #    f.write(data)


        # 从响应中提取数据
        isNext = self.parse_data(data)
        if isNext and self.page < 500:
            self.page+=50;
            self.run();


if __name__ == "__main__":
    tieBa = TieBa("海贼王")
    tieBa.run()
