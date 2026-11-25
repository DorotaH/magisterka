import math

m, n = map(int, input().split())
lcm = [1] * (1 + m)
for i in range(1, 1 + m):
    s, *stores = map(int, input().split())
    a = list(stores)
    if s == n:
        print("impossible")
        exit()
    for j in range(s):
        lcm[i] = lcm[i] * a[j] // math.gcd(lcm[i], a[j])
    for j in range(i):
        lcm[i] = lcm[i] * lcm[j] // math.gcd(lcm[i], lcm[j])
    for j in range(i + 1, 1 + m):
        lcm[j] = lcm[i] * lcm[j] // math.gcd(lcm[j], lcm[i])
for i in range(1, 1 + m):
    if lcm[i] < lcm[i - 1]:
        print("impossible")
        exit()
print("possible")
