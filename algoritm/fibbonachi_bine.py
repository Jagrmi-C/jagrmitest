import math

n = 6

x = ((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n
y = math.sqrt(5)
a = x / y
print(int(a))
