
p, y = map(int, input().split())

for x in range(p, 0, -1):
    can_reach = any(x * j <= y and x != x * j for j in range(2, int(y / x) + 1))
    if not can_reach:
        print(x)
        break
else:
    print(-1)
