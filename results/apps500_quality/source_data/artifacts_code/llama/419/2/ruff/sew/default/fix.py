s = int(input(), 2)
ans = 0
for i in range(1, 101):
    if not s >= 2**i:
        break
    else:
        ans += 1
print(ans)