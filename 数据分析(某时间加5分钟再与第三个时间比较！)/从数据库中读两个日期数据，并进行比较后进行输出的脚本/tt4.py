
import pymysql
import csv
import datetime

test_list =[
    ["a","2019/11/10 20:06"],
    ["b","2019/11/10 20:07"],
    ["c","2019/11/10 20:08"],
    ["d","2019/11/10 20:38"],
    ["e","2012/3/13 8:32"],
    ["f","2012/3/13 8:35"],
    ["g","2012/3/13 8:39"],
    ["h","2004/7/14 21:06"],
    ["i","2004/7/14 21:16"],
    ["l","2004/7/14 21:36"],
    ["m","2012/3/13 8:36"],
    ["n","2004/7/14 21:06"],
    ["o","2004/7/14 21:06"],
]


def copare_twoTime(s1_time,s2_time):
    time_cut = "%Y/%m/%d %H:%M"
    d1_time = datetime.datetime.strptime(s1_time, time_cut)
    d2_time = datetime.datetime.strptime(s2_time, time_cut)
    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec

def ReadDB():
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    f_list = []
    try:
        sql = "select DP5_id,certain_dt,certain_dt_pl5 from datetime_5plus"
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            DP5_id_f = item["DP5_id"]
            certain_dt_f = item['certain_dt']
            certain_dt_pl5_f = item['certain_dt_pl5']
            f_list.append((DP5_id_f,certain_dt_f,certain_dt_pl5_f))


    except StopIteration:
        pass
    return f_list

f = ReadDB()
# print(f)
# print("~"*88)
# print(test_list)
# print("~"*88)

t_c_plus5 = []
for item1 in test_list:
    for item2 in f:
        test_time =item1[1]
        certain_dt_ = item2[1]
        certain_dt_pl5_ = item2[2]
        test_certain_dt = copare_twoTime(test_time,certain_dt_)
        certain_dt_pl5_test = copare_twoTime(certain_dt_pl5_,test_time)
        if test_certain_dt >= 0 and certain_dt_pl5_test >=0 :
            t_item1 = tuple(item1)
            f_ii = t_item1 + item2
            t_c_plus5.append(f_ii)


for item in t_c_plus5:
    print(item)

