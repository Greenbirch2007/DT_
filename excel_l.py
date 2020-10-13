# coding=utf-8


import xlrd
import pandas as pd
import os

# 创建的目录

def mkdir():
    loc_getcwd = os.getcwd()
    path = "{0}/Outputs".format(loc_getcwd)
    #如果存在目录先删除，如果不存在就创建
    if os.path.exists(path):
        os.removedirs(path)
    else:
        os.mkdir(path)
    return path

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile


if __name__ == '__main__':
    loc_getcwd = os.getcwd()
    # excelFile = '{0}\a.xlsx'.format(loc_getcwd) # windows and linux！
    excelFile = '{0}/t1.xlsx'.format(loc_getcwd) # 处理了文件属于当前目录下！
    ln = mkdir()
    f_list=[]

    # 先把单表的名字容器给弄出来
    names_list = set()
    for item in read_xlrd(excelFile=excelFile):
        names_list.add(item[0])
    full_items = read_xlrd(excelFile=excelFile)
    for single_name  in names_list:
        one_list = []
        one_list.append(single_name)
        for item in full_items:
            if single_name == item[0]:
                one_list.append(item[1])
            else:
                pass
        first_item = one_list[0]
        last_item = one_list[1:]
        strNums = [str(x) for x in last_item]
        l_last= ",".join(strNums)
        f_list.append((first_item,l_last))


    columns = ["表名", "字段名"]
    allC_dt = pd.DataFrame(f_list,columns=columns)
    allC_dt.to_excel("{0}/数据表和字段名汇总.xlsx".format(ln), index=0)




