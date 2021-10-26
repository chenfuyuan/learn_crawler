# requests模块

## 1. 介绍

[官网文档](https://docs.python-requests.org/zh_CN/latest/)

### 1.1 作用

发送http请求，获取响应数据。

### 1.2 安装

```
pip install requests
```

### 1.3 发送get请求

```python
'使用requests库，发送get请求'
import requests;

#目标url
url = "https://www.baidu.com/"

#向目标url发送get请求
response = requests.get(url)

#打印响应内容
print(response.text)
```

## 2. response响应对象

观察上边代码运行结果，中文变成了乱码。这是因为编解码使用的字符集不同导致的。

```python
import requests;

#目标url
url = "https://www.baidu.com/"

#向目标url发送get请求
response = requests.get(url)

#打印响应内容
#print("response.text = ",response.text)
#解决乱码问题
print("response.content.decode('utf-8') = ",response.content.decode("utf-8"))
```

1. **response.text是requests模块安装chardet模块推测除的编码字符集进行解码的结果。**
2. 网络传输的字符串都是``bytes``类型，所以``response.text = response.content.decode("推测除的编码字符集")``
3. 可以在网页源码中搜索``charset``,

### 2.1 ``response.text``和``response.content``的区别

- ``response.text``
  - 类型：``str``
  - 解码类型：requests模块自动根据HTTP头部对响应的编码做出有根据的推测，推测的文本编码
- ``response.content``
  - 类型：``bytes``
  - 解码类型：没有指定

### 2.2 通过对response.content进行decode，来解决中文乱码

- ``response.content.decode()`` 默认为``utf-8``
- ``response.content.decode("编码字符集")``
- 常见的编码字符集
  - utf-8
  - gbk
  - gb2312
  - ascii
  - iso-8859-1

### 2.3 response响应对象的其他常用属性和方法

- ``response.url``响应的url，有时候响应的url和请求的url并不一致
- ``response.status_code`` 响应状态码
- ``response.request.headers``响应对应的请求头
- ``response.headers``响应头
- ``response.cookies`` 响应的cookie(经过了set-cookie动作)，返回cookieJar类型
- ``response.request._cookies``响应对应请求中携带的Cookie，返回cookieJar类型
- ``response.json()``自动将json字符串类型的响应内容转换为Python对象(dict or list)

## 3. request发送Get请求

### 3.1  携带请求头发送请求的方法

``requests.get(url, headers=headers)``

- ``headers``参数接收字典形式的请求头
- 请求头字段名为key，字段对应的值为value

```python
import requests;

url = "https://www.baidu.com"

#构建请求头字典
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

#发送不带有请求头的请求
response = requests.get(url)

#发送带有请求头的请求
#headers接收一个字典对象
response_1 = requests.get(url, headers=headers)

print("不带请求头的response len = ",len(response.text))
print("带请求头的response len = ",len(response_1.text))

```

### 3.2 发送带参数的请求

url中``?``后面的内容，即查询字符串。

#### 3.2.1 在url携带参数

直接对含有参数的url发送请求

```
url = "https://www.baidu.com/s?wd=python"
```

#### 3.2.2 传入参数字典

```python
#构建参数字典
params = {
    "wd":"python"
}
```

#### 3.2.3 完整代码

```python
'发送携带参数的请求'
import requests;

url = "https://www.baidu.com/s"

#带有参数的url
url_param = "https://www.baidu.com/s?wd=python"

#构建请求头字典
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

#构建参数字典
params = {
    "wd":"python"
}

def send_success(response):
    text = response.content.decode();
    return text.__contains__("python_百度搜索")


#直接在url携带参数
response_1 = requests.get(url_param,headers=headers)
print("在url中添加参数方式是否发送请求成功?",send_success(response_1))

#使用参数字典携带参数
response_2 = requests.get(url,params=params,headers=headers)
print("传入参数字典方式是否发送请求成功?",send_success(response_2))

```

### 3.3 在headers参数中携带cookie

网站经常利用请求头中的``Cookie``字段来做用户访问状态的保持。

在``headers``字典中，添加``Cookie``属性，向请求传递``Cookie``

```python
'发送带cookies的请求，进入登录状态'
import requests;

url = "https://github.com/chenfuyuan";

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "cookie": "从浏览器中抓取到的cookie"
}

response = requests.get(url, headers=headers)

#获取响应内容
content = response.content.decode()
# 判断是否登录成功
# 登录成功的页面存在 Edit profile,未登录没有
if content.__contains__("Edit profile"):
    print("登录成功")
else:
    print("登录失败")
```

### 3.4 cookies参数使用

requests.get()中有专门的cookies参数。

1. cookies参数的形式：字典

   ``cookies = {"cookie的name":"cookie的value"}``

2. cookies参数的使用方法

   `` response = requests.get(url,cookies)``

3. 将cookie字符串转换为cookies参数所需的字典

   ```python
   cookies_dict = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookie_str.split(";")}
   ```

4. cookie一般有过期时间，一旦过期需要重新获取

#### 3.4.1 完整代码

   ```python
   '通过cookies参数来传递cookie'
   import requests;
   
   url = "https://github.com/chenfuyuan";
   
   headers = {
       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
   }
   
   cookie_str = "浏览器中抓取到的完整cookie信息";
   
   '''
   cookies = {
       "name":"value"
   }
   '''
   
   #将cookie字符串转化为cookies字典
   cookies = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookie_str.split(";")}
   
   response = requests.get(url,headers=headers,cookies=cookies)
   
   content = response.content.decode();
   # 判断是否登录成功
   # 登录成功的页面存在 Edit profile,未登录没有
   if content.__contains__("Edit profile"):
       print("登录成功")
   else:
       print("登录失败")
   ```



### 3.5 CookieJar和dict的互相转换

使用到``requests.utils.dict_from_cookiejar(<RequestsCookieJar>)``和``requests.utils.cookiejar_from_dict(<dict>)``

```python
import requests;

url="https://www.baidu.com"

response = requests.get(url)

#response.cookies =  <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print("response.cookies = ",response.cookies)

#CookieJar -> dict
#cookiejar->dict: {'BDORZ': '27315'}
cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
print("cookiejar->dict:",cookie_dict)

#dict -> CookieJar
#dict->cookiejar: <RequestsCookieJar[<Cookie BDORZ=27315 for />]>
cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
print("dict->cookiejar:",cookie_jar)
```

- dict转化为CookieJar时，for xxx会消失。

### 3.6 超时时间

一个请求等了很久未响应，会让整个项目的效率变得非常低，整个时候可以对请求设置超时时间。规定必须在特定时间内返回结果，否则就报错。

``response = requests.get(url,timeout=<int>)``

```python
'学习 request的超时时间'
import requests;

url = "https://twitter.com";

response = requests.get(url,timeout=3)

print("结束")
```

### 3.7 学代理

#### 3.7.1 理解代理的过程

1. 代理ip是一个ip，指向的是一个代理服务器
2. 代理服务器能够帮我们向目标服务器转发请求

![image-20211018103034787](https://chenfuyuan-markdown-img.oss-cn-shenzhen.aliyuncs.com/20211018103036.png)

#### 3.7.2 正向代理和反向代理区别

知不知道最终服务器的地址作为判断。

1. 从发送请求的一方的角度，来区分正向或反向代理
2. 为浏览器或库互动（发送请求的一方）转发请求的，叫做正向代理
   - 浏览器知道最终处理请求的服务器的真是ip地址，例如VPN
3. 不为浏览器或客户端（发送请求的一方）转发请求、而是为最终处理请求的服务器转发请求的，叫做反向代理。
   - 浏览器不知道服务器的真实地址，例如nginx

#### 3.7.3 代理ip(代理服务器)的分类

1. 根据代理ip的匿名程度，分为下面三类:

   - 透明代理（Transparent Proxy)：透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以查到你是谁。目标服务器收到的请求如下：

     ```
     REMOTE_ADDR = Proxy IP
     HTTP_VIA = Prixy IP
     HTTP_X_FORWARDED_FOR = Your IP
     ```

   - 匿名代理(Anonymous Proxy)：使用匿名代理，别人只知道你用了代理，无法知道你是谁。

     ```
     REMOTE_ADDR = Proxy IP
     HTTP_VIA = Prixy IP
     HTTP_X_FORWARDED_FOR = Proxy IP
     ```

   - 高匿代理（Elite proxy或High Anonymilty Proxy)：高匿代理让别人根本无法发现你是用代理，所以是最好的选择。

     ```
     REMOTE_ADDR = Proxy IP
     HTTP_VIA = not determined
     HTTP_X_FORWARDED_FOR = not determined
     ```

     

