import datetime

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
    set_l = set()
    # sql 语句
    count_sql = "select BYQ_t_id from 2_4w_5400_B_X; "
    cur.execute(count_sql)
    data = cur.fetchall()
    for i_da in data:
        d_id =i_da["BYQ_t_id"]
        set_l.add(d_id)

    big_list = []
    try:
        for item in set_l:
            sql = 'select BYQ_t_id,cu_id1,cu_loc1_name,cu_loc2_name,cu_name,collec_id,taiqu_id,shebei_id,taiqu_name,gong_zhuan,line_id,line_num,line_name,yonghu_id,yonghu_name,dianneng_id,getL_style_name,stopC_time,resumeC_time,stopC_timeL,Measure_dot,C_presue_Col_time,xiangyu,Data_fullSign,t0000,t0015,t0030,t0045,t0100,t0115,t0130,t0145,t0200,t0215,t0230,t0245,t0300,t0315,t0330,t0345,t0400,t0415,t0430,t0445,t0500,t0515,t0530,t0545,t0600,t0615,t0630,t0645,t0700,t0715,t0730,t0745,t0800,t0815,t0830,t0845,t0900,t0915,t0930,t0945,t1000,t1015,t1030,t1045,t1100,t1115,t1130,t1145,t1200,t1215,t1230,t1245,t1300,t1315,t1330,t1345,t1400,t1415,t1430,t1445,t1500,t1515,t1530,t1545,t1600,t1615,t1630,t1645,t1700,t1715,t1730,t1745,t1800,t1815,t1830,t1845,t1900,t1915,t1930,t1945,t2000,t2015,t2030,t2045,t2100,t2115,t2130,t2145,t2200,t2215,t2230,t2245,t2300,t2315,t2330,t2345 from final_5491_indb where BYQ_t_id = %s ' % item
            # #执行sql语句
            cur.execute(sql)
            # #获取所有记录列表
            data = cur.fetchone()
            big_list.append(data)
        print(big_list)
        head = ["BYQ_t_id","cu_id1","cu_loc1_name","cu_loc2_name","cu_name","collec_id","taiqu_id","shebei_id","taiqu_name","gong_zhuan","line_id","line_num","line_name","yonghu_id","yonghu_name","dianneng_id","getL_style_name","stopC_time","resumeC_time","stopC_timeL","Measure_dot","C_presue_Col_time","xiangyu","Data_fullSign","t0000","t0015","t0030","t0045","t0100","t0115","t0130","t0145","t0200","t0215","t0230","t0245","t0300","t0315","t0330","t0345","t0400","t0415","t0430","t0445","t0500","t0515","t0530","t0545","t0600","t0615","t0630","t0645","t0700","t0715","t0730","t0745","t0800","t0815","t0830","t0845","t0900","t0915","t0930","t0945","t1000","t1015","t1030","t1045","t1100","t1115","t1130","t1145","t1200","t1215","t1230","t1245","t1300","t1315","t1330","t1345","t1400","t1415","t1430","t1445","t1500","t1515","t1530","t1545","t1600","t1615","t1630","t1645","t1700","t1715","t1730","t1745","t1800","t1815","t1830","t1845","t1900","t1915","t1930","t1945","t2000","t2015","t2030","t2045","t2100","t2115","t2130","t2145","t2200","t2215","t2230","t2245","t2300","t2315","t2330","t2345"]
        csv_dict_write('E:\\2_4w_5400_intoCSV.csv',head,big_list)
        print("数据导出完成～")
        print(datetime.datetime.now())
    except:
        pass