#! -*- coding:utf-8 -*-
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model_Class import F_error_lname_data,B_byq_table,Basic_table
import copy
import operator

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/DT'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)






@app.route('/index')
def index():
    return render_template('index.html')



# 使用接口后的渲染接口
# 这还只是一个静态的页面,不会自助
@app.route('/feabledt/show')
def feabledtShow():
    return render_template('_static_html.html') # 在一个目录下,templates中




# 思考如何把查询的数据变成一个大字典！而不是若干个小字典！
# 从数据库中一次全部查询展示成功
# 数据接口,API

@app.route('/feabledt/', methods=['GET'])
def feabledt():
    big_list = []
    p_cu_name = db.session.query(F_error_lname_data.cu_name).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_taiqu_name = db.session.query(F_error_lname_data.taiqu_name).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_Error_line_name = db.session.query(F_error_lname_data.Error_line_name).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_basicT_line_name = db.session.query(F_error_lname_data.basicT_line_name).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_yonghu_name = db.session.query(F_error_lname_data.yonghu_name).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_stopC_time= db.session.query(F_error_lname_data.stopC_time).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表

    for i1,i2,i3,i4,i5,i6 in zip(p_cu_name,p_taiqu_name,p_Error_line_name,p_basicT_line_name,p_yonghu_name,p_stopC_time):
        # [{字典1}，{字典2},...]
        f_disc =dict({"A":i1[0],"B":i2[0],"C":i3[0],"D":i4[0],"E":i5[0],"F":i6[0]})
        big_list.append(f_disc)
    #  专门针对日期进行整体的排序
    big_list.sort(key=operator.itemgetter("F"), reverse=True)  # 这个日期是可用的，依然保持了列表中包裹字典！
    f_dic = {"data":big_list}
    return jsonify(f_dic)
#




@app.route('/byqabledt/show')
def byqabledtShow():
    return render_template('_byqstatic_html.html') # 在一个目录下,templates中


#  为了做展示的使用，18条，先展示5k条(倒序)
@app.route('/byqabledt/', methods=['GET'])
def byqabledt():
    big_list = []
    p_CU_LOC2_NAME = db.session.query(B_byq_table.cu_loc2_name).order_by(B_byq_table.cu_loc2_name.desc()).limit(5000) # desc()默认是降序
    p_CU_NAME = db.session.query(B_byq_table.cu_name).order_by(B_byq_table.cu_name.desc()).limit(5000) # desc()默认是降序
    p_TAIQU_NAME = db.session.query(B_byq_table.taiqu_name).order_by(B_byq_table.taiqu_name.desc()).limit(5000)# desc()默认是降序
    p_LINE_NAME = db.session.query(B_byq_table.line_name).order_by(B_byq_table.line_name.desc()).limit(5000) # desc()默认是降序
    p_YONGHU_NAME = db.session.query(B_byq_table.yonghu_name).order_by(B_byq_table.yonghu_name.desc()).limit(5000) # desc()默认是降序
    p_sSTOPC_TIME= db.session.query(B_byq_table.stopC_time).order_by(B_byq_table.stopC_time.desc()).limit(5000) # desc()默认是降序

    for i1,i2,i3,i4,i5,i6 in zip(p_CU_LOC2_NAME,p_CU_NAME,p_TAIQU_NAME,p_LINE_NAME,p_YONGHU_NAME,p_sSTOPC_TIME):
        # [{字典1}，{字典2},...]
        f_disc =dict({"A":i1[0],"B":i2[0],"C":i3[0],"D":i4[0],"E":i5[0],"F":i6[0]})
        big_list.append(f_disc)
    # big_list.sort(key=operator.itemgetter("F"), reverse=True)  # 这个日期是可用的，依然保持了列表中包裹字典！

    f_dic = {"data":big_list}

    return jsonify(f_dic)





@app.route('/basicabledt/show')
def basicabledtShow():
    return render_template('_basicstatic_html.html') # 在一个目录下,templates中



@app.route('/basicabledt/', methods=['GET'])
def basicabledt():
    big_list = []
    p_TRAN_NAME = db.session.query(Basic_table.TRAN_NAME).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    p_LINE_NAME = db.session.query(Basic_table.LINE_NAME).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表


    for i1,i2 in zip(p_TRAN_NAME,p_LINE_NAME):
        # [{字典1}，{字典2},...]
        f_disc =dict({"A":i1[0],"B":i2[0]})
        big_list.append(f_disc)
    f_dic = {"data":big_list}
    return jsonify(f_dic)











if __name__ == '__main__':

    app.run(debug=True)
