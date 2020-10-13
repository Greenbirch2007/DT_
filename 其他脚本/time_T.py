


import datetime

time_cut ="%Y-%m-%d %H:%M:%S"


n_now = datetime.datetime.now().strftime(time_cut)
print(n_now)

# s_5m = (n_now+datetime.timedelta(minutes=5))
print(type(n_now))

print("~"*88)
s_now = datetime.datetime.strptime(n_now,time_cut)

print(s_now)
print(type(s_now))