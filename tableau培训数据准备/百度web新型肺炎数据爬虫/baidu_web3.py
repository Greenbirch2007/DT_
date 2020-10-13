# -*- coding:utf-8 -*-

import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html


# 正则和lxml混用



# 确认索引是55
# 治愈索引是56
# 死亡索引是57



# 写一个函数专门处理包在字符串里面的列表
#
# 1:将字符串去掉[ ]
# 2.将上下的字符串按照,进行分割
# 3.遍历存入新的列表中
# 再与日期，省份，分别组成一个全新的元组然后插入到数据库中




def strlist_intoList(str_item):
    cut_str = str_item[1:-1] # 将字符串去掉[ ]
    spl_str = cut_str.split(",") # 将上下的字符串按照,进行分割
    return spl_str



def insertDB(content):

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into dif_info3 (pros, city,confirmed_n,covered_n,died_n) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    big_list = []
    pro_list = ["湖北", "广东", "浙江", "河南", "湖南", "江西", "安徽", "重庆", "江苏", "山东", "四川", "北京", "上海", "黑龙江", "福建", "陕西", "广西",
                "河北", "云南", "海南", "辽宁", "山西", "天津", "贵州", "甘肃", "吉林", "内蒙古", "宁夏", "新疆", "香港", "青海", "台湾", "澳门", "西藏"]
    for pro_item in pro_list:

        url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1&city={0}-{1}'.format(pro_item,pro_item)
        html = get_first_page(url)
        selector = etree.HTML(html)
        try:

            dif_city = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a/div[1]/text()')
            dif_c_confirmed_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/text()')
            dif_c_convered_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/text()')
            dif_c_died_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/text()')
            l_pro = len(dif_city) * [pro_item]
            if len(dif_city) != 0:

                for i1,i2,i3,i4,i5 in zip(l_pro,dif_city,dif_c_confirmed_n,dif_c_convered_n,dif_c_died_n):
                    big_list.append((i1,i2,i3,i4,i5))
            else:
                pass
        except :
            pass

    insertDB(big_list)









# pros, city,confirmed_n,covered_n,died_n
# create table dif_info3(
# id int not null primary key auto_increment,
# pros varchar(50),
# city varchar(50),
# confirmed_n varchar(50),
# covered_n varchar(50),
# died_n varchar(50)
# ) engine=InnoDB  charset=utf8;


# drop table dif_info3;