# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/27 18:55
# @Author: Enbryan Xie

import requests

data = {
    "user": "william",
    "password": "1234abcd!"
}

res = requests.post("http://www.tcpjwtester.top/api/user/login", json=data)
print(res.text)

token = res.json()["data"]["token"]
print(token)