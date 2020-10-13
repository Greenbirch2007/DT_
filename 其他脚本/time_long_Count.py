#
#
# a1 = '2018/4/27 16:28:00'
# a2 = '2018/12/27 16:28:00'
# a3 = '2018/2/7 16:28:00'
# a4 = '2018/12/7 16:28:00'
# # print(len(a1),len(a2),len(a3),len(a4))
# # print("~"*99)
# a5 = '2018/4/27 16:28'
# a6 = '2018/12/27 16:28'
# a7 = '2018/2/7 16:28'
# a8 = '2018/12/7 16:28'
# # print(len(a5),len(a6),len(a7),len(a8))
#
#
#
# # 18 19 17 18
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 15 16 14 15
#
# # 写一个清洗日期的函数，不要修改脏数据，工作量太大！保证能比较就可以了
# def time_long_Count(ite_time):
#     if len(ite_time) == 18:
#         f_time = ite_time[:15]
#     elif len(ite_time) ==19:
#         f_time = ite_time[:16]
#     elif len(ite_time) == 17:
#         f_time = ite_time[:14]
#     else:
#         f_time = ite_time
#     return f_time
#
#
# print("a1",a1)
# print(time_long_Count(a1))
# print("~"*99)
# print("a2",a2)
# print(time_long_Count(a2))
# print("~"*99)
# print("a3",a3)
# print(time_long_Count(a3))
# print("~"*99)
# print("a4",a4)
# print(time_long_Count(a4))
# print("~"*99)
# print("a5",a5)
# print(time_long_Count(a5))
# print("~"*99)
# print("a6",a6)
# print(time_long_Count(a6))
# print("~"*99)
# print("a7",a7)
# print(time_long_Count(a7))
# print("~"*99)
# print("a8",a8)
# print(time_long_Count(a8))
# print("~"*99)

import datetime


def twoTStyle(sttime):
    if len(sttime) == 18:
        f_time = sttime[:15]
    elif len(sttime) ==19:
        f_time = sttime[:16]
    elif len(sttime) == 17:
        f_time = sttime[:14]
    else:
        f_time = sttime
    time_cut = "%Y/%m/%d %H:%M"
    s_time = datetime.datetime.strptime(f_time,time_cut)
    return s_time


# 这个函数作用在于将已经裁剪到分钟，并且转换为datetime两个对象，进行差计算，并且返回整型
def copare_twoTime(s1_time,s2_time):
    d1_time = twoTStyle(s1_time)
    d2_time = twoTStyle(s2_time)

    cut_d_time = d1_time - d2_time
    int_sec  = cut_d_time.days * 86400  + cut_d_time.seconds
    return int_sec


a1 = '2018/1/19 20:43:09'
a2 = '2018/1/19 20:45:19'
a3 = '2018/01/28 09:05'
t = copare_twoTime(a3,a2)
print(t)