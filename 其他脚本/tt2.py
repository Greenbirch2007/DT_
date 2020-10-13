

import datetime
# str---->datetime+ 5 ----->str

#用两个时间匹配格式！



# 选择两种模式中的一种，如果报错就是选择另外一种！
#用时间字段的长度来判断
# 这样不同的数据格式都进行比较了！
def twoTStyle(sttime):
    str_len = len(sttime)
    time_cut1 = "%Y/%m/%d %H:%M:%S"
    time_cut2 = "%Y/%m/%d %H:%M"
    if str_len == 19:
        s1_time = datetime.datetime.strptime(sttime, time_cut1)
        return s1_time
    else:
        s2_time = datetime.datetime.strptime(sttime, time_cut2)
        return s2_time

def copare_twoTime(s1_time,s2_time):
    d1_time = twoTStyle(s1_time)
    d2_time = twoTStyle(s2_time)

    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec




s1 = '2019/11/10 20:06'
s2 = '2019/11/10 20:11'
s3 = '2019/11/10 20:08:00'

#ValueError


f = copare_twoTime(s2,s3)
print(f>0)
