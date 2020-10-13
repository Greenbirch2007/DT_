#-*- coding:utf-8 -*-


import pymysql
import random



class A_testData():
    def __init__(self):
        pass
    # 实际运行表数据
    def becomeDate(self):

        al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n"]
        sl = ["部门1", "部门2", "部门3", "部门4", "部门5", "部门6", "部门7", "部门8"]
        try:
            content = []

            for item in range(1,888):
                f_tu = tuple((str(item),random.choice(sl),random.randint(1,999),random.choice(al),random.choice(al),
                              random.choice(al),random.choice(al),random.choice(al)))
                content.append(f_tu)

            return content
        except TypeError as e:
            pass
    def insertDB(self,content):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        try:

            cursor.executemany('insert into Tdata (t1,t2,t3,t4,t5,t6,t7,t8) values (%s,%s,%s,%s,%s,%s,%s,%s)', content)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except TypeError as e:
            pass


bn_ = A_testData()
c = bn_.becomeDate()
bn_.insertDB(c)


print("数据插入结束！")


#t1,t2,t3,t4,t5,t6,t7,t8
#  t1,t2,t3,t4,t5,t6,t7,t8
# create table Tdata(
# id int not null primary key auto_increment,
# t1 varchar(20),
# t2 varchar(20),
# t3 varchar(20),
# t4 varchar(20),
# t5 varchar(20),
# t6 varchar(20),
# t7 varchar(20),
# t8 varchar(20)
# ) engine=InnoDB  charset=utf8;

# drop  table Tdata;
#
