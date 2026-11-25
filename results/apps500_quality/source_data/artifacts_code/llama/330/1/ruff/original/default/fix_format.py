p, y = map(int, input().split())

for x in range(p, 0, -1):
    can_reach = False
    for j in range(2, int(y / x) + 1):
        if x * j <= y and x != j * x:
            can_reach = True
            break
    if not can_reach:
        print(x)
        break
else:
    print(-1)
