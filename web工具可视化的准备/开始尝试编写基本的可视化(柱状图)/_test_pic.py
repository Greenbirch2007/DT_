from flask import Flask,jsonify,render_template
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()




@app.route("/")
def index():
    return "<h1>测试Highcharts写接口</h1>"





@app.route('/show')
def showDataTable():
    return render_template('_static_html.html')



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

    pls = db.session.query(Js_infos_finanData.industry).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    c = collections.Counter(pls)
    t = {}
    t['data'] = [c["銀行業",] ,c["小売業",],c["電気機器",],c["不動産業",],c["建設業",]]

    return jsonify(t)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False # 避免接口汉字出现乱码
    app.run(debug=True)

