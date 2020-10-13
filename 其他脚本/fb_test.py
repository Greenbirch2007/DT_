import datetime

import re


def re_cut_Str(item):
    if type(item) != str:
        str_item = str(item)

    else:
        str_item = item
    patt = re.compile("\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}", re.S)
    ite = re.findall(patt, str_item)
    return ite

# 这个函数：1.将两个字符串日期，先进行裁剪
# 2. 因为都只保留到分钟，所以可以用分钟的date格式，转化为datetime对象
# 3.直接将两个datetime对象，进行计算返回int
def copare_twoTime(s1_time,s2_time):
    f1_time = re_cut_Str(s1_time)
    f2_time = re_cut_Str(s2_time)
    time_cut = "%Y/%m/%d %H:%M"
    d1_time = datetime.datetime.strptime(f1_time,time_cut)
    d2_time = datetime.datetime.strptime(f2_time,time_cut)
    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec


# 用长度无法剔除秒数，考虑正则表达式



# str_l = ['2019/9/4 9:00:00', '2018/05/21 13:10:00', '2018/05/21 13:15:00','2018/11/23 9:03:00', '2018/05/21 13:10:00', '2018/05/21 13:15:00','2018/4/12 10:18:00', '2018/04/23 0:50:00', '2018/04/23 00:55:00']
# for item in str_l:
#     patt =re.compile("\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}",re.S)
#     ite = re.findall(patt,item)
#     print(ite,len(ite))




a1 = '2018/11/23 9:03:00'
a2 = '2018/05/21 13:10:00'
a = re_cut_Str(a2)
print(a)