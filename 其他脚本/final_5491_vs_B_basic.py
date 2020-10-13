#-*- coding:utf-8 -*-

import datetime
import time
import pymysql
import copy

def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    try:
        # 制作l1
        count_sql1 = "select count(*) from b_line ; "
        cursor.execute(count_sql1)
        long_count1 = cursor.fetchone()['count(*)']
        for page1 in range(1, long_count1 + 1):
            SQL_search1 = 'select B_linetable_id ,B_line_stopTime ,B_line_name ,B_line_id ,B_line_Byq_Num ,B_line_stopTime_Plus5  from b_line where id = %s  '%  page1

            cursor.execute(SQL_search1)
        #     # #获取所有记录列表
            data1 = cursor.fetchone()
            q1_B_linetable_id = data1["B_linetable_id"]
            q1_line_stopTime = data1["B_line_stopTime"]
            q1_line_name = data1["B_line_name"]
            q1_line_id = data1["B_line_id"]
            q1_line_Byq_Num = data1["B_line_Byq_Num"]
            q1_line_stopTime_Plus5 = data1["B_line_stopTime_Plus5"]
            # 将大基准表重新遍历，插入新列表，以便于后面进行处理
            q1_list.append((q1_B_linetable_id,q1_line_stopTime,q1_line_name,q1_line_id,q1_line_Byq_Num,q1_line_stopTime_Plus5))
            # 单独将大基准表的线路id，存入一个新列表，以便于后续匹配使用
            f_line_id.append(q1_line_id)

    except:
        pass






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into final_5491_vs_B_basic (DT,f_line_stopTime,f__line_name,f_line_id,f_line_countNum,f_line_stopTime_Plus5,sel_Bline_countNum) values (%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



# 直接两层遍历




if __name__ == "__main__":
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    q1_list = []
    f_line_id = []
    afterCount_fNum=[]
    new_line_id =[]

    print(datetime.datetime.now())

    CutData_insert()
    q1_list_dcopy = copy.deepcopy(q1_list)
    f_line_id_dcopy = copy.deepcopy(f_line_id)

    # 自己写的逻辑不做备注都忘了!
    # 脚本的逻辑：1. 先将大基准表的全部数据遍历，重新插入到新列表(最好重新深度复制一下啊！)
    # 2.然后单独将线路id(大基准表中的，因为是唯一的)，重新插入一个新的列表（最好深度复制一下啊）
    #3. 用新的线路id的列表，进行遍历（在），比对计数需要比对的数据表，其中有线路id的情况
    # 4. 针对具体情况，5000条的比对数据，因为开始就已经跟大基准表完成了比对，所以绝对是存在的，即便不存在，也还是要以大基准表为准！
    for item in f_line_id_dcopy:
        SQL_search2 = 'select count(*) from final_5491_inDB where line_id = "%s" ' % item
        cursor.execute(SQL_search2)
        # 同一个线路在匹配后的表的线路id计数结果
        long_count1 = cursor.fetchone()['count(*)']
        new_line_id.append((item,long_count1))

    new_line_id_dcopy = copy.deepcopy(new_line_id)

    for i1_item,i2_item in zip(q1_list_dcopy,new_line_id_dcopy):
        if i1_item[3] == i2_item[0]:
            f_content = i1_item + (i2_item[1],)
            afterCount_fNum.append(f_content)

    else:
        pass

        # 如果线路id相同，就将匹配表的线路id计数的元素加入大基准表中(元组相加)，然后添加如最终需要插入数据库的列表即可



    insertDB(afterCount_fNum)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())




# 大基准表有一些问题，先用线路id遍历大变压器表，然后计数



# DT,f_line_stopTime,f__line_name,f_line_id,f_line_countNum,f_line_stopTime_Plus5,sel_Bline_countNum
# create table final_5491_vs_B_basic(
# id int not null primary key auto_increment,
# DT text,
# f_line_stopTime text,
# f__line_name text,
# f_line_id text,
# f_line_countNum text,
# f_line_stopTime_Plus5 text,
# sel_Bline_countNum text
# ) engine=InnoDB default charset=utf8;

