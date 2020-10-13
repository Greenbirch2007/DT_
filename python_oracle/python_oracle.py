

import cx_Oracle

# 查看安装　版本
print(cx_Oracle.__version__)

#
# 创建数据库连接的三种方式：
#
# 方法一：　用户名，密码和监听分开写

import cx_Oracle

db =cx_Oracle.connect('username/password@host:port/orcl')
db.close()


# 方法二：　用户名，密码和监听写在一起

import cx_Oracle

db =cx_Oracle.connect('username/password@host:1521/orcl')
db.close()


# 方法三：配置监听并连接

import cx_Oracle

tns = cx_Oracle.makedsn("host",1521,'orcl')
db = cx_Oracle.connect("username",'password',tns)
db.close()


# 查询数据

import cx_Oracle

# 连接数据库


db = cx_Oracle.connect("scott/scott@localhost:1521/orcl")

#打开游标

cur = db.cursor()

# 执行sql

sql = "select sysdate from dual"
cur.execute(sql)
data= cur.fetchone()
print("Database time:%s" %data)


# 提交，关闭游标

cur.close()
db.close()


# 创建数据库表并插入数据

db = cx_Oracle.connect("scott/scott@localhost:1521/orcl")
cur = db.cursor()
cur.execute("CREATE TABLE my_job(id INT, name VARCHAR(40),age INT,job VARCHAR(50))")

cur.execute("INSERT INTO my_job(id,name,age) VALUES (12,'xiaoliu',32)")
cur.execute("INSERT INTO my_job(id,name,age) VALUES (13,'xiaoli',32)")
cur.execute("INSERT INTO my_job(id,name,age) VALUES (14,'xiaosha',32)")
cur.execute("INSERT INTO my_job(id,name,age) VALUES (15,'xiaoliu',32)")
cur.execute("INSERT INTO my_job(id,name,age) VALUES (16,'xiaoliu',32)")

db.commit() #一定要commit才行，要不然数据是不会插入的

cur.execute("select * from my_job")


#提取一条数据，返回一个元组


data = cur.fetchone()
print(data)
cur.close()
db.close()


# 删除数据
db = cx_Oracle.connect("scott/scott@localhost:1521/orcl")
cur = db.cursor()

cur.execute("delete from my_job where id =12")
db.commit()
cur.execute("select * from my_job")
rows = cur.fetchall()
for row in rows:
    print("%d,%s,%d,%s" %(row[0],row[1],row[2],row[3]))

cur.close()
db.close()

