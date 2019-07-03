#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

import requests

user_info = {'name': 'letian', 'password': '123'}
r = requests.post("http://127.0.0.1:8080/register", data=user_info)
print(r.text)

json_data = {'a': 1, 'b': 2}
r = requests.post("http://127.0.0.1:8080/add", json=json_data)
print(r.text)