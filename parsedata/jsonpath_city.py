#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jsonpath_city.py
# @Time      :2021/10/19 22:52
# @Author    :Chen

''
from jsonpath import jsonpath;

import json;


city_file = open("city.json","r",encoding="utf-8")

city_dict = json.loads(city_file.read())

result = jsonpath(city_dict,"$..cityname")
print(result)