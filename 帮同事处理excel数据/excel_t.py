# coding=utf-8



  # coding=utf-8
import xlrd

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
    excelFile = '/home/w/帮同事处理excel数据/t1.xlsx'
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
        print(one_list)


