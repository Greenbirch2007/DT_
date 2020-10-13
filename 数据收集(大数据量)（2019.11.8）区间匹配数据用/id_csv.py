


import csv


#　#　#　with open(csvfilepath,'r',newline='',encoding="utf-8")　
# 此时提出utf-8
import time


def readcsv(csvfilepath):# 列表方式读取
    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象


        for row in reader:
            base_table_id = row[0]
            base_table_Lid = row[1]
            oper_table_Lid = row[2]
            oper_table_time = row[3]
            base_list.append((base_table_id,base_table_Lid))
            oper_lineTime_list.append((oper_table_Lid,oper_table_time))

# 基准表的线路ID
# ('要匹配的线路ID', '停电时间')



if __name__=="__main__":
    base_list = []  # 基准表的线路ID
    oper_lineTime_list = []  # ('要匹配的线路ID', '停电时间')
    readcsv(r"G:\\feiq file\李康(1CC1DE329CAE)\ts.csv")
    print(len(base_list))
    print(len(oper_lineTime_list))




