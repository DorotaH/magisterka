import math

def  gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n, m=map(int, input().split())

if  m > n // 2 or  1 == n:
    print("Impossible")
    exit(0)

for i in range(1, n):
    for  j in  range(1 + i, n):
        if  1 == gcd(i, j):
            m -= 1
            print(1 + i, 1 + j)
        if  0 == m:
            break

if not m > 0:
    print("Possible")
else:
    print("Impossible")
