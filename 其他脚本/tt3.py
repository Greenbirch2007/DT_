# -*-coding:utf-8 -*-

import csv,pymysql,datetime
#
# 1. 先从csv文件读取源数据
# 2. 给确定时间的字段加5分钟
# 3. 将整理的新字段的数据插入到数据库中
# 4. 自己制作一个测试的数据列表来跟数据库中的数据进行匹配(测试匹配脚本)



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




# s_time = '2019/11/10 20:19:01'
#
# f = plus_5m(s_time)
# print(s_time)
# print(type(s_time))
# print("~"*99)
# print(f)
# print(type(f))


def readcsv(csvfilepath):#列表方式读取
    s_ltime = []
    cut_onel = []
    fff = []
    with open(csvfilepath, 'r', newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)#创建csv.reader对象
        for row in reader:
            # 读取出的内容是列表格式的
            s_ltime.append(row[1])
            cut_onel.append(row[0])
    f_l = plus_5m_sl(s_ltime)
    for i1,i2,i3 in zip(cut_onel,s_ltime,f_l):
        fff.append((i1,i2,i3))
    return fff


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into datetime_5plus (DP5_id,certain_dt,certain_dt_pl5) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass



#
# if __name__=='__main__':
#     content = readcsv(r'/home/w/Desktop/tt.csv')
#     insertDB(content)
#     print("insert into DB  success~~~")





a1 = '2018/4/27 16:28:00'
a2 = '2018/12/27 16:28:00'
a3 = '2018/2/7 16:28:00'
a4 = '2018/12/7 16:28:00'
print(len(a1),len(a2),len(a3),len(a4))
print("~"*99)
a5 = '2018/4/27 16:28'
a6 = '2018/12/27 16:28'
a7 = '2018/2/7 16:28'
a8 = '2018/12/7 16:28'
print(len(a5),len(a6),len(a7),len(a8))


# DP5_id,certain_dt,certain_dt_pl5
# create table datetime_5plus(
# id int not null primary key auto_increment,
# DP5_id text,
# certain_dt text,
# certain_dt_pl5 text
# ) engine=InnoDB  charset=utf8;
