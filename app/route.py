from flask import (
    Flask, render_template, url_for, request, redirect, flash
)
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError
import logging
import os


# Flaskクラスをインスタンス化する
app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
# ログレベルを設定する
app.logger.setLevel(logging.DEBUG)
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")


# URLと実行する関数をマッピングする
@app.route('/home', method=['GET', 'POST'])
def index():
    return render_template('home.html')


@app.route('/ippin', method=['GET', 'POST'])
def index():
    return render_template('ippin.html')


@app.route('/teisyoku', method=['GET', 'POST'])
def index():
    return render_template('teisyoku.html')


@app.route('/yuzen', method=['GET', 'POST'])
def index():
    return render_template('yuzen.html')


@app.route('/course', method=['GET', 'POST'])
def index():
    return render_template('course.html')


@app.route('/alcohol', method=['GET', 'POST'])
def index():
    return render_template('alcohol.html')


@app.route('/soft-drink', method=['GET', 'POST'])
def index():
    return render_template('soft-drink.html')


@app.route('/service', method=['GET', 'POST'])
def index():
    return render_template('service.html')


@app.route('/order-cart', method=['GET', 'POST'])
def index():
    return render_template('rder-cart.html')


@app.route('/order-history', method=['GET', 'POST'])
def index():
    return render_template('order-history.html')


# @app.get('/hello/<name>', endpoint="hello-endpoint")
# def hello(name):
#     return f"Hello, {name}!"
#
#
# # show_nameエンドポイントを作成する
# @app.get('/name/<name>')
# def show_name(name):
#     # 変数をテンプレートエンジンに渡す
#     return render_template('home.html', name=name)
#
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')