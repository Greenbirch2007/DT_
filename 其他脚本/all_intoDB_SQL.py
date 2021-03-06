


原始基准表
表名 Basic_table
导入的excel文件名: basic_table.csv


# create table Basic_table(
# id int not null primary key auto_increment,
# basic_t_id text,
# TRAN_ID text,
# TRAN_NAME text,
# LINE_ID text,
# LINE_NAME text
# ) engine=InnoDB  charset=utf8;




大变压器表
表名  B_BYQ_table
导入的excel文件名: B_BYQ_table.csv

create table B_BYQ_table(
id int not null primary key auto_increment,
BYQ_t_id text,
cu_id1 text,
cu_loc1_name text,
cu_loc2_name text,
cu_name text,
collec_id text,
taiqu_id text,
shebei_id text,
taiqu_name text,
gong_zhuan text,
line_id text,
line_num text,
line_name text,
yonghu_id text,
yonghu_name text,
dianneng_id text,
getL_style_name text,
stopC_time text,
resumeC_time text,
stopC_timeL text,
Measure_dot text,
C_presue_Col_time text,
xiangyu text,
Data_fullSign text,
t0000 text,
t0015 text,
t0030 text,
t0045 text,
t0100 text,
t0115 text,
t0130 text,
t0145 text,
t0200 text,
t0215 text,
t0230 text,
t0245 text,
t0300 text,
t0315 text,
t0330 text,
t0345 text,
t0400 text,
t0415 text,
t0430 text,
t0445 text,
t0500 text,
t0515 text,
t0530 text,
t0545 text,
t0600 text,
t0615 text,
t0630 text,
t0645 text,
t0700 text,
t0715 text,
t0730 text,
t0745 text,
t0800 text,
t0815 text,
t0830 text,
t0845 text,
t0900 text,
t0915 text,
t0930 text,
t0945 text,
t1000 text,
t1015 text,
t1030 text,
t1045 text,
t1100 text,
t1115 text,
t1130 text,
t1145 text,
t1200 text,
t1215 text,
t1230 text,
t1245 text,
t1300 text,
t1315 text,
t1330 text,
t1345 text,
t1400 text,
t1415 text,
t1430 text,
t1445 text,
t1500 text,
t1515 text,
t1530 text,
t1545 text,
t1600 text,
t1615 text,
t1630 text,
t1645 text,
t1700 text,
t1715 text,
t1730 text,
t1745 text,
t1800 text,
t1815 text,
t1830 text,
t1845 text,
t1900 text,
t1915 text,
t1930 text,
t1945 text,
t2000 text,
t2015 text,
t2030 text,
t2045 text,
t2100 text,
t2115 text,
t2130 text,
t2145 text,
t2200 text,
t2215 text,
t2230 text,
t2245 text,
t2300 text,
t2315 text,
t2330 text,
t2345 text
) engine=InnoDB  charset=utf8;


大线路表(用于反推变压器数量)
表名 B_line
导入的excel文件名: B_line.csv


create table B_line(
id int not null primary key auto_increment,
B_linetable_id text,
B_line_stopTime text,
B_line_name text,
B_line_id text,
B_line_Byq_Num text,
B_line_stopTime_Plus5 text
) engine=InnoDB  charset=utf8;









