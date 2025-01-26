import math


a = int(input("length of the side: "))
n = int(input("number of sides: "))

apofema = a / (2 * math.tan(math.pi / n))

Area = int(0.5 * apofema * a * n)

print(Area)
