

#


import operator

result_data = [{"id":2,"dt":"2019/7/1 15:41:00"},{"id":1,"dt":"2019/9/1 11:41:00"},{"id":3,"dt":"2012/8/1 16:36:00"}]

print("before",result_data)
# 列表中包裹字典中的日期元素进行排序，reverse=False 日期从低到高
# result_data.sort(key=operator.itemgetter("dt"),reverse=False)


# 列表中包裹字典中的日期元素进行排序，reverse=True 日期从高到低
result_data.sort(key=operator.itemgetter("dt"),reverse=True)


print("after",result_data)

