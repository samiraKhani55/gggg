import random
list1 = [0, 0 , 0 , 0 , 0, 0, 0]
for i in range(10):
    list1[random.randrange(1,7)] +=1
print  ("number","         freuency")
for i in range(1,7):
    print(f'{i:3} {list1[i]:17}')