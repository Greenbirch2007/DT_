#-*- coding:utf-8 -*-


import datetime
import time
import pymysql


f_l =[]

# 直接解析线路id有问题，现在直接用5400企业去跑5400的大基准表
def CutData_insert():
    q2_list = []

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    count_sql = "select count(*) from New_BasicTable; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    for num in range(1, long_count+1):
        sql = 'select NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5 from New_BasicTable where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data2 = cur.fetchone()
        q2_NB_TRAN_ID = data2["NB_TRAN_ID"]
        q2_NB_TRAN_NAME = data2["NB_TRAN_NAME"]
        q2_NB_LINE_ID = data2["NB_LINE_ID"]
        q2_NB_LINE_NAME = data2["NB_LINE_NAME"]
        q2_NB_line_stopTime = data2["NB_line_stopTime"]
        q2_NB_line_stopTime_Plus5 = data2["NB_line_stopTime_Plus5"]
        if q2_NB_LINE_ID in f_l:
             q2_list.append((q2_NB_TRAN_ID,q2_NB_TRAN_NAME,q2_NB_LINE_ID,q2_NB_LINE_NAME,q2_NB_line_stopTime,q2_NB_line_stopTime_Plus5))
        else:
            pass
    return q2_list






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into newBasic_again (NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5) values (%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass





if __name__ == "__main__":

    print(datetime.datetime.now())


    content = CutData_insert()
    insertDB(content)


    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())




# NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5
# create table newBasic_again(
# id int not null primary key auto_increment,
# NB_TRAN_ID text,
# NB_TRAN_NAME text,
# NB_LINE_ID text,
# NB_LINE_NAME text,
# NB_line_stopTime text,
# NB_line_stopTime_Plus5 text
# ) engine=InnoDB default charset=utf8;


