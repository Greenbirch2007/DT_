import collections
import requests
from lxml import etree
from selenium import webdriver
import pymysql
import datetime
import time
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文


a ="我"
b = "你"*8

d = "它"*3
f = ["我","吗"]


c = collections.Counter(f)

print(c["我"]) #这个是有效的！
# print(c["你"])
# print(c["它"])

# print(a)
#
# def select_all():
#     f_list = []
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
#                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     cursor.execute('select industry from js_infos_finanData')
#     results = cursor.fetchall()
#     for item in results:
#         data_du = item["industry"]
#         f_list.append(data_du)
#     connection.commit()
#     connection.close()
#     return f_list


# sqlalchemy关系映射　和直接访问数据库



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class Js_infos_finanData(Base):
    __tablename__ = 'js_infos_finanData'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    industry = Column(String(8),nullable=True)  # String在数据库中常见为varchar类型




    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


#
@app.route('/js', methods=['GET'])
def lsdata():
    # f_list = []
    # connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
    #                              charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # cursor = connection.cursor()
    # cursor.execute('select industry from js_infos_finanData')
    # results = cursor.fetchall()
    # for item in results:
    #     data_du = item["industry"]
    #     f_list.append(data_du)
    # connection.commit()
    # connection.close()
    #
    # c = collections.Counter(f_list)
    #
    #
    # t = {}
    # t['data'] = c["銀行業"]
    #
    # return jsonify(t)


    big_list = []
    pls = db.session.query(Js_infos_finanData.industry).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    c = collections.Counter(pls)

    # zhijei
    # for item in pls:
    #     data_du = '銀行業'
    #     if data_du in item:
    #
    #         big_list.append(data_du)
    # return
# 有时候需要用int()函数转换字符串为整型，但是切记int()只能转化由纯数字组成的字符串，如下例：a
    t = {}
    t['data'] = [c["銀行業",] ,c["小売業",],c["電気機器",],c["不動産業",],c["建設業",]]

    # {
    #   "data": 82
    # }
    return jsonify(t)

# #{
#   "data": [
#     82,
#     359,
#     246,
#     135,
#     161
#   ]
# }

if __name__ == '__main__':
    app.run(debug=True)
