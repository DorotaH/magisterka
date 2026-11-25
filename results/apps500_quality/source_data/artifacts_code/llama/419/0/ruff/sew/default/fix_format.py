s = int(input(), 2)

ans = k = 0
while s > 0:
    if s & 1:
        ans = ans + 1
    s >>= 1
    k += 1

print(k - 1)
