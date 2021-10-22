#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :xpath_rule.py
# @Time      :2021/10/22 5:12
# @Author    :Chen

'学习xpath_rule'
from lxml import etree;

#获取html资源
html_file = open("xpath_rule_html.html",'r',encoding='utf-8')
html_text = html_file.read();

#创建element对象
#会纠正一些简单的语法错误，如缺失闭合标签
html = etree.HTML(html_text)
#print(html)
#print(dir(html))

#获取所有a标签中href属性为"link1.html"的文本内容，返回的是一个list
print(html.xpath('//a[@href="link1.html"]/text()'))
print(html.xpath('//a[@href="link1.html"]/text()')[0])

#获取所有a标签的文本内容
text_list = html.xpath('//a/text()')
#获取所有a标签的href值
link_list = html.xpath('//a/@href')
print("text_list = ",text_list)
print("link_list = ",link_list)


for text in text_list:
    myIndex = text_list.index(text)
    link = link_list[myIndex]
    print(text,link)

print("============for enumerate(list)=============")
#for 中直接获取索引,借用 enumerate()方法
for i,text in enumerate(text_list):
    print(text,link_list[i])


print("============for zip(list1,list2)===========")
#zip(分别使用相同索引遍历list,当一个list遍历完后，结束)
for text,link in zip(text_list,link_list):
    print(text,link)


print("=============html.xpath('//a')============")
#获取所有a节点,返回一个Element对象的list
el_list = html.xpath('//a')
print("el_list = ",el_list)
for el in el_list:
    pass;
    #遍历从根节点开始所有标签的 文本内容。(错误)
    #print("el.xpath('//text()')=",el.xpath('//text()'))

    #遍历当前标签的文本内容
    #print("el.xpath('./text()')=",el.xpath('./text()'))
    #当a标签中的文本内容为空时，'./text()'会获取一个空的list,导致使用索引[0]访问报错
    #print(el.xpath('./text()')[0],el.xpath('./@href')[0])

    #遍历当前节点下所有标签的文本内容
    #print("el.xpath('.//text()')=",el.xpath('.//text()'))

    #同el.xpath('./text()')
    #print(el.xpath('text()'))
    print(el.xpath('text()')[0],el.xpath('@href')[0])

#将Element对象转化为bytes对象
print("===============etree.toString()===================")
html_toString = etree.tostring(html)
print("etree.toString(html) = ",html_toString)
print("type(html_toString)",type(html_toString))






