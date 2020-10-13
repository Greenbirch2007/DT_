

import csv
import datetime

#_*_coding=utf-8
import csv
#     time_cut = "%Y-%m-%d %H:%M:%S"
# 完成确定日期加5分钟
# str---->datetime+ 5 ----->str
import pymysql


def plus_5m(s_time):
    time_cut = "%Y/%m/%d %H:%M"
    d_time = datetime.datetime.strptime(s_time, time_cut)
    s_time = d_time + datetime.timedelta(minutes=5)
    f_time = s_time.strftime(time_cut)
    return f_time

def get_Datetime(s_time):
    time_cut = "%Y%m/%d %H:%M"
    d_time = datetime.datetime.strptime(s_time, time_cut)
    return d_time



def plus_5m_sl(s_time_l):
    sl = []
    for s_time in s_time_l:

        time_cut = "%Y/%m/%d %H:%M"
        d_time = datetime.datetime.strptime(s_time, time_cut)
        s_time = d_time + datetime.timedelta(minutes=5)
        f_time = s_time.strftime(time_cut)
        sl.append(f_time)
    return sl





def readcsv(csvfilepath):#列表方式读取
    s_ltime = []
    cut_onel = []
    fff = []
    with open(csvfilepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)#创建csv.reader对象
        for row in reader:
            # 读取出的内容是列表格式的
            # print(row)
            f_t = row[1]
            s_ltime.append(f_t)
            cut_onel.append(row)
    f_l = plus_5m_sl(s_ltime)
    for i5m,item in zip(f_l,cut_onel):
        item.append(i5m)
        f_t = tuple(item)
        fff.append(f_t)
    return fff




def insertDB(content):
    try:

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.executemany('insert into B_line (B_linetable_id,B_line_stopTime,B_line_name,B_line_id,B_line_Byq_Num,B_line_stopTime_Plus5) values (%s,%s,%s,%s,%s,%s)', content)

        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass

if __name__=='__main__':
    con = readcsv(r'D:\\B_line.csv')
    insertDB(con)
    print("给确定时间添加5分钟后，插入数据库！")
