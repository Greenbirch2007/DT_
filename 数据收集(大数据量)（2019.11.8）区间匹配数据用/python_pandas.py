import  pandas  as pd
#方法一：默认读取第一个表单
#这个会直接默认读取到这个Excel的第一个表单


    # for num in range(long_num+1):



def get_pandas1():
    df = pd.read_excel('/home/w/Desktop/data_work/t1.xlsx')
    l1 = []
    f = df.values.T.tolist()
    for i1, i2, i3 in zip(f[0], f[1], f[2]):
        l1.append((i1, i2, i3))


    return l1


#
c = get_pandas1()
print(len(c))