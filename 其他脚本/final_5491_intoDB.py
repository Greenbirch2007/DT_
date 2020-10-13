#-*- coding:utf-8 -*-


import csv


#　#　#　with open(csvfilepath,'r',newline='',encoding="utf-8")　
# 此时提出utf-8
import time

import pymysql


def readcsv(csvfilepath):# 列表方式读取
    base_list = []  # 基准表的编号，变压器编号，变压器名称，线路编号，线路名称

    with open(csvfilepath,'r',newline='') as csvfile:
        reader = csv.reader(csvfile) #创建csv.reader 对象


        for row in reader:
            BYQ_t_id = row[0]
            cu_id1 = row[1]
            cu_loc1_name = row[2]
            cu_loc2_name = row[3]
            cu_name = row[4]
            collec_id = row[5]
            taiqu_id = row[6]
            shebei_id = row[7]
            taiqu_name = row[8]
            gong_zhuan = row[9]
            line_id = row[10]
            line_num = row[11]
            line_name = row[12]
            yonghu_id = row[13]
            yonghu_name = row[14]
            dianneng_id = row[15]
            getL_style_name = row[16]
            stopC_time = row[17]
            resumeC_time = row[18]
            stopC_timeL = row[19]
            Measure_dot = row[20]
            C_presue_Col_time = row[21]
            xiangyu = row[22]
            Data_fullSign = row[23]
            t0000 = row[24]
            t0015 = row[25]
            t0030 = row[26]
            t0045 = row[27]
            t0100 = row[28]
            t0115 = row[29]
            t0130 = row[30]
            t0145 = row[31]
            t0200 = row[32]
            t0215 = row[33]
            t0230 = row[34]
            t0245 = row[35]
            t0300 = row[36]
            t0315 = row[37]
            t0330 = row[38]
            t0345 = row[39]
            t0400 = row[40]
            t0415 = row[41]
            t0430 = row[42]
            t0445 = row[43]
            t0500 = row[44]
            t0515 = row[45]
            t0530 = row[46]
            t0545 = row[47]
            t0600 = row[48]
            t0615 = row[49]
            t0630 = row[50]
            t0645 = row[51]
            t0700 = row[52]
            t0715 = row[53]
            t0730 = row[54]
            t0745 = row[55]
            t0800 = row[56]
            t0815 = row[57]
            t0830 = row[58]
            t0845 = row[59]
            t0900 = row[60]
            t0915 = row[61]
            t0930 = row[62]
            t0945 = row[63]
            t1000 = row[64]
            t1015 = row[65]
            t1030 = row[66]
            t1045 = row[67]
            t1100 = row[68]
            t1115 = row[69]
            t1130 = row[70]
            t1145 = row[71]
            t1200 = row[72]
            t1215 = row[73]
            t1230 = row[74]
            t1245 = row[75]
            t1300 = row[76]
            t1315 = row[77]
            t1330 = row[78]
            t1345 = row[79]
            t1400 = row[80]
            t1415 = row[81]
            t1430 = row[82]
            t1445 = row[83]
            t1500 = row[84]
            t1515 = row[85]
            t1530 = row[86]
            t1545 = row[87]
            t1600 = row[88]
            t1615 = row[89]
            t1630 = row[90]
            t1645 = row[91]
            t1700 = row[92]
            t1715 = row[93]
            t1730 = row[94]
            t1745 = row[95]
            t1800 = row[96]
            t1815 = row[97]
            t1830 = row[98]
            t1845 = row[99]
            t1900 = row[100]
            t1915 = row[101]
            t1930 = row[102]
            t1945 = row[103]
            t2000 = row[104]
            t2015 = row[105]
            t2030 = row[106]
            t2045 = row[107]
            t2100 = row[108]
            t2115 = row[109]
            t2130 = row[110]
            t2145 = row[111]
            t2200 = row[112]
            t2215 = row[113]
            t2230 = row[114]
            t2245 = row[115]
            t2300 = row[116]
            t2315 = row[117]
            t2330 = row[118]
            t2345 = row[119]

            # print((BYQ_t_id,cu_id1,cu_loc1_name,cu_loc2_name,cu_name,collec_id,taiqu_id,shebei_id,taiqu_name,gong_zhuan,line_id,line_num,line_name,yonghu_id,yonghu_name,dianneng_id,getL_style_name,stopC_time,resumeC_time,stopC_timeL,Measure_dot,C_presue_Col_time,xiangyu,Data_fullSign,t0000,t0015,t0030,t0045,t0100,t0115,t0130,t0145,t0200,t0215,t0230,t0245,t0300,t0315,t0330,t0345,t0400,t0415,t0430,t0445,t0500,t0515,t0530,t0545,t0600,t0615,t0630,t0645,t0700,t0715,t0730,t0745,t0800,t0815,t0830,t0845,t0900,t0915,t0930,t0945,t1000,t1015,t1030,t1045,t1100,t1115,t1130,t1145,t1200,t1215,t1230,t1245,t1300,t1315,t1330,t1345,t1400,t1415,t1430,t1445,t1500,t1515,t1530,t1545,t1600,t1615,t1630,t1645,t1700,t1715,t1730,t1745,t1800,t1815,t1830,t1845,t1900,t1915,t1930,t1945,t2000,t2015,t2030,t2045,t2100,t2115,t2130,t2145,t2200,t2215,t2230,t2245,t2300,t2315,t2330,t2345))

            base_list.append((BYQ_t_id,cu_id1,cu_loc1_name,cu_loc2_name,cu_name,collec_id,taiqu_id,shebei_id,taiqu_name,gong_zhuan,line_id,line_num,line_name,yonghu_id,yonghu_name,dianneng_id,getL_style_name,stopC_time,resumeC_time,stopC_timeL,Measure_dot,C_presue_Col_time,xiangyu,Data_fullSign,t0000,t0015,t0030,t0045,t0100,t0115,t0130,t0145,t0200,t0215,t0230,t0245,t0300,t0315,t0330,t0345,t0400,t0415,t0430,t0445,t0500,t0515,t0530,t0545,t0600,t0615,t0630,t0645,t0700,t0715,t0730,t0745,t0800,t0815,t0830,t0845,t0900,t0915,t0930,t0945,t1000,t1015,t1030,t1045,t1100,t1115,t1130,t1145,t1200,t1215,t1230,t1245,t1300,t1315,t1330,t1345,t1400,t1415,t1430,t1445,t1500,t1515,t1530,t1545,t1600,t1615,t1630,t1645,t1700,t1715,t1730,t1745,t1800,t1815,t1830,t1845,t1900,t1915,t1930,t1945,t2000,t2015,t2030,t2045,t2100,t2115,t2130,t2145,t2200,t2215,t2230,t2245,t2300,t2315,t2330,t2345))
    return base_list

