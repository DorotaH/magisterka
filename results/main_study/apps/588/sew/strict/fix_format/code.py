import numpy as np

n, xy = int(input()), []
for i in range(0, n):
    xy.append(list(map(int, input().split())))


def naiseki(a, b):
    if not (a[0] * b[0] + a[1] * b[1]) > 0.0:
        return False
    else:
        return True


ans = 0

for i in range(0, 1001):
    xl = np.cos(np.pi * 2.0 * i / 1000.0)
    yl = np.sin(np.pi * 2.0 * i / 1000.0)
    x = y = 0
    for j in range(0, n):
        if naiseki([xl, yl], xy[j]):
            x += xy[j][0]
            y += xy[j][1]
    ans = max(ans, np.sqrt(x**2 + y**2))
print(ans)
