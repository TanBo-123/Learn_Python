#!/user/bin/env python3.5
#--*-- coding=utf-8--*--

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#初始化
app = Flask(__name__)
#初始化 Flask-Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)