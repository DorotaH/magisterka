import math

n = int(input())

if n == 1 or 2 == n:
    print(1)
elif 3 == n:
    print(2)
elif 4 == n:
    print(3)
else:
    print(math.floor((1 + n) / 2))