def insertDB(content):
    try:

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='DT',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.executemany('insert into final_5491_inDB (BYQ_t_id,cu_id1,cu_loc1_name,cu_loc2_name,cu_name,collec_id,taiqu_id,shebei_id,taiqu_name,gong_zhuan,line_id,line_num,line_name,yonghu_id,yonghu_name,dianneng_id,getL_style_name,stopC_time,resumeC_time,stopC_timeL,Measure_dot,C_presue_Col_time,xiangyu,Data_fullSign,t0000,t0015,t0030,t0045,t0100,t0115,t0130,t0145,t0200,t0215,t0230,t0245,t0300,t0315,t0330,t0345,t0400,t0415,t0430,t0445,t0500,t0515,t0530,t0545,t0600,t0615,t0630,t0645,t0700,t0715,t0730,t0745,t0800,t0815,t0830,t0845,t0900,t0915,t0930,t0945,t1000,t1015,t1030,t1045,t1100,t1115,t1130,t1145,t1200,t1215,t1230,t1245,t1300,t1315,t1330,t1345,t1400,t1415,t1430,t1445,t1500,t1515,t1530,t1545,t1600,t1615,t1630,t1645,t1700,t1715,t1730,t1745,t1800,t1815,t1830,t1845,t1900,t1915,t1930,t1945,t2000,t2015,t2030,t2045,t2100,t2115,t2130,t2145,t2200,t2215,t2230,t2245,t2300,t2315,t2330,t2345)'
                           ' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


if __name__=="__main__":

    db_table =readcsv(r"E:\\final_5491_From_Bbyq.csv")

    insertDB(db_table)
    print("~~~~~成功插入数据库~~~~~~~·")
    # for item in db_table:
    #     print(item)
    #     print(len(item))
    #     time.sleep(9)



# drop table final_5491_inDB;


# create table final_5491_inDB(
# id int not null primary key auto_increment,
# BYQ_t_id text,
# cu_id1 text,
# cu_loc1_name text,
# cu_loc2_name text,
# cu_name text,
# collec_id text,
# taiqu_id text,
# shebei_id text,
# taiqu_name text,
# gong_zhuan text,
# line_id text,
# line_num text,
# line_name text,
# yonghu_id text,
# yonghu_name text,
# dianneng_id text,
# getL_style_name text,
# stopC_time text,
# resumeC_time text,
# stopC_timeL text,
# Measure_dot text,
# C_presue_Col_time text,
# xiangyu text,
# Data_fullSign text,
# t0000 text,
# t0015 text,
# t0030 text,
# t0045 text,
# t0100 text,
# t0115 text,
# t0130 text,
# t0145 text,
# t0200 text,
# t0215 text,
# t0230 text,
# t0245 text,
# t0300 text,
# t0315 text,
# t0330 text,
# t0345 text,
# t0400 text,
# t0415 text,
# t0430 text,
# t0445 text,
# t0500 text,
# t0515 text,
# t0530 text,
# t0545 text,
# t0600 text,
# t0615 text,
# t0630 text,
# t0645 text,
# t0700 text,
# t0715 text,
# t0730 text,
# t0745 text,
# t0800 text,
# t0815 text,
# t0830 text,
# t0845 text,
# t0900 text,
# t0915 text,
# t0930 text,
# t0945 text,
# t1000 text,
# t1015 text,
# t1030 text,
# t1045 text,
# t1100 text,
# t1115 text,
# t1130 text,
# t1145 text,
# t1200 text,
# t1215 text,
# t1230 text,
# t1245 text,
# t1300 text,
# t1315 text,
# t1330 text,
# t1345 text,
# t1400 text,
# t1415 text,
# t1430 text,
# t1445 text,
# t1500 text,
# t1515 text,
# t1530 text,
# t1545 text,
# t1600 text,
# t1615 text,
# t1630 text,
# t1645 text,
# t1700 text,
# t1715 text,
# t1730 text,
# t1745 text,
# t1800 text,
# t1815 text,
# t1830 text,
# t1845 text,
# t1900 text,
# t1915 text,
# t1930 text,
# t1945 text,
# t2000 text,
# t2015 text,
# t2030 text,
# t2045 text,
# t2100 text,
# t2115 text,
# t2130 text,
# t2145 text,
# t2200 text,
# t2215 text,
# t2230 text,
# t2245 text,
# t2300 text,
# t2315 text,
# t2330 text,
# t2345 text
# ) engine=InnoDB  charset=utf8;
