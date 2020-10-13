#-*- coding:utf-8 -*-


import cx_Oracle

# 用户名sys
# 数据库10.216.44.118:1521/orcl
# 口令root
# 连接为SYSDBA

# 正常可用的sql
# sql = "select distinct g.tg_id, c1.id, c1.data_date, c1.phase_flag, c1.u1, c1.u2, c1.u3, c1.u4, c1.u5, c1.u6, c1.u7, c1.u8, c1.u9, c1.u10, c1.u11, c1.u12,c1.u13,c1.u14,c1.u15,c1.u16,c1.u17,c1.u18,c1.u19,c1.u20,c1.u21,c1.u22,c1.u23,c1.u24,c1.u25,c1.u26,c1.u27,c1.u28,c1.u29,c1.u30,c1.u31,c1.u32,c1.u33,c1.u34,c1.u35,c1.u36,c1.u37,c1.u38,c1.u39,c1.u40,c1.u41,c1.u42,c1.u43,c1.u44,c1.u45,c1.u46,c1.u47,c1.u48,c1.u49,c1.u50,c1.u51,c1.u52,c1.u53,c1.u54,c1.u55,c1.u56,c1.u57,c1.u58,c1.u59,c1.u60,c1.u61,c1.u62,c1.u63,c1.u64,c1.u65,c1.u66,c1.u67,c1.u68,c1.u69,c1.u70,c1.u71,c1.u72,c1.u73,c1.u74,c1.u75,c1.u76,c1.u77,c1.u78,c1.u79,c1.u80,c1.u81,c1.u82,c1.u83,c1.u84,c1.u85,c1.u86,c1.u87,c1.u88,c1.u89,c1.u90,c1.u91,c1.u92,c1.u93,c1.u94,c1.u95,c1.u96 from eic2.p_mr_mped p,yyjc_yx.c_mp mp,yyjc_yx.c_cons c,yyjc_yx.g_tg g,yyjc_yx.g_tran tran,eic2.e_mp_vol_curve c1 where p.cons_id = c.cons_id and mp.cons_id = c.cons_id and g.tg_id = mp.tg_id and tran.tg_id = g.tg_id and c1.id = p.mped_id and mp.status_code = '02' and mp.usage_type_code = '02' and c1.Data_Date = To_Date('20191117', 'yyyymmdd') and g.tg_no in ('6100869246', '6100782215', '6301034994', '6200817928') "
# sql = "select distinct g.tg_id, c1.id, c1.data_date, c1.phase_flag, c1.u1, c1.u2, c1.u3, c1.u4, c1.u5, c1.u6, c1.u7, c1.u8, c1.u9, c1.u10, c1.u11, c1.u12,c1.u13,c1.u14,c1.u15,c1.u16,c1.u17,c1.u18,c1.u19,c1.u20,c1.u21,c1.u22,c1.u23,c1.u24,c1.u25,c1.u26,c1.u27,c1.u28,c1.u29,c1.u30,c1.u31,c1.u32,c1.u33,c1.u34,c1.u35,c1.u36,c1.u37,c1.u38,c1.u39,c1.u40,c1.u41,c1.u42,c1.u43,c1.u44,c1.u45,c1.u46,c1.u47,c1.u48,c1.u49,c1.u50,c1.u51,c1.u52,c1.u53,c1.u54,c1.u55,c1.u56,c1.u57,c1.u58,c1.u59,c1.u60,c1.u61,c1.u62,c1.u63,c1.u64,c1.u65,c1.u66,c1.u67,c1.u68,c1.u69,c1.u70,c1.u71,c1.u72,c1.u73,c1.u74,c1.u75,c1.u76,c1.u77,c1.u78,c1.u79,c1.u80,c1.u81,c1.u82,c1.u83,c1.u84,c1.u85,c1.u86,c1.u87,c1.u88,c1.u89,c1.u90,c1.u91,c1.u92,c1.u93,c1.u94,c1.u95,c1.u96 from eic2.p_mr_mped p,yyjc_yx.c_mp mp,yyjc_yx.c_cons c,yyjc_yx.g_tg g,yyjc_yx.g_tran tran,eic2.e_mp_vol_curve c1 where p.cons_id = c.cons_id and mp.cons_id = c.cons_id and g.tg_id = mp.tg_id and tran.tg_id = g.tg_id and c1.id = p.mped_id and mp.status_code = '02' and mp.usage_type_code = '02' and c1.Data_Date = To_Date('20191117', 'yyyymmdd')  and g.tg_id = '239624702' "


# 使用数据库 ，创建数据表（直接执行sql）
#
# "sys/10.216.44.118:1521@root/orcl"
# db = cx.connect("sys","root","10.216.44.118:1521/database")
# python 以管理员的身份进入！
db = cx_Oracle.connect('eic2/eic2@10.216.44.92:1521/pdborcl')
cur = db.cursor()

sql = "select distinct g.tg_id, c1.id, c1.data_date, c1.phase_flag, c1.u1, c1.u2, c1.u3, c1.u4, c1.u5, c1.u6, c1.u7, c1.u8, c1.u9, c1.u10, c1.u11, c1.u12,c1.u13,c1.u14,c1.u15,c1.u16,c1.u17,c1.u18,c1.u19,c1.u20,c1.u21,c1.u22,c1.u23,c1.u24,c1.u25,c1.u26,c1.u27,c1.u28,c1.u29,c1.u30,c1.u31,c1.u32,c1.u33,c1.u34,c1.u35,c1.u36,c1.u37,c1.u38,c1.u39,c1.u40,c1.u41,c1.u42,c1.u43,c1.u44,c1.u45,c1.u46,c1.u47,c1.u48,c1.u49,c1.u50,c1.u51,c1.u52,c1.u53,c1.u54,c1.u55,c1.u56,c1.u57,c1.u58,c1.u59,c1.u60,c1.u61,c1.u62,c1.u63,c1.u64,c1.u65,c1.u66,c1.u67,c1.u68,c1.u69,c1.u70,c1.u71,c1.u72,c1.u73,c1.u74,c1.u75,c1.u76,c1.u77,c1.u78,c1.u79,c1.u80,c1.u81,c1.u82,c1.u83,c1.u84,c1.u85,c1.u86,c1.u87,c1.u88,c1.u89,c1.u90,c1.u91,c1.u92,c1.u93,c1.u94,c1.u95,c1.u96 from eic2.p_mr_mped p,yyjc_yx.c_mp mp,yyjc_yx.c_cons c,yyjc_yx.g_tg g,yyjc_yx.g_tran tran,eic2.e_mp_vol_curve c1 where p.cons_id = c.cons_id and mp.cons_id = c.cons_id and g.tg_id = mp.tg_id and tran.tg_id = g.tg_id and c1.id = p.mped_id and mp.status_code = '02' and mp.usage_type_code = '02' and c1.Data_Date = To_Date('{0}', 'yyyymmdd')  and g.tg_id = '{1}' "

sql_format = sql.format("20190905","2015000228927700")
# 使用一个format的字符串拼接！

cur.execute(sql_format)
row = cur.fetchall()
for item in row:
    U1_96 =item[4:]
    if None not in U1_96:
        print(item)
    else:
        pass


# 判断：1.如果返回的长度不为0继续往下，不然就pass

# 从oracle提取是datetime.datetime对象，要转化为str对象，再与大基准表匹配，最后在插入新表即可

# 一共有100个字段！
cur.close()
db.close()



# datetime.datetime(2019, 11, 15, 0, 0) 日期整理