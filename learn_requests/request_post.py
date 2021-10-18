#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_post.py
# @Time      :2021/10/18 19:39
# @Author    :Chen

'使用post请求，请求金山翻译'
import requests;
import json;


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


class King(object):
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=6f4f53414d4a46dd';

    def get_common_headers(self):
        header_str = """User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36""";
        return dataStr2dict(header_str)

    def get_common_data(self):
        return {};

    def __init__(self, content):
        self.content = content;
        self.common_headers = self.get_common_headers();
        self.common_data = self.get_common_data();
        self.proxy = {
            "http": "117.114.149.66"
        }

    def send_request(self, *, headers={}, data={}):
        if not headers:
            headers = self.common_headers
        if not data:
            data = self.common_data

        print("""request:
                url:%s
                headers:%s
                data:%s""" % (King.url, headers, data))

        response = requests.post(King.url, headers=headers, data=data)

        return response.content;

    # 解析数据
    def parse_data(self, data):
        #使用 json.loads()方法解析数据，转换为dict对象。
        json_dict = json.loads(data)
        #在dict中 翻译内容位于 ["content"]["out"]目录下
        return json_dict["content"]["out"]

    # 英文转换为中文
    def en_to_cn(self):

        # 设置data
        data = self.common_data.copy();
        data["from"] = "auto"
        data["to"] = "auto"
        data["q"] = self.content;

        response = self.send_request(data=data);
        result = self.parse_data(response)
        print("翻译结果:",result)

if __name__ == "__main__":
    #无法根据输入内容进行翻译，因为金山翻译通过查询字符串对查询内容进行了绑定 auth_user=key_ciba&sign=6f4f53414d4a46dd
    #一个sign对应一个内容
    king = King("hello world")
    king.en_to_cn();
