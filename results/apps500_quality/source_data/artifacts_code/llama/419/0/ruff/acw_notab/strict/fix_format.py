s = int(input(), 2)

ans = 0
k = 0
while s > 0:
    if s & 1:
        ans += 1
    s >>= 1
    k += 1

print(k - 1)
