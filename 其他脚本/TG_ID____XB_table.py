#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy
import csv



# 处理逻辑：(都是使用csv标准库模块)
# 1. 用TG_ID的PMS_EQUIP_ID与线变关系表的TRAN_ID(设备id)匹配,
# 2. 往线变关系表中插入TG_ID的一个新列
def re_cut_Str(item):
    if type(item) != str:
        str_item = str(item)

    else:
        str_item = item
    patt =re.compile("\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}",re.S)
    ite = re.findall(patt,str_item)
    return ite


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True

def readcsv(csvfilepath):# 列表方式读取
    base_list = []  # 基准表的编号，变压器编号，变压器名称，线路编号，线路名称

    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象


        for row in reader:
            DT_id = row
            base_list.append(DT_id)
    return base_list







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

def GetData_fromCSV():

    tg_id = readcsv(r"E:\\TG_ID____XB_table\\TG_ID.csv")
    for q1_item in tg_id:
        q1_list.append(tuple(q1_item))

    XB_table = readcsv(r"E:\\TG_ID____XB_table\\XB_table.csv")
    for q2_item in XB_table:
        q2_list.append(tuple(q2_item))








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into TG_ID____XB_table (shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID) values (%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass



# 直接两层遍历


# def ccc_data(l1, l2):
#
#     l3 = []
#     for item_q2 in l2:
#         q2_shebei_id = item_q2[0]
#         q2_shebei_name = item_q2[1]
#         q2_SBBM_ID = item_q2[2]
#         q2_line_id= item_q2[3]
#         q2_line_name= item_q2[4]
#         for item_q1 in l1:
#             q1_PMS_EQUIP_ID = item_q1[0]
#             q1_TG_ID = item_q1[1]
#
#             try:
#                 if q1_PMS_EQUIP_ID == q2_shebei_id:
#                     l3.append((q1_PMS_EQUIP_ID,q1_TG_ID,q2_shebei_name,q2_SBBM_ID,q2_line_id,q2_line_name))
#
#                 else:
#                     pass
#             except IndexError as e:
#                 pass
#     return l3






if __name__ == "__main__":
    l3 = []

    print(datetime.datetime.now())
    # 直接在这里写逻辑算了！
    q1_list = [] # 'PMS_EQUIP_ID', 'TG_ID'
    q2_list = [] # shebei_id,shebei_name,SBBM_ID,line_id,line_name
    # 不要一一匹配，这样会造成重复！就选择一个
    # 不应该从遍历的
    GetData_fromCSV()
    # q1_list_Dcopy = copy.deepcopy(q1_list) # 进行深拷贝，避免List报错
    # q2_list_Dcopy = copy.deepcopy(q2_list) # 进行深拷贝，避免List报错
    print(len(q1_list))
    print(len(q2_list))
    for q1_item in q1_list:
        q1_shebei_id =q1_item[0]
        q1_TG_id =q1_item[1]
        for q2_item in q2_list:
            q2_shebei_id = q2_item[0]
            if q2_shebei_id == q1_shebei_id:
                f_t_content = q2_item + (q1_TG_id,)
                l3.append(f_t_content)
            else:
                pass
    insertDB(l3)
    print("匹配添加tg_id完成")
    print(datetime.datetime.now())






# shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,TG_ID
# create table TG_ID____XB_table(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# XBGXT_line_name text,
# TG_ID text
# ) engine=InnoDB default charset=utf8;


#  drop table TG_ID____XB_table;

