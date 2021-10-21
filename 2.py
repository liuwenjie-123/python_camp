# -*- coding: utf-8 -*-
import requests
import json


# url = 'https://10.116.80.1:8001/#plugins/kimchi/tabs/guests'
url = 'https://10.116.80.1:8001/plugins/kimchi/tasks'
# body = {"type": "raw", "uuid":"machine-10.139.32.52-0622a247157"}
headers = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8',
            'Cookie' : 'wok=dbef6352f7ba9db34d0fec9340115188bafc78ff'
        }

response = requests.post(url, headers = headers,verify = False)

# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)
# 返回信息
print(response.text)
# 返回响应头
print(response.status_code)