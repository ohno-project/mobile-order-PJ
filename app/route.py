from flask import Flask, render_template, url_for, request, redirect, flash
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
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/ippin', methods=['GET', 'POST'])
def ippin():
    return render_template('ippin.html')


@app.route('/teisyoku', methods=['GET', 'POST'])
def teisyoku():
    return render_template('teisyoku.html')


@app.route('/yuzen', methods=['GET', 'POST'])
def yuzen():
    return render_template('yuzen.html')


@app.route('/course', methods=['GET', 'POST'])
def course():
    return render_template('course.html')


@app.route('/alcohol', methods=['GET', 'POST'])
def alcohol():
    return render_template('alcohol.html')


@app.route('/soft-drink', methods=['GET', 'POST'])
def soft_drink():
    return render_template('soft-drink.html')


@app.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')


@app.route('/order-cart', methods=['GET', 'POST'])
def order_cart():
    return render_template('rder-cart.html')


@app.route('/order-history', methods=['GET', 'POST'])
def order_history():
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