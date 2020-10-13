#-*- coding:utf-8 -*-

import datetime
import time
import pymysql



def twoTStyle(sttime):
    str_len = len(sttime)
    time_cut1 = "%Y/%m/%d %H:%M:%S"
    time_cut2 = "%Y/%m/%d %H:%M"
    if str_len == 18: #还是对日期的处理出现了问题
        s1_time = datetime.datetime.strptime(sttime, time_cut1)
        return s1_time
    else:
        s2_time = datetime.datetime.strptime(sttime, time_cut2)
        return s2_time
#还是返回整型int
def copare_twoTime(s1_time,s2_time):
    d1_time = twoTStyle(s1_time)
    d2_time = twoTStyle(s2_time)

    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec


def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql1 = "select count(*) from B_BYQ_table; "
        cursor.execute(count_sql1)
        long_count1 = cursor.fetchone()['count(*)']
        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select BYQ_t_id,line_id,shebei_id,taiqu_name,stopC_time from B_BYQ_table where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_id = data1["BYQ_t_id"]
            q1_line_id = data1["line_id"]
            q1_shebei_id = data1["shebei_id"]
            q1_taiqu_name = data1["taiqu_name"]
            q1_stopC_time = data1["stopC_time"]
            q1_list.append((q1_id,q1_line_id,q1_shebei_id,q1_taiqu_name,q1_stopC_time))
        # 之前没有必要嵌套遍历！



        # 制作l2
        count_sql2 = "select count(*) from b_line; "
        cursor.execute(count_sql2)
        long_count2 = cursor.fetchone()['count(*)']
        for page2 in range(1, long_count2 + 1):
            SQL_search2 = 'select B_linetable_id,B_line_stopTime,B_line_name,B_line_id,B_line_Byq_Num,B_line_stopTime_Plus5 from New_BasicTable where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q1_B_linetable_id = data2["B_linetable_id"]
            q1_line_stopTime = data2["B_line_stopTime"]
            q1_line_name = data2["B_line_name"]
            q1_line_id = data2["B_line_id"]
            q1_line_Byq_Num = data2["B_line_Byq_Num"]
            q1_line_stopTime_Plus5 = data2["B_line_stopTime_Plus5"]

            q2_list.append((q1_B_linetable_id,q1_line_stopTime,q1_line_name,q1_line_id,q1_line_Byq_Num,q1_line_stopTime_Plus5))

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into new_BYQ_table (DT,f_line_id,f_line_stopTime) values (%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



# 直接两层遍历

#  之前已经针对1.线路相同 2. 时间控制1小时之内
# 输出什么？输出新的大变压器表(然后再按照大基准表的方式计数，然后再比对)
# 保留什么字段？
def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            q1_id = item_q1[0]
            q1_line_id = item_q1[1]
            q1_shebei_id = item_q1[2]
            q1_taiqu_name = item_q1[3]
            q1_stopC_time = item_q1[4]

            for item_q2 in l2:
                q1_B_linetable_id = item_q2[0]
                q1_line_stopTime =  item_q2[1]
                q1_line_name = item_q2[2]
                q1_line_id =  item_q2[3]
                q1_line_Byq_Num =  item_q2[4]
                q1_line_stopTime_Plus5 =  item_q2[5]
                # 1.线路相同的情况下，2. 变压器停电时间大于基准表的最低时间 3. 小于增加5分钟的基准标的停电时间
                #　4.把时间缩小在时刻（缩小在1小时之内） '2018/01/02 16:'
                # if q1_line_id == NB_LINE_ID and q1_stopC_time[:14] ==q1_line_stopTime[:14] : #还输出29万条数据
                # 小于等于，大于等于不是随便处理的！！！！！
                # >=,而不是=>    小于等于<=,不是=<
                # 布尔值 不能与 整型
                if q1_line_id == NB_LINE_ID and

                    l3.append((q1_id,q1_line_id,q1_stopC_time))


                else:
                    pass

        return l3
    except:
        pass



# 大变压器表-----大基准表(有计数的)
# 1.线路id相同，2.时间控制在1小时内，
# 输出大基准表id,
if __name__ == "__main__":

    print(datetime.datetime.now())
    q1_list = []
    q2_list = []
    # b2_list =[] # b基准数据容器
    CutData_insert()
    print(len(q1_list))
    print(len(q2_list))

    f_content = ccc_data(q1_list,q2_list)

    insertDB(f_content)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())









# DT,f_line_id,f_line_stopTime
# create table new_BYQ_table(
# id int not null primary key auto_increment,
# DT text,
# f_line_id text,
# f_line_stopTime text
# ) engine=InnoDB default charset=utf8;


