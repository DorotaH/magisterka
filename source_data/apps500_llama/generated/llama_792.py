import math

m, n = map(int, input().split())
lcm = [1] * (m + 1)
for i in range(1, m + 1):
    s, *stores = map(int, input().split())
    a = []
    for store in stores:
        a.append(store)
    if s == n:
        print("impossible")
        exit()
    for j in range(s):
        lcm[i] = lcm[i] * a[j] // math.gcd(lcm[i], a[j])
    for j in range(i):
        lcm[i] = lcm[i] * lcm[j] // math.gcd(lcm[i], lcm[j])
    for j in range(i + 1, m + 1):
        lcm[j] = lcm[j] * lcm[i] // math.gcd(lcm[j], lcm[i])
for i in range(1, m + 1):
    if lcm[i] < lcm[i - 1]:
        print("impossible")
        exit()
print("possible")
