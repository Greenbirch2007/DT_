
import math

def sqre(item):
    s_item = item * item
    return s_item

# [1, 4]
# [1, 4, 9, 16, 25, 36, 49, 64]

# 同样的iOA金
b= []
for i1 in range(1,99999999):
    for i2 in range(1,99999999999999):
        item2 = sqre(i2)
        if i1 == item2:
            b.append(i1)
print(b)
iter