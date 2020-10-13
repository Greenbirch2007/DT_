import  pandas  as pd
#方法一：默认读取第一个表单
df=pd.read_excel('/home/w/Desktop/data_work/t1.xlsx')#这个会直接默认读取到这个Excel的第一个表单



print(df[1])