2. 根据网站所使用的的协议不同，需要使用响应协议的代理服务。从代理服务请求使用的协议可以分为:
   - http代理：目标url为http协议
   - https代理：目标url为https协议
   - socks隧道代理(例如socks5代理)等：
     - socks代理只是简单地传递数据包，不关心是何种应用协议（FTP、HTTP和HTTPS等）
     - socks代理比http、https代理耗时少
     - socks代理可以转发http和https的请求

#### 3.7.4 proxies代理参数的使用

为了让服务器以为不是同一个客户端在请求，为了防止频繁向一个域名发送请求被锁IP，所以我们需要使用代理ip。

- 用法：

  ```python
  response = requests.get(url,proxies=proxies)
  ```

- proxies的形式：字典

- 例如

  ```
  proxies = {
      "http" : "http://12.34.56.79:9527",
      "https" : "http://12.34.56.79:9527"
  }
  ```


#### 3.7.5 使用

```python
'代理'
import requests;

url = "https://www.baidu.com"

proxies = {
    "http":"http://117.88.83.203:3000",
    #该代理不支持https
    #"https":"https://117.88.83.203:3000"
};

response = requests.get(url,proxies=proxies)

print(response.content.decode())
```

### 3.8 使用verify参数忽略CA证书

在使用浏览器上网时，有时候会看到提示您的连接不是私密连接。这样提示的原因是**该网站的CA证书没有经过【受信任的根证书颁发机构】的认证**

