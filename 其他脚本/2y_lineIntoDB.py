# -*-coding:utf-8 -*-

import csv,pymysql,datetime
#
# 1. 先从csv文件读取源数据
# 2. 给确定时间的字段加5分钟
# 3. 将整理的新字段的数据插入到数据库中
# 4. 自己制作一个测试的数据列表来跟数据库中的数据进行匹配(测试匹配脚本)
import time


def plus_5m(s_time):
    time_cut = "%Y/%m/%d %H:%M:%S"
    try:
        if len(s_time) != 11: # 只提出没有时间只有日期的！
            d_time = datetime.datetime.strptime(s_time, time_cut)
            s_time = d_time + datetime.timedelta(minutes=5)
            f_time = s_time.strftime(time_cut)
            return f_time
    except:
        pass


def get_Datetime(s_time):
    time_cut = "%Y/%m/%d %H:%M:%S"
    d_time = datetime.datetime.strptime(s_time, time_cut)
    return d_time



def plus_5m_sl(s_time_l):
        sl = []
        for s_time in s_time_l:
            try:
                f_time =plus_5m(s_time)
                sl.append(f_time)

            except ValueError as e:
                pass
        return sl









def readcsv(csvfilepath):#列表方式读取
    s_ltime = []
    cut_onel = []
    fff = []
    al_l = []
    with open(csvfilepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)#创建csv.reader对象
        for row in reader:
            # 读取出的内容是列表格式的
            s_ltime.append(row[2])
            cut_onel.append(row)


    al = plus_5m_sl(s_ltime)
    for item in al:
        all = [item]
        al_l.append(all)
    for i1,i2 in zip(cut_onel,al_l):
        f_t = tuple(i1+i2)
        fff.append(f_t)
    return fff

















def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into LLine_table (Line_name,Line_id,Line_StopTtime,Line_StopTtimePlus5) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass

# l =['2018/04/27 14:55:00','2018/04/27 14:55:00','2018/04/27 14:55:00']
# al = plus_5m_sl(l)
# print(l)
# print("~"*99)
# print(al)



if __name__=='__main__':
    f =  readcsv(r'D:\\2Y_lines.csv')
    insertDB(f)
    print("insert into DB  success~~~")





# Line_name,Line_id,Line_StopTtime,Line_StopTtimePlus5
# create table LLine_table(
# id int not null primary key auto_increment,
#  Line_name text,
# Line_id text,
# Line_StopTtime text,
# Line_StopTtimePlus5 text
# ) engine=InnoDB  charset=utf8;
