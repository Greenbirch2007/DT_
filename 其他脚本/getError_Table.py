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
        # 制作l1
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



        # 制作l2
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

        # 制作b_list
        # count_sql = "select count(*) from dt2; "
        # cursor.execute(count_sql)
        # long_count2 = cursor.fetchone()['count(*)']
        # for page2 in range(1, long_count2 + 1):
        #     SQL_search2 = 'select byq_name from dt2 where id = %s ' % page2
        #     cursor.execute(SQL_search2)
        #     # #获取所有记录列表
        #     data2 = cursor.fetchone()
        #     q2_BN = data2["byq_name"]
        #     b2_list.append(q2_BN)

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


# 先匹配变压器数据，然后是验证是否在一个容器中(一个遍历加一个容器判断)
# def ccc_data(l1,l2):
#     l3 = []
#     for item_q1 in l1:
#         qq1_1 = item_q1[1:2] # 只要b1的名称相同再去匹配，不相同就不管了
#         qq1_2 = item_q1[1:] #  b1,x1数据
#         for item_q2 in l2:
#             qq2_1 = item_q2[0] #  b2数据
#             if qq1_1 == qq2_1: # b1 = b2
#                 if ( qq1_2 not in l2):  # b1,x1 !=  b2,x2 的容器
#                     l3.append(item_q1)
#                 else:
#                     pass
#             else:
#                 pass
#
#     return l3

# 直接两层遍历

#


def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            qq1_1 = item_q1[1]  # 只要b1的名称相同再去匹配，不相同就不管了
            qq1_2 = item_q1[1:]  # b1,x1数据
            for item_q2 in l2:
                qq2_1 = item_q2[0]  # b2数据 字符串
                qq2_2 = item_q2[1:]  # b2数据 元组拼接

                if qq1_1 == qq2_1 and qq1_2 != item_q2 :
                    err_table = item_q1 + qq2_2 # 形成最终错误比对的元组

                    l3.append(err_table)
                else:
                    pass

        return l3
    except:
        pass


if __name__ == "__main__":

    print(datetime.datetime.now())
    q1_list = []
    q2_list = []
    # b2_list =[] # b基准数据容器

    CutData_insert()

    f_content = ccc_data(q1_list,q2_list)


    insertDB(f_content)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
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



# DT,byq_name,Oper_line_name,Baseline_line_name
# create table error_table(
# id int not null primary key auto_increment,
# DT text,
# byq_name text,
# Oper_line_name text,
# Baseline_line_name text
# ) engine=InnoDB default charset=utf8;



118shu ju ku