如``https://sam.huat.edu.cn:8443/selfservice/``

#### 3.8.1 运行代理查看代码中向不安全链接发起请求效果

```python
'使用verify参数忽略CA证书'
import requests;
url ="https://sam.huat.edu.cn:8443/selfservice/"
#SSLCertVerificationError
response = requests.get(url)
```

报错:``SSLCertVerificationError``

```python
requests.exceptions.SSLError: HTTPSConnectionPool(host='sam.huat.edu.cn', port=8443): Max retries exceeded with url: /selfservice/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1045)')))
```

#### 3.8.2 解决方案

```python
'使用verify参数忽略CA证书'
import requests;
url ="https://sam.huat.edu.cn:8443/selfservice/"
#SSLCertVerificationError
#response = requests.get(url)

#Warning InsecureRequestWarning:
response = requests.get(url,verify=False)
print(response.content.decode("gbk"))
```

在``requests.get()``方法中添加``verify=False``参数。

## 4. request发生Post请求

哪些地方会用到Post请求

1. 登录注册(web工程师看来POST比GET更安全，url地址中不会暴露用户的账号密码)

2. 需要传说大文本内容的时候(POST请求对数据长度没有要求)

#### 4.1requests发送post请求的方法

- ``response = requests.post(url,data)``

- ``data``参数接收一个字典
- **requests模块发送post请求函数的其他参数和发送get请求的参数完全一致**

#### 4.2 案例:金山翻译

```python
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

    def send_request(self, *, headers={}, data={}):
        if not headers:
            headers = self.common_headers
        if not data:
            data = self.common_data

        print("""request:
                url:%s
                headers:%s
                data:%s""" % (__class__.url, headers, data))

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
```

