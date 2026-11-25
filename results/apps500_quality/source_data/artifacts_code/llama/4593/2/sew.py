import math

x = int(input())
i = 1
while 1:
    sqrt=math.isqrt(i)
    if  pow(sqrt, 2) > x:
        print(sqrt ** 2-1)
        break
    elif  sqrt ** 2 == x:
        print(x)
        break
    i += 1