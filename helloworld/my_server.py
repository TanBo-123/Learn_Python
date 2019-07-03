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

#上传文件
from werkzeug.utils import secure_filename
import  os

app.config['UPLOAD_FOLDER'] = 'server_dat/'  #文件上传目录
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  #文件支持类型  集合类型


def allowed_file(filename):     # 判断文件名是否是我们支持的格式
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is '+request.form.get('info', '')+'. success'
    else:
        return 'failed'


if __name__ == '__main__':
    app.run(port=8080,debug=True)



