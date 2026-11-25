p, y = map(int, input().split())

for x in range(p, 0, -1):
    can_reach = False
    for j in range(2, 1 + int(y / x)):
        if x * j <= y and x != x * j:
            can_reach = True
            break
    if not can_reach:
        print(x)
        break
else:
    print(-1)
