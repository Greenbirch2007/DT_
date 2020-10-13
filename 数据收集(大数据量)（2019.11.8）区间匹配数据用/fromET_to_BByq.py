#-*- coding:utf-8 -*-


import datetime
import time
import pymysql



# @jit(nopython=True) # jit，numba装饰器中的一种
def CutData_insert():

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql = "select count(*) from B_BYQ_table; "
        cursor.execute(count_sql)
        long_count1 = cursor.fetchone()['count(*)']

        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select BYQ_t_id,taiqu_name,line_name,shebei_id,line_id from B_BYQ_table where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_id = data1["BYQ_t_id"]
            q1_taiqu_name = data1["taiqu_name"]
            q1_line_name = data1["line_name"]
            q1_shebei_id = data1["shebei_id"]
            q1_line_id = data1["line_id"]
            q1_list.append((q1_id,q1_taiqu_name,q1_line_name,q1_shebei_id,q1_line_id))
        # 之前没有必要嵌套遍历！



        # 制作l2
        count_sql = "select count(*) from Basic_table; "
        cursor.execute(count_sql)
        long_count2 = cursor.fetchone()['count(*)']
        for page2 in range(1, long_count2 + 1):
            SQL_search2 = 'select TRAN_ID,LINE_NAME,LINE_ID from Basic_table where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q2_BN = data2["TRAN_ID"]
            q2_LINE_NAME = data2["LINE_NAME"]
            q2_LINE_ID = data2["LINE_ID"]
            q2_list.append((q2_BN,q2_LINE_NAME,q2_LINE_ID))

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into error_table (DT,byq_name,Oper_line_name,Baseline_line_name) values (%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass


def Python_sel_DB():
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    count_sql = "select count(*) from error_table; "
    cursor.execute(count_sql)
    long_count = cursor.fetchone()['count(*)']
    for err_num in range(1, long_count + 1):
        err_searsql = 'select DT from error_table where id = %s ' % err_num
        cursor.execute(err_searsql)
        data = cursor.fetchone()
        num = data["DT"]
        yield num



if __name__ == "__main__":
    for item in Python_sel_DB():
        print(item)








# DT,byq_name,line_name
# create table dt1(
# id int not null primary key auto_increment,
# DT text,
# byq_name text,
# line_name text
# ) engine=InnoDB default charset=utf8;
#
#
#
# create table dt2(
# id int not null primary key auto_increment,
# byq_name text,
# line_name text
# ) engine=InnoDB default charset=utf8;



# DT,byq_name,line_name
# create table f_dt(
# id int not null primary key auto_increment,
# DT text,
# byq_name text,
# line_name text
# ) engine=InnoDB default charset=utf8;



# DT,byq_name,Oper_line_name,Baseline_line_name
# create table error_table(
# id int not null primary key auto_increment,
# DT text,
# byq_name text,
# Oper_line_name text,
# Baseline_line_name text
# ) engine=InnoDB default charset=utf8;


