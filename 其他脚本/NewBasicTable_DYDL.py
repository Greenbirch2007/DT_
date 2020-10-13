#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy
import csv
import cx_Oracle
from retrying import retry


# 匹配的条件有3个：
# 1. TG_ID相同（这个直接字段匹配即可）
# 2. 日期相同(这个需要专门写一个函数) 一个是datetime.datetime对象，一个是从数据库中拿出来的字符串对象
# 3. 因为直接要用上面的TG_ID和日期格式作为搜索条件，来在Oracle数据中查询结果，如果None出现就输出！


# 其实并不是对比两个日期，而是从大基准表(3.1w条)中，遍历拿出字段，然后送入两个字段(TG_ID和日期，要求格式相同)
# 从而来执行查询格式！




def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        # count_sql1 = "select count(*) from Get_NewBasci_Table; "
        # cursor.execute(count_sql1)
        # long_count1 = cursor.fetchone()['count(*)']
        # for page1 in range(1, long_count1 + 1):
        # 34569 ，蚂蚁搬家 分批次处理！
        # 400条，大致12分钟   每999条就请求一次！不然会变成连接数据库超时
        for page1 in range(28902, 34570):
            SQL_search1 = 'select shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,LineEStop_line_name,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date from Get_NewBasci_Table where id = %s  '%  page1
            cursor.execute(SQL_search1)
            # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_shebei_id = data1["shebei_id"]
            q1_shebei_name = data1["shebei_name"]
            q1_SBBM_ID = data1["SBBM_ID"]
            q1_line_id = data1["line_id"]
            q1_XBGXT_line_name = data1["XBGXT_line_name"]
            q1_TG_ID = data1["TG_ID"]
            q2_city_Name = data1["city_Name"]
            q2_Country_Name = data1["Country_Name"]
            q2_Yunwei_name = data1["Yunwei_name"]
            q2_BdZ_name = data1["BdZ_name"]
            q2_Sale_line_id = data1["Sale_line_id"]
            q2_LineEStop_line_name = data1["LineEStop_line_name"]
            q2_E_StopTime = data1["E_StopTime"]
            q2_E_ResumeTime = data1["E_ResumeTime"]
            q2_StopTime_Long = data1["StopTime_Long"]
            q2_StopTime_Date = data1["StopTime_Date"]



            q1_list.append((q1_shebei_id,q1_shebei_name,q1_SBBM_ID,q1_line_id,q1_XBGXT_line_name,q2_LineEStop_line_name,q1_TG_ID,q2_city_Name,q2_Country_Name,q2_Yunwei_name,q2_BdZ_name,q2_Sale_line_id,q2_E_StopTime,q2_E_ResumeTime,q2_StopTime_Long,q2_StopTime_Date))
    except:
        pass

def retry_if_DBerror(exception):
    return isinstance(exception,cx_Oracle.DatabaseError)




#　字符串拼接 % 或用format()
#  a = "asdfafa{0}asdfaf{1}".format(666,888)
# 'asdfafa666asdfaf888'



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into f_NBBT_DYDL_t (shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,LineEStop_line_name,xbgxt_TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date,DYDL_TG_ID,ID_i,DATA_DATE,PHASE_FLAG,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41,U42,U43,U44,U45,U46,U47,U48,U49,U50,U51,U52,U53,U54,U55,U56,U57,U58,U59,U60,U61,U62,U63,U64,U65,U66,U67,U68,U69,U70,U71,U72,U73,U74,U75,U76,U77,U78,U79,U80,U81,U82,U83,U84,U85,U86,U87,U88,U89,U90,U91,U92,U93,U94,U95,U96) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass

@retry(retry_on_exception=retry_if_DBerror)
def get_Oracle_():
    db = cx_Oracle.connect('eic2/eic2@10.216.44.92:1521/pdborcl')
    cur = db.cursor()
    return cur

