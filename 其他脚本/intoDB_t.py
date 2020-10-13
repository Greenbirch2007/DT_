#-*- coding:utf-8 -*-

import datetime
import time
import pymysql





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into dtd (TG_ID,ID_i,DATA_DATE,PHASE_FLAG,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41,U42,U43,U44,U45,U46,U47,U48,U49,U50,U51,U52,U53,U54,U55,U56,U57,U58,U59,U60,U61,U62,U63,U64,U65,U66,U67,U68,U69,U70,U71,U72,U73,U74,U75,U76,U77,U78,U79,U80,U81,U82,U83,U84,U85,U86,U87,U88,U89,U90,U91,U92,U93,U94,U95,U96) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



a =[(239624702, 14261642, "2019-11-22", 1, 243.70000000000002, 244.0, 243.70000000000002, 243.70000000000002, 244.0, 243.8, 244.20000000000002, 244.1, 244.0, 243.9, 244.0, 244.20000000000002, 244.0, 244.0, 244.1, 244.20000000000002, 244.0, 243.8, 243.8, 243.70000000000002, 243.5, 243.5, 243.3, 243.1, 242.9, 242.6, 242.3, 242.4, 241.8, 241.8, 241.6, 241.5, 240.70000000000002, 239.6, 240.5, 239.70000000000002, 239.20000000000002, 239.9, 239.0, 239.6, 239.3, 239.6, 239.5, 239.70000000000002, 239.3, 238.6, 239.1, 239.5, 239.5, 239.20000000000002, 240.5, 241.8, 241.3, 240.9, 240.4, 240.20000000000002, 240.1, 239.6, 238.5, 237.8, 237.5, 238.3, 238.3, 238.4, 238.8, 238.3, 238.6, 239.20000000000002, 238.0, 237.3, 236.6, 237.4, 236.8, 238.4, 238.1, 238.8, 239.1, 239.9, 239.6, 240.0, 240.3, 240.3, 240.5, 240.9, 240.9, 241.1, 241.4, 241.8, 241.8, 242.0, 241.9, 242.4, 242.0, 242.20000000000002, 242.1, 242.3)]


insertDB(a)









# create table dtd(
# id int not null primary key auto_increment,
# TG_ID text,
# ID_i text,
# DATA_DATE text,
# PHASE_FLAG text,
# U1 text,
# U2 text,
# U3 text,
# U4 text,
# U5 text,
# U6 text,
# U7 text,
# U8 text,
# U9 text,
# U10 text,
# U11 text,
# U12 text,
# U13 text,
# U14 text,
# U15 text,
# U16 text,
# U17 text,
# U18 text,
# U19 text,
# U20 text,
# U21 text,
# U22 text,
# U23 text,
# U24 text,
# U25 text,
# U26 text,
# U27 text,
# U28 text,
# U29 text,
# U30 text,
# U31 text,
# U32 text,
# U33 text,
# U34 text,
# U35 text,
# U36 text,
# U37 text,
# U38 text,
# U39 text,
# U40 text,
# U41 text,
# U42 text,
# U43 text,
# U44 text,
# U45 text,
# U46 text,
# U47 text,
# U48 text,
# U49 text,
# U50 text,
# U51 text,
# U52 text,
# U53 text,
# U54 text,
# U55 text,
# U56 text,
# U57 text,
# U58 text,
# U59 text,
# U60 text,
# U61 text,
# U62 text,
# U63 text,
# U64 text,
# U65 text,
# U66 text,
# U67 text,
# U68 text,
# U69 text,
# U70 text,
# U71 text,
# U72 text,
# U73 text,
# U74 text,
# U75 text,
# U76 text,
# U77 text,
# U78 text,
# U79 text,
# U80 text,
# U81 text,
# U82 text,
# U83 text,
# U84 text,
# U85 text,
# U86 text,
# U87 text,
# U88 text,
# U89 text,
# U90 text,
# U91 text,
# U92 text,
# U93 text,
# U94 text,
# U95 text,
# U96 text
# ) engine=InnoDB default charset=utf8;


