#-*- coding:utf-8 -*-


import cx_Oracle

# 用户名sys
# 数据库ip:1521/orcl
# 口令root
# 连接为SYSDBA


# 使用数据库 ，创建数据表（直接执行sql）
#

# python 以管理员的身份进入！
db = cx_Oracle.connect('sys/root@ip:1521/orcl',mode=cx_Oracle.SYSDBA)
cur = db.cursor()
sql = 'select * from AW$AWREPORT '
f = cur.execute(sql)
row = cur.fetchall()
for item in row:
    print(item)
cur.close()
db.close()
