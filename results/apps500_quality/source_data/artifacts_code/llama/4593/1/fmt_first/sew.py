import math

n = int(input())
i = 2
while True:
    sqrt_n=math.isqrt(n)
    for b in range(1, 1 + sqrt_n):
        p = 2
        while  pow(b, p)<=n:
            if pow(b, p)<=n:
                i=pow(b, p)
            p = p + 1
        if pow(b, p)>n:
            break
    if  n >= i:
        break
    n=i-1
print(i)
