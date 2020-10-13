# coding=utf-8

# import xlrd
#
# # 打开文件
# data = xlrd.open_workbook('/home/w/Desktop/t1.xlsx')
#
# # 查看工作表
# data.sheet_names()
# print("sheets：" + str(data.sheet_names()))

# 通过文件名获得工作表,获取工作表1
# table = data.sheet_by_name('工作表1')

# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
# table = data.sheet_by_index(0)

# 获取行数和列数
# 行数：table.nrows
# 列数：table.ncols
# print("总行数：" + str(table.nrows))
# print("总列数：" + str(table.ncols))

# 获取整行的值 和整列的值，返回的结果为数组
# 整行值：table.row_values(start,end)
# 整列值：table.col_values(start,end)
# 参数 start 为从第几个开始打印，
# end为打印到那个位置结束，默认为none
# print("整行值：" + str(table.row_values(0)))
# print("整列值：" + str(table.col_values(1)))
#
# # 获取某个单元格的值，例如获取B3单元格值
# cel_B3 = table.cell(3,2).value
# print("第三行第二列的值：" + cel_B3)


  # coding=utf-8
import xlrd
import time
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile

#
# def ccc_data(l1,l2):
#     l3 = []
#     for item_q1 in lq

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == '__main__':
    l1 = []
    excelFile1 = '/home/w/Desktop/data_work/t2.xlsx'
    full_items1 = read_xlrd(excelFile=excelFile1)
    for item in full_items1:
        l1.append((item[0],item[1],item[2]))
        # l1.append((item[1],item[2]))
    for i in l1:
        print(i)



    # excelFile2 = '/home/w/Desktop/data_work/t2.xlsx'
    # full_items2 = read_xlrd(excelFile=excelFile2)
    # for item in full_items2:
    #     print(item[1],",",item[2])





