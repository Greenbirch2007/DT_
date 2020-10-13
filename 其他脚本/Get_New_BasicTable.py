#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy
import csv


# 制作新基准表的基础：加入了TG_ID的线变关系表 和 2018.7-2019的线路停电表
# 在PSSM_id相同的情况下，将线变关系表插入到线路停电表中，形成一个新表





def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql1 = "select count(*) from TG_ID____XB_table; "
        cursor.execute(count_sql1)
        long_count1 = cursor.fetchone()['count(*)']
        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID from TG_ID____XB_table where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_shebei_id = data1["shebei_id"]
            q1_shebei_name = data1["shebei_name"]
            q1_SBBM_ID = data1["SBBM_ID"]
            q1_line_id = data1["line_id"]
            q1_XBGXT_line_name = data1["XBGXT_line_name"]
            q1_TG_ID = data1["TG_ID"]

            q1_list.append((q1_shebei_id,q1_shebei_name,q1_SBBM_ID,q1_line_id,q1_XBGXT_line_name,q1_TG_ID))
        # 之前没有必要嵌套遍历！



        # 制作l2
        count_sql2 = "select count(*) from LineStop_Table201807_2019; "
        cursor.execute(count_sql2)
        long_count2 = cursor.fetchone()['count(*)']
        for page2 in range(1, long_count2 + 1):
            SQL_search2 = 'select city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,PMS_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date from LineStop_Table201807_2019 where id = %s ' % page2
            cursor.execute(SQL_search2)
            # #获取所有记录列表
            data2 = cursor.fetchone()
            q2_city_Name = data2["city_Name"]
            q2_Country_Name = data2["Country_Name"]
            q2_Yunwei_name = data2["Yunwei_name"]
            q2_BdZ_name = data2["BdZ_name"]
            q2_Sale_line_id = data2["Sale_line_id"]
            q2_PMS_line_id = data2["PMS_line_id"]
            q2_LineEStop_line_name = data2["LineEStop_line_name"]
            q2_E_StopTime = data2["E_StopTime"]
            q2_E_ResumeTime = data2["E_ResumeTime"]
            q2_StopTime_Long = data2["StopTime_Long"]
            q2_StopTime_Date = data2["StopTime_Date"]
            q2_list.append((q2_city_Name,q2_Country_Name,q2_Yunwei_name,q2_BdZ_name,q2_Sale_line_id,q2_PMS_line_id,q2_LineEStop_line_name,q2_E_StopTime,q2_E_ResumeTime,q2_StopTime_Long,q2_StopTime_Date))
    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into Get_NewBasci_Table (shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass




def ccc_data(l1, l2):
    try:

        l3 = []
        for item_q1 in l1:
            q1_shebei_id = item_q1[0]
            q1_shebei_name = item_q1[1]
            q1_SBBM_ID = item_q1[2]
            q1_line_id = item_q1[3]
            q1_XBGXT_line_name = item_q1[4]
            q1_TG_ID = item_q1[5]

            for item_q2 in l2:
                q2_city_Name = item_q2[0]
                q2_Country_Name = item_q2[1]
                q2_Yunwei_name = item_q2[2]
                q2_BdZ_name = item_q2[3]
                q2_Sale_line_id = item_q2[4]
                q2_PMS_line_id = item_q2[5]
                q2_LineEStop_line_name = item_q2[6]
                q2_E_StopTime = item_q2[7]
                q2_E_ResumeTime = item_q2[8]
                q2_StopTime_Long = item_q2[9]
                q2_StopTime_Date = item_q2[10]

                # 1.线路相同的情况下，2. 变压器停电时间大于基准表的最低时间 3. 小于增加5分钟的基准标的停电时间
                #　4.把时间缩小在时刻（缩小在1小时之内） '2018/01/02 16:'
                # if q1_line_id == NB_LINE_ID and q1_stopC_time[:14] ==q1_line_stopTime[:14] : #还输出29万条数据
                # 小于等于，大于等于不是随便处理的！！！！！
                # >=,而不是=>    小于等于<=,不是=<
                # 布尔值 不能与 整型
                if q2_PMS_line_id == q1_SBBM_ID : # 共16个字段

                    l3.append((q1_shebei_id,q1_shebei_name,q1_SBBM_ID,q1_line_id,q1_XBGXT_line_name,q1_TG_ID,q2_city_Name,q2_Country_Name,q2_Yunwei_name,q2_BdZ_name,q2_Sale_line_id,q2_LineEStop_line_name,q2_E_StopTime,q2_E_ResumeTime,q2_StopTime_Long,q2_StopTime_Date))


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

    f_content = ccc_data(q1_list,q2_list)
    insertDB(f_content)




    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())



# shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date
# create table Get_NewBasci_Table(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# XBGXT_line_name text,
# TG_ID text,
# city_Name text,
# Country_Name text,
# Yunwei_name text,
# BdZ_name text,
# Sale_line_id text,
# LineEStop_line_name text,
# E_StopTime text,
# E_ResumeTime text,
# StopTime_Long text,
# StopTime_Date text
# ) engine=InnoDB default charset=utf8;




# drop table Get_NewBasci_Table;