if __name__ == "__main__":
    f_b_list = []

    print(datetime.datetime.now())
    q1_list = []
    # TG_ID索引为5  ，停电日期索引为15
    CutData_insert()
    print(len(q1_list))
    for q1_item in q1_list:
        # print("TG_ID索引:",type(q1_item[6]),"停电日期：",type(q1_item[15]))
        # time.sleep(9)
        cur = get_Oracle_() #如果连接报错，就重复

        sql = "select distinct g.tg_id, c1.id, c1.data_date, c1.phase_flag, c1.u1, c1.u2, c1.u3, c1.u4, c1.u5, c1.u6, c1.u7, c1.u8, c1.u9, c1.u10, c1.u11, c1.u12,c1.u13,c1.u14,c1.u15,c1.u16,c1.u17,c1.u18,c1.u19,c1.u20,c1.u21,c1.u22,c1.u23,c1.u24,c1.u25,c1.u26,c1.u27,c1.u28,c1.u29,c1.u30,c1.u31,c1.u32,c1.u33,c1.u34,c1.u35,c1.u36,c1.u37,c1.u38,c1.u39,c1.u40,c1.u41,c1.u42,c1.u43,c1.u44,c1.u45,c1.u46,c1.u47,c1.u48,c1.u49,c1.u50,c1.u51,c1.u52,c1.u53,c1.u54,c1.u55,c1.u56,c1.u57,c1.u58,c1.u59,c1.u60,c1.u61,c1.u62,c1.u63,c1.u64,c1.u65,c1.u66,c1.u67,c1.u68,c1.u69,c1.u70,c1.u71,c1.u72,c1.u73,c1.u74,c1.u75,c1.u76,c1.u77,c1.u78,c1.u79,c1.u80,c1.u81,c1.u82,c1.u83,c1.u84,c1.u85,c1.u86,c1.u87,c1.u88,c1.u89,c1.u90,c1.u91,c1.u92,c1.u93,c1.u94,c1.u95,c1.u96 from eic2.p_mr_mped p,yyjc_yx.c_mp mp,yyjc_yx.c_cons c,yyjc_yx.g_tg g,yyjc_yx.g_tran tran,eic2.e_mp_vol_curve c1 where p.cons_id = c.cons_id and mp.cons_id = c.cons_id and g.tg_id = mp.tg_id and tran.tg_id = g.tg_id and c1.id = p.mped_id and mp.status_code = '02' and mp.usage_type_code = '02' and c1.Data_Date = To_Date('{0}', 'yyyymmdd')  and g.tg_id = '{1}' "

        sql_format = sql.format(q1_item[15],q1_item[6])
        # 使用一个format的字符串拼接！
        cur.execute(sql_format)
        row = cur.fetchall()
        len_row = len(row) # 因为前面已经使用了TG_ID和日期来作为搜索条件的！
        if len_row != 0: # 第一个判断，必须要查询到内容
            for item in row: #第2个判断，在确实有返回值时，必须满足U1-U94都是内容的（也就是没有停电）
                U1_96 = item[4:]
                if None not in U1_96 and 0 not in U1_96: # 不但为空，还要非零
                    l1_tu = q1_item
                    l2_tu = item
                    f_tu = l1_tu + l2_tu
                    f_b_list.append(f_tu)

                else:
                    pass
        else:
            pass

        # 判断：1.如果返回的长度不为0继续往下，不然就pass
        # 从oracle提取是datetime.datetime对象，要转化为str对象，再与大基准表匹配，最后在插入新表即可

        # 一共有100个字段！
        cur.close()
        # db.close()
    # for i in f_b_list:
    #     print(i)
    #     time.sleep(9)
    insertDB(f_b_list)
    print("插入数据库完成")
    print(datetime.datetime.now())

# 可以思考，将后面跟的代码放入一个函数，放在while True，如果报错就继续，返回然后重新执行

#  最终拼凑出来的表就是    大基准表(16个字段) + 电压电流表(100个字段)  一个共116个字段

# drop table f_NBBT_DYDL_t;





# create table f_NBBT_DYDL_t(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# XBGXT_line_name text,
# LineEStop_line_name text,
# xbgxt_TG_ID text,
# city_Name text,
# Country_Name text,
# Yunwei_name text,
# BdZ_name text,
# Sale_line_id text,
# E_StopTime text,
# E_ResumeTime text,
# StopTime_Long text,
# StopTime_Date text,
# DYDL_TG_ID text,
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

