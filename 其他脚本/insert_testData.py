#-*- coding:utf-8 -*-


import pymysql




class A_testData():
    def __init__(self):
        pass
    # 实际运行表数据
    def insertData1(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        try:
            content = []
            for al in ["a", "b", "c", "d", "e", "f", "g"]:
                for num in range(1, 66666):
                    f_tu = tuple((al, num, "我是基准表数据"))
                    content.append(f_tu)
            print(content)

            # cursor.executemany('insert into Demo_BYQ1 (BYQ_Num,XL_Num,item) values (%s,%s,%s)', content)
            # connection.commit()
            # connection.close()
            # print('向MySQL中添加数据成功！')
        except StopIteration:
            pass
     # 基准表
    def insertData2(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()


        try:
            content = []
            for al in ["a", "b", "e", "f", "g"]:
                for num in range(1, 35000,2):
                    f_tu = tuple((al, num, "我是基准表数据"))
                    content.append(f_tu)
            print(content)

            cursor.executemany('insert into Demo_BYQ2 (BYQ_Num,XL_Num,item) values (%s,%s,%s)', content)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except StopIteration:
            pass

    # 添加一些错误数据
    def insertData3(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        try:
            content = []

            f_tu = tuple(("a", 98, "~~一些错误数据~~"))
            content.append(f_tu)
            print(content)

            cursor.executemany('insert into Demo_BYQ1 (BYQ_Num,XL_Num,item) values (%s,%s,%s)', content)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except StopIteration:
            pass



in_ = A_testData()
in_.insertData1()
# in_.insertData2()
# in_.insertData3()

print("数据插入结束！")


#
# 测试总表  id,BYQ_Num,XL_Num,item
# create table Demo_BYQ(
# id int not null primary key auto_increment,
# sep_q1_id varchar(10),
# BYQ_Num varchar(10),
# XL_Num varchar(10),
# item  varchar(20)
# ) engine=InnoDB  charset=utf8;
#
#
#
# 测试表１ １－３００００　，共30000万条
# create table Demo_BYQ1(
# id int not null primary key auto_increment,
# BYQ_Num varchar(10),
# XL_Num varchar(10),
# item  varchar(20)
# ) engine=InnoDB  charset=utf8;
#
# 测试表2  １，３，５....　共1０００条
# create table Demo_BYQ2(
# id int not null primary key auto_increment,
# BYQ_Num varchar(10),
# XL_Num varchar(10),
# item  varchar(20)
# ) engine=InnoDB  charset=utf8;






# 查询两个数据表的差异
# select count(*)from Demo_BYQ1 where XL_Num not in (select XL_Num  from Demo_BYQ2) ;
#
#
#
#
# select * from Demo_BYQ1 where XL_Num not in (select XL_Num  from Demo_BYQ2) ;
