

l = [None,None,"a",'asdf']


def count_None(l_content):
    # 第一种方法计数：
    # i = 0
    # for item in l_content:
    #
    #     if item == None:
    #         i = i + 1
    #     else:pass

    # return i
    # 第2种方法：计算None_l 的长度
    None_L =[]
    for item in l_content:
        if item == None:
            None_L.append(item)
    return len(None_L)
print(count_None(l))