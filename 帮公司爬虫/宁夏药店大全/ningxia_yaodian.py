#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver



def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    return html








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DT',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into ningxia_yaodian (name,address) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)


    for item in range(1,81):
        url  = 'http://www.5cm.cn/yaodian/ningxia/'+str(item)+'/'
        html = get_one_page(url)

        selector = etree.HTML(html)
        name = selector.xpath('/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr/td[1]/a/text()')

        address = selector.xpath('/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr/td[3]/text()')

        for i1, i2 in zip(name, address):
            big_list.append((i1, i2))

    insertDB(big_list)


#
# create table ningxia_yaodian(
# id int not null primary key auto_increment,
# name text,
# address text
# ) engine=InnoDB  charset=utf8;


# drop  table ningxia_yaodian;