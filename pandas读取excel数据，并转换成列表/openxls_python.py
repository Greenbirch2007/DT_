#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver



  # coding=utf-8
import xlrd
import time
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile

#
# def ccc_data(l1,l2):
#     l3 = []
#     for item_q1 in lq

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")




# def insertDB(content):
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
#                                  db='DT',
#                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     try:
#         cursor.executemany('insert into dt1 (DT,byq_name,line_name) values (%s,%s,%s)', content)
#         connection.commit()
#         connection.close()
#         print('向MySQL中添加数据成功！')
#     except StopIteration:
#         pass



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into dt2 (byq_name,line_name) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


if __name__ == '__main__':
    l1 = []
    excelFile1 = '/home/w/Desktop/data_work/t2.xlsx'
    full_items1 = read_xlrd(excelFile=excelFile1)
    for item in full_items1:
        l1.append((item[1],item[2]))
    insertDB(l1)




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