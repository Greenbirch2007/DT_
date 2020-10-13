#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy
import csv


# 制作新基准表的基础：加入了TG_ID的线变关系表 和 2018.7-2019的线路停电表
# 在PSSM_id相同的情况下，将线变关系表插入到线路停电表中，形成一个新表


# 写一个直接计算两个日期的差值，转化为分钟


def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql1 = "select count(*) from Get_NewBasci_Table; "
        cursor.execute(count_sql1)
        long_count1 = cursor.fetchone()['count(*)']
        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date from Get_NewBasci_Table where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_shebei_id = data1["shebei_id"]
            q1_shebei_name = data1["shebei_name"]
            q1_SBBM_ID = data1["SBBM_ID"]
            q1_line_id = data1["line_id"]
            q1_XBGXT_line_name = data1["XBGXT_line_name"]
            q1_TG_ID = data1["TG_ID"]
            q1_city_Name = data1["city_Name"]
            q1_Country_Name = data1["Country_Name"]
            q1_Yunwei_name = data1["Yunwei_name"]
            q1_BdZ_name = data1["BdZ_name"]
            q1_Sale_line_id = data1["Sale_line_id"]
            q1_LineEStop_line_name = data1["LineEStop_line_name"]
            q1_E_StopTime = data1["E_StopTime"]
            q1_E_ResumeTime = data1["E_ResumeTime"]
            q1_StopTime_Long = data1["StopTime_Long"]
            q1_StopTime_Date = data1["StopTime_Date"]

            q1_list.append((q1_shebei_id,q1_shebei_name,q1_SBBM_ID,q1_line_id,q1_XBGXT_line_name,q1_TG_ID,q1_city_Name,q1_Country_Name,q1_Yunwei_name,q1_BdZ_name,q1_Sale_line_id,q1_LineEStop_line_name,q1_E_StopTime,q1_E_ResumeTime,q1_StopTime_Long,q1_StopTime_Date))
        # 之前没有必要嵌套遍历！



    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into StopT15_NewBasci_Table (shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date,StopTime_15dot) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass






# str---->datetime---->计算差值并除以15----->str

def datetime_Cut_Dot15(item1,item2):
    try:
        time_cut = "%Y-%m-%d %H:%M:%S"

        d1_time = datetime.datetime.strptime(item1, time_cut)
        d2_time = datetime.datetime.strptime(item2, time_cut)
        cut_d_time = (d2_time - d1_time)
        int_min  = int(cut_d_time.days * 86400  + cut_d_time.seconds)/60 #　以分钟计算
        dt_dot_15 = int_min/15  #每15分钟算一个点
        return dt_dot_15
    except ValueError as e:
        pass


if __name__ == "__main__":

    print(datetime.datetime.now())
    q1_list = []
    f_list =[]
    CutData_insert()
    for q1_item in q1_list:
        q1_shebei_id = q1_item[0]
        q1_shebei_name = q1_item[1]
        q1_SBBM_ID = q1_item[2]
        q1_line_id = q1_item[3]
        q1_XBGXT_line_name = q1_item[4]
        q1_TG_ID = q1_item[5]
        q1_city_Name = q1_item[6]
        q1_Country_Name = q1_item[7]
        q1_Yunwei_name = q1_item[8]
        q1_BdZ_name = q1_item[9]
        q1_Sale_line_id = q1_item[10]
        q1_LineEStop_line_name = q1_item[11]
        q1_E_StopTime = q1_item[12]
        q1_E_ResumeTime = q1_item[13]
        q1_StopTime_Long = q1_item[14]
        q1_StopTime_Date = q1_item[15]
        dt_dot15 = datetime_Cut_Dot15(q1_E_StopTime,q1_E_ResumeTime)
        if dt_dot15 != None:
            f_list.append((q1_shebei_id,q1_shebei_name,q1_SBBM_ID,q1_line_id,q1_XBGXT_line_name,q1_TG_ID,q1_city_Name,q1_Country_Name,q1_Yunwei_name,q1_BdZ_name,q1_Sale_line_id,q1_LineEStop_line_name,q1_E_StopTime,q1_E_ResumeTime,q1_StopTime_Long,q1_StopTime_Date,dt_dot15))

    insertDB(f_list)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())



# shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date,StopTime_15dot
# create table StopT15_NewBasci_Table(
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
# StopTime_Date text,
# StopTime_15dot text
# ) engine=InnoDB default charset=utf8;




# drop table Get_NewBasci_Table;

