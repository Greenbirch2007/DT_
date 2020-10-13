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
        cursor.executemany('insert into dif_info2 (pro_name,dif_p_confirmed_n,dif_p_covered_n,dif_p_died_n) values (%s,%s,%s,%s)', content)
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
    a_url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'

    html = get_first_page(a_url)
    selector = etree.HTML(html)
    pro_name = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr/td[1]/div/span[2]/text()')
    dif_p_confirmed_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr/td[2]/text()')
    dif_p_covered_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr/td[3]/text()')
    dif_p_died_n = selector.xpath('//*[@id="ptab-0"]/div[6]/div[2]/table/tbody/tr/td[4]/text()')

    for i1,i2,i3,i4 in zip(pro_name,dif_p_confirmed_n,dif_p_covered_n,dif_p_died_n):

        big_list.append((i1,i2,i3,i4))
    insertDB(big_list)









# pro_name,dif_p_confirmed_n,dif_p_covered_n,dif_p_died_n
# create table dif_info2(
# id int not null primary key auto_increment,
# pro_name varchar(50),
# dif_p_confirmed_n int,
# dif_p_covered_n int,
# dif_p_died_n varchar(10)
# ) engine=InnoDB  charset=utf8;


# drop table dif_info2;