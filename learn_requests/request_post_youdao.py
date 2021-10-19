#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_post_youdao.py
# @Time      :2021/10/19 8:31
# @Author    :Chen

'有道翻译'

import requests, json;


# 将复制的data字符串 转化为 字典类型
def dataStr2dict(str):
    # return {data_item.split(":")[0]: data_item.split(":")[1] for data_item in str.split("\n")}
    result = {};
    for data_item in str.split("\n"):
        if data_item.strip(" ") == "":
            continue;
        name, value = data_item.split(": ");
        result[name.strip(" ")] = value.strip(" ")
    return result;


#获取list的首个不是list的元素
#如果list的首个元素是list类型数据，继续寻找首元素。
def list_get_first(data):
    if not data:
        return None;
    if isinstance(data, (list,tuple)):
        return list_get_first(data[0])
    return data


class YouDao(object):

    def get_headers(self):
        headers_str = """Accept: application/json, text/javascript, */*; q=0.01
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
        Connection: keep-alive
        Content-Length: 249
        Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        Cookie: OUTFOX_SEARCH_USER_ID=2053498047@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=486372920.58034444; _ga=GA1.2.555909646.1608207152; _ntes_nnid=c567b6a24e916e7fe907d79893e9991f,1617474708522; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcrHGekTNDZCbBbu9vYx; ___rl__test__cookies=1634603909092
        Host: fanyi.youdao.com
        Origin: https://fanyi.youdao.com
        Referer: https://fanyi.youdao.com/?keyfrom=dict2.index
        sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
        sec-ch-ua-mobile: ?0
        sec-ch-ua-platform: "Windows"
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: same-origin
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
        X-Requested-With: XMLHttpRequest"""
        return dataStr2dict(headers_str)

    def get_formdata(self):
        formdata_str = """i: hello world
        from: AUTO
        to: AUTO
        smartresult: dict
        client: fanyideskweb
        salt: 16346039090931
        sign: 667c218c943aa35919fb75e426fbb25f
        doctype: json
        version: 2.1
        keyfrom: fanyi.web
        action: FY_BY_CLICKBUTTION""";
        return dataStr2dict(formdata_str)

    def get_response(self):
        return requests.post(self.url, headers=self.headers, data=self.formdata).content

    def parse_data(self, data):
        translate_dict = json.loads(data)
        return list_get_first(translate_dict['translateResult'])['tgt']

    def __init__(self, content):
        self.content = content;

        self.url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule";
        self.headers = self.get_headers()
        self.formdata = self.get_formdata()
        response = self.get_response()
        print(self.parse_data(response))


if __name__ == "__main__":
    #输入内容进行翻译失效，有道根据Headers中的属性进行翻译
    youDao = YouDao("hello")
