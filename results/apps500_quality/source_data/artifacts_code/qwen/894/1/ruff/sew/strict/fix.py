x, y = map(int, input().split())
if  x>0 and  y>0:
    print(0, y * 2, x * 2, 0)
elif  x < 0 and y > 0:
    print(-2 * x, 0, 0, 2 * y)
elif  x > 0 and y < 0:
    print(0, -2 * y, 2 * x, 0)
else:
    print(-2 * x, 0, 0, -2 * y)
