

import datetime
# str---->datetime+ 5 ----->str

#
def copare_twoTime(s1_time,s2_time):
    time_cut = "%Y/%m/%d %H:%M"
    d1_time = datetime.datetime.strptime(s1_time, time_cut)
    d2_time = datetime.datetime.strptime(s2_time, time_cut)
    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec


s1 = '2019/11/10 20:06'
s2 = '2019/11/10 20:11'
s3 = '2019/11/10 20:08'


f = copare_twoTime(s3,s2)
print(f)