#### 4.3 有道翻译

```python
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
```

#### 4.4 post data数据来源

1. 固定值(通过抓包获取)
2. 输入值(通过抓包获取)

3. 预设值-静态文件

   需要提前从静态html中获取

4. 预设值-发请求

   需要对指定地址发送请求

5. 在客户端通过js生成的

### 5. 使用requests.session进行状态保持

requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的。

#### 5.1 requests.session的作用以及应用场景

- requests.session的作用
  - 自动处理cookie,即下一次请求会带上前一次的cookie
- requests.session应用场景
  - 自动处理连续的多次请求过程中产生的cookie

#### 5.2 案例：gitee的登录

```python
'使用session登录gitee'
import requests;
import re;


def login():
    # session
    session = requests.session();
    # headers
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    # url_1 登录静态页面，用于获取token
    url_1 = "https://gitee.com/login";
    # 发送get请求
    res_1 = session.get(url_1).content.decode();
    # 使用正则表达式匹配token
    token = re.findall('name="csrf-token" content="(.*?)" />',res_1)[0];
    print("token = ",token)

    # url_2 登录
    url_2 = "https://gitee.com/login"
    # 构建登录表单数据
    data = {
        'encrypt_key': 'password',
        'utf8': '✓',
        'authenticity_token':token,
        'redirect_to_url':'',
        'user[login]':'用户名',
        'encrypt_data[user[password]]': '加密后的密码',
        'user[remember_me]': '0'
    }
    # 发送post请求进行登录
    res_2 = session.post(url_1,data=data)
    if res_2.content.decode().__contains__("陈福源"):
        print("登录成功")
    else:
        print("登录失败")

if __name__ =="__main__":
    login()
```

# 数据提取

## 数据提取概述

**知识点**

- 了解响应内容分类
- 了解xml和html区别

### 1. 响应内容分类

- 结构化的响应内容(数据有层次关系)
  - json字符串(高频出现)
    - 可以使用re、json、jsonpath等模块来提取特定数据
  - xml字符串(低频出现)
    - 可以使用re、lxml等模块进行提取
- 非结构化
  - html
    - 可以使用re、lxml提取

### 2.  xml和html区别

二者区别

| 数据格式 | 描述                                       | 设计目标                                 |
| :--: | :----------------------------------------: | :--------------------------------------: |
| XML| Extensible Markup Language(可扩展标记语言) | 被设计为传输和存储数据，其焦点是数据内容 |
| HTML| HyperText Markup Language(超文本标记语言)  | 显示数据以及如何更好的显示数据           |

### 3. 常用数据解析方法

