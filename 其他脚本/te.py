import random

al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n"]


for item in range(1,10):

    content_8 = [(item, random.choice(al), random.choice(al), random.choice(al), random.choice(al),
                  random.choice(al), random.choice(al), random.choice(al), random.choice(al))]
    print(content_8)


