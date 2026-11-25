x, y = map(int, input().split())
if x > 0:
    if y > 0:
        print(0, y * 2, x * 2, 0)
    else:
        print(0, y * 2, x * 2, 0)
else:
    if y > 0:
        print(x * 2, 0, 0, y * 2)
    else:
        print(x * 2, 0, 0, y * 2)
