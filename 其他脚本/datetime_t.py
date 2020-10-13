#
#
# import datetime
# # str---->datetime---->计算差值并除以15----->str
#
# def datetime_Cut_Dot15(item1,item2):
#     try:
#         time_cut = "%Y-%m-%d %H:%M:%S"
#
#         d1_time = datetime.datetime.strptime(item1, time_cut)
#         d2_time = datetime.datetime.strptime(item2, time_cut)
#         cut_d_time = (d2_time - d1_time)
#         int_min  = int(cut_d_time.days * 86400  + cut_d_time.seconds)/60 #　以分钟计算
#         dt_dot_15 = int_min/15  #每15分钟算一个点
#         return dt_dot_15
#     except ValueError as e:
#         pass
#
#
#
# a1 = '2018-07-19 6:55:00'
# a2 = '2018-07-19 8:34:00'
# t = datetime_Cut_Dot15(a1,a2)
# print(t)


a = ['','t','']