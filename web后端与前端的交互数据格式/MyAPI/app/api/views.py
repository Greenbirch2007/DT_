
from flask import make_response,jsonify
from app.api import api
from app.models import getHomepageData

@app.route('/v1/homepage/',method=["GET","POST"])
def homepage():
    response = jsonify(
        code =200,
        msg ="success",
        data = getHomepageData()
    )
    return response
# 也可以使用 make_response 生成指定状态码的响应
# return make_response(reponse,200)
