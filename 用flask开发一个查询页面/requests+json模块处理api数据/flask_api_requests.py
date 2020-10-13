from __future__ import unicode_literals
from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    # 获取api数据
    data = requests.get('https://api.github.com/repos/stedolan/jq/commits?per_page=5')
    s_data = data.json()
    author = []
    for i in s_data:
        author.append(i['commit']['author']['name'])
    # 组合html
    http = """
        <html>
        <head><meta charset="UTF-8"></head>
        <body>
            <h1>name</h1>
            %s <br>
        </body>
        </html>
    """ % author
    # 返回字符串
    return http


app.run(debug=True)