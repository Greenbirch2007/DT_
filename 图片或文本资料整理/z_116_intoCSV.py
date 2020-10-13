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
    count_sql = "select count(*) from f_NBBT_DYDL_t; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count+1):
        sql = 'select shebei_id,shebei_name,SBBM_ID,line_id,XBGXT_line_name,LineEStop_line_name,xbgxt_TG_ID,city_Name,Country_Name,Yunwei_name,BdZ_name,Sale_line_id,E_StopTime,E_ResumeTime,StopTime_Long,StopTime_Date,DYDL_TG_ID,ID_i,DATA_DATE,PHASE_FLAG,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41,U42,U43,U44,U45,U46,U47,U48,U49,U50,U51,U52,U53,U54,U55,U56,U57,U58,U59,U60,U61,U62,U63,U64,U65,U66,U67,U68,U69,U70,U71,U72,U73,U74,U75,U76,U77,U78,U79,U80,U81,U82,U83,U84,U85,U86,U87,U88,U89,U90,U91,U92,U93,U94,U95,U96 from f_NBBT_DYDL_t where id = %s ' % num

        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    print(big_list)
    head = ["shebei_id","shebei_name","SBBM_ID","line_id","XBGXT_line_name","LineEStop_line_name","xbgxt_TG_ID","city_Name","Country_Name","Yunwei_name","BdZ_name","Sale_line_id","E_StopTime","E_ResumeTime","StopTime_Long","StopTime_Date","DYDL_TG_ID","ID_i","DATA_DATE","PHASE_FLAG","U1","U2","U3","U4","U5","U6","U7","U8","U9","U10","U11","U12","U13","U14","U15","U16","U17","U18","U19","U20","U21","U22","U23","U24","U25","U26","U27","U28","U29","U30","U31","U32","U33","U34","U35","U36","U37","U38","U39","U40","U41","U42","U43","U44","U45","U46","U47","U48","U49","U50","U51","U52","U53","U54","U55","U56","U57","U58","U59","U60","U61","U62","U63","U64","U65","U66","U67","U68","U69","U70","U71","U72","U73","U74","U75","U76","U77","U78","U79","U80","U81","U82","U83","U84","U85","U86","U87","U88","U89","U90","U91","U92","U93","U94","U95","U96"]

    csv_dict_write('E:\\f_NBBT_DYDL_t116.csv',head,big_list)
    print("数据导出完成～")

