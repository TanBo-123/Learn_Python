#!/user/bin/env python3.5
#--*-- coding=utf-8--*--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
SQLALCHEMY_TRACK_MODIFICATIONS = True



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode='utf8')