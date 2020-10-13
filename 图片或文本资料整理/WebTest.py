# coding=utf-8




# coding:utf-8
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文


# 在Flask里 sqlachemy是非常方便的，但是假如数据量很大的话，
# 后台返回的json速度就很慢，很影响用户体验，所以用paginate来分页返回数据paginate(id, num)
#  #id为第几页 num表示一页有几条数据很明显
# 我们的页数应该是 [1,sum/num]所以在前台的页数应该是 1到 数据总数/一页的数据量例如 有7311条数据，
# 我们需要一页10条数据的话页数就是 1 ~ 732 因为还有 最后一页 只有一条数据

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/DT'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class Tdata(Base):
    __tablename__ = 'Tdata'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    t1 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t2 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t3 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t4 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t5 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t6 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t7 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型
    t8 = Column(String(20),nullable=True)  # String在数据库中常见为varchar类型




    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict



@app.route('/')
def index():
    return '<h1>"欢迎来到接口界面"</h1>'



@app.route('/td/count')
def lsdata_count():
    num = db.session.query(Tdata.t1).count()
    # return "'<h1>数据库的字段数为:% </h1>' % num "
    return jsonify({"数据库的字段总数":num})



# 思考如何把查询的数据变成一个大字典！而不是若干个小字典！
# 从数据库中一次全部查询展示成功
# 数据接口,API
@app.route('/td', methods=['GET'])
def lsdata():
    big_list = []
    p1 = db.session.query(Tdata.t1)
    p2 = db.session.query(Tdata.t2)  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p3 = db.session.query(Tdata.t3).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p4 = db.session.query(Tdata.t4).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p5 = db.session.query(Tdata.t5).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p6 = db.session.query(Tdata.t6).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p7 = db.session.query(Tdata.t7).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # p8 = db.session.query(Tdata.t8).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    # for i1,i2,i3,i4,i5,i6,i7,i8 in zip(p1,p2,p3,p4,p5,p6,p7,p8):
    #     big_list.append((i1,i2,i3,i4,i5,i6,i7,i8))
    big_list.append(p1,p2)

    # for item in pls:
    #      for i in item:
    #          num_int = float(i)
    #          big_list.append(num_int)  # 需要把字符串类型转换为浮点型,而不是整型
# 有时候需要用int()函数转换字符串为整型，但是切记int()只能转化由纯数字组成的字符串，如下例：a
    t = {}
    t['t1'] = big_list[0]
    t['t2'] = big_list[1]
    return jsonify(t)

# 关键是前端可以使用的数据格式是什么！　所以前端也要开始　了 也就是前端好不好用！接口有没有用！
    # big_list = {}
    # for item in comments:
    #     big_list.insert(item)
    # return jsonify({'data':big_list})
    # result = []
    # for comment in comments:
    #     result.append(comment.to_json())   # 用到了模型中的转换方法！　映射是成功的！　先做思考分页
    # return jsonify(result), 200






if __name__ == '__main__':
    app.run(debug=True)

