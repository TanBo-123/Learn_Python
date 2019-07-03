#!/usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask ,request


app = Flask(__name__)
print(Flask.__doc__)

@app.route('/')
def helloworld():
    print(request.path)
    print(request.full_path)
    return "helloworld!"
    pass

if __name__ == '__main__':
    app.run(port=5000)
