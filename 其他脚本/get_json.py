#-*- coding:utf-8 -*-



import json


#id,t1,t2,t3,t4,t5,t6,t7,t8
#  t1,t2,t3,t4,t5,t6,t7,t8
# create table Tdata(
# id int not null primary key auto_increment,
# t1 varchar(20),
# t2 varchar(20),
# t3 varchar(20),
# t4 varchar(20),
# t5 varchar(20),
# t6 varchar(20),
# t7 varchar(20),
# t8 varchar(20)
# ) engine=InnoDB  charset=utf8;

# drop  table Tdata;
#



import pymysql



if __name__ =='__main__':
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    count_sql = "select count(*) from Tdata; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']

    # 测试
    big_list = []
    for num in range(1,long_count) :


        sql = 'select id,t1,t2,t3,t4,t5,t6,t7,t8  from Tdata where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    # big_list [{}.{}...]
    #
    filename = 'Tdata.json'
    with open(filename,'w') as file_obj:
        json.dump(big_list,file_obj,ensure_ascii=False) # json解析中文会默认使用的ascii编码.
        print("将数据导出json文件")


