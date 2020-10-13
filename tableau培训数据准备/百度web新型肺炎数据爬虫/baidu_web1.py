# -*- coding:utf-8 -*-

import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException






# 确认索引是55
# 治愈索引是56
# 死亡索引是57



# 写一个函数专门处理包在字符串里面的列表
#
# 1:将字符串去掉[ ]
# 2.将上下的字符串按照,进行分割
# 3.遍历存入新的列表中
# 再与日期，省份，分别组成一个全新的元组然后插入到数据库中




def strlist_intoList(str_item):
    cut_str = str_item[1:-1] # 将字符串去掉[ ]
    spl_str = cut_str.split(",") # 将上下的字符串按照,进行分割
    return spl_str



def insertDB(content):

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into dif_info1 (pros, dat,confirmed_n,covered_n,died_n) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

confirmed_n = "[0,0,1,1,1,1,1,1,1,1]"
covered_n  = "[0,0,0,0,0,0,0,0,0,0]"
died_n = "[0,0,0,0,0,0,0,0,0,0]"

if __name__ == '__main__':
    big_list = []
    # pro_list = ["湖北", "广东", "浙江", "河南", "湖南", "江西", "安徽", "重庆", "江苏", "山东", "四川", "北京", "上海", "黑龙江", "福建", "陕西", "广西",
    #             "河北", "云南", "海南", "辽宁", "山西", "天津", "贵州", "甘肃", "吉林", "内蒙古", "宁夏", "新疆", "香港", "青海", "台湾", "澳门", "西藏"]
    # for pro_item in pro_list:
    pro_item ="西藏"


    date_list = ["2020年1月27日", "2020年1月28日", "2020年1月29日", "2020年1月30日", "2020年1月31日", "2020年2月1日", "2020年2月2日",
                 "2020年2月3日", "2020年2月4日", "2020年2月5日"]
    s_confirmed_n = strlist_intoList(confirmed_n)
    s_covered_n = strlist_intoList(covered_n)
    s_died_n = strlist_intoList(died_n)
    l_pro = len(s_confirmed_n) * [pro_item]

    for i1,i2,i3,i4,i5 in zip(l_pro,date_list,s_confirmed_n,s_covered_n,s_died_n):
        big_list.append((i1,i2,i3,i4,i5))
    insertDB(big_list)
    print(pro_item)








# pros, dat,confirmed_n,covered_n,died_n
# create table dif_info1(
# id int not null primary key auto_increment,
# pros varchar(50),
# dat varchar(50),
# confirmed_n int,
# covered_n int,
# died_n int
# ) engine=InnoDB  charset=utf8;


# drop table dif_info1;