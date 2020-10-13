#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy
import csv



# 处理逻辑：(都是使用csv标准库模块)
# 1. 用TG_ID的PMS_EQUIP_ID与线变关系表的TRAN_ID(设备id)匹配,
# 2. 往线变关系表中插入TG_ID的一个新列



def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True

def readcsv(csvfilepath):# 列表方式读取
    base_list = []  # 基准表的编号，变压器编号，变压器名称，线路编号，线路名称

    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象


        for row in reader:
            DT_id = row
            base_list.append(DT_id)
    return base_list






def GetData_fromCSV():

    f_tg_idContent = readcsv(r"E:\\TG_ID____XB_table\\f_TG_ID_intoDB.csv")
    for q1_item in f_tg_idContent:
        q1_list.append(tuple(q1_item))









def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into TG_ID____XB_table (shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID) values (%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



# 直接两层遍历


# def ccc_data(l1, l2):
#
#     l3 = []
#     for item_q2 in l2:
#         q2_shebei_id = item_q2[0]
#         q2_shebei_name = item_q2[1]
#         q2_SBBM_ID = item_q2[2]
#         q2_line_id= item_q2[3]
#         q2_line_name= item_q2[4]
#         for item_q1 in l1:
#             q1_PMS_EQUIP_ID = item_q1[0]
#             q1_TG_ID = item_q1[1]
#
#             try:
#                 if q1_PMS_EQUIP_ID == q2_shebei_id:
#                     l3.append((q1_PMS_EQUIP_ID,q1_TG_ID,q2_shebei_name,q2_SBBM_ID,q2_line_id,q2_line_name))
#
#                 else:
#                     pass
#             except IndexError as e:
#                 pass
#     return l3






if __name__ == "__main__":

    print(datetime.datetime.now())
    # 直接在这里写逻辑算了！
    q1_list = [] # 'PMS_EQUIP_ID', 'TG_ID'
    GetData_fromCSV()
    insertDB(q1_list)


    print("插入数据库完成")
    print(datetime.datetime.now())








# shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID
# create table TG_ID____XB_table(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# XBGXT_line_name text,
# TG_ID text
# ) engine=InnoDB default charset=utf8;


#  drop table TG_ID____XB_table;