![image-20211019221111024](https://chenfuyuan-markdown-img.oss-cn-shenzhen.aliyuncs.com/20211019221112.png)

## 数据提取-jsonpath模块

### 1. jsonpath使用场景

> 如果有一个多层嵌套的复杂字典，想要根据key和下标批量提取value。

jsonpath可以按照key对python字典进行批量数据获取

### 2. jsonpath使用方法

#### 2.1 安装

```shell
pip install jsonpath
```

#### 2.2 使用方法

```
from jsonpath import jsonpath
ret = jsonpath(<dict>,"jsonpath语法规则字符串")
```

#### 2.3 jsonpath语法规则

| JSONPath        | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| ``$``           | 根节点(最外层的大括号)                                       |
| ``@``           | 现行节点                                                     |
| ``.`` or ``[]`` | 取子节点(直接子节点)                                         |
| n/a             | 取父节点，JsonPath不支持                                     |
| ``..``          | 就是不管位置，选择所有符合条件的条件(内部任意位置)           |
| ``*``           | 匹配所有元素节点                                             |
| n/a             | 根据属性访问，Json不支持，因为Json是一个Key-value递归结构，不需要属性访问 |
| ``[]``          | 迭代器标示(可以在里面做简单的迭代操作，如数组下标、根据内容选值等) |
| ``[,]``         | 支持迭代器中做多选                                           |
| ``?()``         | 支持过滤操作                                                 |
| ``()``          | 支持表达式计算                                               |
| n/a             | 分组，JsonPath不支持                                         |

常用``$``、``.``、``..``

#### 2.4 jsonpath使用

```python
'学习如何使用jsonpath获取多层嵌套中的某个数据'
from jsonpath import jsonpath;
#通俗写法
data = {"key1":{"key2":{"key3":{"key4":{"key5":{"key6":"python"}}}}}}
print("传统方式:",data["key1"]["key2"]["key3"]["key4"]["key5"]["key6"])

#使用jsonpath
#jsonpath(<dict>,"jsonpath语法字符串")返回list
print("jsonpath($.key1.key2.key3.key4.key5.key6):",jsonpath(data,'$.key1.key2.key3.key4.key5.key6'))
print("jsonpath($..key6):",jsonpath(data,"$..key6"))

```



### 3. 数据提取-lxml模块

#### 3.1. 了解lxml模块和xpath语法

对html或xml提取特定内容，需要使用到lxml和xpath语法

- lxml模块，可以利用XPath语法，来快速定位HTML\XML文档中特定元素以及获取节点信息(文本内容、属性值)
- XPath(XML Path Language)是一门在HTML\XML文档中查找信息的语言。Xpath文档:[https://www.w3school.com.cn/xpath/xpath_syntax.asp](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

#### 3.2. xpath简单使用

对应的xpath_rule_html.html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试xpath规则</title>
</head>
<body>
    <ul>
        <li>
            <a href="link1.html">item1<div>div</div></a>
        </li>
        <li>
            <a href="link2.html">item2</a>
        </li>
        <li>
            <a href="link3.html">item3</a>
        </li>
        <li>
            <a href="link4.html">item4</a>
        </li>
        <li>
            <a href="link5.html">item5</a>
        </li>
        <li>
            <a href="link6.html">item6</a>
    </ul>

</body>
</html>
```

python代码:

```python
'学习xpath_rule'
from lxml import etree;

#获取html资源
html_file = open("xpath_rule_html.html",'r',encoding='utf-8')
html_text = html_file.read();

#创建element对象
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

```

- 使用``etree.HTML(<str>/<bytes>)``方法，获取一个Element对象
- 使用``element.xpath("xpath规则语法")``解析html文件。
- ``enumermate(list)``返回索引和 对应索引的列表项
- ``zip(list1,list2)``分别使用相同索引遍历两个list,当一个list遍历完后结束

#### 3.3. xpathhelper(谷歌浏览器扩展插件)

作用:对当前页面测试xpath语法规则

#### 3.4 xpath节点关系

每个html、xml标签被称为一个节点。其中最顶层的节点被称为根节点。以xml为例，html也一样。

![image-20211022141822127](https://chenfuyuan-markdown-img.oss-cn-shenzhen.aliyuncs.com/20211022141823.png)

##### 3.4.1 xpath节点的关系

![image-20211022142123602](https://chenfuyuan-markdown-img.oss-cn-shenzhen.aliyuncs.com/20211022142124.png)

 #### 3.5 xpath语法-选取节点以及提取属性或文本内容的语法

1. Xpath使用路径表达式来选取XML文档中的节点或者节点集
2. 这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似
3. 使用chrome插件选择标签时，选中时，选中的标签会添加属性class="xh-highlight"

##### 3.5.1 表达式

| 表达式     | 描述                                                     |
| ---------- | -------------------------------------------------------- |
| nodename   | 选中该元素                                               |
| ``/``      | 从根节点选取、或者元素和元素间的过渡                     |
| ``//``     | 从匹配选中的当前节点选择文档中的节点，而不考虑它们的位置 |
| ``.``      | 选取当前节点                                             |
| ``..``     | 选取当前节点的父节点                                     |
| ``@``      | 选取属性                                                 |
| ``text()`` | 选取文本                                                 |

##### 3.5.2 节点修饰语法

使用``[]``修饰节点。

| 表达式                                     | 结果                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| //title[@lang="eng"]                       | 选择lang属性值为eng的所有title标签                           |
| /bookestore/book[1]                        | 选取属于bookstore子元素的第一个book元素                      |
| /bookestore/book[last()]                   | 选取属于bookstore子元素的最后一个book元素                    |
| /bookestore/book[last()-1]                 | 选取属于bookstore子元素的倒数第二个book元素                  |
| /bookestore/book[position()>1]             | 选取bookstore下面索引大于1的book元素                         |
| //book/title[text()='Harry Potter']        | 选择所有book下的title元素，仅仅选择文本为Harry Potter的title元素 |
| /bookstore/book[price>35.00]/title         | 选取bookstore元素下的book元素的所有title元素。且其中price元素的值须大于35.00 |
| /bookstore/book[contains(class,'science')] | 选取bookstore元素下的book元素，且其中class属性值包含'science' |

##### 3.5.3 选取未知节点

| 通配符 | 描述                 |
| :----- | :------------------- |
| *      | 匹配任何元素节点。   |
| @*     | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

# selenium

selenium是一个自动化测试框架。selenium运用在爬虫中，可以大幅降低爬虫的编写难度，但是也大幅降低爬虫的爬取速度。

> 安装

```
pip install selenium
```

## driver 安装

### 1 chrome driver安装

需要根据浏览器版本下载

功能菜单->帮助->关于Chrome->版本

下载地址:[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

#### 1.1 安装

下载后解压，将``chromedriver.exe``添加到环境变量，或将其放在python安装位置的\script目录下。

#### 1.2 验证

```python
from selenium import webdriver;


#如果driver没有添加到环境变量，需要将driver的绝对路径赋值给executable_path参数
#driver = webdriver.Chrome(executable_path="")

#如果driver添加到了环境变量或将driver放到了python安装路径的/script目录中，则不需要executable_path
driver = webdriver.Chrome();


#向一个url发送一个请求
driver.get("https://www.baidu.com")

print(driver.title)


#推出模拟浏览器，一定要退出，不然会有残留进程
driver.quit()
```

#### 1.3 无界面运行

```python
'测试chrome driver 无界面'
from selenium import webdriver;
from selenium.webdriver.chrome.options import Options;

#设置chromedriver
chrome_options = Options();
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#获取一个driver
driver = webdriver.Chrome(chrome_options=chrome_options)

#发送一个url
driver.get("https://www.baidu.com/")
print(driver.title)

#关闭
driver.quit();
```



### 2 PhantomJS(最新版本不再支持)

一个基于Webkit的"无界面"浏览器。会把网站加载到内存中并执行页面上的javascript。

最新的selenium不再支持PhantomJS。请使用ChromeDriver无界面版，

### 2.1 安装

下载地址:[https://phantomjs.org/download.html](https://phantomjs.org/download.html)

下载完后，进行解压，并将/bin目录添加到环境变量PATH中。

#### 2.2 验证

打开cmd输入``phantomjs -v ``，如果出现版本号，则代表安装成功

```python
from selenium import webdriver;


#如果driver没有添加到环境变量，需要将driver的绝对路径赋值给executable_path参数
#driver = webdriver.Chrome(executable_path="")

#如果driver添加到了环境变量或将driver放到了python安装路径的/script目录中，则不需要executable_path
driver = webdriver.PhantomJS();


#向一个url发送一个请求
driver.get("https://www.baidu.com")

print(driver.title)


#推出模拟浏览器，一定要退出，不然会有残留进程
driver.quit()
```



## selenium的作用和工作原理

利用浏览器原生的API，封装程一套更面向对象的Selenium WebDriver API，直接操作浏览器页面里的元素，甚至操作浏览器本身（截屏、窗口大小、启动、关闭、安装插件、配置证书等)

![image-20211024195118415](https://chenfuyuan-markdown-img.oss-cn-shenzhen.aliyuncs.com/20211024195120.png)

- webdriver本质是一个web-server，对外提供webapi，其中封装了浏览器的各种功能
- 不同浏览器使用各自不同的webdriver

### 1. 简单使用

```python
from selenium import webdriver;
import time;

#executable_path="D:\production\python_install\chromedriver" 为chrmedriver的绝对路径
#driver = webdriver.Chrome(executable_path="D:\production\python_install\chromedriver")

#如果已经将chrome driver放入环境变量中则无需指定路径
driver = webdriver.Chrome();
driver.get("https://www.baidu.com")

#寻找id为'kw'的元素，在其中输入'python'
driver.find_element_by_id("kw").send_keys("python")
#寻找id为'su'的元素，控制它进行点击
driver.find_element_by_id("su").click();

time.sleep(6)

driver.quit();
```

- ``webdriver.Chrome(executable_path='D:\production\python_install\chromedriver')``中executable参数，指定chromedriver的绝对路径
- ``driver.find_element_by_id(<str>'id值')``通过id属性值定义元素
- ``.send_keys<str>"输入内容")``向该元素中输入内容
- ``.click()``模拟浏览器点击，触发元素的click事件



## selenium使用

### 1. driver对象的常用属性和方法

- ``driver.page_source``当前标签页浏览器渲染后的网页源码
- ``driver.current_url``当前标签页的url
- ``driver.close()``关闭当前标签页，如果只有一个标签页则关闭整个浏览器
- ``driver.quit()``关闭浏览器
- ``driver.forward()``页面前进
- ``driver.back()``页面后退
- ``driver.scrent_shot(<str>img_name)``页面截图

### 2. driver对象定位标签元素获取标签对象方法

- **``find_element_by_id()``**根据id
- **``find_element_by_class_name()``**根据类名
- **``find_element_by_name()``**根据标签``name属性值``
- **``find_element_by_xpath()``**根据xpath语法
- ``find_element_by_link_text()``根据连接文本
- ``find_element_by_partial_link_text()``根据链接包含的文本
- ``find_element_by_tag_name()``根据标签名
- **``find_element_by_css()``**根据css选择器

### 3. 标签切换

```python
'selenium 切换标签'

from selenium import webdriver;
import time;

driver =webdriver.Chrome();

url = "https://www.baidu.com";

driver.get(url)

#点击hao123链接会打开一个新标签页
driver.find_element_by_link_text("hao123").click();

print("当前url:",driver.current_url)

#进行标签切换
#1. 获取当前所有标签页句柄构成的列表
current_windows  = driver.window_handles
print("current_windows",current_windows)
#2. 切换标签
driver.switch_to.window(current_windows[1])
print("切换后的url:",driver.current_url)

time.sleep(3)
driver.close();
time.sleep(3)
driver.quit();
```

1. 获取当前所有标签页句柄

   ``driver.window_handles``返回所有标签页组成的句柄 列表

2. 根据句柄切换标签页

   ``driver.switch_to.window(<CDwindow对象>)``

### 4. 窗口切换

```python
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
```

1. 使用``.switch_to.frame()``进行窗口切换

   其中传入frame的id或表示frame的elemenet对象

### 5. cookies的处理

```python
'selenium操作cookie'
from selenium import webdriver;

url = "https://www.baidu.com"

driver = webdriver.Chrome();

driver.get(url)


#获取cookies字典 列表
#type:list<dict>
print(driver.get_cookies())

#通过名称获取指定cookie
print("driver.get_cookie('BA_HECTOR')=",driver.get_cookie("BA_HECTOR"));


cookies_list = driver.get_cookies();


print("=========生成cookies_list============")
cookies_dict = {};
for cookie in cookies_list:
    cookies_dict[cookie["name"]]=cookie["value"]
print("cookies_dict=",cookies_dict)

print();

cookies_dict_generate = {cookie["name"]:cookie["value"] for cookie in cookies_list}
print("使用推导式生成的字典cookies_dict_generate=",cookies_dict_generate)


#删除cookie
#删除指定cookie
#driver.delete_cookie("BA_HECTOR")
#删除所有cookie
#driver.delete_all_cookies();

driver.quit();
```

- 获取cookie
  - ``driver.get_cookies()s`获取所有cookies，返回一个``list``，其中的元素类型为``dict``类型，其中有cookie的各种信息。``name``、``value``等
  - ``driver.get_cookie("cookie_name")``根据cookie的名称获取指定cookie,如果不存在则返回None,如果存在返回一个``dict``对象。
- 删除cookie
  - ``driver.delete_cookie("cookie_name")``删除指定名称的cookie
  - ``driver.delete_all_cookies()``删除所有cookie

### 6. 执行js代码

```python
'selenium 执行js代码'
from selenium import webdriver;
import time;

url="https://xm.lianjia.com/"
driver = webdriver.Chrome();

driver.get(url)

#将浏览器最大化
driver.maximize_window();
#滚动条拖动
js ='scrollTo(1000,1000)'
#执行js
driver.execute_script(js)

time.sleep(3)

#如果页面中看不到该元素时，会报查询不到该元素错误
#通过拖动浏览器滚动条和放大浏览器等操作，使元素可见
driver.find_element_by_xpath('//*[@id="ershoufanglist"]/div/div[1]/p/a').click();
```

- 使用``driver.maximize_window()``放大浏览器窗口
- 使用``scrollTo(x,y)``js方法，对浏览器滚动条进行操作。
  - x,y代表滚动多少个像素
- 使用``driver.execute_script(js)``执行js脚本语句

### 7. 页面等待

分类

1. 强制等待
2. 隐式等待
3. 显式等待

#### 7.1 强制等待

- 其实就是``time.sleep(<int>)``
- 缺点是不智能，设置的过短，元素未加载处理。设置太长，则浪费时间

#### 7.2 隐式等待

- 针对的是元素定位，饮食等待设置了一个时间，在一段时间内判断元素是否定位成功，如果完成了就进行下一步
- 在设置的时间内没有定位成功，报超时加载
- 示例代码

```python
'测试 selenium的页面等待'
from selenium import webdriver;
import time;

url = "https://www.baidu.com"
driver = webdriver.Chrome()

#隐式等待
#设置之后的所有元素定位操作都有最大等待时间十秒，在十秒内会定期进行元素定位，超过设置十秒会报元素定位失败错误
driver.implicitly_wait(3);

driver.get(url);

el = driver.find_element_by_xpath('//*[@id="lg"]/img[1000]')

print(el)
```

使用``driver.implicitly_wait(<int>10);``设置之后的所有元素定位操作都有最大等待时间十秒，在十秒内会定期进行元素定位，超过设置十秒会报元素定位失败错误

#### 7.3 显式等待

- 每经过多少秒就查看一次等待条件是否达到，如果达成就停止等待，继续执行后续代码

- 如果没有达成就继续等待知道超过规定时间后，按超时异常

- 示例代码

  ```python
  'selenium 显式等待'
  from selenium import webdriver;
  from selenium.webdriver.support.wait import WebDriverWait;
  from selenium.webdriver.support import  expected_conditions as EC
  from selenium.webdriver.common.by import By
  
  url = "https://www.baidu.com"
  
  driver = webdriver.Chrome();
  
  driver.get(url);
  
  WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"好123")))
  
  #参数20表示最长等待20秒
  #参数0.5表示0.5秒检查一次规定的标签是否存在
  #EC.presence_of_element_located((By.LINK_TEXT,"好123"))表示通过链接文本内容定位元素
  #EC.presence_of_element_located()只接收一个参数，所以需要用括号把2个参数括起来。形成一个tuple对象
  #每0.5秒检查一次(通过链接文本内容定位标签是否存在)，如果存在就继续向下执行语句，如果不存在，直到20秒后，报TimeoutException(message, screen, stacktrace)
  ```

  

