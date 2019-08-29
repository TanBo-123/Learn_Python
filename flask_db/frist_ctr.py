#!/user/bin/env python3.5
#--*-- coding=utf-8--*--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#初始化
app = Flask(__name__)

#路由和试图函数
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
#启动服务   http://127.0.0.1:5000/


#增强版,添加了一个动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, % s!</h1>' %name








if __name__ == '__main__':
    app.run(debug=True)