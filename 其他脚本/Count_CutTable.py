import datetime
import time

import pymysql
import multiprocessing



# @jit(nopython=True) # jit，numba装饰器中的一种
def CutData_insert():

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        count_sql = "select count(*) from dt1; "
        cursor.execute(count_sql)
        long_count1 = cursor.fetchone()['count(*)']

        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select DT,byq_name,line_name from dt1 where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_id = data1["DT"]
            q1_BN = data1["byq_name"]
            q1_XL = data1["line_name"]
            q1_list.append((q1_id,q1_BN,q1_XL))
        # 之前没有必要嵌套遍历！

        count_sql = "select count(*) from dt2; "
        cursor.execute(count_sql)
        long_count2 = cursor.fetchone()['count(*)']
        for page2 in range(1, long_count2 + 1):
            SQL_search2 = 'select byq_name,line_name from dt2 where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q2_BN = data2["byq_name"]
            q2_XL = data2["line_name"]
            q2_list.append((q2_BN,q2_XL))

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into f_dt (DT,byq_name,line_name) values (%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



def ccc_data(l1,l2):
    l3 = []
    for item_q1 in l1:
        qq = item_q1[1:]
        if (qq not in l2):

            l3.append(item_q1)

    return l3


# Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
# 每次循环将会用空闲出来的子进程去调用目标

if __name__ == "__main__":

    print(datetime.datetime.now())
    q1_list = []
    q2_list = []

    CutData_insert()
    for item in q2_list:
        print(item)
    # f_content = ccc_data(q1_list,q2_list)
    #
    #
    # insertDB(f_content)
    # print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())
    #





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