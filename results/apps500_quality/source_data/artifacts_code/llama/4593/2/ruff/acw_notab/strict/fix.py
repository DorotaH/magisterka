import math

x = int(input())
i = 1
while True:
    sqrt = math.isqrt(i)
    if sqrt ** 2 > x:
        print(sqrt ** 2 - 1)
        break
    elif sqrt ** 2 == x:
        print(x)
        break
    i += 1
