

import csv
import datetime

#_*_coding=utf-8
import csv
#     time_cut = "%Y-%m-%d %H:%M:%S"
# 完成确定日期加5分钟
# str---->datetime+ 5 ----->str
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
    for i in fff:
        print(i)



if __name__=='__main__':
    readcsv(r'/home/w/Desktop/tt.csv')
