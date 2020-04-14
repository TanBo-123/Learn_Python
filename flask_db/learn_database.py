#!/user/bin/env python3.5
# --*-- coding=utf-8--*--
# 在__init__.py文件中的内容
from flask import Flask
# 从flask_sqlalchemy导入SQLAlchemy类
from flask_sqlalchemy import SQLAlchemy

import os
# 通过Flask创建一个app实例
app = Flask(__name__)

# Flask_SQLAlchemy插件从SQLALCHEMY_DATABASE_URI配置的变量中获取应用的数据库位置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/test?charset=utf8mb4'
# 通过SQLAlchemy创建db实例，表示程序使用的数据库，并且db能够使用Flask_SQLAlchemy的所有功能
db = SQLAlchemy(app)


# 定义类User，继承自基类db.Model
class User(db.Model):
    # 定义数据库表的名称，为user表
    __tablename__ = 'user'
    # db.Column类构造函数中的第一个参数表中该字段的类型和该字段的其它属性
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    # print User对象时，会打印return的字符串，方便调试
    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"

if __name__ == "__main__":
     app.run(debug=True)