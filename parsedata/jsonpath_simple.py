#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jsonpath_simple.py
# @Time      :2021/10/19 22:17
# @Author    :Chen

'学习如何使用jsonpath获取多层嵌套中的某个数据'
from jsonpath import jsonpath;
#通俗写法
data = {"key1":{"key2":{"key3":{"key4":{"key5":{"key6":"python"}}}}}}
print("传统方式:",data["key1"]["key2"]["key3"]["key4"]["key5"]["key6"])

#使用jsonpath
#jsonpath(<dict>,"jsonpath语法字符串")返回list
print("jsonpath($.key1.key2.key3.key4.key5.key6):",jsonpath(data,'$.key1.key2.key3.key4.key5.key6'))
print("jsonpath($..key6):",jsonpath(data,"$..key6"))

