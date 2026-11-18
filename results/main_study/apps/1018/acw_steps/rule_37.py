import sys

def Min(x, y):
    return min(x, y)

def Gcd(x, y):
    return y if x == 0 else Gcd(y % x, x)

def Lcm(x, y):
    return y * x // Gcd(x, y)

n = int(input())
a = [int(i) for i in input().split()]
d = [0 for _ in range(0, n)]

ok = 0

cur = 0

len = Lcm(7, n)

for i in range(0, 7 * n):
    if a[i % n] == 0 :
        print(i % n + 1)
        ok = 1
        break
    if cur != 6:
        a[i % n] -= 1
        d[i % n] += 1
    cur = (cur + 1) % 7

if ok == 0:
    k = 10**20

    for i in range(0, n):
        a[i] += d[i]
        if d[i] == 0: continue
        k = Min(k, a[i] // d[i]) if a[i] % d[i] > 0 else Min(k, a[i] // d[i] - 1)
    if k == 10**20:
        k = 0

    for i in range(0, n):
        a[i] -= k * d[i]

    iter = 0
    cur = 0

    while True:
        if a[iter] == 0:
            print(1 + iter % n)
            break
        else:
            if cur != 6:
                a[iter] -= 1
            cur = (cur + 1) % 7
            iter = (iter + 1) % n

