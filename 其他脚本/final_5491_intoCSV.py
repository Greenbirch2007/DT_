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
    count_sql = "select count(*) from Final_fff; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count+1):


        sql = 'select  DT,q1_line_id,NB_LINE_NAME,q1_stopC_time,NB_line_stopTime,NB_line_stopTime_Plus5,twoTime_cut from Final_fff where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    print(big_list)
    head = ['DT','q1_line_id',"NB_LINE_NAME","q1_stopC_time","NB_line_stopTime",'NB_line_stopTime_Plus5','twoTime_cut']
    csv_dict_write('E:\\final_5191_.csv',head,big_list)
    print("数据导出完成～")