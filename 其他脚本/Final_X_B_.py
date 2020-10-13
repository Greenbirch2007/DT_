#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy

# 时间的处理逻辑： 1.都先进行裁剪，最终缩减到
# 直接就报错，这样更容易快速暴露问题！
# 字符串--->正则缩减到分钟(list)---->字符串-----datetime----->计算差值
def re_cut_Str(item):
    if type(item) != str:
        str_item = str(item)
    else:
        str_item = item
    patt =re.compile("\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}",re.S)
    ite = re.findall(patt,str_item)
    return ite
# 这个函数两个功能：1.裁剪脏日期数据，保留分钟 2. 都返回 字符串(这里只裁剪)
# 这个函数：1.将两个字符串日期，先进行裁剪
# 2. 因为都只保留到分钟，所以可以用分钟的date格式，转化为datetime对象
# 3.直接将两个datetime对象，进行计算返回int
# 难道还要做一个装饰器？ 要有正确的数据容器！
def copare_twoTime(s1_time,s2_time):
    c_result =[]
    f1_time = re_cut_Str(s1_time) #是列表
    f2_time = re_cut_Str(s2_time)
    time_cut = "%Y/%m/%d %H:%M"
    dc_f1_time =copy.deepcopy(f1_time) # 在这里同样是使用深度复制，避免列表在使用出现问题！
    dc_f2_time =copy.deepcopy(f2_time)
    l_long = len(dc_f1_time+dc_f2_time)
    if l_long == 2:
        f1_time_str = dc_f1_time[0]
        f2_time_str = dc_f2_time[0]
        d1_time = datetime.datetime.strptime(f1_time_str,time_cut)
        d2_time = datetime.datetime.strptime(f2_time_str,time_cut)
        cut_d_time = (d1_time - d2_time)
        int_sec  = int(cut_d_time.days * 86400  + cut_d_time.seconds)
        c_result.append(int_sec)
    else:
        pass
    return c_result

def CutData_insert():


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()


        # 制作l1
    count_sql1 = "select count(*) from B_BYQ_table; "
    cursor.execute(count_sql1)
    long_count1 = cursor.fetchone()['count(*)']
    for page1 in range(1, long_count1 + 1):
        SQL_search1 = 'select BYQ_t_id,line_id,stopC_time from B_BYQ_table where id = %s  '%  page1
        cursor.execute(SQL_search1)
        # #获取所有记录列表
        data1 = cursor.fetchone()
        q1_id = data1["BYQ_t_id"]
        q1_line_id = data1["line_id"]
        q1_stopC_time = data1["stopC_time"]
        q1_list.append((q1_id,q1_line_id,q1_stopC_time))
    # 之前没有必要嵌套遍历！



    # 制作l2
    count_sql2 = "select count(*) from LLine_table; "
    cursor.execute(count_sql2)
    long_count2 = cursor.fetchone()['count(*)']
    for page2 in range(1, long_count2 + 1):
        SQL_search2 = 'select Line_name,Line_id,Line_StopTtime,Line_StopTtimePlus5 from LLine_table where id = %s ' % page2
        cursor.execute(SQL_search2)
        # #获取所有记录列表
        data2 = cursor.fetchone()
        NB_LINE_NAME = data2["Line_name"]
        NB_LINE_ID = data2["Line_id"]
        NB_line_stopTime = data2["Line_StopTtime"]
        NB_line_stopTime_Plus5 = data2["Line_StopTtimePlus5"]
        q2_list.append((NB_LINE_NAME,NB_LINE_ID,NB_line_stopTime,NB_line_stopTime_Plus5))







