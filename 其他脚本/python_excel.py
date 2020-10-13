#-*- coding:utf-8 -*-


import xlrd
import csv

# 1.读取两个表 运行表命名为t1  基准表命名为t2
# 2. 提取t1的序号，变压器名称，线路名称    提取t2的，变压器名称，线路名称
# 3. 匹配之后，输出t1的序号，单独存储
# 4. 然后用 再次读取t1，按照匹配后的序号去匹配t1中的相关数据
# 5. 导出相关的
# Demo_BYQ1.csv     Demo_BYQ2.csv  Demo_BYwQ1.csv

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

# t1.csv 有185条记录
# t2.csv 有170条数据


# 去掉表头



def ccc_data(l1,l2):
    l3 = []

    for item_q1 in l1:
        qq = item_q1[1:3]

        if (qq not in l2):
            l3.append(item_q1)

    return  l3


def read_csv():
    csvFile1 = open('E:\\t1.csv','r')  # 注意这里必须要用\\ 双斜杠
    reader1 = csv.reader(csvFile1)
    csvFile2 = open('E:\\t2.csv','r')  # 注意这里必须要用\\ 双斜杠
    reader2 = csv.reader(csvFile2)

    # 得到两个列表 : reader1 为实际运行数据， reader2为基准数据
    l1 = []
    l2 =[]
    for item1 in reader1:
        l1.append(item1)
    for item2 in reader2:
        l2.append(item2[1:3])
    c = ccc_data(l1,l2)
    return c











#　写入  csv文件


def write_csv(content):
    csvFile = open('E:\\fff_data.csv','w')  # 创建csv文件
    writer = csv.writer(csvFile)   # 创建写的对象
    #先写入columns_name
    writer.writerrows(["ID","BYQ_NUM","XL_NUM","ITEM"])
    writer.writerrows(content)
    csvFile.close()


if __name__ == "__main__":
    with open('E:\\fff_data.csv','w',encoding='utf-8',newline='') as f:
        r = read_csv()
        writer = csv.writer(f)
        headers = ["ID","BYQ_NUM","XL_NUM","ITEM"]
        writer.writerrow(headers)
        writer.writerrows(r)

        print("匹配并输出文件~")

# print(c)
# if __name__ == '__main__':
#     excelFile = 'E:\Demo_BYQ1.csv'
    # 先把单表的名字容器给弄出来
    # names_list = set()
    # for item in read_xlrd(excelFile=excelFile):
    #     names_list.add(item[0])
    # full_items = read_xlrd(excelFile=excelFile)
    # print(full_items)
    # names_list = set()
    # for item in read_xlrd(excelFile=excelFile):
    #     names_list.add(item[4])
    # full_items = read_xlrd(excelFile=excelFile)
    # for single_name in names_list:
    #     one_list = []
    #     two_list = []
    #
    #     one_list.append(single_name)
    #     for item in full_items:
    #         if single_name == item[4]:
    #             two_list.append(item[3])
    #         else:
    #             pass
    #     print(one_list,two_list)


