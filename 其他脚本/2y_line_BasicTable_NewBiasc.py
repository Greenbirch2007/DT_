#-*- coding:utf-8 -*-


import datetime
import time
import pymysql



def CutData_insert():

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql = "select count(*) from B_line; "
        cursor.execute(count_sql)
        long_count1 = cursor.fetchone()['count(*)']

        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select B_line_id,B_line_name,B_line_stopTime,B_line_stopTime_Plus5 from B_line where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_line_id = data1["B_line_id"]
            q1__line_name = data1["B_line_name"]
            q1_line_stopTime = data1["B_line_stopTime"]
            q1_line_stopTime_Plus5 = data1["B_line_stopTime_Plus5"]
            q1_list.append((q1_line_id,q1__line_name,q1_line_stopTime,q1_line_stopTime_Plus5))
        # 之前没有必要嵌套遍历！



        # 制作l2
        count_sql = "select count(*) from Basic_table; "
        cursor.execute(count_sql)
        long_count2 = cursor.fetchone()['count(*)']
        for page2 in range(1, long_count2 + 1):
            SQL_search2 = 'select TRAN_ID,TRAN_NAME,LINE_ID,LINE_NAME  from Basic_table where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q2_TRAN_ID = data2["TRAN_ID"]
            q2_TRAN_NAME = data2["TRAN_NAME"]
            q2_LINE_ID = data2["LINE_ID"]
            q2_LINE_NAME = data2["LINE_NAME"]
            q2_list.append((q2_TRAN_ID,q2_TRAN_NAME,q2_LINE_ID,q2_LINE_NAME))

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into New_BasicTable (NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5) values (%s,%s,%s,%s,%s,%s)", content)
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
# l2 = (q2_BN,q2_LINE_NAME,q2_LINE_ID)
def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            q1_line_id = item_q1[0]
            q1__line_name = item_q1[1]
            q1_line_stopTime = item_q1[2]
            q1_line_stopTime_Plus5 = item_q1[3]

            for item_q2 in l2:
                q2_TRAN_ID = item_q2[0]
                q2_TRAN_NAME = item_q2[1]
                q2_LINE_ID = item_q2[2]
                q2_LINE_NAME = item_q2[3]

                if q1_line_id == q2_LINE_ID:
                    f_tuple =tuple((q2_TRAN_ID,q2_TRAN_NAME,q2_LINE_ID,q2_LINE_NAME,q1_line_stopTime,q1_line_stopTime_Plus5)) #大变压器表的id,变压器名称，线路名称，基准表的线路名称
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
    print(len(q1_list))
    print(len(q2_list))
    # f_content = ccc_data(q1_list,q2_list)
    # insertDB(f_content)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())




# NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5
# create table New_BasicTable(
# id int not null primary key auto_increment,
# NB_TRAN_ID text,
# NB_TRAN_NAME text,
# NB_LINE_ID text,
# NB_LINE_NAME text,
# NB_line_stopTime text,
# NB_line_stopTime_Plus5 text
# ) engine=InnoDB default charset=utf8;


