"""
@File         : hello.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-28 17:10:50
@Email        : cuixuanstephen@gmail.com
@Description  : 一个完整的 Flask 应用
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"
