#-*- coding:utf-8 -*-


import csv


#　#　#　with open(csvfilepath,'r',newline='',encoding="utf-8")　
# 此时提出utf-8
import time

import pymysql


def readcsv(csvfilepath):# 列表方式读取
    base_list = []  # 基准表的编号，变压器编号，变压器名称，线路编号，线路名称

    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象


        for row in reader:
            table_id = row[0]
            TRAN_ID = row[1]
            TRAN_NAME = row[2]
            LINE_ID = row[3]
            LINE_NAME = row[4]
            base_list.append((table_id,TRAN_ID,TRAN_NAME,LINE_ID,LINE_NAME))
    return base_list


def insertDB(content):
    try:

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.executemany('insert into Basic_table (basic_t_id,TRAN_ID,TRAN_NAME,LINE_ID,LINE_NAME) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


if __name__=="__main__":

    db_table =readcsv(r"E:\\basic_table.csv")
    print(len(db_table))
    print(type(db_table))
    insertDB(db_table)
    print("~~~~~成功插入数据库~~~~~~~·")
    # for item in db_table:
    #     print(item)
    #     time.sleep(9)



# basic_t_id,TRAN_ID,TRAN_NAME,LINE_ID,LINE_NAME
# create table Basic_table(
# id int not null primary key auto_increment,
# basic_t_id text,
# TRAN_ID text,
# TRAN_NAME text,
# LINE_ID text,
# LINE_NAME text
# ) engine=InnoDB  charset=utf8;

