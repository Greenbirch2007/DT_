


import csv
import datetime

#　#　#　with open(csvfilepath,'r',newline='',encoding="utf-8")　
# 此时提出utf-8
import time


def readcsv(csvfilepath):# 列表方式读取
    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象
        for row in reader:
            base_table_id = row[0]
            base_table_Lid = row[1]
            base_list.append((base_table_id,base_table_Lid))



def readcsv1(csvfilepath):# 列表方式读取
    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象
        for row in reader:
            oper_table_Lid = row[0]
            oper_table_time = row[1]
            oper_lineTime_list.append((oper_table_Lid,oper_table_time))



def writecsv(csvfilepath,l_content): #以列表的方式写入
    with open(csvfilepath,"a+",newline='') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        writer.writerows(l_content) #写入多行

    # 基准表的线路ID
# ('要匹配的线路ID', '停电时间')
#84850　用csv模块读取两个csv文件，然后再用数据结构处理
#3304

#将输出结果重新保存为csv 文件
if __name__=="__main__":
    print(datetime.datetime.now())
    base_list = []  # 基准表的线路ID
    oper_lineTime_list = []  # ('要匹配的线路ID', '停电时间')
    f_list = []
    readcsv(r"G:\\feiq file\李康(1CC1DE329CAE)\ts.csv")
    readcsv1(r"G:\\feiq file\李康(1CC1DE329CAE)\ts1.csv")
    # print(len(base_list))
    # print(len(oper_lineTime_list))

    for ope_item in oper_lineTime_list:
        for b_item in base_list:
            if ope_item[0] == b_item[1]: #如果线路id匹配成功
                b_item_list = list(b_item) #先将基准表的前面元组，进行列表化
                b_item_list.append(ope_item[1])# 再插入匹配成功的后一个元组的第二个元素
                f_tuple = tuple(b_item_list) #再将匹配结果元组化
                f_list.append(f_tuple) #最后添加到一个新容器即可
            else:
                pass

    writecsv(r"G:\\feiq file\李康(1CC1DE329CAE)\f_table.csv",f_list)
    print("匹配输出完成")
    print(datetime.datetime.now())






