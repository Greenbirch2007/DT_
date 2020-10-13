#-*- coding:utf-8 -*-


import datetime
import time
import pymysql
import copy

# 现在就比对两个表：newbasic_again   ,final_5491_indb
#
# 在变压器id相同的情况下，只要线路id不同就输出
#
# 这时还是输出整体的变压器id,变压器名称，线路id，线路名称！
#
# 这个时候再少挂载的时候就直接得出结果接口
#
# 多挂载的情况下，因为变压器id和线路id是一一绑定的，再用294多条去5400条明细里面去找，多挂载的明细

# 直接解析线路id有问题，现在直接用5400企业去跑5400的大基准表
def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    # 制作l1
    count_sql = "select count(*) from final_5491_indb; "
    cursor.execute(count_sql)
    long_count1 = cursor.fetchone()['count(*)']

    for page1 in range(1, long_count1 + 1):
        SQL_search1 = 'select BYQ_t_id,shebei_id,taiqu_name,line_id,line_name from final_5491_indb where id = %s  '%  page1
        cursor.execute(SQL_search1)
        # #获取所有记录列表
        data1 = cursor.fetchone()
        q1_BYQ_t_id = data1["BYQ_t_id"]
        q1_shebei_id = data1["shebei_id"]
        q1_taiqu_name = data1["taiqu_name"]
        q1_line_id = data1["line_id"]
        q1_line_name = data1["line_name"]
        q1_list.append((q1_BYQ_t_id,q1_shebei_id,q1_taiqu_name,q1_line_id,q1_line_name))

    # 之前没有必要嵌套遍历！


    # 制作l2
    count_sql = "select count(*) from newbasic_again; "
    cursor.execute(count_sql)
    long_count2 = cursor.fetchone()['count(*)']
    for page2 in range(1, long_count2 + 1):
        SQL_search2 = 'select NB_TRAN_ID,NB_TRAN_NAME,NB_LINE_ID,NB_LINE_NAME from newbasic_again where id = %s ' % page2
        cursor.execute(SQL_search2)
        # #获取所有记录列表
        data2 = cursor.fetchone()
        q2_NB_TRAN_ID = data2["NB_TRAN_ID"]
        q2_NB_TRAN_NAME = data2["NB_TRAN_NAME"]
        q2_NB_LINE_ID = data2["NB_LINE_ID"]
        q2_NB_LINE_NAME = data2["NB_LINE_NAME"]
        q2_list.append((q2_NB_TRAN_ID,q2_NB_TRAN_NAME,q2_NB_LINE_ID,q2_NB_LINE_NAME))
        baiyaqi_name.append(q2_NB_TRAN_NAME)



def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            q1_BYQ_t_id = item_q1[0]
            q1_shebei_id = item_q1[1]
            q1_taiqu_name = item_q1[2]
            q1_line_id = item_q1[3]
            q1_line_name = item_q1[4]

            for item_q2 in l2:
                q2_NB_TRAN_ID = item_q2[0]
                q2_NB_TRAN_NAME = item_q2[1]
                q2_NB_LINE_ID = item_q2[2]
                q2_NB_LINE_NAME = item_q2[3]

                if q1_line_id == q2_NB_LINE_ID and (q1_taiqu_name not in baiyaqi_name) :
                    l3.append((q1_BYQ_t_id,q1_shebei_id,q1_taiqu_name,q1_line_id,q1_line_name))
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
        cursor.executemany("insert into 2_4w_5400_B_X (BYQ_t_id,shebei_id,taiqu_name,line_id,line_name) values (%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass





if __name__ == "__main__":
    q1_list = []
    q2_list =[]
    baiyaqi_name =[] # 集合剔除重复项

    print(datetime.datetime.now())
    CutData_insert()

    f_content = ccc_data(q1_list,q2_list)
    insertDB(f_content)



    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())




#BYQ_t_id,shebei_id,taiqu_name,line_id,line_name
# create table 2_4w_5400_B_X(
# id int not null primary key auto_increment,
# BYQ_t_id text,
# shebei_id text,
# taiqu_name text,
# line_id text,
# line_name text
# ) engine=InnoDB default charset=utf8;



# drop table 2_4w_5400_B_X;
# q1_list
