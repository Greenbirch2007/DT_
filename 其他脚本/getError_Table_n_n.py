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
            SQL_search2 = 'select TRAN_NAME,TRAN_ID,LINE_NAME,LINE_ID from Basic_table where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q2_BN = data2["TRAN_NAME"]
            q2_TRAN_id = data2["TRAN_ID"]
            q2_LINE_NAME = data2["LINE_NAME"]
            q2_LINE_ID = data2["LINE_ID"]
            q2_list.append((q2_BN,q2_TRAN_id,q2_LINE_NAME,q2_LINE_ID))

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into error_table_n_n (DT,byq_name,Oper_line_name,Baseline_line_name,q1_line_id,q2_LINE_ID) values (%s,%s,%s,%s,%s,%s)", content)
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
# l1 id, 变压器name,线路名称,变压器id,，线路id
# l2 变压器编号，线路名称，线路id
# l1= (q1_id,q1_taiqu_name,q1_line_name,q1_shebei_id,q1_line_id)
# l2 = (q2_BN,q2_TRAN_id,q2_LINE_NAME,q2_LINE_ID)
def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            q1_id = item_q1[0]
            q1_taiqu_name = item_q1[1]
            q1_line_name = item_q1[2]
            q1_shebei_id = item_q1[3]
            q1_line_id = item_q1[4]


            for item_q2 in l2:
                q2_BN = item_q2[0]  # b2数据 字符串
                q2_TRAN_id = item_q2[1]  # b2数据 字符串
                q2_LINE_NAME = item_q2[2]  # b2数据 元组拼接
                q2_LINE_ID = item_q2[3]  # b2数据 元组拼接

                if q1_taiqu_name == q2_BN and q1_line_name != q2_LINE_NAME :
                    f_tuple =tuple((q1_id,q1_taiqu_name,q1_line_name,q2_LINE_NAME,q1_line_id,q2_LINE_ID)) #大变压器表的id,变压器名称，线路名称，基准表的线路名称
                    l3.append(f_tuple)
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






# DT,byq_name,Oper_line_name,Baseline_line_name,q1_line_id,q2_LINE_ID
# create table error_table_n_n(
# id int not null primary key auto_increment,
# DT text,
# byq_name text,
# Oper_line_name text,
# Baseline_line_name text,
# q1_line_id text,
# q2_LINE_ID text
# ) engine=InnoDB default charset=utf8;

