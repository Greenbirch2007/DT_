

第一步，先将TG_ID匹配近线变关系表(直接用Excel来处理，然后录入到数据库中)
TG_ID____XB_table
# create table TG_ID____XB_table(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# line_name text,
# TG_ID text
# ) engine=InnoDB default charset=utf8;


# 将2018.7-2019 线路停电表数据录入数据库



LineStop_Table201807_2019
# create table LineStop_Table201807_2019(
# id int not null primary key auto_increment,
# city_Name text,
# Country_Name text,
# Yunwei_name text,
# BdZ_name text,
# Sale_line_id text,
# PMS_line_id text,
# line_name text,
# E_StopTime text,
# E_ResumeTime text,
# StopTime_Long text,
# StopTime_Date text
# ) engine=InnoDB default charset=utf8;

地市单位	city_Name
区县单位	Country_Name
运维班组	Yunwei_name
变电站名称	BdZ_name
营销线路编号	Sale_line_id
PMS线路编码	PMS_line_id
线路名称	line_name
停电时间	E_StopTime
复电时间	E_ResumeTime
停电时长	StopTime_Long
停电日期	StopTime_Date


全新大基准表的

# 从下路停电表中剔除了
# SBBM_id和线路名称
# 一共剩下15个字段

# create table Get_NewBasci_Table(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# line_name text,
# TG_ID text,
# city_Name text,
# Country_Name text,
# Yunwei_name text,
# BdZ_name text,
# Sale_line_id text,
# E_StopTime text,
# E_ResumeTime text,
# StopTime_Long text,
# StopTime_Date text
# ) engine=InnoDB default charset=utf8;


大基准表（3.3万条） 与Oracle数据库中的电压电流数据表，匹配检查出在线路停电的情况下，没有停电的部分


#  最终拼凑出来的表就是    大基准表(15个字段) + 电压电流表(100个字段)  一个共115个字段


# create table f_NBBT_DYDL_t(
# id int not null primary key auto_increment,
# shebei_id text,
# shebei_name text,
# SBBM_ID text,
# line_id text,
# line_name text,
# n_bt_TG_ID text,
# city_Name text,
# Country_Name text,
# Yunwei_name text,
# BdZ_name text,
# Sale_line_id text,
# E_StopTime text,
# E_ResumeTime text,
# StopTime_Long text,
# StopTime_Date text,
# DYDL_TG_ID text,
# ID_i text,
# DATA_DATE text,
# PHASE_FLAG text,
# U1 text,
# U2 text,
# U3 text,
# U4 text,
# U5 text,
# U6 text,
# U7 text,
# U8 text,
# U9 text,
# U10 text,
# U11 text,
# U12 text,
# U13 text,
# U14 text,
# U15 text,
# U16 text,
# U17 text,
# U18 text,
# U19 text,
# U20 text,
# U21 text,
# U22 text,
# U23 text,
# U24 text,
# U25 text,
# U26 text,
# U27 text,
# U28 text,
# U29 text,
# U30 text,
# U31 text,
# U32 text,
# U33 text,
# U34 text,
# U35 text,
# U36 text,
# U37 text,
# U38 text,
# U39 text,
# U40 text,
# U41 text,
# U42 text,
# U43 text,
# U44 text,
# U45 text,
# U46 text,
# U47 text,
# U48 text,
# U49 text,
# U50 text,
# U51 text,
# U52 text,
# U53 text,
# U54 text,
# U55 text,
# U56 text,
# U57 text,
# U58 text,
# U59 text,
# U60 text,
# U61 text,
# U62 text,
# U63 text,
# U64 text,
# U65 text,
# U66 text,
# U67 text,
# U68 text,
# U69 text,
# U70 text,
# U71 text,
# U72 text,
# U73 text,
# U74 text,
# U75 text,
# U76 text,
# U77 text,
# U78 text,
# U79 text,
# U80 text,
# U81 text,
# U82 text,
# U83 text,
# U84 text,
# U85 text,
# U86 text,
# U87 text,
# U88 text,
# U89 text,
# U90 text,
# U91 text,
# U92 text,
# U93 text,
# U94 text,
# U95 text,
# U96 text
# ) engine=InnoDB default charset=utf8;