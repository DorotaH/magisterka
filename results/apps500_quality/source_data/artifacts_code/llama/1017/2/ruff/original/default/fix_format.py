import math

n = int(input())

if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
elif n == 4:
    print(3)
else:
    print(math.floor((n + 1) / 2))
