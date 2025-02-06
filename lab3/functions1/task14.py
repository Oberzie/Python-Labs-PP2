import random
x = random.randint(1, 100)
y = random.randint(1, 100)
z = random.randint(1, 100)
lis = [x, y, z]
for i in lis:
    print('*' * i)
lis.reverse()
for i in lis:
    print('*' * i)       