def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into Final_X_B (DT,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5) values (%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



# 直接两层遍历


# def ccc_data(l1, l2):
#
#
#
#     l3 = []
#     all_B_time= []
#     for item_q2 in l2:
#         NB_LINE_NAME = item_q2[0]
#         NB_LINE_ID = item_q2[1]
#         NB_line_stopTime = item_q2[2]
#         NB_line_stopTime_Plus5 = item_q2[3]
#         for item_q1 in l1:
#             q1_id = item_q1[0]
#             q1_line_id = item_q1[1]
#             q1_stopC_time = item_q1[2]
#
#
#             # 1.线路相同的情况下，2. 变压器停电时间大于基准表的最低时间 3. 小于增加5分钟的基准标的停电时间
#             #　4.把时间缩小在时刻（缩小在1小时之内） '2018/01/02 16:'
#             # 函数用的不对！！是copare_twoTime,不是twoTStyle!!!!
#             # if q1_line_id == NB_LINE_ID and q1_stopC_time[:14] ==NB_line_stopTime[:14] : 还输出29万条数据
#             # if NB_LINE_ID == q1_line_id and copare_twoTime(re_cut_Str(q1_stopC_time),re_cut_Str(NB_line_stopTime)) >=0 and copare_twoTime(re_cut_Str(NB_line_stopTime_Plus5),re_cut_Str(q1_stopC_time)) >= 0:
#             if NB_LINE_ID == q1_line_id : #后面的时间字段不对！！最终是形成新的大变压器表，然后根据线路再计数变压器数量
#                 all_B_time.append((q1_id,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5))
#             #     print((copare_twoTime(re_cut_Str(q1_stopC_time),re_cut_Str(NB_line_stopTime)),q1_stopC_time,NB_line_stopTime))
#             #     time.sleep(9)
#             #     print((q1_id,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5))
#             #     print((q1_id,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5))
#             else:
#                 pass
#
#         #第一步先保证线路相同，整理处理第一个的数据容器 all_B_time
#         #还是在这个函数内，用切分，计算出两组时间的如果差值为正，就添加到最终需要保留的l3,不然就剔除
#     # 是列表all_T[0]，b_time  ，是字符串   last_f[3]
#     for last_f in all_B_time:
#         # b_time = re_cut_Str(last_f[3])
#         # BB_time = re_cut_Str(last_f[4])
#         # BB_timeplus5 = re_cut_Str(last_f[5])
#         # all_T = (b_time,BB_time,BB_timeplus5)
#         # print(copare_twoTime(all_T[0],all_T[1]),copare_twoTime(all_T[2],all_T[0]),all_T)
#
#         # print(re_cut_Str(all_T[0]),re_cut_Str(all_T[1]),re_cut_Str(all_T[2]),"000",last_f[3],last_f[4],last_f[5],"000",b_time,BB_time,BB_timeplus5)
#         # time.sleep(9)
#
#         # 这个结果是一个列表
#         c1 = copare_twoTime(last_f[3],last_f[4])
#         c2 = copare_twoTime(last_f[5],last_f[3])
#         # print(c1,c2,type(c1),type(c2),c1[0],c2[0])
#         # time.sleep(0.1)# 脚本跑慢一点，没有报错！
#         try:
#
#             if c1[0] >= 0 :
#                 if c2[0] >= 0:
#                     l3.append(last_f)
#                 else:
#                     pass
#             else:
#                 pass
#         except IndexError as e:
#             pass
#     return l3

# TypeError: '>=' not supported between instances of 'NoneType' and 'int'


# 应该做一个迭代器，不然很快会报错！过不去！


if __name__ == "__main__":
    error_list = []
    l3 = []

    print(datetime.datetime.now())
    # 直接在这里写逻辑算了！
    q1_list = [] #  BYQ_t_id,line_id,stopC_time
    q2_list = [] #Line_name,Line_id,Line_StopTtime,Line_StopTtimePlus5
    CutData_insert()
    # 下面进行深拷贝，避免List报错
    q1_list_Dcopy = copy.deepcopy(q1_list)
    q2_list_Dcopy = copy.deepcopy(q2_list)
    # for item in q2_list_Dcopy:
    #     print(item)
    #     time.sleep(9)

    for q1_item in iter(q1_list_Dcopy):
        q1_table_id = q1_item[0]
        q1_line_id = q1_item[1]
        q1_stopTime = re_cut_Str(q1_item[2])  ##是列表  同样也要深度复制
        dc_q1_stopTime = copy.deepcopy(q1_stopTime)

        for q2_item in iter(q2_list_Dcopy):
            # 1.线路id相等 2. 大变压器停电时间在大基准表的中间 。干脆直接比较停电时间，把线路相同放在最后！甚至最后再重新剔除
            q2_line_name = q2_item[0]
            q2_line_id = q2_item[1]
            q2_stopTime = re_cut_Str(q2_item[2]) #是列表  同样也要深度复制
            q2_stopTimePlus5 = re_cut_Str(q2_item[3]) #是列表 同样也要深度复制
            line_3_long = len(q1_stopTime+q2_stopTime+q2_stopTimePlus5)
            if  line_3_long ==3:

                dc_q2_stopTime = copy.deepcopy(q2_stopTime)
                dc_q2_stopTimePlus5 = copy.deepcopy(q2_stopTimePlus5)
                str_q1_time = dc_q1_stopTime[0]
                str_q2_stopTime = dc_q2_stopTime[0]
                str_q2_stopTimePlus5 = dc_q2_stopTimePlus5[0]
                int_comp= copare_twoTime(str_q1_time,str_q2_stopTime)[0]

                # if q1_line_id == q2_line_id and copare_twoTime(q1_stopTime,q2_stopTime) in (0,300):
                if q1_line_id == q2_line_id :
                    print((q1_table_id,q1_line_id,q2_line_name,str_q1_time,str_q2_stopTime,str_q2_stopTimePlus5,int_comp))
                    time.sleep(9)
                    # l3.append((q1_table_id,q1_line_id,q2_line_name,q1_stopTime,q2_stopTime,q2_stopTimePlus5))
                #先整理一部分，插入数据库后再做计算！这个需要编写生成器
                # 一定需要写一个生成器，一边遍历，一边计算！不能只遍历
            else:
                pass


    # insertDB(l3)
    print("筛选出异常数据，并插入新创建的异常数据汇总表～～")
    print(datetime.datetime.now())


# print(re_cut_Str(all_T[0]), re_cut_Str(all_T[1]), re_cut_Str(all_T[2]), "000", last_f[3], last_f[4], last_f[5], "000",
#       b_time, BB_time, BB_timeplus5)

# ['2018/1/18 10:08'] ['2018/04/27 14:55'] ['2018/04/27 15:00'] 000 2018/1/18 10:08 2018/04/27 14:55:00 2018/04/27 15:00:00 000 ['2018/1/18 10:08'] ['2018/04/27 14:55'] ['2018/04/27 15:00']



# str---->datetime+ 5 ----->str

#用两个时间匹配格式！



# 选择两种模式中的一种，如果报错就是选择另外一种！
#用时间字段的长度来判断
# 这样不同的数据格式都进行比较了！





# #ValueError
#
#
# f = copare_twoTime(s2,s3)
# print(f)






# q1_id
# q1_line_id
# NB_LINE_NAME
# q1_stopC_time
# NB_line_stopTime
# NB_line_stopTime_Plus5



# DT,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5
# create table Final_X_B(
# id int not null primary key auto_increment,
# DT text,
# q1_line_id text,
# NB_LINE_NAME text,
# q1_stopC_time text,
# NB_line_stopTime text,
# NB_line_stopTime_Plus5 text,
# twoTime_cut int
# ) engine=InnoDB default charset=utf8;


