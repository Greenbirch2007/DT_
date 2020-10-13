import pymysql
import csv

# 数据处理好，看如何塞入execl中


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True



if __name__ =='__main__':
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    # sql 语句
    count_sql = "select count(*) from error_table_n_n; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count):


        sql = 'select DT,byq_name,Oper_line_name,Baseline_line_name,q1_line_id,q2_LINE_ID from error_table_n_n where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    print(big_list)
    head = ['DT','byq_name',"Oper_line_name","Baseline_line_name",'q1_line_id','q2_LINE_ID']
    csv_dict_write('E:\\error_table_n_n.csv',head,big_list)
    print("数据导出完成～")