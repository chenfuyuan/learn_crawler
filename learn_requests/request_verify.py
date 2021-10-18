#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :request_verify.py
# @Time      :2021/10/18 19:22
# @Author    :Chen

'使用verify参数忽略CA证书'
import requests;
url ="https://sam.huat.edu.cn:8443/selfservice/"
#SSLCertVerificationError
#response = requests.get(url)

#Warning InsecureRequestWarning:
response = requests.get(url,verify=False)
print(response.content.decode("gbk"))