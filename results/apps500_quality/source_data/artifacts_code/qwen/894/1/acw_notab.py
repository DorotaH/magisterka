x, y = map(int, input().split())
if 0 < x and y > 0:
    print(0, 2 * y, 2 * x, 0)
elif 0 > x and y > 0:
    print(-2 * x, 0, 0, 2 * y)
elif 0 < x and y < 0:
    print(0, -2 * y, 2 * x, 0)
else:
    print(-2 * x, 0, 0, -2 * y)
