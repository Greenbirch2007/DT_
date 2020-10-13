#! coding:utf-8 -*-
import time
import os
import requests
import re
import urllib
from requests.exceptions import RequestException
from GDG_link import f_l

class Gdgvedio(object):
    def __init__(self,url):
        self.url =url
    def get_one_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                s_response = response.text
                return s_response
            return None

        except RequestException:
            return None
    def parse_Video(self):
        s_html = self.get_one_page()
        pattern = re.compile('<video class="video" src=(.*?)></video>'+'.*?<h2 class="videoinfo-title">(.*?)</h2>',re.S)

        items = re.findall(pattern,s_html)
        for item in items:
            n_path = os.getcwd()
            urllib.request.urlretrieve(item[0], '{0}/{1}.mp4'.format(n_path,item[1]))

if __name__ =="__main__":
    for url_n in f_l:
        f_url = 'https://haokan.baidu.com/v?vid={0}'.format(url_n)
        v = Gdgvedio(f_url)
        v.parse_Video()




        