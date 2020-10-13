#-*- coding:utf-8 -*-


import datetime
import time
import pymysql


# 现在就比对两个表：new_basictable   ,final_fff

# new_basictable
# 字段
# NB_TRAN_ID
# NB_TRAN_NAME
# NB_LINE_ID
# NB_LINE_NAME
# NB_line_stopTime
# NB_line_stopTime_Plus5
# NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5


# final_fff
# q1_line_id,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5
# 字段
# q1_line_id
# NB_LINE_NAME
# NB_line_stopTime
# NB_line_stopTime_Plus5
#
# 所以,在4个字段同时相同的情况下,表一,这样就有了设备的信息

def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    # 制作l1
    count_sql = "select count(*) from new_basictable; "
    cursor.execute(count_sql)
    long_count1 = cursor.fetchone()['count(*)']

    for page1 in range(1, long_count1 + 1):
        SQL_search1 = 'select id,NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5 from new_basictable where id = %s  '%  page1
        cursor.execute(SQL_search1)
        # #获取所有记录列表
        data1 = cursor.fetchone()
        B_biascTable_id = data1["id"]
        q1_NB_TRAN_ID = data1["NB_TRAN_ID"]
        q1_NB_TRAN_NAME = data1["NB_TRAN_NAME"]
        q1_NB_LINE_ID = data1["NB_LINE_ID"]
        q1_NB_LINE_NAME = data1["NB_LINE_NAME"]
        q1_NB_line_stopTime = data1["NB_line_stopTime"]
        q1_NB_line_stopTime_Plus5= data1["NB_line_stopTime_Plus5"]

        q1_list.append((B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5))
    # 之前没有必要嵌套遍历！


    # 制作l2
    count_sql = "select count(*) from final_fff; "
    cursor.execute(count_sql)
    long_count2 = cursor.fetchone()['count(*)']
    for page2 in range(1, long_count2 + 1):
        SQL_search2 = 'select q1_line_id,NB_LINE_NAME,NB_line_stopTime,NB_line_stopTime_Plus5 from final_fff where id = %s ' % page2
        cursor.execute(SQL_search2)
        # #获取所有记录列表
        data2 = cursor.fetchone()
        q2_q1_line_id = data2["q1_line_id"]
        q2_NB_LINE_NAME = data2["NB_LINE_NAME"]
        q2_NB_line_stopTime = data2["NB_line_stopTime"]
        q2_NB_line_stopTime_Plus5 = data2["NB_line_stopTime_Plus5"]
        q2_list.append((q2_q1_line_id,q2_NB_LINE_NAME,q2_NB_line_stopTime,q2_NB_line_stopTime_Plus5))



def ccc_data(l1, l2):

    try:
        l3 = []

        for item_q1 in l1:
            B_biascTable_id = item_q1[0]
            q1_NB_TRAN_ID = item_q1[1]
            q1_NB_TRAN_NAME = item_q1[2]
            q1_NB_LINE_ID = item_q1[3]
            q1_NB_LINE_NAME = item_q1[4]
            q1_NB_line_stopTime = item_q1[5]
            q1_NB_line_stopTime_Plus5 = item_q1[6]

            for item_q2 in l2:
                q2_q1_line_id = item_q2[0]
                q2_NB_LINE_NAME = item_q2[1]
                q2_NB_line_stopTime = item_q2[2]
                q2_NB_line_stopTime_Plus5 = item_q2[3]

                if q1_NB_LINE_ID==q2_q1_line_id and q1_NB_LINE_NAME ==q2_NB_LINE_NAME and q1_NB_line_stopTime == q2_NB_line_stopTime and q1_NB_line_stopTime_Plus5 ==q2_NB_line_stopTime_Plus5 :
                    f_tuple =tuple((B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5)) #大变压器表的id,变压器名称，线路名称，基准表的线路名称
                    l3.append(f_tuple)
                else:
                    pass
        return l3


    except:
        pass


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into 5400_B_basic_5400 (B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5) values (%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass





if __name__ == "__main__":
    q1_list = []
    q2_list =[]
    print(datetime.datetime.now())
    CutData_insert()
    f_content = ccc_data(q1_list,q2_list)
    insertDB(f_content)


    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())




# B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5
create table 5400_B_basic_5400_D(
id int not null primary key auto_increment,
B_biascTable_id text ,
q1_NB_TRAN_ID text,
q1_NB_TRAN_NAME text,
q1_NB_LINE_ID text,
q1_NB_LINE_NAME text,
q1_NB_line_stopTime text,
q1_NB_line_stopTime_Plus5 text
) engine=InnoDB default charset=utf8;

#  drop table 5400_B_basic_5400;

# 剔除重复后，重新插入新表中
insert into 5400_B_basic_5400_D (B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5) select distinct B_biascTable_id,q1_NB_TRAN_ID,q1_NB_TRAN_NAME,q1_NB_LINE_ID,q1_NB_LINE_NAME,q1_NB_line_stopTime,q1_NB_line_stopTime_Plus5 from 5400_B_basic_5400  ;

create table 5400_B_basic_5400_D(
id int not null primary key auto_increment,
B_biascTable_id text ,
q1_NB_TRAN_ID text,
q1_NB_TRAN_NAME text,
q1_NB_LINE_ID text,
q1_NB_LINE_NAME text,
q1_NB_line_stopTime text,
q1_NB_line_stopTime_Plus5 text
) engine=InnoDB default charset=utf8;


# drop table 5400_B_basic_5400_D;
