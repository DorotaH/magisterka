s = int(input(), 2)
ans = 0
for i in range(1, 101):
    if s >= 2**i:
        ans += 1
    else:
        break
print(ans)
