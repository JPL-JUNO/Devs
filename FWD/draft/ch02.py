"""
@File         : ch02.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-28 17:00:55
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


app.add_url_rule("/", "index", index)


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello {name}!</h1>"


from flask import request


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return f"<p>Your browser is {user_agent}</p>"


from flask import make_response


@app.route("/")
def index():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie("answer", 42)
    return response
