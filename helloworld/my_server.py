#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

#get请求，通过http://127.0.0.1:8080/?user=Flask&time&p=7&p=8访问
@app.route('/')
def hello_world():
    r = request.args.getlist('p')
    print(type(r),type(r[0]))
    if r == None:
        return ' '
    return str(int(r[0])+int(r[1]))

#post请求,通过client.py访问
@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'


@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)




if __name__ == '__main__':
    app.run(port=8080,debug=True)