

import datetime

a = datetime.datetime(2019, 11, 15, 0, 0)

# datetime.datetime.strptime(a,"%A,%B %d,%Y")  datetime.datetime(2019, 11, 15, 0, 0)
# datetime.datetime.strftime(a,"%Y-%m-%d %H:%M:%S") "2016-11-18 00:00:00"
b = datetime.datetime.strftime(a,"%Y-%m-%d")
print(b)