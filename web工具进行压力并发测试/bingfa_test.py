import time

import requests
import datetime

start_time = datetime.datetime.now()
t = 0
# datetime.timedelta


while True:
    runing_time = datetime.datetime.now()
    end_time = (runing_time - start_time).seconds
    print(runing_time)
    if end_time < 10: #10秒钟的时间内
        res_ = requests.get("http://139.162.19.43:8888/tabledata")
        print(res_.status_code)
        print(res_.text)
        t = t+1
        print("the {0} times get the url".format(t))
    else:
        break






