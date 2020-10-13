


s = [1, 2, 3, 4, 1, 1]
s1 = s
for i in s1:
    if i == 1:
        s1.remove(i)
print(s1)


s2 = s
for idx in range(len(s2)):
    if s2[idx] == 1:
        del s2[idx]
print(s2)


import copy

s5 = copy.deepcopy(s)
for i in s:
    if i == 1:
        s5.remove(i)
print(s5)